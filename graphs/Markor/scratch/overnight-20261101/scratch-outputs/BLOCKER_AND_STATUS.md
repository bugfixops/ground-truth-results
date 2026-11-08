# Markor — Stream D status (2026-11-01, local only, NO PUSH)

## Gate: BLOCKED (not reached)
Proposed status line (NOT written to PROGRESS_V2, NOT claimed):
"[K] Markor (labels, route checks and logs DONE <date>; device checks not started; awaiting user tick)"
— do NOT use this line yet: labels, route checks, and logs are all blocked below.

## Exact blocker
- graphs/Markor/auto_calls.json, 2,090,438 bytes, on branch work-2026-10-31
  (repo bugfixops/ground-truth-results, branch head ref seen in listings:
  614a9540d5c72ab1406316cb6f05120493ffcfbe).
- GitHub connector get_file_contents: "File graphs/Markor/auto_calls.json is too
  large to display (2090438 bytes)." An alternate fetch with the blob SHA fails:
  "failed to get git tree: Invalid object requested. SHA must identify a commit
  or a tree." The connector schema has no range/chunk parameter.
- The raw download URL returned by the connector carries a token; per hard
  constraints it was NOT used.
- Same blocker class as Stream C Aegis (auto_calls.json 1,625,494 B, build exit 1).

