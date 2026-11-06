"""W2 acceptance check for LibreTorrent (re-audit, 2026-11-06).

Run from the repo root of the W2 copy:
    python3 -I graphs/LibreTorrent/scratch/reaudit/check_w2_acceptance.py

Proves, from graphs/LibreTorrent/out/ (methods.csv best routes +
libretorrent_trigger_graph.json edges):
  1. No REACHABLE method's best route contains a W2-cleared needs_state text.
     (LibreTorrent W2 cleared NO texts -- the only best-route gate text,
     "adapter.getItemCount() > 0", was decided KEEP; see state_gates.csv.
     CLEARED is therefore empty and check 1 is vacuous by construction.)
  2. No REACHABLE method's best route passes through a SETUP_ONLY node,
     except setup-only methods (note "only during the first-run setup").
     SETUP_ONLY is read from graphs/LibreTorrent/graph_def.py (empty set:
     the app has no first-run screens).
  3. Positive control: the kept gate text still gates exactly the 2 methods
     found in the W2 listing, and the methods.csv state column agrees.
  4. The current build_report.txt shows errors: 0 and warnings: 0.
Prints PASS/FAIL lines; exits non-zero on any FAIL.
"""
import ast
import csv
import json
import sys

APP = "graphs/LibreTorrent"
CLEARED = []  # W2 decisions for LibreTorrent: no text cleared (state_gates.csv)
KEPT_TEXT = "adapter.getItemCount() > 0"
KEPT_COUNT = 2

failures = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


# SETUP_ONLY from graph_def.py (literal set only; no module execution)
tree = ast.parse(open(f"{APP}/graph_def.py", encoding="utf-8").read())
setup_only = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "SETUP_ONLY" for t in node.targets
    ):
        v = node.value
        if isinstance(v, ast.Call) and getattr(v.func, "id", "") == "set" and not v.args:
            setup_only = set()
        else:
            setup_only = {elt.value for elt in v.elts}
check("SETUP_ONLY readable from graph_def.py", setup_only is not None,
      f"SETUP_ONLY={setup_only!r}")

g = json.load(open(f"{APP}/out/libretorrent_trigger_graph.json"))
edges = {e["id"]: e for e in g["edges"]}
rows = list(csv.DictReader(open(f"{APP}/out/methods.csv")))
reach = [r for r in rows if r["verdict"] == "REACHABLE"]
check("REACHABLE methods present", len(reach) > 0, f"count={len(reach)}")

# 1. cleared texts on best routes
bad = []
for r in reach:
    for eid in (r["route_edge_ids"] or "").split():
        e = edges.get(eid)
        if e and e.get("needs_state") in CLEARED:
            bad.append((r["method"], eid, e["needs_state"]))
check("no REACHABLE best route contains a cleared needs_state text",
      not bad, f"violations={bad[:3]} (CLEARED={CLEARED!r})")

# 2. SETUP_ONLY nodes on best routes
bad = []
for r in reach:
    nodes = [n.strip() for n in (r["shortest_path"] or "").split(">")]
    hit = [n for n in nodes if n in (setup_only or set())]
    if hit and "only during the first-run setup" not in (r["note"] or ""):
        bad.append((r["method"], hit))
check("no REACHABLE best route passes a SETUP_ONLY node (except setup-only methods)",
      not bad, f"violations={bad[:3]} (SETUP_ONLY={setup_only!r})")

# 3. positive control on the kept gate
hits = set()
for r in reach:
    for eid in (r["route_edge_ids"] or "").split():
        e = edges.get(eid)
        if e and e.get("needs_state") == KEPT_TEXT:
            hits.add(r["method"])
state_col = {r["method"] for r in reach if r["state"] == KEPT_TEXT}
check("kept gate still on the expected REACHABLE best routes",
      len(hits) == KEPT_COUNT, f"methods={sorted(hits)}")
check("methods.csv state column agrees", hits == state_col,
      f"state-column methods={sorted(state_col)}")

# 4. build report
report = open(f"{APP}/out/build_report.txt").read()
check("build_report errors 0", "\nerrors: 0" in report)
check("build_report warnings 0", "\nwarnings: 0" in report)

print("RESULT:", "ALL PASS" if not failures else f"{len(failures)} FAILURES")
sys.exit(1 if failures else 0)
