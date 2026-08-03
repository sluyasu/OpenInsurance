---
type: branch
domain: insurance
country: lu
branch: rc-professionnelle
branch_code: "13"
lang: fr
langs: [fr, de]
mandatory: conditional
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/rc-professionnelle, branch]
aliases: [RC pro, RC professionnelle, Responsabilité civile professionnelle, RC exploitation, Berufshaftpflicht]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Ce que c'est

La responsabilité civile professionnelle couvre les conséquences pécuniaires des dommages causés à des tiers
dans l'exercice d'une activité professionnelle. Elle relève de la **branche 13 de l'annexe I, partie A de la
LSA**, dont la définition est purement résiduelle : « R.C. générale — Toute responsabilité autre que celles
mentionnées sous les branches 10, 11 et 12 », c'est-à-dire toute responsabilité qui n'est ni automobile, ni
aérienne, ni maritime. La branche 13 est l'une des plus détenues du marché : **30 des 44 lignes non-vie du
registre** du [[CAA]] la portent.

Le corpus luxembourgeois donne à cette branche une place particulière : c'est la **seule ligne du marché de
détail pour laquelle de véritables conditions générales sont publiées**. Sur les 304 documents relevés chez
lalux, quatre seulement sont des conditions générales, et deux d'entre elles sont les versions française et
allemande d'un même contrat de RC professionnelle — celui des architectes et ingénieurs-conseils. Partout
ailleurs, y compris pour l'auto et l'habitation, seul le document d'information (IPID) est en ligne.

## La ligne avec la multirisque professionnelle

Les deux relèvent de la même branche 13, et la distinction est contractuelle, pas prudentielle.

Les conditions générales *RC Professionnelle pour Architectes et Ingénieurs-Conseils* (édition 01.05.2025,
réf. EAC/2025/13684) tracent la ligne explicitement, en définissant les deux garanties de base l'une par
rapport à l'autre :

- **Responsabilité civile professionnelle** : « les dommages provenant d'une erreur, d'une négligence ou
  d'une faute ayant un caractère contractuel ou décennal vis-à-vis du maître de l'ouvrage ainsi que des
  dommages qui en résultent à des Tiers qui ne sont pas contractants ». C'est la faute *dans la prestation*.
- **Responsabilité civile exploitation** : « la responsabilité extra-contractuelle […] pour les dommages
  causés à des Tiers au cours de l'exercice de l'activité assurée », et le contrat ajoute qu'elle « couvre
  les dommages **autres que ceux visés par la garantie Responsabilité civile professionnelle** ». C'est le
  dommage causé *à l'occasion* de l'activité, défini par soustraction.

Le même contrat traite les deux garanties différemment sur deux points qui ont des conséquences pratiques :
la RC professionnelle s'exerce **par sinistre et par année d'assurance**, la RC exploitation **par sinistre**
seulement ; et la franchise, fixée aux Conditions Particulières, « ne s'applique pas à la rubrique
responsabilité civile exploitation, sauf dispositions contraires ».

Côté [[Multirisque professionnelle]], la même frontière se lit à l'envers : dans l'IPID easyPROTECT PRO, la
RC exploitation est la garantie de base et la RC professionnelle une **option**, réservée à deux des huit
secteurs d'activité proposés. Un contrat multirisque professionnel ne contient donc pas nécessairement de RC
professionnelle au sens strict, et le nom du produit ne le dit pas.

## Obligation : ce qui est vérifié, et ce qui ne l'est pas

Le champ `mandatory` de cette branche vaut `conditional`. Trois obligations ont été vérifiées dans un texte
primaire ; **la liste complète des professions réglementées porteuses d'une RC obligatoire n'est pas
établie** et ne doit pas être devinée.

**Vérifié :**

- **Architectes et ingénieurs-conseils.** *Loi du 13 décembre 1989 portant organisation des professions
  d'architecte et d'ingénieur-conseil*, **art. 6** : « Les architectes et ingénieurs-conseils visés par la
  présente loi assurent obligatoirement leur responsabilité professionnelle, tant contractuelle que
  délictuelle ou quasi délictuelle, y compris la responsabilité décennale. La prédite assurance couvre
  obligatoirement les architectes et ingénieurs salariés d'une personne physique ou morale. » L'obligation
  s'étend donc aux salariés, et elle absorbe la responsabilité décennale — c'est le point de contact avec
  [[Assurances constructions]].
