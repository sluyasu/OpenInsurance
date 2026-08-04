# dkv — DKV Luxembourg (DKV LUXEMBOURG S.A.)

website: dkv.lu
fetch: plain
status: enumerated
lang: fr, de, en, pt, lu
enumerated: 2026-08-03

## L'entité agréée

Source : registre du CAA, export CSV nocturne, récupéré le 2026-08-03,
`Last-Modified: Mon, 03 Aug 2026 01:00:12 GMT`, 200 `text/csv`, sans clé ni cookie ni compte.

`https://www.caa.lu/uploads/documents/files/csv/AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv`

```
"DKV LUXEMBOURG S.A. (529900AO3Z5MARFY0W76)","11-13, rue Jean Fischbach, 3372 Leudelange","Stefan PELGER","(+352) 426464-1","42 64 64-250","2"
```

**Une seule branche : `2`, Maladie** (ANNEXE I de la LSA). C'est le seul assureur non-vie
luxembourgeois de cette liste à ne détenir qu'une branche unique en dehors de FOYER-ARAG
(branche 17). L'entité est **absente de la liste vie** (`AssurancesDirectes_AssureursLuxembourgeoisVie.csv`,
vérifié : aucune occurrence de `DKV`), ce qui est attendu — le principe de spécialisation
luxembourgeois interdit le cumul.

L'identifiant entre parenthèses est un **LEI** (`529900AO3Z5MARFY0W76`, 20 caractères,
ISO 17442), pas un RCS. Le registre du CAA ne publie pas de RCS.

**Cela ne veut pas dire que l'entité n'en a pas** — précision ajoutée après lecture des documents,
parce que la phrase ci-dessus pourrait se lire ainsi. Les conditions générales impriment
`R.C. Luxembourg, B 45 762` et la forme `Société Anonyme`, repris en toutes lettres par les CGA
BUSINESS TRAVEL : « immatriculée au R.C.S. Luxembourg B 45762 ». Le registre du superviseur et le
registre de commerce sont deux sources différentes, et **c'est le document qui donne le RCS**.

## DKV n'est pas un partenaire de lalux : c'est une société du même groupe

