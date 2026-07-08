# curalia — Curalia (INS 809)
website: www.curalia.be
library: no single library page; product docs are per-profession pages, e.g. https://www.curalia.be/nl/kinesitherapeut/verzekeringen/gewaarborgd-inkomen , https://www.curalia.be/nl/apotheker/verzekeringen/gewaarborgd-inkomen , https://www.curalia.be/nl/apotheker/pensioenopbouw/pensioensparen
fetch: httpx
status: partial
lang: nl,fr

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Gewaarborgd Inkomen "Free Income" (AXA) | ipid | revenu-garanti | 2022 | nl | https://www.curalia.be/sites/default/files/2022-10/4186463%20IPID%20Free%20Income.pdf |
| Gewaarborgd Inkomen "Free Income" (AXA) | conditions_generales | revenu-garanti | 2022 | nl | https://www.curalia.be/sites/default/files/2022-10/AXA%20Algemene%20Voorwaarden%20Free%20Income.pdf |
| Gewaarborgd Inkomen (AMMA Pharmarisk) | ipid | revenu-garanti | 2020 | nl | https://www.curalia.be/sites/default/files/2020-11/IPID%20GI%20AMMA.pdf |
| Gewaarborgd Inkomen (AMMA Pharmarisk) | conditions_generales | revenu-garanti | 2022 | nl | https://www.curalia.be/sites/default/files/2022-05/algemene-voorwaarden-pharmarisk.pdf |
| Pensioensparen / Langetermijnsparen CuraNova | conditions_generales | pension | 2022 | nl | https://www.curalia.be/sites/default/files/2022-01/Algemene_Voorwaarden_CuraNova_40.pdf |
| Pensioensparen Klassiek Contract | conditions_generales | pension | 2022 | nl | https://www.curalia.be/sites/default/files/2022-02/Algemene_Voorwaarden_KlassiekeContract_0.pdf |
| Langetermijnsparen & Pensioensparen CuraNova | kid | pension | 2026-03 | nl | https://www.curalia.be/sites/default/files/2026-03/Financiele%20Infofiche%20Langetermijnsparen%20%26%20Pensioensparen_2026_CURANOVA.pdf |

notes: NOT a health insurer, and NOT a single risk carrier — Curalia is a pension institution + insurance BROKER (Curalia Brokers b.v.) serving the health/liberal professions. Products are income protection ("gewaarborgd inkomen" = revenu garanti) and pension/long-term savings (VAPZ/POZ, pensioensparen), underwritten by THIRD parties that vary by profession: e.g. AXA "Free Income" for kinesitherapeuten, AMMA "Pharmarisk" for apothekers. So the same product concept resolves to different insurers/CG depending on which profession page you open (/nl/<profession>/verzekeringen/…). The site is Drupal; PDFs live under /sites/default/files/. There is no consolidated catalog page — I sampled the kinesitherapeut and apotheker pages; other professions (arts, tandarts, dierenarts, dentist, etc. — professions listed via /nl/profession/<id>) will expose their own underwriter variants. The public legal page (/nl/juridische-bemerkingen) holds only corporate docs (SFCR, verslag aan leden, duurzaamheidsvoorkeuren), no product CG. "Financiele Infofiche" for the savings product ≈ a KID-type key-info doc (mapped to kid). Editions are mostly 2020-2022 (income) with a 2026 financial info fiche. status=partial: representative products only; the full per-profession matrix is broader and points to external insurers (AXA, AMMA).
