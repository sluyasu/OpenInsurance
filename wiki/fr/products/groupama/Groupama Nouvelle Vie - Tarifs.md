---
type: product
domain: insurance
country: fr
insurer: '[[Groupama]]'
insurer_slug: groupama
branch: retraite
product_name: Groupama Nouvelle Vie
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
- Groupama Nouvelle Vie
source_url: https://assets.ctfassets.net/7awcp71bzphk/4gPQ2YoChbWFKeDV4VBICJ/5d3845ce521da29f7bfef4258cc03e7d/transparence-des-frais-groupama-nouvelle-vie.pdf
source_pages: 1
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: groupama-nouvelle-vie
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

Fiche de transparence des frais du PER Individuel Groupama Nouvelle Vie, publiée dans le cadre de l'engagement de Groupama Gan Vie à mettre à jour annuellement ces informations. Elle indique le montant minimal de versement, les frais d'adhésion à l'association souscriptrice, les frais annuels (gestion du plan sur supports en euros et en unités de compte, frais de gestion des fonds en gestion libre et en gestion pilotée par horizon avec les taux de rétrocessions de commissions), les autres frais annuels et les frais ponctuels par opération en taux maximal. Le document ne décrit aucune garantie ni exclusion : c'est un tableau de frais, pas un contrat.

- Assureur : [Groupama](../../insurers/Groupama.md) · Branche : Retraite supplémentaire · Type : Conditions tarifaires

## Définitions

| Terme | Définition | Page |
|---|---|---|
| Frais de gestion du plan ou du contrat | Frais prélevés directement par l'assureur sur l'encours en Unité de Compte ou en Euros. Peuvent s'y ajouter des frais selon le mode de gestion retenu. | p. 1 |
| Frais de gestion des fonds | Frais prélevés par les sociétés de gestion et qui se répercutent sur la performance des Unités de Compte. Ils ont été calculés sur la base d'une moyenne des frais de l'univers d'investissement disponible ; il s'agit donc d'une moyenne et la valeur exacte dépendra des Unités de Compte constituant l'encours du client. | p. 1 |
| Rétrocessions de commissions | Part rétrocédée à l'assureur au titre de la distribution des Unités de Compte. | p. 1 |

## Prime

- Montant minimal de versement : 50 €/mois ou 300 € en versement libre
- Frais d'adhésion à l'association ayant souscrit le contrat : 5 €
- Frais annuels — Frais de gestion du plan — Frais des supports fonds euros : 0.70%
- Frais annuels — Frais de gestion du plan — Frais des supports unités de compte : 0.96%
- Frais annuels — Frais de gestion du plan — Gestion pilotée par horizon : -
- Frais de gestion des fonds — 1/ Gestion libre — Fonds actions (moyenne) : 1.72% ; dont taux de rétrocessions de commissions : 0.86%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds obligations (moyenne) : 1.08% ; dont taux de rétrocessions de commissions : 0.58%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds immobilier (moyenne) : 1.85% ; dont taux de rétrocessions de commissions : 1.00%
- Frais de gestion des fonds — 1/ Gestion libre — Fonds diversifiés (moyenne) : 1.53% ; dont taux de rétrocessions de commissions : 0.90%
- Frais de gestion des fonds — 2/ Gestion pilotée par horizon (allocation 20 ans avant le départ à la retraite) — Profil prudent (moyenne) : 1.51% ; dont taux de rétrocessions de commissions : 0.91%
- Frais de gestion des fonds — 2/ Gestion pilotée par horizon (allocation 20 ans avant le départ à la retraite) — Profil équilibré (moyenne) : 1.72% ; dont taux de rétrocessions de commissions : 1.00%
- Frais de gestion des fonds — 2/ Gestion pilotée par horizon (allocation 20 ans avant le départ à la retraite) — Profil dynamique (moyenne) : 1.82% ; dont taux de rétrocessions de commissions : 1.04%
- Autres frais annuels — Frais forfaitaires : 15 € (frais associatifs annuels)
- Autres frais annuels — Frais proportionnels : 5 € (frais associatifs annuels)
- Frais ponctuels par opération (taux maximal) — Frais sur versement : 4.50%
- Frais ponctuels par opération (taux maximal) — Frais de changement de modes de gestion (en % ou €) : -
- Frais ponctuels par opération (taux maximal) — Frais d'arbitrage proportionnel ou forfaitaires : -
- Frais ponctuels par opération (taux maximal) — Frais d'arbitrage - nombre d'arbitrages gratuits par an : -
- Frais ponctuels par opération (taux maximal) — Frais de transferts sortant vers un autre produit : 1% si moins de 5 ans 0% au-delà
- Frais ponctuels par opération (taux maximal) — Frais sur les versements de rente : 3.00%
- Frais ponctuels par opération (taux maximal) — Frais de rachat : -

