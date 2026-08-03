---
type: branch
domain: insurance
country: lu
branch: prevoyance
branch_code: "I"
lang: fr
langs: [fr]
mandatory: false
regulator: "[[CAA]]"
legal_refs: ["[[CAA]]"]
tags: [insurance/lu/prevoyance, branch]
aliases: [Prévoyance, Décès, Temporaire décès, Capital décès, Vorsorge, Risikoleben]
source: null
date: 2026-08-03
freshness: 2026-08-03
status: ready
generated: false
---

## Ce que c'est

La prévoyance couvre les conséquences financières d'une atteinte à la personne — le décès d'abord, et selon
les contrats l'invalidité. Elle verse un capital ou une rente à un bénéficiaire désigné, ou exonère le
preneur du paiement des primes. Elle relève de la **branche I de l'annexe II de la LSA** : « Assurances en
cas de vie, de décès, assurances mixtes, assurances de rentes — autres que l'assurance nuptialité et natalité
— non liées à des fonds d'investissement ainsi que les assurances complémentaires à ces assurances ». C'est
aussi la branche la plus détenue du marché vie luxembourgeois : les **33 lignes vie du registre** du [[CAA]]
la portent toutes.

Elle se distingue de l'[[Assurance vie et épargne]], dont la finalité est patrimoniale et qui relève des
branches I, III et VI, et de la [[Complémentaire santé]], qui rembourse des dépenses de soins. La couverture
obligatoire en cas de décès et d'invalidité au Luxembourg est publique : elle relève du **Code de la sécurité
sociale**, administré par la CNS et l'AAA, organismes qui ne sont pas des assureurs supervisés par le
[[CAA]] et ne figurent pas au registre. Ce qui est documenté ici est le seul étage privé.

## La ligne avec le solde restant dû

C'est la distinction la plus utile de cette branche au Luxembourg, et le corpus la met à l'épreuve sur un
document précis.

L'IPID *lalux-Security – Assurance décès à capital constant* imprime cinq objectifs pour sa garantie
principale : « Obtenir un crédit immobilier ou autre. **Couvrir un emprunt.** Protection du patrimoine
familial. Pérenniser votre entreprise. Garantir un revenu à vos enfants. » Deux d'entre eux touchent
directement au domaine de l'[[Solde restant dû]], et une lecture par l'objectif y aurait rangé le
document.

Le classement retenu est `prevoyance`, pour deux raisons tirées du document lui-même :

- **le capital est constant** — le titre imprimé est « Assurance décès à **capital constant** », et la
  garantie « couvre le capital fixé[…] dans les Conditions Particulières tout au long de la durée du
  contrat ». Un solde restant dû suit au contraire l'amortissement du prêt, avec un capital décroissant ;
- **le contrat n'est rattaché à aucun prêt.** Le capital est versé « au bénéficiaire désigné par vous », pas à
  un prêteur ; aucune clause ne lie la durée ni le montant à un tableau d'amortissement.

Le même assureur publie d'ailleurs les deux produits côte à côte, et la nomenclature de ses fichiers le dit
plus clairement que ses titres : `ipid_assurance-dec.pdf` (DEC = décès, capital constant, cette branche) et
`ipid_assurance-td.pdf` (**TD = temporaire décroissante**, le solde restant dû). Aucun des deux noms de
fichier ne porte de marqueur de langue et aucun des deux titres ne développe l'abréviation — c'est un piège
de lecture consigné dans le fichier de découverte lalux.

**Ce qui décide n'est donc pas l'usage que l'assuré fait du capital, mais le profil du capital et son
rattachement ou non à une créance.** Un capital constant souscrit pour couvrir un emprunt reste de la
prévoyance ; il ne suit pas la dette et ne s'éteint pas avec elle.

## Ce que le corpus documente

Un seul document, un seul produit : *lalux-Security – Assurance décès à capital constant*, IPID d'une page,
marque « LALUX Assurances-Vie ». Le contrat peut couvrir **un seul assuré ou deux assurés**.

- **Garantie principale — Décès.** Versement du capital fixé aux Conditions Particulières au bénéficiaire
  désigné, si l'assuré décède pendant la période couverte.
- **Garantie complémentaire — Décès par Accident et Accident de la Circulation.** Prestation additionnelle
  égale à « un multiple, à choisir par le preneur, du capital décès de la garantie principale » en cas de
  décès accidentel, **doublée** en cas de décès par accident de circulation.
- **Garantie complémentaire — Invalidité Totale.** Deux effets distincts selon la nature de l'invalidité : en
  cas d'invalidité totale **économique**, le preneur est **exonéré du paiement des primes** ; en cas
  d'invalidité totale **physiologique**, « l'attribution de la prestation principale en cas de décès est
  garantie ».
- **Portée** : le monde entier, sauf pour l'Invalidité Totale, dont la validité mondiale « n'est acquise pour
  les séjours hors de l'Europe que s'ils ne dépassent pas une durée de trois mois et à condition que la
  Compagnie puisse exercer valablement les contrôles médicaux prévus ».
