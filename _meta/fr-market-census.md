# France - market census

Authoritative entity list for `sources/fr/`. Every URL below was fetched on **2026-07-30**
and its HTTP status recorded. Counts are observations from the register export, not
estimates.

## One supervisor, three codes

France is the opposite structural case to Switzerland. Switzerland splits **one market
across two supervisors** (FINMA / OFSP). France puts **one supervisor over three legal
regimes**: the ACPR (Autorité de contrôle prudentiel et de résolution, an arm of the
Banque de France) authorises and supervises every carrier, but a carrier is constituted
under exactly one of three codes, and the code decides its legal form, its governance and
part of its product range.

| Code | Entity kind | Authorised carriers |
|---|---|---|
| Code des assurances | sociétés anonymes, sociétés d'assurance mutuelles | **310** |
| Code de la mutualité | mutuelles, unions de mutuelles | **286** |
| Code de la sécurité sociale | institutions de prévoyance | **32** |

The code is a field in the register (`sous_categorie`), so this is a read, not an
interpretation. It matters for the taxonomy because the three populations do not sell the
same things: the Code de la mutualité population is overwhelmingly **complementary health**
(median 2 authorised branches; 180 of the 286 hold nothing but branches 1 Accidents and
2 Maladie), while long-tail retail non-life sits under the Code des assurances.

A second consequence, for rule 1 and for reader-facing prose: the French words are not
interchangeable. A *mutuelle* is an entity governed by the Code de la mutualité, and in
everyday French "ma mutuelle" means the complementary health cover itself. A *société
d'assurance mutuelle* is a Code des assurances entity and is a different thing. Both
translate to "mutual" and neither maps onto Belgium's usage. This belongs in the country
glossary as a false friend (see BOOTSTRAP-COUNTRY.md §6).

## Register

The ACPR replaced its periodic Excel lists with **Refassu**, a register regenerated daily.
`refassu.fr` now redirects to `regafi.fr`, which since the merge carries both the banking
and the insurance registers.

| Source | URL | Fetched | Contents |
|---|---|---|---|
| Landing | `https://www.refassu.fr/` | 200, redirects to `https://www.regafi.fr/pages/accueil/` | search UI (SPA) |
| API portal | `https://www.regafi.fr/pages/api-acpr` | 200 | Opendatasoft ("huwise") portal, Explore API v2.1 |
| Catalog | `https://www.regafi.fr/api/explore/v2.1/catalog/datasets` | 200, JSON | 17 datasets |
| Entities | `.../datasets/prd-assurance-entites/exports/csv?delimiter=%3B` | 200, 605 KB | **1 763 rows**, `modified` 2026-05-20 |
| Groups | `.../datasets/prd-assurance-groupes/exports/json` | 200, 440 KB | 110 groups, with head-of-group |
| Branch labels | `.../datasets/prd-assurance-ux/exports/json` | 200, 14 KB | 68 rows: the R.321-1 branch and sub-branch labels |
| Inbound passports | `.../datasets/prd-assurance-passeports-entrants/...` | 200 | 1 041 rows |
| Outbound passports | `.../datasets/prd-assurance-passeports-sortants/...` | 200 | 2 693 rows |

**The API answers anonymously.** The portal offers a free account and the page reads as if
one were required; measured, it is not: the catalog, the record endpoints and the CSV/JSON
exports all return 200 with no key and no cookie. Nothing in this census needed an account,
a browser or a scraping service.

### What the 1 763 rows are

The register is not a carrier list until it is filtered. Breakdown by `type_entite`:

| `type_entite` | Rows | Keep? |
|---|---|---|
| Organisme d'assurance | **628** | yes, this is the census |
| Passeport entrant LPS | 586 | no, EEA freedom of services |
| Passeport entrant LE | 250 | no, EEA branch |
| Passeport entrant LPS de LE | 197 | no |
| Véhicule de groupe | 82 | no, holdings, not carriers |
| Autre entité juridique | 16 | no |
| Succursale de pays tiers | 4 | yes, but out of scope for now |

