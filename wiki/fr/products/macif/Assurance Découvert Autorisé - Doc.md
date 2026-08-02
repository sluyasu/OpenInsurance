---
type: product
domain: insurance
country: fr
insurer: '[[Macif]]'
insurer_slug: macif
branch: emprunteur
product_name: Assurance Découvert Autorisé
document_type: other
target_audience: null
target_audience_note: 'Le document s''adresse aux personnes déjà couvertes : « Si
  vous êtes adhérent au contrat d''assurance découvert autorisé ». Il ne définit aucune
  catégorie de clientèle ni condition d''éligibilité.'
reference: null
edition_date: 2020-11
lang: fr
tags:
- insurance/fr/emprunteur
- product
- insurer/macif
aliases:
- Assurance Découvert Autorisé
source_url: https://www.macif.fr/files/live/sites/maciffr/files/dipa/INFORMATION_RELATIVE_ASSURANCE_DECOUVERT_AUTORISE.pdf
source_pages: 1
fetched_at: '2026-08-01'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: assurance-decouvert-autorise
variant: null
edition_status: null
edition_age_years: 6
superseded: null
extends: null
freshness: '2026-08-01'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Note d'information d'une page relative au contrat Assurance Découvert Autorisé, distribué avec le découvert autorisé de Socram Banque. Son unique objet est d'annoncer un changement de dénomination du porteur de risque : depuis le 27/11/2020, Macif-Mutualité est devenue Apivia Macif Mutuelle, mutuelle régie par le Livre II du Code de la mutualité et adhérente à la Mutualité Française (SIREN 779 558 501). Le document précise que ce changement de dénomination ne modifie pas les garanties proposées et renvoie les adhérents vers un conseiller Macifin'. Il ne décrit ni les garanties, ni les exclusions, ni les modalités du contrat.

- Assureur : [Macif](../../insurers/Macif.md) · Branche : [Assurance emprunteur](../../branches/Assurance%20emprunteur.md) · Type : Document · Édition : 2020-11

## Conditions particulières

- « Depuis le 27/11/2020, Macif-Mutualité est devenue Apivia Macif Mutuelle, mutuelle régie par le Livre II du Code de la mutualité et adhérente à la Mutualité Française. SIREN 779 558 501. Siège social : 17-21 place Etienne Pernet - 75015 PARIS cedex 15. » p. 1
- « Si vous êtes adhérent au contrat d'assurance découvert autorisé, ce changement de dénomination ne modifie pas les garanties proposées. » Le document affirme la continuité des garanties sans les énumérer ni les décrire. p. 1
- Le contrat est assuré par Apivia Macif Mutuelle (anciennement Macif-Mutualité), mutuelle régie par le Livre II du Code de la mutualité et adhérente à la Mutualité Française, SIREN 779 558 501, siège social 17-21 place Etienne Pernet - 75015 PARIS cedex 15. Le risque relève donc du Code de la mutualité (adhésion, adhérent) et non du Code des assurances. La MACIF n'est pas l'assureur de ce contrat. p. 1
- La MACIF intervient comme « Intermédiaire en opérations de banque et services de paiement pour le compte exclusif de Socram Banque - N° ORIAS 13005670 », et non comme assureur du contrat. Elle est décrite comme société d'assurance mutuelle à cotisations variables, entreprise régie par le Code des assurances, siège social 2 et 4 rue de Pied de Fond - 79000 Niort. p. 1
- SOCRAM BANQUE - SA au capital social de 70 000 000 euros inscrite au RCS de Niort sous le numéro 682 014 865 - 2 rue du 24 février - CS 90000 - 79092 Niort cedex 9. Mandataire d'assurance N° ORIAS 08044968. Le document est émis par un « Intermédiaire en opérations de Banque et en services de paiement de Socram Banque ». p. 1
- GIE MACIF FINANCE EPARGNE - Groupement d'intérêt économique, au capital de 1 524,50 euros - RCS Niort 400 024 881 - Siège social : 9 rue des Iris - 79000 Bessines. Mandataire d'intermédiaire en opérations de banque et services de paiement et mandataire d'assurance - N°ORIAS 19000688. MACIFIN' - établissement secondaire du GIE MACIF FINANCE EPARGNE - 31 route de Gachet - 44300 Nantes. p. 1
- « Pour toute information complémentaire, un conseiller Macifin' est à votre disposition du lundi au vendredi de 8h à 20h et le samedi de 9h à 17h au : » — suivi de « Macifin' – Votre Relation Banque ». Le numéro de téléphone annoncé par les deux points n'apparaît pas dans la couche texte du PDF. p. 1

## Lacunes d'extraction

