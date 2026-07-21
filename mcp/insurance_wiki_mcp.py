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
import sys
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
    sup = " | superseded=True (an older edition; a newer one exists)" if obj.get("superseded") else ""
    # The age belongs on the primary path, not only in candidate listings: asking for one
    # product by name is how an agent meets a 2010 edition, and without this the answer
    # reads exactly like a current one. It reports age and stops there, because whether
    # the product is still sold is not in the document.
    age = _edition_age_years(obj)
    old = ""
    if age is not None and age >= OLD_EDITION_YEARS and not obj.get("superseded"):
        old = (f" | edition_age_years={age} (this edition was {age} years old when "
               "collected; the insurer was still publishing it, but whether the product "
               "is still sold is NOT stated in the document - do not assert either way)")
    return ("CITATION (state these exactly, do not invent): "
            f"product={obj.get('product_name')!r} | insurer={obj.get('insurer_name')} "
            f"({obj.get('insurer_slug')}) | document_type={obj.get('document_type')} "
            f"| edition_date={ed} | reference={ref}{sup}{old} | source_url={obj.get('source_url')}")

mcp = FastMCP("insurance-wiki")


# --- helpers ----------------------------------------------------------------

# The wiki is read-only at runtime, so parsed data is cached in memory. A
# long-running server reads each file once, not once per query.
_INDEX_CACHE: dict[str, list[dict]] = {}
_EXTRACTED_CACHE: dict[str, list] = {}


def _read_index(cc: str) -> list[dict]:
    if cc not in _INDEX_CACHE:
        p = DATA / cc / "index.json"
        try:
            _INDEX_CACHE[cc] = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else []
        except json.JSONDecodeError as e:
            raise ValueError(f"Corrupt index file {p}: {e}. Rebuild it with "
                             "`python pipeline/build_index.py --country " + cc + "`.") from e
    return _INDEX_CACHE[cc]


_COUNTRIES_CACHE: list[str] | None = None


def _countries() -> list[str]:
    global _COUNTRIES_CACHE
    if _COUNTRIES_CACHE is None:
        _COUNTRIES_CACHE = (sorted(d.name for d in DATA.iterdir()
                                   if (d / "index.json").is_file())
                            if DATA.is_dir() else [])
    return _COUNTRIES_CACHE


_COUNTRY_META_CACHE: dict[str, dict] = {}


def _country_meta(cc: str) -> dict:
    if cc not in _COUNTRY_META_CACHE:
        p = SOURCES / cc / "_country.yml"
        _COUNTRY_META_CACHE[cc] = (yaml.safe_load(p.read_text(encoding="utf-8")) or {}) \
            if p.is_file() else {}
    return _COUNTRY_META_CACHE[cc]


_RAW_PAGE_CACHE: dict[str, str] = {}


def _read_page(p: Path) -> str:
    """Raw text of a knowledge page, read once per server lifetime."""
    key = str(p)
    if key not in _RAW_PAGE_CACHE:
        _RAW_PAGE_CACHE[key] = p.read_text(encoding="utf-8")
    return _RAW_PAGE_CACHE[key]


# Guidance instead of a silent empty server: an installed (pip/uvx) copy that can't
# see a dataset is the most common misconfiguration.
_NO_DATASET = (f"No dataset found under {REPO}. This server reads the openinsurance-wiki "
               "repository itself: run it from inside a clone, or set INSURANCE_WIKI_REPO "
               "to the path of one (git clone https://github.com/sluyasu/OpenInsurance.git).")


def _no_data(cc: str) -> str | None:
    """A message explaining an empty result that is a setup problem, not a data fact."""
    if _extracted(cc):
        return None
    if not _countries():
        return _NO_DATASET
    return (f"No extracted data for country '{cc}'. Covered countries: "
            + ", ".join(_countries()) + ". Use list_countries.")


def _extracted(cc: str) -> list[tuple[Path, dict]]:
    if cc not in _EXTRACTED_CACHE:
        out = []
        base = DATA / cc / "extracted"
        if base.is_dir():
            for jf in sorted(base.glob("*/*.json")):
                try:
                    out.append((jf, json.loads(jf.read_text(encoding="utf-8"))))
                except Exception as e:
                    # Serve the rest, but never silently: a skipped file is a
                    # product that vanished from every tool.
                    print(f"[insurance-wiki-mcp] skipping unreadable {jf}: {e}",
                          file=sys.stderr)
        _EXTRACTED_CACHE[cc] = out
    return _EXTRACTED_CACHE[cc]


