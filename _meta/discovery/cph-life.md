# cph-life — CPH LIFE (INS 2539)
website: cph.be
library: https://www.cph.be/assurances/
fetch: httpx
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| CPH Protect CT (solde restant dû, court terme) | conditions_generales | autres | ? (réf. PROT038) | fr | https://www.cph.be/fichiers/PROT038-–-CPH-Protect-CT-conditions-generales.pdf |
| CPH Protect CT (solde restant dû, court terme) | kid | autres | ? | fr | https://www.cph.be/fichiers/Fiche-dinformation-financiere-CPH-Protect-CT-1.pdf |
| CPH Protect LT (solde restant dû, long terme) | conditions_generales | autres | ? (réf. PROT002) | fr | https://www.cph.be/fichiers/PROT002-CPH-Protect-LT-conditions-generales.pdf |
| CPH Protect LT (solde restant dû, long terme) | kid | autres | ? | fr | https://www.cph.be/fichiers/Fiche-dinformation-financiere-CPH-Protect-LT-2.pdf |
| CPH Quiétude | conditions_generales | autres | ? (réf. QUI001) | fr | https://www.cph.be/fichiers/QUI001-–-Quietude-–-Conditions-generales.pdf |
| CPH Quiétude | kid | autres | ? | fr | https://www.cph.be/fichiers/Fiche-dinformation-CPH-Assurance-Quietude-1.pdf |
| CPH Life Assurance Epargne Pension (branche 21) | conditions_generales | pension | ? (réf. AEPT013) | fr | https://www.cph.be/fichiers/AEPT013-–-AEP-Conditions-generales.pdf |
| CPH Life Assurance Epargne Pension (branche 21) | kid | pension | ? | fr | https://www.cph.be/fichiers/Fiche-dinformation-financiere-CPH-Life-Assurance-Epargne-Pension-4.pdf |

notes: doc_type "kid" here = Fiche d'Information Financière (FIF) assurance-vie, the Belgian pre-contractual info sheet used by CPH (mapped to the nearest enum value; strictly a FIF, not a PRIIPs KID). CPH LIFE = the life-insurance arm of Banque CPH — 4 products, each with CG + FIF: "solde restant dû" = decreasing-term mortgage life (CT = court terme / single premium, LT = long terme); CPH Quiétude = a life/death product (exact branch not stated on the page → autres); CPH Life Assurance Epargne Pension = branch 21 pension-savings (3rd pillar). Editions not printed on the product pages — PROT038 / PROT002 / QUI001 / AEPT013 are the product/version reference codes. An extra "Document d'information — Droit à l'oubli" PDF is linked from the Protect LT page (info doc, not one of the 4 doc types, so excluded). Fetched via httpx/curl after Firecrawl returned ERR_TUNNEL_CONNECTION_FAILED twice on cph.be. NL site exists.
