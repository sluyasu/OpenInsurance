---
type: product
domain: insurance
country: fr
insurer: '[[Macif (MACIF - Mutuelle Assurance des Commerçants et Industriels de France
  et des Cadres et Salariés de l''Industrie et du Commerce)]]'
insurer_slug: macif
branch: sante
product_name: Macif Mutuelle Entreprises
document_type: conditions_generales
target_audience: entreprises
target_audience_note: '"Contrat collectif à adhésion obligatoire" souscrit par l''"entreprise
  souscriptrice" au profit de ses salariés ; "En tant qu''employeur, vous avez le
  choix jusqu''à 6 niveaux de garanties pour couvrir l''étendue des besoins de vos
  salariés tout en maîtrisant le budget de votre entreprise".'
reference: NID M M E - 01/26
edition_date: 2026-01
lang: fr
tags:
- insurance/fr/sante
- product
- insurer/macif
aliases:
- Macif Mutuelle Entreprises
source_url: https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_professionnel_entreprise/nid-macif-mutuelle-entreprises.pdf
source_pages: 29
fetched_at: '2026-08-01'
extraction_model: claude-code-subagent:scale
prompt_version: '1.1'
product_family: macif-mutuelle-entreprises
variant: null
edition_status: current
edition_age_years: 0
superseded: null
extends: null
freshness: '2026-08-01'
status: ready
generated: true
---

<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->

## Résumé

Notice d'information d'un contrat collectif de complémentaire santé à adhésion obligatoire, en vigueur au 01/01/2026, souscrit par une entreprise auprès de Macif Santé Prévoyance au profit de ses salariés et de leurs éventuels ayants droit. Le contrat rembourse tout ou partie des frais de santé en complément des prestations en nature de la Sécurité sociale, ainsi que certains frais médicaux non remboursés par elle expressément prévus au tableau de garanties. L'entreprise souscriptrice choisit une formule socle parmi six niveaux (ESSENTIELLE, ESSENTIELLE +, ÉQUILIBRÉE, CONFORT, ÉTENDUE, EXCELLENCE) respectant le panier de soins minimum "ANI" et le 100 % Santé, et chaque salarié peut y ajouter une option facultative à sa charge exclusive. Des garanties d'assistance à domicile (IMA Assurances) et un service de téléconsultation sont inclus dans toutes les formules.

