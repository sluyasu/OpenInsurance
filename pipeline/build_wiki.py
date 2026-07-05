#!/usr/bin/env python
"""Assemble the wiki from extracted product JSON. Generated pages only
(products/ + insurers/ + the branches MOC); hand-authored pages are never touched.

Resume-safe (write_if_changed) and self-cleaning (stale generated pages are removed),
so a no-op rebuild produces zero diff.

Usage: python pipeline/build_wiki.py --country be
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from common import (WIKI, REPO, extracted_dir, read_json, write_if_changed,
                    insurer_configs, load_country, safe_title)
import render
import link


def load_products(cc: str) -> list[dict]:
    out = []
    base = extracted_dir(cc)
    if base.is_dir():
        for p in sorted(base.glob("*/*.json")):
            obj = read_json(p)
            if obj:
                out.append(obj)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    args = ap.parse_args()
    cc = args.country

    country_meta = load_country(cc)
    products = load_products(cc)
    if not products:
        print(f"[build] no extractions found under data/{cc}/extracted/. Run extract first.")
    websites = {c["insurer"]["slug"]: c["insurer"].get("website")
                for c in insurer_configs(cc)}
    insurer_names = {c["insurer"]["slug"]: c["insurer"].get("name")
                     for c in insurer_configs(cc)}

    relations = link.compute_relations(products)

    prod_root = WIKI / cc / "products"
    ins_root = WIKI / cc / "insurers"
    written = 0
    expected: set[Path] = set()

    # --- product pages (disambiguate title collisions deterministically) ---
    seen: dict[Path, int] = {}
    by_insurer: dict[str, list[dict]] = {}
    for obj in products:
        slug = obj.get("insurer_slug", "unknown")
        obj["insurer_name"] = obj.get("insurer_name") or insurer_names.get(slug, slug)
        by_insurer.setdefault(slug, []).append(obj)
        title = render.product_title(obj)
        path = prod_root / slug / f"{title}.md"
        if path in seen:
            seen[path] += 1
            path = prod_root / slug / f"{title} ({seen[path]}).md"
        else:
            seen[path] = 1
        expected.add(path)
        rel = relations.get(obj.get("source_url"))
        if write_if_changed(path, render.render_product(obj, country_meta, rel)):
            written += 1

    # --- insurer pages ---
    for slug, prods in sorted(by_insurer.items()):
        name = insurer_names.get(slug) or prods[0].get("insurer_name") or slug
        path = ins_root / f"{safe_title(name)}.md"
        expected.add(path)
        if write_if_changed(path, render.render_insurer(name, slug, cc, prods, country_meta,
                                                        websites.get(slug))):
            written += 1

    # --- generated branches MOC ---
    moc = WIKI / cc / "branches" / "00 - Branches MOC.md"
    expected.add(moc)
    if write_if_changed(moc, render.render_branches_moc(cc, products, country_meta)):
        written += 1

    # --- remove stale generated pages (products/ + insurers/ only) ---
    removed = 0
    for folder in (prod_root, ins_root):
        if folder.is_dir():
            for md in folder.rglob("*.md"):
                if md not in expected:
                    md.unlink()
                    removed += 1
    # prune empty insurer product dirs
    if prod_root.is_dir():
        for d in sorted(prod_root.glob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()

    print(f"[build] {len(products)} products, {len(by_insurer)} insurers. "
          f"Wrote/updated {written} pages, removed {removed} stale.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
