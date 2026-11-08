# Kiro report: LibreTorrent
START COMMIT: 3003df16
## Steps
- Step 0: baseline matches handover section 2 (methods 4732, REACHABLE 3882, UNREACHABLE 764, UNRESOLVED 86, errors 86, warnings 16, check2 191/131, check4 141, check8 33). b121.py absent, 0 refs in MERGED_PARTS => Case C. javap present.
- Step 2: commit a04a8b05. rebuild.sh all on the main tree (helper could not start: host memory critical). All 12 other apps 0 problems with distinct counts exactly as the Step 2 table; LibreTorrent 60 distinct / 0 problems. Print: prints/step2_check2_all.txt.
- Step 3: commit fa6abe75. All 10 _K_CITE_FORM names unique except FeedParser (2, expected). check 2 60/0 (before Step 2: 93/33, all FeedParser; prints/check2_after_k1.txt), check 4 7 (all FileDescriptorWrapperImpl.close). Labels unchanged: REACHABLE 3882, UNREACHABLE 764, UNRESOLVED 86, SOURCE 620, INFERRED 4112. Warnings 28 (16 graph + 12 verification.csv).
- Step 5: commit c9384b65. REVIEW lines 0, graph warnings 16 -> 15, labels unchanged (3882/764/86, SOURCE 620).
- Step 4: commit 7997c893 (done before Step 1 because it is independent). 7 try-with-resources blocks printed (prints/step4_try_blocks.txt); check 4 7 -> 0 (1666 checked); labels unchanged 3882/764/86.
- Step 1: case C, commit 2a294908. New parts/b121.py (G1-G7 delivery edges from REACHABLE callers, Path A) + D2 entry; parts/b121.md (87 table rows incl. header = 86 methods: REACHABLE 85, UNREACHABLE 1); prints scratch/b121_printed.txt. Also K4 in graph_def.py: 17 stale select-tag citations corrected (6 pointed past the 195-line SelectTagDialog.java). Build: UNRESOLVED 0, errors 0, REACHABLE 3967, UNREACHABLE 765, SOURCE 621, warnings 28 (16 graph + 12 verification.csv).
- Step 6: commit fd4a16b0. 16 graph warnings -> 0: 12 auto edges in parts/k01_warnings.py SUPPRESS (8 Parcel createFromParcel, notifySound, pow, FileItem.toString, read()->toUnsignedByte auto copy) and 5 hand edges in _K6_HAND_DROPS (graph_def.py). Every source is UNREACHABLE or behind an SDK guard false on API 27 (prints/step6_warnings.txt). No label changed.
- Step 7: commit 58a3600a. parts/k02_check8.py prepends a Caller sentence to 28 reasons; check8_names.py: named 33, missing 0. scratch/check8_explained.md has 33 rows.
- Step 8: labels gate PASS at 58a3600a (SUMMARY below). Graph warnings 0; the 12 warnings are verification.csv ones.
- Step 9: commit 558a9939. Old graph built in worktree ../lt_old at a9e8b93d (removed after). Sample: 29 routes (sampler header "29 of 3967 reachable methods"; STATE stratum has 2 methods, so 1 of its 3 places is empty). compare.txt: NEW 7, SAME ROUTE 22, CHANGED 0. route_print.py: 29 prints, grep anymemo printed nothing. Judgments for the 7 NEW routes in scratch/kiro/judgments/; SAME routes carried over after an edge-by-edge comparison with the old graph (scratch/kiro/same_route_diff.txt: only citation-text changes). Table: CORRECT 18, WRONG 9, UNCLEAR 2, fixed 0, rate 9/27 = 0.3333, 457 steps.
- Step 10: commit 704419cd. make_verification.py: N from the sample, rows 1..N, UNRESOLVED asserted 0, label count len(U)+N, note texts updated. Two runs: md5 8dc8fef015c588ba36bc785555ccb35f both times; header type,item,result,confirmed_by,ref,edges,note. Rebuild: warnings 0, "verification.csv rows: path 29, DEVICE 0". A redraw after the log step gave the same 29 methods (said so in readme_notes.md). readme_notes.md 5 headings; LESSONS.md 6 bullets; AGENT_NOTES.md has both exact headings.
- Step 11: commit 12ac6750. ROUTES.csv 29 rows; 17 scripted, 12 unscriptable (9 WRONG, 3 network). Dry run: "LibreTorrent: 29 PASS, 0 FAIL". Generator: scratch/kiro/make_device_routes.py; UI facts printed in scratch/kiro/prints/ui_map.txt.
- Step 12: all final checks pass (FINAL below). Report committed last.

