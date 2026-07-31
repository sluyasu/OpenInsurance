# gan — Gan Assurances (« Gan Assurances Compagnie française d’assurances et de réassurances », SA, RCS Paris 542 063 797, APE 6512Z, 8-10 rue d’Astorg 75008 Paris) — brand of the Groupama group
website: https://www.gan.fr
library:
  - https://www.gan.fr/page_elementor/documents-reglementaires-page-retraite/
  - https://www.gan.fr/page_elementor/documents-reglementaires-page-retraite-2/
  - https://www.gan.fr/page-daccueil/particuliers/epargne-retraite/
  - https://www.gan.fr/produit/assurance-vie-epargne/
  - https://www.gan.fr/produit/assurance-retraite-complementaire/
  - https://www.gan.fr/produit/solution-retraite-des-salaries/
  - https://www.gan.fr/produit/assurance-prevoyance/
  - https://www.gan.fr/produit/assurance-obseques/
  - https://www.gan.fr/produit/assurance-emprunteur-credit-pret/
  - https://www.gan.fr/produit/assurance-complementaire-sante/
  - https://www.gan.fr/wp-json/wp/v2/media?per_page=100&media_type=application
  - https://www.ganprevoyance.fr/ (product pages, one « Documents » accordion each)
  - https://www.ganpatrimoine.fr/solution/particulier/… and /solution/professionnel/… (one « Documents » block each)
fetch: plain
status: enum
lang: fr
enumerated: 2026-07-30

**50 usable documents** (25 product_sheet, 13 conditions_tarifaires, 12 ipid) across 7 branches (prevoyance 13, assurance-vie 11, retraite 10, obseques 8, sante 4, emprunteur 3, gav 1).
44 further document(s) found but not ingestable, listed at the bottom.

## Carrier

GAN ASSURANCES is a real first-party non-life carrier (own agrément, APE 6512Z, RCS Paris 542 063 797) — but it publishes almost nothing that it carries itself. Of the 94 contractual documents found, 84 name GROUPAMA GAN VIE as the risk carrier (« Assureur : Groupama Gan Vie, société anonyme au capital de 1 371 100 605 euros - 340 427 616 RCS Paris - APE : 6511Z - Siège social : 8-10, rue d’Astorg 75008 Paris »), 1 names Vitis Life S.A. (Luxembourg) and only 2 name Gan Assurances itself — and those two are the Gan Santé « tableau de garanties », which carries the Gan Assurances identity block in its mentions légales but no explicit « Assureur : » line. The relationship is printed verbatim in the fee sheets: « Gan Assurances distribue les produits de Groupama Gan Vie ». Seven documents (CCSF benefit tables and three Gan Prévoyance fee sheets) name no carrier at all. The two sibling Gan brands are intermediaries, not carriers: Gan Patrimoine is « Société anonyme d’intermédiation en assurance … RCS Lille 457 504 694 … N° d’immatriculation ORIAS 09 051 780 … Mandataire exclusif de Groupama Gan Vie et de ses filiales »; Gan Prévoyance is a Groupama Gan Vie sales network. Several IPIDs are co-signed: « Compagnies : Groupama Gan Vie … Mutuaide Assistance (filiale spécialisée du groupe Groupama), RCS Bobigny 383 974 086 » — Mutuaide carries the assistance guarantees.

## What this insurer does not publish

No conditions générales, no notice d’information and no conditions particulières anywhere — zero, on all three Gan hosts. More striking: Gan publishes no contractual document at all for the non-life book it actually underwrites. Only 14 of the 69 /produit/ pages on gan.fr link any PDF, and all 14 are life, retirement, prévoyance, santé, emprunteur or obsèques. The 55 silent product pages include the entire retail non-life line (auto, moto, habitation, remorques/caravanes, vélo, navigation de plaisance, chasse, protection juridique, accidents de la vie), the entire professional and enterprise line (commerce alimentaire and non alimentaire, hôtel, restaurant, traiteur, pharmacie, infirmier, paramédical, expert-comptable, agent immobilier, taxi, artisan, esthétique, bureaux, crèche, intérim, aide à domicile, association, industrie, EHPAD, bris de machine, RC entreprise, RC dirigeant, cyber, événement, flotte auto, marchandises transportées, RC transport, décennale/dommages-ouvrage, GSC) and the entire agricultural line (multirisque agricole, mortalité des animaux, climatique récoltes, tracteurs et machines). Those pages carry a quote form and an agency locator and nothing else. The only non-life IPID-shaped anchor on the site, « Convention Spéciale » on /cyber-securite/, returns HTTP 404. Documents for the non-life book are apparently handed over by the agent at the point of sale, not published.