_PAGE_TEXT_CACHE: dict[str, str] = {}


def _page_text_norm(path: str) -> str:
    """Accent/case-normalized body of a wiki page, cached, for full-text search."""
    if path not in _PAGE_TEXT_CACHE:
        fp = _safe_repo_path(path)
        _PAGE_TEXT_CACHE[path] = _norm(_read_page(fp)) if fp else ""
    return _PAGE_TEXT_CACHE[path]


_HAY_CACHE: dict[str, list[str]] = {}


def _index_hay(cc: str) -> list[str]:
    """Normalized title/branch/insurer/type haystack per index row, aligned with
    _read_index(cc). Normalizing 200 rows per query was the search floor."""
    if cc not in _HAY_CACHE:
        _HAY_CACHE[cc] = [
            _norm(" ".join(str(r.get(k) or "") for k in ("title", "branch", "insurer", "type")))
            for r in _read_index(cc)]
    return _HAY_CACHE[cc]


# Directories the server may read from. Everything else (.env, pipeline code, git
# internals) stays out of reach even if a prompt-injected client asks for it.
# Text formats only: data/ also holds downloaded PDFs on a working machine.
_READABLE_ROOTS = ("wiki", "data", "_meta", "sources", "schema")
_READABLE_SUFFIXES = (".md", ".json", ".yml", ".yaml", ".txt", ".csv")


def _safe_repo_path(path: str) -> Path | None:
    p = (REPO / path).resolve()
    try:
        rel = p.relative_to(REPO)
    except ValueError:
        return None
    if any(part.startswith(".") for part in rel.parts):
        return None
    if p.suffix.lower() not in _READABLE_SUFFIXES:
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
    if re.fullmatch(r"\d{8}", s):                                 # YYYYMMDD / DDMMYYYY
        if s[:2] in ("19", "20") and int(s[4:6]) <= 12:
            return (int(s[:4]), int(s[4:6]), int(s[6:8]))
        if int(s[2:4]) <= 12:
            return (int(s[4:8]), int(s[2:4]), int(s[:2]))
        return (0, 0, 0)
    if re.fullmatch(r"\d{6}", s):                                 # YYYYMM / MMYYYY
        if s[:2] in ("19", "20") and int(s[4:6]) <= 12:
            return (int(s[:4]), int(s[4:6]), 0)
        if int(s[:2]) <= 12 and s[2:4] in ("19", "20"):
            return (int(s[2:6]), int(s[:2]), 0)
        return (0, 0, 0)
    m = re.fullmatch(r"(\d{1,2})[./](\d{2})", s)                  # MM.YY
    if m and int(m.group(1)) <= 12:
        return (2000 + int(m.group(2)), int(m.group(1)), 0)
    if re.fullmatch(r"\d{4}", s) and s[:2] not in ("19", "20") and int(s[:2]) <= 12:
        return (2000 + int(s[2:4]), int(s[:2]), 0)               # MMYY ("0523")
    m = re.match(r"(\d{4,8})\b", s)                               # composite refs: "112020-F012025"
    if m and m.group(1) != s:
        k = _edition_key(m.group(1))
        if k != (0, 0, 0):
            return k
    m = re.search(r"\b(19|20)\d{2}\b", s)                         # bare year somewhere
    if m:
        return (int(m.group(0)), 0, 0)
    return (0, 0, 0)


def _pick_best(matches: list[dict]) -> tuple[dict, list[dict]]:
    """(chosen, alternatives) for one product's documents. Reference and source_url
    close the ranking so ties never fall back to filesystem order."""
    ranked = sorted(matches, key=lambda o: (
        _DOC_PREF.get(o.get("document_type"), 9),
        1 if o.get("superseded") else 0,
        tuple(-x for x in _edition_key(o.get("edition_date"))),
        str(o.get("reference") or ""),
        str(o.get("source_url") or ""),
    ))
    return ranked[0], ranked[1:]


def _selection_tie(chosen: dict, others: list[dict]) -> dict | None:
    """A sibling the ranking cannot tell apart on substance (same type, same
    supersession, same edition): real datasets have them (two general conditions
    issued the same day for different distribution channels). Callers must say the
    choice fell back to reference order."""
    for o in others:
        if (o.get("document_type") == chosen.get("document_type")
                and bool(o.get("superseded")) == bool(chosen.get("superseded"))
                and _edition_key(o.get("edition_date")) == _edition_key(chosen.get("edition_date"))):
            return o
    return None


