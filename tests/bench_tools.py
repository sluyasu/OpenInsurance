#!/usr/bin/env python
"""Warm in-process benchmark of every MCP tool (median + p95 over 50 runs after a
cache-filling warmup). These are the numbers quoted in mcp/README.md; re-run after
touching the server:  .venv/bin/python tests/bench_tools.py"""

import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "mcp"))
import insurance_wiki_mcp as m  # noqa: E402

CASES = [
    ("list_countries", lambda: m.list_countries()),
    ("list_branches", lambda: m.list_branches("be")),
    ("search (title hit)", lambda: m.search("auto familiale", "be")),
    ("search (full-text body scan)", lambda: m.search("tremblement de terre indemnisation", "be")),
    ("get_page", lambda: m.get_page("wiki/be/branches/Auto.md")),
    ("get_product", lambda: m.get_product("be", "ag", "Top Familiale")),
    ("compare_products", lambda: m.compare_products("be", ["Mobility Safe 1", "Confort Auto"],
                                                    "exclusions", ["baloise", "axa"])),
    ("find_overlap", lambda: m.find_overlap("be", ["Police habitation pour le propriétaire",
                                                   "La Police familiale"])),
    ("get_branch_overview", lambda: m.get_branch_overview("be", "auto")),
]
if hasattr(m, "get_coverage"):
    CASES.append(("get_coverage", lambda: m.get_coverage("be", "axa", "Confort Auto", "vol")))
if hasattr(m, "verify_claim"):
    CASES.append(("verify_claim", lambda: m.verify_claim(
        "be", "axa", "Confort Auto", "le vol est couvert en formule omnium")))

N = 50


def main() -> None:
    print(f"{'tool':<34}{'median':>10}{'p95':>10}")
    for name, fn in CASES:
        fn(); fn()  # warmup: fill the read-once caches
        times = []
        for _ in range(N):
            t0 = time.perf_counter()
            fn()
            times.append((time.perf_counter() - t0) * 1000)
        times.sort()
        print(f"{name:<34}{statistics.median(times):>9.2f}ms{times[int(N * 0.95) - 1]:>9.2f}ms")


if __name__ == "__main__":
    main()