## Traps (do not re-derive)

1. The single most useful entry point is the open WordPress REST media endpoint on gan.fr — https://www.gan.fr/wp-json/wp/v2/media?per_page=100&media_type=application (X-WP-Total: 149). It saves crawling 350 pages. But do not trust it as complete: /app/uploads/2021/12/3370-77383-122021-WebVdef.pdf is linked from https://www.gan.fr/cyber-securite/ under the anchor « Convention Spéciale » and is not in the media list. It is also a dead link (HTTP 404) — the only genuinely contract-shaped anchor anywhere on gan.fr for a non-life product points at nothing.
2. PDF hrefs on gan.fr are RELATIVE (/app/uploads/YYYY/MM/…). A grep for 'https?://…\.pdf' finds 10 URLs and misses 34. Resolve against the page URL.
3. Gan does not publish under one brand. Three Gan-branded hosts each carry their own document set, with heavy product overlap and different filenames for the same contract family: www.gan.fr (agency network, 46 docs), www.ganpatrimoine.fr (31, ASP.NET, /Media/documents/DIC|DIS|Dépliants/), www.ganprevoyance.fr (16, docs served as /<page-slug>/<n-n>/<human-readable-name>.pdf?date=YYYYMMDDHHMMSS). One document lives off-brand on https://www.pia.ggvie.fr/ (the Groupama Gan Vie partner portal).
4. ganpatrimoine.fr emits the SAME href in two encodings on sibling pages — e.g. .../DIS/DIS_GD_Equilibré_Durable_Gan Patrimoine_2025_02_13.pdf (raw space + raw accent) on the /particulier/ page and .../DIS_GD_Equilibr%C3%A9_Durable_Gan%20Patrimoine_2025_02_13.pdf on the /professionnel/ page. Percent-normalise before de-duplicating or you will double-count ~15 files. That alone takes the ganpatrimoine link count from 65 to 31.
5. ganprevoyance.fr serves one physical file under several human-readable URLs, one per product page. 13 of the 107 URLs are byte-identical to another (same sha256), e.g. the Gan Prévoyance Protection IPID appears at /securite-famille/2-1/telecharger-le-document.pdf, /securite-professionnel-gan-prevoyance-protection/2-1/telecharger-le-document-d-information.pdf and /arret-travail-invalidite-deces-commercant-gan-prevoyance/2-1/telecharger-le-document-d-information.pdf. The DIC Fonds en Euros appears at 5 URLs. See dropped_duplicates. No text-identical-but-byte-different pair was found on any Gan host.
6. Basenames repeat across directories on ganprevoyance.fr (telecharger-le-document.pdf, telecharger-le-document-d-information.pdf, document-d-informations-cles-dic-fonds-en-euros.pdf) and on ganpatrimoine.fr (DIC_FONDS_EN_EUROS.pdf served from both /Media/Images/gan-pictures/ and /images/gan-pictures/). Anything that flattens to the basename will overwrite. Listed in case_collisions.
7. Naming: Groupama/Gan call the DDA IPID a « DIN » in the filename (032023-DIN_Gan-Solutions-Prevoyance.pdf) but the document header reads « Document d’information sur le produit d’assurance » / « Document d’information d’un produit d’assurance ». Conversely one file named DIC PREV_Gan Patrimoine Protection Plus 042022.pdf is an IPID, not a DIC. Classify from the header, never from the filename.
8. document_type mapping used here: true IPIDs → ipid; PRIIPs « Document d’informations clés » (DIC/KID) and « Document d’informations spécifiques » (DIS, one per delegated-management profile) → product_sheet; « Fiche d’information sur les frais » / « Transparence des frais » → conditions_tarifaires; CCSF « engagement lisibilité » benefit tables → product_sheet. Every record carries printed_doc_type with the exact French header so the distinction is not lost. There is NO conditions_generales anywhere.
9. Edition dates: PRIIPs DIC/DIS print « Document produit le DD/MM/YYYY » in the body — always prefer that. CCSF tables carry a print-shop stamp « … – 012026 – PAO – GGVie ». Fee sheets and the Gan Patrimoine « Transparence des frais » files print no date at all; for those the only signal is the /app/uploads/YYYY/MM/ path or the ?date=YYYYMMDDHHMMSS query on ganprevoyance.fr, both recorded with edition_source = filename. Five ganpatrimoine « Transparence des frais » files and one DIC_FONDS_EN_EUROS.pdf have no date signal at all.
10. Real editions vs parallel variants. Editions: the gan.fr Gestion Déléguée DIS set exists twice — /2025/04/DIS_GD_*_Gan_Assurance_2025_02_13.pdf (« Document produit le 13/02/2025 ») and /2026/07/DIS_Gestion_Deleguee_*_GASS-2026-07.pdf (« Document produit le 13/05/2026 »); both are still linked, from different pages, and both cover the same contracts (« Chromatys Evolution », « Chromatys », « Gan Capitalisation Exception »). Variants, NOT editions: DIC-FONDS-EN-EURO-GASS-2026-07.pdf vs DIC-FONDS-EN-EURO-RETRAITE-GASS-2026-07.pdf differ only in « fonds en euros » vs « fonds en euros retraite » (assurance vie vs plan d’épargne retraite). Likewise the identically-titled DIS profiles on gan.fr and on ganpatrimoine.fr are different documents — they name different underlying contracts (Chromatys/Gan Capitalisation vs Gan Patrimoine Evolution/Stratégies).
11. site_label vs document. The gan.fr page /produit/solution-retraite-des-salaries/ lists the whole 2025 DIS set under labels like « Infos – Profil DYNAMIQUE », but the documents themselves say they apply to the individual savings contracts « Chromatys Evolution », « Chromatys » and « Gan Capitalisation Exception » — not to a collective retirement plan. The site's placement is misleading; the document wins. Similarly ganprevoyance labels several IPIDs simply « Télécharger le document ».
12. Group overlap with the sibling Groupama enumeration: none of these files sit on groupama.fr, but 84 of 94 name GROUPAMA GAN VIE (RCS Paris 340 427 616) as the carrier, and Mutuaide Assistance (RCS Bobigny 383 974 086) co-signs the prévoyance/santé IPIDs. If the Groupama agent also enumerates Groupama Gan Vie material, expect the same products (Gan Prévoyance Perspectives Épargne, Gan Patrimoine Evolution, the Gestion Déléguée DIS series) under different filenames. These files are Gan-branded and Gan-distributed, so they are recorded here, but the carrier field is Groupama Gan Vie, not Gan Assurances.
13. Excluded on purpose, so nobody re-derives them: SFCR/RSR solvency reports 2016-2025 (~10 PDFs on /page_elementor/informations-legales*/); the espace-client CGU (CGU-Gan-Assurances-V8.pdf and predecessors); annual « taux de rendement / participation aux bénéfices » disclosures; commercial plaquettes and dépliants; agricultural prevention leaflets; « Exemples de remboursements » santé illustrations; FFA/AMF/FBF mediation charters; the OPCI/SCPI DICI-for-investor documents on ganpatrimoine (UCITS, not insurance); and kid-telluma-boost-septembre-2026.pdf, which is the PRIIPs KID of a structured note (issuer documentation at gspriips.eu), i.e. a unit-linked underlying rather than a Gan insurance document.
14. Two genuine two-dated-editions pairs beyond the DIS set: the Gan Patrimoine Protection Plus IPID exists as DIC PREV_…042022.pdf (2022-04) and DIN PREV_…122023.pdf (2023-12) — same printed « Produit : Gan Patrimoine Protection Plus », different dates, and only the 2023 one lists Mutuaide Assistance as co-signer; and the Gan Patrimoine Capitalisation fee sheet exists as /Media/GPATCAPI_Frais_2023.pdf and as the undated /Media/documents/Transparence frais contrat/Gan-Patrimoine-Capitalisation.pdf. Both members of each pair are still linked from live pages.
15. The emprunteur IPID on gan.fr prints « Produit : Gan Assurances Emprunteur » on its cover but names Groupama Gan Vie as the compagnie — the product carries the Gan Assurances name while the risk sits with the life entity. Do not infer the carrier from the product name on any Gan document.
16. The Gan Santé « tableau de garanties » explicitly prints « Document non contractuel, fourni à titre d’information ». It is kept as product_sheet because it is the only document Gan publishes describing santé cover levels, but do not treat it as contract text.

