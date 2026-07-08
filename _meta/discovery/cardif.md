# cardif — BNP Paribas Cardif Belgium (credit / payment protection insurer)
website: https://www.bnpparibascardif.be
library: https://bnpparibascardif.be/fr/informations-juridiques (section "Conditions générales", Liferay document store /documents/36051/...)
fetch: httpx (Liferay download URLs, ?download=true)
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Hypo Protect CLASSIC et 2WIN | conditions_generales | autres | ? | fr | https://bnpparibascardif.be/documents/36051/36444/Hypo+Protect+CLASSIC+et+2WIN.pdf/5df2b90a-4cbe-e102-f577-f5760c733a1b?version=1.3&t=1732007179273&download=true |
| Hypo Protect Luxembourg | conditions_generales | autres | ? | fr | https://bnpparibascardif.be/documents/36051/427355/Hypo+Protect+Luxembourg.pdf/a9f52cb5-fafb-fae2-30fd-d7be2ed9519b?version=1.1&t=1703113548436&download=true |
| Short Term Protect Classic et 2WIN | conditions_generales | autres | ? | fr | https://bnpparibascardif.be/documents/36051/427355/Short+Term+Protect+Classic+et+2WIN.pdf/0bebb643-def2-82de-a852-b86656a67600?version=1.1&t=1703114846510&download=true |
| Short Term Protect Business | conditions_generales | autres | ? | fr | https://bnpparibascardif.be/documents/36051/427355/Short+Term+Protect+Business.pdf/c711fc99-68d6-2090-e27d-03b13ffc4f8b?version=1.1&t=1703113515816&download=true |
| Short Term Protect Luxembourg | conditions_generales | autres | ? | fr | https://bnpparibascardif.be/documents/36051/427355/Short+Term+Protect+Luxembourg.pdf/4cbb82d8-0e72-f90c-cb18-dcc8d4798ffe?version=1.1&t=1703113400716&download=true |
| Hypo Protect (fiche client IU) | product_sheet | autres | 2024-06 | fr | https://bnpparibascardif.be/documents/36051/36444/202406_Fiche+client_HYPO_IU_FR.pdf |

notes:
- BNP Paribas Cardif Belgium is a credit / payment protection insurer. Hypo Protect = assurance solde restant du
  (decreasing term death cover on a mortgage, may include incapacity riders). Short Term Protect = payment
  protection on temperament / consumer loans (death, incapacity, involuntary unemployment). No pure "vie" branch
  exists in the taxonomy and these are not savings products, so they are filed under autres (credit protection).
- Docs enumerated from the "Informations juridiques" page (Conditions générales section). Liferay download URLs
  carry version/token query params but resolve to public PDFs over plain httpx.
- Hypo Protect Luxembourg and Short Term Protect Luxembourg are the Luxembourg-market variants, published on the
  Belgian site; kept for completeness and marked as such.
- NL equivalents exist on the same store (/documents/36051/...); FR captured.
