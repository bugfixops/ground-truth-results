# KIRO CONVERSION RULES: AmazeFileManager, AnkiDroid, MMEX, LibreTorrent

These rules are strict. Read all of them before you start. If a step and a rule conflict, the rule wins. If something is unclear, STOP and report. Do not guess, and do not invent a waiver.

## 0. Scope and order
- Kiro works on AmazeFileManager only. AnkiDroid, MMEX and LibreTorrent are not Kiro's: the overnight convert run does them (handoff/RESUME_PROMPT_CONVERT.md). Work one app at a time, and do not start another app (section 9).
- Build prefix for each app (the name used in the output files): AmazeFileManager = amazefilemanager; AnkiDroid = ankidroid; MMEX = mmex; LibreTorrent = libretorrent.
- Never touch: graphs/Aegis (another agent is working there), graphs/AnyMemo, graphs/Markor, graphs/AnkiDroid, graphs/MMEX, graphs/LibreTorrent (the overnight convert run), the six finished apps (Currency, Diary, hash-checker, Omni-Notes, openlauncher, Vanilla-Music), tools/, final_java_only/, the zip files, the memory folder, any git repository. Do not push, commit, or install anything.
- Do not download anything. No adb, emulator, gradle, sudo, or network access.
- Do not delete any file. Do not delete scratch/ folders.

## 1. Lock rule
Every bash command you run starts with this text:
touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;
Run every tool from /Users/darshan/Desktop/yang/work with python3 -I.

## 2. Start of each app (in this order, all steps)
1. Read, in full: handoff/SCHEMA_V2.md, handoff/CONVERSION_RECIPE.md, handoff/AGENT_BRIEF_V2.md (sections 2, 4, 5), handoff/examples/README.md.
2. Read the first 300 lines of graphs/AnyMemo/graph_def.py for style only. Do not copy its app-specific content.
3. Read final_java_only/<App>/app/DATASET.txt. Its package line names the app's main package, and its apk line names the APK. These datasets do not name a module or a flavor. The app source root is the src/main/java folder that holds the main package. These roots were checked against the files:
   - AmazeFileManager: final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java (package com.amaze.filemanager)
   - AnkiDroid: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java (package com.ichi2.anki; the api folder next to it is a separate library)
   - MMEX: final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java (package com.money.manager)
   - LibreTorrent: final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java (package org.proninyaroslav.libretorrent)
   Flavor: use src/main only. Flavor folders (for example src/fdroid and src/play in AmazeFileManager) are used only if DATASET.txt names them. Write in AGENT_NOTES.md that the flavor is not stated in DATASET.txt.
4. Move the old draft out of the way: mv graphs/<App>/graph_def.py graphs/<App>/generated_draft_graph_def.py.txt. This file is never built. Then create the scratch folder: mkdir -p graphs/<App>/scratch (it does not exist yet for these apps).
5. The old draft and archive/graphs_v1_2026-10-25/<App>/ are an INVENTORY only: method names and call lists. Never take a label or a route from them without reading the source.
6. Write graphs/<App>/AGENT_NOTES.md at once: the step you are on and the last command. Update it after every step.

## 3. Labels (hard rules)
- Every method in graphs/<App>/method_list.json gets exactly one of:
  - REACHABLE: a route from an entry point exists in the standard configuration; or
  - UNREACHABLE: with one kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), a reason, and a source reference.
- confirmed_by is SOURCE or INFERRED. Never write DYN, FW-MEMORY, or UNVERIFIED.
- Tool coverage (coverage_baseline.json, sanity_check.csv, monkey, ape) is never evidence. Do not open these files to decide a label.
- An UNREACHABLE entry overrides any route in the build. Never mark a method UNREACHABLE if it has a route.
- method_list.json also contains library classes that are packaged in the APK (for example com.bumptech.glide, org.nanohttpd, com.ernieyu.feedparser). Label them too. Their source is INFERRED unless the source is in the app's source folder.
- Library and generated classes (for example com.bumptech.glide, the GlideApp and GlideRequest classes, Dagger and Hilt components, Room *_Impl classes, protobuf classes): their label is INFERRED. An UNREACHABLE label for such a method needs two things, both written in graphs/<App>/scratch/conflicts.md: (1) the output of grep -rn "<ClassName>" over the app's source folder, showing every call site (file:line); (2) the reason. If the app calls the class, the method is reachable through that call and must get a route. "Generated code is not called" without the grep output is not a reason.
- Tool conflicts: a tool run that touched a method is never a reason to add or remove a label, and it is never evidence. If the build reports a method that is UNREACHABLE but ran in a tool run, or any other conflict, write it in graphs/<App>/scratch/conflicts.md with: the method; the source lines printed around its callers and its trigger; the decision (REACHABLE with its route, or UNREACHABLE with a reason that the printed source shows, and why the tool run does not change it); and the printed lines behind that reason. If the source does not settle it, the label stays unresolved and the app is NOT DONE. Do not change a label because of a tool run, in either direction, without this log entry.