- **Courtiers d'assurances et sociétés de courtage.** **LSA art. 290, paragraphe 4** : les courtiers
  « doivent en outre souscrire à une police d'assurance auprès d'une entreprise d'assurance autorisée à
  pratiquer l'assurance de la responsabilité civile au Grand-Duché de Luxembourg et couvrant leur
  responsabilité civile professionnelle », dont l'étendue, le champ territorial, les exclusions et la preuve
  sont fixés par règlement du [[CAA]]. La preuve de cette couverture est une **condition d'agrément** (LSA
  art. 283, paragraphe 1er, point e) et art. 283-1, paragraphe 1er, point c).
- **Professionnels du secteur des assurances (PSA).** **LSA art. 262, paragraphe 4** : police obligatoire
  « comportant les garanties minimales de couverture suivantes : 50.000 euros par sinistre et 500.000 euros
  globalement par année pour les PSA personnes physiques, et 125.000 euros par sinistre et 1.250.000 euros
  globalement par année pour les PSA personnes morales. Toute franchise éventuelle doit être inopposable à
  la personne lésée. »

**Non établi, et écrit ici comme tel :**

- La liste exhaustive des professions réglementées luxembourgeoises portant une obligation d'assurance de
  responsabilité professionnelle. Le recensement de marché n'a vérifié que le texte de 1989 ; les autres
  professions n'ont pas été contrôlées contre leur statut propre. **Ne pas transposer la liste française**
  (santé, avocats, notaires, experts-comptables, agents immobiliers) : chacune de ces professions relève au
  Luxembourg d'un statut distinct, qui n'a pas été lu.
- Si une obligation d'assurance s'attache à l'*autorisation d'établissement*. Question ouverte du
  recensement, non tranchée.
- Le document de politique de « general good » publié par le [[CAA]] ne liste **aucune** disposition
  luxembourgeoise d'assurance obligatoire au titre de l'art. 180 de Solvabilité II — sa table est vide pour
  la LPS comme pour le libre établissement. Ce document se déclare lui-même non exhaustif et non
  nécessairement à jour : c'est une observation, pas une preuve d'absence.

Pour les professions sans obligation légale, l'assurance reste fréquemment exigée par contrat, par un donneur
d'ordre ou par un maître d'ouvrage. C'est un fait sur les contrats commerciaux, pas sur la loi.

## Ce que le corpus documente

Un seul contrat, dans ses deux versions linguistiques : *Assurance R.C. Professionnelle pour Architectes et
Ingénieurs-Conseils* / *Berufshaftpflichtversicherung für Architekten und beratende Ingenieure*, 19 pages
chacune, même référence EAC/2025/13684, gamme APROBAT.

C'est aussi l'un des rares documents du corpus luxembourgeois qui **nomme son porteur avec sa forme
juridique**. Le fascicule Définitions donne « Assureur : LA LUXEMBOURGEOISE Société Anonyme d'Assurances,
9, rue Jean Fischbach, L-3372 Leudelange » — donc l'entité **non-vie**, R.C.S. Luxembourg **B 31035**, et non
LA LUXEMBOURGEOISE-VIE (B 31036). Partout ailleurs dans ce corpus, les documents s'en tiennent à la marque
« LALUX Assurances » et à « la Compagnie », sans forme sociale ni numéro.

Deux versions du même contrat, deux qualités d'identification, et cela vaut d'être noté parce qu'un lecteur
ne lit qu'une langue : la version **française** imprime la dénomination complète et le numéro RCS **dans le
bandeau de chaque page** ; la version **allemande** ne porte le numéro que sur les pages 10, 12, 14 et 16,
imprime « R.C.S. LUXEMBOURG » sans numéro sur treize autres pages, un « R.C.S. » tronqué page 18, et **aucun
en-tête du tout page 8**. L'identification du porteur peut donc dépendre de la page — et de la langue — qu'on
ouvre.

Points saillants du contrat, tels qu'imprimés :

- **Déclenchement en base réclamation.** « Les garanties du présent contrat ne sont acquises que pour les
  réclamations adressées au Preneur d'assurance pendant la période de validité du contrat », pour les
  missions réalisées depuis la date d'effet, et pour celles antérieures « pour autant que le Preneur
  d'assurance n'ait pas eu connaissance, au moment de la souscription, d'une éventuelle réclamation ». La
  date du sinistre est celle de la première réclamation.
