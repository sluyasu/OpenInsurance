# baloise — Baloise (BALOISE ASSURANCES LUXEMBOURG S.A. et BALOISE VIE Luxembourg S.A.)

website: baloise.lu
fetch: plain
status: enum
lang: fr, de, en
enumerated: 2026-08-03

**1 164 documents inventoriés, 268 accessibles, 34 ingérables. Et le chiffre qui compte est le
quatrième : zéro conditions générales, sur un site entièrement ouvert par son robots.txt.**

Baloise est le seul des trois assureurs luxembourgeois déjà examinés dont rien ne bloque la
bibliothèque — ni règle robots, ni WAF, ni rendu client. Le résultat est le même que chez Foyer,
qui bloque, et que chez lalux, qui ne bloque pas non plus : **le contrat n'est pas publié.**
Ce n'est donc pas un fait d'accès, c'est un fait de marché.

## Les deux entités agréées

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-03,
`Last-Modified: Mon, 03 Aug 2026 01:00:12 GMT`, 200 `text/csv`, sans clé ni cookie ni compte.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv`

```
"BALOISE ASSURANCES LUXEMBOURG S.A. (549300J4JNKWP52PIP34)","8, rue du Château d'Eau, 3364 Leudelange","Christine THEODOROVICS","(+352) 290190-1","290 591","1, 3, 6, 7, 8, 9, 10, 12, 13, 16, 17, 18"
```

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisVie.csv`

```
"BALOISE VIE Luxembourg S.A. (549300NF39GNDIKK4T88)","8, rue du Château d'Eau, 3364 Leudelange","Christine THEODOROVICS","(+352) 290190-1","290 190 9001","I, II, III, VI, VII"
```

Les deux dénominations sont exactes, au détail de casse près : le registre écrit
`BALOISE ASSURANCES LUXEMBOURG S.A.` tout en capitales et `BALOISE VIE Luxembourg S.A.` avec
`Luxembourg` en minuscules. Même adresse, même responsable, et le principe de spécialisation
luxembourgeois fait que les deux listes ne se croisent pas.

**Le registre ne publie pas de RCS.** L'identifiant entre parenthèses est un **LEI** (20
caractères, ISO 17442), pas un RCS luxembourgeois (`B` + chiffres). Les deux ne se substituent
pas l'un à l'autre.

### Le RCS vient du site — et le site contredit le registre sur une branche

`https://www.baloise.lu/fr/assurance-baloise-luxembourg/mentions-legales.html` publie ce que le
CSV n'a pas :

| | Baloise Assurances Luxembourg S.A. | Baloise Vie Luxembourg S.A. |
|---|---|---|
| forme | société anonyme de droit luxembourgeois | société anonyme de droit luxembourgeois |
| RCS | **B 68 065** | **B 54 686** |
| matricule | 1998 2235 882 | 1996 2205 790 |
| TVA | LU 18 47 59 84 | LU 16 74 29 20 |
| capital social | 14 648 626,02 € | 32 680 320 € |
| siège | 8, rue du Château d'Eau, L-3364 Leudelange | idem |
| LEI (registre CAA) | 549300J4JNKWP52PIP34 | 549300NF39GNDIKK4T88 |
| branches (registre CAA) | 1, 3, 6, 7, 8, 9, 10, 12, 13, 16, 17, 18 | I, II, III, VI, VII |
| branches (mentions légales) | 1, 3, **—**, 7, 8, 9, 10, 12, 13, 16, 17, 18 | I, II, III, VI, VII |

**La branche 6 manque dans les mentions légales.** Onze branches y sont listées, douze au
registre. La divergence n'est pas théorique : la branche 6 est celle des corps de véhicules
maritimes, lacustres et fluviaux, et Baloise publie une page produit *bateau* avec son IPID.
Le registre du CAA fait foi ; **ne jamais dériver un agrément d'une page web.**

La page se décrit elle-même comme le site des deux sociétés à la fois — « www.baloise.lu est le
site Internet des sociétés Baloise Assurances Luxembourg S.A., et Baloise Vie Luxembourg S.A. ».
C'est exactement ce qui rend `carrier: null` obligatoire par défaut ici : la marque est partagée
entre deux porteurs de risque, et seul le document sait lequel il engage. Aucun PDF n'a été
ouvert dans cette passe, donc aucun `carrier` n'est renseigné.

## Verdict robots.txt, hôte par hôte

Trois hôtes ont été rencontrés. Les trois `robots.txt` ont été récupérés **avant toute autre
requête**, et deux d'entre eux ont empêché des requêtes qui auraient sinon eu lieu.

