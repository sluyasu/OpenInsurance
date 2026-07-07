"""Shared test setup: import the MCP server module against the committed dataset.

The repo IS the dataset, so the tests run on the real committed wiki/data (162
extracted documents). No fixtures to build, no network, no LLM.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "mcp"))

import insurance_wiki_mcp as server  # noqa: E402


@pytest.fixture(scope="session")
def mcp():
    return server


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