## Same name, same document type, no orderable edition

These are the same document more than once and could not be ordered, because the
editions are missing or equal. Left as parallel rather than guessing a supersession;
resolve from the documents after extraction.

- `gan patrimoine capitalisation` x2: GPATCAPI_Frais_2023.pdf, Gan-Patrimoine-Capitalisation.pdf

## Product names colliding case-insensitively

These would overwrite each other as page filenames on a case-insensitive
filesystem. Disambiguate in the data after extraction.

- `gan performance retraite` claimed by 2: Gan-Performance-Retraite-Fiche-Infos-Frais.pdf, GAN-Performance-Retraite-Infos-Cles.pdf
- `tableau de garanties des exemples de remboursement` claimed by 2: Tableau-de-garanties-2025.pdf, Tableau-de-garanties-GAN-Sante-02-2026.pdf
- `lisibilité obsèques` claimed by 3: Lisibilite-obseques-Gan-Assurances-072025.pdf, Lisibilite-obseques-Gan-Patrimoine-032026.pdf, lisibilite-obseques.pdf?date=20260313123059
- `gan patrimoine capitalisation` claimed by 3: GPATCAPI_Frais_2023.pdf, Gan-Patrimoine-Capitalisation.pdf, DIC%20GL%20Capitalisation%20Gan%20Patrimoine_2025_03_07.pdf
- `gan patrimoine objectif retraite` claimed by 2: Gan-Patrimoine-Objectif-Retraite.pdf, DIC%20GL%20Objectif%20Retraite%20Gan%20Patrimoine_2025_03_05.pdf
- `gan patrimoine protection plus` claimed by 2: DIC%20PREV_Gan%20Patrimoine%20Protection%20Plus%20042022.pdf, DIN%20PREV_Gan%20Patrimoine%20Protection%20Plus%20122023.pdf
- `gan patrimoine sérénité essentiel` claimed by 2: 1412-062023%20-%20DIC%20GPatSE.pdf, 1412-112018%20GPatSE.pdf

