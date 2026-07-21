"""Deterministic renderers: extracted product JSON -> rich Markdown wiki pages.

Keeping rendering deterministic (not LLM-generated) makes pages consistent and makes
`build_wiki.py` idempotent. The richness comes from the JSON, which the extraction agent
fills exhaustively.
"""

from __future__ import annotations

import posixpath
from urllib.parse import quote

from common import frontmatter, safe_title, slugify, today

DISCLAIMER = (
    "⚠️ Ceci n'est pas le document officiel de l'assureur et peut contenir des erreurs "
    "d'extraction. Information, non un conseil - vérifiez toujours par rapport au document source."
)

DOC_TYPE_LABEL = {
    "conditions_generales": "Conditions générales",
    "ipid": "IPID / Fiche d'information",
    "conditions_particulieres": "Conditions particulières",
    "product_sheet": "Fiche produit",
    "other": "Document",
}
DOC_TYPE_SUFFIX = {"ipid": " (IPID)", "conditions_particulieres": " (CP)", "product_sheet": " (Fiche)"}


def _pg(p) -> str:
    return f"p. {p}" if p not in (None, "", 0) else ""


def _dicts(items, namekey="name"):
    """Defensive: yield only dict items (coerce bare strings) so a malformed extraction
    can never crash the renderer."""
    out = []
    for x in items or []:
        if isinstance(x, dict):
            out.append(x)
        elif isinstance(x, str):
            out.append({namekey: x})
    return out


def product_title(obj: dict) -> str:
    """Disambiguated page title so a product's CG and IPID don't collide."""
    name = obj.get("product_name") or "Untitled"
    return safe_title(name + DOC_TYPE_SUFFIX.get(obj.get("document_type", ""), ""))


def mdlink(from_page: str, to_page: str, label: str) -> str:
    """A relative markdown link between two wiki pages, both given as paths relative to
    `wiki/<cc>/` (posix separators).

    Generated pages must never emit a bare `[[Title]]`. Product names are not unique:
    'Assurance Auto' is claimed by eight pages in Belgium alone, and a basename resolver
    (the site's roamlinks plugin, validate's own map) silently picks one, so an Argenta
    page can link to Yuzzu's product. That is worse than a broken link because nothing
    looks wrong. It gets worse per country added: the same name will exist in BE, CH and
    FR at once. A path says exactly which page is meant.

    The path is percent-encoded, so spaces, parentheses and accents survive both Obsidian
    and MkDocs. Unencoded parentheses would truncate the link at the first ')'."""
    rel = posixpath.relpath(to_page, posixpath.dirname(from_page))
    return f"[{label}]({quote(rel)})"


def _ref(target: str | None, label: str, self_page: str | None) -> str:
    """Link to `target` if it exists, otherwise render the label as plain text.

    A missing target means the page was never written (a branch overview nobody wrote
    yet). Emitting a link anyway would publish a 404; plain text is the honest gap
    (rule 6). Plain text is also the fallback when routes are absent, which keeps the
    renderers usable from a test without a full build."""
    if not target or not self_page:
        return label
    return mdlink(self_page, target, label)


def _page_ref(source_url: str | None, label: str, routes: dict | None,
              self_page: str | None) -> str:
    """Link to another product page, resolved by source_url (unique) not by title."""
    target = (routes or {}).get("product", {}).get(source_url)
    return _ref(target, label, self_page)


def _insurer_ref(slug: str, label: str, routes: dict | None, self_page: str | None) -> str:
    target = (routes or {}).get("insurer", {}).get(slug)
    return _ref(target, label, self_page)


def _branch_ref(bslug: str, label: str, routes: dict | None, self_page: str | None) -> str:
    target = (routes or {}).get("branch", {}).get(bslug)
    return _ref(target, label, self_page)


def branch_label(country_meta: dict, slug: str) -> str:
    return country_meta.get("branches", {}).get(slug, {}).get("label", slug)


