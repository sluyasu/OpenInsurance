"""Shared test setup: import the MCP server module against the committed dataset.

The repo IS the dataset, so the tests run on the real committed wiki/data. Counts
grow with every ingestion batch, so tests never hardcode dataset sizes: they derive
the expected numbers from the same committed files the server reads (index_rows,
country_branches) and assert the server's aggregation matches. No fixtures to build,
no network, no LLM.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "mcp"))

import insurance_wiki_mcp as server  # noqa: E402


@pytest.fixture(scope="session")
def mcp():
    return server


def index_rows(cc: str = "be") -> list[dict]:
    """Ground truth: the committed data/<cc>/index.json rows the server aggregates."""
    return json.loads((REPO / "data" / cc / "index.json").read_text(encoding="utf-8"))


def country_branches(cc: str = "be") -> dict:
    """Ground truth: the branch taxonomy declared in sources/<cc>/_country.yml."""
    meta = yaml.safe_load((REPO / "sources" / cc / "_country.yml").read_text(encoding="utf-8"))
    return (meta or {}).get("branches", {})


def branch_without_overview(cc: str = "be"):
    """A taxonomy branch slug with no hand-authored overview page (or None if every
    branch now has one). Mirrors get_branch_overview's own file lookup (label or slug)."""
    bdir = REPO / "wiki" / cc / "branches"
    for slug, b in country_branches(cc).items():
        label = b.get("label", slug)
        if not (bdir / f"{label}.md").is_file() and not (bdir / f"{slug}.md").is_file():
            return slug
    return None


def parse_payload(text: str):
    """Parse the JSON body of a tool response, skipping the DISCLAIMER/CITATION
    header lines the tools prepend (the disclaimer itself starts with '[', so try
    every bracket until one parses)."""
    dec = json.JSONDecoder()
    for i, ch in enumerate(text):
        if ch in "[{":
            try:
                obj, _ = dec.raw_decode(text[i:])
                return obj
            except json.JSONDecodeError:
                continue
    raise AssertionError(f"no JSON payload in: {text[:200]}")