## Dropped duplicates

- `DIC_FONDS_EN_EUROS.pdf` = `DIC_FONDS_EN_EUROS.pdf` — byte-identical (same sha256 09187c0eb2f4…), served from a second product page under a different filename
- `telecharger-le-document-d-information.pdf?date=20231114103959` = `telecharger-le-document.pdf?date=20231114103947` — byte-identical (same sha256 56aa04bfe991…), served from a second product page under a different filename
- `telecharger-le-document-d-information.pdf?date=20231114104008` = `telecharger-le-document.pdf?date=20231114103947` — byte-identical (same sha256 56aa04bfe991…), served from a second product page under a different filename
- `telecharger-le-tableau-des-garanties.pdf?date=20251222151629` = `telecharger-le-tableau-des-garanties.pdf?date=20251222151901` — byte-identical (same sha256 26cffdec23d9…), served from a second product page under a different filename
- `document-d-informations-cles-dic-gan-prevoyance-perspectives-epargne.pdf?date=20250428114237` = `document-d-informations-cles-dic-gan-prevoyance-perspectives-epargne.pdf?date=20250428141040` — byte-identical (same sha256 d9d1961c92b7…), served from a second product page under a different filename
- `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428114350` = `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428141040` — byte-identical (same sha256 c5dcca101e50…), served from a second product page under a different filename
- `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428140856` = `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428141040` — byte-identical (same sha256 c5dcca101e50…), served from a second product page under a different filename
- `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428135304` = `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428141040` — byte-identical (same sha256 c5dcca101e50…), served from a second product page under a different filename
- `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428114237` = `document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428141040` — byte-identical (same sha256 c5dcca101e50…), served from a second product page under a different filename
- `document-d-informations-cles-dic-gan-prevoyance-retraite-active.pdf?date=20250428140856` = `document-d-informations-cles-dic-gan-prevoyance-retraite-active.pdf?date=20250428141040` — byte-identical (same sha256 599a2f26f5a1…), served from a second product page under a different filename
- `document-d-informations-gan-prevoyance-sante-pro.pdf?date=20231127095904` = `document-d-informations-gan-prevoyance-sante.pdf?date=20231127095936` — byte-identical (same sha256 1ac16210b5e6…), served from a second product page under a different filename
- `document-d-informations-gan-prevoyance-sante-special-senior.pdf?date=20231127095904` = `document-d-informations-gan-prevoyance-sante-senior.pdf?date=20231127095936` — byte-identical (same sha256 56e003f9bb44…), served from a second product page under a different filename
- `fiche-d-information-frais-du-per-individuel-gan-nouvelle-vie.pdf?date=20260318121207` = `fiche-d-information-sur-les-frais-du-per-individuel-gan-nouvelle-vie.pdf?date=20260318121107` — byte-identical (same sha256 8f117aa48678…), served from a second product page under a different filename

