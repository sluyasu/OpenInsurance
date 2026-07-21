# Switzerland - market census

Authoritative entity list for `sources/ch/`. Every URL below was fetched on **2026-07-21**
and its HTTP status recorded. Counts are observations, not estimates.

## Two supervisors, split by activity

The boundary is **by activity, not by legal entity**. The same company can be
OFSP-supervised for its LAMal book and FINMA-supervised for its LCA book, so the census
has to join both registers rather than pick one.

**LSA (RS 961.01)** art. 2 al. 2 let. b, verbatim:

> Ne sont pas soumis à la surveillance au sens de la présente loi: [...] b. les entreprises
> d'assurance dont l'activité en matière d'assurance est soumise à une surveillance
> particulière en vertu du droit fédéral, **dans la mesure de la surveillance exercée sur
> cette activité**

That closing clause is the boundary: social health insurance is carved out of FINMA's
remit *only to the extent* it is separately supervised.

**LSAMal (RS 832.12)**:

- art. 2 al. 2: caisses-maladie may also write supplementary cover, and "**Toutes ces
  assurances sont régies par la loi du 2 avril 1908 sur le contrat d'assurance**" (LCA).
- art. 4 al. 2: "**Elle publie la liste des assureurs admis.**"

So: **OFSP** = the LAMal/AOS social layer. **FINMA** = everything under the LCA, including
supplementary health.

## Registers

| Source | URL | Fetched | Contents |
|---|---|---|---|
| FINMA, PDF | `https://www.finma.ch/fr/~/media/finma/dokumente/bewilligungstraeger/pdf/vu.pdf?la=fr` | 200, `%PDF`, 422 KB | 190 insurers, 8 pp |
| FINMA, XLSX | `https://www.finma.ch/fr/~/media/finma/dokumente/bewilligungstraeger/xlsx/vu.xlsx?la=fr` | 200, 149 KB | same 190, 211 rows |
| FINMA, CSV | `https://www.finma.ch/fr/~/media/finma/dokumente/bewilligungstraeger/csv/uid.csv?la=fr` | 200, `text/csv`, 464 KB | all licensees, 2929 rows, **with UID** |
| OFSP | `https://www.bag.admin.ch/fr/listes-des-assureurs-et-des-reassureurs-autorises` | 200 | landing page, archive back to 2022 |
| OFSP, XLSX | `.../dam/fr/sd-web/wKeV97535ICf/Zugelassene%20Krankenversicherer_1.1.2026.xlsx` | 200, 49.6 KB | **37** health insurers, with UID |
| OFSP, XLSX | `.../dam/fr/sd-web/0CGTd62Qowhy/Liste_Zugelassene_R%C3%BCckversicherer_1.1.2026.xlsx` | 200, 30.5 KB | 7 reinsurers |

The FINMA files are regenerated daily (the PDF footer carried `21.07.2026 / 04:31`), and
`?la=fr|de|it|en` switches language on the same path.

**Neither FINMA file is the census on its own.** Measured: `uid.csv` holds 170 insurance
entities against 190 in `vu.xlsx`. The 20-entity gap is exactly the 19 marked
`*` = "En cessation d'activité (RunOff)" plus one in liquidation. So `vu.xlsx` is complete
but has no join key, `uid.csv` carries the CHE-xxx.xxx.xxx UID but drops run-off entities.
Join them on normalised name; the UID is the clean key to OFSP.

`vu.xlsx` breakdown (190): 96 assureurs dommage, 27 captives de réassurance, 22 réassureurs
professionnels, 18 assureurs-vie, 18 assureurs-maladie, 9 caisses maladie.

`uid.csv` also lists 6 `Groupe d'assurance` entries (Helvetia Baloise Holding, Schweizerische
Mobiliar Holding, Swiss Life Holding, Swiss Re, Zurich Insurance Group, SIEP Holding).
These are group holdings, not carriers: exclude them from a carrier census.

**OFSP parsing traps, both measured:**

- The data is in **sheet 3** (`Zugelassene Krankenversicherer`), not sheet 1, which is a
  `Deckblatt` cover page. A naive parser reads the cover and finds nothing.
- **37 is not the number of basic-cover insurers.** The PDF legend defines the `x` flag:
  "Assureur qui ne pratique que l'assurance d'indemnités journalières." Five carry it, so
  the corpus is **32 LAMal basic-cover (AOS) insurers + 5 daily-allowance-only**. Quote 32
  when describing Swiss basic health cover.
