# Output specification

Return **exactly one JSON object** conforming to `schema/product.schema.json`. No text outside the JSON. It must
parse and validate. Below is what each part must contain; the schema is authoritative for types and field names.

## Metadata (fill what the document/context gives you)

- `schema_version`: "1.0". `prompt_version`: provided in the task (echo it back).
- `country`, `insurer_slug`, `insurer_name`, `branch`, `document_type`, `language`, `source_url`: given in the
  task - copy them through.
- `product_name`: the commercial product name exactly as printed on the document.
- `reference`, `edition_date`, `target_audience`, `branch_code`: from the document if present, else null.
- **`edition_date`** matters a lot: the same product is re-issued over time and an old edition may describe a product no longer sold. Capture the edition/version date whenever the document shows one (cover, footer code, "édition MM/AAAA").
- `product_family`: the base product line with the edition date and distribution variant removed (e.g. `Confort Auto`, `Top Habitation`, `Police Familiale`). This groups editions/variants/related documents of the same product.
- `variant`: a distribution channel or formula that distinguishes parallel versions of the same product (e.g. `BNPPF`, `courtier`, `Flex Premium`), else null.
- `is_extension` / `extends`: if this document is an OPTION / EXTENSION / rider of a base product (not a standalone product), set `is_extension: true` and put the base product's name in `extends`. Otherwise `is_extension: false`, `extends: null`.
- Leave `superseded` null (it is computed at build time).
- `source_pages`: total pages (given). Leave `source_pdf`, `source_sha256`, `fetched_at`, `extraction_model`
  null unless provided - the pipeline fills them.

## Content (the substance - be exhaustive)

- `summary`: 2-4 neutral factual sentences. What the product is and its main cover. No advice.
- `definitions[]`: every defined term with its definition and page.
- `coverages[]`: **every** guarantee. For each: `name`, `description` (close to source wording), `is_optional`,
  `territorial_scope`, `limits` (verbatim), `sub_limits[]`, `deductible`, `conditions[]`, `page`.
- `exclusions[]`: **every** exclusion. `name`, `description`, `applies_to` (a coverage name or "all"), `page`.
  Do not skip the general exclusions section.
- `deductibles`: general franchise info (`standard`, `variable`, `per_coverage`, `page`).
- `waiting_periods[]`, `obligations[]` (duties of the insured, with `timing` and `sanction` if stated),
  `claims_procedure[]` (steps with `deadline`), `duration_and_cancellation` (duration, tacit renewal, notice,
  methods, special rights), `prescription_period`, `premium` (mechanics only, never a price quote),
  `special_conditions[]`.
- `key_quotes[]`: a handful of exact verbatim sentences anchoring the core cover and main exclusions (each must
  be findable in the source text - see grounding rules).
- `gaps[]`: anything you could not extract, and why.

## Rules of thumb

- Prefer many precise items over few merged ones. A conditions-générales for auto typically has 10-30 coverages
  and 15-40 exclusions - if you produced 3, you under-extracted.
- Empty arrays are fine when a section genuinely doesn't exist; note it in `gaps` if you'd expect it to.
- Keep values in the source language; use the schema's English keys.
- Output valid JSON: no trailing commas, no comments, no NaN/Infinity, no Markdown fences around commentary
  (a bare ```json fenced block is tolerated by the parser, but plain JSON is preferred).
