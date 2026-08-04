# foyer-vie — FOYER VIE S.A.

website: foyer.lu (pas d'hôte propre)
fetch: plain
status: enum
lang: fr, de, en
enumerated: 2026-08-04

**Cinq IPID, zéro conditions générales, et zéro document récupérable. Mais la découverte
rapporte mieux qu'un compte : elle rapporte la raison. Chez Foyer, les conditions générales
existent bel et bien en PDF — elles sont derrière un formulaire qui exige un numéro de client
et un numéro de contrat. Le « zéro CG » de [foyer.md](foyer.md) n'est pas une absence de
document, c'est une porte.**

## L'entité agréée

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-04,
`Last-Modified: Tue, 04 Aug 2026 01:00:12 GMT`, 200 `text/csv`, sans clé ni cookie ni compte.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisVie.csv`

```
"FOYER VIE S.A. (549300387YFQKY1VF456)","12, rue Léon Laval, 3372 Leudelange","Franck MARCHAND, Marie-Hélène MASSARD, Jim RASQUE","(+352) 43743-4000","437 43 4500","I, II, III, VI, VII"
```

**Société luxembourgeoise agréée en vie, pas une succursale étrangère.** Elle détient cinq des
sept branches de l'ANNEXE II de la loi modifiée du 7 décembre 2015 : I (vie, décès, mixtes,
rentes non liées à des fonds), II (nuptialité, natalité), III (liées à des fonds
d'investissement), VI (capitalisation), VII (gestion de fonds collectifs de retraite). Elle est
**absente des trois listes non-vie** — le principe de spécialisation luxembourgeois interdit le
cumul, comme pour DKV. Sa jumelle non-vie du même groupe et de la même adresse est
`FOYER ASSURANCES S.A.`

L'identifiant entre parenthèses est un **LEI** (`549300387YFQKY1VF456`), pas un RCS ; le CAA n'en
publie pas.

Rappel de méthode déjà écrit dans [le recensement](../../lu-market-census.md) : côté vie,
**le registre ne discrimine rien** — les vingt-huit assureurs vie luxembourgeois détiennent tous
la branche I et tous la branche III. L'agrément de FOYER VIE ne la distingue donc pas d'un
véhicule de placement transfrontalier ; c'est la bibliothèque publiée qui la distingue, et c'est
elle qui a été mesurée ici.

### Une cinquième entité du groupe, absente du décompte à quatre

[foyer.md](foyer.md) énumérait « quatre agréments distincts ». Il y en a un cinquième, à la même
adresse et dans le même périmètre :

```
"RAIFFEISEN VIE S.A. (549300QOM0DY7TROFK76)","12, rue Léon Laval, 3372 Leudelange","Franck MARCHAND, Jim RASQUE","(+352) 26683620","26 68 36 22","I, II, III, VI"
```

Deux preuves, l'une et l'autre publiées par Foyer : le bandeau de consentement répété sur **87 des
180 pages** récupérées de `foyer.lu`, dans les trois langues, nomme le périmètre — « **Foyer Group
(Foyer Assurances, Foyer Vie, Raiffeisen Vie, Foyer Distribution, Nexfin)** » — et
`groupe.foyer.lu/fr/documents` publie un `QRT public 2025 de Raiffeisen Vie` parmi les annexes SFCR
du groupe.

Deux remarques sur ce bandeau, parce qu'il est le seul endroit où Foyer énumère son périmètre en
clair : **FOYER-ARAG et Foyer Global Health n'y figurent pas**, alors que leurs QRT sont bien dans
les annexes SFCR du groupe. La liste du bandeau est une liste de consentement marketing, pas un
périmètre de consolidation. Ne pas l'utiliser comme organigramme.

Raiffeisen Vie n'a **pas été traitée dans cette passe** et reste à faire.

## Verdict robots.txt

Il n'existe **pas d'hôte propre à FOYER VIE** : `foyervie.lu` et `foyer-vie.lu` sont NXDOMAIN.
L'entité publie via `www.foyer.lu`, dont le `robots.txt` a été récupéré le 2026-08-04 (200
`text/plain`, 305 octets, `Last-Modified: Tue, 16 Jun 2026 08:48:18 GMT`) :

```
User-agent: *
Disallow: /fr/basedoc_file/*
Disallow: /en/basedoc_file/*
Disallow: /de/basedoc_file/*
Disallow: /fr/mydoc/*
Disallow: /en/mydoc/*
Disallow: /de/mydoc/*
Disallow: /wp-admin/
Disallow: /wp-include/
Allow: /fr/mydoc/12727
Allow: /en/mydoc/12800
Sitemap: https://www.foyer.lu/sitemap_index.xml
```

Inchangé depuis [foyer.md](foyer.md), à une ligne près : **le fichier déclare aujourd'hui un
sitemap**, que la citation précédente ne portait pas. Il a servi ici, et uniquement, à énumérer les
**pages HTML** : `sitemap_index.xml` renvoie trois sitemaps de langue (`/fr/`, `/en/`, `/de/`),
soit **1 706 URL distinctes** (611 fr, 595 en, 596 de). Aucun document n'a été demandé sous un
chemin interdit.

## Inventaire

179 pages ciblées (`/particuliers/`, `/individual/`, `/privatpersonen/`, `/professionnels/`,
`/info/`, plus les six pages `ipid` et `conditions générales` des trois langues) ont été
récupérées : **179 sur 179 en 200, zéro échec.**

**Sur ces 180 pages, il y a exactement un lien `.pdf` direct**, et il pointe vers
`etsi.org` — la norme d'accessibilité EN 301 549. Exactement la même anomalie que sur
[dkv.md](dkv.md), et le même verdict : hors sujet. **`foyer.lu` ne publie aucun PDF en direct.**
Tous ses documents passent par `/xx/mydoc/<id>`, c'est-à-dire par le chemin fermé.

Autre mesure de la même série : **`FOYER VIE S.A.` n'est écrite en toutes lettres que sur trois
pages** — les trois versions du simulateur fiscal (`/fr/…/simulateur-fiscal/`,
`/de/…/steuersimulator/`, `/en/…/fiscal-simulator/`), et seulement dans une clause de
non-responsabilité (« des résultats indicatifs qui ne constituent ni une offre ni un engagement
contractuel de FOYER VIE S.A. »). Sur les pages produit vie elles-mêmes, le porteur n'est jamais
nommé : c'est « Foyer ». **Le porteur se lit dans le document, jamais dans la marque** — et ici,
faute de document accessible, il ne se lit nulle part.

### Les cinq documents de FOYER VIE

La page `https://www.foyer.lu/fr/ipid` (`Document d'information sur le produit d'assurance |
Foyer Assurances`) liste **30 IPID avec leur édition**. Cinq relèvent de la vie :

| Document | Édition | Identifiant | Branche wiki |
|---|---|---|---|
| IPID Horizont60 Invest | 31/10/2018 | `/fr/mydoc/11294` | `assurance-vie` |
| IPID Horizont60 Capi | 31/10/2018 | `/fr/mydoc/11293` | `assurance-vie` |
| IPID Focus Investissement | 31/10/2018 | `/fr/mydoc/11291` | `solde-restant-du` (voir plus bas) |
| IPID Focus Financement | 31/10/2018 | `/fr/mydoc/11290` | `assurance-vie` |
| IPID Chronos Temporaire Décès | 31/10/2018 | `/fr/mydoc/11286` | `prevoyance` |

**Cinq documents, pas quinze.** Les pages `/de/ipid` et `/en/ipid` pointent les **mêmes
identifiants numériques** que `/fr/ipid` — vérifié lien par lien. Le préfixe de langue de l'URL
est cosmétique, comme déjà mesuré dans [foyer.md](foyer.md) ; ici la démonstration est faite sur
les liens et non sur un balayage.

*(Pour les IPID auto, Medicis, mozaïk et Multirisk Pro, les versions `de`/`en` frappent en revanche
des identifiants distincts — 12806-12817, 13018-13035. Le comportement n'est donc pas uniforme sur
la page : la gamme vie est mono-document, la gamme non-vie est trilingue. Ne pas généraliser dans
un sens ni dans l'autre.)*

S'y ajoutent **huit brochures** attribuables aux pages vie (`8929`/`8930`/`8931` épargne-retraite
et optimisation fiscale, `12430`/`12442` investissement, `13031`/`13032`/`13033` prévoyance) —
documents commerciaux, non contractuels.

Toutes ces URL sont sous `Disallow`. **Aucune n'a été demandée.**

| Type | Documents | Langues distinctes |
|---|---|---|
| IPID | **5** | 1 fichier par produit, servi aux trois arbres |
| Brochures / dépliants | 8 | fr, de, en (identifiants distincts) |
| **Conditions générales** | **0** | — |

### La branche `solde-restant-du` : le produit est nommé, le document n'existe pas publiquement

Les trois pages du produit —
`/fr/particuliers/habitation-quotidien/assurance-solde-restant-du/`,
`/de/privatpersonen/wohngebaude-alltag/restschuldversicherung/`,
`/en/individual/home-lifestyle/outstanding-balance-insurance/` — **ne portent aucun lien de
document, dans aucune des trois langues.** Ni IPID, ni conditions générales, ni brochure.

Elles nomment en revanche le produit, et c'est utile pour le manifeste pays :

> « L'assurance temporaire solde restant dû (**TSRD**) *focus investissement* couvre les emprunts
> immobiliers et les investissements à long terme consentis pour acheter ou construire une
> habitation ou des locaux professionnels. »

Le sigle **TSRD** est le nom local du produit et devrait rejoindre les `aliases` de la branche
`solde-restant-du` dans `sources/lu/_country.yml`, qui ne le porte pas.

Observation, pas déduction : un `IPID Focus Investissement` figure bien dans la liste ci-dessus,
et la page produit appelle le TSRD « focus investissement ». **Le document n'a pas été ouvert** —
il est sous chemin interdit — donc rien ne permet d'affirmer qu'il documente le TSRD plutôt qu'un
autre usage de la même enveloppe. À vérifier le jour où l'accès existera, pas avant.

## Ce qui bloque : les conditions générales sont un service authentifié, pas un document publié

C'est le résultat principal de cette passe, et il corrige la lecture de [foyer.md](foyer.md) sans
en changer le chiffre.

Les trois pages `https://www.foyer.lu/{fr/conditions-generales, en/general-conditions,
de/allgemeine-bedingungen}` existent, sont autorisées, et ont été récupérées (200). Ce ne sont
**pas des pages de listing**. Ce sont des formulaires :

> « **Consultez vos conditions générales.** Pour consulter vos conditions générales, merci de
> renseigner le **Numéro Client** et le **Numéro Contrat** dans les champs prévus à cet effet. Ces
> informations sont imprimées sur vos Conditions Particulières reçues par courrier postal. »

Et, dans le gabarit de résultat que la page porte déjà en HTML :

> « Conditions Générales trouvées. Tous les documents listés ci-dessous et proposés en
> téléchargement sont au format PDF. »

**Les conditions générales de Foyer existent donc en PDF.** Elles ne sont simplement pas publiées :
elles sont servies contrat par contrat, à qui présente deux identifiants imprimés sur ses propres
conditions particulières. Le seul lien documentaire de ces pages est
`/{fr,en,de}/mydoc/GEN-Comp-9` — un identifiant alphanumérique, sous `Disallow`.

### Limite dure, à ne franchir dans aucune passe future

Ce formulaire est un **point d'entrée d'énumération sur données personnelles**. Un balayage de
couples (numéro client, numéro contrat) exposerait des documents rattachés à des personnes
identifiables. **Aucun essai n'a été fait, aucun couple n'a été soumis, et aucun ne doit l'être** —
y compris « pour tester si ça répond ». Ce projet ne recueille que des documents publics ; un
document accessible uniquement à un assuré au moyen de ses identifiants n'est pas public, quelle
que soit la facilité technique de l'atteindre.

C'est la même famille de risque que les spécimens de contrats remplis déjà rencontrés ailleurs sur
ce marché : la bonne réaction est de ne pas déréférencer et de ne pas écrire l'URL dans le dépôt.

## Ce qui n'a pas pu être atteint

| Objet | Raison |
|---|---|
| Les 5 IPID vie | chemin `Disallow: /fr/mydoc/*`, non demandés |
| Les 8 brochures vie | idem |
| Les conditions générales | authentification par numéro de client + numéro de contrat |
| Un IPID solde restant dû | **aucun lien de document sur les trois pages du produit** |
| `QRT public 2025 de Foyer Vie` | servi depuis `/fr/mydoc/WebSites-Documentsgroupe-371`, fermé — et prudentiel, donc hors périmètre du wiki de toute façon |
| RAIFFEISEN VIE S.A. | entité du groupe non traitée dans cette passe |

## Pas de `sources/lu/foyer-vie.yml`

Cinq documents connus, cinq documents interdits, zéro conditions générales publiée. Rien à
télécharger, donc rien à déclarer. Même traitement que [foyer.md](foyer.md) et
[foyer-arag.md](foyer-arag.md).
