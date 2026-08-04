---
type: branch
domain: insurance
country: lu
branch: moto
branch_code: "10/3"
lang: fr
langs: [fr]
mandatory: true
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/moto, branch]
aliases: [Moto, Deux-roues, Motocyclette, Scooter, Cyclomoteur, Quad, Motorrad, Zweirad, Motorbike]
source: null
date: 2026-08-04
freshness: 2026-08-04
status: stub
generated: false
---

## Ce que c'est

Les deux-roues motorisés — motocyclettes, scooters, cyclomoteurs — et, par extension de vente, les quads,
relèvent au Luxembourg de **la même loi et des mêmes branches prudentielles que l'automobile** : la
responsabilité civile en **branche 10** de l'annexe I de la LSA (« R.C. véhicules terrestres automoteurs »),
les dommages au véhicule en **branche 3** (« Corps de véhicules terrestres (autres que ferroviaires) »).

Il n'existe **aucune loi luxembourgeoise propre au deux-roues** en matière d'assurance. Ce qui distingue
cette branche de l'[[Assurance auto]] n'est donc pas le droit : c'est l'engin, et la manière — ou l'absence
de manière — dont le marché le documente.

## L'obligation, et sur qui elle pèse

C'est le texte de l'[[Assurance auto]], mot pour mot, parce que c'est le même texte. Loi modifiée du 16 avril
2003 relative à l'assurance obligatoire de la responsabilité civile en matière de véhicules automoteurs,
**art. 2, point 1** : les véhicules ne sont admis à la circulation que si la responsabilité civile à laquelle
ils peuvent donner lieu est couverte par un contrat conforme à cette loi.

Le débiteur de l'obligation est, dans la rédaction issue de la **loi du 21 septembre 2023**, « soit le futur
titulaire du certificat d'immatriculation soit le titulaire du certificat d'immatriculation » — **et le
propriétaire pour un véhicule non immatriculé**. Cette seconde branche de la règle est celle qui compte ici :
elle est la seule qui puisse s'appliquer à un engin motorisé circulant sans certificat d'immatriculation.
Quels deux-roues luxembourgeois sont immatriculés et lesquels ne le sont pas n'a **pas été vérifié** dans
cette passe, et n'est donc pas affirmé.

Le défaut d'assurance est pénalement sanctionné dans les mêmes termes (**art. 28, point 1** : huit jours à
trois ans d'emprisonnement et 500 à 10 000 euros d'amende, ou l'une de ces peines seulement), et vise
également le conducteur.

## Le seuil qui décide si un engin est dans la branche ou en dehors

C'est la question opérante au Luxembourg, et elle se lit dans **l'art. 1er, lettre a)** de la loi de 2003 tel
que modifié par la **loi du 29 mars 2024** (transposition de la directive (UE) 2021/2118). Sont visés les
véhicules automoteurs actionnés exclusivement par une force mécanique sans être liés à une voie ferrée :

> avec, soit une vitesse maximale par construction supérieure à 25 km/h, soit un poids net maximal supérieur
> à 25 kg et une vitesse maximale par construction supérieure à 14 km/h.

**Le test a deux branches, et l'une porte sur le poids.** Un scooter bridé à 45 km/h est dedans par la
première. Un engin de plus de 25 kg roulant à plus de 14 km/h est dedans par la seconde, même s'il reste
sous 25 km/h. Une trottinette électrique standard — 25 km/h, moins de 25 kg — est **dehors**, et c'est la
raison pour laquelle la taxonomie luxembourgeoise de ce dépôt ne comporte pas de branche `edpm` là où la
France en a une. Deux pays voisins, la même directive en arrière-plan, deux résultats opposés pour le même
engin.

À ne pas confondre avec le seuil de 25 km/h qui apparaît dans un contrat habitation du corpus pour délimiter
une extension « mobilité douce » : celui-là ne porte que sur la vitesse, c'est un critère d'éligibilité
contractuelle, et il ne recouvre pas le test légal. Voir [[Assurance habitation]].

## Une branche que le marché luxembourgeois ne vend presque pas séparément

C'est le fait central de cette page, et il repose sur trois mesures indépendantes, faites sur les
bibliothèques publiées des porteurs de détail.

- **Foyer** — zéro occurrence de *moto*, *scooter* ou *zweirad* sur les 800 lignes de sa bibliothèque
  énumérée, et les **douze IPID de la gamme Mobilité sont tous des IPID Auto**.