def _tie_note(chosen: dict, others: list[dict]) -> str:
    tie = _selection_tie(chosen, others)
    if not tie:
        return ""
    return (f"\n[NOTE: another {chosen.get('document_type')} with the same edition exists "
            f"(reference {tie.get('reference')!r}); they may differ in substance and the "
            "choice between them is by reference order. Check the alternatives or filter "
            "by document_type/edition.]")


OLD_EDITION_YEARS = 7   # keep in step with pipeline/render.py


def _edition_age_years(obj: dict) -> int | None:
    """Whole years between the printed edition date and the day the PDF was collected."""
    ey = _edition_key(obj.get("edition_date"))[0]
    fy = _edition_key(obj.get("fetched_at"))[0]
    if not ey or not fy or fy < ey:
        return None
    return fy - ey


def _doc_meta(obj: dict) -> dict:
    """The identifiers that tell two same-named documents apart."""
    out = {"product_name": obj.get("product_name"), "insurer_slug": obj.get("insurer_slug"),
           "document_type": obj.get("document_type"), "edition_date": obj.get("edition_date"),
           "reference": obj.get("reference"), "superseded": obj.get("superseded"),
           "source_url": obj.get("source_url")}
    # An agent asking "what does ERGO sell?" was getting 2010 editions back with nothing
    # to distinguish them from current ones. State the age, not a conclusion: whether the
    # product is still sold is not in the document.
    age = _edition_age_years(obj)
    if age is not None and age >= OLD_EDITION_YEARS:
        out["edition_age_years"] = age
        out["edition_age_note"] = (
            f"this edition was {age} years old when collected; the insurer was still "
            "publishing it, but whether the product is still sold is not stated in the "
            "document")
    return out


def _product_groups(matches: list[dict]) -> list[list[dict]]:
    """Group matched documents into distinct commercial products.

    Same normalized name (within one insurer) = same product. Cross-name grouping
    then follows, in order of authority:
    - a shared normalized `product_family` merges (rule 8's field for exactly this);
    - families stated on both sides but different NEVER merge;
    - otherwise a containment merge for a product's CG/IPID name variants
      ("Mobility Safe 1" vs "Assurance Auto Mobility Safe 1"), only when their
      document types don't overlap AND the attachment is unambiguous on both
      sides. A name that could attach to several groups stays separate, so the
      result never depends on file order (AMMA's HOSPI-PLAN and HOSPI SAFE must
      not swallow the HOSPI IPID by glob order)."""
    groups: list[list[dict]] = []
    for o in matches:
        key = (o.get("insurer_slug"), _norm(o.get("product_name") or ""))
        for g in groups:
            if (g[0].get("insurer_slug"), _norm(g[0].get("product_name") or "")) == key:
                g.append(o)
                break
        else:
            groups.append([o])

    def families(g: list[dict]) -> set[str]:
        return {_norm(d.get("product_family")) for d in g if d.get("product_family")}

    def same_insurer(a: list[dict], b: list[dict]) -> bool:
        return a[0].get("insurer_slug") == b[0].get("insurer_slug")

    # 1) Authoritative: a shared stated family always merges (transitive).
    merged = True
    while merged:
        merged = False
        for a in groups:
            for b in groups:
                if b is not a and same_insurer(a, b) and families(a) & families(b):
                    a.extend(b)
                    groups.remove(b)
                    merged = True
                    break
            if merged:
                break

    def containable(a: list[dict], b: list[dict]) -> bool:
        if not same_insurer(a, b):
            return False
        if families(a) and families(b):          # both stated and (post step 1) different
            return False
        na, nb = _norm(a[0].get("product_name") or ""), _norm(b[0].get("product_name") or "")
        ta = {d.get("document_type") for d in a}
        tb = {d.get("document_type") for d in b}
        return (na in nb or nb in na) and not (ta & tb)

    # 2) Heuristic: containment merges, only when unambiguous on both sides.
    merged = True
    while merged:
        merged = False
        for a in groups:
            partners = [b for b in groups if b is not a and containable(a, b)]
            if len(partners) == 1 and [g for g in groups
                                       if g is not partners[0]
                                       and containable(partners[0], g)] == [a]:
                a.extend(partners[0])
                groups.remove(partners[0])
                merged = True
                break
    return groups