## Documents

| product_name | doc_type | branch | edition | carrier | pp | url |
|---|---|---|---|---|---|---|
| Chromatys Evolution | conditions_tarifaires | assurance-vie | 2026-03 | Groupama Gan Vie | 1 | https://www.gan.fr/app/uploads/2026/03/Gan-Chromatys-Evolution-Fiche-Infos-Frais.pdf |
| Gan Assurance Capitalisation Exception | conditions_tarifaires | assurance-vie | 2026-03 | Groupama Gan Vie | 1 | https://www.gan.fr/app/uploads/2026/03/Gan-Capitalisation-Exception-Fiche-Infos-Frais.pdf |
| Gan Patrimoine Capitalisation | conditions_tarifaires | assurance-vie | 2023 | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/GPATCAPI_Frais_2023.pdf |
| Gan Patrimoine Capitalisation | conditions_tarifaires | assurance-vie |  | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/documents/Transparence%20frais%20contrat/Gan-Patrimoine-Capitalisation.pdf |
| Gan Patrimoine Evolution | conditions_tarifaires | assurance-vie |  | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/documents/Transparence%20frais%20contrat/Gan-Patrimoine-Evolution.pdf |
| Gan Prevoyance Perspectives Epargne | conditions_tarifaires | assurance-vie | 2026-03 |  | 1 | https://www.ganprevoyance.fr/assurance-vie-gan-prevoyance-perspectives-epargne/3-4/fiche-d-information-frais-du-contrat-gan-prevoyance-perspectives-epargne.pdf?date=20260318121419 |
| Chromatys Évolution | product_sheet | assurance-vie | 2026-06 | Groupama Gan Vie | 3 | https://www.gan.fr/app/uploads/2026/07/GAN-Chromatys-Evolution-Infos-Cles-2026-07.pdf |
| Gan Capitalisation Exception | product_sheet | assurance-vie | 2026-06 | Groupama Gan Vie | 3 | https://www.gan.fr/app/uploads/2026/07/GAN-Capitalisation-Exception-Infos-Cles-2026-07.pdf |
| Gan Patrimoine Capitalisation | product_sheet | assurance-vie | 2025-03 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/DIC%20GL%20Capitalisation%20Gan%20Patrimoine_2025_03_07.pdf |
| Gan Patrimoine Évolution | product_sheet | assurance-vie | 2025-03 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/DIC%20GL%20Evolution%20Gan%20Patrimoine_2025_03_05.pdf |
| Gan Prévoyance Perspectives Épargne | product_sheet | assurance-vie | 2025-03 | Groupama Gan Vie | 3 | https://www.ganprevoyance.fr/epargne-handicap/2-4/document-d-informations-cles-dic-gan-prevoyance-perspectives-epargne.pdf?date=20250428141040 |
| Gan Assurances Emprunteur | ipid | emprunteur | 2023-06 | Groupama Gan Vie | 2 | https://www.gan.fr/app/uploads/2024/11/062023_DIN-Emprunteur.pdf |
| Gan Patrimoine Emprunteur | ipid | emprunteur | 2026-03 | Groupama Gan Vie | 2 | https://www.ganpatrimoine.fr/Media/documents/D%C3%A9pliants/DIN%20GAN%20PAT%20Emprunteur-GPE09-032026.pdf |
| Gan Prévoyance Emprunteur | ipid | emprunteur | 2021-04 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/assurance-emprunteur/2-1/assurance-emprunteur.pdf?date=20211108150730 |
| Gan Prévoyance Garantie des Accidents de la Vie | ipid | gav | 2023-03 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/gav/1-1/document-d-informations-garantie-accidents-de-la-vie.pdf?date=20230317164344 |
| Gan Patrimoine Sérénité Essentiel | product_sheet | obseques | 2023-06 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/1412-062023%20-%20DIC%20GPatSE.pdf |
| Gan Patrimoine Sérénité Essentiel | product_sheet | obseques | 2018-11 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/1412-112018%20GPatSE.pdf |
| Gan Patrimoine Sérénité Succession | product_sheet | obseques | 2023-06 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/1414-062023%20DIC%20GPatSS.pdf |
| Gan Prévoyance Sérénité Obsèques | product_sheet | obseques | 2025-01 | Groupama Gan Vie | 3 | https://www.ganprevoyance.fr/obseques-succession/1-1/document-d-informations-cles-gan-prevoyance-serenite-obseques.pdf?date=20250117135714 |
| Gan Sérénité Obsèques | product_sheet | obseques | 2023-03 | Groupama Gan Vie | 3 | https://www.gan.fr/app/uploads/2024/11/032023-DIC_Gan-Serenite-Obseques.pdf |
| Lisibilité obsèques | product_sheet | obseques | 2025-07 | Groupama Gan Vie | 6 | https://www.gan.fr/app/uploads/2025/06/Lisibilite-obseques-Gan-Assurances-072025.pdf |
| Lisibilité obsèques | product_sheet | obseques | 2026-03 | Groupama Gan Vie | 6 | https://www.ganpatrimoine.fr/Media/documents/Lisibilite-obseques-Gan-Patrimoine-032026.pdf |
| Lisibilité obsèques | product_sheet | obseques | 2026-03 | Groupama Gan Vie | 6 | https://www.ganprevoyance.fr/obseques-succession/1-4/lisibilite-obseques.pdf?date=20260313123059 |
| Gan Patrimoine Protection Plus | ipid | prevoyance | 2022-04 | Groupama Gan Vie | 2 | https://www.ganpatrimoine.fr/Media/documents/DIC/DIC%20PREV_Gan%20Patrimoine%20Protection%20Plus%20042022.pdf |
| Gan Patrimoine Protection Plus | ipid | prevoyance | 2023-12 | Groupama Gan Vie | 2 | https://www.ganpatrimoine.fr/Media/documents/DIC/DIN%20PREV_Gan%20Patrimoine%20Protection%20Plus%20122023.pdf |
| Gan Prévoyance Protection | ipid | prevoyance | 2023-12 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/securite-famille/2-1/telecharger-le-document.pdf?date=20231114103947 |
| Gan Prévoyance Protection Homme Clé | ipid | prevoyance | 2023-10 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/protection-homme-cle/2-1/document-d-information-gan-prevoyance-protection-homme-cle.pdf?date=20230927144012 |
| Gan Solutions Prévoyance | ipid | prevoyance | 2024-03 | Groupama Gan Vie | 2 | https://www.gan.fr/app/uploads/2024/11/032023-DIN_Gan-Solutions-Prevoyance.pdf |
| Gan Solutions Prévoyance Homme Clé | ipid | prevoyance | 2023-10 | Groupama Gan Vie | 2 | https://www.gan.fr/app/uploads/2024/11/102023-DIN_-GSP-Homme-Cle.pdf |
| Actifs salariés du secteur privé Tableaux d’exemples de prise en charge au 01/01/2025 des | product_sheet | prevoyance | 2025 |  | 5 | https://www.ganprevoyance.fr/prevoyance-salaries/2-1/telecharger-le-document.pdf?date=20250103140538 |
| Exemple de prise en charge pour les TNS | product_sheet | prevoyance | 2026-01 | Groupama Gan Vie | 6 | https://www.ganpatrimoine.fr/Media/documents/Lisibilite-prevoyance/Tableau-TNS_CCSF_Lisibilite-GPP-2026.pdf |
| Lisibilité Prévoyance GSP | product_sheet | prevoyance | 2025 |  | 3 | https://www.gan.fr/app/uploads/2025/01/Tableau-TNS_CCSF_Lisibilite-GSP_2025.pdf |
| Lisibilité Prévoyance GVMP non salariés | product_sheet | prevoyance | 2026-01 | Groupama Gan Vie | 6 | https://www.gan.fr/app/uploads/2025/12/Tableau-TNS_CCSF_Lisibilite-GSP_2026.pdf |
| Lisibilité Prévoyance GVMP salariés | product_sheet | prevoyance | 2025 |  | 5 | https://www.gan.fr/app/uploads/2024/12/Tableau-salarie-secteur-prive-_CCSF-VF-GA.pdf |
| Tableaux d’exemples de prise en charge au 01/01/2025 des garanties Incapacité / invalidité / décès en vigueur | product_sheet | prevoyance | 2025 |  | 3 | https://www.ganpatrimoine.fr/Media/documents/Exemple%20tableaux%20de%20garanties%20pr%C3%A9voyance%20TNS/Tableau-TNS-CCSF-Lisibilit%C3%A9-GPP-2025.pdf |
| Travailleurs non-salariés Exemples de prise en charge au 01/01/2026 des garanties incapaci | product_sheet | prevoyance | 2026-01 | Groupama Gan Vie | 6 | https://www.ganprevoyance.fr/securite-professionnel-gan-prevoyance-protection/2-2/telecharger-le-tableau-des-garanties.pdf?date=20251222151901 |
| Gan Assurance Nouvelle Vie | conditions_tarifaires | retraite | 2026-03 | Groupama Gan Vie | 1 | https://www.gan.fr/app/uploads/2026/03/Gan-Nouvelle-Vie-Retraite-Fiche-Infos-Frais.pdf |
| Gan Nouvelle Vie (Gan Patrimoine) | conditions_tarifaires | retraite |  | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/documents/Transparence%20frais%20contrat/Transparence%20des%20frais%20Gan%20Patrimoine%20Nouvelle%20Vie.pdf |
| Gan Patrimoine Nouvelle Vie | conditions_tarifaires | retraite |  | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/documents/Transparence%20frais%20contrat/Gan-Patrimoine-Nouvelle-Vie.pdf |
| Gan Patrimoine Objectif Retraite | conditions_tarifaires | retraite |  | Groupama Gan Vie | 1 | https://www.ganpatrimoine.fr/Media/documents/Transparence%20frais%20contrat/Gan-Patrimoine-Objectif-Retraite.pdf |
| Gan Performance Retraite | conditions_tarifaires | retraite | 2026-03 | Groupama Gan Vie | 1 | https://www.gan.fr/app/uploads/2026/03/Gan-Performance-Retraite-Fiche-Infos-Frais.pdf |
| Gan Prevoyance Retraite Active | conditions_tarifaires | retraite | 2026-03 |  | 1 | https://www.ganprevoyance.fr/assurance-vie-retraite/1-4/fiche-d-information-frais-du-contrat-retraite-active.pdf?date=20260318121327 |
| Gan Prévoyance Nouvelle Vie | conditions_tarifaires | retraite | 2026-03 |  | 1 | https://www.ganprevoyance.fr/plan-epargne-retraite/2-3/fiche-d-information-sur-les-frais-du-per-individuel-gan-nouvelle-vie.pdf?date=20260318121107 |
| Gan Patrimoine Objectif Retraite | product_sheet | retraite | 2025-03 | Groupama Gan Vie | 3 | https://www.ganpatrimoine.fr/Media/documents/DIC/DIC%20GL%20Objectif%20Retraite%20Gan%20Patrimoine_2025_03_05.pdf |
| Gan Performance Retraite | product_sheet | retraite | 2026-06 | Groupama Gan Vie | 3 | https://www.gan.fr/app/uploads/2026/07/GAN-Performance-Retraite-Infos-Cles.pdf |
| Gan Prévoyance Retraite Active | product_sheet | retraite | 2025-03 | Groupama Gan Vie | 3 | https://www.ganprevoyance.fr/epargne-handicap/2-3/document-d-informations-cles-dic-gan-prevoyance-retraite-active.pdf?date=20250428141040 |
| Gan Prévoyance Santé | ipid | sante | 2023-11 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/complementaire-sante-gan-prevoyance/2-1/document-d-informations-gan-prevoyance-sante.pdf?date=20231127095936 |
| Gan Prévoyance Santé Sénior | ipid | sante | 2023-11 | Groupama Gan Vie | 2 | https://www.ganprevoyance.fr/complementaire-sante-gan-prevoyance/2-2/document-d-informations-gan-prevoyance-sante-senior.pdf?date=20231127095936 |
| Tableau de garanties des exemples de remboursement | product_sheet | sante | 2025-03 | Gan Assurances | 8 | https://www.gan.fr/app/uploads/2025/03/Tableau-de-garanties-2025.pdf |
| Tableau de garanties des exemples de remboursement | product_sheet | sante | 2026-02 | Gan Assurances | 8 | https://www.gan.fr/app/uploads/2026/03/Tableau-de-garanties-GAN-Sante-02-2026.pdf |

