# Overnight run: finish all 13 apps (labels, route checks, logs)

**Superseded on 2026-11-01 by `handoff/MUSE_FINISH_ALL.md`.** Follow that file; this one is kept for history.


Written 2026-11-01 for Muse, on the user's instruction: "use Muse to work overnight to finish everything ... emulator we can choose later, first we need to build this whole. Now nobody is required, all should be handled by Muse."

Read this file in full now, and again after every reset. It overrides `handoff/MUSE_COMPLETE_BRIEF.md` sections 6, 7 and 8, and `handoff/MUSE_HANDOVER.md` where they differ. For everything else, those two files and the rule files still apply.

## 0. The job tonight

1. **Finish every app to 100%, except device checks.** That means labels, route checks, all eight checks and all logs, for all 13 apps.
2. **Device checks are deferred.** The user picks the emulator later. Tonight: no emulator, no adb, no device scripts, no new repositories, no GitHub Actions runs, no APKs anywhere.
3. **Nobody will answer tonight. Never stop to ask.** When a choice comes up, decide it by section 5, record it, and carry on.
4. **Stop only when:**
   - every stream in section 3 is done, or
   - a usage or session limit stops you. Save your state first (section 7), and resume from it on the next start.

## 1. Read first (from branch work-2026-10-31)

1. `handoff/MUSE_COMPLETE_BRIEF.md`: setup, the 2026-11-01 baseline, the LibreTorrent answers (4.2) and steps (4.3), the per-app work (5).
2. `handoff/MUSE_HANDOVER.md` section 2: label rules, edge and gate rules, route checks, the eight checks, logs.
3. `handoff/KIRO_CONVERT_APPS.md` sections 3 to 7, `handoff/KIRO_CORRECTIONS.md` C1 to C8, and `handoff/SCHEMA_V2.md`.
4. `handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md` rules A to K, for LibreTorrent, with the USE_AUTO exception in the brief, section 4.1.
5. `handoff/AGENT_BRIEF_V2.md` section 5: the list of route mistakes to check every route against.
6. The raw baseline outputs: `handoff/baseline_2026-11-01/<App>/`.

If a read is cut off, read the rest before you go on.

## 2. Setup (once)

1. **Get a full working copy of `work-2026-10-31`.** Use whichever of these works first:
   - (a) `git clone --branch work-2026-10-31 https://github.com/bugfixops/ground-truth-results.git gtr`, with the token from your vault through a credential helper. Never put the token in the URL, a file, a commit or a log.
   - (b) Any clone or archive download your GitHub connector offers.
   - (c) If neither works, fetch the files through the connector into a local tree with the same paths. Fetch them in this order:
     - `tools/`
     - `handoff/`
     - `graphs/<App>/` without `out/` and `*.html`. Include `graphs/Markor/scratch/{hier,textcount,dotcount,route_guards}.json`, which Markor's `graph_def.py` reads.
     - `final_java_only/<App>/`
     - only the `fw_src/` files you cite

     Do the apps in stream order, and pause between requests if you hit rate limits.

   Record which method you used in `handoff/MUSE_RUN_LOG.md`.
2. Install a JDK 17 or newer (for `javap`), and confirm Python 3.10 or newer.
3. Clone `https://github.com/bugfixops/work-emulator.git` (public, depth 1). You need only `classes/<App>/<i>/` (bytecode for `javap`) and `ci/apps.csv`. Do not use its APKs tonight.
4. **Confirm the baseline before you edit anything.** From the repo root, run `python3 -I tools/build_graph.py graphs/Currency currency`, and check that it prints errors 0 and warnings 0, as in the brief, section 2. If it does not, fix your setup first.

## 3. Streams (run them in parallel)

Each stream owns its apps. Create `graphs/<App>/WORKING_LOCK` while you work on an app, and delete it when the app's stream step ends. A stream never edits another stream's app.

Helpers:
- At most 4 per app, and at most 12 at once in total.
- At most 40 methods (labels) or 10 routes (route checks) per helper.
- Helpers never edit `graph_def.py`, `out/`, `verification.csv`, `PROGRESS_V2.md`, `AGENT_NOTES.md`, `tools/` or another helper's files, and they never run the build. Only the stream's main agent merges and builds.

### Stream D: logs for the eight ticked apps (start first; it is small)

Apps: Currency, Diary, hash-checker, Omni-Notes, openlauncher, Vanilla-Music, Markor, AnyMemo. Do not change any label, edge or route, and do not edit their `graph_def.py`.

1. **Currency, Diary, hash-checker, Omni-Notes: add `graphs/<App>/make_verification.py`.**
   - It must regenerate the current `verification.csv` byte for byte: write to a temporary file, then `cmp` it against the current file. Save the `cmp` output in `scratch/`.
   - Start from `handoff/examples/make_vlog_hash_checker.py` and `make_vlog_omni_notes.py` for those two apps. Use `graphs/AnyMemo/make_verification.py` as the model for Currency and Diary, and encode their existing rows.
