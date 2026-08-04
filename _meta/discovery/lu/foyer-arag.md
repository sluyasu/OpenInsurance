# foyer-arag — FOYER-ARAG

website: aucun
fetch: n/a
status: unreachable
lang: —
enumerated: 2026-08-04

**Un seul assureur luxembourgeois ne détient que la branche 17, et il n'a pas de site web.
Un seul document lui est attribuable dans tout l'espace public — l'`IPID Arag Particulier`,
édition 30/09/2019 — et il est servi depuis un chemin que le `robots.txt` de `foyer.lu`
interdit. Zéro conditions générales, et zéro document récupérable.**

## L'entité agréée

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-04,
`Last-Modified: Tue, 04 Aug 2026 01:00:12 GMT`, 200 `text/csv`, sans clé ni cookie ni compte.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv`

```
"FOYER-ARAG (549300AOZVE762VZ0D50)","12, rue Léon Laval, 3372 Leudelange","Franck MARCHAND, Jim RASQUE","(+352) 437437","42 87 17","17"
```

**Société luxembourgeoise agréée, pas une succursale étrangère** : elle figure dans la liste des
assureurs luxembourgeois non-vie, et non dans
`AssurancesDirectes_SuccursalesEtrangeresNonVie.csv` — dont la seule entrée dont le nom évoque
ARAG est `DARAG Deutschland AG, succursale luxembourgeoise` (branches 3, 10, 13, 17, 18), une
entité sans lien avec celle-ci. Absente également de la liste vie.

L'identifiant entre parenthèses est un **LEI** (`549300AOZVE762VZ0D50`, 20 caractères, ISO 17442),
pas un RCS ; le CAA n'en publie pas.

### Correction : elle n'est pas le seul détenteur de la branche 17, elle est la seule à ne détenir qu'elle

La formulation « seul détenteur de la branche 17 du registre luxembourgeois » est fausse et a été
vérifiée ligne à ligne : **21 des 35 assureurs non-vie luxembourgeois détiennent la branche 17**,
dont FOYER ASSURANCES S.A. elle-même (`1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18`),
LA LUXEMBOURGEOISE, AXA, Baloise, AIG, Tokio Marine, plusieurs P&I clubs maritimes.

Ce qui est vrai, et ce qui compte, c'est l'**exclusivité inverse** : FOYER-ARAG est la seule à
détenir la 17 **et rien d'autre**. Le registre ne compte que trois assureurs mono-branche :

| Assureur | Branche unique |
|---|---|
| BOLTON INTERNATIONAL S.C.A. | 16 (pertes pécuniaires diverses) |
| DKV LUXEMBOURG S.A. | 2 (maladie) |
| **FOYER-ARAG** | **17 (protection juridique)** |

Le Luxembourg a donc bien un porteur spécialisé de la protection juridique, comme la Belgique, et
c'est ce fait-là — pas un monopole d'agrément — que la page de branche doit énoncer. La note de
`sources/lu/_country.yml` (« FOYER-ARAG holds an authorisation for branch 17 and nothing else »)
était déjà correcte ; c'est le brief de cette passe qui l'avait durcie à tort.

## Pas de `robots.txt`, parce qu'il n'y a pas de site

Trois hôtes ont été testés, et aucun n'est le site de l'entité.

**`foyer-arag.lu`** — le domaine est enregistré et actif, mais il ne porte **que des enregistrements
MX** (`mx1.hc1686-69.eu.iphmx.com`, `mx2.…`) : pas d'enregistrement A. C'est un domaine de courrier.

**`www.foyer-arag.lu`** — alias de `teros.lefoyer.lu` → `194.154.209.229`, une machine de
l'infrastructure Foyer distincte de celle de `www.foyer.lu` (`195.46.232.215`). Rien n'y écoute :

```
https://www.foyer-arag.lu/robots.txt → curl (7) Failed to connect … port 443
http://www.foyer-arag.lu/robots.txt  → curl (56) Recv failure: Connection reset by peer
```

Le nom résout, le serveur refuse la connexion. Il n'y a donc **ni `robots.txt`, ni site, ni
politique d'indexation propre** — et rien ne se déduit ici de la politique de `foyer.lu`.

**`arag.lu`** — répond, mais ce n'est pas l'entité luxembourgeoise. Le certificat TLS présenté est
`CN=www.meinearag.de` (SAN : `meinearag.de`, `meine-arag.de`, `www.meine-arag.de`) et `http://arag.lu/`
redirige vers `https://www.arag.com/`. C'est une réservation défensive du groupe allemand ARAG, sans
rapport avec l'agrément luxembourgeois. Le piège est exactement celui du recensement : **la marque
n'est pas le porteur**, et ici le domaine à son nom appartient à quelqu'un d'autre.

## Le seul document attribuable, et pourquoi il reste hors d'atteinte

FOYER-ARAG publie via `foyer.lu`, dont le `robots.txt` (récupéré le 2026-08-04, 200 `text/plain`,
305 octets, `Last-Modified: Tue, 16 Jun 2026 08:48:18 GMT`) dit :

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

