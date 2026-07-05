# Wiki conventions - canonical reference

Source of truth for how notes are structured in `wiki/`. Any agent or contributor that adds, edits, or reads
notes follows these rules. (Adapted for insurance from a general knowledge-vault convention.)

## 1. Structure

```
wiki/
├── 00 - START HERE.md              # global MOC (all countries)
└── <cc>/                            # one folder per country (ISO 3166-1 alpha-2)
    ├── 00 - <Country> MOC.md
    ├── branches/                    # hand-authored: one overview per line of insurance
    │   └── 00 - Branches MOC.md     # generated list of branches + their products
    ├── insurers/                    # generated: one page per insurer
    ├── products/<insurer>/          # generated: one page per product document
    ├── regulations/                 # hand-authored: regulator + key laws
    └── glossary/                    # hand-authored: country-specific terms

_meta/
├── README.md                        # this file
├── templates/                       # one template per note type
└── universal-glossary/              # hand-authored: insurance concepts common to all countries
```

Folders prefixed `_` sort first and stay out of the Obsidian graph by convention.

## 2. Note types

| Type | Folder | Origin | Naming |
|---|---|---|---|
| `branch` | `<cc>/branches/` | hand | `Title Case.md` (e.g. `Auto.md`) |
| `product` | `<cc>/products/<insurer>/` | **generated** | `Product Name.md` (sanitized) |
| `insurer` | `<cc>/insurers/` | **generated** | `Insurer Name.md` |
| `concept` | `_meta/universal-glossary/` + `<cc>/glossary/` | hand | `Title Case.md` |
| `regulation` | `<cc>/regulations/` | hand | `Title Case.md` |
| `moc` | folder roots | hand + generated hooks | `00 - <Scope> MOC.md` |

**Generated vs hand-authored is a hard boundary.** The generator (`pipeline/build_wiki.py`) writes ONLY
`products/` and `insurers/`. Never hand-edit a page whose frontmatter says `generated: true`; fix the data in
`data/<cc>/extracted/` and rebuild.

## 3. Frontmatter

Every note has YAML frontmatter. Common base fields: `type`, `domain: insurance`, `country`, `lang`, `tags`,
`aliases`, `date` (ISO), `freshness` (ISO), `status` (`stub|draft|ready`), `generated` (bool). Per-type extras
and full examples live in `templates/` and are validated by the `schema/*.json` contracts.

`status`: `ready` = solid enough to cite/publish · `draft` = present but incomplete · `stub` = title +
frontmatter only. `freshness` = when the content was last confirmed current (products inherit the PDF
`edition_date` too).

## 4. Wikilinks

- `[[shortest]]` form; Obsidian resolves via aliases. Never `[[full/path/Note]]`.
- Link generously; each note should have ≥1 incoming and ≥1 outgoing link (orphans are flagged by `validate.py`).
- Product pages link **up** to `[[<Branch>]]` and `[[<Insurer>]]`. Branch pages link to their `[[Regulation]]`
  and relevant `[[Glossary Term]]`s.

## 5. Internal structure

Markdown starts at **H2** (`##`) - the filename/frontmatter is the title, never an H1. Neutral, encyclopedic
tone. End hand-authored notes with `## Related` (wikilinks) and `## Sources` (URL + access date). Product page
section order is fixed by `extraction-agent/OUTPUT_SPEC.md`.

## 6. Tone & discipline

Neutral and factual. **No advice, no ranking, no sales language** (see `CLAUDE.md`). Numbers, limits and amounts
are quoted as they appear in the source. Preserve the source language of product content (FR/NL/DE) - don't
silently translate.

## 7. MOCs

Three levels: global (`wiki/00 - START HERE.md`) → country (`wiki/<cc>/00 - <Country> MOC.md`) → branch list
(`wiki/<cc>/branches/00 - Branches MOC.md`, partly generated). A MOC's frontmatter has `type: moc`.

## 8. Dates

ISO `YYYY-MM-DD` everywhere. Cite an access/fetch date with every source URL.
