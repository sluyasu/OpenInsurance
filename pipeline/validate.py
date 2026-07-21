#!/usr/bin/env python
"""Validation gates for the wiki. Fails (exit 1) on: missing/invalid frontmatter,
a product page without a source_url, or broken wikilinks. Orphans are reported as
warnings.

Usage: python pipeline/validate.py --country be
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from common import WIKI, REPO, read_note, wikilinks, load_country

REQUIRED = {"type", "status"}


def resolution_targets() -> dict[str, str]:
    """Map every resolvable name (stem + aliases) -> the note path that owns it."""
    targets = {}
    # The universal glossary lives under wiki/ so that it is published and reachable:
    # while it sat in _meta/ it resolved in the vault but 404'd on the site.
    roots = [WIKI]
    for root in roots:
        if not root.is_dir():
            continue
        for md in root.rglob("*.md"):
            meta, _ = read_note(md)
            names = [md.stem] + [str(a) for a in (meta.get("aliases") or [])]
            for n in names:
                targets.setdefault(n.strip(), str(md.relative_to(REPO)))
    return targets


MDLINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+\.md)\)")


def mdlinks(md: Path, body: str) -> list[tuple[str, Path | None]]:
    """Relative markdown links to other notes: (raw target, resolved path or None).

    Generated pages link by path rather than by [[name]], so link health has to be
    checked here too. Unlike a wikilink, a path link can be verified outright: either
    the file is there or the published site 404s."""
    out = []
    for m in MDLINK_RE.finditer(body):
        raw = m.group(1)
        if "://" in raw:
            continue
        target = (md.parent / unquote(raw)).resolve()
        out.append((raw, target if target.is_file() else None))
    return out


def ambiguous_names(cc: str) -> dict[str, list[str]]:
    """Names claimed by more than one published page, i.e. every name a basename-only
    resolver has to guess at.

    This models the PUBLISH surface, not the vault: Obsidian shows a disambiguation
    prompt, but the site's roamlinks plugin and resolution_targets() both silently take
    the first match, so a bare [[Assurance Auto]] on an Argenta page can land on Yuzzu's
    product. Silent wrong routing is worse than a broken link, because nothing looks
    wrong. It matters more as countries are added: 'Assurance Auto' will exist in BE, CH
    and FR at once, so the same bug starts routing across borders."""
    claims: dict[str, list[str]] = {}
    for md in sorted((WIKI / cc).rglob("*.md")):
        meta, _ = read_note(md)
        rel = str(md.relative_to(REPO))
        # a page whose stem is repeated in its own aliases claims the name once, not
        # twice: counting per name would report every such page as self-ambiguous
        for n in {md.stem} | {str(a).strip() for a in (meta.get("aliases") or [])}:
            paths = claims.setdefault(n.strip(), [])
            if rel not in paths:
                paths.append(rel)
    return {n: paths for n, paths in claims.items() if len(paths) > 1}


def data_layer_errors(cc: str) -> list[str]:
    """Validate the extracted JSON against the committed schema and the country taxonomy.

    The wiki gates checked the rendered pages only, so a schema-invalid extraction passed
    as long as it rendered. It needs no PDFs, so unlike the grounding check it can run in
    CI, where it is the only thing standing between a drifted extraction and the dataset
    other people install from PyPI."""
    import jsonschema
    from common import read_json, extracted_dir, load_country

    schema = read_json(REPO / "schema" / "product.schema.json")
    v = jsonschema.Draft202012Validator(schema)
    branches = set((load_country(cc).get("branches") or {}).keys())
    out = []
    for f in sorted(extracted_dir(cc).glob("*/*.json")):
        rel = f.relative_to(REPO)
        try:
            obj = read_json(f)
        except Exception as e:                                   # noqa: BLE001
            out.append(f"{rel}: unreadable ({e})")
            continue
        for e in list(v.iter_errors(obj))[:3]:
            out.append(f"{rel}: {'/'.join(map(str, e.path))}: {e.message[:160]}")
        if obj.get("branch") not in branches:
            out.append(f"{rel}: branch '{obj.get('branch')}' is not in the {cc} taxonomy")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--strict-links", action="store_true",
                    help="treat ambiguous link targets as errors (CI gate once they reach 0)")
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
    missing_branch_pages: dict[str, int] = {}
    ambiguous_link_counts: dict[str, int] = {}

    # stray files at the vault root: a wikilink click in Obsidian creates an empty
    # note at wiki/ root, outside the per-country scan - catch it here
    for p in sorted(WIKI.glob("*.md")):
        if p.name != "00 - START HERE.md":
            errors.append(f"{p.relative_to(REPO)}: unexpected file at wiki/ root")

    for md in notes:
        rel = str(md.relative_to(REPO))
        if md.stat().st_size == 0:
            errors.append(f"{rel}: empty file")
            continue
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

        path_links = mdlinks(md, body)
        for raw, target in path_links:
            if target is None:
                errors.append(f"{rel}: broken link ({raw}) - no such file")
            else:
                tgt = str(target.relative_to(REPO))
                incoming[tgt] = incoming.get(tgt, 0) + 1

        links = wikilinks(body)
        outgoing[rel] = len(links) + len(path_links)
        for link in links:
            ambiguous_link_counts[link] = ambiguous_link_counts.get(link, 0) + 1
            if link in targets:
                incoming[targets[link]] = incoming.get(targets[link], 0) + 1
            elif link in branch_labels:
                # a known branch, but nobody wrote its page yet: a labeled gap, not an error
                missing_branch_pages[link] = missing_branch_pages.get(link, 0) + 1
            else:
                errors.append(f"{rel}: broken wikilink [[{link}]]")

    for label in sorted(missing_branch_pages):
        warnings.append(f"branch '{label}': {missing_branch_pages[label]} wikilinks but no "
                        f"branch page yet (wiki/{cc}/branches/{label}.md)")

    # data layer: the extractions the pages are rendered from
    for e in data_layer_errors(cc):
        errors.append(e)

    # publish surface: bare links whose target name is claimed by several pages
    ambiguous = ambiguous_names(cc)
    if ambiguous:
        bare = {n: c for n, c in ambiguous_link_counts.items() if n in ambiguous}
        bucket = errors if args.strict_links else warnings
        for n in sorted(bare, key=lambda x: -bare[x]):
            bucket.append(f"ambiguous link target [[{n}]]: {bare[n]} bare link(s), "
                          f"{len(ambiguous[n])} pages claim the name "
                          f"({', '.join(Path(p).parent.name for p in ambiguous[n])}) - "
                          f"a basename resolver picks one silently")
        unlinked = sorted(set(ambiguous) - set(bare))
        if unlinked:
            warnings.append(f"{len(unlinked)} duplicate page name(s) with no bare link yet "
                            f"(harmless today, a trap for the next hand-authored link): "
                            f"{', '.join(unlinked[:5])}{' ...' if len(unlinked) > 5 else ''}")

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
