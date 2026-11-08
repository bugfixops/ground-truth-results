# Currency — eight checks (local re-check, 2026-11-01, branch work-2026-10-31)

Build command: `python3 -I tools/build_graph.py graphs/Currency Currency`
(from ~/workspace/overnight/stream-D/Currency, on connector-reconstructed
copies of graph_def.py, method_list.json, auto_calls.json, verification.csv,
readme_notes.md, tools/*.py, app source, DATASET.txt, and the cited AOSP files).

Build printed counts: methods 145, pages 22, edges 393.
Verdicts: REACHABLE 140, UNREACHABLE 5 (branch_never_taken 1,
framework_never_calls 3, no_trigger_in_app 1). Labels confirmed by:
SOURCE 144, INFERRED 1. Path status: SOURCE_OK 24, UNCHECKED 116, STALE 0.
Evidence: FW-SRC 76, INFERRED 3, SRC 314. Errors 0, warnings 0.
STRICT = True in graph_def.py (line 20); strict mode produced no error.

1. build_graph.py — PASS. 0 errors, 0 warnings, STALE 0, STRICT=True
   (output: scratch/build_1.txt, re-run scratch/build_2.txt identical).
2. check_citations.py — PARTIAL (not a graph failure). First run: 41
   distinct citations, 41 problems, all "file not held" (no fw_src tree
   locally), 0 unbacked-evidence. After reconstructing the cited AOSP
   files: 41 distinct, 2 problems, both "file not held:
   am/ActivityManagerService.java" — that file is 1,086,106 B, over the
   connector display limit, and its token-bearing download URL was not
   used (connector-only rule). Library citations not checked: 4.
   Unbacked evidence (FW-MEMORY/DYN/UNVERIFIED): 0.
   Output: scratch/check2_citations.txt.
3. check_routes.py — PASS. 0 routes flagged (output: scratch/check3_routes.txt).
4. check_bytecode_lines.py — PASS (vacuous). 0 bytecode-cited edges
   checked, 0 bad — the build adds 0 auto edges, so no edge carries a
   `(bytecode)` citation (output: scratch/check4_bytecode.txt).
5. grep DEAD|FRAMEWORK_ONLY on graph_def.py — PASS. Count 0
   (output: scratch/check5_7_greps.txt).
6. grep FW-MEMORY on graph_def.py — PASS. Count 0.
7. grep PENDING on graph_def.py — PASS. Count 0.
8. scan_unreachable.py — PASS with explanations.
   --all: 5 UNREACHABLE methods triaged; hits are same-name overloads
   (ChartParser.startParser, getItem) or the already-explained dead
   else-branch (Singleton.getList), plus onBind with no other mention.
   --callers: 1 of 5 has a bytecode caller outside the set
   (Singleton.getList <- ChartActivity.onCreate), explained by its
   branch_never_taken reason (ChartActivity.java:163-177 re-read).
   Outputs: scratch/check8_scan_all.txt, scratch/check8_scan_callers.txt.

Logs:
- verification.csv: local copy of the branch file, UNCHANGED (98 rows;
  header exactly type,item,result,confirmed_by,ref,edges,note). NOT
  regenerated: tools/make_verification.py does not exist on the branch
  (verified via tools/ directory listing). New path judgements are in
  scratch/route_judgements.md instead (see DECISIONS.md D1).
- readme_notes.md: local copy updated with a dated 2026-11-01 re-check
  paragraph; five headings in original order; generated README via
  gen_readme_v2.py (exit 0, 51 lines) at graphs/Currency/out/README.md,
  copied to scratch/README_generated.md.
- LESSONS.md: scratch/LESSONS.md (6 bullets).
- AGENT_NOTES.md: scratch/AGENT_NOTES.md (this run's step log).

Gate: BLOCKED on two tooling items only — (a) check_citations cannot fully
pass without ActivityManagerService.java (oversize for the connector);
(b) verification.csv cannot be regenerated without make_verification.py.
Labels, route checks (error rate 0.0), and the other six checks pass.
No branch file was edited and nothing was pushed.
