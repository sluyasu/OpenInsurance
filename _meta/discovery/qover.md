# qover — Qover (INS ?)
website: qover.com
library: https://www.qover.com/terms-and-policies (corporate/legal PDFs only) ; product policy wordings + IPID are embedded per partner brand (e.g. https://assets.qover.com/documents/<brand>/ and brand microsites bike.qover.com, revolut.qover.com, insuremynio.qover.com)
fetch: firecrawl
status: partial
lang: fr,nl

| product_name | doc_type | branch | edition | lang | url |
|---|---|---|---|---|---|
| bunq Elite – travel & purchase package | conditions_generales | voyage | ? | fr | https://assets.qover.com/documents/bunq/bunq_T%26Cs_FR.pdf |

notes: Qover is an embedded/white-label insurance orchestrator (MGA / Lloyd's of London coverholder; risk carried by partners such as Lloyd's syndicates, Munich Re, Helvetia, Everest depending on programme). There is NO consumer-facing document library on qover.com: the /be path 404s and /terms-and-policies exposes only corporate legal PDFs (privacy policy EN/FR/NL, complaints procedure, legal notice EN/FR/NL, conflict-of-interest, cookie policy), not product CG/IPID. Product policy wordings & IPID are served per partner brand — visible brands with BE relevance in the sitemap include Belfius, Immoweb (homeowner), Revolut, bunq, bike insurance (bike.qover.com), NIO/Helvetia motor. Only one concrete product doc was directly enumerable (bunq Elite T&C, FR; NL/EN variants exist by swapping the locale suffix). Full enumeration would require crawling each brand microsite (out of ~3-call budget). Mobilité/vélo docs live on bike.qover.com per-country locales rather than a central BE page.
