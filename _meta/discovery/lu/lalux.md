# lalux — lalux
website: 
library:
fetch: None
status: enum
lang: fr
enumerated: 2026-08-01

**90 usable documents** (86 ipid, 4 conditions_generales) across 13 branches (autres 16, multirisque-professionnelle 15, voyage 13, construction 11, auto 11, rc-professionnelle 6, accidents 6, habitation 3, rc-familiale 3, sante 2, solde-restant-du 2, prevoyance 1, protection-juridique 1).
214 further document(s) found but not ingestable, listed at the bottom.

## Carrier

(first-party carrier)

## What this insurer does not publish

Does lalux publish full conditions generales, or only the IDD information document? — ALMOST ONLY THE IDD DOCUMENT. Exactly 4 of 304 documents are real conditions generales, and all 4 belong to the APROBAT construction/professional range: RC Professionnelle Architectes et Ingenieurs-Conseils (FR 19p + DE 19p, ed. 01-05-2025) and RC Decennale et Biennale (FR 18p + DE 17p, ed. 10-07-2025). For the ENTIRE retail book - auto, habitation, RC familiale, protection juridique, accidents, voyage, and every life product - NO conditions generales are published anywhere on lalux.lu. — The string "conditions generales" occurs in 47 bodies, but in 43 of them it is the IPID boilerplate pointing AWAY from the site: "pour l'integralite des droits et obligations de l'entreprise d'assurances et de l'assure, veuillez consulter les conditions generales et/ou particulieres relatives au produit d'assurance choisi". The CG it names are not on the site. Checked every document >= 8 pages: all are annual reports, SFCR, or tax/newcomer guides, no retail CG hiding among them. The documents hub has no CG section in any of its 5 language trees, and the 435-URL sitemap has zero conditions/bedingungen pages. — {'site_section_slug': 'ipid (identical slug in all 5 UI languages: /fr/.../ipid, /de/.../ipid, /en/.../ipid, /lu/.../ipid, /pt/.../ipid)', 'fr': "Document d'information sur le produit d'assurance", 'de': 'Informationsblatt zum Versicherungsprodukt', 'en': 'Insurance Product Information Document', 'note': 'lalux uses the acronym IPID as its own filing term, in the URL path and in filenames. It does NOT use a local Luxembourgish term. The FR wording is the EU IPID standard wording, not a lalux coinage.'} — Same dividing line as the French market, and lalux falls on the same side as most French insurers: summary only. The difference is WHERE the exception sits - in France the exceptions were usually retail lines from mutual insurers; here the only published CG are B2B construction liability, i.e. the lines sold through brokers to professionals who negotiate on wording.
Is anything aimed at frontaliers (225 840 cross-border workers)? — YES, and it is a deliberate, named, multilingual campaign - but it is confined to the pension/life side, exactly where the brief predicted. — ['easyLIFE Pension brochure exists in 3 languages and addresses them in the headline: FR "FRONTALIER ?", DE "GRENZGAENGER?", EN "Did you know that as a cross-border worker, you can take...". This is the Luxembourg tax-deduction product (art. 111bis LIR) which a non-resident can still claim by opting into Luxembourg taxation.', 'A dedicated expat brochure exists in 3 languages: ASSURANCES_POUR_EXPATS-FR / VERSICHERUNGEN_FUR_EXPATS-DE / INSURANCES_FOR_EXPATS-EN.', 'The tax-advantage brochure exists in 3 languages: GAINS_IMPOT-FR / STEUERVORTEILE-DE / TAX_GAINS-EN.', 'Newcomer guides, 84 pages, FR and EN: guide-nouveaux_arrivants_au_luxembourg-fr-2027 / guide-newcomers_in_luxembourg-en-2027, plus GUIDE_DES_IMPOTS_2026 (116p).', 'The affiliate-exit form names the frontalier countries explicitly: "si vous residez en dehors du Luxembourg et en dehors d\'un pays frontalier (France, Belgique, ...)".', 'The easyLIFE Epargne and easyLIFE Mixte fiches carry a non-resident carve-out: "Les non-residents doivent s\'en referer [a la legislation de leur pays]".'] — Nothing on the motor or home side is aimed at frontaliers - consistent with the fact that a frontalier garages the car and lives at home in FR/BE/DE, so those contracts are written by a foreign insurer. lalux targets frontaliers precisely and only where the Luxembourgish situation follows the person rather than the address: pension, life, tax.
Any document in letzebuergesch? — NO. Confirmed, and confirmed the hard way rather than by assuming. — The /lu/ UI tree is fully built and returns 200 on the hub and all 11 sub-sections (/lu/infoen-tools/dokumenter/...). It lists 90 PDFs. Every one of those 90 is a document already served under another language tree - ZERO are listed only under /lu/ - and their bodies are 33 fr, 27 en, 25 de, 5 pt, with 0 lb. So lalux has a letzebuergesch INTERFACE and no letzebuergesch DOCUMENT. This corroborates the market-wide finding rather than breaking it. — Language was measured on the extracted body text of every PDF, not on the URL suffix.

