"""Shared helpers for the pipeline. Pure stdlib + pyyaml so every stage stays light."""

from __future__ import annotations

import json
import os
import re
import unicodedata
from datetime import date
from pathlib import Path

import yaml

# --- paths -------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "sources"
DATA = REPO / "data"
WIKI = REPO / "wiki"
SCHEMA = REPO / "schema"
AGENT = REPO / "extraction-agent"


def country_dir(cc: str) -> Path:
    return DATA / cc


def pdfs_dir(cc: str) -> Path:
    return DATA / cc / "pdfs"


def extracted_dir(cc: str) -> Path:
    return DATA / cc / "extracted"


def manifest_path(cc: str) -> Path:
    return DATA / cc / "manifest.json"


def today() -> str:
    # date.today() is fine in scripts (not in the workflow sandbox).
    return date.today().isoformat()


# --- slugs & filenames -------------------------------------------------------

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text) or "untitled"


def safe_title(text: str) -> str:
    """Filesystem-safe page title (keeps spaces/case, strips path-hostile chars)."""
    text = text.replace("/", "-").replace("\\", "-").replace(":", " -")
    text = re.sub(r'[<>"|?*\x00-\x1f]', "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:120] or "Untitled"


# --- config loading ----------------------------------------------------------

def load_country(cc: str) -> dict:
    p = SOURCES / cc / "_country.yml"
    if not p.is_file():
        raise FileNotFoundError(f"Missing country config: {p}")
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def branch_slugs(cc: str) -> list[str]:
    return list(load_country(cc).get("branches", {}).keys())


def insurer_configs(cc: str, only: str | None = None) -> list[dict]:
    """All insurer source configs for a country (excludes _country.yml)."""
    out = []
    d = SOURCES / cc
    if not d.is_dir():
        return out
    for p in sorted(d.glob("*.yml")):
        if p.stem.startswith("_"):
            continue
        cfg = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        cfg["_path"] = str(p)
        slug = cfg.get("insurer", {}).get("slug", p.stem)
        if only and slug != only:
            continue
        out.append(cfg)
    return out


# --- json / manifest ---------------------------------------------------------

def read_json(p: Path, default=None):
    if p.is_file():
        return json.loads(p.read_text(encoding="utf-8"))
    return default


def write_json(p: Path, obj) -> None:
    """Write JSON atomically: a kill mid-write must not leave a half-file.

    The manifest and the extraction index are read by every later stage, so a truncated
    one is not a lost file but a corrupted pipeline that keeps running. Writing to a
    temporary file in the same directory and renaming means a reader sees either the old
    file or the new one, never a partial one. This matters more once runs are unattended
    on the VPS, where nobody sees the traceback."""
    p.parent.mkdir(parents=True, exist_ok=True)
    # default=str coerces YAML-parsed date objects (from frontmatter) to ISO strings.
    text = json.dumps(obj, ensure_ascii=False, indent=2, default=str) + "\n"
    tmp = p.with_name(f".{p.name}.tmp")
    try:
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, p)          # atomic within a filesystem
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def load_manifest(cc: str) -> dict:
    return read_json(manifest_path(cc), default={}) or {}


def save_manifest(cc: str, manifest: dict) -> None:
    # sort keys for a stable, diff-friendly file
    write_json(manifest_path(cc), dict(sorted(manifest.items())))


# --- resume-safe writes ------------------------------------------------------

def write_if_changed(path: Path, content: str) -> bool:
    """Write only if content differs. Returns True if it wrote. Keeps git history clean."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


# --- frontmatter -------------------------------------------------------------

def frontmatter(meta: dict) -> str:
    """Render a YAML frontmatter block. Values kept as-is (dates as strings)."""
    body = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return f"---\n{body}---\n"


def prompt_version() -> str:
    v = (AGENT / "VERSION")
    return v.read_text(encoding="utf-8").strip() if v.is_file() else "0"


def read_note(path: Path) -> tuple[dict, str]:
    """Parse a Markdown note into (frontmatter dict, body). Empty dict if no frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    try:
        meta = yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        meta = {}
    return (meta if isinstance(meta, dict) else {}), body


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def wikilinks(body: str) -> list[str]:
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(body)]
