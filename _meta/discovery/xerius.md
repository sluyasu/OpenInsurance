# xerius — Xerius AAM (INS 1052)
website: www.xerius.be
library: https://www.xerius.be/fr-be/assurances-pension (product pages) ; PDFs on https://media.xerius.be/-/media/project/xerius/sites/public/boekhouders/formulieren-en-publicaties/ovv/fr/
fetch: firecrawl
status: enum
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Revenu garanti (Xerius AAM) | ipid | revenu-garanti | 2024-08 | fr | https://media.xerius.be/-/media/project/xerius/sites/public/boekhouders/formulieren-en-publicaties/ovv/fr/ipid_gi_fr_28082024.pdf?rev=-1&hash=3D08EC701DFDFC32E548B61A04AEDDC4 |
| VAPZ / PLCI sociale (Xerius AAM) | conditions_generales | pension | 2023-07 | fr | https://media.xerius.be/-/media/project/xerius/sites/public/boekhouders/formulieren-en-publicaties/ovv/fr/conditions-generales.pdf?rev=5a96a605a79544cbb8c2635bf6e603c9&modified=20230703142307&hash=9A61ECA0EE794656F0E66203F3D43ABA |
| VAPZ / PLCI sociale (Xerius AAM) — Fiche Info Financière | kid | pension | 2023-03 | fr | https://media.xerius.be/-/media/project/xerius/sites/public/boekhouders/formulieren-en-publicaties/ovv/fr/fif-vapz-fr_versie-017_01032023.pdf?rev=d656f965e4c8495caec8c68604b7742f&modified=20240906084226&hash=758CA16E46A3B39CBE26D4A576226BFE |

notes:
- Xerius AAM = Association d'Assurances Mutuelles (OVV) = the fund's OWN mutual insurer, so revenu garanti + VAPZ/PLCI sociale docs are genuine own conditions générales / IPID / fiche info. Docs live in the media.xerius.be OVV folder (nl equivalents exist at the same path with nl filenames).
- "Fiche Info Financière VAPZ" bucketed under kid (nearest enum) — it is the regulated pre-contractual financial info sheet for the life product, not strictly a PRIIPs KID.
- conditions-generales.pdf was linked from the PLCI/VAPZ page, so it is labelled to VAPZ/PLCI sociale; not opened, so it may also cover the mutual's revenu garanti/solidarity. Revenu garanti's own CG was not found separately (only its IPID is public).
- Two more public docs in the same OVV folder, not listed as rows (not CG/IPID/CS/KID): reglement-de-solidarite.pdf (solidarity regulation of PLCI sociale, 2023-07) and avance-fiche-technique.pdf (technical sheet on advances, 2024-09).
- Other Xerius pension products advertised (EIP, CPTI, épargne-pension individuelle, épargne long terme, assurance complémentaire décès) are life products likely via a partner insurer; no own Xerius IPID/CG found for them this pass.
