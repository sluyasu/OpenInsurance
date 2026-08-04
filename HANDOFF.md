# Handoff / current state

Snapshot of where the project stands, for a fresh agent or contributor.

## What this is
A self-sufficient, open-source insurance wiki: scrape public insurer PDFs → extract to rich, source-cited
Markdown → browse/query as a wiki or via MCP. Belgium first, then France, Luxembourg and Switzerland;
country-agnostic. See [`README.md`](README.md).
Public on GitHub since 2026-07-05: https://github.com/sluyasu/OpenInsurance

## Status
Four countries are live. The country-agnostic recipe is no longer a claim to prove - it has been run three
more times after Belgium. Belgium remains the reference country: it is the only one with a complete
hand-authored layer, and the one to look at to see what "finished" is supposed to mean.

- **Scaffold + docs + schema + extraction agent + MCP + test suite in CI:** done. 134 tests pass.
- **Coverage:** 38 insurers, 1,206 documents, 25,992 coverages, 31,607 exclusions.

  | cc | insurers | documents | coverages | exclusions | branch pages | regulations | glossary |
  |---|---:|---:|---:|---:|---:|---:|---:|
  | be | 24 | 269 | 4,574 | 7,431 | 17 | 3 | 6 |
  | fr | 10 | 774 | 19,218 | 21,694 | 24 | 1 | 0 |
  | lu | 3 | 160 | 2,086 | 2,183 | 13 | 1 | 0 |
  | ch | 1 | 3 | 114 | 299 | 0 | 0 | 0 |

  Belgium (17 populated branches): axa, ethias, kbc, ag, baloise, belfius, belfius-direct, dvv, nn, pv,
  vivium, yuzzu, dkv, das, amma, argenta, federale, touring, hiscox, acm, actel, ergo, athora, cardif.
  France: matmut 200, macif 151, smacl 111, maaf 92, maif 69, gan 50, thelem 45, groupama 31, luko 14,
  direct-assurance 11. Luxembourg: lalux 90, dkv 36, baloise 34. Switzerland: vaudoise 3.
  The generated coverage table in `AGENTS.md` is the live version of these counts.
- **Version method:** live - `edition_date`/`product_family`/`variant`/`is_extension`/`extends` + `pipeline/link.py`
  computes current-vs-superseded and cross-links editions/variants/extensions ("Documents liés" section).
- **Analysis:** MCP `compare_products` + `find_overlap` (candidate duplicate cover across policies, via the
  committed `schema/coverage_categories.json` taxonomy), plus `get_coverage` (topic-scoped compact answers)
  and `verify_claim` (verbatim evidence for a fact-check). One product name can map to several documents
  (CG + IPID, several editions): the tools select general conditions first, newest edition, refuse ambiguous
  names with the candidates listed, and always say which document they picked. See `mcp/README.md`.
- **Validation:** `validate.py --strict-links` is at **0 errors on all four countries**. Note counts as of
  2026-08-04 (be 321 / 1 warning, fr 811 / 1, lu 179 / 3, ch 6 / 0); the Luxembourg figures move while
  foyer-global-health lands, so re-run rather than trust them. The remaining warnings are duplicate page
  names with no bare link yet, plus the Luxembourg branches that are wikilinked but have no overview page.
  `make build` is idempotent (no-op rebuild = 0 diff).
- **Distribution:** the repo is at **0.3.0** but **PyPI still serves 0.2.0** - releases are tag-driven
  (`.github/workflows/release.yml`) and no `v0.3.0` tag was pushed, so an install from PyPI is a version
  behind a clone. Also on the MCP registry; GitHub Pages live at https://sluyasu.github.io/OpenInsurance/.

### Still open (not blocking)
- **Ingestion in flight:** `lu` foyer-global-health (101 PDFs downloaded, extraction running) and `ch`
  vaudoise (12 PDFs downloaded, 3 extracted).
- **Switzerland is a starter slice, not a country yet** - 1 insurer, 3 documents of 12 downloaded, and no
  branch, regulation or glossary page. The country MOC exists and says so explicitly (`status: stub`).
- **France is nowhere near its enumerated market** - generali is censused but not arbitrated; abeille, mgen,
  cnp, sogessur, creditmutuel, gmf, mma and swisslife are not started. See `_meta/fr-market-census.md`.
- **Belgium group B** (~45 brands/carriers, `_meta/be-market-census.md`) is still to enumerate.
- **Allianz (be)** - Cloudflare-blocked on the free httpx stack; the 28 documents are enumerated in
  `sources/be/allianz.yml` but no PDF is registered yet, so the entries are inert.
- **Edition metadata is sparse** in the current extractions (`product_family`/`edition_status` mostly absent);
  linking falls back to name heuristics. Populating it means a re-extraction pass.
- **NL-language** editions for Belgium (currently FR only).
- **Render strings are hardcoded French** in `pipeline/render.py` ("Garanties", "Exclusions",
  "Documents liés"). Harmless while every country ingested is French-language; a blocker for the German and
  Italian sides of Switzerland.
- **Higher-precision overlap** (option 2): a coverage-normalization pass tagging one category per coverage.

## How to run
```bash
make setup                         # deps + playwright chromium
cp .env.example .env               # set LLM_PROVIDER + key
make all COUNTRY=be                # download → extract → ground → build → index → validate
# or per insurer: make download extract build COUNTRY=be INSURER=<slug>
```
`COUNTRY` is any of `be`, `fr`, `lu`, `ch`.

## Key locations
- Pipeline: `pipeline/*.py` (discover, download, extract, verify_grounding, build_wiki, build_index, validate)
- The exact LLM prompts: `extraction-agent/*.md`
- Where to find PDFs: `sources/<cc>/*.yml`
- Data: `data/<cc>/pdfs/` (gitignored), `data/<cc>/extracted/` (committed), `data/<cc>/manifest.json`,
  `data/<cc>/gaps.json` (extraction gaps, e.g. scanned PDFs without a text layer)
- Wiki: `wiki/<cc>/`
- Conventions: `_meta/README.md`

## Guardrails
Information only (no advice/ranking). Never hand-edit `generated: true` pages. Every product fact cites a source.
Full rules in [`CLAUDE.md`](CLAUDE.md).

## Cost note
Only `extract.py` calls a paid/LLM API. It is resumable (skip-existing keyed by the source-url hash of the
filename + PDF checksum + prompt version), so large runs can stop and restart safely. Validate the chain with a
single-PDF smoke run before a bulk run.
