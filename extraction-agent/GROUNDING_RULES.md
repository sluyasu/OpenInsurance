# Grounding rules (anti-hallucination)

These rules are absolute. A grounded-but-incomplete extraction is far better than a complete-but-invented one.

1. **Source-bound.** Every value you output must be supported by the provided text. If it is not in the text, it
   does not go in the JSON. When in doubt, leave the field `null`.
2. **Observation ≠ inference.** Record what the document *states*, not what it *implies* or what is *usual*. Do
   not add "standard" exclusions or "typical" limits that this document does not mention.
3. **Verbatim where it matters.** Amounts, percentages, limits, deductibles, deadlines and territorial scopes are
   copied exactly as printed. Do not round, convert currencies, or normalize formats.
4. **`key_quotes` must be exact.** Each entry in `key_quotes` must be a substring that actually appears in the
   source text (allowing for whitespace/line-break differences). `verify_grounding.py` checks this; a mismatch is
   treated as an extraction bug.
5. **No external knowledge.** Do not use anything you know about the insurer, the product, or the market beyond
   this document. Two different PDFs from the same insurer are extracted independently.
6. **Name the gaps.** If a section is unreadable, ambiguous, or missing, say so in `gaps` (e.g. "pages 12-13 are
   a scanned image with no text layer", "franchise mentioned but amount not stated"). Silence reads as false
   completeness.
7. **Page honesty.** Only cite a page you actually drew the content from. If unsure of the exact page, use the
   nearest certain page and note the uncertainty in `gaps` rather than guessing precisely.