## Found but not ingestable

| file | why |
|---|---|
| DIC_Fonds_En_Euros_Gan_Assurances_2025_02_20.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD1.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Dynamique_Gan-Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Equilibre_Durable_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Equilibre_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Modere_Durable_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Modere_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Offensif_Durable_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Offensif_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Serenite_Durable_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Serenite_Gan_Assurance_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIC-FONDS-EN-EURO-GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIC-FONDS-EN-EURO-RETRAITE-GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS-GDT-Modere_Thematique_FEP_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GDT_Dynamique_Thematique_DH_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GDT_Dynamique_Thematique_FEP_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GDT_Equilibre_Thematique_DH_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GDT_Equilibre_Thematique_FEP_GASS.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GDT_Modere_Thematique_DH_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion-_Deleguee_Equilibre_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Dynamique_Durable_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Dynamique_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Equilibre_Durable_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Modere_Durable_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Modere_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Offensif_Durable_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Offensif_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Serenite_Durable_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_Gestion_Deleguee_Serenite_GASS-2026-07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIC_Fonds_En_Euros_Gan_Patrimoine_2025_02_20.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Dynamique_Durable_Gan%20Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Dynamique_Gan_Patrimoine_2025_02_07.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Equilibr%C3%A9_Durable_Gan%20Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Equilibr%C3%A9_Gan_Patrimoine%20_2025_02_11.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Mod%C3%A9r%C3%A9_Durable_Gan_Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Mod%C3%A9r%C3%A9_Gan_Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Offensif%20Durable_Gan%20Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Offensif_Gan_Patrimoine%20_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_S%C3%A9r%C3%A9nit%C3%A9_Durable_Gan_Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_S%C3%A9r%C3%A9nit%C3%A9_Gan_Patrimoine_2025_02_13.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIS_GD_Tranquillit%C3%A9_Durable_Gan_Patrimoine_2025_02_12.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| DIC_FONDS_EN_EUROS.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |
| document-d-informations-cles-dic-fonds-en-euros.pdf?date=20250428141040 | euro-fund information sheet, not an insurance product: the fonds en euros is an investment support inside a life or retirement contract, not a contract of its own. |
| DIC-Magestia.pdf | per-fund / per-profile PRIIPs sheet (DIC / DIS), not an insurance product: it describes an investment option inside a life contract. Ingesting these would show one contract as dozens of products. |

