#!/usr/bin/env python
"""Regenerate the README visuals from the live wiki.

Outputs:
  assets/knowledge-graph.html + .png  - the knowledge web (fig. 1)
  assets/architecture.png             - screenshot of assets/architecture.html (fig. 2)

fig. 1 is the hand-designed knowledge-web figure from stochasticanalytics.com
(branch hubs on a loose ellipse, product dots gathered gaussian around their
branch, insurer nodes in indigo, one seeded PRNG so the drawing is stable),
re-rendered here with the REAL numbers of the committed dataset injected:
branch product counts, insurer count, country count. A force-directed dump of
all 1 300 pages was tried first and looked like a hairball; the designed figure
says the same thing legibly. The layout is illustrative, the numbers are not.

Deps (not part of the core pipeline): pip install playwright
(+ `playwright install chromium`). Run: python assets/make_visuals.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
DATA = REPO / "data"
SOURCES = REPO / "sources"

# the site shortens long branch labels; same idea, keyed on the folded label
SHORT = {
    "complémentaire santé": "santé",
    "assurance auto": "auto",
    "multirisque habitation": "habitation",
    "multirisque professionnelle": "multirisque pro.",
    "protection juridique": "protection jur.",
    "rc professionnelle": "rc pro",
    "voyage et assistance": "voyage",
    "responsabilité civile vie privée": "vie privée",
    "assurance vie et épargne": "assurance vie",
}


def dataset_numbers():
    """Real counts from the committed extractions. Branches are aggregated by SLUG
    (sante/auto/habitation are shared across the taxonomies), then displayed under
    the SHORTEST label any country gives that slug: aggregating on label text drew
    'complémentaire santé' (fr) and 'santé' (be) as two different hubs."""
    slug_labels: dict[str, list[str]] = {}
    for cy in SOURCES.glob("*/_country.yml"):
        meta = yaml.safe_load(cy.read_text(encoding="utf-8")) or {}
        for slug, b in (meta.get("branches") or {}).items():
            slug_labels.setdefault(slug, []).append(str(b.get("label") or slug))

    per_slug: Counter[str] = Counter()
    insurers, countries = set(), set()
    n_products = 0
    for f in DATA.glob("*/extracted/*/*.json"):
        cc = f.relative_to(DATA).parts[0]
        try:
            obj = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("out_of_scope_reason"):
            continue
        countries.add(cc)
        insurers.add((cc, obj.get("insurer_slug")))
        n_products += 1
        per_slug[obj.get("branch") or "?"] += 1

    per_branch: Counter[str] = Counter()
    for slug, n in per_slug.items():
        label = min(slug_labels.get(slug, [slug]), key=len).casefold()
        label = SHORT.get(label, label if len(label) <= 16 else label[:15] + ".")
        per_branch[label] += n
    return per_branch, len(insurers), n_products, len(countries)


TEMPLATE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>openinsurance-wiki - knowledge graph</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { width: 760px; background: #f7f6f2; padding: 36px 40px 28px; }
  .card {
    background: #ffffff;
    border: 1px solid rgba(26, 26, 33, 0.14);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 1px 2px rgba(26, 26, 33, 0.04), 0 12px 32px -16px rgba(26, 26, 33, 0.12);
  }
  svg { width: 100%; height: auto; display: block; }
  figcaption {
    margin-top: 12px;
    font-family: "JetBrains Mono", monospace;
    font-size: 11px;
    letter-spacing: 0.02em;
    color: #8e8e98;
  }
  figcaption .no { color: #52525c; }
</style>
</head>
<body>
<figure>
  <div class="card"><svg id="fig" viewBox="0 0 640 440" role="img"></svg></div>
  <figcaption><span class="no">fig. 1</span> · __CAPTION__</figcaption>
</figure>
<script>
// The knowledge-web figure from stochasticanalytics.com (knowledge-graph-figure.tsx),
// static render. Same seeded PRNG, same grammar; only the data below is injected
// by make_visuals.py from the committed dataset.
const BRANCHES = __BRANCHES__;
const N_INSURERS = __N_INSURERS__;
const LABELED = new Set(__LABELED__);
const ANNOTATION = "__ANNOTATION__";

const W = 640, H = 440;
function mulberry32(seed) {
  let a = seed;
  return () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const rand = mulberry32(20260707);
const gauss = () => {
  const u1 = Math.max(rand(), 1e-9), u2 = rand();
  return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
};

const cx = W / 2, cy = H / 2 - 6;
const maxN = Math.max(...BRANCHES.map(b => b.n));
const hubs = BRANCHES.map((b, i) => {
  const angle = i * 2.399963 + 0.9;
  const rx = 218 + gauss() * 10, ry = 148 + gauss() * 8;
  return { x: cx + Math.cos(angle) * rx * (0.72 + rand() * 0.28),
           y: cy + Math.sin(angle) * ry * (0.72 + rand() * 0.28),
           label: b.slug, n: b.n };
});

const nodes = [], edges = [];
hubs.forEach(h => {
  // spread normalised to the biggest branch so a 300-product cluster still
  // fits the same canvas the site drew 34 into
  const spread = 14 + 41 * Math.sqrt(h.n / maxN);
  const pEdge = Math.min(0.55, 60 / h.n);
  for (let i = 0; i < h.n; i++) {
    const x = h.x + gauss() * spread, y = h.y + gauss() * spread * 0.78;
    nodes.push({ x, y, r: 1.15 + rand() * 0.95, kind: "product", opacity: 0.22 + rand() * 0.26 });
    if (rand() < pEdge) edges.push({ x1: x, y1: y, x2: h.x, y2: h.y, o: 0.05 + rand() * 0.05 });
  }
});
for (let i = 0; i < N_INSURERS; i++) {
  const angle = i * 2.399963 + 0.35;
  const x = cx + Math.cos(angle) * (66 + rand() * 52);
  const y = cy + Math.sin(angle) * (46 + rand() * 38);
  nodes.push({ x, y, r: 3.0 + rand() * 1.4, kind: "insurer", opacity: 0.55 + rand() * 0.3 });
  for (let k = 0; k < 2; k++) {
    const h = hubs[Math.floor(rand() * hubs.length)];
    edges.push({ x1: x, y1: y, x2: h.x, y2: h.y, o: 0.06 + rand() * 0.05 });
  }
}

const S = [];
S.push(`<text x="${W - 20}" y="30" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="11" fill="#8e8e98">${ANNOTATION}</text>`);
for (const e of edges)
  S.push(`<line x1="${e.x1.toFixed(1)}" y1="${e.y1.toFixed(1)}" x2="${e.x2.toFixed(1)}" y2="${e.y2.toFixed(1)}" stroke="#1a1a21" stroke-opacity="${e.o.toFixed(3)}" stroke-width="1"/>`);
for (const n of nodes)
  S.push(`<circle cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${n.r.toFixed(2)}" fill="${n.kind === "insurer" ? "#4f46e5" : "#1a1a21"}" fill-opacity="${n.opacity.toFixed(3)}"/>`);
for (const h of hubs) {
  S.push(`<circle cx="${h.x.toFixed(1)}" cy="${h.y.toFixed(1)}" r="4.5" fill="none" stroke="#1a1a21" stroke-opacity="0.4" stroke-width="1"/>`);
  if (LABELED.has(h.label))
    S.push(`<text x="${h.x.toFixed(1)}" y="${(h.y - 10).toFixed(1)}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="#52525c" stroke="#ffffff" stroke-width="3.5" paint-order="stroke" stroke-linejoin="round">${h.label} \\u00b7 ${h.n}</text>`);
}
S.push(`<circle cx="${W - 150}" cy="${H - 34}" r="3.6" fill="#4f46e5" fill-opacity="0.7"/>`);
S.push(`<text x="${W - 142}" y="${H - 30}" font-family="JetBrains Mono, monospace" font-size="11" fill="#8e8e98">assureurs</text>`);
S.push(`<circle cx="${W - 66}" cy="${H - 34}" r="2.2" fill="#1a1a21" fill-opacity="0.4"/>`);
S.push(`<text x="${W - 58}" y="${H - 30}" font-family="JetBrains Mono, monospace" font-size="11" fill="#8e8e98">produits</text>`);
document.getElementById("fig").innerHTML = S.join("");
</script>
</body>
</html>
"""


