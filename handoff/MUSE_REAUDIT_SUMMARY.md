# Re-audit of five apps: summary (Kiro)

**Read "Final state" at the end first.** Every section before it is labelled "Round 1 state (historical)": it records the state at that time and is not updated (for example its "Routes re-verified: none yet" and "Reachable audit: drawn, not checked" are no longer true).

Kiro took over from Muse at `e0866b9c` (W1 done; W2 done for LibreTorrent, AnkiDroid and MMEX). Kiro worked alone: no helpers could start (host memory critical, spawn gate paused), so every decision below is self-checked only, and every check the brief gives to a second agent is marked "second: pending reviewer". The session ran on its default model, not `claude-haiku-5-5` (the session cannot switch models).

Round 1 covers W2 to W7. CI of round 1: `9371563e` (built `018a3e43`): all 13 apps at 0 errors; the eight other apps at 0 warnings; the five apps warn only on stale `verification.csv` paths (W8 point 2); checks 2 and 4 at 0; `check_unchanged_apps.py` prints ALL UNCHANGED.

The tuning half of the sample (`review/sample_tune/`) never arrived on the branch, so W0, the round measurement (W8 point 5) and the agreement numbers could not be run.

## Round 1 state (historical): class shares over never-run methods

Classes follow `review/TASK_NOTE.md`; "before" is the CI output at `e0866b9c`, "after" is CI `9371563e` (`tools_dev/reaudit_shares.py e0866b9c`).

| App | never-run | before: dead / config / env / state / library / gui (%) | after (%) |
|---|---|---|---|
| Aegis | 2,244 | 20.4 / 0.0 / 7.8 / 69.6 / 0.9 / 1.3 | 20.8 / 0.0 / 11.6 / 8.2 / 11.9 / 47.5 |
| AmazeFileManager | 1,849 | 23.9 / 0.5 / 1.9 / 0.2 / 1.1 / 72.5 | 24.1 / 0.5 / 3.3 / 2.7 / 3.5 / 66.0 |
| AnkiDroid | 2,175 | 38.8 / 3.0 / 9.0 / 33.1 / 0.0 / 16.1 | 38.8 / 3.0 / 8.8 / 3.1 / 0.5 / 45.7 |
| LibreTorrent | 2,652 | 27.8 / 0.9 / 70.8 / 0.0 / 0.4 / 0.0 | 27.8 / 0.9 / 3.9 / 25.2 / 41.4 / 0.7 |
| MMEX | 3,999 | 20.8 / 0.2 / 1.9 / 11.5 / 11.2 / 54.5 | 20.8 / 0.2 / 2.5 / 2.0 / 22.5 / 52.0 |
| weighted (`review/measure.py` weights) | | 27.3 / 1.1 / 20.4 / 20.4 / 2.9 / 27.8 | 27.4 / 1.1 / 5.8 / 8.6 / 17.0 / 40.2 |

Read with care: W2 removed the setup and baseline gates (Aegis's intro gates sat on about 1,500 best routes, AnkiDroid's sample-deck gates on about 1,600), and W7's guard work is mostly still open (4,814 flagged steps PENDING). Until those guards are judged, gui is over-counted: the review's "too much gui" finding is not yet fixed by this round.

### Round 1 state (historical): after the reviewer's round-1 fixes and W7 round 2 (local builds, not yet CI)

The try rule now counts every guard of a step line (242 rows back to PENDING), the LibreTorrent AndroidX vias are standard, and the flagged steps were judged in impact order (number of never-run targets using a step) until about 90% of the flagged target-uses per app were judged. A tool bug was found and fixed on the way: `guard_judge.py` had cut 43 judged STATE/ENV gate texts at a ';' and kept them off the graph; they are applied now (REAUDIT-W7-JUDGEFIX).

