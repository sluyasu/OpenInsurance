"""Product/page name matching must be accent- and case-insensitive: French product
names are full of accents and clients type without them."""


def test_norm_folds_accents_and_case(mcp):
    assert mcp._norm("Véhicules Automoteurs") == mcp._norm("vehicules automoteurs")
    assert mcp._norm("Santé") == "sante"


def test_norm_collapses_whitespace(mcp):
    assert mcp._norm("a  b\n c") == "a b c"


def test_get_product_matches_without_accents(mcp):
    out = mcp.get_product("be", "ag", "assurance de responsabilite top familiale")
    assert "No product matching" not in out
    assert "CITATION" in out


def test_search_matches_without_accents(mcp, request):
    from conftest import parse_payload
    rows = parse_payload(mcp.search("velo", "be", type="product"))
    assert rows, "accent-insensitive search returned nothing for 'velo'"
