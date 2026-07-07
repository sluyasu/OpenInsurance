"""Misconfiguration and bad-input behavior: an installed server without a dataset
must explain itself (not serve []), a corrupt index must name the file, caps must
be announced. These run the module in a subprocess against a throwaway repo
skeleton, since the repo root is resolved at import time."""

import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

from conftest import parse_payload  # noqa: E402


def run_in(repo_path: Path, code: str) -> subprocess.CompletedProcess:
    env = {**os.environ,
           "INSURANCE_WIKI_REPO": str(repo_path),
           "PYTHONPATH": str(REPO / "mcp")}
    return subprocess.run([sys.executable, "-c", code],
                          env=env, capture_output=True, text=True, timeout=60)


def test_missing_dataset_fails_fast(tmp_path):
    r = run_in(tmp_path, "import insurance_wiki_mcp as m; m.main()")
    assert r.returncode == 1
    assert "INSURANCE_WIKI_REPO" in r.stderr
    assert "github.com/sluyasu/OpenInsurance" in r.stderr


def test_missing_dataset_tools_explain(tmp_path):
    r = run_in(tmp_path, "import insurance_wiki_mcp as m; "
                         "print(m.list_countries()); print(m.search('auto')); "
                         "print(m.get_product('be', 'ag', 'x'))")
    assert r.returncode == 0
    assert r.stdout.count("No dataset found") == 3


def test_unknown_country_is_explained(mcp):
    out = mcp.get_product("xx", "ag", "auto")
    assert "No extracted data for country 'xx'" in out
    assert "be" in out


def test_corrupt_index_names_the_file(tmp_path):
    (tmp_path / "data" / "be").mkdir(parents=True)
    (tmp_path / "data" / "be" / "index.json").write_text("{not json", encoding="utf-8")
    r = run_in(tmp_path, "import insurance_wiki_mcp as m\n"
                         "try:\n"
                         "    m.search('auto', 'be')\n"
                         "except ValueError as e:\n"
                         "    print('RAISED:', e)\n")
    assert "RAISED:" in r.stdout
    assert "index.json" in r.stdout and "Corrupt index" in r.stdout


def test_corrupt_extracted_file_is_logged_not_fatal(tmp_path):
    (tmp_path / "data" / "be").mkdir(parents=True)
    (tmp_path / "data" / "be" / "index.json").write_text("[]", encoding="utf-8")
    bad = tmp_path / "data" / "be" / "extracted" / "ins"
    bad.mkdir(parents=True)
    (bad / "broken.json").write_text("{nope", encoding="utf-8")
    r = run_in(tmp_path, "import insurance_wiki_mcp as m; "
                         "print(len(m._extracted('be')))")
    assert r.stdout.strip().endswith("0")
    assert "skipping unreadable" in r.stderr and "broken.json" in r.stderr


def test_empty_country_yml_does_not_crash(tmp_path):
    (tmp_path / "data" / "be").mkdir(parents=True)
    (tmp_path / "data" / "be" / "index.json").write_text("[]", encoding="utf-8")
    (tmp_path / "sources" / "be").mkdir(parents=True)
    (tmp_path / "sources" / "be" / "_country.yml").write_text("", encoding="utf-8")
    r = run_in(tmp_path, "import insurance_wiki_mcp as m; print(m.list_branches('be'))")
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout) == []


def test_search_announces_truncation(mcp):
    out = mcp.search("", "be", limit=5)
    assert "showing the first 5" in out
    assert len(parse_payload(out)) == 5


def test_search_no_truncation_header_when_complete(mcp):
    out = mcp.search("mobility safe", "be", limit=20)
    assert "showing the first" not in out