| App | never-run | after round 2: dead / config / env / state / library / gui (%) | W7 judged rows | decision rows: NONE / STATE / ENV / DEAD / PENDING | flagged target-uses judged |
|---|---|---|---|---|---|
| Aegis | 2,244 | 20.8 / 0.0 / 21.1 / 16.7 / 8.6 / 32.8 | 155 | 240 / 14 / 15 / 0 / 858 | 95.8% |
| AmazeFileManager | 1,849 | 24.1 / 1.0 / 7.5 / 7.1 / 3.4 / 56.9 | 398 | 377 / 38 / 25 / 4 / 538 | 89.8% |
| AnkiDroid | 2,175 | 38.8 / 3.0 / 11.5 / 10.0 / 0.3 / 36.4 | 150 | 186 / 21 / 17 / 0 / 728 | 89.8% |
| LibreTorrent | 2,652 | 27.8 / 0.9 / 6.3 / 27.1 / 35.2 / 2.6 | 202 | 195 / 19 / 11 / 0 / 569 | 89.3% |
| MMEX | 3,999 | 20.8 / 0.2 / 3.7 / 11.2 / 14.3 / 49.9 | 189 | 205 / 19 / 12 / 0 / 1,268 | 89.5% |
| weighted | | 27.4 / 1.2 / 9.2 / 14.7 / 13.2 / 34.3 | 1,094 | | |

The PENDING rows that remained (3,961) were the long tail: each is used by few never-run targets (mostly 1 to 3). The gui share is still over-counted, and the size of the over-count is not known yet: re-reading the 20 changed AmazeFileManager sample routes (W8) and the reviewer's round-2 fixes moved its state share from 7.1% to 27.4% (local builds), far more than the share of flagged target-uses that was still PENDING.

### Round 1 state (historical): after the reviewer's round-2 check (local builds, not yet CI)

"Covered by a gate earlier on the route" is no longer a NONE reason (REAUDIT-R2-NONE): the rows that said so and left gui/library targets on their routes were re-judged one step per line. AmazeFileManager drops 154 INFERRED "framework calls ... after construction" edges (REAUDIT-R2-INFERRED). The pre-screen now follows one helper-call level and was re-run on the current build; the steps it found on the current best routes were added (Aegis 105, AmazeFileManager 199, AnkiDroid 154, LibreTorrent 85, MMEX 137), so the judged share of flagged target-uses fell again (Aegis 95.3%, AmazeFileManager 77.0%, AnkiDroid 83.6%, LibreTorrent 86.6%, MMEX 87.0%).

| App | dead / config / env / state / library / gui (%) |
|---|---|
| Aegis | 20.8 / 0.0 / 22.5 / 16.7 / 8.4 / 31.6 |
| AmazeFileManager | 24.1 / 1.0 / 11.5 / 27.2 / 3.7 / 32.5 |
| AnkiDroid | 38.8 / 3.0 / 12.3 / 11.1 / 0.3 / 34.4 |
| LibreTorrent | 27.8 / 0.9 / 11.5 / 29.2 / 28.0 / 2.6 |
| MMEX | 20.8 / 0.2 / 4.6 / 13.3 / 12.6 / 48.6 |
| weighted | 27.4 / 1.2 / 11.6 / 19.0 / 11.1 / 29.6 |

NONE rows were also rewritten one step per line with their own reason and file:line (LibreTorrent, MMEX, Aegis and AnkiDroid in full; AmazeFileManager: the 150 rows that decide a class, the 142 rows that shared a batch text were rewritten in round 5: 22 STATE, 22 ENV, 2 DEAD, 96 NONE with their own reason). The AmazeFileManager sample routes were re-verified: 30 of 30 hold, 0 build warnings.

All judgments are self-checked only (second: pending reviewer). Two AmazeFileManager steps that run only on API 19 or 23 are DEAD, and the 9 methods behind them are UNREACHABLE closed_by_api_level.

## Round 1 state (historical): Aegis

- CI `9371563e`: methods 2,995; REACHABLE 2,528; UNREACHABLE 467 (no_trigger_in_app 435, framework_never_calls 31, branch_never_taken 1).
- W2: baseline = onboarding passed, password vault (Q3) with two default TOTP entries (Q6); 12 gate texts cleared, 23 kept, the four intro pages SETUP_ONLY (37 setup-only methods).
- W3: MainActivity.onStart -> startAuthActivity restored; methods with env on the best route 1,613 -> 218. Exported entries kept: panic app, backup agent, quick-settings tiles.
- W4: RTA dropped 0 edges; Aegis-16 hand fix for the nine non-direct importers (9 getAppPath UNREACHABLE).
- W5: ESR_CREATION on; 4 listed edges kept.
- W6: Aegis-46 (old vault format) and Aegis-47 (document-picker backup) env; 7 import-picker variants env.
- W7 round 1: 1,124 flagged or unreadable steps; 189 NONE by rule, 935 PENDING; Q7 makes the settings sub-page navigation standard (Aegis-38, -39 gui).
- Checked cases: 5 of 5 match their source class.
- Routes re-verified: none yet (11 path warnings). Device: dry run 2 `42168202056-1` 25 PASS / 0 FAIL; real run `42168580707-1` reached 1 of 25 (DEVICE rows wait for route re-verification). Reachable audit: 60 drawn, not checked.