- **Baloise** — les pages produit `moto-scooter.html` (FR), `moto.html` (DE) et `motorbike.html` (EN)
  existent, et **elles publient toutes les trois l'IPID auto *Drive***. Aucun document deux-roues distinct
  n'est servi. Le produit est présenté séparément et documenté par le document d'un autre produit.
- **AXA** — c'est la seule exception observée, et elle est réelle : une gamme **OptiDrive Moto** avec sa
  propre page produit (`/fr/particuliers/assurance-moto`, distincte de `/fr/particuliers/assurance-auto`),
  ses propres conditions d'assurance référencées **W04.2021** et ses propres IPID en français et en anglais.
  **Aucun de ces documents n'a pu être récupéré** : le `robots.txt` d'`axa.lu` porte `Disallow: /*.pdf`, qui
  ferme les 631 documents du site. L'existence du produit est établie, son contenu est inconnu.

La conséquence pour la lecture de cette branche : **elle tient par l'obligation de l'art. 2 de la loi de
2003, et par un produit dont on sait qu'il existe et pas ce qu'il dit.** Elle ne tient pas par une pratique
commerciale de produit séparé — c'est une hypothèse qui a été portée par le manifeste pays, puis démentie
deux fois.

## Ce que le corpus contient — et ce qu'il n'y a pas

**Aucun document du corpus luxembourgeois n'est classé dans cette branche : zéro produit, zéro assureur.**
Ce n'est pas une omission de rédaction, c'est l'état mesuré du dépôt à la date de cette page.

Trois familles de documents rangées dans **d'autres** branches parlent pourtant du deux-roues, et c'est tout
ce qu'un lecteur peut en tirer aujourd'hui :

- **Le deux-roues professionnel est couvert à l'intérieur d'un contrat auto.** L'IPID *easyPROTECT-PRO -
  Auto*, déclinaison « Véhicules autres que voitures ou camping cars » (allemand : « Andere Fahrzeuge als PKW
  und Wohnmobile » ; anglais : « Vehicles other than cars and motorhomes »), énumère dans sa propre phrase de
  périmètre les véhicules visés : « taxis, voitures de location sans chauffeur, camionnettes, camions,
  tracteurs de semi-remorques, autobus, tracteurs, caravanes, **motocycles**, … ». Le document est classé
  `auto`, et son extraction consigne elle-même la tension : les motocycles qu'il couvre ne sont pas rattachés
  à la branche `moto`. L'usage décrit est professionnel ; le document ne permet pas de distinguer entreprises
  et indépendants.
- **Conduire un deux-roues fait sortir de l'assurance accidents privée, sauf convention contraire.** Les IPID
  *easyPROTECT-Accident* (fr), *easyPROTECT-Unfall* (de) et leur version anglaise portent, sous « Exclusions,
  sauf convention contraire », l'entrée « **Usage et conduite de motocycles légers, motocycles et
  quadricycles** ». Les mêmes documents prévoient une **réduction d'un tiers** de la prestation « en cas
  d'accident en tant que conducteur ou passager […] d'un motocycle : […] en cas d'absence de port de casque ».
  Détail dans [[Assurance accidents]].
- **La frontière avec la mobilité douce se lit dans un contrat habitation.** L'IPID *easyPROTECT Habitation*
  documente une extension optionnelle : « Bris et vol des engins de mobilité douce : vélos, vélos à
  assistance électrique, trottinettes etc. **allant jusqu'à maximum 25 km/h** » (sa version anglaise,
  *easyPROTECT-Home*, imprime « up to a maximum speed of 25 km/h »). Au-delà, l'engin n'est plus dans ce
  contrat, et le test de l'art. 1er a) reprend la main.

**Le motif à retenir : dans ce corpus, le deux-roues motorisé apparaît presque toujours comme une exclusion
ou comme un sous-cas d'un autre contrat, jamais comme un contrat à lui.**

## À surveiller

- **Le document d'un produit deux-roues n'est pas nécessairement un document deux-roues.** Trois pages
  produit d'un même assureur servent l'IPID d'un contrat auto. Lire le titre du PDF, pas celui de la page qui
  l'héberge.
- **Le casque et le motocycle jouent en réduction, pas en exclusion sèche**, dans l'assurance accidents du
  corpus : la prestation est réduite d'un tiers, elle n'est pas supprimée. Ce sont deux régimes juridiques
  différents et le même encadré les imprime côte à côte.