## 4. Route checks (hard rules)
- Sample: python3 -I tools/verify_sample.py <App> 30 20261025 > graphs/<App>/scratch/sample_30.txt. If the sampler returns fewer than 30 methods, record the number and the reason in the log.
- Print every step: copy handoff/examples/route_print_template.py to graphs/<App>/scratch/route_print.py. In the copy, set these constants at the top to the app: GDIR (graphs/<App>), SAMPLE (graphs/<App>/scratch/sample_30.txt), METHODS_CSV (graphs/<App>/out/methods.csv), GRAPH_JSON (graphs/<App>/out/<prefix>_trigger_graph.json), OUT_DIR (graphs/<App>/scratch/route_print), APP_BASE (the app's main package folder), APP_MODULE (the app's src/main folder), and FW_BASE stays as it is. Then run grep -n "AnyMemo" graphs/<App>/scratch/route_print.py: it must print nothing. Do not change the template or any AnyMemo file. The printer must show, for each step: the edge id, source -> target, class, guard, needs_state, env, and the full evidence text, plus every cited source line range (including ranges after a comma, such as "ui/X.java:594, 480").
- Judge every step against its printed lines, including the if, catch, and for conditions around each call. A route with any step not printed counts as NOT checked. It cannot be marked correct.
- Verdict per route: correct (every step supported, guards and gates included), fixed (you corrected graph_def.py, rebuilt, and the route is right now), wrong (wrong and not fixed), unclear (depends on another app, the keyboard, a WebView engine, or code you cannot read).
- Error rate = (fixed + wrong) / (correct + fixed + wrong).
- Check every route against the mistakes list in handoff/AGENT_BRIEF_V2.md section 5, especially: the first-resume shortcut, a best route that ignores guards, an early return that hides a guard, a static flag, a file URI versus a content URI, a guard-less bytecode edge, a line number one line off, and an ENV text that does not match the code.
- Fix each wrong route in graph_def.py. Rebuild. Print the route again. Log the fix in graphs/<App>/scratch/fix_log.md: method, step, lines printed, what changed.
- After the last fix, draw the sample again. The final table covers only the final draw. Re-read every route whose steps changed.

## 5. Framework and library claims
- Cite the framework only from lines you printed from fw_src/android-8.1.0_r1/ (write FW-SRC path:lines). If the framework file is not in fw_src/, the claim is INFERRED, and the text says "source not read".
- Libraries whose source is not in the dataset (androidx, material, Glide, Dagger/Hilt generated code, Room, ORMLite, Rx, EventBus, and others) are INFERRED.
- Do not write a framework claim from memory.

## 6. Build and checks (all must pass before DONE)
Run each command, and save the output to graphs/<App>/scratch/. Do not write "passed" without the output.
1. python3 -I tools/build_graph.py graphs/<App> <prefix>: errors 0, warnings 0, no STALE line. The file contains the line STRICT = True.
2. python3 -I tools/check_citations.py <App>: 0 problems; "FW-MEMORY / DYN / UNVERIFIED: 0".
3. python3 -I tools/check_routes.py <App>: 0 flagged. A flagged route is allowed only when readme_notes.md explains it with printed source lines.
4. python3 -I tools/check_bytecode_lines.py <App>: 0 bad.
5. grep -c "DEAD\|FRAMEWORK_ONLY" graphs/<App>/graph_def.py: 0.
6. grep -c "FW-MEMORY" graphs/<App>/graph_def.py: 0.
7. grep -c "PENDING" graphs/<App>/graph_def.py: 0. Do not use the word PENDING in any text or identifier.
8. python3 -I tools/scan_unreachable.py <App> --all and --callers: every UNREACHABLE method has a kind, a reason, and a source reference. Every bytecode caller that is outside the reachable set is explained in its reason.

## 7. Logs and notes (all must exist)
- graphs/<App>/verification.csv: header exactly "type,item,result,confirmed_by,ref,edges,note". Rows: path (one per sampled method), label (one per UNREACHABLE method, and one per sampled reachable method), edge (one per corrected edge and per framework claim checked). Write it with graphs/<App>/make_verification.py. That script must assert every note against the graph and stop if one does not match. Do not write the file by hand.
- graphs/<App>/readme_notes.md with exactly these five headings, in this order:
  ## What the re-audit changed (compared with the schema 1 graph)
  ## How the checked paths were chosen
  ## What waits for a device (API 27)
  ## Hazard candidates (from reading the code, not reproduced)
  ## Limits
  Then run python3 -I tools/gen_readme_v2.py <App>.
- graphs/<App>/LESSONS.md: 3 to 8 short bullets on what found real errors in this app.

## 8. What you must not write
- Do not write a decision in the name of the orchestrator, the parent session, the user, or "Option A". If a decision is needed, write it under "## Open decisions for the user" in the app's AGENT_NOTES.md, and stop.
- Do not write a waiver for any rule. If a check cannot pass, the app is NOT DONE, and you say why.
- Do not claim a count you did not print.

