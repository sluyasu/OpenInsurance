---
type: product
domain: insurance
country: fr
insurer: '[[Gan Assurances]]'
insurer_slug: gan
branch: prevoyance
product_name: Gan Vision Majoritaire Prévoyance
document_type: product_sheet
target_audience: null
target_audience_note: 'Le document s’intitule « Actifs salariés du secteur privé »
  et retient un « Profil type » : « Salarié (à temps plein) ; 36 ans, marié, 1 enfant
  (12 ans) ; Ancienneté professionnelle : 2 ans ; Salaire brut de référence perçu
  au cours des 12 derniers mois : 24 000€ soit 2 000 € / mois ; Salaire journalier
  de référence : 65,75 € (2 000 / 91,25) ; Salaire annuel moyen brut des 10 meilleures
  années d’activité : 22 000 € ; Accord de prévoyance conclu par la branche professionnelle
  ». Les garanties décrites relèvent d’un « contrat collectif de prévoyance souscrit
  par l’employeur » : l’assuré est le salarié, le souscripteur est l’employeur. Aucune
  des catégories du schéma ne recouvre exactement ce cas ; target_audience est donc
  laissé null.'
reference: null
edition_date: au 01/01/2025
lang: fr
tags:
- insurance/fr/prevoyance
- product
- insurer/gan
aliases:
- Gan Vision Majoritaire Prévoyance
source_url: https://www.gan.fr/app/uploads/2024/12/Tableau-salarie-secteur-prive-_CCSF-VF-GA.pdf
source_pages: 5
fetched_at: '2026-07-30'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: gan-vision-majoritaire-prevoyance
variant: Actifs salariés du secteur privé
edition_status: null
edition_age_years: 1
superseded: null
extends: null
freshness: '2026-07-30'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Document de lisibilité au format « tableaux d’exemples de prise en charge au 01/01/2025 » pour les actifs salariés du secteur privé, portant sur les garanties incapacité, invalidité et décès. Pour chaque risque, il juxtapose trois colonnes — le régime obligatoire de la Sécurité sociale, les obligations légales de l’employeur et/ou de la convention collective, et la garantie du contrat collectif de prévoyance souscrit par l’employeur — puis en donne le total, sur la base d’un profil type de salarié à 24 000 € de salaire annuel brut. Les garanties de l’assureur y sont décrites comme déterminées contractuellement par l’employeur, avec deux exemples chiffrés de niveaux de couverture pour le capital décès, la rente éducation, les frais d’obsèques, la rente d’invalidité et les indemnités journalières complémentaires. Le document précise qu’il ne peut se substituer aux documents contractuels et que les garanties sont accordées sous réserve des limitations et exclusions définies au contrat souscrit par l’employeur.

- Assureur : [Gan Assurances](<../../insurers/Gan Assurances.md>) · Branche : [Prévoyance](<../../branches/Prévoyance.md>) · Type : Fiche produit · Édition : au 01/01/2025

## Définitions

| Terme | Définition | Page |
|---|---|---|
| PMSS | PMSS (Plafond Mensuel de la Sécurité Sociale) au 01/01/2025 : 3 925 € | p. 2 |
| PASS | PASS (Plafond annuel de la sécurité sociale) au 01/01/2025 = 47 100 € | p. 3 |
| Catégories d’invalidité (CAT 1, CAT 2, CAT 3) | CAT 1 : invalides capables d’exercer une activité rémunérée ; CAT 2 : invalides absolument incapables d’exercer une profession quelconque ; CAT 3 : invalides absolument incapables d’exercer une profession et se trouvant en outre dans l’obligation d’avoir recours à l’assistance d’une tierce personne pour effectuer les actes ordinaires de la vie (majoration pour tierce personne revalorisée chaque année) | p. 3 |
| Salaire journalier de base | Salaire journalier de base : total des 3 derniers salaires bruts perçus avant l'arrêt de travail, divisé par 91,25. Dans cet exemple : Revenu mensuel brut 3 derniers mois = 2000 € | p. 4 |
| Salaire de référence convention collective | Salaire de référence convention collective = salaire perçu par le salarié au cours des 12 mois civils précédant l’invalidité | p. 3 |
| Conditions de versement de la rente invalidité par l’organisme assureur | Conditions requises pour versement de la rente invalidité par l’organisme assureur : Reconnaissance de l’état d’invalidité par la Sécurité sociale | p. 3 |

