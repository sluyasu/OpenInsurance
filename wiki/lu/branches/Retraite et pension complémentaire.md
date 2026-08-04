---
type: branch
domain: insurance
country: lu
branch: retraite
branch_code: "I/VII"
lang: fr
langs: [fr]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/retraite, branch]
aliases: [Retraite, Pension complémentaire, Épargne pension, Rente viagère, Altersvorsorge, Pensionsplan]
source: null
date: 2026-08-04
freshness: 2026-08-04
status: stub
generated: false
---

## Ce que c'est

Cette branche couvre l'épargne constituée en vue de la retraite et servie ensuite en rente ou en capital, que
le contrat soit souscrit à titre individuel ou mis en place par un employeur.

Dans la nomenclature prudentielle — annexe II de la LSA — elle relève de la **branche I** (« Assurances en cas
de vie, de décès, assurances mixtes, assurances de rentes […] non liées à des fonds d'investissement ») pour
les rentes classiques et de la **branche VII**, « **Gestion de fonds collectifs de retraite** », pour les
engagements collectifs. Sur les 33 lignes vie du registre du [[CAA]], **19 détiennent la branche VII**.

Elle se distingue de la [[Prévoyance et décès]], qui couvre un risque et non une épargne, et de
l'assurance [[Solde restant dû]], qui adosse un capital à une dette. Sa proximité est avec
l'épargne-placement, dont la page de branche luxembourgeoise n'est pas encore écrite dans ce dépôt.

## Trois étages, et pas le même superviseur à chaque étage

C'est la particularité luxembourgeoise de cette branche, et elle mérite d'être posée avant tout produit :
**« retraite » ne désigne pas un objet unique, et selon le véhicule choisi l'autorité de contrôle n'est pas
la même.** Les trois vérifications ci-dessous ont été faites en source primaire le 2026-08-04.

**1. Le régime légal.** La pension légale relève du **Livre III du Code de la sécurité sociale**
(« assurance pension »). C'est un régime public, administré hors du registre du [[CAA]], exactement comme
l'assurance maladie (Livre I) et l'assurance accident (Livre II). *L'article précis fixant l'affiliation
obligatoire n'a pas été lu dans cette passe et n'est donc pas cité.*

**2. Les régimes complémentaires d'entreprise.** La **loi modifiée du 8 juin 1999 relative aux régimes
complémentaires de pension** s'applique, selon son **art. 1er**, aux régimes « mis en place par une entreprise
ou un groupe d'entreprises au profit de ses salariés », et son **art. 2** les définit comme « tout régime ou
mécanisme issu d'une promesse de pension de nature collective ». Son **art. 29** désigne l'autorité
compétente, et **ce n'est pas le [[CAA]]** : les missions de la loi sont exercées par l'**Inspection générale
de la sécurité sociale**, « sans préjudice des compétences réservées à d'autres administrations, notamment
l'administration des contributions directes, la Commission de surveillance du secteur financier et le
Commissariat aux assurances ». L'art. 30 détaille ces missions.

**3. Les véhicules de financement, partagés entre deux superviseurs.**

- Les **institutions de retraite professionnelle sous forme de sepcav et d'assep** relèvent de la **loi du
  13 juillet 2005**. Son art. 1er, point 5 et son **art. 58, paragraphe 1er** sont sans ambiguïté :
  « L'autorité de contrôle est la **Commission de surveillance du secteur financier** ». Le Commissariat aux
  Assurances n'y apparaît qu'à l'art. 52, paragraphe 1er, pour l'agrément des gestionnaires du passif.
- Les **fonds de pension agréés par le [[CAA]]** figurent, eux, au registre du superviseur des assurances,
  dans une liste distincte de celles des assureurs vie et non-vie. Elle compte **exactement deux entités** :
  `FONDS DE PENSION GOODYEAR` et `SWISS LIFE INTERNATIONAL PENSION FUND` (lues le 2026-08-04).

## Un quatrième jeu de numéros de branche, à ne pas confondre avec les autres

Les fonds de pension du registre du [[CAA]] ne sont **pas** classés selon l'annexe I ni selon l'annexe II.
Ils sont agréés au titre de l'**ANNEXE IV de la LSA, « Définition des branches d'activité des fonds de
pension »**, qui n'en compte que trois :

> Branche 1 : Prestations comportant un risque viager ou un risque d'investissement supporté par le fonds de
> pension
> Branche 2 : Prestations de régimes sans risque viager où le risque d'investissement est supporté par
> l'affilié
> Branche 3 : Prestations complémentaires en cas de décès ou d'invalidité d'affiliés en activité

Au registre, `FONDS DE PENSION GOODYEAR` porte « 1, 3 » et `SWISS LIFE INTERNATIONAL PENSION FUND` porte
« 1, 2, 3 ».

**Le piège de lecture est direct : une « branche 1 » lue sur la liste des fonds de pension n'est pas la
« branche 1 Accidents » de l'annexe I, ni la « branche I » de l'annexe II.** Le champ `code` de la taxonomie
de ce dépôt ne référence que les annexes I et II ; l'annexe IV n'y est pas représentée, et le `code: "I/VII"`
de cette branche ne décrit donc que le côté assureur, pas le côté fonds de pension.

## Ce que le corpus documente : rien — et le motif n'est pas celui qu'on croit

**Aucun document du corpus luxembourgeois n'est classé dans cette branche : zéro produit, zéro assureur.**

L'intérêt de cette branche est que la lacune est **documentée, et qu'elle vient en partie de ce dépôt et non
du marché**. Les quatre porteurs de détail luxembourgeois vendent tous un produit de retraite ; aucun
document contractuel n'a pu entrer, pour quatre raisons différentes.

- **lalux — les documents ont été trouvés, puis refusés par le schéma.** Douze fichiers de retraite sont
  inventoriés dans la découverte et rejetés à l'ingestion : `easyLIFE_Pension-FR/-DE/-EN` (motif :
  `document_type 'brochure'` n'est pas une valeur du schéma), les six
  `Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Performance_` et `_formule_Securite_` en trois langues,
  et les trois `Fiche_info_fin_032026_-_lalux-Safe_Future_volet_retraite_` (motif :
  `document_type 'fiche_information_financiere'` n'est pas une valeur du schéma). **La lacune est ici une
  lacune de schéma, pas une lacune de marché.** Piège de nommage associé, consigné dans la découverte : le
  suffixe `_ALL` désigne l'**allemand**, pas « toutes langues ».
- **Baloise — le produit existe et ne publie aucun document contractuel.** Le *Pension Plan* (individuel) et
  l'*Employee Benefits Plan* (collectif) n'ont que des KID PRIIPs et des fiches d'information financière ; les
  pages `retraite-luxembourg.html` et `epargne-prevoyance-retraite.html` ne publient rien. Les 896 documents
  de fonds de `kid.baloise.lu` sont fermés par un `Disallow` et **n'ont jamais été demandés**. Le livre vie
  ingérable de cet assureur tient en un seul document, et c'est un solde restant dû.
- **AXA — les produits sont nommés, les documents sont fermés.** *MySmartPension* et *Save for Life Pension*
  sont publiés sur `axa.lu` sous l'onglet particuliers et relèvent d'`AXA Assurances Vie Luxembourg`, seule
  entité vie de détail du groupe au Luxembourg. Le `robots.txt` du site porte `Disallow: /*.pdf` et ferme les
  631 documents inventoriés.
- **Foyer — huit brochures, zéro conditions générales, et tout sous `Disallow`.** Les identifiants
  `8929`/`8930`/`8931` correspondent aux brochures épargne-retraite et optimisation fiscale ; elles sont
  commerciales, non contractuelles, et **aucune n'a été demandée**. Les cinq seuls IPID de la gamme vie de ce
  porteur ne comportent aucun produit de retraite.

**Quatre porteurs, quatre motifs distincts, zéro document.** Une branche vide n'est pas ici le signe d'un
marché absent ; c'est le signe d'un marché qui ne publie pas ses conditions générales, plus une règle de
schéma qui écarte les documents non contractuels.

## La seule branche où les frontaliers sont explicitement adressés

C'est mesuré, et c'est propre à cette branche. La brochure *easyLIFE Pension* titre « **FRONTALIER ?** » en
français, « **GRENZGÄNGER?** » en allemand et « *as a cross-border worker* » en anglais. Aucun équivalent n'a
été trouvé côté auto ni côté habitation.

La lecture qu'en fait le recensement de ce dépôt est cohérente avec le reste : le frontalier — **225 840
salariés entrants en 2023 selon le STATEC** — gare sa voiture et habite chez lui, en France, en Belgique ou
en Allemagne, et ses contrats auto et habitation sont écrits là-bas ; la retraite, la vie et la fiscalité,
elles, suivent la personne et non l'adresse. Voir [[Assurance auto]] pour le même partage vu de l'autre côté.

**Le mécanisme fiscal qui rend ce ciblage possible n'est pas établi ici.** Un article du droit fiscal
luxembourgeois est cité dans le fichier de découverte lalux ; il n'a été vérifié ni contre le texte, ni
contre la brochure, laquelle n'a pas pu être ouverte. Il n'est donc pas repris.

## À surveiller

- **« Brochure » n'est pas « conditions générales ».** Même si le schéma de ce dépôt les acceptait, les douze
  documents lalux resteraient des documents commerciaux. **Aucune conditions générales de produit de retraite
  luxembourgeois n'a été trouvée en accès libre chez aucun des quatre porteurs.**
- **Le superviseur dépend du véhicule, pas de la marque.** Un même groupe peut proposer un contrat
  d'assurance (CAA), une sepcav ou une assep (CSSF) et un régime complémentaire d'entreprise dont le contrôle
  relève de l'IGSS.
- **Le principe de spécialisation joue.** Une entité vie porte le contrat, jamais l'entité non-vie du même
  groupe. AXA compte deux entités vie agréées au Luxembourg, de sorte que la seule marque « AXA » n'identifie
  pas le porteur de risque.
- **Les formules portent des noms, pas des définitions.** Deux fiches d'information financière distinctes
  existent pour un même produit sous les intitulés « formule Performance » et « formule Sécurité » ; ce que
  chacune recouvre n'est pas lisible depuis les seuls noms de fichiers.
- **Rente ou capital, frais, table de conversion.** Ce sont les paramètres qui décident du montant servi ;
  **aucun n'est documenté ici**, faute de document. Ils ne sont pas décrits par analogie avec un autre pays.

## Lacunes établies

- **Zéro document, zéro produit, zéro assureur dans la branche.** `status: stub` en conséquence.
- **Le régime fiscal de l'épargne-retraite luxembourgeoise n'est pas établi** dans ce dépôt et n'est pas
  cité.
- **L'article du Livre III du Code de la sécurité sociale fixant l'affiliation obligatoire n'a pas été lu**
  dans cette passe.
- **On ignore si les deux fonds de pension du registre du [[CAA]] servent un particulier luxembourgeois.**
  Leurs dénominations renvoient à un groupe industriel et au régime international d'un assureur ; rien n'a
  été vérifié au-delà de la ligne du registre.
- **Les garanties, options et exclusions typiques ne sont pas écrites**, et ne le seront que depuis des
  documents luxembourgeois.
- **Le manifeste pays est en retard sur cette page.** `sources/lu/_country.yml`, entrée `retraite`, porte
  encore « The statutory framework for occupational schemes was NOT ESTABLISHED in this pass; do not cite one
  until it is ». Il l'est désormais — loi du 8 juin 1999, loi du 13 juillet 2005, annexe IV de la LSA,
  vérifiées en source primaire ci-dessus. **Le manifeste n'a pas été modifié par cette page** ; la
  contradiction est signalée plutôt que corrigée en silence.

## Cadre légal

- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA)** : annexe II, branches **I** et
  **VII** (assureurs vie) ; **annexe IV**, branches 1 à 3 (fonds de pension).
- **Loi modifiée du 8 juin 1999 relative aux régimes complémentaires de pension** : art. 1er (champ
  d'application), art. 2 (définition), art. 29 (autorité compétente : l'Inspection générale de la sécurité
  sociale), art. 30 (missions).
- **Loi du 13 juillet 2005** relative aux institutions de retraite professionnelle sous forme de société
  d'épargne-pension à capital variable (sepcav) et d'association d'épargne-pension (assep) : art. 1er point 5
  et art. 58 paragraphe 1er (autorité de contrôle : la Commission de surveillance du secteur financier),
  art. 52 paragraphe 1er (rôle du Commissariat aux Assurances pour les gestionnaires du passif).
- **Code de la sécurité sociale, Livre III** (assurance pension) pour le régime légal, public et hors
  registre du [[CAA]].
- **Loi modifiée du 27 juillet 1997 sur le contrat d'assurance**, pour le régime du contrat d'assurance.
- **Aucune obligation d'assurance privée.** `mandatory: false`.
- Superviseur des contrats d'assurance et des fonds de pension listés au registre : [[CAA]].

## Related

- [[Prévoyance et décès]] · [[Solde restant dû]] · [[Assurance auto]] · [[CAA]] · [[Premium]] ·
  [[00 - Luxembourg MOC]]

## Sources

- Loi modifiée du 8 juin 1999 relative aux régimes complémentaires de pension, texte publié sur Legilux
  (`data.legilux.public.lu/eli/etat/leg/loi/1999/06/08/n5/jo/fr/html`), consulté le 2026-08-04.
- Loi du 13 juillet 2005 relative aux institutions de retraite professionnelle sous forme de sepcav et
  d'assep, texte publié sur Legilux (`data.legilux.public.lu/eli/etat/leg/loi/2005/07/13/n3/jo/fr/html`),
  consulté le 2026-08-04.
- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe II et annexe IV
  (`caa.lu/uploads/documents/files/LSA_Annexe4.pdf`), consultées le 2026-08-04.
- Registre du Commissariat aux Assurances, liste « Fonds de pension luxembourgeois »
  (`caa.lu/uploads/documents/files/csv/FondsDePension_FondsDePensionLuxembourgeois.csv`), lue le 2026-08-04.
- `secu.lu`, rubrique « Assurance pension », pour le rattachement du régime légal au Livre III du Code de la
  sécurité sociale, consulté le 2026-08-04.
- `_meta/lu-market-census.md` (détentions de branches vie, frontaliers, courte liste d'ingestion).
- `_meta/discovery/lu/lalux.md` (douze documents de retraite trouvés et refusés ; piège `_ALL` = allemand ;
  ciblage frontaliers d'*easyLIFE Pension*).
- `_meta/discovery/lu/baloise.md` (*Pension Plan*, pages retraite sans document, 896 documents de fonds sous
  `Disallow`).
- `_meta/discovery/lu/axa.md` (*MySmartPension*, *Save for Life Pension*, `robots.txt` fermant les PDF).
- `_meta/discovery/lu/foyer-vie.md` (huit brochures dont l'épargne-retraite, zéro conditions générales).
- `sources/lu/_country.yml`, branche `retraite`.
