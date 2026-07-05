"""Provider-agnostic LLM adapters for the extraction step.

Each adapter implements `complete(system, prompt) -> str`. The active provider is
chosen by the `LLM_PROVIDER` env var (see `.env.example`). Import `load_provider()`
to get a ready-to-use instance.
"""

from .base import Provider, load_provider

__all__ = ["Provider", "load_provider"]
