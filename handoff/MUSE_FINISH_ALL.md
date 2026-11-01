# MUSE_FINISH_ALL: the complete, strict work order for every open item (all 13 apps)

Written 2026-11-01 by the orchestrator (Claude, on the user's Mac), on the user's instruction to give Muse everything it needs to finish every open cell, with nothing missing.

**Precedence.** This file overrides `handoff/MUSE_OVERNIGHT_PROMPT.md`, `handoff/MUSE_COMPLETE_BRIEF.md` and `handoff/MUSE_HANDOVER.md` wherever they differ. The rule files still apply where this file is silent: `KIRO_CONVERT_APPS.md` sections 3 to 7, `KIRO_CORRECTIONS.md` C1 to C8, `SCHEMA_V2.md`, `AGENT_BRIEF_V2.md` section 5, and `CHATGPT_PROMPT_LIBRETORRENT_3.md` rules A to K, with the USE_AUTO exception in brief section 4.1.

**Scope.** Every cell of the table in section 1 except device checks. The user chooses the emulator later. Tonight: no emulator, no adb, no device scripts, no new repositories, no APKs.

**Nobody will answer. Never stop to ask.** Decide by section 6, record the decision, and continue. A step that truly cannot be done is written under `## Blocked` with the reason. Then go to the next item.

## 1. What is left (the work items)

Each cell names the work item IDs in section 5. Device checks (deferred) apply to every app.

| App | Labels | Checks 2–8 | Route checks | Logs |
|---|---|---|---|---|
| Currency | done | pass | done (28) | **T1** |
| Diary | done | pass; 5 grep hits to note | done (30) | **T2** |
| hash-checker | done | pass; 11 grep hits to note | done (37) | **T3** |
| Omni-Notes | done | pass; 11 grep hits to note | done (33; 1 wrong, allowed) | **T4** |
| openlauncher | done | pass; 1 grep hit to note | done (27) | **T5** |
| Vanilla-Music | done | pass | done (30) | **T6** |
| Markor | done | pass | done (30) | **T7** |
| AnyMemo | done | pass (1 flagged route, explained) | done (30) | **T8** |
| Aegis | done | **C1** | **C2, C3** | **C4** |
| AmazeFileManager | done | **B1–B4** | **B6** | **B7** |
| AnkiDroid | done; strict mode off | **B1–B4** | **B6** | **B7** |
| MMEX | done; strict mode off | **B1–B5** | **B6** | **B7** |
| LibreTorrent | **A1–A6** | **A5** | **A7** | **A8** |

The final gate for every app is **F1** (section 5.5).

## 2. How you work: setup, local builds, pushing, CI

### 2.1 Get a complete working tree (once, before anything else)

The connector refuses files above about 1 MB. Everything you need is therefore also on the branch in parts below 700 KB.

1. **Fetch the files, byte for byte, from branch `work-2026-10-31`:**
   - `handoff/workspace_bundle/MANIFEST.json`
   - every part it lists, `handoff/workspace_bundle/<bundle>/<bundle>.partNNN.txt` (125 parts, about 80 MB)
   - `handoff/connector_kit/unpack.py`

   Keep the same relative layout under a local folder `wb/`.
2. **Unpack:** `python3 -I unpack.py wb gtr`. It checks the SHA-256 of every part, every bundle and every file, and stops with the name of anything bad. Fetch a bad part again, then rerun. It must end with `all bundles OK: 6178 files written`.
3. **What `gtr/` then holds,** at commit 44be970: `tools/`, `handoff/examples/`, `handoff/connector_kit/`, `handoff/ci/`, `fw_src/`, and for each app its graph inputs (`graph_def.py`, `graph_def_mod/`, `method_list.json`, `auto_calls.json`, `calls_all.json` for Vanilla-Music, `verification.csv`, `make_verification.py`, `readme_notes.md`, `LESSONS.md`, `AGENT_NOTES.md`). It also holds LibreTorrent's `parts/`, `scratch/merge-ready/` and `scratch/gates.md`, Markor's four scratch JSON files, and every app's sources under `final_java_only/<App>/app/` (without the `build`, `test`, `androidTest` and JaCoCo report folders).
4. **Bring it up to date.** List the commits on the branch after 44be970. For every file they changed, except `graphs/*/out/**` and `graphs/*/scratch/ci_latest/**`, fetch the branch version into `gtr/`.
5. **Check the tree.** In `gtr/`, run `bash handoff/ci/rebuild.sh Currency MMEX`. The printed summaries must match `graphs/Currency/scratch/ci_latest/SUMMARY.txt` on the branch, and the MMEX values in `handoff/baseline_2026-11-01/MMEX/`: errors 0, warnings 0, and checks 2 and 4 showing 43 and 244 problems. If they differ, your tree is wrong; fix that first.
6. **Clone `https://github.com/bugfixops/work-emulator.git`** (public). Use only `classes/<App>/<i>/` for `javap -c -p`. Install a JDK 17 or newer.

### 2.2 Local builds (use these for every edit)

From the `gtr/` root:

- **Build:** `python3 -I tools/build_graph.py graphs/<App> <prefix>`. Prefixes: Currency currency, Diary diary, hash-checker hash-checker, Omni-Notes omni-notes, openlauncher openlauncher, Vanilla-Music vanilla, Markor markor, AnyMemo anymemo, Aegis aegis, AmazeFileManager amazefilemanager, AnkiDroid ankidroid, MMEX mmex, LibreTorrent libretorrent.
- **Build plus all eight checks:** `bash handoff/ci/rebuild.sh <App>`. It writes `graphs/<App>/scratch/ci_latest/` (`1_build.txt` to `8b_scan_callers.txt` and `SUMMARY.txt`).
- **Syntax check:** `python3 -m py_compile graphs/<App>/graph_def.py` (and every file you changed in `graph_def_mod/` or `parts/`).
- **No `coverage_baseline.json` locally.** It is not in the bundles, because it is tool coverage and never evidence. Your local `sanity_check.csv` and the sanity lines in the build report will therefore differ from CI. Ignore them; nothing else changes.

### 2.3 Where and how to push

- **Push target:** only branch `work-2026-10-31` of `bugfixops/ground-truth-results`, through the connector. Never push to `main` or `result`. Never force-push. Never delete history.
- **Every file you push must be below 900 KB.** The large graph files are already split:
  - `graphs/AmazeFileManager/graph_def.py` with `graph_def_mod/01.py`
  - `graphs/AnkiDroid/graph_def.py` with `graph_def_mod/01.py`
  - `graphs/MMEX/graph_def.py` with `graph_def_mod/01.py` and `02.py`

  They load in name order and behave exactly like one file; the build outputs were byte-identical before and after the split. Edit the file that holds the text. If any file grows past 900 KB, run `python3 -I handoff/connector_kit/split_graph_def.py graphs/<App>` and prove the build output is byte-identical before you push.
- **The paths you may write:**
  - `graphs/<App>/graph_def.py`
  - `graphs/<App>/graph_def_mod/*.py`
  - `graphs/LibreTorrent/parts/*`
  - `graphs/<App>/verification.csv`, only as produced by `make_verification.py`
  - `graphs/<App>/make_verification.py`
  - `graphs/<App>/readme_notes.md`, `LESSONS.md`, `AGENT_NOTES.md`
  - `graphs/<App>/scratch/**`, except `scratch/ci_latest/`
  - `handoff/PROGRESS_V2.md`, only the line of an app that passed F1, and never `[x]`
  - `handoff/MUSE_RUN_LOG.md`, `handoff/MUSE_DECISIONS.md`, `handoff/MUSE_FINISH_SUMMARY.md`
  - `handoff/REBUILD_REQUEST.txt`
- **Never write:**
  - `graphs/*/out/**` and `graphs/*/scratch/ci_latest/**` (only CI writes these)
  - `tools/`, `final_java_only/`, `fw_src/`
  - `.github/`, `handoff/ci/`, `handoff/connector_kit/`, `handoff/workspace_bundle/`
  - other apps' folders outside your current work item
- **Commit message:** `<App> <item id>: <what> (local build: methods N, REACHABLE R, UNREACHABLE U, unclassified C, errors E, warnings W)`. The counts come from the local build you ran after your last edit.
- **Commit identity:** `bugfixops <bugfixops@users.noreply.github.com>`. The user's own identity is also accepted.
- **When to push:** after every finished work item step that changes the graph; after every 5 merged LibreTorrent parts; and at least every 60 minutes while work goes on.
- **Never push** a `graph_def.py`, module or part that fails `py_compile`, or whose local build shows more errors than before your edit.
- **Never commit** tokens, secrets, personal data, APKs, zips, or absolute paths from your machine (`/home/...`, `~/workspace/...`). Write repo-relative paths.

### 2.4 CI: the authoritative build, checks and `out/` files

- **What it is.** `.github/workflows/rebuild-graphs.yml` runs `handoff/ci/rebuild.sh` on GitHub, with the full repo. It then commits `graphs/<App>/out/` and `graphs/<App>/scratch/ci_latest/` as `bugfixops` with the message `[ci] rebuild and checks (<apps>)`. Tested on 2026-11-01: a Currency request produced commit 7f8646c three minutes after the push.
- **To run it,** push `handoff/REBUILD_REQUEST.txt` with:
  - line 1: unchanged
  - line 2: `# request <UTC time> <your purpose>`, which must be new each time
  - then one app name per line, or `all`
- **Read the result.** Wait for the `[ci]` commit that comes after your request commit, then read `graphs/<App>/scratch/ci_latest/SUMMARY.txt` and the files next to it. Its first line names the commit it built; it must be your request commit or a later one.
- **Use it sparingly.** At most one request every 10 minutes. List all the apps you need in one request.
- **When CI is authoritative:** for every gate, every PROGRESS line, and every count in the final summary. Local builds are for iteration.
- **If no `[ci]` commit appears within 30 minutes,** write that in the run log and continue with local builds. Retry once later.

## 3. Hard rules (any break stops that item; record it and continue)

1. **Every label and every edge comes from source you printed (`sed -n` with file and line range) and read.** Bytecode (`auto_calls.json`, `javap`) is INFERRED evidence for generated and library code. It never replaces printing the app source around a guard. Tool coverage, the old generated graphs and the build's REACHABLE count are never evidence.
2. **`confirmed_by` is only SOURCE or INFERRED.** Never write DYN, FW-MEMORY or UNVERIFIED. Framework claims cite FW-SRC lines from `fw_src/android-8.1.0_r1/`; otherwise they are INFERRED, with "source not read".
3. **Never mark a method UNREACHABLE if it has a route.** Every UNREACHABLE has one kind (`no_trigger_in_app`, `branch_never_taken`, `framework_never_calls`, `closed_by_configuration`, `closed_by_api_level`), a reason and a source reference.
4. **For the eight ticked apps,** never change a label, an edge or a route, and never edit their `graph_def.py`. T1 to T8 are log work only.
5. **`verification.csv` is only ever written by `graphs/<App>/make_verification.py`.** Run it from the repo root, with relative paths only. It must be deterministic: two runs in a row give byte-identical files.
6. **Helpers.**
   - At most 4 per app, and at most 12 in total.
   - At most 40 methods (labels) or 10 routes (route checks) per helper.
   - Helpers never edit `graph_def.py`, modules, `verification.csv`, `PROGRESS_V2.md` or `AGENT_NOTES.md`, and they never run the build.
   - You check at least 1 claim in 5 of every helper part with `sed -n` before you merge it.
   - A helper with no output for 30 minutes is stuck: give its items to one new helper. If that one stalls too, write `## Blocked` and carry on.
7. **Never report a count you did not print** in the same session. Never write "passed" without the saved output.
8. **Never write `[x]`.** Never change another app's PROGRESS line.

## 4. Logs every app must end with (the standard for T, B, C and A)

- **`graphs/<App>/verification.csv`.** The header is exactly `type,item,result,confirmed_by,ref,edges,note`.
  - It has one `path` row per route in the final sample (after the last fix and the redraw).
  - It keeps the `label` and `edge` rows from the route checks.
  - It is written only by `make_verification.py`.
- **`graphs/<App>/make_verification.py`,** modelled on `graphs/AnyMemo/make_verification.py`:
  - It validates every row against the built graph (`out/methods.csv` and the trigger JSON): every edge id exists, every label verdict matches, and every path row's edges are the method's route.
  - It stops with an error on any mismatch.
  - It writes the rows in a fixed, sorted order.
  - It reads only repo-relative files.
- **`graphs/<App>/readme_notes.md`** with these five headings, exactly and in this order:
  1. `## What the re-audit changed (compared with the schema 1 graph)`
  2. `## How the checked paths were chosen`
  3. `## What waits for a device (API 27)`
  4. `## Hazard candidates (from reading the code, not reproduced)`
  5. `## Limits`

  CI runs `gen_readme_v2.py` and commits `out/README.md`.
- **`graphs/<App>/LESSONS.md`:** 3 to 8 bullets on what found real errors.
- **`graphs/<App>/AGENT_NOTES.md`:** the time, each step, the build file or CI commit, `## Current step` and `## Decisions made by Muse (for the user and Yang to review)`.

## 5. The work items

### 5.1 The eight ticked apps (T1 to T8): logs only, no graph changes

**T1 Currency**
1. **Write `graphs/Currency/make_verification.py`.** There is no old writer.
   - Seed its row data once from the current `graphs/Currency/verification.csv`, into `graphs/Currency/scratch/verification_rows.json`, which is repo data and is pushed.
   - Validate every row against the build (section 4).
   - Write the file in the current row order.
   - **Accept when** running it gives a `verification.csv` that is byte-identical to the current one: `cmp` prints nothing, and two runs are identical. If a row fails validation, the row is out of date. Re-check that route from printed source, correct the row, and record it in `scratch/fix_log.md`. The file then changes for that reason only.
2. **Write `graphs/Currency/LESSONS.md`,** from `readme_notes.md` and `AGENT_NOTES.md`.
3. **CI request for Currency. Accept when** `SUMMARY.txt` shows errors 0 and warnings 0; check 2: 0 problems; check 3: 0 flagged; check 4: 0; checks 5 to 7: 0, 0, 0; STRICT line 1; and path rows 28.
4. **Check 8 shows 1 UNREACHABLE method with an outside caller** (`Singleton.getList`, from `ChartActivity.onCreate`). Confirm that its reason explains that caller. If it does not, explain it in `readme_notes.md` under `## Limits`, with printed lines. Do not edit the graph.

**T2 Diary.** As T1, plus:
- In `readme_notes.md` under `## Limits`, write: "check 5 counts 5 lines (graph_def.py 199, 228, 1608, 1624, 1629). They are the schema-1 dictionaries DEAD and FRAMEWORK_ONLY, used only as temporary containers that are converted to UNREACHABLE entries and emptied at line 1629. No placeholder label exists."
- Diary has no `auto_calls.json`, so check 8 does not apply. Say so in the same section.

**T3 hash-checker.** As T1, with these differences:
- **Writer.** The old writer, `handoff/examples/make_vlog_hash_checker.py`, read `sample_final.txt` from a Claude session folder that no longer exists. Write a portable `graphs/hash-checker/make_verification.py`. Take the sample list from the current `path` rows (or save it as `graphs/hash-checker/scratch/sample_final.txt`), and keep the same rows. The output must be byte-identical to the current file.
- **Notes under `## Limits`:**
  - check 5 counts 7 lines (63, 79, 684, 692, 695, 704, 706): the temporary DEAD/FRAMEWORK_ONLY containers, converted to UNREACHABLE.
  - check 7 counts 4 lines (33, 460, 463, 464): the page id `S_MAIN_EXIT_PENDING`. Renaming it would change the edge ids and make the checked paths stale.
- **Check 8 shows 4.** Confirm each one is explained, as in T1 step 4.

**T4 Omni-Notes.** As T1, with these differences:
- **Writer.** The old writer, `handoff/examples/make_vlog_omni_notes.py`, read an old graph from a session folder that no longer exists. Write a portable `make_verification.py` with the same rows; byte-identical output.
- **Note under `## Limits`:** check 5 counts 11 lines (1635, 1641, 1693, 1694, 1793, 1794, 1801, 1808, 2078, 2136, 2145): the DEAD/FRAMEWORK_ONLY containers and their SUPPRESS lines, not placeholders.
- **The one wrong route,** `DbHelper.deleteNote(long,boolean)`, is an allowed verdict. Keep it, and report it in the route table.
- **Check 8 shows 5.** Confirm each one, as in T1 step 4.

**T5 openlauncher**
1. Its `make_verification.py` exists and reproduced the current file byte for byte on 2026-11-01. Run it twice. **Accept when** both runs are byte-identical to the current file.
2. **Note under `## Limits`:** check 7 counts 1 line (942), which is AsyncTask code text, not a placeholder.
3. CI request; acceptance as in T1, with path rows 27. Check 8 shows 2; confirm both, as in T1 step 4.

**T6 Vanilla-Music**
1. Its `make_verification.py` reproduced the current file byte for byte on 2026-11-01. Run it twice; it must be identical both times.
2. CI request; acceptance as in T1, with path rows 30. Check 8 shows 3; confirm them.

**T7 Markor**
1. **Rewrite `graphs/Markor/make_verification.py` so it is portable.**
   - Lines 8 to 13 use absolute paths: `WORK`, `SCR` (a session folder that no longer exists) and `APP` (a source copy outside the repo).
   - Line 20 reads `methods_before_refs.csv` from that missing folder.
   - Line 23 calls `verify_sample.py` without a seed.

   Use repo-relative paths, data saved under `graphs/Markor/scratch/`, and the seeded sample (`verify_sample.py Markor 30 20261025`, or the current `path` rows). **Accept when** the output is byte-identical to the current `verification.csv`, and two runs are identical.
2. CI request; acceptance as in T1, with path rows 30. Check 8 shows 0. Markor's `graph_def.py` reads `scratch/{hier,textcount,dotcount,route_guards}.json`; keep them.

**T8 AnyMemo**
1. Its `make_verification.py` gives the same 347 rows as the current file, but in a different order on each run, because it iterates over Python sets.
   - Make the order fixed: sort the label and edge rows by (type, item).
   - Prove the row set is unchanged: `sort` both files and `cmp`; it must print nothing.
   - Then commit the new, ordered file.
   - **Accept when** two runs are identical and the sorted comparison is identical.
2. CI request; acceptance as in T1, with path rows 30. Check 3 shows 1 flagged route. It is explained in `readme_notes.md` line 77, and that is allowed. Check 8 shows 3; confirm them.

**For T1 to T8:** keep their `[x]` lines in PROGRESS_V2.md exactly as they are.

### 5.2 AmazeFileManager, AnkiDroid, MMEX (B1 to B7, one app at a time per sub-stream; the three may run in parallel)

The problem lists are in `handoff/baseline_2026-11-01/<App>/` (`2_citations.txt`, `4_bytecode.txt`, `8b_scan_callers.txt`). Regenerate them locally with `bash handoff/ci/rebuild.sh <App>`.

**B1. Strict mode.** AnkiDroid `graph_def.py` line 10 and MMEX `graph_def.py` line 8 read `STRICT = False`. Change both to `STRICT = True`. AmazeFileManager already has it.
- **Accept when** the local build shows errors 0 and warnings 0. It did on 2026-11-01.

**B2. Check 2: citation problems** (AmazeFileManager 23, AnkiDroid 3, MMEX 43). For each PROBLEM line:
- "file not held: X.java": search `final_java_only/<App>/` for the file. If it exists, write the citation in the form the passing citations of that app use (read `tools/check_citations.py` to see how a path resolves; do not edit it). If it is a generated or library file that is not in the upload, rewrite the claim as INFERRED with "source not read".
- "line out of range" or a wrong line: print the file and correct the line.
- **Accept when** check 2 shows 0 problems.

**B3. Check 4: bytecode lines** (AmazeFileManager 63, AnkiDroid 48, MMEX 244). These edges are mostly bytecode edges that `USE_AUTO` adds. Their evidence text comes from `auto_calls.json`, so fix them through the `EDIT` hook in `graph_def.py`. `EDIT` is a function that gets every edge before its id is made; it already exists in some graphs. If one does not exist, define it. In that hook:
- **"file not found" for a generated class** (for example `DaggerMmxComponent.java`): rewrite that edge's evidence as `INFERRED generated <Class> (no source in the upload; bytecode call)`.
- **"name on line N" (the call is on another line):** correct the cited line to the printed line. `python3 -I tools/check_bytecode_lines.py <App> --emit` prints a `FIX_LINES` literal you can use.
- **A basename that matches two files:** rewrite the citation with the path that makes it unique (see A5).

**Accept when** check 4 shows "0 where the cited line does not show the callee". Edge ids change for the edited edges. None of these apps has path rows yet, so nothing goes stale.

**B4. Check 8: UNREACHABLE methods with a bytecode caller outside the set** (AmazeFileManager 4, AnkiDroid 169, MMEX 19). For each one:
- print the caller's lines;
- either write the reason that caller never calls it in the standard configuration (and add the edge to `SUPPRESS`, with that reason), or give the method a route;
- for AnkiDroid's 169, group them by caller and handle each group once.

**Accept when** every method listed by `scan_unreachable.py <App> --callers` has its caller named and explained in its reason. Record the list in `scratch/check8_explained.md`.

**B5. MMEX wording.** `graph_def_mod/02.py` lines 1277 and 1402 use the word DEAD in reason and comment text. Reword them, for example "never called". **Accept when** check 5 shows 0.

**B6. Route checks.**
1. **Known issues first** (MUSE_HANDOVER WP2). Your earlier files under `graphs/<App>/scratch/proposals/` and `scratch/overnight-20261101/` are inputs only.
   - AmazeFileManager: the Glide contradictions (`GlideOptions.*`, `GlideRequest.*`, rule C5), E89e2cedd (`SftpConnectDialog.lambda$null$2`) and Ee1aeff93 (`CompressedExplorerFragment.<init>` to `Decompressor.decompress`).
   - AnkiDroid: `Card.toString` (find its caller before you route it), `EasySSLSocketFactory.equals` and `hashCode`, the API 27 versus target 23 question, and the `Hooks.runFilter` pair.
   - MMEX: the INFERRED UNREACHABLE entries (`getPageTitle`, `AccountBillsWidgetService.onGetViewFactory`, `MmxDatabaseUtils.<clinit>`, the generated Dagger and ButterKnife methods).
2. **Sample:** `python3 -I tools/verify_sample.py <App> 30 20261025 > graphs/<App>/scratch/sample_30.txt`. If it gives fewer than 30, record the number and why.
3. **Print the routes.** Copy `handoff/examples/route_print_template.py` to `graphs/<App>/scratch/route_print.py` and set its constants (KIRO_CONVERT_APPS section 4). `grep -n AnyMemo graphs/<App>/scratch/route_print.py` must print nothing. Print every route into `scratch/route_print/`.
4. **Judge every step** against its printed lines, including the if, catch and for conditions, and against the mistakes list in AGENT_BRIEF_V2 section 5. A step you did not print is not checked.
5. **Fix wrong routes,** one at a time: edit, rebuild, reprint, and log in `scratch/fix_log.md` (method, step, lines printed, what changed).
6. **Redraw.** After the last fix, draw the sample again with the same command. The final table covers only the final draw; re-read every route whose steps changed.
7. **Write the table,** `scratch/route_table.md`: method, verdict (correct, fixed, wrong or unclear), steps, and the reason for wrong or unclear. Error rate = (fixed + wrong) / (correct + fixed + wrong). A route you cannot fix without editing `tools/` is `wrong`, with the reason.

**B7. Logs** (section 4). `make_verification.py` writes the path rows from `route_table.md` and the label and edge rows from the checks. Then `readme_notes.md` and `LESSONS.md`. MMEX already has a draft `make_verification.py` (pushed 2026-11-01); test it like any other.

**F1** follows in section 5.5.

### 5.3 Aegis (C1 to C4)

**C1. Check 2.** Edges E24649299 and E2a97bab7 cite `services/LaunchScannerTileService.java`, which is reported as "file not held". The file exists at `final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/services/LaunchScannerTileService.java`. Write the citation in the form that passing Aegis citations use, and print the lines. **Accept when** check 2 shows 0.

**C2. The 7 open decisions.** Decide each one yourself, and record it in `handoff/MUSE_DECISIONS.md` (section 6). You already made D1 to D7 overnight (`graphs/Aegis/scratch/overnight-20261101/DECISIONS.md`). Re-check each against printed source, then apply it in `graph_def.py`. The starting choices (MUSE_OVERNIGHT_PROMPT section 5.2), by line in Aegis's AGENT_NOTES:

| Line | Item | Choice |
|---|---|---|
| 379 | R1 step 13 | Add the producer edge, with `needs_state`, using variant nodes if needed |
| 479 | Route 4 step 9 | A STATE precondition with its producer; no reclassification |
| 599 | Route 1 step 21 | Reprint it; the notes at about line 609 say it is fixed |
| 603 | Step 14 | The method stays REACHABLE; a STATE `settings` gate with a relaunch; the route verdict is `unclear` under rule D2 |
| 609 | G3_5 step 34 | Model both the default Authy path and the row-tap path |
| 636 | GlideRequests step 50 | An ENV `other` gate (root shell, text copied from the code) on the app-import edge |
| 659 | `readFromApp` | Print `AbsListView.performItemClick` from `fw_src/android-8.1.0_r1/core/java/android/widget/AbsListView.java` and the dialog's choice mode, then write the edge as printed |

**C3. Route steps 6 to 10,** from the last RESUME POINT in `graphs/Aegis/AGENT_NOTES.md`.
- 23 round-7 routes are not checked yet (your `steps6-10_report.md`).
- Fix the "structural" ERROR steps with variant nodes that only the producer chain reaches (the `MainActivity.doShortcutActions@SCAN` technique). Never edit `tools/`.
- A step still not fixable makes its route `wrong`, with the reason.
- Then sample, redraw and write the table, as in B6 steps 2 to 7.

**C4. Logs** (section 4). Your draft `graphs/Aegis/make_verification.py` (pushed 2026-11-01) must pass section 4. It lives in `graphs/Aegis/`, never in `tools/`. Your drafts in `scratch/overnight-20261101/logs-phase2-drafts/` are inputs.

### 5.4 LibreTorrent (A1 to A8)

State on 2026-11-01: 120 proposal files in `graphs/LibreTorrent/scratch/merge-ready/`, with 3,964 REACHABLE, 691 UNREACHABLE and 77 OPEN. The orchestrator recounted them, and every row matches the batch plan. Only batches 13 and 14 are in `graph_def.py`. The current build shows 2,266 unclassified and 222 warnings.

**A1. Close the 77 OPEN rows** (batches 2, 12, 17, 21, 22, 28 to 34, 48, 73, 82, 103, 114). Use the rules in MUSE_COMPLETE_BRIEF section 4.2. You can now run the full-folder grep and `javap` yourself:

- **The 42 Parcelable rows.** Run `grep -rn` over `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main` for each class's marshalling sites: `putExtra`, `putParcelable`, `putParcelableArrayList`, `writeParcelable`, the Fragment arguments, and `getParcelable*`.
  - A printed write or read site on a reachable route makes the matching method REACHABLE.
  - No site after the full grep makes it UNREACHABLE (`framework_never_calls` for `newArray` and `describeContents`, `no_trigger_in_app` otherwise).
  - Save each grep in `scratch/A1_parcel_greps/`.
- **The 6 mapper rows.** `javap -c -p` on `work-emulator/classes/LibreTorrent/0/org/proninyaroslav/libretorrent/DataBinderMapperImpl*.class`, plus `auto_calls.json`, plus the AnyMemo pattern (brief 4.2, item 3).
- **The 2 Room rows** (48/12 and 48/13). Room's library source is not needed: label them from the bytecode callers (`auto_calls.json`, `javap`), INFERRED.
- **The 27 R5 rows** (plain constructors, `compareTo`, `equals`, getters, setters). Brief 4.2 items 8 and 9: callers by grep plus bytecode.

**Accept when** a recount of the 120 files (last occurrence per row) gives OPEN 0.

**A2. Batch 5 rows 19, 20, 25, 26 (your D29).** Settled: they stay UNREACHABLE `no_trigger_in_app`. On 2026-11-01 the orchestrator checked `auto_calls.json` for all 200 base `*Binding` statics of batches 5 to 9, and none has a caller outside its own class. That includes `AddTorrentInfoBinding` and `DetailTorrentAppbarBinding`; the parent layouts reach the included bindings through the mapper and `*BindingImpl.<init>`. Cite that check.

**A3. Turn every batch file into a part,** `graphs/LibreTorrent/parts/b<NNN>.py` (three digits), with `.md` and `scratch/b<NNN>_printed.txt`, in the format of `parts/b013.py`.
- The old `parts/b016.md`, `b017.py`, `b018.md` and `b018.py` are superseded; overwrite them.
- Never write parts for batches 13 and 14; they are inline already.
- For each proposed UNREACHABLE method that a proposed REACHABLE method calls in the bytecode (31 such methods on 2026-11-01), add the calling edge to `SUPPRESS` with the printed reason. For example, `TorrentNotifier.java:276` returns early for SDK 26 and above, so its calls are `closed_by_api_level` on API 27. Without this, the build warns "UNREACHABLE but has incoming edges".

**A4. Merge, one part at a time.**
1. **Trunks first,** each from the launcher entry: feed refresh (`SettingsFragment.java` lines 122 and 195 to 198, `PreferenceActivity.java` lines 113 to 114, `FeedSettingsFragment.java` lines 121, 134 and 142, then `Scheduler`, then `FeedFetcherWorker`); the torrent service and engine (`TorrentService.onStartCommand`, then `TorrentEngine.doStart`, then `session.start`, then `TorrentSessionImpl.onAfterStart`, then `engineListener`); add-torrent; the streaming server; the notification actions. Write them as a part, `parts/b000_trunks.py`.
2. **Then the batches in plan order:** 1 to 12, then 15 to 120.
3. **For each part:**
   - add its file name to the `MERGED_PARTS` list at the end of `graphs/LibreTorrent/graph_def.py`
   - run `python3 -m py_compile` on it and on the part
   - build locally, and save the output as `scratch/build_<n>.txt`
   - errors must not rise
   - write one line in AGENT_NOTES: part, build file, counts
   - push the part, `graph_def.py` and the build file

   These are the C1 conditions.
4. **After the trunks are in:**
   - set `STRICT = True` (line 8)
   - delete the `AUTO_DEAD` line (47) and the `FW-MEMORY` rewrite in `_source_audit_edit` (lines 52 to 53; that function is LibreTorrent's edge-edit hook)
   - fix every claim that the rewrite was hiding: print FW-SRC lines, or write INFERRED with "source not read"
   - from then on, every build shows the remaining unclassified methods as errors; drive them to 0

**A5. Checks.**
- **Check 4 crashes** (an IndexError at `check_bytecode_lines.py` line 77) because 41 bytecode edges cite a basename that matches two files. The tool picks the shorter file, and the cited line is past its end:
  - 22 edges from `drawer.TagsAdapter*` cite `TagsAdapter.java`, which should be `ui/main/drawer/TagsAdapter.java` (316 lines), not `ui/tag/TagsAdapter.java` (111 lines);
  - 19 edges cite `FeedParser.java`, which should be the app's `core/FeedParser.java`, not the library's `com/ernieyu/feedparser/FeedParser.java`.

  In `_source_audit_edit`, rewrite the citation of those edges to the qualified path (for example `SRC ui/main/drawer/TagsAdapter.java:230 (bytecode)`). Then bring check 4 to 0.
- **Check 2** shows 102 problems: fix them as in B2.
- **Checks 5 and 6** count the `AUTO_DEAD` and `FW-MEMORY` lines, which go away in A4.

**A6. The labels gate.** CI request for LibreTorrent. **Accept when** `SUMMARY.txt` shows unclassified absent (0), errors 0 and warnings 0, `STRICT = True` line 1, and checks 2 and 4 at 0. Then change the PROGRESS line to `- [L] LibreTorrent (labelled <date>; route checks not started)`.

**A7. Route checks:** as B6 steps 2 to 7.

**A8. Logs:** as B7 (section 4).

### 5.5 F1, the final gate for each app

For every app except the eight ticked ones:
1. Push the final edits, then send a CI request for the app.
2. **Accept when** `SUMMARY.txt` (built at your final commit or later) shows:
   - errors 0, warnings 0, no unclassified, and STRICT line 1
   - check 2: 0 problems
   - check 3: 0 flagged, or each flagged route explained in `readme_notes.md` with printed lines
   - check 4: 0
   - checks 5 to 7: 0 (or the hits explained in `## Limits`, ticked apps only)
   - check 8: every caller explained (B4)
   - path rows equal to the final sample size
3. All section 4 logs exist and pass.
4. Then change the app's PROGRESS line to exactly `- [K] <App> (labels, route checks and logs DONE <date>; device checks not started; awaiting user tick)`.

For the eight ticked apps, F1 means T1 to T8 are accepted. Their lines stay `[x]`.

## 6. Decisions: Muse decides, records, and continues

1. Look for a written rule, and apply it.
2. If none, look for a precedent in the eight ticked apps (`graph_def.py`, `out/methods.csv`, `readme_notes.md`), and apply it.
3. If none, choose the option that models what the printed source does, without editing `tools/`:
   - prefer adding a gate, a `needs_state` or a variant node over deleting a route
   - never change a label without printed source
4. **Record every decision** in `handoff/MUSE_DECISIONS.md` (append) and in the app's AGENT_NOTES, with:
   - an id
   - the app
   - the item, with its file and line
   - the options
   - the choice
   - the printed evidence (file:lines)
   - the effect on labels and routes
   - how to reverse it

   Write each one as Muse's decision under the user's instruction of 2026-11-01. Never write a decision in Yang's name.

## 7. Order and parallel streams

Run these in parallel. Each stream has its own apps, and each app has its own `graphs/<App>/WORKING_LOCK`.

- **Stream 1:** T1 to T8 (small). Start first.
- **Stream 2:** B1 to B7 and F1 for AmazeFileManager, AnkiDroid and MMEX. Do B1 to B5 for all three before any B6.
- **Stream 3:** C1 to C4 and F1 for Aegis.
- **Stream 4:** A1 to A8 and F1 for LibreTorrent. This is the longest; start it at once.

## 8. State, resets, the end

- **Run log.** Append one line per step to `handoff/MUSE_RUN_LOG.md`: UTC time, stream, app, item id, command, local build or CI commit, counts. Each app's `AGENT_NOTES.md` keeps `## Current step`.
- **On every start or reset:**
  - re-read this file
  - read the last 30 lines of the run log and each app's `## Current step`
  - refresh your tree (section 2.1 step 4)
  - continue

  Never redo finished work. Never start a second worker on an app whose `WORKING_LOCK` is younger than 30 minutes.
- **Usage, session or rate limit:** start no new helpers, save the current step everywhere, push, and stop. Continue from the saved state when you are restarted.
- **When every F1 has passed, or nothing more can be done:**
  1. Write `handoff/MUSE_FINISH_SUMMARY.md`, one section per app:
     - its PROGRESS line
     - methods, REACHABLE, UNREACHABLE by kind, unclassified, errors, warnings, from CI `SUMMARY.txt`, with its commit
     - the eight checks
     - the route table (correct, fixed, wrong, unclear, error rate)
     - the logs present
     - the decision ids
     - anything blocked
  2. Push it.
  3. Final message, at most 15 lines.
- **Cleanup.** After every F1 has passed, delete `handoff/workspace_bundle/` in one commit. It is a snapshot of 2026-11-01, and it is stale by then.

Device checks are the next phase, after the user chooses the emulator.
