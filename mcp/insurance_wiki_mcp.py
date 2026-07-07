#!/usr/bin/env python
"""openinsurance-wiki MCP server (read-only).

Exposes the wiki to any MCP client: list countries/branches, search, read pages,
get a product's structured data, compare products, read a branch overview. Every
product/coverage response carries the source_url and a no-advice disclaimer.

Run: python mcp/insurance_wiki_mcp.py   (registered in the repo/.mcp.json)
"""

from __future__ import annotations

import json
import os
import re
import unicodedata
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

# Default: the server file lives in <repo>/mcp/. When installed as a package
# (pip/uvx), point INSURANCE_WIKI_REPO at a clone of the repo instead.
REPO = Path(os.environ.get("INSURANCE_WIKI_REPO")
            or Path(__file__).resolve().parent.parent).resolve()
WIKI = REPO / "wiki"
DATA = REPO / "data"
SOURCES = REPO / "sources"
SCHEMA = REPO / "schema"

DISCLAIMER = (
    "[GROUNDING CONTRACT for the answering assistant: use ONLY facts present in this response. "
    "Quote edition dates, references, limits, deductibles and wording exactly as shown; if a value is "
    "'not stated', say it is not stated. Do NOT add article numbers, dates, figures, formulas or product "
    "names that are not present here. Always cite the source_url. Do not advise, recommend or rank insurers. "
    "This is a factual extraction, not the insurer's official document, and may contain errors "
    "- verify against source_url.]")


def _citation(obj: dict) -> str:
    """A compact, front-loaded citation line so the answering model quotes the real
    edition/reference/source instead of reconstructing (and inventing) them."""
    ed = obj.get("edition_date") or "not stated in document"
    ref = obj.get("reference") or "not stated"
    return ("CITATION (state these exactly, do not invent): "
            f"product={obj.get('product_name')!r} | insurer={obj.get('insurer_name')} "
            f"({obj.get('insurer_slug')}) | document_type={obj.get('document_type')} "
            f"| edition_date={ed} | reference={ref} | source_url={obj.get('source_url')}")

mcp = FastMCP("insurance-wiki")


# --- helpers ----------------------------------------------------------------

# The wiki is read-only at runtime, so parsed data is cached in memory. A
# long-running server reads each file once, not once per query.
_INDEX_CACHE: dict[str, list[dict]] = {}
_EXTRACTED_CACHE: dict[str, list] = {}


def _read_index(cc: str) -> list[dict]:
    if cc not in _INDEX_CACHE:
        p = DATA / cc / "index.json"
        _INDEX_CACHE[cc] = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else []
    return _INDEX_CACHE[cc]


def _countries() -> list[str]:
    if not DATA.is_dir():
        return []
    return sorted(d.name for d in DATA.iterdir() if (d / "index.json").is_file())


def _country_meta(cc: str) -> dict:
    p = SOURCES / cc / "_country.yml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.is_file() else {}


def _extracted(cc: str) -> list[tuple[Path, dict]]:
    if cc not in _EXTRACTED_CACHE:
        out = []
        base = DATA / cc / "extracted"
        if base.is_dir():
            for jf in sorted(base.glob("*/*.json")):
                try:
                    out.append((jf, json.loads(jf.read_text(encoding="utf-8"))))
                except Exception:
                    pass
        _EXTRACTED_CACHE[cc] = out
    return _EXTRACTED_CACHE[cc]


_PAGE_TEXT_CACHE: dict[str, str] = {}


def _page_text_norm(path: str) -> str:
    """Accent/case-normalized body of a wiki page, cached, for full-text search."""
    if path not in _PAGE_TEXT_CACHE:
        fp = _safe_repo_path(path)
        _PAGE_TEXT_CACHE[path] = _norm(fp.read_text(encoding="utf-8")) if fp else ""
    return _PAGE_TEXT_CACHE[path]


# Directories the server may read from. Everything else (.env, pipeline code, git
# internals) stays out of reach even if a prompt-injected client asks for it.
_READABLE_ROOTS = ("wiki", "data", "_meta", "sources", "schema")


def _safe_repo_path(path: str) -> Path | None:
    p = (REPO / path).resolve()
    try:
        rel = p.relative_to(REPO)
    except ValueError:
        return None
    if any(part.startswith(".") for part in rel.parts):
        return None
    if len(rel.parts) == 1:
        if p.suffix.lower() != ".md":
            return None
    elif rel.parts[0] not in _READABLE_ROOTS:
        return None
    return p if p.is_file() else None