### `www.baloise.lu` — ouvert (`Last-Modified: Fri, 14 Jul 2023 05:56:17 GMT`)

```
# robots.txt for baloise-lu
User-agent: *
Disallow:
```

Trois lignes. Un `Disallow:` **sans valeur** n'interdit rien : c'est la formulation canonique qui
autorise tout le site. Aucun chemin de documents fermé, aucune règle `*.pdf`, aucun agent nommé.
C'est le contraire exact de Foyer, qui avait énuméré ses chemins de documents pour les fermer.

### `kid.baloise.lu` — fermé sur le seul chemin qui contient quelque chose

```
User-agent: *
Disallow: international/
```

**896 documents perdus, et c'est la totalité de ce que cet hôte publie.** Les 896 URL trouvées
sont toutes sous `/international/` : 698 sous `/international/employee-benefit/` et 198 sous
`/international/pension-plan/`. **Aucune n'a été demandée** — seul `robots.txt` a été lu sur cet
hôte.

Le `Disallow` est écrit **sans barre oblique initiale**, ce qui est une valeur malformée au sens
strict de la norme (un chemin d'URL commence toujours par `/`, donc un motif sans `/` ne peut
littéralement rien apparier). Un analyseur littéral en conclurait que rien n'est interdit. Ce
projet retient la lecture d'intention : l'éditeur a un seul répertoire, il l'a nommé, il l'a
fermé. Une faute de frappe dans une interdiction reste une interdiction.

Ce que contiennent ces 896 fichiers, lu depuis les libellés publiés sur les pages qui les
appellent, sans en ouvrir aucun : 414 **KID PRIIPs**, 402 informations **SFDR** (245 art. 8,
142 art. 6, 15 art. 9, 15 art. 10) et 64 **factsheets**, portant sur **364 ISIN distincts**.
Ce sont les fonds sous-jacents de deux contrats en unités de compte — l'*Employee Benefits Plan*
(collectif) et le *Pension Plan* (individuel) — et non des documents de contrat d'assurance.
Suffixes de langue des noms de fichiers : 606 `FR`, 186 `EN`, 102 `DE`, 2 `NL`.

**La perte est donc réelle mais latérale** : elle porte sur de la documentation de fonds, pas sur
un seul document contractuel. Aucune conditions générales ne se trouve derrière ce blocage.

### `www.mybaloise.lu` — fermé intégralement

```
User-agent: *
Disallow: /
```

Le portail client est interdit en entier. Rien n'y a été demandé, et son espace n'a pas été
sondé. À noter pour la comparaison : côté belge, `sources/be/baloise.yml` liste au contraire une
page publique `mybaloise.baloise.be/fr/documenten/all-ipid-eid` comme page de listing. La même
marque, dans deux pays, ouvre son portail d'un côté et le ferme de l'autre.

### `www.caa.lu` — ouvert

```
# @package    vanilla
# @subpackage web
# @author     Loops <evrard@h2a.lu>
# @version    SVN: $Id: robots.txt 1 2013-01-14 10:30:16Z loops $

User-agent: *
Allow: /
```

## Correction au census : `baloise.lu` n'est pas « curl-hostile »

`_meta/lu-market-census.md` classe cet hôte en `plain, curl-hostile` — « 200 to `urllib`,
**406 to `curl`** with the same User-Agent ». **Mesuré le 2026-08-03, c'est l'inverse, et le vrai
discriminant n'est ni curl ni urllib : c'est l'en-tête `Accept`.**

| requête | résultat |
|---|---|
| `curl` + User-Agent personnalisé (envoie `Accept: */*` par défaut) | **200** |
| `urllib` + même User-Agent, **sans** en-tête `Accept` | **406 Not Acceptable** |
| `urllib` + même User-Agent + `Accept: */*` | **200** |

Le serveur refuse une requête sans `Accept`, ce qu'aucun navigateur n'envoie jamais. La leçon du
census français tient toujours — « a curl 4xx is not proof of a block » — mais son illustration
luxembourgeoise est à corriger : il faut lire `plain`, en envoyant un `Accept`.

## Comment le site a été énuméré

Il n'y a **ni sitemap** (`/sitemap.xml`, `/sitemap_index.xml`, `/fr/sitemap.xml` → 404 chacun)
**ni page-bibliothèque**. Chaque document pend de sa page produit. L'énumération est donc un
parcours du graphe de liens publiés, et rien d'autre : aucun identifiant sondé, aucun motif
d'URL balayé.