- **« Sauf convention contraire » n'est pas « exclu ».** L'exclusion des motocycles dans l'assurance
  accidents est levable par accord ; le document ne dit ni comment, ni à quel prix, ni sous quelles
  conditions.
- **Les quadricycles voyagent avec les motos dans les documents commerciaux, pas dans la loi.** Où tombe un
  quad se décide sur le test de l'art. 1er a), pas sur l'étiquette de vente.
- **Il n'existe pas de statistique deux-roues publiée.** La nomenclature prudentielle ne connaît pas de
  branche deux-roues : les primes correspondantes sont à l'intérieur des branches 3 et 10, avec l'automobile,
  et ne sont pas séparables dans les agrégats publiés par le [[CAA]].

## Lacunes établies

- **Zéro document, zéro produit, zéro assureur dans la branche.** La page est en `status: stub` et le restera
  tant qu'un document deux-roues luxembourgeois n'aura pas été extrait.
- **Le seul produit deux-roues luxembourgeois observé est illisible.** *OptiDrive Moto* : nom, référence de
  wording (W04.2021), page produit et noms de fichiers connus ; contenu jamais ouvert, par respect du
  `robots.txt` de l'éditeur.
- **Aucune règle luxembourgeoise propre au deux-roues n'a été vérifiée** en matière de permis, de cylindrée,
  d'âge minimal ou d'immatriculation. Absence de vérification, pas absence de règle — la distinction est
  faite ici plutôt que laissée à deviner.
- **Les garanties, exclusions et plafonds typiques ne sont pas écrits**, et ne le seront que depuis des
  documents. Les recopier depuis la page française *Deux-roues, quads et voiturettes* reviendrait à importer
  du droit qui ne s'applique pas ici.

## Cadre légal

- **Loi modifiée du 16 avril 2003** relative à l'assurance obligatoire de la responsabilité civile en matière
  de véhicules automoteurs : art. 1er a) (définition du véhicule, seuils de 2024), art. 2 point 1
  (obligation, débiteur), art. 5 (étendue de la garantie), art. 28 point 1 (sanctions). Mêmes mécanismes
  collectifs que l'automobile — FGA, Bureau luxembourgeois, pool des risques aggravés, FIAA — décrits dans
  [[Assurance auto]].
- **Loi du 29 mars 2024** portant transposition de la directive (UE) 2021/2118 : nouvelle définition du
  véhicule à l'art. 1er a).
- **Loi du 21 septembre 2023** : transfert de l'obligation d'assurance au titulaire du certificat
  d'immatriculation.
- **Loi modifiée du 27 juillet 1997 sur le contrat d'assurance**, pour le régime du contrat.
- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA), annexe I**, branches 3 et 10.
- **Aucun texte luxembourgeois spécifique aux deux-roues** n'a été trouvé en matière d'assurance.
- Superviseur : [[CAA]].

## Related

- [[Assurance auto]] · [[Assurance accidents]] · [[Assurance habitation]] · [[Autres]] · [[CAA]] ·
  [[Civil Liability|responsabilité civile]] · [[Exclusion]] · [[00 - Luxembourg MOC]]

## Sources

- Loi modifiée du 16 avril 2003, texte coordonné au 6 avril 2024 publié par le Commissariat aux Assurances.
- Loi du 29 mars 2024, Mémorial A n° 136 du 2 avril 2024, publiée sur Legilux.
- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe I.
- `sources/lu/_country.yml`, branche `moto` (et l'absence déclarée de `edpm`).
- `_meta/lu-market-census.md`, section « Compulsory covers » et correction du 2026-08-03 sur le titulaire du
  certificat d'immatriculation.
- `_meta/discovery/lu/foyer.md` (gamme Mobilité, douze IPID Auto, zéro occurrence deux-roues).
- `_meta/discovery/lu/baloise.md` (piège n° 3 : l'IPID *Drive* est l'IPID moto).
- `_meta/discovery/lu/axa.md` (OptiDrive Moto : catalogue énuméré, documents fermés par `robots.txt`).
- `data/lu/extracted/lalux/` : `easyprotect-pro-auto-*.json`, `easyprotect-accident-*.json`,
  `easyprotect-unfall-*.json`, `easyprotect-habitation-*.json`, `easyprotect-home-*.json`.
