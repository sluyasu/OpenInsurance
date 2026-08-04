# foyer-global-health — Foyer Global Health S.A. (ex-Globality S.A.)

website: globalhealth.insurance
fetch: plain
status: enumerated
lang: en, fr, de, es
enumerated: 2026-08-04

**Vingt-deux conditions générales, en clair, sans `robots.txt` à respecter parce qu'il n'y en a
pas. C'est plus du double de tout ce que le corpus luxembourgeois compte aujourd'hui — treize CG
sur 160 documents — et c'est la même maison mère que celle qui n'en publie aucune. Le contraste
n'est pas un accident de site : `foyer.lu` et `globalhealth.insurance` sont deux hôtes, deux
politiques, deux métiers.**

## L'entité agréée

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-04,
`Last-Modified: Tue, 04 Aug 2026 01:00:12 GMT`, 200 `text/csv`, sans clé ni cookie ni compte.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv`

```
"Foyer Global Health (222100M5YXWXWJ8ING43)","12, rue Léon Laval, 3372 Leudelange","Marie-Hélène MASSARD, Jeroen VAN DE VELDE","(+352) 437 434 243","","1, 2, 13, 16, 18"
```

**Société luxembourgeoise agréée, pas une succursale étrangère** : elle figure dans la liste des
assureurs luxembourgeois non-vie. Cinq branches de l'ANNEXE I — **1** (accidents), **2**
(maladie), **13** (RC générale), **16** (pertes pécuniaires diverses), **18** (assistance) —
c'est-à-dire l'attelage classique d'un livre santé-expatriés : le soin, la responsabilité, le
remboursement de frais et l'assistance/rapatriement.

Deux détails que le registre ne donne pas et que les documents donnent :

- **Le CAA l'inscrit sans forme juridique** (« Foyer Global Health »), là où il écrit
  « FOYER ASSURANCES S.A. » ou « DKV LUXEMBOURG S.A. » pour les autres. Ses propres contrats
  impriment **`Foyer Global Health S.A.`**, société anonyme.
- **Le RCS**, que le CAA ne publie jamais : `R.C.S. Luxembourg **B 134.471**`, TVA `LU22284578`,
  imprimés en pied de page des conditions générales et en en-tête de chaque IPID. L'identifiant
  entre parenthèses du registre est un LEI (`222100M5YXWXWJ8ING43`), pas un RCS.

### Ex-Globality S.A., et ce sont les documents qui le prouvent

Le corpus contient les deux états civils de la même société, avec le même RCS :

| Document | Entité imprimée | Siège imprimé | RCS |
|---|---|---|---|
| `Globality_EcoGenio_GCI_ES_131222` | **Globality S.A.** | 1A, rue Gabriel Lippmann, L-5365 Munsbach | B 134.471 |
| les 21 autres CG | **Foyer Global Health S.A.** | 12, rue Léon Laval, L-3372 Leudelange | B 134.471 |

Même numéro d'immatriculation, deux noms et deux sièges : c'est une **même entité renommée et
déménagée au siège de Foyer**, pas une acquisition de portefeuille. Le communiqué
`Foyer S.A. acquiert Globality S.A.` (13/03/2023) publié sur `groupe.foyer.lu` date l'opération.

L'adresse de l'autorité de contrôle imprimée dans les documents date également les rédactions :
les plus anciennes écrivent « Commissariat aux Assurances, **7, boulevard Joseph II, L-1840** », les
récentes « **11, rue Robert Stumper, L-2557** ».

Le domaine historique **`foyerglobalhealth.com`** est retiré : `/robots.txt` y répond **410 Gone**.
Cinq liens du site actuel y pointent encore ; deux « PDF » y répondent 200 `text/html` (169 octets,
donc pas des PDF), trois sont des communiqués de presse.

## Verdict robots.txt

```
https://globalhealth.insurance/robots.txt  →  404 Not Found (nginx)
https://www.globalhealth.insurance/robots.txt  →  301 vers l'apex, puis 404
```

**Il n'y a pas de `robots.txt`. Rien n'est interdit.** C'est le verdict le plus simple du corpus
luxembourgeois, et il ne se déduisait pas de `foyer.lu` : ce sont deux hôtes distincts
(`globalhealth.insurance` → `54.216.50.99` / `52.210.147.107`, derrière un ELB AWS ;
`www.foyer.lu` → `195.46.232.215`), et la politique restrictive de la maison mère — qui ferme
`/fr|/en|/de/basedoc_file/*` et `/mydoc/*` — **ne s'applique pas ici**. Vérifié séparément pour
chacun des trois autres agréments du groupe : voir [foyer.md](foyer.md),
[foyer-arag.md](foyer-arag.md) et [foyer-vie.md](foyer-vie.md).

L'énumération est venue de `https://globalhealth.insurance/sitemap.xml`, index Yoast/WordPress qui
déclare cinq sous-sitemaps :

| Sous-sitemap | URL | Récupérées |
|---|---:|---:|
| `page-sitemap.xml` | 110 | 110 |
| `post-sitemap.xml` | 699 | 699 |
| `destinationcpt-sitemap.xml` | 700 | 700 |
| `testimonialcpt-sitemap.xml` | 26 | 26 |
| `category-sitemap.xml` | 22 | 22 |
| **Total** | **1 557** | **1 557 — zéro échec** |

**Aucun sondage d'URL n'a été nécessaire et aucun n'a été fait.**

**Les 1 447 pages éditoriales n'apportent rien.** Elles contiennent 27 liens PDF, dont 24 vers des
sites tiers cités dans des articles de blog (Eurostat, DREES, INSEAD, World Happiness Report…) et 3
communiqués sur le domaine retiré. **Zéro document du domaine en plus.** Toute la bibliothèque
tient sur les 110 pages du `page-sitemap`.

## Inventaire

**194 URL PDF distinctes** du domaine extraites des liens publiés. Vérifiées **une par une en
HEAD** :

- **191 répondent 200 `application/pdf`** (93 Mo au total) ;
- **3 répondent 404** — et la raison est instructive : `Special_Conditions_Epion_Care_FR_…`,
  `…_Epion_FlexCare_FR_…`, `…_Epion_TotalCare_FR_…`. Les mêmes fichiers écrits `EPION` en
  capitales répondent 200. **Le serveur est sensible à la casse et le site publie les deux
  graphies.** Compter les liens publiés sans vérifier en HEAD aurait produit trois documents
  fantômes.

Sur les 191 vivantes, **190 documents distincts** : `Special_Conditions_EPION_TotalCare_FR_Layout_20250522.pdf`
est servi sous deux URL (`/uploads/2025/05/` et `/uploads/2026/03/`), sha256 identique.

| Type | en | fr | de | es | Total |
|---|---:|---:|---:|---:|---:|
| **Conditions générales** | 7 | 5 | 6 | 4 | **22** |
| Conditions spéciales | 7 | 16 | 7 | 2 | **32** |
| IPID | 18 | 14 | 15 | 18 | **65** |
| Formulaires de souscription | 5 | 4 | 5 | 4 | **18** |
| Tableaux de garanties (PB) | 6 | 2 | 5 | 4 | **17** |
| Marketing (brochures, flyers, affiches) | 4 | 4 | 4 | 4 | **16** |
| RGPD | 3 | 3 | 3 | | **9** |
| Tables of benefits (ToB) | 1 | 1 | 1 | 1 | **4** |
| Listes de juridictions sous surveillance | 1 | 1 | 1 | 1 | **4** |
| Étendue des prestations | 1 | 1 | 1 | | **3** |
| Formulaire de sinistre | 1 | | | | **1** |
| **Total** | **54** | **51** | **48** | **38** | **191** |

L'**espagnol** est ici une vraie langue de document (38 fichiers), ce qu'aucun autre assureur
luxembourgeois du corpus ne pratique. Il n'y a en revanche **aucun document en luxembourgeois ni en
portugais** — cohérent avec un livre expatriés vendu hors du Grand-Duché.

### Vingt-deux conditions générales

| Produit | Langues | Pages | Référence imprimée |
|---|---|---:|---|
| Journey | en, fr, de, es | 24–27 | `GH_JOY_OO_GT_25.11` |
| CoGenio | en, fr ×2, de, es | 41–44 | `CG GCI 09.17/2` |
| YouGenio World | en, fr, de, es | 46–49 | `YGW GCI 14.02/5` |
| Foyer Global Health (socle) | en, fr, de | 18–19 | `FGHGCIV3 / 03.2024` |
| Xtend | en, de | 23–26 | `GCI 10.24` |
| YouGenio Germany | en, de | 43–44 | `YG GER GCI 13.02/5` |
| Corporate Travel | en | 44 | `CTI GCI 10.24` |
| EcoGenio | es | 45 | `ECG GCI 23.01` |

Ce sont de vrais contrats, pas des résumés : de 18 à 49 pages, structurés en « Base contractuelle
/ Cadre de l'assurance / Prestations / Exclusions ». Le document dit lui-même de quoi la police est
faite :

> « Les droits et obligations réciproques […] sont régis par les documents ci-après […] : le
> Formulaire de Souscription ; le Certificat d'Assurance ; les **Conditions Générales d'Assurance**
> (le présent document) ; les **Conditions Spéciales** ; les **Conditions Particulières** ; les
> Glossaires »

Les 32 **conditions spéciales** (21 à 29 pages chacune) sont donc, elles aussi, du contrat — elles
portent la portée, les prestations et les exclusions par formule. Le chiffre à retenir pour le
corpus reste **22 conditions générales proprement dites** ; l'ensemble contractuel publié fait
**54 documents**.

**Le porteur est nommé, avec sa forme juridique, son siège et son RCS** : 21 des 22 CG impriment
« Foyer Global Health S.A., 12, rue Léon Laval, L-3372 Leudelange » ; la 22e imprime
« Globality S.A. ». Les IPID ouvrent sur « Société : Foyer Global Health S.A., R.C.S. Luxembourg
B 134.471 ». C'est le comportement de DKV, l'inverse exact de lalux (4 documents sur 90).

### Deux fichiers qui ne diffèrent que d'un caractère

`Globality_CoGenio_GCI_FR_V18_0224.pdf` et `Globality_CoGenio_GCI_FR_V18_0224-3-1.pdf` ont des
sha256 et des tailles distincts (595 497 et 603 191 octets) — donc pas un fichier servi deux fois.
Mais leur texte extrait diffère d'**un seul caractère** sur 129 738 octets : un astérisque devenu
double, ligne 947. Ce n'est pas une nouvelle édition, c'est une correction typographique
re-téléversée. **22 fichiers, 21 rédactions.**

## Les pièges mesurés

### 1. Le droit applicable change à l'intérieur de la même bibliothèque

C'est le piège le plus lourd de conséquences, et il ne se voit ni dans le nom de fichier, ni dans
l'arborescence, ni dans la marque.

> Conditions générales YouGenio World (fr) : « La police d'assurance est régie par le **droit
> luxembourgeois** dans la mesure où aucune réglementation nationale ne serait incompatible […] »

> Conditions spéciales VDP Liberté (fr) : « Le contrat est régi par la **loi française**. »

Les **huit** conditions spéciales des gammes **EPION**, **GTE** et **VDP** sont des contrats de
**droit français**, pour des **résidents en France** — l'une d'elles porte même un chapitre
« CONDITIONS ADMINISTRATIVES RÉSIDENTS **en France** ». Elles sont publiées sur le même site, dans
les quatre arbres de langue, à côté de contrats luxembourgeois.

**Elles sont exclues de `sources/lu/foyer-global-health.yml`**, pour la raison que
`sources/lu/_country.yml` énonce déjà à propos des véhicules vie transfrontaliers : une page produit
`lu` construite dessus documenterait une histoire de consommateur français depuis une adresse
luxembourgeoise. Les 22 conditions générales, elles, disent toutes « Luxembourg law » / « droit
luxembourgeois » et sont retenues.

### 2. La langue officielle du contrat est l'anglais — les autres versions sont des traductions

> « La langue officielle de la police d'assurance est l'**anglais**. Sauf accord contraire […],
> l'anglais est la langue de correspondance. **La version anglaise prévaut** sur toute autre. »
> — conditions générales YouGenio World, version française

Le champ `lang:` du fichier de sources décrit donc **la langue du fichier, pas celle du contrat**.
Une divergence entre la version française et la version anglaise n'est pas une erreur d'extraction :
c'est une traduction non contractuelle face à un original. À ne jamais présenter comme deux
variantes équivalentes.

Les langues déclarées ont été **vérifiées sur le contenu**, pas sur le nom de fichier : dix
documents tirés au sort ont été ouverts et leur langue mesurée. Dix sur dix conformes — le seul cas
douteux, `FGH-Special-Conditions-EN_ESSENTIAL`, l'était parce que sa table des matières à points de
conduite trompe un compteur de mots ; le document est bien en anglais.

### 3. Les fichiers « -combined » sont des lots, et leur nom ment sur leur contenu

Ce piège est nouveau — ce n'est ni la date fausse de DKV, ni le fichier partagé de Baloise.

| Fichier | Pages | Contient réellement |
|---|---:|---|
| `IPID_CoGenio_Classic_EN_0224-combined.pdf` | 6 | CoGenio **Classic + Plus + Top** |
| `IPID_GH_Journey_Short_DE-combined.pdf` | 10 | Journey **Short + Basic + Advanced + Extensive + Premium** |
| `IPID_YouGenio_Germany_Plus_EN_0224-combined.pdf` | 4 | Germany **Plus + Top** |

Un fichier nommé d'après **un** palier en contient **trois à cinq**. L'extraire sous le nom du
premier attribuerait à *Classic* les garanties de *Top*. **Les neuf fichiers `-combined` /
`-copy` sont exclus** du fichier de sources ; les 56 IPID par palier les couvrent tous, à une
exception près, signalée plus bas.

### 4. Aucune date d'édition fiable pour 19 des 22 conditions générales

Seules les trois `FGH-GCI-*` impriment une édition lisible — **`FGHGCIV3 / 03.2024`** — et leur nom
de fichier annonce `20240909`. **Six mois d'écart**, dans le sens du piège DKV.

Les dix-neuf autres n'impriment **aucune date**, seulement un code de pied de page, selon au moins
trois conventions incompatibles entre elles :

- `CG GCI **09.17**/2` (CoGenio) — alors que le nom de fichier dit `V18_0224` ;
- `YGW GCI **14.02**/5` (YouGenio World) — qui se lit plutôt « version 14 » que « septembre 17 » ;
- `GH_JOY_OO_GT_**25.11**` (Journey) — porté à l'identique par quatre fichiers dont deux nommés 2026 ;
- `GCI **10.24**` — porté à l'identique par `Globality_Xtend_GCI_EN_**0924**.pdf` **et** par
  `Globality_Xtend_GCI_DE_**300125**.pdf`.

Sans la clé de l'éditeur, ces codes ne sont pas des dates. **Règle 8 : `edition_date` doit rester
nul plutôt qu'être tiré du nom de fichier.**

## Ce que l'ingestion apporterait

Le corpus luxembourgeois compte aujourd'hui **160 documents dont treize vraies conditions
générales** — quatre chez lalux, neuf chez DKV. Foyer en publie zéro sur huit cents, Baloise zéro
sur 268, AXA plus de trois cents mais toutes fermées par son `robots.txt`.

**Foyer Global Health en publie vingt-deux**, plus 32 conditions spéciales et 65 IPID. Le fichier
`sources/lu/foyer-global-health.yml` en retient **101** :

| Retenu | Nombre |
|---|---:|
| Conditions générales (les 22) | 22 |
| Conditions spéciales de droit luxembourgeois | 23 |
| IPID par palier | 56 |
| **Total** | **101** |

et laisse de côté, en le disant : les 8 conditions spéciales de droit français, les 9 fichiers
« combined », et les 82 documents non contractuels (17 tableaux de garanties, 18 formulaires de
souscription, 16 documents marketing, 9 RGPD, 4 ToB, 4 listes de juridictions, 3 étendues de
prestations, 1 formulaire de sinistre) — même découpe que `lalux.yml`, `baloise.yml` et `dkv.yml`.

**Cinq gammes y seraient documentées à la fois par leur IPID et par leur contrat** — Journey,
CoGenio, EcoGenio, YouGenio World, YouGenio Germany — ce qui n'existe encore pour aucun produit
luxembourgeois du corpus. La couverture n'est toutefois pas totale : **Xtend, Corporate Travel et
le socle Essential / Exclusive / Special ont des conditions générales mais aucun IPID publié**, et
seule la gamme **EU Health** a un IPID sans conditions générales propres (elle s'appuie sur le socle
`FGH-GCI`). Lacunes constatées côté éditeur, pas côté découverte.

### Les `listing_pages`, et pourquoi celles-là

Les quatre pages `/conditions/`, `/fr/conditions-generales/`, `/de/geschaftsbedingungen/`,
`/es/condiciones/` portent **36 documents chacune, mais pas les mêmes 36** : chaque arbre de langue
sert une sélection adaptée, et leur union fait **93 documents dont 75 contractuels** (21 CG sur 22,
26 IPID, 28 conditions spéciales). Douze documents sont communs aux quatre — dont les **huit
conditions spéciales françaises**, servies dans tous les arbres de langue. La leçon Baloise tient
donc ici aussi : **l'arborescence de langue ne dit ni la langue ni le marché du document.**

`discover.py` ré-ajoute au yml tout ce qu'il trouve sur une page de listing. Ces quatre pages
ramèneront donc aussi 4 tableaux de garanties, 4 formulaires, 4 listes de sanctions, 3 RGPD, 3
étendues de prestations **et les 8 conditions spéciales françaises volontairement exclues** — à
retrier à chaque passage. C'est le prix, assumé, du choix le plus étroit disponible.

Ce qui a été **écarté** comme page de listing :
`/professionals-and-brokers/partner-document-centre/` et ses trois jumelles (20 documents dont 3
marketing), `/individuals/explore-our-plans/` et ses jumelles (10 documents dont du marketing), et
bien sûr les sitemaps XML — qui ont servi à énumérer, ne sont pas des pages de listing, et que
`discover.py` rendrait avec Playwright.

## Ce qui n'a pas pu être atteint

| Objet | État |
|---|---|
| `Special_Conditions_Epion_{Care,FlexCare,TotalCare}_FR` | **404** — variante de casse ; les fichiers en `EPION` répondent 200, rien de perdu |
| 2 « PDF » sur `foyerglobalhealth.com` | 200 `text/html`, 169 octets — pages de redirection du domaine retiré |
| IPID **CoGenio Top en français** | **n'existe pas** en fichier autonome ; il n'est publié que dans le lot `IPID_CoGenio_FR_0224-combined.pdf`, exclu pour la raison ci-dessus. Lacune assumée, à combler en découpant le lot si le besoin apparaît |
| Édition de 19 des 22 CG | non imprimée ; voir piège 4 |
| `QRT public 2025 de Foyer Global Health` | servi depuis `www.foyer.lu/fr/mydoc/WebSites-Documentsgroupe-372`, chemin fermé — et prudentiel, donc hors périmètre |

## Note d'attribution pays, à trancher avant la construction des pages produit

La totalité du livre est de la **santé internationale pour expatriés** — les IPID le disent
littéralement : « Assurance médicale privée complète pour les expatriés » — à une exception près,
**Corporate Travel**, un contrat de groupe de voyages d'affaires, classé `voyage`. **YouGenio
Germany** vise explicitement l'Allemagne (43 occurrences de « Germany » dans ses conditions
générales).

**Aucun de ces produits n'est un produit de détail luxembourgeois domestique.** Ce qui les rattache
au Luxembourg, c'est l'agrément du CAA et le droit applicable choisi dans le contrat, pas la
résidence de l'assuré. La question posée par `sources/lu/_country.yml` à propos des véhicules vie
transfrontaliers se pose ici sous une forme plus douce — le droit luxembourgeois s'applique
vraiment — mais elle se pose : une page produit `lu` doit dire à qui le produit est vendu, ou elle
décrira le Grand-Duché avec le contrat de quelqu'un d'autre.