**490 pages HTML distinctes récupérées**, sur les trois arbres de langue `/fr/`, `/de/`, `/en/`,
en deux passes dont chacune a **vidé sa file d'attente** — l'arbre produits/société (224 pages
demandées, 216 servies) puis l'arbre blog et déclarations de sinistre (295 pages), recouvrement
de 21. Le graphe est clos : il ne reste aucune page connue non visitée.

**25 liens publiés sont morts** (404). Les 25 sont des variantes de casse de pages qui existent
en minuscules et qui ont bien été récupérées (`/fr/particuliers/Mon-assurance-Luxembourg/…` pour
`/mon-assurance-luxembourg/…`, `/de/Privatekunden/…` pour `/de/privatekunden/…`). **Aucun
document n'est perdu de ce fait.**

**Trois liens vers des PDF sont écrits avec un suffixe `.pdf0`**, sur la page allemande des
rapports annuels : `Rapport-Annuel-BVLUX-2022_Web-2.pdf0`, `Rapport-Annuel-BVLUX-2015.pdf0`,
`Rapport-Annuel-BALSA-2015.pdf0`. Les deux rapports 2015 n'apparaissent nulle part ailleurs, donc
ils sont inatteignables par un lien correct. L'URL corrigée n'a **pas** été tentée : retirer un
caractère pour deviner une cible est déjà du sondage d'espace d'URL.

## Inventaire : 268 documents sur `www.baloise.lu`

Comptés, pas estimés. **Les 268 ont répondu 200 à une requête HEAD**, sans exception.

| type | n |
|---|---|
| fiche de fonds / factsheet | 70 |
| **IPID (document d'information sur le produit d'assurance)** | **34** |
| communiqué de presse | 28 |
| formulaire de déclaration de sinistre | 21 |
| SFCR (rapport prudentiel) | 20 |
| rapport annuel | 20 |
| brochure / dépliant / flyer | 20 |
| KID ou fiche de fonds interne | 17 |
| KID PRIIPs de contrat | 8 |
| fiche d'information financière (vie) | 5 |
| information fonds art. 10 SFDR | 5 |
| politique d'investissement responsable | 5 |
| guide ESG | 3 |
| tableau d'avantage fiscal | 3 |
| checklist publiée sur le blog | 3 |
| brochure corporate | 2 |
| convention « droit à l'oubli » | 1 |
| politique de gestion des réclamations | 1 |
| notice RGPD | 1 |
| divers | 1 |
| **total** | **268** |

Langues, mesurées sur le chemin d'URL de l'éditeur : les 34 IPID se répartissent en **29 fr,
3 de, 2 en**. L'ensemble du site est trilingue ; **sa bibliothèque contractuelle ne l'est pas.**

## Le chiffre qui compte : zéro conditions générales

**Aucune conditions générales n'est publiée. Zéro sur 268, et zéro sur 490 pages.**

La vérification a porté sur le corps de texte des **490 pages HTML**, hors ligne, avec le motif
`conditions? g[ée]n[ée]rales?` · `allgemeine (versicherungs)?bedingungen` · `versicherungs-
bedingungen` · `vertragsbedingungen` · `general (terms|conditions)` · `policy wording`.

**33 pages contiennent une de ces chaînes. Aucune des 33 n'est un lien vers un document.** Elles
se répartissent en exactement deux familles :

1. **Les mentions légales**, pour les « Conditions générales **d'utilisation du site Internet**
   www.baloise.lu ». Ce sont les CGU du site, pas un contrat d'assurance.
2. **32 pages éditoriales** — 30 articles de blog et les 2 pages produit *assurance voyage* FR et
   EN — qui **renvoient le lecteur vers des conditions générales que le site ne publie pas.**

La seconde famille est le résultat, et il vaut d'être cité. Le blog explique aux lecteurs que
« les conditions générales sont longues », leur recommande de « consult[er] les conditions
générales de votre contrat à la rubrique "événements naturels" », et va jusqu'à écrire, sur la
page anglaise consacrée à l'annulation de voyage, que la liste exacte des motifs couverts
« can be found exclusively in the Travel General Terms and Conditions and the table of guarantees
of the Baloise contract ». **Le document ainsi désigné comme la seule source n'existe nulle part
sur le site.**

C'est la troisième mesure luxembourgeoise concordante, et la seule des trois où rien ne bloque :

| assureur | vraies CG | corpus | cause |
|---|---|---|---|
| Foyer | **0** / 800 lignes | IPID + DIC PRIIPs | ne publie pas (et bloque par ailleurs) |
| lalux | **4** / 304 | IPID | ne publie pas, sauf RC construction B2B |
| **Baloise** | **0** / 268 | IPID | **ne publie pas — et n'a rien fermé** |

