---
type: product
domain: insurance
country: fr
insurer: '[[MAIF]]'
insurer_slug: maif
branch: autres
product_name: Barème de frais
document_type: conditions_tarifaires
target_audience: null
target_audience_note: 'Le document ne déclare aucune cible de clientèle. Il ne cite
  de segment qu’en note de bas de page : « 1. Pour les souscripteurs du seul contrat
  Offre Métiers de l’Éducation, le montant du droit d’adhésion est de 1 € TTC. »'
reference: null
edition_date: 03/2026
lang: fr
tags:
- insurance/fr/autres
- product
- insurer/maif
aliases:
- Barème de frais
source_url: https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/bareme-frais.pdf
source_pages: 1
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: bareme-de-frais
variant: null
edition_status: null
edition_age_years: 0
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Barème de frais MAIF d’une page, édition 03/2026, transverse aux contrats détenus. Il répertorie le droit d’adhésion, les frais de paiement appliqués en cas de fractionnement de la cotisation annuelle (2 fois et 12 fois), les frais d’impayés et la contribution « solidarité victimes terrorisme infractions », en indiquant pour chaque somme le montant ou le taux HT, le montant ou le taux TTC et le taux de taxes. Il ne décrit aucune garantie et n’énonce aucune exclusion.

- Assureur : [MAIF](../../insurers/MAIF.md) · Branche : Autres · Type : Conditions tarifaires · Édition : 03/2026

## Prime

- Pourquoi ce document ? Il répertorie l’ensemble des frais applicables en fonction des contrats détenus.
- Les montants TTC indiqués incluent les taxes sur les conventions d’assurance (lorsqu’elles s’appliquent).
- Droit d’adhésion1 (Somme recouvrable une seule fois à la souscription du premier contrat) : Montant HT 5,00 €, Montant TTC 5,00 €, Taux de taxes 0 %.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 2 X », contrat(s) détenu(s) « Présence d’un contrat Auto » : Frais HT 1 %, Frais TTC 1,33 %, Taux de taxes 33 %.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 2 X », contrat(s) détenu(s) « Autres situations » : Frais HT 1 %, Frais TTC 1,09 %, Taux de taxes 9 %.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 12 X », contrat(s) détenu(s) « Quel que soit le contrat » : Frais HT 1,80 %, Frais TTC 2,39 %, Taux de taxes 33 %.
- Pour le paiement en 2 fois, le montant des frais est calculé à partir de la cotisation annuelle HT.
- Pour le paiement en 12 fois, le montant des frais est calculé à partir de la cotisation annuelle TTC.
- Frais d’impayés (Frais d’impayés applicables en cas de défaut de paiement de la cotisation) : Montant HT 5,34 €, Montant TTC 7,10 €, Taux de taxes 33 %.
- Note 1 du barème : 1. Pour les souscripteurs du seul contrat Offre Métiers de l’Éducation, le montant du droit d’adhésion est de 1 € TTC.
- Note 2 du barème : 2. Frais HT x taux de taxes applicable.

## Conditions particulières

- 1. Pour les souscripteurs du seul contrat Offre Métiers de l’Éducation, le montant du droit d’adhésion est de 1 € TTC. p. 1
- La contribution « solidarité victimes terrorisme infractions » est fixée à 6,50 €. Elle est perçue à la souscription puis une fois par an, à l’échéance, au profit du Fonds de garantie des victimes d’actes de terrorisme et d’autres infractions (FGTI), pour chaque contrat comportant une garantie dommages. Elle n’est ni fractionnable lors de la souscription, ni remboursable en cas de suppression ou de résiliation en cours d’année. p. 1
- Pour le paiement en 12 fois et les frais d’impayés, des taux de taxes spécifiques sont appliqués à Saint-Martin 10 %, à Monaco 7 % et à Saint-Barthélemy 0 %. p. 1
- MAIF Société d’assurance mutuelle à cotisations variables Entreprise régie par le Code des assurances CS 90000 - 79038 Niort cedex 9 p. 1

## Lacunes d'extraction

- Ce document n’est pas un contrat : c’est un barème de frais d’une page. Il ne décrit aucune garantie et n’énonce aucune exclusion — `coverages` et `exclusions` sont donc volontairement vides, et non incomplets. Le contenu tarifaire a été porté dans `premium.notes` et `special_conditions`.
- Aucun produit commercial n’est nommé. Le titre imprimé est le générique « Barème de frais », sans qualificatif de segment ni référence interne : ce nom risque d’entrer en collision, côté wiki, avec les autres barèmes MAIF (notamment le « Barème de frais applicables à compter du 01/07/2024 pour les Associations et les Collectivités », source distincte). Ils sont groupés ici sous le même `product_family` « Barème de frais », le présent document sans `variant`.
- Ce barème et le barème « Associations et Collectivités » sont des variantes parallèles, pas deux éditions d’un même document : leurs tableaux diffèrent sur le fond. Ici la ligne « 2 X » distingue « Présence d’un contrat Auto » (1,33 % TTC / 33 %) et « Autres situations » (1,09 % TTC / 9 %) ; l’autre barème distingue « Vam seul ou Raqvam + Vam ou Auto-mission » et « Raqvam uniquement ». De même, les taux de taxes spécifiques (Saint-Martin, Monaco, Saint-Barthélemy) sont ici limités au paiement en 12 fois et aux frais d’impayés, alors que l’autre barème les rattache à des colonnes « Taux de taxes » repérées par un appel de note. Aucun des deux n’est donc réputé périmé.
- Aucune référence interne n’est imprimée. La date d’édition n’est pas dans le nom de fichier : c’est le « 03/2026 » isolé en dernière ligne, sous le bloc d’identification MAIF. Le document n’indique pas de date d’application (contrairement au barème Associations et Collectivités).
- L’assureur imprimé est MAIF, « Société d’assurance mutuelle à cotisations variables, Entreprise régie par le Code des assurances, CS 90000 - 79038 Niort cedex 9 ». Aucun SIREN/RCS n’est imprimé et MAIF VIE n’est pas mentionnée.
- Le tableau des frais d’impayés ne porte pas d’appel de note sur sa colonne « Taux de taxes » : la couche texte fusionne l’en-tête en « Montant TTC Taux de taxes ». Le renvoi vers les taux spécifiques est fait par une phrase séparée, reproduite telle quelle.
- Les montants et taux de cette édition sont saisis avec des espaces fines U+2009 (« 5,00 € », « 1,33 % ») et des espaces insécables U+00A0 (« 6,50 € », « 1 € TTC », « en 2 fois ») ; ils sont reproduits tels qu’imprimés, sans normalisation.
- Le texte du PDF a été vérifié caractère par caractère contre une ré-extraction PyMuPDF `page.get_text("text")` du fichier local : identique, 1 971 caractères, 1 page — pas de troncature.

## Documents liés

- [Barème de frais applicables à compter du 01-07-2024 pour les Associations et les Collectivités - Tarifs](Bar%C3%A8me%20de%20frais%20applicables%20%C3%A0%20compter%20du%2001-07-2024%20pour%20les%20Associations%20et%20les%20Collectivit%C3%A9s%20-%20Tarifs.md) - Conditions tarifaires, éd. 07/2024

## Source & fidélité

- Source : [https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/bareme-frais.pdf](https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/bareme-frais.pdf) - téléchargé le 2026-07-30 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