# --- document selection ------------------------------------------------------
# One commercial product usually has several extracted documents (CG + IPID, several
# editions). Tools that take a product name resolve to ONE document deterministically:
# general conditions over summaries, non-superseded over superseded, newest edition
# last - and always say which document was chosen.

_DOC_PREF = {"conditions_generales": 0, "conditions_particulieres": 1,
             "conditions_tarifaires": 2, "ipid": 3}


def _edition_key(ed) -> tuple[int, int, int]:
    """Sortable (year, month, day) from an edition date as printed in the source PDF
    (04.2025, 2026-05-12, 12/05/2026, 01042026, 2019, ...). (0,0,0) when unparseable."""
    if not ed:
        return (0, 0, 0)
    s = str(ed).strip()
    m = re.fullmatch(r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})", s)   # YYYY-MM-DD
    if m:
        y, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return (y, a, b) if a <= 12 else (y, b, a)
    m = re.fullmatch(r"(\d{1,2})[-./](\d{1,2})[-./](\d{4})", s)   # DD-MM-YYYY
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if mo > 12 and d <= 12:
            d, mo = mo, d
        return (y, mo, d)
    m = re.fullmatch(r"(\d{1,2})[-./](\d{4})", s)                 # MM-YYYY
    if m:
        return (int(m.group(2)), int(m.group(1)), 0)
    m = re.fullmatch(r"(\d{4})[-./](\d{1,2})", s)                 # YYYY-MM
    if m:
        return (int(m.group(1)), int(m.group(2)), 0)
    m = re.fullmatch(r"(\d{2})(\d{2})(\d{4})", s)                 # DDMMYYYY
    if m:
        return (int(m.group(3)), int(m.group(2)), int(m.group(1)))
    m = re.fullmatch(r"(\d{1,2})[./](\d{2})", s)                  # MM.YY
    if m and int(m.group(1)) <= 12:
        return (2000 + int(m.group(2)), int(m.group(1)), 0)
    m = re.search(r"\b(19|20)\d{2}\b", s)                         # bare year somewhere
    if m:
        return (int(m.group(0)), 0, 0)
    return (0, 0, 0)


def _pick_best(matches: list[dict]) -> tuple[dict, list[dict]]:
    """(chosen, alternatives) for one product's documents."""
    ranked = sorted(matches, key=lambda o: (
        _DOC_PREF.get(o.get("document_type"), 9),
        1 if o.get("superseded") else 0,
        tuple(-x for x in _edition_key(o.get("edition_date"))),
    ))
    return ranked[0], ranked[1:]


def _doc_meta(obj: dict) -> dict:
    """The identifiers that tell two same-named documents apart."""
    return {"product_name": obj.get("product_name"), "insurer_slug": obj.get("insurer_slug"),
            "document_type": obj.get("document_type"), "edition_date": obj.get("edition_date"),
            "reference": obj.get("reference"), "superseded": obj.get("superseded"),
            "source_url": obj.get("source_url")}


def _resolve_product(allp: list[tuple[Path, dict]], name: str,
                     insurer: str = "") -> tuple[dict | None, list[dict]]:
    """Match a product name (case- and accent-insensitive substring), optionally within
    one insurer, and pick the best document. Returns (chosen | None, alternatives)."""
    w = _norm(name)
    m = [o for _, o in allp
         if w in _norm(o.get("product_name") or "")
         and (not insurer or o.get("insurer_slug") == insurer)]
    if not m:
        return None, []
    return _pick_best(m)


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
    terms = [t for t in _norm(query).split() if t]
    results = []
    for r in _read_index(country):
        if type and r.get("type") != type:
            continue
        if branch and r.get("branch") != branch:
            continue
        if insurer and (r.get("insurer") or "") != insurer:
            continue
        hay = _norm(" ".join(str(r.get(k) or "") for k in ("title", "branch", "insurer", "type")))
        score = sum(1 for t in terms if t in hay)
        if score == 0 and terms:
            body = _page_text_norm(r.get("path", ""))
            if body and all(t in body for t in terms):
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
def get_product(country: str, insurer_slug: str, product_name: str,
                document_type: str = "", edition: str = "") -> str:
    """Return a product's structured data (coverages, exclusions, deductibles, etc.) as JSON,
    plus its source_url. `product_name` is matched case-insensitively (substring).
    Optional filters: document_type (conditions_generales | ipid | conditions_particulieres |
    conditions_tarifaires) and edition (substring of the edition_date, e.g. '2026').
    When one product has several documents (e.g. its CG and its IPID share the commercial
    name), the general conditions with the newest edition are returned and the other
    documents are listed under `other_documents`."""
    want = _norm(product_name)
    matches = []
    for jf, obj in _extracted(country):
        if obj.get("insurer_slug") != insurer_slug:
            continue
        if want not in _norm(obj.get("product_name") or "") and want not in _norm(jf.stem):
            continue
        if document_type and obj.get("document_type") != document_type:
            continue
        if edition and edition not in str(obj.get("edition_date") or ""):
            continue
        matches.append(obj)
    if not matches:
        return f"{DISCLAIMER}\nNo product matching '{product_name}' for insurer '{insurer_slug}' in {country}."
    names = {(m.get("product_name") or "").lower() for m in matches}
    if len(names) > 1:
        return ("Multiple distinct products match; refine product_name or filter by "
                "document_type/edition:\n"
                + json.dumps([_doc_meta(m) for m in matches], ensure_ascii=False, indent=2))
    chosen, others = _pick_best(matches)
    payload = dict(chosen)
    head = DISCLAIMER + "\n" + _citation(chosen)
    if others:
        payload["other_documents"] = [_doc_meta(o) for o in others]
        head += (f"\n[{len(others)} other document(s) for this product under `other_documents`.]")
    return head + "\n" + json.dumps(payload, ensure_ascii=False, indent=2)


