---
type: product
domain: insurance
country: fr
insurer: '[[Macif]]'
insurer_slug: macif
branch: obseques
product_name: Garantie Obsèques
document_type: other
target_audience: null
target_audience_note: Le document ne désigne son public que par « l'adhérent » et
  « votre contrat obsèques » ; aucune catégorie de clientèle n'est indiquée.
reference: null
edition_date: null
lang: fr
tags:
- insurance/fr/obseques
- product
- insurer/macif
aliases:
- Garantie Obsèques
source_url: https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_prevoyance/tableau-principaux-indicateurs-economiques-garantie-obseques.pdf
source_pages: 1
fetched_at: '2026-08-01'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: garantie-obseques
variant: null
edition_status: null
edition_age_years: null
superseded: null
extends: null
freshness: '2026-08-01'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Publication annuelle d'information et de transparence sur les droits exprimés en euros de la Garantie Obsèques : un tableau d'une page reprenant les principaux indicateurs économiques du contrat pour les exercices 2024 et 2025. Il donne le rendement garanti moyen, le taux moyen des frais prélevés par la mutuelle, le rendement net moyen servi à l'adhérent, le taux des taxes et prélèvements sociaux et le taux moyen de la participation aux bénéfices, ainsi que l'éligibilité des contrats aux affaires nouvelles. Le document ne décrit ni garanties, ni exclusions, ni modalités contractuelles : c'est une publication chiffrée, pas une notice.

- Assureur : [Macif](../../insurers/Macif.md) · Branche : [Obsèques](../../branches/Obs%C3%A8ques.md) · Type : Document

## Prime

- Le taux moyen des frais prélevés par la mutuelle au titre des droits exprimés en euros : 25,51 % (2024), 27,37 % (2025).
- Le taux des taxes et des prélèvements sociaux en vigueur au 1er janvier de l'exercice : 0,39 % (2024), 0,38 % (2025).
- Le document ne donne aucune information sur la cotisation elle-même (montant, périodicité, revalorisation) : il ne porte que sur le rendement et les frais des droits exprimés en euros.

## Conditions particulières

- « Publication relative à l'information et la transparence des droits exprimés en euros ». Le tableau reprend les principaux indicateurs économiques du contrat obsèques, pour les deux exercices 2024 et 2025 présentés en colonnes. p. 1
- 2024 : 0,50 % — 2025 : 0,50 %. p. 1
- 2024 : 25,51 % — 2025 : 27,37 %. p. 1
- 2024 : 0,66 % — 2025 : 0,85 %. p. 1
- 2024 : 0,39 % — 2025 : 0,38 %. p. 1
- 2024 : 2,25 % — 2025 : 2,31 %. p. 1
- « Oui, pour l'offre Garantie Obsèques commercialisée depuis 2019 ». La même mention vaut pour les deux colonnes 2024 et 2025 : le contrat reste ouvert aux affaires nouvelles. p. 1
- Le document parle de « la mutuelle » qui prélève les frais et de « l'adhérent » à qui le rendement net est servi — vocabulaire du Code de la mutualité (adhésion à un règlement mutualiste), et non de « l'assureur » et « le souscripteur » du Code des assurances. p. 1

## Lacunes d'extraction

- PORTEUR DE RISQUE NON NOMMÉ : le document ne nomme aucune entité juridique. Il n'y a ni mention légale, ni SIREN, ni adresse de siège social, ni numéro d'agrément. Le texte ne dit que « la mutuelle » (« Le taux moyen des frais prélevés par la mutuelle ») et « l'adhérent ». Le porteur de risque ne peut donc pas être déterminé à partir de ce document et n'a pas été déduit : le vocabulaire (mutuelle / adhérent) indique une mutuelle relevant du Livre II du Code de la mutualité, mais aucun nom n'est imprimé. À rapprocher d'un autre document du même produit pour l'établir.
- AUCUNE DATE D'ÉDITION : le document ne porte ni date d'édition, ni code de référence en dernière page, ni mention « édition MM/AAAA ». `edition_date` est laissé null. Les seules années imprimées, 2024 et 2025, sont les deux exercices comparés dans le tableau — ce sont les millésimes des données, pas la date d'édition du document, et elles n'ont pas été reportées dans `edition_date`. (Comportement connu de l'éditeur sur ce corpus : de nombreux documents Macif ne portent aucune date d'édition.)
- AUCUNE RÉFÉRENCE : pas de code de référence imprimé (aucune chaîne de la forme <FAMILLE>/<PRODUIT>/05 - MM/AA - N<nnn>), donc `reference` est null. Le nom de fichier (tableau-principaux-indicateurs-economiques-garantie-obseques.pdf) ne porte pas non plus de date ; rien n'a été inféré du nom de fichier.
- DOCUMENT NON CONTRACTUEL : ce PDF d'une page est une publication de transparence financière, pas une notice ni un règlement mutualiste. Il ne contient par nature AUCUNE garantie, AUCUNE exclusion, aucune définition, aucun délai d'attente, aucune obligation de l'adhérent, aucune procédure de sinistre, aucune clause de durée / résiliation / prescription et aucune franchise. Les tableaux `coverages`, `exclusions`, `definitions`, `waiting_periods`, `obligations`, `claims_procedure` sont donc vides et `deductibles`, `duration_and_cancellation`, `prescription_period` sont null — c'est l'état réel de la source, pas une extraction incomplète. Les six indicateurs chiffrés ont été portés dans `special_conditions` faute d'emplacement plus juste dans le schéma.
- `target_audience` laissé null : le document n'énonce aucune cible commerciale. Sa seule désignation de personne est « l'adhérent ». La catégorie n'a pas été déduite du type de produit.
- MISE EN PAGE EN TABLEAU : le texte extrait restitue le tableau en colonne — libellé de la ligne, puis la valeur 2024, puis la valeur 2025. L'appariement libellé / année repose sur cet ordre et sur l'en-tête « 2024 » puis « 2025 » en tête de flux ; il est cohérent sur les six lignes. Une cellule d'en-tête vide ressort comme un tiret isolé (« - ») avant « 2024 ».
- Aucune mention de l'autorité de contrôle (ACPR) ni d'un quelconque dispositif de réclamation ou de médiation dans le document.
- Texte vérifié : les quotes sont des tranches exactes du texte ré-extrait du PDF local (PyMuPDF, page.get_text("text")), lequel est identique caractère pour caractère au texte fourni dans le prompt une fois les marqueurs [page N] retirés. Le document contient 5 apostrophes typographiques U+2019 (aucune apostrophe ASCII), aucun espace de largeur nulle, aucun tiret conditionnel et aucun glyphe de zone privée.

## Documents liés

- [contrat GARANTIE OBSÈQUES - IPID](contrat%20GARANTIE%20OBS%C3%88QUES%20-%20IPID.md) - IPID / Fiche d'information, éd. 01/26
- [Garantie Obsèques - IPID](Garantie%20Obs%C3%A8ques%20-%20IPID.md) - IPID / Fiche d'information, éd. 1er juillet 2026
- [Garantie Obsèques - Fiche](Garantie%20Obs%C3%A8ques%20-%20Fiche.md) - Fiche produit, éd. Garanties en vigueur au 1er juillet 2026

## Source & fidélité

- Source : [https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_prevoyance/tableau-principaux-indicateurs-economiques-garantie-obseques.pdf](https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_prevoyance/tableau-principaux-indicateurs-economiques-garantie-obseques.pdf) - téléchargé le 2026-08-01 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
