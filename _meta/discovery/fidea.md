# fidea — Fidea (Baloise brand, non-life) (NBB INS ?)
website: https://www.fidea.be
library: https://www.fidea.be/fr/conditions-generales (exists per brief, but could not be retrieved)
fetch: blocked
status: none
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| (none retrieved) | | | | | |

notes:
- Fidea is fully unreachable via Firecrawl in this session. Attempts (5, all failed):
  1. firecrawl_scrape https://www.fidea.be/fr/conditions-generales (basic proxy, waitFor 4000) → ERR_TUNNEL_CONNECTION_FAILED (Firecrawl internal proxy error).
  2. firecrawl_scrape same URL (proxy=stealth, waitFor 8000) → ERR_TUNNEL_CONNECTION_FAILED.
  3. firecrawl_map https://www.fidea.be (search="conditions générales IPID PDF") → empty.
  4. firecrawl_map https://www.fidea.be (sitemap=only) → empty.
  5. firecrawl_search includeDomains=fidea.be → empty (0 results).
- Errors 1-2 are Firecrawl-side proxy/tunnel failures (not a confirmed WAF block); map/search/sitemap all returned empty, so the site is either JS/Cloudflare-gated or not exposed to Firecrawl's crawler.
- Fidea is a non-life brand of Baloise (Baloise Belgium). A public CG/IPID library is expected at /fr/conditions-generales (and NL /nl/algemene-voorwaarden).
- Broad firecrawl_search (2026-07-08, not domain-restricted) surfaced no fidea.be document URLs but confirmed context: assurances.be/fidea lists Fidea's range as assurance auto, habitation, santé; a Baloise comparison PDF (baloise.be/.../Fiche-de-comparaison-HabitationSelect-AssuranceHabitationFidea) confirms Fidea Habitation policies were migrated into Baloise's Habitation Select — so some/all Fidea CG may now be superseded by Baloise editions.
- RECOMMEND: retry later, or fetch directly with httpx (the tunnel errors were infra-side), or route through the Baloise/Fidea broker portal.
