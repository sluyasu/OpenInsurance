#!/usr/bin/env python
"""Regenerate the README visuals from the live wiki.

Outputs:
  assets/knowledge-graph.png  - force-directed graph of the whole wiki (fig. 1)
  assets/architecture.png     - screenshot of assets/architecture.html (fig. 2)

Both are figures in the light editorial style (paper background, ink, one indigo
accent, JetBrains Mono captions). The graph reads BOTH link forms the wiki uses:
`[[wikilinks]]` (hand-authored pages) and relative markdown path links (generated
pages, which stopped emitting wikilinks when links became path-resolved). Parsing
only wikilinks - as the first version did - silently drops almost every product
edge and draws a near-empty graph that still looks plausible.

Nodes are keyed by PATH, not by page stem: with four countries in the vault the
same name exists several times ("Assurance Auto" alone is claimed in be, fr and
ch), and stem-keyed nodes silently fuse them into one cross-country blob.

Deps (not part of the core pipeline): pip install networkx matplotlib scipy
playwright (+ `playwright install chromium`) for the architecture screenshot.
Run: python assets/make_visuals.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
ASSETS = REPO / "assets"

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
# Same two destination forms as pipeline/validate.py: `(<path.md>)` and `(path%20.md)`.
MDLINK = re.compile(r"\[[^\]]*\]\((?:<([^>]+\.md)>|([^)<]+\.md))\)")

PAPER = "#f7f6f2"
INK = "#1a1a21"
INK2 = "#52525c"
CAP = "#8e8e98"

TYPE_COLOR = {
    "product": "#4f46e5",       # indigo (the accent - products are the mass)
    "insurer": "#d97706",       # amber
    "branch": "#059669",        # emerald
    "regulation": "#dc2626",    # red
    "concept": "#0891b2",       # cyan
    "moc": "#7c3aed",           # violet
}
DEFAULT_COLOR = "#8e8e98"


def register_mono() -> str:
    """Use the committed JetBrains Mono if matplotlib can load it, else any mono."""
    for ttf in sorted((ASSETS / "fonts").glob("*.ttf")):
        try:
            fm.fontManager.addfont(str(ttf))
        except Exception:
            pass
    names = {f.name for f in fm.fontManager.ttflist}
    return "JetBrains Mono" if "JetBrains Mono" in names else "monospace"


def read_note(p: Path):
    t = p.read_text(encoding="utf-8")
    meta, body = {}, t
    if t.startswith("---"):
        end = t.find("\n---", 3)
        if end != -1:
            try:
                meta = yaml.safe_load(t[3:end]) or {}
            except yaml.YAMLError:
                meta = {}
            body = t[end + 4:]
    return (meta if isinstance(meta, dict) else {}), body


def country_of(rel: str) -> str:
    head = rel.split("/", 1)[0]
    return head if len(head) == 2 else "shared"


def build_graph():
    notes = sorted(WIKI.rglob("*.md"))
    node_type, bodies, labels = {}, {}, {}
    by_name: dict[str, list[str]] = {}     # folded name/alias -> node ids claiming it

    for p in notes:
        meta, body = read_note(p)
        nid = p.relative_to(WIKI).as_posix()
        node_type[nid] = meta.get("type", "other")
        bodies[nid] = body
        labels[nid] = p.stem
        for name in [p.stem] + [str(a).strip() for a in (meta.get("aliases") or [])]:
            by_name.setdefault(name.casefold(), []).append(nid)

    G = nx.Graph()
    for nid, t in node_type.items():
        G.add_node(nid, type=t)

    for nid, body in bodies.items():
        cc = country_of(nid)
        # path links (all generated pages, and most hand-authored ones since Lot 2)
        for m in MDLINK.finditer(body):
            raw = m.group(1) or m.group(2)
            if "://" in raw:
                continue
            target = ((WIKI / nid).parent / unquote(raw)).resolve()
            try:
                tid = target.relative_to(WIKI).as_posix()
            except ValueError:
                continue
            if tid in node_type and tid != nid:
                G.add_edge(nid, tid)
        # wikilinks (hand-authored pages) - resolved own-country-first, like validate
        for m in WIKILINK.finditer(body):
            cands = by_name.get(m.group(1).strip().casefold())
            if not cands:
                continue
            tid = next((c for c in cands if country_of(c) == cc), cands[0])
            if tid != nid:
                G.add_edge(nid, tid)

    G.remove_nodes_from(list(nx.isolates(G)))
    return G, node_type, labels


def draw_graph(G, node_type, labels, mono: str) -> None:
    print(f"graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    pos = nx.spring_layout(G, k=0.14, iterations=120, seed=7)
    deg = dict(G.degree())
    sizes = [10 + 9 * min(deg[n], 90) ** 0.85 for n in G.nodes()]
    colors = [TYPE_COLOR.get(node_type.get(n, "other"), DEFAULT_COLOR) for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(16, 10.5), dpi=160)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=INK, width=0.35, alpha=0.07)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=sizes, node_color=colors,
                           linewidths=0, alpha=0.9)

    # country tag above each cluster. No node count here: the cluster also holds
    # branch/insurer/moc pages, so its size differs from the README's product count
    # and two almost-equal numbers on one figure read as an error. Placement uses
    # medians and a percentile top - a single stray node must not drag the tag away
    # from the visual mass (Switzerland's did).
    for cc in sorted({country_of(n) for n in G.nodes()} - {"shared"}):
        own = [n for n in G.nodes() if country_of(n) == cc]
        if len(own) < 10:
            continue
        xs = sorted(pos[n][0] for n in own)
        ys = sorted(pos[n][1] for n in own)
        cx = xs[len(xs) // 2]
        top = ys[int(len(ys) * 0.9)]
        ax.text(cx, top + 0.05, cc.upper(),
                fontsize=14, fontfamily=mono, color=INK2, ha="center", va="bottom")

    # label only the recognizable brands: the top insurers of each country
    hubs = {}
    for cc in {country_of(n) for n in G.nodes()}:
        insurers = [n for n in G.nodes()
                    if node_type.get(n) == "insurer" and country_of(n) == cc]
        for n in sorted(insurers, key=lambda n: -deg[n])[:4]:
            hubs[n] = labels[n]
    texts = nx.draw_networkx_labels(G, pos, labels=hubs, ax=ax, font_size=7.5,
                                    font_color=INK, font_weight="bold")
    for t in texts.values():
        t.set_path_effects([pe.withStroke(linewidth=2.4, foreground=PAPER)])

    counts = {}
    for n in G.nodes():
        t = node_type.get(n, "other")
        counts[t] = counts.get(t, 0) + 1
    handles = [plt.Line2D([0], [0], marker="o", linestyle="", markersize=7,
                          markerfacecolor=c, markeredgecolor="none",
                          label=f"{t} ({counts.get(t, 0):,})".replace(",", " "))
               for t, c in TYPE_COLOR.items() if counts.get(t)]
    ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=9,
              labelcolor=INK2, prop={"family": mono, "size": 8.5})

    ax.text(0.995, 0.005,
            "fig. 1 · four markets, one linked graph · generated from the committed wiki by assets/make_visuals.py",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8, fontfamily=mono, color=CAP)

    ax.axis("off")
    fig.tight_layout(pad=0.6)
    out = ASSETS / "knowledge-graph.png"
    fig.savefig(out, facecolor=PAPER, bbox_inches="tight")
    print("wrote", out.relative_to(REPO))


def shoot_architecture() -> None:
    """assets/architecture.html -> assets/architecture.png (2x), via Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed; skipping architecture.png")
        return
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1180, "height": 900},
                                device_scale_factor=2)
        page.goto((ASSETS / "architecture.html").as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        height = page.evaluate("document.body.scrollHeight")
        page.set_viewport_size({"width": 1180, "height": height})
        page.screenshot(path=str(ASSETS / "architecture.png"))
        browser.close()
    print("wrote assets/architecture.png")


def main() -> int:
    G, node_type, labels = build_graph()
    draw_graph(G, node_type, labels, register_mono())
    shoot_architecture()
    return 0


if __name__ == "__main__":
    sys.exit(main())