2. **The same four apps: write `LESSONS.md`.** 3 to 8 bullets on what found real errors, taken from their `readme_notes.md` and `AGENT_NOTES.md`.
3. **Note the grep hits in `readme_notes.md` under `## Limits`, with line numbers.** These hits are not placeholders:
   - Diary: 5 DEAD/FRAMEWORK_ONLY hits
   - hash-checker: 7 DEAD/FRAMEWORK_ONLY hits, plus 4 PENDING hits, which are the page id `S_MAIN_EXIT_PENDING`
   - Omni-Notes: 11 DEAD/FRAMEWORK_ONLY hits
   - openlauncher: 1 PENDING hit (AsyncTask code text)

   Then run `python3 -I tools/gen_readme_v2.py <App>`.
4. **For all eight apps, run the build and all eight checks.** Save them to `graphs/<App>/scratch/final_checks_2026-11-01/`. The expected result is the brief's baseline. Any difference is a work item: record it, find the cause, and report it.
5. **Keep their `[x]` lines in `PROGRESS_V2.md` exactly as they are.**

### Stream B: AmazeFileManager, AnkiDroid, MMEX (one sub-stream per app; they may run in parallel)

For each app:

1. **Baseline.** Run the build and the eight checks, saved to `scratch/final_checks_2026-11-01/`.
2. **Set `STRICT = True`** (AnkiDroid line 10, MMEX line 8; AmazeFileManager already has it). Rebuild and confirm errors 0 and warnings 0. With STRICT on, the baseline gives 0/0 for both.
3. **Fix check 2, the citation problems** (AmazeFileManager 23, AnkiDroid 3, MMEX 43). Take each line from `2_citations.txt`, print the source, and correct the citation. If the file is not in the upload, write the claim as INFERRED with "source not read".
4. **Fix check 4, the bytecode lines** (AmazeFileManager 63, AnkiDroid 48, MMEX 244). For each edge whose cited line does not show the callee, print the method's source and correct the line. If no source line shows the call (synthetic, bridge, or compiler-generated), use the method's declaration line and say so in the evidence. Do not edit `tools/`.
5. **Clear check 8.** Each UNREACHABLE method that has a bytecode caller outside the UNREACHABLE set (AmazeFileManager 4, AnkiDroid 169, MMEX 19) needs one of two fixes:
   - its reason explains, from printed source, why that caller never calls it in the standard configuration, or
   - it gets a route, if the caller can call it.
6. **MMEX:** reword the two reason texts that use the word DEAD (lines 13360 and 13485).
7. **The known issues** from MUSE_HANDOVER WP2:
   - AmazeFileManager: the Glide contradictions, and E89e2cedd and Ee1aeff93.
   - AnkiDroid: `Card.toString`, `EasySSLSocketFactory.equals` and `hashCode`, API 27 versus target 23, `Hooks.runFilter`.
   - MMEX: the INFERRED UNREACHABLE entries.

   Your earlier proposals in `graphs/<App>/scratch/proposals/` are inputs only.
8. **Route checks** (MUSE_HANDOVER section 2):
   - Run `python3 -I tools/verify_sample.py <App> 30 20261025 > graphs/<App>/scratch/sample_30.txt`.
   - Copy `handoff/examples/route_print_template.py` to `scratch/route_print.py` and set its constants.
   - Print every step, and judge each one against the printed lines, including the if, catch and for conditions around it.
   - Check every route against AGENT_BRIEF_V2 section 5.
   - Fix wrong routes one at a time: rebuild, reprint, and log each fix in `scratch/fix_log.md`.
   - After the last fix, draw the sample again. The final table covers only the final draw.
   - Each route's verdict is correct, fixed, wrong or unclear. A route you cannot fix without editing `tools/` is `wrong`, with the reason. That is allowed; report it.
9. **Logs:**
   - `make_verification.py`, modelled on AnyMemo, writes `verification.csv`. Never write that file by hand.
   - `readme_notes.md` with the five headings, then `gen_readme_v2.py`.
   - `LESSONS.md`.
   - `AGENT_NOTES.md`.
10. **The gate:** UNRESOLVED 0, errors 0, warnings 0, `STRICT = True`, and all eight checks clean, with the output saved. Then set the app's line in `PROGRESS_V2.md` to `- [K] <App> (labels, route checks and logs DONE <date>; device checks not started; awaiting user tick)`.

### Stream C: Aegis