def _exact_or_ambiguous(groups: list[list[dict]], want: str) -> tuple[list[list[dict]], list[str]]:
    """Disambiguate product groups against the normalized query. An exact name match
    wins over products that merely contain it ('Confort Auto' must resolve even
    though 'Confort Auto - Protection juridique' also matches); the near-misses are
    returned so callers can list them instead of hiding them."""
    if len(groups) <= 1:
        return groups, []
    exact = [g for g in groups if any(_norm(d.get("product_name") or "") == want for d in g)]
    if len(exact) == 1:
        near = sorted({_pick_best(g)[0].get("product_name") or ""
                       for g in groups if g is not exact[0]})
        return exact, near
    return groups, []


def _resolve_document(country: str, insurer_slug: str, product_name: str,
                      document_type: str = "", edition: str = ""
                      ) -> tuple[dict | None, list[dict], list[str], str | None]:
    """Shared resolution for the product-scoped tools: filter by insurer and the
    optional document_type/edition, group into distinct products, apply the
    exact-match rule, pick the best document. Returns (chosen, alternatives,
    similar, error) where error is a ready-to-return message on failure."""
    guard = _no_data(country)
    if guard:
        return None, [], [], f"{DISCLAIMER}\n{guard}"
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
        return None, [], [], (f"{DISCLAIMER}\nNo product matching '{product_name}' "
                              f"for insurer '{insurer_slug}' in {country}.")
    groups, near = _exact_or_ambiguous(_product_groups(matches), want)
    if len(groups) > 1:
        return None, [], [], (
            DISCLAIMER + "\nMultiple distinct products match; refine product_name or "
            "filter by document_type/edition:\n"
            + json.dumps([_doc_meta(_pick_best(g)[0]) for g in groups],
                         ensure_ascii=False, indent=2))
    chosen, others = _pick_best(groups[0])
    return chosen, others, near, None


def _head(chosen: dict, others: list[dict], near: list[str]) -> str:
    """The grounding header every product-scoped response starts with."""
    head = DISCLAIMER + "\n" + _citation(chosen) + _tie_note(chosen, others)
    if near:
        head += (f"\n[Similar products at this insurer not returned: {', '.join(near)}"
                 " - name one exactly to get it.]")
    return head


def _resolve_product(allp: list[tuple[Path, dict]], name: str,
                     insurer: str = "") -> tuple[dict | None, list[dict], list[dict], list[str]]:
    """Match a product name (case- and accent-insensitive substring), optionally within
    one insurer, and pick the best document. Returns (chosen, alternatives, ambiguous,
    similar): when the name matches several distinct products and none is an exact
    match, chosen is None and ambiguous lists the best document of each candidate so
    the caller can ask to refine; similar lists exact-match near-misses."""
    w = _norm(name)
    m = [o for _, o in allp
         if w in _norm(o.get("product_name") or "")
         and (not insurer or o.get("insurer_slug") == insurer)]
    if not m:
        return None, [], [], []
    groups, near = _exact_or_ambiguous(_product_groups(m), w)
    if len(groups) > 1:
        return None, [], [_doc_meta(_pick_best(g)[0]) for g in groups], []
    chosen, others = _pick_best(groups[0])
    return chosen, others, [], near


# --- coverage categorization (for the overlap detector) ---------------------

def _norm(s: str) -> str:
    # NFKD strips accents but leaves curly apostrophes and ligatures alone, and
    # French PDFs are full of both ("L’assurance", "cœur") - fold them by hand.
    s = (s or "").replace("’", "'").replace("‘", "'")
    s = s.replace("œ", "oe").replace("Œ", "OE")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).lower()


_CATS = None


def _categories() -> dict:
    """Controlled vocabulary with keywords pre-normalized once: re-normalizing
    every keyword on every _categorize call dominated find_overlap's latency."""
    global _CATS
    if _CATS is None:
        p = SCHEMA / "coverage_categories.json"
        raw = json.loads(p.read_text(encoding="utf-8")).get("categories", {}) if p.is_file() else {}
        _CATS = {key: {"label": meta.get("label", key),
                       "kw": [_norm(kw) for kw in meta.get("keywords", [])]}
                 for key, meta in raw.items()}
    return _CATS


