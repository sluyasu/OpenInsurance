# euromex — EUROMEX (INS 463)
website: www.euromex.be
library: https://www.euromex.be/fr/courtier/documents (F5/BIG-IP WAF — HTTP 403, not scrapeable) ; document PDFs via https://www.euromex.be/documents/download?id=<id>
fetch: blocked
status: partial
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| PJ Vie privée | conditions_generales | vie-privee | ? | fr | https://www.euromex.be/documents/download?id=2420 |
| PJ Vie privée — Conditions particulières | conditions_speciales | vie-privee | ? | fr | https://www.euromex.be/documents/download/file?id=1635 |
| PJ All-risk Auto | conditions_generales | auto | ? | fr | https://www.euromex.be/documents/download?id=2462 |
| PJ All-risk Circulation | conditions_generales | auto | ? | fr | https://www.euromex.be/documents/download?id=2442 |
| PJ All-risk Mobilité | conditions_generales | auto | ? | fr | https://www.euromex.be/documents/download?id=2468 |
| PJ Medicus / Medicus Forte | conditions_generales | rc-professionnelle | ? | fr | https://www.euromex.be/documents/download/file?id=1419 |
| PJ Entrepreneur | conditions_generales | rc-professionnelle | ? | fr | https://euromex.be/documents/download/file?id=1733 |
| PJ Bien immobilier | conditions_generales | habitation | ? | fr | https://www.euromex.be/documents/download/file?id=1645 |
| PJ Association des Copropriétaires | conditions_generales | habitation | ? | fr | https://www.euromex.be/documents/download/file?id=25242 |
| IPID Assurance Protection Juridique (générique) | ipid | protection-juridique | 2024-10 | fr | https://www.euromex.be/documents/download/file?id=25678 |
| IPID Assurance Protection Juridique | ipid | protection-juridique | ? | fr | https://www.euromex.be/documents/download?id=2581 |
| IPID Assurance Protection Juridique | ipid | protection-juridique | ? | fr | https://www.euromex.be/documents/download?id=2673 |
| IPID PJ Navigation de plaisance | ipid | autres | 2024-10 | fr | https://www.euromex.be/documents/download?id=2664 |
| IPID PJ Pilote/élève/instructeur | ipid | autres | 2024-10 | fr | https://www.euromex.be/documents/download?id=2637 |
| IPID PJ Garagiste All-risk | ipid | rc-professionnelle | 2024-09 | fr | https://www.euromex.be/documents/download?id=21951 |

notes: PARTIAL / library WAF-blocked. Every HTML page (homepage and /fr/courtier/documents) returns HTTP 403 from an F5 BIG-IP WAF, on all 3 attempts (proxy basic AND proxy stealth) — the document library cannot be scraped. The rows above were recovered from the Google index via firecrawl_search and point at real euromex.be PDF endpoints (/documents/download?id= and /documents/download/file?id=). Because the library itself is unreachable, this is a PARTIAL sample and the product-name / doc_type / branch / edition mapping is best-effort from PDF titles+snippets (verify once the WAF is bypassed, e.g. from a Belgian residential IP or via the broker portal). Editions 2024-09 / 2024-10 appear in several IPID internal doc codes (e.g. FGARARAF092024). Euromex also acts as PJ product manager / white-label underwriter for other carriers (Baloise IPIDs are literally stamped "© Product management Euromex"), so some Euromex PJ CG/IPID are additionally discoverable on partner-insurer domains. NL versions exist. No KID.