So **628 French-authorised carriers**, plus 1 033 EEA entities that may write French risks
without French authorisation. The 82 `Véhicule de groupe` rows are the same trap as
Switzerland's six `Groupe d'assurance` entries in `uid.csv`: group holdings that look like
carriers if you count rows. Exclude them.

Of the 628: 338 non-vie, 177 mixte, 71 vie, 42 réassurance. 452 are `Soumis à Solva II`.

### De-duplication, decided in writing

`denomination_groupe` is populated in the entity export, so group affiliation is free data
rather than research. Carriers per group, top of the list:

| Group | Carriers | Group | Carriers |
|---|---|---|---|
| GROUPAMA | 23 | AG2R LA MONDIALE | 10 |
| COVEA (MAAF, MMA, GMF) | 19 | Groupe AXA | 10 (+6 Mutuelles AXA) |
| AEMA (Macif, Abeille, Aésio) | 17 | KLESIA ASSURANCES | 9 |
| MALAKOFF HUMANIS | 15 | PRO BTP | 7 |
| SGAM MATMUT | 13 | GROUPE VYV | 7 |
| SGAM BTP | 12 | APICIL | 7 |

286 of the 628 carriers belong to no group at all; almost all of those are small Code de la
mutualité entities.

**Rule adopted for France: the ACPR register is the carrier list, ORIAS is the
intermediary list, and a consumer brand may be neither.** France's retail market is full of
brands that are not carriers. They are `mandataire d'assurance` or `courtier` entities
registered at ORIAS, distributing a carrier's paper. Measured examples:

- **Direct Assurance** is absent from the register. Its own conditions générales say, at
  the top of the auto and the MRH contract: "L'Assureur auprès duquel vous avez souscrit
  votre contrat est AXA France IARD" and "La gestion de votre contrat a été déléguée par
  AXA France IARD à Avanssur dont la marque est Direct Assurance mandataire d'assurance
  d'AXA France IARD et courtier d'assurance - Orias n° 19006337". Carrier = AXA France
  IARD. Avanssur itself returns 0 hits in the register (searched `denomination` and the
  full-text search dataset).
- **Luko** now trades as "Luko by Allianz Direct" and is absent from the register.
- **L'olivier assurance**, **Leocare**, **Lovys**: absent. L'olivier's carrier is
  ADMIRAL EUROPE COMPANIA DE SEGUROS, which appears only as a `Passeport entrant`
  (Spanish supervision, DGSFP).
- **April**, **Solly Azar**, **Alptis**: absent, and correctly so. These are courtiers
  grossistes, not carriers.
- **Wakam** *is* in the register (Code des assurances, 12 branches) and is the carrier
  behind a large share of the French MGA brands. Expect the same product library to
  surface under several brand names on top of Wakam paper.

The Belgian lesson (one health carrier behind three names) therefore recurs in France in a
stronger form, and the resolution is better here: **the document itself names its carrier**,
under a heading like "Assureur" or "Qui vous assure ?", because the DDA requires it. So
carrier attribution is grounded in the source document, never inferred from a brand.

Following the Belgian precedent for `lar` (keep the brand slug, record the carrier), a
brand with its own distinct document library gets its own slug with an explicit
`carrier:` note. A brand that merely rebadges a carrier's identical library is a duplicate
and is skipped.

Trade names diverge from legal names often enough that name search alone will miss
entities. Measured: MAIF is registered as `MUTUELLE ASSURANCE DES INSTITUTEURS DE FRANCE`,
MGEN as `MUTUELLE GENERALE DE L EDUCATION NATIONALE`, Swiss Life as `SWISSLIFE ...` in one
word. The register also strips apostrophes and accents inconsistently, so match on a
normalised string, not on equality.

