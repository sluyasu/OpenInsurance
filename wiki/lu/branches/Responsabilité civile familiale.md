---
type: branch
domain: insurance
country: lu
branch: rc-familiale
branch_code: "13"
lang: fr
langs: [fr, de, en]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/rc-familiale, branch]
aliases: [RC familiale, Responsabilité civile familiale, Privathaftpflicht, RC vie privée]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: stub
generated: false
---

## Ce que c'est

La responsabilité civile familiale couvre les dommages que l'assuré, les personnes de son ménage et
souvent ses animaux causent à des tiers dans la vie privée. Elle indemnise **le tiers lésé**, pas
l'assuré : c'est ce qui la distingue des couvertures de dommages, qui indemnisent le patrimoine de
l'assuré.

## Pourquoi c'est une branche à part ici

Dans beaucoup de marchés, cette garantie n'existe que comme un chapitre du contrat habitation, et une
taxonomie la range donc sous ce contrat. Deux raisons de ne pas le faire au Luxembourg :

- **Le superviseur la mesure séparément.** Le CAA lui consacre sa propre ligne dans les statistiques
  de marché, ce qui en fait un segment reconnu et non une garantie annexe.
- **Elle se vend séparément.** Le corpus contient un produit dont le socle est une RC privée avec
  extension logement étudiant et protection juridique, sans contrat habitation associé — un produit
  pour étudiants et apprentis de 15 à 27 ans qui **exclut explicitement les activités
  professionnelles**. Ce document avait d'ailleurs été étiqueté `multirisque-professionnelle` par la
  découverte ; il a été reclassé ici sur signalement d'un extracteur.

Ce cas est la meilleure justification de la branche : un produit dont la RC privée **est** l'objet,
et non un accessoire.

## Ce qu'elle n'est pas

- **Pas la [[RC professionnelle]]** : celle-ci répond des dommages causés dans l'exercice d'un métier,
  et plusieurs professions luxembourgeoises la portent à titre obligatoire. La RC familiale l'exclut
  en général expressément.
- **Pas une couverture des dommages subis par l'assuré.** Un assuré blessé chez lui ne relève pas de
  cette branche mais des [[Assurance accidents]].
- **Pas la RC automobile**, qui est obligatoire et relève de l'[[Assurance auto]] (LSA annexe I,
  branche 10).

## État de la documentation

**Un seul produit est documenté dans cette branche à ce jour**, et il y est arrivé par correction.
Cette page porte donc `status: stub` : les garanties typiques, les exclusions fréquentes et les
plafonds usuels seront écrits **depuis les documents** à mesure qu'ils entrent, et non depuis une
connaissance générale du produit.

Ce qu'un lecteur peut déjà retenir, parce que c'est mesuré : dans ce corpus, la protection juridique
accompagne fréquemment la RC privée dans un même contrat **sans être portée par le même assureur** —
le registre montre `FOYER-ARAG` détenant la seule branche 17, et le corpus français a livré le même
schéma sur des dizaines de contrats. Lire qui porte quoi, garantie par garantie.

## Cadre légal

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe I, branche **13**
  (responsabilité civile générale).
- Loi modifiée du 27 juillet 1997 sur le contrat d'assurance, pour le régime du contrat.
- Aucune obligation légale d'assurance : `mandatory: false`.
- Superviseur : [[CAA]].

## Related

- [[RC professionnelle]] · [[Assurance habitation]] · [[Protection juridique]] · [[CAA]] · [[00 - Luxembourg MOC]]

## Sources

- `sources/lu/_country.yml`, branche `rc-familiale`.
- `_meta/lu-market-census.md`.
- `_meta/discovery/lu/foyer.md` pour la répartition d'agréments du groupe Foyer.
