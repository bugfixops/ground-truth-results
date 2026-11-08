# KIRO FIX SESSION: AnyMemo, round 3 (fix what round 2 got wrong)

AnyMemo only. Same workspace, lock rule, and "Never" list as handoff/KIRO_SESSION_ANYMEMO.md. Every bash command starts with:
touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;

Run every command from /Users/darshan/Desktop/yang/work. Do not touch Aegis or Markor.

## Files you may edit
- graphs/AnyMemo/graph_def.py (F2 and F4 only)
- graphs/AnyMemo/scratch/fix_round2.md (F1 only)
- graphs/AnyMemo/scratch/fix_round3.md (new; your log)
- graphs/AnyMemo/scratch/route_print.py (new; your printer)
- graphs/AnyMemo/scratch/route_print/ (new folder; printer output)
- graphs/AnyMemo/scratch/route_check_final.md (new; the final table)
- graphs/AnyMemo/scratch/kiro_*.txt (new; command outputs)
- graphs/AnyMemo/make_verification.py, verification.csv, readme_notes.md (only when F5 says so)
- graphs/AnyMemo/AGENT_NOTES.md: the last line only (F5, step 6)

## Problems this session fixes
P1. scratch/fix_round2.md says a decision was made by "the orchestrator", "the parent session", or "Option A". No such decision was made. The waiver it describes is not approved.
P2. graph_def.py has 7 matches for the word PENDING, all from the constant C3_LIB_PENDING (lines 2080, 2246, 2248, 2264, 2266, 2282, 2284). The gate requires 0.
P3. The route check in round 2 said 30 of 30 routes are correct. It did not print the source lines for most steps: tools/show_route.py crashes on citations with a comma, and round 2 checked edge lists only. The check must be done again with every step's cited lines printed.
P4. check_routes flags FileBrowserFragment$3.<init>. readme_notes.md calls it a false positive, but no printed lines back that up.

## F0. Start check (no edits)
1. touch ...; stat -f '%Sm' -t '%Y-%m-%d %H:%M:%S' graphs/AnyMemo/graph_def.py
   Record the time in fix_round3.md. (Round 2 changed the file, so it is later than 2026-10-26 23:04:53.)
2. touch ...; python3 -I tools/build_graph.py graphs/AnyMemo anymemo > graphs/AnyMemo/scratch/fix3_build_0.txt 2>&1; then grep -m1 for methods, verdicts, errors, warnings in that file.
   Expected: methods 2207; verdicts REACHABLE 1966, UNREACHABLE 241; errors 0; warnings 0. If not, STOP and report.

## F1. Remove the false attribution (P1)
In scratch/fix_round2.md, find every heading or sentence that says a decision was made by "orchestrator", "orchestrator decision", "parent session", "Decision received", or "Option A". Replace each one with: "Not decided. Open for the user (see Open decisions for the user)." Keep the facts below each one.
At the end of the file, add the section "## Open decisions for the user" with one line for the PENDING gate: "Resolved by the rename in F2 (if F2 is done). Otherwise the user must decide whether to waive the gate."
Check: grep -c -i "orchestrator decision\|parent session\|option a" graphs/AnyMemo/scratch/fix_round2.md must print 0.

## F2. Clear the PENDING gate (P2)
This renames one constant. The brief forbids renames, so run F2 only if the user has approved it. The rename changes identifiers only; the evidence text stays the same.
1. touch ...; grep -c "C3_LIB_PENDING" graphs/AnyMemo/graph_def.py   (expect 7)
2. touch ...; sed -i '' 's/C3_LIB_PENDING/C3_LIB_BINDING_PASS/g' graphs/AnyMemo/graph_def.py
3. touch ...; grep -c "C3_LIB_PENDING" graphs/AnyMemo/graph_def.py (expect 0); grep -c "C3_LIB_BINDING_PASS" graphs/AnyMemo/graph_def.py (expect 7); grep -c "PENDING" graphs/AnyMemo/graph_def.py (expect 0)
4. Build (F0 item 2 command). Expect the same counts as F0: REACHABLE 1966, UNREACHABLE 241, edges 4492, errors 0, warnings 0. If any count differs, undo the rename with sed -i '' 's/C3_LIB_BINDING_PASS/C3_LIB_PENDING/g' graphs/AnyMemo/graph_def.py, rebuild, and report.
Note: the lowercase phrase "pending-bindings pass" is not the gate word; leave it alone.

