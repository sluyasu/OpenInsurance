# MCP server

A read-only [MCP](https://modelcontextprotocol.io) server over the wiki. Point any MCP client at it to let an
agent query the insurance knowledge base.

## Install & run

The server is **keyless and read-only**; the dataset is the repo itself. From a clone:

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r mcp/requirements.txt
python mcp/insurance_wiki_mcp.py
```

Or install it as a console script (`pip install .` from the repo root, or from anywhere with
`pip install git+https://github.com/sluyasu/OpenInsurance.git`). When the script does not run
from inside a clone, point it at one:

```bash
INSURANCE_WIKI_REPO=/path/to/OpenInsurance insurance-wiki-mcp
```

## Register with a client

Claude Code one-liner (from the repo root):

```bash
claude mcp add insurance-wiki -- "$(pwd)/.venv/bin/python" "$(pwd)/mcp/insurance_wiki_mcp.py"
```

Or in any MCP client config (e.g. a project `.mcp.json`):

```json
{
  "mcpServers": {
    "insurance-wiki": {
      "command": "/absolute/path/to/OpenInsurance/.venv/bin/python",
      "args": ["/absolute/path/to/OpenInsurance/mcp/insurance_wiki_mcp.py"]
    }
  }
}
```

## Tools

| Tool | Purpose |
|---|---|
| `list_countries()` | Countries covered: products, insurers, branches covered vs taxonomy vs written overviews. |
| `list_branches(country)` | Branches for a country, with mandatory flag and product counts. |
| `search(query, country, type, branch, insurer, limit)` | Search pages by title/content, filterable; announces when results were truncated. |
| `get_page(path)` | Full text of one knowledge page. |
| `get_product(country, insurer_slug, product_name, document_type?, edition?)` | A product's full structured data (coverages, exclusions, ...) + source_url. |
| `get_coverage(country, insurer_slug, product_name, topic, document_type?, edition?)` | **Compact answer to one question**: only the coverages/exclusions relevant to `topic`, with limits, conditions, quotes and pages. |
| `verify_claim(country, insurer_slug, product_name, claim)` | Verbatim excerpts that share the claim's terms, so the calling agent can fact-check its own draft. Retrieval, not judgment. |
| `compare_products(country, product_names, on, insurer_slugs?)` | Compare products on coverages / exclusions / deductibles. |
| `find_overlap(country, product_names, on, insurer_slugs?)` | Flag candidate **duplicate cover** when combining 2+ products (e.g. home + family liability). |
| `get_branch_overview(country, branch)` | The hand-authored branch overview. |

One commercial product usually maps to **several documents** (its general conditions and its IPID share the
name, and several editions can coexist). Tools that take a product name resolve deterministically - general
conditions over summaries, non-superseded, newest edition, then reference order as the final tie-break - and
every response identifies the chosen document (`document_type`, `edition_date`, `reference`, `superseded`):
the single-product tools list the alternatives under `other_documents`, the multi-product tools carry the
identifiers inside each entry. Use `document_type=` / `edition=` on `get_product` / `get_coverage` to pick a
specific one.

## What keeps the answering LLM honest

The LLM consuming these tools is the layer that can hallucinate, so the response shape works against that:

- **Grounding contract + citation line.** Every response carrying product facts starts with a short contract
  ("state only what's here, never invent dates/articles/figures, cite source_url, no advice or ranking");
  single-product responses add a compact CITATION line carrying the real product, insurer, document type,
  edition date (or "not stated"), reference and source_url. The model copies real values instead of
  reconstructing them.
- **Ambiguity is refused, not guessed.** A name matching several distinct products ("Assurance Auto" exists
  at several insurers) returns the candidates instead of silently picking one. An exact name wins over
  products that merely contain it, and the response lists the similar products it skipped.
- **Ties are flagged.** When two documents of the same type carry the same edition date, the response says the
  choice fell back to reference order and points at the alternative.
- **Gaps and caps are explicit.** Superseded documents say so in the citation, empty topic matches say "not
  proof of absence", truncated search results announce the real total.
- **Self-verification.** A chatbot can (and should) re-check its own draft: extract each factual assertion,
  call `verify_claim` with it, and drop or soften anything whose evidence does not literally say it. The
  recommended system-prompt rules for any chatbot built on this server:
  1. State a fact (date, article, amount, deductible, formula) only if it appears in a tool response;
     otherwise say "not stated in the document".
  2. Never pick an insurer for the user: if none is named, ask or list neutrally.
  3. No advice verbs (recommend, choose, drop, best): information, not advice.
  4. End with the `source_url` the tools returned.

## Measured latency

Warm server, in-process, median of 50 runs per tool (Apple silicon, Belgium dataset, 269 documents;
reproduce with `.venv/bin/python tests/bench_tools.py`):

| Tool | median | p95 |
|---|---|---|
| `list_countries` | 0.04 ms | 0.04 ms |
| `list_branches` | 0.04 ms | 0.05 ms |
| `search` (title hit) | 3.4 ms | 3.6 ms |
| `search` (full-text body scan) | 3.6 ms | 3.9 ms |
| `get_page` | 0.02 ms | 0.03 ms |
| `get_product` | 0.24 ms | 0.25 ms |
| `get_coverage` | 1.7 ms | 1.8 ms |
| `verify_claim` | 2.0 ms | 2.2 ms |
| `compare_products` | 1.1 ms | 1.2 ms |
| `find_overlap` | 1.1 ms | 1.1 ms |
| `get_branch_overview` | 0.01 ms | 0.01 ms |

The server reads every file once (index, extractions, page bodies, country metadata, category keywords) and
serves from memory, so no file is re-read per query. The first call after startup pays the cache fill
(tens of ms). In a real chatbot, the user-perceived time is dominated by the LLM's own inference (seconds),
not by these tools: keep the server process warm (any MCP client does) and the tool side is imperceptible.
Full-text search scans the corpus in memory (~3 ms for one country); an inverted index only becomes worth it
with several countries.

## Security & testing

Every product/coverage response carries the `source_url` and a no-advice disclaimer. The server never writes,
and `get_page` only reads text files in the knowledge folders (`wiki/`, `data/`, `_meta/`, `sources/`,
`schema/`, root `*.md`) - never dotfiles, code or git internals, even through path tricks. Without a dataset
(installed via pip/uvx but no clone configured) the server refuses to start with instructions, instead of
serving empty results.

The test suite (`tests/`, run in CI) covers the `get_page` confinement, deterministic document selection,
accent/apostrophe-insensitive matching, ambiguity refusals, honest caps and a smoke test of every tool:

```bash
.venv/bin/pip install pytest && .venv/bin/python -m pytest tests/ -q
```

---

## Overlap detection - and how to build an analysis tool like it

`find_overlap` answers a real question: *"If I take policy A and policy B, which covers am I paying for twice?"*
(the classic case: a **home** policy and a **family-liability** policy both cover civil liability). It's also a
worked example of how to add your own analysis tool to this server. Read it before writing one.

### The design principle: the MCP tool stays a deterministic data provider

The tool does **not** call an LLM and does **not** give advice. It shapes the data so the *calling* agent can
reason. Semantic judgment ("is this really the same cover?") is the agent's job; the tool's job is to surface
strong, deterministic **candidates** with their sources. That keeps the server keyless, reproducible, and honest.

### How `find_overlap` is built (4 pieces)

1. **A controlled vocabulary** - [`schema/coverage_categories.json`](../schema/coverage_categories.json) maps
   insurance concepts (`responsabilite_civile`, `assistance`, `protection_juridique`, `vol`, `incendie`, …) to
   keyword patterns (accent-insensitive, fr/nl). This is *data*, committed and versioned - extend it without
   touching code.
2. **A categorizer** - `_categorize(text)` normalizes a coverage's `name + description` (lowercase, strip
   accents) and returns every category whose keywords appear. Pure string matching, no model.
