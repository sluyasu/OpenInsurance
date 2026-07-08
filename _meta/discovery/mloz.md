# mloz — MLOZ Insurance (INS ?)
website: www.mloz.be
library: https://www.mloz.be/fr/conditions-generales-assurances-mloz-insurance , https://www.mloz.be/fr/documents-dinformations-produit , https://www.mloz.be/sites/default/files/docs_juridiques/
fetch: httpx
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Hospitalia Care | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Care_Gen_FR._2026.pdf |
| Hospitalia Smart | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Smart_Con_Gen_FR_2026.pdf |
| Hospitalia Plus | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/HospPlus_Con_Gen_FR_2026%20%281%29.pdf |
| Hospitalia Continuité | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hospitalia_Continuite_Con_Gen_FR_2026.pdf |
| Hospitalia Ambulatoire | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Ambulatoire_Con_Gen_FR_2026.pdf |
| Medicalia | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Medicalia_Con_Gen_FR_2026.pdf |
| Forfait H | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/ForfaitH_Con_Gen_FR_2026.pdf |
| Garantie Maladies Graves (GMG) | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/GMG_Con_Gen_FR_2026.pdf |
| Dentalia Plus | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Dentalia_Plus_Con_Gen_FR_2026.pdf |
| Dentalia Up | conditions_generales | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Dentalia_Up_Con_Gen_FR_2026.pdf |
| Hospitalia Care | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Care_IPID_FR_2026.pdf |
| Hospitalia Smart | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Smart_IPID_FR_2026.pdf |
| Hospitalia Plus | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Plus_IPID_FR_2026.pdf |
| Hospitalia Continuité | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Continuite_IPID_FR_2026.pdf |
| Hospitalia Ambulatoire | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Hosp_Ambu_IPID_FR_2026.pdf |
| Medicalia | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Medicalia_IPID_FR_2026.pdf |
| Forfait H | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/ForfaitH_IPID_FR_2026.pdf |
| Dentalia Plus | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Dentalia_Plus_IPID_FR_2026.pdf |
| Dentalia Up | ipid | sante | 2026 | fr | https://www.mloz.be/sites/default/files/docs_juridiques/Dentalia_Up_IPID_FR_2026.pdf |

notes: MLOZ Insurance SA is the VMOB (risk carrier) for the entire Hospitalia / Dentalia / Medicalia / Forfait H / GMG range distributed by the Mutualités Libres group (Partenamut, Helan, etc.). These CG/IPID on mloz.be are effectively the master source documents; partenamut.be and helan.be republish the SAME product range per-language (see those files) — model once, alias per-mutualité to avoid duplication. All FR 2026 editions listed above are current. NL mirrors exist in the same docs_juridiques dir (e.g. HospPlus_Con_Gen_NL_2026.pdf) and EN mirrors too (CG_HCare_EN_2026.pdf, IPID_HospitaliaCare_EN.pdf, etc.) — full FR/NL/EN trilingual set. Superseded editions also present in docs_juridiques/: 2023 (*_con_gen_fr_2023.pdf), 2024 (OK_*_CondGen FR 2024.pdf), 2025 (*_CondGen FR 2025.pdf). Base "Hospitalia" product (24122024-Hosp_Con_Gen_FR2025.pdf) appears superseded by the Care/Smart split in 2026. "Hospitalia Medium" has only a 2025 CG (Hosp Medium_CondGen FR 2025.pdf), no 2026 edition — likely closed to new business. GMG has a CG but no standalone FR IPID in the 2026 set. All fetched via curl/httpx (site is Drupal, static PDFs, no WAF).
