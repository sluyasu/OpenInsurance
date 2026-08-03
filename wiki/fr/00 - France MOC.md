---
type: moc
domain: insurance
country: fr
lang: fr
tags: [insurance/fr, moc]
aliases: [France MOC, France]
date: 2026-07-30
status: ready
generated: false
---

## France - carte du marché

Le marché français de l'assurance est supervisé par une seule autorité, l'[[ACPR]] (Autorité de contrôle
prudentiel et de résolution, adossée à la Banque de France), mais les organismes qui le composent relèvent de
**trois codes différents**, et le code détermine la forme juridique, la gouvernance et une partie de la gamme :

| Code | Type d'organisme | Organismes agréés |
|---|---|---|
| Code des assurances | sociétés anonymes, sociétés d'assurance mutuelles | 310 |
| Code de la mutualité | mutuelles, unions de mutuelles | 286 |
| Code de la sécurité sociale | institutions de prévoyance | 32 |

C'est la différence structurelle avec les deux autres pays couverts : la Belgique a un superviseur et un
régime, la Suisse a deux superviseurs répartis par activité, la France a un superviseur et trois régimes.
Le registre officiel est publié par l'ACPR sous le nom **Refassu** et régénéré quotidiennement. Le détail,
les chiffres et leur source figurent dans le recensement de marché du dépôt (`_meta/fr-market-census.md`).

Attention aux faux amis : une *mutuelle* est un organisme régi par le Code de la mutualité, et dans l'usage
courant « ma mutuelle » désigne la complémentaire santé elle-même ; une *société d'assurance mutuelle* est un
organisme régi par le Code des assurances. Les deux se traduisent par « mutual » et ne recouvrent pas la même
chose.

## Distributeurs et porteurs de risque

Trois relations distinctes ont été rencontrées dans le corpus, et les confondre change qui répond :

- **La distribution.** Une marque mandataire ou courtier vend le papier d'un porteur. Direct Assurance
  distribue de l'AXA France IARD ; Luko trade sous une entité allemande supervisée par la BaFin.
- **Le partage par garantie.** Un même contrat nomme plusieurs assureurs, chacun sur son bloc — protection
  juridique chez une filiale dédiée, assistance chez un GIE. Un contrat MAAF en porte quatre, dont une
  garantie *assurée* par la mutuelle mais *gérée* par une autre entité : assureur et gestionnaire ne sont pas
  la même question.
- **La substitution**, propre au Code de la mutualité. Une mutuelle reste l'assureur nommé au contrat mais une
  autre assume ses engagements et son exigence de solvabilité. Mesuré sur la Garantie Santé des Territoriaux :
  *assurée par la MNFCT, substituée par Apivia Macif Mutuelle*, Macif n'étant que distributeur. Trois
  organismes, trois rôles, une seule marque sur la couverture.

### Combien de fois, mesuré

Le pipeline enregistre chaque document dont le **texte nomme un porteur autre que l'entité dont la bibliothèque
publique l'a fourni**. Le décompte se recalcule depuis le dépôt — il augmente à chaque vague d'extraction, donc
tout chiffre écrit ici est un instantané :

```bash
grep -rl "Porteur de risque:" data/*/extracted/ | wc -l
```

**Au 2026-08-03 : trente-neuf documents, dix-sept dénominations imprimées.** Les plus fréquentes sont MAAF
Santé (10), Matmut & Co (5), Inter Mutuelles Entreprises et Mutuelle Ociane (3 chacune).

**Compter les dénominations surestime le nombre de porteurs, et le corpus le montre crûment.** Le SIREN
**779 558 501** apparaît sous **quatre noms** : « Apivia Macif Mutuelle », « Macif Santé Prévoyance »,
« Macif-Mutualité » — et c'est aussi lui qui **substitue** la MNFCT (784 442 899) sur un contrat. Une seule
personne morale, quatre libellés, selon l'édition et selon le rôle. Les éditions récentes impriment même un
siège différent (Niort au lieu de Paris 15ᵉ).

**C'est le numéro d'immatriculation qui identifie une personne morale, jamais la dénomination.** C'est aussi
lui qui permet de reconnaître un changement de nom au lieu d'inventer un porteur de plus — une première
version de cette page comptait deux de ces libellés comme deux entités distinctes.

**Et la bibliothèque de publication ne dit rien du groupe.** Quatre documents publiés sous le slug `macif` ne
sont assurés ni par la Macif ni par aucune entité de son groupe : deux le sont par **AXA France IARD / AXA
France Vie** (assurances de carte bancaire souscrites par Visa Europe Limited — le mot « Macif » n'apparaît
nulle part en huit pages), deux par **Fragonard Assurances**. Le slug reste celui de la bibliothèque ; la
divergence est dans `gaps`.

Deux autres lectures s'en dégagent, et aucune ne se déduirait des registres seuls.

**Une marque de détail recouvre couramment plusieurs personnes morales, sous des régimes différents.** Matmut
en réunit une société d'assurance mutuelle, une société anonyme, plusieurs organismes du Code de la mutualité
(dont Mutuelle Ociane), une société de vie et une SA à directoire partagée avec Macif. Macif en réunit une
mutuelle du Livre II, une société de vie et un GIE d'assistance.

