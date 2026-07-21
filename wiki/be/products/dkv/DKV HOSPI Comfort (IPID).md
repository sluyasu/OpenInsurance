---
type: product
domain: insurance
country: be
insurer: '[[DKV Belgium]]'
insurer_slug: dkv
branch: sante
product_name: DKV HOSPI Comfort
document_type: ipid
target_audience: Toute personne physique n'ayant pas atteint l'âge de 70 ans à la
  conclusion du contrat d'assurance, ayant son lieu de résidence et sa résidence principale
  en Belgique, étant assujetti à la sécurité sociale belge et en bénéficiant.
reference: 31 174_FR_6_202603
edition_date: '202603'
lang: fr
tags:
- insurance/be/sante
- product
- insurer/dkv
aliases:
- DKV HOSPI Comfort
source_url: https://biblio.dkv.be/pdfbib.ashx?lang=fr&id=31174
source_pages: 3
fetched_at: '2026-07-05'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: dkv-hospi-comfort
variant: null
edition_status: null
superseded: null
extends: null
freshness: '2026-07-05'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

DKV HOSPI Comfort est une assurance hospitalisation individuelle à caractère indemnitaire, complémentaire à l'intervention de l'assurance maladie légale/statutaire belge, assortie d'une assurance assistance à l'étranger. Elle rembourse les frais réels supportés (tickets modérateurs et suppléments inclus) en cas d'hospitalisation pour maladie, accident ou accouchement, avec libre choix de l'hôpital et du type de chambre (hors chambre de luxe ou suite). Elle couvre également les soins ambulatoires pré- et post-hospitaliers ainsi que les soins liés à 33 maladies graves. Elle peut être souscrite par toute personne physique résidant principalement en Belgique n'ayant pas atteint 70 ans à la conclusion du contrat.

- Assureur : [DKV Belgium](../../insurers/DKV%20Belgium.md) · Branche : [Santé](../../branches/Sant%C3%A9.md) · Type : IPID / Fiche d'information · Édition : 202603

## Définitions

| Terme | Définition | Page |
|---|---|---|
| Maladie Graves (MG) | Ensemble de 33 maladies (par exemple le cancer, le diabète, la maladie d'Alzheimer, la sclérose en plaques, etc.) donnant droit à la prise en charge des frais médicaux des soins ambulatoires ainsi que des frais de soins non-médicaux pendant la période post-hospitalière d'une hospitalisation couverte avec nuitée. | p. 1 |
| Contribution personnelle | Une franchise par cas d'assurance, dont le montant est déterminé dans les Conditions Particulières d'Assurance, appliquée à chaque hospitalisation en chambre à un lit. | p. 1 |
| Nouvelle hospitalisation (rechute) | Une rechute causant une nouvelle admission est considérée comme une nouvelle hospitalisation. | p. 1 |

## Garanties

### Libre choix de l'hôpital, du type de chambre et du prestataire de soins - p. 1
Libre choix de l'hôpital, du type de chambre à l'exception d'une chambre de luxe ou une suite, et du prestataire de soins reconnu.
- Optionnelle : non

### Frais d'hospitalisation - p. 1
Remboursement des frais réels supportés (tickets modérateurs et suppléments inclus) : frais d'hospitalisation (salle de plâtre et l'extraction dentaire chirurgicale sous anesthésie générale incluses) en cas de maladie, d'accident ou d'accouchement.
- Optionnelle : non · Franchise : Une contribution personnelle (franchise par cas d'assurance), dont le montant est déterminé dans les Conditions Particulières d'Assurance, est appliquée à chaque hospitalisation en chambre à un lit.

### Frais de séjour - p. 1
Frais de séjour, y compris le logement d'un des parents dans la même chambre que l'enfant hospitalisé.
- Optionnelle : non

### Frais de traitement médical et paramédical - p. 1
Frais de traitement médical et paramédical (kinésithérapeutes, infirmières, sage-femmes, podologues et logopèdes).
- Optionnelle : non
  - Condition : Traitements médicaux et paramédicaux sur prescription médicale d'un médecin.
  - Condition : Le remboursement des frais de logopédie est soumis à une autorisation préalable et à un remboursement par l'assurance obligatoire soins de santé et indemnités.

### Frais de médicaments, pansements et matériel médical - p. 1
Frais de médicaments, pansements et matériel médical.
- Optionnelle : non
  - Sous-limite : {'description': 'Remboursement à 80% des médicaments, pansements et matériel médical en pré-post et "MG"', 'amount': '80%'}
  - Condition : Médicaments, pansements et matériel médical sur prescription médicale d'un médecin.

### Frais de dispositifs médicaux, de prothèses et de membres artificiels - p. 1
Frais de dispositifs médicaux, de prothèses et de membres artificiels.
- Optionnelle : non
  - Condition : Dispositifs médicaux sur prescription médicale d'un médecin.
  - Condition : Le remboursement de la location ou de l'achat de dispositifs médicaux est soumis à l'approbation préalable de DKV, à l'exception des verres de lunettes ou des lentilles de contact, des appareils auditifs entièrement non-implantables, des bandages pour hernies, des bas à varices, des semelles orthopédiques, des coquilles plâtrées, des lombostats, des attelles et des béquilles.

### Frais de transport en Belgique en cas d'hospitalisation - p. 1
Frais de transport en Belgique en cas d'hospitalisation : en ambulance ou en hélicoptère vers et depuis l'hôpital, ainsi que le transfert vers un autre hôpital.
- Optionnelle : non · Portée : Belgique

### Frais pré et post-hospitalisation (soins ambulatoires) - p. 1
Pré et post : frais médicaux des soins ambulatoires, y compris les soins post-natals, 30 jours avant et 90 jours après une hospitalisation.
- Optionnelle : non · Portée : Belgique
  - Sous-limite : {'description': "Remboursement réduit de 50 % pour pré et post si l'assurance maladie légale n'intervient pas", 'amount': '50%'}
  - Sous-limite : {'description': 'Remboursement à 80% des médicaments, pansements et matériel médical en pré-post', 'amount': '80%'}

### "Maladie Graves" (MG) - Frais médicaux des soins ambulatoires - p. 1
Les frais médicaux des soins ambulatoires, de 33 maladies (par exemple le cancer, le diabète, la maladie d'Alzheimer, la sclérose en plaques, etc.).
- Optionnelle : non · Portée : Belgique · Limite : Frais médicaux des soins ambulatoires « MG » jusqu'à € 25.000 (par personne assurée et par année d'assurance)
  - Sous-limite : {'description': 'Remboursement réduit de 50 % pour "MG" si l\'assurance maladie légale n\'intervient pas', 'amount': '50%'}
  - Sous-limite : {'description': 'Remboursement à 80% des médicaments, pansements et matériel médical en "MG"', 'amount': '80%'}

### "Maladie Graves" (MG) - Frais de soins non-médicaux - p. 1
Les frais de soins non-médicaux (soins corporels quotidiens, aide-ménagère, garde d'enfants ou d'animaux) pendant la période post-hospitalière d'une hospitalisation couverte avec nuitée pour une "Maladie grave" (MG).
- Optionnelle : non · Portée : Belgique · Limite : Frais de soins non-médicaux liés à une "MG" jusqu'à € 250 (par personne assurée et par année d'assurance)

