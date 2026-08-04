# Luxembourg - market census

Authoritative entity list for `sources/lu/`. Every URL below was fetched on **2026-08-02**
with plain Python `urllib` and its HTTP status recorded. No browser, no scraping service.
Counts are observations from the register exports, not estimates.

## One supervisor, one law - and a market that is not domestic

Belgium has one supervisor and one regime. Switzerland splits one market across two
supervisors (FINMA / OFSP). France puts one supervisor over three legal codes. Luxembourg
is structurally simpler than all three on the supervision axis and stranger than all three
on the *market* axis.

The **Commissariat aux Assurances (CAA)** authorises and supervises every insurance
undertaking, reinsurance undertaking, pension fund, insurance-sector professional and
distributor. There is one authorising statute, the **loi modifiée du 7 décembre 2015 sur
le secteur des assurances** (hereafter "LSA"), and one contract statute, the **loi modifiée
du 27 juillet 1997 sur le contrat d'assurance**. No second supervisor, no parallel code.

The distinguishing fact is elsewhere: **the overwhelming majority of the insurance written
from Luxembourg is not sold to people in Luxembourg.** Measured from the CAA's own
annual-report annexes for financial year 2025:

| | Total premiums 2025 | Written on the Luxembourg market | Share |
|---|---|---|---|
| Life (`Primes par pays d'engagement`, Tab 4.25) | 35 095 771 k€ | 1 765 819 k€ | **5,0 %** |
| Non-life (`Primes émises brutes par pays de situation du risque`, Tab 3.18) | 19 918 771 k€ | 1 735 762 k€ | **8,7 %** |

The life side is a French savings market operated from Luxembourg: France alone accounts
for **18 332 210 k€, more than 52 % of total life premiums**, and **122 970 391 k€ of
technical provisions, 42 % of the sector's 290 247 596 k€**. Luxembourg itself is the
*fifth* market by provisions (15 639 624 k€), behind France, Italy, Germany and Belgium.
The CAA states it plainly in the non-life chapter of the 2025-2026 annual report: the sector
is "fortement interconnecté de par son modèle économique reposant sur les opérations
transfrontalières".

Reinsurance is a third population again: **207 authorised reinsurance undertakings**, almost
all captives of foreign industrial and financial groups (the 2025-2026 report's agrément
table lists new entrants by *nationalité du groupe*: Germany, France, Belgium, Austria,
Spain, Morocco…). They write no consumer contracts at all.

### What that means for a wiki that documents consumer contracts

Concretely, and this should be stated before anyone plans an ingestion:

- **The licence count is not the corpus.** 63 Luxembourg-authorised direct insurers exist;
  the number that sell a retail product to a resident, with public documents, is under ten.
- The domestic retail market is genuinely small in absolute terms. Non-life premiums written
  on Luxembourg risks were **1,74 bn €** in 2025 across a resident population of
  **690 959** (STATEC, 1 January 2026, published 2026-05-06). The CAA's own per-capita
  indicators (Tab 3.27, 2025, €/inhabitant): CASCO **625**, RC véhicules terrestres
  automoteurs **279**, incendie risques simples d'habitation **188**, RC familiale **29**.
  Those four lines *are* the Luxembourg retail non-life market as the supervisor measures it.
- **The whole domestic non-life book fits in one table** - `Primes émises brutes sur les
  opérations luxembourgeoises` (Tab 3.23), 2025, k€: 3 Corps de véhicules terrestres
  (casco) **428 790**, 13 RC générale **290 152** *of which a) RC familiale 20 245*,
  8 Incendie et éléments naturels **207 214** *of which a) risques simples d'habitation
  129 236*, 9 Autres dommages aux biens **192 303**, 10 RC véhicules terrestres automoteurs
  **191 451**, 2 Maladie **148 317**, 16 Pertes pécuniaires **75 902**, 1 Accidents
  **41 865**, 19 Réassurance acceptée **36 138**, 17 Protection juridique **33 399**,
  18 Assistance **20 394**, 14 Crédit **19 211**, 7 Marchandises **16 075**, 11 RC aériens
  **9 961**, 15 Caution **8 505**, 6 Corps maritimes **7 832**, 12 RC maritimes **4 581**,
  5 Corps aériens **3 671**, 4 Corps ferroviaires **0**. Total **1 735 762**. That table
  *is* the branch taxonomy's evidence base.
- The domestic share is concentrated in exactly the consumer branches and nowhere else
  (Tab 3.26, share of each branch written on Luxembourg operations, 2025): RC familiale
  **83,05 %**, protection juridique **80,42 %**, incendie risques simples d'habitation
  **57,93 %**, corps de véhicules terrestres **44,37 %**, assistance **32,72 %**, RC auto
  **26,08 %**, accidents **25,80 %**, maladie **23,10 %**, autres dommages aux biens
  **11,48 %**. Every other branch is below 10 % and most are below 3 %. The mirror image
  of that table is the ingestion plan: the Luxembourg-facing corpus is auto, habitation,
  RC familiale, protection juridique, accidents, santé complémentaire, assistance, and
  the life savings products.
- **A large part of the working population is not a Luxembourg consumer at all.** STATEC
  counts **225 840 incoming cross-border salaried workers in 2023** (Regards N°01 03/2026),
  54,2 % resident in France, 23,0 % in Germany, 22,7 % in Belgium. Their car, home and
  household liability contracts are bought where they live and are governed by that
  country's law; only their health and accident cover follows the Luxembourg workplace
  (see "Compulsory covers" below). This is a reason the Luxembourg retail corpus is small
  relative to the size of the economy, and a reason a Luxembourg branch page must not be
  read as advice for a frontalier.

So: expect a **small, high-quality domestic corpus** and a very large licence population
that is out of scope. Say which number is meant, every time.

## Register

The CAA publishes its registers as HTML lists under `https://www.caa.lu/fr/operateurs`,
one page per category, each with an **"Exporter en CSV"** link to a static file under
`/uploads/documents/files/csv/`.

**The register is machine-readable, anonymously, over plain HTTP.** Every CSV returned
`200 text/csv` to `urllib` with no key, no cookie and no account. All fifteen files carried
`Last-Modified: Sun, 02 Aug 2026 01:00:1x GMT`, i.e. they are regenerated nightly. There
is no JSON API and no Opendatasoft-style query endpoint as France's ACPR turned out to
have - what exists is a flat nightly CSV dump per list, which is enough.

