# direct-assurance — Direct Assurance (marque d'Avanssur, FR)
website: direct-assurance.fr
library: https://www.direct-assurance.fr/nos-assurances/conditions-generales-particulieres
fetch: plain            # listing page 200; PDFs on directassurance.cdn.prismic.io, no WAF
status: enum
lang: fr
enumerated: 2026-07-30

## Not a carrier, and not one carrier either

Direct Assurance is **absent from the ACPR register**. It is a brand of **Avanssur SA**,
which the documents describe as `mandataire d'assurance d'AXA France IARD et courtier
d'assurance - Orias n° 19006337`, wholly owned by AXA. Avanssur is itself absent from the
carrier register, as an intermediary should be.

The library is kept under the brand slug `direct-assurance`, following the Belgian `lar`
precedent (keep the brand, record the carrier). The carrier is recorded **per document**,
because it is not constant across the library. Three distinct AXA entities sign these
eleven documents, and all three are in the ACPR register:

| Product line | Carrier named in the document |
|---|---|
| Auto, Auto connectée, Habitation | AXA France IARD |
| Moto (conditions générales) | AXA Assurances IARD Mutuelle |
| Santé | AXA France Vie |

The moto IPID names AXA France IARD while its conditions générales name AXA Assurances
IARD Mutuelle; both are recorded as found rather than reconciled.

Santé is a **contrat d'assurance de groupe à adhésion facultative**, concluded between AXA
France Vie and the Association Conseil Branche Santé (ACBS). That is why its master
document is a *notice d'information* and not conditions générales; it is mapped to
`conditions_generales` because it plays that role for the member.

## Site labels vs documents

Same pattern as Thélem, so treat it as a French-market default rather than one insurer's
sloppiness: **the library page's link text and the document's own heading diverge.**

- The link reads *Conditions générales Auto et Auto connectée*. The document is headed
  **Contrat Auto** and contains **zero** occurrences of `connectée`, `télématique` or
  `boîtier`. The connected offer lives entirely in its own conditions particulières
  (`CPYD_04.26`), which the document itself frames as riding on the base contract:
  on deactivation *"Votre contrat d'assurance basculera sur l'offre auto standard"*.
  So the CP is an extension (`is_extension: true`), not a standalone product.
- The moto IPID never names *Direct Assurance* anywhere in its text; it names only
  AXA France IARD. Its attribution to this brand comes from the library page, not from
  the document, and is recorded as such.
- The CP is edition `04.26` while the IPID it pairs with says *"Cet IPID appartient aux CG
  02/2026"*. The connected-offer paperwork is a later edition than the base contract.

## Why this insurer matters for the corpus

Unlike Thélem, Direct Assurance publishes **real conditions générales**: 57, 50 and 80
pages. Three of them exceed `extract.MAX_TEXT_CHARS` (240 000) and will be truncated with
a note in `gaps`, by design and not by fault:

| Document | Pages | Characters |
|---|---|---|
| Auto et Auto connectée (conditions_generales) | 57 | 256 294 |
| Contrat Habitation (conditions_generales) | 50 | 242 744 |
| Ma Moto  Mon Cyclo (conditions_generales) | 80 | 260 979 |

## Documents

| product_name | doc_type | branch | edition | carrier | pages | lang | url |
|---|---|---|---|---|---|---|---|
| Auto et Auto connectée | conditions_generales | auto | 2026-02 | AXA France IARD | 57 | fr | https://directassurance.cdn.prismic.io/directassurance/aYnw_90YXLCxVnsY_AUTO_02.26_VW_VF.pdf |
| Auto connectée | conditions_particulieres | auto | 2026-04 | AXA France IARD | 9 | fr | https://directassurance.cdn.prismic.io/directassurance/afNVWsBOoF08xf0r_CPYD_04.26.pdf |
| Assurance Automobile | ipid | auto | 2026-02 | AXA France IARD | 3 | fr | https://directassurance.cdn.prismic.io/directassurance/aYnxBN0YXLCxVnsa_fiche-ipid-auto-022026.pdf |
| Contrat Habitation | conditions_generales | habitation | 2026-03 | AXA France IARD | 50 | fr | https://directassurance.cdn.prismic.io/directassurance/abglZ7bci2UF6D7w_HABITATION_MRH_03.26_Vdef.pdf |
| Assurance Habitation | ipid | habitation |  | AXA France IARD | 2 | fr | https://directassurance.cdn.prismic.io/directassurance/aHDKPEMqNJQqHyOg_IPID_HABITATION.pdf |
| Ma Moto, Mon Cyclo | conditions_generales | moto | 2024-03 | AXA Assurances IARD Mutuelle | 80 | fr | https://directassurance.cdn.prismic.io/directassurance/aG-PfkMqNJQqHv6Q_CG-Ma-Moto-Mon-Cyclo-981029-0324.pdf |
| Ma Moto, Mon Cyclo | ipid | moto | 2024-09 | AXA France IARD | 2 | fr | https://directassurance.cdn.prismic.io/directassurance/aG-PekMqNJQqHv6P_DiPAMaMotoMonCyclo-2004493-0924_04.pdf |
| Direct Assurance Santé | conditions_generales | sante |  | AXA France Vie | 47 | fr | https://directassurance.cdn.prismic.io/directassurance/aG-PbkMqNJQqHv6O_DirectAssurance-NoticeinformationSante.pdf |
| Direct Assurance Santé - formules Hospi | ipid | sante |  | AXA France Vie | 2 | fr | https://directassurance.cdn.prismic.io/directassurance/aG-PaUMqNJQqHv6L_fiche-ipid-sante-non-responsable.pdf |
| Direct Assurance Santé - gamme responsable | ipid | sante |  | AXA France Vie | 2 | fr | https://directassurance.cdn.prismic.io/directassurance/aG-PZkMqNJQqHv6K_fiche-ipid-sante-responsable.pdf |
| Direct Assurance Santé - exemples de remboursements | other | sante |  | AXA France Vie | 61 | fr | https://directassurance.cdn.prismic.io/directassurance/aVudaXNYClf9ox-__DirectAssurance-Exemplesderemboursements.pdf |
