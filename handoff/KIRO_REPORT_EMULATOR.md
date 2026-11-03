# Kiro report: emulator run (all 13 apps)

## Part A: prepare the workflow
- A0: synced to origin/work-2026-10-31, head `f435fca8` ("PROGRESS_V2: user ticks Aegis, AmazeFileManager, AnkiDroid, MMEX, LibreTorrent ([K] -> [x]); all 13 apps ticked").
- A1: commit `e6ad6ad8` edits `.github/workflows/device-replay.yml` with the three approved changes only: `target` input default `google_apis` (description updated) and the replay step's `target: ${{ inputs.target || 'google_apis' }}`; new step "SSH server for Amaze SSH routes" (openssh-server via apt, only when not a dry run and `matrix.app == 'AmazeFileManager'`) before "Emulator and route replay"; `env: WITH_SSH_SERVER: ${{ matrix.app == 'AmazeFileManager' && '1' || '0' }}` on the replay step. `git diff --stat`: 1 file, 12 insertions, 3 deletions; no tab characters.
- A2: dry-run request `f51230f1` (line 2 time 2026-11-03T04:27:17Z, `all`); bot commit `1b659ea6` `[device] dryrun 41578222764-1`; Actions run 41578222764 "Device replay" completed, conclusion success (so the edited YAML parses). SUMMARY: FAIL 0 for all 13 apps; PASS Currency 28, Diary 30, hash-checker 37, Omni-Notes 33, openlauncher 27, Vanilla-Music 30, Markor 30, AnyMemo 30, Aegis 25, AmazeFileManager 30, AnkiDroid 30, MMEX 30, LibreTorrent 29 (all as expected).
- A3: `handoff/NEXT_DEVICE_REPLAY.md` updated: status paragraph (workflow ready at `e6ad6ad8`, dry run `41578222764-1` passed, no real run started), image choice (Google APIs x86_64, API 27, user decision 2026-11-03), the Amaze SSH section replaced by a "Done" note, and a new section "How the user starts the real run" (steps and expected time). Committed with this report.
- No real emulator run was started.