## Conditions particulières

- Afin de renforcer la transparence des frais sur ces contrats, Groupama Gan Vie s'engage à mettre à jour annuellement les informations ci-dessous. p. 1
- Caisse Régionale d'Assurances Mutuelles Agricoles. Groupama Gan Vie, Société anonyme au capital de 1 371 100 605 euros - RCS Paris 340 427 616 - APE : 6511Z. Siège social : 8-10, rue d'Astorg - 75008 Paris. groupama.fr. Entreprises régies par le Code des assurances. p. 1

## Lacunes d'extraction

- Document de transparence des frais (fiche tarifaire CCSF) : il ne contient aucune garantie ni aucune exclusion. `coverages` et `exclusions` sont donc vides — les garanties, obligations, durée et résiliation du PER figurent dans la notice/les conditions générales, non fournies ici.
- Aucune date d'édition, aucune référence interne ni numéro de version imprimés : `edition_date` et `reference` restent null. Seul repère temporel : l'engagement de mise à jour annuelle.
- Le document n'indique aucun public cible : `target_audience` laissé à null.
- Incohérence interne relevée telle quelle : les « frais associatifs annuels » sont chiffrés à « 15 € (frais associatifs annuels) » sur la ligne « Frais forfaitaires » et à « 5 € (frais associatifs annuels) » sur la ligne « Frais proportionnels », tandis que la ligne « Frais d'adhésion à l'association ayant souscrit le contrat » indique « 5 € ». Les trois montants sont reproduits sans arbitrage.
- Plusieurs lignes de frais sont imprimées avec un simple tiret « - » sans préciser s'il s'agit d'une absence de frais ou d'une donnée non applicable : reproduites telles quelles.
- Les taux sont imprimés avec un point décimal (« 0.70% », « 4.50% ») et conservés tels quels.
- Le document est mis en page en colonnes et le texte extrait ne suit pas l'ordre de lecture : les « Remarques introductives », le titre et les mentions légales apparaissent après le tableau. L'appariement libellé/valeur restitué ici suit l'ordre du tableau imprimé.
- Mentions légales : le porteur du risque nommé est Groupama Gan Vie (RCS Paris 340 427 616) ; la « Caisse Régionale d'Assurances Mutuelles Agricoles » est mentionnée sans être identifiée nominativement, aucune caisse régionale précise n'est donc enregistrée.
- L'association souscriptrice du contrat n'est pas nommée dans ce document, bien que des frais d'adhésion à celle-ci soient chiffrés.

## Documents liés

- [Groupama Nouvelle Vie - Tarifs](Groupama%20Nouvelle%20Vie%20-%20Tarifs%20%282%29.md) - Conditions tarifaires

## Source & fidélité

- Source : [https://assets.ctfassets.net/7awcp71bzphk/4gPQ2YoChbWFKeDV4VBICJ/5d3845ce521da29f7bfef4258cc03e7d/transparence-des-frais-groupama-nouvelle-vie.pdf](https://assets.ctfassets.net/7awcp71bzphk/4gPQ2YoChbWFKeDV4VBICJ/5d3845ce521da29f7bfef4258cc03e7d/transparence-des-frais-groupama-nouvelle-vie.pdf) - téléchargé le 2026-07-30 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
