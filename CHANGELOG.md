# Changelog

Notable changes to the MCP server and the dataset. Dates are the release dates.

The package version tracks the **server**; the dataset it reads lives in this repo and
grows independently (see the coverage table in `AGENTS.md`).

## 0.3.0 - 2026-07-21

The server had drifted from the published package: 0.2.0 was tagged before the product
grouping work landed, so an install from PyPI and a clone of this repo answered the same
question differently. This release closes that gap and adds what came after it.

### Correctness

- **Product grouping is driven by `product_family`.** Documents merge into one commercial
  product only when the shared family is unambiguous, and the result no longer depends on
  the order documents are read in. Containment alone used to merge names it should not.
- **Variants no longer supersede each other.** Supersession compares editions within the
  same `(document_type, variant)`, so a Luxembourg edition sold alongside a Belgian one is
  no longer stamped "replaced by a newer edition". Being the only edition of its kind now
  reports no status rather than "current", since one document is not evidence that a newer
  one does not exist.
- **Every edition date format the wiki understands is understood here too**: `YYYYMMDD`
  (previously misread as year 201, month 23), `YYYYMM`, `MMYYYY`, `MMYY`, and dates
  embedded in form references. A regression test asserts the two parsers agree.
- **`find_overlap` reports unmatched product names.** A name that resolved to nothing used
  to disappear, so a caller asking about three products received a confident analysis of
  two. Unmatched names are returned and the note marks the result incomplete.

### Honesty

- **Old editions carry their age.** Documents whose printed edition is seven or more years
  older than the day they were collected now report `edition_age_years` and a note in every
  citation. The note states the age and that the insurer was still publishing the document;
  it does **not** claim the product was withdrawn, because the documents do not say so.
- Unknown country codes are explained in `search` and `list_branches` instead of returning
  an empty result.

### Dataset

- 269 products across 24 insurers and 17 branches (was 162 / 17 / 12).
- Every extraction validates against the committed schema, checked in CI.
- All quoted evidence is verbatim in the source PDFs (1771 of 1771 quotes).

## 0.2.0 - 2026-07-07

- New tools: `get_coverage` (topic-scoped answers) and `verify_claim` (verbatim evidence).
- Ambiguous product names are refused with the candidates listed instead of silently
  picking one; exact name wins over prefix siblings; deterministic tie-break with a flag.
- A server started without a dataset fails fast with instructions instead of serving `[]`.
- Every file read once: all tools respond in under 4 ms warm.
- 87-test pytest suite wired into CI.

## 0.1.0 - 2026-07-06

- First public release: `list_countries`, `list_branches`, `search`, `get_page`,
  `get_product`, `compare_products`, `find_overlap`, `get_branch_overview`.
- Citation line and grounding contract in every response.
- `get_page` restricted to a whitelist of readable roots.
