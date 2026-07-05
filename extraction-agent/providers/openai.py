"""OpenAI adapter (chat completions)."""

from __future__ import annotations

import os


class OpenAIProvider:
    name = "openai"

    def __init__(self, model: str, max_tokens: int = 16000, temperature: float = 0.0):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def complete(self, system: str, prompt: str) -> str:
        try:
            from openai import OpenAI
        except ImportError as e:
            raise RuntimeError('Install the SDK: pip install "openai>=1.40"') from e

        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not set (see .env).")

        client = OpenAI(api_key=key, max_retries=4, timeout=600.0)
        kwargs = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "max_completion_tokens": self.max_tokens,
        }
        # Some newer models only accept the default temperature - retry without it on error.
        try:
            resp = client.chat.completions.create(temperature=self.temperature, **kwargs)
        except Exception:
            resp = client.chat.completions.create(**kwargs)
        return resp.choices[0].message.content or ""
