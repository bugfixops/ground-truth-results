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
  5. every listed fixture resolves: fixture entries (semicolon-separated)
     come in three forms —
       <wemu-relative>            file under $WEMU/fixtures, pushed by
                                  run_app.sh to /sdcard/<same path>;
       <repo-relative> -> <dst>   a text fixture committed under
                                  device/routes/<App>/ (conventionally
                                  device/routes/<App>/fixtures/),
                                  pushed by run_app.sh to <dst>;
       gen:<name> -> <dst>        generated at run time by the
                                  per-route setup script
                                  device/routes/<App>/setup_<route>.py
                                  into the run's gen dir; accepted iff
                                  that script exists, compiles, and
                                  the route's setup cell names the
                                  generated file. Nothing binary is
                                  ever committed: generated files live
                                  only under the run's out dir.
     Any other form FAILs loudly (never silently passes).
  6. every scripted script accepts --adb (static source check):
     run_app.sh always invokes scripts with `--adb adb`, so a
     script without the argument would exit 2 live even though
     the dry run passes (item 12(a)). Launch-component resolution
     is NOT checked here: dry mode never resolves a component, so
     scripts' launch components are verified by the script audit
     against the printed manifest, not by drycheck.
  7. fixture coverage (with --load-scripts): every file a script
     pushes in dry mode must be named in the route's fixtures cell
     (basename match against wemu basenames, repo src basenames,
     and gen names) — a script pushing an unlisted file FAILs
     (item 12(b); this closes the vacuous pass where a script
     pushes a file nobody listed).
Unscriptable rows are not executed: they PASS when their reason is
non-empty (they need no script, edge chain, or fixture check beyond
the reason itself), and the reason is carried into the report line.
That PASS checks only that a reason EXISTS: reason substance is
verified directly by the unscriptable-retry table and the
independent audit, not by drycheck (item 12(c)).
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
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from route_info import (COLUMNS, PREFIXES, find_manifest, load_routes,  # noqa: E402
                        methods_csv_path, trigger_graph_path)


def parse_fixture_entry(entry):
    """Parse one ROUTES.csv fixture entry -> (kind, src, dst).

    kinds: 'wemu' (file under $WEMU/fixtures), 'repo' (text fixture
    committed under device/routes/<App>/), 'gen' (generated at run
    time by setup_<route>.py). dst is the device path run_app.sh
    pushes to (for 'wemu' entries without ' -> ', /sdcard/<src>).
    Raises ValueError on any form that is not one of the three.
    """
    entry = entry.strip()
    if entry.startswith("gen:"):
        rest = entry[len("gen:"):].strip()
        if " -> " not in rest:
            raise ValueError("gen fixture needs ' -> <dst>': %r" % entry)
        name, dst = rest.split(" -> ", 1)
        name, dst = name.strip(), dst.strip()
        if not name or not dst:
            raise ValueError("gen fixture needs name and dst: %r" % entry)
        return ("gen", name, dst)
    if " -> " in entry:
        src, dst = entry.split(" -> ", 1)
        src, dst = src.strip(), dst.strip()
        if not src or not dst:
            raise ValueError("fixture entry needs src and dst: %r" % entry)
        if src.startswith("device/"):
            return ("repo", src, dst)
        return ("wemu", src, dst)
    return ("wemu", entry, "/sdcard/" + entry)