# An edition older than this gets an age notice. Long enough not to cry wolf over a
# document an insurer simply has not restyled, short enough to catch the 2010-2014 batch.
OLD_EDITION_YEARS = 7


def edition_age_years(obj: dict) -> int | None:
    """Whole years between the printed edition date and the day the PDF was collected.

    Measured against fetched_at, not today(): a date that moves would make every rebuild
    a diff and break the idempotence gate.

    This is deliberately an AGE, not a "closed product" flag. The corpus holds ERGO
    editions from 2010 and Athora contracts written when the carrier was still Generali,
    and it is tempting to mark them run-off. Nothing in those documents says so. An
    insurer publishing an old edition may still sell it, or may be serving policyholders
    whose contracts still run. The age is a fact; "no longer sold" would be a guess."""
    import link as _link  # local import: render is imported by tools that never build
    ey = _link._edition_key(obj.get("edition_date"))[0]
    fy = _link._edition_key(obj.get("fetched_at"))[0]
    if not ey or not fy or fy < ey:
        return None
    return fy - ey


def _table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return ""
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        cells = [str(c).replace("\n", " ").replace("|", "\\|") if c is not None else "" for c in r]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def _neutralize_links(o):
    """Break any [[ ]] coming from extracted source text so only the wikilinks the
    renderer adds (insurer, branch) are real. Prevents source content from injecting
    or breaking graph links."""
    if isinstance(o, str):
        return o.replace("[[", "[").replace("]]", "]")
    if isinstance(o, list):
        return [_neutralize_links(x) for x in o]
    if isinstance(o, dict):
        return {k: _neutralize_links(v) for k, v in o.items()}
    return o


