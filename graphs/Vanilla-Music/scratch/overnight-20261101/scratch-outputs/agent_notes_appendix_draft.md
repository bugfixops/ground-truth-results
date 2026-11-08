## Overnight re-verification (Stream D, 2026-11-01) — local mirror only, NOT pushed
Rebuilt from connector-reconstructed local copies (no true git clone on the VM):
`python3 -I tools/build_graph.py graphs/Vanilla-Music vanilla` — exit 0, errors 0,
warnings 0, STRICT = True, methods 1473, pages 44, edges 3429, REACHABLE 1325 /
UNREACHABLE 148 (no_trigger_in_app 144, branch_never_taken 4), SOURCE 1157 /
INFERRED 316, UNRESOLVED 0, STALE 0. Counts match this file's Final status exactly.
Route sample: `python3 -I tools/verify_sample.py Vanilla-Music 30 20261025` — same
30 methods, same order, 270 distinct route edges. Every step of all 30 routes
re-read against freshly fetched cited sources (local printer scratch/print_routes.py,
working around the known tools/show_route.py evidence-regex bug): 30 CORRECT,
0 newly fixed, 0 wrong, 0 unclear. Two method-level caveats recorded, labels
unchanged: SongTimeline.removeSongPosition (guarded LiftAnimator step vs
RemoveAnimator step; coherent path through mRemoveAnimator.start) and
MediaLibrary.renamePlaylist (printed dialog entry is the create flow, exit
callback is the rename callback; coherent rename path exists). No route redrawn
after a fix this run, so the final sample is the initial sample. Logged-convention
rate (resume-variant fix) from regenerated verification.csv: 19 fixed / 11 correct
/ 0 wrong, 0.63 — the branch's own fix history, not new errors.
Checks: check_routes.py 0 flagged; greps DEAD|FRAMEWORK_ONLY / FW-MEMORY / PENDING
all 0; scan_unreachable.py --callers 3/148, each already explained in its own
reason. check_bytecode_lines.py and scan --all NOT RUN (partial source tree;
blockers in scratch/); check_citations.py pending FW batch 6 at last note.
readme_notes.md prose counts corrected to the rebuild (1157/316, 270 edges) in
the local mirror only. LESSONS.md reviewed, kept at 8 bullets. DECISIONS.md D1-D4
(Muse's own, for user/Yang review). No branch file touched, no push, no tick marks.