## 9. Finishing an app
- When every check in section 6 and every log in section 7 is complete, and no helper is running (section 11): change the app's line in handoff/PROGRESS_V2.md from "- [K] <App> (Kiro queue, not started)" to "- [K] <App> (Kiro DONE <date>, awaiting user tick)". Do not write "[x]". The user ticks.
- Add one paragraph for the app to handoff/KIRO_APPS_STATUS.md (create it if it does not exist): methods, REACHABLE, UNREACHABLE by kind, labels SOURCE and INFERRED, route table counts (correct, fixed, wrong, unclear, error rate), flagged routes, open items.
- Then start the next app in section 0.
- If an app is blocked: write the blocker under "## Blocked" in its AGENT_NOTES.md. Leave its PROGRESS line as it is (not DONE). Stop the session. Do not start the next app.

## 10. STOP AND REPORT
Stop immediately, change nothing more, and report, if:
- DATASET.txt is missing, or its package line does not match a package folder under the app source root in section 2, step 3;
- the build cannot reach 0 errors and 0 warnings in 3 tries;
- a cited source file does not exist;
- a check fails and you cannot fix it in 3 tries;
- you are tempted to break any rule in this file.

## 11. Parallel helpers (use them: this is how the work finishes sooner)
- Work on one app at a time (section 0). Inside that app, run up to 4 helper agents at the same time. Never more than 4. Create the folders graphs/<App>/parts/ and graphs/<App>/scratch/route_check/ with mkdir -p if they do not exist.
- Split the work so that no class is split between two helpers. Each helper gets its own set of classes or route files.
- Two helper tasks only:
  (a) LABEL: a list of classes and their methods from graphs/<App>/method_list.json. The helper reads the source for each method, applies sections 3 and 5, and writes two files: graphs/<App>/parts/label_<n>.py (only e(...) edges and UNREACHABLE[...] entries, in the same style as graph_def.py, with no new constants) and graphs/<App>/parts/label_<n>.md (one row per method: method | label | kind | reason | printed file:lines).
  (b) ROUTE: a list of up to 10 route files in graphs/<App>/scratch/route_print/. The helper judges every step against its printed lines (section 4) and writes graphs/<App>/scratch/route_check/route_<n>.md: one row per route with the steps read, the verdict, and for every wrong step the exact replacement text it proposes, with the printed lines behind it.
- Helpers never edit: graph_def.py, out/, verification.csv, make_verification.py, readme_notes.md, handoff/PROGRESS_V2.md, graphs/<App>/AGENT_NOTES.md, tools/, or another helper's file. Helpers never run tools/build_graph.py and never apply a fix.
- Every claim a helper writes must carry the printed source lines. A claim without printed lines is rejected.
- The main agent (the session that works on the app) does the following, in this order:
  1. Gives each helper its list, and gives it sections 3, 4, 5 and 11 of this file.
  2. Waits for every helper to finish, or applies the stuck rule in section 12.
  3. Checks each helper report: spot-checks at least one claim in five with sed -n against the source. Rejects any unsupported claim and gives that item to a new helper.
  4. Appends each accepted label part to graph_def.py as a block headed "# ---- part <n> (<date>)". Then runs python3 -m py_compile graphs/<App>/graph_def.py (it must pass) and the build.
  5. Applies the route fixes itself, one at a time, with a build after each (section 4).
  6. Where two helpers disagree about a method, reads the source, decides, and writes the decision in conflicts.md.
- Finish condition: the build shows UNRESOLVED 0, every part is accepted, every route fix is applied, and the sample has been drawn again and read (section 4).

## 12. Stuck and resume rules (nothing may stay stuck)
- At the start of a session, read graphs/<App>/AGENT_NOTES.md ("Current step") and continue from it. Do not restart finished work. Number new build outputs after the highest number already in scratch/ (for example build_007).
- Write graphs/<App>/AGENT_NOTES.md after every step: the step, the last command, and the next command.
- Each helper writes "STATUS: RUNNING <time>" as its first line and "STATUS: DONE" or "STATUS: INCOMPLETE <reason>" as its last line.
- A helper that writes nothing for 30 minutes is stuck. Stop waiting for it, mark its items "INCOMPLETE" in AGENT_NOTES.md, and give them to one new helper. If that helper also gets stuck, write the items under "## Blocked" in AGENT_NOTES.md and continue with the other items. The app is then NOT DONE.
- Never wait without a time limit. The 30-minute rule above applies to every wait.
- If a message says session limit, usage limit, or rate limit: start no new helpers, write the current step in AGENT_NOTES.md, and stop. The user restarts the session.
- If a required file is missing, STOP and report (section 10).

## 13. Final message (at most 12 lines, nothing else)
1. App, status (DONE or NOT DONE), and the open step.
2. Build counts: methods, REACHABLE, UNREACHABLE, errors, warnings.
3. Route table: 30 rows (or the sampler's number), correct, fixed, wrong, unclear, error rate.
4. Checks: the result of each command in section 6.
5. Files changed.
6. Blockers, if any.
7. Helpers: how many started, how many reports were accepted, how many rejected, and how many got stuck.

## 14. Corrections in force
handoff/KIRO_CORRECTIONS.md (from 2026-10-27 21:10) is in force. Read it before your next step. Where it sets a stricter limit, it wins: for example, a helper batch is at most 40 methods, and a part is merged only after the checks in its C1.
