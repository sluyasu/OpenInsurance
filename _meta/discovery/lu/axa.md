# axa — AXA au Luxembourg (AXA ASSURANCES LUXEMBOURG, AXA Assurances Vie Luxembourg, AXA Wealth Europe)

website: axa.lu, axa-wealtheurope.lu
fetch: plain
status: blocked
lang: fr, de, en
enumerated: 2026-08-03

**631 documents inventoriés sur axa.lu, 0 récupérable. Et cette fois le chiffre qui compte
aggrave le blocage au lieu de le rendre secondaire : au moins 302 de ces 631 documents sont de
véritables conditions d'assurance, et jusqu'à 372 en comptant les familles de noms probables.
Là où Foyer n'en publie aucune sur huit cents documents et lalux quatre sur quatre-vingt-dix,
AXA en publie plusieurs centaines — et son `robots.txt` les ferme toutes.**

## Les trois entités agréées

Source : registre du CAA, exports CSV du 2026-08-03, en-tête `"Nom","Adresse","Responsable","Téléphone","Fax","Branches"`.

| Nom au registre | Liste | Branches (verbatim) | Adresse |
|---|---|---|---|
| `AXA ASSURANCES LUXEMBOURG (222100W6SMT3RLPML260)` | non-vie | `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18` | 1, Place de l'Etoile, 1479 Luxembourg |
| `AXA Assurances Vie Luxembourg (2221007TDHL8NJ2B3448)` | vie | `I, II, III, VI, VII` | idem |
| `AXA Wealth Europe (222100WCM48LSUO2KP31)` | vie | `I, III, VI, VII` | idem |

Les trois partagent l'adresse, le responsable déclaré et le numéro de téléphone. Le principe de
spécialisation joue : l'entité non-vie et les deux entités vie ne se recoupent pas.

**L'identifiant entre parenthèses est un LEI, pas un RCS.** Vingt caractères alphanumériques ;
le CSV du CAA ne comporte aucune colonne RCS. Le LEI d'AXA Wealth Europe est corroboré hors du
registre : il est écrit deux fois dans le nom de fichier de ses propres rapports SFCR
(`N09V-LU-01-20251231-CAA-222100WCM48LSUO2KP31-222100WCM48LSUO2KP31.pdf`).

**Un seul RCS est publié, et c'est celui de l'entité qui ne vend pas au détail résident.** Les
mentions légales d'`axa-wealtheurope.lu` donnent l'identité complète : « AXA Wealth Europe.
Société anonyme, 1 place de l'Etoile, L-1479 Luxembourg. R.C.S. Luxembourg B 206515. N° TVA
international : LU29173986 ». Les mentions légales d'`axa.lu` (`/fr/legal`,
`/fr/informations-legales`) ne nomment aucune entité, ne donnent aucun RCS et parlent
collectivement des « Compagnies d'assurances AXA à Luxembourg ». La seule dénomination avec
forme juridique trouvée sur `axa.lu` est « AXA Assurances Luxembourg s.a. », sur la page
`/fr/compliance`, dans un paragraphe FATCA. La page `/fr/disclosure-information` nomme « AXA
Assurances vie Luxembourg ». Aucun RCS nulle part.

### Laquelle vend au détail luxembourgeois

Attribution par entité, pas par document : ce qui suit se déduit de l'agrément détenu et du
segment du produit, jamais d'une mention lue dans un contrat. Aucun document n'a pu être ouvert.

- **`AXA ASSURANCES LUXEMBOURG`** — c'est la seule des trois à détenir un agrément non-vie, donc
  la seule qui puisse porter le livre de détail non-vie publié sur `axa.lu`. La branche 10 est
  détenue et le produit correspondant est publié : gamme OptiDrive, conditions d'assurance de
  millésime W03.2026 et IPID dédié. Le reste suit : OptiHome (habitation), OptiSoins et VivaZen
  (santé), Pet (animaux), OptiTravel (voyage), RC Chasse.
- **`AXA Assurances Vie Luxembourg`** — c'est l'entité vie du site de détail. Vie Particuliers,
  MySmartPension, Save for Life Pension, Domia et Serena, et un produit solde restant dû
  (`CG_BILProtectionPretImmobyAXA_W12_18_*`) sont publiés sur `axa.lu` sous l'onglet
  particuliers. La branche II (nuptialité-natalité) n'est détenue que par elle, et par aucune
  autre compagnie AXA luxembourgeoise ; aucun produit correspondant n'a été observé.