- **Deux clauses de survie de la garantie décennale**, qui répondent à un problème propre au déclenchement
  par réclamation : en cas de **cessation d'activité**, la garantie décennale « est maintenue, durant la
  période décennale subséquente, pour les réclamations en relation avec les travaux assurés », extension
  « comprise dans la prime annuelle » ; en cas de **résiliation**, elle est maintenue pour les chantiers
  assurés avant la résiliation « dans les cas où l'Assuré ne trouverait pas de couverture avec reprise du
  passé auprès de son nouvel assureur », sauf résiliation pour non-paiement ou fraude.
- **Maintien 10 ans au décès du preneur**, à concurrence des montants prévus pour la RC professionnelle, ces
  montants constituant « le maximum par Sinistre et pour la période de 10 ans, sans possibilité de
  reconstitution quelconque ».
- **Portée territoriale : le monde entier à l'exclusion des États-Unis d'Amérique et du Canada**, et
  l'exclusion vise aussi bien les actions intentées sur ces territoires que celles jugées selon leur droit,
  frais de défense compris.
- **La faute lourde est exclue**, et le contrat en donne une définition puis une énumération de faits qui la
  constituent — dont « le fait de laisser ériger des constructions sans examen de sol préalable », « le
  non-respect des normes d'isolement thermique » ou « le contrôle inexistant ou irrégulier de la bonne
  exécution des travaux ». Cette liste est le cœur opérationnel du contrat.
- Aucun montant n'est chiffré dans les conditions générales : sommes assurées et franchise sont toutes
  renvoyées aux Conditions Particulières.

## À surveiller

- **Le régime de déclenchement.** En base réclamation, une résiliation sans reprise du passé chez le nouvel
  assureur laisse une période découverte. C'est précisément ce que les deux clauses de survie ci-dessus
  traitent, et uniquement pour la garantie décennale.
- **La liste des activités déclarées.** Le contrat couvre « l'exercice légal des activités professionnelles
  décrites aux Conditions Particulières » et exclut « toutes activités étrangères à la profession de
  l'Assuré […] notamment celle de promoteur immobilier ou toute autre activité de négoce ».
- **Les honoraires servent d'assiette à la prime**, avec une prime provisoire, une prime minimum et une prime
  définitive arrêtée par décompte. Le contrat définit les trois notions.
- **Un point de la liste des exclusions n'en est pas une** : le point 8 énonce que les responsabilités
  solidaires non acceptées mais mises à charge par une décision judiciaire (condamnation « in solidum »)
  « restent cependant couvertes dans les limites du contrat ». Le fait est enregistré tel qu'imprimé.

## Cadre légal

- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA), annexe I, partie A, branche 13** :
  « R.C. générale — Toute responsabilité autre que celles mentionnées sous les branches 10, 11 et 12. »
- **Loi du 13 décembre 1989 portant organisation des professions d'architecte et d'ingénieur-conseil,
  art. 6** : obligation d'assurance de la responsabilité professionnelle, décennale incluse, salariés inclus.
  Vérifié sur le texte publié au Journal officiel (Legilux, ELI
  `eli/etat/leg/loi/1989/12/13/n1/jo/fr/html`, consulté le 2026-08-03). Legilux ne publie aucune version
  consolidée de cette loi.
- **LSA art. 262, paragraphe 4** (PSA) et **art. 290, paragraphe 4** (courtiers) : assurance de
  responsabilité civile professionnelle obligatoire. Vérifiés dans le texte coordonné publié par le [[CAA]]
  (`Loi_SecteurAssurances_2015-12-07_coord_2026-04-03_ESAP_.pdf`, consulté le 2026-08-03).
- **Non établi** : toute autre profession réglementée porteuse d'une obligation d'assurance.
- Superviseur : [[CAA]].

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[CAA]] · [[Multirisque professionnelle]] · [[Assurances constructions]] ·
  [[Responsabilité civile familiale]] · [[Protection juridique]]

## Sources

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe I partie A, art. 262, art. 283,
  art. 283-1, art. 290.
- Loi du 13 décembre 1989 portant organisation des professions d'architecte et d'ingénieur-conseil, art. 6.
- `_meta/lu-market-census.md` (couvertures obligatoires, détentions de branches, règles de « general good »).
- `_meta/discovery/lu/lalux.md` (bibliothèque énumérée le 2026-08-01 ; identification du porteur).
- `sources/lu/_country.yml`, clé `branches.rc-professionnelle`.