| List | CSV | Rows (excl. header) |
|---|---|---|
| Assureurs luxembourgeois non-vie | `AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv` | **35** |
| Assureurs luxembourgeois vie | `AssurancesDirectes_AssureursLuxembourgeoisVie.csv` | **28** |
| Succursales étrangères non-vie | `AssurancesDirectes_SuccursalesEtrangeresNonVie.csv` | **9** |
| Succursales étrangères vie | `AssurancesDirectes_SuccursalesEtrangeresVie.csv` | **5** |
| Réassurances | `Reassurances.csv` | **207** |
| Fonds de pension luxembourgeois | `FondsDePension_FondsDePensionLuxembourgeois.csv` | **2** |
| Professionnels du secteur des assurances (PSA) | `ProfessionnelsDuSecteurDesAssurances.csv` | **33** |
| Domiciliataires | `Domiciliataires.csv` | **6** |
| Agents d'assurances | `Distribution_AgentsDAssurances.csv` | **3 112** |
| Agences d'assurances | `Distribution_AgencesDAssurances.csv` | **233** |
| Sociétés de courtage | `Distribution_SocietesDeCourtage.csv` | **78** |
| Courtiers personnes physiques | `Distribution_CourtiersPersonnesPhysiques.csv` | **100** |
| Sous-courtiers | `Distribution_SousCourtiers.csv` | **430** |
| Intermédiaires d'assurance à titre accessoire | `Distribution_IntermediairesDAssuranceATitreAccessoire.csv` | **8** |
| Responsables de la distribution | `Distribution_ResponsablesDeLaDistribution.csv` | **268** |

Base URL for all of them: `https://www.caa.lu/uploads/documents/files/csv/<file>`.

**Two lists have no CSV export.** The freedom-of-services notification pages
(`/fr/operateurs/assurances-directes/lps-notifications-non-vie` and `…-vie`) return the
whole table inline in HTML - no export link, no pagination. Parsed from the markup on
2026-08-02: **631 rows / 628 distinct names** inbound non-life, **129 rows / 128 distinct
names** inbound life. These are EEA insurers notified to write Luxembourg risks under
freedom of services; they hold no Luxembourg authorisation.

### The population, as the register itself splits it

**Direct insurance, Luxembourg-established: 63.** 35 non-vie + 28 vie, and the two sets do
**not intersect** - Luxembourg applies the specialisation principle strictly, so no single
Luxembourg company is both a life and a non-life insurer. (Four life companies additionally
hold non-life branches 1 Accidents and 2 Maladie as complementary covers: ERGO Life,
iptiQ Life, Swiss Life (Luxembourg), Zurich Eurolife. That is a life authorisation with
accessory covers, not a mixed insurer.)

**Foreign branches (libre établissement): 14 rows, 11 distinct entities.** Three appear in
both the vie and the non-vie list (`ASSICURAZIONI GENERALI S.p.A.-LUXEMBOURG BRANCH`,
`ERGO INSURANCE`, `FIDELIDADE - COMPANHIA DE SEGUROS S.A.`), so counting rows overstates
the population by three. Count entities.

**Reinsurance: 207.** **Pension funds: 2.**

Measured total of the three carrier categories: **63 + 11 + 207 = 281**. The CAA's own
2025-2026 annual report states "Le nombre total d'entreprises d'assurance et de réassurance
établies au Luxembourg s'établit à **283** unités fin juin 2026". The two-unit difference is
not reconciled here: the report's cut-off is 01/07/2026 and this read is 02/08/2026, and the
report may be counting branch rows rather than distinct branch entities. Recorded as a
discrepancy, not resolved.

**Freedom of services, inbound: 628 non-life + 128 life distinct notified EEA insurers.**
Not authorised in Luxembourg, but legally able to write Luxembourg risks. The French census
settled that passporting entities can be behind mainstream consumer brands (Luko / Allianz
Direct); the same possibility exists here and has **not** been tested against Luxembourg
consumer brands. Open question below.

**Distribution: 3 112 agents, 233 agencies, 78 brokerage companies, 100 individual brokers,
430 sub-brokers, 8 ancillary intermediaries, 268 responsables de la distribution.** Note
the ratio: 3 112 tied agents against 178 broker entities. Luxembourg retail distribution is
overwhelmingly an agent market, which matters because the agent's principal is named in the
`Compagnies pour lesquelles l'agent détient un agrément` column of the CSV - carrier
attribution for a distributor is free data here, not research.

### De-duplication and the carrier/brand rule

**Rule adopted for Luxembourg: the CAA register is the carrier list; the CAA distribution
registers are the intermediary lists; a consumer brand may be neither.** Same rule as
France, with two Luxembourg specifics measured on 2026-08-02:

- The **holding/brand pattern is visible inside the register**. `FOYER ASSURANCES S.A.`
  (non-vie), `FOYER VIE S.A.` (vie), `FOYER-ARAG` (branch 17 only, legal protection) and
  `Foyer Global Health` (branches 1, 2, 13, 16, 18 - the expat health book) are four
  separate authorisations under one commercial group. Likewise
  `LA LUXEMBOURGEOISE S.A.` / `LA LUXEMBOURGEOISE-VIE S.A.` (brand "lalux"), which also
  fronts `DKV LUXEMBOURG S.A.` in its agency network. Four authorisations are not four
  document libraries: decide slug ownership before ingesting.
- **`CMCM` (Caisse Médico-Complémentaire Mutualiste) is absent from the CAA register**,
  checked against both Luxembourg lists. It is a significant provider of consumer
  complementary-health cover in Luxembourg. **Its legal basis and supervisor were not
  established** from a primary source in this pass - its own "À propos" page states no
  legal form beyond the name. Treat as an open item; do not assume it is an insurer, and
  do not assume it is not.

The trade-name/legal-name divergence that bit the French census is milder here (`lalux` for
`LA LUXEMBOURGEOISE`, `Foyer` matching the legal name) but the register normalises
inconsistently: entries carry the LEI in parentheses after the name
(`FOYER ASSURANCES S.A. (5493000DB4L2GMHE8F84)`) on some lists and not others, and the
`Branches` column carries occasional sub-branch suffixes with no legend published on the
page (`COLONNADE INSURANCE S.A.` reads `… 9, 10b*, 11 …`; the meaning of `10b*` is **not
established**). Match on a normalised string with the parenthesised LEI stripped.

## Branch nomenclature

The register carries, per undertaking, the branches it is authorised for, and the scheme is
the **annexes of the LSA itself**, which transpose the Solvency II annexe:

- **ANNEXE I - CLASSIFICATION PAR BRANCHE D'ASSURANCE NON VIE**, A. *Classification des
  risques par branches d'assurance*: 1 Accidents, 2 Maladie, 3 Corps de véhicules terrestres
  (autres que ferroviaires), 4 Corps de véhicules ferroviaires, 5 Corps de véhicules aériens,
  6 Corps de véhicules maritimes, lacustres et fluviaux, 7 Marchandises transportées,
  8 Incendie et éléments naturels, 9 Autres dommages aux biens, 10 R.C. véhicules terrestres
  automoteurs, 11 R.C. véhicules aériens, 12 R.C. véhicules maritimes lacustres et fluviaux,
  13 R.C. générale, 14 Crédit, 15 Caution, 16 Pertes pécuniaires diverses, 17 Protection
  juridique, 18 Assistance. Part B of the same annexe gives the combined-authorisation
  labels ("Assurance automobile" = branches 1 (4e tiret), 3, 7 and 10; "Toutes branches";
  etc.).
- **ANNEXE II - CLASSIFICATION PAR BRANCHE D'ASSURANCE VIE**: I Assurances en cas de vie, de
  décès, mixtes, de rentes non liées à des fonds d'investissement; II Nuptialité, natalité;
  III Assurances liées à des fonds d'investissement; IV Permanent health insurance;
  V Opérations tontinières; VI Opérations de capitalisation; VII Gestion de fonds collectifs
  de retraite.

This is the **prudential** scheme, not the way products are sold, so `sources/lu/_country.yml`
declares consumer-facing slugs and records the annexe number in `code:`, exactly as the
Swiss and French manifests do.

Branch holdings across the 44 non-life rows (35 Luxembourg + 9 branches), most populated
first: 16 Pertes pécuniaires **32**, 13 RC générale **30**, 7 Marchandises / 8 Incendie /
9 Autres dommages **28** each, 1 Accidents **27**, 2 Maladie / 17 Protection juridique **23**,
6 Corps maritimes **22**, 12 RC maritime **20**, 18 Assistance **20**, 3 Corps terrestres **19**,
5 Corps aériens / 15 Caution / 10 **RC auto 16**, 4 Corps ferroviaires **15**, 11 RC aérienne /
14 Crédit **13**. Six undertakings hold all eighteen branches; the median holding is eight.

Over the 33 life rows: I **33**, III **32**, VI **27**, II **23**, VII **19**, IV **2**,
V **0** - no Luxembourg undertaking holds the tontine branch.

The retail signal is in branch 10: only **13 of 35** Luxembourg non-life insurers and **3 of
9** foreign branches are authorised for compulsory motor liability, and most of the thirteen
(AIG, Aioi Nissay Dowa, Colonnade, Hiscox, Liberty Mutual, SI Insurance, Stadhold, Swiss Re
International, Tokio Marine) are commercial or fronting operations, not retail motor
insurers. The retail motor carriers are **AXA Assurances Luxembourg, Baloise Assurances
Luxembourg, Foyer Assurances, La Luxembourgeoise**.

## Legal regime (rule 1, per jurisdiction)

Luxembourg transposed the IDD (directive (UE) 2016/97) into the LSA. Two provisions matter.

**LSA art. 279, point 16** defines distribution, and its point f) is the limb that catches
comparison sites:

> 16. «distribution d'assurances» : toute activité, y compris celle exercée par une entreprise
> d'assurance sans l'intervention d'un intermédiaire d'assurances, consistant :
> a) à fournir des conseils sur des contrats d'assurance,
> b) à proposer des contrats d'assurance,
> c) à réaliser d'autres travaux préparatoires à leur conclusion,
> d) à conclure de tels contrats,
> e) à contribuer à la gestion et à l'exécution des contrats d'assurance, sous réserve des
> dispositions de l'article 281-1, paragraphe 2, point b), notamment en cas de sinistre ou
> f) à fournir une des prestations suivantes lorsque le client peut choisir des critères
> relatifs à un contrat d'assurance sur un site internet ou par d'autres moyens de
> communication, et qu'il peut conclure le contrat directement ou indirectement par ce
> biais :
> (i) la fourniture d'informations sur un ou plusieurs contrats d'assurance, ou
> (ii) l'établissement d'un classement de produits d'assurance comprenant une comparaison
> des prix et des produits, ou annonçant une remise de prime.

**LSA art. 281-1, paragraphe 2, point d)** is the exact Luxembourg counterpart of the French
`C. assur. art. L. 511-1 II 4°`:

> (2) Aucune des activités suivantes n'est considérée comme une distribution d'assurances ou
> de réassurances:
> […]
> d) la simple fourniture d'informations sur des produits d'assurance ou de réassurance, sur
> un intermédiaire d'assurances, un intermédiaire de réassurances, une entreprise d'assurance
> ou de réassurance à des preneurs d'assurance potentiels, lorsque le fournisseur ne prend
> pas d'autres mesures pour aider le client à conclure un contrat d'assurance ou de
> réassurance.

Source for both: the CAA's own coordinated text,
`https://www.caa.lu/uploads/documents/files/Loi_SecteurAssurances_2015-12-07_coord_2026-04-03_ESAP_.pdf`
(version coordonnée au 2026-04-03, fetched 2026-08-02). Point d) was inserted by the loi du
10 août 2018 transposing the IDD; the paragraph is marked as amended in the coordinated text.

So the Luxembourg analysis lands in the same place as the French and the Swiss one, and the
line is drawn twice, in the same place, from opposite directions:

- **art. 281-1 (2) d)** takes a pure information service *out* of distribution, on the
  express condition that the provider "ne prend pas d'autres mesures pour aider le client à
  conclure un contrat".
- **art. 279, 16 f)** puts information and ranking *into* distribution precisely when "il
  peut conclure le contrat directement ou indirectement par ce biais". Note what f) does
  and does not say: even a *ranking with a price comparison* is only caught when the site
  is a path to conclusion. A wiki with no quote engine, no lead capture, no deep link to a
  subscription page and no remuneration is on the safe side of both.

The project's rule 1 is already stricter than either provision requires, and it should stay
that way. **No disclaimer change is required for Luxembourg**: the rendered disclaimer's
claim (information only, no advice, not an intermediary) is true here.

Two Luxembourg specifics to keep in view:

- **Advice is the default here, by national rule.** The CAA's published general-good rules
  (`https://www.caa.lu/uploads/documents/files/GeneralGoodRules_Luxembourg.pdf`, fetched
  2026-08-02) record, against IDD art. 22, **LSA art. 295-10, paragraphe 1**: "When
  distributing insurance products to customers whose habitual residence or establishment is
  in the Grand Duchy of Luxembourg, any distributor of insurance products shall provide
  advice […] however the customer may agree to waive this advice individually in writing and
  before any act of distribution." Luxembourg goes *beyond* the IDD minimum in requiring
  advice. That raises, not lowers, the cost of accidentally being a distributor.