@mcp.tool()
def compare_products(country: str, product_names: list[str], on: str = "coverages",
                     insurer_slugs: list[str] | None = None) -> str:
    """Compare 2+ products side by side on one dimension: coverages | exclusions | deductibles.
    Each name is matched case-insensitively against extracted product names; pass
    insurer_slugs (same length/order as product_names) to pin each name to one insurer.
    For each name the best document is selected (general conditions over IPID, newest
    edition) and identified in the response."""
    if on not in ("coverages", "exclusions", "deductibles"):
        return "on must be one of: coverages | exclusions | deductibles"
    if insurer_slugs and len(insurer_slugs) != len(product_names):
        return "insurer_slugs must have the same length/order as product_names"
    allp = _extracted(country)
    chosen, unmatched = [], []
    for i, name in enumerate(product_names):
        obj, others = _resolve_product(allp, name, insurer_slugs[i] if insurer_slugs else "")
        if obj:
            chosen.append((obj, len(others)))
        else:
            unmatched.append(name)
    if len(chosen) < 2:
        return (f"{DISCLAIMER}\nNeed at least 2 matching products; matched {len(chosen)}."
                + (f" Unmatched: {unmatched}" if unmatched else ""))
    result = {"on": on, "products": []}
    if unmatched:
        result["unmatched"] = unmatched
    for obj, n_alt in chosen:
        entry = {"product_name": obj.get("product_name"), "insurer": obj.get("insurer_name"),
                 "insurer_slug": obj.get("insurer_slug"),
                 "document_type": obj.get("document_type"),
                 "edition_date": obj.get("edition_date"), "reference": obj.get("reference"),
                 "other_documents_exist": n_alt, "source_url": obj.get("source_url")}
        if on == "deductibles":
            entry["deductibles"] = obj.get("deductibles")
        else:
            entry[on] = [c.get("name") for c in (obj.get(on) or [])]
        result["products"].append(entry)
    return DISCLAIMER + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def find_overlap(country: str, product_names: list[str], on: str = "coverages",
                 insurer_slugs: list[str] | None = None) -> str:
    """Flag CANDIDATE duplicate cover when combining 2+ products (e.g. a home policy + a
    family-liability policy). Each product's coverages (or exclusions) are tagged with a
    controlled category (schema/coverage_categories.json); a candidate overlap is a
    category present in 2+ of the products. Deterministic + heuristic: it surfaces likely
    duplicates for an agent to confirm against the actual descriptions. It does not advise
    or rank, and can miss overlaps the taxonomy doesn't yet cover. Pass insurer_slugs
    (same length/order as product_names) to pin each name to one insurer; the best
    document per name is selected (general conditions over IPID, newest edition)."""
    from collections import defaultdict
    if on not in ("coverages", "exclusions"):
        return "on must be 'coverages' or 'exclusions'"
    if insurer_slugs and len(insurer_slugs) != len(product_names):
        return "insurer_slugs must have the same length/order as product_names"
    allp = _extracted(country)
    chosen = []
    for i, name in enumerate(product_names):
        o, _others = _resolve_product(allp, name, insurer_slugs[i] if insurer_slugs else "")
        if o:
            chosen.append(o)
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
                            "branch": o.get("branch"), "document_type": o.get("document_type"),
                            "edition_date": o.get("edition_date"),
                            "source_url": o.get("source_url"), on: items})
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


def main() -> None:
    """Console entry point (`insurance-wiki-mcp` once installed)."""
    mcp.run()


if __name__ == "__main__":
    main()