## F3. Check every route with every step printed (P3)
Do not edit tools/show_route.py. Write graphs/AnyMemo/scratch/route_print.py (run with python3 -I) that does this:
1. Reads the 30 methods from graphs/AnyMemo/scratch/kiro_sample_30_final.txt (the last word on each line after line 1).
2. For each method, reads its route from out/methods.csv (column route_edge_ids) and the edges from out/anymemo_trigger_graph.json.
3. For each step, prints: step number, edge id, source -> target, class (explicit, standard, or non_standard), guard, needs_state, env, and the full evidence text.
4. For each citation in the evidence, including a range after a comma (for example "ui/FileBrowserFragment.java:594, 480"), prints each cited range from the source with line numbers.
   App citations come from final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/ (quote the path; it contains a #). Framework citations come from fw_src/android-8.1.0_r1/. If the framework file is not there, print "framework not printed" for that step.
5. Writes one file per method: graphs/AnyMemo/scratch/route_print/<method, with $ replaced by _>.txt.
Run it for all 30 methods. Then read every printed file and judge every step against its printed lines, including the if, catch, and for conditions around each call. Also check the mistake list in handoff/AGENT_BRIEF_V2.md section 5 for each route.
Verdict per route (same definitions as before):
- correct: every step is supported by its printed lines, guards and gates included
- fixed: a step or guard was wrong or missing; you fixed graph_def.py and the route is now right (F4)
- wrong: wrong and not fixed
- unclear: depends on another app, the keyboard, a WebView engine, or code you cannot read

## F4. Fix, rebuild, redraw (only if F3 found something)
1. For each wrong route: change graph_def.py only at the block that causes it. Build (errors 0, warnings 0). Print the route again with route_print.py. Log in scratch/fix_round3.md: the method, the step, the lines printed, and the change.
2. Redraw the sample: python3 -I tools/verify_sample.py AnyMemo 30 20261025 > graphs/AnyMemo/scratch/kiro_sample_30_final2.txt. Compare it with kiro_sample_30_final.txt. If it differs, print and judge the new methods the same way. Re-read every route whose steps changed.
3. Keep fixing and redrawing until every route in the final draw is correct, or the route is marked unclear with the reason. If a wrong route cannot be fixed in 3 tries, STOP and report.

## F5. Final table, checks, and notes
1. Write graphs/AnyMemo/scratch/route_check_final.md: one table, one row per method in the final draw. Columns: method | steps | steps printed | verdict | printed file | one-line reason. "steps printed" must equal "steps" on every row.
2. Counts for the final draw: correct, fixed, wrong, unclear. Error rate = (fixed + wrong) / (correct + fixed + wrong).
3. If the graph or the sample changed, run python3 -I graphs/AnyMemo/make_verification.py from the work folder and rebuild. verification.csv path rows must equal the final draw.
4. check_routes flagged route, FileBrowserFragment$3.<init>: print the lines of its flagged edges (E078aae8d and Eb8b53150) and the check's text. Then either:
   (a) the lines show the route is right: rewrite its "## Limits" note in readme_notes.md to cite the printed lines, not just "heuristic"; or
   (b) the route is wrong: fix it under F4.
5. Run the checks (commands in handoff/KIRO_SESSION_ANYMEMO.md, step 8): check_citations, check_routes, check_bytecode_lines, the DEAD / FRAMEWORK_ONLY grep, and the PENDING grep. If readme_notes.md changed, run python3 -I tools/gen_readme_v2.py AnyMemo.
6. Replace the last line of graphs/AnyMemo/AGENT_NOTES.md (the line that starts "- 2026-10-27 round 2: DONE") with one line: date, "round 3", the status, "route table scratch/route_check_final.md", and the open items or "none". Status is DONE only if every expected result in R below holds. Otherwise it is NOT DONE and you name the open step.

## R. Expected results (all must hold for DONE)
R1. grep -c "PENDING" graphs/AnyMemo/graph_def.py prints 0.
R2. grep -c "C3_LIB_PENDING" graphs/AnyMemo/graph_def.py prints 0, and C3_LIB_BINDING_PASS prints 7 (only if F2 was run; otherwise state that the gate is still open).
R3. The build prints errors 0 and warnings 0, no STALE line. Methods 2207. REACHABLE and UNREACHABLE counts are stated as they are (1966 and 241 unless F4 changed them).
R4. grep -c -i "orchestrator decision\|parent session\|option a" graphs/AnyMemo/scratch/fix_round2.md prints 0.
R5. scratch/route_check_final.md has one row per method in the final draw. Every row has steps printed = steps, and a printed file.
R6. check_citations: 0 problems; "FW-MEMORY / DYN / UNVERIFIED: 0".
R7. check_routes: 0 flagged, or the one flagged route is explained with printed lines (not only "heuristic").
R8. check_bytecode_lines: 0 bad.
R9. grep -c "DEAD\|FRAMEWORK_ONLY" graphs/AnyMemo/graph_def.py prints 0.
R10. verification.csv path rows = 30 and identical to the final draw; label rows = 241 + 30 = 271 (say so if the sample changed the count).

## STOP AND REPORT
Stop and change nothing more if:
- the F0 build differs from the expected counts;
- the F2 rename changes any count (undo it first);
- a route cannot be fixed in 3 tries;
- a cited source file does not exist.
Write the blocker in graphs/AnyMemo/scratch/fix_round3.md under "## Blocked", then stop.

## FINAL MESSAGE (at most 12 lines, nothing else)
1. Status DONE or NOT DONE, and the open step.
2. Build counts: methods, REACHABLE, UNREACHABLE, errors, warnings.
3. Route table: 30 rows, correct, fixed, wrong, unclear, error rate.
4. The flagged route: result (a) or (b), and the printed lines it rests on.
5. PENDING gate: count, and whether F2 ran.
6. Files changed.
7. Open decisions for the user.
