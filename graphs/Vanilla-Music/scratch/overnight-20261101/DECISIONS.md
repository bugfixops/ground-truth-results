# DECISIONS (Vanilla-Music, Stream D overnight re-verification) — Muse's own decisions, for user/Yang review, never in Yang's name

## D1. Scope of re-verification vs. full source fetch (decided by Muse)
The build itself needs app sources (cases.Cases indexes final_java_only), which the leaf task's step-1 list did not include. Muse fetched: all graph/tool inputs, the 10 Cases() build inputs, the 38 further app .java files + manifest + 5 res XML cited on the 30 sampled routes, and (planned) the 47 FW-SRC files cited in the built graph for check_citations.py. Muse did NOT fetch the remaining ~67 app .java files and the remaining res XML solely to run check_bytecode_lines.py (full) and scan_unreachable.py --all: at ~30 s per connector fetch that is roughly another hour of fetches, on top of the ~90 already done, with rising 429 risk shared with the other 7 leaves. Those two checks are therefore reported NOT-RUN with exact blockers, and the prior session's passes on the byte-identical-count rebuild are cited as carry-over evidence only, not re-claimed. (To be completed after route reading: confirm this decision stands.)

## D2. readme_notes prose counts corrected to the rebuild (labels unchanged)
Branch readme_notes.md said 1158 SOURCE / 315 INFERRED and 266 sample edges; the rebuild prints 1157 / 316 and 270 (union of the 30 routes' route_edge_ids, matching verify_sample.py's header). Muse corrected those three prose numbers in the LOCAL mirror readme_notes.md only; no label, edge, or route changed. AGENT_NOTES.md's final counts (1157/316) already agreed with the rebuild.

## D3. Route judgments: this-run result vs. branch logged convention (decided by Muse)
This run re-read every step of all 30 sampled routes from the rebuilt graph's
printed routes (scratch/routes_30.txt, via the local printer scratch/print_routes.py,
which works around the known tools/show_route.py evidence-regex bug) against the
freshly fetched cited sources. Result: 30 CORRECT, 0 newly fixed, 0 wrong,
0 unclear. Two method-level caveats were recorded and do NOT change any label:
(1) SongTimeline.removeSongPosition step 11 enters SmoothAnimator.start through
startDrag's mLiftAnimator.start() (guarded, and the LiftAnimator assignment is
commented out) while step 13's RemoveAnimator.onStop belongs to the RemoveAnimator
started at lines 1457-1458 — a coherent path exists through mRemoveAnimator.start,
and the graph's route semantics ignore guards and model virtual dispatch per
method; (2) MediaLibrary.renamePlaylist's printed entry is the create-playlist
dialog flow while its exit callback is the rename callback — a coherent rename
path exists (playlist-row Rename -> same dialog with the LibraryActivity$2
callback -> onSuccess). No fix was applied in either case: re-deriving would
change route costs, not verdicts, and no route was redrawn after a fix this run,
so the "final sample" is the initial sample (same 30 methods, same order as
make_verification.py's P list).
Separately, the branch logging convention (readme_notes.md, make_verification.py)
logs a sampled path as 'fixed' when its route runs through the systemic onResume
fix, even though it reads correct after the fix. Under that convention the
regenerated verification.csv path rows are 19 fixed / 11 correct / 0 wrong,
error rate (fixed+wrong)/(correct+fixed+wrong) = 19/30 = 0.63 — identical to the
branch record. Muse reports BOTH rates and does not conflate them: this-run
re-verification found 0 new errors; the 0.63 is the logged-convention rate
carried from the branch's own fix history, not new errors found this run.
Confirmed from the regenerated verification.csv (make_verification.py exit 0):
Counter path fixed 19 / path correct 11, label correct 178, edge correct 70 /
edge fixed 10 — exactly the branch record. The D3 numbers above stand as written.


## D4. LESSONS.md kept at 8 bullets (decided by Muse)
The local mirror LESSONS.md already has 8 bullets, within the required 3-8.
This run confirmed the same lessons rather than adding new ones (show_route.py
evidence-regex bug worked around with the local printer; scan --callers' 3
flagged callers each already explained in the method's own reason; tool coverage
contradictions are the same 4 methods as the build's sanity check prints), so
no bullet was added or removed. This run's one new observation class — routes
that are valid at method level (guards ignored, virtual dispatch per method)
while individual guard combinations on the printed chain do not all fire
together (removeSongPosition, renamePlaylist) — is recorded in
scratch/route_judgments.md and the local AGENT_NOTES, not as a 9th bullet.

## D5. check_citations.py reported PARTIAL, not pass, over one unfetchable FW file (decided by Muse)
FW batch 6 finished 47/47 with one failure: ActivityManagerService.java
(1,086,106 B) exceeds the connector get_file_contents display limit ("too large
to display"); a single retry failed identically, and the suggested raw URL is
unusable (private repo, no token allowed). The batch-6 list also missed
HandlerThread.java (5,279 B); the checker's own enumeration caught that gap and
the file was fetched, after which the re-run reads: 100 distinct citations,
1 problem, 0 FW-MEMORY/DYN/UNVERIFIED. The single problem is edge E40f400d7
(S_LIBRARY_PAUSED -> PlaybackService.onDestroy), whose ActivityManagerService
:22975 segment (stopInBackgroundLocked) is unverified locally; its other two
segments (ActiveServices, ActivityThread:3504) are held and verified. Muse does
NOT claim check_citations.py as passed and does NOT change the onDestroy label:
the gate is reported as partial on this one check, with the exact blocker, for
the parent to decide (a full checkout, or an authorised large-file route, would
close it). No public-AOSP lookup was substituted for the branch citation.