L'IPID est obligatoire, les conditions générales ne le sont pas. Le Luxembourg transpose la même
directive que la France et produit le même partage.

## Les 34 IPID, et leur âge

C'est le seul type contractuel normalisé publié. Éditions lues dans les noms de fichiers de
l'éditeur :

| édition | n |
|---|---|
| 10-18 (octobre 2018) | 25 |
| 01-19 | 3 |
| 02-19 | 2 |
| 02-22 | 1 |
| 11-23 | 1 |
| aucune date dans le nom | 2 |

**Trente des trente-quatre datent de 2018-2019**, c'est-à-dire du lot déposé à l'entrée en
vigueur de la DDA. La règle 8 s'applique : capturer `edition_date` et ne pas présenter ces pièces
comme le contrat courant sans vérifier qu'une édition plus récente existe hors bibliothèque.
C'est la même alerte de fraîcheur que le census a déjà posée sur AXA Luxembourg.

## Pièges mesurés ici

1. **Un seul fichier français sert les trois arbres de langue.** Les pages allemandes et
   anglaises de la RC professionnelle, des dégâts matériels, du transport, de la construction,
   des flottes, du bateau, de la RC vie privée, des accidents et du voyage pointent toutes vers
   le **même** PDF `…-FR-LU-….pdf`. Il n'existe que 3 IPID allemands (Business, Drive, Home) et
   2 anglais (Business, Drive) sur 34. Un pipeline qui déduit la langue de l'arbre de la page se
   trompe **trois fois sur quatre**. La règle « ne jamais compléter une langue depuis une autre »
   s'applique ici dans l'autre sens : il faut se garder d'inventer trois documents là où
   l'éditeur en sert un.

2. **Les éditions divergent entre langues du même produit.** *Home* : le fichier FR est en
   édition 11-23, le fichier DE en édition 01-19 — presque cinq ans d'écart. *Drive* : les
   fichiers DE et EN sont en 02-19, le fichier FR n'a aucune date dans son nom et est
   manifestement plus récent. Ce ne sont pas des variantes parallèles, ce sont des éditions
   différentes du même produit.

3. **L'IPID Drive EST l'IPID moto.** Les pages `moto-scooter.html` (FR), `moto.html` (DE),
   `motorbike.html` (EN) et `assurance-auto-electrique.html` publient toutes l'IPID auto Drive.
   Aucun document deux-roues distinct n'existe. **C'est la deuxième confirmation indépendante**,
   après Foyer, du motif corrigé dans `_country.yml` sous la branche `moto` : la branche tient
   par l'obligation de l'art. 2 de la loi du 16 avril 2003, pas par une pratique commerciale de
   produit séparé.

4. **`IPID-RC10-FR-LU-10-18.pdf` est intitulé simplement « IPID RC » par l'éditeur.** Le « 10 »
   du nom de fichier n'est pas élucidé : code produit, ou responsabilité **décennale** — auquel
   cas le document bascule de `rc-professionnelle` vers `construction`. Classé sur son contexte
   de publication, à trancher à l'extraction. C'est précisément le piège « les intitulés de
   rubrique sont peu fiables ».

5. **L'éditeur écrit « IPID RCSM SD » là où le fichier s'appelle `IPID-RCMS-SD`.** Les lettres
   sont transposées dans le libellé du site. Le nom de fichier fait foi.

6. **Le chemin dans le DAM n'est pas un segment de clientèle.** `IPID-BUSINESS-UNTERNEHMEN-DE` et
   `IPID-Business-EN` sont rangés sous `/1890/particulier/documents/` alors que ce sont des
   produits entreprise publiés sur les pages *Geschäftskunden* / *professionals*. Le seul IPID
   réellement rangé sous `/professionnel/` est la version française du même produit, plus celui
   des flottes.

7. **« IPID Travel agent » n'est pas « IPID Travel ».** Le premier est la RC d'une agence de
   voyages (page RC professionnelle), le second l'assurance voyage des particuliers. Deux
   branches différentes derrière deux libellés à un mot d'écart.

8. **`ipid-flottes.pdf` pèse 100 kB** là où tous les IPID de la même génération font ~700 kB.
   À vérifier à l'extraction : le fichier est peut-être tronqué, ou simplement produit par une
   autre chaîne.

## Produits vendus sans le moindre document publié

Le catalogue de vente est plus large que la bibliothèque. Ces pages produit existent, décrivent
une couverture, et **ne publient aucun document, d'aucun type** :