- **Exclusions sans dérogation possible** : faits intentionnels, crimes et délits, aviation militaire, guerre
  et émeutes, risques nucléaires. S'y ajoutent, pour les deux garanties complémentaires, les ivresses et
  drogues ; et pour l'Invalidité Totale seule, l'état de santé antérieur et les « cas non contrôlables ».
- **Options de gestion en cours de contrat**, telles qu'énumérées : augmenter ou diminuer la couverture,
  augmenter ou diminuer la durée, changer le mode de paiement, libérer le contrat du paiement des primes
  moyennant une diminution de la couverture, racheter le contrat moyennant des frais éventuels. La liste
  imprimée se termine par un « … » : elle est explicitement ouverte.

## À surveiller

- **Le profil du capital.** Constant, il ne suit pas une dette ; décroissant, il la suit. C'est le paramètre
  qui range un contrat de ce côté-ci ou de l'autre, et le titre commercial ne le dit pas toujours.
- **Ce que recouvre l'invalidité.** Le document distingue invalidité **économique** et **physiologique** et
  leur attache des effets différents, mais ne définit ni l'une ni l'autre, et n'indique aucun taux, aucun
  seuil ni aucune modalité de constatation.
- **La formalité médicale n'est pas décrite.** Le document ne mentionne ni questionnaire de santé, ni examen,
  ni âge limite, ni capital minimum ou maximum. L'exclusion « état de santé antérieur » suppose pourtant une
  sélection médicale, dont les modalités ne sont pas publiées.
- **Le rachat et la réduction sont possibles**, ce qui indique une valeur de rachat éventuelle sur un produit
  présenté par ailleurs comme une « couverture de risque ». Ni les frais de rachat ni la valeur ne sont
  chiffrés.
- **Aucun régime de substitution.** Contrairement à la France, aucun dispositif comparable aux lois Lagarde
  ou Lemoine n'a été trouvé au Luxembourg — ni droit de substitution d'assureur, ni statut légal du
  questionnaire médical. C'est une absence constatée, pas une règle vérifiée : voir
  [[Solde restant dû]].

## Lacunes établies

- **Deux rubriques obligatoires du format IPID manquent entièrement** à ce document : il n'y a **aucun
  encadré « Y a-t-il des restrictions à la couverture ? »** et **aucun encadré « Comment puis-je résilier le
  contrat ? »**. À la place du second, la page imprime « Comment puis-je modifier le contrat ? », dont le
  contenu porte sur les modifications et non sur la résiliation. Le contenu a été rangé selon sa nature et
  l'intitulé n'a pas été réparé. Conséquence pour un lecteur : **les conditions de résiliation de ce contrat
  ne sont pas publiées.**
- **Aucun montant, aucun pourcentage et aucune date** ne figurent nulle part dans le document : ni âge
  limite, ni capital, ni prime, ni frais de rachat, ni durée minimale.
- **Aucune date d'édition, aucune référence, aucun porteur nommé au sens juridique** : le document imprime la
  marque « LALUX Assurances-Vie » puis « la Compagnie » / « l'Assureur », sans forme sociale ni numéro RCS.
  Le registre du [[CAA]] compte deux entités vie sous cette marque, et le document ne permet pas de savoir
  laquelle porte le risque.
- **Aucune condition générale n'est publiée** pour ce produit, ni pour aucun autre produit vie de détail de
  cet assureur.
- **Le caractère optionnel des deux garanties complémentaires n'est pas tranché** par la source : elles sont
  qualifiées de « Garantie complémentaire » et de « Prestation additionnelle », sans que le document dise si
  elles sont incluses d'office ou souscrites en supplément.
- **Un seul produit, un seul assureur, une seule langue.** Les gammes de prévoyance des autres porteurs
  luxembourgeois n'ont pas été ingérées, et aucune version allemande ni anglaise de ce document n'a été
  reprise pour combler ses rubriques manquantes.

## Cadre légal

- **Loi modifiée du 7 décembre 2015 sur le secteur des assurances (LSA), annexe II, branche I**, citée
  au premier paragraphe. Vérifiée dans le texte coordonné publié par le [[CAA]]
  (`Loi_SecteurAssurances_2015-12-07_coord_2026-04-03_ESAP_.pdf`, consulté le 2026-08-03).
- **Aucune obligation d'assurance privée.** La couverture obligatoire décès-invalidité relève du Code de la
  sécurité sociale et d'organismes publics qui ne sont pas au registre du [[CAA]].
- Superviseur : [[CAA]].

## Produits documentés

Voir [[00 - Branches MOC]] pour la liste générée des produits de cette branche.

## Related

- [[CAA]] · [[Solde restant dû]] · [[Assurance vie et épargne]] ·
  [[Retraite et pension complémentaire]] · [[Assurance accidents]]

## Sources

- Loi modifiée du 7 décembre 2015 sur le secteur des assurances, annexe II.
- `_meta/lu-market-census.md` (détentions de branches vie, principe de spécialisation).
- `_meta/discovery/lu/lalux.md` (piège n° 4 : `ipid_assurance-td.pdf` et `ipid_assurance-dec.pdf`).
- `sources/lu/_country.yml`, clés `branches.prevoyance` et `branches.solde-restant-du`.
