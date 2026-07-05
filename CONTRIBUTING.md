# Contributing

Everything here is reproducible from committed inputs. There are three kinds of contribution: **add a country**,
**add an insurer**, **add/fix a product**. All three go through the pipeline - you never hand-write a generated
page.

## Ground rules

- Information only - **no advice, no rankings** (see [`CLAUDE.md`](CLAUDE.md) for the full discipline).
- Only scrape **publicly published** documents (general conditions, IPID, product sheets). Respect each site's
  robots and terms; the downloader is polite (rate-limited, identifies itself) - keep it that way.
- Every product fact must trace to a `source_url` + page. No source, no page.

## How the pipeline works

```
sources/<cc>/<insurer>.yml   →  discover.py  →  download.py  →  extract.py  →  build_wiki.py  →  wiki/<cc>/…
   (you write this)             (find PDFs)     (fetch PDFs)     (LLM→MD+JSON)   (assemble)
```

Run it with `make`:

```bash
make setup                                  # once: deps + playwright chromium
make discover download extract build validate COUNTRY=<cc> INSURER=<slug>
```

Only `extract` calls an LLM. Configure it in `.env` (`LLM_PROVIDER`, `LLM_MODEL`, key). It is provider-agnostic -
the prompts in [`extraction-agent/`](extraction-agent/) are identical whatever model you use.

## Add a country

1. **`sources/<cc>/_country.yml`** - regulator, industry body, official languages, and the branch taxonomy
   (slugs + labels + any codes, e.g. life "branche 21/23"). This taxonomy is *data*: nothing in the code is
   country-specific.
2. **`sources/<cc>/<insurer>.yml`** for each insurer (see below).
3. **`wiki/<cc>/`** - hand-author the conceptual layer: `branches/` overviews, `regulations/`, `glossary/`, and
   the MOCs (`00 - <Country> MOC.md`, `branches/00 - Branches MOC.md`). Start pages as `status: stub` if needed.
4. `make all COUNTRY=<cc>`.

## Add an insurer

Create `sources/<cc>/<insurer-slug>.yml`:

```yaml
insurer:
  slug: axa
  name: "AXA Belgium"
  website: "https://www.axa.be"
  segment: particuliers          # particuliers | professionnels | both
languages: [fr, nl]
# Where the public PDFs live. Either list listing pages for discover.py to crawl,
# and/or direct PDF URLs. Map each to a branch slug from _country.yml.
listing_pages:
  - url: "https://www.axa.be/.../conditions-generales"
    branch: auto                 # optional hint; discover can also infer per-link
    lang: fr
pdfs:                            # optional: direct URLs (bypass discovery)
  - url: "https://…/Confort-Auto-CG.pdf"
    branch: auto
    document_type: conditions_generales   # conditions_generales | ipid | conditions_particulieres
    lang: fr
selectors:                       # optional: CSS selectors for discover.py
  pdf_link: "a[href$='.pdf']"
```

Then `make discover download extract build COUNTRY=<cc> INSURER=<slug>`.

## Add or fix a product

- **New product:** add its PDF (a `listing_page` or a direct `pdfs:` entry) to the insurer's source config, then
  `make download extract build`.
- **Fix an extraction error:** never edit the generated `wiki/**/products/*.md`. Either
  (a) fix the value in `data/<cc>/extracted/<insurer>/<product>.json` and `make build`, or
  (b) if the whole extraction is off, improve the prompts in `extraction-agent/`, bump the prompt version, and
  re-run `make extract` (the offending PDF re-extracts because its cache key changed).

## Versions, editions & extensions (the dates method)

Insurers re-issue the same product over time, sell it through several channels, document it in several files,
and extend it with options. The wiki keeps these straight so an old product is never confused with a current one:

- **Edition date is first-class.** Extraction captures `edition_date` from the document; the source config can
  also carry an `edition_date:` (and `superseded: true`) hint per PDF, which flows through as a fallback. Prefer
  the CURRENT edition of a product when choosing what to scrape, and mark older ones `superseded: true`.
- **Product family.** Extraction sets `product_family` (the base product line without the date/variant). At build
  time `pipeline/link.py` groups all documents of the same `(insurer, branch, family)`.
- **Current vs superseded.** Within a family, documents of the **same** `document_type` are ordered by
  `edition_date`; the newest is `edition_status: current`, older ones `superseded` (with a `superseded_by`
  link). This is computed in `link.py`, surfaced in each product page's **Documents liés** section and in the
  frontmatter (`edition_status`, `superseded`).
- **Variants** (e.g. `BNPPF` vs broker) are parallel versions, not editions: capture `variant`, and they are
  cross-linked as related documents (not marked superseded).
- **Extensions / options.** If a document is an option/rider of a base product (not standalone), extraction sets
  `is_extension: true` and `extends: "<base product>"`; the page links to its base, and the base lists its
  extensions. Do not treat an extension as a standalone product.

So: to add a newer edition, just add its PDF (with the newer `edition_date`) and rebuild; the previous edition is
automatically marked superseded and linked. Never delete the old edition, existing policies still reference it.

## Validation gates (must pass)

`make validate` checks: valid frontmatter per note type, no broken `[[wikilinks]]`, no orphan pages, and every
non-stub product page has a `source_url` + page citations. `verify_grounding.py` additionally checks that quoted
text in an extraction actually appears in the source PDF text.
