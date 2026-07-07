"""get_page must only read the knowledge folders. A prompt-injected client may ask
for anything; dotfiles, code and git internals must stay out of reach."""

import pytest

REFUSED = [
    ".env",
    ".env.example",
    ".gitignore",
    ".git/config",
    "../../etc/passwd",
    "/etc/passwd",
    "pipeline/extract.py",
    "mcp/insurance_wiki_mcp.py",
    ".github/workflows/validate.yml",
    "wiki/../.env",
    "Makefile",
    "pyproject.toml",
]

ALLOWED = [
    "README.md",
    "wiki/be/branches/Auto.md",
    "data/be/index.json",
    "sources/be/_country.yml",
    "schema/coverage_categories.json",
    "_meta/universal-glossary/Deductible.md",
]


@pytest.mark.parametrize("path", REFUSED)
def test_refused(mcp, path):
    out = mcp.get_page(path)
    assert out.startswith("Not found or outside repo"), f"{path} was readable"


@pytest.mark.parametrize("path", ALLOWED)
def test_allowed(mcp, path):
    out = mcp.get_page(path)
    assert not out.startswith("Not found or outside repo"), f"{path} was refused"
    assert len(out) > 0
