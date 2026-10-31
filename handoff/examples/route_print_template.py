#!/usr/bin/env python3
# Route printer template: one copy per app. Set the constants below for the app.
# Run from the work folder:  python3 -I graphs/<App>/scratch/route_print.py
#
# For each of the 30 methods in scratch/kiro_sample_30_final.txt it reads the
# route (route_edge_ids) from out/methods.csv and the edges from
# out/anymemo_trigger_graph.json, and for every step prints:
#   step number, edge id, source -> target, class, guard, needs_state, env,
#   and the FULL evidence text.
# For every citation in the evidence -- INCLUDING ranges after a comma
# (e.g. "ui/FileBrowserFragment.java:594, 480") -- it prints each cited range
# from the source with line numbers.
#   App citations  (SRC ...)    resolve under APP_BASE.
#   Framework      (FW-SRC ...) resolve under FW_BASE; "framework not printed"
#                               if the file is absent.
# One output file per method is written to scratch/route_print/<method>.txt
# with '$' replaced by '_'.

import csv
import json
import os
import re

WORK = os.getcwd()
GDIR = os.path.join(WORK, "graphs", "AnyMemo")
SAMPLE = os.path.join(GDIR, "scratch", "kiro_sample_30_final.txt")
METHODS_CSV = os.path.join(GDIR, "out", "methods.csv")
GRAPH_JSON = os.path.join(GDIR, "out", "anymemo_trigger_graph.json")
OUT_DIR = os.path.join(GDIR, "scratch", "route_print")

APP_BASE = os.path.join(
    WORK,
    "final_java_only", "AnyMemo", "app", "AnyMemo-#10.12.2",
    "app", "src", "main", "java", "org", "liberty", "android", "fantastischmemo",
)
# Some citations give a bare class file (e.g. "AMApplication.java:56-60") whose
# real path is under a sub-package (common/), and AndroidManifest.xml lives at
# the module root (app/src/main/).  Index the whole app module by basename and
# by "/<suffix>" so both forms resolve to the real file.
APP_MODULE = os.path.join(
    WORK, "final_java_only", "AnyMemo", "app", "AnyMemo-#10.12.2", "app", "src", "main",
)
FW_BASE = os.path.join(WORK, "fw_src", "android-8.1.0_r1")

_APP_INDEX = None


def app_index():
    global _APP_INDEX
    if _APP_INDEX is None:
        idx = {}
        for root, _dirs, files in os.walk(APP_MODULE):
            for fn in files:
                full = os.path.join(root, fn)
                idx.setdefault(fn, []).append(full)
        _APP_INDEX = idx
    return _APP_INDEX


def resolve_app(path):
    """Resolve an app citation path to a real file, or None.

    Tries: direct join under the fantastischmemo package base; then basename
    lookup in the app module index (prefer a unique match, else one whose tail
    equals the citation path)."""
    direct = os.path.join(APP_BASE, path)
    if os.path.exists(direct):
        return direct
    base = os.path.basename(path)
    cands = app_index().get(base, [])
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    # multiple same-named files: prefer one whose path ends with the citation
    norm = path.replace("\\", "/")
    for c in cands:
        if c.replace("\\", "/").endswith("/" + norm) or c.replace("\\", "/").endswith("/" + base):
            if c.replace("\\", "/").endswith("/" + norm):
                return c
    return cands[0]

# A citation = a path ending in .java or .xml, then ':', then one or more
# comma-separated ranges (num or num-num).  Whitespace after commas allowed.
CITE = re.compile(
    r"(?P<path>[\w./$#-]+\.(?:java|xml)):"
    r"(?P<ranges>\d+(?:-\d+)?(?:\s*,\s*\d+(?:-\d+)?)*)"
)
# Prefix markers tell us app (SRC) vs framework (FW-SRC).
MARKER = re.compile(r"\bFW-SRC\b|\bSRC\b")


def load_methods():
    rows = {}
    with open(METHODS_CSV, newline="") as fh:
        for row in csv.DictReader(fh):
            rows[row["method"]] = row
    return rows


