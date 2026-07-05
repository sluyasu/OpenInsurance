#!/usr/bin/env python
"""openinsurance-wiki MCP server (read-only).

Exposes the wiki to any MCP client: list countries/branches, search, read pages,
get a product's structured data, compare products, read a branch overview. Every
product/coverage response carries the source_url and a no-advice disclaimer.

Run: python mcp/insurance_wiki_mcp.py   (registered in the repo/.mcp.json)
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
DATA = REPO / "data"
SOURCES = REPO / "sources"
SCHEMA = REPO / "schema"

DISCLAIMER = ("[Information only, not advice. Not the insurer's official document, may contain "
              "extraction errors, verify against source_url.]")

mcp = FastMCP("insurance-wiki")


# --- helpers ----------------------------------------------------------------

def _read_index(cc: str) -> list[dict]:
    p = DATA / cc / "index.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else []


def _countries() -> list[str]:
    if not DATA.is_dir():
        return []
    return sorted(d.name for d in DATA.iterdir() if (d / "index.json").is_file())


def _country_meta(cc: str) -> dict:
    p = SOURCES / cc / "_country.yml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.is_file() else {}


def _extracted(cc: str) -> list[tuple[Path, dict]]:
    out = []
    base = DATA / cc / "extracted"
    if base.is_dir():
        for jf in sorted(base.glob("*/*.json")):
            try:
                out.append((jf, json.loads(jf.read_text(encoding="utf-8"))))
            except Exception:
                pass
    return out


def _safe_repo_path(path: str) -> Path | None:
    p = (REPO / path).resolve()
    try:
        p.relative_to(REPO)
    except ValueError:
        return None
    return p if p.is_file() else None


# --- coverage categorization (for the overlap detector) ---------------------

def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).lower()


_CATS = None


def _categories() -> dict:
    global _CATS
    if _CATS is None:
        p = SCHEMA / "coverage_categories.json"
        _CATS = json.loads(p.read_text(encoding="utf-8")).get("categories", {}) if p.is_file() else {}
    return _CATS


def _categorize(text: str) -> list[str]:
    """Return the category keys whose keywords appear in the (accent-normalized) text.
    Heuristic candidate tags, not an authority."""
    t = _norm(text)
    hits = []
    for key, meta in _categories().items():
        if any(_norm(kw) in t for kw in meta.get("keywords", [])):
            hits.append(key)
    return hits


# --- tools ------------------------------------------------------------------

@mcp.tool()
def list_countries() -> str:
    """List countries covered, with page/product/insurer counts."""
    rows = []
    for cc in _countries():
        idx = _read_index(cc)
        meta = _country_meta(cc)
        counts = {}
        for r in idx:
            counts[r.get("type")] = counts.get(r.get("type"), 0) + 1
        rows.append({"country": cc, "name": meta.get("name", cc),
                     "regulator": meta.get("regulator"),
                     "branches": counts.get("branch", 0), "products": counts.get("product", 0),
                     "insurers": counts.get("insurer", 0), "regulations": counts.get("regulation", 0)})
    return json.dumps(rows, ensure_ascii=False, indent=2)


@mcp.tool()
def list_branches(country: str = "be") -> str:
    """List insurance branches for a country with their labels, mandatory flag and product counts."""
    meta = _country_meta(country)
    idx = _read_index(country)
    prod_counts = {}
    for r in idx:
        if r.get("type") == "product" and r.get("branch"):
            prod_counts[r["branch"]] = prod_counts.get(r["branch"], 0) + 1
    rows = []
    for slug, b in meta.get("branches", {}).items():
        rows.append({"branch": slug, "label": b.get("label"), "mandatory": b.get("mandatory"),
                     "code": b.get("code"), "products": prod_counts.get(slug, 0)})
    return json.dumps(rows, ensure_ascii=False, indent=2)


@mcp.tool()
def search(query: str, country: str = "be", type: str = "", branch: str = "",
           insurer: str = "", limit: int = 20) -> str:
    """Search wiki pages by title/branch/insurer and page content. Filter by type
    (product|branch|insurer|regulation|concept|moc), branch slug, insurer slug.
    Returns matches with path, source_url and freshness."""
    q = query.lower().strip()
    terms = [t for t in q.split() if t]
    results = []
    for r in _read_index(country):
        if type and r.get("type") != type:
            continue
        if branch and r.get("branch") != branch:
            continue
        if insurer and (r.get("insurer") or "") != insurer:
            continue
        hay = " ".join(str(r.get(k) or "") for k in ("title", "branch", "insurer", "type")).lower()
        score = sum(1 for t in terms if t in hay)
        if score == 0 and terms:
            fp = _safe_repo_path(r.get("path", ""))
            if fp and all(t in fp.read_text(encoding="utf-8").lower() for t in terms):
                score = 1
        if score or not terms:
            results.append((score, r))
    results.sort(key=lambda x: (-x[0], x[1].get("title", "")))
    out = [{"title": r["title"], "type": r["type"], "branch": r.get("branch"),
            "insurer": r.get("insurer"), "path": r["path"], "source_url": r.get("source_url"),
            "freshness": r.get("freshness")} for _, r in results[:limit]]
    return json.dumps(out, ensure_ascii=False, indent=2)


@mcp.tool()
def get_page(path: str) -> str:
    """Return the full Markdown of one wiki page by its repo-relative path (from search results)."""
    p = _safe_repo_path(path)
    if not p:
        return f"Not found or outside repo: {path}"
    return p.read_text(encoding="utf-8")


@mcp.tool()
def get_product(country: str, insurer_slug: str, product_name: str) -> str:
    """Return a product's structured data (coverages, exclusions, deductibles, etc.) as JSON,
    plus its source_url. `product_name` is matched case-insensitively (substring)."""
    want = product_name.lower().strip()
    matches = []
    for jf, obj in _extracted(country):
        if obj.get("insurer_slug") != insurer_slug:
            continue
        if want in (obj.get("product_name") or "").lower() or want in jf.stem.lower():
            matches.append(obj)
    if not matches:
        return f"{DISCLAIMER}\nNo product matching '{product_name}' for insurer '{insurer_slug}' in {country}."
    if len(matches) > 1:
        names = [m.get("product_name") for m in matches]
        return f"Multiple matches, refine product_name: {json.dumps(names, ensure_ascii=False)}"
    return DISCLAIMER + "\n" + json.dumps(matches[0], ensure_ascii=False, indent=2)


@mcp.tool()
def compare_products(country: str, product_names: list[str], on: str = "coverages") -> str:
    """Compare 2+ products side by side on one dimension: coverages | exclusions | deductibles.
    Each name is matched case-insensitively against extracted product names."""
    if on not in ("coverages", "exclusions", "deductibles"):
        return "on must be one of: coverages | exclusions | deductibles"
    chosen = []
    allp = _extracted(country)
    for name in product_names:
        w = name.lower().strip()
        m = [obj for _, obj in allp if w in (obj.get("product_name") or "").lower()]
        if m:
            chosen.append(m[0])
    if len(chosen) < 2:
        return f"{DISCLAIMER}\nNeed at least 2 matching products; matched {len(chosen)}."
    result = {"on": on, "products": []}
    for obj in chosen:
        entry = {"product_name": obj.get("product_name"), "insurer": obj.get("insurer_name"),
                 "source_url": obj.get("source_url")}
        if on == "deductibles":
            entry["deductibles"] = obj.get("deductibles")
        else:
            entry[on] = [c.get("name") for c in (obj.get(on) or [])]
        result["products"].append(entry)
    return DISCLAIMER + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def find_overlap(country: str, product_names: list[str], on: str = "coverages") -> str:
    """Flag CANDIDATE duplicate cover when combining 2+ products (e.g. a home policy + a
    family-liability policy). Each product's coverages (or exclusions) are tagged with a
    controlled category (schema/coverage_categories.json); a candidate overlap is a
    category present in 2+ of the products. Deterministic + heuristic: it surfaces likely
    duplicates for an agent to confirm against the actual descriptions. It does not advise
    or rank, and can miss overlaps the taxonomy doesn't yet cover."""
    from collections import defaultdict
    if on not in ("coverages", "exclusions"):
        return "on must be 'coverages' or 'exclusions'"
    allp = _extracted(country)
    chosen = []
    for name in product_names:
        w = name.lower().strip()
        m = [o for _, o in allp if w in (o.get("product_name") or "").lower()]
        if m:
            chosen.append(m[0])
    if len(chosen) < 2:
        return f"{DISCLAIMER}\nNeed at least 2 matching products; matched {len(chosen)}."
    labels = {k: v.get("label", k) for k, v in _categories().items()}
    cat_items = defaultdict(list)
    per_product = []
    for o in chosen:
        pname = o.get("product_name")
        items = []
        for it in (o.get(on) or []):
            if not isinstance(it, dict):
                continue
            cats = _categorize(f"{it.get('name','')} {it.get('description','')}")
            items.append({"name": it.get("name"), "categories": [labels.get(c, c) for c in cats]})
            for c in cats:
                cat_items[c].append({"product": pname, "item": it.get("name")})
        per_product.append({"product_name": pname, "insurer": o.get("insurer_name"),
                            "branch": o.get("branch"), "source_url": o.get("source_url"), on: items})
    overlaps = []
    for c, entries in cat_items.items():
        if len({e["product"] for e in entries}) >= 2:
            overlaps.append({"category": labels.get(c, c),
                             "products": sorted({e["product"] for e in entries}), "items": entries})
    overlaps.sort(key=lambda x: -len(x["products"]))
    result = {"on": on, "products": per_product, "candidate_overlaps": overlaps,
              "note": ("candidate_overlaps are heuristic (a shared controlled category); confirm each "
                       "against the actual coverage descriptions. Absence of a category is not proof of "
                       "no overlap - the taxonomy is not exhaustive.")}
    return DISCLAIMER + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def get_branch_overview(country: str, branch: str) -> str:
    """Return the hand-authored overview page for a branch (by slug or label)."""
    meta = _country_meta(country)
    label = meta.get("branches", {}).get(branch, {}).get("label", branch)
    for cand in (label, branch):
        p = WIKI / country / "branches" / f"{cand}.md"
        if p.is_file():
            return p.read_text(encoding="utf-8")
    return f"No branch overview for '{branch}' in {country}."


if __name__ == "__main__":
    mcp.run()
