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
    _coerce_drift(obj)
    return obj


def _audience_enum(text: str) -> str | None:
    """Map a free-text audience to the schema enum, or None when it is not clear-cut.

    Only unambiguous wording is mapped, and a text naming several audiences maps to None
    rather than to whichever matches first: "Personnes physiques et morales" is not
    "particuliers", and reducing it to that would silently drop companies from the
    stated scope. "Professionnels des soins de santé (médecins, vétérinaires)" is
    likewise left unmapped, since they may practise as independants or as entreprises.

    Nothing is lost by declining: the verbatim wording is kept in target_audience_note.
    A wrong category is worse than an absent one, because only the wrong one is read as
    a fact about the product."""
    t = text.lower()
    signals = set()
    if re.search(r"ind[ée]pendant", t) or "profession lib" in t:
        signals.add("independants")
    if "secteur public" in t or "service public" in t or "commune" in t:
        signals.add("secteur_public")
    if re.search(r"particuliers?\b", t) or re.search(r"personnes?\s+physiques?", t) \
            or re.search(r"propri[ée]taires?\b", t) or "consommateur" in t:
        signals.add("particuliers")
    # `morale` on its own, not `personne morale`: the common wording is "personnes
    # physiques et morales", where the noun is shared and a stricter pattern misses it.
    if re.search(r"entreprises?\b", t) or re.search(r"\bpme\b", t) \
            or re.search(r"\bmorales?\b", t) or re.search(r"soci[ée]t[ée]s?\b", t):
        signals.add("entreprises")
    return signals.pop() if len(signals) == 1 else None


def _coerce_drift(obj: dict) -> dict:
    """Shapes that models emit and the schema rejects.

    This ran only in the sidecar harness used for bulk ingestion, so the committed
    pipeline could not reproduce its own dataset: re-extracting through extract.py
    produced schema-invalid objects that the sidecar would have fixed. Rule 7 wants one
    path, so it lives here now."""
    ta = obj.get("target_audience")
    if isinstance(ta, str) and ta not in ("particuliers", "independants",
                                          "entreprises", "secteur_public"):
        obj["target_audience"] = _audience_enum(ta)
        obj.setdefault("target_audience_note", ta.strip())

    ded = obj.get("deductibles")
    if isinstance(ded, dict):
        desc = ded.pop("description", None)
        if desc and not ded.get("standard"):
            ded["standard"] = desc
        for k in [k for k in ded if k not in ("standard", "variable", "per_coverage", "page")]:
            ded.pop(k, None)
        # `variable` holds the wording of a variable franchise; a bare True says only
        # that one exists, which is not quotable, so it is dropped rather than invented.
        if isinstance(ded.get("variable"), bool):
            ded["variable"] = None
        pc = ded.get("per_coverage")
        if isinstance(pc, bool):
            ded["per_coverage"] = None
        elif isinstance(pc, list):
            # [{coverage, amount}, ...] -> {coverage: amount}
            out = {}
            for it in pc:
                if isinstance(it, dict):
                    k = it.get("coverage") or it.get("name") or it.get("garantie")
                    v = it.get("amount") or it.get("limit") or it.get("value")
                    if k:
                        out[str(k)] = _flatten_str(v) if v is not None else ""
                elif isinstance(it, str):
                    out[it] = ""
            ded["per_coverage"] = out or None
        elif isinstance(pc, dict):
            ded["per_coverage"] = {k: (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
                                   for k, v in pc.items()}
    elif isinstance(ded, str):
        obj["deductibles"] = {"standard": ded}

    # gaps are plain strings in the schema; some models emit {description, page}
    gaps = obj.get("gaps")
    if isinstance(gaps, list):
        flat = []
        for g in gaps:
            if isinstance(g, str):
                flat.append(g)
            elif isinstance(g, dict):
                d = g.get("description") or g.get("note") or _flatten_str(g)
                pg = g.get("page")
                flat.append(f"{d} (p. {pg})" if pg else str(d))
            elif g is not None:
                flat.append(_flatten_str(g))
        obj["gaps"] = flat

    # `restrictions` is not a schema field, but models occasionally emit one holding real
    # coverage limitations. Fold it into special_conditions rather than drop extracted
    # content; the wording is carried over untouched.
    extra = obj.pop("restrictions", None)
    if isinstance(extra, list) and extra:
        sc = obj.get("special_conditions")
        obj["special_conditions"] = (sc if isinstance(sc, list) else []) + [
            {k: v for k, v in it.items() if k in ("name", "description", "page", "applies_to")}
            if isinstance(it, dict) else {"description": _flatten_str(it)}
            for it in extra]

    dc = obj.get("duration_and_cancellation")
    if isinstance(dc, dict) and isinstance(dc.get("tacit_renewal"), str):
        t = dc["tacit_renewal"].lower()
        dc["tacit_renewal"] = True if any(w in t for w in
                                          ("tacit", "reconduit", "reconduc", "renouvel", "prorog")) else None

    pp = obj.get("prescription_period")
    if isinstance(pp, dict):
        if pp.get("duration") and not pp.get("description"):
            pp["description"] = pp["duration"]
        for k in [k for k in pp if k not in ("description", "page")]:
            pp.pop(k, None)

    # coverages[].sub_limits / conditions are arrays of strings in the schema; some
    # models emit {name, limit} objects. Flatten to "name: limit".
    for cov in obj.get("coverages") or []:
        if not isinstance(cov, dict):
            continue
        for key in ("sub_limits", "conditions"):
            arr = cov.get(key)
            if arr is None:
                continue
            if not isinstance(arr, list):
                arr = [arr]
            cov[key] = [_flatten_str(x) for x in arr]
    return obj


def _flatten_str(v):
    """Coerce a sub_limit / condition item to a plain string, best effort."""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        name = v.get("name") or v.get("label") or v.get("coverage") or v.get("item")
        val = v.get("limit") or v.get("amount") or v.get("value") or v.get("sub_limit") or v.get("description")
        if name and val:
            return f"{name}: {val}"
        parts = [f"{k}: {x}" for k, x in v.items() if x is not None]
        return "; ".join(parts) if parts else json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        return "; ".join(_flatten_str(x) for x in v)
    return json.dumps(v, ensure_ascii=False)


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
            # printed and skipped used to be the whole story, so a document that never
            # made it into the wiki left no trace anywhere except a line of stdout
            print(f"[extract] missing file {pdf}, skip")
            record_gap(cc, rec, "source PDF listed in the manifest but missing on disk")
            n_fail += 1
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
            record_gap(cc, rec, f"extraction failed ({type(ex).__name__}): {str(ex)[:200]}")
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
