"""Local model adapter via Ollama (no external API, no key).

Runs against a local Ollama server (default http://localhost:11434). Uses httpx so no
extra SDK is required. Good for fully-offline reproduction of the extraction.
"""

from __future__ import annotations

import os


class OllamaProvider:
    name = "local"

    def __init__(self, model: str, temperature: float = 0.0):
        self.model = model
        self.temperature = temperature
        self.host = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")

    def complete(self, system: str, prompt: str) -> str:
        try:
            import httpx
        except ImportError as e:
            raise RuntimeError("Install httpx: pip install httpx") from e

        resp = httpx.post(
            f"{self.host}/api/chat",
            json={
                "model": self.model,
                "stream": False,
                "options": {"temperature": self.temperature},
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
            },
            timeout=600.0,
        )
        resp.raise_for_status()
        return resp.json().get("message", {}).get("content", "")
