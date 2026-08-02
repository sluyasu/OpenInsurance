---
type: product
domain: insurance
country: fr
insurer: '[[MAIF]]'
insurer_slug: maif
branch: autres
product_name: Barème de frais applicables à compter du 01/07/2024 pour les Associations
  et les Collectivités
document_type: conditions_tarifaires
target_audience: null
target_audience_note: 'Le document ne nomme aucune catégorie de clientèle au sens
  des cases disponibles ; son titre indique « Barème de frais applicables à compter
  du 01/07/2024 pour les Associations et les Collectivités ». Il précise également
  : « * Les écoles maternelles et primaires sont exemptées du paiement du droit d’adhésion.
  »'
reference: null
edition_date: 07/2024
lang: fr
tags:
- insurance/fr/autres
- product
- insurer/maif
aliases:
- Barème de frais applicables à compter du 01/07/2024 pour les Associations et les
  Collectivités
source_url: https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/associations-collectivites/bareme-frais-associations-et-collectivites.pdf
source_pages: 1
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: bareme-de-frais
variant: Associations et Collectivités
edition_status: null
edition_age_years: 2
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Barème de frais MAIF applicable à compter du 01/07/2024 aux contrats des Associations et des Collectivités. Le document d’une page répertorie, hors tout contrat particulier, le droit d’adhésion, les frais de fractionnement de la cotisation annuelle (paiement en 2 fois et en 12 fois), les frais d’impayés et la contribution « solidarité victimes terrorisme infractions », avec pour chaque somme le montant HT, le montant TTC et le taux de taxes. Il ne décrit aucune garantie et n’énonce aucune exclusion.

- Assureur : [MAIF](../../insurers/MAIF.md) · Branche : [Autres](../../branches/Autres.md) · Type : Conditions tarifaires · Édition : 07/2024

## Prime

- Pourquoi ce document ? Il répertorie l’ensemble des frais applicables en fonction des contrats détenus.
- Les montants TTC indiqués incluent les taxes sur les conventions d’assurance (lorsqu’elles s’appliquent).
- Droit d’adhésion* (Droit d’adhésion recouvrable une seule fois à la souscription du premier contrat) : Montant HT 5,00 €, Montant TTC 5,00 €, Taux de taxes 0 %.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 2 X », contrat(s) détenu(s) « Vam seul ou Raqvam + Vam ou Auto-mission » : Frais HT 1 %, Frais TTC 1,33 %, Taux de taxes 33 %.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 2 X », contrat(s) détenu(s) « Raqvam uniquement » : Frais HT 1 %, Frais TTC 1,09 %, Taux de taxes 9 %.
- Pour le paiement en 2 fois, le montant des frais est calculé à partir de la cotisation annuelle HT.
- Frais de paiement applicables en cas de fractionnement de la cotisation annuelle — Modalité de paiement « 12 X », contrat(s) détenu(s) « Quel que soit le contrat » : Frais HT 1,80 %, Frais TTC 2,39 %, Taux de taxes 33 %.
- Pour le paiement en 12 fois, le montant des frais est calculé à partir de la cotisation annuelle TTC.
- Frais d’impayés (Frais d’impayés applicables en cas de défaut de paiement de la cotisation) : Montant HT 5,34 €, Montant TTC 7,10 €, Taux de taxes 33 %.
- Note 1 du barème : 1. Frais HT x taux de taxes applicable.
- Note 2 du barème : 2. Taux spécifiques appliqués à Saint-Martin 10 %, à Monaco 7 % et à Saint-Barthélemy 0 %.

## Conditions particulières

- * Les écoles maternelles et primaires sont exemptées du paiement du droit d’adhésion. p. 1
- La contribution « solidarité victimes terrorisme infractions » est fixée à 6,50 €. Elle est perçue à la souscription puis une fois par an, à l’échéance, au profit du Fonds de garantie des victimes d’actes de terrorisme et d’autres infractions (FGTI), pour chaque contrat comportant une garantie dommages. Elle n’est ni fractionnable lors de la souscription, ni remboursable en cas de suppression ou de résiliation en cours d’année. p. 1
- 2. Taux spécifiques appliqués à Saint-Martin 10 %, à Monaco 7 % et à Saint-Barthélemy 0 %. (renvoi porté sur les colonnes « Taux de taxes » du tableau « 12 X » et du tableau des frais d’impayés). p. 1
- MAIF Société d’assurance mutuelle à cotisations variables Entreprise régie par le Code des assurances CS 90000 - 79038 Niort cedex 9 p. 1

## Lacunes d'extraction

- Ce document n’est pas un contrat : c’est un barème de frais d’une page. Il ne décrit aucune garantie et n’énonce aucune exclusion — `coverages` et `exclusions` sont donc volontairement vides, et non incomplets. Le contenu tarifaire a été porté dans `premium.notes` et `special_conditions`.
- Aucun nom de produit commercial n’est imprimé. Le `product_name` reprend le titre du document (« Barème de frais applicables à compter du 01/07/2024 pour les Associations et les Collectivités »), qui est un titre de barème et non un produit d’assurance.
- Le barème est transverse à plusieurs contrats, qu’il nomme sans les décrire : Vam, Raqvam, Auto-mission, ainsi que « Quel que soit le contrat ». Le document ne dit pas ce que recouvrent ces contrats.
- Aucune référence interne de document n’est imprimée. La date d’édition n’apparaît pas non plus dans le nom de fichier : elle est le « 07/2024 » isolé en dernière ligne de la page, sous le bloc d’identification MAIF. Le titre porte par ailleurs une date d’application distincte : « à compter du 01/07/2024 ».
- L’assureur imprimé est MAIF, « Société d’assurance mutuelle à cotisations variables, Entreprise régie par le Code des assurances, CS 90000 - 79038 Niort cedex 9 ». Aucun SIREN/RCS n’est imprimé sur ce document, et MAIF VIE n’y est pas mentionnée.
- Le tableau des frais de fractionnement en 2 fois distingue deux situations (« Vam seul ou Raqvam + Vam ou Auto-mission » à 1,33 % TTC / 33 % de taxes, et « Raqvam uniquement » à 1,09 % TTC / 9 % de taxes) ; le document n’explicite pas le sort des autres combinaisons de contrats.
- Aucune cible de clientèle au sens réglementaire n’est déclarée : `target_audience` reste null. Le titre vise « les Associations et les Collectivités », qui ne correspond à aucune des valeurs autorisées prises isolément (les collectivités relèveraient de `secteur_public`, les associations d’aucune).
- Le texte de la page contient des espaces fines U+2009 dans plusieurs libellés d’appels de note ; les montants de cette édition sont en revanche saisis avec des espaces ordinaires. Les montants sont reproduits tels qu’imprimés.
- Le texte du PDF a été vérifié caractère par caractère contre une ré-extraction PyMuPDF `page.get_text("text")` du fichier local : identique, 2 081 caractères, 1 page — pas de troncature.

## Documents liés

- [Barème de frais - Tarifs](Bar%C3%A8me%20de%20frais%20-%20Tarifs.md) - Conditions tarifaires, éd. 03/2026

## Source & fidélité

- Source : [https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/associations-collectivites/bareme-frais-associations-et-collectivites.pdf](https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/associations-collectivites/bareme-frais-associations-et-collectivites.pdf) - téléchargé le 2026-07-30 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