- **`AXA Wealth Europe`** — non, autant que l'inventaire permette de le dire. Site distinct,
  gamme distincte (Lifinity Europe et Borea Invest), déclinée par pays de résidence du preneur :
  `/product/lifinity-europe-be`, `-fr`, `-lu`, `-mc`, plus des notes d'information fiscale
  séparées pour la France, la Belgique, le Luxembourg, Monaco et le Portugal. Langues du site :
  français, anglais, **néerlandais** — pas d'allemand. Un « espace apporteurs » sert la
  distribution intermédiée. C'est le profil transfrontalier décrit dans
  `sources/lu/_country.yml`, et la vérification confirme l'hypothèse au lieu de la supposer.
  La variante `lifinity-europe-lu` existe, donc le produit est vendu aussi à des résidents ;
  cela n'en fait pas pour autant un produit de détail.

**Attention : la marque ne tranche pas, et le nom de produit non plus.** `Borea Invest` est
publié à la fois sur `axa.lu` (conditions d'assurance `caboreainvestw072015_FR.pdf`,
KID 2025, liste de fonds UC) et sur `axa-wealtheurope.lu` (notes d'information fiscale
`08-Note-d-information-fiscale-Borea-Invest-FR.pdf`, variante belge). Avec deux entités vie
agréées et un même nom commercial des deux côtés, ni « AXA » ni « Borea Invest » n'identifie le
porteur de risque. `carrier: null` est ici la lecture exacte, pas une extraction incomplète — et
elle ne pourra pas être levée sans ouvrir les documents, ce que le `robots.txt` interdit.

## Le verdict robots.txt, hôte par hôte

Cinq hôtes servent des documents. Chacun a été interrogé sur `/robots.txt` **avant** toute
autre requête le concernant.

### `axa.lu` — tous les PDF interdits

`https://axa.lu/robots.txt`, 200 `text/plain`. `https://www.axa.lu/robots.txt` redirige en 301
vers le même fichier. Le corps est le gabarit Drupal standard (`/core/`, `/profiles/`,
`/admin/`, `/user/login`, les `README.txt`…), suivi d'un ajout maison en fin de fichier :

```
# Pdf
Disallow: /*.pdf

Sitemap: https://axa.lu/sitemap.xml
```

sous le seul groupe déclaré, `User-agent: *`.

**La règle française vaut donc aussi au Luxembourg — mais il fallait le vérifier, et l'écriture
n'est même pas la même.** Le corpus français portait `Disallow: *.pdf` ; ici c'est
`Disallow: /*.pdf`, ancré sur la racine. La portée pratique est identique et totale : les 631
URL de documents relevées sur `axa.lu` commencent toutes par `/` et finissent toutes par `.pdf`.
Vérifié : **0 sur 631** échappe au motif. Rien n'a été récupéré sous ce chemin.

Ce n'est pas le geste délibéré de Foyer, qui avait énuméré ses chemins de documents, les avait
fermés, puis en avait rouvert exactement deux. C'est une règle d'un seul mot posée sur toute une
extension, sans exception, à côté d'un gabarit Drupal non modifié. L'effet est plus large que
chez Foyer et l'intention est moins lisible — mais la conclusion opérationnelle est la même, et
ce projet la respecte.

Ce que la même règle **n'**interdit **pas** : les pages HTML. Le `sitemap.xml` que `robots.txt`
déclare lui-même a répondu 200 et publie 928 URL (324 en, 304 fr, 299 de, 1 node). Tout
l'inventaire ci-dessous en vient, plus le pager publié de la page `/cgv`. Aucun PDF n'y figure.

### `axa-wealtheurope.lu` — aucune restriction sur les PDF

`https://axa-wealtheurope.lu/robots.txt`, 200, 1593 octets. Gabarit Drupal seul, un cran plus
ancien que celui d'`axa.lu` (pas de lignes `media/oembed`, `Disallow: /README.txt` au lieu de la
liste `composer/`). Sous `User-agent: *` : `/core/`, `/profiles/`, `/README.txt`, `/web.config`,
`/admin/`, `/comment/reply/`, `/filter/tips`, `/node/add/`, `/search/`, `/user/register/`,
`/user/password/`, `/user/login/`, `/user/logout/`, et les variantes `/index.php/…`.

**Aucune ligne `.pdf`. Aucune ligne `Sitemap:`.** Les deux hôtes luxembourgeois d'AXA divergent
donc sur ce point précis : le site de détail ferme ses PDF, le véhicule transfrontalier non.

### `new-axa-prod.s3.amazonaws.com` — robots.txt inaccessible

