# Roadmap

## Phase 1 - Foundation & vertical slice (in progress)
- [x] Repo scaffold, dual license, conventions, schemas
- [x] Committed provider-agnostic extraction agent (prompts + adapters)
- [ ] Source configs for 2-3 representative Belgian insurers
- [ ] Pipeline: discover → download → extract → verify_grounding → build_wiki → build_index → validate
- [ ] Cheap smoke run (1 PDF) to validate the chain and prompt quality
- [ ] Vertical-slice run across the 2-3 insurers
- [ ] Hand-authored layer: branch overviews, regulations, glossary, MOCs
- [ ] MCP server + smoke test

## Phase 2 - Scale Belgium
- [ ] Source configs for all Belgian insurers
- [ ] Full download + extract run (resumable)
- [ ] Coverage & freshness dashboard in AGENTS.md

## Phase 3 - Distribution & second country
- [ ] Publish to public GitHub; finalize licensing/attribution
- [ ] Optional MkDocs Material static site
- [ ] Prove the country-agnostic recipe on a second country
- [ ] NL/DE language coverage parity

## Non-goals
- No RAG / vector store - this is a wiki, not a retrieval black box.
- No advice, scoring, or ranking of insurers.
- No hidden datasets - everything regenerates from committed inputs.