## Garanties

### Capital décès - garantie du contrat collectif de prévoyance souscrit par l’employeur - p. 1
Montant du capital décès défini contractuellement par l’employeur. Montant du capital décès fonction de la situation familiale de l’intéressé au jour du décès. Prestations servies au bénéficiaire du contrat désigné ou défini par clause.
- Limite : Exemple 1 : 200% du Salaire Annuel Brut, soit un total de 48 000 € et 30% de majoration par Enfant à charge, soit 55 200 €. Exemple 2 : 250% du Salaire Annuel Brut soit un total de 60 000 € et 30% de majoration par Enfant à charge, soit 67 200 €.
  - Sous-limite : Total exemple 1 (avec capital décès Sécurité sociale) : 3 910 € + 55 200 € = 59 111 €
  - Sous-limite : Total exemple 2 (avec capital décès Sécurité sociale) : 3 910 € + 67 200 € = 71 110 €
  - Condition : Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur.
  - Condition : Les montants sont exprimés bruts de prélèvements sociaux.

### Rente éducation - garantie du contrat collectif de prévoyance souscrit par l’employeur - p. 2
Montant de la rente éducation et périodicité de son versement définis contractuellement par l’employeur. Conditions d’âges des enfants (possibilité de prévoir des paliers). La Sécurité sociale ne prévoit pas de rente éducation en cas de décès du salarié.
- Limite : Exemple 1 - rente annuelle par enfant (en % du Salaire Annuel Brut) : 14% (soit 3 360 €) / an jusqu’au 31/12 suivant le 12ème anniversaire ; 16% (soit 3 840 €) / an jusqu’au 31/12 suivant le 17ème anniversaire ; 18% (soit 4 320 €) / an jusqu’à la fin du trimestre civil post-21ème anniversaire (26 ans si étudiant). Exemple 2 : 20% (4 800 € / an) jusqu’au 31/12 suivant le 12ème anniversaire ; 22% (5 280 € / an) jusqu’au 31/12 suivant le 17ème anniversaire ; 24% (5 760 € / an) jusqu’à la fin du trimestre civil post-21ème anniversaire (26 ans si étudiant).
  - Sous-limite : Total par enfant - exemple 1 : 3 360 € / an jusqu’au 31/12 suivant le 12ème anniversaire ; 3 840 € / an jusqu’au 31/12 suivant le 17ème anniversaire ; 4 320 € / an jusqu’à la fin du trimestre civil post-21ème anniversaire (26 ans si étudiant)
  - Sous-limite : Total par enfant - exemple 2 : 4 800 € / an jusqu’au 31/12 suivant le 12ème anniversaire ; 5 280 € / an jusqu’au 31/12 suivant le 17ème anniversaire ; 5 760 € / an jusqu’à la fin du trimestre civil post-21ème anniversaire (26 ans si étudiant)
  - Condition : Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur.

### Frais d’obsèques - garantie du contrat collectif de prévoyance souscrit par l’employeur - p. 2
Frais d’obsèques organisme assureur : montant défini contractuellement par l’employeur. La Sécurité sociale ne prévoit pas de remboursement de frais d’obsèques en cas de décès du salarié.
- Limite : Exemple 1 : 150 % d’un PMSS (5 887,5 €). Exemple 2 : 200 % d’un PMSS (7 850 €).
  - Sous-limite : Total exemple 1 : 5 887,5 €
  - Sous-limite : Total exemple 2 : 7 850 €
  - Condition : PMSS (Plafond Mensuel de la Sécurité Sociale) au 01/01/2025 : 3 925 €
  - Condition : Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur.