def render_product(obj: dict, country_meta: dict, relation: dict | None = None,
                   routes: dict | None = None, self_page: str | None = None) -> str:
    obj = _neutralize_links(obj)
    relation = relation or {}
    cc = obj.get("country", "")
    slug = obj.get("insurer_slug", "")
    insurer = obj.get("insurer_name") or slug
    branch = obj.get("branch", "autres")
    blabel = branch_label(country_meta, branch)

    meta = {
        "type": "product",
        "domain": "insurance",
        "country": cc,
        "insurer": f"[[{insurer}]]",
        "insurer_slug": slug,
        "branch": branch,
        "product_name": obj.get("product_name"),
        "document_type": obj.get("document_type"),
        "target_audience": obj.get("target_audience"),
        "target_audience_note": obj.get("target_audience_note"),
        "reference": obj.get("reference"),
        "edition_date": obj.get("edition_date"),
        "lang": obj.get("language"),
        "tags": [f"insurance/{cc}/{branch}", "product", f"insurer/{slug}"],
        # A generated page must not claim a name the hand-authored layer owns: AMMA's
        # product is really called "Auto", but keeping that alias let a bare [[Auto]] in
        # a glossary page resolve to a product instead of the Auto branch overview.
        "aliases": ([obj["product_name"]]
                    if obj.get("product_name")
                    and obj["product_name"] not in {branch_label(country_meta, b)
                                                    for b in (country_meta.get("branches") or {})}
                    else []),
        "source_url": obj.get("source_url"),
        "source_pages": obj.get("source_pages"),
        "fetched_at": obj.get("fetched_at"),
        "extraction_model": obj.get("extraction_model"),
        "prompt_version": obj.get("prompt_version"),
        "product_family": relation.get("family") or obj.get("product_family"),
        "variant": obj.get("variant") or relation.get("variant"),
        "edition_status": relation.get("edition_status"),
        "edition_age_years": edition_age_years(obj),
        "superseded": (relation.get("edition_status") == "superseded") or bool(obj.get("superseded")) or None,
        "extends": obj.get("extends") if obj.get("is_extension") else None,
        "freshness": obj.get("fetched_at") or today(),
        "status": "ready",
        "generated": True,
    }

    L = [frontmatter(meta),
         "<!-- GENERATED - do not edit. Fix data/<cc>/extracted/ and run `make build`. -->\n"]

    L.append("## Résumé\n")
    L.append((obj.get("summary") or "_(pas de résumé)_") + "\n")
    L.append(f"- Assureur : {_insurer_ref(slug, insurer, routes, self_page)}"
             f" · Branche : {_branch_ref(branch, blabel, routes, self_page)} · Type : "
             f"{DOC_TYPE_LABEL.get(obj.get('document_type',''), obj.get('document_type',''))}"
             + (f" · Édition : {obj['edition_date']}" if obj.get("edition_date") else "") + "\n")

    # Age notice sits here, above the content, because it changes how everything below
    # should be read. It states the age and stops there: the corpus holds ERGO editions
    # from 2010 and Athora contracts from the Generali era, and nothing in those
    # documents says whether the product is still sold.
    age = edition_age_years(obj)
    if age is not None and age >= OLD_EDITION_YEARS and not relation.get("superseded_by"):
        L.append(f"> ⚠️ **Édition ancienne** : {obj.get('edition_date')}, soit {age} ans à la "
                 f"date de collecte, et aucune édition plus récente de ce document n'a été "
                 f"trouvée. Le document était toujours publié par l'assureur au moment de la "
                 f"collecte. Un document ancien peut décrire un produit qui n'est plus "
                 f"commercialisé mais dont des contrats sont toujours en cours ; ce point "
                 f"n'est pas déterminable à partir du document et est à vérifier auprès de "
                 f"l'assureur.\n")

    defs = _dicts(obj.get("definitions"), "term")
    if defs:
        L.append("## Définitions\n")
        L.append(_table(["Terme", "Définition", "Page"],
                        [[d.get("term"), d.get("definition"), _pg(d.get("page"))] for d in defs]) + "\n")

    covs = _dicts(obj.get("coverages"))
    if covs:
        L.append("## Garanties\n")
        for c in covs:
            head = c.get("name", "Garantie")
            pg = _pg(c.get("page"))
            L.append(f"### {head}" + (f" - {pg}" if pg else ""))
            if c.get("description"):
                L.append(c["description"])
            bits = []
            if c.get("is_optional") is not None:
                bits.append(f"Optionnelle : {'oui' if c['is_optional'] else 'non'}")
            if c.get("territorial_scope"):
                bits.append(f"Portée : {c['territorial_scope']}")
            if c.get("limits"):
                bits.append(f"Limite : {c['limits']}")
            if c.get("deductible"):
                bits.append(f"Franchise : {c['deductible']}")
            if bits:
                L.append("- " + " · ".join(bits))
            for sl in c.get("sub_limits") or []:
                L.append(f"  - Sous-limite : {sl}")
            for cond in c.get("conditions") or []:
                L.append(f"  - Condition : {cond}")
            L.append("")

    excl = _dicts(obj.get("exclusions"))
    if excl:
        L.append("## Exclusions\n")
        L.append(_table(["Exclusion", "Description", "S'applique à", "Page"],
                        [[e.get("name"), e.get("description"), e.get("applies_to"), _pg(e.get("page"))]
                         for e in excl]) + "\n")

    ded = obj.get("deductibles")
    if ded and any(ded.get(k) for k in ("standard", "variable", "per_coverage")):
        L.append("## Franchises\n")
        if ded.get("standard"):
            L.append(f"- Standard : {ded['standard']}")
        if ded.get("variable"):
            L.append(f"- Variable : {ded['variable']}")
        pc = ded.get("per_coverage")
        if isinstance(pc, dict):
            for k, v in pc.items():
                L.append(f"- {k} : {v}")
        elif isinstance(pc, str) and pc.strip():
            L.append(f"- Par garantie : {pc}")
        L.append("")

    wp = _dicts(obj.get("waiting_periods"), "description")
    if wp:
        L.append("## Délais d'attente\n")
        for w in wp:
            L.append(f"- {w.get('coverage','') and w['coverage']+' : '}{w.get('description','')}"
                     f"{' ('+w['duration']+')' if w.get('duration') else ''} {_pg(w.get('page'))}".strip())
        L.append("")

    obl = _dicts(obj.get("obligations"))
    if obl:
        L.append("## Obligations de l'assuré\n")
        for o in obl:
            extra = " · ".join(x for x in [o.get("timing"), o.get("sanction")] if x)
            L.append(f"- {o.get('description','')}" + (f" ({extra})" if extra else "") + f" {_pg(o.get('page'))}".rstrip())
        L.append("")

    cp = _dicts(obj.get("claims_procedure"))
    if cp:
        L.append("## Procédure de sinistre\n")
        for i, s in enumerate(cp, 1):
            txt = s.get("description") or s.get("step") or ""
            L.append(f"{i}. {txt}"
                     + (f" (délai : {s['deadline']})" if s.get("deadline") else "")
                     + (f" {_pg(s.get('page'))}" if s.get("page") else ""))
        L.append("")

    dc = obj.get("duration_and_cancellation")
    if dc and any(dc.get(k) for k in ("duration", "notice_period", "methods", "special_rights", "tacit_renewal")):
        L.append("## Durée & résiliation\n")
        if dc.get("duration"):
            L.append(f"- Durée : {dc['duration']}")
        if dc.get("tacit_renewal") is not None:
            L.append(f"- Reconduction tacite : {'oui' if dc['tacit_renewal'] else 'non'}")
        if dc.get("notice_period"):
            L.append(f"- Préavis : {dc['notice_period']}")
        for m in dc.get("methods") or []:
            L.append(f"- Modalité : {m}")
        for s in dc.get("special_rights") or []:
            L.append(f"- Droit spécial : {s}")
        L.append("")

    pr = obj.get("prescription_period")
    if isinstance(pr, dict) and pr.get("description"):
        L.append("## Prescription\n")
        L.append(f"{pr['description']} {_pg(pr.get('page'))}".strip() + "\n")

    pm = obj.get("premium")
    if isinstance(pm, dict) and (pm.get("notes") or pm.get("indexation")):
        L.append("## Prime\n")
        if pm.get("indexation"):
            L.append(f"- Indexation : {pm['indexation']}")
        for n in pm.get("notes") or []:
            L.append(f"- {n}")
        L.append("")

    sc = _dicts(obj.get("special_conditions"))
    if sc:
        L.append("## Conditions particulières\n")
        for s in sc:
            L.append(f"- {s.get('description','')} {_pg(s.get('page'))}".rstrip())
        L.append("")

    gaps = obj.get("gaps") or []
    if gaps:
        L.append("## Lacunes d'extraction\n")
        for g in gaps:
            L.append(f"- {g}")
        L.append("")

    related = relation.get("related") or []
    if related or relation.get("superseded_by") or relation.get("extends_parent") or relation.get("extensions"):
        L.append("## Documents liés\n")
        sb = relation.get("superseded_by")
        if sb:
            L.append("- ⚠️ Édition remplacée par une version plus récente : "
                     + _page_ref(sb.get("source_url"), sb.get("title"), routes, self_page))
        elif relation.get("edition_status") == "current":
            L.append("- Édition courante de ce produit.")
        if relation.get("extends_parent"):
            L.append(f"- Extension / option du produit : **{relation['extends_parent']}**")
        for ext in relation.get("extensions") or []:
            L.append("- Extension liée : "
                     + _page_ref(ext.get("source_url"), ext.get("title"), routes, self_page))
        for r in related:
            dt = DOC_TYPE_LABEL.get(r.get("document_type"), r.get("document_type") or "")
            ed = f", éd. {r['edition_date']}" if r.get("edition_date") else ""
            L.append(f"- {_page_ref(r.get('source_url'), r['title'], routes, self_page)} - {dt}{ed}")
        L.append("")

    L.append("## Source & fidélité\n")
    su = obj.get("source_url")
    L.append(f"- Source : [{su}]({su}) - téléchargé le {obj.get('fetched_at','?')} - "
             f"{obj.get('source_pages','?')} pages")
    L.append(f"- Extraction : {obj.get('extraction_model','?')} · prompt v{obj.get('prompt_version','?')}")
    L.append(f"- {DISCLAIMER}\n")
    return "\n".join(L)