3. **Grouping** - each product's coverages are tagged; a **candidate overlap** is any category that appears in
   **2 or more** of the products. Groups are returned with the offending items per product, sorted by how many
   products share them.
4. **Honesty** - the response carries the no-advice disclaimer plus a `note`: candidates are heuristic (a shared
   category), must be confirmed against the actual descriptions, and absence of a category is **not** proof of no
   overlap (the taxonomy isn't exhaustive). The tool has good recall and modest precision **by design** - it is a
   lead generator for an agent, not a verdict.

### Worked example

```
find_overlap("be", ["Police habitation pour le propriétaire", "La Police familiale"])
→ candidate_overlaps: Responsabilité civile (both), Dommages / responsabilité animaux,
  Incendie et périls connexes, Vol / vandalisme, Relogement / frais supplémentaires, …
```
The top hit is the true one: home cover (RC immeuble / locataire) and family cover (RC vie privée) both carry
civil liability - a real potential duplication for the policyholder to check.

### How to extend it

- **Improve coverage** without code: add categories or keywords to `coverage_categories.json`, bump its `version`.
- **Higher precision (the deterministic upgrade)**: instead of keyword-matching at query time, tag **one** primary
  `coverage_category` per coverage during extraction/build (a normalization pass), then overlap becomes an exact
  set intersection with no keyword noise. The same `coverage_categories.json` is the seed for that pass.

### How to add a brand-new tool

1. Write a function in `mcp/insurance_wiki_mcp.py` decorated with `@mcp.tool()`. The docstring **is** the tool's
   description the agent sees - state what it does and its limits.
2. Read from `data/<cc>/extracted/*.json` (structured product data) and/or `wiki/` (Markdown) via the existing
   `_extracted()` / `_read_index()` / `_safe_repo_path()` helpers. Never write.
3. Return a string (JSON or Markdown). For anything about coverages, prepend `DISCLAIMER` and include `source_url`.
4. Restart the server; the new tool is exposed automatically. No registration step.

---

## Publishing to the MCP registry (maintainers)

The server is packaged by the root [`pyproject.toml`](../pyproject.toml) (console script
`insurance-wiki-mcp`, PyPI name `openinsurance-wiki-mcp`). To list it on the
[official MCP registry](https://registry.modelcontextprotocol.io) (which the public
directories like PulseMCP ingest automatically):

1. Publish the package to PyPI: `python -m build && twine upload dist/*`.
2. Install the publisher CLI and generate the manifest: `mcp-publisher init`
   (namespace `io.github.sluyasu/*`, package `openinsurance-wiki-mcp`, transport stdio,
   document the `INSURANCE_WIKI_REPO` environment variable).
3. `mcp-publisher login github` then `mcp-publisher publish`.

See https://github.com/modelcontextprotocol/registry for the current publishing guide.

<!-- Registry ownership marker: the official MCP registry validates that the PyPI
     package below belongs to this server name. Do not remove. -->
mcp-name: io.github.sluyasu/openinsurance-wiki