### Rente invalidité - garantie du contrat collectif de prévoyance souscrit par l’employeur - p. 3
Montant de la rente invalidité déterminée contractuellement en fonction du taux d’invalidité déterminé par le médecin expert et du choix de l’employeur. Garantie en complément de la Sécurité sociale ou sous déduction de la Sécurité sociale. Cas illustré : invalidité permanente suite à maladie ou accident dans le cadre de la vie privée, avec indemnisation sans reprise d’activité.
- Limite : Le total ne peut être supérieur aux revenus professionnels perçus antérieurement à l’arrêt de travail.
  - Sous-limite : Exemple 1 : rente trimestrielle, sous déduction de la Sécurité sociale et à terme échu, 85% du Salaire de référence - 85% * 24 000 = 20 400 € / an, sous déduction des 11 000 € perçus via la Sécurité sociale : 9 400 € / an, soit : 783 € / mois
  - Sous-limite : Exemple 2 : rente trimestrielle, sous déduction de la Sécurité sociale et à terme échu, 90% du Salaire de référence - 90% * 24 000 = 21 600 € / an, sous déduction des 11 000 € perçus via la Sécurité sociale : 10 600 € / an, soit : 883 € / mois
  - Sous-limite : Total exemple 1 : 916 € + 783 € = 1 700 € / mois
  - Sous-limite : Total exemple 2 : 916 € + 883 € = 1 800 € / mois
  - Condition : Conditions requises pour versement de la rente invalidité par l’organisme assureur : Reconnaissance de l’état d’invalidité par la Sécurité sociale.
  - Condition : Les décisions de l’organisme assureur peuvent différer de celles de la Sécurité sociale.
  - Condition : Hypothèse retenue dans l’exemple : taux d’invalidité déterminé par l’expert de l’assureur : 70%, salaire mensuel perçu avant l’invalidité de 2 000 €.
  - Condition : Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur.