def load_edges():
    g = json.load(open(GRAPH_JSON))
    return {e["id"]: e for e in g["edges"]}


def sample_methods():
    out = []
    with open(SAMPLE) as fh:
        for i, line in enumerate(fh):
            line = line.rstrip("\n")
            if i == 0 or not line.strip():
                continue
            out.append(line.split()[-1])
    return out


def citations_with_kind(evidence):
    """Yield (kind, path, [(a,b), ...]) for each citation, kind is 'app' or 'fw'.

    The citation inherits the kind of the nearest preceding SRC / FW-SRC marker.
    """
    # record marker positions and kinds
    markers = [(m.start(), m.group(0)) for m in MARKER.finditer(evidence)]

    def kind_at(pos):
        kind = "app"  # default to app when no marker precedes
        for mpos, mtxt in markers:
            if mpos <= pos:
                kind = "fw" if mtxt == "FW-SRC" else "app"
            else:
                break
        return kind

    for m in CITE.finditer(evidence):
        path = m.group("path")
        ranges = []
        for part in m.group("ranges").split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-", 1)
                ranges.append((int(a), int(b)))
            else:
                n = int(part)
                ranges.append((n, n))
        yield kind_at(m.start()), path, ranges


def print_range(lines, a, b):
    out = []
    for n in range(a, b + 1):
        if 1 <= n <= len(lines):
            out.append("    %5d: %s" % (n, lines[n - 1].rstrip("\n")))
        else:
            out.append("    %5d: <line out of range (file has %d lines)>" % (n, len(lines)))
    return out


def emit_citation(w, kind, path, ranges):
    if kind == "fw":
        full = os.path.join(FW_BASE, path)
        label = "FW-SRC"
    else:
        full = resolve_app(path)
        label = "SRC"
    rng = ", ".join("%d-%d" % (a, b) if a != b else "%d" % a for a, b in ranges)
    w("  cite [%s] %s:%s" % (label, path, rng))
    if full is None or not os.path.exists(full):
        if kind == "fw":
            w("    framework not printed")
        else:
            w("    SOURCE FILE NOT FOUND for citation: %s" % path)
        return False
    if kind != "fw" and os.path.realpath(full) != os.path.realpath(os.path.join(APP_BASE, path)):
        w("    (resolved to %s)" % os.path.relpath(full, WORK))
    with open(full, errors="replace") as fh:
        lines = fh.readlines()
    for a, b in ranges:
        for ln in print_range(lines, a, b):
            w(ln)
    return True


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    methods = sample_methods()
    mrows = load_methods()
    edges = load_edges()

    for method in methods:
        safe = method.replace("$", "_")
        path_out = os.path.join(OUT_DIR, safe + ".txt")
        buf = []
        w = buf.append
        row = mrows.get(method)
        w("METHOD: %s" % method)
        if row is None:
            w("  (not found in methods.csv)")
            open(path_out, "w").write("\n".join(buf) + "\n")
            continue
        w("verdict: %s   steps_from_launch: %s" % (row["verdict"], row["steps_from_launch"]))
        eids = row["route_edge_ids"].split()
        w("route steps: %d edges" % len(eids))
        w("=" * 70)
        for i, eid in enumerate(eids, 1):
            e = edges.get(eid)
            w("")
            w("STEP %d  edge %s" % (i, eid))
            if e is None:
                w("  (edge id not found in graph json)")
                continue
            w("  %s -> %s" % (e.get("src"), e.get("dst")))
            w("  class: %s   kind: %s" % (e.get("edge_class"), e.get("kind")))
            w("  guard: %s" % e.get("guard"))
            w("  needs_state: %s" % e.get("needs_state"))
            w("  env: %s" % e.get("env"))
            ev = e.get("evidence") or ""
            w("  evidence: %s" % ev)
            cits = list(citations_with_kind(ev))
            if not cits:
                w("  (no file:line citations in evidence)")
            for kind, p, ranges in cits:
                emit_citation(w, kind, p, ranges)
        open(path_out, "w").write("\n".join(buf) + "\n")
        print("wrote %s (%d steps)" % (path_out, len(eids)))


if __name__ == "__main__":
    main()
