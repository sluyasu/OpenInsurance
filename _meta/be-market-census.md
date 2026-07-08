# Belgium insurance market — full census (working tracker)

_Source of truth for "who is present in Belgium". Built 2026-07-08 from the two NBB registers
(authorized Belgian undertakings + EEA branches operating in Belgium) cross-checked with Assuralia
and per-insurer sites via Firecrawl. INS = NBB institution number. Not committed until the plan is locked._

Legal universe (NBB): **52 authorized Belgian undertakings + 43 EEA branches = ~95 legal entities.**
Consumer brands map many-to-one onto these entities (e.g. DVV→Belfius Assurances, Vivium→P&V).

Legend — doc status: `enum` = product PDFs already enumerated · `lib+` = public library confirmed rich ·
`lib?` = library to confirm · `verify` = existence of public IPID/CG to check · `none` = no public consumer docs.

---

## A. Already in the wiki (17 brands → ~13 legal entities)

| Brand (slug) | Legal entity (INS) |
|---|---|
| ag | AG Insurance (79) |
| axa | AXA Belgium (39) |
| baloise | Baloise Belgium (96) |
| kbc | KBC Assurances (14) |
| belfius | Belfius Assurances (37) |
| dvv | Belfius Assurances (37) — brand |
| pv | P&V Assurances (58) |
| vivium | P&V Assurances (58) — brand |
| ethias | Ethias (196) |
| federale | Fédérale Assurance (124) |
| nn | NN Insurance Belgium (2550) — life/pension |
| argenta | Argenta Assurances (858) |
| dkv | DKV Belgium (739) |
| amma | Amma Assurances (126) |
| das | DAS Protection juridique (687) |
| touring | Touring Assurances — brand (Baloise-linked) |
| yuzzu | ex-Touring Assurances, now Baloise (96) |

---

## B. INGEST TARGETS — consumer-facing, public docs likely (the expansion set)

### B1. Generalists / bancassurance
| Slug | Entity (INS) | Lines | Doc status | Note |
|---|---|---|---|---|
| allianz | Allianz Benelux (97) | full-line + cyber, AT, hospi, transport | **lib+** (enum via map) | ⚠️ Cloudflare → Firecrawl fetch |
| athora | Athora Belgium (145) | vie/pension br.21/23 + legacy non-vie | **lib+** | ex-Generali; mark legacy superseded |
| acm | ACM Belgium + Life (964/956) | bancassurance Beobank (auto, habitation, vie) | verify | **NEW vs brief** |
| ergo | ERGO Insurance (735) | vie, obsèques (Munich Re) | verify | **NEW vs brief** |
| cardif | Cardif Vie + Risques Divers (979/978) | solde restant dû, protection crédit, vie | **enum** (Hypo Protect) | |
| belfius-direct | Belfius Assurances (37) — direct arm | auto-km, habitation, familiale, funérailles, animaux, voyage, vélo, assistance | **enum** | ex-Corona; coronadirect.be→belfiusdirect.be |
| fidea | Baloise Belgium (96) — brand | auto, incendie, RC fam, accidents | lib? (proxy err) | own CG on fidea.be |
| actel | P&V Assurances (58) — direct brand | auto direct | verify | **NEW vs brief** |
| nn-non-life | NN Schadeverzekering (2925) | auto (NN Car), mobilité, home | **enum** (NN Mobility) | distinct entity from nn (2550) |
| monument | Monument Assurance Belgium (1644) | vie/pension run-off | verify | ex-Integrale/Contassur |
| patronale-life | Patronale Life (9081) | vie br.21/23/26, crédit hypo | verify | docs = FIF/KID |

### B2. Legal protection (protection juridique) — carriers + brands
| Slug | Entity (INS) | Doc status | Note |
|---|---|---|---|
| euromex | EUROMEX (463) | verify | own carrier |
| justitia | Justitia (878) | verify | own carrier (Antwerpen) |
| arag | ARAG SE (2812) | verify | EEA branch |
| cfdp | CFDP Assurances (2673) | verify | **NEW vs brief** (Liège) |
| lar | AXA group brand | verify | check own vs AXA CG |
| providis | AG/BNPPF brand | verify | |
| arces | P&V brand | verify | |
| juridica | KBC brand ("Defendo") | verify | |

### B3. Assistance & travel
| Slug | Entity (INS) | Doc status |
|---|---|---|
| europ-assistance | Europ Assistance (888) | verify |
| allianz-assistance | AWP P&C / Allianz Partners (2769) | verify |
| inter-partner-assistance | Inter Partners Assistance (3290) — AXA Assist | verify |
| vab | VAB (mobility club) | verify entity |

### B4. Health / hospitalisation / mutualités
| Slug | Entity (INS) | Doc status | Note |
|---|---|---|---|
| mloz | MLOZ Insurance (VMOB) | lib? (Hospitalia) | grosse biblio CG/IPID |
| partenamut | Partenamut (VMOB) | verify | Hospitalia shared |
| helan | Helan (VMOB) | verify | |
| solidaris | Solidaris (VMOB) | verify | |
| cigna | Cigna Europe + Life (2176/938) | verify | expat/individual health |
| curalia | Curalia (809) | verify | health professions pension — niche |
| precura | Precura (2790) | verify | health mutuelle — niche |