*(La ligne `Sitemap:` ne figurait pas dans la citation de [foyer.md](foyer.md) ; elle est présente
aujourd'hui et a servi ici à énumérer les pages HTML — jamais les documents.)*

Sur la page publique `https://www.foyer.lu/fr/ipid`, qui liste 30 IPID avec leur édition, une seule
ligne relève de la protection juridique :

> `IPID Arag Particulier` — Édition **30/09/2019** — `https://www.foyer.lu/fr/mydoc/11341`

`/fr/mydoc/11341` tombe sous `Disallow: /fr/mydoc/*` et ne figure pas parmi les deux exceptions
`Allow`. **Il n'a pas été demandé.** C'est le seul document du corpus public rattachable à
FOYER-ARAG, et il est fermé par choix de l'éditeur.

Détail mesuré : les versions `/de/ipid` et `/en/ipid` de cette page pointent **le même
`/fr/mydoc/11341`**. Il n'existe donc pas trois IPID Arag linguistiques mais **un seul document**, et
le préfixe de langue de l'URL est cosmétique — même observation que [foyer.md](foyer.md), reconfirmée
ici lien par lien.

Le titre de la page qui l'héberge est instructif : `Document d'information sur le produit d'assurance
| **Foyer Assurances**`. Une seule marque en en-tête, et sous elle des IPID d'au moins **trois
porteurs distincts** — Foyer Assurances (auto, Multirisk Pro, Medicis), Foyer Vie (Horizont60, Focus,
Chronos) et Foyer-ARAG (Arag Particulier). La marque de la page ne dit pas le porteur du document.

## L'hypothèse « porteur nommé dans les documents d'autrui » n'est pas confirmée

Les 160 PDF du corpus luxembourgeois déjà téléchargés (lalux, Baloise, DKV) ont été convertis en
texte et fouillés : **zéro occurrence** de `FOYER-ARAG`, `ARAG`, `FOYER ASSURANCES`, `FOYER VIE` ou
`Foyer Global Health`. Les seuls appariements bruts sur la chaîne `arag` étaient des occurrences de
*garage* dans des contrats auto, et ceux sur `foyer` le nom commun (« les personnes vivant à son
foyer »).

C'est cohérent, et il faut le dire dans ce sens : le corpus est composé de documents lalux, Baloise
et DKV, c'est-à-dire de **concurrents**. Le document lalux classé en `protection-juridique`
(`ipid_assurance_protection_juridique_fr.pdf`, unique document de la branche à ce jour) nomme
`LA LUXEMBOURGEOISE S.A.` comme porteur, pas FOYER-ARAG. L'hypothèse selon laquelle la protection
juridique accompagne la RC privée sans être portée par le même assureur reste ouverte pour Foyer,
mais **elle ne peut pas être testée sur ce corpus** : il faudrait les documents Foyer, qui sont
fermés.

## Ce que l'entité publie par ailleurs : rien de contractuel, et rien d'atteignable

`groupe.foyer.lu` est un **hôte distinct avec sa propre politique**, et cette politique est ouverte
(200 `text/plain`, 24 octets, `Last-Modified: Mon, 20 Jul 2026 12:37:02 GMT`) :

```
User-agent: *
Disallow:
```

Un `Disallow:` vide n'interdit rien. Les 67 URL de son sitemap ont toutes été récupérées (après
correction : le sitemap publie des URL contenant des **espaces et des accents non encodés**, du type
`/fr/actualites/Communiqués de presse/…`, qui échouent en 500 tant qu'on ne les percent-encode pas).

**Cette ouverture n'apporte rien.** La page `groupe.foyer.lu/fr/documents` publie les annexes SFCR par
entité, dont `QRT public 2025 de Foyer ARAG` — mais le lien est
`https://www.foyer.lu/fr/mydoc/WebSites-Documentsgroupe-369`, c'est-à-dire **le chemin fermé de
l'autre hôte**. Les huit QRT 2025 (Foyer ARAG, Foyer Assurances, Foyer Groupe, Foyer Luxembourg Ré,
Foyer Global Health, Foyer Vie, Raiffeisen Vie, WEALINS) et le SFCR 2025 sont tous servis ainsi.
Le `robots.txt` ouvert du site institutionnel ne fait qu'ouvrir des pages qui pointent vers des
documents interdits.

Une génération d'URL plus ancienne subsiste dans le HTML — `www.foyer.lu/uploads/content/file/13/70/
QRT public 2017 Foyer-ARAG_….pdf` — hors des chemins interdits, mais **404** en HEAD (comme ses
sept jumelles 2017). Rien à récupérer là non plus.

Ces documents sont de toute façon **prudentiels et non contractuels** : des QRT Solvabilité II ne
décrivent aucun produit et n'ont pas leur place dans le wiki.

## Ce qui bloque, et ce qui n'est pas bloqué

| Fait | Valeur |
|---|---|
| Documents inventoriés | **1** (`IPID Arag Particulier`, éd. 30/09/2019) |
| Documents récupérables | **0** — chemin `Disallow` |
| **Vraies conditions générales** | **0** |
| Site propre | aucun (domaine sans A record, hôte sans serveur) |
| Verdict `robots.txt` | pas de `robots.txt` (pas de site) ; documents fermés par celui de `foyer.lu` |

Ce qui n'a pas pu être atteint, et pourquoi :

- **Le contenu de l'IPID Arag Particulier** — chemin interdit. Non demandé. On sait qu'il existe et
  quelle est son édition ; on ne sait pas ce qu'il couvre.
- **Les conditions générales de la protection juridique Foyer** — voir [foyer-vie.md](foyer-vie.md) :
  chez Foyer, les conditions générales ne sont pas un document public mais une **consultation
  authentifiée par numéro de client et numéro de contrat**. Aucune énumération n'a été tentée sur ce
  formulaire et aucune ne doit l'être.

## Pas de `sources/lu/foyer-arag.yml`

Un document connu et interdit ne justifie pas un fichier de sources. Même traitement que
[foyer.md](foyer.md), et pour la même raison : le choix de l'éditeur, pas un obstacle technique.
