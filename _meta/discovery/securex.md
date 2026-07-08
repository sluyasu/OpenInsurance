# securex — Securex (Vie INS 944 / Caisse AT INS 519 / Risques Divers INS 805)
website: www.securex.be
library: https://www.securex.be/fr/independants/assurances/vous-proteger/life-at-ease ; PDFs served from https://www.securex.be/getmedia/...
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Life@Ease (Securex Vie) — Conditions générales CGUL-L@E-202312 | conditions_generales | pension | 2023-12 | fr | https://www.securex.be/getmedia/9651944d-ef3a-4018-b537-7275a45bdbd8/CGUL-L@E-202312-202601.pdf |
| Life@Ease PLCI (Securex Vie) — Fiche Info | kid | pension | 2026-01 | fr | https://www.securex.be/getmedia/883662d2-1438-442b-b0c0-3bd90ba0f6f0/PCLI-Fiche-Info-01012026.pdf |
| Life@Ease PLCI sociale / Convention INAMI (Securex Vie) — Fiche Info | kid | pension | 2025-07 | fr | https://www.securex.be/getmedia/7863665f-eace-47ca-ab7f-cbede7b9dd72/INAMI-Fiche-Info-14072025.pdf |
| Life@Ease EIP (Securex Vie) — Fiche Info | kid | pension | 2025-01 | fr | https://www.securex.be/getmedia/bd798ee2-8434-4380-8641-37f4260c5879/EIP-Fiche-Info-01012025.pdf |
| Life@Ease CPTI (Securex Vie) — Fiche Info | kid | pension | 2020-10 | fr | https://www.securex.be/getmedia/b9802ea0-a663-480f-a725-0b2d45053823/cpti-fiche-info-01102020.pdf |
| Life@Ease Épargne-pension & Épargne long terme (Securex Vie) — Fiche Info Financière | kid | epargne | 2020-10 | fr | https://www.securex.be/getmedia/e1371597-a003-4d64-85a3-b6e72480b111/fr-2020_10_financiele-infofiche-ps-en-lts-life@ease-final.pdf |
| PLCI — Document d'information pension complémentaire (2e pilier) | kid | pension | ? | fr | https://www.securex.be/getmedia/727f8d55-40a8-47b4-acea-4784d8952da4/Document-d-information-PCLI.pdf |
| EIP dirigeant — Document d'information pension complémentaire (2e pilier) | kid | pension | ? | fr | https://www.securex.be/getmedia/304f4478-a119-4d65-8dab-d712a744b7b8/Document-d-information-EIP-dirigeant-d-entreprise-independant.pdf |

notes:
- Securex Vie SA is the fund's OWN life insurer (INS 944); Life@Ease is its modular life product covering pension (PLCI/EIP/CPTI/épargne), revenu de remplacement en cas d'incapacité de travail, and décès. The CGUL-L@E-202312 conditions générales govern all Life@Ease modules — genuine own CG.
- Revenu garanti here is a Life@Ease optional life-cover module (governed by the CGUL), not a standalone non-life IPID product; no separate revenu-garanti IPID found.
- "Fiche Info" / "Fiche Info Financière" / "Document d'information (2e pilier)" bucketed under kid (nearest enum) — regulated pre-contractual info sheets for the life modules, not strictly PRIIPs KIDs.
- Superseded: PLCI Fiche Info 2025-11 (https://www.securex.be/getmedia/1540a14a-35cd-4877-aa25-0f7479bf2042/PCLI-Fiche-Info-01112025.pdf) replaced by the 2026-01 edition above.
- Also public but not a listed doc type: "technische fiche Life@Ease" FR 2025-11 (https://www.securex.be/getmedia/28365438-5b2a-42ab-bdb7-4d1d319d99a3/2025_11-technische-fiche-Life@Ease_FR.pdf); its 2020-10 predecessor is superseded.
- NOT covered this pass: Securex Caisse Commune d'assurances accidents du travail (INS 519) and Risques Divers (INS 805) — separate carriers; their non-life IPID/CG were not enumerated here and warrant a follow-up.
- nl versions of the getmedia PDFs exist.
