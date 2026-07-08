# Belgium — product inventory (discovery results, 2026-07-08)

_Output of the parallel discovery pass (9 agents + inline). Per-carrier detail in `_meta/discovery/<slug>.md`.
Counts = documents enumerated with real public URLs. This is the "everything present in Belgium" map before ingestion._

## Totals
- **Carriers probed:** 60 (55 discovery files + hiscox, allianz, belfius-direct, cardif, nn-non-life enumerated inline).
- **Products enumerated:** ~500 · **document rows (CG/IPID/CondSpéc/KID):** ~630.
- **Status:** ~33 with usable public libraries (`enum`), ~11 `partial` (docs behind funnels/WAF/tokens), ~16 `none` (no first-party public docs).

## NEW branches confirmed by real products → extend `_country.yml` (data, GATE)
| slug | label | doc rows | seen at |
|---|---|---|---|
| animaux | Animaux | 16 | figo/agila, santevet, petexpert, belfius-direct |
| revenu-garanti | Revenu garanti | 8 | xerius, curalia, precura, securex |
| obseques | Obsèques | 6 | dela, belfius-direct, ergo |
| cyber | Cyber | 4 | hiscox, allianz |
Note: Athora rows tagged `vie` (2) should map to `epargne`/`pension` (not a new branch).

## Ingestable — first-party public libraries (the real target set)

### Generalists / bancassurance / life
| slug | docs | branch focus | note |
|---|---|---|---|
| allianz | ~40-60* | full-line + cyber, AT, hospi, transport | ⚠️ Cloudflare → Firecrawl fetch; full enum still to do |
| athora | 26 | epargne/pension (br.21/23) | LIFE-ONLY (no auto/incendie — brief was off); +~470 per-fund DIS/KID |
| patronale-life | 43 | epargne/pension/obseques | KID+FIF+CG; 1 Tak-26 on partner Korfine |
| credimo | 25 | epargne (br.21/26) | 25 CG, full history |
| belfius-direct | ~20* | auto-km, habitation, familiale, funérailles, animaux, voyage, vélo | ex-Corona; deep edition history |
| acm | 17 | auto, habitation, vie-privee | Beobank/Crédit Mutuel; Euro-Information CDN |
| actel | 9 | auto | P&V direct brand |
| ergo | 8 | epargne, obseques | Munich Re; life/funeral |
| securex | 8 | pension/epargne | Securex Vie (own); Caisse AT (519) not yet enum |
| cph-life | 8 | pension/epargne | CG+FIF |
| nn-non-life | ~8* | auto (NN Car/Mobility) | distinct entity from nn(life) |
| cardif | ~5* | solde restant dû, vie | Hypo Protect |
| xerius | 3 | revenu-garanti, pension | Xerius AAM (own) |

### Protection juridique
| slug | docs | note |
|---|---|---|
| lar | 24 | = "Legal Village" (AXA's PJ brand); lar.be dead; genuine LAR only in superseded archive |
| arag | 21 | own PJ specialist, clean |
| euromex | 15 | ⚠️ F5 WAF (403) → PDFs via Google index only |
| arces | 14 | own docs, carrier P&V |
| providis | 5 | own CG, underwritten by AG; IPID via intermediary only |

### Assistance & travel
| slug | docs | note |
|---|---|---|
| europ-assistance | 26 | ⚠️ IPID/CG behind session-tokenized URLs → use product-page URLs |
| allianz-assistance | 11 | clean (AWP P&C); voyage/vélo |
| vab | 16 | NL only; underwritten by KBC |
| inter-partner-assistance | 2 | SPA, docs behind purchase funnel — partial |

### Health / hospitalisation
| slug | docs | note |
|---|---|---|
| mloz | 19 | **the VMOB carrier behind Hospitalia** — model once |
| partenamut | (19) | = MLOZ products republished → **alias, don't re-ingest** |
| helan | (19) | = MLOZ products (NL) → **alias** |
| solidaris | 3 | "Hospimut" — SEPARATE carrier, keep |
| cigna | 4 | broker/quote-only IPIDs — partial |

### RC pro / niche
| slug | docs | note |
|---|---|---|
| aig | 32 | only foreign specialist with a public IPID library; commercial/specialty |
| hiscox | ~16* | rc-pro, cyber, D&O, PJ pro |
| protect | 9 | IPID-only (architects/engineers); no public CG |
| curalia | 7 | revenu-garanti + pension (fronts AXA/AMMA) |
| euromaf | 6 | RC architecte/ingénieur + PJ + chantier |
| precura | 6 | revenu-garanti/pension, CG-only (stale) |

### Obsèques / animaux / vélo-niche
| slug | docs | note |
|---|---|---|
| aedes | 28 | MGA (risk Monceau/AXA); auto/home/vélo/PJ |
| petexpert | 6 | animaux; carrier unconfirmed (Czech MGA) |
| dela | 4 | obsèques (own carrier, br.21) |
| figo | 4 | animaux; carrier = AGILA AG |
| agila | (4) | = figo (same carrier + product line) → **merge into figo** |
| bikmo | 4 | vélo; carrier = UNIQA (Liechtenstein) |
| santevet | 2 | animaux; carrier = AXA |
| qover | 1 | embedded per-partner; no own library — partial |

## EXCLUDE — no first-party public docs (labeled, not hidden)
- **No public library / broker-only:** justitia (Vanbreda health, not PJ), cfdp (new site, no docs), juridica (KBC "Defendo" docs live under kbc.be), notariat (closed scheme), chubb (affinity scraps only), zurich, hdi, qbe (broker-only B2B), mensura, b2bike, ucm, group-s.
- **Third-party underwritten → would duplicate parent:** liantis (KBC), acerta (KBC), partena (P&V), crelan non-life (AXA), ardenne-prevoyante (AXA-rebranded — dup of AXA "Confort" catalogue).
- **Run-off / blocked:** monument (products no longer marketed), fidea (Baloise-absorbed 2020; site blocks datacenter IPs → fetch from BE IP at ingestion).

## Dedup / brand→carrier map (to model cleanly, avoid duplicate PDFs)
- agila = figo (AGILA AG) · partenamut = helan = mloz (Hospitalia range) · lar = Legal Village (AXA) ·
  ardenne-prevoyante = AXA · crelan non-life = AXA · santevet → AXA · aedes → Monceau/AXA · bikmo → UNIQA ·
  vab → KBC · providis → AG · arces → P&V · curalia → AXA/AMMA · petexpert → ? (open).

## Remaining follow-ups (cheap, optional)
- allianz full enumeration (Firecrawl, ~40-60 PDFs) · securex Caisse AT (519) + Risques Divers (805) libraries ·
  fidea from a BE IP · IPA / europ-assistance stable URLs at download time · write discovery files for the 5 inline carriers.

\* enumerated inline earlier; counts approximate, to finalize at ingestion.