- PORTEUR DE RISQUE : le document nomme DEUX dénominations successives de la même entité, et les deux sont enregistrées telles qu'imprimées. Le pavé de mentions légales dit « Le contrat Assurance Découvert Autorisé est assuré par Apivia Macif Mutuelle, mutuelle régie par le Livre II du Code de la mutualité et adhérente à la Mutualité Française. SIREN 779 558 501 » tandis que le corps du texte dit « L'assurance découvert autorisé est assurée par Macif-Mutualité ». Ce n'est PAS une contradiction : le document explique lui-même qu'il s'agit d'un renommage (« Depuis le 27/11/2020, Macif-Mutualité est devenue Apivia Macif Mutuelle »), avec le même SIREN 779 558 501 et le même siège. Une seule et même entité, sous deux noms. Cette entité a depuis été renommée une nouvelle fois (Macif Santé Prévoyance) ; ce troisième nom ne figure PAS dans le document et n'a donc pas été enregistré. Dans tous les cas l'assureur n'est pas la MACIF, qui n'intervient ici que comme intermédiaire en opérations de banque pour Socram Banque.
- AUCUNE DATE D'ÉDITION : le document ne porte ni date d'édition, ni code de référence, ni mention « édition MM/AAAA ». `edition_date` est laissé null. La seule date imprimée, 27/11/2020, est la date d'effet du changement de dénomination — un fait relaté par le document, PAS sa date d'édition ; elle n'a délibérément pas été reportée dans `edition_date`. Le document est nécessairement postérieur à cette date, mais de combien, il ne le dit pas. Rien n'a été déduit du nom de fichier.
- BRANCHE NON CARACTÉRISÉE PAR LE DOCUMENT : la valeur `emprunteur` provient des métadonnées de la tâche. Le document lui-même ne dit jamais quel risque est couvert (décès, incapacité, perte d'emploi ?) ni sur quoi porte la prestation. Il désigne uniquement un contrat adossé à un découvert autorisé accordé par Socram Banque. Aucune requalification n'a été tentée.
- NOM DU PRODUIT : trois graphies coexistent dans la même page — « Assurance Découvert Autorisé » (mentions légales, retenue comme `product_name`), « INFORMATION RELATIVE A L'ASSURANCE DECOUVERT AUTORISE » (titre, en capitales non accentuées) et « l'assurance découvert autorisé » / « le contrat d'assurance découvert autorisé » (corps du texte, en minuscules). Aucune n'a été normalisée dans les citations.
- DOCUMENT NON CONTRACTUEL ET SANS SUBSTANCE DE GARANTIE : cette note d'information ne contient AUCUNE garantie, AUCUNE exclusion, aucune définition, aucun plafond, aucune franchise, aucun délai d'attente, aucune obligation de l'adhérent, aucune procédure de sinistre, aucune clause de durée / résiliation / prescription et aucune information sur la cotisation. Les tableaux correspondants sont vides et les objets `deductibles`, `duration_and_cancellation`, `prescription_period`, `premium` sont null : c'est l'état réel de la source, pas une extraction incomplète. Le document se borne à affirmer que les garanties sont inchangées, sans les énoncer. Pour connaître les garanties, il faut la notice / le règlement mutualiste du contrat, qui n'est pas ce document.
- VOCABULAIRE MUTUALISTE : le document parle d'« adhérent au contrat » et non de souscripteur, ce qui est cohérent avec un porteur de risque relevant du Livre II du Code de la mutualité. Le document ne précise cependant pas l'instrument contractuel (règlement mutualiste, notice, bulletin d'adhésion).
- NUMÉRO DE TÉLÉPHONE ABSENT : la phrase de contact se termine par « ... et le samedi de 9h à 17h au : » et aucun numéro ne suit dans la couche texte ; vient directement « Macifin' – Votre Relation Banque ». Le numéro est vraisemblablement une image ou un encadré graphique sans texte extractible.
- ZONE D'EN-TÊTE SANS TEXTE : les premières lignes du PDF ne contiennent que des suites d'espaces (bandeau / logos sans couche texte). Aucune information n'en a été tirée.
- AUCUNE mention de l'autorité de contrôle (ACPR), ni de dispositif de réclamation ou de médiation, ni d'information sur la protection des données.
- Texte vérifié : les quotes sont des tranches exactes du texte ré-extrait du PDF local (PyMuPDF, page.get_text("text")), identique caractère pour caractère au texte du prompt une fois les marqueurs [page N] retirés. La couche texte contient 12 apostrophes typographiques U+2019 (aucune apostrophe ASCII), aucun espace de largeur nulle, aucun tiret conditionnel, aucun glyphe de zone privée, aucune ligature perdue et aucune coupure de mot par tiret en fin de ligne. Attention en revanche : le SIREN est coupé par un retour à la ligne dans le corps du texte (« SIREN 779 \n558 501 ») ; les citations retenues l'évitent et reprennent la forme non coupée du pavé légal (« SIREN 779 558 501. »). De même les mentions légales coupent les lignes en plein milieu de phrase, coupures conservées telles quelles dans les citations.

## Source & fidélité

- Source : [https://www.macif.fr/files/live/sites/maciffr/files/dipa/INFORMATION_RELATIVE_ASSURANCE_DECOUVERT_AUTORISE.pdf](https://www.macif.fr/files/live/sites/maciffr/files/dipa/INFORMATION_RELATIVE_ASSURANCE_DECOUVERT_AUTORISE.pdf) - téléchargé le 2026-08-01 - 1 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
