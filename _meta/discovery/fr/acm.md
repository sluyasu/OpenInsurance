# acm — Assurances du Crédit Mutuel

website: acm.fr (library also served from creditmutuel.fr and cic.fr)
fetch: plain
status: enum
lang: fr
enumerated: 2026-08-01

**197 documents enumerated. 6 are fetchable by a robots-respecting GET. The other 191 are not, and
that — not the document count — is the finding.**

ACM is the bancassurance arm of Crédit Mutuel and CIC: three ACPR carriers (ASSURANCES DU CREDIT
MUTUEL IARD SA, ASSURANCES DU CREDIT MUTUEL VIE SA, ASSURANCES DU CREDIT MUTUEL VIE — a société
d'assurance mutuelle), all in the Groupe des Assurances du Crédit Mutuel. Not to be confused with
**ACM Belgium**, a separate entity already in the Belgian part of this dataset.

The library is real and large: **181 IPIDs** covering 193 catalogue references across 13
distribution networks, plus 10 contract-level PRIIPs KIDs and 6 fee tables. It is also, as far as
this pipeline is concerned, **unreachable**.

## Why: the library is a POST form, and its GET form is disallowed

| how a document can be addressed | count | usable here |
|---|---|---|
| `direct_get`, but path matches a `robots.txt` `Disallow` | 116 | no |
| reachable only by POSTing through the catalogue form | 75 | no |
| `direct_get`, allowed | **6** | yes |

The catalogue is a stateful form: choose `Data_sitecode`, then `Data_familycode`, paginate, then
submit `_FID_DoDownload_id:<row>`. There *is* a per-document GET — `IPID.html?refipid=<REF>` — but
all three hosts disallow exactly that pattern. Verified directly, not taken on trust:

```
www.creditmutuel.fr/robots.txt   Disallow: *?*refipid=*
acm.fr/robots.txt                Disallow: *?*refipid=*
www.acm.fr/robots.txt            Disallow: *?*refipid=*
www.cic.fr/robots.txt            Disallow: /fr/assurances/
```

So the only stable, linkable address for 116 of these documents is one the publisher has asked
crawlers not to take, and the remaining 75 have no GET address at all. `download.py` fetches a `url:`
from a source YAML — it cannot POST through a multi-step form, and it should not be pointed at a
disallowed path. **No `sources/fr/acm.yml` is emitted.**

Note what this is *not*: the documents are not private, not paywalled, and not accidental. IPIDs are
exactly what the DDA requires an insurer to make available. ACM publishes them properly, through a
form. The obstacle is between that form and this pipeline's design, and honesty about that is worth
more than 181 pages fetched down a route the publisher declined.

The enumerating agent behaved correctly here and it is worth recording: a predecessor had already
pulled 230 files through the disallowed pattern. It did **not** extend that, flagged each address
with `robots_disallowed: true`, and re-verified five references through the allowed POST route
instead — byte-identical, sha256 equal.

## What was learned about the market anyway

**Zero conditions générales, zero notices, zero conditions particulières.** Every IPID says the full
terms sit "dans la documentation précontractuelle et contractuelle", which is published nowhere.
The same pattern as most of this market.

**ACM is not the only carrier in its own catalogue.** Read from the documents:

| carrier | documents | what |
|---|---|---|
| **Sérénis Assurances SA** | 31 alone + 4 co-carried | Zéphir motor range, flotte, moyens de paiement, the whole loyers-impayés range, SNPI professional liability, pet cover |
| **Allianz IARD** | 5 co-carried | professional and agricultural IPIDs, printed as "Allianz IARD et Assurances du Crédit Mutuel IARD SA" |
| ACM IARD SA / VIE SA / VIE SAM | the rest | Gentiane sits with the mutuelle entity |

**The banking trap did not bite, and that is itself informative.** 44 IPIDs are named after loans
(PRET IMMOBILIER, CREDIT AMAZON RENOUVELABLE, FLEX BY MONABANQ) — the shape that cost six exclusions
at another insurer — but every readable one prints *"Compagnie : Assurances du Crédit Mutuel VIE
SA"*. They are borrower insurance, not credit. Only `XX04FRFR001` looks like the excluded case, its
sole readable company being CM-CIC Leasing Solutions acting as *courtier d'assurances*; it was kept
with `carrier: null` rather than attributed, because its body is a flat image with no text layer and
its four catalogue siblings all name ACM. Not attributing beats guessing.

**54 per-fund KIDs excluded** with reasons. The manufacturer named inside them is Crédit Mutuel Asset
Management, an asset manager — so they are doubly not insurance products.

## Smaller findings

- ACM's dedicated fee page is live but **all seven of its PDF links 404**; the working copies are
  older filenames on the informations-réglementaires page. That dead page is also the only trace of
  a product called "Options Vie Génération".
- The three **PER contracts publish no contract-level KID at all**.
- `P1XXFRFR001` "Indemni+ pour Monabanq" is listed in the catalogue but its download returns HTML
  from all three hosts.
- 12 references collapse to 3 documents; three CM/CIC pairs are **parallel network variants, not
  editions** (rule 8).
- Document identity here is the catalogue reference (`doc_ref`), not the URL: 105 references were
  held from two hosts at once and none differed.

No personal data was encountered in this run.

## If this is ever revisited

Ingesting ACM needs `download.py` to drive the catalogue form — select site, select family,
paginate, submit a row id — which is a scraper rather than a downloader, and would be the first
insurer-specific fetch path in the pipeline. That is a deliberate design change, not a configuration
tweak, and it is left undone rather than smuggled in. The enumeration is preserved so the decision
can be made on real numbers.
