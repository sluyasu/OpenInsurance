# acm — ACM Belgium (Assurances du Crédit Mutuel Belgium / Beobank bancassurance) (NBB INS ?)
website: https://www.acm.be
library: per-product pages under https://www.acm.be/fr/particulier/ and /fr/professionnel/ (no single document index; each product page links its CG + IPID PDFs, hosted on the Euro-Information CDN cdnwmii.e-i.com under /assets/articles/<category>/1.0/)
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Assurance Auto | conditions_generales | auto | 2025-09 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/auto/1.0/20250925_FR_CG_AUTO_ACM_INSURANCE.pdf |
| Assurance Auto | ipid | auto | 2025-09 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/auto/1.0/20250916_IPID_Auto_FR.pdf |
| Assurance Habitation (Home Serenity) | conditions_generales | habitation | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/logement/1.0/20241001_FR_CG_HABITATION_ACM_INSURANCE.pdf |
| Assurance Habitation (Home Serenity) — CG partie 2 | conditions_generales | habitation | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/logement/1.0/20241001_FR_CG_HABITATION_ACM_INSURANCE_2.pdf |
| Assurance Habitation (Home Serenity) | ipid | habitation | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/logement/1.0/20241001_IPID_Home_Serenity_FR.pdf |
| Assurance familiale (RC familiale) | conditions_generales | vie-privee | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/famille/1.0/20241001_FR_CG_RC_Familiale_ACM_INSURANCE.pdf |
| Assurance familiale (Family Serenity) | ipid | vie-privee | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/famille/1.0/20241001_IPID_Family_Serenity_FR.pdf |
| Assurance Scoot & Bike (cyclomoteur) | conditions_generales | auto | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/scoot-bike/1.0/20241001_FR_CG_CYCLOMOTEUR_ACM_INSURANCE.pdf |
| Assurance Scoot & Bike (Scoot Bike Serenity) | ipid | auto | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/scoot-bike/1.0/20241001_IPID_Scoot_Bike_Serenity_FR.pdf |
| Assurance vélo | conditions_generales | velo | 2025-03 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/velo/1.0/20250322_FR_CG_VELO_ACM_INSURANCE.pdf |
| Assurance vélo | ipid | velo | 2025-08 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/velo/1.0/20250820_IPID_Velo_FR.pdf |
| Assurance Moto | conditions_generales | auto | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/moto/1.0/20241001_FR_CG_MOTO_ACM_INSURANCE.pdf |
| Assurance Moto (Moto Serenity) | ipid | auto | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/moto/1.0/20241001_IPID_Moto_Serenity_FR.pdf |
| Accidents vie privée (AVP) | conditions_generales | accidents | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/vie-prive/1.0/20241001_FR_CG_AVP_ACM_INSURANCE.pdf |
| Accidents vie privée (AVP) | ipid | accidents | 2024-10 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/vie-prive/1.0/20241001_IPID_AVP_FR.pdf |
| Assurance Auto Professionnels | conditions_generales | auto | 2025-09 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/auto-pros/1.0/20250925_FR_CG_AUTO_ACM_INSURANCE.pdf |
| Assurance Auto Professionnels | ipid | auto | 2025-09 | fr | https://cdnwmii.e-i.com/SITW/wm/global/1.0.0/WEBA/ACM/BE/assets/articles/auto-pros/1.0/20250916_IPID_Auto_FR.pdf |

notes:
- ACM Insurance is the Assurances du Crédit Mutuel bancassurance carrier in Belgium (distributed via Beobank / Crédit Mutuel channel). PDFs hosted on Euro-Information CDN (cdnwmii.e-i.com), pattern: .../assets/articles/<category>/1.0/<YYYYMMDD>_<TYPE>_<product>_<lang>.pdf. Edition dates read directly from the YYYYMMDD filename prefix.
- 8 products, all with real CG + IPID URLs (17 rows incl. a second CG part for Habitation). Category slugs: auto, logement, famille, scoot-bike, velo, moto, vie-prive, auto-pros.
- Scoot & Bike CG is titled CYCLOMOTEUR (moped/scooter) → tagged auto; the vélo product is separate → velo.
- Assurance Auto Professionnels: its own CG/IPID live under the auto-pros/ category (2025-09); its page also cross-links the particulier auto/ CG (same file as the personal Auto row).
- NL equivalents exist at https://www.acm.be/nl/... (captured FR).
- Assistance cover co-branded with Allianz Assistance (each page links an allianz-assistance.be privacy PDF, not listed — not an ACM product doc).
- status = enum: full product line + all current CG/IPID document URLs resolved.