- **Monetisation defeats the exclusion**, as in France and Switzerland: art. 281-1 (2) d)
  is conditioned on the absence of any *other measure to help conclude*, and an affiliate
  parameter or referral fee is such a measure.

**No Luxembourg-specific compulsory-insurance provisions are listed in the general-good
document.** Its "General good provisions referred to in Article 180 of Solvency II" table is
empty ("/") for both FoS and FoE. Solvency II art. 180 is the compulsory-insurance article,
so this reads as "nothing beyond the general regime" - but the document's own disclaimer says
it is "not necessarily comprehensive, complete or up to date", so it is recorded as an
observation, not as proof that no specific provisions exist.

### Copyright on verbatim quoting

**Loi modifiée du 18 avril 2001 sur les droits d'auteur, les droits voisins et les bases de
données, art. 10, 1°** (fetched from Legilux 2026-08-02,
`https://data.legilux.public.lu/eli/etat/leg/loi/2001/04/18/n2/jo/fr/html`):

> Art. 10. Lorsque l'œuvre a été licitement rendue accessible au public, l'auteur ne peut
> interdire:
> 1° les courtes citations en original ou en traduction, justifiées par le caractère
> critique, polémique, pédagogique, scientifique ou d'information de l'œuvre à laquelle elles
> sont incorporées.
> Les utilisations visées à l'alinéa ci-avant ne peuvent être faites sans l'autorisation de
> l'auteur que pour autant qu'elles soient conformes aux bons usages, qu'elles ne poursuivent
> pas un but de lucre et qu'elles ne portent atteinte ni à l'œuvre ni à son exploitation.

Close to the French *exception de courte citation*, with one condition France does not spell
out in the same words: **"qu'elles ne poursuivent pas un but de lucre"**. Non-commercial use
is an explicit statutory condition of the Luxembourg quotation exception. The article also
requires the author's name and the title of the reproduced work to be indicated. So
monetising this project would change the analysis in Luxembourg **twice over** - once under
LSA art. 281-1 (2) d), once under this article. Worth recording as the sharpest reason yet
to keep the project non-commercial.

## Languages

**Loi du 24 février 1984 sur le régime des langues** (Legilux,
`https://data.legilux.public.lu/eli/etat/leg/loi/1984/02/24/n1/jo/fr/html`, fetched
2026-08-02):

> Art. 1er. Langue nationale
> La langue nationale des Luxembourgeois est le luxembourgeois.
>
> Art. 2. Langue de la législation
> Les actes législatifs et leurs règlements d'exécution sont rédigés en français. […]
>
> Art. 3. Langues administratives et judiciaires
> En matiére administrative, contentieuse ou non contentieuse, et en matière judiciaire, il
> peut être fait usage des langues française, allemande ou luxembourgeoise, sans préjudice
> des dispositions spéciales concernant certaines matières.

The insurance statutes then bind documents to "les langues officielles du Grand-Duché"
without enumerating them:

- **loi du 27 juillet 1997 sur le contrat d'assurance, art. 16, point 2**: "Les contrats ne
  sont valables que s'ils sont rédigés dans l'une des langues officielles du Grand-Duché de
  Luxembourg ou dans une langue comprise par le preneur d'assurance."
- **same law, art. 17, point 2**: pre-contractual and in-contract information "doi[t] être
  […] fournie[s] dans une des langues officielles du Grand-Duché de Luxembourg", with a
  derogation to another language understood by the policyholder.
- **same law, art. 17-1** ("Langue de communication"): communications during the contract
  must be in the language the contract was drafted in.
- **LSA art. 295-13 (1) c)**: IDD information is given "dans une langue officielle de l'État
  membre où le risque est situé ou de l'État membre de l'engagement ou dans toute autre
  langue convenue par les parties".

**Measured practice, 2026-08-02.** The statutes permit three languages; the corpus uses two,
plus English off-statute:

| Carrier | Documents observed | Languages |
|---|---|---|
| lalux (LA LUXEMBOURGEOISE) | `D.G._RC_Decennale_Biennale__10-07-2025_{FR,DE}.pdf` | **FR + DE** (both 200; `_EN`, `_LU`, `_PT` all 404) |
| AXA Assurances Luxembourg | `/{fr,de,en}/cgv`, 10 CG PDFs per language, **distinct files per language** | **FR + DE + EN** |
| Foyer Assurances | `/fr/ipid` (30 IPIDs) served via `/{lang}/mydoc/{id}` | **FR only** - `/fr/`, `/de/` and `/en/` return the *same byte-identical PDF* (602 996 bytes for `12530`), with a French title on the German page |
| Hiscox S.A. (Luxembourg) | site | **EN** (`<html lang="en">`) |
| CAA itself | whole site | **FR + EN** only (`Changer de langue: fr / en`) |

Site *interface* languages go wider than documents: lalux and DKV offer `lb` and `pt` UI
variants, but `https://www.lalux.lu/de/infos-outils/documents` and
`https://www.dkv.lu/lb/infos-outils/documents` both 404 and no `lb` contractual document was
found anywhere.

**Verdict.** For the pipeline's `lang` field and `official_languages`:

- **`fr` is the default and the safest single guess.** It is the language of Luxembourg
  legislation (loi de 1984 art. 2), and it is the only language in which every carrier
  sampled publishes.
- **`de` is genuinely a document language**, not just an interface language, and it must be
  detectable: lalux ships true German variants of the same conditions générales, AXA ships a
  separate German CG set.
- **`en` is used for real consumer documents** (AXA's English CG set; the expat/international
  carriers Hiscox Luxembourg and Foyer Global Health; the whole cross-border life segment).
  It is not an official language of Luxembourg.
- **`lb` (lëtzebuergesch) is the national language but was not found on a single insurance
  document.** Recorded as a measured absence, not as an assumption.

`sources/lu/_country.yml` therefore declares `official_languages: [fr, de, en]`, which is
*not* the constitutional list. The field is consumed by `discover.py`'s `guess_lang()`, which
matches `/xx/`, `-xx.` and `_xx.` in URLs and falls back to the first element; declaring `lb`
would detect nothing and declaring only `[fr, de]` would silently mislabel English documents
as French. The divergence is deliberate and is written into the manifest's comments.

## Compulsory covers

Established from primary texts, fetched 2026-08-02. What is *not* compulsory is as
load-bearing as what is, so both are recorded.

**Compulsory:**