## Between Part A and Part B: getting a real run to work (user instruction 2026-11-03: "run it yourself, fix what needs to be fixed")
- 41578755210 (user's manual run, b3356c5b): all 13 jobs failed in the emulator setup in about 23 s. Google's image list (dl.google.com sys-img google_apis) has no `system-images;android-27;google_apis;x86_64`; it has x86 and arm64-v8a. All 13 APKs have no native code or ship x86 libs (checked in the local APKs). Fix e97b62cb: `arch` default `x86` (still Google APIs), plus a real-run request file `handoff/DEVICE_REPLAY_REQUEST.txt` (no API token on this machine; the push credential is in the keychain and was not read). Dry run 41579127015-1 after the edit: 13 apps, FAIL 0.
- 41579432533 (1890c6a8): the real request ran as a dry run (the push-payload expression did not match). Fix 60862462: the plan job decides `dry` from `git diff-tree` of the pushed commit and the run/collect jobs read it from `needs.plan.outputs.dry`.
- 41580035601 (60862462): real run, 1 route per app. `device/run_app.sh`: `IFS=tab read` collapsed empty columns (status read as fixtures) and adb inside the loop consumed the route list; sshd needs an absolute path. Fix a147c559 (fd 3, 0x1f separator; absolute sshd and key paths). Local test: 28/29 routes read with correct columns.
- 41580858995 (a147c559): every UI dump failed to parse ("junk after document element", the status line after the XML); method names with commas shifted results.csv; non-root sshd could not read /etc/ssh/sshd_config.d. Fix 453a3b6a (parse only <hierarchy>, quote the method field, own sshd config file). 30 harness tests pass.
- 41581852815 (453a3b6a): first complete run, workflow success, 70/389 reached. Taps raced cold starts. Fix 71d7ca9d (tap polls up to 20 s, wait_for at least 30 s, visible labels to stderr on a miss).
- 41583852305 (71d7ca9d): 62/359 reached; Markor job lost to a JaCoCo download error (curl 22); AnyMemo and AmazeFileManager never came to the front: their launch components used the application id (`...fantastischmemopro`, `...filemanager.debug`) as the class package. Fix 3404c1c9 (56 component strings in 44 scripts, drycheck 30/30 PASS each; JaCoCo download retried).
- 41586297765 (3404c1c9): 76/389. API 27 dumps all-caps buttons/tabs as ARTISTS, SKIP; Diary's start-up permission dialog covered 16 routes. Fix 5c2bc466 (case-insensitive fallback after an exact match; Diary: 22 empty permission cells filled with the 4 permissions Diary requests on start).
- 41589762145 (5c2bc466): 102/389. The baseline fixture folders were never pushed (ROUTES setup notes "push fixtures/Music + media scan" etc.); Vanilla needs storage to show its library. Fix d4b1e3af (push Download/Music/Pictures/Documents and media-scan once per app, as work-emulator ci/run_app.sh does; Vanilla: 26 empty permission cells filled with READ/WRITE_EXTERNAL_STORAGE).
- 41593209101 (d4b1e3af): 104/389 reached; the run of record for Part B.

## Part B: process the run results (run 41593209101-1)
- B0: `[device] results 41593209101-1` (ab7c5f90); all 13 app jobs and collect finished with success; 13 `results.csv` present.
- B1: `device/compare.py` wrote 13 `graphs/<App>/device/results.csv` (rows = routes for every app).
- B2: all 13 writers ran twice with exit 0 and byte-identical output (md5); DEVICE rows = routes for every app (Currency 28, Diary 30, hash-checker 37, Omni-Notes 33, openlauncher 27, Vanilla-Music 30, Markor 30, AnyMemo 30, Aegis 25, AmazeFileManager 30, AnkiDroid 30, MMEX 30, LibreTorrent 29); DEVICE `correct` = reached in every app, no `wrong`; only DEVICE lines were added, no other line changed.
- B3: commit with the 26 files, CI request 21c73e8e, bot commit c2e5b6b7 `[ci] rebuild and checks`: every SUMMARY names 21c73e8e; errors 0, warnings 0, check 2 0 problems, check 4 0 for all 13; verdicts identical to the previous CI table; `verification.csv rows: ... DEVICE n` with n = routes everywhere; no "no longer the best route" warning.
- B4: `handoff/DEVICE_RUN_SUMMARY.md`: reached 104/389 (26.7%); lowest shares AmazeFileManager 0/30, AnkiDroid 0/30, Aegis 1/25.

## Decisions (Kiro, 2026-11-03, for the reviewer)
- Image Google APIs x86 instead of x86_64 (the x86_64 image does not exist for API 27).
- A real-run request file (`handoff/DEVICE_REPLAY_REQUEST.txt`) was added as a second trigger, because the user asked Kiro to run it and no API token is available. Pushing `handoff/DEVICE_DRYRUN_REQUEST.txt` still gives a dry run.
- Shared fixtures pushed once per app (the baseline tool runs' device state); permissions still per route, install still without `-g`.
- Diary (22 rows) and Vanilla-Music (26 rows): permissions the app requests on every start were added to the empty cells; permission-dialog routes untouched.
- Run-to-run noise exists (AnyMemo 6 then 5, hash-checker 25 then 23 reached between the last two runs); the numbers are one run.

## Not fixed (per-app first-start state; candidates for the reviewer and Yang)
- AnkiDroid opens on Preferences instead of the deck list on most routes (20 misses); Markor shows its intro and then a storage request (14); Omni-Notes shows an empty notes list where scripts expect content (15); AmazeFileManager crashes ("Amaze Debug has stopped"); openlauncher stays in its own launcher/onboarding states. Fixing these needs app-specific setup (preset preferences, seed data) in ticked apps' route scripts.

## Part C: DEVICE-row fix
- C0: head `09de7506` (Kiro emulator report Part B).
- C1: `tools/build_graph.py` copied to `tools/build_graph_v9_backup.py`; reviewer patch printed `patched` for tools/build_graph.py, tools/gen_readme_v2.py, handoff/ci/rebuild.sh. `git diff --stat`: handoff/ci/rebuild.sh 2 (+1/-1), tools/build_graph.py 45 (+45), tools/gen_readme_v2.py 6 (+6); backup untracked.
- C2: local `rebuild.sh all` exit 0; `check_device_fix.py`: PASS for all 13, `ALL PASS`.
- C3: device bullet added as the first bullet under `## What waits for a device (API 27)` in 12 apps (Currency +1 and Vanilla-Music +3 "reached but script stopped early" sentences); Diary line 9 replaced by the Appendix A text. Rebuild exit 0, `ALL PASS`, every readme_notes.md has 5 `## ` headings, `graphs/Diary/out/README.md` shows the device sentence and "Path status over all reachable methods: DEVICE_OK 16, SOURCE_OK 11, UNCHECKED 238."
- C4: correction section added to `handoff/DEVICE_RUN_SUMMARY.md`, CI line rewritten.
- C5: fix commit `8185289c` (18 files); CI request `001fd881`; bot commit `60e7e0a6` `[ci] rebuild and checks`. All 13 SUMMARY files name `001fd881`; errors 0 and warnings 0 for all 13; each has a `verification device: routes N, reached R (script finished F), unclear U` line. `check_device_fix.py` on the CI outputs: `ALL PASS`; DEVICE_OK total 100, WRONG total 14.
- C6: placeholders in `handoff/DEVICE_RUN_SUMMARY.md` filled (`8185289c`, `60e7e0a6`); this section; pushed last.
- Model: this session cannot switch itself to claude-haiku-5-5; it ran on the session model. No helper agents were used (host memory critical).

## Blocked
- none. Notes: `git config user.email` in this clone prints a personal address, not bugfixops (the handover expected it set); every commit was made with GIT_AUTHOR_*/GIT_COMMITTER_* set to `bugfixops <bugfixops@users.noreply.github.com>` instead, and the config was left unchanged. The model could not be switched to claude-haiku-5-5 from inside the session. At the A1 push, the only running Actions job was GitHub's own "Graph Update: pip" dependency scan, not a CI or dry-run job.
