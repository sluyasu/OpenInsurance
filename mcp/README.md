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
| `list_countries()` | Countries covered, with counts. |
| `list_branches(country)` | Branches for a country, with mandatory flag and product counts. |
| `search(query, country, type, branch, insurer, limit)` | Search pages by title/content, filterable. |
| `get_page(path)` | Full Markdown of one page. |
| `get_product(country, insurer_slug, product_name, document_type?, edition?)` | A product's structured data (coverages, exclusions, ...) + source_url. |
| `compare_products(country, product_names, on, insurer_slugs?)` | Compare products on coverages / exclusions / deductibles. |
| `find_overlap(country, product_names, on, insurer_slugs?)` | Flag candidate **duplicate cover** when combining 2+ products (e.g. home + family liability). |
| `get_branch_overview(country, branch)` | The hand-authored branch overview. |

One commercial product usually maps to **several documents** (its general conditions and its IPID share the
name, and several editions can coexist). Tools that take a product name resolve deterministically - general
conditions over summaries, non-superseded, newest edition - and every response says which document was chosen
(`document_type`, `edition_date`, `reference`) with the alternatives listed. Use `document_type=` / `edition=`
on `get_product` to pick a specific one.

Every product/coverage response carries the `source_url` and a no-advice disclaimer. The server never writes,
and `get_page` only reads the knowledge folders (`wiki/`, `data/`, `_meta/`, `sources/`, `schema/`, root
`*.md`) - never dotfiles or code.

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
→ candidate_overlaps: Responsabilité civile (both), Protection juridique (both), Incendie, Vol, Relogement, …
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
