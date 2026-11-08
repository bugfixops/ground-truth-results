# Brief: convert LibreTorrent to the schema 2 ground truth

You convert ONE app: LibreTorrent (Java, Android). Work only on this app. The other apps (Aegis, AmazeFileManager, AnkiDroid, AnyMemo, MMEX, Markor, Currency, Diary, hash-checker, Omni-Notes, openlauncher, Vanilla-Music) belong to other agents: do not read them as work and do not write to them.

Read this whole brief before your first step. Follow it exactly. If a step and a rule conflict, the rule wins. If something is unclear, stop and report it. Do not guess.

## 0. What you produce

A trigger graph of the app. For every method in its method list, one label. For every link between methods, an edge with its class and its conditions. Plus a log of checked paths.

Files, all in graphs/LibreTorrent/ (create the folder if it is missing):
- graph_def.py: written by you, by hand, from the source
- verification.csv: path, label and edge rows
- make_verification.py: writes verification.csv and asserts each note against graph_def.py
- readme_notes.md: five headings (step 8)
- LESSONS.md: 3 to 8 short bullets on what found real errors
- AGENT_NOTES.md: your running notes (current step, last action, next action), updated after every step

## 1. Inputs (the user uploads these; paths are relative to the LibreTorrent folder)

1. Source code: app/LibreTorrent-#3.5.2/app/src/main/java (code package org.proninyaroslav.libretorrent).
2. Manifest: app/LibreTorrent-#3.5.2/app/src/main/AndroidManifest.xml.
3. Dataset note: app/DATASET.txt. It says the instrumented APK's package is org.proninyaroslav.libretorrent.debug, min SDK 24, target SDK 34, source commit d93e92e. Note the code package is org.proninyaroslav.libretorrent.
4. Method list: graphs/LibreTorrent/method_list.json (4,732 methods). Every one of them gets a label.
5. The old generated draft: graphs/LibreTorrent/graph_def.py (from 2026-10-25). Inventory only. Never take a label or a route from it without reading the source.
6. Tools (folder tools/), only if you can run Python 3: build_graph.py, verify_sample.py, show_route.py, check_citations.py, check_routes.py, check_bytecode_lines.py, scan_unreachable.py, gen_readme_v2.py, tests/check_v2.py.
7. Android framework source for 8.1.0_r1 (fw_src/android-8.1.0_r1/), if the user provides it.

Do not download anything. Do not use the network except to fetch AOSP 8.1.0_r1 files from raw.githubusercontent.com/aosp-mirror/platform_frameworks_base (tag android-8.1.0_r1), and only if your environment allows it.

If an input is missing, stop and report which one (section 8). Do not invent its content.

## 2. Hard rules (Yang's requirements). Any failed rule means the app is NOT DONE.

R1. Labels come from the source code. Tool coverage (Monkey, APE, coverage files, sanity_check) is never evidence and never changes a label. Do not open those files to decide a label.

R2. Every method gets exactly one label:
- REACHABLE: a route from an entry point exists in the standard configuration.
- UNREACHABLE: one kind, a reason, and a source reference. The kinds are only: no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration (debug build, manifest, permission), closed_by_api_level (code for another Android version than 27).
An UNREACHABLE label is never given to a method that has a route.

R3. confirmed_by is SOURCE (you printed the lines and read them) or INFERRED (not read, or it depends on code outside the source). Never write FW-MEMORY, DYN or UNVERIFIED.

R4. Standard configuration: the instrumented debug build from the dataset, a fresh install on an Android API 27 emulator, runtime permissions granted only where a route needs them, and the dataset's fixtures.

R5. Edge classes:
- explicit: app code calls app code directly.
- standard: the framework calls a callback the app registered in app code (lifecycle, listeners, menu callbacks, AsyncTask, activity results, the launcher entry).
- non_standard, with a `via`: a library or reflection makes the link and no app code calls or registers the target (EventBus, ButterKnife, data binding, dependency injection, Rx, reflection, XML android:onClick, intents resolved by action name, widget providers and broadcast receivers reached by name).

R6. Gates are structured, not prose:
- ENV kinds (things outside the app): network, tls_chain, permission, hardware, other_app, system_event, time, other.
- STATE kinds (things set up by earlier in-app actions): data, settings, account, file, session.
Each gate's text is copied exactly from the code. An ordinary program condition is not a gate.

R7. A framework claim cites lines you printed from AOSP 8.1.0_r1, as FW-SRC core/java/...:lines. A library claim (androidx, Material, Room, Dagger/Hilt generated code, Rx, EventBus, and anything else not in the source) is INFERRED.

R8. Route check: 30 sampled paths, each read step by step against the printed source lines, including every if, catch and for around each call. Error rate = (fixed + wrong) / (correct + fixed + wrong).

R9. Do not write a waiver for any rule. Do not write "passed" for a check you did not run. Write the output.

## 3. Steps (in order; update AGENT_NOTES.md after each one)

S1. Read DATASET.txt and AndroidManifest.xml. From the manifest, list the entry points: launcher activity, exported components, receivers, providers, services, and widget providers.

S2. Rename the old draft: graph_def.py becomes generated_draft_graph_def.py.txt. Never delete it.