def _latest_fetch(products: list[dict]) -> str:
    """Newest fetched_at across the given products: a data-derived date, stable
    across rebuilds (today() would break the build-idempotence gate)."""
    dates = [str(p.get("fetched_at")) for p in products if p.get("fetched_at")]
    return max(dates) if dates else today()


def render_insurer(insurer_name: str, slug: str, cc: str, products: list[dict],
                   country_meta: dict, website: str | None,
                   routes: dict | None = None, self_page: str | None = None) -> str:
    branches: dict[str, list[dict]] = {}
    for p in products:
        branches.setdefault(p.get("branch", "autres"), []).append(p)

    stamp = _latest_fetch(products)
    meta = {
        "type": "insurer", "domain": "insurance", "country": cc, "insurer_slug": slug,
        "name": insurer_name, "website": website,
        "products_count": len(products),
        "branches_covered": sorted(branches.keys()),
        "tags": [f"insurance/{cc}", "insurer"], "aliases": [insurer_name],
        "date": stamp, "freshness": stamp, "status": "ready", "generated": True,
    }
    L = [frontmatter(meta), "<!-- GENERATED - do not edit. -->\n", "## Résumé\n"]
    site = f" - [{website}]({website})" if website else ""
    # the page's own name, not a self-link: [[insurer_name]] here pointed at this file
    L.append(f"**{insurer_name}**{site}. {len(products)} document(s) across {len(branches)} branch(es).\n")
    L.append("## Produits par branche\n")
    for b in sorted(branches.keys()):
        L.append(f"### {_branch_ref(b, branch_label(country_meta, b), routes, self_page)}")
        for p in sorted(branches[b], key=lambda x: x.get("product_name", "")):
            dt = DOC_TYPE_LABEL.get(p.get("document_type", ""), "")
            ed = f" ({p['edition_date']})" if p.get("edition_date") else ""
            # reference disambiguates two same-named documents in the same list, which
            # otherwise read as a duplicated entry rather than two distinct contracts
            ref = f" · réf. {p['reference']}" if p.get("reference") else ""
            L.append(f"- {_page_ref(p.get('source_url'), product_title(p), routes, self_page)}"
                     f" - {dt}{ed}{ref}")
        L.append("")
    L.append("## Source\n")
    L.append(f"- Documents extraits des sources publiques listées dans `sources/{cc}/{slug}.yml`.")
    return "\n".join(L)


