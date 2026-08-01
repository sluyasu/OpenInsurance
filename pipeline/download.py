#!/usr/bin/env python
"""Download the PDFs declared in sources/<cc>/<insurer>.yml into data/<cc>/pdfs/.

Free stack (httpx). Resumable and idempotent: a PDF already present with a matching
checksum is skipped. Records provenance (url, sha256, bytes, pages, fetched_at) in
data/<cc>/manifest.json - the manifest is committed even though the PDFs are gitignored.

Usage: python pipeline/download.py --country be [--insurer axa]
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

import httpx

from common import (fallback_branch, insurer_configs, pdfs_dir, load_manifest,
                    save_manifest, slugify, today, REPO)

UA = "openinsurance-wiki/0.1 (+https://github.com/sluyasu/OpenInsurance; polite public-document fetcher)"


class Robots:
    """Per-origin robots.txt gate. Refuses a URL its host asks crawlers not to take.

    This project is public and its pipeline is meant to be re-run by strangers, so shipping a
    source file that points every downstream user at a disallowed path would be worse than
    shipping no source file at all. Enumerating French insurers turned this from a principle
    into a routine event: axa.fr carries `Disallow: *.pdf` over its whole 152-document library,
    static.mma.fr answers `Disallow: /` while serving 51 IPIDs, and creditmutuel.fr and acm.fr
    both disallow the only per-document GET their catalogue offers.

    An unreadable robots.txt is treated as permissive, per RFC 9309: 4xx is "unavailable" and
    the crawler may proceed, while 5xx is "unreachable" and it must not. That distinction
    matters here — macif.fr's robots.txt is 403 behind a bot shield, so its policy is genuinely
    unknown rather than restrictive, and the documents themselves sit on an unprotected path.
    """

    def __init__(self, client: httpx.Client):
        self._client = client
        self._cache: dict[str, object] = {}

    def _parser(self, url: str):
        from urllib.parse import urlsplit
        import urllib.robotparser as rp
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin in self._cache:
            return self._cache[origin]
        p = rp.RobotFileParser()
        try:
            r = self._client.get(origin + "/robots.txt")
            if r.status_code >= 500:
                p.disallow_all = True          # unreachable: assume the strictest reading
            elif r.status_code >= 400:
                p.allow_all = True             # unavailable: RFC 9309 says proceed
            else:
                p.parse(r.text.splitlines())
        except Exception:
            p.allow_all = True
        self._cache[origin] = p
        return p

    def allows(self, url: str) -> bool:
        try:
            return self._parser(url).can_fetch(UA, url)
        except Exception:
            return True


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def page_count(path: Path) -> int | None:
    try:
        import fitz
        with fitz.open(path) as doc:
            return doc.page_count
    except Exception:
        return None


def is_pdf(content: bytes, content_type: str) -> bool:
    return content[:5] == b"%PDF-" or "application/pdf" in (content_type or "").lower()


def local_path_for(cc: str, insurer: str, branch: str, url: str, product_name: str | None) -> Path:
    base = slugify(product_name) if product_name else slugify(Path(url.split("?")[0]).stem)
    # short url hash keeps distinct docs from colliding on the same slug
    h = sha256_bytes(url.encode())[:8]
    return pdfs_dir(cc) / insurer / branch / f"{base}-{h}.pdf"


def gather_entries(cc: str, only: str | None) -> list[dict]:
    entries = []
    fb = fallback_branch(cc)
    for cfg in insurer_configs(cc, only=only):
        ins = cfg.get("insurer", {})
        slug = ins.get("slug")
        for pdf in cfg.get("pdfs", []) or []:
            entries.append({
                "insurer_slug": slug,
                "insurer_name": ins.get("name"),
                "url": pdf["url"],
                "branch": pdf.get("branch") or fb,
                "document_type": pdf.get("document_type", "conditions_generales"),
                "lang": pdf.get("lang"),
                "product_name": pdf.get("product_name"),
                "edition_date": pdf.get("edition_date"),   # research hint; LLM value wins if it finds one
                "superseded": pdf.get("superseded"),        # explicit research flag (older edition)
            })
    return entries


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--insurer")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests (politeness)")
    args = ap.parse_args()
    cc = args.country

    entries = gather_entries(cc, args.insurer)
    if not entries:
        print(f"[download] no PDFs declared for country={cc}"
              f"{' insurer='+args.insurer if args.insurer else ''}. "
              f"Add `pdfs:` to sources/{cc}/<insurer>.yml (or run discover.py).")
        return 0

    manifest = load_manifest(cc)
    n_new = n_skip = n_fail = n_robots = 0

    with httpx.Client(follow_redirects=True, timeout=60.0,
                      headers={"User-Agent": UA, "Accept": "application/pdf,*/*"}) as client:
        robots = Robots(client)
        for e in entries:
            url = e["url"]
            if not robots.allows(url):
                print(f"[download] ROBOTS disallow, not fetched: {url}")
                n_robots += 1
                continue
            rec = manifest.get(url)
            if rec and rec.get("local_path"):
                local = REPO / rec["local_path"]
                # skip only when the local file really matches the recorded checksum;
                # a corrupted or truncated file gets re-downloaded
                if local.is_file() and sha256_bytes(local.read_bytes()) == rec.get("sha256"):
                    n_skip += 1
                    continue
            try:
                r = client.get(url)
                r.raise_for_status()
                content = r.content
                if not is_pdf(content, r.headers.get("content-type", "")):
                    print(f"[download] NOT a PDF (skipped): {url}")
                    n_fail += 1
                    continue
                dest = local_path_for(cc, e["insurer_slug"], e["branch"], url, e.get("product_name"))
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(content)
                manifest[url] = {
                    **e,
                    "local_path": str(dest.relative_to(REPO)),
                    "sha256": sha256_bytes(content),
                    "bytes": len(content),
                    "pages": page_count(dest),
                    "fetched_at": today(),
                    "status": "downloaded",
                }
                n_new += 1
                # Persist after each PDF, not at the end: a run interrupted at 150 of 200
                # used to lose all 150 provenance records while keeping the files on
                # disk, so the resume logic could not tell downloaded from missing.
                save_manifest(cc, manifest)
                print(f"[download] ok  {e['insurer_slug']}/{e['branch']}  {dest.name}  ({len(content)//1024} KB)")
                time.sleep(args.delay)
            except Exception as ex:
                print(f"[download] FAIL {url}: {ex}")
                n_fail += 1

    save_manifest(cc, manifest)
    print(f"[download] done: {n_new} new, {n_skip} skipped, {n_fail} failed"
          f"{f', {n_robots} robots-disallowed' if n_robots else ''}. Manifest: {len(manifest)} entries.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
