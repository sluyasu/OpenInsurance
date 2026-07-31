---
type: moc
domain: insurance
country: fr
lang: fr
tags: [insurance/fr, moc]
aliases: [France MOC, France]
date: 2026-07-30
status: ready
generated: false
---

## France - carte du marché

Le marché français de l'assurance est supervisé par une seule autorité, l'[[ACPR]] (Autorité de contrôle
prudentiel et de résolution, adossée à la Banque de France), mais les organismes qui le composent relèvent de
**trois codes différents**, et le code détermine la forme juridique, la gouvernance et une partie de la gamme :

| Code | Type d'organisme | Organismes agréés |
|---|---|---|
| Code des assurances | sociétés anonymes, sociétés d'assurance mutuelles | 310 |
| Code de la mutualité | mutuelles, unions de mutuelles | 286 |
| Code de la sécurité sociale | institutions de prévoyance | 32 |

C'est la différence structurelle avec les deux autres pays couverts : la Belgique a un superviseur et un
régime, la Suisse a deux superviseurs répartis par activité, la France a un superviseur et trois régimes.
Le registre officiel est publié par l'ACPR sous le nom **Refassu** et régénéré quotidiennement. Le détail,
les chiffres et leur source figurent dans le recensement de marché du dépôt (`_meta/fr-market-census.md`).

Attention aux faux amis : une *mutuelle* est un organisme régi par le Code de la mutualité, et dans l'usage
courant « ma mutuelle » désigne la complémentaire santé elle-même ; une *société d'assurance mutuelle* est un
organisme régi par le Code des assurances. Les deux se traduisent par « mutual » et ne recouvrent pas la même
chose.

## Distributeurs et porteurs de risque

En France, une marque grand public n'est pas nécessairement un assureur. Beaucoup de marques sont des
**mandataires ou courtiers inscrits à l'ORIAS** qui distribuent le papier d'un porteur de risque. Le registre
de l'ACPR liste les porteurs de risque ; l'ORIAS liste les intermédiaires. Chaque document contractuel nomme
lui-même son assureur, sous une rubrique « Assureur » ou « Qui vous assure ? », parce que la directive sur la
distribution d'assurances l'impose : l'attribution se lit donc dans le document, elle ne se déduit pas de la
marque.

## Branches

La segmentation retenue ici est celle du marché français vu du souscripteur. Chaque branche porte, quand elle
existe, la référence à la nomenclature prudentielle de l'**article R. 321-1 du Code des assurances**, qui est
le découpage sur lequel l'ACPR délivre les agréments.

- [[Assurance auto]] (RC obligatoire, art. L. 211-1)
- [[Multirisque habitation]]
- [[Complémentaire santé]]
- [[Assurance emprunteur]]
- [[Assurance construction]]
- Autres branches : voir [[00 - Branches MOC]]

Trois branches n'ont d'équivalent ni en Belgique ni en Suisse et sont proprement françaises :
l'[[Assurance emprunteur]], l'[[Assurance construction]] (décennale et dommages-ouvrage, loi du 4 janvier
1978) et l'assurance des [[EDPM et mobilités douces]], rendue obligatoire par le décret du 23 octobre 2019.

Les dix-sept branches effectivement peuplées par les produits documentés ont leur fiche conceptuelle dans
`branches/`. Les branches déclarées dans la taxonomie mais encore sans produit (assurance vie et épargne,
retraite, voyage, navigation, animaux, transport, crédit et caution, cyber) n'en ont pas : `make validate`
les signale une par une plutôt que de les passer sous silence.

## Assureurs documentés

<!-- BEGIN GENERATED: insurers -->
- [Direct Assurance](insurers/Direct%20Assurance.md) (11 documents)
- [Gan Assurances](insurers/Gan%20Assurances.md) (50 documents)
- [Groupama](insurers/Groupama.md) (30 documents)
- [Luko](insurers/Luko.md) (14 documents)
- [MAIF](insurers/MAIF.md) (69 documents)
- [Matmut](insurers/Matmut.md) (9 documents)
- [Thélem assurances](insurers/Th%C3%A9lem%20assurances.md) (45 documents)
<!-- END GENERATED -->

## Portée et limites

Le document public standard en France est l'**IPID** (document d'information sur le produit d'assurance,
format imposé au niveau européen). Les conditions générales sont publiées par certains assureurs et remises
seulement à la souscription par d'autres. Le corpus français est donc plus riche en IPID qu'en conditions
générales, ce qui est une observation sur la pratique de publication, pas un manquement des assureurs :
publier l'IPID est une obligation, publier les conditions générales n'en est pas une.
