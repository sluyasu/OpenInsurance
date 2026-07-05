# The extraction agent

This folder is the **entire brain** of the extraction step, committed and transparent. It defines exactly what
the LLM is asked to do when turning an insurance PDF into structured data. It is **provider-agnostic**: the model
is chosen in `.env` (`LLM_PROVIDER`, `LLM_MODEL`); these prompt files never change per provider. Anyone can read
precisely what was asked and reproduce the identical extraction with their own model.

## Files

| File | Role |
|---|---|
| `SYSTEM_PROMPT.md` | The system prompt: role, mission, hard rules (max fidelity, page cites, no advice). |
| `GROUNDING_RULES.md` | Anti-hallucination discipline (appended to the system prompt). |
| `OUTPUT_SPEC.md` | The output contract: a single JSON object conforming to `schema/product.schema.json`, field by field. |
| `EXTRACTION_TASK.md` | The user-prompt template (placeholders filled per PDF by `pipeline/extract.py`). |
| `providers/` | Thin adapters implementing a common `complete(system, prompt) -> text`. |
| `VERSION` | Prompt version string. Part of the extraction cache key - **bump it when you edit any prompt file**. |

## How `extract.py` assembles the call

```
system  = SYSTEM_PROMPT.md + "\n\n" + GROUNDING_RULES.md + "\n\n" + OUTPUT_SPEC.md
prompt  = EXTRACTION_TASK.md with {placeholders} filled (raw text, insurer, branch, schema, …)
text    = provider.complete(system, prompt)      # provider chosen by .env
data    = parse first JSON object from text; validate against schema/product.schema.json
```

The LLM outputs **JSON only**. The wiki Markdown is rendered deterministically from that JSON by
`pipeline/build_wiki.py`, so pages are consistent and reproducible. Prose fidelity is preserved because the JSON
schema carries free-text `description` fields on every block plus a `key_quotes` array of verbatim text
(checked by `verify_grounding.py`).

## Reproduce with your own model

Set `LLM_PROVIDER`/`LLM_MODEL` in `.env`, then `make extract`. Different models yield slightly different
extractions, but the **task, rules and output contract are identical** - that's the point.
