# Brief: convert one app to the schema 2 ground truth (for a sub-agent or the resume job)

You convert ONE app. Its name is in your task (the folder under work/graphs/). Read this whole brief, then the files it names. Write only inside work/graphs/<App>/ (see Scope).

## 1. Read first, in this order
1. work/handoff/SCHEMA_V2.md: the file format, the vocabularies (ENV and STATE kinds, UNREACHABLE kinds, edge classes), the label rules.
2. work/handoff/CONVERSION_RECIPE.md: steps 1-9 and the sections "hash-checker", "Omni-Notes" and "Added after Omni-Notes". They list the errors that reading the routes found. Apply them from the start, not after the first build.
3. work/handoff/examples/README.md, and the first ~300 lines plus the helper functions of work/graphs/Omni-Notes/graph_def.py (the style to imitate). You do not need the whole file.
4. final_java_only/<App>/app/DATASET.txt (provenance, package, sha256, which flavor was built) and the APP MODULE of the app (its src/main folder; the table 'App modules' in work/handoff/HANDOFF_V2.md gives the path of each app; other modules of the project are libraries unless DATASET.txt or the method list says they are part of the APK).
5. The old generated output of the app, for an INVENTORY only: work/archive/graphs_v1_2026-10-25/<App>/ (edge list, method names, notes). A label or a route copied from it is wrong until you have read the source for it.

## 2. Rules (the reviewer's requirements, summary)
- Every method is REACHABLE (a route from an entry point exists in the standard configuration) or UNREACHABLE with a kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), a reason and a source reference. confirmed_by is SOURCE or INFERRED.
- Gates are structured: ENV kinds (network, tls_chain, permission, hardware, other_app, system_event, time, other) and STATE kinds (data, settings, account, file, session), each with a text. Gesture prose is a guard, not a state.
- Edge classes: explicit (app code calls app code), standard (the framework calls a callback the app registered), non_standard (a library or reflection links the two).
- Standard configuration: the instrumented debug build that the dataset was made from (DATASET.txt; use its flavor), a fresh install on an API 27 emulator, runtime permissions granted only where a route needs them (an ENV permission gate), the fixtures of final_java_only/_fixtures.
- Tool coverage (Monkey / APE, in coverage_baseline.json and sanity_check.csv) is a one-way sanity check. It can show a contradiction; it never sets a label.
- Framework claims cite Android 8.1.0_r1 lines that you printed and read (FW-SRC core/java/... :lines), or are written INFERRED with what was not read. Never FW-MEMORY, DYN or UNVERIFIED.
- Not available here, so their steps stay INFERRED: androidx, Material dialogs, ButterKnife, EventBus, RxJava, SmartLocation, ACRA, ORMLite, LocalBroadcastManager, the JVM class-initialiser rule.
- The only download allowed: AOSP 8.1.0_r1 files from raw.githubusercontent.com/aosp-mirror/platform_frameworks_base (tag android-8.1.0_r1), into work/fw_src/android-8.1.0_r1/ (write to a temp file, then move). No other network use.

## 3. Scope
- Write only in work/graphs/<App>/ and new files in work/fw_src/android-8.1.0_r1/.
- Do not edit work/tools/, work/handoff/ (except nothing), PROGRESS_V2.md, the memory directory, other apps, final_java_only/, the zips, or any git repository. Do not push, commit or install packages.
- If a tool bug blocks you, work around it inside your app folder and report the bug in your final message (the orchestrator fixes tools).
- Before you overwrite graphs/<App>/graph_def.py, move the old file to graphs/<App>/generated_draft_graph_def.py.txt (it is kept for reference and is never built).
- LOCK: start every bash command you run with `touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;`. The resume watcher waits while this file was touched in the last 30 minutes, so this keeps it from starting in the middle of your work.

