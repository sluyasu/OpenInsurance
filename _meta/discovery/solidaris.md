# solidaris — Solidaris (Assurance Hospitalisation "Hospimut") (INS ?)
website: www.solidaris.be (product docs on regional sites: www.solidaris-brabant.be, www.solidaris-wallonie.be)
library: https://www.solidaris-brabant.be/fr/assurances-facultatives/assurances-hospitalisation/hospimut , https://www.solidaris-wallonie.be/couverture/hospitalisation/
fetch: httpx
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Hospimut | conditions_generales | sante | 2026 | fr | https://www.solidaris-brabant.be/sites/default/files/uploads/Solidaris%20Brabant%20Assurances-Solidaris%20Brabant%20Verzekeringen/CondGenerales-AlgVoorwaarden/CG_Hospimut_2026_FR.pdf |
| Hospimut | ipid | sante | 2026 | fr | https://www.solidaris-brabant.be/sites/default/files/uploads/Solidaris%20Brabant%20Assurances-Solidaris%20Brabant%20Verzekeringen/Fiches-Guides/Fiche-Hospimut_FR_2026.pdf |
| Hospimut | ipid | sante | 2022 | fr | https://www.solidaris-wallonie.be/api/wp-content/uploads/2021/12/2.-Fiche-Infos-2022-Hospimut.pdf |

notes: SEPARATE from the Hospitalia/MLOZ range — Solidaris is the socialist mutualité (NOT a Mutualité Libre); its hospitalisation product is "Hospimut", underwritten by Solidaris' own regional VMOBs (e.g. "Solidaris Brabant Assurances / Verzekeringen"). Do NOT alias to MLOZ. Solidaris is federated into regional entities each with its own site and doc library: Solidaris Brabant (bilingual FR/NL, cleanest — carries current 2026 CG + Fiche/IPID), Solidaris Wallonie (FR, WordPress, older 2022 IPID found), plus Solidaris Liège, Solidaris Centre, etc. The main www.solidaris.be is a JS portal shell (curl returned a 6 KB stub) that links out to regional sites — discovery done via firecrawl_search, extraction via curl on the regional Drupal sites. Solidaris Brabant's uploads path (…/Solidaris Brabant Assurances-Solidaris Brabant Verzekeringen/) also holds NL versions (CG/Fiche _NL_) and adjacent products (e.g. Dentimut dental, Declaration forms) not fully enumerated here — expand at ingest. A "Declaration_Hospimut FR.pdf" (membership declaration form, not a doc_type) sits in the same tree. status=enum for the Hospimut hospitalisation core; the full multi-region, multi-product catalog is larger.
