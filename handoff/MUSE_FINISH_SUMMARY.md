# MUSE_FINISH_SUMMARY — final per-app summary

Written by Kiro on 2026-11-03, as the finishing agent (Muse had stopped), per `handoff/MUSE_FINISH_ALL.md` section 8.
Every number below is copied from the file it names, on branch `work-2026-10-31` after CI commit `ae203fe7`
(`[ci] rebuild and checks`, all 13 apps, request commit `185cd5e1`) and the final all-apps dry run `41576644702-1`.

## Currency

1. PROGRESS line: `- [x] Currency`
2. CI (`graphs/Currency/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 145`; `verdicts: REACHABLE 140, UNREACHABLE 5`; `unreachable by kind: branch_never_taken 1, framework_never_calls 3, no_trigger_in_app 1`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 41 distinct, 0 problems; library citations (not checked): 4; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Currency: 0 routes flagged`; `check 4: Currency: 0 bytecode-cited edges checked, 0 skipped (lambda / clinit / anonymous), 0 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 1 of 5 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 24, errors found 1 (rate 0.042), unclear 4` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 47, errors found 23 (rate 0.489), unclear 0`; `verification edge: checked 20, errors found 0 (rate 0.0), unclear 3`; `verification path: checked 24, errors found 1 (rate 0.042), unclear 4`; `verification.csv rows: path 28, DEVICE 0`.
6. Device: 28 routes, 28 scripted, 0 unscriptable (`device/routes/Currency/ROUTES.csv`). Final dry run `41576644702-1`: PASS 28, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Currency D1, Currency D2, Currency D3, Currency D4, Currency D5, Currency D6, Currency-CUR-T1-D1, Currency-CUR-T1-D2, Currency-CUR-D3-D1, Currency-CUR-D3-D2
8. Blocked: none.

## Diary

1. PROGRESS line: `- [x] Diary`
2. CI (`graphs/Diary/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 286`; `verdicts: REACHABLE 265, UNREACHABLE 21`; `unreachable by kind: framework_never_calls 4, no_trigger_in_app 17`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 81 distinct, 0 problems; library citations (not checked): 29; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Diary: 0 routes flagged`; `check 4: Diary: 0 bytecode-cited edges checked, 0 skipped (lambda / clinit / anonymous), 0 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 5`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): graphs/Diary/auto_calls.json does not exist: no bytecode edges to compare`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 25, errors found 7 (rate 0.28), unclear 5` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 51, errors found 7 (rate 0.137), unclear 0`; `verification edge: checked 37, errors found 0 (rate 0.0), unclear 10`; `verification path: checked 25, errors found 7 (rate 0.28), unclear 5`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 30 scripted, 0 unscriptable (`device/routes/Diary/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Diary D1, Diary D2, Diary D3, Diary D4, Diary D5, Diary D7, Diary D8, Diary D9, Diary D10, Diary D6, Diary-D3-05F, Diary-D3-14, Diary-D3-28, Diary-D3-12P, Diary-D3-PERM, Diary-D3-CAP, Diary-14-STAGED, Diary-14-GATE-SATISFIED, Diary-14-stale-note, Diary-14-AUDIT-PASS, Diary-14-load-scripts-CLOSED
8. Blocked: none.

## hash-checker

1. PROGRESS line: `- [x] hash-checker`
2. CI (`graphs/hash-checker/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 529`; `verdicts: REACHABLE 507, UNREACHABLE 22`; `unreachable by kind: closed_by_configuration 3, framework_never_calls 3, no_trigger_in_app 16`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 15 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # hash-checker: 0 routes flagged`; `check 4: hash-checker: 548 bytecode-cited edges checked, 32 skipped (lambda / clinit / anonymous), 90 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 7`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 4`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 4 of 22 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 37, errors found 13 (rate 0.351), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 52, errors found 2 (rate 0.038), unclear 0`; `verification edge: checked 35, errors found 26 (rate 0.743), unclear 0`; `verification path: checked 37, errors found 13 (rate 0.351), unclear 0`; `verification.csv rows: path 37, DEVICE 0`.
6. Device: 37 routes, 36 scripted, 1 unscriptable (`device/routes/hash-checker/ROUTES.csv`). Final dry run `41576644702-1`: PASS 37, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
   - route_31 `LogUtils.e`: LogUtils.e fires only in the ActivityNotFoundException catch when no app handles ACTION_OPEN_DOCUMENT (HashCalculatorFragment.java:191-200); on the replay image DocumentsUI handles the intent, and the harness has no supported component-disable action.
7. Decision ids (`handoff/MUSE_DECISIONS.md`): hash-checker D1, hash-checker D2, hash-checker D3, hash-checker D4, hash-checker D5, hash-checker D6, Hash-HC-T3-1, Hash-HC-T3-2, Hash-HC-D1-1, Hash-HC-D3-31, Hash-HC-D3-31-NOTE
8. Blocked: none.

## Omni-Notes

1. PROGRESS line: `- [x] Omni-Notes`
2. CI (`graphs/Omni-Notes/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 1456`; `verdicts: REACHABLE 1202, UNREACHABLE 254`; `unreachable by kind: branch_never_taken 5, closed_by_configuration 21, framework_never_calls 34, no_trigger_in_app 194`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 18 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Omni-Notes: 0 routes flagged`; `check 4: Omni-Notes: 1381 bytecode-cited edges checked, 114 skipped (lambda / clinit / anonymous), 32 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 11`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 5 of 254 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 33, errors found 30 (rate 0.909), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 288, errors found 7 (rate 0.024), unclear 0`; `verification edge: checked 49, errors found 34 (rate 0.694), unclear 0`; `verification path: checked 33, errors found 30 (rate 0.909), unclear 0`; `verification.csv rows: path 33, DEVICE 0`.
6. Device: 33 routes, 31 scripted, 2 unscriptable (`device/routes/Omni-Notes/ROUTES.csv`). Final dry run `41576644702-1`: PASS 33, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
   - route_13 `TextHelper.getAlternativeTitle`: needs the DashClock or Pushbullet host app installed and calling the extension; neither host app is available on the AOSP emulator
   - route_17 `UpgradeProcessor.<init>`: needs an older-version database on disk (install an old build with data, then update); no old-version database fixture exists in $WEMU/fixtures
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Omni-Notes D1, Omni-Notes D2, Omni-Notes D3, Omni-Notes D4, Omni-Notes D5, Omni-Notes D6, Omni-Notes D7, Omni-Notes D8, Omni-Notes D9, Omni-Notes D10, Omni-Notes D11
8. Blocked: none.

## openlauncher

1. PROGRESS line: `- [x] openlauncher`
2. CI (`graphs/openlauncher/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 900`; `verdicts: REACHABLE 728, UNREACHABLE 172`; `unreachable by kind: closed_by_configuration 19, framework_never_calls 10, no_trigger_in_app 143`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 64 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # openlauncher: 0 routes flagged`; `check 4: openlauncher: 569 bytecode-cited edges checked, 60 skipped (lambda / clinit / anonymous), 16 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 1`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 2 of 172 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 27, errors found 1 (rate 0.037), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 199, errors found 0 (rate 0.0), unclear 0`; `verification edge: checked 37, errors found 3 (rate 0.081), unclear 0`; `verification path: checked 27, errors found 1 (rate 0.037), unclear 0`; `verification.csv rows: path 27, DEVICE 0`.
6. Device: 27 routes, 26 scripted, 1 unscriptable (`device/routes/openlauncher/ROUTES.csv`). Final dry run `41576644702-1`: PASS 27, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
   - route_14 `AutoFinishActivity.onCreate`: caller package must be org.kustom.wallpaper or org.kustom.widget (FiveSecsDelayContentProvider.checkCallingPackage); adb shell content delete runs as shell with no calling package and throws SecurityException, and no such caller app is among the inputs
7. Decision ids (`handoff/MUSE_DECISIONS.md`): openlauncher D1, openlauncher D2, openlauncher D3, openlauncher D4
8. Blocked: none.

## Vanilla-Music

1. PROGRESS line: `- [x] Vanilla-Music`
2. CI (`graphs/Vanilla-Music/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 1473`; `verdicts: REACHABLE 1325, UNREACHABLE 148`; `unreachable by kind: branch_never_taken 4, no_trigger_in_app 144`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 100 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Vanilla-Music: 0 routes flagged`; `check 4: Vanilla-Music: 2020 bytecode-cited edges checked, 290 skipped (lambda / clinit / anonymous), 67 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 3 of 148 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 30, errors found 19 (rate 0.633), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 178, errors found 0 (rate 0.0), unclear 0`; `verification edge: checked 80, errors found 10 (rate 0.125), unclear 0`; `verification path: checked 30, errors found 19 (rate 0.633), unclear 0`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 30 scripted, 0 unscriptable (`device/routes/Vanilla-Music/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Vanilla-Music D1, Vanilla-Music D2, Vanilla-Music D3, Vanilla-Music D4, Vanilla-Music D5
8. Blocked: none.

## Markor

1. PROGRESS line: `- [x] Markor`
2. CI (`graphs/Markor/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 2864`; `verdicts: REACHABLE 2450, UNREACHABLE 414`; `unreachable by kind: closed_by_api_level 1, closed_by_configuration 9, no_trigger_in_app 404`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 36 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Markor: 0 routes flagged`; `check 4: Markor: 4352 bytecode-cited edges checked, 748 skipped (lambda / clinit / anonymous), 130 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 0 of 414 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 30, errors found 17 (rate 0.567), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 445, errors found 48 (rate 0.108), unclear 0`; `verification edge: checked 82, errors found 40 (rate 0.488), unclear 5`; `verification path: checked 30, errors found 17 (rate 0.567), unclear 0`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 30 scripted, 0 unscriptable (`device/routes/Markor/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Markor D1, Markor D2, Markor D3, Markor D4, Markor D5, Markor D6, Markor-D3-04
8. Blocked: none.

## AnyMemo

1. PROGRESS line: `- [x] AnyMemo (round 3 by Kiro 2026-10-27; checked by the orchestrator 2026-10-27 18:50: build 0/0, PENDING 0, citations and bytecode checks pass, 30 path rows; see graphs/AnyMemo/AGENT_NOTES.md)`
2. CI (`graphs/AnyMemo/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 2207`; `verdicts: REACHABLE 1966, UNREACHABLE 241`; `unreachable by kind: branch_never_taken 7, framework_never_calls 18, no_trigger_in_app 216`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 33 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # AnyMemo: 1 routes flagged`; `check 4: AnyMemo: 2294 bytecode-cited edges checked, 534 skipped (lambda / clinit / anonymous), 139 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 3 of 241 unreachable methods have a bytecode caller outside the set`.
4. Route table: no `scratch/route_table.md` totals line for this ticked app; the verification totals are `verification path: checked 30, errors found 0 (rate 0.0), unclear 0` (SUMMARY, from `verification.csv` path rows).
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 271, errors found 0 (rate 0.0), unclear 0`; `verification edge: checked 45, errors found 7 (rate 0.156), unclear 0`; `verification path: checked 30, errors found 0 (rate 0.0), unclear 0`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 27 scripted, 3 unscriptable (`device/routes/AnyMemo/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: none named.
   - route_02 `UploadDropboxActivity.onDestroy`: Dropbox account and saved access token cannot be created by adb on an AOSP emulator (no Dropbox account or token fixture exists; OAuth login in an external browser/Custom Tab and api.dropboxapi.com reachability required)
   - route_08 `DropboxApiHelper$4.call`: Dropbox account and saved access token cannot be created by adb on an AOSP emulator (no Dropbox account or token fixture exists; OAuth login in an external browser/Custom Tab and api.dropboxapi.com reachability required)
   - route_17 `Card.toString`: DAO-failure state cannot be created by adb on an AOSP emulator (Card.toString fires only in the RuntimeException at LearnQueueManager.java:267 when cardDao.update returns 0; this chain's flush is the build-time flush with an empty dirtyCache; and deleting the card trips the earlier :263 LearningData check first)
7. Decision ids (`handoff/MUSE_DECISIONS.md`): AnyMemo D1, AnyMemo D2, AnyMemo D3, AnyMemo D4, AnyMemo-D3-17, AnyMemo-D3-07-cell
8. Blocked: none.

## Aegis

1. PROGRESS line: `- [K] Aegis (labels, route checks, logs and device scripts DONE 2026-11-02; CI run 2195fccb; D9 run 41557528925-1 PASSED; awaiting user tick)`
2. CI (`graphs/Aegis/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 2995`; `verdicts: REACHABLE 2537, UNREACHABLE 458`; `unreachable by kind: branch_never_taken 1, framework_never_calls 31, no_trigger_in_app 426`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 22 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # Aegis: 0 routes flagged`; `check 4: Aegis: 4273 bytecode-cited edges checked, 345 skipped (lambda / clinit / anonymous), 168 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 0 of 458 unreachable methods have a bytecode caller outside the set`.
4. Route table (`graphs/Aegis/readme_notes.md`, lines 3-6): "errors 0, warnings 0. Final route table (post-fix redraw, seed 20261025): 25 routes, 1093 steps, 446 distinct edges; CORRECT 13 / WRONG 1 / UNCLEAR 11; fixed 2 (AndOtp, Stratum); distinct error rate 3/14 = 0.2143; table-formula rate 3/16 = 0.1875. CI SUMMARY"
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 472, errors found 1 (rate 0.002), unclear 11`; `verification edge: checked 26, errors found 0 (rate 0.0), unclear 0`; `verification path: checked 14, errors found 1 (rate 0.071), unclear 11`; `verification.csv rows: path 25, DEVICE 0`.
6. Device: 25 routes, 22 scripted, 3 unscriptable (`device/routes/Aegis/ROUTES.csv`). Final dry run `41576644702-1`: PASS 25, FAIL 0. Earlier dry-run id in the PROGRESS line: `41557528925-1`.
   - route_02 `FreeOtpImporter$DecryptedStateV2.<init>`: rooted device plus su grant plus installed FreeOTP V2 tokens.xml data; no in-run producer (table steps 48, 50, 52); adb root does not provide the app's libsu su call
   - route_09 `IconAdapter$CategoryHeader.getPosition`: drawn route omits the Google Authenticator app-import sub-flow needing root plus an installed Google Authenticator app plus its import result, and an installed icon pack (table steps 46, 48); creating entries in-run cures neither precondition
   - route_17 `AuthActivity.lambda$onCreate$3`: drawn steps false as drawn: step 28 lock-icon tap impossible (lock item hidden on the unencrypted NONE vault, MainActivity.java:1155-1160) and step 35 biometric-button tap impossible (no BiometricSlot plus keystore key; steps 8 and 21-22 contradict a biometric vault); changing the vault type would be a different route, not this one
7. Decision ids (`handoff/MUSE_DECISIONS.md`): Aegis D1, Aegis D2, Aegis D3, Aegis D4, Aegis D5, Aegis D6, Aegis D7, Aegis-C2-D1, Aegis-C2-D2, Aegis-C2-D3, Aegis-C2-D4, Aegis-C2-D5, Aegis-C2-D6, Aegis-C2-D7, Aegis-C2-R1, Aegis-C3-Step8, Aegis-C3-Exit-Hold, Aegis-C3-Audit-PASS, Aegis-C3-Push-Scope, Aegis-C3-Rejudge-Followup, Aegis-Importer-Sequence, Aegis-GenCode-Rule, Aegis-row3-amended
8. Blocked: none.

## AmazeFileManager

1. PROGRESS line: `- [K] AmazeFileManager (labels, route checks, logs and device scripts DONE 2026-11-02; CI run 33e3ca1a; D9 run 41483333085-1 PASSED; awaiting user tick)`
2. CI (`graphs/AmazeFileManager/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 2981`; `verdicts: REACHABLE 2512, UNREACHABLE 469`; `unreachable by kind: closed_by_api_level 9, framework_never_calls 38, no_trigger_in_app 422`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 1 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # AmazeFileManager: 0 routes flagged`; `check 4: AmazeFileManager: 3441 bytecode-cited edges checked, 687 skipped (lambda / clinit / anonymous), 162 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 3 of 469 unreachable methods have a bytecode caller outside the set`.
4. Route table (`graphs/AmazeFileManager/scratch/route_table.md`, lines 70-70): "correct 5, fixed 25, wrong 0, unclear 0; error rate 25/30 = 0.833."
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 499, errors found 25 (rate 0.05), unclear 0`; `verification edge: checked 14, errors found 10 (rate 0.714), unclear 0`; `verification path: checked 30, errors found 25 (rate 0.833), unclear 0`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 26 scripted, 4 unscriptable (`device/routes/AmazeFileManager/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: `41483333085-1`.
   - route_05 `StreamSource.getCurrentPosition`: reaching the target requires a configured cloud provider account and a media file inside it, which adb and the harness cannot create
   - route_06 `StreamSource.read(byte[],int,int)`: reaching read() requires a live SMB server and an external player fetching the app's local HTTP stream; the harness provides no SMB server fixture and adb cannot create one
   - route_12 `StreamNotFoundException.<init>(Throwable)`: the (Throwable) constructor is reachable only through a write failure the harness cannot arrange (read-only content URI grant; delete-then-save yields EXCEPTION_IO, not the RuntimeException needed)
   - route_22 `SmbSearchDialog$1.lambda$computerFound$0`: computerFound fires ONLY when a real SMB host responds on the local network (adb cannot create one; the emulator network has no SMB host)
7. Decision ids (`handoff/MUSE_DECISIONS.md`): AmazeFileManager D1, AmazeFileManager D2, AmazeFileManager D3, AmazeFileManager D4, AmazeFileManager D5, AmazeFileManager D6, AmazeFileManager D7, AmazeFileManager D8, Amaze-D3-CAP, Amaze-D3-CAP-ACCEPT, Amaze-D3-CAP-ACCEPT-RENEWAL, AMAZE-G4-ENDORSEMENT
8. Blocked: none.

## AnkiDroid

1. PROGRESS line: `- [K] AnkiDroid (labels, route checks, logs and device scripts DONE 2026-11-02; CI run 2195fccb; D9 run 41557528925-1 PASSED; awaiting user tick)`
2. CI (`graphs/AnkiDroid/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 4186`; `verdicts: REACHABLE 3275, UNREACHABLE 911`; `unreachable by kind: branch_never_taken 48, closed_by_api_level 44, closed_by_configuration 22, framework_never_calls 48, no_trigger_in_app 749`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 273 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # AnkiDroid: 0 routes flagged`; `check 4: AnkiDroid: 7122 bytecode-cited edges checked, 1068 skipped (lambda / clinit / anonymous), 212 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 1`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 169 of 911 unreachable methods have a bytecode caller outside the set`.
4. Route table (`graphs/AnkiDroid/scratch/route_table.md`, lines 13-15): "Totals: CORRECT 27 / WRONG 3 / UNCLEAR 0. Rate = (fixed + wrong) / (correct-only + fixed + wrong) = (13 + 3) / (14 + 13 + 3) = 16 / 30 = 0.5333 (approx), where fixed means WRONG in ANY earlier draw (first"
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 941, errors found 3 (rate 0.003), unclear 0`; `verification edge: checked 232, errors found 0 (rate 0.0), unclear 0`; `verification path: checked 30, errors found 3 (rate 0.1), unclear 0`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 26 scripted, 4 unscriptable (`device/routes/AnkiDroid/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: `41557528925-1`.
   - route_02 `EasyX509TrustManager.<init>`: reaching the target requires a logged-in AnkiWeb account (stored hkey non-empty) and a real HTTPS sync to the AnkiWeb server; no test account exists and a real sync must not be attempted; with an empty hkey the flow diverts to the not-logged-in dialog before any Connection.sync
   - route_26 `CollectionLoader.deliverResult`: the row's only entry is the no-space dialog, shown only when BackupManager.enoughDiscSpace is false (DeckPicker.java:848-850); no harness action (launch, tap, key, type, scroll, rotate, push_fixture) creates a below-threshold free-space state, the threshold is 10 MiB (BackupManager.java:47, 207-208), and filling storage risks breaking the collection load the route itself needs; other loader entries (for example Reviewer onCreate) are not this row's route and must not be substituted
   - route_36 `Models.validateBrackets`: route WRONG as drawn (see route_table.md)
   - route_37 `Collection.getServer`: route WRONG as drawn (see route_table.md)
7. Decision ids (`handoff/MUSE_DECISIONS.md`): AnkiDroid Decision A, AnkiDroid Decision B, AnkiDroid Decision C, AnkiDroid Decision D, AnkiDroid Decision E, Anki-B2-1, Anki-B2-2, Anki-B4-binding, ANKI-ROUTES-CRITERION
8. Blocked: none.

## MMEX

1. PROGRESS line: `- [K] MMEX (labels, route checks, logs and device scripts DONE 2026-11-02; CI run 70607c2c; D9 run 41535141998-1 PASSED; awaiting user tick)`
2. CI (`graphs/MMEX/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 4270`; `verdicts: REACHABLE 3430, UNREACHABLE 840`; `unreachable by kind: branch_never_taken 13, closed_by_api_level 9, framework_never_calls 77, no_trigger_in_app 741`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 247 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # MMEX: 0 routes flagged`; `check 4: MMEX: 6019 bytecode-cited edges checked, 616 skipped (lambda / clinit / anonymous), 149 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 19 of 840 unreachable methods have a bytecode caller outside the set`.
4. Route table (`graphs/MMEX/scratch/route_table.md`, lines 24-27): "- Routes: CORRECT 20 / FIXED 8 / WRONG 0 / UNCLEAR 2 = 30. - Steps: correct 433 / fixed 14 / wrong 0 / unclear 3 = 450. - Final error rate = (fixed + wrong) / (correct + fixed + wrong) = (8 + 0) / (20 + 8 + 0) = 8 / 28 = 0.2857."
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 868, errors found 8 (rate 0.009), unclear 2`; `verification edge: checked 0, errors found 0 (rate None), unclear 0`; `verification path: checked 28, errors found 8 (rate 0.286), unclear 2`; `verification.csv rows: path 30, DEVICE 0`.
6. Device: 30 routes, 26 scripted, 4 unscriptable (`device/routes/MMEX/ROUTES.csv`). Final dry run `41576644702-1`: PASS 30, FAIL 0. Earlier dry-run id in the PROGRESS line: `41535141998-1`.
   - route_07 `StockHistoryRepository$UpdateType.<init>`: needs an investment account row to tap (no account exists on a fresh database, no row text grounded, no MMEX database fixture in $WEMU/fixtures) plus Morningstar as configured quote provider and a live Morningstar price download, a network result adb cannot create (follow-up: specified-but-unverified HTTP substitute)
   - route_08 `CurrencyRepository.saveExchangeRate`: ENV gate needs a live Fixer price download to finish while the currency list is started (FixerService BASE_URL https://api.fixer.io); a network result adb cannot create (follow-up: specified-but-unverified HTTPS/CA substitute)
   - route_11 `DatabaseMetadataFactory.getInstance(String,String)`: requires a real online cloud-storage account (Dropbox/OneDrive/GoogleDrive/Box/pCloud) holding a remotely-modified database; the sync-on-start plus remote-only pull branch cannot be produced by adb, fixtures, or setup (genuinely unscriptable on current evidence)
   - route_19 `ExceptionHandler.getLogcat`: double blocker, genuinely unscriptable on current evidence: (a) the prefix reaches showMessage only when the base currency is null, but an app-created database always sets a base currency; (b) getLogcat executes only if Toast.show() throws inside the posted Runnable's catch, and no grounded fault trigger exists on a normal foreground flow
7. Decision ids (`handoff/MUSE_DECISIONS.md`): D-MMEX-1, D-MMEX-2, D-MMEX-3, D-MMEX-4, D-MMEX-5, D-MMEX-6, D-MMEX-7, D-MMEX-8, D-MMEX-9, D-MMEX-10, D-MMEX-11, MMEX-D1, MMEX-D2, MMEX-B6-DispatchSplit, MMEX-B6-INFERRED, MMEX-B6-getContext, MMEX-B6-Gate-Ruling, MMEX-B6-Push-Ready, MMEX-R18-VERBATIM, MMEX-Sync-v2-AUTHORIZED, MMEX-designs-ALL-APPROVED, MMEX-B3-UIDRIVE, MMEX-B3-CAP, MMEX-D3-CAP-ACCEPT-ROUND2
8. Blocked: none.

## LibreTorrent

1. PROGRESS line: `- [K] LibreTorrent (labels, route checks, logs and device scripts DONE 2026-11-03; CI run ae203fe7; D9 run 41575076492-1 PASSED; awaiting user tick)`
2. CI (`graphs/LibreTorrent/scratch/ci_latest/SUMMARY.txt`, commit 185cd5e1): `methods 4732`; `verdicts: REACHABLE 3967, UNREACHABLE 765`; `unreachable by kind: branch_never_taken 12, closed_by_api_level 24, closed_by_configuration 1, framework_never_calls 13, no_trigger_in_app 715`; unclassified 0 (no UNRESOLVED in verdicts); `errors: 0`; `warnings: 0`.
3. Checks: `check 2: citations: 65 distinct, 0 problems; library citations (not checked): 0; evidence with FW-MEMORY / DYN / UNVERIFIED: 0`; `check 3: # LibreTorrent: 0 routes flagged`; `check 4: LibreTorrent: 1655 bytecode-cited edges checked, 549 skipped (lambda / clinit / anonymous), 55 implicit (super / enum / Dagger), 0 where the cited line does not show the callee`; `check 5-7: DEAD|FRAMEWORK_ONLY lines: 0`; `check 5-7: FW-MEMORY lines: 0`; `check 5-7: PENDING lines: 0`; `check 5-7: STRICT = True line in graph_def.py: 1`; `check 8 (--callers): 33 of 765 unreachable methods have a bytecode caller outside the set`.
4. Route table (`graphs/LibreTorrent/scratch/route_table.md`, lines 10-11): "- Counts: **CORRECT 18 / WRONG 9 / UNCLEAR 2**. Fixed (WRONG in the first draw, CORRECT now): 0. Rate = (fixed + WRONG) / (correct-only + fixed + WRONG) = (0 + 9) / (18 + 0 + 9) = **9/27 ≈ 0.3333**. UNCLEAR (2) is not in the rate and is reported separately."
5. Logs: verification.csv present, make_verification.py present, readme_notes.md present, LESSONS.md present, AGENT_NOTES.md present. `verification label: checked 792, errors found 9 (rate 0.011), unclear 2`; `verification edge: checked 78, errors found 25 (rate 0.321), unclear 0`; `verification path: checked 27, errors found 9 (rate 0.333), unclear 2`; `verification.csv rows: path 29, DEVICE 0`.
6. Device: 29 routes, 17 scripted, 12 unscriptable (`device/routes/LibreTorrent/ROUTES.csv`). Final dry run `41576644702-1`: PASS 29, FAIL 0. Earlier dry-run id in the PROGRESS line: `41575076492-1`.
   - route_02 `TorrentDownloadImpl.havePiece`: step 13 (NanoHTTPD$ClientHandler.run) needs an HTTP client connected to the app streaming server and the route needs a downloaded piece to stream (TorrentInputStream.waitForPiece); no harness primitive makes an HTTP request on the device, and piece data needs a live BitTorrent peer (network)
   - route_03 `FeedDao_Impl$11.finalize`: route WRONG as drawn (see route_table.md)
   - route_04 `PathResolver.join`: route WRONG as drawn (see route_table.md)
   - route_05 `SafFileSystem$FakePath.serialize`: route WRONG as drawn (see route_table.md)
   - route_06 `FeedDao_Impl$1.bind`: route WRONG as drawn (see route_table.md)
   - route_07 `BaseElement.getUri`: route WRONG as drawn (see route_table.md)
   - route_08 `AdvancedPeerInfo.isUtp`: the route builds a PeerInfo for a connected peer (PeerInfo.java:110); a connected BitTorrent peer needs a live swarm on the network, which adb cannot create on an AOSP emulator
   - route_11 `AddTagViewModel$TagAlreadyExistsException.<init>`: route WRONG as drawn (see route_table.md)
   - route_12 `SettingsRepositoryImpl.proxyRequiresAuth(boolean)`: route WRONG as drawn (see route_table.md)
   - route_13 `TorrentEngine$5.lambda$onTorrentMoving$4`: the route needs a torrent that finishes downloading (TorrentDownloadImpl.handleTorrentFinished, step 11) with move-after-download on; finishing needs the data from a live BitTorrent peer (network)
   - route_20 `SafFileSystem.getParentDirUri`: route WRONG as drawn (see route_table.md)
   - route_22 `SafFileSystem$FakePath.makeRelativePathNodes`: route WRONG as drawn (see route_table.md)
7. Decision ids (`handoff/MUSE_DECISIONS.md`): LibreTorrent D1, LibreTorrent D2, LibreTorrent D3, LibreTorrent D4, LibreTorrent D5, LibreTorrent D6, LibreTorrent D7, LibreTorrent D8, LibreTorrent D9, LibreTorrent D10, LibreTorrent D11, LibreTorrent D12, LibreTorrent D13, LibreTorrent D14, LibreTorrent D15, LibreTorrent D16, LibreTorrent D17, LibreTorrent D18, LibreTorrent D19, LibreTorrent D20, LibreTorrent D21, LibreTorrent D22, LibreTorrent D23, LibreTorrent D24, LibreTorrent D25, LibreTorrent D26, LibreTorrent D27, LibreTorrent D28, LibreTorrent D29, LibreTorrent D30, LibreTorrent D31, LibreTorrent D32, LibreTorrent D33, LibreTorrent D18 correction, LibreTorrent D37, LT-A1-C1, LT-A1-C2, LT-A1-C3, LT-A3-B019-1, LT-b003-minus1-EXPLAINED, LT-b003b007-SOURCE-RESTORE, LT-row26-NOT-CLOSED, LT-citation-no-increase, LT-repair-LANDED, LT-restoration-READY-78, LT-row26-OPEN-CONFIRMED, LT-restoration-LANDED, LT-HAZARD-GATE-CLOSED, LT-2205-1, LT-2205-2, LT-2205-3, LT-2205-4, LT-2205-6, LT-2205-7, LT-2205-8, LT-2205-9, LT-2205-10, LT-2205-b015
8. Blocked: none.

## What waits for the user

- Tick the 5 `[K]` lines in `handoff/PROGRESS_V2.md` (only the user ticks; no agent writes `[x]`).
- Choose the emulator image for the real device run.
- The workflow-side items for the Amaze SSH routes listed in `handoff/NEXT_DEVICE_REPLAY.md` (a step installing openssh-server; WITH_SSH_SERVER=1 for Amaze jobs only). The user's reviewer edits the workflow, never an agent.
- Start the real run by hand from `.github/workflows/device-replay.yml` with `dry_run=false`.

## The tools change

- Commit `4e0ad648` "tools: check_citations ROOT_STYLE must not match inside a longer path" (rewritten from local `a04a8b05`): `tools/check_citations.py` line 20 now matches `core/`, `services/`, `data/`, `libcore/` and `packages/` only at the start of a path (`(?<![\w/])`), so app paths such as `libretorrent/core/FeedParser.java` are no longer read as Android framework citations.
- Effect in CI `ae203fe7`: every app keeps 0 check-2 problems; distinct counts dropped only where app paths had been miscounted as framework paths (AmazeFileManager 2 to 1, AnkiDroid 274 to 273, MMEX 250 to 247, per the reviewer's measurement). No app's problem count changed except LibreTorrent's FeedParser false alarms, which went to 0.
