# mgen — Mutuelle Générale de l'Éducation Nationale

website: mgen.fr
fetch: plain
status: enum
lang: fr
enumerated: 2026-08-01

**19 documents found, 0 ingestable. This is the finding, not a failure — and it is the finding this
insurer was picked for.**

MGEN is a **Livre II mutuelle under the Code de la mutualité** (SIREN 775 685 399), in Groupe VYV.
It was chosen deliberately: nothing in this dataset yet covers what a Code de la mutualité entity
publishes, and the answer turns out to be the most interesting negative result of the French batch.

## A mutuelle's contractual instrument is not a contract, and it is not published

A mutuelle does not issue *conditions générales*. Its equivalent instrument is the **règlement
mutualiste**, adopted by the assemblée générale alongside the **statuts**. The member is an
*adhérent*, not a *souscripteur*, and the terms are amended by vote rather than by agreement between
two parties. That is a genuinely different legal object from an insurance contract under the Code
des assurances, and it is worth stating plainly because the two are routinely conflated.

MGEN publishes **neither**. Its own documents point at the instrument without linking it:

> Le détail des garanties et conditions figure aux Statuts et Règlements mutualistes collectifs
> **remis lors de l'adhésion**

*Remis*, not *publiés*. Handed over on joining. So the operative terms of one of France's largest
health mutuals are, by design, unavailable to anyone deciding whether to join.

Across 288 crawled pages there is exactly **one IPID** — for the *Contrat de sortie de la
Complémentaire Santé Solidaire*, a small statutory product — and **zero** conditions générales,
règlements mutualistes or statuts that resolve.

## The two links that would have resolved it are both dead

This part is a migration bug, not a policy, and the distinction matters: MGEN did once publish the
statuts, and the intent to publish is still visible in its own pages.

- The statuts URL printed in the espace-personnel CGU → **404**
- The entire seven-link documents block on the MTE product page, including *"Statuts et règlements
  mutualistes MTE"* and an IPID → **404**, every one

Both are old `/fileadmin/` TYPO3 paths that were never migrated to the current Drupal site. Verified
404 on two independent clients. A predecessor agent had also constructed roughly 170 candidate
`/fileadmin/` paths and probed them: **zero hits**. That tree is gone. Recorded here so nobody
retries it on the theory that it might work — and note that such probing is now forbidden by the
discovery spec anyway.

## What is published instead

A consistent tier of 5–24-page *Guides de Bienvenue* and *Tableaux des garanties*, each stamped by
MGEN itself:

> Document publicitaire n'ayant pas de valeur contractuelle

and each redirecting the reader to the règlement it cannot reach. These carry real reimbursement
levels in `% BR` / `% BRSS` notation — a percentage of the Sécurité sociale **base de
remboursement**, never of the cost — so they are substantive. They are still not the terms, and the
publisher says so.

**No `sources/fr/mgen.yml` is emitted.** Ingesting self-declared non-contractual marketing as
products would show a reader guarantee levels with no instrument behind them, which is the failure
mode rule 3 exists to prevent. Same treatment as [Wakam](wakam.md), [Acheel](acheel.md) and
Generali, for a different reason each time.

## Half the library is not MGEN's risk

MGEN carries santé and prévoyance itself under Livre II. Everything else is somebody else's paper:

| Line | Carrier | Regime |
|---|---|---|
| Épargne Vie, Assurance Décès, Néobsia | **MUTEX** SA | Code des assurances |
| Retraite (régime Corem) | **UMR** (Union Mutualiste Retraite) | Code de la mutualité |
| Assistance | Ressources Mutuelles Assistance | — |
| IPID Complémentaire Santé Solidaire | **MAIF** | Code des assurances |

The Épargne Vie brochure spells out a structure worth recording: the contract was *souscrit par VYV
Protection Avenir auprès de MUTEX*. On that line the adhérent sits under **another VYV entity's
group contract with a Code des assurances insurer** — not under an MGEN règlement at all. One brand,
one member card, three legal regimes underneath.

## Notes for a later pass

- `robots.txt` names three sitemaps; `sitemap.xml` is a trap that returns HTML. Only
  `sitemap_drupal.xml` (288 URLs) is real.
- One PDF has **no text layer** (3 pages, 2 characters). Product name and carrier were read from the
  rendered images.
- Two live URLs serve the same Épargne Vie fiche; the only difference is that the newer one adds
  "Assuré par MUTEX".
- An anchor reading *"Consulter le règlement"* leads to a **Mutex sales-promotion rulebook**, not to
  a règlement mutualiste. A reader following that link would be badly misled.

## Member area: deliberately not recorded

A predecessor had reached a CMS endpoint on the member extranet holding, among other things, a
24-page *"STATUTS & RÈGLEMENT MUTUALISTE — MGEN COMPLÉMEN'TER PRÉVOYANCE, applicables au 1er mars
2021"* — precisely the missing instrument.

It is **not** in the document list and **its URL is recorded nowhere**, here or elsewhere in this
repository. It sits behind the member area, reachable only through opaque per-document identifiers
that no public page links. This project records what a member of the public can fetch anonymously;
that document is not that, and publishing a pointer to it in a public repository would defeat the
access control its publisher chose. Nothing was re-fetched from that host.

No personal data was encountered in this run. The one bulletin d'adhésion found is a blank specimen.
