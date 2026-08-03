---
type: branch
domain: insurance
country: lu
branch: habitation
branch_code: "8/9/13"
lang: fr
langs: [fr, de, en]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/habitation, branch]
aliases: [Habitation, Assurance habitation, Incendie, Logement, Hausrat, Gebäude, Household]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Ce que c'est

L'assurance habitation réunit dans un seul contrat la couverture des dommages au logement et à son contenu.
Elle couvre trois branches de l'**annexe I, partie A de la LSA** — 8 *Incendie et éléments naturels*,
9 *Autres dommages aux biens* et 13 *R.C. générale* pour le volet responsabilité — et le marché
luxembourgeois la vend comme la France : **bâtiment et contenu dans le même acte**, sans la séparation
ménage / bâtiment du marché suisse.

Une particularité locale : la [[Responsabilité civile familiale]] a son propre article dans ce wiki alors
qu'elle se souscrit le plus souvent comme une garantie du contrat habitation. Ce n'est pas un choix
d'éditeur : le [[CAA]] la mesure séparément dans ses propres statistiques, sous « 13. RC générale /
a) RC familiale ». Le contrat habitation du corpus se contente d'indiquer que « la Responsabilité Civile
(hors automobile) des personnes vivant dans ce logement et la Responsabilité Civile Immeuble **peuvent
également être couvertes** », sans en décrire ni l'étendue ni les plafonds.

## L'assurance du locataire n'est pas obligatoire au Luxembourg

C'est la différence la plus nette avec la France, et elle a été vérifiée dans le texte plutôt que supposée.

La ***loi modifiée du 21 septembre 2006 sur le bail à usage d'habitation*** ne contient **aucune obligation
d'assurance à la charge du locataire**. Contrôle effectué sur la version consolidée au 1er août 2024 — la
dernière que publie Legilux — le 2026-08-03 : le mot « assurance » n'apparaît que **deux fois** dans tout le
statut, et une seule de ces occurrences est dans le corps de la loi. Il s'agit de l'**article 2 ter,
paragraphe (2), point 4°**, dans le chapitre I bis sur la colocation, qui impose au pacte de colocation de
régler « les modalités de conclusion des contrats d'approvisionnement et d'assurance relatifs au bien loué ».

C'est une **règle de rédaction du pacte, pas une obligation d'assurer** : la loi exige que les colocataires
disent entre eux comment les contrats seront conclus, elle n'exige de personne qu'il en conclue un. L'autre
occurrence figure dans la liste des lois modifiées citées en tête du texte consolidé et concerne des
cotisations d'assurance sociale, sans rapport avec le bail.

Le contraste avec la France est net et il porte sur le texte, pas sur la pratique : la page française
[[Multirisque habitation]] rattache l'obligation du locataire à la **loi n° 89-462 du 6 juillet 1989,
art. 7 g)**, dont le défaut est un motif de résiliation du bail. Rien de tel ici, ni d'équivalent aux régimes
wallon et bruxellois.

**En pratique, l'assurance est très largement imposée par les bailleurs par voie contractuelle.** C'est un
fait sur les baux, pas sur la loi, et il doit être lu comme tel : un bailleur peut l'exiger, un locataire
luxembourgeois qui ne s'assure pas ne contrevient à aucun texte.

Le champ `mandatory` de cette branche vaut donc **`false`**, contre `conditional` en France.

## Ce que le corpus documente

Un seul produit : *easyPROTECT Habitation* (lalux), IPID de deux pages, décliné en **trois formules
cumulatives** — SÉCURITÉ, puis CONFORT = SÉCURITÉ + garanties supplémentaires, puis PERFORMANCE = CONFORT +
garanties supplémentaires — pour « une maison, un appartement ou une copropriété » et « que vous soyez
propriétaire, co-propriétaire ou locataire ».

- **SÉCURITÉ** : incendie (fumée, suie, foudre, explosions, implosions) ; dégâts électriques et dégâts
  ménagers, décongélation des provisions ; dégâts des eaux, infiltrations à travers toitures ou balcons,
  gel ; bris de glaces ; « tempête, grêle, tornade et tremble de terre » (coquille du document, voir plus
  bas), pression de la neige et de la glace.
