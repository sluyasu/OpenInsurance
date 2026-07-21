"""get_coverage (compact, topic-scoped answers) and verify_claim (verbatim
evidence retrieval). Both exist to keep the answering LLM inside the document:
small relevant payloads instead of a 75 KB JSON to paraphrase."""

from conftest import country_branches, index_rows, parse_payload


def test_citation_line_carries_the_edition_age(mcp):
    """The age signal has to be on the primary path. It was added to _doc_meta, which only
    feeds candidate listings and other_documents, so get_product still returned a 2010
    edition looking exactly like a current one."""
    line = next(l for l in mcp.get_product("be", "ergo", "Terme Fixe").splitlines()
                if l.startswith("CITATION"))
    assert "edition_age_years=" in line
    assert "NOT stated in the document" in line
    recent = next(l for l in mcp.get_product("be", "axa", "Confort Auto").splitlines()
                  if l.startswith("CITATION"))
    assert "edition_age_years=" not in recent


def test_citation_never_claims_a_product_is_withdrawn(mcp):
    """Same rule as the wiki page: report the age, never infer the commercial status."""
    line = next(l for l in mcp.get_product("be", "ergo", "Terme Fixe").splitlines()
                if l.startswith("CITATION")).lower()
    for f in ("no longer sold", "discontinued", "withdrawn", "run-off"):
        assert f not in line


def test_get_coverage_returns_only_relevant_items(mcp):
    out = mcp.get_coverage("be", "axa", "Confort Auto", "vol")
    assert out.startswith("[GROUNDING CONTRACT")
    assert "CITATION" in out
    payload = parse_payload(out)
    items = payload["matched_coverages"] + payload["matched_exclusions"]
    assert items, "topic 'vol' matched nothing in a comprehensive auto policy"
    assert all("vol" in mcp._norm(f"{i.get('name', '')} {i.get('description', '')}")
               for i in items)
    assert payload["source_url"]


def test_get_coverage_much_smaller_than_get_product(mcp):
    full = mcp.get_product("be", "axa", "Confort Auto")
    compact = mcp.get_coverage("be", "axa", "Confort Auto", "vol")
    assert len(compact) < len(full) / 3


def test_get_coverage_empty_topic_match_is_honest(mcp):
    out = mcp.get_coverage("be", "axa", "Confort Auto", "xylophone quantique")
    payload = parse_payload(out)
    assert payload["matched_coverages"] == []
    assert "not proof of absence" in payload["note"]


def test_get_coverage_accent_insensitive_topic(mcp):
    out = mcp.get_coverage("be", "ag", "Top Familiale", "degats causes par un animal")
    assert "No product matching" not in out


def test_verify_claim_finds_supporting_quote(mcp):
    # The canonical chatbot-test example: Touring's travel conditions state that
    # off-piste skiing is only covered with a certified instructor.
    out = mcp.verify_claim("be", "touring", "Travel",
                           "le ski hors-piste est couvert avec un moniteur agree")
    payload = parse_payload(out)
    top = mcp._norm(payload["evidence"][0]["text"])
    assert "hors-piste" in top and "moniteur" in top
    assert payload["note"].startswith("this tool retrieves")


def test_verify_claim_no_evidence_means_not_supported(mcp):
    out = mcp.verify_claim("be", "ag", "Top Familiale",
                           "couvre les fusees interplanetaires xyzzy")
    payload = parse_payload(out)
    assert payload["evidence"] == []
    assert payload["evidence_total"] == 0


def test_verify_claim_keeps_amounts(mcp):
    # Digits are content: a claim about an amount must match on the number.
    terms = mcp._claim_terms("franchise de 319,76 euros par sinistre")
    assert any("319" in t for t in terms)


def test_list_countries_honest_branch_counts(mcp):
    rows = parse_payload(mcp.list_countries())
    be = next(r for r in rows if r["country"] == "be")
    idx = index_rows("be")
    covered = {r["branch"] for r in idx
               if r.get("type") == "product" and r.get("branch")}
    assert be["branches_covered"] == len(covered)
    assert be["branch_taxonomy"] == len(country_branches("be"))
    assert be["branch_overview_pages"] == sum(1 for r in idx if r.get("type") == "branch")
    assert be["branch_overview_pages"] >= 3  # some overview pages exist