- **Motor third-party liability.** *Loi modifiée du 16 avril 2003 relative à l'assurance
  obligatoire de la responsabilité civile en matière de véhicules automoteurs*, **art. 2,
  point 1**: "Les véhicules ne sont admis à la circulation sur la voie publique […] que si
  la responsabilité civile à laquelle ils peuvent donner lieu est couverte par un contrat
  d'assurance répondant aux dispositions de la présente loi […]". The obligation falls on
  the holder of the registration certificate. Source: CAA coordinated text,
  `Loi_RCVTA_2003-04-16_coord_2024-04-06.pdf`.
  **The scope of "véhicules" was narrowed in 2024 and this matters for the taxonomy.**
  Art. 1er a), as amended by the loi du 29 mars 2024 (transposing directive (UE) 2021/2118),
  now reads: "les véhicules «automoteurs» destinés à circuler sur le sol […] actionnés
  «exclusivement» par une force mécanique sans être liés à une voie ferrée «avec, soit une
  vitesse maximale par construction supérieure à 25 km/h, soit un poids net maximal supérieur
  à 25 kg et une vitesse maximale par construction supérieure à 14 km/h»". A standard
  electric scooter (25 km/h cap, under 25 kg) therefore falls **outside** the Luxembourg
  compulsory motor insurance. This is the opposite of France, where the décret 2019-1082 made
  EDPM into VTAM under `C. assur. art. L. 211-1` and forced a compulsory-RC product into
  existence. **Luxembourg gets no `edpm` branch.**
- **Hunting.** *Loi du 25 mai 2011 relative à la chasse*, **art. 63, point 2** (the annual
  permit is issued on production of "une attestation d'assurance conforme aux dispositions de
  l'article 66") and **art. 66** ("Le contrat d'assurance doit couvrir la responsabilité
  civile du preneur lors de l'exercice de la chasse ou en sa qualité d'organisateur de
  chasse"). Same shape as France's `C. env. art. L. 423-16`.
- **Professional liability of architects and consulting engineers, décennale included.**
  *Loi du 13 décembre 1989 portant organisation des professions d'architecte et
  d'ingénieur-conseil*, **art. 6**: "Les architectes et ingénieurs-conseils visés par la
  présente loi assurent obligatoirement leur responsabilité professionnelle, tant
  contractuelle que délictuelle ou quasi délictuelle, y compris la responsabilité décennale.
  La prédite assurance couvre obligatoirement les architectes et ingénieurs salariés d'une
  personne physique ou morale."
- **Health and work-accident cover, but as social security, not as private insurance.**
  *Code de la sécurité sociale*, Livre I (Assurance maladie-maternité) art. 1er "Assurance
  obligatoire", and Livre II (Assurance accident) art. 85 "Sont assurés obligatoirement dans
  le cadre d'un régime général d'assurance accident : les personnes qui exercent au
  Grand-Duché de Luxembourg contre rémunération une activité professionnelle pour le compte
  d'autrui […]". Administered by the CNS and the AAA, which are not CAA-supervised insurers
  and are not in the register.

**Not compulsory - each checked against the text, not assumed:**

- **Tenant's household insurance.** The *loi modifiée du 21 septembre 2006 sur le bail à
  usage d'habitation* (official consolidated text at `logement.public.lu`,
  `bl-loi-modifiee-du-21-09-2006.pdf`) contains **no insurance obligation for the tenant**.
  The only occurrence of "assurance" in the whole statute is in the colocation-pact article,
  which requires the pact to set out "les modalités de conclusion des contrats
  d'approvisionnement et d'assurance relatifs au bien loué" - a drafting requirement, not an
  obligation to insure. So Luxembourg differs from France (`loi 89-462 art. 7 g)`) and from
  Wallonia/Brussels. Insurance is contractually imposed by landlords, which is a fact about
  leases, not about statute; the branch page should say so in those words.