## One document is not a Gan product

`telecharger-le-document.pdf?date=20250103140538`, served from `ganprevoyance.fr`, prints
**« Galya Prévoyance Entreprise »** and nothing links it to the Gan brand. It is a collective
employer scheme, not an individual contract, and like the other CCSF lisibilité tables in this
library it **names no insurer at all** — only « l'organisme assureur ».

It is kept, because it is genuinely published on a Gan network's public site and dropping it
would hide a real document. But it should not be read as a Gan-branded product, and its carrier
is unknown from the document. Recorded here rather than silently reattributed or deleted.

## Carrier, restated after extraction

Extraction confirmed the discovery finding and sharpened it. Across the 50 ingested documents,
**« Gan Assurances » is named as the insurer essentially nowhere.** What the documents actually
print:

- **Groupama Gan Vie** (RCS Paris 340 427 616) as assureur or initiateur, on the large majority.
- **Groupama Gan Vie and Gan Assurances jointly**, under a single « Compagnie : » line, on the
  three emprunteur documents.
- **Société Française de Protection Juridique (SFPJ)**, RCS Paris B 321776775, as a second
  carrier on two of the Gan Patrimoine obsèques documents. Not anticipated by discovery.
- **Mutuaide Assistance** as co-signer of the assistance guarantees on several prévoyance and
  santé documents.
