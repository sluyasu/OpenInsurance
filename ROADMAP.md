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

## Phase 3 - Distribution (done)
- [x] Publish to public GitHub (2026-07-05); licensing/attribution finalized
- [x] CI: validation + build-idempotence gates on every push
- [x] Browsable static site from `wiki/` (MkDocs Material + GitHub Pages)
- [x] MCP server listed on the official MCP registry (and on PyPI)
- [x] Monthly source-freshness check (opens an issue when an insurer republishes a PDF)

## Phase 4 - Content depth
- [x] Branch overview pages for every branch that has products
- [ ] Complete the insurer list in the Belgium MOC
- [ ] Make the universal glossary reachable from inside the vault
- [ ] Populate edition metadata (`product_family`, edition status) across extractions
- [ ] Flag run-off and legacy editions so closed products stop reading as current
- [ ] Allianz - Cloudflare-blocked on the free httpx stack; needs a browser fetcher
- [ ] NL-language coverage parity (currently FR only)

## Phase 5 - Second country
- [ ] Prove the country-agnostic recipe on a second country
- [ ] Move the remaining FR-hardcoded render strings (section titles, disclaimer) into the country config

## Non-goals
- No RAG / vector store - this is a wiki, not a retrieval black box.
- No advice, scoring, or ranking of insurers.
- No hidden datasets - everything regenerates from committed inputs.
