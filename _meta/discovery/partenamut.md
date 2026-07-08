# partenamut — Partenamut (INS ?)
website: www.partenamut.be
library: https://www.partenamut.be/fr/informations-juridiques/conditions-generales-assurance
fetch: httpx
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Hospitalia | conditions_generales | sante | 2024 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5726&filename=conditions-generales-assurance-hospitalisation-hospitalia-2024.pdf |
| Hospitalia Medium | conditions_generales | sante | 2024 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5727&filename=conditions-generales-assurance-hospitalisation-hospitalia-medium-2024.pdf |
| Hospitalia Plus | conditions_generales | sante | 2024 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5728&filename=conditions-generales-assurance-hospitalisation-hospitalia-plus-2024.pdf |
| Hospitalia Continuité | conditions_generales | sante | 2024 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5729&filename=conditions-generales-assurance-hospitalisation-hospitalia-continuite-2024.pdf |
| Hospitalia Ambulatoire | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5724&filename=conditions-generales-assurance-hospitalisation-hospitalia-ambulatoire-2025.pdf |
| Medicalia | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5722&filename=conditions-generales-assurance-medicalia-2025.pdf |
| Forfait H | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5723&filename=conditions-generales-assurance-forfait-h-2025.pdf |
| Garantie Maladies Graves | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5725&filename=conditions-generales-garantie-maladies-graves-2025.pdf |
| Dentalia Plus | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5720&filename=conditions-generales-assurance-dentaire-dentalia-plus-2025.pdf |
| Dentalia Up | conditions_generales | sante | 2025 | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5721&filename=conditions-generales-assurance-dentaire-dentalia-up-2025.pdf |
| Hospitalia | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4946&filename=infofiche-hospitalia.pdf |
| Hospitalia Medium | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5162&filename=infofiche-hospitalia-medium.pdf |
| Hospitalia Plus | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4945&filename=infofiche-hospitalia-plus.pdf |
| Hospitalia Continuité | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4949&filename=infofiche-hospitalia-continuite.pdf |
| Hospitalia Ambulatoire | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4950&filename=infofiche-hospitalia-ambulant.pdf |
| Medicalia | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4944&filename=infofiche-medicalia.pdf |
| Forfait H | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4947&filename=infofiche-forfait-h.pdf |
| Dentalia Plus | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=4948&filename=infofiche-dentalia-plus.pdf |
| Dentalia Up | ipid | sante | ? | fr | https://my.partenamut.be/ajax/documentPreview.html?id=5430&filename=infofiche-dentalia-up.pdf |

notes: SHARED RANGE — Partenamut is a Mutualité Libre; its hospitalisation/dental products (Hospitalia*, Medicalia, Forfait H, Dentalia*, GMG) are the SAME range underwritten by MLOZ Insurance (see mloz.md). Partenamut hosts its own PDF copies on my.partenamut.be (documentPreview.html?id=…). Model the product once (MLOZ) and treat Partenamut as a distributor edition, but note the edition YEARS differ: Partenamut still serves 2024 CG for Hospitalia/Medium/Plus/Continuité and 2025 for the others, whereas mloz.be already serves 2026 — so the Partenamut PDFs may be a version behind. NL "algemene voorwaarden 2025" mirrors also exist on the same page (documentPreview ids 5730-5738, e.g. algemene-voorwaarden-hospitalisatieverzekering-hospitalia-2025.pdf) plus a 2026 NL Hospitalia Plus at https://www.partenamut.be/dam/jcr:ee2c572e-5fea-40b2-ae6a-9c4bc7791d84/Algemene%20voorwaarden%20hospitalisatieverzekering%20Hospitalia%20Plus%20-%2001012026.pdf . The infofiche-* PDFs carry no year in filename (edition ?) and are the IPIDs. Non-doc-type product brochures (documentPreview ids 4936-4943, plain names like hospitalia.pdf) were excluded. Bundled precontractual-info PDF: id=5420 (FR) / id=5421 (NL). All fetched via curl/httpx.
