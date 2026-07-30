# thelem — Thélem assurances (FR, Code des assurances)
website: thelem-assurances.fr
library: https://www.thelem-assurances.fr/documents-information-produit/
fetch: plain            # 200 to plain HTTP, direct .pdf hrefs, no WAF, no renderer
status: enum
lang: fr
enumerated: 2026-07-30

Société d'assurance mutuelle à cotisations variables, SIREN 085 580 4xx, régie par le
Code des assurances, supervised by the ACPR. First-party carrier: the IPIDs name Thélem
itself as the insurer, so there is no fronting question here. In the ACPR register:
THELEM ASSURANCES, Code des assurances, 14 branches, group THELEM.

One page lists the whole public library as direct `.pdf` hrefs. Everything below was
fetched and verified as `%PDF` on 2026-07-30.

## What the library is, and is not

45 documents, **all IPID** (Document d'Information sur le Produit d'Assurance)
except two reimbursement-example annexes for the health range. Thélem publishes no
conditions générales. That is the French norm rather than a Thélem gap: the DDA requires
the IPID to be public, it does not require the CG to be. Expect ~2 pages and ~8 000
characters per document, against 50+ pages for a Belgian CG.

## Traps found while enumerating (do not re-derive)

1. **The site labels and the PDFs disagree.** Ten documents carry an anchor label on the
   library page that differs from the `Produit :` line inside the PDF, and for two of them
   the labels are effectively swapped: TA 483 is labelled *Multirisque Habitation
   Propriétaire non Occupant* on the site but says *Assurance multirisque immeuble*
   inside, while TA 621 is labelled *multirisque immeuble PNO* and says *multirisque
   habitation Propriétaire non occupant*. **The document wins** (rule 3). `product_name`
   below is the `Produit :` line, falling back to the site label only where the Produit
   line does not distinguish two documents.
2. **The CMS re-uploads the same file under a second `/YYYY/MM/` path.** Three URLs were
   dropped as re-uploads. Two of them are NOT byte-identical and NOT text-identical:
   they differ only by a trailing product-code fragment (`– DG 810`, a stray `–`) on the
   Produit line. Neither a sha256 nor a normalised-text hash catches them; they were
   confirmed by reading both. Dropped:
   - `IPID_TA_810_DCBAT_-012025.pdf` (2025/09) = `IPID_TA_810_DCBAT_-012025.pdf`
   - `IPIP_-MRP-PME-PMI-Aout-2025.pdf` (2025/09) = `IPIP_-MRP-PME-PMI-Aout-2025.pdf`
   - `IPID_TA_810_DCBAT_-012025-1.pdf` (2025/12) = `IPID_TA_810_DCBAT_-012025.pdf`
3. **TA 483 and TA 630 share a `Produit :` line** (*Assurance multirisque immeuble*) with
   editions 07/2023 and 08/2025, which looks like two editions of one product. It is not.
   Reading the documents in full shows each names its own variant: **TA 483 is
   PROPRIETAIRE NON OCCUPANT, TA 630 is COPROPRIETE**. They are parallel variants, not
   editions (rule 8), and neither supersedes the other. This was initially modelled the
   wrong way from the `Produit :` line alone and corrected from the extraction; the lesson
   is that the Produit line is a name, not a product identity.

## Site label vs Produit line, all divergences

| file | site label | Produit line |
|---|---|---|
| `IPID_TA_580_Camping-cars-012026.pdf` | Assurance Camping cars | Assurance Camping-Car |
| `IPID_TA_570-Dommages-aux-biens.pdf` | Assurance Dommages aux biens | Assurance multirisque habitation |
| `IPID_TA_483-MRI-PNO-juillet-2023.pdf` | Assurance Multirisque Habitation Propriétaire non Occupant | Assurance multirisque immeuble |
| `IPID_TA_621-PNO-janvier-2026.pdf` | Assurance multirisque immeuble Propriétaire non Occupant | Assurance multirisque habitation Propriétaire non occupant |
| `IPID_TA_710-Evolution-Resp-janvier-2026.pdf` | Assurance Complémentaire Santé – Evolution – gamme responsable et solidaire | Assurance Complémentaire Santé – gamme responsable et solidaire |
| `IPID_TA_710-Evolution-NResp-janvier-2024.pdf` | Assurance Complémentaire Santé – Evolution | Assurance Complémentaire Santé – gamme non responsable et solidaire |
| `IPID_TA_201_Garauto-Aout-2025.pdf` | Assurances pour les professionnels de l’automobile | Assurance Garauto |
| `IPID_TA_-TERRENIS-01-2026.pdf` | Assurance Multirisque agricole | Assurance Terrenis |
| `IPID_TA_RCPRO.pdf` | Assurance Responsabilité Chef d’entreprise | Responsabilité Civile Chef d’Entreprise/ Professions libérales |
| `IPID_TA_810_DCBAT_-012025.pdf` | Assurance Responsabilité civile Entreprises du bâtiment | DCBAT / Responsabilité Décennale des entreprises du Bâtiment |