## Build attempt (exact command, run from local work/ mirror)
- Command: `python3 -I tools/build_graph.py graphs/Markor markor`
  (workdir ~/workspace/overnight/stream-D/Markor/work, with tools/*.py,
  graph_def.py, method_list.json, coverage_baseline.json, and
  scratch/{hier,textcount,dotcount,route_guards}.json all connector-fetched)
- Attempt 1 output (scratch/build_attempt.txt): exit 1, FileNotFoundError for
  graphs/Markor/scratch/hier.json — graph_def.py also needs scratch/*.json
  inputs, which were then fetched.
- Attempt 2 output (scratch/build_attempt2.txt): exit 1,
  `File "graphs/Markor/graph_def.py", line 1293, in <module>:
  for _c in AUTO['calls']: TypeError: 'NoneType' object is not subscriptable`
  because build_graph.py sets AUTO = None when auto_calls.json is absent.
- Printed counts from MY build: NONE (no build_report.txt produced).
  UNRESOLVED / errors / warnings / STALE / STRICT: NOT ESTABLISHED by my run.
- Branch build_report.txt (local mirror, scratch/branch_build_report.txt) says:
  methods 2864, pages 19, edges 6891; REACHABLE 2450, UNREACHABLE 414
  (closed_by_api_level 1, closed_by_configuration 9, no_trigger_in_app 404);
  edge kinds CALL 5631, ENTERS 24, ENTRY 7, FRAMEWORK 1074, GUI 83, INTENT 10,
  LIFECYCLE 39, REGISTER 15, RESULT 4, SYSTEM 4; auto edges 5214 of 6891;
  labels confirmed by INFERRED 2412, SOURCE 452; errors 0, warnings 0.
  These are BRANCH figures, not re-verified by me.

## Counts verified by my own local analysis (not a build)
- method_list.json fetched via connector: 2859 entries.
- Branch readme_notes.md explains 2864 = 2859 + 5 framework nodes
  (IntroActivity.onResume; onCreate/onBind of WrFilesWidgetService and
  TodoWidgetService). Consistent, but the +5 step is branch text, not my build.
- py_compile passes on graph_def.py, all fetched tools, make_verification.py.
- Static AST count of UNREACHABLE dict in fetched graph_def.py: 414 entries
  (404 no_trigger_in_app, 9 closed_by_configuration, 1 closed_by_api_level;
  SOURCE 272, INFERRED 142) — matches branch report's unreachable breakdown.
- SCREENS: 19 (matches branch report's pages 19).
- graph_def.py: USE_AUTO = True, STRICT = True (lines 11-12).

## Route checks (step 2): NOT RUN
- Command that could not run: `python3 -I tools/verify_sample.py Markor 30 20261025`
  — it reads graphs/Markor/out/methods.csv, which was never produced (build
  blocked) and whose branch copy (2,228,936 bytes) is also over the connector
  display limit. No sample_30.txt, no fresh route steps, no error rate from me.
- Branch verification.csv (local mirror) path rows, prior work only:
  30 rows: 13 correct / 17 fixed / 0 wrong (prior error rate 17/30 = 0.567);
  label rows 445: 397 correct / 48 fixed; edge rows 87: 42 correct / 40 fixed /
  5 unclear. Header verified exactly: type,item,result,confirmed_by,ref,edges,note.
  No forbidden confirmed_by (DYN/FW-MEMORY/UNVERIFIED) in the branch file.

## Eight checks
1. build_graph.py 0 errors/0 warnings/no STALE/STRICT=True — NOT RUN (exit 1, see above).
2. check_citations.py — NOT RUN (needs out/*_trigger_graph.json; branch copy
   5,207,767 bytes, over connector limit).
3. check_routes.py — NOT RUN (needs out/methods.csv).
4. check_bytecode_lines.py — NOT RUN (needs out JSON + app sources).
5. grep DEAD|FRAMEWORK_ONLY on graph_def.py — PASS, 0 matches (grep -E).
6. grep FW-MEMORY on graph_def.py — PASS, 0 matches.
7. grep PENDING on graph_def.py — PASS, 0 matches.
   (Saved: scratch/check_greps.txt.)
8. scan_unreachable.py --all and --callers — NOT RUN (needs out JSON + app sources
   in final_java_only; also needs auto_calls-derived graph).

## Logs (step 4): NOT REGENERATED (blocked, see DECISIONS.md D5)
- verification.csv: NOT regenerated. Only legal producer is
  graphs/Markor/make_verification.py (fetched, 81,683 bytes), which reads
  out/markor_trigger_graph.json and out/methods.csv — unavailable. Branch
  verification.csv kept as an untouched local mirror (261,134 bytes, 562 rows).
- readme_notes.md: NOT regenerated (needs gen_readme_v2.py + build outputs).
  Branch copy kept as mirror (25,026 bytes); its five headings in order are:
  What the re-audit changed / How the checked paths were chosen /
  What waits for a device (API 27) / Hazard candidates / Limits.
- LESSONS.md: NOT regenerated. Branch copy kept as mirror (2,050 bytes).
- AGENT_NOTES.md: local mirror copy with an overnight section appended
  (branch file untouched; local file at ../AGENT_NOTES.md).
- gen_readme_v2.py: fetched (9,223 bytes) but NOT run (needs build outputs).

## Files fetched via connector (one at a time, ~30 s pauses, no token)
tools/: build_graph.py, verify_sample.py, check_citations.py,
check_routes.py, check_bytecode_lines.py, scan_unreachable.py, gen_readme_v2.py
(tools/make_verification.py does NOT exist; the producer is
graphs/Markor/make_verification.py).
graphs/Markor/: graph_def.py (269,284 B), method_list.json (673,461 B),
coverage_baseline.json (616,383 B), make_verification.py (81,683 B),
verification.csv, readme_notes.md, AGENT_NOTES.md, LESSONS.md,
scratch/{hier.json (47,128 B), textcount.json (471,959 B),
dotcount.json (35,732 B), route_guards.json (9,718 B)},
out/build_report.txt, out/README.md.
NOT fetched (over connector display limit): auto_calls.json (2,090,438 B),
out/methods.csv (2,228,936 B), out/markor_trigger_graph.json (5,207,767 B),
out/markor_trigger_graph.html (4,653,228 B).
No 429 was hit during this work. No push was made. No branch file was edited.
No tick mark was written anywhere.

## Morning need (single item)
An authorized route for graphs/Markor/auto_calls.json (2,090,438 B) — e.g. a
Mac/full clone — after which the build, sample, eight checks, and logs can be
run exactly as specified. Everything else needed is already reconstructed
locally under ~/workspace/overnight/stream-D/Markor/.