## Branch nomenclature (this is where France pays off)

The register carries, per carrier, the list of branches it is authorised for
(`branches`, `branche_count`), and `prd-assurance-ux` carries the official labels. That is
the French branch scheme of **art. R.321-1 du Code des assurances**, from the regulator,
with sub-branches: 1 Accidents (1A-1D), 2 Maladie (2A-2C), 3 Corps de véhicules terrestres,
4 ferroviaires, 5 aériens, 6 maritimes/lacustres/fluviaux (6A-6C), 7 Marchandises
transportées, 8 Incendie et éléments naturels (8A-8F), 9 Autres dommages aux biens,
10 RC véhicules terrestres automoteurs, 11 RC véhicules aériens, 12 RC véhicules maritimes,
13 RC générale, 14 Assurance crédits (14A-14E), 15 Caution (15A-15B), 16 Pertes pécuniaires
diverses (16A-16K), 17 Protection juridique, 18 Assistance, 20 Vie-décès,
21 Nuptialité-natalité, 22 Assurances liées à des fonds d'investissements,
23 Opérations tontinières, 24 Capitalisation, 25 Gestion de fonds collectifs,
26 Prévoyance collective, plus the IRP variants (20IRP, 22IRP, 26IRP), FRPS, and
R1/R2 for reinsurance. Branch 28 exists in the nomenclature and is flagged
"abrogé par décret n 94-635 du 25 juillet 1994"; one carrier still carries it.

This is the *prudential authorisation* scheme, not the way products are sold, so
`sources/fr/_country.yml` declares consumer-facing slugs and records the R.321-1 number in
`code:`, exactly as `sources/ch/_country.yml` records the OS annexe 1 codes.

Branch counts over the 628 carriers, most populated first: 2 Maladie 381, 1 Accidents 380,
20 Vie-décès 198, 16 Pertes pécuniaires 128, 9 Autres dommages aux biens 116,
17 Protection juridique 114, 13 RC générale 108, 8 Incendie 107, 3 Corps de véhicules
terrestres 87, 10 RC auto 80, 18 Assistance 76, 7 Marchandises 75, 21 Nuptialité-natalité
70, 22 Fonds d'investissement 64, 6 Corps maritimes 62, 12 RC maritime 61, 15 Caution 47,
24 Capitalisation 46, 5 Corps aériens 35, 11 RC aérienne 35, 4 Corps ferroviaires 28,
14 Crédits 22, 26 Prévoyance collective 14, 25 Gestion de fonds collectifs 12,
23 Opérations tontinières 1.

## Legal regime (rule 1, per jurisdiction)

France is the most explicitly permissive of the three countries covered so far for a pure
information tool, and the reasoning is close to Switzerland's.

**Code des assurances art. L. 511-1** defines distribution, in force since 2018-10-01:

> La distribution d'assurances ou de réassurances est l'activité qui consiste à fournir des
> recommandations sur des contrats d'assurance ou de réassurance

and then carves out, at II 4°:

> La simple fourniture d'informations sur des produits d'assurance ou de réassurance, sur
> un intermédiaire d'assurance ou de réassurance, une entreprise d'assurance ou de
> réassurance à des preneurs d'assurance potentiels, lorsque le fournisseur ne prend pas
> d'autres mesures pour aider le souscripteur ou l'adhérent à conclure un contrat
> d'assurance ou de réassurance.

So the French exposure, like the Swiss one, is not in describing or even in comparing: it
is in **taking a further step towards a contract being concluded**. A free, source-cited
wiki with no quote engine, no lead capture, no subscription funnel and no remuneration
falls inside II 4°. Registration at **ORIAS** (art. L. 512-1) attaches to intermediaries,
which II 4° says this is not.

Two French specifics to keep in view, both stricter than the Belgian framing:

