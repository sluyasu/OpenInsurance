#!/usr/bin/env python
"""Flag PDFs whose text layer does not restitute everything the page draws.

WHY THIS EXISTS. On a Macif contract, `page.get_text("text")` silently dropped four whole
sections — every "Qu'est-ce qui n'est pas assuré ?" item, the entire exclusions body, the
territorial scope, and 7 of the 12 coverages — leaving only one U+0007 per lost item. The fonts
are ordinary Type1 CFF and the text IS in the content stream; PyMuPDF just would not give it
back. A naive extraction of that PDF loses essentially every exclusion, and produces a page that
looks complete. Nothing downstream can catch it: the JSON validates, the quotes ground (they are
real spans of the truncated layer), and the product page renders normally.

THE TEST. `get_texttrace()` reports the glyphs the page actually draws, straight from the content
stream. `get_text("text")` reports what the extractor restitutes. Comparing the two catches the
divergence. On this corpus the median ratio is 1.02 — extraction is slightly LONGER than the glyph
count, because it inserts spaces and newlines the content stream does not contain.

WHAT THIS IS NOT. A ratio below 1 is a SCREENING SIGNAL, not proof. Two other things depress it:
- documents with many Private-Use-Area glyphs (Wingdings bullets), which cluster tightly around
  0.68 on one insurer whose contracts are demonstrably complete (100+ coverages each);
- ligature and encoding quirks.
So this reports suspects for a human or a worker to check by rendering the page. It does not
delete, rewrite or block anything.

Usage: python pipeline/check_textlayer.py --country fr [--threshold 0.85] [--json]
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

import fitz

from common import load_manifest, REPO


def measure(path: Path) -> tuple[int, int, int]:
    """(characters restituted, glyphs drawn ON the page, glyphs drawn off-canvas).

    Only glyphs whose origin falls inside the page rectangle count. Counting all of them
    produced a false positive that cost a worker real time: a Macif protection-juridique
    document scored 0.58 — among the five worst in the corpus — purely because page 1 draws
    10 595 glyphs of which 5 619 sit OUTSIDE the page (x up to 4741, y down to −1616). They
    are leftover artwork from the publisher's design file, an executive org chart in a font
    whose encoding is shifted by +3, invisible to any reader and correctly ignored by
    `get_text`. Filtered to what is actually on the page, that document scores 1.019 — the
    corpus median — and a render confirmed its text layer is complete.
    """
    restituted = drawn = offpage = 0
    with fitz.open(path) as doc:
        for page in doc:
            restituted += len(page.get_text("text"))
            rect = page.rect
            for span in page.get_texttrace():
                for ch in span.get("chars") or []:
                    ox, oy = ch[2][0], ch[2][1]
                    if rect.x0 <= ox <= rect.x1 and rect.y0 <= oy <= rect.y1:
                        drawn += 1
                    else:
                        offpage += 1
    return restituted, drawn, offpage


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--threshold", type=float, default=0.85,
                    help="report PDFs whose restituted/drawn ratio falls below this (default 0.85)")
    ap.add_argument("--json", action="store_true", help="emit the suspect list as JSON")
    args = ap.parse_args()

    manifest = load_manifest(args.country)
    rows = []
    for url, rec in manifest.items():
        p = REPO / (rec.get("local_path") or "")
        if not p.is_file():
            continue
        try:
            restituted, drawn, offpage = measure(p)
        except Exception as e:                                    # a broken PDF is its own finding
            print(f"[textlayer] UNREADABLE {p.name}: {e}")
            continue
        if drawn < 500:                                           # too small to say anything
            continue
        rows.append({"ratio": round(restituted / drawn, 3), "restituted": restituted,
                     "drawn": drawn, "offpage": offpage, "insurer": rec.get("insurer_slug"),
                     "file": p.name, "url": url})

    if not rows:
        print("[textlayer] no PDF measured.")
        return 0

    rows.sort(key=lambda r: r["ratio"])
    median = statistics.median(r["ratio"] for r in rows)
    suspects = [r for r in rows if r["ratio"] < args.threshold]

    if args.json:
        json.dump(suspects, sys.stdout, ensure_ascii=False, indent=1)
        return 0

    print(f"[textlayer] {len(rows)} PDF measured, median ratio {median:.2f}, "
          f"{len(suspects)} below {args.threshold}")
    if suspects:
        print("[textlayer] SUSPECT - render these pages before trusting a linear extraction:")
        for r in suspects:
            off = f"  (+{r['offpage']} glyphes hors page, ignores)" if r["offpage"] else ""
            print(f"[textlayer]   {r['ratio']:.2f}  {r['insurer']:<12} {r['file'][:56]}{off}")
        print("[textlayer] A low ratio is a signal, not a verdict: PUA bullet glyphs depress it "
              "too. Check by rendering the page, not by deleting the extraction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
