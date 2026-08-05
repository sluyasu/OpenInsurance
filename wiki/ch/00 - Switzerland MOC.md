---
type: moc
domain: insurance
country: ch
lang: fr
tags: [insurance/ch, moc]
aliases: [Switzerland MOC, Suisse MOC]
date: 2026-08-04
freshness: 2026-08-04
status: stub
generated: false
---

## Suisse — carte du marché

**Cette page est une amorce, et elle le déclare.** Le corpus suisse compte un assureur et trois
documents. Les pages de branche, de régulation et de glossaire n'existent pas encore. Rien ici ne doit
être lu comme une description du marché suisse : c'est la description d'un début d'ingestion.

## Deux superviseurs, répartis par activité

C'est la différence structurelle avec les trois autres pays couverts, et elle se répartit **par
activité, pas par entité juridique** — une même société peut être supervisée par l'OFSP pour son livre
LAMal et par la FINMA pour son livre LCA.

| Pays | Structure |
|---|---|
| Belgique | un superviseur, un régime |
| France | un superviseur, **trois** codes juridiques |
| Luxembourg | un superviseur, une loi |
| Suisse | **deux** superviseurs répartis par activité (FINMA / OFSP) |

- **OFSP/BAG** — l'assurance maladie sociale (LAMal/AOS), sous la LSAMal (RS 832.12).
- **FINMA** — tout ce qui relève de la LCA (RS 961.01), **y compris la complémentaire santé**.

La frontière est dans la clause finale de la LSA (RS 961.01) art. 2 al. 2 let. b, qui écarte de la
surveillance FINMA les entreprises soumises à une surveillance particulière « **dans la mesure de la
surveillance exercée sur cette activité** ». Un recensement doit donc joindre les deux registres au
lieu d'en choisir un.

Conséquence pratique pour la lecture d'un produit suisse : `maladie-base` et
`maladie-complementaire` sont deux régimes distincts, vendus souvent sous la même marque par la même
société. Le premier est social, l'assureur doit accepter tout candidat ; le second relève de la LCA,
avec questionnaire de santé et droit de refus. Les confondre est l'erreur de lecture la plus facile
à commettre sur ce marché.

## Assureurs

<!-- BEGIN GENERATED: insurers -->
- [Vaudoise Assurances](<insurers/Vaudoise Assurances.md>) (12 documents)
<!-- END GENERATED -->

Un seul porteur est entré dans le corpus, et partiellement : **13 documents énumérés dans
`sources/ch/vaudoise.yml`, 12 PDF téléchargés, 3 extraits** au 2026-08-04. Le décompte à jour est la
liste ci-dessus, maintenue par `pipeline/build_wiki.py`, et le tableau de couverture d'`AGENTS.md`.

Le recensement des porteurs est fait, l'ingestion ne l'est pas. Relevé dans
`_meta/ch-market-census.md` (registres consultés le 2026-07-21) : **190 entreprises d'assurance** au
registre FINMA, et **32 assureurs LAMal** pratiquant l'assurance de base, plus cinq qui ne pratiquent
que l'indemnité journalière. La liste d'ingestion classée, les hubs de conditions générales
atteignables et les blocages constatés — dont Helvetia, rejeté activement et enregistré comme
blocage plutôt que maquillé — figurent dans ce même fichier.

## Branches

La taxonomie est écrite et non exercée : **21 branches déclarées** dans `sources/ch/_country.yml`,
**3 rencontrées** dans les documents extraits (`batiment`, `protection-juridique`, `vehicules`).
**Aucune page de branche n'est écrite** — `wiki/ch/branches/` ne contient que sa MOC.

Quatre traits de la taxonomie suisse n'ont pas d'équivalent direct ailleurs dans ce dépôt, et sont
documentés en commentaire dans le manifeste de pays :

- **`batiment`** — 19 cantons exploitent un **monopole public** (ECA). Une page produit peut donc,
  par construction légale, n'avoir aucun concurrent à qui se comparer.
- **`menage`** — le contenu seulement. C'est la moitié de l'`habitation` belge ; le bâtiment relève
  d'un régime séparé.
- **`lpp`** — la prévoyance professionnelle du 2e pilier, hors FINMA (LSA art. 2 al. 2 let. b).
- **Pas de `velo`** — la vignette vélo a été abolie en 2012 ; la responsabilité du cycliste est
  absorbée par `rc-privee`.

## Portée et limites

Les lacunes, énoncées plutôt que tues (règle 6) :

- **Un assureur, trois documents.** Aucune conclusion de marché ne peut être tirée du corpus actuel.
- **Aucune page de branche, de régulation ni de glossaire.** La couche rédigée à la main, qui existe
  en Belgique et partiellement en France et au Luxembourg, est ici entièrement à écrire.
- **Les intitulés de section des pages produit sont codés en dur en français** dans
  `pipeline/render.py`. Sans équivalent en allemand et en italien, les deux tiers linguistiques du
  pays ne peuvent pas être rendus correctement. C'est le prérequis technique à toute extension
  au-delà de la Suisse romande.

Sur la position juridique du projet en Suisse — le déclencheur y est **l'intérêt économique à la
conclusion d'un contrat**, pas la comparaison (OS RS 961.011 art. 182a al. 3) — voir la règle 1 de
`CLAUDE.md` et la section « Legal position » de `_meta/ch-market-census.md`.

## Related

- [[00 - Branches MOC]] · [[00 - Luxembourg MOC]]
