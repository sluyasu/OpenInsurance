# inter-partner-assistance — Inter Partner Assistance SA / AXA Assistance (AXA Partners) (INS 3290)
website: axa-assistance.be (retail client portal) ; axa-schengen.com (travel brand) ; axapartners.be (corporate)
library: no enumerable public doc library — axa-assistance.be is a JS single-page app returning zero links; axa-schengen.com exposes only visa-info/policy-management HTML pages (no GC/IPID PDFs in sitemap)
fetch: firecrawl (axa-assistance.be empty; axa-schengen.com map = HTML pages only; one GC PDF via firecrawl_search)
status: partial
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| AXA Schengen — Multi-Trip (Schengen visa travel) | conditions_generales | voyage | ? | en | https://neo-bo-prod-documents.s3.eu-central-1.amazonaws.com/travel/products/74647f90-a143-4cbd-88c1-db1e6c6b3219/7433b2e3-b71a-48c9-841e-a8d735e13ea3/EN_-_SCHENGEN_Multi-Trip_General_Conditions.pdf |
| AXA Schengen — travel insurance (terms & conditions page) | conditions_generales | voyage | ? | en | https://www.axa-schengen.com/en_GB/infos/terms-and-conditions |

notes: INS 3290 = Inter Partner Assistance SA/NV (Brussels), the AXA Partners assistance carrier that also trades as "AXA Assistance". Its Belgian retail site www.axa-assistance.be is a client-portal SPA — firecrawl_map returned an empty sitemap and firecrawl_scrape (onlyMainContent:false) returned zero links, so no public product library is enumerable there. The public-facing product with retrievable conditions is AXA Schengen (Schengen-visa travel insurance, underwritten by Inter Partner Assistance SA): its sitemap is huge but exposes only visa-requirement info pages and policy-management pages, not the policy PDFs (those are generated in the purchase funnel). One real General Conditions PDF surfaced via search (Schengen Multi-Trip, EN, hosted on the neo-bo-prod S3 bucket). Corporate site: axapartners.be. Also note: www.axa.be (the separate AXA Belgium insurer) references "AXA Assistance" services bundled inside its own policies (e.g. cdn.website.axa.be/.../FullServices_AXA_Assistance.pdf) but that is AXA Belgium's library, not Inter Partner's. status=partial: entity confirmed, but no browsable IPID/CG library — the retail docs live behind the axa-schengen / axa-assistance purchase flows. Suggest retry via httpx on axa-schengen.com localized product pages (fr_BE) to harvest per-country IPID/GC.
