---
type: product
domain: insurance
country: fr
insurer: '[[Groupama]]'
insurer_slug: groupama
branch: retraite
product_name: Groupama Horizon Retraite
document_type: conditions_tarifaires
target_audience: null
target_audience_note: null
reference: null
edition_date: null
lang: fr
tags:
- insurance/fr/retraite
- product
- insurer/groupama
aliases:
- Groupama Horizon Retraite
source_url: https://assets.ctfassets.net/7awcp71bzphk/2KR970BhlHyMtEUnGDoYY4/d5f313002250b84601bf1df372961b02/Transparence-des-frais-Groupama-Horizon-Retraite.pdf
source_pages: 1
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: groupama-horizon-retraite
variant: null
edition_status: null
edition_age_years: null
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Fiche de transparence des frais du PER Individuel Groupama Horizon Retraite, publiée dans le cadre de l'engagement de Groupama Gan Vie à mettre à jour annuellement ces informations. Elle indique le montant minimal de versement, les frais annuels (frais de gestion du plan sur les supports en euros et en unités de compte, frais de gestion des fonds en gestion libre et en gestion pilotée/à horizon, avec le taux de rétrocessions de commissions), les autres frais annuels et les frais ponctuels par opération exprimés en taux maximal. Le document ne décrit aucune garantie, aucune exclusion et aucune modalité contractuelle : c'est un tableau de frais, pas un contrat.

- Assureur : [Groupama](../../insurers/Groupama.md) · Branche : Retraite supplémentaire · Type : conditions_tarifaires

## Définitions

| Terme | Définition | Page |
|---|---|---|
| Frais de gestion du plan ou du contrat | Frais prélevés directement par l'assureur sur l'encours en Unité de Compte ou en Euros. Peuvent s'y ajouter des frais selon le mode de gestion retenu. | p. 1 |
| Frais de gestion des fonds | Frais prélevés par les sociétés de gestion et qui se répercutent sur la performance des Unités de Compte. Ils ont été calculés sur la base d'une moyenne des frais de l'univers d'investissement disponible ; il s'agit donc d'une moyenne et la valeur exacte dépendra des Unités de Compte constituant l'encours du client. | p. 1 |
| Rétrocessions de commissions | Part rétrocédée à l'assureur au titre de la distribution des Unités de Compte. | p. 1 |

## Prime

- Montant minimal de versement : 300€ en versement libre ou 50€/ mois en versements périodiques
- Frais d'adhésion à l'association ayant souscrit le contrat : -
- Frais annuels — Frais de gestion du plan — Frais des supports fonds euros : 0,70%
- Frais annuels — Frais de gestion du plan — Frais des supports unités de compte : 0,96%
- Frais annuels — Frais de gestion du plan — Gestion à horizon : -
- Frais de gestion des fonds — 1/ Gestion libre — Fonds actions (moyenne) : 1,88% ; dont taux de rétrocessions de commissions : 0,94%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds obligations (moyenne) : 1,11% ; dont taux de rétrocessions de commissions : 0,57%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds immobilier (moyenne) : 1,85% ; dont taux de rétrocessions de commissions : 1,00%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds diversifiés (moyenne) : 1,63% ; dont taux de rétrocessions de commissions : 0,88%
- Frais de gestion des fonds — 2/ Mode de gestion pilotée ou standardisée — Gestion à horizon : 1,71% ; dont taux de rétrocessions de commissions : 0,97%
- Autres frais annuels — Frais forfaitaires : -
- Autres frais annuels — Frais proportionnels : 4€ (frais associatifs annuels)
- Frais ponctuels par opération (taux maximal) — Frais sur versement : 4,50%
- Frais ponctuels par opération (taux maximal) — Frais de changement de modes de gestion (en % ou €) : -
- Frais ponctuels par opération (taux maximal) — Frais d'arbitrage proportionnel ou forfaitaires : -
- Frais ponctuels par opération (taux maximal) — Frais d'arbitrage - nombre d'arbitrages gratuits par an : -
- Frais ponctuels par opération (taux maximal) — Frais de transferts sortant vers un autre produit : -
- Frais ponctuels par opération (taux maximal) — Frais sur les versements de rente : 3%
- Frais ponctuels par opération (taux maximal) — Frais de rachat : -

## Conditions particulières

- Afin de renforcer la transparence des frais sur ces contrats, Groupama Gan Vie s'engage à mettre à jour annuellement les informations ci-dessous. p. 1
- Groupama Assurances Mutuelles pour le compte des Caisses Régionales d'Assurances Mutuelles Agricoles. Caisse Nationale de Réassurance Mutuelle Agricole Groupama, RCS Paris 343 115 135 - Siège social: 8-10 rue d'Astorg - 75008 Paris. Les contrats d'assurance vie et de capitalisation sont assurés par Groupama Gan Vie, Société anonyme au capital de 1 371 100 605 euros, RCS Paris 340 427 616 - APE : 6511Z - Siège social : 8-10, rue d'Astorg - 75008 Paris. Entreprises régies par le Code des assurances et soumises à l'Autorité de Contrôle Prudentiel et de Résolution (ACPR), 4 place de Budapest - CS 92459 - 75436 Paris Cedex 09. p. 1

## Lacunes d'extraction

- Document de transparence des frais (fiche tarifaire CCSF) : il ne contient aucune garantie ni aucune exclusion. Les tableaux `coverages` et `exclusions` sont donc volontairement vides — les garanties, définitions contractuelles, obligations, durée et résiliation du PER figurent dans la notice/les conditions générales, non fournies ici.
- Aucune date d'édition, aucune référence interne et aucun numéro de version ne sont imprimés sur le document ; `edition_date` et `reference` restent null. Le seul repère temporel est l'engagement de mise à jour annuelle.
- Le document n'indique aucun public cible : `target_audience` laissé à null (la seule mention est « PER Individuel », qui n'est pas une déclaration de public visé).
- De nombreuses lignes de frais sont imprimées avec un simple tiret « - » sans préciser s'il s'agit d'une absence de frais ou d'une donnée non applicable : reproduites telles quelles.
- Le document est mis en page en colonnes ; l'appariement libellé/valeur restitué ici suit l'ordre du texte extrait. Les intitulés « Frais forfaitaires » (« - ») et « Frais proportionnels » (« 4€ (frais associatifs annuels) ») sont reproduits tels que le PDF les imprime, alors qu'un montant en euros figure sous la ligne « proportionnels ».
- Le porteur de risque nommé est Groupama Gan Vie SA (RCS Paris 340 427 616) ; la fiche est éditée par Groupama Assurances Mutuelles pour le compte des Caisses Régionales d'Assurances Mutuelles Agricoles, aucune caisse régionale n'étant nommée individuellement.
- L'association souscriptrice du contrat est évoquée (« Frais d'adhésion à l'association ayant souscrit le contrat ») mais n'est pas nommée dans ce document.

## Documents liés

- [Groupama Horizon Retraite - Fiche](Groupama%20Horizon%20Retraite%20-%20Fiche.md) - Fiche produit, éd. 01/06/2026

## Source & fidélité

- Source : [https://assets.ctfassets.net/7awcp71bzphk/2KR970BhlHyMtEUnGDoYY4/d5f313002250b84601bf1df372961b02/Transparence-des-frais-Groupama-Horizon-Retraite.pdf](https://assets.ctfassets.net/7awcp71bzphk/2KR970BhlHyMtEUnGDoYY4/d5f313002250b84601bf1df372961b02/Transparence-des-frais-Groupama-Horizon-Retraite.pdf) - téléchargé le 2026-07-30 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
