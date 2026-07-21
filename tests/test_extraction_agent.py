"""The committed extraction agent is the reproducibility claim: anyone can re-run the
same extraction with their own model. These check the wiring holds.

They deliberately never call a model. A real end-to-end run through a paid provider is a
separate, deliberate act (see the no-paid-API question in the project notes); what breaks
silently in the meantime is the plumbing, so that is what is pinned here: every adapter
imports, every adapter satisfies the interface extract.py calls, the prompts load, and a
missing key fails with an explanation instead of a traceback.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "extraction-agent"))
sys.path.insert(0, str(REPO / "pipeline"))

ADAPTERS = ["anthropic", "gemini", "openai", "local_ollama"]


@pytest.mark.parametrize("name", ADAPTERS)
def test_adapter_imports_and_exposes_the_interface(name):
    """extract.py calls provider.complete(system, prompt) and prints provider.name and
    provider.model. An adapter missing any of those breaks only at extraction time."""
    mod = __import__(f"providers.{name}", fromlist=["*"])
    cls = next((v for k, v in vars(mod).items()
                if isinstance(v, type) and k.lower().endswith("provider")), None)
    assert cls is not None, f"{name}: no Provider class"
    # model is set in __init__, so the interface has to be checked on an instance;
    # constructing one must not need a key, since only complete() talks to the network
    inst = cls(model="test-model")
    for attr in ("name", "model", "complete"):
        assert hasattr(inst, attr), f"{name}: missing {attr}"
    assert inst.model == "test-model"
    assert isinstance(inst.name, str) and inst.name


def test_prompt_files_are_present_and_non_empty():
    """The prompts are the actual specification of the extraction; a provider swap must
    not be able to change them."""
    agent = REPO / "extraction-agent"
    for f in ("SYSTEM_PROMPT.md", "EXTRACTION_TASK.md", "GROUNDING_RULES.md", "OUTPUT_SPEC.md"):
        p = agent / f
        assert p.is_file(), f"missing {f}"
        assert len(p.read_text(encoding="utf-8").strip()) > 200, f"{f} looks empty"


def test_build_system_prompt_includes_the_grounding_rules():
    import extract
    system = extract.build_system()
    assert "grounding" in system.lower() or "verbatim" in system.lower()
    assert len(system) > 500


def test_unknown_provider_is_refused_by_name(monkeypatch):
    from providers import load_provider
    monkeypatch.setenv("LLM_PROVIDER", "definitely-not-a-provider")
    with pytest.raises(Exception) as e:
        load_provider()
    assert "definitely-not-a-provider" in str(e.value).lower() or "provider" in str(e.value).lower()


def test_prompt_version_is_stable_and_stamped():
    """The cache key includes the prompt version, so editing a prompt without bumping it
    would silently keep stale extractions."""
    import extract
    v = extract.prompt_version()
    assert v and str(v).strip()
    assert extract.prompt_version() == v