def render_branches_moc(cc: str, products: list[dict], country_meta: dict,
                        routes: dict | None = None, self_page: str | None = None) -> str:
    branches: dict[str, list[dict]] = {}
    for p in products:
        branches.setdefault(p.get("branch", "autres"), []).append(p)

    meta = {"type": "moc", "domain": "insurance", "country": cc,
            "tags": [f"insurance/{cc}", "moc"], "date": _latest_fetch(products),
            "status": "ready", "generated": True}
    L = [frontmatter(meta), "<!-- GENERATED - do not edit. -->\n",
         "## Branches - produits documentés\n",
         "Liste générée des produits par branche. Les fiches conceptuelles de branche sont "
         "rédigées à la main dans ce dossier.\n"]
    for slug in country_meta.get("branches", {}):
        prods = branches.get(slug, [])
        label = branch_label(country_meta, slug)
        if prods:
            L.append(f"### {_branch_ref(slug, label, routes, self_page)} ({len(prods)})")
            for p in sorted(prods, key=lambda x: (x.get("insurer_name", ""), x.get("product_name", ""))):
                iname = p.get("insurer_name") or p.get("insurer_slug")
                L.append(f"- {_page_ref(p.get('source_url'), product_title(p), routes, self_page)}"
                         f" - {_insurer_ref(p.get('insurer_slug'), iname, routes, self_page)}")
            L.append("")
    return "\n".join(L)
