#!/usr/bin/env python
"""Check whether the source PDFs behind the wiki are still live and unchanged.

Report-only: sends a HEAD request for every manifest URL and compares HTTP status
and Content-Length against the recorded download. Prints a Markdown report and
always exits 0 - the monthly workflow turns a non-empty Changed/Gone section into
a GitHub issue. No LLM, no re-download: acting on the report stays a human call.

Usage: python pipeline/check_freshness.py --country be [--timeout 20]
"""

from __future__ import annotations

import argparse
import sys

import httpx

from common import load_manifest

UA = "openinsurance-wiki/0.1 (+https://github.com/sluyasu/OpenInsurance; polite public-document fetcher)"

# Statuses that mean "our fetcher is refused", not "the document is gone"
BLOCKED_STATUSES = {401, 403, 405, 406, 429}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--timeout", type=float, default=20.0)
    args = ap.parse_args()

    manifest = load_manifest(args.country)
    if not manifest:
        print(f"No manifest for country={args.country}; nothing to check.")
        return 0

    ok, changed, gone, blocked = [], [], [], []
    with httpx.Client(follow_redirects=True, timeout=args.timeout,
                      headers={"User-Agent": UA, "Accept": "application/pdf,*/*"}) as client:
        for url, rec in sorted(manifest.items()):
            try:
                r = client.head(url)
                if r.status_code in BLOCKED_STATUSES:
                    blocked.append((url, f"HTTP {r.status_code} (fetcher refused; not necessarily gone)"))
                elif r.status_code >= 400:
                    gone.append((url, f"HTTP {r.status_code}"))
                else:
                    clen = r.headers.get("content-length")
                    if clen and rec.get("bytes") and int(clen) != rec["bytes"]:
                        changed.append((url, f"size {rec['bytes']} -> {clen} bytes (new edition?)"))
                    else:
                        ok.append(url)
            except Exception as ex:
                blocked.append((url, f"{type(ex).__name__}: {ex}"))

    print(f"# Source freshness - {args.country}\n")
    print(f"{len(ok)} unchanged, {len(changed)} changed, {len(gone)} gone, "
          f"{len(blocked)} unreachable/blocked (of {len(manifest)} sources)\n")
    sections = (("## Changed (re-download + re-extract candidates)", changed),
                ("## Gone (link dead or moved; find the new URL)", gone),
                ("## Unreachable or blocked (check manually)", blocked))
    for title, rows in sections:
        if rows:
            print(title + "\n")
            for url, note in rows:
                rec = manifest.get(url, {})
                print(f"- `{rec.get('insurer_slug', '?')}` / {rec.get('branch', '?')}: {url}\n  {note}")
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
