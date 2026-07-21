"""Version & relationship linking (build-time).

The same insurance product is re-issued over time (editions), sold through several
channels (variants), documented in several files (CG + IPID), and extended by options
(extensions). This module groups the extracted products by product family and computes,
for each document, its edition status (current vs superseded), its related documents,
and any parent/extension links. build_wiki.py feeds the result to the renderer.

Nothing here fabricates data: it only relates what extraction captured (edition_date,
product_family, variant, is_extension/extends). When those fields are absent (older
prompt version), it falls back to a product-name heuristic for the family key.
"""

from __future__ import annotations

import re
from collections import defaultdict

from common import slugify
import render


def _family_base(obj: dict) -> str:
    fam = obj.get("product_family")
    if fam:
        src = str(fam)
    else:
        src = obj.get("product_name", "") or ""
        src = re.sub(r"\(.*?\)", " ", src)            # drop parentheticals
        src = re.split(r"\s[-–—]\s|,", src)[0]  # drop after " - " (hyphen/en/em dash) / comma
        src = re.sub(r"\b(19|20)\d\d\b", " ", src)     # drop years
    return slugify(src) or "produit"


def _edition_key(ed) -> tuple[int, int, int]:
    """Sortable (year, month, day) from an edition date as printed in the source PDF
    (04.2025, 2026-05-12, 12/05/2026, 01042026, 2019, ...). (0,0,0) when unparseable.

    Kept byte-identical to the MCP server's parser (mcp/insurance_wiki_mcp.py). The two
    cannot share a module: the server ships standalone on PyPI and never imports pipeline/.
    tests/test_pipeline_link.py asserts the two stay in agreement."""
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


def compute_relations(products: list[dict]) -> dict[str, dict]:
    """url -> relation dict {family, variant, edition_status, superseded_by,
    related[], extends_parent, extensions[]}."""
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for obj in products:
        key = (obj.get("insurer_slug"), obj.get("branch"), _family_base(obj))
        groups[key].append(obj)

    rel: dict[str, dict] = {}
    for key, group in groups.items():
        titles = {id(o): render.product_title(o) for o in group}
        # Version status among documents of the same type AND the same variant. Variants
        # (channel/formula, e.g. a Luxembourg edition sold alongside the Belgian one) run
        # in parallel and never supersede each other - only editions do (rule 8).
        by_type: dict[tuple, list[dict]] = defaultdict(list)
        for o in group:
            by_type[(o.get("document_type", ""), o.get("variant"))].append(o)

        superseded_by = {}
        current_flag = {}
        for dt, docs in by_type.items():
            dated = [(o, _edition_key(o.get("edition_date"))) for o in docs]
            dated = [(o, k) for o, k in dated if k != (0, 0, 0)]
            if len(dated) >= 2:
                maxk = max(k for _, k in dated)
                newest = next(o for o, k in dated if k == maxk)
                for o, k in dated:
                    if k < maxk:
                        superseded_by[id(o)] = {"title": titles[id(newest)],
                                                "source_url": newest.get("source_url")}
                    else:
                        current_flag[id(o)] = True

        for o in group:
            others = [x for x in group if x is not o]
            # source_url travels with every relation: it is the key the renderer resolves
            # to a real page path, since titles are not unique across insurers.
            related = [{
                "title": titles[id(x)],
                "source_url": x.get("source_url"),
                "document_type": x.get("document_type"),
                "edition_date": x.get("edition_date"),
            } for x in others]
            # extension links within the family
            parent = None
            if o.get("is_extension") and o.get("extends"):
                parent = o.get("extends")
            extensions = [{"title": titles[id(x)], "source_url": x.get("source_url")}
                          for x in others
                          if x.get("is_extension") and x.get("extends")
                          and _family_base(x) == key[2]] if not o.get("is_extension") else []
            status = None
            if id(o) in superseded_by:
                status = "superseded"
            elif id(o) in current_flag:
                status = "current"
            rel[o.get("source_url")] = {
                "family": key[2],
                "variant": o.get("variant"),
                "edition_status": status,
                "superseded_by": superseded_by.get(id(o)),
                "related": related,
                "extends_parent": parent,
                "extensions": extensions,
            }
    return rel
