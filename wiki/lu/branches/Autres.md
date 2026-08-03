---
type: branch
domain: insurance
country: lu
branch: autres
branch_code: null
lang: fr
langs: [fr, de, en]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/autres, branch]
aliases: [Autres, Divers, Sonstige]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Ce que c'est

**`autres` n'est pas un segment de marché. C'est le repli de la taxonomie luxembourgeoise**, déclaré comme
tel dans `sources/lu/_country.yml` sous la clé `fallback_branch`.

Un document y atterrit quand aucune des dix-huit autres branches déclarées ne lui convient. La page existe pour
que cette catégorie soit lisible plutôt que muette : sans elle, un lecteur verrait des produits classés
« Autres » sans savoir si c'est une famille cohérente ou une réserve.

Son `branch_code` est délibérément nul. Elle ne correspond à aucune rubrique de l'annexe I ni de l'annexe II
de la LSA, et un assureur ne peut pas être agréé « pour la branche autres ».

## Ce qu'on y trouve dans ce corpus

À ce jour, les documents classés ici forment un cas de figure unique et cohérent : **des produits d'affinité,
distribués par un tiers qui n'est pas assureur.** Le chemin de publication le dit avant le contenu — ils
sont tous servis depuis le répertoire `ipid-partenaires/` de la bibliothèque lalux.

- **Assurances liées aux cartes de crédit SPUERKEESS** (gammes VISA INFINITE, VISA BUSINESS, VISA PREMIER,
  en français, allemand et anglais). Chaque document énumère douze garanties « hors assistance » et deux
  garanties « assistance », sans en décrire le contenu ni les montants : accident de voyage, solde restant
  dû, annulation et interruption de voyage, retard d'avion, départ manqué, protection des achats, livraison
  de biens achetés sur Internet, protection bagages, matériel de sport, exonération de la franchise du
  véhicule de location, extension de garantie, vol des espèces. La couverture est subordonnée au fait
  qu'« au moins 30 % des coûts du voyage » aient été réglés avec la carte, et les assurés sont le titulaire,
  son conjoint ou partenaire et ses enfants de moins de 25 ans du même ménage.
- **Assurance Tous Risques LINEHEART**, qui couvre « les iPhone ou autres appareils Apple (et accessoires) »
  contre la casse accidentelle, le vol et l'oxydation accidentelle. Le contrat « doit être contracté au
  moment de l'achat du produit assuré et figurer sur la même facture », pour une durée limitée à trois ans à
  compter de l'achat.

**Pourquoi ils tombent ici, et pas ailleurs.** Un contrat de carte de crédit traverse quatre ou cinq branches
consumer à la fois — voyage, solde restant dû, pertes pécuniaires, assistance, dommages aux biens — sans
qu'aucune ne commande les autres ; le classer dans l'une d'elles reviendrait à choisir arbitrairement une
garantie parmi douze. Un contrat d'appareil électronique vendu en caisse ne correspond à aucune des branches
déclarées. Dans les deux cas, le rattachement le plus honnête est le repli.

## Ce que sa taille signifie

Le nombre de produits classés ici est un **indicateur de qualité de la taxonomie**, pas la mesure d'un
segment. S'il croît, c'est que la segmentation manque une famille réelle, et la réponse correcte est de
créer une branche — pas d'agrandir le repli.

Deux précautions de lecture s'imposent pour le corpus luxembourgeois :

- **Le compte est provisoire et repose sur un seul assureur.** Toute la collecte luxembourgeoise vient d'une
  bibliothèque, celle de lalux. Trois autres porteurs de détail existent et n'ont pas été énumérés.
- **Un produit peut être ici pour une mauvaise raison.** Le corpus en fournit déjà un exemple, mais dans une
  autre branche : deux documents classés en [[Multirisque professionnelle]] sont en réalité un forfait pour
  les 15-27 ans et une assurance tous risques d'objets personnels. Un mauvais classement se lit aussi bien
  hors du repli que dedans.

## Le cas de l'Assurance Vélo : pourquoi il n'y a pas de branche `velo` au Luxembourg

Ce cas mérite d'être écrit, parce qu'il illustre exactement ce que le repli sert à garder visible et qu'il
corrige un motif erroné consigné dans le recensement de marché.

**Le produit existe.** lalux commercialise une *Assurance Vélo LALUX*, dont la brochure trilingue
(FR/EN/DE dans un seul fichier) est en ligne et a répondu 200 le 2026-08-03. Elle annonce, pour une prime
mensuelle de 10 €, un vélo « classique ou électrique » assuré jusqu'à 5 000 € : vol et tentative de vol,
dégâts matériels en cas d'accident ou de vandalisme (vélo, casque et équipements de protection), dommages
corporels du conducteur et des passagers (frais médicaux jusqu'à 2 500 €, décès et invalidité jusqu'à
50 000 €) et responsabilité civile familiale. La brochure oriente au-delà de 5 000 € vers le « pack Cyclisme
et Mobilité Douce » de l'assurance [[Assurance habitation]].

