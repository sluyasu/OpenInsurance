#!/usr/bin/env python
"""Validation gates for the wiki. Fails (exit 1) on: missing/invalid frontmatter,
a product page without a source_url, or broken wikilinks. Orphans are reported as
warnings.

Usage: python pipeline/validate.py --country be
"""

from __future__ import annotations

import argparse
import sys

from common import WIKI, REPO, read_note, wikilinks, load_country

REQUIRED = {"type", "status"}


def resolution_targets() -> dict[str, str]:
    """Map every resolvable name (stem + aliases) -> the note path that owns it."""
    targets = {}
    roots = [WIKI, REPO / "_meta" / "universal-glossary"]
    for root in roots:
        if not root.is_dir():
            continue
        for md in root.rglob("*.md"):
            meta, _ = read_note(md)
            names = [md.stem] + [str(a) for a in (meta.get("aliases") or [])]
            for n in names:
                targets.setdefault(n.strip(), str(md.relative_to(REPO)))
    return targets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    args = ap.parse_args()
    cc = args.country

    root = WIKI / cc
    if not root.is_dir():
        print(f"[validate] no wiki for country={cc}")
        return 0

    targets = resolution_targets()
    branch_labels = {m.get("label") for m in load_country(cc).get("branches", {}).values()}

    errors, warnings = [], []
    notes = sorted(root.rglob("*.md"))
    incoming: dict[str, int] = {}
    outgoing: dict[str, int] = {}

    for md in notes:
        rel = str(md.relative_to(REPO))
        meta, body = read_note(md)
        if not meta:
            errors.append(f"{rel}: no/invalid frontmatter")
            continue
        missing = REQUIRED - set(meta.keys())
        if missing:
            errors.append(f"{rel}: missing frontmatter {sorted(missing)}")
        if meta.get("type") == "product":
            if not meta.get("source_url"):
                errors.append(f"{rel}: product page missing source_url")
            if meta.get("status") != "stub" and "p. " not in body and "pages" not in body:
                warnings.append(f"{rel}: product page has no page citations")

        links = wikilinks(body)
        outgoing[rel] = len(links)
        for link in links:
            if link in targets or link in branch_labels:
                incoming[targets.get(link, link)] = incoming.get(targets.get(link, link), 0) + 1
            else:
                errors.append(f"{rel}: broken wikilink [[{link}]]")

    # orphans: non-MOC notes with no links either way
    for md in notes:
        rel = str(md.relative_to(REPO))
        meta, _ = read_note(md)
        if meta.get("type") == "moc":
            continue
        if outgoing.get(rel, 0) == 0 and incoming.get(rel, 0) == 0:
            warnings.append(f"{rel}: orphan (no incoming or outgoing links)")

    for w in warnings:
        print(f"[validate] WARN {w}")
    for e in errors:
        print(f"[validate] ERROR {e}")
    print(f"[validate] {len(notes)} notes · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
