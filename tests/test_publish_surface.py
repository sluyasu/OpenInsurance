"""What a reader actually lands on.

These run against the committed wiki, so they fail if a future build reintroduces the
bug they describe. The failure mode they guard is silent: a link that resolves to the
wrong page looks exactly like a working link, which is why it survived 269 products.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline"))

import render  # noqa: E402

WIKI = REPO / "wiki" / "be"
MDLINK = re.compile(r"\[[^\]]*\]\(([^)]+\.md)\)")


def _frontmatter(p: Path) -> dict:
    txt = p.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return {}
    return yaml.safe_load(txt.split("---", 2)[1]) or {}


def _branch_labels() -> set[str]:
    meta = yaml.safe_load((REPO / "sources" / "be" / "_country.yml").read_text(encoding="utf-8"))
    return {b.get("label", s) for s, b in (meta.get("branches") or {}).items()}


def _generated_pages() -> list[Path]:
    return [p for p in WIKI.rglob("*.md") if _frontmatter(p).get("generated") is True]


def _links(p: Path):
    for m in MDLINK.finditer(p.read_text(encoding="utf-8")):
        raw = m.group(1)
        if "://" not in raw:
            yield raw, (p.parent / unquote(raw)).resolve()


def test_every_generated_link_resolves():
    broken = [(p.relative_to(WIKI), raw)
              for p in _generated_pages() for raw, t in _links(p) if not t.is_file()]
    assert not broken, f"{len(broken)} broken link(s): {broken[:5]}"


def test_no_generated_page_links_to_another_insurers_product():
    """The original defect: an Argenta page listing Yuzzu's products, because both name
    a product 'Assurance Auto' and the link was resolved by name."""
    wrong = []
    for p in WIKI.glob("products/*/*.md"):
        for _raw, t in _links(p):
            if t.is_file() and t.parent.parent.name == "products" and t.parent.name != p.parent.name:
                wrong.append((p.relative_to(WIKI), t.relative_to(WIKI)))
    assert not wrong, f"cross-insurer product links: {wrong[:5]}"


def test_product_pages_link_to_their_own_insurer_page():
    wrong = []
    for p in WIKI.glob("products/*/*.md"):
        for _raw, t in _links(p):
            if t.is_file() and t.parent.name == "insurers":
                if _frontmatter(t).get("insurer_slug") != p.parent.name:
                    wrong.append((p.relative_to(WIKI), t.name))
    assert not wrong, f"product pages pointing at the wrong insurer page: {wrong[:5]}"


def test_generated_pages_emit_no_bare_wikilinks():
    """A [[name]] in a generated page is resolved by basename, which is ambiguous for
    269 products and will be more so once a second country lands."""
    offenders = [p.relative_to(WIKI) for p in _generated_pages()
                 if re.search(r"\[\[", p.read_text(encoding="utf-8").split("---", 2)[-1])]
    assert not offenders, f"generated pages with wikilinks: {offenders[:5]}"


def test_no_product_page_takes_a_branch_pages_name():
    """Both layers are addressable by name; a product called 'Auto' made a hand-authored
    [[Auto]] ambiguous with the Auto branch overview."""
    labels = _branch_labels()
    clashes = [p.relative_to(WIKI) for p in WIKI.glob("products/*/*.md") if p.stem in labels]
    assert not clashes, f"product pages named like a branch: {clashes}"


def test_no_product_page_claims_a_branch_name_as_alias():
    labels = _branch_labels()
    clashes = [(p.relative_to(WIKI), a) for p in WIKI.glob("products/*/*.md")
               for a in (_frontmatter(p).get("aliases") or []) if a in labels]
    assert not clashes, f"product aliases colliding with a branch: {clashes}"


def test_bare_filename_never_belongs_to_a_superseded_edition():
    """Readers land on the unsuffixed name. Argenta's withdrawn 2024 Assurance Auto held
    it while the current edition sat behind a '(2)' suffix."""
    bad = []
    for p in WIKI.glob("products/*/*.md"):
        if re.search(r" \(\d+\)$", p.stem):
            continue
        fm = _frontmatter(p)
        if fm.get("edition_status") != "superseded":
            continue
        family = fm.get("product_family")
        siblings = [q for q in p.parent.glob("*.md")
                    if _frontmatter(q).get("product_family") == family
                    and _frontmatter(q).get("edition_status") == "current"]
        if siblings:
            bad.append(p.relative_to(WIKI))
    assert not bad, f"superseded editions holding the bare filename: {bad}"


def test_write_json_is_atomic(tmp_path):
    """A kill mid-write must leave the previous file intact, not a truncated one: the
    manifest and the index are read by every later stage, so a half-file is not a lost
    file but a pipeline that keeps running on corrupt input."""
    sys.path.insert(0, str(REPO / "pipeline"))
    from common import write_json
    f = tmp_path / "a.json"
    write_json(f, {"v": 1})
    circular: dict = {}
    circular["self"] = circular
    with pytest.raises(ValueError):
        write_json(f, circular)
    assert json_loads(f) == {"v": 1}
    assert not [p for p in tmp_path.iterdir() if p.name.startswith(".")], "temp file left behind"


def json_loads(p: Path):
    import json
    return json.loads(p.read_text(encoding="utf-8"))


def test_every_extraction_matches_the_committed_schema():
    """The wiki gates only ever looked at rendered pages, so a schema-invalid extraction
    passed as long as it rendered. Six of them did."""
    sys.path.insert(0, str(REPO / "pipeline"))
    import validate as v
    assert v.data_layer_errors("be") == []


def test_free_text_audience_is_kept_and_never_guessed():
    """A wording naming several audiences must not be reduced to one of them."""
    sys.path.insert(0, str(REPO / "pipeline"))
    import extract
    assert extract._audience_enum("Personnes physiques et morales") is None
    assert extract._audience_enum("Professionnels des soins de santé") is None
    assert extract._audience_enum("Toute personne physique de moins de 70 ans") == "particuliers"
    assert extract._audience_enum("Personnes physiques de moins de 70 ans") == "particuliers"
    assert extract._audience_enum("indépendants") == "independants"
    obj = extract.normalize({"target_audience": "Personnes physiques et morales"})
    assert obj["target_audience"] is None
    assert obj["target_audience_note"] == "Personnes physiques et morales"


def test_old_editions_carry_an_age_notice():
    """A 2010 edition read exactly like a current one, so "what does ERGO sell?" answered
    with contracts written 15 years ago."""
    missing = []
    for p in WIKI.glob("products/*/*.md"):
        fm = _frontmatter(p)
        age = fm.get("edition_age_years")
        if isinstance(age, int) and age >= render.OLD_EDITION_YEARS \
                and fm.get("edition_status") != "superseded":
            if "Édition ancienne" not in p.read_text(encoding="utf-8"):
                missing.append(p.relative_to(WIKI))
    assert not missing, f"old editions with no age notice: {missing[:5]}"


def test_age_notice_states_age_without_claiming_the_product_is_withdrawn():
    """The documents do not say whether the product is still sold. The notice must report
    the age and say the question is open, not assert a run-off."""
    forbidden = ["produit fermé", "n'est plus commercialisé.", "run-off", "retiré de la vente"]
    for p in WIKI.glob("products/*/*.md"):
        txt = p.read_text(encoding="utf-8")
        if "Édition ancienne" not in txt:
            continue
        notice = next(l for l in txt.splitlines() if "Édition ancienne" in l)
        assert "à vérifier auprès de l'assureur" in notice
        for f in forbidden:
            assert f not in notice, f"{p.name}: notice asserts withdrawal ({f!r})"


def test_edition_age_is_measured_against_collection_not_today():
    """Measuring against today() would make every rebuild a diff."""
    obj = {"edition_date": "2010", "fetched_at": "2026-07-08"}
    assert render.edition_age_years(obj) == 16
    assert render.edition_age_years({"edition_date": "2010"}) is None
    # a document collected before its printed edition date is not negative-aged
    assert render.edition_age_years({"edition_date": "2026", "fetched_at": "2020-01-01"}) is None


@pytest.mark.parametrize("frm,to,expected", [
    ("products/axa/A.md", "insurers/AXA.md", "[l](../../insurers/AXA.md)"),
    ("products/axa/A.md", "products/axa/B.md", "[l](B.md)"),
    ("insurers/AXA.md", "products/axa/A.md", "[l](../products/axa/A.md)"),
])
def test_mdlink_paths(frm, to, expected):
    assert render.mdlink(frm, to, "l") == expected


def test_mdlink_encodes_characters_that_would_break_the_link():
    """An unencoded ')' ends the link early, so 'X (IPID).md' would truncate."""
    out = render.mdlink("insurers/A.md", "products/p/X (IPID).md", "X")
    assert "(IPID)" not in out.split("](")[1]
    assert "%28IPID%29" in out and "%20" in out
