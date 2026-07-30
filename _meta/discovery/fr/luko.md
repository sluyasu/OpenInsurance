# luko — Luko by Allianz Direct — marque commerciale d'Allianz Direct Versicherungs-AG / Succursale France
website: https://www.fr.luko.eu
library:
  - https://www.fr.luko.eu/conditions-generales/
  - https://www.fr.luko.eu/assurance-voyage/
  - https://www.fr.luko.eu/assurance-habitation/
  - https://www.fr.luko.eu/assurance-habitation/pno/
  - https://www.fr.luko.eu/assurance-voyage/assurance-annuelle/
  - https://www.fr.luko.eu/assurance-voyage/assurance-long-sejour/
fetch: plain
status: enum
lang: fr
enumerated: 2026-07-30

**14 usable documents** (9 conditions_generales, 5 ipid) across 2 branches (habitation 8, voyage 6).
4 further document(s) found but not ingestable, listed at the bottom.

## Carrier

Luko is a trade name, not an insurer, which is why it is absent from the ACPR carrier register — and the entity behind it is not ACPR-authorised either. The four habitation/PNO conditions générales define, under 'Assureur': 'Allianz Direct Versicherungs-AG (succursale France) pour l'assurance multirisque habitation (Titre III du présent contrat). Allianz Direct Versicherungs-AG (succursale France) opère sous la marque Luko.' The habitation IPIDs give the regulatory detail: 'Allianz Direct Versicherungs-AG succursale France (Luko) est une Société de droit étranger au capital de 819 200€ - SIREN : 953 811 338 - Entreprise régie par le Code des assurances et soumise au contrôle de l'autorité fédérale de supervision financière, BaFin, numéro d'enregistrement: 5441. Identifiant Refassu : 11600008.' So the risk carrier is a German insurer (Munich, HRB 95802) operating in France through a branch, supervised by BaFin rather than the ACPR — hence a Refassu identifier instead of an ACPR agrément. THREE other carriers appear across the same library: (1) Opteven Assurances carries the assistance section of all four habitation/PNO contracts — 'Opteven Assurances Société Anonyme au capital social de 5 335 715 € - Entreprise régie par le Code des assurances Immatriculée en France — Numéro d'agrément 4021184'; the HCE body adds 'Luko, marque commerciale opérée par Allianz Direct Versicherungs-AG (Succursale France) distribue le produit d'assurance, et OPTEVEN Assurances est l'Assisteur/Assureur.' (2) Wakam — the pre-acquisition carrier — survives inside Conditions_generales_HCE_2504.pdf only, as the insurer of the annexed Protection juridique convention: the annex's definitions table reads 'Assureur/ Nous — Wakam', and the annex has its own claims and mediation route ('vous pouvez vous adresser à Wakam', 'Le médiateur est une personnalité extérieure à Wakam'). Its reference is CVT_ProtectionJuridique_AVO2021 and EKIE is named alongside Wakam as a data recipient. This is the older/newer split the acquisition produced: the Wakam paperwork was folded into the 2025 Allianz Direct document as an annex rather than replaced. (3) The five travel notices name only 'ALLIANZ DIRECT VERSICHERUNGS- AG […] Königinstraße 28, 80802 Munich, Allemagne. Tribunal d'enregistrement : Munich HRB 95802' as assureur — same carrier, no French entity — although every travel PDF is authored by 'AWP France SAS' (Allianz Partners) in its metadata and every travel IPID is branded 'Allianz Travel'. AWP is never named as a party inside the text.

## What this insurer does not publish

