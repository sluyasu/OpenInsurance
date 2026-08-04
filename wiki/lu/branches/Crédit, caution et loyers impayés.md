---
type: branch
domain: insurance
country: lu
branch: credit-caution
branch_code: "14/15"
lang: fr
langs: [fr]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/credit-caution, branch]
aliases: [Crédit et caution, Assurance-crédit, Caution, Loyers impayés, Garantie locative, Kaution, Mietausfall]
source: null
date: 2026-08-04
freshness: 2026-08-04
status: stub
generated: false
---

## Ce que c'est, et ce que le titre de cette page réunit

Ce libellé recouvre **trois objets que le droit luxembourgeois ne traite pas comme un seul**. C'est un
regroupement éditorial de ce dépôt, dicté par la minceur de la part de détail, et il faut le lire comme tel.
L'annexe I de la LSA, dont le texte est cité ci-dessous, les répartit ainsi :

| Objet | Branche de l'annexe I | Ce que le texte de l'annexe énumère |
|---|---|---|
| Crédit | **14** | insolvabilité générale ; crédit à l'exportation ; vente à tempérament ; crédit hypothécaire ; crédit agricole |
| Caution | **15** | caution directe ; caution indirecte |
| Loyers impayés | **16**, sous « pertes de loyers ou de revenus » | et non 14 ni 15 |

**Les deux premiers sont appariés par la loi elle-même.** L'annexe I, partie B, point g) énonce : « Lorsque
l'agrément porte à la fois […] sur les branches 14 et 15, il est donné sous l'appellation « **Crédit et
caution** » ». Le couple « crédit et caution » est donc une appellation d'agrément du droit luxembourgeois,
pas une invention de ce wiki.

**Le troisième ne l'est pas.** La branche 16, « Pertes pécuniaires diverses », énumère onze postes, dont
« **pertes de loyers ou de revenus** ». C'est là que le texte range la perte de loyer, et pas ailleurs.

**Conséquence, énoncée plutôt que masquée : le champ `branch_code: "14/15"` de cette page ne couvre pas son
propre troisième terme.** Il décrit le couple crédit-caution ; les loyers impayés, tels que l'annexe I les
nomme, relèvent de la 16. Le code n'a pas été élargi ici parce qu'il est déclaré dans
`sources/lu/_country.yml`, qui n'est pas modifié par cette page.

## Comment un produit de loyers impayés peut être monté — et pourquoi on ne le sait pas ici

Trois montages sont concevables à la lecture de l'annexe I : une **caution** donnée au bailleur pour les
obligations du locataire (branche 15), une **couverture de la perte de loyer** subie par le bailleur
(branche 16), ou un **recouvrement** mené au titre d'une [[Protection juridique]] (branche 17).

**Lequel est retenu par un produit luxembourgeois n'est pas établi**, pour la raison la plus simple : aucun
document de ce type n'est entré dans le corpus. Ce paragraphe énumère des possibilités que le texte de
l'annexe autorise ; il n'affirme aucune pratique de marché. Observation et inférence sont séparées ici parce
que c'est précisément le point où elles se confondent facilement.

Un point de droit voisin est en revanche vérifié, et il vaut d'être posé : la **loi modifiée du 21 septembre
2006 sur le bail à usage d'habitation ne comporte aucune obligation d'assurance**, ni pour le locataire ni
pour le bailleur. Sa seule occurrence du mot « assurance » se trouve dans l'article relatif au pacte de
colocation, qui exige que le pacte fixe « les modalités de conclusion des contrats d'approvisionnement et
d'assurance relatifs au bien loué » — une règle de rédaction du pacte, pas un devoir de s'assurer. Ce qui
existe en pratique relève du bail, pas du statut. Le régime de la **garantie locative** elle-même (dépôt,
plafond, forme bancaire) **n'a pas été vérifié** dans cette passe et n'est pas décrit.

## Ce que le registre montre : un socle large, une part de détail invisible

Sur les 44 lignes non-vie du registre du [[CAA]] (35 assureurs luxembourgeois et 9 succursales
étrangères) :

- **branche 16, Pertes pécuniaires diverses : 32 détentions** — c'est la branche la plus détenue des dix-huit ;
- **branche 15, Caution : 16 détentions** ;
- **branche 14, Crédit : 13 détentions**.

Ces chiffres ne disent rien du détail. La branche 16 est large par construction — elle va des risques
d'emploi aux pertes de bénéfices — et un agrément dit ce qu'une entreprise **a le droit** d'écrire, jamais ce
qu'elle écrit. Les porteurs que le recensement de ce dépôt rattache à ces branches sont des opérations
commerciales : Atradius, Greenstars BNP Paribas, SG LuCI, Camca. Une seule entité du registre est
**mono-branche sur la 16**, `BOLTON INTERNATIONAL S.C.A.` — l'un des trois seuls assureurs mono-branche du
marché, avec `FOYER-ARAG` (17) et `DKV LUXEMBOURG` (2).

Côté détail, `sources/lu/_country.yml` nomme un produit, « Assurance loyer impayé » chez Foyer. **Cette
mention est de niveau recensement et n'a pas été corroborée par un document énuméré** : aucune fiche de
découverte luxembourgeoise ne contient d'occurrence de *loyer* ni d'*impayé*, et le porteur concerné ne
publie aucune conditions générales en accès libre. Le produit est donc nommé, et rien de plus.

## Ce que le corpus contient : zéro produit, et un homonyme partout

**Aucun document du corpus luxembourgeois n'est classé dans cette branche.**

Le mot « caution » y est pourtant fréquent, et **jamais au sens de la branche 15**. C'est le piège de lecture
principal de cette page : dans les documents luxembourgeois lus, « caution » désigne presque toujours une
**caution pénale**, c'est-à-dire l'avance d'une somme réclamée par une autorité pour libérer une personne ou
un bien — une garantie d'assistance ou de défense, rangée dans le contrat qui la porte.

