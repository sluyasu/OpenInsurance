# europ-assistance — Europ Assistance (Belgium) (INS 888)
website: europ-assistance.be
library: per-product pages under europ-assistance.be (each shows "Fiche IPID" + "Conditions Générales"); docs served via tokenized endpoints /fr/commands/download-ipid/<CODE>/<ts>/<hash> and /fr/commands/download-cgs/<CODE>/<ts>/<hash>
fetch: firecrawl
status: partial
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| Assurance voyage annuelle Light | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-light |
| Assurance voyage annuelle Light | conditions_generales | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-light |
| Assurance voyage annuelle Smart | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-smart |
| Assurance voyage annuelle Smart | conditions_generales | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-smart |
| Assurance voyage annuelle Sport | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-sport |
| Assurance voyage annuelle Sport | conditions_generales | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-sport |
| Assurance voyage annuelle VIP | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-vip |
| Assurance voyage annuelle VIP | conditions_generales | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage/annuel-vip |
| Assurance voyage temporaire | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage-temporaire/temporaire |
| Assurance voyage temporaire | conditions_generales | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage-temporaire/temporaire |
| Assurance voyage temporaire Digital | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage-temporaire/temporaire-digital |
| Assurance voyage temporaire Snow | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage-temporaire/snow |
| Assurance voyage temporaire Longtrip | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-voyage-temporaire/temporaire-longtrip |
| NoGo annulation (annuel) | ipid | voyage | ? | fr | https://www.europ-assistance.be/assurance-annulation-voyage/nogo-annuel |
| NoGo annulation (temporaire) | ipid | voyage | ? | fr | https://www.europ-assistance.be/fr/product/nogo-tempo |
| Drive — assistance voiture | ipid | auto | ? | fr | https://www.europ-assistance.be/assistance-voiture/drive |
| Drive — assistance voiture | conditions_generales | auto | ? | fr | https://www.europ-assistance.be/assistance-voiture/drive |
| Motorbike — assistance moto | ipid | auto | ? | fr | https://www.europ-assistance.be/assistance-moto/motorbike |
| Bike — assistance vélo | ipid | velo | ? | fr | https://www.europ-assistance.be/assistance-velo/bike |
| House Assist — assistance habitation | ipid | habitation | ? | fr | https://www.europ-assistance.be/assistance-habitation/house-assist |
| Medicall — téléconseil médical | ipid | sante | ? | fr | https://www.europ-assistance.be/teleconseil-medical/medicall |
| Safe Connected — support informatique | ipid | autres | ? | fr | https://www.europ-assistance.be/support-informatique/safe-connected |
| Easy Rent — protection caution location | ipid | auto | ? | fr | https://www.europ-assistance.be/protection-caution/easy-rent |
| Business Essential | ipid | voyage | ? | fr | https://www.europ-assistance.be/assistance-entreprise/business-essential |
| Business Smart | ipid | voyage | ? | fr | https://www.europ-assistance.be/assistance-entreprise/business-smart |
| Business VIP | ipid | voyage | ? | fr | https://www.europ-assistance.be/assistance-entreprise/business-vip |

notes: Europ Assistance does NOT expose a flat document library; every product page carries "Fiche IPID · Conditions Générales · Informations précontractuelles" links that resolve to tokenized download endpoints — pattern confirmed on annuel-smart (code YA02): /fr/commands/download-ipid/YA02/<timestamp>/<hash> and /fr/commands/download-cgs/YA02/<timestamp>/<hash>. Those URLs are session-bound (timestamp + hash), so they expire and are NOT stable — the durable entry point is the product page (used as url above). Each product has both an IPID and CG; I marked conditions_generales only where the page nav confirmed both, and ipid for the rest (all products expose an IPID; most also a CG). Static precontractual info sheet: https://www.europ-assistance.be/upload/documents/info-pre-contractuelle.pdf. NL/EN mirrors exist (/nl/product/..., /en/product/...). status=partial because actual PDF URLs are ephemeral and per-product codes were not harvested for every product (would need one page fetch each). Legal entity: Europ Assistance Belgium SA/NV, INS 888.