def write_knowledge_graph_html() -> None:
    per_branch, n_insurers, n_products, n_countries = dataset_numbers()
    top = per_branch.most_common(12)
    labeled = [label for label, _ in top[:5]]
    fmt = lambda n: f"{n:,}".replace(",", " ")          # narrow nbsp thousands
    annotation = (f"{fmt(n_products)} produits · {n_insurers} assureurs "
                  f"· {n_countries} pays")
    caption = ("le graphe de connaissances · produits groupés par branche, "
               "assureurs en indigo · comptes réels du dataset")
    html = (TEMPLATE
            .replace("__BRANCHES__", json.dumps(
                [{"slug": l, "n": n} for l, n in top], ensure_ascii=False))
            .replace("__N_INSURERS__", str(n_insurers))
            .replace("__LABELED__", json.dumps(labeled, ensure_ascii=False))
            .replace("__ANNOTATION__", annotation)
            .replace("__CAPTION__", caption))
    (ASSETS / "knowledge-graph.html").write_text(html, encoding="utf-8")
    print(f"wrote assets/knowledge-graph.html "
          f"({fmt(n_products)} products, {n_insurers} insurers, top branch: "
          f"{top[0][0]} · {top[0][1]})")


def shoot(html_name: str, png_name: str, width: int) -> None:
    """assets/<html> -> assets/<png> (2x), via Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"playwright not installed; skipping {png_name}")
        return
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": 800},
                                device_scale_factor=2)
        page.goto((ASSETS / html_name).as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        height = page.evaluate("document.body.scrollHeight")
        page.set_viewport_size({"width": width, "height": height})
        page.screenshot(path=str(ASSETS / png_name))
        browser.close()
    print(f"wrote assets/{png_name}")


def main() -> int:
    write_knowledge_graph_html()
    shoot("knowledge-graph.html", "knowledge-graph.png", 760)
    shoot("architecture.html", "architecture.png", 1180)
    return 0


if __name__ == "__main__":
    sys.exit(main())
