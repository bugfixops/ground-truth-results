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

### Blind second pass of the reachable audit (W9b and W9c, 2026-11-09; second pass by Kiro, blind; reviewer compared)

The 300 audited rows were judged again from the source, without opening the earlier verdicts, the class columns or the gate texts until every row of a part was written (`kiro_scripts/w9b/`, `kiro_scripts/w9c/`). It is a second pass by the same worker, weaker than an independent check; it does not make the check independent.

- **Part 1 (W9b, 100 rows):** 80 of 100 agreed with the graph at `224f1c94`. Of the 20 disagreements, the graph was right in 13, the second pass in 6, and 1 is a tie (Q-R7-7, MMEX-12: kept gui on the reviewer's answer). Fixes: Aegis-16 (the icon back handler is enabled only after an image from the system picker: ENV), AnkiDroid-05 (packages in the import list come from outside the app: ENV on the import-dialog and Add edges; the shared Replace edges E19e47dc6 and Efcc41abb stay STATE with a true text, "a backup the app writes into AnkiDroid/backup, or a package", because Restore backup uses them too; check: 0 env methods among the 13 whose route passes DeckPicker.restoreFromBackup), AnkiDroid-20 (deck-options putInt comes only from the XML-inflated NumberRangePreference: library), LibreTorrent-01 (the IP filter file row needs IP filtering on: STATE), LibreTorrent-16 (filter lambdas and comparators run only for torrents in the list: STATE), MMEX-19 (RecentDatabasesProvider.remove needs a database path from the picker or another app: ENV), and the MMEX reflection fix (edges leaving the two fragments that only showFragment(Class) creates are non_standard, TASK_NOTE item 3; 64 methods gui -> library, none with an explicit route that avoids the reflection edge). Rows: `graphs/<App>/scratch/reaudit/w9b_compare.csv`.
- **Part 2 (W9c, the other 200 rows):** 163 of 200 agreed before the fixes (169 after). Of the 37 disagreements, the graph was right in 26, the second pass in 6, and 5 are open (Q-R7-8: AnkiDroid-c20; Q-R7-9: AnkiDroid-c06, -c29; MMEX-c11, the Q-R7-7 family; MMEX-c15, which the second pass left unclear). Fixes: Aegis-c13 (the FAB hide animation needs a list that scrolls: STATE), Aegis-c27 (CustomSvgIcon exists only from a picked SVG: ENV on its 6 call edges), AnkiDroid-c23 (Enable whiteboard in the Reviewer menu makes it in the same session: the STATE row is NONE), LibreTorrent-c18 (the sw600dp-land binding is built only on a two-pane screen: ENV hardware), LibreTorrent-c24 (feed items open only from a tapped feed row: STATE), LibreTorrent-c34 (SafFsModule is chosen only for a content:// uri from the picker: ENV on the 11 facade dispatch edges), and a STATE session gate on the split-list restore edges found by MMEX-c33 (the class stays library through the split screen). Rows: `graphs/<App>/scratch/reaudit/w9c_compare.csv`. Every shared gate was checked to hold on every route through its edge; the methods whose class changed are listed by fix in the run log.
- **Audit totals now:** 259 correct, 39 fixed, 0 wrong, 2 unclear (the 12 rows the second pass found wrong are fixed; 10 of them had been counted correct, 2 were already fixed rows that needed a second fix; error rate (fixed+wrong)/(correct+fixed+wrong) = 39/298 = 0.131, was 0.097).

| App | env | state | library | gui |
|---|---|---|---|---|
| Aegis | 15/0/0 | 13/2/0 | 8/7/0 | 12/3/0 |
| AmazeFileManager | 14/1/0 | 13/2/0 | 11/4/0 | 14/0/1 |
| AnkiDroid | 15/0/0 | 11/4/0 | 9/6/0 | 14/1/0 |
| LibreTorrent | 15/0/0 | 14/1/0 | 9/5/1 | 15/0/0 |
| MMEX | 15/0/0 | 14/1/0 | 14/1/0 | 14/1/0 |

(correct / fixed / unclear by drawn class.)

- **Methods whose class changed** (W9b and W9c together, local build after the fixes, against `224f1c94`): Aegis 3, AmazeFileManager 0, AnkiDroid 55, LibreTorrent 140, MMEX 65.
- **Sampled routes:** `route_diff.py` after every rebuild. Routes whose edge ids changed but whose steps stayed the same: AnkiDroid Anki2Importer._mediaPick and Models.validateBrackets (W9b), LibreTorrent FeedDao_Impl$11.finalize, SafFileSystem$FakePath.serialize, SafFileSystem.getParentDirUri and SafFileSystem$FakePath.makeRelativePathNodes (W9c). Their path rows were re-pointed with the note "gate text changed, edge ids re-pointed, no replay, same steps"; the DEVICE rows of _mediaPick, FeedDao_Impl$11.finalize and SafFileSystem.getParentDirUri were re-pointed too (results kept). The DEVICE rows of validateBrackets, FakePath.serialize and makeRelativePathNodes were left as replayed: they hold older routes with other steps (unscriptable, not run). No sampled route changed its steps.

Class shares over never-run methods, "before" `e0866b9c`, "after" the local build after the blind pass (`tools_dev/reaudit_shares.py e0866b9c`):

| App | dead / config / env / state / library / gui (%) |
|---|---|
| Aegis | 20.9 / 0.2 / 33.0 / 15.6 / 4.9 / 25.4 |
| AmazeFileManager | 25.6 / 2.1 / 26.0 / 20.2 / 2.7 / 23.5 |
| AnkiDroid | 38.9 / 3.0 / 21.7 / 14.4 / 0.5 / 21.6 |
| LibreTorrent | 27.9 / 1.0 / 15.8 / 35.9 / 17.0 / 2.3 |
| MMEX | 20.8 / 0.3 / 6.0 / 15.8 / 13.7 / 43.4 |
| weighted | 27.7 / 1.4 / 19.0 / 20.7 / 8.3 / 22.9 (before: 27.3 / 1.1 / 20.4 / 20.4 / 2.9 / 27.8) |

- **Third real run (prepared, not requested):** the route scripts of the 9 stale rows replay the current best routes (Aegis route_21 now unlocks a vault that its setup creates before the coverage reset; LibreTorrent routes 01, 09, 10, 17, 19 keep their steps under new edge ids; MMEX routes 21, 24, 29 tap the seeded account row, its Balance account item, and its group header). Local drycheck: the 9 rows PASS.
- Not done: W0 (neither `review/sample_tune/` nor `review/checked_cases.csv` is on the branch), publishing (no PUBLISH_REQUEST).

### Final state after the third real run and Q-R7-9 (Kiro, 2026-11-09)

- **Device runs.** Three real device attempts, and the cap of 3 is used; no further real run.
  1. `42560435293-1` (five apps): 14 of 144 routes reached (Aegis 1/25, AmazeFileManager 0/30, AnkiDroid 0/30, LibreTorrent 7/29, MMEX 6/30).
  2. `42674277844-1`: lost to a GitHub incident ("Incident with Actions and Checks API", 18:12-18:59Z). No emulator job was created and no device was reached; `device/results/42674277844-1/SUMMARY.md` ("No device-* artifacts found") is kept as it was committed.
  3. `42683233983-1`, the retry (Aegis, LibreTorrent, MMEX; every scripted route of those apps was replayed): the 9 re-scripted stale routes gave LibreTorrent route_01, 09, 10, 17 and 19 reached, each with the whole script finished and with edge ids equal to the current best route. Aegis route_21 failed at step 13: after the relaunch, the unlock screen showed no decrypt button. MMEX routes 21, 24 and 29 failed in their per-route setup, at the Save tap in create_account; that is the same step on which setup_route_04, the setup they copy, failed in both runs with results. Raw totals of this run: Aegis 0/25, LibreTorrent 7/29, MMEX 3/30. The other routes of this run replay scripts older than the graph, so they give no rows; their raw results stay in `device/results/42683233983-1/`.
- **DEVICE row rule** (`tools_dev/device_rows.py`, used by every `make_verification.py` of the five apps):
  - A reached row is written only when its replayed edge ids, after the documented re-point, equal the method's current best route.
  - Rows that did not reach their method make no reach claim and stay as replayed.
  - `LATER_RUNS` names the only rows taken from a later run: the 5 LibreTorrent routes of `42683233983-1`.
  - Effect, against the previous HEAD (`graphs/<App>/scratch/reaudit/device_rule_check.txt`), DEVICE rows: Aegis 25 -> 24 (Salsa20Engine.salsaCore dropped), AmazeFileManager 30 -> 30, AnkiDroid 30 -> 30, LibreTorrent 29 -> 29 (5 replaced by run `42683233983-1`), MMEX 30 -> 27 (DefinedDateRange$1.<init>, NumericHelper.getNumberOfDecimals, AppSettings.getPreferences dropped). No other row of these four apps changed; AnkiDroid changed only by the Q-R7-9 rows below. The four methods keep their static label (REACHABLE, class gui).
- **Device totals rule.**
  - Two different numbers are reported, and neither replaces the other.
  - A run total ("N of M routes reached") is always read from that run's own `device/results/<run>/<App>/results.csv`, unchanged. Run `42560435293-1` stays 14 of 144 (Aegis 1, MMEX 6).
  - The build line `verification device: routes N, reached R` and the app README count the DEVICE rows that `verification.csv` holds under the row rule: confirmations of the current best route. Now: Aegis 0 of 24, AmazeFileManager 0 of 30, AnkiDroid 0 of 30, LibreTorrent 7 of 29, MMEX 3 of 27 (10 of 140).
  - Where a row was dropped, the app README says so in a sentence after the count (Aegis 1, MMEX 3), so the lower count is not read as the run's total.
  - The four re-scripted routes are kept and marked in `ROUTES.csv` as failed on device 2026-11-09 (setup or unlock step).
- **Q-R7-9 decided: dead.**
  - The 25 batch 055 S_ENTRY edges into AddContentApi are removed.
  - The 53 methods of the api module are UNREACHABLE `no_trigger_in_app` (`graphs/AnkiDroid/graph_def_mod/04.py`), and the 65 auto CALL edges inside the module are suppressed.
  - A grep over the 944 app files outside `api/` finds no use of AddContentApi, NoteInfo or com.ichi2.anki.api.
  - 1-in-3 audit (`graphs/AnkiDroid/scratch/reaudit/q_r7_9_audit.txt`, script `q_r7_9_audit.py`): 9 of 25 edges, 18 of 53 entries, 22 of 65 suppressions, 0 mismatches (done by Kiro alone, not by a second agent).
  - Audit rows AnkiDroid-c06 and -c29 are now fixed (env -> dead).
- **Audit totals now:** 257 correct, 41 fixed, 0 wrong, 2 unclear; error rate 41/298 = 0.138.
- **Build:** errors 0 and warnings 0 in all five apps; check_cases 23 of 23; ALL UNCHANGED; `route_diff.py` 0 of 144 sampled routes changed.
- **Q-R7-8** is not applied (default kept) and stays under Known problems.

Class shares over never-run methods, "before" `e0866b9c`, "after" this build (`tools_dev/reaudit_shares.py e0866b9c`):

| App | dead / config / env / state / library / gui (%) |
|---|---|
| Aegis | 20.9 / 0.2 / 33.0 / 15.6 / 4.9 / 25.4 |
| AmazeFileManager | 25.6 / 2.1 / 26.0 / 20.2 / 2.7 / 23.5 |
| AnkiDroid | 41.3 / 3.0 / 19.4 / 14.4 / 0.5 / 21.4 |
| LibreTorrent | 27.9 / 1.0 / 15.8 / 35.9 / 17.0 / 2.3 |
| MMEX | 20.8 / 0.3 / 6.0 / 15.8 / 13.7 / 43.4 |
| weighted | 28.3 / 1.4 / 18.4 / 20.7 / 8.3 / 22.9 (before: 27.3 / 1.1 / 20.4 / 20.4 / 2.9 / 27.8) |

- Not done: W0, because neither `review/sample_tune/` nor `review/checked_cases.csv` is on the branch. Publishing is not done either (no PUBLISH_REQUEST).

### Round 2: causes of the 21 wrong labels (Kiro, 2026-11-10)

Input: `review/rounds/1/adjudication.csv`, the 21 rows where the source supports the sample. Every fix is a rule in the pipeline (`tools_dev/round2_rules.py`, run at the end of each `graphs/<App>/graph_def.py`), not a row edit.

- **A, state gates the W7 screen missed.**
  - The new screen `tools_dev/guard_prescreen_r2.py` reads the routes of never-run gui and library methods for four kinds of condition: multi-clause conditions, setting reads, hidden or disabled triggers (source and res XML), and stored rows and list items.
  - It flagged 616 steps. Steps were judged in order of the number of never-run methods that use them until at least 90% of the flagged uses per app were judged (`graphs/<App>/scratch/reaudit/r2_judged.csv`): Aegis 30 steps (97.3% of uses), AmazeFileManager 42 (94.4%), AnkiDroid 41 (91.0%), LibreTorrent 43 (90.8%), MMEX 54 (92.1%). That leaves 46, 19, 79, 22 and 243 steps unjudged.
  - AnkiDroid-15: only My searches opens the list type of the dialog (`CardBrowser.java:642-653`; the save type at `:636-640` does not run that branch), and My searches shows only with a saved search, so it is a state gate.
- **B, data and devices from outside: env.**
  - Saved SFTP, cloud and SMB entries: env network.
  - Biometric slots and preferences: env hardware.
  - `launchSAF` (removable SD card): env hardware.
  - Root mode: env other.
  - The SMS-started editor: env other_app.
- **C, calls that never run.**
  - The edge becomes a REGISTER record, and the method gets an UNREACHABLE entry when no live edge is left.
  - The base `DatabaseImporter$State.convert` (every state that reaches it overrides it).
  - `Hooks.runFilter` runs only the hooks registered under its name (AnkiDroid-39: nothing is registered under mungeFields).
  - `AsyncTask.onCancelled` when no instance can be cancelled. An instance that is returned to a caller counts as cancellable.
  - Framework calls into an app's `describeContents`.
  - New UNREACHABLE entries: 12. AmazeFileManager-49 (`ShareAdapter.getItemId`) is left as it is, because the RecyclerView library source is not in the tree.
- **D, GUI actions.**
  - Aegis open floating action menu and search box: not session state.
  - AmazeFileManager storage-permission denial: a GUI action.
- **E, dialog rule.** Tried behind `R2_DIALOG_RULE` and switched off, because it broke 3 checked cases (MUSE_REAUDIT_QUESTIONS Q-R7-6; `graphs/AnkiDroid/scratch/reaudit/round2_E_trial.txt`).
- **Agreement on `review/sample_tune`** (`review/measure.py`, outputs in `review/rounds/2/`):
  - 72.1% before (round 1).
  - 84.6% after A to D (115 of 136; 97 of 113 without the checked cases).
  - 84.6% with E on (not kept).
  - 17 of the 21 rows now have the source class. Still different: AnkiDroid-13, -35, -41 (the dialog rule) and AmazeFileManager-49.
  - None of the 12 rows where the adjudication supports the full label changed.
- **Sampled routes.** 9 changed (Aegis 5, AmazeFileManager 3, MMEX 1); 4 of them changed steps, 5 only edge ids. Each was re-checked from the source, and its path row and ROUTES.csv entry ("route changed in round 2, not replayed") were updated (`graphs/<App>/scratch/reaudit/round2_route_changes.txt`). DEVICE rows unchanged: 24, 30, 30, 29, 27.
- **Audit, 1 in 3.** The population is 79 new gates (35 judged rows, 34 rule B edges, 10 rule D edges) and 12 new UNREACHABLE entries. 31 items were re-read from the source, all OK (`graphs/<App>/scratch/reaudit/round2_audit.txt`). One error was found and fixed outside the sample: the AnkiDroid statistics tasks are cancelled under their AsyncTask type.
- **Methods whose class changed** against eb139585 (before -> after):
  - Aegis 160: state->gui 126, state->library 17, gui->state 8, gui->env 5, state->env 2, env->dead 1, library->state 1.
  - AmazeFileManager 48: state->env 32, gui->env 9, gui->state 3, state->dead 3, state->gui 1.
  - AnkiDroid 23: gui->state 22, gui->dead 1.
  - LibreTorrent 78: library->state 71, library->dead 5, state->dead 2.
  - MMEX 6: gui->state 6.

Class shares over never-run methods, before `e0866b9c`, after this build (dead / config / env / state / library / gui, %):

| App | after round 2 |
|---|---|
| Aegis | 20.9 / 0.2 / 33.2 / 10.4 / 5.5 / 29.8 |
| AmazeFileManager | 25.7 / 2.1 / 28.2 / 18.4 / 2.7 / 22.9 |
| AnkiDroid | 41.3 / 3.0 / 19.4 / 15.4 / 0.5 / 20.3 |
| LibreTorrent | 28.2 / 1.0 / 15.8 / 38.5 / 14.3 / 2.3 |
| MMEX | 20.8 / 0.3 / 6.0 / 16.0 / 13.7 / 43.2 |
| weighted | 28.4 / 1.4 / 18.8 / 20.6 / 7.7 / 23.1 (before: 27.3 / 1.1 / 20.4 / 20.4 / 2.9 / 27.8) |