- **Décennale insurance for contractors.** Luxembourg's decennial *liability* exists -
  **Code civil art. 1792** ("Si l'édifice périt en tout ou en partie par le vice de la
  construction, même par le vice du sol, les architectes, entrepreneurs et autres personnes
  liées au maître de l'ouvrage par un contrat de louage d'ouvrage en sont responsables
  pendant dix ans") and **art. 2270**, which adds the two-year tier ("après dix ans, s'il
  s'agit de gros ouvrages, après deux ans pour les menus ouvrages"), both quoted verbatim
  inside lalux's own conditions générales *RC décennale et biennale* (edition 01.05.2025).
  But **no statute making that insurance compulsory for entrepreneurs was found**, and there
  is **no dommages-ouvrage equivalent**: the only compulsory limb is the architect/engineer
  one above. Luxembourg is therefore a **décennale + biennale** country with a *partial*
  insurance obligation, where France (loi Spinetta 78-12) has a general one on both sides of
  the contract. Recorded as established for architects, **not established** as a general
  obligation - the absence of a statute is weaker evidence than a statute, and it is labelled
  as such.
- **Complementary health.** Optional. The compulsory layer is the CNS.
- **School insurance.** There is no private compulsory school cover, and arguably no need for
  a private product at all: *Code de la sécurité sociale*, Livre II, **art. 91, 1°** places
  "les écoliers, élèves et étudiants admis à l'enseignement précoce, préscolaire, scolaire et
  universitaire, y compris les activités péripréscolaires, périscolaires et
  périuniversitaires" inside a **special public accident-insurance scheme**. France and
  Belgium both sell `scolaire` as a retail product; Luxembourg does not need to. **No
  `scolaire` branch.**

**Not established** (write as gaps, do not infer): the full list of regulated professions
carrying a compulsory RC (only the architect/engineer statute was verified); whether any
compulsory cover attaches to the *autorisation d'établissement*; the legal basis and
supervisor of CMCM.

## Fetch tiers, measured 2026-08-02

Everything in this census was retrieved with Python `urllib`. No Firecrawl, no browser.

| Tier | Hosts | Note |
|---|---|---|
| `plain` | caa.lu (incl. all CSV and PDF), data.legilux.public.lu, logement.public.lu, secu.lu, statistiques.public.lu, foyer.lu, lalux.lu, axa.lu, dkv.lu, cmcm.lu, raiffeisen.lu, europ-assistance.lu, hiscox.lu, onelife.com, wealins.com, sogelife.com, vitislife.com, utmostgroup.com | 200 to plain Python stdlib |
| `plain` | **baloise.lu** | ~~200 to `urllib`, 406 to `curl`~~ — **cette ligne était fausse dans les deux sens, corrigée le 2026-08-03, voir plus bas.** Le discriminant est l'en-tête `Accept`, et il ne s'applique qu'aux pages HTML : le chemin `/dam/` qui sert les documents répond 200 à tout. Les 34 IPID ont été récupérés sans aucune adaptation. |
| client-rendered | foyer.lu `/fr/conditions-generales` and `/fr/ipid` document lists; lalux.lu `/fr/infos-outils/documents`; dkv.lu documents | pages return 200 but list zero `.pdf` hrefs. Foyer's IPIDs *are* reachable without a browser via the `/{lang}/mydoc/{id}` redirect endpoints enumerated from the page markup; lalux's are under `/fileadmin/mediatheque/documents/…` with a `_FR` / `_DE` suffix convention. Both need an enumeration step, not a browser. |
| SPA, unusable as-is | **legilux.public.lu** (Angular; returns a 2 KB shell) | use `data.legilux.public.lu/eli/…/fr/html` instead, which serves the full text as static HTML over plain HTTP. Recorded so the dead end is not re-derived. |
| dead | cardifluxvie.lu (200, 114-byte body), aaa.public.lu (400 to every path tried), guichet.public.lu (404/timeout on every path tried) | not blocked, just not serving; find the content elsewhere |

Sources used for the numbers above, all `plain`:
`https://www.caa.lu/uploads/documents/files/CAA_RA_2025.pdf` (94 pp),
`…/CAA_RA_2025_annexes.pdf` (120 pp),
`…/ChiffresCles_2025.pdf`,
`…/Communique_2026-1.pdf`,
`https://statistiques.public.lu/dam-assets/catalogue-publications/regards/2026/regards-frontaliers-120326-03.pdf`.

## Ingestion shortlist

Ranked by "Luxembourg-facing consumer product, public document library, first-party carrier,
reachable without a browser". This is a *census* judgement, not a discovery pass - none of
these libraries has been enumerated yet.

**Tier 1, the domestic retail core (four carriers, ~all of the retail market):**

1. **foyer** - FOYER ASSURANCES S.A. (branches 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16,
   17, 18) + FOYER VIE S.A. + FOYER-ARAG (17) + Foyer Global Health. 30 IPIDs enumerated on
   `/fr/ipid`, plus a separate `/fr/conditions-generales` library. Documents are **FR only**,
   even from the German site. Product range spans auto, moto, habitation, voyage, animaux,
   loyer impayé, solde restant dû, complémentaire santé, prévoyance, retraite, investissement,
   multirisque pro. Exercises most of the taxonomy in one group.
2. **lalux** - LA LUXEMBOURGEOISE S.A. + LA LUXEMBOURGEOISE-VIE S.A. Retail line:
   easyPROTECT auto / habitation / accident, pack voyage, protection juridique familiale
   intégrale, assurances constructions, santé, easyLIFE (prévoyance, pension, solde restant
   dû, invest, education). Documents under `/fileadmin/mediatheque/documents/…` with a
   **FR/DE** suffix convention - the place to prove the pipeline handles a two-language corpus.
3. **axa-lu** - AXA ASSURANCES LUXEMBOURG + AXA Assurances Vie Luxembourg. `/{fr,de,en}/cgv`
   carries 10 CG PDFs per language as **distinct files**, i.e. a genuine trilingual library.
   **Freshness warning, measured:** the published editions are old - `TeamUp Agricole`
   janvier 2013, `Private Unfallversicherung / VivaZen` mars 2013, `Borea Invest` janvier
   2010, `déplacements & loisirs` octobre 2009, `TeamUp Multirisques Pro` septembre 2015. Rule
   8 applies: capture `edition_date` and do not present these as the current contracts without
   checking whether a newer edition exists off-library.
4. **baloise-lu** - BALOISE ASSURANCES LUXEMBOURG S.A. + BALOISE VIE Luxembourg S.A.
   **INGERE le 2026-08-03 : 34 IPID, robots.txt vide (rien d'interdit), zero conditions
   generales sur 268 documents inventories.** Voir `_meta/discovery/lu/baloise.md`.

**Tier 2, single-line domestic specialists:** dkv (DKV LUXEMBOURG S.A., branch 2 only -
complementary health, distributed through the lalux agency network), foyer-arag (branch 17
only), europ-assistance-lu (branches 16, 18, foreign branch), raiffeisen-vie, cardif-lux-vie.

**Tier 3, expat/English-language:** foyer-global-health, hiscox-lu. Real Luxembourg consumer
products, English documents, distinct from the domestic corpus.

**Out of scope for a consumer wiki, and it is most of the register:** the 207 reinsurance
undertakings; the ~25 non-life carriers that are commercial, marine, credit or fronting
operations (P&I clubs Britannia / Shipowners' / West of England, Convex, CNA, FM, Tokio
Marine, Liberty Mutual, AIG, Aioi Nissay Dowa, Swiss Re International, SES, THAIC, Atradius,
Greenstars BNP Paribas, SG LuCI, Bolton, CGPA, Colombe, Stadhold, Stonefort, Westfield,
Le Sphinx, Camca…); and the ~20 life carriers that are cross-border wealth vehicles
(Cardif Lux Vie, Utmost, Vitis, OneLife, Wealins, Sogelife, Swiss Life Products, La Mondiale
Europartner, Scottish Widows Europe, BPCE Life, CALI Europe, CNP Luxembourg, DB Vita,
Monument, Zurich Eurolife, International Credit Mutuel Life, Generali Luxembourg,
AFI.ESCA Luxembourg, Allianz Life Luxembourg, iptiQ Life…). Their documents are KID/DIC and
notices aimed at French, Italian, Belgian and German savers, sold through private banks. If
they are ever ingested, they are a *French* or *Italian* consumer story documented from
Luxembourg, and the country attribution would need deciding first.

## Open questions

- **Is a mainstream Luxembourg consumer brand carried by a passporting EEA insurer?** The
  French census settled the equivalent question with evidence (Luko / Allianz Direct
  Versicherungs-AG). The 628 + 128 inbound freedom-of-services notifications make the same
  arrangement possible here, and nothing in this pass tested it. Until it is tested, "63
  Luxembourg-authorised direct insurers" is not the number of insurers a Luxembourg consumer
  can buy from.
- **CMCM.** Present in the market, absent from the CAA register, legal basis not established.
  Resolve before writing anything about Luxembourg complementary health.
- **The frontalier question is a scope question, not a data question.** 225 840 people work
  in Luxembourg and are insured for health and work accidents under Luxembourg social
  security while holding French, Belgian or German motor and household contracts. A
  Luxembourg branch page that does not say so will read as if it applied to them.
  Decide, in writing, whether `lu` pages address residents only.
- **The 2-unit gap** between this register read (281 carriers) and the CAA's own
  2025-2026 annual report (283 at 01/07/2026) is unreconciled.
- **`10b*`** and any other sub-branch suffixes in the register's `Branches` column have no
  published legend. Meaning not established.
- **Cross-border life as a country problem.** Over 90 % of what Luxembourg life insurers
  write is sold into other Member States, mostly France. If those products are ever
  documented, they belong under the country whose consumers buy them, not under `lu`.
  Deferred, not decided.

## Corrections (2026-08-02) — deux affirmations de ce recensement démenties par la découverte

Les deux venaient d'une observation faite sur quelques URL, généralisée trop vite. Elles sont
corrigées ici plutôt que réécrites en silence, parce que le raisonnement qui a mené à l'erreur est
lui-même utile.

**1. « `_PT` renvoie 404 » : faux.** Cinq brochures portugaises sont bien en ligne chez lalux. Le
portugais n'est pas une langue officielle du Luxembourg mais c'est la première langue d'une part
importante de la population résidente, et un assureur de détail y publie. Le manifeste garde
`official_languages: [fr, de, en]` — ce champ décrit les langues **des documents contractuels**,
et les cinq documents portugais sont des brochures commerciales, non contractuelles. La nuance est
notée ici pour qu'une prochaine passe ne re-suppose pas leur absence.

**2. « Pas de branche `velo`, faute de produit luxembourgeois observé » : le motif était faux.**
lalux vend bien une *Assurance Vélo LALUX*. La branche n'a pas été créée pour autant, et le
document est classé `autres` : en France, `velo` a été créée parce que la définition du cycle
assuré (assistance ≤ 250 W, coupure à 25 km/h, exclusion des VTAM) divergeait matériellement de
celle d'un EDPM et changeait le caractère obligatoire de la couverture. Un seul produit ne
justifie pas une branche ; c'est la divergence de définition qui l'avait justifiée. La question
reste ouverte et `autres` est l'endroit prévu pour la garder visible.

**Ce que la découverte a confirmé, en revanche :**

- **Aucun document en lëtzebuergesch**, et pour une raison plus intéressante que l'absence : le hub
  `/lu/` de lalux **existe et est complet**, il liste 90 PDF — tous en FR, DE, EN ou PT. La langue
  de l'interface n'est pas celle des documents.
- **Les frontaliers ont bien des produits nommés pour eux**, mais seulement en épargne et retraite :
  *easyLIFE Pension* titre « FRONTALIER ? » / « GRENZGÄNGER? » / « as a cross-border worker » dans
  trois langues, à côté de guides fiscaux et d'accueil. **Rien d'équivalent en auto ni en
  habitation** — exactement la ligne de partage que le census prévoyait, leurs contrats de ce
  côté-là étant étrangers.
- **`_ALL` signifie *allemand*, pas *toutes langues*.** Trois fiches portent `_EN`, `_FR` et `_ALL`
  sans aucun `_DE`. Un piège de nommage qui aurait produit un document trilingue fictif.
- **lalux.lu héberge un troisième assureur agréé**, **DKV Luxembourg** (RCS B 45762), avec ses
  propres IPID et ses propres comptes. Lire le porteur sur la marque l'aurait annexé à lalux.

## Corrections (2026-08-03) — deux affirmations vérifiées contre le texte et rectifiées

Trouvées en rédigeant les fiches de branche, sur consultation de Legilux, et corrigées ici plutôt
que laissées à l'état d'à-peu-près défendable.

**1. L'obligation d'assurance automobile ne pèse pas sur le propriétaire.** Elle pèse sur le
**titulaire du certificat d'immatriculation**, depuis la loi du 21 septembre 2023. La rédaction
initiale de la loi du 16 avril 2003 visait bien le propriétaire, et c'est cette version, la plus
souvent citée, qui avait été reprise ici. La distinction n'est pas académique : elle décide qui est
en infraction quand le détenteur du véhicule n'en est pas le propriétaire — leasing, véhicule de
société, prêt durable.

**2. Il existe bien une assurance accidents privée au Luxembourg.** Ce recensement disait qu'il n'y
avait « pas de branche `accidents-travail` parce que c'est un régime public obligatoire », ce qui
laissait entendre qu'aucun marché privé n'existait. C'est faux : le régime public du Livre II du
Code de la sécurité sociale (art. 85) est la couche **obligatoire**, et des couvertures accidents
privées se vendent au-dessus. La formulation exacte est donc : *pas de branche accidents du travail
**obligatoire** côté privé*, la branche `accidents` de la taxonomie couvrant ce qui se vend.

Les deux corrections viennent d'une vérification en source primaire là où le recensement s'était
appuyé sur la version la plus diffusée d'un texte. C'est le mode de défaillance à surveiller sur ce
genre de fiche : une affirmation qui a été vraie, et qui ne l'est plus.

## Le registre borne la liste de détail par le haut, il ne la donne pas (mesuré 2026-08-03)

Ce recensement affirmait « moins de dix des soixante-trois assureurs directs vendent un
produit à un résident ». L'affirmation tenait, mais elle n'était pas mesurée. Elle l'est
maintenant, et la mesure dit surtout **où le registre cesse d'aider**.

### Côté non-vie, la branche 10 filtre

La branche **10 (RC véhicules terrestres automoteurs)** est le meilleur signal disponible :
l'assurance RC auto est obligatoire pour tout titulaire d'un certificat d'immatriculation
luxembourgeois, et aucun assureur ne la détient par accident.

**Douze des trente-cinq assureurs non-vie luxembourgeois la détiennent** :

| Entité | Aussi 8+9+13 (socle habitation + RC) |
|---|---|
| AIG EUROPE S.A. | oui |
| AIOI NISSAY DOWA INSURANCE COMPANY OF EUROPE SE | oui |
| AXA ASSURANCES LUXEMBOURG | oui |
| BALOISE ASSURANCES LUXEMBOURG S.A. | oui |
| FOYER ASSURANCES S.A. | oui |
| HISCOX S.A. | oui |
| LA LUXEMBOURGEOISE S.A. | oui |
| LIBERTY MUTUAL INSURANCE EUROPE SE | oui |
| SI INSURANCE (EUROPE), SA | oui |
| STADHOLD INSURANCES (LUXEMBOURG) S.A. | non |
| SWISS RE INTERNATIONAL SE | oui |
| TOKIO MARINE EUROPE S.A. | oui |

**Douze est un plafond, pas un décompte.** La branche 10 couvre aussi la RC des flottes
d'entreprise, et plusieurs de ces douze sont des porteurs spécialisés ou grands risques qui
n'ont jamais vendu une auto à un particulier luxembourgeois. L'agrément dit ce qu'une
entreprise **a le droit** d'écrire, jamais ce qu'elle écrit.

Le second filtre confirme que l'agrément ne tranche pas : **vingt-deux des trente-cinq**
détiennent le socle 8+9+13 (incendie, autres dommages aux biens, RC générale), soit presque
les deux tiers du marché non-vie. Un socle « habitation + RC » ne distingue donc rien.

### Côté vie, le registre ne discrimine rien du tout

**Les vingt-huit assureurs vie luxembourgeois détiennent tous la branche I et tous la
branche III.** Vingt-huit sur vingt-huit, dans les deux cas. Le pouvoir séparateur du
registre vie est exactement nul.

C'est cohérent avec ce que dit déjà ce document : la place vie luxembourgeoise est
majoritairement un marché de contrats de placement transfrontaliers en libre prestation de
services, et 5,0 % seulement des primes vie écrites depuis le Luxembourg y sont vendues.
Une entité qui n'assure que des résidents français en unités de compte détient le même
agrément que celle qui vend un solde restant dû à Esch-sur-Alzette.

### Conséquence de méthode

**L'appartenance au marché de détail se décide à la découverte, pas au registre.** Le test
opérant est celui que ce projet applique déjà : l'entreprise publie-t-elle, sur un site
luxembourgeois, une bibliothèque de documents contractuels destinés à un particulier ?
Foyer a été traité ainsi et le résultat — aucune conditions générales en libre accès, zéro ligne
sur huit cents — n'aurait été lisible dans aucun registre.

Le registre reste indispensable pour deux choses, et il faut s'y tenir : **nommer les
entités exactement** (forme juridique comprise) et **savoir combien d'entités portent une
même marque**. Baloise en a deux, AXA en a trois. C'est précisément ce qui rend
`carrier: null` fréquent ici : sur trente et un documents extraits, onze seulement nomment
une entité identifiable, et « Baloise » ou « AXA » seuls ne permettent pas de choisir.

Source : `AssurancesDirectes_AssureursLuxembourgeoisNonVie.csv` et
`AssurancesDirectes_AssureursLuxembourgeoisVie.csv`, lus le 2026-08-03.

## Correction (2026-08-03) — « baloise.lu curl-hostile » était faux dans les deux sens

Le tableau des paliers de récupération portait : « 200 to `urllib`, **406 to `curl`** with the same
User-Agent ». Mesuré aujourd'hui sur `https://www.baloise.lu/fr.html`, User-Agent identique,
redirections suivies :

| Client | En-tête `Accept` envoyé | Code |
|---|---|---|
| `curl` (défaut) | `*/*` | **200** |
| `curl -H 'Accept:'` | aucun | **406** |
| `curl -H 'Accept: text/html'` | `text/html` | **200** |
| `urllib` (défaut) | aucun | **406** |
| `urllib` + `Accept: */*` | `*/*` | **200** |

**Ce n'est donc pas `curl` qui échoue, c'est l'absence d'en-tête `Accept`** — et `curl` en envoie un
par défaut là où `urllib` n'en envoie aucun. Le palier était nommé d'après le mauvais client, et le
sens du test était inversé.

**Et la portée était fausse aussi.** Le discriminant ne s'applique qu'aux **pages HTML**. Le chemin
`/dam/` qui sert les documents répond 200 dans les quatre combinaisons testées, ce qui est
cohérent avec le fait que les 34 IPID ont été récupérés sans aucune adaptation :
`download.py` envoie déjà `Accept: application/pdf,*/*`.

**Ce que le cas apprend.** L'entrée précédente tirait pourtant la bonne leçon — « a curl 4xx is not
proof of a block » — mais l'appliquait à un diagnostic qu'elle n'avait pas vérifié. Nommer un palier
d'après le **client** qui échoue plutôt que d'après l'**en-tête** qui manque enterre la cause :
« curl-hostile » ne se corrige pas, alors que « exige un en-tête `Accept` » se corrige en une ligne.
Quand deux clients divergent, la question n'est jamais « lequel est bloqué » mais **« quel en-tête
les sépare »**, et la réponse s'obtient en fixant un en-tête à la fois.


## Correction (2026-08-04) — « Foyer ne publie aucune conditions générales » était faux

Ce recensement, et le MOC après lui, ont répété que Foyer ne publie aucune conditions générales,
sur la foi d'un balayage : zéro occurrence de *condition*, *AGB* ou *general terms* sur huit cents
documents énumérés.

Le balayage était juste, la conclusion non. Une seconde passe a lu la page
`https://www.foyer.lu/fr/conditions-generales` au lieu de la compter : **c'est un formulaire**, qui
demande un « Numéro Client » et un « Numéro Contrat » imprimés sur les conditions particulières
reçues par courrier. Son gabarit de résultat, présent dans le HTML, annonce « Conditions Générales
trouvées. Tous les documents […] sont au format PDF ».

**Les conditions générales de Foyer existent donc bien en PDF. Elles sont servies au souscripteur
identifié, contrat par contrat.** Ce n'est pas une absence de document, c'est une politique de
publication — et pour ce dépôt, la conséquence pratique est la même (rien à ingérer), mais la
description était fausse.

**Aucune énumération n'a été tentée sur ce formulaire et aucune ne doit l'être.** Il demande des
identifiants de client réels ; sonder son espace de paramètres reviendrait à deviner des numéros de
contrat de personnes réelles. La règle du dépôt — n'énumérer que ce qui est publié à tous, ne jamais
sonder un espace d'URL — s'applique ici dans sa forme la plus stricte.

**La leçon de méthode :** compter les occurrences d'un mot dans une bibliothèque dit ce que la
bibliothèque contient, jamais pourquoi. « Zéro résultat » a deux causes — le document n'existe pas,
ou il n'est pas là où on cherche — et seules les deux se distinguent en lisant la page, pas en la
comptant.

## Correction (2026-08-04) — FOYER-ARAG n'est pas le seul détenteur de la branche 17

Une note de ce dépôt disait « le registre montre FOYER-ARAG détenant la seule branche 17 », au sens
de *ne détenant que* la branche 17. La phrase a été relue comme « le seul détenteur de la branche
17 » et propagée ainsi dans un brief de découverte.

Mesuré sur le CSV du CAA : **vingt et un des trente-cinq** assureurs non-vie luxembourgeois
détiennent la branche 17, **dont FOYER ASSURANCES elle-même**.

Ce qui est vrai, et qui était le sens d'origine : FOYER-ARAG est l'un des **trois seuls assureurs
mono-branche** du registre, avec BOLTON INTERNATIONAL (16) et DKV LUXEMBOURG (2).