### Indemnité journalière complémentaire (IJC) - garantie du contrat collectif de prévoyance souscrit par l’employeur - p. 4
Montant de l’indemnité journalière complémentaire (IJC) versée par l’assureur, déterminée dans le contrat de prévoyance souscrit par l’employeur. Montant pouvant s’exprimer en complément de la Sécurité sociale ou sous déduction de la Sécurité sociale. Possibilité, le cas échéant, de choisir différentes options au regard de son contrat. Cas illustré : maladie ou accident dans le cadre de la vie privée, avec une durée d’arrêt de travail de 120 jours.
- Limite : Le total des revenus de remplacement ne peut être supérieur aux revenus professionnels perçus antérieurement à l’arrêt de travail. · Franchise : Franchise au choix de l’employeur (exemples chiffrés : Franchise 1 = 30 jours, Franchise 2 = 60 jours).
  - Sous-limite : Taux de garantie au choix de l’employeur. Exemple 1 : 90% du Salaire de référence, sous déduction de la Sécurité sociale et des obligations légales employeur. Exemple 2 : 100% du Salaire de référence, sous déduction de la Sécurité sociale et des obligations légales employeur.
  - Sous-limite : Franchise 1 (30 jours), taux de garantie exemple 1 : IJC = 90% Salaire journalier = 59,18 € / jour, sous déduction des IJSS et des obligations employeurs ; J38 à J67 : IJ complémentaire = 59,18 – 32,87 – 10,96 = 15,36 € ; J68 à J120 : IJ complémentaire = 59,18 – 32,87 = 26,30 €
  - Sous-limite : Franchise 1 (30 jours), taux de garantie exemple 2 : IJC = 100% Salaire journalier = 65,75 € / jour, sous déduction des IJSS et des obligations employeurs ; J31 à J37 : IJ complémentaire = 65,75 – 32,87 – 26,30 – 10,96 = 6,58 € ; J38 à J67 : IJ complémentaire = 65,75 – 32,87 – 10,95 = 21,92 € ; J68 à J120 : IJ complémentaire = 65,75 – 32,87 = 32,88 €
  - Sous-limite : Total IJ – exemple 1 en € /jour pendant 120 jours, franchise de 30 jours : J1 à J3 : 0 € ; J4 à J7 : 32,87 € ; J8 à J120 : 59,18 €
  - Sous-limite : Total IJ – exemple 2 en € /jour pendant 120 jours, franchise de 30 jours : J1 à J3 : 0 € ; J4 à J7 : 32,87 € ; J8 à J30 : 59,18 € ; J31 à J120 : 65,75 €
  - Sous-limite : Franchise 2 (60 jours), taux de garantie exemple 1 : J61 à J67 : IJ complémentaire = 59,18 – 32,87 – 10,96 = 15,35 € ; J68 à J120 : IJ complémentaire = 59,18 – 32,87 = 26,30 €
  - Sous-limite : Franchise 2 (60 jours), taux de garantie exemple 2 : J61 à J67 : IJ complémentaire = 65,75 – 32,87 – 10,96 = 21,92 € ; J68 à J120 : IJ complémentaire = 65,75 – 32,87 = 32,88 €
  - Sous-limite : Total IJ – exemple 1 en € /jour pendant 120 jours, franchise de 60 jours : J1 à J3 : 0 € ; J4 à J7 : 32,87 € ; J8 à J37 : 59,18 € ; J38 à J60 : 43,83 € ; J61 à J120 : 59,18 €
  - Sous-limite : Total IJ – exemple 2 en € /jour pendant 120 jours, franchise de 60 jours : J1 à J3 : 0 € ; J4 à J7 : 32,87 € ; J8 à J37 : 59,18 € ; J38 à J60 : 43,83 € ; J61 à J120 : 65,75 €
  - Condition : Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur.
  - Condition : Salaire journalier de base = ((2000x3) / 91,25) = 65,75 € ; IJSS = 50 % x 65,75 €, soit 32,87 € à compter de J4.

### Rachat de franchise - p. 5
Option proposée par l’organisme assureur (facultatif) : Rachat de franchise. Le document n’en décrit ni les modalités, ni le coût, ni l’effet chiffré.
- Optionnelle : oui

## Exclusions

| Exclusion | Description | S'applique à | Page |
|---|---|---|---|
| Limitations et exclusions définies au contrat souscrit par l’employeur (renvoi, non détaillées) | Ces garanties sont accordées sous réserve des limitations et exclusions de garanties (ex : pratique d’un sport extrême), définies au contrat souscrit par l’employeur. Le document ne donne qu’un seul exemple d’exclusion (la pratique d’un sport extrême) et renvoie au contrat pour la liste réelle. | all | p. 1 |

## Franchises

- Standard : Franchise au choix de l’employeur
- Variable : Deux franchises sont illustrées : Franchise 1 = 30 jours, Franchise 2 = 60 jours. Une option facultative de « Rachat de franchise » est proposée par l’organisme assureur.
- Indemnité journalière complémentaire (IJC) : Franchise au choix de l’employeur ; exemples : 30 jours et 60 jours

## Délais d'attente

- Indemnités journalières de la Sécurité sociale (IJSS) - régime obligatoire, pas la garantie de l’assureur : Versement des IJSS à partir du 4eme jour (Délai de carence de 3 jours). Il existe des exceptions au délai de carence (ex : arrêt de travail dû à une Affection de longue durée). (3 jours) p. 4
- Maintien de salaire - obligation légale de l’employeur, pas la garantie de l’assureur : Délai de carence de 7 jours pour l’obligation légale de maintien de salaire par l’employeur, indemnités versées sous certaines conditions définies dans le Code du travail (ex : ancienneté du salarié). (7 jours) p. 4
- Maintien de salaire - exemple de convention collective, pas la garantie de l’assureur : Exemple de convention collective : Délai de carence de 60 jours (à préciser par chaque organisme). (60 jours) p. 4

