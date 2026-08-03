---
type: branch
domain: insurance
country: lu
branch: solde-restant-du
branch_code: "I"
lang: fr
langs: [fr, de, en]
mandatory: conditional
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/solde-restant-du, branch]
aliases: [Solde restant dû, SRD, Restschuldversicherung, Assurance solde restant dû]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: stub
generated: false
---

## Ce que c'est

L'assurance **solde restant dû** garantit le remboursement du capital encore dû sur un crédit — le
plus souvent immobilier — en cas de décès de l'emprunteur, et selon les contrats en cas d'invalidité
ou d'incapacité. L'indemnité va au prêteur, à hauteur de la quotité assurée.

## Pourquoi ce nom, et pourquoi c'est une branche à part

Le mécanisme est celui que la France appelle *assurance emprunteur*. **Le nom retenu ici est celui
que les documents luxembourgeois impriment**, et ce n'est pas un détail de vocabulaire : importer le
slug `emprunteur` aurait produit une branche dont aucun titre de contrat luxembourgeois ne porte le
libellé, ce qui casse à la fois la reconnaissance automatique et la recherche d'un lecteur.

C'est l'application de la règle qui gouverne toute la taxonomie de ce dépôt : **la segmentation est
celle du marché vu du souscripteur, pas une nomenclature importée**.

## À ne pas confondre avec la prévoyance

La distinction est ténue et le corpus en offre déjà un cas. Un contrat luxembourgeois liste
*« Couvrir un emprunt »* parmi ses objectifs — ce qui pousserait à le classer ici — mais son capital
est **explicitement constant**. Or le propre du solde restant dû est que le capital assuré **décroît
avec l'amortissement du prêt**. Un capital constant qui sert accessoirement à rembourser un crédit
est une [[Prévoyance et décès]], et c'est ainsi qu'il a été classé.

Le critère opérant est donc : **le capital suit-il le tableau d'amortissement ?**

## Obligatoire ou non

`mandatory: conditional`. Aucune disposition luxembourgeoise n'impose cette couverture ; elle est
exigée en pratique par le prêteur comme condition d'octroi du crédit. C'est la même obligation de
fait sans obligation de droit qu'en France — mais **sans l'édifice législatif** que la France a
construit autour d'elle (Lagarde, Hamon, Bourquin, Lemoine), qui organise la délégation et la
substitution d'assurance.

**C'est la différence à retenir pour un lecteur** : les droits de résiliation et de substitution
qu'un emprunteur français tient de la loi n'ont pas d'équivalent automatique ici, et se lisent dans
le contrat.

## État de la documentation

**Aucun produit n'est encore documenté dans cette branche.** Le recensement a identifié des contrats
de solde restant dû chez les porteurs de détail luxembourgeois, et la bibliothèque enumérée en
contient au moins un ; il n'est pas encore extrait.

Cette page existe malgré tout parce que la branche porte une part de l'argument structurel du pays,
et sa `status: stub` le dit. Ce qui suit — garanties typiques, exclusions fréquentes — sera écrit
**depuis les documents** et non depuis la connaissance générale du produit, conformément à la
règle 4.

## Cadre légal

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe II, branche **I** (vie,
  décès, mixtes et rentes non liées à des fonds d'investissement).
- Loi modifiée du 27 juillet 1997 sur le contrat d'assurance, pour le régime du contrat.
- Superviseur : [[CAA]].

## Related

- [[Prévoyance et décès]] · [[CAA]] · [[00 - Luxembourg MOC]]

## Sources

- `sources/lu/_country.yml`, branche `solde-restant-du`.
- `_meta/lu-market-census.md`.
