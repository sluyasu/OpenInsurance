---
type: branch
domain: insurance
country: lu
branch: solde-restant-du
branch_code: "I"
lang: fr
langs: [fr, de, en]
mandatory: conditional
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/solde-restant-du, branch]
aliases: [Solde restant dû, SRD, Restschuldversicherung, Assurance solde restant dû]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: stub
generated: false
---

## Ce que c'est

L'assurance **solde restant dû** garantit le remboursement du capital encore dû sur un crédit — le
plus souvent immobilier — en cas de décès de l'emprunteur, et selon les contrats en cas d'invalidité
ou d'incapacité. L'indemnité va au prêteur, à hauteur de la quotité assurée.

## Pourquoi ce nom, et pourquoi c'est une branche à part

Le mécanisme est celui que la France appelle *assurance emprunteur*. **Le nom retenu ici est celui
que les documents luxembourgeois impriment**, et ce n'est pas un détail de vocabulaire : importer le
slug `emprunteur` aurait produit une branche dont aucun titre de contrat luxembourgeois ne porte le
libellé, ce qui casse à la fois la reconnaissance automatique et la recherche d'un lecteur.

C'est l'application de la règle qui gouverne toute la taxonomie de ce dépôt : **la segmentation est
celle du marché vu du souscripteur, pas une nomenclature importée**.

## À ne pas confondre avec la prévoyance

La distinction est ténue et le corpus en offre déjà un cas. Un contrat luxembourgeois liste
*« Couvrir un emprunt »* parmi ses objectifs — ce qui pousserait à le classer ici — mais son capital
est **explicitement constant**. Or le propre du solde restant dû est que le capital assuré **décroît
avec l'amortissement du prêt**. Un capital constant qui sert accessoirement à rembourser un crédit
est une [[Prévoyance et décès]], et c'est ainsi qu'il a été classé.

Le critère opérant est donc : **le capital est-il dégressif, ou constant ?**

**Formulé plus strictement, ce critère ne serait pas fondé.** Une première version de cette page
demandait si « le capital suit le tableau d'amortissement ». Or **aucun des deux documents de la
branche n'écrit « tableau d'amortissement », « plan d'amortissement » ni « échéancier »**. Le second
dit « le capital assuré est **dégressif en fonction de la durée du contrat** » — de la durée *du
contrat*, pas de celle du prêt — et ne relie le prêt à la garantie que par son objet, « rembourser
le capital assuré du prêt hypothécaire ».

L'indexation sur un tableau d'amortissement est donc une **inférence sur le mécanisme**, exacte en
pratique mais absente du texte. La règle 4 impose de séparer les deux : le critère retenu ici est
celui que les documents impriment, la dégressivité.

## Obligatoire ou non

`mandatory: conditional`. Aucune disposition luxembourgeoise n'impose cette couverture ; elle est
exigée en pratique par le prêteur comme condition d'octroi du crédit. C'est la même obligation de
fait sans obligation de droit qu'en France — mais **sans l'édifice législatif** que la France a
construit autour d'elle (Lagarde, Hamon, Bourquin, Lemoine), qui organise la délégation et la
substitution d'assurance.

**C'est la différence à retenir pour un lecteur** : les droits de résiliation et de substitution
qu'un emprunteur français tient de la loi n'ont pas d'équivalent automatique ici, et se lisent dans
le contrat.

## État de la documentation

**Trois documents sont placés dans cette branche, pour deux produits** : le contrat lalux existe en
français et en anglais, le contrat Baloise en français seulement. Les deux versions lalux sont
comptées séparément parce que ce sont deux documents distincts — la règle de ce dépôt interdit de
compléter une langue depuis une autre, et rien ne garantit qu'elles disent la même chose.

La comparaison entre les deux porteurs est déjà instructive.

Le second, arrivé avec Baloise, est le **seul document de son éditeur à nommer l'entité vie** :
« Compagnie : Baloise Vie Luxembourg S.A. », là où ses trente-trois frères nomment l'entité non-vie.
Le principe de spécialisation luxembourgeois — une société n'écrit pas à la fois la vie et la
non-vie — se lit donc directement dans le document, et pas seulement au registre du [[CAA]].

C'est aussi **lui qui énonce la dégressivité** : « Le capital assuré est dégressif en fonction de la
durée du contrat », et la prestation est « le capital restant dû à la date du décès ». Deux
garanties, treize exclusions, et **aucun montant** dans tout le document.

Le premier est *Assurance Solde Restant Dû – Assurance hypothécaire*, un document d'information
(IPID), en français.

Ce qu'il permet déjà de dire, et rien de plus :

- Le document se décrit lui-même comme « une forme d'assurance risque dont le but principal consiste
  à couvrir en cas de décès une dette hypothécaire ». **Le critère du capital décroissant énoncé plus
  haut est donc bien celui que le porteur retient**, et il est écrit dans le document.
- Deux garanties : une **garantie principale Décès**, qui rembourse le capital restant dû et les
  intérêts courus depuis la dernière échéance, et une **garantie complémentaire Invalidité permanente
  totale**. Huit exclusions.
- C'est **le seul document du corpus luxembourgeois à nommer le côté vie du porteur** — il imprime
  « LALUX Assurances-Vie », là où les autres s'arrêtent à « LALUX Assurances ». La marque distingue
  donc ici ce que les autres documents laissent indéterminé, sans pour autant donner la forme
  juridique.
- Le document ne porte **aucun montant** : ni capital, ni plafond, ni prime. Ses deux intitulés
  d'encadré sont agrammaticaux tels qu'imprimés, et conservés tels quels.

La page reste en `status: stub` : un IPID de deux pages ne fournit ni les garanties détaillées, ni
les conditions de souscription, ni les modalités de substitution. Les conditions générales de ce
produit ne sont **pas publiées**, ce qui est le cas de quatre-vingt-six documents sur quatre-vingt-dix
chez ce porteur. Ce qui manque sera écrit depuis les documents s'ils paraissent, jamais depuis la
connaissance générale du produit (règle 4).

## Cadre légal

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe II, branche **I** (vie,
  décès, mixtes et rentes non liées à des fonds d'investissement).
- Loi modifiée du 27 juillet 1997 sur le contrat d'assurance, pour le régime du contrat.
- Superviseur : [[CAA]].

## Related

- [[Prévoyance et décès]] · [[CAA]] · [[00 - Luxembourg MOC]]

## Sources

- `sources/lu/_country.yml`, branche `solde-restant-du`.
- `_meta/lu-market-census.md`.
