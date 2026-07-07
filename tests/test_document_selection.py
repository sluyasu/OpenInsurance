"""One commercial product maps to several documents (CG + IPID, several editions).
Selection must be deterministic: general conditions over summaries, non-superseded,
newest edition, and the response must say which document was chosen."""

import pytest


# --- edition date parsing (formats as printed in real source PDFs) -----------

@pytest.mark.parametrize("raw,expected", [
    ("2026-05-12", (2026, 5, 12)),
    ("12/05/2026", (2026, 5, 12)),
    ("12.05.2026", (2026, 5, 12)),
    ("04.2025", (2025, 4, 0)),
    ("2025-08", (2025, 8, 0)),
    ("03/25", (2025, 3, 0)),
    ("01042026", (2026, 4, 1)),        # DDMMYYYY
    ("20260401", (2026, 4, 1)),        # YYYYMMDD
    ("202508", (2025, 8, 0)),          # YYYYMM (DKV editions)
    ("092024", (2024, 9, 0)),          # MMYYYY
    ("0523", (2023, 5, 0)),            # MMYY
    ("112020-F012025", (2020, 11, 0)), # date embedded in a form reference
    ("2019", (2019, 0, 0)),
    ("septembre 2024", (2024, 0, 0)),  # bare year inside prose
    ("", (0, 0, 0)),
    (None, (0, 0, 0)),
])
def test_edition_key(mcp, raw, expected):
    assert mcp._edition_key(raw) == expected


def test_edition_key_orders_editions(mcp):
    older, newer = mcp._edition_key("01/2025"), mcp._edition_key("10/2025")
    assert newer > older


# --- document ranking ---------------------------------------------------------

def _doc(**kw):
    base = {"document_type": "conditions_generales", "edition_date": "2025-01-01",
            "superseded": None, "product_name": "X", "reference": "r"}
    base.update(kw)
    return base


def test_cg_beats_ipid(mcp):
    chosen, others = mcp._pick_best([_doc(document_type="ipid", edition_date="2026-01-01"),
                                     _doc(document_type="conditions_generales",
                                          edition_date="2024-01-01")])
    assert chosen["document_type"] == "conditions_generales"
    assert len(others) == 1


def test_newest_edition_wins(mcp):
    chosen, _ = mcp._pick_best([_doc(edition_date="01/2024", reference="old"),
                                _doc(edition_date="01/2025", reference="new")])
    assert chosen["reference"] == "new"


def test_non_superseded_wins(mcp):
    chosen, _ = mcp._pick_best([_doc(superseded=True, edition_date="01/2026", reference="s"),
                                _doc(superseded=None, edition_date="01/2024", reference="n")])
    assert chosen["reference"] == "n"


# --- against the real dataset --------------------------------------------------

def test_get_product_selects_cg_and_says_so(mcp):
    out = mcp.get_product("be", "ag", "Top Familiale")
    assert "CITATION" in out
    assert "document_type=conditions_generales" in out
    assert "source_url=" in out


def test_get_product_document_type_filter(mcp):
    # P&V Assurance Familiale exists as both CG and IPID under the same name:
    # unfiltered resolution must prefer the CG, the filter must reach the IPID.
    out = mcp.get_product("be", "pv", "P&V Assurance Familiale")
    assert "document_type=conditions_generales" in out
    out = mcp.get_product("be", "pv", "P&V Assurance Familiale", document_type="ipid")
    assert "document_type=ipid" in out