- Assureur : [Macif (MACIF - Mutuelle Assurance des Commerçants et Industriels de France et des Cadres et Salariés de l'Industrie et du Commerce)](../../insurers/Macif%20%28MACIF%20-%20Mutuelle%20Assurance%20des%20Commer%C3%A7ants%20et%20Industriels%20de%20France%20et%20des%20Cadres%20et%20Salari%C3%A9s%20de%20l%27Industrie%20et%20d.md) · Branche : [Complémentaire santé](../../branches/Compl%C3%A9mentaire%20sant%C3%A9.md) · Type : Conditions générales · Édition : 2026-01

## Lacunes d'extraction

- Instrument juridique : le document se présente en couverture comme une "NOTICE D'INFORMATION" d'un "Contrat collectif à adhésion obligatoire" et son code de pied de page est "NID M M E - 01/26" (NID = notice d'information). L'article 20 confirme qu'il s'agit de la notice d'information visée à l'article L.221 - 6 du Code de la mutualité, remise par l'employeur. Ce n'est donc ni un règlement mutualiste ni des conditions générales négociées bilatéralement : l'adhérent est un "salarié" / "membre participant" affilié à titre obligatoire par son employeur ("entreprise souscriptrice"), qui est le seul cocontractant de la mutuelle. Le type de document imposé par les métadonnées du pipeline (conditions_generales) ne correspond donc pas à l'auto-qualification du document.
- Contradiction interne sur l'instrument : bien qu'intitulé "notice d'information", le corps renvoie à plusieurs reprises à "les conditions générales" (article 1 : "sous réserve des limitations de garanties et exclusions prévues aux conditions générales") et l'article 5 dit "La notice d'assistance constitue une annexe aux présentes Conditions générales". Les deux lectures sont conservées telles quelles.
- L'autre document de la même ligne de produit "Macif Mutuelle Entreprises" présent dans la bibliothèque porte un code de pied de page "CG M M E - 01/25" (conditions générales, édition 01/25) alors que celui-ci porte "NID M M E - 01/26" : les deux codes diffèrent à la fois par la date ET par le préfixe de type de document (CG vs NID). Seul le code effectivement imprimé sur CE document est enregistré ici. Le champ superseded est laissé null (calculé au build).
- edition_date ("2026-01") est dérivée du code de pied de page "Référence du document : NID M M E - 01/26" et non d'une ligne "édition MM/AAAA" imprimée : le document ne comporte aucune mention d'édition explicite. La couverture imprime par ailleurs une date d'entrée en vigueur distincte, "en vigueur au 01/01/2026".
- Porteur du risque : les métadonnées de la tâche donnent "Macif (MACIF - Mutuelle Assurance des Commerçants et Industriels de France et des Cadres et Salariés de l'Industrie et du Commerce)", mais le document désigne explicitement une AUTRE entité comme assureur : "Le contrat Macif Mutuelle Entreprises est assuré par Macif Santé Prévoyance - Mutuelle régie par le Livre II du Code de la mutualité et adhérente à la Mutualité Française. SIREN 779 558 501". MACIF SAM (société d'assurance mutuelle régie par le Code des assurances) n'apparaît en dernière page qu'au titre des mentions légales du groupe, sans porter le risque santé. insurer_name a donc été renseigné avec le porteur de risque imprimé (Macif Santé Prévoyance).
- Note d'identité d'entité (hors document) : Macif Santé Prévoyance, SIREN 779 558 501, est la même personne morale que celle antérieurement dénommée Macif-Mutualité puis Apivia Macif Mutuelle ; il s'agit d'un changement de dénomination, pas d'un changement d'assureur. Le document n'imprime que la dénomination actuelle, qui est celle retenue ici.
- Nom commercial : la couverture, l'article de présentation (page 3), la page 13 ("le contrat MACIF MUTUELLE ENTREPRISES étant responsable") et les mentions légales impriment "Macif Mutuelle Entreprises", mais la page 11 imprime "le contrat Macif Mutuelle Santé Entreprises". Les deux formulations sont conservées ; product_name reprend celle de la couverture.
- Tableau de garanties (pages 8 à 10) : la couche texte du PDF aplatit le tableau à six colonnes en lignes successives. L'affectation de chaque montant à une formule repose sur l'ordre fixe des colonnes réimprimé en tête de chaque page du tableau (ESSENTIELLE, ESSENTIELLE +, ÉQUILIBRÉE, CONFORT, ÉTENDUE, EXCELLENCE) ; aucune ligne ne comporte un nombre de valeurs différent de six, mais l'appariement reste une lecture de mise en page et non une donnée explicite du texte.
- Le tableau de garanties applicable est celui "figurant dans les conditions particulières" et la formule retenue est "fixée aux conditions particulières" : les conditions particulières ne font pas partie de ce document. De même, la catégorie de personnel assurée et les montants de cotisation sont renvoyés aux conditions particulières / au bulletin d'affiliation et ne sont pas chiffrés ici.
- Les garanties d'assistance sont "assurées par IMA Assurances et définies dans la notice d'assistance" : cette notice d'assistance n'est pas incluse dans le document, le contenu détaillé des garanties d'assistance n'a donc pas pu être extrait.
- Aucun délai d'attente (ni stage) n'est stipulé pour l'affiliation au contrat collectif lui-même ; le document ne mentionne des délais d'attente que pour en écarter l'application aux assurances individuelles de suite (loi Evin et article 27).
- Durée du contrat collectif, reconduction tacite et préavis de résiliation à l'échéance ne sont pas énoncés pour le contrat collectif : le document ne décrit la résiliation que du côté du non-paiement des cotisations, des options facultatives et du maintien loi Evin. duration et tacit_renewal sont donc laissés null.
- Le montant de la cotisation n'est pas chiffré (renvoyé au contrat souscrit par l'entreprise et au bulletin d'affiliation) ; seules les mécaniques d'indexation et de paiement sont extraites.
- Coquilles et artefacts de la couche texte conservés tels quels, sans correction : "Cures thermale" (pages 10 et 18), "soins d'obsturation" (note 8), "incisive" au singulier (pages 11 et 15), "1erer" / "1rere" (exposants aplatis), "cumu latives", "di spensation" / "dispensa tion", "Hord d'encadré" (page 14), "prévus par décret" (page 25), ainsi que les marqueurs "Encadré." / "Hors d'encadré." injectés par l'extraction du PDF.
- Pages 2, 4 et 12 : la couche texte contient de nombreuses lignes dupliquées (sommaire, encadrés marketing, exemples de remboursement). Les exemples chiffrés de la page 12 sont partiellement corrompus ("1133 € 1133 €  3 €", "1023,35 € 1023,35 €  5 €") ; ils n'ont pas été retenus comme montants de garantie car ce sont des illustrations commerciales et non des engagements contractuels.
- Les exemples de reste à charge de la page 4 (couronne dentaire hors 100 % Santé de 547,90 euros, lunettes à verres progressifs de 601 euros, consultation de dermatologue avec 58 euros de dépassements) sont présentés comme "quelques exemples de remboursements" à visée pédagogique ; ils sont enregistrés en special_conditions et non comme des garanties.

## Documents liés

- Édition courante de ce produit.
- [Macif Mutuelle Entreprises](Macif%20Mutuelle%20Entreprises%20%282%29.md) - Conditions générales, éd. 2025-01

## Source & fidélité

- Source : [https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_professionnel_entreprise/nid-macif-mutuelle-entreprises.pdf](https://www.macif.fr/files/live/sites/maciffr/files/conditions_generales_professionnel_entreprise/nid-macif-mutuelle-entreprises.pdf) - téléchargé le 2026-08-01 - 29 pages
- Extraction : claude-code-subagent:scale · prompt v1.1
- ⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source.