def _categorize(text: str) -> list[str]:
    """Return the category keys whose keywords appear in the (accent-normalized) text.
    Heuristic candidate tags, not an authority."""
    t = _norm(text)
    return [key for key, meta in _categories().items() if any(kw in t for kw in meta["kw"])]


_DOC_CATS_CACHE: dict[tuple[str, str], tuple[list, list]] = {}


def _doc_category_items(o: dict, on: str) -> tuple[list, list]:
    """Category tags for one document's coverages/exclusions, computed once per
    document: (items with their category labels, (category, item_name) pairs)."""
    key = (str(o.get("source_sha256") or o.get("source_url") or id(o)), on)
    if key not in _DOC_CATS_CACHE:
        labels = {k: v["label"] for k, v in _categories().items()}
        items, pairs = [], []
        for it in (o.get(on) or []):
            if not isinstance(it, dict):
                continue
            cats = _categorize(f"{it.get('name', '')} {it.get('description', '')}")
            items.append({"name": it.get("name"),
                          "categories": [labels.get(c, c) for c in cats]})
            pairs.extend((c, it.get("name")) for c in cats)
        _DOC_CATS_CACHE[key] = (items, pairs)
    return _DOC_CATS_CACHE[key]


# --- tools ------------------------------------------------------------------

@mcp.tool()
def list_countries() -> str:
    """List countries covered: product/insurer/regulation counts, how many branches
    have at least one product (branches_covered), the size of the country's branch
    taxonomy (branch_taxonomy), and how many hand-written branch overview pages
    exist (branch_overview_pages)."""
    if not _countries():
        return _NO_DATASET
    rows = []
    for cc in _countries():
        idx = _read_index(cc)
        meta = _country_meta(cc)
        counts = {}
        for r in idx:
            counts[r.get("type")] = counts.get(r.get("type"), 0) + 1
        covered = {r.get("branch") for r in idx if r.get("type") == "product" and r.get("branch")}
        rows.append({"country": cc, "name": meta.get("name", cc),
                     "regulator": meta.get("regulator"),
                     "branches_covered": len(covered),
                     "branch_taxonomy": len(meta.get("branches", {})),
                     "branch_overview_pages": counts.get("branch", 0),
                     "products": counts.get("product", 0),
                     "insurers": counts.get("insurer", 0),
                     "regulations": counts.get("regulation", 0)})
    return json.dumps(rows, ensure_ascii=False, indent=2)