## Obligations de l'assuré

- Conditions requises pour versement de la rente invalidité par l’organisme assureur : Reconnaissance de l’état d’invalidité par la Sécurité sociale. (en cas d’invalidité) p. 3
- À noter que les garanties souscrites par l’employeur doivent être au moins équivalentes à celles prévues par la convention collective si un accord de prévoyance a été conclu par votre branche professionnelle. (à la souscription du contrat collectif par l’employeur) p. 1

## Conditions particulières

- Ce document présente des exemples de prise en charge par l’assurance maladie, et par votre contrat de prévoyance selon le niveau de couverture garanti. Ils ne correspondent pas forcément à votre situation, mais ils vous permettent de comprendre et comparer les tableaux de garantie. Ils ne peuvent se substituer aux documents contractuels qui seuls engagent votre employeur et/ou votre organisme assureur. Pour plus de renseignements consultez la notice d’information de votre contrat. p. 1
- Tous les montants exprimés sont bruts de prélèvements sociaux. Les montants du régime obligatoire sont spécifiques aux affiliés à la Sécurité sociale : les prestations peuvent différer pour des affiliés à des régimes obligatoires autres tels que la MSA par exemple. Les versements par l’assurance maladie obligatoire sont soumis à conditions. p. 1
- Salarié (à temps plein) ; 36 ans, marié, 1 enfant (12 ans) ; Ancienneté professionnelle : 2 ans ; Salaire brut de référence perçu au cours des 12 derniers mois : 24 000€ soit 2 000 € / mois ; Salaire journalier de référence : 65,75 € (2 000 / 91,25) ; Salaire annuel moyen brut des 10 meilleures années d’activité : 22 000 € ; Accord de prévoyance conclu par la branche professionnelle. p. 1
- Capital décès Sécurité sociale : montant du capital décès forfaitaire revalorisé chaque année, chiffré à 3 910 € dans l’exemple. La Sécurité sociale ne prévoit pas de rente éducation en cas de décès du salarié, ni de remboursement de frais d’obsèques. Pension d’invalidité : calcul en % sur la base du salaire annuel moyen brut des 10 meilleures années d’activité, dans la limite du PASS, et % du revenu calculé en fonction de la catégorie d’invalidité déterminée par le médecin conseil de la Sécurité sociale après examen de l’assuré ; exemple invalidité catégorie 2 : 50 % x 22 000 € = 11 000 € par an, soit 11 000 € / 12 = 916 € par mois. IJSS égales à 50 % du salaire journalier de base, salaire pris en compte plafonné à 1,8 fois le montant du Smic en vigueur lors du dernier jour du mois qui précède l'arrêt de travail ; IJSS = 50 % x 65,75 €, soit 32,87 € à compter de J4. p. 1
- Obligation légale de maintien de salaire par l’employeur ; l’obligation légale de l’employeur peut être assurée dans certains cas par un organisme assureur. Indemnités versées sous certaines conditions définies dans le Code du travail (ex : ancienneté du salarié). Délai de carence de 7 jours. Mesure légale selon l’ancienneté : 90% du salaire pendant 30 jours, puis 66,66% du salaire pendant 30 jours. Chiffrage : J8 à J37 : maintien à 90% (IJSS incluses), IJ complémentaire = (90% x 65,75€) - 32,87 = 26,30 € ; J38 à J67 : maintien à 66,66% (IJSS incluses), IJ complémentaire = (66,66 % x 65,75) - 32,87 € = 10,96 €. p. 4
- La convention collective peut prévoir une couverture minimale en matière de décès, de rente éducation, de frais d’obsèques et d’invalidité. Exemples de socle minimal cités : capital décès égal à 150% du salaire de référence, majoré de 30% par enfant à charge (soit 150% x 24 000 € = 36 000 € + 30% x 24 000€ = 7200€, total 36000€ + 7200€ = 43 200 €) ; rente éducation annuelle minimale de 12% x 24 000€ = 2 880 € par an jusqu’à 18 ans, ou 26 ans si poursuite d’études (12% du salaire de référence jusqu’au 18ème anniversaire, 15% au-delà et jusqu’au 26ème anniversaire si poursuite d’études) ; forfait obsèques minimal 150% PMSS soit 150% x 3 925 € = 5887,5 € ; invalidité 1ère catégorie 40% du salaire de référence, 2ème catégorie 75%, 3ème catégorie 75% + majoration pour tierce personne (pension invalidité catégorie 2 convention collective : 75% X 24 000€ = 18 000 € par an, 18 000€ /12 = 1500 € par mois). Incapacité : si la convention collective prévoit des mesures plus favorables que les dispositions légales (1er niveau), les dispositions de la convention s’appliquent ; exemple de convention collective : délai de carence de 60 jours (à préciser par chaque organisme), 90% du salaire pendant 40 jours, puis 66,66% du salaire pendant 40 jours, convention collective plus favorable dans ce cas, >80 jours : 60% du salaire. p. 1
- Un accident du travail ou une maladie professionnelle enclenchent un processus d’indemnisation différent de la part de la Sécurité sociale. Les exemples du document portent sur une maladie ou un accident dans le cadre de la vie privée. p. 3