## Round 1 state (historical): AmazeFileManager

- CI `9371563e`: methods 2,981; REACHABLE 2,507; UNREACHABLE 474 (no_trigger_in_app 427, framework_never_calls 38, closed_by_api_level 9).
- W2: no first-run screen; both state texts kept.
- W3: in-app text-editor and FTP-receiver starts; exported-entry routes 57 -> 5.
- W4: HybridFile templates renumbered from javap; HybridFile$9.execute and 4 related methods UNREACHABLE (AmazeFileManager-20); RTA dropped 2 edges, 1 method lost every route.
- W5: 12 XML-inflated constructors non_standard.
- W6: 24 consuming edges env (SSH, stream servers, pickers, database upgrades; AmazeFileManager-12).
- W7 round 1: 982 rows; 7 STATE, 1 ENV, 87 NONE, 887 PENDING (AmazeFileManager-01, -27, -46).
- Checked cases: 6 of 6 match. Routes re-verified: none yet (9 path warnings). Device: dry run 2 30 / 0; real run `42168580707-1` reached 0 of 30 (DEVICE rows wait for route re-verification). Reachable audit: 60 drawn, not checked.

## Round 1 state (historical): AnkiDroid

- CI `9371563e`: methods 4,186; REACHABLE 3,275; UNREACHABLE 911 (no_trigger_in_app 749, branch_never_taken 48, framework_never_calls 48, closed_by_api_level 44, closed_by_configuration 22).
- W2 (Muse): 5 gate texts cleared (sample deck). W3: no change (no in-app start for the provider, AddContentApi, widget or SD-card receiver). W4: RTA dropped 0.
- W5: 6 XML-inflated preference constructors non_standard.
- W6: 9 consuming edges env (AnkiWeb sync, image picker, upgrades; AnkiDroid-34).
- W7 round 1: 940 rows; 8 STATE, 119 NONE, 813 PENDING; database-error dialogs need a broken collection (AnkiDroid-07); S_PREFERENCES gets its page entry from Preferences.onCreate.
- Checked cases: 2 of 2 match. Routes re-verified: none yet (46 path warnings). Device: dry run 2 30 / 0; real run `42168580707-1` reached 0 of 30 (DEVICE rows wait for route re-verification). Reachable audit: 60 drawn, not checked.

## Round 1 state (historical): LibreTorrent

- CI `9371563e`: methods 4,732; REACHABLE 3,967; UNREACHABLE 765 (no_trigger_in_app 715, closed_by_api_level 24, framework_never_calls 13, branch_never_taken 12, closed_by_configuration 1).
- W2 (Muse): no first-run screen.
- W3: launcher gates removed (Ef4711e98, E558b0012, E50191c30), 5 in-app starts, torrent-row bind needs data; exported-entry routes 3,918 -> 9.
- W4: RTA dropped 1 edge, 0 lost. W5: 35 data-binding and 2 Rx edges non_standard. W6: stream server and Room migrations env.
- W7 round 1: 794 rows; 3 STATE, 42 NONE, 749 PENDING (LibreTorrent-16, -19).
- Checked cases: 4 of 4 match. Routes re-verified: none yet (24 path warnings). Device: dry run 2 29 / 0; real run `42168580707-1` reached 6 of 29 (DEVICE rows wait for route re-verification). Reachable audit: 60 drawn, not checked.

## Round 1 state (historical): MMEX