## 4. Steps
1. First version of graph_def.py, in sections: entry points (manifest launcher, exported components, system broadcasts), lifecycle, pages (SCREENS) and the GUI handlers that move between them, framework callbacks (listeners, adapters, menus, AsyncTask, Handler messages, activity results, EventBus, Rx), gates. Direct app-to-app calls come from the bytecode extractor (USE_AUTO); write only what the bytecode cannot see.
2. Keep graphs/<App>/AGENT_NOTES.md current: what is done, what is left, which step you are on, the last command. If the session can end at any time, the next agent continues from this file.
3. Build: from work/, `python3 -I tools/build_graph.py graphs/<App> <prefix>` (prefix = the app name in lower case with dashes, as in the old output names). Goal: errors 0, warnings 0, STRICT = True.
4. Unreachable review: `python3 -I tools/scan_unreachable.py <App> --all` and `--callers`. Each UNREACHABLE method has a kind, a reason and a source reference. Each caller that the bytecode still shows is explained in the reason.
5. Gates and classes: every edge with a condition has a guard, every edge that needs an earlier action has a STATE, every outside trigger has an ENV kind. A method's reachability must not depend on the test tools.
6. Paths: `python3 -I tools/verify_sample.py <App> 30`, then read each route step by step against the cited source lines with tools/show_route.py <App> <method> --dedupe, including the `if` / `catch` / `for` conditions around each call (tools/cases.py: CS.guard_of(file, line)). Fix every error in graph_def.py. Draw the sample again after the last fix so the logged routes are the final ones. Count checked paths, errors found, fixed, wrong. Error rate = (fixed + wrong) / (correct + fixed + wrong).
7. Log: graphs/<App>/verification.csv (columns type, item, result, confirmed_by, ref, edges, note) with path rows for the sample and the extra methods you read, label rows for every UNREACHABLE method and for the reachable methods of the sample, edge rows for each corrected edge and each framework citation you read. Write your own generator (graphs/<App>/make_verification.py) on the pattern of work/handoff/examples/make_vlog_omni_notes.py, and assert every note against the graph.
8. Notes: graphs/<App>/readme_notes.md with exactly these five headings, in this order: "## What the re-audit changed (compared with the schema 1 graph)", "## How the checked paths were chosen", "## What waits for a device (API 27)", "## Hazard candidates (from reading the code, not reproduced)", "## Limits". Then `python3 -I tools/gen_readme_v2.py <App>` (writes out/README.md).
9. Final checks, all must pass: `python3 -I tools/check_citations.py <App>` (0 problems, 0 FW-MEMORY / DYN / UNVERIFIED), `python3 -I tools/check_routes.py <App>` (0 flagged), `python3 -I tools/check_bytecode_lines.py <App>` (0 where the cited line does not show the callee), `python3 -I tools/tests/check_v2.py` (no app with problems), and `grep -c "DEAD\|FRAMEWORK_ONLY" graphs/<App>/graph_def.py` is 0.
10. Lessons: graphs/<App>/LESSONS.md, 3-8 short bullets on what found real errors in this app.

## 5. Mistakes that reading the routes found in the finished apps (check for them from the start)
- The first-resume shortcut: page edges from onResume or a lambda straight into a list or detail page skip what the first start does (password check, init, adding the fragment). Start every route at the cold start; an edge that is valid only after an earlier visit carries a STATE.
- The best route minimises ENV edges, then STATE edges, then steps, and ignores guards. Check every step of every sampled route, even when the route looks odd.
- `if (!debug && x())` never calls x() in the debug build: remove the bytecode edge (sup) and classify what only x leads to as closed_by_configuration.
- Split a method by how it is reached when its branches depend on it: context variants (X@CASE, X@IMPORT / X@LEGACY, X@EXIST), or the page variant that matches the state. Automatic outgoing edges are copied to every variant: give the branch-specific callee a sup and one hand edge per variant.
- An early return hides the guard of everything after it (for example a save that returns for an empty name). A static flag read once per process (first call only), a SDK-version check, a LeakCanary or other process check: each one is a guard.
- Where data came from: a stored attachment is a file:// URI, a picker result is a content:// URI of the picker's provider. Say which one a route uses.
- Guard-less bytecode edges are the main source of error. For each one, look at the enclosing conditions (CS.guard_of) before you accept it.
- Bytecode line numbers can point one line off (a call inside a chained or multi-line expression): check_bytecode_lines.py finds them; FIX_LINES maps them.
- Copy every ENV text from the code exactly (the reviewer found one that named the wrong locales).
- A framework claim in a hazard list needs the printed source lines, or it is not a hazard candidate.

## 6. Done means
Step 9 passes and steps 1-8 are complete. If you cannot finish, say so exactly: which step is open and why. Never claim done without the checks.

## 7. Your final message (the answer to the orchestrator; at most 250 words, plain words)
App; status DONE or NOT DONE (and the open step); methods, REACHABLE, UNREACHABLE by kind; labels SOURCE / INFERRED; paths checked, errors found, fixed, wrong, error rate, sample size; tool bugs found; the three most important lessons.
