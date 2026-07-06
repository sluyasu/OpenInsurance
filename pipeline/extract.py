#!/usr/bin/env python
"""Extract downloaded PDFs into structured JSON via the committed extraction agent.

Pipeline: PDF -> PyMuPDF page-annotated text -> LLM (extraction-agent prompts, provider
chosen by .env) -> JSON validated against schema/product.schema.json.

Resumable: an already-extracted PDF is skipped when its source checksum and the prompt
version are unchanged (change a prompt -> bump extraction-agent/VERSION -> re-extracts).

Usage:
  python pipeline/extract.py --country be [--insurer axa] [--limit N] [--url <one pdf url>]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from common import (AGENT, SCHEMA, REPO, country_dir, load_manifest, extracted_dir,
                    read_json, write_json, slugify, branch_slugs, prompt_version, today)

# Make the hyphenated extraction-agent/providers package importable.
sys.path.insert(0, str(AGENT))
from providers import load_provider  # noqa: E402

SCHEMA_VERSION = "1.0"
MAX_TEXT_CHARS = 240_000  # single-call guard; longer docs get a truncation note in `gaps`


def pdf_text_with_pages(path: Path) -> tuple[str, int]:
    import fitz
    parts = []
    with fitz.open(path) as doc:
        n = doc.page_count
        for i, page in enumerate(doc, start=1):
            txt = page.get_text("text")
            parts.append(f"[[page {i}]]\n{txt}")
    return "\n".join(parts), n


def build_system() -> str:
    def rd(name):
        return (AGENT / name).read_text(encoding="utf-8").strip()
    return "\n\n".join([rd("SYSTEM_PROMPT.md"), rd("GROUNDING_RULES.md"), rd("OUTPUT_SPEC.md")])


def build_prompt(rec: dict, raw_text: str, cc: str, pv: str) -> str:
    tmpl = (AGENT / "EXTRACTION_TASK.md").read_text(encoding="utf-8")
    return tmpl.format(
        country=cc,
        insurer_slug=rec.get("insurer_slug", ""),
        insurer_name=rec.get("insurer_name", ""),
        branch=rec.get("branch", ""),
        document_type=rec.get("document_type", ""),
        language=rec.get("lang", "") or "",
        source_url=rec.get("url", ""),
        source_pages=rec.get("pages", "") or "",
        prompt_version=pv,
        schema_version=SCHEMA_VERSION,
        branch_slugs=", ".join(branch_slugs(cc)),
        raw_text=raw_text,
    )


def parse_json_object(text: str) -> dict:
    text = text.strip()
    # strip ```json fences if present
    fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object in model output")
    return json.loads(text[start:end + 1])


def normalize(obj: dict) -> dict:
    """Coerce common model-drift shapes to the canonical schema shapes, so render.py
    and verify_grounding.py always see consistent data regardless of which LLM ran."""
    # list-of-strings -> list-of-dicts for the array fields (some models emit bare strings)
    _namekey = {"definitions": "term"}
    for field in ("definitions", "coverages", "exclusions", "obligations",
                  "waiting_periods", "claims_procedure", "special_conditions"):
        v = obj.get(field)
        if isinstance(v, list):
            nk = _namekey.get(field, "name") if field != "waiting_periods" else "description"
            obj[field] = [x if isinstance(x, dict) else {nk: str(x)} for x in v]
    # key_quotes: bare strings -> {"quote": s}; alternate field names (text/content/value) -> quote
    kq = obj.get("key_quotes")
    if isinstance(kq, list):
        fixed = []
        for q in kq:
            if isinstance(q, str):
                fixed.append({"quote": q})
            elif isinstance(q, dict):
                if not q.get("quote"):
                    for alt in ("text", "content", "value"):
                        if q.get(alt):
                            q["quote"] = q.pop(alt)
                            break
                fixed.append(q)
        obj["key_quotes"] = fixed
    # duration_and_cancellation: string list-fields -> [string]; 'notice' -> 'notice_period'
    dc = obj.get("duration_and_cancellation")
    if isinstance(dc, dict):
        if "notice" in dc and not dc.get("notice_period"):
            dc["notice_period"] = dc.pop("notice")
        for k in ("methods", "special_rights"):
            if isinstance(dc.get(k), str):
                dc[k] = [dc[k]]
    # prescription_period / premium sometimes come back as bare strings
    if isinstance(obj.get("prescription_period"), str):
        obj["prescription_period"] = {"description": obj["prescription_period"]}
    if isinstance(obj.get("premium"), str):
        obj["premium"] = {"notes": [obj["premium"]]}
    return obj


def validate(obj: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []  # validation optional if lib missing
    schema = read_json(SCHEMA / "product.schema.json")
    v = jsonschema.Draft202012Validator(schema)
    return [f"{'/'.join(map(str, e.path))}: {e.message}" for e in v.iter_errors(obj)]


def out_path(cc: str, rec: dict, product_name: str) -> Path:
    # Unique & stable per source PDF: a product_name alone collides (e.g. a product's
    # CG and IPID share the same commercial name). The url hash disambiguates.
    h = hashlib.sha256(rec.get("url", "").encode()).hexdigest()[:8]
    base = slugify(product_name) if product_name else f"{rec.get('branch','')}-{rec.get('document_type','')}"
    return extracted_dir(cc) / rec["insurer_slug"] / f"{base}-{h}.json"


def find_existing(cc: str, rec: dict) -> Path | None:
    """A previous extraction for this source PDF, whatever product name the model chose
    for the filename: the url-hash suffix is the stable key."""
    h = hashlib.sha256(rec.get("url", "").encode()).hexdigest()[:8]
    d = extracted_dir(cc) / rec.get("insurer_slug", "")
    if not d.is_dir():
        return None
    hits = sorted(d.glob(f"*-{h}.json"))
    return hits[0] if hits else None


def record_gap(cc: str, rec: dict, reason: str) -> None:
    """Persist an extraction gap in data/<cc>/gaps.json (gaps are labeled, not hidden)."""
    p = country_dir(cc) / "gaps.json"
    gaps = read_json(p, default={}) or {}
    gaps[rec.get("url") or rec.get("local_path", "?")] = {
        "insurer_slug": rec.get("insurer_slug"), "branch": rec.get("branch"),
        "document_type": rec.get("document_type"), "reason": reason, "recorded_at": today()}
    write_json(p, dict(sorted(gaps.items())))


def clear_gap(cc: str, rec: dict) -> None:
    p = country_dir(cc) / "gaps.json"
    gaps = read_json(p, default={}) or {}
    if gaps.pop(rec.get("url"), None) is not None:
        write_json(p, dict(sorted(gaps.items())))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--insurer")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--url", help="extract only this one PDF url (smoke test)")
    args = ap.parse_args()
    cc = args.country
    pv = prompt_version()

    manifest = load_manifest(cc)
    items = [r for r in manifest.values() if r.get("local_path")]
    if args.insurer:
        items = [r for r in items if r.get("insurer_slug") == args.insurer]
    if args.url:
        items = [r for r in items if r.get("url") == args.url]
    items.sort(key=lambda r: (r.get("insurer_slug", ""), r.get("branch", ""), r.get("url", "")))
    if args.limit:
        items = items[: args.limit]

    if not items:
        print(f"[extract] nothing to extract (country={cc}). Run download first.")
        return 0

    provider = None  # lazily created so `--limit 0` / all-cached runs need no key
    n_new = n_skip = n_fail = 0

    for rec in items:
        pdf = REPO / rec["local_path"]
        if not pdf.is_file():
            print(f"[extract] missing file {pdf}, skip")
            continue

        # cache check: any existing extraction for this source url (same checksum +
        # prompt version). Looked up by the url-hash suffix, NOT by product name -
        # the model's chosen name rarely matches the preliminary one from sources/.
        prelim_name = rec.get("product_name") or Path(rec["local_path"]).stem
        candidate = find_existing(cc, rec)
        existing = read_json(candidate) if candidate else None
        if existing and existing.get("source_sha256") == rec.get("sha256") \
                and existing.get("prompt_version") == pv:
            n_skip += 1
            continue

        raw_text, pages = pdf_text_with_pages(pdf)
        if not raw_text.strip():
            print(f"[extract] no text layer (scanned?) -> {pdf.name}; recording gap, skip")
            record_gap(cc, rec, "no text layer (scanned PDF?); extraction needs OCR")
            n_fail += 1
            continue
        truncated = len(raw_text) > MAX_TEXT_CHARS
        if truncated:
            raw_text = raw_text[:MAX_TEXT_CHARS]

        if provider is None:
            provider = load_provider()
        try:
            system = build_system()
            prompt = build_prompt(rec, raw_text, cc, pv)
            print(f"[extract] {rec['insurer_slug']}/{rec['branch']}  {pdf.name}  "
                  f"({pages}p, {len(raw_text)//1000}k chars) via {provider.name}:{provider.model}")
            out = provider.complete(system, prompt)
            obj = parse_json_object(out)
        except Exception as ex:
            print(f"[extract] FAIL {pdf.name}: {ex}")
            n_fail += 1
            continue

        # authoritatively stamp provenance/metadata (don't trust the model to echo perfectly)
        obj.update({
            "schema_version": SCHEMA_VERSION,
            "prompt_version": pv,
            "country": cc,
            "insurer_slug": rec.get("insurer_slug"),
            "insurer_name": rec.get("insurer_name") or obj.get("insurer_name"),
            "branch": obj.get("branch") if obj.get("branch") in branch_slugs(cc) else rec.get("branch"),
            "document_type": rec.get("document_type") or obj.get("document_type"),
            "language": rec.get("lang") or obj.get("language"),
            "edition_date": obj.get("edition_date") or rec.get("edition_date"),
            "superseded": obj.get("superseded") if obj.get("superseded") is not None else rec.get("superseded"),
            "source_url": rec.get("url"),
            "source_pdf": Path(rec["local_path"]).name,
            "source_sha256": rec.get("sha256"),
            "source_pages": rec.get("pages") or pages,
            "fetched_at": rec.get("fetched_at"),
            "extraction_model": f"{provider.name}:{provider.model}",
        })
        obj.setdefault("product_name", prelim_name)
        obj = normalize(obj)
        if truncated:
            obj.setdefault("gaps", []).append(
                f"source text truncated to {MAX_TEXT_CHARS} chars for a single-call extraction; "
                f"long-document chunking not yet applied")

        errors = validate(obj)
        final = out_path(cc, rec, obj["product_name"])
        write_json(final, obj)
        if candidate and candidate != final:
            candidate.unlink()  # the model's name drifted; keep one extraction per source PDF
        clear_gap(cc, rec)
        if errors:
            print(f"[extract]  ⚠ schema warnings ({len(errors)}): " + "; ".join(errors[:4]))
        print(f"[extract]  -> {final.relative_to(REPO)}  "
              f"({len(obj.get('coverages', []))} coverages, {len(obj.get('exclusions', []))} exclusions)")
        n_new += 1

    print(f"[extract] done: {n_new} extracted, {n_skip} cached, {n_fail} failed.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