- CI `9371563e`: methods 4,270; REACHABLE 3,430; UNREACHABLE 840 (no_trigger_in_app 741, framework_never_calls 77, branch_never_taken 13, closed_by_api_level 9).
- W2 (Muse): 7 gate texts cleared; tutorial SETUP_ONLY. W3: no change (no in-app start for any exported entry on a best route).
- W4: RTA dropped 0; MMEX-03 @ACCOUNTS clone of showFragment_Internal. W5: 2 XML-inflated views non_standard; MMEX-03 library.
- W6: 6 consuming edges env (price and rate servers, backup picker, database upgrade; MMEX-38).
- W7 round 1: 1,499 rows; 3 STATE, 66 NONE, 1,430 PENDING (MMEX-41, -49, -20).
- Checked cases: 6 of 6 match. Routes re-verified: none yet (10 path warnings). Device: dry run 2 30 / 0; real run `42168580707-1` reached 7 of 30 (DEVICE rows wait for route re-verification). Reachable audit: 60 drawn, not checked.

## Round 1 state (historical): rounds

One round. A second round would need the W7 guard judging and the measurement first; the gates that wait (G4 verified only against Appendix B; G5, G6, G7 waiting for re-verification, the reachable-audit checks and the rounds folder) are listed in the run log and the final message.

## Round 1 state (historical): Markor (Q4)

Markor is not touched. In its CI output (`9371563e`), 10 of its 2,450 REACHABLE best routes pass its intro (the page S_INTRO or an Intro class on the shortest path).

## Round 1 state (historical): rounds 4-5 (review 3 and review 4 fixes)

All numbers below come from a fresh `bash handoff/ci/rebuild.sh Aegis AmazeFileManager AnkiDroid LibreTorrent MMEX`, run before every count (REAUDIT-R4-REBUILD: the committed `graphs/*/out/` is the CI copy and was stale; the round-4 shares and warnings in the earlier version of this section were read from that stale copy for MMEX and AnkiDroid and were wrong).

| App | dead / config / env / state / library / gui (%) |
|---|---|
| Aegis | 20.8 / 0.0 / 23.4 / 15.8 / 8.4 / 31.6 |
| AmazeFileManager | 24.2 / 1.0 / 19.3 / 19.6 / 3.7 / 32.2 |
| AnkiDroid | 38.8 / 3.0 / 12.3 / 11.7 / 0.3 / 33.9 |
| LibreTorrent | 27.8 / 0.9 / 11.2 / 29.7 / 27.8 / 2.6 |
| MMEX | 20.8 / 0.2 / 4.6 / 13.3 / 12.6 / 48.6 |
| weighted | 27.4 / 1.2 / 12.9 / 18.0 / 11.1 / 29.4 |

Build: errors 0; warnings 11 / 0 / 55 / 24 / 3 (the stale-path warnings of Aegis, AnkiDroid, LibreTorrent W8 and the MMEX device re-run). `check_cases.py` 23 of 23; `check_unchanged_apps.py` ALL UNCHANGED. AmazeFileManager verification.csv: 25 fixed and 5 correct path rows (first verdict kept).

Review 4 changes: archive content steps are ENV other_app on every route (REAUDIT-R4-ARCHIVE); AmazeFileManager edges that started at a shared helper (AppConfig.runInBackground / runInParallel and their AppConfig$1 dispatch, SshClientUtils.execute and its $2 wrapper, Operations.mkdir) now start at the caller that passes the lambda, template or callback; the TBD-evidence edges have real lines or are cut; Aegis E27acc957 is NONE (normal cold start); AnkiDroid whiteboard clear/undo steps are STATE settings; LibreTorrent sort-column comparators are STATE session. Self-checked only; second: pending reviewer.

## Final state (Kiro, 2026-11-09; CI fd266ef6)

CI `fd266ef6` (built at `1e76293a`): all 13 apps at 0 errors; the eight other apps at 0 warnings and ALL UNCHANGED; AmazeFileManager and AnkiDroid at 0 warnings; Aegis 1, LibreTorrent 5 and MMEX 3 warnings, all of them device-replayed routes that are no longer the best route (no real run is left to replay them). The 23 checked cases match ("23 of 23").

