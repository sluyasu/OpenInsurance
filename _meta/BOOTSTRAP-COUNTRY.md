# Adding a country

The taxonomy is data, not code, so adding a country is configuration plus research. This
is the order that worked for Belgium, written down after the fact so the second country
costs days rather than weeks.

Nothing here requires touching `pipeline/`. If you find yourself editing pipeline code to
make a country work, that is a bug in the pipeline: open an issue instead of special-casing.

---

## 1. Establish the regulator(s), then the census

**Do not start from insurers' websites.** Start from the supervisor's official register,
because it is the only list that is authoritative and complete. Belgium's census came from
the two NBB registers (52 authorised + 43 EEA branches).

A country may have **more than one supervisor**, split by product rather than by company.
Model that split explicitly: it decides which entities you are even looking for.

Record in `_meta/<cc>-market-census.md`:

- each supervisor, what it supervises, and the URL of its register (with the date fetched)
- the entity list: legal name, trade names, whether it writes business itself or fronts
  another carrier
- for each, the note that matters later: *does it publish public documents in the target
  language, or is it a brand of someone who does?*

De-duplication is where the census pays off. Belgium taught that the same product library
can appear under several brands (one health carrier behind three names), and that a "new"
insurer is sometimes a rebrand of one already ingested. Decide, in writing, which slug owns
a document, before ingesting anything.

## 2. Write `sources/<cc>/_country.yml`

```yaml
country: <cc>
name: <Country>
regulator: <supervisor(s)>
official_languages: [fr, ...]
fallback_branch: autres        # a slug that EXISTS below; where an unmapped product lands
branches:
  <slug>:
    label: <Label as a reader would say it>
    aliases: [words, that, identify, this, branch, in, document, titles]
```

Rules learned the hard way:

- **Branch slugs are the country's own segmentation, not a translation of another
  country's.** If a branch has no equivalent elsewhere, that is a feature: it proves the
  taxonomy is data. Do not force a foreign slug onto a local product.
- `label` becomes a filename. Slashes are stripped by `safe_title`, so a label like
  `Épargne / Placement` produces a file named `Épargne et Placement`; put the full label in
  the branch page's `aliases:` so links resolve.
- `aliases` feed `discover.py`'s branch inference. Give it words that really appear in
  document titles, not concepts.
- `fallback_branch` must name a branch declared in the same file. It is validated.

## 3. Check the legal regime before publishing anything

Rule 1 (information, never advice) is not one rule: it is per jurisdiction. Establish, with
sources, what counts as advice locally, who regulates intermediation, and whether anything
about a free, source-cited, non-commercial wiki needs registration.

If the regime differs from the ones already covered, the rendered disclaimer must say so.
`render.DISCLAIMER` is currently one string; make it per-country before shipping a country
whose regime differs, rather than publishing a claim that is only true elsewhere.

Also confirm the copyright position on quoting general conditions verbatim. The project
quotes short excerpts and cites the source; check that this holds locally.

## 4. Discovery, then transcription

Per insurer, find the public document library and record it in `_meta/discovery/<slug>.md`.
Then transcribe those rows into `sources/<cc>/<slug>.yml`.

The gap between these two steps is the real bottleneck: Belgium has 58 discovery files and
25 source YAMLs, so more than half of the enumeration sits untranscribed. Transcribe as you
discover, or the backlog compounds.

Record the **fetch tier** per insurer in the source file, so an unattended run knows what
it can refresh alone:

- `plain` - plain HTTP works
- `browser` - needs a real browser or a scraping service (WAF tolerates it)
- `manual` - a WAF blocks automation; a human downloads and `register_manual.py` records
  provenance (Belgium's Allianz has been in this tier since day one, documented rather
  than faked)

## 5. One insurer end to end, before all the others

```bash
make download COUNTRY=<cc> INSURER=<slug>
# extraction: the committed agent, or the subagent harness in openinsurance-wiki-tooling/
make ground-strict COUNTRY=<cc>
make build COUNTRY=<cc> && make index COUNTRY=<cc> && make validate COUNTRY=<cc>
```

Everything must be green on one insurer before the second is downloaded. The gates that
matter: grounding at 100%, validate with zero errors including `--strict-links`, the data
layer valid against the committed schema, and a rebuild that is a zero diff.

## 6. Hand-authored layer

Generated pages are not enough to be useful. Write, at minimum:

- one branch overview per populated branch (`make validate` lists the gaps)
- the regulator page(s) and the mandatory-cover rules
- a country glossary for terms that do not exist elsewhere

**Watch for false friends.** A word shared with another covered country but meaning
something different is the dangerous case for both readers and text matching. Add such
terms to the country glossary explicitly, and check `schema/coverage_categories.json`:
categories may need *enrichment* per country, not translation.

## 7. Wire it in

- `wiki/<cc>/00 - <Country> MOC.md` with a `<!-- BEGIN GENERATED: insurers -->` block
- add the country to the homepage `wiki/00 - START HERE.md`
- CI already loops over `sources/*/`, so the new country is gated from its first commit

## Checklist

- [ ] census from the official register(s), with de-duplication decided in writing
- [ ] `_country.yml` with branches, aliases, `fallback_branch`
- [ ] legal regime checked; disclaimer accurate for this country
- [ ] discovery files, transcribed into source YAML, with a fetch tier each
- [ ] one insurer green end to end
- [ ] branch overviews, regulator pages, glossary (false friends included)
- [ ] country MOC and homepage entry
- [ ] `make validate COUNTRY=<cc>` clean, rebuild a zero diff
