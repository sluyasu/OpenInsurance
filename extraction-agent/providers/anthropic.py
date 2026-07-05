"""Anthropic (Claude) adapter."""

from __future__ import annotations

import os


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str, max_tokens: int = 16000, temperature: float = 0.0):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def complete(self, system: str, prompt: str) -> str:
        try:
            import anthropic
        except ImportError as e:
            raise RuntimeError('Install the SDK: pip install "anthropic>=0.40"') from e

        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set (see .env).")

        client = anthropic.Anthropic(api_key=key, max_retries=4, timeout=600.0)
        # A single extraction easily fits one call. For very long docs the caller
        # chunks; if a single call ever risks >10 min, switch to client.messages.stream().
        msg = client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(block.text for block in msg.content if getattr(block, "type", None) == "text")
