---
type: branch
domain: insurance
country: fr
branch: assurance-vie
branch_code: "20/22/24"
lang: fr
langs: [fr]
mandatory: false
regulator: "[[ACPR]]"
legal_refs: ["[[ACPR]]"]
tags: [insurance/fr/assurance-vie, branch]
aliases: [Assurance vie, Épargne, Multisupport, Unités de compte, Fonds en euros]
source: null
date: 2026-08-01
freshness: 2026-08-01
status: ready
generated: false
---

## Ce que c'est

L'assurance vie française est d'abord un **véhicule d'épargne**, et accessoirement une couverture de risque.
Le souscripteur verse des primes, l'assureur les investit, et le capital est versé au terme, en cas de rachat,
ou au décès aux bénéficiaires désignés. C'est le premier placement financier des ménages français.

Le nom prête à confusion pour un lecteur venu d'un autre marché : « assurance vie » ne désigne pas ici une
assurance décès temporaire — celle-là relève de la [[Prévoyance]] ou de l'[[Obsèques]] — mais un contrat de
capitalisation assorti d'un dénouement en cas de décès.

## Deux supports, deux régimes de risque

- Le **fonds en euros** : le capital est garanti par l'assureur, net de frais, avec un effet de cliquet sur
  les intérêts acquis. Le risque de placement est porté par l'assureur.
- Les **unités de compte** : le contrat est libellé en parts d'OPCVM, de SCPI ou d'autres actifs. L'assureur
  garantit **le nombre d'unités, jamais leur valeur**. Le risque de placement est porté par le souscripteur.

Cette formule, « l'assureur garantit le nombre d'unités de compte et non leur valeur, laquelle est sujette à
des fluctuations », se retrouve à l'identique dans presque tous les contrats du corpus. C'est la phrase qui
déplace le risque, et elle est courte.

## Le document, et ce qu'il n'est pas

Un contrat d'assurance vie ne se lit pas dans des conditions générales mais dans une **notice d'information**,
accompagnée d'un **document d'informations clés** (DIC) au format PRIIPs. Deux pièges observés dans ce corpus :

- La **liste des supports** est un document séparé. Sur une notice examinée, elle est annoncée au sommaire et
  référencée une trentaine de fois, mais **physiquement absente du PDF** : l'univers d'investissement et les
  frais par support y sont donc inconnaissables.
- Un DIC **par support** n'est pas un produit. Ingérer les fiches de chaque fonds ferait apparaître un contrat
  unique comme des dizaines de produits distincts ; ce wiki les écarte explicitement (64 fiches sur deux
  assureurs, plus 54 sur un troisième).

## Fiscalité, en deux temps

**En cas de rachat**, seule la part d'intérêts est imposée. Au-delà de **huit ans** de détention s'ouvrent un
abattement annuel (4 600 € pour une personne seule, 9 200 € pour un couple) et un taux réduit sur les produits
correspondant aux primes n'excédant pas 150 000 €. Avant huit ans, le prélèvement forfaitaire unique
s'applique. Les prélèvements sociaux s'ajoutent dans tous les cas.

**Au décès**, le capital échappe en principe à la succession : le Code des assurances (art. L. 132-12) dispose
que le capital stipulé payable à un bénéficiaire déterminé ne fait pas partie de la succession de l'assuré.
La fiscalité dépend alors de l'âge auquel les primes ont été versées — avant ou après le **70e anniversaire** —
selon deux régimes distincts du Code général des impôts (art. 990 I et 757 B), avec des abattements de nature
différente : par bénéficiaire dans un cas, global dans l'autre.

Les taux et seuils évoluent. Les pages produit de ce wiki citent ce que **le document imprime**, à sa date
d'édition ; un contrat du corpus imprime « 17,20 % au 1er janvier 2023 » à côté d'une mention « au 1er octobre
2025 », contradiction enregistrée telle quelle et non arbitrée.

## À surveiller

- Les **frais**, qui se superposent : frais sur versement, frais de gestion annuels du contrat, frais de
  gestion propres à chaque unité de compte, frais d'arbitrage. Le DIC les agrège ; la notice les détaille.
- Le **délai de paiement du rachat**. Un contrat du corpus l'énonce **trois fois différemment** dans le même
  document (30 jours ouvrés, 30 jours, 2 mois). Les trois lectures sont conservées.
- La **clause bénéficiaire**, qui décide de tout au décès, et dont la rédaction type ne convient pas à toutes
  les situations familiales.
- Les **garanties plancher**, qui assurent au décès un capital au moins égal aux versements. Une notice du
  corpus en mentionne deux (indexée, majorée) sans jamais les définir.
- Les **contrats en déshérence** : la loi Eckert (2014) impose aux assureurs de rechercher les bénéficiaires
  et de publier le nombre de contrats non réglés.

## Cadre légal

- Code des assurances, livre Ier titre III (assurances de personnes) ; art. L. 132-12 et L. 132-13 pour le
  sort successoral ; art. L. 132-21 et suivants pour la valeur de rachat.
- Règlement (UE) n° 1286/2014 (PRIIPs) pour le document d'informations clés.
- Loi n° 2014-617 du 13 juin 2014 (Eckert) sur les contrats non réclamés.
- Loi n° 2019-486 du 22 mai 2019 (PACTE) : transférabilité, information annuelle renforcée, obligation de
  référencer des unités de compte solidaires, vertes ou socialement responsables.
- Superviseur : [[ACPR]].

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[ACPR]] · [[Retraite supplémentaire]] · [[Prévoyance]] · [[Obsèques]]

## Sources

- Code des assurances, articles L. 132-12, L. 132-13, L. 132-21 et suivants.
- Code général des impôts, articles 990 I et 757 B.
- Règlement (UE) n° 1286/2014 du 26 novembre 2014 sur les documents d'informations clés relatifs aux produits
  d'investissement packagés de détail et fondés sur l'assurance.