## Documents

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Assurance Engins agricoles | ipid | agricole | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/Ipid-EA-2026.pdf |
| Assurance Terrenis | ipid | agricole | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_-TERRENIS-01-2026.pdf |
| Assurance Automobile | ipid | auto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA-012026.pdf |
| Assurance Camping-Car | ipid | auto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_580_Camping-cars-012026.pdf |
| Assurance Caravane | ipid | auto | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_90B_Caravane-juillet-2023.pdf |
| Assurance Engins de chantiers | ipid | auto | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/Ipid-EC-2026.pdf |
| Assurance Flotte Automobile | ipid | auto | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_Flotte-standard-juillet-2023.pdf |
| Assurance Véhicule de collection | ipid | auto | 2024-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_13R_collection-juillet-2024.pdf |
| Assurance Véhicule de plus de 3,5 tonnes | ipid | auto | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_13S_Camions-juillet-2023.pdf |
| Assurance chasse | ipid | chasse | 2024-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_Chasse-332-juillet-2024.pdf |
| DCBAT / Responsabilité Décennale des entreprises du Bâtiment | ipid | decennale | 2025-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_810_DCBAT_-012025.pdf |
| Assurance EDPM | ipid | edpm | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_EDPM-012026.pdf |
| Assurance Emprunteur | ipid | emprunteur | 2025-06 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_488_juin-2025.pdf |
| Assurance Accidents de la vie privée | ipid | gav | 2025 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_700-ACCVP-08-2025.pdf |
| Assurance Dommages aux biens | ipid | habitation |  | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_570-Dommages-aux-biens.pdf |
| Assurance Multirisque Habitation | ipid | habitation | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_601-Occupants-janvier-2026.pdf |
| Assurance multirisque habitation Propriétaire non occupant | ipid | habitation | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2026/03/IPID_TA_621-PNO-janvier-2026.pdf |
| Assurance multirisque habitation du mobil home | ipid | habitation | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_611-mobilhome-janvier-2026.pdf |
| Assurance multirisque immeuble (superseded) | ipid | habitation | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2026/03/IPID_TA_483-MRI-PNO-juillet-2023.pdf |
| Assurance multirisque immeuble | ipid | habitation | 2025-08 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_630-MRI-aout-2025.pdf |
| Assurance Cyclo | ipid | moto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_Cyclo-012026.pdf |
| Assurance Moto | ipid | moto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_Moto-012026.pdf |
| Assurance Quad | ipid | moto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_Quad-012026.pdf |
| Assurance Voiturette | ipid | moto | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_Voiturette-012026.pdf |
| Assurance Garauto | ipid | multirisque-professionnelle | 2025-08 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_201_Garauto-Aout-2025.pdf |
| Assurance multirisque professionnelle | ipid | multirisque-professionnelle | 2025-08 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPIP_-MRP-PME-PMI-Aout-2025.pdf |
| Bris de machine | ipid | multirisque-professionnelle | 2023-06 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_26_BDM-juin-2023.pdf |
| Assurance Initiative Obsèques Capital | ipid | obseques | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_419-IOC-2026.pdf |
| Assurance Initiative Obsèques Services | ipid | obseques | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_IOS-418-2026.pdf |
| Assurance Capital Décès | ipid | prevoyance | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_396-capital-deces-juillet-2023.pdf |
| Assurance Protection famille | ipid | prevoyance | 2025-08 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_Protection-famille-572_082025.pdf |
| Prévoyance Agri | ipid | prevoyance | 2024-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_PREVAGRI_440_072024.pdf |
| Prévoyance Pro | ipid | prevoyance |  | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_prev-pro-ISIS.pdf |
| Prévoyance Pro Madelin | ipid | prevoyance |  | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TP_Prev-madelin_ISIS_v2.pdf |
| Assurance Protection Juridique du particulier | ipid | protection-juridique | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_PJ_PART_012026_VF.pdf |
| Assurance Protection Juridique du professionnel | ipid | protection-juridique | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_PJ-PRO_012026.pdf |
| Assurance Protection Juridique du professionnel agricole | ipid | protection-juridique | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_PJ-PRO-AGRI_012026.pdf |
| Assurance responsabilité civile association | ipid | rc-privee | 2023-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_RC-AssociationDG-477-CS-437-juillet-2023.pdf |
| Assurance responsabilité civile vie privée | ipid | rc-privee | 2024-07 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_RCVP-CS-456-juillet-2024.pdf |
| Responsabilité Civile Chef d’Entreprise/ Professions libérales | ipid | rc-professionnelle |  | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_RCPRO.pdf |
| Assurance Complémentaire Santé – gamme non responsable et solidaire | ipid | sante | 2024-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_710-Evolution-NResp-janvier-2024.pdf |
| Assurance Complémentaire Santé – gamme responsable et solidaire | ipid | sante | 2026-01 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_710-Evolution-Resp-janvier-2026.pdf |
| Exemples de remboursements formules NON RESPONSABLES | other | sante | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/Exemples_remboursements_TA_2026_NON_RESPONSABLE.pdf |
| Exemples de remboursements formules RESPONSABLES | other | sante | 2026 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/Exemples_remboursements_TA_2026_RESPONSABLE.pdf |
| Assurance scolaire et extra-scolaire | ipid | scolaire | 2024-09 | fr | https://www.thelem-assurances.fr/wp-content/uploads/2025/12/IPID_TA_scolaire-19-septembre-2024.pdf |