S3. Write graph_def.py by hand from the source, in sections:
- entry points
- lifecycle
- pages (screens) and the GUI handlers that move between them
- framework callbacks (listeners, adapters, menus, AsyncTask, Handler messages, activity results)
- library and reflection links (non_standard)
- gates (ENV and STATE, with their kinds)
Each edge has: source, target, class, text, guard, needs_state, env and evidence. Use the same field names as the old draft. Cite the source line for every claim.

S4. Label all 4,732 methods in graphs/LibreTorrent/method_list.json: UNREACHABLE entries with kind, reason and source reference; the rest REACHABLE by a route. Work class by class, in batches of at most 40 methods. After each batch, record the batch and the count in AGENT_NOTES.md.

S5. Build. From the folder that holds tools/: python3 -I tools/build_graph.py graphs/LibreTorrent libretorrent. Goal: errors 0, warnings 0, and the file contains the line STRICT = True. Save the output.

S6. Route check. Run python3 -I tools/verify_sample.py LibreTorrent 30 to draw the sample. If you cannot run the tool, choose 30 methods by a rule you state, and record that rule in readme_notes.md. For each sampled route, print every step (python3 -I tools/show_route.py LibreTorrent <method> --dedupe, or your own printout with the same fields) and read each step against the source. Fix every wrong step in graph_def.py, rebuild, reprint the route, and log the fix. After the last fix, redraw the sample if the tool allows, and read the final routes.

S7. Logs. Write verification.csv with the header exactly: type,item,result,confirmed_by,ref,edges,note
Rows: path (one for each sampled method), label (one for each UNREACHABLE method and each sampled REACHABLE method), edge (each corrected edge and each framework claim you checked). Result values: correct, fixed, wrong, unclear. Write the file with make_verification.py, which must assert each note against graph_def.py and stop if one does not match. Do not write the CSV by hand.

S8. readme_notes.md with exactly these five headings, in this order:
## What the re-audit changed (compared with the schema 1 graph)
## How the checked paths were chosen
## What waits for a device (API 27)
## Hazard candidates (from reading the code, not reproduced)
## Limits
Then python3 -I tools/gen_readme_v2.py LibreTorrent.

S9. Final checks. Run each one, save its output, and report the result:
- python3 -I tools/check_citations.py LibreTorrent: 0 problems; FW-MEMORY, DYN and UNVERIFIED count 0
- python3 -I tools/check_routes.py LibreTorrent: 0 flagged (a flagged route is allowed only if readme_notes.md explains it with printed source lines)
- python3 -I tools/check_bytecode_lines.py LibreTorrent: 0 bad
- grep -c "DEAD\|FRAMEWORK_ONLY" graphs/LibreTorrent/graph_def.py: 0
- python3 -I tools/tests/check_v2.py: no app with problems

S10. LESSONS.md: 3 to 8 short bullets on what found real errors in this app.

## 4. Errors found in other apps. Check for them from the start.

- First-resume shortcut: an edge from onResume, or from a lambda, straight to a page skips what the first start does. Start every route at the cold start. An edge that is valid only after an earlier visit carries a STATE gate.
- The cheapest route ignores guards. Check every step of every sampled route, even when a route looks odd.
- if (!debug && x()) never calls x() in the debug build. Remove that edge, and label what only x leads to as closed_by_configuration. Grep the source for BuildConfig.DEBUG and for debug checks.
- An early return hides the guard of every later statement. A static flag read once per process is also a guard.
- Data origin: a file:// URI and a content:// URI come from different places. Data carried by the starting intent must be a context from the entry edge to the point where it is read.
- Bytecode line numbers can be one line off (a call inside a chained or multi-line expression). check_bytecode_lines.py finds these.
- Copy every ENV text from the code exactly. One earlier app named the wrong locales.
- A method split by how it is reached (for example a variant per intent action) needs one hand edge per variant.

## 5. Things to check in LibreTorrent (do not assume them)

- The code package is org.proninyaroslav.libretorrent. The debug APK's package is org.proninyaroslav.libretorrent.debug.
- DATASET.txt lists 3 source directories. Find out whether any module besides app/ is part of the APK. Anything outside the APK is a library: INFERRED.
- The old draft has 4,732 methods and 12,622 edges, generated by a tool. Treat all of it as unverified.
- Any native or JNI code, and any third-party library, is INFERRED unless its source is in the upload.

## 6. Stop rules

- Stop and report if the source tree, the manifest or the method list is missing, or DATASET.txt does not name the package above.
- Stop and report if the build cannot reach errors 0 and warnings 0 after 3 tries.
- If your session is about to end, write AGENT_NOTES.md with the current step and the next action, then stop. The user can continue from that file.
- Do not edit handoff/PROGRESS_V2.md. The user ticks apps.

## 7. Never

- Work on another app.
- Push, commit, install packages, or send any file anywhere.
- Put personal data (names, email addresses) into any file.
- Claim a count you did not print.

## 8. Final message (at most 12 lines, plain words)

1. App LibreTorrent; status DONE or NOT DONE; the open step if NOT DONE.
2. Methods; REACHABLE; UNREACHABLE by kind; labels SOURCE and INFERRED.
3. Route table: sample size; correct; fixed; wrong; unclear; error rate.
4. Checks: the result of each command in S9, or NOT RUN with the reason.
5. Files changed.
6. Blockers, and any missing input from section 1.
7. The three most important lessons.
