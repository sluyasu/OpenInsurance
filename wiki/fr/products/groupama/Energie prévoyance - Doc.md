---
type: product
domain: insurance
country: fr
insurer: '[[Groupama]]'
insurer_slug: groupama
branch: prevoyance
product_name: Energie prévoyance
document_type: other
target_audience: independants
target_audience_note: 'Le document décrit un régime obligatoire « Sécurité sociale
  des indépendants » et un « Profil type retenu » : « Commerçant », « 50 ans, marié,
  1 enfant (13 ans) ». La note 3 vise « le décès d''un artisan ou commerçant cotisant
  (non retraité) ou bénéficiaire d''une pension d''invalidité ».'
reference: null
edition_date: null
lang: fr
tags:
- insurance/fr/prevoyance
- product
- insurer/groupama
aliases:
- Energie prévoyance
source_url: https://assets.ctfassets.net/7awcp71bzphk/6TaB6zk8XVLyn83vszOtX8/31cfaa6a1e539be35223f96ac055b0fa/Exemples-TNS-CCSF-2026.pdf.pdf
source_pages: 4
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: energie-prevoyance
variant: null
edition_status: null
edition_age_years: null
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Document d'exemples chiffrés, de format normalisé, comparant la prise en charge par le régime obligatoire (Sécurité sociale des indépendants) et par un contrat de prévoyance complémentaire, pour un profil type de commerçant de 50 ans percevant 43 000 € bruts par an. Il couvre quatre risques : décès (capital décès), invalidité permanente (rente d'invalidité), incapacité de travail (indemnités journalières) et deux options facultatives (frais d'adaptation, pic d'activité). Le contrat de prévoyance est désigné « Energie prévoyance - Groupama Gan Vie » en page 1 et « ENERGIE – CAISSE REGIONALE GROUPAMA » en pages 2 et 3. Le document précise qu'il ne peut se substituer aux documents contractuels et n'énumère ni les garanties du contrat, ni ses exclusions.

- Assureur : [Groupama](<../../insurers/Groupama.md>) · Branche : [Prévoyance](<../../branches/Prévoyance.md>) · Type : Document

## Définitions

| Terme | Définition | Page |
|---|---|---|
| PASS | PASS (Plafond annuel de la Sécurité sociale) au 01/01/2026 = 47100 € | p. 1 |
| PMSS | PMSS (plafond mensuel de la Sécurité sociale) = 4 005 € | p. 1 |
| CAT 1 | CAT 1 : pension pour incapacité partielle au métier (PIPM) | p. 2 |
| CAT 2 | CAT 2 : pension pour invalidité totale et définitive (PITD) | p. 2 |
| CAT 3 | CAT 3 : pension pour invalidité totale et définitive (PITD) plus majoration pour tierce personne (MTP), l'invalide ayant besoin d'une tierce personne pour effectuer les actes ordinaires de la vie | p. 2 |
| IJSS | Indemnités journalières de la Sécurité sociale (IJSS) | p. 3 |
| IJC | l'indemnité journalière complémentaire (IJC) versée par l'assureur, déterminée dans le contrat de prévoyance souscrit | p. 3 |

## Garanties

