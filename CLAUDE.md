# openinsurance-wiki - operating rules for agents

You are working in a public, open-source, country-agnostic insurance knowledge base. It scrapes insurers' public
PDFs and extracts them into a rich, source-cited Markdown wiki. Read this before editing anything.

## The eight rules

1. **No personalized advice.** This is an information tool. Never recommend, rank, or score insurers/products, and
   never tell a user what to buy. Factual descriptions and neutral side-by-side comparisons only. (Giving
   personalized insurance advice requires a license - e.g. FSMA in Belgium.)
   **This rule is per jurisdiction, and it is deliberately stricter than any single one of them.** Switzerland,
   for instance, draws the line elsewhere: OS (RS 961.011) art. 182a al. 3 says "les personnes qui fournissent
   uniquement des données ou des informations ne sont pas considérées comme des intermédiaires d'assurance", and
   al. 2 catches ranking and price comparison only for those who "ont un intérêt économique" in a contract being
   concluded. So in Switzerland the exposure comes from **monetisation**, not from comparing. Keeping the strict
   rule everywhere is the simple way to be safe in all of them at once; before relaxing it anywhere, check that
   jurisdiction's own text, and note that monetising the project would change the analysis in Switzerland even
   if nothing else changed. Per-country detail lives in `_meta/<cc>-market-census.md`.
2. **Never edit generated pages.** Anything with `generated: true` in its frontmatter (everything under
   `wiki/**/products/` and `wiki/**/insurers/`) is produced by `pipeline/build_wiki.py` from the extraction data.
   To fix a fact, edit the JSON in `data/<cc>/extracted/` (or fix the prompt/re-extract) and rebuild. Editing a
   generated `.md` by hand will be overwritten.
3. **Every product fact traces to a source.** Each product page cites its `source_url` and page numbers. If a
   claim can't be tied to the source document, it does not go on the page. When in doubt, leave it out.
4. **Grounded, not inferred.** The extraction transcribes and structures what the PDF says. Do not generalize,
   infer market norms, or fill gaps from outside knowledge. Observation ≠ inference - keep them separate.
5. **Freshness is explicit.** Every page carries a `freshness` date (and products carry the PDF `edition_date`).
   Flag stale editions rather than hiding them.
6. **Gaps are labeled, not hidden.** Missing coverage, an unresolved PDF URL, or an unwritten page → mark it
   (`status: stub`, an explicit "not found" note). Silent omission reads as false completeness.
7. **Reproducibility is sacred.** Every input (sources, prompts, schema) is committed; every output is
   regenerable. Don't introduce a hidden dataset, a hand-tweaked generated page, or a non-committed prompt.
8. **Mind dates, versions, extensions.** Never conflate an old edition of a product with the current one. Capture
   `edition_date`; group by `product_family`; the newer edition supersedes the older (linked, not deleted).
   Variants (channel/formula) are parallel, not superseded. An extension/option is not a standalone product
   (`is_extension`/`extends`). See CONTRIBUTING.md "Versions, editions & extensions".

## The two layers (do not blur them)

- **Hand-authored** (`branches/`, `regulations/`, `glossary/`, `wiki/universal-glossary/`, all MOCs): curated
  conceptual/regulatory prose. `generated: false`.
- **Generated** (`products/`, `insurers/`): emitted by the pipeline. `generated: true`. Never hand-edit.

The generator's write-scope is only the generated folders, so a human editing a branch page and a full rebuild
can never conflict.

## The pipeline (what runs, in order)

`discover.py` → `download.py` → `extract.py` → `verify_grounding.py` → `build_wiki.py` → `build_index.py` →
`validate.py`. All resumable and idempotent (`make all`). Only `extract.py` calls an LLM.

## The extraction agent

The LLM is asked exactly what's in `extraction-agent/SYSTEM_PROMPT.md` + `EXTRACTION_TASK.md`, constrained by
`GROUNDING_RULES.md`, `OUTPUT_SPEC.md`, and `schema/product.schema.json`. It is **provider-agnostic** - the model
is chosen in `.env`; the prompts never change per provider. If you improve extraction quality, you edit the
prompt files (and bump the prompt version so cached extractions re-run), never a per-provider hack.

## Style

- Neutral, encyclopedic. No sales language, no buzzwords.
- Markdown starts at H2 (the filename/frontmatter is the title). Wikilinks in `[[shortest]]` form.
- Dates ISO `YYYY-MM-DD`. Money/limits quoted as they appear in the source.
- Belgian product content is primarily FR/NL - preserve the source language; don't silently translate.