No conditions particulières, no conditions tarifaires, no product sheets, and no older editions — the library is exactly one current edition per formula. Only two branches are covered: habitation (4 CG + 4 IPID, April 2025) and voyage (5 notices d'information + 5 IPID, March/September 2025). Nothing is published for auto or moto even though both are marketed on the site (they run under the Eurofil brand), and nothing for the GLI / assurance loyer impayé that the PNO editorial pages discuss at length. The four PDFs under /dam/documents/ are résiliation and déclaration letter templates, which are not contractual documents and are excluded.

## Traps (do not re-derive)

1. The file stems are formula codes, not products, and they decode from the documents: H = multirisque habitation, L = Landlord / propriétaire non occupant (confirmed by the printed internal references CG_FR_LANDLORD_CE_20230712 and CG_FR_LANDLORD_MINLEG_20230712), CE = 'Police : COUVERTURE ÉTENDUE', MIN = 'Police : COUVERTURE MINIMUM LÉGAL'. HCE/HMIN and LCE/LMIN are parallel formulas of one product each, NOT successive editions — the IPIDs print the same 'Produit :' line and differ only on the 'Police :' line. The trailing 2504 is the edition YYMM (April 2025).
2. The four conditions générales cover pages are images that read only 'Conditions générales de votre contrat d'assurance' plus a badge 'Couverture étendue' or 'Minimum légal'. The cover never names habitation vs PNO — anyone titling these from the cover will merge HCE with LCE. The distinguishing text is the Titre III heading and the 'Références : Conditions_générales_XXX_2504' line on page 5.
3. /conditions-generales/ lists 16 PDFs but the library is 18. /assurance-voyage/ links two more that appear nowhere on the conditions-générales page: CG_Medical-Assistance-Gold-Sport_Long-trip_507657.pdf and IPID_MEDICAL-ASSISTANVE-GOLD-SPORT_LONG-TRIP_507657.pdf. Always crawl the product pages too.
4. IPID_MEDICAL-ASSISTANVE-GOLD-SPORT_LONG-TRIP_507657.pdf contains a publisher typo — ASSISTANVE, not ASSISTANCE. The URL is correct as published; do not 'fix' it.
5. Four of the nine travel PDFs (the four long-trip IPIDs, 507333/507655/507656/507657) have no usable text layer: PyMuPDF returns 110-124 characters because the body is vector outlines rather than glyphs. They are not scans and OCR is not required — rendering the page and reading it recovers everything, including the 'Produit :' line, the 'Compagnie :' line and a printed footer carrying the edition date.
6. One file serves many products. CG_Medical-Assistance-Gold_Long-trip_507656.pdf is linked on /assurance-voyage/ under four different names (Long Séjour, Étudiants, Multirisque, PVT), and its IPID under three. The travel internal naming is the real key: 'Comprehensive' = with cancellation cover, 'Medical & Assistance' = without, 'Sport' = sport option, 'Annual' = annual multi-trip. The site's 'Long Séjour' label is marketing — the document itself excludes trips over 365 consecutive days.
7. /assurance-voyage/ contains one malformed absolute link, 'https://content/dam/onemarketing/direct/luko/documents/travel/CG-ANNUAL-507332.pdf', where the host is literally 'content'. It leaks the Adobe Experience Manager authoring path (/content/dam/onemarketing/direct/luko/documents/...) but that path is NOT served: it 404s on www.fr.luko.eu. It is a broken link, not a second copy — do not record it as a document or a duplicate.
8. The travel PDFs' Word metadata is authored by 'RATTE, AURELIE (AWP France SAS)' and the IPIDs are branded 'Allianz Travel'. Neither AWP France SAS nor Allianz Partners is named as a party anywhere in the text — do not promote the metadata author to carrier.
9. www.luko.eu and luko.eu both 301 to www.fr.luko.eu; there is no surviving legacy library. The Wayback CDX index has only ever captured four PDFs under /dam/documents/ (lettre-resiliation-assurance-habitation-echeance-annuelle-contrat, lettre-resiliation-caution-solidaire, modele-lettre-attestation-proprietaire-bailleur, modele-lettre-declaration-sinistre) — letter templates, not contractual documents.
10. No older editions exist on the live host: probed Conditions_generales_{HCE,HMIN,LCE,LMIN}_{YYMM}.pdf across 2301-2607 under /dam/documents/t-c/ and got 404 on everything except 2504.
11. Auto and moto are sold on fr.luko.eu under the Eurofil brand ('Auto avec Eurofil' in the nav, and /allianz-direct/presse/allianz-direct-finalise-l-acquisition-d-eurofil-aupres-d-abeille/). /assurance-auto/ and /assurance-moto/ carry zero PDFs — those contractual documents are not published under the Luko slug.

## Documents

| product_name | doc_type | branch | edition | carrier | pp | url |
|---|---|---|---|---|---|---|
| Conditions générales de votre contrat d'assurance — Couverture étendue (assurance multirisque habitation) | conditions_generales | habitation | 2025-04 | Allianz Direct Versicherungs-AG (succursale France) | 115 | https://www.fr.luko.eu/dam/documents/t-c/Conditions_generales_HCE_2504.pdf |
| Conditions générales de votre contrat d'assurance — Couverture étendue (assurance propriétaire non occupant) | conditions_generales | habitation | 2025-04 | Allianz Direct Versicherungs-AG (succursale France) | 95 | https://www.fr.luko.eu/dam/documents/t-c/Conditions_generales_LCE_2504.pdf |
| Conditions générales de votre contrat d'assurance — Minimum légal (assurance multirisque habitation) | conditions_generales | habitation | 2025-04 | Allianz Direct Versicherungs-AG (succursale France) | 82 | https://www.fr.luko.eu/dam/documents/t-c/Conditions_generales_HMIN_2504.pdf |
| Conditions générales de votre contrat d'assurance — Minimum légal (assurance propriétaire non occupant) | conditions_generales | habitation | 2025-04 | Allianz Direct Versicherungs-AG (succursale France) | 75 | https://www.fr.luko.eu/dam/documents/t-c/Conditions_generales_LMIN_2504.pdf |
| Multirisques habitation et assistance — Police : COUVERTURE MINIMUM LÉGAL | ipid | habitation | 2025-04 | Allianz Direct Versicherungs-AG succursale France (Luko) | 2 | https://www.fr.luko.eu/dam/documents/legal/IPID_HMIN_2504.pdf |
| Multirisques habitation et assistance — Police : COUVERTURE ÉTENDUE | ipid | habitation | 2025-04 | Allianz Direct Versicherungs-AG succursale France (Luko) | 2 | https://www.fr.luko.eu/dam/documents/legal/IPID_HCE_2504.pdf |
| Propriétaire non-occupant — Police : COUVERTURE MINIMUM LÉGAL | ipid | habitation | 2025-04 | Allianz Direct Versicherungs-AG succursale France (Luko) | 2 | https://www.fr.luko.eu/dam/documents/legal/IPID_LMIN_2504.pdf |
| Propriétaire non-occupant — Police : COUVERTURE ÉTENDUE | ipid | habitation | 2025-04 | Allianz Direct Versicherungs-AG succursale France (Luko) | 2 | https://www.fr.luko.eu/dam/documents/legal/IPID_LCE_2504.pdf |
| Comprehensive Gold Long Trip 507655 | conditions_generales | voyage | 2025-09 | ALLIANZ DIRECT VERSICHERUNGS- AG | 34 | https://www.fr.luko.eu/dam/documents/travel/dftralong202512/CG_Comprehensive-Gold_Long-trip_507655.pdf |
| Comprehensive Gold Sport Annual 507332 | conditions_generales | voyage | 2025-03 | ALLIANZ DIRECT VERSICHERUNGS- AG | 40 | https://www.fr.luko.eu/dam/documents/travel/CG-ANNUAL-507332.pdf |
| Comprehensive Gold Sport Long trip 507333 | conditions_generales | voyage | 2025-09 | ALLIANZ DIRECT VERSICHERUNGS- AG | 37 | https://www.fr.luko.eu/dam/documents/travel/dftralong202512/CG_Comprehensive-Gold-Sport_Long-trip_507333.pdf |
| Medical & Assistance Gold Long trip 507656 | conditions_generales | voyage | 2025-09 | ALLIANZ DIRECT VERSICHERUNGS- AG | 31 | https://www.fr.luko.eu/dam/documents/travel/dftralong202512/CG_Medical-Assistance-Gold_Long-trip_507656.pdf |
| Medical & assistance Gold Sport Long trip 507657 | conditions_generales | voyage | 2025-09 | ALLIANZ DIRECT VERSICHERUNGS- AG | 33 | https://www.fr.luko.eu/dam/documents/travel/dftralong202512/CG_Medical-Assistance-Gold-Sport_Long-trip_507657.pdf |
| ASSURANCE MULTI-VOYAGES A L'ANNEE - 507332 | ipid | voyage |  | ALLIANZ DIRECT VERSICHERUNGS- AG | 2 | https://www.fr.luko.eu/dam/documents/travel/IPID-ANNUAL-507332.pdf |

## Found but not ingestable

| file | why |
|---|---|
| IPID_COMPREHENSIVE-GOLD_Long-Trip_507655.pdf | no text layer (112 chars) - pipeline cannot extract |
| IPID_COMPREHENSIVE-GOLD-SPORT_LONG-TRIP_507333.pdf | no text layer (124 chars) - pipeline cannot extract |
| IPID_MEDICAL-ASSISTANCE-GOLD_LONG-TRIP_507656.pdf | no text layer (116 chars) - pipeline cannot extract |
| IPID_MEDICAL-ASSISTANVE-GOLD-SPORT_LONG-TRIP_507657.pdf | no text layer (110 chars) - pipeline cannot extract |