## Lacunes d'extraction

- Nature du document : il s’agit d’un document de LISIBILITÉ au format « engagement de place » CCSF (le nom du fichier source porte « CCSF »), constitué de tableaux d’exemples de prise en charge. Ce n’est PAS le texte contractuel et ce n’est pas non plus une notice : le document imprime lui-même que les exemples « ne peuvent se substituer aux documents contractuels qui seuls engagent votre employeur et/ou votre organisme assureur ». Les montants cités sont des ILLUSTRATIONS pour un profil type, non des garanties contractuelles.
- Nom du produit : le seul nom commercial imprimé est « Gan Vision Majoritaire Prévoyance », en bas de la page 1, alors que le document est intitulé « Actifs salariés du secteur privé » et décrit un contrat collectif souscrit par l’employeur. Le qualificatif « Majoritaire » renvoie habituellement à une cible de dirigeants, ce qui est en tension avec « salariés du secteur privé ». Le document n’explique pas ce rattachement : product_name reprend ce qui est imprimé et la tension est signalée ici, pas arbitrée. variant a été renseigné avec la population du document (« Actifs salariés du secteur privé »).
- Assureur : le document ne nomme AUCUNE entité juridique d’assurance. Il ne cite ni Gan Assurances, ni Groupama Gan Vie, ni de RCS, ni d’adresse, ni l’ACPR. Il parle seulement de « votre organisme assureur » et de « l’organisme assureur ». insurer_name a donc été laissé à « Gan », marque à laquelle le seul nom de produit imprimé (« Gan Vision Majoritaire Prévoyance ») rattache le document ; le porteur de risque réel n’est pas déterminable à partir de ce document.
- Date : le document n’imprime pas de date d’édition ni de code de pied de page. edition_date reprend la date d’effet des chiffrages telle qu’imprimée (« au 01/01/2025 », reprise par les valeurs de PMSS et de PASS au 01/01/2025). Ce n’est pas nécessairement la date de publication du document.
- Structure à trois colonnes : le document juxtapose pour chaque risque le régime obligatoire de la Sécurité sociale, les obligations légales de l’employeur et/ou de la convention collective, et la garantie du contrat collectif de prévoyance. Seule la troisième colonne relève de l’assureur. coverages[] ne contient donc que les garanties de cette colonne ; les montants de la Sécurité sociale, des obligations légales et de la convention collective ont été rangés dans special_conditions, clairement étiquetés « hors garantie de l’assureur », pour ne pas les faire passer pour des garanties du produit.
- CONTRADICTION ARITHMÉTIQUE DANS LA SOURCE : le total de l’exemple 1 pour le capital décès est imprimé « 3 910 € + 55 200 € = 59 111 € » alors que l’addition donne 59 110 €. Le total de l’exemple 2, « 3 910 € + 67 200 € = 71 110 € », est exact. Les deux lignes sont consignées verbatim, sans correction.
- Autres écarts d’arrondi imprimés tels quels : les totaux mensuels d’invalidité « 916 € + 783 € = 1 700 € / mois » et « 916 € + 883 € = 1 800 € / mois » (les additions donnent 1 699 € et 1 799 €). De même, la même IJ complémentaire est chiffrée 15,36 € page 5 pour la franchise 30 jours et 15,35 € pour la franchise 60 jours, et une soustraction utilise « 10,95 » là où le reste du tableau utilise « 10,96 ».
- ARTEFACT DE PUBLICATION : la page 4 contient la chaîne « sous déduction de la Sécurité socialeErreur ! Signet non défini. » — un champ de renvoi non résolu (« Erreur ! Signet non défini. ») laissé dans le PDF publié. Le texte manquant derrière ce renvoi n’est pas récupérable.
- Numérotation de notes de bas de page incohérente : pages 4 et 5, le titre « Exemple : maladie ou accident dans le cadre de la vie privé6 » renvoie à la note 6 (définition du PASS), alors que la note pertinente est la note 5 (accident du travail / maladie professionnelle), correctement appelée page 3 (« vie privée5 »). La faute d’accord « vie privé » est également conservée telle quelle.
- Page 4 incomplète : les cellules « Total exemple 1 » et « Total exemple 2 » de la page 4 sont vides dans le texte extrait ; les totaux correspondants figurent en page 5. Les colonnes « Exemple 1 : 90% du Salaire de référence… » et « Exemple 2 : 100% du Salaire de référence… » de la page 4 sont fragmentées mot à mot par la mise en page (un mot par ligne) ; elles ont été recomposées dans l’ordre de lecture.
- Reconstruction des tableaux : le texte extrait du PDF est linéarisé cellule par cellule, sans structure de tableau. Le rattachement de chaque montant à sa colonne (Sécurité sociale / obligations / garantie assureur / total) et à son exemple (1 ou 2) a été reconstitué par l’ordre de lecture et par cohérence des calculs affichés. Les cas où le rattachement reste incertain sont signalés dans les libellés.
- Exclusions : le document n’en énonce qu’une seule, à titre d’exemple (« ex : pratique d’un sport extrême »), et renvoie pour le reste au contrat souscrit par l’employeur. L’unique entrée d’exclusions est donc ce renvoi, pas une liste réelle.
- Aucune information sur les cotisations, la durée, la reconduction, la résiliation, la renonciation, la prescription ou la procédure de sinistre : premium, duration_and_cancellation et prescription_period sont null et claims_procedure est vide. Ces sujets sont absents de CE document, non du contrat.
- Le document ne précise ni le nom de l’assisteur, ni de garanties d’assistance, ni de portée territoriale.
- L’option « Rachat de franchise » est nommée en toute fin de document (page 5) sans aucune description, tarification ou condition.

## Source & fidélité

- Source : [https://www.gan.fr/app/uploads/2024/12/Tableau-salarie-secteur-prive-_CCSF-VF-GA.pdf](https://www.gan.fr/app/uploads/2024/12/Tableau-salarie-secteur-prive-_CCSF-VF-GA.pdf) - téléchargé le 2026-07-30 - 5 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
