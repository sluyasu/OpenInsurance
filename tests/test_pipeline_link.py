"""Supersession is a published claim: a banner saying "replaced by" on a document that
is still sold is a factual error (rule 8). These pin the two ways that went wrong:
variants read as old editions, and edition dates the pipeline parser could not read
while the MCP parser could."""

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "pipeline"))  # pipeline modules import each other flat

import link  # noqa: E402


def _doc(url, **kw):
    base = {
        "source_url": url,
        "insurer_slug": "cardif",
        "branch": "autres",
        "product_family": "hypo-protect",
        "product_name": "Hypo Protect",
        "document_type": "conditions_generales",
        "edition_date": "2025-01-01",
        "variant": None,
    }
    base.update(kw)
    return base


# --- variants run in parallel, they do not supersede each other ----------------

def test_variant_is_not_superseded_by_another_variant():
    """Cardif Hypo Protect Luxembourg is sold alongside the Belgian edition. Comparing
    them by date alone stamped the older one "replaced by" the newer."""
    be = _doc("https://x/be.pdf", variant="Belgique", edition_date="2024-01-01")
    lu = _doc("https://x/lu.pdf", variant="Luxembourg", edition_date="2025-01-01")
    rel = link.compute_relations([be, lu])
    assert rel["https://x/be.pdf"]["superseded_by"] is None
    assert rel["https://x/lu.pdf"]["superseded_by"] is None


def test_editions_of_the_same_variant_still_supersede():
    """The variant partition must not disable supersession within a variant."""
    old = _doc("https://x/2024.pdf", variant="Luxembourg", edition_date="2024-01-01")
    new = _doc("https://x/2025.pdf", variant="Luxembourg", edition_date="2025-01-01")
    rel = link.compute_relations([old, new])
    assert rel["https://x/2024.pdf"]["superseded_by"] is not None
    assert rel["https://x/2025.pdf"]["superseded_by"] is None
    assert rel["https://x/2025.pdf"]["edition_status"] == "current"


def test_undated_documents_are_never_superseded():
    """An unparseable date must not be treated as "oldest" and stamped superseded."""
    dated = _doc("https://x/dated.pdf", edition_date="2025-01-01")
    undated = _doc("https://x/undated.pdf", edition_date=None)
    rel = link.compute_relations([dated, undated])
    assert rel["https://x/undated.pdf"]["superseded_by"] is None


# --- the pipeline parser must read every format the MCP parser reads -----------

@pytest.mark.parametrize("raw,expected", [
    ("2026-05-12", (2026, 5, 12)),
    ("12/05/2026", (2026, 5, 12)),
    ("04.2025", (2025, 4, 0)),
    ("01042026", (2026, 4, 1)),        # DDMMYYYY
    ("20230201", (2023, 2, 1)),        # YYYYMMDD, previously read as year 201 month 23
    ("202508", (2025, 8, 0)),          # YYYYMM
    ("092024", (2024, 9, 0)),          # MMYYYY
    ("0523", (2023, 5, 0)),            # MMYY, the amma editions
    ("112020-F012025", (2020, 11, 0)),  # date embedded in a form reference
    ("2019", (2019, 0, 0)),
    ("", (0, 0, 0)),
    (None, (0, 0, 0)),
])
def test_edition_key(raw, expected):
    assert link._edition_key(raw) == expected


def test_edition_key_matches_the_mcp_parser(mcp):
    """The two parsers are duplicated on purpose: the MCP server ships standalone on
    PyPI and never imports pipeline/. Duplication is only safe while they agree, so
    disagreement is a test failure rather than a silent divergence in what the wiki
    publishes versus what the server answers."""
    cases = ["2026-05-12", "12/05/2026", "12.05.2026", "04.2025", "2025-08", "03/25",
             "01042026", "20260401", "20230201", "202508", "092024", "0523",
             "112020-F012025", "2019", "septembre 2024", "31/13/2025", "abc", "", None]
    for raw in cases:
        assert link._edition_key(raw) == mcp._edition_key(raw), f"diverged on {raw!r}"


def test_amma_editions_are_now_comparable():
    """MMYY dates parsed as (0,0,0) dropped these documents out of supersession
    entirely, so an outdated edition never got a banner."""
    old = _doc("https://x/0523.pdf", insurer_slug="amma", edition_date="0523")
    new = _doc("https://x/0524.pdf", insurer_slug="amma", edition_date="0524")
    rel = link.compute_relations([old, new])
    assert rel["https://x/0523.pdf"]["superseded_by"] is not None
    assert rel["https://x/0524.pdf"]["edition_status"] == "current"