- **InsureMyBike** (`/fr/particuliers/mon-assurance-luxembourg/insure-my-bike.html`) — vol et
  dommages des vélos neufs et e-bikes, plafond 15 000 €, couverture mondiale, sans franchise,
  distribué exclusivement chez des magasins partenaires. Ni IPID, ni conditions générales, ni
  brochure.
- **Assurance décès** (`/…/assurance-vie-epargne-prevoyance/assurance-deces.html`) et sa version
  allemande *Risikolebensversicherung* — capital décès, garanties complémentaires incapacité /
  hospitalisation / accident, déduction art. 111 L.I.R. Aucun document. Un produit de prévoyance
  pur n'appelle ni IPID (réservé au non-vie) ni KID PRIIPs (réservé aux produits
  d'investissement), donc l'absence est ici cohérente avec la réglementation — la relever quand
  même, parce qu'elle rend la branche `prevoyance` indocumentable chez cet assureur.
- **GoodStart** (appartement) — la page FR et la page EN ne publient rien ; seule la page DE
  affiche un document, et c'est l'IPID *Home*, celui d'un autre produit.
- **Retraite** (`retraite-luxembourg.html`, `epargne-prevoyance-retraite.html`), **Pour vous**,
  **RC pro accidents** côté professionnels, et les pages d'assistance, prévention et déclaration
  de sinistre côté particuliers FR.

**Une correction pour `sources/lu/_country.yml`.** Le manifeste justifie l'absence de branche
`velo` ainsi : « No Luxembourg bicycle product was observed (Foyer and lalux retail ranges
checked 2026-08-02, zero hits). France's `velo` was added from evidence; adding one here would be
adding it from theory. » **Un produit vélo luxembourgeois est désormais observé** : InsureMyBike,
nommé, tarifé et distribué. Le motif tiré de l'absence d'observation ne tient donc plus tel quel.
La conclusion pratique, elle, ne change pas : ce produit ne publie **aucun** document, donc
aucune page produit ne peut être bâtie et la branche resterait vide. La correction à porter est
sur le motif — « aucun document publié » — et non sur la décision. Elle n'a pas été appliquée
ici : ce fichier de découverte ne modifie pas le manifeste pays.

## `sources/lu/baloise.yml` — 34 IPID

Le fichier existe : la bibliothèque est atteignable, ouverte, et vérifiée document par document.
Il calque `sources/lu/lalux.yml` et n'ingère, comme lui, que les IPID et les conditions générales
— soit ici 34 IPID et rien d'autre.

Répartition sur les branches du Luxembourg :

| branche | n | | branche | n |
|---|---|---|---|---|
| `rc-professionnelle` | 14 | | `voyage` | 1 |
| `multirisque-professionnelle` | 7 | | `solde-restant-du` | 1 |
| `auto` | 4 | | `construction` | 1 |
| `habitation` | 2 | | `rc-familiale` | 1 |
| `autres` | 2 | | `accidents` | 1 |

`autres` porte l'IPID *RC Bateau* et l'IPID *Transport (CMR)* : `_country.yml` déclare
explicitement l'absence de `navigation` et de `transport`, et cette découverte ne crée pas de
branche. À noter que l'IPID Bateau relève de la branche 6 du registre — celle-là même que les
mentions légales du site omettent.

**Le livre vie tient en un seul document ingérable** : l'IPID *Solde restant dû*. Les autres
produits vie — Life Plan, Kid's Plan, Switch Plan, Pension Plan — n'ont que des KID PRIIPs et des
fiches d'information financière, non repris, plus les 896 documents de fonds bloqués par robots.
Rien pour `assurance-vie`, `prevoyance` ni `retraite`.

## Ce qui n'a pas pu être atteint

| quoi | combien | pourquoi |
|---|---|---|
| documents de fonds sur `kid.baloise.lu` | **896** | `Disallow: international/` — respecté, aucune requête |
| portail client `www.mybaloise.lu` | inconnu | `Disallow: /` — respecté, aucune requête |
| rapports annuels BVLUX 2015 et BALSA 2015 | 2 | seuls liens publiés écrits en `.pdf0` ; URL non devinée |
| conditions générales | **n'existent pas** | non publiées, et non bloquées |

Rien d'autre. Les 268 documents de `www.baloise.lu` ont tous répondu 200, les deux files de
parcours ont été vidées, et aucun contenu n'a été rendu inaccessible par un WAF, un rendu client
ou une limitation de débit.

Aucun formulaire prérempli, spécimen de contrat nominatif ou identifiant client n'a été
rencontré — le seul espace susceptible d'en contenir est le portail `mybaloise`, qui est fermé
par `robots.txt` et n'a pas été approché.
