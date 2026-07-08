# actel — Actel (P&V Group direct auto brand) (NBB INS ?)
website: https://www.actel.be
library: https://www.actel.be/fr/conditions-generales (CG) + https://www.actel.be/fr/ipid (IPID) — NL: /algemene-voorwaarden + /ipid
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Assurance Auto Actel | conditions_generales | auto | ? | fr | https://www.actel.be/documents/d/actel/conditions-generales-auto-fr?download=true |
| Assurance Auto Actelaffinity | conditions_generales | auto | ? | fr | https://www.actel.be/documents/d/actel/conditions-generales-auva-fr?download=true |
| Actel Individuelles Circulation | conditions_generales | accidents | ? | fr | https://www.actel.be/documents/d/actel/conditions-generales-individuelles-fr?download=true |
| Assurance Auto Acteldirect (Start / Mini-Omnium / Maxi-Omnium / Vol / Confort Conducteur / Confort Assistance / Confort Juridique) | conditions_generales | auto | ? | fr | https://www.actel.be/documents/d/actel/assurance-auto-actel-conditions-generales-start-mini-omnium-maxi-omnium-vol-confort-conducteur-confort-assistance-confort-juridique-?download=true |
| Assurance Auto Acteldirect — garantie «Bob» | conditions_generales | auto | ? | fr | https://www.actel.be/documents/d/actel/assurance-auto-actel-garantie-bob?download=true |
| Assurance Incendie Acteldirect (Assistance Habitation / Assurance Habitation / Assurance familiale) | conditions_generales | habitation | ? | fr | https://www.actel.be/documents/d/actel/assurance-incendie-actel-conditions-generales-assistance-habitation-assurance-habitation-assurance-familiale-?download=true |
| Assurance Moto Actel | conditions_generales | auto | ? | fr | https://www.actel.be/documents/d/actel/conditions-generales-moto-fr?download=true |
| IPID Auto | ipid | auto | ? | fr | https://www.actel.be/documents/d/actel/ipid-auto-fr |
| IPID Moto | ipid | auto | ? | fr | https://www.actel.be/documents/d/actel/ipid-moto_fr |

notes:
- Actel is the online direct brand of P&V Group. Both library pages fully scraped: /fr/conditions-generales (7 CG PDFs) and /fr/ipid (2 IPID PDFs). Complete for the FR site.
- Mostly auto (the brand is auto-first); one fire/home CG bundles Assistance Habitation + Habitation + Assurance familiale (tagged habitation); "Individuelles Circulation" = individual traffic-accident cover (tagged accidents).
- Editions not exposed in link text — these are Liferay document endpoints (/documents/d/actel/<slug>[?download=true]); edition dates would require opening each PDF.
- NL equivalents: /algemene-voorwaarden and /ipid (same document store). FR captured.