- **CONFORT** : vol du mobilier (par effraction ou agression), détériorations immobilières résultant du vol,
  attentats, vandalisme et graffiti.
- **PERFORMANCE** : aménagements extérieurs ; bris et vol des effets personnels et objets de loisirs ; périls
  climatiques (refoulement des égouts, inondation) ; valeur à neuf du mobilier, de l'électroménager et du
  multimédia ; bris et vol des appareils multimédia, numériques et instruments de musique ; reconstruction
  sur base de nouvelles normes. Chacune de ces six garanties porte la mention imprimée « en option pour
  CONFORT ».
- **Extensions optionnelles pour CONFORT et PERFORMANCE** : mobilier au premier risque ; installations de
  piscines et jacuzzis ; bris des appareils énergie verte (chauffages à condensation, installations
  photovoltaïques, partie vitrée des panneaux comprise) ; **bris et vol des engins de mobilité douce —
  « vélos, vélos à assistance électrique, trottinettes etc. allant jusqu'à maximum 25 km/h »** ; bris et vol
  des objets de valeur « d'une valeur supérieure à 1.500 € ».
- **Hors formules**, sans rattachement indiqué : assurance voyage annuelle, Home Assistance 24 h/24, et
  easyPROTECT Discover pour les 15-27 ans, qui fait l'objet d'un document séparé.

**Portée** : « à l'adresse du risque indiquée aux conditions particulières du contrat, située au Grand-Duché
de Luxembourg », avec des extensions prévues en cas de déménagement, de déplacement temporaire du mobilier,
de logement étudiant ou de résidence de vacances. En cas de déménagement **hors** du Grand-Duché, le contrat
n'est pas reconduit tacitement.

## À surveiller

- **Le seuil de 25 km/h sur les engins de mobilité douce** est le seul critère technique chiffré du contrat,
  et le même nombre figure dans la loi — sans que les deux se recouvrent exactement. La *loi modifiée du
  16 avril 2003 relative à l'assurance obligatoire de la responsabilité civile en matière de véhicules
  automoteurs*, **art. 1er a)** tel que modifié par la loi du 29 mars 2024, soumet à l'assurance obligatoire
  les véhicules automoteurs « avec, **soit** une vitesse maximale par construction supérieure à 25 km/h,
  **soit** un poids net maximal supérieur à 25 kg **et** une vitesse maximale par construction supérieure à
  14 km/h ». Le seuil du contrat ne porte que sur la vitesse ; le critère légal a **deux branches**, dont une
  de poids. Un engin de plus de 25 kg roulant à plus de 14 km/h relève de l'assurance obligatoire même s'il
  reste sous 25 km/h, et donc de [[Assurance auto]] ou de [[Deux-roues motorisés]]. Le seuil de l'extension
  habitation est un critère d'éligibilité contractuelle, pas le test légal.
- **L'inoccupation** : le vol n'est pas couvert au-delà de **45 jours consécutifs** d'inoccupation des
  locaux, et les bâtiments totalement inoccupés ou à démolir sont exclus en général.
- **Les obligations propres à la garantie vol** : employer les moyens de fermeture et de protection prévus,
  et déposer plainte immédiatement auprès des autorités compétentes.
- **La responsabilité civile n'est pas décrite.** Le document ne dit rien de son étendue, de ses plafonds ni
  de ses exclusions. Voir [[Responsabilité civile familiale]].

## Poids de la branche

Mesuré sur les annexes du rapport annuel du [[CAA]], exercice 2025 : la branche 8 « Incendie et éléments
naturels » représente **207 214 k€** de primes émises sur les opérations luxembourgeoises, dont **129 236 k€**
pour le sous-poste « risques simples d'habitation » ; la branche 9 « Autres dommages aux biens » ajoute
**192 303 k€**, dont une partie seulement est domestique. L'indicateur par habitant du superviseur donne
**188 €/habitant** pour l'incendie risques simples d'habitation, et **57,93 %** des primes de ce poste sont
écrites sur des risques luxembourgeois — la troisième branche la plus domestique du marché, après la
[[Responsabilité civile familiale]] et la [[Protection juridique]].

