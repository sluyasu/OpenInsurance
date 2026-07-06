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


def _edition_key(ed) -> tuple[int, int]:
    """(year, month) sortable key from an edition date as printed in the source PDF
    (04.2025, 2026-05-12, 12/05/2026, 01042026, 2019, ...); (0, 0) if undated/unparseable."""
    if not ed:
        return (0, 0)
    s = str(ed).strip()
    m = re.fullmatch(r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})", s)   # YYYY-MM-DD
    if m:
        y, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return (y, a) if a <= 12 else (y, b)
    m = re.fullmatch(r"(\d{1,2})[-./](\d{1,2})[-./](\d{4})", s)   # DD-MM-YYYY
    if m:
        return (int(m.group(3)), int(m.group(2)))
    m = re.fullmatch(r"(\d{1,2})[-./](\d{4})", s)                 # MM-YYYY
    if m:
        return (int(m.group(2)), int(m.group(1)))
    m = re.fullmatch(r"(\d{4})[-./](\d{1,2})", s)                 # YYYY-MM
    if m:
        return (int(m.group(1)), int(m.group(2)))
    m = re.fullmatch(r"(\d{2})(\d{2})(\d{4})", s)                 # DDMMYYYY
    if m:
        return (int(m.group(3)), int(m.group(2)))
    m = re.fullmatch(r"(\d{1,2})[./](\d{2})", s)                  # MM.YY
    if m and int(m.group(1)) <= 12:
        return (2000 + int(m.group(2)), int(m.group(1)))
    m = re.search(r"\b(19|20)\d\d\b", s)                          # bare year somewhere
    if m:
        return (int(m.group(0)), 0)
    return (0, 0)


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
        # version status among same document_type
        by_type: dict[str, list[dict]] = defaultdict(list)
        for o in group:
            by_type[o.get("document_type", "")].append(o)

        superseded_by = {}
        current_flag = {}
        for dt, docs in by_type.items():
            dated = [(o, _edition_key(o.get("edition_date"))) for o in docs]
            dated = [(o, k) for o, k in dated if k != (0, 0)]
            if len(dated) >= 2:
                maxk = max(k for _, k in dated)
                newest = next(o for o, k in dated if k == maxk)
                for o, k in dated:
                    if k < maxk:
                        superseded_by[id(o)] = titles[id(newest)]
                    else:
                        current_flag[id(o)] = True

        for o in group:
            others = [x for x in group if x is not o]
            related = [{
                "title": titles[id(x)],
                "document_type": x.get("document_type"),
                "edition_date": x.get("edition_date"),
            } for x in others]
            # extension links within the family
            parent = None
            if o.get("is_extension") and o.get("extends"):
                parent = o.get("extends")
            extensions = [titles[id(x)] for x in others
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
