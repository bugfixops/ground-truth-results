#!/usr/bin/env python3
"""Dry-run checker for one app's device routes (brief D4, --dry-run).

Usage: python3 -I device/drycheck.py <App> [--root R] [--wemu W] [--out O]
  --root R   repo root (default: derived from this file's location)
  --wemu W   work-emulator checkout (default: $WEMU env, else required)
  --out O    directory for dryrun_report.txt (default: <root>/out/<App>)

For every row of device/routes/<App>/ROUTES.csv it checks:
  1. every edge id exists in graphs/<App>/out/<prefix>_trigger_graph.json;
  2. the edges form a contiguous chain (each edge's dst == next src),
     starting at S_ENTRY and ending at the method node (a trailing
     @VARIANT suffix on the final node is allowed: variant nodes such
     as ChoiceDialog.onRestoreInstanceState@MAIN are the method's node
     reached through one producer chain);
  3. the method exists in graphs/<App>/out/methods.csv;
  4. every listed permission is declared in the app manifest;
  5. every listed fixture exists under $WEMU/fixtures.
Unscriptable rows are not executed: they PASS when their reason is
non-empty (they need no script, edge chain, or fixture check beyond
the reason itself), and the reason is carried into the report line.
Scripted rows must also have a device/routes/<App>/<route>.py script.
With --load-scripts, each scripted script is additionally executed in
dry mode (python3 -I <script> --package drycheck --log <tmp> --dry-run
--outdir <tmp>) to prove it loads under the harness and honours the
route-script invocation contract; a nonzero exit fails the route.

Writes <out>/dryrun_report.txt: one line per route
    <route> PASS
    <route> FAIL <reason>
plus a final line: <App>: N PASS, M FAIL
Exit 0 when M == 0, else 1. Report lines are the contract consumed by
device/run_app.sh --dry-run and by the D9 dry-run acceptance.
"""

import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from route_info import (COLUMNS, PREFIXES, find_manifest, load_routes,  # noqa: E402
                        methods_csv_path, trigger_graph_path)


def check_app(app, root, wemu, load_scripts=False, tmpdir=None):
    import subprocess
    import tempfile
    rows = load_routes(app, root)
    with open(trigger_graph_path(app, root), encoding="utf-8") as f:
        graph = json.load(f)
    edges = {e["id"]: e for e in graph["edges"]}
    with open(methods_csv_path(app, root), newline="", encoding="utf-8") as f:
        methods = {r["method"] for r in csv.DictReader(f)}
    manifest = find_manifest(app, root)
    declared = ""
    if manifest:
        with open(manifest, encoding="utf-8", errors="replace") as f:
            declared = f.read()
    results = []
    for row in rows:
        route, method = row["route"], row["method"]
        if row["status"].startswith("unscriptable"):
            reason = row["status"][len("unscriptable:"):].strip()
            results.append((route, True,
                            "unscriptable: " + reason if reason else
                            "unscriptable with no reason"))
            continue
        problems = []
        script = os.path.join(root, "device", "routes", app, route + ".py")
        if not os.path.isfile(script):
            problems.append("missing script %s" % (route + ".py"))
        if method not in methods:
            problems.append("method not in methods.csv")
        chain = [edges[e] for e in row["edges"].split() if e in edges]
        missing = [e for e in row["edges"].split() if e not in edges]
        if missing:
            problems.append("edge(s) not in trigger graph: %s"
                            % ",".join(missing))
        elif chain:
            if chain[0]["src"] != "S_ENTRY":
                problems.append("first edge src %s != S_ENTRY"
                                % chain[0]["src"])
            for a, b in zip(chain, chain[1:]):
                if a["dst"] != b["src"]:
                    problems.append("chain break %s dst %s != next src %s"
                                    % (a["id"], a["dst"], b["src"]))
                    break
            if chain[-1]["dst"].split("@")[0] != method:
                problems.append("last edge dst %s != method %s"
                                % (chain[-1]["dst"], method))
        if not manifest:
            problems.append("no manifest found")
        else:
            for perm in [p.strip() for p in row["permissions"].split(";")
                         if p.strip()]:
                if perm not in declared:
                    problems.append("permission %s not in manifest" % perm)
        for fix in [p.strip() for p in row["fixtures"].split(";")
                    if p.strip()]:
            if not os.path.exists(os.path.join(wemu, "fixtures", fix)):
                problems.append("fixture missing: %s" % fix)
        if load_scripts and os.path.isfile(script) and not problems:
            tmp = tempfile.mkdtemp(dir=tmpdir)
            proc = subprocess.run(
                [sys.executable, "-I", script, "--package", "drycheck",
                 "--log", os.path.join(tmp, "route.log"),
                 "--outdir", tmp, "--dry-run"],
                capture_output=True, timeout=120)
            if proc.returncode != 0:
                tail = (proc.stderr.decode("utf-8", "replace")
                        if isinstance(proc.stderr, bytes) else proc.stderr)
                problems.append("script dry run failed (%s): %s"
                                % (proc.returncode, tail.strip()[-200:]))
        results.append((route, not problems, "; ".join(problems)))
    return results


def main(argv):
    if not argv:
        sys.stderr.write("usage: drycheck.py <App> [--root R] [--wemu W] [--out O]\n")
        return 1
    app = argv[0]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wemu = os.environ.get("WEMU", "")
    out = None
    load_scripts = False
    i = 1
    while i < len(argv):
        if argv[i] == "--root" and i + 1 < len(argv):
            root = argv[i + 1]
            i += 1
        elif argv[i] == "--wemu" and i + 1 < len(argv):
            wemu = argv[i + 1]
            i += 1
        elif argv[i] == "--out" and i + 1 < len(argv):
            out = argv[i + 1]
            i += 1
        elif argv[i] == "--load-scripts":
            load_scripts = True
        else:
            sys.stderr.write("unknown argument: %s\n" % argv[i])
            return 1
        i += 1
    if not wemu:
        sys.stderr.write("drycheck: need --wemu or $WEMU\n")
        return 1
    if out is None:
        out = os.path.join(root, "out", app)
    os.makedirs(out, exist_ok=True)
    results = check_app(app, root, wemu, load_scripts=load_scripts)
    n_pass = sum(1 for _r, ok, _p in results if ok)
    n_fail = len(results) - n_pass
    lines = []
    for route, ok, problem in results:
        lines.append("%s %s" % (route, "PASS" if ok else "FAIL " + problem))
    lines.append("%s: %d PASS, %d FAIL" % (app, n_pass, n_fail))
    with open(os.path.join(out, "dryrun_report.txt"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
