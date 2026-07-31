---
type: product
domain: insurance
country: fr
insurer: '[[MAIF]]'
insurer_slug: maif
branch: rc-privee
product_name: Fiche d'information responsabilité civile
document_type: other
target_audience: null
target_audience_note: null
reference: null
edition_date: 10/2021
lang: fr
tags:
- insurance/fr/rc-privee
- product
- insurer/maif
aliases:
- Fiche d'information responsabilité civile
source_url: https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/fiche-informations-responsabilite-civile.pdf
source_pages: 1
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: fiche-dinformation-responsabilite-civile
variant: null
edition_status: null
edition_age_years: 5
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Fiche d'information réglementaire remise par MAIF en application de l'article L112-2 du Code des assurances et conforme à l'annexe de l'article A112 du même code. Elle n'est pas un contrat : elle explique le fonctionnement dans le temps de la garantie responsabilité civile et précise que la garantie du contrat MAIF est déclenchée par le fait dommageable. Elle définit les notions de fait dommageable, de réclamation et de période de validité de la garantie, et indique à quel assureur la déclaration de sinistre doit être adressée.

- Assureur : [MAIF](../../insurers/MAIF.md) · Branche : [Responsabilité civile vie privée](../../branches/Responsabilit%C3%A9%20civile%20vie%20priv%C3%A9e.md) · Type : Document · Édition : 10/2021

## Définitions

| Terme | Définition | Page |
|---|---|---|
| Fait dommageable | Fait, acte ou événement à l'origine des dommages subis par la victime et faisant l'objet d'une réclamation. | p. 1 |
| Réclamation | Mise en cause de votre responsabilité civile soit par lettre adressée à l'assuré ou à l'assureur, soit par assignation devant un tribunal civil ou administratif. Un même sinistre peut faire l'objet de plusieurs réclamations, soit d'une même victime, soit de plusieurs victimes. | p. 1 |
| Période de validité de la garantie | Période comprise entre la date de prise d'effet de la garantie et, après d'éventuelles reconductions, sa date de résiliation ou d'expiration. | p. 1 |

## Obligations de l'assuré

- La déclaration de sinistre doit être adressée à l'assureur dont la garantie est ou était en cours de validité au moment où le fait dommageable s'est produit. (En cas de sinistre) p. 1

## Procédure de sinistre

1. La déclaration de sinistre doit être adressée à l'assureur dont la garantie est ou était en cours de validité au moment où le fait dommageable s'est produit. p. 1

## Conditions particulières

- La présente fiche d'information vous est délivrée en application de l'article L112-2 du Code des assurances. Elle a pour objet d'apporter les informations nécessaires à une bonne compréhension du fonctionnement de la garantie responsabilité civile dans le temps. Elle est établie conformément à l'annexe de l'article A112 du Code des assurances. p. 1
- Votre contrat : la garantie est déclenchée par le fait dommageable. L'assureur apporte sa garantie lorsqu'une réclamation consécutive à des dommages causés à autrui est formulée et que votre responsabilité ou celle des autres personnes garanties par le contrat est engagée, dès lors que le fait à l'origine de ces dommages est survenu entre la date de prise d'effet et la date de résiliation ou d'expiration de la garantie. p. 1
- MAIF Société d’assurance mutuelle à cotisations variables Entreprise régie par le Code des assurances CS 90000 - 79038 Niort cedex 9 p. 1

## Lacunes d'extraction

- Ce document n'est pas un contrat : c'est la fiche d'information réglementaire sur le fonctionnement dans le temps de la garantie responsabilité civile (annexe de l'article A112 du Code des assurances). Il ne décrit donc aucune garantie, aucun plafond, aucune franchise et aucune exclusion — d'où les tableaux coverages, exclusions, deductibles, premium et duration_and_cancellation vides ou nuls.
- Aucun nom commercial de produit n'est imprimé : le document ne se rattache à aucun contrat nommé. Le champ product_name reprend le titre imprimé « Fiche d'information responsabilité civile » ; le nom retenu dans le manifeste (« Fiche d'information responsabilité civile (annexe de l'article A112 du Code des assurances) ») ajoute le sous-titre, absent du titre lui-même.
- edition_date : le document ne porte qu'un « 10/2021 » nu, imprimé seul entre le corps du texte et le bloc assureur, sans mention « édition ». Aucun code interne n'accompagne cette date, contrairement aux autres documents MAIF, donc reference reste null. Les métadonnées PDF (/ModDate D:20211006150851+02'00') ne sont pas utilisées comme source.
- Assureur tel qu'imprimé : « MAIF - Société d'assurance mutuelle à cotisations variables - Entreprise régie par le Code des assurances - CS 90000 - 79038 Niort cedex 9 ». Aucun SIREN, aucun numéro RCS et aucune référence à MAIF VIE ne figurent sur ce document.
- target_audience : le document n'indique aucun public destinataire ; il n'est ni déduit du type de produit ni du contexte, et reste null.
- Le texte mélange apostrophes ASCII (') et courbes (U+2019) à l'intérieur d'une même page : les key_quotes ont été découpées programmatiquement dans le texte PyMuPDF pour préserver ces caractères tels quels.

## Source & fidélité

- Source : [https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/fiche-informations-responsabilite-civile.pdf](https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/commun/fiche-informations-responsabilite-civile.pdf) - téléchargé le 2026-07-30 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
