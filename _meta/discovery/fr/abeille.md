# abeille — Abeille Assurances

website: abeille-assurances.fr
fetch: plain-urllib-only
status: enum
lang: fr
enumerated: 2026-08-01

**69 documents enumerated. None ingested: 63 of them answer 403 to this project's own User-Agent.**

`abeille-assurances.fr` serves these files to a browser User-Agent and refuses
`openinsurance-wiki/0.1 (+https://github.com/sluyasu/OpenInsurance; polite public-document fetcher)`.
Presenting a browser string to get round that is not something this project does quietly — the whole
point of a descriptive agent is that the publisher can see who is asking and decline. Six fetchable
documents out of sixty-nine, none of them a wording, would misrepresent the library rather than
document it, so the source YAML was withdrawn and the six already downloaded were removed.

Note this is a *different* obstacle from the three others in this batch. [AXA](axa.md) forbids PDFs
in `robots.txt`; [MMA](mma.md)'s serving host answers `Disallow: /`; [ACM](acm.md) offers no
permitted GET address at all. Here `robots.txt` permits everything and the block is on the client
identity. Four insurers, four different walls.

## What Abeille publishes, for whoever revisits this

**44 IPIDs, 24 contract-level PRIIPs DICs, and exactly one notice d'information** (assurance
scolaire, ref 17076). **No conditions générales at all** — every IPID says the full terms are "dans
la documentation précontractuelle et contractuelle" without linking them. The same sentence, almost
word for word, appears at ACM and MMA.

Carriers are first-party, three attributions printed in the documents: **Abeille IARD & Santé** (36),
**Abeille Vie** (31), and two AFER contracts co-insured by Abeille Vie *and* Abeille Épargne Retraite
("ci-après dénommés les « coassureurs »"). The fourth ACPR entity, **Abeille Retraite
Professionnelle, carries none** of them.

### The retraite range has no contractual document at all

The contracts exist — Abeille Retraite Plurielle, Premium Retraite Active and Plurielle Retraite
Entreprise all have live annexes financières — but the two files the site anchors as *"Document
d'informations clés du contrat…"* and *"…du PERO interentreprises"* contain **not one mandatory
PRIIPs section**, and one of them prints *"Document non contractuel à caractère publicitaire"*. The
document wins over the anchor text, so both are excluded. An anchor reading "document d'informations
clés" is not evidence that the file is one.

### 35 per-fund sheets excluded

Two families: 18 per-fund PRIIPs sheets keyed by ISIN or internal `FIC#########` codes, and 17
"GESTION SOUS MANDAT – ORIENTATION DE GESTION PRUDENTE/ÉQUILIBRÉE/DYNAMIQUE" sheets (3 profiles × 6
asset managers). Ingesting them would have turned roughly 19 savings contracts into roughly 54
products — the same trap that cost 64 exclusions at two other insurers here.

## Traps worth keeping

- **Documents are served from `/abdoc/<CODE>` with no `.pdf` extension.** Filtering hrefs on `.pdf`
  finds almost nothing. Two predecessor agents lost time to this.
- **PyMuPDF's column ordering makes two editions of one document score 0.67 on difflib**, which
  reads as "different documents". Sorted token bags score the same pair 0.97. That is what cleanly
  separated two genuine editions of PREMIUM EPARGNE ACTIVE from two genuinely *parallel* Suli
  Prévoyance Obsèques variants — an edition and a variant are different things under rule 8, and a
  naive diff cannot tell them apart.
- A live page links the **pre-production host** `pprd.abeille-assurances.fr` for one DIC. The
  canonical `www` copy is the one recorded.
- Three case-collision pairs (`V8606` / `v8606` and friends) — the hazard that silently merges two
  documents into one page on a case-insensitive filesystem.
- Four dead links, including three obsèques products advertised with no reachable document.

**The Aviva rebrand leaves almost no trace**: it survives in one filename and a 2022 bond
memorandum. Unlike [MGEN](mgen.md), there is **no dead legacy document tree** here — `/abdoc/` is the
single current store, so that migration was done properly.

The 69 documents come from the four sitemaps named in `robots.txt` (936 URLs, all crawled) and the
product pages they reveal. No URL space was enumerated. No personal data was encountered.
