"""Provider interface + factory.

A Provider turns (system prompt, user prompt) into completion text. Nothing about the
extraction task lives here - only the transport to a given LLM. Swap providers by
editing `.env`; the prompts in extraction-agent/*.md never change.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Protocol


# --- minimal .env loader (avoids a python-dotenv dependency) -----------------

def load_dotenv(start: Path | None = None) -> None:
    """Load KEY=VALUE lines from the nearest .env up the tree into os.environ.

    Existing environment variables win (so CI / shell overrides are respected).
    """
    here = (start or Path(__file__)).resolve()
    for parent in [here, *here.parents]:
        env = parent / ".env"
        if env.is_file():
            for raw in env.read_text(encoding="utf-8").splitlines():
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key, val = key.strip(), val.strip().strip('"').strip("'")
                os.environ.setdefault(key, val)
            return


class Provider(Protocol):
    """Common interface every adapter implements."""

    name: str
    model: str

    def complete(self, system: str, prompt: str) -> str:
        """Return the model's completion text for (system, prompt)."""
        ...


def _cfg() -> dict:
    load_dotenv()
    return {
        "provider": os.environ.get("LLM_PROVIDER", "anthropic").strip().lower(),
        "model": os.environ.get("LLM_MODEL", "").strip(),
        "max_tokens": int(os.environ.get("LLM_MAX_OUTPUT_TOKENS", "16000")),
        "temperature": float(os.environ.get("LLM_TEMPERATURE", "0")),
    }


def load_provider() -> Provider:
    """Instantiate the provider selected by LLM_PROVIDER."""
    cfg = _cfg()
    provider = cfg["provider"]

    if provider == "anthropic":
        from .anthropic import AnthropicProvider
        return AnthropicProvider(model=cfg["model"] or "claude-sonnet-5",
                                 max_tokens=cfg["max_tokens"], temperature=cfg["temperature"])
    if provider == "gemini":
        from .gemini import GeminiProvider
        return GeminiProvider(model=cfg["model"] or "gemini-2.5-flash",
                              max_tokens=cfg["max_tokens"], temperature=cfg["temperature"])
    if provider == "openai":
        from .openai import OpenAIProvider
        return OpenAIProvider(model=cfg["model"] or "gpt-5",
                              max_tokens=cfg["max_tokens"], temperature=cfg["temperature"])
    if provider == "local":
        from .local_ollama import OllamaProvider
        return OllamaProvider(model=cfg["model"] or "llama3.1:70b",
                              temperature=cfg["temperature"])

    raise ValueError(
        f"Unknown LLM_PROVIDER={provider!r}. Use one of: anthropic | gemini | openai | local."
    )