### B5. Obsèques & animaux
| Slug | Entity (INS) | Line | Doc status |
|---|---|---|---|
| dela | Dela Natura- en Levensverz. (2864) | obsèques | verify |
| agila | AGILA Haustierversicherung (3262) | animaux | verify — **NEW vs brief** (pet carrier) |
| santevet | brand (porté AXA) | animaux | verify |
| figo | brand | animaux | verify |
| petexpert | brand (porté KBC) | animaux | verify |

### B6. Independents / PME (social funds + mutuals)
| Slug | Entity (INS) | Doc status | Note |
|---|---|---|---|
| xerius | Xerius AAM (1052) | verify | own carrier |
| securex | Securex Caisse AT (519) + Risques Divers (805) + Vie (944) | verify | own carriers |
| liantis | Liantis | verify | risk often P&V-backed |
| acerta | Acerta | verify | |
| partena | Partena Professional | verify | |
| ucm | UCM | verify | |
| group-s | Group S | verify | |

### B7. Professional liability (architects/engineers/notaries)
| Slug | Entity (INS) | Doc status | Note |
|---|---|---|---|
| protect | Protect (1009) | verify | architects/engineers PI — **NEW vs brief** |
| euromaf | Euromaf Ing. & Architectes (2242) | verify | **NEW vs brief** |
| notariat | Assurances du Notariat (355) | verify | notaries — niche |
| hiscox | Hiscox S.A. (3099) | **enum** | rc-pro, cyber, D&O, PJ pro |

### B8. Niche bancassurance / mortgage-life
| Slug | Entity (INS) | Doc status |
|---|---|---|
| cph-life | CPH LIFE (2539) | verify |
| credimo | Credimo (1665) | verify |

---

## C. Foreign specialists / large-commercial (Tranche 5 — only if public IPID)
AIG Europe (3084 — aig.be/ipid ✓), Chubb European + Life (3158/3159), Zurich Insurance Europe (2079),
HDI Global + Specialty (2877/2931), QBE Europe (3093), MSIG Europe (3092), Tokio Marine Europe (3100),
Liberty Mutual Europe (3148), CNA (3122), FM Insurance (3032), Axis Specialty (2259),
Berkshire Hathaway European (3150), XL Insurance / AXA XL (3142), Intact (Europe) (3285),
SI Insurance (3101), Lloyd's Insurance Company (3094), Allianz Global Corporate & Specialty (2145),
Aioi Nissay Dowa (3151), Tokio Marine, Tryg Forsikring (2736), TVM Verzekeringen (2796 — transport).
→ Mostly broker-distributed, no public IPID library. Ingest only where a public IPID page exists (AIG).
Brief-only (not on NBB list, likely FoS or via Lloyd's): MS Amlin, Markel.

## D. EXCLUDE — no consumer product docs (credit / surety / nuclear / affinity / reinsurance / MGA)
Credendo G&S (2364) + Trade Credit (2385), Euler Hermes/Allianz Trade (418), Coface (2005),
Atradius (3004) — credit/surety. ELINI (2275), EMANI (921) — nuclear. Mutual Insurance for Information
Systems (3228). Fonds de Garantie Voyages (1055). Fortegra (3251) + SquareTrade (3276) — device/warranty.
CG CAR-Garantie (2268) + Real Garant (2276) — car warranty (dealer affinity). Accelerant (3193),
Alpha Insurance (3253), Premia (333), SiriusPoint (1336) — MGA/specialty/run-off. L'Alliance Batelière
de la Sambre (870) — inland-barge mutual. Credimo/Contassur (952) — group/mortgage (Contassur = run-off).

## E. Wealth / unit-linked life (broker-distributed, low priority — docs = KID/FIF not IPID)
Lombard International (1322), OneLife (1256), Vitis Life (1424), Aviva Life & Pensions Ireland (3139),
ABEILLE Épargne Retraite (1480) + ABEILLE Vie (1479) — AFER, AFI ESCA (2746).

## F. Brokers / aggregators — NOT carriers, EXCLUDE (not on NBB register)
Yago, Callant, IncoInsurance.

---

## Counts
- In wiki: **17 brands** (~13 entities).
- Ingest targets (Group B): **~45 brands/carriers** across generalists, PJ, assistance, health, obsèques/animaux, independents, pro-liability, niche.
- Tranche-5 foreign (Group C): ~20 (few with public IPID).
- Excluded (D/E/F): ~30 (credit/nuclear/affinity/reinsurance/wealth/brokers).

## Next: product discovery
For every Group B brand, enumerate the public IPID/CG library (product name, doc type, branch, edition, URL).
`enum` rows done: hiscox, allianz, belfius-direct, cardif, nn-non-life. Everything else = to enumerate.
