# Handoff / current state

Snapshot of where the project stands, for a fresh agent or contributor.

## What this is
A self-sufficient, open-source insurance wiki: scrape public insurer PDFs → extract to rich, source-cited
Markdown → browse/query as a wiki or via MCP. Belgium first; country-agnostic. See [`README.md`](README.md).
Public on GitHub since 2026-07-05: https://github.com/sluyasu/OpenInsurance

## Status (Belgium)
- **Scaffold + docs + schema + extraction agent + MCP + test suite in CI:** done.
- **Coverage:** 24 insurers, 269 products, ~4570 coverages, ~7430 exclusions, 17 populated branches
  (auto, habitation, vie-privee, sante, voyage, protection-juridique, velo, accidents, rc-professionnelle,
  navigation, chasse, epargne, pension, obseques, animaux, cyber, autres). Insurers: axa, ethias, kbc, ag,
  baloise, belfius, belfius-direct, dvv, nn, pv, vivium, yuzzu, dkv, das, amma, argenta, federale, touring,
  hiscox, acm, actel, ergo, athora, cardif.
- **Version method:** live - `edition_date`/`product_family`/`variant`/`is_extension`/`extends` + `pipeline/link.py`
  computes current-vs-superseded and cross-links editions/variants/extensions ("Documents liés" section).
- **Analysis:** MCP `compare_products` + `find_overlap` (candidate duplicate cover across policies, via the
  committed `schema/coverage_categories.json` taxonomy), plus `get_coverage` (topic-scoped compact answers)
  and `verify_claim` (verbatim evidence for a fact-check). One product name can map to several documents
  (CG + IPID, several editions): the tools select general conditions first, newest edition, refuse ambiguous
  names with the candidates listed, and always say which document they picked. See `mcp/README.md`.
- **Validation:** 321 notes, 0 errors, 0 warnings (every populated branch now has an overview page).
  `make build` is idempotent (no-op rebuild = 0 diff).
- **Distribution:** `openinsurance-wiki-mcp` 0.3.0 on PyPI and on the MCP registry (releases are
  tag-driven, see `.github/workflows/release.yml`); GitHub Pages live at
  https://sluyasu.github.io/OpenInsurance/.

### Still open (not blocking)
- **Allianz** - Cloudflare-blocked on the free httpx stack; the 28 documents are enumerated in
  `sources/be/allianz.yml` but no PDF is registered yet, so the entries are inert.
- **Edition metadata is sparse** in the current extractions (`product_family`/`edition_status` mostly absent);
  linking falls back to name heuristics. Populating it means a re-extraction pass.
- **NL-language** editions (currently FR only) and a **2nd country** to prove the country-agnostic recipe.
- **Higher-precision overlap** (option 2): a coverage-normalization pass tagging one category per coverage.

## How to run
```bash
make setup                         # deps + playwright chromium
cp .env.example .env               # set LLM_PROVIDER + key
make all COUNTRY=be                # download → extract → ground → build → index → validate
# or per insurer: make download extract build COUNTRY=be INSURER=<slug>
```

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
