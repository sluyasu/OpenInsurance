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
- A branch used in a source config MUST exist in `sources/<cc>/_country.yml` (slug + label), or product pages
  link `[[<slug>]]` which doesn't resolve -> validate fails. Add the branch to the taxonomy first.
- Opening the repo in Obsidian creates `.obsidian/` dirs; keep them gitignored and make any "list countries"
  logic skip dot/underscore folders, or a stray `.obsidian` gets treated as a country.
- YAML parses unquoted frontmatter dates into `datetime.date`; `json.dumps(default=str)` when serializing.

## Extraction drift (models vary — normalize, don't fight the schema)
- Different models emit the same data in different shapes. Keep the schema tolerant and coerce to canonical in a
  `normalize()` step, run on every extraction (also in the placement path). Cases seen in the wild:
  list-of-strings instead of list-of-objects (coverages/exclusions/definitions); `key_quotes` under `text`
  instead of `quote`; `duration_and_cancellation.methods` a string not a list; `prescription_period`/`premium`
  as bare strings; `deductibles.per_coverage` a string. Also make the renderer defensive (`_dicts()`), so a bad
  extraction can never crash the build.
- **Filename collisions:** a product's CG and IPID share the same `product_name` -> keying the output JSON on the
  name alone makes the IPID overwrite the CG (silent data loss). Key the file on a hash of `source_url`
  (unique per PDF). Page titles disambiguate separately with a doc-type suffix.
- **Grounding vs typography:** French PDFs use curly apostrophes (U+2019) and a space before `:` (nbsp). Verbatim
  quote matching fails unless you NFKC-normalize, map curly->straight quotes, and also compare whitespace-stripped.

## Versions, editions, extensions
- The same product is re-issued (editions), sold via channels (variants), documented in several files (CG+IPID),
  and extended by options. Capture `edition_date` + `product_family` + `is_extension`/`extends`; `pipeline/link.py`
  groups by family and marks current-vs-superseded by date, cross-linking them. Never conflate an old edition with
  the current one; never delete the old one (existing policies reference it).
- Research agents should carry `edition_date:` and `superseded: true` hints in the source config; the pipeline
  threads them through as fallbacks when the PDF doesn't print a date.

## Fetching quirks (per insurer)
- Not every "PDF" is served as `application/pdf`: NN/AMMA/DKV serve `application/octet-stream` (real `%PDF`).
  Detect PDFs by **magic bytes** (`content[:5] == b'%PDF-'`), not content-type alone.
- Cloudflare-fronted sites (e.g. Allianz) return HTTP 403 to `httpx`/`curl` from datacenter IPs -> the free stack
  can't fetch them; needs a real-browser fetcher (Firecrawl/Playwright). Note the gap, don't fake it.
- AMMA defaults documents to NL; append `?lang=fr`. Baloise's Fastly WAF 406s datacenter curl but serves fine to
  a residential/browser fetcher. Query-string cache-busters (`?t=`, `?rev=`) are load-bearing — keep them.

## Scaling many PDFs (the run harness)
- Extraction is the only paid/LLM step. Drive big batches with a **Workflow fan-out** of subagents (each reads a
  committed prompt file, writes one JSON), then a placement pass. Everything is **resumable**: a helper regenerates
  prompts only for not-yet-extracted PDFs; a session token limit just means re-run the leftovers later. Keep the
  output-file check so an in-flight/finished key is never re-launched (no double spend).

## MCP server (the consumer-facing layer)
- **The tool's output shape governs the answering LLM.** A chatbot on top of this MCP hallucinates when the real
  value isn't salient: bury `edition_date` inside a 75 KB `get_product` JSON and the model reconstructs (invents)
  it. Front-load a compact `CITATION` line (product, insurer, document_type, edition_date-or-"not stated",
  reference, source_url) and prepend a short grounding-contract disclaimer ("state only what's here; never add
  dates/article numbers/figures; cite source_url; no advice/ranking"). Measured on a 11-question set that all
  failed before: 9 pass / 2 warn / 0 fail after, with the invented dates, an FSMA advice slip and an invented
  legal article number all fixed. The knowledge base was already correct; the fix was the tool's presentation.
- **One product = several documents.** A product's CG and IPID share the commercial name, and editions coexist.
  Tools that take a product name must resolve to ONE document deterministically (general conditions over IPID,
  newest edition, non-superseded) and echo which one they chose (`document_type`, `edition_date`, `reference`),
  or the model silently answers from a stale IPID. Add an `insurer_slugs` pin so a generic name ("Assurance
  Auto") doesn't resolve to an arbitrary insurer.
- **Match names accent- and case-insensitively.** Reuse the same `_norm()` on both sides so "vehicules
  automoteurs" finds "Véhicules automoteurs". French product names are full of accents; exact matching dead-ends.
- **Cache read-only data in memory.** The wiki never changes at runtime, so a long-running server should read
  each file once. Memoizing the parsed index, extracted products and normalized page bodies took search from
  ~300 ms to ~1 ms and a full-text miss (whole-corpus body scan) from ~1.2 s to ~5 ms. Tool latency is then
  imperceptible next to LLM inference.
- **`get_page` is an arbitrary-file-read risk.** Confining to "inside the repo" is not enough: a prompt-injected
  agent reading scraped web text can ask for `.env` and exfiltrate keys. Whitelist the knowledge folders
  (`wiki/`, `data/`, `_meta/`, `sources/`, `schema/`, root `*.md`) and reject any path component starting with a dot.
- **Refuse ambiguity, don't guess - but let the exact name win.** Substring matching means "assurance auto"
  hits 9 documents at 5 insurers: tools must return the candidates, not silently pick one. The counter-trap:
  a strict distinct-names guard turns "Confort Auto" into a dead end because its add-ons ("Confort Auto -
  Protection juridique") also match. Rule that works: group name variants of the same product (containment +
  disjoint document types), refuse when several products remain, resolve when exactly one group matches the
  query verbatim, and list the skipped siblings in the response.
- **Ranking needs a total order.** CG > IPID > non-superseded > newest edition still leaves real ties (Yuzzu:
  two different CG issued the same day). Close the sort key with reference/source_url and FLAG the tie in the
  response; otherwise the choice is filesystem order and nobody knows.
- **The discriminating detail hides in `conditions`.** "Off-piste skiing covered only with an instructor"
  lives in a coverage's conditions list, not its name/description: topic matching and evidence retrieval must
  flatten the whole item (conditions, limits, sub_limits, deductible), or the best quote is unreachable.
- **A server installed without its dataset must fail loudly.** Packaged (pip/uvx), the default repo path is
  site-packages: every tool returns [] and the user concludes the wiki is empty. Fail fast at startup with
  the clone + INSURANCE_WIKI_REPO instructions, and have discovery tools return the same guidance.
- **Watch stopwords in claim matching.** "couvre/couvert" appears in virtually every insurance document (and
  inside "recouvrement"), so a verify-style tool that matches on it finds false evidence for any claim. Drop
  near-universal domain words from the term set; keep digits (amounts and dates are the point).

## Before going public
- Run the `pre-public-repo-audit` skill: scan tracked files AND full git history for secrets/PII, and rewrite the
  commit-author email to a GitHub noreply address so a personal email isn't published.