### Soins dentaires - p. 2
Soins dentaires, à l'exclusion de l'orthodontie.
- Optionnelle : non · Limite : jusqu'à € 750 (plafond de remboursement par personne assurée et par année d'assurance)
  - Condition : Le remboursement des traitements dentaires est soumis à l'approbation préalable de DKV : plan de traitement avec devis précis des coûts pour les traitements dentaires.

### Frais d'une perruque - p. 2
Les frais d'une perruque.
- Optionnelle : non · Limite : avec un maximum de € 1.250 (par personne assurée et par année d'assurance)

### Soins post-natals après un accouchement (à domicile) - p. 2
Soins post-natals après un accouchement (à domicile).
- Optionnelle : non · Limite : jusqu'à € 500 (par personne assurée et par année d'assurance)

### Frais de logopédie et de procréation médicalement assistée - p. 2
Remboursement des frais de logopédie et de procréation médicalement assistée.
- Optionnelle : non
  - Condition : Sous réserve d'une autorisation préalable et d'un remboursement par l'assurance obligatoire soins de santé et indemnités.

### Garantie "Frais médicaux" - Couverture mondiale (hospitalisation non-planifiée) - p. 2
Couverture mondiale : pour toute hospitalisation non-planifiée et médicalement nécessaire à l'étranger. Pour les hospitalisations en dehors de l'Union européenne, DKV rembourse jusqu'à un maximum de € 300.000 euros par cas d'assurance.
- Optionnelle : non · Portée : Couverture mondiale · Limite : Pour les hospitalisations en dehors de l'Union européenne, DKV rembourse jusqu'à un maximum de € 300.000 euros par cas d'assurance

### Garantie "Frais médicaux" - Couverture dans les États membres de l'Union européenne (hospitalisation planifiée) - p. 2
Couverture dans les États membres de l'Union européenne (excepté les pays et les territoires d'outre-mer) : pour toute hospitalisation planifiée et médicalement nécessaire et à l'étranger.
- Optionnelle : non · Portée : États membres de l'Union européenne (excepté les pays et les territoires d'outre-mer)
  - Condition : Sous réserve d'un accord préalable avec la mutualité.