1. **Fix check 2.** Edges E24649299 and E2a97bab7 cite `services/LaunchScannerTileService.java`, and `check_citations.py` reports "file not held". The file does exist, at `final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis/services/LaunchScannerTileService.java`. Find out how the citations that pass are written (open `check_citations.py` read-only, and look at passing Aegis citations). Write these two the same way, print the cited lines, and rerun check 2 until it shows 0.
2. **Make the 7 open decisions yourself** (section 5.2). Record each one, and apply it.
3. **Finish the route check** from the last RESUME POINT in `graphs/Aegis/AGENT_NOTES.md`, steps 6 to 10.
   - Most remaining ERROR steps are "structural": the router in `build_graph.py` does not track state. Fix them with variant nodes that only the producer chain reaches. This is the `MainActivity.doShortcutActions@SCAN` technique the notes describe at around line 609.
   - Never edit `tools/`. A step you still cannot fix makes its route `wrong`, with the reason.
4. **Logs:** `make_verification.py`, `verification.csv`, `readme_notes.md`, `gen_readme_v2.py`, `LESSONS.md`, the eight checks.
5. **The gate** is the same as Stream B step 10. Change the line `- [ ] Aegis` to the `[K]` line.

### Stream A: LibreTorrent (the largest; start it at the same time as the others)

Follow brief section 4.3, using the answers in 4.2. In short:

1. Close all 564 OPEN rows by 4.2. Re-run the full-folder grep for every row that was flipped on the 252-file grep.
2. Turn the 120 merge-ready files into parts, `parts/b<NNN>.py` and `.md`, in the format of `parts/b013.py`.
3. **Merge order:**
   - Merge the shared trunks from the launcher entry first: feed refresh through `SettingsFragment.java` lines 122 and 195 to 198 and `PreferenceActivity.java` lines 113 to 114; the torrent service and engine; add-torrent; the streaming server; the notification actions.
   - Then merge the batch parts in plan order, one at a time. After each part: `python3 -m py_compile graphs/LibreTorrent/graph_def.py`, then the build saved as `scratch/build_<n>.txt`, then check that errors did not rise and record the counts in AGENT_NOTES (C1).
4. As soon as the trunks are in:
   - set `STRICT = True`
   - delete `AUTO_DEAD` (line 47) and the `FW-MEMORY` rewrite (lines 52 to 53)
   - fix every claim that the rewrite was hiding
5. Fix the edge whose cited line is past the end of its file, so that check 4 runs. Then bring check 4 to 0 and check 2 to 0 (102 problems now).
6. **The gate for [L]:** UNRESOLVED 0, errors 0, warnings 0, unclassified 0, and `STRICT = True`. Set `- [L] LibreTorrent (labelled <date>; route checks not started)`.
7. **Then** route checks, logs and the eight checks, as in Stream B steps 8 to 10, and the `[K]` line.

## 4. Push and checkpoint

1. **Push to `work-2026-10-31` only.** Never push to `main` or `result`, and never force-push.
   - Commit as `bugfixops <bugfixops@users.noreply.github.com>`. The user's own identity is also accepted.
   - Never commit APKs, zips, tokens, secrets, personal data or absolute paths from your VM.
2. **When to push:** after every app gate; after every 5 merged LibreTorrent parts; and at least every 60 minutes while work is going on. Never push a build that is broken (errors above 0, or a `py_compile` failure) on `graph_def.py`. Push only after the build after your last edit.
3. **Commit message:** `<App>: <what> (build <file>: methods N, REACHABLE R, UNREACHABLE U, unclassified C, errors E, warnings W)`. The counts come from the build you just ran.
4. Unverified proposals stay under `scratch/` and are marked UNVERIFIED. Merged work in `graph_def.py` has passed the build and C1.

## 5. Decisions: Muse decides, records, and goes on

### 5.1 The rule for every choice

1. Look for a written rule (the rule files in section 1) and apply it.
2. If none, look for a precedent in the eight ticked apps: grep their `graph_def.py`, `out/methods.csv` and `readme_notes.md`. Apply it.
3. If none, choose the option that models what the printed source does, without editing `tools/`.
   - Prefer adding a gate, a `needs_state` or a variant node over deleting a route.
   - Never change a label unless the printed source shows it.
   - Never mark a method UNREACHABLE if it has a route.
4. Record every decision in `handoff/MUSE_DECISIONS.md` (create it) and in the app's AGENT_NOTES, under `## Decisions made by Muse (for the user and Yang to review)`. Give each one:
   - an id
   - the app
   - the item, with its file and line
   - the options
   - the choice
   - the printed evidence (file:lines)
   - its effect on labels and routes
   - how to reverse it

   Write each one as Muse's decision under the user's instruction of 2026-11-01. Never write a decision in Yang's name.

### 5.2 The 7 Aegis items (line numbers in `graphs/Aegis/AGENT_NOTES.md`)

These are starting choices. Verify each one from printed source first, and choose differently if the source says otherwise.

