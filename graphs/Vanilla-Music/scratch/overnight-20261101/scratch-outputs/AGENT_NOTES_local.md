# AGENT_NOTES (local mirror, Stream D overnight re-verification, Vanilla-Music)
- 2026-11-01 ~07:20 UTC: leaf started; 13 branch files reconstructed via GitHub connector (graph_def.py 249814 B, method_list.json 300063 B = 1473 methods, tools, readme_notes, AGENT_NOTES, LESSONS, make_verification.py), all byte sizes matching branch listing except readme_notes/LESSONS char-count artefact (wc -c matches: 14194 / 5041).
- Build not yet run: USE_AUTO=True in graph_def.py, so auto_calls.json is still required before the build step.
- Build attempt 1 FAILED: `python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla` -> ModuleNotFoundError: No module named 'cases' (graph_def.py line 25 imports cases; tools/cases.py not yet reconstructed). Fetching tools/cases.py next, plus graphs/Vanilla-Music/coverage_baseline.json so sanity_check.csv is reproduced.
- Build attempts 1-3 failed on missing reconstructed inputs (cases.py, calls_all.json, app sources), not on graph errors. Cases() build inputs are 9 .java files; locating their branch paths via connector directory listings.
- Build 1 (after 10 source files reconstructed) PASSES: `python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla` exit 0, methods 1473, pages 44, edges 3429, REACHABLE 1325 / UNREACHABLE 148 (no_trigger_in_app 144, branch_never_taken 4), confirmed_by SOURCE 1157 / INFERRED 316, errors 0, warnings 0, STRICT=True in graph_def.py (no STRICT error, no UNRESOLVED verdict, no STALE path status in methods.csv). Matches branch AGENT_NOTES final counts exactly. Sanity: 1101 ran, 4 contradictions (same 4 as branch notes), 27 ENV-gated-but-ran.
- Sample redrawn: `python3 -I tools/verify_sample.py Vanilla-Music 30 20261025` -> 30 of 1325, 270 distinct edges (seed 20261025). Same 30 methods and order as make_verification.py's P list. NOTE: readme_notes.md says 266 edges and 1158 SOURCE / 315 INFERRED; rebuild says 270 / 1157 / 316 — readme_notes prose counts are stale by those amounts (labels themselves unchanged; only prose numbers differ). Local mirror readme_notes will be corrected to the rebuilt numbers before gen_readme_v2.
- Route sources fetched 44/44 (38 app .java + AndroidManifest.xml + 5 res xml), no 429, no failures. Routes printed via scratch/print_routes.py (own printer; handles comma-space ranges, unlike tools/show_route.py which truncates them — see branch readme_notes Limits).

## 2026-11-01 ~08:50 UTC — routes 11-30 judged, checks run
- Routes 11-30 all CORRECT on re-verification (full judgments in scratch/route_judgments.md). Totals for the 30: 30 correct, 0 newly fixed, 0 wrong, 0 unclear.
- Caveats recorded (labels unchanged): removeSongPosition guard/method-level note; renamePlaylist create-vs-rename dialog entry/exit note.
- check_routes.py: 0 routes flagged (scratch/check_routes.txt).
- Greps on graph_def.py: DEAD|FRAMEWORK_ONLY 0, FW-MEMORY 0, PENDING 0.
- scan_unreachable.py --callers: 3/148, exactly the branch-explained three (scratch/scan_callers.txt).
- check_bytecode_lines.py and scan --all: NOT RUN, blockers written to scratch/check_bytecode_lines_NOT_RUN.md and scratch/scan_all_NOT_RUN.md (partial source tree; running would produce missing-cache artefacts).
- DECISIONS.md: D3 (route judgments + error-rate convention) and D4 (LESSONS.md kept at 8 bullets) written.
- FW batch 6 in progress (11/47 at last check); check_citations.py + verification.csv + rebuild + README still pending on it.
