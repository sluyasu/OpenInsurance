# allianz — Allianz France

website: allianz.fr
fetch: plain-urllib-only
status: enum
lang: fr
enumerated: 2026-08-01

**73 documents enumerated, including 10 conditions générales. All 73 are disallowed by
`www.allianz.fr/robots.txt`. None ingested.**

Checked mechanically, every URL against the live `robots.txt`: 73 of 73 refused. As at
[AXA](axa.md), this is not a technical obstacle — the host answers 200 to `urllib` (and 403 to
`curl`, the measured trap of this market) and every document was verified as a live PDF. Allianz
asks crawlers not to take them, and this repository is public. `download.py` now enforces the rule
for every insurer, so the decision cannot be quietly reversed.

That makes **five insurers in this batch blocked at the fetch layer** — AXA, Allianz, MMA, ACM,
Abeille — against three ingested. On a market of 628 authorised carriers that is not a
representative sample of anything yet, but it is a real feature of the French landscape and worth
recording as such rather than as a run of bad luck.

## What Allianz publishes

**59 IPIDs, 10 conditions générales, 4 product sheets.** The same shape as most of this market:
Allianz publishes what the DDA obliges it to publish, and wordings only patchily.

## The two entities that must not be merged

This matters beyond Allianz itself, because this dataset already holds documents from both:

- **Allianz IARD** — French carrier, ACPR-supervised. It carries **Acheel's** motor line, and
  Acheel's documents in this dataset name it.
- **Allianz Direct Versicherungs-AG (succursale France)** — a **German, BaFin-supervised** company
  present in the ACPR register only as a `Passeport entrant LE`. It is the carrier behind
  **[Luko](luko.md)**.

Two different companies, two different supervisors, one brand family. A reader who conflates them
would be wrong about who regulates their policy and under which country's law it sits. Any later
pass on Allianz must keep them apart, and must not attribute Luko's paper to Allianz IARD.

## Status of the enumeration itself

The enumerating agent was killed mid-run by the same infrastructure fault that took roughly a dozen
agents that day, but it had written `result.json` first — the discovery spec's write-early rule,
added earlier the same session after two insurers each lost two agents that held everything in
memory. So the count above is what it had confirmed at that point, not necessarily the whole
library: it was still finding current editions when it died. Treat 73 as a floor.

No personal data was encountered.