### Garantie "Frais médicaux" - Couverture en Belgique (soins ambulatoires) - p. 2
Couverture en Belgique : pour les consultations et/ou traitements ambulatoires dans la période pré- et post-hospitalière d'une hospitalisation couverte, dans le cadre des "Maladies Graves", de l'aide non-médicale dans le cadre des "Maladies Graves".
- Optionnelle : non · Portée : Belgique

### Garantie "Assistance à l'étranger" DKV ASSISTANCE - Couverture mondiale - p. 2
Couverture mondiale : pour toute hospitalisation non-planifiée médicalement nécessaire à l'étranger dans la mesure où la personne assurée ne séjourne pas temporairement à l'étranger pendant plus de 90 jours consécutifs. Cette période est portée à 6 mois en cas de séjour temporaire effectif dans les Etats membres de l'Union européenne (à l'exclusion des pays et les territoires d'outre-mer) d'étudiants de moins de 26 ans lorsqu'il est effectué en continuité de leurs études et rentrent dans des programmes unilatéraux ou multilatéraux ou dans le cadre d'une convention entre deux ou plusieurs établissements d'enseignement supérieur.
- Optionnelle : non · Portée : Couverture mondiale
  - Condition : La personne assurée ne doit pas séjourner temporairement à l'étranger pendant plus de 90 jours consécutifs (période portée à 6 mois pour les étudiants de moins de 26 ans dans les États membres de l'Union européenne sous conditions).

### DKV ASSISTANCE - Rapatriement - p. 2
Rapatriement en cas d'accident/maladie et de décès.
- Optionnelle : non · Portée : étranger

### DKV ASSISTANCE - Remboursement des frais médicaux d'une hospitalisation urgente à l'étranger - p. 2
Remboursement des frais médicaux d'une hospitalisation urgente et non-planifiée à l'étranger.
- Optionnelle : non · Portée : étranger

### DKV ASSISTANCE - Retour des autres assurés et des enfants mineurs - p. 2
Retour des autres assurés et des enfants mineurs en cas d'hospitalisation d'une personne assurée.
- Optionnelle : non · Portée : étranger

### Service Medi-Card® - p. 2
Mode de paiement Medi-Card® : paiement direct de la facture d'hospitalisation à l'hôpital.
- Optionnelle : non

### Service AssurPharma - p. 2
AssurPharma : envoi automatisé à DKV des attestations par un pharmacien reconnu.
- Optionnelle : non

## Exclusions

| Exclusion | Description | S'applique à | Page |
|---|---|---|---|
| Affections/symptômes préexistants | Affections/symptômes préexistants à la conclusion du contrat d'assurance sauf en cas de continuation individuelle d'une assurance collective similaire de DKV. | all | p. 1 |
| Produits et compléments alimentaires, produits d'hygiène et cosmétiques | Produits et compléments alimentaires, vitamines et minéraux, produits d'hygiène et cosmétiques. | all | p. 1 |
| Frais liés à une vaccination, la contraception, une stérilisation | Frais autres qu'une consultation qui sont en lien avec une vaccination, la contraception, une stérilisation. | all | p. 1 |
| Traitements esthétiques | Traitements esthétiques à l'exception de la chirurgie plastique reconstructive qui a été approuvée préalablement. | all | p. 1 |
| Utilisation de drogues | Utilisation de drogues. | all | p. 1 |
| Frais résultant d'état d'ébriété, intoxication, alcoolisme, toxicomanie | Frais résultant entre autres de : état d'ébriété, intoxication punissable ou état analogue résultant de produits autres qu'alcoolisés, alcoolisme, toxicomanie, l'usage non conforme de médicaments. | all | p. 1 |
| Pratique sportive professionnelle ou rémunérée | La pratique sportive professionnelle ou rémunérée. | all | p. 1 |

## Franchises

- Standard : Une contribution personnelle (c-à-d une franchise par cas d'assurance), dont le montant est déterminé dans les Conditions Particulières d'Assurance, est appliquée à chaque hospitalisation en chambre à un lit. Une rechute causant une nouvelle admission est considérée comme une nouvelle hospitalisation.
- Variable : True
- Par garantie : Franchise appliquée à chaque hospitalisation en chambre à un lit.

## Délais d'attente

- Frais encourus pendant le stage d'attente pour les traitements dentaires (12m) sauf en cas de continuation individuelle d'une assurance collective similaire de DKV. (12m) p. 1

## Obligations de l'assuré

- Remplir et signer correctement une proposition d'assurance, qui consiste en un questionnaire administratif et médical. (à la conclusion du contrat) p. 2
- Aviser DKV dans les 30 jours à compter du moment où les conditions pour le maintien du contrat d'assurance ne sont plus remplies. En particulier : (1) tout changement de lieu de résidence ou de résidence principale, (2) tout séjour à l'étranger de plus de 90 jours consécutifs ou tout séjour temporaire de plus de 6 mois dans les États membres de l'Union européenne (à l'exclusion des pays et les territoires d'outre-mer) des d'étudiants de moins de 26 ans lorsqu'ils sont effectués en continuité de leurs études et rentrent dans des programmes unilatéraux ou multilatéraux ou dans le cadre d'une convention entre deux ou plusieurs établissements d'enseignement supérieur, (3) tout changement de statut en matière de sécurité sociale ayant pour conséquence que la personne assurée n'est plus assujettie à la sécurité sociale belge et ne peut plus en bénéficier. (dans les 30 jours) p. 2
- Prendre toutes les mesures raisonnables pour éviter et limiter les conséquences d'un cas d'assurance. p. 2
- Entreprendre toutes les démarches pour obtenir une intervention au titre de toutes les éventuelles interventions ou prestations légales/statutaires possibles, préalablement à toute demande d'indemnisation à DKV. (préalablement à toute demande d'indemnisation à DKV) p. 2
- Déclarer chaque cas d'assurance à DKV conformément aux directives, délais et modalités décrits dans les Conditions Générales d'Assurance. p. 3
- Signaler à DKV l'existence de tout autre accord pouvant donner lieu à un remboursement total ou partiel des frais réels supportés. p. 3

