"""Smoke test of every tool against the committed dataset: parseable output,
disclaimer where facts are served, honest messages on gaps."""

import pytest

from conftest import (branch_without_overview, country_branches, index_rows,
                      parse_payload)


def test_list_countries(mcp):
    rows = parse_payload(mcp.list_countries())
    be = next(r for r in rows if r["country"] == "be")
    idx = index_rows("be")
    assert be["products"] == sum(1 for r in idx if r.get("type") == "product")
    assert be["insurers"] == sum(1 for r in idx if r.get("type") == "insurer")
    assert be["products"] > 0 and be["insurers"] > 0


def test_list_branches(mcp):
    rows = parse_payload(mcp.list_branches("be"))
    idx = index_rows("be")
    n_products = sum(1 for r in idx if r.get("type") == "product")
    with_products = {r["branch"] for r in idx
                     if r.get("type") == "product" and r.get("branch")}
    assert len(rows) == len(country_branches("be"))  # one row per taxonomy branch
    assert sum(1 for r in rows if r["products"]) == len(with_products)
    assert sum(r["products"] for r in rows) == n_products


def test_search_title_hit(mcp):
    rows = parse_payload(mcp.search("familiale", "be"))
    assert rows
    assert all({"title", "path", "type"} <= set(r) for r in rows)


def test_search_type_filter(mcp):
    rows = parse_payload(mcp.search("assurance", "be", type="product"))
    assert rows and all(r["type"] == "product" for r in rows)


def test_search_full_text_fallback(mcp):
    rows = parse_payload(mcp.search("tremblement de terre", "be", limit=5))
    assert rows, "full-text body search found nothing"


def test_search_finds_universal_glossary(mcp):
    rows = parse_payload(mcp.search("deductible", "be", type="concept"))
    paths = [r["path"] for r in rows]
    assert any(p.startswith("_meta/universal-glossary/") for p in paths)
    page = mcp.get_page(next(p for p in paths if p.startswith("_meta/")))
    assert not page.startswith("Not found")


def test_get_page_roundtrip_from_search(mcp):
    rows = parse_payload(mcp.search("familiale", "be", type="product", limit=1))
    page = mcp.get_page(rows[0]["path"])
    assert not page.startswith("Not found")
    assert "source_url" in page


def test_get_product_grounding_header(mcp):
    out = mcp.get_product("be", "ag", "Top Familiale")
    assert out.startswith("[GROUNDING CONTRACT")
    assert "CITATION" in out and "source_url=" in out
    payload = parse_payload(out)
    assert payload["insurer_slug"] == "ag"


def test_get_product_not_found_is_honest(mcp):
    out = mcp.get_product("be", "ag", "produit qui n'existe pas")
    assert "No product matching" in out


def test_compare_products(mcp):
    out = mcp.compare_products("be", ["Mobility Safe 1", "Confort Auto"], "exclusions",
                               insurer_slugs=["baloise", "axa"])
    assert out.startswith("[GROUNDING CONTRACT")
    payload = parse_payload(out)
    assert len(payload["products"]) == 2
    for p in payload["products"]:
        assert p["source_url"]
        assert isinstance(p["exclusions"], list)


def test_compare_products_bad_dimension(mcp):
    assert "must be one of" in mcp.compare_products("be", ["a", "b"], "prix")


def test_find_overlap_worked_example(mcp):
    out = mcp.find_overlap("be", ["Police habitation pour le propriétaire",
                                  "La Police familiale"])
    payload = parse_payload(out)
    assert payload["candidate_overlaps"], "the canonical home+family overlap found nothing"
    cats = [o["category"] for o in payload["candidate_overlaps"]]
    assert any("responsabilit" in c.lower() for c in cats)
    assert "note" in payload


def test_find_overlap_reports_unmatched_products(mcp):
    """A name that resolves to nothing used to vanish from the result: the caller got a
    confident overlap analysis over 2 products while believing it covered 3."""
    out = mcp.find_overlap("be", ["Police habitation pour le propriétaire",
                                  "La Police familiale", "produit qui n'existe pas"])
    payload = parse_payload(out)
    assert payload["unmatched"] == ["produit qui n'existe pas"]
    assert len(payload["products"]) == 2
    assert "INCOMPLETE" in payload["note"]


def test_find_overlap_too_few_matches_names_the_unmatched(mcp):
    out = mcp.find_overlap("be", ["La Police familiale", "produit qui n'existe pas"])
    assert "Need at least 2 matching products" in out
    assert "produit qui n'existe pas" in out


def test_get_branch_overview(mcp):
    out = mcp.get_branch_overview("be", "auto")
    assert "No branch overview" not in out and len(out) > 200


def test_get_branch_overview_gap_is_honest(mcp):
    slug = branch_without_overview("be")
    if slug is None:
        pytest.skip("every taxonomy branch now has an overview page")
    out = mcp.get_branch_overview("be", slug)
    assert "No branch overview" in out