- *Assurance BUREAUX DE VOYAGES – Formule 1 et 2* (lalux, branche `voyage`) : garantie « **Avance pour
  caution pénale** », plafonnée à « 5000 EUR » de caution et « 1500 EUR » d'honoraires d'avocat.
- *Luxair Tours – Assistance et Frais d'Annulation ou de Retard* (lalux, branche `voyage`, versions française
  et allemande) : « Assistance en cours de voyage – **Caution pénale** », plafond « maximum 12 500 EUR ».
- *Navigation de Plaisance* (Baloise, branche `autres`) : extension facultative « **Cautionnement** » — « le
  cautionnement qui serait exigé en cas de détention des assurés ou de saisie du bateau suite à un sinistre ».
- *Responsabilité Civile des Dirigeants et Mandataires Sociaux dans les Entreprises* (Baloise, branche
  `rc-professionnelle`) : « les frais de constitution d'une **caution pénale** ».

Le loyer connaît le même sort, à l'inverse : la seule occurrence de *Mietausfall* (perte de loyer) du corpus
figure dans les conditions générales *Zehn- und Zweijahreshaftpflichtversicherung* (lalux, branche
`construction`) comme un dommage immatériel **exclu** — « Die vorliegende Versicherung betrifft weder
immaterielle Schäden wie Mietausfall […] ». Une exclusion de perte de loyer dans un contrat de construction
n'est pas une garantie de loyers impayés.

**Un moteur de recherche sur les alias de cette branche ramènerait donc, dans ce corpus, exclusivement des
faux positifs.** C'est le fait le plus utile qu'elle puisse enregistrer aujourd'hui.

## À surveiller

- **« Caution » est un homonyme.** Caution pénale (avance de fonds dans une garantie d'assistance ou de
  défense) et caution au sens de la branche 15 (engagement de garantie donné à un créancier) sont deux
  objets sans rapport. Le corpus ne contient que le premier.
- **Le libellé de la branche n'est pas un code d'agrément.** « Crédit et caution » l'est (annexe I, partie B,
  point g)) ; « crédit, caution et loyers impayés » ne l'est pas.
- **Où tombe un produit de loyers impayés se lit dans le document, pas dans son nom commercial.** Selon le
  montage, il peut relever de la 15, de la 16 ou être servi comme recouvrement en 17.
- **La comparaison avec la France ne vaut pas preuve ici.** Le dépôt a documenté, côté français, un choix de
  classer les garanties de loyers impayés en `credit-caution` plutôt qu'en habitation. Cela éclaire
  l'intention de la taxonomie ; **cela ne dit rien du droit luxembourgeois**, et aucun document luxembourgeois
  n'a été trouvé pour trancher.

## Lacunes établies

- **Zéro document, zéro produit, zéro assureur dans la branche.** `status: stub` en conséquence.
- **Aucun produit de détail de cette branche n'a été observé sur un document.** Le seul nommé l'est par le
  manifeste pays, sans document à l'appui.
- **Le montage juridique d'un produit luxembourgeois de loyers impayés n'est pas établi** (branche 15, 16 ou
  17).
- **Le régime de la garantie locative n'a pas été vérifié.**
- **Les garanties, exclusions et plafonds typiques ne sont pas écrits**, et ne le seront que depuis des
  documents luxembourgeois.
- **Le `branch_code` de cette page est plus étroit que son libellé**, comme expliqué plus haut. Le manifeste
  n'a pas été modifié.

## Cadre légal

- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA), annexe I** : branche **14**
  (Crédit : insolvabilité générale, crédit à l'exportation, vente à tempérament, crédit hypothécaire, crédit
  agricole) ; branche **15** (Caution : caution directe, caution indirecte) ; branche **16** (Pertes
  pécuniaires diverses, dont « pertes de loyers ou de revenus ») ; **partie B, point g)**, appellation
  « Crédit et caution » pour l'agrément portant à la fois sur les branches 14 et 15.
- **Loi modifiée du 21 septembre 2006 sur le bail à usage d'habitation** : **aucune obligation d'assurance**
  n'y figure ; sa seule occurrence du mot « assurance » relève de l'article sur le pacte de colocation.
- **Loi modifiée du 27 juillet 1997 sur le contrat d'assurance**, pour le régime du contrat.
- **Aucune obligation d'assurance.** `mandatory: false`.
- Superviseur : [[CAA]].

## Related

- [[Protection juridique]] · [[Assurance habitation]] · [[Autres]] · [[Solde restant dû]] · [[CAA]] ·
  [[Exclusion]] · [[00 - Luxembourg MOC]]

## Sources

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe I, texte publié par le Commissariat
  aux Assurances (`caa.lu/uploads/documents/files/LSA_Annexe1.pdf`), consulté le 2026-08-04.
- `_meta/lu-market-census.md` : détentions par branche sur les 44 lignes non-vie ; absence d'obligation
  d'assurance dans la loi du 21 septembre 2006 ; correction du 2026-08-04 sur les trois assureurs
  mono-branche.
- `_meta/discovery/lu/foyer-arag.md` (tableau des assureurs mono-branche).
- `sources/lu/_country.yml`, branche `credit-caution`.
- `data/lu/extracted/lalux/assurance-bureaux-de-voyages-formule-1-et-2-*.json`,
  `luxair-tours-*.json`, `zehn-und-zweijahreshaftpflichtversicherung-*.json` ;
  `data/lu/extracted/baloise/navigation-de-plaisance-*.json`,
  `responsabilite-civile-des-dirigeants-et-mandataires-sociaux-dans-les-entreprises-*.json`.