**Et la répartition n'est jamais la même d'un contrat à l'autre chez un même assureur.** Sur les seuls contrats
MAAF : quatre nomment la mutuelle, deux nomment MAAF Vie, un fait de Covéa Protection Juridique à la fois
l'assureur et le gestionnaire selon la garantie, un autre confie la protection juridique à Assistance
Protection Juridique SA. Il n'y a pas de « structure MAAF » à apprendre une fois — elle se lit contrat par
contrat, et souvent garantie par garantie.

Le slug d'un assureur dans ce dépôt désigne donc **la bibliothèque qui publie**, jamais le porteur du risque.

**Et le champ `insurer_name` ne peut pas porter cette information.** Il sert à regrouper les pages sous une
fiche assureur et doit rester stable ; la lecture du document part donc dans `gaps`, document par document. Le
schéma n'ayant pas de champ `carrier`, c'est le seul endroit où le fait tienne sans invalider les extractions
existantes — et c'est cherchable.

En France, une marque grand public n'est pas nécessairement un assureur. Beaucoup de marques sont des
**mandataires ou courtiers inscrits à l'ORIAS** qui distribuent le papier d'un porteur de risque. Le registre
de l'ACPR liste les porteurs de risque ; l'ORIAS liste les intermédiaires. Chaque document contractuel nomme
lui-même son assureur, sous une rubrique « Assureur » ou « Qui vous assure ? », parce que la directive sur la
distribution d'assurances l'impose : l'attribution se lit donc dans le document, elle ne se déduit pas de la
marque.

## Branches

La segmentation retenue ici est celle du marché français vu du souscripteur. Chaque branche porte, quand elle
existe, la référence à la nomenclature prudentielle de l'**article R. 321-1 du Code des assurances**, qui est
le découpage sur lequel l'ACPR délivre les agréments.

- [[Assurance auto]] (RC obligatoire, art. L. 211-1)
- [[Multirisque habitation]]
- [[Complémentaire santé]]
- [[Assurance emprunteur]]
- [[Assurance construction]]
- Autres branches : voir [[00 - Branches MOC]]

Trois branches n'ont d'équivalent ni en Belgique ni en Suisse et sont proprement françaises :
l'[[Assurance emprunteur]], l'[[Assurance construction]] (décennale et dommages-ouvrage, loi du 4 janvier
1978) et l'assurance des [[EDPM et mobilités douces]], rendue obligatoire par le décret du 23 octobre 2019.

Toute branche effectivement peuplée par les produits documentés a sa fiche conceptuelle dans `branches/`.
Les branches déclarées dans la taxonomie mais encore sans produit (transport, crédit et caution, cyber) n'en
ont pas : `make validate` les signale une par une plutôt que de les passer sous silence.

La branche `autres` est le repli de la taxonomie, pas un segment de marché ; sa taille est un indicateur de
qualité du découpage, et sa croissance appellerait la création d'une branche — comme l'a fait le [[Vélo]],
né d'un contrat que le classement en [[EDPM et mobilités douces]] aurait mal décrit.

## Assureurs documentés

<!-- BEGIN GENERATED: insurers -->
- [Direct Assurance](insurers/Direct%20Assurance.md) (11 documents)
- [Gan Assurances](insurers/Gan%20Assurances.md) (50 documents)
- [Groupama](insurers/Groupama.md) (31 documents)
- [Luko](insurers/Luko.md) (14 documents)
- [MAAF](insurers/MAAF.md) (92 documents)
- [Macif](insurers/Macif.md) (151 documents)
- [MAIF](insurers/MAIF.md) (69 documents)
- [Matmut](insurers/Matmut.md) (200 documents)
- [SMACL Assurances](insurers/SMACL%20Assurances.md) (111 documents)
- [Thélem assurances](insurers/Th%C3%A9lem%20assurances.md) (45 documents)
<!-- END GENERATED -->

## Portée et limites

Le document public standard en France est l'**IPID** (document d'information sur le produit d'assurance,
format imposé au niveau européen). Les conditions générales sont publiées par certains assureurs et remises
seulement à la souscription par d'autres. Le corpus français est donc plus riche en IPID qu'en conditions
générales, ce qui est une observation sur la pratique de publication, pas un manquement des assureurs :
publier l'IPID est une obligation, publier les conditions générales n'en est pas une.

Le contraste entre les trois codes se lit d'ailleurs directement dans ce qui est publié. Un organisme du
**Code de la mutualité** n'émet pas de conditions générales : son instrument contractuel est le **règlement
mutualiste**, adopté par l'assemblée générale avec les statuts. L'adhérent n'est pas un souscripteur, et les
termes se modifient par vote et non par accord entre deux parties. Or ce règlement est le plus souvent
« remis lors de l'adhésion » plutôt que publié — c'est le cas chez la MGEN, l'une des plus grandes mutuelles
du pays, dont les 288 pages publiques ne contiennent qu'un seul IPID et aucun règlement qui aboutisse
(détail et sources : `_meta/discovery/fr/mgen.md`). Autrement dit, pour une part du marché, les termes
opérants ne sont par construction pas consultables avant d'adhérer.