- **No insurer whatsoever** on the CCSF lisibilité tables, which say only « l'organisme
  assureur ».

Gan Patrimoine (RCS Lille 457 504 694, ORIAS 09 051 780) and Gan Prévoyance (ORIAS 09 051 779)
appear as intermediaries, never as carriers, exactly as their own footers state.

## Editions and duplicates found only at extraction

- The two **Gan Santé** guarantee tables, dated 03/2025 and 02/2026, are **byte-for-byte
  identical in every guarantee label and every Niveau 1 to 5 value** — verified programmatically,
  0 of 36 rows differ. Only the footer print code distinguishes them. The 2025 one is marked
  superseded; the pair is worth remembering as evidence that a new edition of a French tariff
  document does not imply a change in cover.
- **Gan Patrimoine Protection Plus** and **Gan Prévoyance Protection** are the same contract word
  for word, differing only in product name and print code, and carry the same date. Parallel
  network variants, not editions, so neither supersedes the other.

## The three emprunteur documents are not interchangeable

Same group contract, three distribution networks, and genuinely different cover:

| | Gan Assurances | Gan Patrimoine | Gan Prévoyance |
|---|---|---|---|
| PTIA ends at | 65 ans | **70 ans** | 65 ans |
| « Aide à la famille » | no | **yes, 50 % of the quotité** | no |
| Résiliation regime | current | current | **pre-Lemoine (12 mois / 2 mois)** |

The Gan Prévoyance document still describes the résiliation regime that applied before the loi
Lemoine of 2022 allowed termination at any time. Recorded as printed; it is a staleness finding,
not an extraction error.
