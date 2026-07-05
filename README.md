# openinsurance-wiki

> A self-sufficient, open-source **wiki of every insurance product in a country** - built by scraping public
> insurer documents and extracting them into rich, source-cited Markdown that any AI agent can read.

Not a chatbot. Not a RAG black box. A **transparent, reproducible knowledge base**: the repo contains the whole
chain - it finds the insurers' public general-conditions PDFs, downloads them, and turns each one into a faithful
Markdown page that preserves the maximum of what the PDF actually says, with a citation back to the source.

**Belgium** is the first country. The structure is country-agnostic - adding a country is a documented recipe.

---

## Why this exists

Insurance products are documented in dense PDFs scattered across dozens of insurer websites. There is no neutral,
machine-readable, navigable map of what actually exists in a national market. This project builds one - as a
public good, and in a form an AI agent can plug into.

Three things make it different:

1. **Self-sufficient & reproducible.** Clone it, add your own LLM key, run `make all`. It scrapes, downloads and
   extracts from scratch. No hidden datasets - every input is committed, every output is regenerable.
2. **Transparent extraction.** The exact prompt sent to the LLM is a file in this repo
   ([`extraction-agent/`](extraction-agent/)), not buried in code. You can read precisely what the model was
   asked, and run the identical extraction **with your own model** (Claude, Gemini, GPT, or a local model).
3. **Grounded & cited.** Every product page traces back to the source PDF and cites page numbers. Quotes are
   verified against the raw text. If it isn't in the document, it isn't on the page.

---

## What's in the wiki

Per country (`wiki/be/`):

| Folder | What | How it's made |
|---|---|---|
| `products/<insurer>/` | One rich page per insurance product (general conditions / IPID) | **Generated** from the PDFs |
| `insurers/` | One page per insurer, aggregating its products | **Generated** |
| `branches/` | Overview of each line of insurance (auto, home, liability…) | **Hand-authored** |
| `regulations/` | The regulator and key laws (FSMA, mandatory RC auto, cat-nat…) | **Hand-authored** |
| `glossary/` | Country-specific terms (bonus-malus, franchise, Branche 21/23…) | **Hand-authored** |

Generated and hand-authored pages live in **separate folders** and never collide: you fix a fact by editing the
extraction data and rebuilding, never by editing a generated page.

Every page is Obsidian-compatible Markdown with YAML frontmatter and `[[wikilinks]]` - open the repo as an
Obsidian vault to browse the graph, or read it straight on GitHub.

---

## Plug it into any agent - three tiers

1. **Plain Markdown + manifest** - any file/git-capable agent (Claude Code, Cursor, an SDK agent) reads the
   `.md` files directly. [`AGENTS.md`](AGENTS.md) is a generated index (note types, per-country counts, a flat
   table with `path`, `source_url`, `freshness`) so an agent can navigate without guessing.
2. **MCP server** - [`mcp/insurance_wiki_mcp.py`](mcp/) exposes `list_branches`, `search`, `get_product`,
   `compare_products`, `find_overlap`, … over the wiki. Point any MCP client at it. This is where analysis lives:
   compare products/insurers, read exclusions side by side, and detect **duplicate cover** when combining two
   policies (e.g. home + family liability). See [`mcp/README.md`](mcp/README.md) for how the overlap tool is built
   and how to add your own.
3. **Machine-readable data** - `data/<cc>/` holds the structured JSON behind each page, validated against
   [`schema/`](schema/). Agents that want raw structure skip the Markdown entirely.

---

## Quickstart

```bash
git clone <this-repo> && cd openinsurance-wiki
make setup                      # deps + playwright chromium (free stack, no paid scraping dependency)
cp .env.example .env            # set LLM_PROVIDER + your API key (any provider)

# Reproduce a slice end-to-end:
make download COUNTRY=be INSURER=<slug>   # fetch the public PDFs
make extract  COUNTRY=be INSURER=<slug>   # PDFs -> rich Markdown + JSON (uses YOUR model)
make build    COUNTRY=be                  # assemble the wiki
make validate COUNTRY=be                  # citation / wikilink / frontmatter gates

# ...or the whole chain:
make all COUNTRY=be
```

The extraction step is the only one that calls an LLM. Scraping and download use a free stack (`httpx` +
`Playwright`) and need no API key.

---

## How the pipeline works

```
sources/be/<insurer>.yml     (committed: where the public PDFs live)
        │  discover.py   crawl listing pages (httpx, Playwright fallback)
        ▼
data/be/pdfs/…               (downloaded; gitignored - regenerable; manifest.json committed)
        │  extract.py    PyMuPDF text  ──►  LLM (extraction-agent/ prompts)  ──►  MD + JSON
        ▼
data/be/extracted/…          (rich Markdown + structured JSON, page-cited)
        │  build_wiki.py
        ▼
wiki/be/…                    (the browsable, agent-readable knowledge base)
```

Details: [`CONTRIBUTING.md`](CONTRIBUTING.md) (how to add a country / insurer / product) and
[`extraction-agent/`](extraction-agent/) (the exact prompts).

---

## Add a country

1. `sources/<cc>/_country.yml` - regulator, languages, branch taxonomy.
2. `sources/<cc>/<insurer>.yml` - where each insurer's public PDFs live.
3. `wiki/<cc>/` - hand-author branch/regulation/glossary overviews (or start them as stubs).
4. `make all COUNTRY=<cc>`.

Nothing in the code or schema is Belgium-specific - the taxonomy is data, not structure.

---

## Licensing & provenance

Dual-licensed: **code** ([pipeline/](pipeline/), [mcp/](mcp/), adapters, schema) under **MIT**; **content**
(`wiki/`, extracted data, prompts, sources) under **CC-BY-4.0**. See [`LICENSE`](LICENSE) and
[`LICENSE-CONTENT`](LICENSE-CONTENT).

Product pages are a factual extraction from insurers' **publicly published** documents, attributed to each source
PDF. **They are not the insurers' official documents** and may contain extraction errors - always verify against
the cited `source_url`. This project provides **information, not personalized insurance advice**.
