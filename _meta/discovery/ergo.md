# ergo — ERGO Insurance SA/NV Belgium (Munich Re / ERGO Group; life + accident) (NBB INS ?)
website: https://www.ergo.be
library: https://www.ergo.be/fr_be/infos-produits (FR "Informations produit" / NL https://www.ergo.be/nl_be/productinformatie) — direct PDF links per product; PRIIPs KID portal for branch-23 funds at https://ergo-be.insurances.priips.clever-soft.com/fr/
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Free | kid | epargne | ? | fr | https://www.ergo.be/priips/free%20%20111107%20fr.pdf |
| Program | kid | epargne | ? | fr | https://www.ergo.be/priips/program%20dd120305%20fr.pdf |
| Management | kid | epargne | ? | fr | https://www.ergo.be/priips/management%20120102%20fr.pdf |
| T50 | kid | autres | ? | fr | https://www.ergo.be/priips/t50fr_v1dd140414.pdf |
| inSure Accident | ipid | accidents | ? | fr | https://www.ergo.be/priips/ergo-00612_ipid-fr.pdf |
| CDCA | kid | epargne | ? | fr | https://www.ergo.be/priips/cdcafr_v1dd140414.pdf |
| EL | kid | epargne | ? | fr | https://www.ergo.be/priips/elfr_v1dd140414.pdf |
| Terme Fixe | kid | epargne | ? | fr | https://www.ergo.be/priips/terme_fixefr_010210.pdf |

notes:
- ERGO Insurance SA (Munich Re / ERGO Group) — mostly a branch 21/23 life-savings & pension book (largely legacy/run-off, distributed historically under ERGO brand), plus one non-life accident product (inSure Accident). The 8 PDFs above are the "essential product information" documents (KID-equivalent) except inSure Accident which is an explicit IPID (filename ...ipid-fr.pdf).
- Editions marked "?": the filename tokens (111107, dd120305, 120102, v1dd140414, 010210) look like internal product/version codes and predate the PRIIPs KID era (2018), so they were NOT interpreted as edition dates. These are the current documents linked on the live product page.
- branch guesses: Free/Program/Management/CDCA/EL/Terme Fixe = branch 21/23 life savings (tagged epargne); T50 = unclear (tagged autres); inSure Accident = accidents.
- Additional (not product CG/IPID/KID, so not listed as rows): branch-23 fund barometer PDF (Fondsenbarometer, June 2026) and current guaranteed interest rates page; full branch-23 KID set on the clever-soft PRIIPs portal.
- NL mirror at https://www.ergo.be/nl_be/productinformatie ("Essentiële productinformatie"). FR captured.