1. **Line 379, R1 step 13** (the ENTERS edge compresses the Next tap and `setCurrentSlide`). Add the producer as its own edge, with `needs_state` on the Next edges (variant nodes if the router skips it). Model what the code does; do not compress it.
2. **Line 479, route 4 step 9** (needs an icon pack from an earlier action, `IconPackManager.java:136-158`). If an in-app action creates it, add the precondition as a STATE gate with its producer route. Do not reclassify edges as non-standard. `explicit_standard_route` stays whatever the build computes.
3. **Line 599, route 1 step 21.** The notes near line 609 say this was fixed later (the RESULT edge now starts from `IntroActivity.onDonePressed@SAVED`). Reprint the route. If it is fixed, record "resolved by R6E fix". If not, use a variant node after `initNew`.
4. **Line 603, step 14, SEARCH_IN_GROUPS** (it applies only after a relaunch, `MainActivity.java:234`). The method stays REACHABLE. Model the relaunch as a STATE `settings` gate with the relaunch step. The route verdict is `unclear` under rule D2 ("prior run"), as the notes say.
5. **Line 609, G3_5 step 34** (Authy is checked by default, `DatabaseImporter.java:37`). Model both paths: the default Authy path (OK without a row tap) as one variant, and the Google Authenticator path (row tap, then OK) as another. Both exist in the source.
6. **Line 636, GlideRequests step 50** (app import needs root, `ImportEntriesActivity.java:143-153`). Put an ENV gate (kind `other`, with the root-shell text copied from the code) on the app-import edge, so that the router prefers the file route. Then re-judge the route.
7. **Line 659, `GoogleAuthImporter.readFromApp`** (OK reads the ListView's checked row). Print the framework code that sets the checked item on a tap, `AbsListView.performItemClick` in `fw_src/android-8.1.0_r1/`, and the dialog's choice mode. Write the edge as those printed lines show, then re-judge step 24.

### 5.3 Other choices already made for you

- **The LibreTorrent conventions:** brief section 4.2.
- **LibreTorrent may keep `USE_AUTO = True`,** like the six ticked apps that use it: brief section 4.1.
- **AnyMemo's storage-permission question (D2)** does not arise tonight. There are no device runs, and AnyMemo's labels do not change.

## 6. Hard rules (any break stops that item; record it and move on)

- Every label and every edge comes from source you printed (`sed -n` with file and line range) and read. Tool coverage (Monkey, APE, JaCoCo from tool runs, `coverage_baseline.json`, `sanity_check.csv`), the old generated graphs and the build's REACHABLE count are never evidence.
- **`confirmed_by` is only SOURCE or INFERRED.** Never write DYN, FW-MEMORY or UNVERIFIED.
- **Framework claims cite FW-SRC lines from `fw_src/android-8.1.0_r1/`.** Otherwise the claim is INFERRED, with "source not read".
- **Read only:** `tools/`, `final_java_only/`, `fw_src/`, the zip files. Do not touch any other repository.
- **Never write `[x]`.** Change only the line of the app you finished.
- **Never report a count you did not print in the same session.** Never write "passed" without the saved output.
- **Spot-check helpers.** Check at least 1 claim in 5 of every helper part with `sed -n` before you merge it. Reject anything that has no printed lines.
- **Stuck rule.** A helper with no output for 30 minutes is stuck: give its items to one new helper. If that one stalls too, write the items under `## Blocked` in AGENT_NOTES and carry on.

## 7. State, resets and limits

- **Run log.** Append one line per step to `handoff/MUSE_RUN_LOG.md`: time, stream, app, step, command, build file, counts. Push it with each checkpoint.
- **Current step.** Each app's `AGENT_NOTES.md` has a `## Current step` section with the next action. Update it after every step.
- **On every start or reset:**
  - re-read this file
  - read the last 30 lines of `handoff/MUSE_RUN_LOG.md`
  - read each app's `## Current step`
  - pull the branch
  - continue from there

  Never redo finished work. Never start a second worker on an app that has a `WORKING_LOCK` younger than 30 minutes.
- **Usage, session or rate limit:** start no new helpers, save the current step everywhere, push, and stop. Continue from the saved state when you are restarted.

## 8. When everything is done

1. Write `handoff/MUSE_OVERNIGHT_SUMMARY.md`, with one section per app:
   - its status line
   - methods, REACHABLE, UNREACHABLE by kind, unclassified, errors, warnings, with the build file
   - SOURCE and INFERRED counts
   - each of the eight checks, with its result and saved file
   - the route table: correct, fixed, wrong, unclear, error rate
   - the log files present
   - the decisions made (ids from `MUSE_DECISIONS.md`)
   - anything blocked, and why
2. Push.
3. Final message, at most 15 lines:
   - which apps reached `[K]` (labels, route checks and logs done; device checks not started)
   - which did not, and the open step for each
   - the decision count
   - the summary file path

Device checks remain the next step, after the user chooses the emulator.