- **Step 2 (W7 guards):** PENDING 0 in all five apps (`graphs/<App>/scratch/reaudit/w7_judged.csv`, `rejudge_*.txt`).
- **Step 3 (W8 routes):** on the `8d46166a` build, `tools_dev/route_diff.py` showed 0 of 144 sampled routes changed. The W9 fixes then changed two sampled routes; both were re-checked: AmazeFileManager SshConnectionPool$AsyncRemoveConnection.onPostExecute keeps the same 15 steps, and AnkiDroid Sound.notifyConfigurationChanged keeps the same 19 steps. Each moved its step gate from state to env.
- **Step 4 (W9 reachable audit):** 300 drawn methods (15 per class and app, seed 20261106, drawn and pushed before any check). Result: 269 correct, 29 fixed, 0 wrong, 2 unclear; error rate (fixed+wrong)/(correct+fixed+wrong) 0.097. (First count at bde40318: 270/28; the review of 6d94e9c4 triage then found AmazeFileManager env row 15, LZMA2Decoder.numberOptionOrDefault, dead: its route used a wrong edge.)

| App | env | state | library | gui |
|---|---|---|---|---|
| Aegis | 15/0/0 | 15/0/0 | 8/7/0 | 13/2/0 |
| AmazeFileManager | 14/1/0 | 13/2/0 | 11/4/0 | 14/0/1 |
| AnkiDroid | 15/0/0 | 12/3/0 | 9/6/0 | 14/1/0 |
| LibreTorrent | 15/0/0 | 15/0/0 | 13/1/1 | 15/0/0 |
| MMEX | 15/0/0 | 14/1/0 | 15/0/0 | 14/1/0 |

(correct / fixed / unclear; no row is wrong). Label rows are written through each `make_verification.py` (`tools_dev/w9_audit_rows.py`; 297 rows, 3 drawn methods already had a path-sample label row). One checker did two passes; the second, independent check is open (Q-R7-1). Open choices: Q-R7-2 to Q-R7-5.

- **Step 5 (device):** dry run `42559057193-1` with 0 FAIL in all five apps, then the last real run `42560435293-1` (2 of 2): 14 of 144 routes reached (Aegis 1/25, AmazeFileManager 0/30, AnkiDroid 0/30, LibreTorrent 7/29, MMEX 6/30); DEVICE rows correct when reached, otherwise unclear, never wrong.

Class shares over never-run methods, "before" `e0866b9c`, "after" CI `fd266ef6` (`tools_dev/reaudit_shares.py e0866b9c`):

| App | dead / config / env / state / library / gui (%) |
|---|---|
| Aegis | 20.9 / 0.2 / 32.9 / 15.6 / 4.9 / 25.5 |
| AmazeFileManager | 25.3 / 2.1 / 26.0 / 20.2 / 2.7 / 23.8 |
| AnkiDroid | 38.9 / 3.0 / 19.6 / 16.8 / 0.5 / 21.2 |
| LibreTorrent | 27.9 / 1.0 / 14.6 / 34.3 / 19.9 / 2.3 |
| MMEX | 20.8 / 0.3 / 6.0 / 15.8 / 12.2 / 45.0 |
| weighted | 27.6 / 1.4 / 18.1 / 21.0 / 8.6 / 23.3 (before: 27.3 / 1.1 / 20.4 / 20.4 / 2.9 / 27.8) |

Not done: W0 and the round measurement (the tuning half `review/sample_tune/` never arrived), publishing (no PUBLISH_REQUEST, as instructed), and every second-person check (second: pending reviewer).

### After the review of 6d94e9c4 (2026-11-09)

- **Wrong cited-line edges.** CALL edges whose cited line lies inside another method (`kiro_scripts/cited_line_in_caller.py`, sorted by `tools_dev/cited_triage.py`; lists and decisions in `graphs/<App>/scratch/reaudit/cited_line_triage.txt`). AmazeFileManager: 219 hits; 103 pairs cut (the reviewer's four edges and a fifth beside them, every pair the helper matched to a real edge from the method that holds the line, and 26 more after reading the source), 2 of them re-pointed, 6 methods UNREACHABLE (MainActivity.getPaste, ScreenUtils.convertDbToPx, four 7z write-side helpers); the rest are real calls with an off citation. LibreTorrent: 13 hits; 4 cut, 1 citation corrected. Aegis 4 and MMEX 20 hits, AnkiDroid 0: all real calls. `tools_dev/route_diff.py`: 0 of 144 sampled routes changed.
- **Q-R7-6** (an open dialog as GUI or state) added with the default used; nothing relabelled on it.
- The 9 device-replay warnings wait for the user's decision (a third small real run, or dropping those 9 DEVICE rows).