@mcp.tool()
def list_branches(country: str = "be") -> str:
    """List insurance branches for a country with their labels, mandatory flag and product counts."""
    if country not in _countries():
        return _NO_DATASET if not _countries() else (
            f"No data for country '{country}'. Covered countries: " + ", ".join(_countries()) + ".")
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
    Returns matches with path, source_url and freshness; when more than `limit`
    pages match, the response says how many were left out."""
    if country not in _countries():
        return _NO_DATASET if not _countries() else (
            f"No data for country '{country}'. Covered countries: " + ", ".join(_countries()) + ".")
    terms = [t for t in _norm(query).split() if t]
    results = []
    for r, hay in zip(_read_index(country), _index_hay(country)):
        if type and r.get("type") != type:
            continue
        if branch and r.get("branch") != branch:
            continue
        if insurer and (r.get("insurer") or "") != insurer:
            continue
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
    body = json.dumps(out, ensure_ascii=False, indent=2)
    if len(results) > limit:
        return f"[{len(results)} pages match; showing the first {limit}. Raise limit for more.]\n" + body
    return body


@mcp.tool()
def get_page(path: str) -> str:
    """Return the full text of one knowledge page by its repo-relative path (from
    search results). Text files in the knowledge folders only (.md, .json, .yml,
    .yaml, .txt, .csv)."""
    p = _safe_repo_path(path)
    if not p:
        return f"Not found or outside repo: {path}"
    try:
        return _read_page(p)
    except UnicodeDecodeError:
        return f"Not a readable text file: {path}"


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
    chosen, others, near, err = _resolve_document(country, insurer_slug, product_name,
                                                  document_type, edition)
    if err:
        return err
    payload = dict(chosen)
    head = _head(chosen, others, near)
    if others:
        payload["other_documents"] = [_doc_meta(o) for o in others]
        head += (f"\n[{len(others)} other document(s) for this product under `other_documents`.]")
    return head + "\n" + json.dumps(payload, ensure_ascii=False, indent=2)


_STOPWORDS = {"les", "des", "une", "aux", "est", "sont", "dans", "pour", "avec", "par",
              "que", "qui", "pas", "sur", "the", "and", "for", "are", "not", "was",
              "assurance", "assure", "assuree", "police", "contrat", "garantie",
              # near-universal in insurance wording: zero discriminating power
              "couvre", "couvert", "couverte", "couverts", "couvertes", "couverture",
              "cover", "covered", "coverage", "exclusion", "exclu", "exclue"}


def _item_text(it: dict) -> str:
    """One coverage/exclusion flattened to quotable text: the discriminating detail
    often lives in conditions/limits, not in the name or description."""
    head = ": ".join(str(it.get(k)) for k in ("name", "description") if it.get(k))
    tail = []
    for k in ("limits", "deductible", "territorial_scope"):
        if it.get(k):
            tail.append(f"{k}: {it.get(k)}")
    conds = it.get("conditions")
    if conds:
        tail.append("conditions: " + ("; ".join(str(c) for c in conds)
                                      if isinstance(conds, list) else str(conds)))
    if it.get("sub_limits"):
        tail.append("sub_limits: " + json.dumps(it.get("sub_limits"), ensure_ascii=False))
    return head + ((" | " + " | ".join(tail)) if tail else "")


def _claim_terms(text: str) -> list[str]:
    """Content words of a claim/topic: normalized tokens, stopwords and generic
    insurance words dropped, digits kept (amounts and dates are the point)."""
    tokens = re.findall(r"[a-z0-9]+(?:[.,]\d+)?", _norm(text))
    return [t for t in tokens if (len(t) >= 3 or t.isdigit()) and t not in _STOPWORDS]


def _match_score(text_norm: str, terms: list[str]) -> int:
    return sum(1 for t in terms if t in text_norm)


_MAX_MATCHED_ITEMS = 12


@mcp.tool()
def get_coverage(country: str, insurer_slug: str, product_name: str, topic: str,
                 document_type: str = "", edition: str = "") -> str:
    """Compact, question-oriented view of ONE product: only the coverages and
    exclusions relevant to `topic` (e.g. 'vol', 'degats des eaux', 'ski hors-piste'),
    with their limits, deductibles, verbatim quotes and page numbers. Prefer this
    over get_product when answering a specific guarantee question: everything needed
    to quote is in the response and nothing else. Matching is accent- and
    case-insensitive over coverage/exclusion names and descriptions. An empty match
    list means the topic was not found in THIS document; that is not proof the
    product has no such cover - say so and point to the source_url."""
    chosen, others, near, err = _resolve_document(country, insurer_slug, product_name,
                                                  document_type, edition)
    if err:
        return err
    terms = _claim_terms(topic) or [t for t in _norm(topic).split() if t]
    if not terms:
        return f"{DISCLAIMER}\nEmpty topic; give a coverage question or keyword."

    def matched(items):
        scored = []
        for it in (items or []):
            if not isinstance(it, dict):
                continue
            s = _match_score(_norm(_item_text(it)), terms)
            if s:
                scored.append((s, it))
        scored.sort(key=lambda x: (-x[0], str(x[1].get("name"))))
        return [it for _, it in scored]

    cov = matched(chosen.get("coverages"))
    exc = matched(chosen.get("exclusions"))
    quotes = [q for q in (chosen.get("key_quotes") or []) if isinstance(q, dict)
              and _match_score(_norm(q.get("quote") or ""), terms)]
    result = {"topic": topic,
              "matched_coverages": cov[:_MAX_MATCHED_ITEMS],
              "matched_exclusions": exc[:_MAX_MATCHED_ITEMS],
              "related_quotes": quotes[:_MAX_MATCHED_ITEMS],
              "source_url": chosen.get("source_url")}
    for name, full in (("matched_coverages", cov), ("matched_exclusions", exc),
                       ("related_quotes", quotes)):
        if len(full) > _MAX_MATCHED_ITEMS:
            result[f"{name}_omitted"] = len(full) - _MAX_MATCHED_ITEMS
    ded = chosen.get("deductibles")
    if ded and _match_score(_norm(json.dumps(ded, ensure_ascii=False)), terms):
        result["deductibles"] = ded
    if not (cov or exc or quotes):
        result["note"] = ("no coverage, exclusion or quote in this document matches "
                          "the topic; not proof of absence - check the source document "
                          "or get_product for the full extraction")
    return _head(chosen, others, near) + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def verify_claim(country: str, insurer_slug: str, product_name: str, claim: str) -> str:
    """Verbatim evidence check for ONE factual claim about a product ('le ski
    hors-piste est couvert avec un moniteur', 'franchise de 250 EUR en vol').
    Returns the document excerpts (coverages, exclusions, quotes, definitions,
    deductibles, summary) sharing the claim's terms, each with its page when
    stated. The tool does NOT judge: compare the claim against the excerpts. If a
    number, date, article or condition the claim relies on appears in no excerpt,
    treat it as NOT SUPPORTED by this document and say so. Use it as a self-check
    before asserting product facts to a user."""
    chosen, others, near, err = _resolve_document(country, insurer_slug, product_name)
    if err:
        return err
    terms = _claim_terms(claim)
    if not terms:
        return f"{DISCLAIMER}\nEmpty claim; state the fact to check."
    evidence = []

    def add(source, text, page=None):
        s = _match_score(_norm(text), terms)
        if s:
            e = {"source_field": source, "text": text}
            if page is not None:
                e["page"] = page
            evidence.append((s, e))

    for it in (chosen.get("coverages") or []):
        if isinstance(it, dict):
            add("coverages", _item_text(it), it.get("page"))
    for it in (chosen.get("exclusions") or []):
        if isinstance(it, dict):
            add("exclusions", _item_text(it), it.get("page"))
    for q in (chosen.get("key_quotes") or []):
        if isinstance(q, dict):
            add("key_quotes", q.get("quote") or "", q.get("page"))
    for d in (chosen.get("definitions") or []):
        if isinstance(d, dict):
            add("definitions", f"{d.get('term', '')}: {d.get('definition', '')}",
                d.get("page"))
    ded = chosen.get("deductibles")
    if ded:
        add("deductibles", json.dumps(ded, ensure_ascii=False))
    if chosen.get("summary"):
        add("summary", str(chosen.get("summary")))
    evidence.sort(key=lambda x: -x[0])
    top = [e for _, e in evidence[:_MAX_MATCHED_ITEMS]]
    result = {"claim": claim, "terms_matched_on": terms, "evidence": top,
              "evidence_total": len(evidence), "source_url": chosen.get("source_url"),
              "note": ("this tool retrieves, it does not judge: the claim is supported "
                       "only if the evidence above literally says so. No evidence = "
                       "not supported by this document.")}
    if len(evidence) > _MAX_MATCHED_ITEMS:
        result["evidence_omitted"] = len(evidence) - _MAX_MATCHED_ITEMS
    return _head(chosen, others, near) + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def compare_products(country: str, product_names: list[str], on: str = "coverages",
                     insurer_slugs: list[str] | None = None) -> str:
    """Compare 2+ products side by side on one dimension: coverages | exclusions | deductibles.
    Each name is matched case-insensitively against extracted product names; pass
    insurer_slugs (same length/order as product_names) to pin each name to one insurer.
    A name matching several DISTINCT products is refused with the candidates listed
    (refine it rather than let the server guess). For each resolved name the best
    document is selected (general conditions over IPID, newest edition) and identified
    in the response, including its superseded flag."""
    if on not in ("coverages", "exclusions", "deductibles"):
        return "on must be one of: coverages | exclusions | deductibles"
    if insurer_slugs and len(insurer_slugs) != len(product_names):
        return "insurer_slugs must have the same length/order as product_names"
    guard = _no_data(country)
    if guard:
        return f"{DISCLAIMER}\n{guard}"
    allp = _extracted(country)
    chosen, unmatched, ambiguous = [], [], {}
    for i, name in enumerate(product_names):
        obj, others, amb, near = _resolve_product(allp, name,
                                                  insurer_slugs[i] if insurer_slugs else "")
        if amb:
            ambiguous[name] = amb
        elif obj:
            chosen.append((obj, others, near))
        else:
            unmatched.append(name)
    if ambiguous:
        return (DISCLAIMER + "\nAmbiguous product name(s): each matches several distinct "
                "products (candidates below). Use a more specific name or pin each name "
                "to one insurer with insurer_slugs.\n"
                + json.dumps(ambiguous, ensure_ascii=False, indent=2))
    if len(chosen) < 2:
        return (f"{DISCLAIMER}\nNeed at least 2 matching products; matched {len(chosen)}."
                + (f" Unmatched: {unmatched}" if unmatched else ""))
    result = {"on": on, "products": []}
    if unmatched:
        result["unmatched"] = unmatched
    for obj, others, near in chosen:
        entry = {"product_name": obj.get("product_name"), "insurer": obj.get("insurer_name"),
                 "insurer_slug": obj.get("insurer_slug"),
                 "document_type": obj.get("document_type"),
                 "edition_date": obj.get("edition_date"), "reference": obj.get("reference"),
                 "superseded": obj.get("superseded"),
                 "other_documents_exist": len(others), "source_url": obj.get("source_url")}
        if _selection_tie(obj, others):
            entry["selection_note"] = ("another document of the same type and edition "
                                       "exists; selection fell back to reference order")
        if near:
            entry["similar_products_not_compared"] = near
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
    guard = _no_data(country)
    if guard:
        return f"{DISCLAIMER}\n{guard}"
    allp = _extracted(country)
    chosen, unmatched, ambiguous = [], [], {}
    for i, name in enumerate(product_names):
        o, _others, amb, near = _resolve_product(allp, name,
                                                 insurer_slugs[i] if insurer_slugs else "")
        if amb:
            ambiguous[name] = amb
        elif o:
            chosen.append((o, near))
        else:
            unmatched.append(name)
    if ambiguous:
        return (DISCLAIMER + "\nAmbiguous product name(s): each matches several distinct "
                "products (candidates below). Use a more specific name or pin each name "
                "to one insurer with insurer_slugs.\n"
                + json.dumps(ambiguous, ensure_ascii=False, indent=2))
    if len(chosen) < 2:
        return (f"{DISCLAIMER}\nNeed at least 2 matching products; matched {len(chosen)}."
                + (f" Unmatched: {unmatched}" if unmatched else ""))
    labels = {k: v["label"] for k, v in _categories().items()}
    cat_items = defaultdict(list)
    per_product = []
    for o, near in chosen:
        pname = o.get("product_name")
        items, pairs = _doc_category_items(o, on)
        for c, item_name in pairs:
            cat_items[c].append({"product": pname, "item": item_name})
        entry = {"product_name": pname, "insurer": o.get("insurer_name"),
                 "branch": o.get("branch"), "document_type": o.get("document_type"),
                 "edition_date": o.get("edition_date"), "reference": o.get("reference"),
                 "superseded": o.get("superseded"),
                 "source_url": o.get("source_url"), on: items}
        if near:
            entry["similar_products_not_included"] = near
        per_product.append(entry)
    overlaps = []
    for c, entries in cat_items.items():
        if len({e["product"] for e in entries}) >= 2:
            overlaps.append({"category": labels.get(c, c),
                             "products": sorted({e["product"] for e in entries}), "items": entries})
    overlaps.sort(key=lambda x: -len(x["products"]))
    note = ("candidate_overlaps are heuristic (a shared controlled category); confirm each "
            "against the actual coverage descriptions. Absence of a category is not proof of "
            "no overlap - the taxonomy is not exhaustive.")
    if unmatched:
        note += (" INCOMPLETE: the products listed in 'unmatched' were not found and were not "
                 "analysed, so overlaps involving them cannot appear here.")
    result = {"on": on, "products": per_product, "candidate_overlaps": overlaps, "note": note}
    if unmatched:
        result["unmatched"] = unmatched
    return DISCLAIMER + "\n" + json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def get_branch_overview(country: str, branch: str) -> str:
    """Return the hand-authored overview page for a branch (by slug or label)."""
    meta = _country_meta(country)
    label = meta.get("branches", {}).get(branch, {}).get("label", branch)
    for cand in (label, branch):
        p = WIKI / country / "branches" / f"{cand}.md"
        if p.is_file():
            return _read_page(p)
    return f"No branch overview for '{branch}' in {country}."


def main() -> None:
    """Console entry point (`insurance-wiki-mcp` once installed). Refuses to start
    without a dataset: a silent empty server reads as "the wiki covers nothing"."""
    if not _countries():
        print(f"[insurance-wiki-mcp] {_NO_DATASET}", file=sys.stderr)
        raise SystemExit(1)
    mcp.run()


if __name__ == "__main__":
    main()
