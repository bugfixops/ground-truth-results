KIRO SESSION: finish the schema 2 conversion of the Diary graph. One app only. Follow this exactly and do nothing else.

Workspace: /Users/darshan/Desktop/yang/work. Run every command from there.

READ FIRST, in this order, and nothing else:
1. handoff/SCHEMA_V2.md (the output format)
2. handoff/CONVERSION_RECIPE.md (the steps)
3. graphs/Diary/KIRO_WORKLIST.md (your task list: 54 claims)
4. graphs/Currency/verification.csv and the last 60 lines of graphs/Currency/graph_def.py (a finished example of the log and the hooks)

STATE NOW: graphs/Diary/graph_def.py already ends with a "schema 2" block written by Claude (UNREACHABLE, ENV and STATE kinds, EDIT, CLASSIFY). It builds with errors 0 and warnings 0. Do not rewrite that block unless a step below says so.

YOU MAY EDIT ONLY: graphs/Diary/graph_def.py, graphs/Diary/verification.csv, graphs/Diary/readme_notes.md. Files in graphs/Diary/out/ change only by running the tools. Not tools/, not other apps, not final_java_only/, not ../work-emulator/.

NEVER: download anything; run adb, an emulator or gradle; use tool coverage (monkey_hit, ape_hit, coverage_baseline.json, sanity_check.csv) as evidence for a label; cite a line you did not print; write FW-SRC from memory; create any other file, script or note; refactor or reformat graph_def.py; "improve" the model of the app; start another app; commit or push.

STEPS

1. EVIDENCE. Go through every row of graphs/Diary/KIRO_WORKLIST.md in order and edit graph_def.py as the Action column says:
   S = cite. First print the lines: sed -n "A,Bp" graphs/Diary/.plan/fw_src/android-8.1.0_r1/<path> . If they show what the claim says, cite as FW-SRC <path>:A-B (same style as the existing citations). If they do not support it, make the claim INFERRED and say why.
   I = keep the claim, make the text start with INFERRED, and say what was not read.
   R = delete the DYN segment.
   After every 10 rows run: python3 -I tools/build_graph.py graphs/Diary diary (errors must stay 0) and python3 -I tools/check_citations.py Diary (must say 0 problems).
   Done when check_citations shows "evidence with FW-MEMORY / DYN / UNVERIFIED: 0".

2. STRICT. Add the line STRICT = True at the very end of graph_def.py. Build. Required: errors 0, warnings 0. If TO CLASSIFY lines appear, classify them (kinds from SCHEMA_V2.md) and change nothing else.

3. EDGE CLASSES. If the build prints a REVIEW warning, decide for each listed edge standard or non_standard (rules in SCHEMA_V2.md). Change CLASSIFY only where the default is wrong.

4. READ PATHS. Run python3 -I tools/verify_sample.py Diary 30. For each method it lists run: python3 -I tools/show_route.py Diary "<method>" --dedupe --max 8
   Read every step against the printed source lines, including guards and ENV/STATE gates. Result per path:
   correct = every step is supported.
   fixed = a step was wrong or a guard/context was missing; you corrected graph_def.py, rebuilt, and the new route is right. Fix by splitting a node into @CONTEXT variants, as you did in v1 (example in Currency: onActivityResult@OK and @CANCEL).
   wrong = wrong and not fixed.
   unclear = depends on another app, the IME, the WebView engine, or something you cannot read.
   Then run python3 -I tools/check_routes.py Diary and read every route it flags.

5. LOG (do this last, after the final build, because edge ids change when evidence text changes). Write graphs/Diary/verification.csv with the header exactly: type,item,result,confirmed_by,ref,edges,note
   - one path row per sampled method: item = method, edges = its route_edge_ids from out/methods.csv, ref = the key file:line, confirmed_by = SOURCE (INFERRED for unclear), result as above;
   - one label row per UNREACHABLE method: result correct, ref = its source_ref, after you grep its call sites once more;
   - one label row per sampled reachable method: correct or fixed;
   - one edge row per distinct framework claim you verified (the edge id is in out/*_trigger_graph.json).
   Rebuild. No STALE warning may remain.

6. NOTES. Write graphs/Diary/readme_notes.md with exactly these headings: "## What the re-audit changed (compared with the schema 1 graph)", "## How the checked paths were chosen", "## What waits for a device (API 27)", "## Hazard candidates (from reading the code, not reproduced)" (copy the hazards from archive/graphs_v1_2026-10-25/Diary/out/README.md), "## Limits". Every number must come from out/build_report.txt or from the table in out/README.md. Then run python3 -I tools/gen_readme_v2.py Diary

7. FINAL CHECKS, all must hold: build_graph.py errors 0 and warnings 0; check_citations.py 0 problems; check_routes.py 0 flagged, or each flagged route explained in readme_notes.md; python3 tools/tests/check_v2.py ends with "apps with problems: 0".

STOP AND REPORT if a step needs a file or fact you do not have, if you cannot fix a build error in 3 tries, or if you are tempted to do anything not listed. Write what blocked you under "## Blocked" at the end of readme_notes.md and stop.

FINAL MESSAGE, max 12 lines, nothing else: the counts from out/build_report.txt (verdicts, labels confirmed SOURCE and INFERRED, path status); the verification table (rows, correct, errors found, unclear); one line per edge or route you changed in graph_def.py and why; every claim still INFERRED.
