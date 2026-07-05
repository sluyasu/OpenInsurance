#!/usr/bin/env python
"""Grounding check: every `key_quotes[]` entry in an extraction must actually appear in
the source PDF's text. Flags ungrounded quotes as likely extraction hallucinations.

A report by default (exit 0); pass --strict to fail (exit 1) if any quote is ungrounded.

Usage: python pipeline/verify_grounding.py --country be [--strict]
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

from common import REPO, extracted_dir, read_json, load_manifest

# Normalize typographic variants so verbatim matching isn't defeated by them.
# Written with \u escapes so the file itself contains no exotic characters.
_QUOTES = str.maketrans({
    "\u2019": "'", "\u2018": "'", "\u02bc": "'",           # curly / modifier apostrophes
    "\u201c": '"', "\u201d": '"', "\u00ab": '"', "\u00bb": '"',  # smart quotes / guillemets
    "\u2014": "-", "\u2013": "-",                             # em / en dash
    "\u00a0": " ", "\u202f": " ", "\u2009": " ",             # nbsp / narrow-nbsp / thin space
})


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").translate(_QUOTES)
    return re.sub(r"\s+", " ", s).strip().lower()


def nospace(s: str) -> str:
    """Whitespace-insensitive form: neutralizes French space-before-punctuation and
    line breaks inside a quote so verbatim matching isn't defeated by layout."""
    return re.sub(r"\s+", "", norm(s))


def pdf_text(path: Path) -> str:
    try:
        import fitz
        with fitz.open(path) as doc:
            return "\n".join(page.get_text("text") for page in doc)
    except Exception:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    cc = args.country

    manifest = load_manifest(cc)
    by_url = {u: r for u, r in manifest.items()}
    text_cache: dict[str, tuple[str, str]] = {}

    total_q = grounded_q = files = files_with_issues = 0
    base = extracted_dir(cc)
    if not base.is_dir():
        print(f"[ground] no extractions for country={cc}")
        return 0

    for jf in sorted(base.glob("*/*.json")):
        obj = read_json(jf)
        if not obj:
            continue
        quotes = obj.get("key_quotes") or []
        if not quotes:
            continue
        files += 1
        url = obj.get("source_url")
        rec = by_url.get(url)
        if not rec or not rec.get("local_path"):
            print(f"[ground] {jf.name}: source PDF not in manifest, skip")
            continue
        pdf = REPO / rec["local_path"]
        if url not in text_cache:
            raw = pdf_text(pdf)
            text_cache[url] = (norm(raw), nospace(raw))
        haystack, haystack_ns = text_cache[url]

        miss = []
        for q in quotes:
            quote = q.get("quote", "") if isinstance(q, dict) else str(q)
            total_q += 1
            nq = norm(quote)
            if nq and (nq in haystack or nospace(quote) in haystack_ns):
                grounded_q += 1
            else:
                miss.append(quote[:80])
        if miss:
            files_with_issues += 1
            print(f"[ground] {jf.relative_to(REPO.parent)}: {len(miss)}/{len(quotes)} ungrounded")
            for m in miss[:3]:
                print(f"          x {m!r}")

    rate = (grounded_q / total_q * 100) if total_q else 100.0
    print(f"[ground] {files} files, {grounded_q}/{total_q} quotes grounded ({rate:.0f}%), "
          f"{files_with_issues} files with issues.")
    if args.strict and grounded_q != total_q:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
