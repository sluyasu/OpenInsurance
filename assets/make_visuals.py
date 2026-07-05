#!/usr/bin/env python
"""Regenerate the README visuals from the live wiki.

Outputs:
  assets/knowledge-graph.png  - force-directed graph of the whole wiki (Obsidian-style)

Deps (not part of the core pipeline): pip install networkx matplotlib scipy
Run: python assets/make_visuals.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parent.parent
ROOTS = [REPO / "wiki", REPO / "_meta" / "universal-glossary"]
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")

TYPE_COLOR = {
    "product": "#6366f1",       # indigo
    "insurer": "#f59e0b",       # amber
    "branch": "#10b981",        # green
    "regulation": "#ef4444",    # red
    "concept": "#22d3ee",       # cyan
    "moc": "#a78bfa",           # violet
}
DEFAULT_COLOR = "#64748b"


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


def main() -> int:
    notes = []
    for root in ROOTS:
        if root.is_dir():
            notes += list(root.rglob("*.md"))

    resolve = {}          # name/alias -> node id (stem)
    node_type = {}
    bodies = {}
    branch_labels = {}
    # country branch labels resolve to branch pages
    for cc_dir in (REPO / "sources").glob("*"):
        cy = cc_dir / "_country.yml"
        if cy.is_file():
            for b in (yaml.safe_load(cy.read_text(encoding="utf-8")) or {}).get("branches", {}).values():
                if b.get("label"):
                    branch_labels[b["label"]] = b["label"]

    for p in notes:
        meta, body = read_note(p)
        nid = p.stem
        node_type[nid] = meta.get("type", "other")
        bodies[nid] = body
        resolve.setdefault(nid, nid)
        for a in meta.get("aliases") or []:
            resolve.setdefault(str(a).strip(), nid)

    G = nx.Graph()
    for nid, t in node_type.items():
        G.add_node(nid, type=t)
    for nid, body in bodies.items():
        for m in WIKILINK.finditer(body):
            target = resolve.get(m.group(1).strip())
            if target and target != nid:
                G.add_edge(nid, target)

    # drop isolated nodes for a cleaner picture
    G.remove_nodes_from(list(nx.isolates(G)))
    print(f"graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    pos = nx.spring_layout(G, k=0.45, iterations=200, seed=7)
    deg = dict(G.degree())
    sizes = [30 + 14 * deg[n] for n in G.nodes()]
    colors = [TYPE_COLOR.get(node_type.get(n, "other"), DEFAULT_COLOR) for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(16, 11), dpi=150)
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#30363d", width=0.6, alpha=0.7)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=sizes, node_color=colors,
                           linewidths=0, alpha=0.95)
    # label only the hubs (branches, insurers, MOCs)
    hubs = {n: n for n in G.nodes()
            if node_type.get(n) in ("branch", "insurer", "moc") and deg[n] >= 3}
    nx.draw_networkx_labels(G, pos, labels=hubs, ax=ax, font_size=7,
                            font_color="#e6edf3", font_weight="bold")
    handles = [plt.Line2D([0], [0], marker="o", linestyle="", markersize=9,
                          markerfacecolor=c, markeredgecolor="none", label=t.capitalize())
               for t, c in TYPE_COLOR.items()]
    leg = ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=10,
                    labelcolor="#e6edf3")
    ax.set_title("openinsurance-wiki  ·  the insurance knowledge graph",
                 color="#e6edf3", fontsize=16, pad=16)
    ax.axis("off")
    fig.tight_layout()
    out = REPO / "assets" / "knowledge-graph.png"
    fig.savefig(out, facecolor="#0d1117", bbox_inches="tight")
    print("wrote", out.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