## Procédure de sinistre

1. Déclarer le cas d'assurance pour la garantie « Assistance à l'étranger » DKV ASSISTANCE par téléphone au numéro +32 2 230 31 32, dans les 48 heures suivant le début de l'hospitalisation ou à la suite d'un accident de sports d'hiver sur une piste de ski sans hospitalisation, ou dès que raisonnablement possible. (délai : dans les 48 heures suivant le début de l'hospitalisation, ou dès que raisonnablement possible) p. 3
2. Déclarer le cas d'assurance pour la garantie "Frais médicaux" par écrit et de préférence via le portail client digital (My DKV) ou l'application sur smartphone (DKV App) fournie par DKV. p. 3
3. Obtenir l'approbation préalable de DKV pour le remboursement de : la location ou l'achat de dispositifs médicaux (à l'exception des verres de lunettes ou des lentilles de contact, des appareils auditifs entièrement non-implantables, des bandages pour hernies, des bas à varices, des semelles orthopédiques, des coquilles plâtrées, des lombostats, des attelles et des béquilles) ; un plan de traitement avec devis précis des coûts pour les traitements dentaires ; un devis précis pour la chirurgie plastique reconstructive. (délai : préalablement) p. 3

## Durée & résiliation

- Durée : Durée du contrat : à vie, non résiliable par DKV sous réserve des exceptions prévues par la loi. La couverture d'assurance commence après l'émission de la police, après l'expiration des stages d'attente et après le paiement de la première prime convenue.
- Préavis : au plus tard trois mois avant l'échéance annuelle
- Modalité : La notification de résiliation du contrat à l'assureur doit se faire par lettre recommandée, par exploit d'huissier ou par la remise d'une lettre de résiliation avec accusé de réception.
- Droit spécial : Vous pouvez résilier votre contrat d'assurance à chaque échéance annuelle en le notifiant à DKV au plus tard trois mois avant cette date. DKV peut résilier le contrat d'assurance pour non-paiement de la prime.

## Conditions particulières

- Remboursement à 50% des frais d'hospitalisation couverts en Belgique si l'assurance maladie légale n'intervient pas du tout (sur aucun des postes de la facture d'hospitalisation). p. 1
- Cette assurance peut être souscrite par toute personne physique ayant son lieu de résidence et sa résidence principale en Belgique. Cette assurance s'adresse à toute personne physique n'ayant pas atteint l'âge de 70 ans à la conclusion du contrat d'assurance, ayant son lieu de résidence et sa résidence principale en Belgique, étant assujetti à la sécurité sociale belge et en bénéficiant. p. 1

## Lacunes d'extraction

- Le montant exact de la contribution personnelle (franchise) n'est pas indiqué dans ce document ; il est déterminé dans les Conditions Particulières d'Assurance.
- Aucun délai de prescription (prescription_period) n'est mentionné dans le document.
- La liste complète des 33 maladies graves (MG) n'est pas fournie ; seuls quelques exemples sont cités (cancer, diabète, maladie d'Alzheimer, sclérose en plaques).
- Le document est un IPID (aperçu général) et précise lui-même que les informations qu'il reprend ne sont pas exhaustives ; les détails complets figurent dans les informations précontractuelles et contractuelles (Conditions Générales/Particulières d'Assurance).

## Documents liés

- [DKV Hospi Comfort](DKV%20Hospi%20Comfort.md) - Conditions générales, éd. 08/2025

## Source & fidélité

- Source : [https://biblio.dkv.be/pdfbib.ashx?lang=fr&id=31174](https://biblio.dkv.be/pdfbib.ashx?lang=fr&id=31174) - téléchargé le 2026-07-05 - 3 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