## Traps (do not re-derive)

1. {'trap': '_ALL suffix does NOT mean "all languages" - it means allemand', 'detail': 'Fiche_info_fin_022026_-_easyLIFE_Epargne_-_ALL.pdf, _easyLIFE_Pension_-_formule_Performance_-_ALL.pdf and _formule_Securite_-_ALL.pdf are pure German (de score 102-118, fr 4-5). In each of those three product families there is an _EN and an _FR but no _DE - the _ALL file IS the German one, labelled with the French abbreviation for "allemand". A pipeline reading _ALL as multilingual, or failing to find _DE and recording German as absent, gets both wrong.'}
2. {'trap': 'Four claim forms are byte-identical across a _FR and a _DE filename', 'detail': 'sha 57950675df22, e45ddf11087e, bc357765ab87, 61753cf1499a. Each is ONE bilingual FR/DE form published twice. Kept once, the twin listed in dropped_duplicates.'}
3. {'trap': 'Filename language suffix contradicts body language on 4 files', 'detail': 'The 3 Declaration-*-FR.pdf claim forms read as German-dominant and Schadenmeldung-Stromschaeden-DE.pdf reads as French-dominant, because they are bilingual forms whose column order differs. Body-text measurement, not the suffix, is what settles lang.'}
4. {'trap': 'Two IPID filenames carry an opaque abbreviation and NO language marker', 'detail': 'ipid_assurance-td.pdf is French and is the Solde Restant Du / mortgage product (TD = temporaire decroissante). ipid_assurance-dec.pdf is French and is lalux-Security, assurance deces a capital constant (DEC = deces). Neither says fr. Both are LALUX Assurances-Vie. Also note the solde-restant-du line publishes only FR (ipid_assurance-td) and EN (ipid_assurance-solde-restant-du_en_version-112018, edition 11/2018) - no German at all, and the EN one is 8 years old.'}
5. {'trap': 'KID duplicates across two naming generations', 'detail': 'The capital-differe KIDs exist twice under two schemes (KID_Assurance_de_capital_differe_..._FR_prime_unique.pdf vs kid_Capital_Differe_fin_CapitalDiffereAR_fr_102024.pdf) and are byte-identical in 4 cases. Deduped by sha256; the remaining ones differ and were kept.'}
6. {'trap': 'The /lu/ and /pt/ hubs return 200 and are NOT evidence of documents in those languages', 'detail': '/lu/ lists 90 files, all of them FR/DE/EN/PT. /pt/ returns 200 on all 11 sections but yields only 5 real PT files. Status codes on the hub say nothing about document language.'}
7. {'trap': 'One transient network failure masqueraded as a missing document', 'detail': 'IPID_BUSINESS_TRAVEL_fr.pdf errored on first fetch while _de and _en returned 200, which reads exactly like a missing French variant. Forced refetch returned 200, 347602 bytes. Re-verify before recording any language as absent.'}
8. {'trap': 'One dead link and one text-free PDF', 'detail': "404: /fileadmin/mediatheque/documents/Divers/RCP/20200220-RCP-fiche-contact-vierge.pdf (still linked from the divers shelf). Text-free (3 chars extracted, likely a scan): /fileadmin/mediatheque/documents/Divers/convention-droit-a-l-oubli-29102019.pdf - the droit a l'oubli convention, which would otherwise be an interesting health-underwriting document."}

## Dropped duplicates

