# wakam — Wakam SA

website: wakam.com
fetch: plain
status: enum
lang: fr
enumerated: 2026-07-30

**0 ingestable documents. This is the finding, not a failure.**

Wakam is a real French carrier — ACPR agrément 4020259, SIREN 562 117 085, Code des assurances,
group Big Wakam, 12 authorised branches — but it is **never a retail brand**. It writes the risk
behind other people's products and says so itself: *"La gestion des contrats et sinistres de nos
assurés est effectuée par nos partenaires"*, and, in its own machine-readable site description,
*"Policyholders should contact their distributing partner directly, as Wakam operates as a B2B2C
insurer."*

So Wakam's products can only ever be reached **through the brands that distribute them**. There is
no `sources/fr/wakam.yml`: there is nothing to point it at.

## The proof is an asymmetry, not an absence

The site footer offers *Informations réglementaires UK* and *Informations réglementaires Italie*.
There is **no French equivalent**. The Italian page carries a section headed "Contractual
Documentation" with 17 verified PDFs, because IVASS obliges an insurer writing into Italy under
freedom of services to publish the *set informativo*. Wakam publishes contract documents exactly
where a regulator compels it, and nowhere else.

France does not compel it, so France gets nothing. That is a useful thing to know about the French
regime as much as about Wakam: **the DDA obliges the distributor to hand the IPID to the customer,
it does not oblige the carrier to publish anything on its own website.**

The Italian documents are out of scope for a French wiki and are not ingested.

## Wakam used to publish a French library, and deleted it

The former WordPress site served, under `/wp-content/uploads/`, a "Self Service" catalogue in
Wakam's own name: conditions générales + IPID + fiche produit for *Assurance Eco-Mobilité* (NVEI,
i.e. what the taxonomy calls `edpm`), conditions générales + IPID for *Assurance Vélo Casse & Vol*,
and an IPID for flight cancellation/delay. All now return 404, and the routes that held them
client-redirect to the newsroom.

Six were recovered from the Internet Archive and are genuine (the Eco-Mobilité conditions générales
run 60 pages, edition 02/2022, and its IPID prints "Compagnie : Wakam … agrément 4020259").

**Not ingested, deliberately.** Rule 3 requires every product fact to cite a live public source, and
a 404 with an archive copy is not that. Recorded here so the deletion is visible rather than silently
absent, and so nobody re-derives it. If a future decision allows archive-sourced documents, this is
the first candidate and it would need its own provenance marking.

## A privacy problem on Wakam's live site — not ingested, needs a human decision

Four PDFs served from a public path on wakam.com are **completed policy specimens rather than blank
templates**, and they carry what appear to be real personal identifiers of named individuals. They
are Italian, so they were out of scope anyway.

They are **not ingested, not mirrored, and their URLs are deliberately not recorded in this
repository**, because writing them down here would republish a pointer to third-party personal data
from a public repo. The details are held outside the repo, in the session's working notes.

This is a responsible-disclosure decision for a human, not something this project should act on by
itself. Nothing further should be done with those files.

## De-duplication map: brands Wakam is reported to carry

This is the reason to have looked at Wakam at all. French consumer brands are frequently ORIAS
intermediaries whose risk carrier is someone else, and Wakam is one of the largest such carriers in
France. When one of these brands is enumerated, expect its documents to name Wakam.

Leads worth checking first: **Lovys, Luko, Orus, Dalma, Dattak, Flitter, Yeet Assurances, Garantme,
Cautionneo, Sharelock, Solly Azar, Netvox, Assurone, Aramisauto, Ulygo, Serenitrip, Matera, Solucia,
+Simple, Entoria, Klian, FMA.**

**Read that list as leads, not as facts.** Three cautions, all of which matter:

1. It is a *distribution* list, not proof of risk-carrying. It mixes MGAs and brokers with service
   providers (loss adjusting, assistance, pricing software) and even with rival carriers.
2. It comes from 2020 and 2023 archive snapshots, because the live site names almost no partners.
   Relationships move: Luko appears on it and is now carried by Allianz Direct Versicherungs-AG.
3. **Only the brand's own IPID settles it.** Every one of these needs the same treatment as the
   rest of the French market: read the carrier out of the document.

## Fetch notes

`plain` — nothing refused, no WAF. But the site is a client-rendered SPA that **returns 200 with an
identical 7 KB shell for every html path, including paths that do not exist**, so HTTP status is
useless for probing pages here. The whole route table, all five locales and every document href live
in one 2 MB JavaScript bundle; grepping that bundle is the complete site map and is far more reliable
than crawling.

Minor data-quality notes on the public financial reports: the "English documents" column serves the
French SFCR for several years, and one file named as a 2020 group SFCR is in fact the report of the
group's former name.
