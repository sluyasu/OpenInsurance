---
type: product
domain: insurance
country: fr
insurer: '[[Macif]]'
insurer_slug: macif
branch: assurance-vie
product_name: Multi Vie
document_type: conditions_tarifaires
target_audience: null
target_audience_note: null
reference: MUT/ FC/ FRAIS/MV - 06/24
edition_date: 2024-06
lang: fr
tags:
- insurance/fr/assurance-vie
- product
- insurer/macif
aliases:
- Multi Vie
source_url: https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_banque/MultiVie-Frais.pdf
source_pages: 1
fetched_at: '2026-08-01'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: multi-vie
variant: null
edition_status: null
edition_age_years: 2
superseded: true
extends: null
freshness: '2026-08-01'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Tableau standardisé des frais du contrat d'assurance vie Multi Vie, sur une page, édition JUIN 2024. Il présente le montant minimal de versement initial (50 €), les frais annuels (frais de gestion du contrat par support, frais de gestion des unités de compte en gestion libre avec la part rétrocédée au distributeur, autres frais annuels) et les frais ponctuels par opération (versement, arbitrage, changement de mode de gestion, transfert sortant, versements de rente, rachat). Le contrat est assuré par Mutavie SE, entreprise régie par le Code des assurances. Le document ne décrit ni les garanties ni les modalités contractuelles : il ne porte que sur les frais du dernier exercice clos.

- Assureur : [Macif](../../insurers/Macif.md) · Branche : [Assurance vie et épargne](../../branches/Assurance%20vie%20et%20%C3%A9pargne.md) · Type : Conditions tarifaires · Édition : 2024-06

## Définitions

