---
type: regulation
domain: insurance
country: lu
lang: fr
tags: [insurance/lu, regulator, regulation]
aliases: [CAA, Commissariat aux Assurances]
source: https://www.caa.lu/
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Ce que c'est

Le **Commissariat aux Assurances** est l'établissement public qui agrée et supervise les entreprises
d'assurance et de réassurance établies au Luxembourg, ainsi que les intermédiaires. Contrairement à
l'[[ACPR]] française, adossée à la Banque de France et compétente pour la banque comme pour
l'assurance, le CAA est un superviseur **sectoriel** : la banque relève de la CSSF.

Un superviseur, une loi d'agrément — la **loi modifiée du 7 décembre 2015 sur le secteur des
assurances** (« LSA ») — et une loi de contrat, la **loi modifiée du 27 juillet 1997 sur le contrat
d'assurance**. C'est le schéma le plus simple des quatre pays couverts par ce wiki : la Belgique a
un superviseur et un régime, la Suisse deux superviseurs répartis par activité, la France un
superviseur et trois codes.

## Le trait qui distingue ce marché n'est pas la supervision

Il est ailleurs, et il est chiffré dans le recensement du dépôt (`_meta/lu-market-census.md`) à
partir des annexes du rapport annuel du CAA, exercice 2025 :

| | Primes totales | dont Luxembourg | part domestique |
|---|---|---|---|
| Vie | 35 095 771 k€ | 1 765 819 k€ | **5,0 %** |
| Non-vie | 19 918 771 k€ | 1 735 762 k€ | **8,7 %** |

La France seule représente plus de la moitié de la production vie écrite depuis le Luxembourg. À
quoi s'ajoutent **207 entreprises de réassurance** agréées, très majoritairement des captives de
groupes étrangers qui n'écrivent aucun contrat de particulier.

Autrement dit : **le nombre d'agréments n'est pas la taille du marché de détail**. Soixante-trois
assureurs directs luxembourgeois existent ; moins de dix vendent un produit à un résident. C'est la
raison pour laquelle ce wiki documente peu d'assureurs luxembourgeois, et ce n'est pas une lacune de
la collecte.

## Le registre

Publié sur `caa.lu/fr/operateurs`, une liste HTML par catégorie, chacune assortie d'un **export CSV**
servi anonymement en HTTP simple et régénéré chaque nuit. Il n'existe pas d'API de requête — rien
d'équivalent à l'Opendatasoft de l'ACPR — mais un vidage plat par liste suffit à établir la
population.

Deux points de méthode relevés lors du recensement (2026-08-02) :

- **Les listes vie et non-vie ne se recoupent pas.** Le Luxembourg applique le principe de
  spécialisation : aucune société luxembourgeoise n'est à la fois assureur vie et non-vie. C'est une
  différence directe avec la France, où un même groupe détient des entités des deux côtés mais où
  certaines sociétés portent des agréments mixtes.
- **Les deux listes de libre prestation de services n'ont pas d'export CSV** et ont dû être lues en
  HTML : 628 notifications entrantes non-vie et 128 vie. Ces entités ne détiennent aucun agrément
  luxembourgeois ; elles sont agréées ailleurs et notifient leur activité ici.

## Ce que le CAA impose aux documents, et ce que le corpus en montre

La LSA transpose la directive sur la distribution d'assurances, donc le document d'information
standardisé existe ici comme ailleurs — *document d'information sur le produit d'assurance* en
français, *Informationsblatt zum Versicherungsprodukt* en allemand.

Le corpus permet une observation sur son application, formulée comme un constat et non comme un
jugement : sur les documents extraits d'un assureur de détail luxembourgeois, **une majorité porte au
moins un intitulé de rubrique faux ou contredit par son contenu**, et plusieurs manquent entièrement
une rubrique du format. Le détail, les comptes et leurs limites figurent dans
`_meta/discovery/lu/lalux.md`.

## Langues

La **loi du 24 février 1984 sur le régime des langues** fait du luxembourgeois la langue nationale
(art. 1er) et du français la langue des actes législatifs (art. 2), l'administration pouvant employer
« les langues française, allemande ou luxembourgeoise » (art. 3).

Les lois d'assurance ne les énumèrent pas : la loi du 27 juillet 1997 art. 16 point 2 dispose que
« les contrats ne sont valables que s'ils sont rédigés dans l'une des langues officielles du
Grand-Duché de Luxembourg ou dans une langue comprise par le preneur d'assurance ».

**Mesuré : aucun document contractuel en lëtzebuergesch n'a été trouvé sur ce marché** — et pour une
raison plus intéressante que l'absence, puisqu'un assureur maintient un hub `/lu/` complet qui liste
quatre-vingt-dix PDF, tous en français, allemand, anglais ou portugais. La langue de l'interface
n'est pas celle des documents.

## La règle 1 au Luxembourg

La LSA **art. 281-1, paragraphe 2, point d)** exclut du champ de la distribution d'assurances :

> la simple fourniture d'informations sur des produits d'assurance ou de réassurance, sur un
> intermédiaire d'assurances, un intermédiaire de réassurances, une entreprise d'assurance ou de
> réassurance à des preneurs d'assurance potentiels, lorsque le fournisseur ne prend pas d'autres
> mesures pour aider le client à conclure un contrat d'assurance ou de réassurance.

L'**art. 279, 16 f)** ne saisit le classement et la comparaison que lorsque le client « peut conclure
le contrat directement ou indirectement par ce biais ».

Deux particularités locales méritent d'être notées, parce qu'elles déplaceraient l'analyse si ce
projet changeait de nature :

- L'**art. 295-10 §1** fait du **conseil** le régime par défaut pour un client résidant au Luxembourg.
- L'exception de courte citation du droit d'auteur luxembourgeois (loi du 18 avril 2001, art. 10, 1°)
  est expressément conditionnée à ce que les citations « ne poursuivent pas un but de lucre ».

Une monétisation casserait donc l'analyse **deux fois** ici, là où en Suisse elle n'en cassait qu'une.

## Related

- [[00 - Luxembourg MOC]] · [[ACPR]]

## Sources

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, art. 279, 281-1, 295-10.
- Loi modifiée du 27 juillet 1997 sur le contrat d'assurance, art. 16, 17, 17-1.
- Loi du 24 février 1984 sur le régime des langues.
- Loi du 18 avril 2001 sur les droits d'auteur, art. 10.
- Registre du CAA, `https://www.caa.lu/fr/operateurs`, consulté le 2026-08-02.
- Rapport annuel du CAA, annexes de l'exercice 2025.
