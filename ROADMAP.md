# Roadmap

## Phase 1 - Foundation & vertical slice (done)
- [x] Repo scaffold, dual license, conventions, schemas
- [x] Committed provider-agnostic extraction agent (prompts + adapters)
- [x] Source configs for representative Belgian insurers
- [x] Pipeline: discover → download → extract → verify_grounding → build_wiki → build_index → validate
- [x] Smoke run + vertical slice across the first insurers
- [x] Hand-authored layer started: Auto / Habitation / Vie privée + regulations, glossary, MOCs
- [x] MCP server (list, search, get_product, compare_products, find_overlap)

## Phase 2 - Scale Belgium (in progress)
- [x] Source configs for 24 Belgian insurers
- [x] Full download + extract run: 269 products, 17 branches (resumable)
- [x] Coverage & freshness dashboard in AGENTS.md
- [ ] Finish the enumerated market (~630 document rows enumerated, 269 ingested)
- [ ] Enumerate census group B (~45 brands/carriers, `_meta/be-market-census.md`)
- [ ] Allianz - 28 documents enumerated in `sources/be/allianz.yml`, Cloudflare-blocked on the free httpx
      stack, 0 PDFs fetched; needs a browser fetcher

## Phase 3 - Distribution (done)
- [x] Publish to public GitHub (2026-07-05); licensing/attribution finalized
- [x] CI: validation + build-idempotence gates on every push
- [x] Browsable static site from `wiki/` (MkDocs Material + GitHub Pages)
- [x] MCP server listed on the official MCP registry (and on PyPI)
- [x] Monthly source-freshness check (opens an issue when an insurer republishes a PDF)
- [ ] Tag and release 0.3.0 - the repo is at 0.3.0, PyPI still serves 0.2.0, and releases are tag-driven

## Phase 4 - Content depth
- [x] Branch overview pages for every branch that has products (Belgium)
- [x] Complete the insurer list in the Belgium MOC
- [x] Make the universal glossary reachable from inside the vault
- [ ] Populate edition metadata (`product_family`, edition status) across extractions
- [ ] Flag run-off and legacy editions so closed products stop reading as current
- [ ] NL-language coverage parity for Belgium (currently FR only)
- [ ] Branch pages for the Luxembourg branches that are wikilinked but still unwritten -
      `make validate COUNTRY=lu` names the remaining ones on every run

## Phase 5 - Second country (done)
- [x] Prove the country-agnostic recipe on a second country - done three times over: France (10 insurers,
      774 documents), Luxembourg (3 insurers, 160 documents), Switzerland (1 insurer, 3 documents)
- [x] Country bootstrap written up as a repeatable recipe (`_meta/BOOTSTRAP-COUNTRY.md`)
- [ ] Move the remaining FR-hardcoded render strings (section titles, disclaimer) into the country config -
      still hardcoded in `pipeline/render.py`; blocks any non-French-language country

## Phase 6 - Broaden the four countries
- [ ] **fr** - finish the enumerated market: arbitrate generali; start abeille, mgen, cnp, sogessur,
      creditmutuel, gmf, mma, swisslife (`_meta/fr-market-census.md`)
- [ ] **lu** - land foyer-global-health (101 PDFs downloaded, extraction in flight)
- [ ] **ch** - Switzerland is a starter slice, not a country: 1 insurer, 3 documents of 12 downloaded, and no
      branch, regulation or glossary page. The country MOC exists as a declared stub; the rest of the
      hand-authored layer and more carriers are the work, plus the Phase 5 render-strings item for the DE/IT
      sides. Ingestion shortlist and the Helvetia blocker are in `_meta/ch-market-census.md`.

## Non-goals
- No RAG / vector store - this is a wiki, not a retrieval black box.
- No advice, scoring, or ranking of insurers.
- No hidden datasets - everything regenerates from committed inputs.