## Lacunes établies

- **Aucune condition générale habitation n'est publiée.** L'IPID renvoie aux « conditions générales et/ou
  particulières relatives au produit d'assurance choisi » sans les nommer, les dater ni les référencer, et
  aucun document de ce type n'existe sur le site de l'assureur pour ce produit.
- **Aucun plafond, aucune franchise, aucune somme assurée** ne figurent dans le document. Les deux seules
  valeurs chiffrées imprimées — 25 km/h et 1.500 € — sont des seuils d'éligibilité, pas des plafonds
  d'indemnisation.
- **Aucune date d'édition n'est imprimée**, alors même que le nom du fichier source porte « 2023 ». Le
  millésime du nom de fichier n'a pas été promu en donnée. Aucun porteur n'est nommé au sens juridique : le
  document imprime « LALUX Assurances » puis « la compagnie », sans forme sociale ni numéro RCS.
- **Les listes sont expressément non exhaustives** : la mention « Liste non exhaustive » est imprimée trois
  fois en page 1. Les 25 garanties et 13 exclusions relevées sont tout ce que le document imprime, mais pas,
  de son propre aveu, tout ce que contient le contrat.
- **Deux défauts éditoriaux conservés tels quels**, parce qu'une citation doit rester une portion exacte du
  document : un intitulé « **Garanties accessoires** » imprimé en gras à la fin du bloc SÉCURITÉ **sans aucun
  contenu en dessous** — le document ne dit pas de quelles garanties il s'agit ; et la garantie imprimée
  « Tempête, grêle, tornade et **tremble de terre** ». Les deux ont été vérifiés au rendu et ne sont pas des
  artefacts d'extraction.
- **Un seul produit, un seul assureur.** L'habitation est l'une des quatre lignes qui *font* le marché de
  détail luxembourgeois ; le corpus n'en documente qu'un contrat, sur les quatre porteurs de détail du pays.

## Cadre légal

- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA), annexe I, partie A**, branches 8, 9
  et 13. Vérifié dans le texte coordonné publié par le [[CAA]]
  (`Loi_SecteurAssurances_2015-12-07_coord_2026-04-03_ESAP_.pdf`, consulté le 2026-08-03).
- **Loi modifiée du 21 septembre 2006 sur le bail à usage d'habitation** : **aucune obligation d'assurance du
  locataire**. Seule occurrence du mot dans le corps du texte : **art. 2 ter, paragraphe (2), point 4°**
  (contenu obligatoire du pacte de colocation). Vérifié sur la version consolidée au 2024-08-01 servie par
  Legilux (ELI `eli/etat/leg/loi/2006/09/21/n1/consolide/20240801/fr/html`, consultée le 2026-08-03).
- **Loi modifiée du 16 avril 2003 relative à l'assurance obligatoire de la responsabilité civile en matière
  de véhicules automoteurs, art. 1er, point a)**, tel que modifié par la loi du 29 mars 2024, pour les deux
  bornes citées ci-dessus. Vérifié dans le texte coordonné publié par le [[CAA]]
  (`Loi_RCVTA_2003-04-16_coord_2024-04-06.pdf`, consulté le 2026-08-03).
- Comparaison France : **loi n° 89-462 du 6 juillet 1989, art. 7 g)**, citation de la page
  [[Multirisque habitation]] du corpus français ; non revérifiée contre le texte français dans cette passe.
- Superviseur : [[CAA]].

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[CAA]] · [[Responsabilité civile familiale]] · [[Protection juridique]] · [[Voyage et assistance]] ·
  [[Crédit, caution et loyers impayés]] · [[Autres]]

## Sources

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe I partie A.
- Loi modifiée du 21 septembre 2006 sur le bail à usage d'habitation, version consolidée au 2024-08-01,
  art. 2 ter (2) 4°.
- `_meta/lu-market-census.md` (couvertures obligatoires ; tab. 3.23, 3.26 et 3.27 du rapport annuel 2025).
- `_meta/discovery/lu/lalux.md` ; `sources/lu/_country.yml`, clé `branches.habitation`.