LABELS GATE
```
app LibreTorrent | commit 58a3600a | 2026-11-03 02:51 UTC
methods 4732, pages 1, edges 7303
verdicts: REACHABLE 3967, UNREACHABLE 765
unreachable by kind: branch_never_taken 12, closed_by_api_level 24, closed_by_configuration 1, framework_never_calls 13, no_trigger_in_app 715
labels confirmed by: INFERRED 4111, SOURCE 621
verification label: checked 791, errors found 8 (rate 0.01), unclear 0
verification edge: checked 71, errors found 25 (rate 0.352), unclear 0
verification path: checked 27, errors found 8 (rate 0.296), unclear 0
errors: 0
warnings: 12
exit 0
check 2: citations: 65 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0
check 3: # LibreTorrent: 0 routes flagged
check 4: LibreTorrent: 1655 bytecode-cited edges checked, 549 skipped (lambda / clinit / anonymous), 55 implicit (super / enum / Dagger), 0 where the cited line does not show the callee
check 5-7: DEAD|FRAMEWORK_ONLY lines: 0
check 5-7: FW-MEMORY lines: 0
check 5-7: PENDING lines: 0
check 5-7: STRICT = True line in graph_def.py: 1
check 8 (--callers): 33 of 765 unreachable methods have a bytecode caller outside the set
verification.csv rows: path 27, DEVICE 0
```
## Decisions
- Kiro (2026-11-03): helper model. The runtime refused the requested helper model claude-haiku-5-5 (InvalidModelError, run 2b1adf50f29b71b3). I did not switch helpers to another model; all work was done by the lead alone. Helpers per wave: wave 1 = 2 submitted (0 ran: tools-check cancelled while queued on memory, old-graph refused the model), wave 2 = 0, wave 3 = 0.
- Kiro (2026-11-03): route 5 judged WRONG at step 13 (edge E127a23cd) although first-draw row 5 (same first 13 steps; method not in the final sample) was CORRECT. Evidence: prints/judge_saf.txt.
- Kiro (2026-11-03): routes 9 and 10 UNCLEAR (a tag must already exist; Aegis STATE precedent). Their device scripts create the tag in setup_route_09/10.py.
- Kiro (2026-11-03): device. 3 of the 20 non-WRONG rows are unscriptable (15%, above the 10% aim): route_02 havePiece (needs an HTTP client on the stream server and streamed piece data from a peer), route_08 isUtp (needs a connected BitTorrent peer), route_13 onTorrentMoving lambda (needs a torrent that finishes downloading). Each needs a live swarm on the network.
- Kiro (2026-11-03): device. Routes that tap UI from MainActivity grant READ/WRITE_EXTERNAL_STORAGE (declared at AndroidManifest.xml:16-17): MainActivity.java:177-178 asks for storage on every start while it is not granted, and the system dialog would cover the taps. Torrent-needing routes add a generated torrent in a UI-driving per-route setup (MMEX-B3-UIDRIVE pattern); setup grants storage itself.
- Kiro (2026-11-03): commit-message correction. K1 (fa6abe75) was amended before any later commit to fix its warnings count (28, not 16); no other amend.
- Kiro (2026-11-03): helpers. Host memory stayed CRITICAL (about 1.1-1.7 GB free, spawn gate paused) for the whole run. The two wave-1 helpers I queued (tools-check, old-graph) never started; I cancelled tools-check and did Steps 0-8 myself, in order, as the single writer.
- Kiro (2026-11-03): AddTorrentInfoFragment.showOpenDirErrorDialog is left REACHABLE through the existing edge Ef80b5c5d (guard data == null), mirroring DetailTorrentInfoFragment.showOpenDirErrorDialog. Printed lines (FileManagerViewModel.java:72-107, FileSystemFacadeImpl.java:80-90) suggest data is null only when the public Download dir is missing; reviewer to decide whether both should be branch_never_taken.
- Kiro (2026-11-03): existing auto edges map the FragmentCallback.onFragmentFinished interface call from every dialog's finish() to SelectTagActivity.onFragmentFinished (e.g. Eabda0a81 AddFeedDialog.finish). These over-approximations can enter routes; judged in Step 9.
## Label changes
- 85 methods UNRESOLVED -> REACHABLE (part b121; list in parts/b121.md).
- TorrentInputStream.toUnsignedByte UNRESOLVED -> UNREACHABLE no_trigger_in_app (ruling D2).
- No REACHABLE/UNREACHABLE label flipped in Steps 2-7 (verdict counts printed after each step).
## Route check
- Sample size 29 (seed 20261025). NEW 7 / SAME 22 / CHANGED 0. CORRECT 18 / WRONG 9 / UNCLEAR 2. Fixed 0. Rate (0 + 9) / (18 + 0 + 9) = 9/27 = 0.3333. UNCLEAR rows 9, 10.
## Device
- 29 rows, 17 scripted, 12 unscriptable: 9 "route WRONG as drawn (see route_table.md)" (rows 03, 04, 05, 06, 07, 11, 12, 20, 22) and 3 network (rows 02, 08, 13, reasons in ROUTES.csv). Dry run: LibreTorrent: 29 PASS, 0 FAIL.
- Self-check, 1 script in 3 against the printed route: route_01 checked, route_14 checked, route_18 checked, route_21 checked, route_25 checked, route_28 checked (actions sit on the edges that need them; all other edges are comments).
- Not validated by the dry run: the 7 setup scripts (drycheck only compiles them), tab/notification label matches (noted in each script docstring as live risks).
## Blocked
- Parallel helpers (all waves): not run. Host memory stayed CRITICAL (spawn gate paused) and the helper model claude-haiku-5-5 is not available on this runtime. Consequence: no independent judge/audit of the 7 NEW routes or of the device scripts; the reviewer should audit them.
## FINAL
```
$ bash handoff/ci/rebuild.sh LibreTorrent && cat SUMMARY.txt
app LibreTorrent | commit 12ac6750 | 2026-11-03 03:08 UTC
methods 4732, pages 1, edges 7303
verdicts: REACHABLE 3967, UNREACHABLE 765
unreachable by kind: branch_never_taken 12, closed_by_api_level 24, closed_by_configuration 1, framework_never_calls 13, no_trigger_in_app 715
labels confirmed by: INFERRED 4111, SOURCE 621
verification label: checked 792, errors found 9 (rate 0.011), unclear 2
verification edge: checked 78, errors found 25 (rate 0.321), unclear 0
verification path: checked 27, errors found 9 (rate 0.333), unclear 2
errors: 0
warnings: 0
exit 0
check 2: citations: 65 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0
check 3: # LibreTorrent: 0 routes flagged
check 4: LibreTorrent: 1655 bytecode-cited edges checked, 549 skipped (lambda / clinit / anonymous), 55 implicit (super / enum / Dagger), 0 where the cited line does not show the callee
check 5-7: DEAD|FRAMEWORK_ONLY lines: 0
check 5-7: FW-MEMORY lines: 0
check 5-7: PENDING lines: 0
check 5-7: STRICT = True line in graph_def.py: 1
check 8 (--callers): 33 of 765 unreachable methods have a bytecode caller outside the set
verification.csv rows: path 29, DEVICE 0

$ drycheck | tail -1
LibreTorrent: 29 PASS, 0 FAIL
$ make_verification.py && git status --short verification.csv
(end status)
$ grep ^## readme_notes.md
## What the re-audit changed (compared with the schema 1 graph)
## How the checked paths were chosen
## What waits for a device (API 27)
## Hazard candidates (from reading the code, not reproduced)
## Limits
$ git log --oneline 3003df16..HEAD
12ac6750 LibreTorrent K10 (Step 11): device routes, 29 rows, 17 scripted, dry run 29 PASS 0 FAIL
704419cd LibreTorrent K9 (Step 10): writer for the final table, verification.csv, readme_notes, LESSONS, AGENT_NOTES (local build: methods 4732, REACHABLE 3967, UNREACHABLE 765, unclassified 0, errors 0, warnings 0)
558a9939 LibreTorrent K8 (Step 9): route check on the final graph, 29 routes: CORRECT 18, WRONG 9, UNCLEAR 2, rate 9/27 (local build: methods 4732, REACHABLE 3967, UNREACHABLE 765, unclassified 0, errors 0, warnings 12 (0 graph + 12 verification.csv))
58a3600a LibreTorrent K7 (Step 7): name every check-8 caller (local build: methods 4732, REACHABLE 3967, UNREACHABLE 765, unclassified 0, errors 0, warnings 12 (0 graph + 12 verification.csv))
fd4a16b0 LibreTorrent K6 (Step 6): graph warnings to 0 (local build: methods 4732, REACHABLE 3967, UNREACHABLE 765, unclassified 0, errors 0, warnings 12 (0 graph + 12 verification.csv))
2a294908 LibreTorrent K5 (Step 1): part b121, last 86 labels + select-tag citation fixes (local build: methods 4732, REACHABLE 3967, UNREACHABLE 765, unclassified 0, errors 0, warnings 28 (16 graph + 12 verification.csv))
7997c893 LibreTorrent K3: try-with-resources close() citations (check 4 to 0) (local build: methods 4732, REACHABLE 3882, UNREACHABLE 764, unclassified 86, errors 86, warnings 27 (15 graph + 12 verification.csv))
c9384b65 LibreTorrent K2: non_standard class for data-binding edges (REVIEW warning) (local build: methods 4732, REACHABLE 3882, UNREACHABLE 764, unclassified 86, errors 86, warnings 27 (15 graph + 12 verification.csv))
fa6abe75 LibreTorrent K1: citation form (check 2) and generated-code evidence (check 4) (local build: methods 4732, REACHABLE 3882, UNREACHABLE 764, unclassified 86, errors 86, warnings 28 (16 graph + 12 verification.csv))
a04a8b05 tools: check_citations ROOT_STYLE must not match inside a longer path (Kiro K0; reviewer approval needed before push)
graph warnings: 0
named: 33, missing: 0
```
