# Lessons & gotchas

Running notes on things that bit us or that a contributor should know. Append as you learn.

## Scraping / download
- Insurer PDF links are often on JS-rendered "documents légaux" pages → `discover.py` needs the Playwright
  fallback, not just `httpx`. Direct CDN PDF URLs, once found, download fine over `httpx`.
- Be polite: rate-limit, set a descriptive User-Agent, back off on 429/403. Some insurer sites sit behind a WAF
  that bans rapid parallel hits from one IP - keep discovery serial per host.
- Same product often exists in FR and NL editions - treat them as separate PDFs (different `lang`), link them.

## PDF text extraction
- PyMuPDF (`fitz`) is the primary; `pdfplumber` is a fallback for table-heavy conditions. Keep a page map so the
  extractor can cite page numbers.
- Some general-conditions PDFs are scanned images → no text layer. Flag these (they need OCR, out of scope for
  the free path) rather than silently producing an empty extraction.

## LLM extraction
- The extraction cache key = PDF sha256 + prompt version + schema version. Bump the prompt version when you edit
  `extraction-agent/` prompts, or edited prompts won't take effect on already-extracted PDFs.
- Long conditions PDFs can exceed a model's output budget → the extractor chunks by section and stitches, so a
  single page's content is never split mid-block.
- Ground everything: `verify_grounding.py` flags any quoted span that isn't in the source text. Treat flags as
  extraction bugs, not noise.

## Wiki / build
- Generated vs hand-authored folders are disjoint - the generator only writes `products/` and `insurers/`. If a
  hand-authored page ever shows a machine diff, something wrote to the wrong subtree.
- `build_wiki.py` is resume-safe (`write_if_changed`): a no-op rebuild must produce zero diff. If it doesn't,
  a nondeterministic ordering crept into the generator (sort everything).
