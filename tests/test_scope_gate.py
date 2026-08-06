"""The scope gate: a document that is not a product document must not become a page.

France made the gate necessary: the mutuelles' download pages mix company statutes,
fund performance sheets, promotional-discount riders and service conventions with the
real product documents, and 70 of them shipped as product pages before the gate
existed. Three layers are pinned here: the `out_of_scope:` source marker (shared
reader + download skip), the validate errors that make a slip-through CI-blocking,
and the render/serve refusals in build_wiki and the MCP server. The extraction
agent's side of the contract is pinned by asserting the prompts still carry it.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline"))

import common  # noqa: E402
import build_wiki  # noqa: E402
import download  # noqa: E402
import validate  # noqa: E402
from test_robustness import run_in  # noqa: E402

CC = "xx"

COUNTRY_YML = """\
name: Testland
branches:
  auto:
    label: Auto
fallback_branch: auto
"""

INSURER_YML = """\
insurer:
  slug: ins
  name: "Test Insurer"
  website: "https://example.org"
pdfs:
- url: https://example.org/cg-auto.pdf
  branch: auto
  document_type: conditions_generales
- url: https://example.org/statuts.pdf
  out_of_scope: "statuts de l'entreprise, pas un document produit"
"""


def product(url: str, **over) -> dict:
    base = {
        "schema_version": "1.0",
        "country": CC,
        "insurer_slug": "ins",
        "product_name": "Assurance Auto Test",
        "branch": "auto",
        "document_type": "conditions_generales",
        "language": "fr",
        "source_url": url,
    }
    base.update(over)
    return base


@pytest.fixture()
def repo(tmp_path, monkeypatch):
    """A throwaway country: one in-scope row, one marked row, one committed extraction
    for each (the marked one modelling the historical slip-through). The real schema is
    copied in, and the consumers' REPO is re-rooted so their relative_to() calls hold."""
    (tmp_path / "sources" / CC).mkdir(parents=True)
    (tmp_path / "sources" / CC / "_country.yml").write_text(COUNTRY_YML, encoding="utf-8")
    (tmp_path / "sources" / CC / "ins.yml").write_text(INSURER_YML, encoding="utf-8")
    ext = tmp_path / "data" / CC / "extracted" / "ins"
    ext.mkdir(parents=True)
    (ext / "ok.json").write_text(
        json.dumps(product("https://example.org/cg-auto.pdf")), encoding="utf-8")
    shutil.copytree(REPO / "schema", tmp_path / "schema")
    monkeypatch.setattr(common, "SOURCES", tmp_path / "sources")
    monkeypatch.setattr(common, "DATA", tmp_path / "data")
    monkeypatch.setattr(validate, "REPO", tmp_path)
    monkeypatch.setattr(build_wiki, "REPO", tmp_path)
    return tmp_path


def test_marked_rows_are_read_by_the_shared_helper(repo):
    marked = common.out_of_scope_urls(CC)
    assert marked == {"https://example.org/statuts.pdf":
                      "statuts de l'entreprise, pas un document produit"}


def test_download_never_fetches_a_marked_row(repo):
    from download import gather_entries
    urls = {e["url"] for e in gather_entries(CC, None)}
    assert "https://example.org/cg-auto.pdf" in urls
    assert "https://example.org/statuts.pdf" not in urls


def test_validate_blocks_an_extraction_of_a_marked_url(repo):
    from validate import data_layer_errors
    ext = repo / "data" / CC / "extracted" / "ins"
    (ext / "statuts.json").write_text(
        json.dumps(product("https://example.org/statuts.pdf",
                           product_name="Statuts de Test Insurer")), encoding="utf-8")
    errs = data_layer_errors(CC)
    assert any("marked out_of_scope" in e and "statuts.json" in e for e in errs)
    # the in-scope extraction stays clean: the gate must not flag real products
    assert not any("ok.json" in e for e in errs)


def test_validate_blocks_an_extraction_carrying_its_own_verdict(repo):
    from validate import data_layer_errors
    ext = repo / "data" / CC / "extracted" / "ins"
    (ext / "verdict.json").write_text(
        json.dumps({"out_of_scope_reason": "nomenclature d'activites"}), encoding="utf-8")
    errs = data_layer_errors(CC)
    assert any("out of scope per its own extraction" in e and "verdict.json" in e
               for e in errs)


def test_validate_flags_a_stale_manifest_entry_for_a_marked_url(repo):
    from validate import data_layer_errors
    common.save_manifest(CC, {"https://example.org/statuts.pdf": {"status": "downloaded"}})
    errs = data_layer_errors(CC)
    assert any("manifest" in e and "statuts.pdf" in e for e in errs)


def test_build_renders_no_page_for_a_verdict_file(repo, capsys):
    from build_wiki import load_products
    ext = repo / "data" / CC / "extracted" / "ins"
    (ext / "verdict.json").write_text(
        json.dumps({"out_of_scope_reason": "bareme de frais transverse"}), encoding="utf-8")
    prods = load_products(CC)
    assert [p["product_name"] for p in prods] == ["Assurance Auto Test"]
    assert "OUT OF SCOPE" in capsys.readouterr().out


def test_mcp_serves_no_verdict_file(tmp_path):
    """Same refusal on the serving side (duplicated there on purpose: the server ships
    standalone from PyPI and cannot import pipeline/)."""
    ext = tmp_path / "data" / CC / "extracted" / "ins"
    ext.mkdir(parents=True)
    (tmp_path / "data" / CC / "index.json").write_text("[]", encoding="utf-8")
    (ext / "ok.json").write_text(
        json.dumps(product("https://example.org/cg-auto.pdf")), encoding="utf-8")
    (ext / "verdict.json").write_text(
        json.dumps({"out_of_scope_reason": "convention de service"}), encoding="utf-8")
    r = run_in(tmp_path, "import insurance_wiki_mcp as m; "
                         f"print(len(m._extracted('{CC}')))")
    assert r.stdout.strip().endswith("1")
    assert "out-of-scope" in r.stderr


def test_prompts_carry_the_scope_gate():
    """extract.py's verdict handling reads `out_of_scope_reason`; the prompts are where
    the model is told to emit it. Dropping the gate from either file would silently
    disarm the extraction layer."""
    agent = REPO / "extraction-agent"
    spec = (agent / "OUTPUT_SPEC.md").read_text(encoding="utf-8")
    system = (agent / "SYSTEM_PROMPT.md").read_text(encoding="utf-8")
    assert "out_of_scope_reason" in spec
    assert "scope gate" in system.lower()
