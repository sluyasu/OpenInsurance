"""Google Gemini adapter (google-genai SDK)."""

from __future__ import annotations

import os


def _gemini_key() -> str | None:
    # Env key casing is inconsistent in the wild - accept the common variants.
    for k in ("GEMINI_API_KEY", "Gemini_API_KEY", "GOOGLE_API_KEY"):
        v = os.environ.get(k)
        if v:
            return v
    return None


class GeminiProvider:
    name = "gemini"

    def __init__(self, model: str, max_tokens: int = 16000, temperature: float = 0.0):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def complete(self, system: str, prompt: str) -> str:
        try:
            from google import genai
            from google.genai import types
        except ImportError as e:
            raise RuntimeError('Install the SDK: pip install "google-genai>=0.3"') from e

        key = _gemini_key()
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not set (see .env).")

        client = genai.Client(api_key=key)
        resp = client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=self.temperature,
                max_output_tokens=self.max_tokens,
            ),
        )
        return resp.text or ""