### Capital décès (contrat de prévoyance) - p. 1
Capital décès versé au titre du contrat de prévoyance. Montant du capital décès déterminé au moment de la souscription du contrat. Garantie forfaitaire ou indemnitaire. Possibilité, le cas échéant, de choisir différentes options au regard de son contrat. Montant du capital décès (Au choix de l'assuré).
- Optionnelle : non · Limite : Le montant du capital décès peut être soumis à un ou plusieurs plafonds (note 5). Le document ne chiffre aucun plafond.
  - Sous-limite : Exemple 1 : 120 000 € (Groupama Gan Vie)
  - Sous-limite : Exemple 2 : 150 000 € (Groupama Gan Vie)
  - Sous-limite : Total exemple 1 (capital Sécurité sociale + capital assureur) : 9 612 € + 120000 €=129 612€
  - Sous-limite : Total exemple 2 (capital Sécurité sociale + capital assureur) : 9 612 € + 150000 €=159 612€
  - Condition : Pas d'option en capital décès.

### Rente invalidité (contrat de prévoyance) - p. 2
Rente invalidité versée au titre du contrat de prévoyance souscrit. Taux d'invalidité déterminé par le médecin expert de l'assureur. Montant pouvant s'exprimer en complément de la Sécurité sociale, sous déduction de la Sécurité sociale ou forfaitaire. Possibilité, le cas échéant, de choisir différentes options au regard de son contrat. Les décisions de l'organisme assureur peuvent différer de celles de la Sécurité sociale (note 8).
- Optionnelle : non
  - Sous-limite : Hypothèse taux invalidité déterminé par l'expert de l'assureur : 70%
  - Sous-limite : Exemple 1 – Choix d'une rente mensuelle correspondant à un montant journalier de 37 euros. La rente est versée de manière forfaitaire en complément de la sécurité sociale : 1147 € / mois (CAISSE REGIONALE GROUPAMA)
  - Sous-limite : Exemple 2 – Choix d'une rente mensuelle correspondant à un montant journalier de 55 euros. La rente est versée de manière forfaitaire en complément de la sécurité sociale : 1705 € / mois (CAISSE REGIONALE GROUPAMA)
  - Sous-limite : Total exemple 1 : 1792 € + 1147 €= 2939€
  - Sous-limite : Total exemple 2 : 1792 € +1705€=3497€
  - Condition : Exemple : maladie ou accident dans le cadre de la vie privée. Un accident du travail ou une maladie professionnelle enclenchent un processus d'indemnisation différent de la part de la Sécurité sociale (note 6).

### Frais d'adaptation (option) - p. 2
Option proposée par le contrat de prévoyance (facultatif). FRAIS D'ADAPTATION : à partir d'un taux d'invalidité 66%, on peut se faire rembourser, sur présentation de justificatifs, les frais de relogement ou des dépenses engagées…etc. Dans la limite du montant choisi.
- Optionnelle : oui · Limite : Dans la limite du montant choisi
  - Condition : à partir d'un taux d'invalidité 66%
  - Condition : sur présentation de justificatifs

### Indemnités journalières complémentaires — incapacité de travail - p. 3
Indemnités complémentaires versées au titre du contrat de prévoyance souscrit. Montant de l'indemnité journalière complémentaire (IJC) versée par l'assureur, déterminée dans le contrat de prévoyance souscrit. Garantie pouvant s'exprimer en complément de la Sécurité sociale, sous déduction de la Sécurité sociale ou forfaitaire. Possibilité, le cas échéant, de choisir différentes options au regard de son contrat. Montant de l'indemnité journalière (au choix de l'assuré).
- Optionnelle : non · Franchise : Niveau de franchise (au choix de l'assuré) ; le document illustre « Franchise 1 (À préciser par chaque organisme) Ex : 15 jours » et « Franchise 2 (À préciser par chaque organisme) Ex : … 30 jours ».
  - Sous-limite : Exemple 1 : IJ CLASSIQUE 37 euros
  - Sous-limite : Exemple 2 : IJ SAISONNIERE 37euros sur 4 mois (oct.-jan.) (MAX 8 MOIS)
  - Sous-limite : Franchise 1, exemple 15 jours — J0 à J15 : 0€ ; J> 15 à J120 :37€
  - Sous-limite : Franchise 2, exemple 30 jours — J0 à J30 : 0€ ; J> 30 à J120 :37€
  - Condition : Exemple retenu : une durée d'arrêt de travail de 120 jours

### Pic d'activité (option) - p. 4
Option proposée par contrat de prévoyance (facultatif). PIC D'ACTIVITE : selon le choix IJ classique : nous garantissons une majoration de vos indemnités journalières classiques de 50% pendant une ou plusieurs périodes. Sans franchises. La période clé correspond au minimum à un mois de l'année et au maximum à trois mois de l'année.
- Optionnelle : oui · Limite : majoration de vos indemnités journalières classiques de 50% · Franchise : Sans franchises.
  - Sous-limite : PIC D'ACTIVITE SUR 3 MOIS (oct.-déc.) =55,5
  - Sous-limite : J0 à J3 : 55,5€
  - Sous-limite : J> 3 à J92 :  55,5€ + 58,9€ =114,40€
  - Sous-limite : J> 92 :  58,9€
  - Condition : selon le choix IJ classique
  - Condition : La période clé correspond au minimum à un mois de l'année et au maximum à trois mois de l'année.

## Exclusions

| Exclusion | Description | S'applique à | Page |
|---|---|---|---|
| Limitations et exclusions de garanties définies au contrat souscrit | Ces garanties (parfois optionnelles) sont souscrites, en fonction des besoins de l'assuré. Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d'un sport extrême), définies au contrat souscrit. Le seul exemple d'exclusion cité par le document est la pratique d'un sport extrême ; la liste complète n'y figure pas. | all | p. 1 |

## Franchises

- Variable : Niveau de franchise (au choix de l'assuré) pour les indemnités journalières. Le document illustre deux niveaux : « Franchise 1 (À préciser par chaque organisme) Ex : 15 jours » et « Franchise 2 (À préciser par chaque organisme) Ex : … 30 jours ». Aucune franchise n'est indiquée pour le capital décès ni pour la rente invalidité.

## Délais d'attente

- Indemnités journalières de la Sécurité sociale (IJSS) : Versement des IJSS à partir du 4eme jour (Délai de carence de 3 jours). Il existe des exceptions au délai de carence (ex : arrêt de travail dû à une affection longue durée) (note 9). Cette carence est celle du régime obligatoire, pas celle du contrat de prévoyance. (Délai de carence de 3 jours) p. 3

## Conditions particulières

- « Ce document présente des exemples de prise en charge par l'assurance maladie, et par votre contrat de prévoyance selon le niveau de couverture choisi. Ils ne correspondent pas forcément à vos besoins ou à votre situation mais, ils vous permettent de comprendre, choisir ou comparer les tableaux de garantie. Ils ne peuvent se substituer aux documents contractuels qui seuls engagent l'organisme assureur. Pour plus de renseignements, consultez la notice d'information de votre contrat. » p. 1
- Commerçant ; 50 ans, marié, 1 enfant (13 ans) ; Revenu annuel brut : 43 000 € soit 3 583 € par mois ; Moyenne 3 dernières années : 43 000 € ; Moyenne 10 meilleurs années : 43 000 €. p. 1
- Le contrat est désigné « Contrat de prévoyance : Energie prévoyance - Groupama Gan Vie » en page 1, puis « ENERGIE – CAISSE REGIONALE GROUPAMA » en pages 2 et 3, et les montants d'exemple sont attribués tantôt à « (Groupama Gan Vie) » (capital décès), tantôt à « (CAISSE REGIONALE GROUPAMA) » (rente invalidité). Les deux désignations sont reproduites telles quelles ; aucune caisse régionale n'est nommée. p. 1
- Régime obligatoire : Sécurité sociale des indépendants. Capital Décès égal à 20% du plafond annuel de la Sécurité sociale (PASS). Si plusieurs bénéficiaires prioritaires de même rang, capital décès partagé à parts égales. Versements par l'assurance maladie obligatoire soumis à conditions (note 1). Calcul affiché : 20% x 48 060€ = 9 612 €. p. 1
- Calcul de la pension Sécurité sociale en % sur la base du revenu annuel moyen brut des 10 meilleures années d'activité. % du revenu calculé en fonction de la catégorie d'invalidité déterminée par le médecin conseil de la Sécurité sociale après examen de l'assuré. En cas d'invalidité catégorie 2 Sécurité sociale : 50 % x (43 000 /12) = 1 792 € par mois. Hypothèse revenu mensuel perçu avant l'invalidité de 3 583 €. p. 2
- Montant (IJSS) égal à 1/730 de la moyenne des revenus des 3 dernières années dans la limite du PASS. Versement des IJSS à partir du 4eme jour (Délai de carence de 3 jours). Calcul affiché : IJSS = (43 000 € X 1/730)  = 58,90 € par jour à compter de J4. p. 3
- Total € /jour pendant 120 jours : J0 à J3 : 0€ ; J4 à J15 : 58,90 ; J> 15 à J120 :  58,90€ +37€ =95,90€ ; J>120 : 58,90€. Les deux exemples affichent le même total. p. 3
- Total € /jour pendant 120 jours, exemple 1 : J0 à J3 : 0€ ; J4 à J30 : 58,90 ; J> 30 à J120 :  58,90€ +40€ =95,90€ ; J>120 : 58,90€. Exemple 2 : J0 à J3 : 0€ ; J4 à J30 : 58,90 ; J> 30 à J120 :  58,90€ + 37€ =95,90€ ; J>120 : 58,90€. Le « +40€ » de l'exemple 1 est reproduit tel quel (voir gaps). p. 3

## Lacunes d'extraction

- Ce document n'est pas contractuel et ne décrit pas le contrat : c'est un jeu d'exemples chiffrés de format normalisé (type CCSF), qui « ne peu[t] se substituer aux documents contractuels qui seuls engagent l'organisme assureur ». Les garanties du contrat Energie prévoyance n'y sont ni énumérées ni définies ; seuls des montants d'exemple sont donnés.
- CONTRADICTION sur l'assiette du capital décès Sécurité sociale, les deux lectures étant conservées : la note 4 indique « PASS (Plafond annuel de la Sécurité sociale) au 01/01/2026 = 47100 € », tandis que le calcul affiché en page 1 est « 20% x 48 060€ = 9 612 € ». 20 % de 47100 € donneraient 9 420 €, non 9 612 €. Le document ne dit pas laquelle des deux valeurs fait foi.
- CONTRADICTION sur l'organisme assureur, les deux désignations étant conservées : « Contrat de prévoyance : Energie prévoyance - Groupama Gan Vie » (page 1, avec des montants d'exemple attribués à « (Groupama Gan Vie) ») contre « ENERGIE – CAISSE REGIONALE GROUPAMA » (pages 2 et 3, montants attribués à « (CAISSE REGIONALE GROUPAMA) »). Aucune caisse régionale n'est nommée et le document ne précise pas laquelle des deux entités porte quel risque.
- ANOMALIE ARITHMÉTIQUE reproduite sans correction : dans le total de l'exemple 1 pour la franchise 30 jours, le document imprime « J> 30 à J120 :  58,90€ +40€ =95,90€ ». Les trois autres totaux comparables impriment « +37€ =95,90€ », et 58,90 + 37 = 95,90. Le « +40€ » est reproduit tel qu'imprimé.
- Le document contient un renvoi Word non résolu, reproduit tel quel dans le texte source : « sous déduction de la Sécurité sociale ou forfaitaireError! Bookmark not defined. » (page 3). Le contenu de la note appelée est donc inconnu.
- Le modèle normalisé n'a pas été entièrement complété par l'organisme. Plusieurs cellules conservent les mentions génériques du gabarit : « Franchise 1 (À préciser par chaque organisme) », « Franchise 2 (À préciser par chaque organisme) », « X €/ % revenu pendant XX jours (À préciser par chaque organisme) », « Total € /jour pendant 120 jours (À préciser par chaque organisme en fonction de la franchise retenue) ». Les niveaux de franchise réellement proposés par le contrat ne sont donc pas connus : « 15 jours » et « 30 jours » sont introduits par « Ex : ».
- Aucune date d'édition ni référence documentaire n'est imprimée : edition_date et reference sont laissés à null. Le nom de fichier de la source contient « 2026 » et la note 4 date le PASS « au 01/01/2026 », mais le document lui-même ne porte aucune mention d'édition. Contrairement au tableau « salariés du secteur privé » du même émetteur, il n'a pas non plus de titre daté.
- Aucune exclusion nominative : le document renvoie aux « limitations et exclusions de garanties […] définies au contrat souscrit » et n'en cite qu'un exemple entre parenthèses (« pratique d'un sport extrême »). L'entrée unique d'exclusions[] reflète cette mention, et non une liste d'exclusions du contrat.
- Aucune information sur la durée du contrat, la résiliation, la prescription, les obligations de l'assuré, la procédure de sinistre ou les cotisations : le document n'en traite pas. Les blocs correspondants sont donc vides.
- Aucune garantie décès optionnelle : le document indique explicitement « Pas d'option en capital décès. » En revanche il ne dit pas si les rentes éducation, rentes de conjoint ou frais d'obsèques existent au contrat — ces risques ne sont pas abordés.
- Page 1 : les treize premières lignes du texte extrait sont vides (mise en page à base de tableaux et d'images), et le titre éventuel de la page n'a pas de couche texte. Le document commence directement par les notes de bas de page.
- Les tableaux à colonnes multiples ont été linéarisés par l'extraction de texte. L'affectation des montants aux colonnes « Exemple 1 » / « Exemple 2 » a été recoupée avec les lignes « Total exemple 1 » / « Total exemple 2 » du document, qui confirment l'ordre retenu.
- Ce document et le tableau « Actifs salariés du secteur privé » (Tableau-salarie-secteur-prive-CCSF-VF-GROUPAMA) sont deux documents distincts du même format normalisé, non deux éditions du même document : populations différentes (indépendants contre salariés du secteur privé), contrats différents (« Energie prévoyance » contre « Synergie Prévoyance Entreprise »), et millésimes différents (PASS au 01/01/2026 contre garanties « au 01/01/2025 »).
- edition_date remise a null le 2026-08-01: la valeur 2026-01 venait du manifeste, deduite d'un YYMMDD non libelle dans le code de reference, alors que ce document n'imprime aucune date d'edition. Une date deduite presentee comme la date du document contrevient aux regles 4 et 5.

## Source & fidélité

- Source : [https://assets.ctfassets.net/7awcp71bzphk/6TaB6zk8XVLyn83vszOtX8/31cfaa6a1e539be35223f96ac055b0fa/Exemples-TNS-CCSF-2026.pdf.pdf](https://assets.ctfassets.net/7awcp71bzphk/6TaB6zk8XVLyn83vszOtX8/31cfaa6a1e539be35223f96ac055b0fa/Exemples-TNS-CCSF-2026.pdf.pdf) - téléchargé le 2026-07-30 - 4 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
