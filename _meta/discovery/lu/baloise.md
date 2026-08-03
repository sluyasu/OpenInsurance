# baloise — Baloise (BALOISE ASSURANCES LUXEMBOURG S.A. / BALOISE VIE Luxembourg S.A.)

website: baloise.lu
fetch: plain
status: en cours
lang: fr, de, en
enumerated: 2026-08-03

**DÉCOUVERTE EN COURS — ce fichier est écrit au fil de l'eau.**

## Les deux entités agréées

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-03,
`Last-Modified: Mon, 03 Aug 2026 01:00:12 GMT`.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv`

```
"BALOISE ASSURANCES LUXEMBOURG S.A. (549300J4JNKWP52PIP34)","8, rue du Château d'Eau, 3364 Leudelange","Christine THEODOROVICS","(+352) 290190-1","290 591","1, 3, 6, 7, 8, 9, 10, 12, 13, 16, 17, 18"
```

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisVie.csv`

```
"BALOISE VIE Luxembourg S.A. (549300NF39GNDIKK4T88)","8, rue du Château d'Eau, 3364 Leudelange","Christine THEODOROVICS","(+352) 290190-1","290 190 9001","I, II, III, VI, VII"
```

Les deux dénominations de la commande sont exactes, au détail de casse près : le registre écrit
`BALOISE ASSURANCES LUXEMBOURG S.A.` tout en capitales et `BALOISE VIE Luxembourg S.A.` avec
`Luxembourg` en minuscules. Même adresse et même responsable pour les deux.

**Le registre ne publie pas de numéro RCS.** L'identifiant entre parenthèses est un **LEI**
(20 caractères alphanumériques, format ISO 17442), pas un RCS luxembourgeois (`B` + chiffres).
Ne pas confondre les deux : à renseigner comme LEI ou à laisser vide, jamais recopié en RCS.

Branches détenues, telles que le registre les écrit :

- **BALOISE ASSURANCES LUXEMBOURG S.A.** (non-vie) — 1, 3, 6, 7, 8, 9, 10, 12, 13, 16, 17, 18.
  La branche 10 (R.C. véhicules terrestres automoteurs) et la branche 3 (corps de véhicules
  terrestres) confirment la vente au détail. Pas de branche 2 (maladie), pas de 14/15
  (crédit/caution).
- **BALOISE VIE Luxembourg S.A.** (vie) — I, II, III, VI, VII.

Conformément au principe de spécialisation luxembourgeois, les deux listes du registre ne se
croisent pas : aucune société n'est à la fois vie et non-vie.

### Le RCS vient du site, pas du registre — et le site contredit le registre sur une branche

`https://www.baloise.lu/fr/assurance-baloise-luxembourg/mentions-legales.html` publie les
identifiants que le CSV du CAA n'a pas :

- **Baloise Assurances Luxembourg S.A.** — société anonyme de droit luxembourgeois, capital
  social 14 648 626,02 €, **RCS Luxembourg B 68 065**, matricule 1998 2235 882,
  TVA LU 18 47 59 84, siège 8 rue du Château d'Eau, L-3364 Leudelange.
- **Baloise Vie Luxembourg S.A.** — société anonyme de droit luxembourgeois, capital social
  32 680 320 €, **RCS Luxembourg B 54 686**, matricule 1996 2205 790, TVA LU 16 74 29 20,
  même siège.

La page se décrit elle-même comme le site des deux sociétés à la fois : « www.baloise.lu est le
site Internet des sociétés Baloise Assurances Luxembourg S.A., et Baloise Vie Luxembourg S.A. ».
C'est la formulation qui rend `carrier: null` obligatoire par défaut — la marque est partagée
entre deux porteurs de risque distincts, et seul le document sait lequel il engage.

**Divergence mesurée.** Les mentions légales énumèrent les branches non-vie
« 1, 3, 7, 8, 9, 10, 12, 13, 16, 17, 18 » : **onze branches, la 6 manque**, alors que le registre
du CAA en publie douze et inclut la 6 (corps de véhicules maritimes, lacustres et fluviaux). La
divergence n'est pas théorique : Baloise publie une page produit « bateau », qui est précisément
ce que la branche 6 couvre. Le registre du CAA fait foi ; la liste du site est incomplète. Ne pas
dériver l'agrément d'une page web.

## robots.txt — verdict par hôte

### `www.baloise.lu` (récupéré 2026-08-03, `Last-Modified: Fri, 14 Jul 2023 05:56:17 GMT`)

```
# robots.txt for baloise-lu
User-agent: *
Disallow:
```

**Trois lignes, et un `Disallow:` vide.** Un `Disallow:` sans valeur n'interdit rien : c'est la
formulation qui autorise l'intégralité du site. Aucun chemin de documents n'est fermé, aucune
règle `*.pdf`, aucun agent nommé. C'est le contraire exact de Foyer, qui avait énuméré ses chemins
de documents pour les fermer.

### `www.caa.lu` (récupéré 2026-08-03)

```
# @package    vanilla
# @subpackage web
# @author     Loops <evrard@h2a.lu>
# @version    SVN: $Id: robots.txt 1 2013-01-14 10:30:16Z loops $

User-agent: *
Allow: /
```

Ouvert. Les deux CSV du registre ont répondu 200 `text/csv` à une requête simple, sans clé,
sans cookie et sans compte.

## Correction au census : `baloise.lu` n'est pas « curl-hostile »

`_meta/lu-market-census.md` classe `baloise.lu` en `plain, curl-hostile` — « 200 to `urllib`,
**406 to `curl`** with the same User-Agent ». **Mesuré le 2026-08-03, c'est l'inverse, et le
vrai discriminant n'est ni curl ni urllib : c'est l'en-tête `Accept`.**

- `curl` avec un User-Agent personnalisé : **200** sur `robots.txt`, la page d'accueil, la page
  auto et les mentions légales. curl envoie `Accept: */*` par défaut.
- `urllib` avec le même User-Agent et **aucun en-tête `Accept`** : **406 Not Acceptable** sur les
  trois pages d'accueil de langue.
- `urllib` avec `Accept: */*` ajouté : **200**.

Le serveur refuse une requête sans `Accept`, ce qu'aucun navigateur n'envoie jamais. La leçon du
census française tient toujours (« a curl 4xx is not proof of a block ») mais son exemple
luxembourgeois est à corriger : il faut lire `plain`, en envoyant un `Accept`.

## Inventaire de la bibliothèque

_(en cours)_

## Ce qui n'a pas pu être atteint

_(en cours)_
