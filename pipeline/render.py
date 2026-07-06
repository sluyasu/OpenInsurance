"""Deterministic renderers: extracted product JSON -> rich Markdown wiki pages.

Keeping rendering deterministic (not LLM-generated) makes pages consistent and makes
`build_wiki.py` idempotent. The richness comes from the JSON, which the extraction agent
fills exhaustively.
"""

from __future__ import annotations

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


def branch_label(country_meta: dict, slug: str) -> str:
    return country_meta.get("branches", {}).get(slug, {}).get("label", slug)


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


def render_product(obj: dict, country_meta: dict, relation: dict | None = None) -> str:
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
        "reference": obj.get("reference"),
        "edition_date": obj.get("edition_date"),
        "lang": obj.get("language"),
        "tags": [f"insurance/{cc}/{branch}", "product", f"insurer/{slug}"],
        "aliases": [obj.get("product_name")] if obj.get("product_name") else [],
        "source_url": obj.get("source_url"),
        "source_pages": obj.get("source_pages"),
        "fetched_at": obj.get("fetched_at"),
        "extraction_model": obj.get("extraction_model"),
        "prompt_version": obj.get("prompt_version"),
        "product_family": relation.get("family") or obj.get("product_family"),
        "variant": obj.get("variant") or relation.get("variant"),
        "edition_status": relation.get("edition_status"),
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
    L.append(f"- Assureur : [[{insurer}]] · Branche : [[{blabel}]] · Type : "
             f"{DOC_TYPE_LABEL.get(obj.get('document_type',''), obj.get('document_type',''))}"
             + (f" · Édition : {obj['edition_date']}" if obj.get("edition_date") else "") + "\n")

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
        if relation.get("superseded_by"):
            L.append(f"- ⚠️ Édition remplacée par une version plus récente : [[{relation['superseded_by']}]]")
        elif relation.get("edition_status") == "current":
            L.append("- Édition courante de ce produit.")
        if relation.get("extends_parent"):
            L.append(f"- Extension / option du produit : **{relation['extends_parent']}**")
        for ext in relation.get("extensions") or []:
            L.append(f"- Extension liée : [[{ext}]]")
        for r in related:
            dt = DOC_TYPE_LABEL.get(r.get("document_type"), r.get("document_type") or "")
            ed = f", éd. {r['edition_date']}" if r.get("edition_date") else ""
            L.append(f"- [[{r['title']}]] - {dt}{ed}")
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
                   country_meta: dict, website: str | None) -> str:
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
    L.append(f"[[{insurer_name}]]{site}. {len(products)} document(s) across {len(branches)} branch(es).\n")
    L.append("## Produits par branche\n")
    for b in sorted(branches.keys()):
        L.append(f"### [[{branch_label(country_meta, b)}]]")
        for p in sorted(branches[b], key=lambda x: x.get("product_name", "")):
            title = product_title(p)
            dt = DOC_TYPE_LABEL.get(p.get("document_type", ""), "")
            ed = f" ({p['edition_date']})" if p.get("edition_date") else ""
            L.append(f"- [[{title}]] - {dt}{ed}")
        L.append("")
    L.append("## Source\n")
    L.append(f"- Documents extraits des sources publiques listées dans `sources/{cc}/{slug}.yml`.")
    return "\n".join(L)


def render_branches_moc(cc: str, products: list[dict], country_meta: dict) -> str:
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
            L.append(f"### [[{label}]] ({len(prods)})")
            for p in sorted(prods, key=lambda x: (x.get("insurer_name", ""), x.get("product_name", ""))):
                L.append(f"- [[{product_title(p)}]] - [[{p.get('insurer_name', p.get('insurer_slug'))}]]")
            L.append("")
    return "\n".join(L)