C'est le document lui-même qui le dit, et cela corrige la formulation du recensement
(« distribué par le réseau d'agences lalux »). Les conditions générales TRAVEL conditionnent
l'éligibilité à la qualité de client :

> « d'au moins l'une des trois sociétés du Groupe LALUX (LA LUXEMBOURGEOISE Société Anonyme
> d'Assurances, LA LUXEMBOURGEOISE-VIE Société Anonyme d'Assurances ou DKV Luxembourg S.A.) »

**Trois sociétés, un groupe, et la spécialisation luxembourgeoise répartie entre elles** : la
non-vie, la vie, et la maladie. Cela explique matériellement ce que le corpus avait déjà mesuré
sans l'expliquer — deux documents publiés dans la bibliothèque **lalux** nomment `DKV Luxembourg
S.A.` comme porteur et ne prononcent jamais « lalux ». Ils n'étaient pas mal rangés : ils sont
d'une société sœur.

Un document du présent inventaire est d'ailleurs servi depuis `www.lalux.lu` et non
`www.dkv.lu` — les deux bibliothèques se recouvrent.

## Verdict robots.txt

`https://www.dkv.lu/robots.txt`, 200, 433 octets. `dkv.lu` redirige vers `www.dkv.lu` et sert le
même fichier. Une seule directive de groupe :

```
User-agent: *
Disallow: sdk/*
Disallow: /typo3/
```

**Rien n'est fermé côté documents.** `/typo3/` est le back-office du CMS, `sdk/*` un chemin
d'outillage. Les documents vivent sous `/fileadmin/mediatheque/`, hors de toute interdiction.

Le fichier déclare en outre **cinq sitemaps, un par langue** — `fr`, `de`, `en`, `pt`, `lu` — ce qui
a servi de source d'énumération : aucun sondage d'URL n'a été nécessaire.

## Inventaire

**477 pages distinctes** déclarées par les cinq sitemaps (96 fr, 96 de, 96 en, 96 pt, 93 lu), toutes
récupérées, **zéro échec**. Les liens `.pdf` en ont été extraits : **61 URL distinctes**, dont une
vers `etsi.org` (une norme d'accessibilité, écartée comme hors sujet).

**Les soixante restantes répondent toutes `200 application/pdf`.** Vérifié une par une en HEAD.

| Type | Documents |
|---|---|
| **Conditions générales** | **9** |
| IPID | 27 |
| Infographies | 10 |
| Dépliants | 8 |
| RGPD / conformité | 3 |
| Brochures | 2 |
| Formulaire | 1 |
| Divers | 1 |

### Neuf conditions générales — plus du double de tout le corpus luxembourgeois

Au moment de cette passe, le corpus luxembourgeois compte **124 documents dont quatre seulement sont
de vraies conditions générales**. Foyer en publie zéro sur huit cents documents, Baloise zéro sur
268, AXA plus de trois cents mais toutes fermées par son `robots.txt`.

DKV en publie **neuf**, en clair — et la neuvième n'est pas là où on la chercherait :
`DKV_EASY_HEALTH_AVB_CGA_GCI__09_25_Ansicht.pdf` est rangée dans `/Divers/`, pas dans `/CG/`, tout
en portant le même motif trilingue `AVB/CGA/GCI` que les deux gros documents. **Le chemin ne dit
donc pas le type** : un classement par dossier l'aurait ratée, et c'est la page `/documents/cg` qui
la publie qui l'a fait remonter.


| Fichier | Pages | Édition imprimée |
|---|---|---|
| `DKV_KK_AVB_CGA_GCI_01_21_Ansicht.pdf` | 32 | aucune sous forme `MM\|AAAA` |
| `DKV_KT_AVB_CGA_GCI_12_15_Ansicht.pdf` | 28 | aucune sous forme `MM\|AAAA` |
| `CG_TRAVEL_{FR,DE,EN}_03_2025.pdf` | 5 | **03\|2025** |
| `CGA_BUSINESS_TRAVEL_2025_{FR,DE,EN}.pdf` | 4 | **04\|2017** |

**Et le porteur est nommé, avec sa forme juridique et son siège** : « DKV Luxembourg S.A, Société
Anonyme d'Assurances, sise à L-3372 ». C'est l'inverse exact de lalux, où quatre documents sur
quatre-vingt-dix nomment le porteur.

### Deux pièges mesurés, l'un et l'autre inverses de ceux déjà connus

**Le nom de fichier ment sur l'édition, de huit ans.** `CGA_BUSINESS_TRAVEL_2025_FR.pdf` imprime
`CGA BUSINESS TRAVEL 04|2017`. Le millésime du nom de fichier n'est donc pas une date d'édition, et
la règle 8 impose de retenir ce que le document imprime. Le piège est **l'inverse** de celui mesuré
chez Baloise, où le nom de fichier portait une date que le document n'imprimait pas du tout : ici il
en porte une **fausse**.

**Un seul fichier peut être réellement trilingue.** `DKV_KK_AVB_CGA_GCI_01_21` empile ses titres en
allemand, français et anglais sur sa page de garde — « KRANKHEITSKOSTENVERSICHERUNG /
KRANKENHAUSTAGEGELDVERSICHERUNG / ASSURANCE FRAIS DE MALADIE / ASSURANCE INDEMNITÉ JOURNALIÈRE
D'HOSPITALISATION / HEALTH … » — et ses trente-deux pages portent les trois langues (marqueurs
mesurés : de 130, fr 209, en 328). C'est également **l'inverse** du piège Baloise, où un seul
fichier *français* servait les trois arbres de langue. Ici le document est vraiment trilingue, et le
découper par langue serait une erreur symétrique.

Les vingt-sept IPID, eux, sont **neuf produits × trois langues** en fichiers distincts : BUSINESS
TRAVEL, COMPACT HEALTH, COMPLETE HEALTH, CONTINUE, EASY HEALTH, EU PLUS, HOSPITAL HEALTH, PLUS
HEALTH, TRAVEL / TRAVEL PLUS. Une anomalie à vérifier à l'extraction : `IPID_EU_PLUS_fr.pdf` fait
448 Ko contre 690 et 693 Ko pour ses versions allemande et anglaise.

### Ce que l'ingestion apporterait

Le produit **BUSINESS TRAVEL** a déjà son IPID dans le corpus, arrivé par la bibliothèque lalux.
Ingérer DKV lui adjoindrait ses **conditions générales** — ce serait le premier produit luxembourgeois
documenté à la fois par sa fiche d'information et par son contrat.

### Portugais

Le site publie en **cinq langues**, dont le portugais — la communauté portugaise est la première
communauté étrangère du pays. Aucun document PDF n'est toutefois publié en portugais ni en
luxembourgeois : les documents sont en `fr`, `de`, `en`. Les cinq arbres de langue mènent aux mêmes
trois versions.
