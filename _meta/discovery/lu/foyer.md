# foyer — Foyer (FOYER ASSURANCES S.A. et al.)

website: foyer.lu
fetch: plain
status: enum
lang: fr, de
enumerated: 2026-08-02

**485 documents inventoriés, 2 accessibles, 0 ingérables. Et le chiffre qui compte n'est aucun des
trois : Foyer ne publie aucune conditions générales, indépendamment de tout blocage.**

Foyer est le premier groupe d'assurance de détail luxembourgeois, sous quatre agréments distincts :
`FOYER ASSURANCES S.A.` (non-vie), `FOYER VIE S.A.` (vie), `FOYER-ARAG` (**branche 17 seule**,
protection juridique) et `Foyer Global Health` (branches 1, 2, 13, 16, 18, le livre expatriés).

## Ce que dit le robots.txt, et pourquoi c'est une décision et non un pare-feu

```
User-agent: *
Disallow: /fr/basedoc_file/*      Disallow: /fr/mydoc/*
Disallow: /en/basedoc_file/*      Disallow: /en/mydoc/*
Disallow: /de/basedoc_file/*      Disallow: /de/mydoc/*
Disallow: /wp-admin/              Disallow: /wp-include/
Allow: /fr/mydoc/12727
Allow: /en/mydoc/12800
```

Les deux dernières lignes de `Disallow` sont du gabarit WordPress ; les six premières ne le sont
pas. L'éditeur a **énuméré ses chemins de documents, les a fermés, puis en a rouvert exactement
deux**. Ce n'est pas une règle anti-robot qui attrape des PDF par effet de bord, c'est un choix, et
ce projet le respecte : rien sous les chemins interdits n'a été récupéré.

**Les deux exceptions ne sont même pas des documents de la bibliothèque.** Elles n'apparaissent dans
aucune des 800 lignes des pages de listing : ce sont le *Guide du Nouvel Arrivant* et le
*Newcomer's Guide 2026-2027*, 72 pages, exportés du même projet InDesign à 85 secondes d'intervalle,
de sha256 distincts — donc deux vraies éditions linguistiques et non un fichier servi deux fois.
Non contractuels. Seule entité nommée : FOYER ASSURANCES S.A.

Ils ont été récupérés **redirections désactivées** : `Allow: /fr/mydoc/12727` ne s'étendrait pas à
une cible de redirection sous `basedoc_file`, qui est interdite. Les deux ont répondu 200
`application/pdf` directement, donc aucune URL interdite n'a jamais été demandée.

## Le fait qui rend le blocage secondaire

**Foyer ne publie aucune conditions générales.** Zéro ligne sur 800 contient *condition*, *AGB* ou
*Bedingung*, dans les trois langues. Un accès complet ne livrerait donc toujours pas un seul
contrat : la bibliothèque est faite de 54 IPID et de 431 fiches d'information financière — 371 DIC
PRIIPs, une quarantaine de fiches et une cinquantaine de documents SFDR.

C'est la même observation que sur le marché français, où publier l'IPID est une obligation et
publier les conditions générales n'en est pas une. Le Luxembourg transpose la même directive et
produit le même résultat.

## Corrections apportées en cours de route

- **La bibliothèque fait 485 documents, pas 155.** Une première passe avait extrait les identifiants
  avec une expression régulière `(\d+)` et manqué les 209 identifiants en toutes lettres
  (`vepr-dl-74`, `ep-dl-111`) — 43 % du total.
- **Le préfixe de langue est cosmétique** : les 800 liens utilisent `/fr/mydoc/` dans les trois
  versions du site. Une passe intermédiaire avait cru que la version allemande frappait ses propres
  identifiants ; c'est faux.
- **L'anglais n'est pas une langue de document chez Foyer** — le site le dit lui-même, un `h2`
  annonçant « french version ». L'allemand l'est, avec environ 200 documents distincts.
- Une passe avait conclu que la version anglaise était injoignable : c'était son propre balayage qui
  échouait, pas le site.

## Une erreur du manifeste pays trouvée ici

`sources/lu/_country.yml` justifiait la branche `moto` en affirmant que le deux-roues se vend au
Luxembourg comme un produit distinct avec son propre IPID, « mesuré sur la bibliothèque de Foyer ».
**Cette citation est fausse** : zéro occurrence de *moto*, *scooter* ou *zweirad* sur 800 lignes, et
les douze IPID de la gamme Mobilité sont tous des IPID Auto. La branche est conservée — l'obligation
de l'art. 2 de la loi du 16 avril 2003 vise bien tout véhicule automoteur — mais le motif tiré de la
pratique commerciale a été corrigé dans le manifeste.

## Pas de `sources/lu/foyer.yml`

Deux documents non contractuels ne justifient pas un fichier de sources, et le reste est
inaccessible par choix de l'éditeur. Même traitement que [Wakam](../fr/wakam.md),
[Acheel](../fr/acheel.md), [MGEN](../fr/mgen.md) et [ACM](../fr/acm.md) côté français — quatre
raisons différentes à chaque fois, celle-ci en est une cinquième.