| Terme | Définition | Page |
|---|---|---|
| NA | non applicable. | p. 1 |
| fonds actions | La catégorie “fonds actions” inclut les ETF et mais exclut les fonds de capital-investissement (FCPR, FPCI, FPS) et les titres vifs. [note (2) — la formulation « inclut les ETF et mais exclut » est reproduite telle qu'imprimée] | p. 1 |
| taux de rétrocessions de commissions | Part des frais reversés au profit du distributeur et, du gestionnaire du contrat au cours du dernier exercice clos. [note (3) — ponctuation reproduite telle qu'imprimée] | p. 1 |
| fonds immobilier | La catégorie “fonds immobilier” inclut les OPCI, les SCPI et les SCI. [note (4)] | p. 1 |

## Prime

- Montant minimal de versement initial : 50 €.
- Frais sur versement : 0%.
- Frais de rachat : 0%.
- Frais d'arbitrage, proportionnels ou forfaitaires : 0,10% avec un minimum de 5€ et un maximum de 30 € ; nombre d'arbitrages gratuits par an : 0.
- Frais de gestion du contrat : 0,60% sur le support fonds en euros comme sur le support unités de compte ; NA pour le support Eurocroissance et pour la gestion pilotée ou standardisée.
- Frais de gestion des unités de compte en gestion libre : fonds actions 1,46% (dont 0,80% de rétrocessions), fonds diversifiés 1,00% (dont 0,63%) ; fonds obligations et fonds immobilier NA.
- Frais de changement de modes de gestion, frais de transfert sortant vers un autre produit, frais sur les versements de rente, autres frais annuels forfaitaires et proportionnels : NA.
- « Le tableau indique les principaux frais du contrat au dernier exercice clos. Il peut cependant subsister des frais ne figurant pas dans ce tableau. » — le tableau n'est donc pas exhaustif de son propre aveu.
- L'exercice de référence n'est pas daté dans le document : il n'est désigné que par « le dernier exercice clos ».

## Conditions particulières

- 50 € p. 1
- 0,60% p. 1
- 0,60% p. 1
- NA p. 1
- NA p. 1
- 1,46% p. 1
- 0,80% p. 1
- NA p. 1
- NA p. 1
- NA p. 1
- NA p. 1
- 1,00% p. 1
- 0,63% p. 1
- NA p. 1
- NA p. 1
- NA p. 1
- NA p. 1
- 0% p. 1
- NA p. 1
- 0,10% avec un minimum de 5€ et un maximum de 30 € p. 1
- 0 p. 1
- NA p. 1
- NA p. 1
- 0% p. 1
- « Le contrat Multi Vie est assuré par Mutavie. » MUTAVIE SE - Société européenne à Directoire et Conseil de surveillance. Entreprise régie par le Code des assurances - Capital 46 200 000 € - RCS Niort B 315 652 263. Siège social : 9 rue des Iris - CS 50000 - Bessines - 79088 Niort cedex 9. Tél. 05 49 32 50 50 - mutavie.fr. Le risque est donc porté par une société d'assurance régie par le Code des assurances, distincte de la MACIF (société d'assurance mutuelle IARD). p. 1
- Le tableau indique les principaux frais du contrat au dernier exercice clos ; il peut subsister des frais qui n'y figurent pas. Les taux de gestion des unités de compte sont des moyennes. p. 1
- Le tableau distingue trois supports — fonds en euros, unités de compte, Eurocroissance — le support Eurocroissance étant porté à NA. Il distingue également la gestion libre et la gestion pilotée ou standardisée, cette dernière étant portée à NA (« Mode de gestion n°1 (moyenne) : NA »). p. 1

## Lacunes d'extraction

- PORTEUR DE RISQUE : le document nomme MUTAVIE SE (RCS Niort B 315 652 263, capital 46 200 000 €, siège 9 rue des Iris - CS 50000 - Bessines - 79088 Niort cedex 9), et non la MACIF. C'est l'ancienne dénomination de l'entité vie du groupe, aujourd'hui Macif Vie ; le document ne mentionne pas ce changement de nom, le nom a donc été enregistré exactement tel qu'imprimé (« Mutavie » / « MUTAVIE SE ») et le renommage n'est signalé qu'ici. Il ne s'agit pas d'un assureur différent. `insurer_name` reste la valeur imposée par les métadonnées de la tâche (MACIF), qui diverge donc du porteur de risque imprimé sur le document.
- DATE D'ÉDITION : imprimée « JUIN 2024 » en pied de première page et confirmée par le code de référence « MUT/ FC/ FRAIS/MV - 06/24 » lu en dernière page. Normalisée en « 2024-06 » ; les deux formes imprimées sont conservées, l'une dans `reference`, l'autre citée dans `key_quotes`. Rien n'a été déduit du nom de fichier (MultiVie-Frais.pdf), qui ne porte aucune date.
- ORDRE DU FLUX TEXTE : la couche texte du PDF ne restitue pas l'ordre de lecture visuel. Les notes de bas de page (NA, (1) à (4)) sortent EN PREMIER, le tableau ensuite, puis les mentions légales, le code de référence, et enfin le titre « Les frais du Multi Vie (1) » et la date « JUIN 2024 » tout à la fin. Le titre et la date sont donc physiquement en tête de page, pas en fin. Les numéros de page cités (tous page 1) restent exacts, le document ne comptant qu'une page.
- APPARIEMENT LIBELLÉ / VALEUR : le tableau ressort en colonne (série de libellés, puis série de valeurs). Les groupes 1.1 et 1.2.1 listent plusieurs libellés d'affilée avant leurs valeurs (« Support fonds en euros / Support unités de compte / Support Eurocroissance » puis « 0,60% / 0,60% / NA »). L'appariement a été fait dans l'ordre d'apparition, cohérent sur l'ensemble du tableau. Pour la ligne 1.2.2, un seul mode (« Mode de gestion n°1 ») est listé, avec NA en valeur comme en rétrocession.
- COQUILLE DE L'ÉDITEUR NON CORRIGÉE, note (2) : « La catégorie “fonds actions” inclut les ETF et mais exclut les fonds de capital-investissement ». Le « et » est surnuméraire. Reproduit verbatim. Le même paragraphe imprimé sur le tableau de frais du produit Multi Horizon Retraite ne comporte pas ce « et » : les deux formulations coexistent dans le corpus de l'éditeur.
- PONCTUATION ANORMALE NON CORRIGÉE, note (3) : « Part des frais reversés au profit du distributeur et, du gestionnaire du contrat » — la virgule après « et » est reproduite telle quelle.
- DOCUMENT NON CONTRACTUEL : c'est un tableau de frais standardisé, pas une notice. Il ne contient AUCUNE garantie (décès, rachat, arbitrage en tant que prestations), AUCUNE exclusion, aucun délai d'attente, aucune obligation du souscripteur, aucune procédure en cas de sinistre, aucune clause de durée / renonciation / résiliation, aucune prescription, aucune franchise. `coverages` et `exclusions` sont donc vides et plusieurs objets sont null : c'est l'état réel de la source. Le détail des frais a été porté ligne par ligne dans `special_conditions` et en synthèse dans `premium`, faute d'emplacement dédié dans le schéma.
- `target_audience` laissé null : le document n'énonce aucune cible de clientèle, ni condition d'âge, ni condition d'adhésion. Aucune catégorie n'a été déduite du type de produit.
- Aucun rendement, aucune performance, aucune participation aux bénéfices n'est donné ici : le document ne porte que sur les frais. Aucune information non plus sur l'autorité de contrôle, la réclamation, la médiation ou la fiscalité.
- Le contrat n'est pas rattaché à une association souscriptrice dans ce document (contrairement au tableau de frais Multi Horizon Retraite du même éditeur, souscrit par l'AGEPER) ; aucun « frais d'adhésion à l'association » n'y figure d'ailleurs.
- PIÈGE TYPOGRAPHIQUE — ESPACES FINES AVANT LES APPELS DE NOTE : la couche texte insère une ESPACE FINE U+2009 (et non une espace ordinaire) entre le libellé et son appel de note, aux 8 emplacements suivants : « Fonds actions␉(2) », « Fonds immobilier␉(4) », « Les frais du Multi Vie␉(1) » et les cinq occurrences de « Dont taux de rétrocessions de commissions␉(3) ». Une citation retapée à la main avec une espace ordinaire à ces endroits ne correspondrait PAS au texte source. Les citations de ce fichier sont des tranches programmatiques et contiennent donc bien le caractère U+2009.
- Texte vérifié : les quotes sont des tranches exactes du texte ré-extrait du PDF local (PyMuPDF, page.get_text("text")), identique caractère pour caractère au texte du prompt une fois les marqueurs [page N] retirés. Autres particularités de la couche texte préservées telles quelles : 2 apostrophes typographiques U+2019 (aucune apostrophe ASCII), 8 espaces fines U+2009 (ci-dessus), 1 espace insécable U+00A0 dans la toute première ligne « NA : non applicable. » (entre « NA » et le deux-points — les espaces de « 46 200 000 € » sont en revanche ordinaires), 5 tabulations dans les numéros de section (« 1.1\t », « 1.2.1\t »…), des guillemets courbes U+201C/U+201D autour de “fonds actions” et “fonds immobilier”, un signe degré dans « Mode de gestion n°1 » et une espace finale après « un maximum de 30 € ». Aucun espace de largeur nulle, aucun tiret conditionnel, aucun glyphe de zone privée, aucune ligature perdue, aucune coupure de mot par tiret en fin de ligne.

## Source & fidélité

- Source : [https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_banque/MultiVie-Frais.pdf](https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_banque/MultiVie-Frais.pdf) - téléchargé le 2026-08-01 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