`https://new-axa-prod.s3.amazonaws.com/robots.txt` répond **403 `AccessDenied`**
(`<Code>AccessDenied</Code>`, 263 octets `application/xml`). C'est le comportement par défaut
d'un bucket S3 sans objet `robots.txt` exposé, pas une politique d'exploration.

Statut retenu : **indéterminé, traité comme non exploré.** Le RFC 9309 §2.3.1.3 range les codes
400-499 dans « unavailable » et autorise alors l'accès, mais la pratique historique traite 401
et 403 comme un refus complet. La divergence est réelle ; en découverte elle n'a pas eu à être
tranchée, puisque rien n'a été téléchargé. Elle devra l'être avant toute ingestion.

### `luxembourg-axa.cdn.axa-contento-118412.eu` — même bucket, même 403

CDN placé devant le même stockage (préfixe d'objet `luxembourg-axa` identique). `/robots.txt`
répond le même **403 `AccessDenied`**, mot pour mot. Deux documents seulement y sont liés, tous
deux depuis `axa-wealtheurope.lu` : les *Binding Corporate Rules* du groupe, en français et en
anglais. Ce sont des documents de protection des données, pas des contrats d'assurance. Même
statut indéterminé, mêmes conséquences : non exploré.

### `www.luxair.lu` — tiers, hors périmètre

Gabarit Drupal, `Sitemap:` déclaré, **aucune règle `.pdf`**. Neuf formulaires de déclaration de
sinistre voyage (FR/DE/EN) y sont hébergés et liés depuis `axa.lu/fr/particuliers/assurance-luxair`.
Ce sont les documents du partenaire, pas la bibliothèque d'AXA.

## L'inventaire de la bibliothèque publique

### Méthode, et ce qu'elle interdit

Aucune énumération d'espace d'URL. Les 631 URL viennent de deux sources, toutes deux réellement
publiées :

1. **Le hub `/cgv`**, intitulé « Vos Conditions d'Assurances », dans ses trois arbres de langue.
   Il est paginé à dix résultats par page par un pager Drupal classique ; la page courante publie
   le lien `rel="next"` de la suivante, et c'est cette chaîne qui a été suivie jusqu'à sa fin
   (26 pages en `/fr`, 17 en `/de`, 7 en `/en`). Aucun `?page=N` n'a été deviné.
2. **Le `sitemap.xml`** déclaré par `robots.txt` : 293 pages produits, légales et de conformité
   ont été lues en HTML et leurs liens `.pdf` relevés.

Aucun PDF n'a été demandé, sur aucun hôte. **Tout ce qui suit se lit donc sur des noms de
fichier et des libellés de lien, jamais sur un contenu.** C'est une preuve plus faible qu'une
extraction, et les comptes ci-dessous doivent être lus avec cette réserve.

### Ce que la page dit d'elle-même

Deux textes publiés par l'éditeur décodent toute la nomenclature, ce qui évite de l'inférer.

Le chapô de `/fr/cgv` : « Veuillez indiquer la référence mentionnée sur votre contrat, sans
espace et sans caractère tiret simple "-" ou point "." » suivi de « Exemple :
"CA_OptiDrive_W07_16_Fr" ». Le hub n'est donc pas un catalogue de produits mais **une recherche
par référence de rédaction imprimée sur le contrat du preneur** : `CA` = conditions d'assurance,
`OptiDrive` = produit, `W07_16` = wording de juillet 2016, `Fr` = langue.

Et sur la page habitation, les libellés de lien de `CA_OptiHome_W03_24_FR.pdf` et
`CA_OptiHome_W03_24_EN.pdf` sont, mot pour mot, « Conditions d'assurance » et « Conditions of
Insurance ». Le préfixe `CA` est donc nommé par l'éditeur, pas déduit.

### Les comptes

631 URL de documents distinctes sur `axa.lu` : 479 depuis le hub `/cgv`, 153 depuis les pages
produits et légales, 1 commune aux deux.

| Type | URL | Base de la lecture |
|---|---:|---|
| Conditions d'assurance, préfixe `CA` | 293 | préfixe nommé par l'éditeur |
| Conditions générales, préfixe `CG` | 9 | idem |
| **Sous-total conditions, lecture ferme** | **302** | |
| Probable `CA` — référence de wording numérique (`2083094173W052009`) | 38 | famille de nommage |
| Probable `CA` — produit + wording sans préfixe (`ProtectionjuridiqueW082014`) | 32 | famille de nommage |
| **Borne haute conditions** | **372** | |
| IPID | 88 | |
| `CS` — conditions spéciales (extensions, garanties optionnelles) | 67 | |
| Flyers et dépliants | 34 | |
| KID PRIIPs | 15 | |
| `CC` — conditions complémentaires | 10 | |
| Listes, gabarits, divers | 10 | |
| Tableaux des garanties | 9 | |
| Mandats SEPA | 6 | |
| `GC`/`GS` — garanties complémentaires | 5 | |
| SFDR et gouvernance | 5 | |
| Formulaires (sinistre, entente préalable) | 3 | |
| Formulaires FATCA/CRS | 3 | |
| Fiches d'information financière | 3 | |
| Clause isolée | 1 | |
| **Total** | **631** | |

**Le chiffre utile : au moins 302 vraies conditions, contre 4 sur 90 chez lalux et 0 sur 800
chez Foyer.** C'est un ordre de grandeur différent, pas une variation. AXA Luxembourg est, à ce
stade du recensement luxembourgeois, le seul assureur observé qui publie le contrat lui-même
plutôt que son résumé IDD — et il est aussi le seul dont la bibliothèque soit intégralement
fermée aux robots.

Les 67 `CS` ne sont pas des contrats autonomes : ce sont des extensions (bagages par plafond,
bris de machine, perte d'exploitation, sécurité du conducteur…). Elles relèvent de
`is_extension`/`extends`, pas d'une fiche produit propre.

### Millésimes

263 des 302 conditions fermes portent un jeton de wording lisible. Le plus ancien est W05.2004,
le plus récent W03.2026. La masse est ancienne : 80 documents en 2013, 42 en 2016, 27 en 2015,
16 en 2014. Le hub conserve les rédactions historiques — c'est cohérent avec sa fonction, qui
est de servir au preneur la rédaction de *son* contrat, pas la rédaction courante. Une ingestion
devrait donc traiter la quasi-totalité de ce fonds comme des éditions superseded au sens de la
règle 8, et non comme le catalogue actuel.

### Langues

**Non mesurées.** Les corps n'ont pas pu être lus. Sur les seuls marqueurs de nom de fichier :
201 `fr`, 118 `de`, 84 `en`, et 228 sans aucun marqueur. Ces chiffres ne valent pas une mesure
et ne doivent pas être recopiés comme telle — le corpus luxembourgeois a déjà produit, chez
lalux, quatre fichiers dont le suffixe de langue contredit le corps.

Ce qui est en revanche mesurable, c'est que **les trois arbres du hub sont presque disjoints** :
259 URL sous `/fr`, 161 sous `/de`, 66 sous `/en`, et seulement 5 URL apparaissent dans plus
d'un arbre (2 dans les trois). Ce ne sont donc pas trois vues d'un même fonds mais trois fonds
largement distincts, ce qui corrobore la note de `sources/lu/_country.yml` (« AXA Assurances
Luxembourg publishes three DISTINCT CG sets under /fr/cgv, /de/cgv, /en/cgv ») et confirme au
passage qu'aucune langue ne doit être complétée depuis une autre.

L'arbre de langue n'est d'ailleurs pas la langue du document : la première page de `/de/cgv`
sert `VivaZen Jeunes et Adultes CA-W.03.2013.pdf` et `TUpagricoleCAW012013.pdf`, dont les
intitulés sont français.

### Doublons possibles, non vérifiables

Les 479 URL du hub ne portent que 378 noms de fichier distincts. **73 noms sont servis sous plus
d'une URL opaque**, soit 101 URL excédentaires. Chez lalux, ce motif recouvrait à la fois de
vrais doublons octet à octet et de vraies variantes ; ici la question ne peut pas être tranchée,
puisque départager exigerait de calculer un sha256, donc de télécharger. À enregistrer comme
incertitude, pas comme doublon.

## AXA Wealth Europe : atteignable, et sans conditions générales

Son `robots.txt` n'interdit rien d'utile, donc c'est le seul endroit où un
`sources/lu/axa.yml` aurait pu prendre appui. L'inventaire referme la question.

130 pages au sitemap (45 fr, 43 en, 42 nl), 85 URL de documents distinctes : 63 servies en
relatif depuis `axa-wealtheurope.lu`, 3 en absolu depuis le même hôte, 17 depuis le bucket S3,
2 depuis un CDN `axa-contento`.

Familles : 19 listes de supports financiers, 11 rapports SFCR (millésimes 2016 à 2025), 10 notes
d'information fiscale par pays, 9 fiches de fonds, 6 guides d'utilisation du portail Lifinity4U,
5 formulaires de réclamation et de médiation ACA, 3 documents BCR, 2 publications SFDR, 1
document précontractuel à qualifier, 19 non classés — 85 au total.

**Zéro document dont le nom contienne `condition`, `bedingung`, `algemene` ou `voorwaard`.**
Le fonds est prudentiel, financier et administratif ; il ne contient pas de contrat.

## Ce qui n'a pas pu être atteint, et pourquoi

- **Les 631 documents d'`axa.lu`**, dont au moins 302 conditions d'assurance et 88 IPID :
  interdits par `Disallow: /*.pdf`. C'est la totalité de la bibliothèque de l'assureur de détail.
- **Le porteur de risque de chaque document** : il ne se lit que dans le document. Trois entités
  agréées, une adresse commune, aucun RCS publié pour les deux entités opérantes, et un nom de
  produit (`Borea Invest`) partagé entre les deux entités vie. Rien dans l'inventaire ne permet
  de l'attribuer.
- **La langue réelle de chaque document** : mesurable seulement sur le corps.
- **L'identité des 101 URL excédentaires** : mesurable seulement par empreinte.
- **Les 154 documents du bucket S3** liés depuis `axa.lu` (annexes précontractuelles SFDR,
  fiches de fonds, déclarations de sinistre, formulaires d'entente préalable), les 17 liés
  depuis `axa-wealtheurope.lu`, et les 2 servis par le CDN `axa-contento` : `robots.txt` en 403
  sur les deux hôtes, statut indéterminé, non explorés. Aucun n'est une conditions générales.

Rien de tout cela n'est un échec de la passe : c'est le résultat.

## Aucun balayage, et rien de sensible rencontré

Aucune énumération de motif d'URL n'a été faite : le pager publié a été suivi, le sitemap déclaré
a été lu, et rien d'autre. Les 794 noms de fichier relevés ont été passés au filtre des motifs
qui, sur d'autres sites, ont déjà exposé des spécimens de contrats remplis : **zéro
correspondance**. Les identifiants numériques du hub (`2083094173W052009`) sont des références de
rédaction et non des numéros de police — le même radical revient avec plusieurs millésimes de
wording, et les mêmes références apparaissent dans les arbres français et allemand.

## Pas de `sources/lu/axa.yml`

La condition posée — « seulement si la bibliothèque est atteignable et non bloquée » — n'est pas
remplie. Elle est atteignable en inventaire et bloquée en récupération, à 100 %.

Le fonds d'AXA Wealth Europe, lui, est libre d'accès mais ne contient aucun contrat, et relève
d'un placement transfrontalier dont `sources/lu/_country.yml` demande explicitement de trancher
l'attribution pays avant toute ingestion.

Même traitement donc que [Foyer](foyer.md), et sixième motif distinct après
[Wakam](../fr/wakam.md), [Acheel](../fr/acheel.md), [MGEN](../fr/mgen.md),
[ACM](../fr/acm.md) et Foyer. C'est aussi le plus coûteux des six : c'est la seule fois où le
blocage porte sur un fonds de conditions générales réellement publié.

## Une correction en attente pour le manifeste pays

`sources/lu/_country.yml`, entrée `moto`, porte depuis la passe Foyer la mention « Aucun produit
deux-roues luxembourgeois n'est encore observé ». **Cette passe l'observe.** AXA publie une gamme
deux-roues distincte, avec ses propres conditions d'assurance et son propre IPID :

- `CA_OptiDrive_Moto_W04_21_FR_12-2021.pdf` et `CA_OptiDrive_Moto_W04_21_EN_12-2021.pdf`
- `IPID_OptiDrive_Moto_W04_21_Fr.pdf`, `IPID_OptiDrive_Moto_W04_21_En.pdf`,
  `Fiche IPID_OptiDrive MOTO_FR_2024.pdf`, `Fiche IPID_OptiDrive MOTO_EN_2024.pdf`
- une page produit dédiée, `/fr/particuliers/assurance-moto`, distincte de
  `/fr/particuliers/assurance-auto`

La branche `moto` reposait sur le seul texte de l'art. 2 de la loi du 16 avril 2003 ; elle repose
désormais aussi sur un produit observé. La ligne du manifeste n'a pas été modifiée ici — elle
sort du périmètre de cette fiche — mais elle est fausse en l'état et devrait l'être.

Autres branches du manifeste nouvellement adossées à un produit luxembourgeois observé :
`animaux` (Pet, CA W01.2026), `chasse` (RC Chasse, CA W04.2014 — la branche était marquée comme
reposant sur la loi seule), `solde-restant-du` (BIL Protection Prêt Immobilier by AXA, CG W12.2018).
