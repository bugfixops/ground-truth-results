## Overnight re-verification (Stream D, 2026-11-01) — local mirror only, NOT pushed
Rebuilt from connector-reconstructed local copies (no true git clone on the VM).
Build 1: `python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla` — exit 0,
errors 0, warnings 0, STRICT = True, methods 1473, pages 44, edges 3429,
REACHABLE 1325 / UNREACHABLE 148 (no_trigger_in_app 144, branch_never_taken 4),
SOURCE 1157 / INFERRED 316, UNRESOLVED 0, STALE 0 — matching this file's Final
status exactly. Build 2 (after verification.csv): same counts, errors 0,
warnings 0, verification embedded, path SOURCE_OK 30 / UNCHECKED 1295.
Route sample: `python3 -I tools/verify_sample.py Vanilla-Music 30 20261025` — same
30 methods, same order, 270 distinct route edges. Every step of all 30 routes
re-read against freshly fetched cited sources (local printer scratch/print_routes.py,
working around the known tools/show_route.py evidence-regex bug): 30 CORRECT,
0 newly fixed, 0 wrong, 0 unclear. Two method-level caveats recorded, labels
unchanged: SongTimeline.removeSongPosition (guarded LiftAnimator step vs
RemoveAnimator step; coherent path through mRemoveAnimator.start) and
MediaLibrary.renamePlaylist (printed dialog entry is the create flow, exit
callback is the rename callback; coherent rename path exists). No route redrawn
after a fix this run, so the final sample is the initial sample.
verification.csv regenerated ONLY via make_verification.py (exit 0, header
type,item,result,confirmed_by,ref,edges,note, 288 rows): path fixed 19 / correct
11, label correct 178, edge correct 70 / fixed 10 — exactly the branch record.
Logged-convention error rate 19/30 = 0.63 is the branch's own fix history, not
new errors (this run: 0). README regenerated via gen_readme_v2.py (53 lines).
Checks: check_routes.py 0 flagged (build 1 and build 2); greps
DEAD|FRAMEWORK_ONLY / FW-MEMORY / PENDING all 0; scan_unreachable.py --callers
3/148, each already explained in its own reason; check_citations.py PARTIAL —
100 distinct, 1 problem, 0 FW-MEMORY/DYN/UNVERIFIED: ActivityManagerService.java
(1,086,106 B) exceeds the connector display limit, retry failed identically,
affecting only edge E40f400d7's one citation segment (see DECISIONS.md D5).
check_bytecode_lines.py and scan --all NOT RUN (partial source tree; blockers in
scratch/). readme_notes.md prose counts corrected to the rebuild in the local
mirror only (1157/316, 270 edges, and a missed 315 -> 316 in Limits prose);
LESSONS.md reviewed, kept at 8 bullets. DECISIONS.md D1-D5 (Muse's own, for
user/Yang review). No branch file touched, no push, no tick marks.
