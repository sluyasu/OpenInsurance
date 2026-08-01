# mma — MMA

website: mma.fr
library: https://www.mma.fr/documents-ipid.html
fetch: waf
status: enum
lang: fr
enumerated: 2026-08-01

**51 documents enumerated. None ingested — the two routes to them fail for two different reasons,
and one of those reasons is the publisher's own stated wish.**

- The canonical addresses on **`www.mma.fr`** are robots-**allowed** (its `Disallow` lines for
  `/*.pdf$` and `/files/*/documents*` are commented out, and `/documents-ipid.html` is in no rule)
  but the host is behind DataDome and answers **403** to every plain-HTTP client.
- The one host that does serve the bytes, **`static.mma.fr`**, answers `User-agent: * / Disallow: /`.

Both verified directly. So there is no route that is simultaneously reachable and permitted, and no
`sources/fr/mma.yml` is emitted.

The distinction matters and is worth stating, because it is what separates this insurer from
[Macif](macif.md), which *is* ingested. Macif's `robots.txt` is unreadable (403 behind a bot shield),
so its policy is genuinely **unknown**, and RFC 9309 says an unavailable robots.txt lets a crawler
proceed. MMA's asset host states a policy and the policy is no. An unreadable rule and a rule that
says no are not the same thing, and reading the second as "they probably only meant search engines"
would be inferring intent from a mechanical protocol — exactly what this project refuses to do
elsewhere.

**The enumeration itself came through that route**, fetched at 1.3 s intervals before the conflict
was noticed. That is recorded rather than quietly dropped: the counts and structure below are real,
and they are the reason this file exists at all.

## How the library was found, since it is not obvious

The WAF is scoped to **HTML on the two customer-facing hosts**, not to the origin. `robots.txt` and
the sitemaps return 200 on `www.mma.fr` itself, which is how `/documents-ipid.html` was located
(`Sitemap.xml` → `home.sitemap.xml`). `static.mma.fr` then serves the identical Jahia pages and the
identical `/files/…` PDFs to plain `urllib`. No browser, no scraping service, no CAPTCHA, no
URL-space probing.

Worth noting that this is **not** the curl-vs-urllib trap that catches so many French insurers:
urllib across 8 header variants, httpx, and curl on both HTTP/2 and HTTP/1.1, http and https, www
and apex, and a warmed session carrying the `datadome` cookie — all 403.

## What MMA publishes

**41 IPIDs, 2 notices d'information, 8 non-contractual "exemples chiffrés".** No conditions
générales: 30 CG numbers are referenced by the IPIDs and never linked, and `robots.txt` carries
`Disallow: /sites/mmafr/documents-cg` — the one document path the publisher explicitly forbids,
while deliberately un-forbidding the IPID paths. Not fetched, not probed. The message is legible.

## MMA is a counter-example to a pattern this dataset had started to treat as a rule

Elsewhere here, the mutuelle-carried version of a product required **Sociétaire** status and carried
a **cotisations variables** article — a call for additional contribution capped at twice the annual
premium — while the SA-carried version of the same product had neither. That held across five
Matmut contracts and I was propagating it to extraction workers as background knowledge.

**It does not hold at MMA, and the reason is clean.** Both MMA mutuelles are constituted
**`à cotisations fixes`**, printed in the carrier block of every document. Across roughly 470 000
characters there are **zero** occurrences of `cotisations variables`, zero of `sociétaire`, zero of
`rappel de cotisation`, zero of `assemblée générale`.

And MMA runs no SA-version / mutuelle-version split at all: the SA and the mutuelle **co-sign the
same contract** — 33 documents by the IARD pair, 15 by all four entities, never by one alone. There
is one version of each product, so there is nothing to compare.

So the pattern was a Matmut house rule, not a property of French mutual insurers.
[SMACL](smacl.md) independently confirms this: its mutual is also *à cotisations fixes*.

## Smaller findings

- **One document is not MMA-carried.** The Protection Juridique IPID (CG 400) names *Covéa
  Protection Juridique, SA, RCS Le Mans 442 935 227* as sole assureur. Two others (Assurance
  Emprunteur, MMA Sérénité obsèques) are Vie-pair only. **No GMF or MAAF overlap anywhere** —
  Fidelia appears once as an assistance provider, not as a carrier.
- **Ten professional IPIDs all print the bare name "MMA PRO-PME"**, separable only by a small
  conventions-spéciales sub-line. Parallel trade variants, not editions (rule 8).
- Unusually for this market, **every IPID prints its own edition** as `AM nnnn (Version MM/YYYY)`,
  so the edition comes from the document rather than the filename on 50 of 51.

A predecessor agent's leftovers came from a Wayback-CDX harvest plus live HEAD-probing of ~264
paths — the enumeration the discovery spec now forbids. None of it was reused and those URLs are not
recorded. No personal data was encountered.
