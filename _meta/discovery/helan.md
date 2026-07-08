# helan — Helan (ex-OZ / Partena Ziekenfonds) (INS ?)
website: www.helan.be
library: https://www.helan.be/nl/over-ons/juridische-info/vmob-mloz-insurance/
fetch: httpx
status: enum
lang: nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Hospitalia | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3882&filename=Hospitalia-Algemene-voorwaarden-2026.pdf |
| Hospitalia Plus | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3879&filename=Hospitalia-Plus-Algemene-voorwaarden-2026.pdf |
| Hospitalia Continuiteit | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3876&filename=Hospitalia-Continuiteit-Algemene-voorwaarden-2026.pdf |
| Hospitalia Medium | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3873&filename=Hospitalia-Medium-Algemene-voorwaarden-2026.pdf |
| Hospitalia Ambulant | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3870&filename=Hospitalia-Ambulant-Algemene-voorwaarden-2026.pdf |
| Medicalia | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3885&filename=Medicalia-Algemene-voorwaarden-2026.pdf |
| Forfait H | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3867&filename=Forfait-H-Algemene-voorwaarden-2026.pdf |
| Waarborg zware ziekten (GMG) | conditions_generales | sante | 2025 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3888&filename=Waarborg-zware-ziekten-Algemene-voorwaarden-2025.pdf |
| Dentalia Plus | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3865&filename=Dentalia-Plus-Algemene-Voorwaarden-2026.pdf |
| Dentalia Up | conditions_generales | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3862&filename=Dentalia-Up-Algemene-Voorwaarden-2026.pdf |
| Hospitalia Care | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3904&filename=Hospitalia-Care-Informatiedocument-2026.pdf |
| Hospitalia Smart | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3913&filename=Hospitalia-Smart-Informatiedocument-2026.pdf |
| Hospitalia Plus | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3910&filename=Hospitalia-Plus-Informatiedocument-2026.pdf |
| Hospitalia Continuiteit | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3908&filename=Hospitalia-Continuiteit-Informatiedocument-2026.pdf |
| Hospitalia Ambulant | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3902&filename=Hospitalia-Ambulant-Informatiedocument-2026.pdf |
| Medicalia | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3917&filename=Medicalia-Informatiedocument-2026.pdf |
| Forfait H | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3898&filename=Forfait-H-Informatiedocument-2026.pdf |
| Dentalia Plus | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3892&filename=Dentalia-Plus-Informatiedocument-2026.pdf |
| Dentalia Up | ipid | sante | 2026 | nl | https://mijn.helan.be/ajax/documentPreview.htm?id=3893&filename=Dentalia-Up-Informatiedocument-2026.pdf |

notes: SHARED RANGE — Helan (Flemish Mutualité Libre, ex-OZ / Partena) distributes the SAME MLOZ Insurance Hospitalia range as mloz.md and partenamut.md; the library page is literally titled "VMOB MLOZ Insurance" and confirms MLOZ Insurance is the risk carrier. Helan hosts NL-only copies on mijn.helan.be (documentPreview.htm?id=…). Model the product once (MLOZ), alias Helan as the NL distribution edition. Note the naming-transition quirk shared with MLOZ: the CG PDFs still use legacy product names (Hospitalia / Hospitalia Medium) while the 2026 IPIDs already use the new Care/Smart names — Hospitalia base CG ≈ Hospitalia Care IPID, and there is no separate "Care"/"Smart" CG on Helan yet. Waarborg zware ziekten = Garantie Maladies Graves (GMG), only 2025 CG, no IPID listed. Original href used &amp; entity; normalized to & in URLs above. A precontractual-info bundle also lives on the page (/nl/dam/…Fiche%20info%20précontractuelles_526_NL_CORR.pdf). All fetched via curl/httpx.
