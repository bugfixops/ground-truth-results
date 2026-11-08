# Stream C phase-2 — Aegis sample 30 + eight checks ATTEMPT

Scope: Aegis ONLY, repo bugfixops/ground-truth-results, branch
work-2026-10-31. Local workdir: ~/workspace/overnight/stream-C/work/
(run from that directory for every command below).
No push, no branch edit, no graph_def.py edit, no device work
(no emulator/adb/APKs/new repos). No stub auto_calls.json was created.
No tick mark was written anywhere in this leaf.

Context read first, in full: ~/workspace/overnight/stream-C/DECISIONS.md
(7 items decided as Muse's own), steps6-10_report.md, logs_gap.md.

## How the scripts were obtained (read this before the table)

Local work/tools/ holds only build_graph.py and build_all.sh — the
check scripts were NOT present locally. Each missing script was fetched
via the GitHub connector only, one file at a time with ~30 s pauses,
no token used/waited for/written anywhere, and saved under scratch/
for execution only (not into work/tools/, not onto the branch):

- tools/check_citations.py — connector SHA 81f52dec7ed9435cfa6da9ba001a6ff44095d1da
- tools/check_routes.py — connector SHA 1e14cdfeb85ceb2f08a1aaa53252f8d7190e19ac
- tools/check_bytecode_lines.py — connector SHA f16d37ba77cafc01bfd1fa1c314c3c66df97fc4b
- tools/show_route.py (dependency imported by check_bytecode_lines.py)
  — connector SHA 141e53a379cdeeebcb02cfbe424114b6033b3a36
- tools/scan_unreachable.py — connector SHA ec3329fc6cffe6a7a1f639873067b0dffa595dc0
- tools/verify_sample.py — connector SHA 9edb841a1dd5b7c1732ef839c926b79d0603d420

No 429 was encountered during this leaf's six connector fetches.
No fetch was retried. Where a usage text says `tools/<script>.py`,
the command below substitutes the scratch copy at the same relative
position; the arguments after the script name are exactly per usage.
Every command's full output is saved verbatim under
~/workspace/overnight/stream-C/scratch/.

Root cause chain for every NOT RUN below: the build (check 1) fails,
so graphs/Aegis/out/ stays empty (verified empty after every run).
Checks 2, 3, 4 and 8 read graphs/Aegis/out/*_trigger_graph.json and
the sample reads graphs/Aegis/out/methods.csv, so they cannot proceed
past opening those files. Nothing below invents a count, a route, a
verdict, or an error rate from a missing build output.

## Summary

| # | Check | Result | Exact reason in one line |
|---|-------|--------|--------------------------|
| 1 | Build | NOT RUN (BLOCKED) | FileNotFoundError: graphs/Aegis/auto_calls.json, build_graph.py:206 |
| 2 | check_citations.py | NOT RUN | IndexError: no graphs/Aegis/out/*_trigger_graph.json to open |
| 3 | check_routes.py | NOT RUN | Same IndexError: no trigger-graph JSON |
| 4 | check_bytecode_lines.py | NOT RUN | First ModuleNotFoundError: show_route; after fetching show_route, same IndexError as 2/3 |
| 5 | Grep DEAD\|FRAMEWORK_ONLY | PASS (0 hits) | grep ran on local graph_def.py; count 0, confirmed with -E |
| 6 | Grep FW-MEMORY | PASS (0 hits) | grep ran on local graph_def.py; count 0 |
| 7 | Grep PENDING | PASS (0 hits) | grep ran on local graph_def.py; count 0 |
| 8 | scan_unreachable.py --all / --callers | NOT RUN (both) | Same IndexError: no trigger-graph JSON |
| S | verify_sample.py Aegis 30 20261025 | NOT RUN | FileNotFoundError: graphs/Aegis/out/methods.csv |

PASS above means only that the named grep ran and returned the stated
count on the local graph_def.py (487286 B, unchanged). It is NOT a
pass of the build, the sample, or any build-dependent check.

## (1) Build — NOT RUN (BLOCKED)

Command (from work/):

    python3 -I tools/build_graph.py graphs/Aegis aegis

Output: scratch/check1_build.txt — exit code 1. Full output verbatim:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/work/tools/build_graph.py", line 731, in <module>
        sys.exit(main(sys.argv))
      File "/home/hatch/workspace/overnight/stream-C/work/tools/build_graph.py", line 343, in main
        add_auto_edges(gdir, edges, e, set(ns['SUPPRESS']))
      File "/home/hatch/workspace/overnight/stream-C/work/tools/build_graph.py", line 206, in add_auto_edges
        auto = json.load(open(os.path.join(gdir, 'auto_calls.json')))
    FileNotFoundError: [Errno 2] No such file or directory: 'graphs/Aegis/auto_calls.json'

This matches the coordinator's expected failure exactly (same file,
same line, same error as scratch/build_baseline2.txt). No build counts
(methods, verdicts, errors, warnings) were printed, so none are claimed.
graphs/Aegis/out/ remains empty. The hardcoded method_list path at
graph_def.py:1582 did NOT fail this run (the pre-existing local symlink
/Users/darshan/Desktop/yang/work -> the workdir resolved it); the sole
remaining build blocker in this run is the missing local auto_calls.json.
No stub was created and no branch file was edited to work around it.

## (2) check_citations.py — NOT RUN

Usage from the script's own docstring (from work/):

    python3 -I tools/check_citations.py <App> [--show]

Command run (scratch copy, no --show flag):

    python3 -I ~/workspace/overnight/stream-C/scratch/check_citations.py Aegis

Output: scratch/check2_citations.txt — exit code 1. Full output:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_citations.py", line 108, in <module>
        sys.exit(main(sys.argv))
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_citations.py", line 64, in main
        g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0]))
    IndexError: list index out of range

Reason: the script reads graphs/Aegis/out/*_trigger_graph.json, which
does not exist because check (1) is blocked. The --show variant was not
run separately because it fails at the identical line before printing
anything. No citation count, distinct-citation count, or problem count
is claimed. (For the record, the local graph_def.py greps in checks
5–7 found 0 occurrences of FW-MEMORY, and 0 of UNVERIFIED/DYN as an
extra check — that is a graph_def.py text fact, not a check_citations
result, and it does not substitute for this check.)

## (3) check_routes.py — NOT RUN

Usage from the script's own docstring (from work/):

    python3 -I tools/check_routes.py <App> [--all]

Command run (scratch copy, without --all):

    python3 -I ~/workspace/overnight/stream-C/scratch/check_routes.py Aegis

Output: scratch/check3_routes.txt — exit code 1. Full output:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_routes.py", line 56, in <module>
        main(sys.argv)
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_routes.py", line 29, in main
        g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0]))
    IndexError: list index out of range

Reason: same missing trigger-graph JSON as check (2); the script also
reads graphs/Aegis/out/methods.csv, which is likewise absent. The
--all variant was not run separately because it fails at the identical
line before any route is walked. No flagged-route count is claimed.

## (4) check_bytecode_lines.py — NOT RUN

Usage from the script's own docstring (from work/):

    python3 -I tools/check_bytecode_lines.py <App> [--all] [--emit]

Command run, first attempt (scratch copy, no flags):

    python3 -I ~/workspace/overnight/stream-C/scratch/check_bytecode_lines.py Aegis

Output: scratch/check4_bytecode_lines.txt — exit code 1. Full output:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_bytecode_lines.py", line 21, in <module>
        import show_route  # noqa: E402
    ModuleNotFoundError: No module named 'show_route'

That failure is a missing local dependency, not a bytecode result, so
tools/show_route.py was fetched via the connector (SHA above, saved to
scratch/show_route.py) and the check was re-run. Second attempt:

    python3 -I ~/workspace/overnight/stream-C/scratch/check_bytecode_lines.py Aegis

Output: scratch/check4_bytecode_lines_retry.txt — exit code 1:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_bytecode_lines.py", line 102, in <module>
        sys.exit(main(sys.argv))
      File "/home/hatch/workspace/overnight/stream-C/scratch/check_bytecode_lines.py", line 47, in main
        g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0]))
    IndexError: list index out of range

Reason after the dependency fix: the same missing trigger-graph JSON
as checks (2) and (3). No checked/mismatch count is claimed, and no
stage-5 figure (3,654 checked / 0 mismatches, from AGENT_NOTES via
logs_gap.md) is carried forward as a current result.

## (5) Grep DEAD / FRAMEWORK_ONLY on graph_def.py — PASS (0 hits)

Commands (from work/):

    grep -n 'DEAD\|FRAMEWORK_ONLY' graphs/Aegis/graph_def.py
    grep -c 'DEAD\|FRAMEWORK_ONLY' graphs/Aegis/graph_def.py

Output: scratch/check5_grep_dead_framework.txt. Result: no matching
lines; count 0. (grep's exit code 1 here means "no matches", not a
failure of the check.) Re-confirmed with grep -E, which also returned
0. This grep runs against the local graph_def.py only and does not
depend on the build.

## (6) Grep FW-MEMORY on graph_def.py — PASS (0 hits)

Commands (from work/):

    grep -n 'FW-MEMORY' graphs/Aegis/graph_def.py
    grep -c 'FW-MEMORY' graphs/Aegis/graph_def.py

Output: scratch/check6_grep_fw_memory.txt. Result: no matching lines;
count 0. Consistent with the hard rule (confirmed_by only SOURCE or
INFERRED; no FW-MEMORY text in the graph file).

## (7) Grep PENDING on graph_def.py — PASS (0 hits)

Commands (from work/):

    grep -n 'PENDING' graphs/Aegis/graph_def.py
    grep -c 'PENDING' graphs/Aegis/graph_def.py

Output: scratch/check7_grep_pending.txt. Result: no matching lines;
count 0.

Extra text checks run at the same time (not part of the assigned
eight, recorded only as graph_def.py text facts): UNVERIFIED count 0,
DYN count 0, file 4982 lines / 487286 B, method_list.json 695547 B.
The local graph_def.py was not modified by any command in this leaf
(size unchanged at 487286 B before and after).

## (8) scan_unreachable.py --all and --callers — NOT RUN (both)

Usage from the script's own docstring (from work/):

    python3 -I tools/scan_unreachable.py <App> [--all] [--refs] [--callers]

Commands run (scratch copy):

    python3 -I ~/workspace/overnight/stream-C/scratch/scan_unreachable.py Aegis --all
    python3 -I ~/workspace/overnight/stream-C/scratch/scan_unreachable.py Aegis --callers

Outputs: scratch/check8_scan_all.txt and scratch/check8_scan_callers.txt,
both exit code 1. --all output:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/scan_unreachable.py", line 115, in <module>
        main(sys.argv)
      File "/home/hatch/workspace/overnight/stream-C/scratch/scan_unreachable.py", line 66, in main
        g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0]))
    IndexError: list index out of range

--callers output is identical except the traceback line (line 52
instead of 66). Reason: the script reads the trigger-graph JSON (and,
for --callers, its bytecode call edges), which does not exist because
check (1) is blocked. No "no other mention" list, no caller list, and
no UNREACHABLE triage result is claimed.

## SAMPLE: verify_sample.py Aegis 30 20261025 — NOT RUN

Usage from the script's own docstring (from work/):

    python3 -I tools/verify_sample.py <App> [N] [seed]

Command run (scratch copy, exact arguments from the task):

    python3 -I ~/workspace/overnight/stream-C/scratch/verify_sample.py Aegis 30 20261025

Output: scratch/sample30.txt — exit code 1. Full output:

    Traceback (most recent call last):
      File "/home/hatch/workspace/overnight/stream-C/scratch/verify_sample.py", line 57, in <module>
        main(sys.argv)
      File "/home/hatch/workspace/overnight/stream-C/scratch/verify_sample.py", line 36, in main
        rows = [r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')) if r['verdict'] == 'REACHABLE']
    FileNotFoundError: [Errno 2] No such file or directory: 'graphs/Aegis/out/methods.csv'

Reason: the sampler reads graphs/Aegis/out/methods.csv, which only a
successful build produces; check (1) is blocked, so no sample was
drawn. Consequences, stated plainly:

- No sample route list exists from this leaf: no 30 routes to print.
- No step was printed, so there is NO verdict table (no
  correct / fixed / wrong / unclear rows) and NO error rate — the
  formula (fixed + wrong) / (correct + fixed + wrong) has no inputs,
  and none are estimated or carried over from round 7 (seed 20261025,
  25 routes, a different sample on an earlier graph state).
- No route was judged, so no fix is proposed, applied, or counted
  here. The fixes described in DECISIONS.md remain DESCRIBED ONLY:
  they were not applied to graph_def.py in this leaf, and no claim
  of a final sample is made.
- A redraw after the last fix is STILL OWED: after any future
  application of the DECISIONS.md graph edits and a successful build,
  a fresh sample must be drawn, every sampled route must be printed
  with show_route and judged step by step, and only then can an
  error rate be computed and a redraw question be answered.

## What was NOT done (explicit)

- No push, no branch edit, no edit to any file outside
  ~/workspace/overnight/stream-C/scratch/ and this file.
- No stub auto_calls.json, no edited graph_def.py, no claimed build
  counts, citation counts, route flags, bytecode mismatches, scan
  results, sample routes, verdicts, or error rate.
- No device work, no emulator/adb/APK/new repo, no token used or
  written anywhere, no 429 encountered, no fetch retried.
- Workdir after all runs: graphs/Aegis/out/ still empty;
  graph_def.py still 487286 B; method_list.json still 695547 B.

## Files written by this leaf

- ~/workspace/overnight/stream-C/checks_phase2.md (this file)
- ~/workspace/overnight/stream-C/scratch/check1_build.txt
- ~/workspace/overnight/stream-C/scratch/check2_citations.txt
- ~/workspace/overnight/stream-C/scratch/check3_routes.txt
- ~/workspace/overnight/stream-C/scratch/check4_bytecode_lines.txt
- ~/workspace/overnight/stream-C/scratch/check4_bytecode_lines_retry.txt
- ~/workspace/overnight/stream-C/scratch/check5_grep_dead_framework.txt
- ~/workspace/overnight/stream-C/scratch/check6_grep_fw_memory.txt
- ~/workspace/overnight/stream-C/scratch/check7_grep_pending.txt
- ~/workspace/overnight/stream-C/scratch/check8_scan_all.txt
- ~/workspace/overnight/stream-C/scratch/check8_scan_callers.txt
- ~/workspace/overnight/stream-C/scratch/sample30.txt
- ~/workspace/overnight/stream-C/scratch/*.py (connector-fetched tool
  copies for execution only) and connector_*_fetch.txt (raw fetch
  records, including connector SHAs)
