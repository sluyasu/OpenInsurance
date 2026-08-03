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

## Inventaire de la bibliothèque

_(en cours)_

## Ce qui n'a pas pu être atteint

_(en cours)_