- `Schadenmeldung-KFZ-Unfall-DE.pdf` = `?` — byte-identical body served under a second filename
- `Schadenmeldung-Sachversicherung-DE.pdf` = `?` — byte-identical body served under a second filename
- `Schadenmeldung-Stromschaeden-DE.pdf` = `?` — byte-identical body served under a second filename
- `Schadenmeldung-Haftpflicht-Rechtschutz-DE.pdf` = `?` — byte-identical body served under a second filename
- `kid_Capital_Differe_fin_CapitalDiffereAR_de_102024.pdf` = `?` — byte-identical body served under a second filename
- `kid_Capital_Differe_fin_CapitalDiffereAR_en_102024.pdf` = `?` — byte-identical body served under a second filename
- `kid_Capital_Differe_fin_CapitalDiffereAR_fr_102024.pdf` = `?` — byte-identical body served under a second filename
- `kid_Capital_Differe_fin_CapitalDiffereSR_en_102024.pdf` = `?` — byte-identical body served under a second filename

## Documents

| product_name | doc_type | branch | edition | carrier | pp | url |
|---|---|---|---|---|---|---|
| (689.5kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-accident-entreprise_en.pdf |
| (691.44kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-accident_lalux_easyprotect-accident_en.pdf |
| (691.45kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-accident-entreprise_fr.pdf |
| (692.75kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-accident-entreprise_de.pdf |
| (693.94kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-accident_lalux_easyprotect-accident_fr.pdf |
| (694.73kB) | ipid | accidents |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-accident_lalux_easyprotect-accident_de.pdf |
| (689.33kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect-auto_vehicules-type-2_en.pdf |
| (691.91kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect-auto_vehicules-type-1_en.pdf |
| (692.28kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_easyprotect-pro-auto_vehicules-type-2_en.pdf |
| (692.57kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_easyprotect-pro-auto_vehicules-type-1_en.pdf |
| (692.96kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect_auto_vehicules-type-2_fr.pdf |
| (693.05kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect-auto_vehicules-type-2_de.pdf |
| (694.56kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_easyprotect-pro-auto_vehicules-type-2-fr.pdf |
| (694.92kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_easyprotect-pro-auto_vehicules-type-1-fr.pdf |
| (695.24kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_easyprotect-pro-auto_vehicules-type-2_de.pdf |
| (695.38kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect-auto_vehicules-type-1_de.pdf |
| (696.38kB) | ipid | auto |  | LA LUXEMBOURGEOISE S.A. | 3 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-auto_lalux_easyprotect_auto_vehicules-type-1_fr.pdf |
| (312.17kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_assurance_lineheart_tous_risques_fr.pdf |
| (312.81kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_assurance_orange_tous_risques_fr.pdf |
| (313.82kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_assurance_lineheart_tous_risques_de.pdf |
| (314.91kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_assurance_orange_tous_risques_de.pdf |
| (619.77kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_CLASSIC_EN.pdf |
| (621.21kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_CLASSIC_FR.pdf |
| (621.64kB) | ipid | autres |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_CLASSIC_DE.pdf |
| (622.31kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_INFINITE_EN.pdf |
| (622.34kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_PREMIER_EN.pdf |
| (622kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_BUSINESS_EN.pdf |
| (623.76kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_BUSINESS_FR.pdf |
| (623.98kB) | ipid | autres |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_BUSINESS_DE.pdf |
| (624.19kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_PREMIER_FR.pdf |
| (624.39kB) | ipid | autres |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_INFINITE_FR.pdf |
| (624.53kB) | ipid | autres |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_PREMIER_DE.pdf |
| (624.58kB) | ipid | autres |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_VISA_INFINITE_DE.pdf |
| (274.76kB) | conditions_generales | construction |  | LA LUXEMBOURGEOISE S.A. | 17 | https://www.lalux.lu/fileadmin/mediatheque/documents/Divers/Aprobat/D.G._RC_Decennale_Biennale__10-07-2025_DE.pdf |
| (646.21kB) | conditions_generales | construction |  | LA LUXEMBOURGEOISE S.A. | 18 | https://www.lalux.lu/fileadmin/mediatheque/documents/Divers/Aprobat/D.G._RC_Decennale_Biennale__10-07-2025_FR.pdf |
| (688.06kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-1_en.pdf |
| (688.34kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-2_en.pdf |
| (689.12kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_rc-decennale_en.pdf |
| (689.85kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-2_fr.pdf |
| (690.08kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-1_fr.pdf |
| (690.83kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-1_de.pdf |
| (691.05kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_tous-risques-chantier_section-2_de.pdf |
| (691.53kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_rc-decennale_fr.pdf |
| (692.52kB) | ipid | construction |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_aprobat_rc-decennale_de.pdf |
| (692.83kB) | ipid | habitation |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/IPID_Assurance_Habitation_LALUX_easyPROTECT-Habitation_2023_FR.pdf |
| (694.13kB) | ipid | habitation |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/IPID_Assurance_Habitation_LALUX_easyPROTECT-Habitation_2023_EN.pdf |
| (697.09kB) | ipid | habitation |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/IPID_Assurance_Habitation_LALUX_easyPROTECT-Habitation_2023_DE.pdf |
| (689.3kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_discover_lalux_easyprotect_en.pdf |
| (692.01kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_discover_lalux_easyprotect.pdf |
| (692.49kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-responsabilite-civile_en.pdf |
| (693.04kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_discover_lalux_easyprotect_de.pdf |
| (693.23kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-choses_en.pdf |
| (694.72kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-responsabilite-civile_fr.pdf |
| (695.74kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-choses_fr.pdf |
| (696.17kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-responsabilite-civile_de.pdf |
| (696.48kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_lalux_easyprotect-pro-entreprise-assurance-de-choses_de.pdf |
| (704.06kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_services-a-la-personne_lalux_easyprotect_en.pdf |
| (706.18kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_tous-risques-relative-aux-biens_lalux_fr.pdf |
| (707.71kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_services-a-la-personne_lalux_easyprotect_fr.pdf |
| (707.85kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_services-a-la-personne_lalux_easyprotect_de.pdf |
| (720.16kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_tous-risques-relative-aux-biens_lalux_en.pdf |
| (723.49kB) | ipid | multirisque-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_tous-risques-relative-aux-biens_lalux_de.pdf |
| IPID lalux-Security Assurance décès (268.62kB) | ipid | prevoyance |  | LA LUXEMBOURGEOISE-VIE S.A. | 1 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-dec.pdf |
| IPID Protection juridique (687.06kB) | ipid | protection-juridique |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance_protection_juridique_fr.pdf |
| (688.72kB) | ipid | rc-familiale |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_rc-familiale-immeuble-et-chasse_lalux_easyprotect_en.pdf |
| (691.97kB) | ipid | rc-familiale |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_rc-familiale-immeuble-et-chasse_lalux_easyprotect_fr.pdf |
| (692.55kB) | ipid | rc-familiale |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_rc-familiale-immeuble-et-chasse_lalux_easyprotect_de.pdf |
| (325.55kB) | conditions_generales | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 19 | https://www.lalux.lu/fileadmin/mediatheque/documents/Divers/Aprobat/D.G._RC_Architectes-Ingenieur_01-05-2025_DE.pdf |
| (677.2kB) | conditions_generales | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 19 | https://www.lalux.lu/fileadmin/mediatheque/documents/Divers/Aprobat/D.G._RC_Architectes-Ingenieur_01-05-2025_FR__version_definitive_.pdf |
| (691.33kB) | ipid | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-aprobat-rcpro-architectes-ingenieurs-en.pdf |
| (692.53kB) | ipid | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-aprobat-rcpro-architectes-ingenieurs-fr.pdf |
| (693.9kB) | ipid | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-aprobat-rcpro-architectes-ingenieurs-de.pdf |
| (714.21kB) | ipid | rc-professionnelle |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-aprobat-rc-professionnelle-des-agents-immobiliers-adm-de-biens-et-syndics-de-copropriete-fr.pdf |
| (324.98kB) | ipid | sante |  | DKV LUXEMBOURG S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/DKV/documents/IPID/IPID_BUSINESS_TRAVEL_de.pdf |
| (338.01kB) | ipid | sante |  | DKV LUXEMBOURG S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/DKV/documents/IPID/IPID_BUSINESS_TRAVEL_en.pdf |
| (268.03kB) | ipid | solde-restant-du |  | LA LUXEMBOURGEOISE-VIE S.A. | 1 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-td.pdf |
| (586.43kB) | ipid | solde-restant-du |  | LA LUXEMBOURGEOISE-VIE S.A. | 1 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_assurance-solde-restant-du_en_version-112018.pdf |
| (307.07kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_luxair_tours_assistance_et_annulation_retard_fr.pdf |
| (309.16kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_luxair_tours_assistance_et_annulation_et_retard_de.pdf |
| (622.88kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_EN.pdf |
| (623.78kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_BUSINESS_EN.pdf |
| (624.81kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_FR.pdf |
| (624.95kB) | ipid | voyage |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_DE.pdf |
| (625.02kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_BUSINESS_FR.pdf |
| (625.09kB) | ipid | voyage |  |  | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/IPID_SPUERKEESS_Cartes_de_credit_Assistance_et_Hors_assistance_MILES_MORE_LUXAIR_VISA_BUSINESS_DE.pdf |
| (691.25kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_bureaux_de_voyages__remanie__-_formule_1_et_2_fr.pdf |
| (691.72kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid-partenaires/ipid_bureaux_de_voyages__remanie__-_formule_1_et_2_-de.pdf |
| (704.66kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_vacances-sans-soucis_lalux_en.pdf |
| (707.36kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_vacances-sans-soucis_lalux_fr.pdf |
| (707.81kB) | ipid | voyage |  | LA LUXEMBOURGEOISE S.A. | 2 | https://www.lalux.lu/fileadmin/mediatheque/documents/compliance/ipid/ipid_vacances-sans-soucis_lalux_de.pdf |

## Found but not ingestable

| file | why |
|---|---|
| easyPROTECT-PT.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_ACCIDENT-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_ACCIDENT-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_ACIDENTE-PT.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_UNFALL-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Invest_for_Future-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Mixed-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Mixed-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_AUTO-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_AUTO-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_AUTO-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_AUTO-PT.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PRO-FR.pdf | document_type 'brochure' not a schema enum |
| ASSURANCES_POUR_EXPATS-FR.pdf | document_type 'brochure' not a schema enum |
| Assurance_velo_-FR-DE-EN.pdf | document_type 'brochure' not a schema enum |
| GAINS_IMPOT-FR.pdf | document_type 'brochure' not a schema enum |
| INSURANCES_FOR_EXPATS-EN.pdf | document_type 'brochure' not a schema enum |
| STEUERVORTEILE-DE.pdf | document_type 'brochure' not a schema enum |
| TAX_GAINS-EN.pdf | document_type 'brochure' not a schema enum |
| VERSICHERUNGEN_FUR_EXPATS-DE.pdf | document_type 'brochure' not a schema enum |
| APROBAT_Constructions-EN.pdf | document_type 'brochure' not a schema enum |
| APROBAT_Constructions-FR.pdf | document_type 'brochure' not a schema enum |
| APROBAT_Versicherungen_BAUEN-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HABITACAO-PT.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HABITATION-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HABITATION_mobilier-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HAUS_UND_WOHNUNG-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HAUS_UND_WOHNUNG_Hausrat-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HOME-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_HOME_furniture-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PACK_VOYAGE-FR.pdf | document_type 'brochure' not a schema enum |
| DISCOVER_DE_2023.pdf | document_type 'brochure' not a schema enum |
| DISCOVER_EN_2023.pdf | document_type 'brochure' not a schema enum |
| DISCOVER_FR_2023.pdf | document_type 'brochure' not a schema enum |
| easyPRO-Cyber-DE.pdf | document_type 'brochure' not a schema enum |
| easyPRO-Cyber-EN.pdf | document_type 'brochure' not a schema enum |
| easyPRO-Cyber-FR.pdf | document_type 'brochure' not a schema enum |
| easyPRO-Cyber-PT.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PRO-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PRO-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Education-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Education-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Education-FR.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_FORESIGHT-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Mixte-FR.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_PREVOYANCE-FR.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Study_Cover-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Study_Cover-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Study_Cover-FR.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_VORSORGE-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_LEGAL_PROTECTION-EN.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PROTECTION_JURIDIQUE-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_RECHTSSCHUTZ-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Pension-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Pension-EN.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Pension-FR.pdf | document_type 'brochure' not a schema enum |
| lalux-Safe_Future-DE.pdf | document_type 'brochure' not a schema enum |
| lalux-Safe_Future-EN.pdf | document_type 'brochure' not a schema enum |
| lalux-Safe_Future-FR.pdf | document_type 'brochure' not a schema enum |
| lalux-Staff_Protect_-_DE.pdf | document_type 'brochure' not a schema enum |
| lalux-Staff_Protect_-_EN.pdf | document_type 'brochure' not a schema enum |
| lalux-Staff_Protect_-_FR.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Invest_for_Future-DE.pdf | document_type 'brochure' not a schema enum |
| easyLIFE_Invest_for_Future-FR.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_PACK_REISE-DE.pdf | document_type 'brochure' not a schema enum |
| easyPROTECT_TRAVEL_PACK-EN.pdf | document_type 'brochure' not a schema enum |
| 33_2481_Declar_SIn_Voy_2023_FR.pdf | branch None not in the fr taxonomy |
| 33_2789_Declar_SIn_Voy_2023_DE.pdf | branch None not in the fr taxonomy |
| 33_2790_Declar_SIn_Voy_2023_EN.pdf | branch None not in the fr taxonomy |
| Declaration-accident-automobile-FR.pdf | branch None not in the fr taxonomy |
| Declaration-de-sinistre-assurances-de-choses-FR.pdf | branch None not in the fr taxonomy |
| Declaration-de-sinistre-dommages-electriques-FR.pdf | branch None not in the fr taxonomy |
| Declaration-de-sinistre-responsabilite-civile-protection-juridique-FR.pdf | branch None not in the fr taxonomy |
| Politique_d_investissement_responsable_042024.pdf | branch None not in the fr taxonomy |
| Charte_fournisseurs_et_achats_responsable_de_LALUX.pdf | branch None not in the fr taxonomy |
| Informations-ESG-SFDR-easyLIFE-Invest-for-Future.pdf | branch None not in the fr taxonomy |
| Informations-ESG-SFDR-precontractuelles-easyLIFE-Invest-for-Future-Support-a-capital-protege.pdf | branch None not in the fr taxonomy |
| Informations-ESG-SFDR-rapport-periodique-easyLIFE-Invest-for-Future-Support-a-capital-protege.pdf | branch None not in the fr taxonomy |
| Politique_d_investissement_responsable.pdf | branch None not in the fr taxonomy |
| Politique_de_remuneration_short_version.pdf | branch None not in the fr taxonomy |
| Politique_en_matiere_de_Risques_de_Durabilite_-_Finale.pdf | branch None not in the fr taxonomy |
| Fiche_info_fin_022026_-_easyLIFE_Epargne_-_ALL.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Epargne_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Epargne_-_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Mixte_-_DE.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Mixte_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Mixte_-_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLife_Education_-_DE.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLife_Education_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLife_Education_-_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Performance_-_ALL.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Performance_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Performance_-_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Securite_-_ALL.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Securite_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_022026_-_easyLIFE_Pension_-_formule_Securite_-_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_032026_-_lalux-Safe_Future_volet_retraite_-_DE.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_032026_-_lalux-Safe_Future_volet_retraite_-_EN.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Fiche_info_fin_032026_-_lalux-Safe_Future_volet_retraite_FR.pdf | document_type 'fiche_information_financiere' not a schema enum |
| Comment_importer_sa_voiture_au_Luxembourg.pdf | branch None not in the fr taxonomy |
| How_do_you_import_your_car_to_Luxembourg.pdf | branch None not in the fr taxonomy |
| Wie_ueberfuehren_Sie_Ihr_Auto_nach_Luxemburg.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Inondation_DE.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Inondation_EN.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Inondation_FR.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Meteo_extreme_DE.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Meteo_extreme_EN.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Meteo_extreme_FR.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Vol_DE.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Vol_EN.pdf | branch None not in the fr taxonomy |
| Guide_Prevention_Vol_FR.pdf | branch None not in the fr taxonomy |
| GUIDE_DES_IMPOTS_2026.pdf | branch None not in the fr taxonomy |
| guide-newcomers_in_luxembourg-en-2027.pdf | branch None not in the fr taxonomy |
| guide-nouveaux_arrivants_au_luxembourg-fr-2027.pdf | branch None not in the fr taxonomy |
| KID_Assurance_de_capital_differe_avec_contre-assurance_des_primes_DE_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_Assurance_de_capital_differe_avec_contre-assurance_des_primes_EN_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_Assurance_de_capital_differe_avec_contre-assurance_des_primes_FR_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_Assurance_de_capital_differe_sans_contre-assurance_des_primes_DE.pdf | document_type 'kid_priips' not a schema enum |
| KID_Assurance_de_capital_differe_sans_contre-assurance_des_primes_EN.pdf | document_type 'kid_priips' not a schema enum |
| KID_Assurance_de_capital_differe_sans_contre-assurance_des_primes_FR.pdf | document_type 'kid_priips' not a schema enum |
| KID_lalux-Life___easy_LIFE_Mixte_formule_Securite_DE_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_lalux-Life___easy_LIFE_Mixte_formule_Securite_EN_prime_unique_01.pdf | document_type 'kid_priips' not a schema enum |
| kid_Capital_Differe_fin_CapitalDiffereSR_de_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_Capital_Differe_fin_CapitalDiffereSR_fr_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_InvestForFuture_fin_EasyLifeInvest_de_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_InvestForFuture_fin_EasyLifeInvest_en_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_InvestForFuture_fin_EasyLifeInvest_fr_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Mixte_fin_AssuranceMixte_de_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Mixte_fin_AssuranceMixte_en_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Mixte_fin_AssuranceMixte_fr_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easylife_mixte_pu_fr_2025.pdf | document_type 'kid_priips' not a schema enum |
| KID_lalux-Education_DE_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_lalux-Education_EN_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| KID_lalux-Education_FR_prime_unique.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Education_fin_TermeFixe_en_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Education_fin_TermeFixe_fr_102024.pdf | document_type 'kid_priips' not a schema enum |
| kid_easyLIFE_Eductaion_fin_TermeFixe_de_102024.pdf | document_type 'kid_priips' not a schema enum |
| Formulaire-KYC-AML_DE.pdf | branch None not in the fr taxonomy |
| Formulaire-KYC-AML_EN.pdf | branch None not in the fr taxonomy |
| Formulaire-KYC-AML_FR.pdf | branch None not in the fr taxonomy |
| formulaire-auto-certification-fiscale-fatca-crs-personne-morale.pdf | branch None not in the fr taxonomy |
| formulaire-declaration-identite-personnes-morales.pdf | branch None not in the fr taxonomy |
| Formulaire_d_identification_d_une_personne_morale_2024_DE.pdf | branch None not in the fr taxonomy |
| Formulaire_d_identification_d_une_personne_morale_2024_EN.pdf | branch None not in the fr taxonomy |
| Formulaire_d_identification_d_une_personne_morale_2024_FR.pdf | branch None not in the fr taxonomy |
| Formulaire_de_sortie_affilie_nouv_2024_DE_EXTENDED.pdf | branch None not in the fr taxonomy |
| Formulaire_de_sortie_affilie_nouv_2024_EN_EXTENDED.pdf | branch None not in the fr taxonomy |
| Formulaire_de_sortie_affilie_nouv_2024_FR_EXTENDED.pdf | branch None not in the fr taxonomy |
| choix-inv-2020-en.pdf | branch None not in the fr taxonomy |
| choix-inv-2020-fr.pdf | branch None not in the fr taxonomy |
| cotpers-choix-affilie-de-2011-annuel.pdf | branch None not in the fr taxonomy |
| cotpers-choix-affilie-de-2011.pdf | branch None not in the fr taxonomy |
| cotpers-choix-affilie-en-2011-annuel.pdf | branch None not in the fr taxonomy |
| cotpers-choix-affilie-en-2011.pdf | branch None not in the fr taxonomy |
| cotpers-choix-affilie-fr-2011.pdf | branch None not in the fr taxonomy |
| convention-droit-a-l-oubli-29102019.pdf | branch None not in the fr taxonomy |
| llv-criteres-segmentation-2020_01.pdf | branch None not in the fr taxonomy |
| De__claration_RGPD_clients_LALUX_-_V_Finale_2023_DE.pdf | branch None not in the fr taxonomy |
| De__claration_RGPD_clients_LALUX_-_V_Finale_2023_EN.pdf | branch None not in the fr taxonomy |
| De__claration_RGPD_clients_LALUX_-_V_Finale_2023_FR.pdf | branch None not in the fr taxonomy |
| Notice_d_information_RGPD_lanceurs_d_alertes.pdf | branch None not in the fr taxonomy |
| assurance-vie-groupe-fiche-information-sur-la-protection-des-donnees.pdf | branch None not in the fr taxonomy |
| lebensgruppenversicherung-informationsblatt-zum-datenschutz.pdf | branch None not in the fr taxonomy |
| life-group-insurance-information-sheet-on-data-protection.pdf | branch None not in the fr taxonomy |
| RSSF_Group_final.pdf | branch None not in the fr taxonomy |
| RSSF_LALUX_Group_2021.pdf | branch None not in the fr taxonomy |
| RSSF_LALUX_Group_2022.pdf | branch None not in the fr taxonomy |
| RSSF_LALUX_Group_2023.pdf | branch None not in the fr taxonomy |
| RSSF_LALUX_Group_2024.pdf | branch None not in the fr taxonomy |
| RSSF_LALUX_Group_2025.pdf | branch None not in the fr taxonomy |
| SFCR_DKVL_2025.pdf | branch None not in the fr taxonomy |
| SFCR_LLGRE_2025.pdf | branch None not in the fr taxonomy |
| SFCR_LLN_2025.pdf | branch None not in the fr taxonomy |
| SFCR_LLV_2025.pdf | branch None not in the fr taxonomy |
| rssf-dkv-2016.pdf | branch None not in the fr taxonomy |
| rssf-llg-2017.pdf | branch None not in the fr taxonomy |
| rssf-llg-2018.pdf | branch None not in the fr taxonomy |
| rssf-llg-unique-2019.pdf | branch None not in the fr taxonomy |
| rssf-lln-2016.pdf | branch None not in the fr taxonomy |
| rssf-lln-2017.pdf | branch None not in the fr taxonomy |
| rssf-lln-2018.pdf | branch None not in the fr taxonomy |
| rssf-llv-2016.pdf | branch None not in the fr taxonomy |
| rssf-llv-2017.pdf | branch None not in the fr taxonomy |
| rssf-llv-2018.pdf | branch None not in the fr taxonomy |
| RA2025_LLGR_CONSO.pdf | branch None not in the fr taxonomy |
| Rapport-annuel-llv-2015.pdf | branch None not in the fr taxonomy |
| Rapport_Annuel_Groupe_LALUX_2022.pdf | branch None not in the fr taxonomy |
| Rapport_Annuel_groupe_LALUX_2020.pdf | branch None not in the fr taxonomy |
| jahresabschluss-dkv-2017.pdf | branch None not in the fr taxonomy |
| rapport-annuel-dkv-2018.pdf | branch None not in the fr taxonomy |
| rapport-annuel-groupe-lalux-2019.pdf | branch None not in the fr taxonomy |
| rapport-annuel-groupe-lalux-2021.pdf | branch None not in the fr taxonomy |
| rapport-annuel-groupe-lalux-2023.pdf | branch None not in the fr taxonomy |
| rapport-annuel-groupe-lalux-2024.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lln-2017.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2010.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2011.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2012.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2013.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2014.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2016.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2017.pdf | branch None not in the fr taxonomy |
| rapport-annuel-llv-2018.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2010.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2011.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2012.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2013.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2014.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2015.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2016.pdf | branch None not in the fr taxonomy |
| rapport-annuel-lnv-2018.pdf | branch None not in the fr taxonomy |

## Qualité éditoriale des documents : ce qui a été compté

Cette section énonce des **observations sur les documents**, pas un jugement sur l'assureur. La règle 1
interdit de noter ou de classer ; compter ce qu'on lit ne s'y oppose pas, et un lecteur qui va citer
un IPID a besoin de savoir ce qu'on y a trouvé.

Sur les **16 premiers documents extraits**, chaque constat vérifié au rendu et conservé verbatim :

| Ce qui a été relevé | Documents |
|---|---|
| Fautes imprimées conservées telles quelles | 10 / 16 |
| Contradictions internes, enregistrées sans arbitrage | 6 / 16 |
| **Texte de gabarit destiné au rédacteur, jamais remplacé** | **2 / 16** |
| Garantie nommée dans une rubrique mais absente de la liste des garanties | 1 / 16 |

Le troisième cas est celui qui a une conséquence directe pour un lecteur. Deux IPID de la gamme
**APROBAT en anglais** portent, sous « How do I cancel the contract ? », le texte suivant :

> Decide what to write, as the cancellation terms are different (single premium, etc.)
> E.g. Cancellation is possible within 30 days…

Les trente jours sont donc **un exemple laissé par le rédacteur**, pas une condition du contrat.
`notice_period` reste null sur ces deux documents : promouvoir cet exemple aurait inventé un droit de
résiliation. Les versions françaises des mêmes produits portent, au même endroit, une vraie clause.

Deux remarques qui encadrent ce comptage :

- **Il porte sur 16 documents sur 90.** Ce n'est pas une mesure de la bibliothèque entière, et la
  proportion peut bouger — les seize premiers ont été pris dans l'ordre du listing, pas choisis.
- **Ces défauts sont conservés, jamais réparés.** Une citation doit être une portion exacte du
  document ; corriger « tremble de terre » ou compléter une puce tronquée depuis la version
  allemande rendrait la citation invérifiable et attribuerait au document un texte qu'il ne contient
  pas. Tout est dans `gaps`, document par document.
