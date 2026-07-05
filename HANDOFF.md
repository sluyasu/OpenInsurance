# Handoff / current state

Snapshot of where the project stands, for a fresh agent or contributor.

## What this is
A self-sufficient, open-source insurance wiki: scrape public insurer PDFs → extract to rich, source-cited
Markdown → browse/query as a wiki or via MCP. Belgium first; country-agnostic. See [`README.md`](README.md).

## Status (Belgium)
- **Scaffold + docs + schema + extraction agent + MCP:** done.
- **Coverage:** 17 insurers, 162 products, ~3290 coverages, ~5540 exclusions, 12 branches
  (auto, habitation, vie-privee, sante, voyage, protection-juridique, velo, accidents, rc-professionnelle,
  navigation, chasse, autres). Insurers: axa, ethias, kbc, ag, baloise, belfius, dvv, nn, pv, vivium, yuzzu,
  dkv, das, amma, argenta, federale, touring.
- **Version method:** live - `edition_date`/`product_family`/`variant`/`is_extension`/`extends` + `pipeline/link.py`
  computes current-vs-superseded and cross-links editions/variants/extensions ("Documents liés" section).
- **Analysis:** MCP `compare_products` + `find_overlap` (candidate duplicate cover across policies, via the
  committed `schema/coverage_categories.json` taxonomy). See `mcp/README.md`.
- **Validation:** 0 errors, 0 warnings; grounding ~98%. `make build` is idempotent (no-op rebuild = 0 diff).

### Still open (not blocking)
- **Allianz** - Cloudflare-blocked on the free httpx stack; needs a browser fetcher.
- **NL-language** editions (currently FR only) and a **2nd country** to prove the country-agnostic recipe.
- **Higher-precision overlap** (option 2): a coverage-normalization pass tagging one category per coverage.
- Not yet **committed to git** / pushed to public GitHub (awaiting go-ahead + licensing confirmation).

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
- Data: `data/<cc>/pdfs/` (gitignored), `data/<cc>/extracted/` (committed), `data/<cc>/manifest.json`
- Wiki: `wiki/<cc>/`
- Conventions: `_meta/README.md`

## Guardrails
Information only (no advice/ranking). Never hand-edit `generated: true` pages. Every product fact cites a source.
Full rules in [`CLAUDE.md`](CLAUDE.md).

## Cost note
Only `extract.py` calls a paid/LLM API. It is resumable (skip-existing keyed by PDF checksum + prompt version),
so large runs can stop and restart safely. Validate the chain with a single-PDF smoke run before a bulk run.
