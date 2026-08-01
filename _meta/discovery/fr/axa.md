# axa — AXA France

website: axa.fr
library: https://www.axa.fr/bibliotheque-ipid.html
fetch: plain
status: enum
lang: fr
enumerated: 2026-08-01

**152 documents enumerated, including 27 real conditions générales. None ingested.**
`www.axa.fr/robots.txt` carries `Disallow: *.pdf`.

That is the whole verdict, and it is not a technical obstacle: the host answers 200 to plain HTTP,
there is no WAF, and every one of the 152 documents was verified as a live `%PDF` with a matching
checksum. AXA simply asks crawlers not to take its PDFs, and this repository is public — shipping a
`sources/fr/axa.yml` would instruct every downstream user of this pipeline to ignore that. So the
enumeration is preserved here and nothing is fetched. `download.py` now enforces the same rule for
every insurer, so this cannot be re-decided by accident.

The largest insurer in France is therefore absent from the corpus for a reason that has nothing to
do with what it publishes.

## What is there, for whoever revisits this

**AXA publishes no library of wordings.** `/bibliotheque-ipid.html` is IPID-only: 107 files, zero
conditions générales. The IPIDs even cite the wording they belong to — *"Ce DIP appartient à la CG
référence 180304 E"* — without publishing it. The 27 conditions générales that do exist hang off
individual product pages with no index at all, which is why they were nearly missed (see below).

Coverage is lopsided in a way worth recording: retail lines get a full CG, while the professional
and corporate range has **2 wordings against roughly 60 IPIDs**.

## The entity split is per-network, not per-document

This is the finding that would have mattered most had the corpus been ingestable, because it breaks
the assumption that a document has one carrier.

Non-life conditions générales carry a **joint footer naming AXA France IARD (S.A.) *and* AXA
Assurances IARD Mutuelle (société d'assurance mutuelle) together** — the same wording, two possible
issuers depending on which network sold the policy. Life does the same with AXA France Vie and AXA
Assurances Vie Mutuelle. **No document is signed by a mutuelle alone**, so a single carrier per
document simply cannot be derived from the paper. Elsewhere in this dataset the SA/mutuelle
distinction is decidable per document (SMACL dual-publishes, Matmut splits by product); at AXA it is
not, and any attempt to assign one would be invention.

Two carriers that are not AXA France appear in its own library:

| carrier | documents | line |
|---|---|---|
| **JURIDICA** | 28 | all protection juridique |
| **Inter Partner Assistance** (Belgian, French branch, trading as AXA Assistance) | 21 | travel and assistance |

**No Direct Assurance / Avanssur paper exists on axa.fr.** AXA France IARD carries that risk — the
Direct Assurance documents already in this dataset name it — but the brand publishes its own
library. The only distributed-brand paper here is AXA Banque's: effets personnels (→ AXA France
IARD) and a borrower cover under group policy n° 24312634, which is a master policy number and not a
customer's.

## Traps recorded for a later pass

- `www.axa.fr` and `media.axa.fr` serve the same DAM tree with **different coverage**: 7 documents
  404 on the host that links them and 200 on the sibling. Always retry the other host before
  concluding a document is gone.
- **5 IPIDs are permanently unreachable** because AXA filed them under a directory whose name
  contains an apostrophe, and its own WAF answers 406 to every encoding of it. All five exist in the
  library under other references, so nothing is actually lost.
- 4 of the 21 library categories are genuinely empty.
- **72 of 152 site labels disagree with the product name printed in the document.** The document
  wins, as everywhere in this project.

## Two corrections to a predecessor's work, worth keeping

An earlier enumeration of this insurer got two things wrong, and both are the kind of error that
looks like success:

1. `chunk_Ipid-Ipid.js` and `chunk_Priips-Priips.js` were not JavaScript. They were byte-identical
   131 KB copies of AXA's **soft-404 page** — the guessed chunk URLs did not exist. A soft 404
   returns 200 and looks like a fetch that worked.
2. Its crawl **silently lost 270 of 926 sitemap pages** to bulk DNS failures, disproportionately the
   product pages. Re-fetching exactly those 270 returned 270/270 OK and 360 new PDF URLs — **which
   is where every one of the 27 conditions générales came from.** A partial crawl that reports no
   error reads as a complete one.

The library is genuinely React-fed by `POST /bibliotheque-ipid.searchdocument.json` with
`{productIndex, currentPage, currentResource}`, where `productIndex` indexes the page's own
`<select>` options — 21 published categories. Reading 0–20 is following the publisher; probing an ID
space is not, and is forbidden by the discovery spec.

The retirement-savings DIC page is a second client-rendered table behind
`apis.axa.fr/apipriips/v1/information-produit`, but its body requires a per-support `codeUV` that no
page HTML contains. Enumerating that is exactly what the spec forbids, and the payload would be fund
KIDs rather than contract wordings, so it was left alone.

No personal data was encountered.
