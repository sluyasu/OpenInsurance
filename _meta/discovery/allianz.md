# allianz — Allianz Benelux SA (Belgium) (generalist)
website: https://www.allianz.be
library: PDFs on the CDN tree /content/dam/onemarketing/benelu/allianz-be/downloads/fr/ (per branch)
fetch: BLOCKED (see note) — URLs enumerated via Google/Firecrawl index
status: enum-partial (not ingested)

⚠️ FETCH BLOCKER (2026-07-08): the /content/dam/ PDFs sit behind Cloudflare. Confirmed 403 on:
plain httpx (bot UA), httpx with a desktop Chrome user-agent, and headless Playwright/Chromium
(warm-up visit + browser request context). Firecrawl can return the parsed TEXT of each PDF, but
NOT the raw bytes, so there is no local PDF for verify_grounding.py to check quotes against. A
text-only extraction would not pass the grounding gate. Groundable ingestion therefore needs one
of: a manual browser download of the PDFs into data/be/pdfs/allianz/<branch>/ (+ manifest rows),
a residential-IP fetch, or a Cloudflare-clearing headful browser. Recorded as a labeled gap.

Enumerated CG / IPID / KID (real URLs, current unless noted):

| product_name | doc_type | branch | edition | url |
|---|---|---|---|---|
| Car Plan | conditions_generales | auto | 2023-02 | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/vehicules/conditions-generales/carplan-ad1129fr-022023.pdf |
| Car Plan | ipid | auto | 2022 | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/vehicules/fiche-ipid/ipid-fiche-car-plan-2022.pdf |
| Car Plan Assistance Plus | conditions_generales | auto | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/vehicules/conditions-generales/car-plan-assistance-plus-conditions-generales-ad1123.pdf |
| Assurance Conducteur | conditions_generales | auto | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/vehicules/conditions-generales/assurance-conducteur-conditions-generales.pdf |
| Protection Juridique Auto | conditions_generales | protection-juridique | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/vehicules/conditions-generales/protection-juridique-auto-conditions-generales.pdf |
| Traffic Plan | conditions_generales | accidents | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/accident-corporel/conditions-generales/traffic-plan-conditions-generales.pdf |
| Accidents corporels vie privée | conditions_generales | accidents | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/accident-corporel/conditions-generales/accidents-corporels-vie-privee-conditions-generales.pdf |
| Assistance 24h/24 accident indépendant | conditions_generales | accidents | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/accident-corporel/conditions-generales/conditions-generales-assistance-24h-24-assurance-accident-independant.pdf |
| Accidents collectives indépendants 24h/24 | ipid | accidents-travail | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/accidents-du-travail/fiche-ipid/ipid-assurance-accidents-collectives-independants-24.pdf |
| New Home Plan | conditions_generales | habitation | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/incendie/conditions-generales/newhomeplanconditionsgeneralesfr.pdf |
| BIZ Plan / BIZ Solution | conditions_generales | habitation | 2007-10 | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/incendie/conditions-generales/biz-plan-solutions-ad1039fr-1007.pdf |
| Dégâts matériels et pertes d'exploitation | conditions_generales | autres | 2012-09 | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/incendie/conditions-generales/degats-materiels-et-pertes-exploitation-ad1056fr-092012-conditions-generales.pdf |
| Family Plan (RC familiale) | conditions_generales | vie-privee | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/responsabilite/conditions-generales/family-plan-ad1085-fr.pdf |
| Family Plan (RC familiale) | ipid | vie-privee | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/responsabilite/fiche-ipid/ipid-family-plan-fiche-client.pdf |
| Liability Plan (RC entreprise) | conditions_generales | rc-professionnelle | 2011-01 | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/responsabilite/conditions-generales/liability-plan-rc-entreprise-ad-1005-01-2011.pdf |
| RC professionnelle | ipid | rc-professionnelle | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/responsabilite/fiche-ipid/ipid-rc-professionnel.pdf |
| Restart (tous risques chantier) | conditions_generales | autres | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/tous-risques-chantier-risques-techniques/conditions-generales/conditions-generales-restart.pdf |
| Tous Risques Chantier | conditions_generales | autres | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/tous-risques-chantier-risques-techniques/conditions-generales/conditions-generales-tous-risques-chantier.pdf |
| Bris de machine | conditions_generales | autres | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/tous-risques-chantier-risques-techniques/conditions-generales/conditions-generales-bris-de-machine-fixe.pdf |
| Transport (TCP) | ipid | autres | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/non-vie/transport-marine/fiche-ipid/ipid-transport-tcp.pdf |
| Hospit-All | conditions_generales | sante | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/employee-benefits/hospit-all/conditions-generales/conditions-generales-hospit-all.pdf |
| Comfort@hospital | ipid | sante | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/employee-benefits/allianz-medical-plan/fiche/ipid-comfort-at-hospital.pdf |
| Plan for Life | conditions_generales | pension | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/pension/autre/conditions-generales/plan-for-life-conditions-generales.pdf |
| Plan for Life + | conditions_generales | pension | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/pension/plan-for-life-plus/conditions-generales/plan-for-life-plus-conditions-generales-fr.pdf |
| Assurance chiffre d'affaires avec décès (V972) | conditions_generales | pension | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/pension/assurance-chiffre-daffaires-avec-deces/conditions-generales/conditions-generales-assurance-chiffre-dafaires-avec-deces-v-972.pdf |
| Allianz ActiveInvest | conditions_generales | epargne | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/investissement/allianz-activeinvest/conditions-generales/conditions-generales-allianz-active-invest.pdf |
| Allianz ActiveInvest | product_sheet | epargne | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/investissement/allianz-activeinvest/document-dinformations-cles/allianz-activeinvest-kid-fr.pdf |
| Allianz Opportunity3A New Generation | product_sheet | epargne | ? | https://www.allianz.be/content/dam/onemarketing/benelu/allianz-be/downloads/fr/investissement/allianz-opportunity3a-new-generation/document-dinformations-cles/allianz-opportunity3a-new-generation-kid-fr.pdf |

notes:
- Allianz Benelux SA (BE 0403.258.197). Large generalist; the tree above is a representative
  enumeration (~27 docs) from the public index, not necessarily exhaustive.
- Once a groundable fetch is available, this file is ready to become sources/be/allianz.yml.
