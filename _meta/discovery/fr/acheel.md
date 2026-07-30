# acheel — ACHEEL SA

website: acheel.com
fetch: plain
status: enum
lang: fr
enumerated: 2026-07-30

**0 ingestable documents in the insurer's own library.** No `sources/fr/acheel.yml`.

This is the opposite of what a digital-native carrier was expected to do. Acheel holds its own
ACPR agrément (ACHEEL SA, 879 605 350 RCS Paris, Code des assurances, 7 branches, no group), which
already makes it unusual among French neo-insurers — most are ORIAS intermediaries fronted by
someone else. But it publishes **nothing contractual** on any of its domains: no conditions
générales, no IPID, no notice, no fiche produit, across `acheel.com`, `v2.`, `faq.`, `emprunteur.`,
`partners.` and `charlee.fr`. The entire estate holds one PDF, the Solvency II SFCR, which is a
regulatory report and out of scope.

Enumeration was thorough enough to make the absence meaningful: there is no robots.txt and no
sitemap, so the route list came from the Next.js build manifest (151 routes), a 72-URL crawl, all
243 JavaScript chunks, and the Internet Archive's index (2 089 archived URLs). **The SFCR is the
only PDF ever captured on the domain**, so this is not a recent regression.

The library exists, it is simply gated three ways: per-contract inside the quote funnel and the
espace client, behind a broker login, and in distributors' hands.

## Carrier: real, but not for every line

Four genuine Acheel contracts were located on **distributors'** sites (3 conditions générales —
two MRH of 106 and 111 pages, one animaux of 40 — plus one habitation IPID). All name
*« L'Assureur des garanties d'assurance est ACHEEL, Société Anonyme … 879 605 350 RCS Paris »*.

They are **not ingested here**, deliberately. The unit of this project is an insurer's own public
library, and a distributor's copy carries no guarantee of being the current edition. Recorded so a
later decision can revisit it; if it does, they need provenance marking as third-party-hosted.

**The auto line is not Acheel's risk.** Acheel's own privacy page names **Allianz IARD** as data
controller for auto contract management, corroborated by the public product API, where every auto
product sits on a different participant identifier than every Acheel-underwritten one. A legacy
"MRH Wakam" product is also still exposed. So even a carrier that holds its own agrément does not
carry its whole range — the French rule holds again: read the carrier out of each document.

## Traps (do not re-derive)

1. **Footer-based carrier extraction returns the wrong entity.** Every Acheel document prints
   ACHEEL FRANCE — the ORIAS intermediary — on the cover and in every page footer. The actual
   carrier, ACHEEL SA, appears only inside the section « 1.2. Votre Assureur ». An extraction that
   trusts the footer will attribute the contract to an intermediary.
2. The contracts print a share capital of 46 812,48 € while the site prints 330 800 €. Same SIREN;
   the documents are simply older. Not two entities.
3. **No moto line exists**, despite what a product-range guess would suggest. The live catalogue is
   habitation, PNO, auto, santé, animaux, scolaire, protection juridique and RC Pro, plus an
   emprunteur lead form.
4. The curl-versus-urllib trap reproduced on a distributor host: 403 to `curl`, 200 to `urllib`,
   same URL and same User-Agent.

## A privacy line deliberately not crossed

Real customer contract identifiers are visible in the Internet Archive index, and the endpoint they
address appears to still be live. It returns a document set that includes a personalised
*Proposition d'assurance*. That is customer data, not a public library, and it was not
dereferenced. The identifiers are not recorded in this repository. Nothing further should be done
with them.
