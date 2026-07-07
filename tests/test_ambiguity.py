"""A name matching several distinct products must be refused with candidates, never
silently resolved to an arbitrary one. Real ties must be flagged, superseded
documents must say so."""

from conftest import parse_payload


def test_compare_refuses_cross_insurer_ambiguity(mcp):
    # "assurance auto" matches distinct products at several insurers.
    out = mcp.compare_products("be", ["assurance auto", "Confort Auto"],
                               insurer_slugs=None)
    assert "Ambiguous product name" in out
    payload = parse_payload(out)
    assert len(payload["assurance auto"]) >= 2
    slugs = {c["insurer_slug"] for c in payload["assurance auto"]}
    assert len(slugs) >= 2


def test_compare_refuses_within_insurer_ambiguity(mcp):
    # "assurance" matches many distinct AG products and none exactly.
    out = mcp.find_overlap("be", ["assurance", "La Police familiale"],
                           insurer_slugs=["ag", "kbc"])
    assert "Ambiguous product name" in out
    payload = parse_payload(out)
    names = {c["product_name"] for c in payload["assurance"]}
    assert len(names) >= 2


def test_prefix_without_exact_match_is_ambiguous(mcp):
    # AMMA sells HOSPI-PLAN and HOSPI SAFE - SERENITY; no product is named just
    # "HOSPI", so the query must be refused with both candidates listed.
    out = mcp.get_product("be", "amma", "HOSPI")
    assert "Multiple distinct products match" in out
    payload = parse_payload(out)
    assert {"AMMA HOSPI-PLAN", "AMMA HOSPI SAFE - SERENITY"} <= {c["product_name"]
                                                                 for c in payload}


def test_exact_name_wins_over_prefix_siblings(mcp):
    # AXA sells "Confort Auto" and its legal-protection add-ons "Confort Auto -
    # Protection juridique Fix/Full". The exact name must resolve to the main
    # product and say which similar products it skipped.
    out = mcp.get_product("be", "axa", "Confort Auto")
    assert "Multiple distinct products match" not in out
    assert "product='Confort Auto'" in out
    assert "document_type=conditions_generales" in out
    assert "Similar products at this insurer not returned" in out
    assert "Protection juridique" in out.split("\n[Similar products")[1].split("]")[0]


def test_cg_and_ipid_name_variants_resolve_as_one_product(mcp):
    # Baloise "Mobility Safe 1" (CG) and "Assurance Auto Mobility Safe 1" (IPID)
    # are the same product: resolution must pick the CG, not refuse.
    out = mcp.get_product("be", "baloise", "Mobility Safe 1")
    assert "Multiple distinct products match" not in out
    assert "document_type=conditions_generales" in out
    assert "other_documents" in out


def test_get_product_ambiguity_lists_one_candidate_per_product(mcp):
    out = mcp.get_product("be", "amma", "hospi")
    assert "Multiple distinct products match" in out
    assert out.startswith("[GROUNDING CONTRACT")  # disclaimer also on this path
    payload = parse_payload(out)
    assert len({c["product_name"] for c in payload}) == len(payload)


def test_real_tie_is_flagged(mcp):
    # Yuzzu has two general conditions of "Assurance Auto" issued the same day
    # (AUTO-07-FR and AUTO-08-FR) with different content: the response must say
    # the selection between them fell back to reference order.
    out = mcp.get_product("be", "yuzzu", "Assurance Auto")
    assert "same edition exists" in out
    # deterministic: reference order puts AUTO-07-FR first
    assert "reference=AUTO-07-FR" in out.split("\n")[1]


def test_superseded_choice_is_visible(mcp):
    # AMMA HOSPI-PLAN only has a superseded CG from 2007: choosing it is fine,
    # hiding that it is superseded is not.
    out = mcp.get_product("be", "amma", "HOSPI-PLAN")
    assert "superseded=True" in out
    comp = mcp.compare_products("be", ["HOSPI-PLAN", "La Police familiale"],
                                insurer_slugs=["amma", "kbc"])
    payload = parse_payload(comp)
    hospi = next(p for p in payload["products"] if "HOSPI-PLAN" in p["product_name"])
    assert hospi["superseded"] is True
