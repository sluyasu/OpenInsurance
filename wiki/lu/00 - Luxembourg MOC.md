---
type: moc
domain: insurance
country: lu
lang: fr
tags: [insurance/lu, moc]
aliases: [Luxembourg MOC, Luxembourg]
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Luxembourg — carte du marché

Un superviseur, le [[CAA]] (Commissariat aux Assurances), une loi d'agrément — la loi modifiée du
7 décembre 2015 sur le secteur des assurances, dite « LSA » — et une loi de contrat, celle du
27 juillet 1997. C'est le schéma institutionnel le plus simple des quatre pays couverts ici.

| Pays | Structure |
|---|---|
| Belgique | un superviseur, un régime |
| Suisse | **deux** superviseurs répartis par activité (FINMA / OFSP) |
| France | un superviseur, **trois** codes juridiques |
| Luxembourg | un superviseur, une loi — et un marché qui n'est pas domestique |

## Le trait distinctif n'est pas la supervision, c'est la destination

Mesuré sur les annexes du rapport annuel du CAA, exercice 2025 : **5,0 %** des primes vie écrites
depuis le Luxembourg y sont vendues, et **8,7 %** des primes non-vie. La France seule représente plus
de la moitié de la production vie. S'y ajoutent **207 entreprises de réassurance** agréées, presque
toutes des captives de groupes étrangers qui n'écrivent aucun contrat de particulier.

Soixante-trois assureurs directs luxembourgeois existent ; **moins de dix vendent un produit à un
résident**. Le pays compte 691 000 habitants et **225 840 travailleurs frontaliers**, dont les
contrats auto et habitation relèvent de leur pays de résidence.

**Conséquence assumée pour ce wiki : le corpus luxembourgeois est petit, et cette petitesse est un
fait de marché, pas un défaut de collecte.** Le détail et les sources figurent dans
`_meta/lu-market-census.md`.

## Distributeurs et porteurs de risque

Comme partout, le document nomme lui-même son assureur — sauf que dans ce corpus, souvent, il ne le
nomme pas assez.

Mesuré sur les documents extraits : **onze sur trente et un nomment une entité avec sa forme
juridique ou son numéro RCS**. Les autres impriment la marque — « LALUX Assurances »,
« la Compagnie », « die Versicherungsgesellschaft » — sans permettre de choisir entre les deux
entités agréées derrière elle.

Et l'identification peut dépendre de **quelle page on regarde** : des conditions générales impriment
`R.C.S. LUXEMBOURG B31035` dans leur en-tête courant sur quatre pages seulement, un `R.C.S.` tronqué
à la page 18, et rien du tout à la page 8.

La règle de ce projet — lire le porteur dans le document, jamais dans la marque — donne donc ici
`carrier: null` plus souvent qu'ailleurs. **C'est la lecture exacte, pas une extraction incomplète.**

## Branches

La segmentation est celle du marché luxembourgeois vu du souscripteur. Chaque branche porte le
`code` des annexes de la LSA, qui transposent l'annexe Solvabilité II et sur lesquelles le CAA
délivre les agréments — chiffres arabes pour le non-vie (annexe I, 1 à 18), chiffres romains pour la
vie (annexe II, I à VII), de sorte qu'un code ne collisionne jamais entre les deux.

Trois branches sont proprement luxembourgeoises et n'ont pas d'équivalent direct dans les taxonomies
déjà écrites :

- **[[Solde restant dû]]** — le nom que les porteurs de détail impriment réellement. L'`emprunteur`
  français importé ici ne correspondrait à aucun titre de document.
- **[[Responsabilité civile familiale]]** — que le superviseur mesure séparément.
- **[[Assurances constructions]]** — décennale **et** biennale (Code civil art. 1792 et art. 2270),
  obligatoires pour les seuls architectes et ingénieurs-conseils, et **sans dommages-ouvrage**. Une
  branche là où la France en a deux.

Quatre absences sont délibérées, chacune vérifiée dans le texte :

- **Pas d'`edpm`.** La loi du 29 mars 2024 définit le véhicule au-delà de 25 km/h, ce qui met les
  trottinettes électriques **hors** de l'obligation d'assurance — exactement l'inverse du décret
  français de 2019.
- **Pas de `scolaire` ni d'`accidents du travail`** : ce sont des régimes publics obligatoires
  (CSS Livre II, art. 85 et 91).
- **`habitation` en `mandatory: false`** : la loi du 21 septembre 2006 sur le bail à usage
  d'habitation ne comporte aucune obligation d'assurance du locataire.

## Assureurs

<!-- BEGIN GENERATED: insurers -->
- [lalux](insurers/lalux.md) (31 documents)
<!-- END GENERATED -->

**Foyer**, premier groupe de détail du pays, est en découverte seule. Son `robots.txt` ferme les
chemins de documents dans les trois langues puis en rouvre exactement deux — qui ne sont pas des
documents contractuels. Mais le fait qui rend ce blocage secondaire est ailleurs : **Foyer ne publie
aucune conditions générales**, zéro ligne sur huit cents. Détail dans `_meta/discovery/lu/foyer.md`.

## Portée et limites

Comme en France, le document public standard est celui qu'impose la directive sur la distribution.
**Sur les quatre-vingt-dix documents d'un assureur de détail, quatre seulement sont de vraies
conditions générales** — toutes en construction B2B. Le reste est constitué de documents
d'information, dont beaucoup renvoient à des conditions générales publiées nulle part.

Deux observations sur les documents eux-mêmes, énoncées comme des constats et non comme un jugement
— la règle 1 interdit de noter un assureur, compter ce qu'on lit dans ses documents ne s'y oppose
pas :

- **La majorité des documents extraits porte au moins un intitulé de rubrique faux ou contredit par
  son contenu**, et plusieurs manquent entièrement une rubrique du format imposé. Deux portent un
  texte de gabarit destiné au rédacteur et jamais remplacé.
- Ces défauts sont **conservés et jamais réparés** : une citation doit être une portion exacte du
  document.

Le comptage, ses cas et ses limites sont dans `_meta/discovery/lu/lalux.md`.

## Related

- [[CAA]] · [[00 - Branches MOC]] · [[00 - France MOC]]