- Columns are trilingual DE/FR/IT inside single cells, and a `Gruppe` column is already
  populated (`Groupe Mutuel`, `Visana`): free group-affiliation data for de-duplication.
- The files are versioned at 01.01 each year, not continuously updated.

**Intermediary register is a partial blocker.** FINMA keeps the public register of
"intermédiaires d'assurance non liés" (LSA art. 42) at
`https://www.finma.ch/fr/surveillance/versicherungsvermittler/registersuche/`, but it is a
search-only web app with a 3-character minimum and **no bulk export**. Not needed to build
the product census; noted so nobody re-derives the dead end.

## Ingestion shortlist

Ranked by "public French CGA library, reachable without a browser, high consumer value".
PDF URLs in tiers 1 and 2 were spot-checked to return `%PDF` magic bytes.

**Tier 1 - central FR CGA hub, plain HTTP works**

| Insurer | Kind | Hub | FR PDFs |
|---|---|---|---|
| Sanitas | health | `/fr/clients-prives/services/aide/documents-et-telechargements/conditions-generales-d-assurance.html` | 76 |
| Helsana | health | `/fr/prives/services/documents-et-telechargements/conditions-assurance.html` | 42 |
| **Vaudoise** | non-life | `/fr/a-notre-propos/courtiers/documentations/conditions-generales-assurance` | 34 |
| TCS / Assista | non-life | `/fr/produits/cga` | 27 |
| CSS | health | `/fr/clients-prives/vite-regle/faire-soi-meme/commande/cga.html` | 26 |

**Tier 2 - no central hub, per-product discovery needed**: Assura, Groupe Mutuel,
Generali Suisse, Allianz Suisse, AXA Suisse, SWICA, Concordia. Assura and Groupe Mutuel are
Romandy-native (Vaud / Valais), so French is the source language rather than a translation.

**Tier 3 - needs a renderer**: Mobilière (hub returns 200 but zero `.pdf` in raw HTML; PDFs
are served extension-less as `/media/<id>/download` and do work on curl, so a
content-type-based filename fallback is needed), Zurich Suisse (CGA not in raw HTML;
**`?sc_lang=fr` is the language selector, dropping it silently yields German**).

**Blocked - do not schedule**: Helvetia. `helvetia.com` returns 504 in 0.37 s to plain curl
on HTML and on PDFs alike; that speed is active rejection, not a timeout, and the site
carries FriendlyCaptcha. Firecrawl reads the HTML and exposes CGA URLs, but no PDF could be
downloaded. This is Switzerland's Allianz: recorded as a blocker rather than faked.

## Legal position (see also CLAUDE.md rule 1)

The Swiss trigger for intermediary regulation is **economic interest in a contract being
concluded**, not comparison. **OS (RS 961.011) art. 182a al. 3, verbatim:**

> **Les personnes qui fournissent uniquement des données ou des informations ne sont pas
> considérées comme des intermédiaires d'assurance.**

Art. 182a al. 2 catches ranking and price comparison, but only for persons who "**ont un
intérêt économique** à proposer ou à conclure un contrat". FINMA states it plainly: "La
simple mise à disposition de données ou d'informations n'est par contre pas considérée
comme de l'intermédiation en assurance."

Consequence for this project: its Swiss safety rests on **not monetising**, not on avoiding
comparison. Comparis is a registered intermediary (FINMA register F01093895) because it
monetises hand-offs. priminfo is the state comparator publishing as the supervisor itself,
so it is not a precedent a private wiki can borrow.

**Quoting general conditions**: LDA (RS 231.1) art. 25 allows citation "dans la mesure où
elles servent de commentaire, de référence ou de démonstration" and where "leur emploi en
justifie l'étendue", and art. 25 al. 2 requires naming **the source and the author**. There
is no word-count safe harbour: the test is purpose and proportionality, so reproducing a
complete set of general conditions would fail even with perfect attribution. Structured
extraction with cited excerpts, which is what this project does, fits. Swiss statutory and
regulatory material (LSA, OS, FINMA circulars, court decisions) is free of copyright under
art. 5 and may be reproduced in full; insurers' CG get no such exemption.