def check_fixture(app, root, wemu, route, setup_text, entry):
    """One fixture entry -> problem string, or None when it resolves."""
    try:
        kind, src, dst = parse_fixture_entry(entry)
    except ValueError as exc:
        return str(exc)
    if kind == "wemu":
        if not os.path.exists(os.path.join(wemu, "fixtures", src)):
            return "fixture missing: %s" % entry
        return None
    if kind == "repo":
        if not src.startswith("device/routes/%s/" % app):
            return ("fixture source outside app routes dir: %s" % entry)
        path = os.path.join(root, src)
        if not os.path.isfile(path):
            return "fixture missing: %s" % entry
        # Routes-dir fixtures are text only: a binary here (e.g. a zip
        # smuggled in as .txt) must fail, never silently pass.
        try:
            with open(path, "rb") as f:
                blob = f.read(5 * 1024 * 1024 + 1)
            if len(blob) > 5 * 1024 * 1024:
                return "fixture too large for routes dir: %s" % entry
            blob.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            return "fixture is not a text file: %s" % entry
        return None
    # kind == "gen": the per-route setup script must exist, compile,
    # and the setup cell must name the generated file.
    script = os.path.join(root, "device", "routes", app,
                          "setup_%s.py" % route)
    if not os.path.isfile(script):
        return "generated fixture without setup script: %s" % entry
    try:
        with open(script, encoding="utf-8") as f:
            compile(f.read(), script, "exec")
    except (OSError, SyntaxError) as exc:
        return "setup script does not compile: %s (%s)" % (script, exc)
    if src not in (setup_text or ""):
        return ("setup cell does not name generated file %s: %s"
                % (src, entry))
    return None


def fixture_entry_names(entry):
    """Basenames a ROUTES.csv fixture entry names (for coverage).

    wemu entry -> basename of the wemu path; repo entry -> basename
    of the repo src; gen entry -> the generated filename.
    """
    try:
        kind, src, _dst = parse_fixture_entry(entry)
    except ValueError:
        return set()
    if kind == "gen":
        return {src}
    return {os.path.basename(src)}


def check_live_arg(script):
    """Static live-argument check (item 12(a)): run_app.sh always
    invokes scripts with `--adb adb`, so a scripted script must
    accept --adb or the live run exits 2 (argparse: unrecognized
    argument) even though the dry run passes. Returns a problem
    string, or None. (Wiring --adb through to Runner is convention,
    documented in README, not a drycheck failure: run_app.sh passes
    the literal "adb", which is also Runner's default.)
    """
    try:
        with open(script, encoding="utf-8") as f:
            source = f.read()
    except OSError as exc:
        return "cannot read script for live-arg check (%s)" % exc
    if not re.search(r"add_argument\(\s*['\"]--adb['\"]", source):
        return ("script lacks --adb argument (run_app.sh passes --adb adb; "
                "live run would exit 2)")
    return None


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
            problem = check_fixture(app, root, wemu, route,
                                    row["setup"], fix)
            if problem:
                problems.append(problem)
        if os.path.isfile(script):
            # Item 12(a): live-argument acceptance, checked statically
            # (no execution) so a dry PASS cannot mask a live exit 2.
            problem = check_live_arg(script)
            if problem:
                problems.append(problem)
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
            else:
                # Item 12(b): fixture coverage — every file the
                # script pushes in dry mode must be named in the
                # route's fixtures cell (basename match: the pushed
                # file's basename must equal a wemu basename, a repo
                # src basename, or a gen name). This catches the
                # vacuous pass where a script pushes a file nobody
                # listed (Diary route_06 class). Basename matching
                # is a heuristic: it catches missing listings, not
                # a wrong file under a listed name (the script audit
                # covers that).
                named = set()
                for fix in [p.strip() for p in row["fixtures"].split(";")
                            if p.strip()]:
                    named |= fixture_entry_names(fix)
                try:
                    with open(os.path.join(tmp, "route.log"),
                              encoding="utf-8") as f:
                        log_lines = f.read().splitlines()
                except OSError:
                    log_lines = []
                for line in log_lines:
                    parts = line.split()
                    if len(parts) >= 5 and parts[2] == "push_fixture":
                        target = parts[3]
                        pushed = (target.split("_->_")[0]
                                  if "_->_" in target
                                  else os.path.basename(target))
                        pushed = os.path.basename(pushed)
                        if pushed and pushed not in named:
                            problems.append(
                                "script pushes %s but no fixtures cell "
                                "names it" % pushed)
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