**La branche n'a pourtant pas été créée, et le motif importe.** En France, `velo` a été ajoutée à partir
d'une **divergence de définition** : le contrat vélo du corpus français définissait le cycle assuré comme
étant « à assistance électrique, moteur limité à 250 W, coupure à 25 km/h » ou sans assistance au pédalage,
et excluait les véhicules terrestres à moteur — or un EDPM *est* un véhicule terrestre à moteur au sens
français et porte à ce titre une obligation d'assurance de responsabilité civile. Fusionner les deux aurait
réuni un produit sans couverture obligatoire et un produit qui en porte une. **C'est la divergence de
définition qui a justifié la branche, pas l'existence d'un produit.**

Rien de tel ici, sur trois points mesurés :

1. **La brochure luxembourgeoise ne définit pas le cycle assuré.** Elle dit « classique ou électrique » et
   s'arrête là : ni puissance, ni coupure d'assistance, ni exclusion des véhicules terrestres à moteur.
   Aucune divergence de définition ne peut donc être constatée dans ce document.
2. **Le Luxembourg n'a pas d'obligation d'assurance sur les engins de mobilité douce standard**, et il est
   allé dans le sens inverse de la France : la loi du 29 mars 2024 a redéfini le véhicule soumis à assurance
   obligatoire à l'art. 1er a) de la loi du 16 avril 2003, et une trottinette électrique bridée à 25 km/h et
   pesant moins de 25 kg tombe **hors** de l'obligation. C'est aussi la raison pour laquelle la taxonomie
   luxembourgeoise ne déclare pas de branche `edpm`.
3. **Le risque est déjà servi par une autre branche.** L'IPID habitation du corpus porte une extension
   optionnelle « bris et vol des engins de mobilité douce : vélos, vélos à assistance électrique,
   trottinettes etc. allant jusqu'à maximum 25 km/h », et un IPID *easyPROTECT Comprehensive* range les
   « cycles » parmi les catégories d'objets assurables. Le vélo n'est pas un angle mort de la taxonomie.

**Un seul produit ne justifie pas une branche.** Tant que rien n'oppose la définition du cycle assuré à celle
d'un engin soumis à obligation, la question reste ouverte plutôt que tranchée, et `autres` est l'endroit
prévu pour la garder visible.

Réserve à porter au compte de cet exemple : **la brochure Assurance Vélo n'est pas dans le corpus.** Elle a
été écartée à l'ingestion parce que son type de document, `brochure`, n'est pas une valeur du schéma. Ce
n'est pas un document contractuel, et rien de ce qui précède ne doit être lu comme une description des
conditions du contrat — seulement de ce que l'assureur en publie.

## Ce qui n'est pas dans cette branche, et pourquoi

Le manifeste luxembourgeois écarte explicitement plusieurs branches qui existent ailleurs dans ce wiki. Elles
ne sont pas repliées ici : elles sont **déclarées absentes**, ce qui n'est pas la même chose qu'un repli.

- **`scolaire`** : le *Code de la sécurité sociale*, Livre II, **art. 91, 1°** place les écoliers, élèves et
  étudiants dans un régime public spécial d'assurance accident. Il n'y a pas de produit privé à documenter.
- **`accidents-travail`** : le *Code de la sécurité sociale*, Livre II, **art. 85** en fait une assurance
  publique obligatoire administrée par l'AAA, qui n'est pas un assureur supervisé par le [[CAA]] et ne
  figure pas au registre.
- **`edpm`**, pour la raison exposée plus haut.
- **`navigation`, `transport`, `agricole`, `cyber`, `obseques`** : les branches 6, 7 et 12 sont très
  peuplées au registre, mais par des clubs P&I et des porteurs maritimes commerciaux, pas par des produits de
  détail ; les autres n'ont été observées dans aucune gamme luxembourgeoise de détail.

## Cadre légal

**Aucun.** Cette branche ne correspond à aucune rubrique de l'annexe I ni de l'annexe II de la loi modifiée
du 7 décembre 2015 sur le secteur des assurances, et son `branch_code` est délibérément nul. Les assureurs
dont relèvent les produits classés ici sont, eux, agréés pour des branches précises et supervisés par le
[[CAA]] comme les autres.

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[CAA]] · [[00 - Branches MOC]] · [[Assurance habitation]] · [[Voyage et assistance]] ·
  [[Multirisque professionnelle]]

## Sources

- `sources/lu/_country.yml`, clé `fallback_branch` et bloc de commentaires « what this file deliberately
  does not contain ».
- `_meta/lu-market-census.md`, section « Corrections (2026-08-02) », point 2 sur le motif erroné de l'absence
  de branche `velo`.
- `_meta/discovery/lu/lalux.md` (bibliothèque énumérée le 2026-08-01 ; `Assurance_velo_-FR-DE-EN.pdf` écarté
  à l'ingestion, type de document hors schéma).
- Brochure *Assurance Vélo LALUX*,
  `https://www.lalux.lu/fileadmin/mediatheque/documents/Brochures/Assurance_velo_-FR-DE-EN.pdf`, consultée le
  2026-08-03.
- Code de la sécurité sociale, Livre II, art. 85 et art. 91, 1° — citations reprises du recensement de
  marché et des commentaires du manifeste, non revérifiées contre le texte dans cette passe.
- Loi modifiée du 16 avril 2003, art. 1er, point a), tel que modifié par la loi du 29 mars 2024 — vérifié
  dans le texte coordonné publié par le [[CAA]] (`Loi_RCVTA_2003-04-16_coord_2024-04-06.pdf`, consulté le
  2026-08-03).
