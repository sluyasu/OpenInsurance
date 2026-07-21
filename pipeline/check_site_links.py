#!/usr/bin/env python
"""Check the BUILT site for links that go nowhere.

validate.py checks the markdown sources; this checks what MkDocs actually published.
The two are not the same surface: a source link can be perfectly valid and still 404
once the site is rendered, because a page moved into a directory, a wikilink was left
for the roamlinks plugin to resolve and it could not, or a relative path escaped the
published tree. Those are exactly the failures nobody notices, since the wiki gates stay
green while readers hit dead ends.

Usage: python pipeline/check_site_links.py [site_dir]
Exit code 1 if any internal link is broken, so it can gate a deploy.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urldefrag

HREF = re.compile(r'<a\s[^>]*href="([^"]+)"', re.I)
# A wikilink that survived into the HTML means the plugin could not resolve it: the
# reader sees literal [[Name]] text where a link belongs.
WIKILINK_LEFTOVER = re.compile(r"\[\[([^\]]+)\]\]")


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#"))


def site_base_path(repo: Path) -> str:
    """The URL prefix the site is served under, from mkdocs.yml site_url.

    GitHub Pages serves this project under /OpenInsurance/, so root-relative hrefs in the
    built HTML carry that prefix. Resolving them against the local build directory
    without stripping it reports every one of them as broken."""
    cfg = repo / "mkdocs.yml"
    if not cfg.is_file():
        return ""
    m = re.search(r"^site_url:\s*(\S+)", cfg.read_text(encoding="utf-8"), re.M)
    if not m:
        return ""
    path = re.sub(r"^https?://[^/]+", "", m.group(1).strip().strip("'\""))
    return path.rstrip("/")


def target_exists(site: Path, page: Path, href: str, base_path: str = "") -> bool:
    path, _ = urldefrag(unquote(href))
    if not path:
        return True
    if path.startswith("/") and base_path and path.startswith(base_path):
        path = path[len(base_path):] or "/"
    base = site if path.startswith("/") else page.parent
    target = (base / path.lstrip("/")).resolve()
    if target.is_file():
        return True
    if target.is_dir() and (target / "index.html").is_file():
        return True
    # MkDocs serves pretty URLs: /a/b/ -> a/b/index.html
    return target.with_suffix(".html").is_file()


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
    if not site.is_dir():
        print(f"[site-links] no built site at {site}. Run `mkdocs build` first.")
        return 2

    base_path = site_base_path(Path(__file__).resolve().parent.parent)
    pages = sorted(site.rglob("*.html"))
    broken: list[str] = []
    leftovers: list[str] = []
    checked = 0
    seen: set[str] = set()
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        rel = page.relative_to(site)
        for href in HREF.findall(html):
            if is_external(href):
                continue
            checked += 1
            if not target_exists(site, page, href, base_path):
                # the theme repeats the nav on every page: report each dead target once
                key = f"{rel.parent}|{href}"
                if key not in seen:
                    seen.add(key)
                    broken.append(f"{rel}: {href}")
        # only look at the rendered body, not the search index MkDocs inlines
        for m in WIKILINK_LEFTOVER.findall(html):
            if "search" not in page.name:
                leftovers.append(f"{rel}: [[{m}]]")

    print(f"[site-links] {len(pages)} pages, {checked} internal links checked")
    for b in broken[:40]:
        print(f"[site-links] BROKEN {b}")
    if len(broken) > 40:
        print(f"[site-links] ... and {len(broken) - 40} more")
    for l in leftovers[:20]:
        print(f"[site-links] UNRESOLVED WIKILINK {l}")
    if len(leftovers) > 20:
        print(f"[site-links] ... and {len(leftovers) - 20} more")

    if broken or leftovers:
        print(f"[site-links] FAIL: {len(broken)} broken link(s), "
              f"{len(leftovers)} unresolved wikilink(s)")
        return 1
    print("[site-links] OK: no broken internal links, no unresolved wikilinks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
