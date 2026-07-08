# dela — DELA (DELA Natura- en Levensverzekeringen N.V., succursale belge) (INS 2864)
website: dela.be
library: https://www.dela.be/fr/mentions-legales/documentation-assurances (FR) ; https://www.dela.be/nl/juridische-informatie/documentatie-verzekeringen (NL)
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Plan de Prévoyance obsèques DELA | conditions_generales | obseques | 2026-01 | fr | https://www.dela.be/-/media/corporate/documenten/productdocumenten/20260101-dela-uzpn-algemene-voorwaarden-a4-fr.ashx |
| Plan de Prévoyance obsèques DELA | ipid | obseques | ? | fr | https://www.dela.be/-/media/corporate/documenten/productdocumenten/infofiche%20plan%20de%20prevoyance%20obseques%20dela.ashx |
| Plan de Prévoyance Héritage DELA | conditions_generales | epargne | ? | fr | https://www.dela.be/-/media/corporate/documenten/productdocumenten/nzp/fr%20conditions%20gnrales%20plan%20de%20prvoyance%20hritage.ashx |
| Plan de Prévoyance Héritage DELA | ipid | epargne | ? | fr | https://www.dela.be/-/media/corporate/documenten/productdocumenten/nzp/fr%20fiche%20dinformations%20plan%20de%20prvoyance%20hritage.ashx |

notes: DELA is its own risk carrier — "DELA Natura- en levensverzekeringen N.V. - succursale belge (0665.931.229), agréée pour les assurances-vie de la branche 21 sous le n° de code 2864" (matches INS 2864). Two products, both branch-21 life insurance: (1) Plan de Prévoyance obsèques DELA = funeral/death-capital cover (branch=obseques); (2) Plan de Prévoyance Héritage DELA = death-capital for succession costs (classed branch=epargne here as a branche-21 product; there is no generic "vie" branch in the enum). doc_type=ipid rows are the "Fiche d'information" summary sheets — for branche-21 life products this is the fiche d'information financière (IPID-equivalent; a PRIIPs KID may also apply). Extra Héritage docs on the same page, not product conditions so not tabled: "Critères de segmentation" (https://www.dela.be/-/media/corporate/documenten/productdocumenten/nzp/fr%20critres%20de%20segmentation%20plan%20de%20prvoyance%20hritage.ashx) and "Devoir de diligence" (https://www.dela.be/-/media/corporate/documenten/productdocumenten/nzp/fr%20devoir%20de%20diligence%20plan%20de%20prvoyance%20hritage.ashx). Obsèques CG edition = V01/01/2026 (filename 20260101); other editions not dated on page (?). Only FR fetched; identical NL library at the NL URL above (…algemene-voorwaarden-a4-nl / nl-labelled .ashx equivalents) not enumerated. .ashx = Sitecore media handler that serves the underlying PDF.
