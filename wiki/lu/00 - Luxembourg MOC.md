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

Le registre du [[CAA]] borne cette liste par le haut sans la donner. Côté non-vie, la branche 10
(RC véhicules terrestres) est le seul filtre utile : **douze des trente-cinq** la détiennent, mais
elle couvre aussi les flottes d'entreprise, donc douze est un plafond et non un décompte. Côté vie,
le registre ne sépare rien : **les vingt-huit assureurs vie détiennent tous les branches I et III**.
Un agrément dit ce qu'une entreprise a le droit d'écrire, jamais ce qu'elle écrit — l'appartenance
au marché de détail se décide donc à la découverte, en regardant si l'entreprise publie une
bibliothèque de contrats destinés à un particulier.

**Conséquence assumée pour ce wiki : le corpus luxembourgeois est petit, et cette petitesse est un
fait de marché, pas un défaut de collecte.** Le détail et les sources figurent dans
`_meta/lu-market-census.md`.

## Distributeurs et porteurs de risque

Comme partout, le document nomme lui-même son assureur — sauf que dans ce corpus, souvent, il ne le
nomme pas assez.

Mesuré sur les quatre-vingt-dix documents d'un assureur de détail, en cherchant dans le texte des
PDF eux-mêmes : **quatre nomment le porteur de risque** avec sa dénomination complète
(« LA LUXEMBOURGEOISE Société Anonyme d'Assurances ») ou son numéro R.C.S. Ce sont les quatre mêmes
documents dans les deux cas — et ce sont les quatre seules vraies conditions générales du lot.
Quatre sur quatre-vingt-dix, soit **4 %**.

Les autres impriment la marque — « LALUX Assurances », « la Compagnie »,
« die Versicherungsgesellschaft » — sans permettre de choisir entre les deux entités agréées
derrière elle (LA LUXEMBOURGEOISE S.A. en non-vie, LA LUXEMBOURGEOISE-VIE S.A. en vie).

**Et douze documents nomment bien une entité avec sa forme juridique — mais ce n'est pas
l'assureur.** C'est le gestionnaire de sinistres : « Willis Towers Watson Luxembourg S.A. réceptionne
les déclarations de sinistre ». Aucun de ces douze ne nomme le porteur ailleurs. La seule raison
sociale complète imprimée dans le document appartient donc à quelqu'un qui ne porte pas le risque,
et une extraction qui cherche « un nom suivi d'une forme juridique » y attrape systématiquement le
mauvais.

Et l'identification peut dépendre de **quelle page on regarde** : des conditions générales impriment
`R.C.S. LUXEMBOURG B31035` dans leur en-tête courant sur quatre pages seulement, un `R.C.S.` tronqué
à la page 18, et rien du tout à la page 8.

La règle de ce projet — lire le porteur dans le document, jamais dans la marque — donne donc ici
`carrier: null` plus souvent qu'ailleurs. **C'est la lecture exacte, pas une extraction incomplète.**

### Mais ce n'est pas une fatalité du marché : c'est un choix d'éditeur

Les deux porteurs entrés ensuite dans le corpus le démontrent. Mesuré de la même façon, sur le texte
des PDF :

| Porteur | Documents | Nomment une entité agréée |
|---|---|---|
| lalux | 90 | **4** (4 %) |
| Baloise | 34 | **33** (97 %) |
| DKV | 36 | **36** (100 %) |

Baloise imprime « Compagnie : » — « Gesellschaft : » en allemand — **en tête de chaque page**, sur
des documents du même format IPID, chez un porteur soumis au même superviseur et à la même loi. DKV
va plus loin : ses trente-six documents nomment tous `DKV Luxembourg S.A.`, et **aucun des trois
éditeurs n'a ici de mauvais candidat** — ni gestionnaire de sinistres, ni assisteur, ni courtier
n'est nommé, alors que douze documents lalux nomment « Willis Towers Watson Luxembourg S.A. » sans
jamais nommer l'assureur.

**Le constat « un IPID ne nomme pas son assureur » était donc une observation sur un éditeur, pas
sur le format.** Le format ne l'interdit pas ; un éditeur le fait, deux autres le font
systématiquement. Et l'écart n'est pas une question de taille ou d'ancienneté : c'est un choix
éditorial, mesurable document par document.

Mieux : la spécialisation légale se lit dans les documents. Baloise a deux entités agréées, et **un
seul de ses trente-quatre documents nomme l'entité vie** — celui du [[Solde restant dû]], seule
branche vie du lot, qui imprime « Compagnie : Baloise Vie Luxembourg S.A. ». Les trente-trois autres
nomment l'entité non-vie. Le principe de spécialisation luxembourgeois, qui interdit à une même
société d'écrire vie et non-vie, n'est pas seulement au registre : il est imprimé, document par
document.

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
- [Baloise Luxembourg](insurers/Baloise%20Luxembourg.md) (34 documents)
- [DKV Luxembourg](insurers/DKV%20Luxembourg.md) (36 documents)
- [Foyer Global Health](insurers/Foyer%20Global%20Health.md) (34 documents)
- [lalux](insurers/lalux.md) (90 documents)
<!-- END GENERATED -->

**Foyer**, premier groupe de détail du pays, est en découverte seule. Son `robots.txt` ferme les
chemins de documents dans les trois langues puis en rouvre exactement deux — qui ne sont pas des
documents contractuels.

**Correction (2026-08-04) : ses conditions générales existent, et l'affirmation « Foyer ne publie
aucune conditions générales » était fausse.** Une première passe avait relevé zéro occurrence du mot
sur huit cents documents et conclu à une absence. Une seconde a lu la page
`/fr/conditions-generales` elle-même : **ce n'est pas une page de listing, c'est un formulaire**.

> « Pour consulter vos conditions générales, merci de renseigner le **Numéro Client** et le
> **Numéro Contrat** […] Ces informations sont imprimées sur vos Conditions Particulières reçues par
> courrier postal. »

Et le gabarit de résultat que la page porte déjà en HTML annonce « Conditions Générales trouvées.
Tous les documents […] sont au format PDF ». Les contrats sont donc publiés **au souscripteur
identifié, contrat par contrat** — ce qui est une politique de publication, pas une absence.

**Aucune énumération n'a été tentée sur ce formulaire et aucune ne doit l'être** : il demande des
identifiants de client réels. La limite est de méthode autant que de droit — ce dépôt n'énumère que
ce qui est publié à tous.

Détail dans `_meta/discovery/lu/foyer.md` et `_meta/discovery/lu/foyer-vie.md`.

**AXA Luxembourg** est en découverte seule aussi, et c'est le cas le plus frustrant du corpus.
**631 documents inventoriés, 0 récupérable** : `robots.txt` d'`axa.lu` porte `Disallow: /*.pdf`,
ancré à la racine, et aucune des 631 URL n'échappe au motif. Aucun PDF n'a été demandé.

Ce qui rend ce blocage coûteux, c'est **ce qu'il y a derrière**. Au moins **302 de ces documents sont
de vraies conditions d'assurance** — le contrat lui-même, pas le résumé imposé par la directive. À
comparer aux quatre sur quatre-vingt-dix de lalux et au zéro en libre accès de Foyer :

| Porteur | Documents publiés | Vraies conditions générales |
|---|---|---|
| Foyer | ~800 | **0 en libre accès** — servies au souscripteur identifié |
| lalux | 90 | **4** |
| AXA Luxembourg | 631 | **≥ 302**, toutes inaccessibles |

**AXA est le premier porteur luxembourgeois observé à publier le contrat plutôt que sa fiche.** Le
constat corrige au passage l'idée, formée sur les deux premiers porteurs, que le marché
luxembourgeois ne publierait pas ses conditions générales : au moins un porteur le fait, largement,
et c'est `robots.txt` qui l'écarte de ce dépôt, pas l'absence de publication.

Deux hôtes AXA luxembourgeois divergent d'ailleurs exactement sur ce point : `axa-wealtheurope.lu`
ne porte aucune règle `.pdf` — mais c'est l'entité qui ne vend pas au détail, et ses 85 documents ne
comptent **aucune** conditions générales. Détail dans `_meta/discovery/lu/axa.md`.

## Portée et limites

Comme en France, le document public standard est celui qu'impose la directive sur la distribution :
la fiche d'information, pas le contrat. Le corpus luxembourgeois le montre crûment, et l'écart entre
éditeurs y est plus grand que l'écart au format.

| Porteur | Documents publiés | Vraies conditions générales |
|---|---|---|
| Foyer | ~800 | **0 en libre accès** — servies au souscripteur identifié |
| Baloise | 268 | **0** |
| lalux | 90 | **4** (toutes en construction B2B) |
| **DKV** | 60 | **9** |
| AXA Luxembourg | 631 | **≥ 302**, toutes fermées par `robots.txt` |

**Sur les 151 documents extraits à ce jour, 140 sont des IPID et onze seulement sont de vraies
conditions générales.** Beaucoup des IPID renvoient d'ailleurs à des conditions générales publiées
nulle part — c'est une observation sur la pratique de publication, pas un manquement : publier
l'IPID est une obligation, publier les conditions générales n'en est pas une.

DKV change la donne à lui seul : neuf contrats, en santé et en voyage, là où le corpus n'en comptait
que quatre. Et le cas AXA reste le plus frustrant du pays — trois cents contrats publiés, tous hors
d'atteinte.

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
