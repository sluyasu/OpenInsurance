#!/usr/bin/env python
"""Check that extractions of over-long documents actually read past the prompt's character cap.

WHY. `extract.py` pastes at most MAX_TEXT_CHARS of document text into the prompt. Forty French
documents exceed it, one by 46 % — the cap falls at page 62 of a 110-page contract, and everything
after it is the "Vie du contrat", the lexique, the annexe and the **exclusions générales**. An
extraction that stops at the cap therefore loses the largest exclusion block in the document while
looking entirely normal: it validates, every quote grounds (they are real spans of the truncated
text), and the page renders with dozens of exclusions on it.

So the pipeline's own grounding gate cannot see this, in exactly the way it cannot see a wrong page
number or a missing key_quotes block. This is the third instance of the same shape, and it is worth
naming: a gate that checks one property is silent about every other one.

THE TEST. Replay the truncation — accumulate `get_text("text")` page by page until the cap is
exceeded — then look at the page numbers the extraction actually cites. If it cites pages beyond
the cut, the worker recovered the tail from the PDF as the spec instructs. If it never does, the
extraction probably stops where the prompt stopped, and a human should look.

Usage: python pipeline/check_truncation.py --country fr [--cap 240000]
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
from pathlib import Path

import fitz

from common import load_manifest, REPO


def cut_page(pdf: Path, cap: int) -> tuple[int | None, int]:
    """(1-based page at which the cap is first exceeded, total pages)."""
    acc, cut = 0, None
    with fitz.open(pdf) as doc:
        for i, page in enumerate(doc, 1):
            acc += len(page.get_text("text"))
            if cut is None and acc > cap:
                cut = i
        return cut, doc.page_count


def cited_pages(obj: dict) -> list[int]:
    out = []
    for key in ("key_quotes", "coverages", "exclusions", "definitions"):
        for item in obj.get(key) or []:
            if isinstance(item, dict) and isinstance(item.get("page"), int):
                out.append(item["page"])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--cap", type=int, default=240_000)
    args = ap.parse_args()

    manifest = load_manifest(args.country)
    checked = recovered = 0
    suspects = []
    not_yet = 0

    for url, rec in manifest.items():
        pdf = REPO / (rec.get("local_path") or "")
        if not pdf.is_file():
            continue
        try:
            with fitz.open(pdf) as doc:
                chars = sum(len(p.get_text("text")) for p in doc)
        except Exception:
            continue
        if chars <= args.cap:
            continue

        h = hashlib.sha256(url.encode()).hexdigest()[:8]
        found = glob.glob(str(REPO / f"data/{args.country}/extracted/*/*{h}.json"))
        if not found:
            not_yet += 1
            continue

        cut, total = cut_page(pdf, args.cap)
        obj = json.load(open(found[0]))
        # If the cap falls on the LAST page there is nothing past it to cite, and flagging
        # such a document is a false positive of this check, not a finding about the extraction.
        if cut is None or cut >= total:
            continue
        beyond = [p for p in cited_pages(obj) if p > cut]
        checked += 1
        if beyond:
            recovered += 1
        else:
            suspects.append((h, rec.get("insurer_slug"), cut, total, os.path.basename(found[0])))

    print(f"[truncation] cap {args.cap:,} chars · {checked} over-long extractions checked, "
          f"{recovered} cite pages past the cut, {not_yet} not extracted yet")
    if suspects:
        print("[truncation] NO citation past the cut - check these read their tail:")
        for h, insurer, cut, total, name in suspects:
            print(f"[truncation]   {h}  {insurer:<12} cut at p.{cut}/{total}  {name[:52]}")
    else:
        print("[truncation] every over-long extraction cites past its cut.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