- The line that would be crossed is **"recommandations"** and, in art. L. 521-4, the
  *recommandation personnalisée*. Ranking, scoring or "best for you" output is exactly the
  thing II 4° stops covering. The project's rule 1 already forbids all of it.
- The exclusion is conditioned on the absence of any *other measure to help conclude*. A
  deep link to a subscription page, an affiliate parameter or a referral fee would each
  defeat it. Monetisation changes the analysis in France as it does in Switzerland.

Keeping rule 1 strict everywhere remains the simple way to be safe in Belgium, Switzerland
and France at once. **No disclaimer change is required for France**: the rendered
disclaimer's claim (information only, no advice, not an intermediary) is true here.
`render.DISCLAIMER` can stay one string for now; the moment a country needs a different
claim, make it per-country before shipping that country.

**Copyright on verbatim quoting.** France has no fair-use doctrine; it has the *exception
de courte citation*, **Code de la propriété intellectuelle art. L. 122-5 3° a)**, which
permits short quotations justified by the critical, polemical, pedagogical, scientific or
informational character of the work incorporating them, provided the author's name and the
source are indicated. The project quotes short excerpts, cites the source URL and the page
number, and is informational and non-commercial, which is the shape the exception expects.
Two cautions specific to France: the exception requires the quotation to be **short
relative to the quoting work and to the quoted work**, so key_quotes must stay excerpts and
never approach a reproduction of a document's substance; and the *droit moral* means the
quote must not be altered. Both are already enforced by the grounding rules, which require
quotes to be verbatim substrings.

## Fetch tiers, measured 2026-07-30

The whole census was built without Firecrawl and without a browser. Insurer sites are
mixed. Status codes below are the homepage; "urllib" and "curl" differ on some hosts
because the WAF fingerprints the client, which is itself a useful finding.

| Tier | Insurers | Note |
|---|---|---|
| `plain` | maif, matmut, axa, groupama, gan, direct-assurance, acheel, alan, generali, thelem, suravenir, lolivier, luko, mgen, april, cnp, sogessur, creditmutuel, wakam, leocare, smacl, apivia, malakoff-humanis, ag2r, harmonie-mutuelle | 200 to plain Python stdlib |
| `plain`, curl-hostile | gmf, maaf, allianz, abeille-assurances | 200 to Python `urllib`, **403 to `curl`** on the same URL. Do not conclude "WAF" from a curl 403 alone. |
| `browser` | axa's `bibliotheque-ipid.html` | page returns 200 but the document list is client-rendered; 0 PDF hrefs in the HTML |
| `waf` | macif, mma, swisslife | 403 to both clients |
| `unreachable` | pacifica.fr, assurances.credit-agricole.fr | connection timed out; Crédit Agricole's library is under `credit-agricole.fr` instead |

Two non-insurer sources also matter and behave differently:

- **Legifrance is Cloudflare-gated.** `curl` gets a 403 interstitial ("Enable JavaScript
  and cookies to continue") even with a full browser header set. It *is* readable through
  the `WebFetch` tool. The legal text above was read that way. Do not add Legifrance to an
  unattended fetch loop.
- **ORIAS** (`https://www.orias.fr/web/guest/search`) returns 200 but is a search UI. No
  bulk export was found. Not needed to build the product census; recorded so the dead end
  is not re-derived.

### Document libraries found so far, without Firecrawl

| Insurer | Library | Docs seen | Kind |
|---|---|---|---|
| thelem | `https://www.thelem-assurances.fr/documents-information-produit/` | **46** | IPID, all branches, one page, direct `.pdf` hrefs |
| luko | `https://www.fr.luko.eu/conditions-generales/` | 16 | 8 CG + 8 IPID (habitation, voyage) |
| direct-assurance | `https://www.direct-assurance.fr/nos-assurances/conditions-generales-particulieres` | 11 | full CG (auto 57 pp, MRH 50 pp) + IPID + notice, on `cdn.prismic.io` |
| maif | `https://www.maif.fr/files/live/sites/maif-fr/files/pdf/documentation-contractuelle/<cat>/` | 11+ | mostly IPID, plus notices for life/décès. No directory index; enumerate from product pages |

**A market-level observation to carry into the ingestion plan.** In Belgium the standard
public document is the *conditions générales*. In France the standard public document is
the **IPID** (Document d'Information sur le Produit d'Assurance, the French DDA/IDD
mandated 2-page sheet). Full CGs are published by some insurers (Direct Assurance, Luko)
and withheld until subscription by others (MAIF publishes IPIDs and life notices, not auto
or MRH CGs). The corpus will therefore be IPID-heavy, which the schema already supports
(`document_type: ipid`) but which yields thinner extractions per document than Belgium's
CGs. Record it as an observation, not as a gap in the insurer's compliance: publishing the
IPID is what the law requires, publishing the CG is not.

Sample text-layer check, `pymupdf`, on downloaded files:

| File | Pages | Chars |
|---|---|---|
| Direct Assurance auto CG (02.26) | 57 | 256 238 |
| Direct Assurance MRH CG (03.26) | 50 | 242 695 |
| MAIF IPID VAM auto | 2 | 7 457 |

The two CGs exceed `extract.MAX_TEXT_CHARS` (240 000), so they will be truncated with a
`gaps` note by design. Nothing to fix; noted so the note is not read as a bug.

## Ingestion shortlist

Ranked by "public French document library, reachable without a browser, first-party
carrier, high consumer value".

**Tier 1, ready to transcribe:**

1. **thelem** - THELEM ASSURANCES, Code des assurances, 14 branches, group THELEM. Own
   agrément, no fronting ambiguity. One library page, 46 IPIDs spanning auto, moto, cyclo,
   quad, voiturette, EDPM, camping-car, caravane, mobil-home, MRH, MRI, MRP, RC pro,
   protection juridique (part / pro / agri), chasse, scolaire, agricole (Terrenis,
   Prévagri), prévoyance and capital décès. Exercises most of the taxonomy in one insurer.
2. **direct-assurance** - brand of Avanssur, **carrier AXA France IARD**. Full CGs, plain
   CDN. The place to see whether the extraction holds on a 57-page French CG.
3. **luko** - "Luko by Allianz Direct", carrier to confirm from the documents. CG + IPID
   pairs, habitation and voyage.
4. **maif** - MUTUELLE ASSURANCE DES INSTITUTEURS DE FRANCE, own agrément, group MAIF.
   IPIDs and life notices; enumerate from product pages, there is no index.

**Tier 2, needs enumeration work:** groupama, gan (both GROUPAMA, own agréments),
generali, matmut, acheel, wakam, smacl, thelem's sister brands.

**Tier 3, blocked or deferred:** macif, mma, swisslife (WAF); axa's IPID library
(client-rendered); gmf, maaf, allianz, abeille (fetchable, but with `urllib` only, so
record the client in the source file).

**Excluded as non-carriers** (ORIAS intermediaries or courtiers grossistes, no first-party
paper): april, solly azar, alptis, leocare, lovys, l'olivier (Admiral, passeport entrant).
Ingest their documents, if at all, under the carrier that signs them.

## Open questions

- Whether `Succursale de pays tiers` (4 entities) should ever enter the census. They hold
  French authorisation under the Code des assurances but are branches of non-EEA carriers.
  Deferred, not decided.
- Whether the 1 033 EEA passporting entities deserve a presence. They write French risks
  under home-state supervision, and at least one consumer brand (l'olivier / Admiral) sits
  there. Deferred: the wiki's unit is a document, and their documents are French-language
  and French-law, so the argument for including them is stronger than it looks.
- The 286 Code de la mutualité carriers are a long tail of small health mutuals. A census
  is not an ingestion plan: most publish little and duplicate each other's cover. Decide a
  cutoff before touching them.
