#!/usr/bin/env python
"""Discover PDF URLs from insurers' public listing pages and write them into the
source config's `pdfs:` list. Free stack: httpx first, Playwright fallback for
JS-rendered pages. Optional - you can also hand-fill `pdfs:` directly.

Usage: python pipeline/discover.py --country be [--insurer axa]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
import yaml

from common import fallback_branch_of, insurer_configs, load_country

UA = "openinsurance-wiki/0.1 (+https://github.com/sluyasu/OpenInsurance; polite public-document fetcher)"


def branch_aliases(cc: str) -> dict[str, str]:
    """keyword -> branch slug, from the country taxonomy labels + aliases."""
    out = {}
    for slug, meta in load_country(cc).get("branches", {}).items():
        out[slug] = slug
        for alias in [meta.get("label", "")] + (meta.get("aliases") or []):
            for tok in str(alias).lower().split():
                if len(tok) >= 4:
                    out.setdefault(tok, slug)
    return out


def guess_branch(text: str, aliases: dict[str, str], fallback: str) -> str:
    """`fallback` comes from the country manifest, never a hardcoded Belgian slug."""
    t = text.lower()
    for kw, slug in aliases.items():
        if kw in t:
            return slug
    return fallback


def guess_doc_type(text: str) -> str:
    t = text.lower()
    if "ipid" in t:
        return "ipid"
    if "particuli" in t:
        return "conditions_particulieres"
    return "conditions_generales"


def guess_lang(url: str, langs: list[str]) -> str | None:
    u = url.lower()
    for lg in langs:
        if f"/{lg}/" in u or f"-{lg}." in u or f"_{lg}." in u or f"={lg}" in u:
            return lg
    return langs[0] if langs else None


def fetch_html(url: str, render: str | None) -> str:
    if render != "playwright":
        try:
            r = httpx.get(url, follow_redirects=True, timeout=45.0, headers={"User-Agent": UA})
            r.raise_for_status()
            html = r.text
            if ".pdf" in html.lower() or render == "httpx":
                return html
        except Exception as ex:
            print(f"[discover] httpx failed for {url}: {ex}; trying Playwright…")
    # Playwright fallback
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[discover] Playwright not installed (run `make setup`). Skipping JS render.")
        return ""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(user_agent=UA)
            page.goto(url, wait_until="networkidle", timeout=60000)
            html = page.content()
            browser.close()
            return html
    except Exception as ex:
        # one broken/slow listing page must not kill the whole discover run
        print(f"[discover] Playwright failed for {url}: {ex}; skipping this page")
        return ""


def extract_pdf_links(html: str, base_url: str, selector: str | None) -> list[tuple[str, str]]:
    """Return [(absolute_url, link_text)] for PDF links."""
    from selectolax.parser import HTMLParser
    tree = HTMLParser(html)
    nodes = tree.css(selector) if selector else tree.css("a[href]")
    out = []
    for a in nodes:
        href = a.attributes.get("href", "")
        if not href or ".pdf" not in href.lower():
            continue
        url = urljoin(base_url, href)
        text = (a.text() or "") + " " + href
        out.append((url.split("#")[0], text))
    # dedup preserving order
    seen, uniq = set(), []
    for u, t in out:
        if u not in seen:
            seen.add(u)
            uniq.append((u, t))
    return uniq


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", required=True)
    ap.add_argument("--insurer")
    args = ap.parse_args()
    cc = args.country
    aliases = branch_aliases(cc)
    fb = fallback_branch_of(load_country(cc))

    total_new = 0
    for cfg in insurer_configs(cc, only=args.insurer):
        path = Path(cfg["_path"])
        langs = cfg.get("languages", [])
        selectors = (cfg.get("selectors") or {})
        existing = {p["url"] for p in (cfg.get("pdfs") or [])}
        found: list[dict] = []
        for lp in cfg.get("listing_pages", []) or []:
            html = fetch_html(lp["url"], lp.get("render"))
            if not html:
                continue
            for url, text in extract_pdf_links(html, lp["url"], selectors.get("pdf_link")):
                if url in existing:
                    continue
                existing.add(url)
                found.append({
                    "url": url,
                    "branch": guess_branch(text, aliases, lp.get("branch") or fb),
                    "document_type": guess_doc_type(text),
                    "lang": lp.get("lang") or guess_lang(url, langs),
                })
        if found:
            cfg_out = {k: v for k, v in cfg.items() if not k.startswith("_")}
            cfg_out.setdefault("pdfs", [])
            cfg_out["pdfs"].extend(found)
            path.write_text(yaml.safe_dump(cfg_out, allow_unicode=True, sort_keys=False), encoding="utf-8")
            print(f"[discover] {cfg['insurer']['slug']}: +{len(found)} PDFs -> {path.name}")
            total_new += len(found)
        else:
            print(f"[discover] {cfg['insurer']['slug']}: no new PDFs found")

    print(f"[discover] done: {total_new} new PDF URLs. Review the configs, then `make download`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
