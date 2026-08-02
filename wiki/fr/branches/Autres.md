---
type: branch
domain: insurance
country: fr
branch: autres
branch_code: null
lang: fr
langs: [fr]
mandatory: false
regulator: "[[ACPR]]"
legal_refs: ["[[ACPR]]"]
tags: [insurance/fr/autres, branch]
aliases: [Autres, Divers]
source: null
date: 2026-08-01
freshness: 2026-08-01
status: ready
generated: false
---

## Ce que c'est

**`autres` n'est pas un segment de marché. C'est le repli de la taxonomie**, déclaré comme tel dans
`sources/fr/_country.yml` sous la clé `fallback_branch`.

Un document y atterrit quand aucune des vingt-six autres branches ne lui convient. La page existe pour que
cette catégorie soit lisible plutôt que muette : sans elle, un lecteur verrait des produits classés « Autres »
sans savoir si c'est une famille cohérente ou une réserve.

## Ce qu'on y trouve dans ce corpus

Trois cas de figure, tous rencontrés :

1. **Le document n'est pas un contrat d'assurance.** Un barème d'honoraires, une convention de service, une
   fiche de vente à distance, des conditions générales d'achat portant par erreur un nom de fichier
   contractuel. Ces documents restent recensés parce qu'ils sont publiés dans une bibliothèque contractuelle
   et qu'un lecteur les y trouvera ; leurs sections garanties et exclusions sont vides, ce qui est la lecture
   exacte et non une extraction incomplète.
2. **Le produit couvre un risque qui n'a pas de branche propre ici.** La taxonomie est celle du marché
   français vu du souscripteur, pas la nomenclature prudentielle de l'art. R. 321-1 ; certains produits de
   niche ne correspondent à aucune des deux.
3. **Le document couvre plusieurs branches sans dominante.** Un contrat multi-risques dont aucune garantie ne
   commande les autres.

## Ce que sa taille signifie

Le nombre de produits classés ici est un **indicateur de qualité de la taxonomie**. S'il croît, c'est que la
segmentation manque une famille réelle — et la réponse correcte est alors de créer une branche, comme cela a
été fait pour [[Vélo]], née d'un contrat que le classement en [[EDPM et mobilités douces]] aurait mal décrit.

S'il reste résiduel, la taxonomie couvre le marché.

## Cadre légal

Aucun. Cette branche ne correspond à aucune catégorie d'agrément de l'art. R. 321-1 du Code des assurances, et
son `branch_code` est délibérément nul. Le superviseur des organismes concernés reste l'[[ACPR]].

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[ACPR]] · [[00 - Branches MOC]]

## Sources

- `sources/fr/_country.yml`, clé `fallback_branch`.
