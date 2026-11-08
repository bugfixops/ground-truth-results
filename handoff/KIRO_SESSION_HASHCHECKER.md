KIRO SESSION: finish the schema 2 conversion of the hash-checker graph. One app only. Follow this exactly and do nothing else.

Workspace: /Users/darshan/Desktop/yang/work. Run every command from there. The app name in every command is hash-checker (folder graphs/hash-checker, build prefix hash-checker).

READ FIRST, in this order, and nothing else:
1. handoff/SCHEMA_V2.md (the output format)
2. handoff/CONVERSION_RECIPE.md (the steps)
3. graphs/hash-checker/KIRO_WORKLIST.md (your task list: 36 claims, then 22 UNREACHABLE methods)
4. graphs/Diary/verification.csv and graphs/Diary/readme_notes.md (a finished example of the log and the notes; Diary was done the same way)

STATE NOW: graphs/hash-checker/graph_def.py already ends with a "schema 2" block written by Claude (UNREACHABLE, ENV and STATE kinds, EDIT, CLASSIFY) and the line STRICT = True. It builds with errors 0 and warnings 0. Do not rewrite that block. Claude already did these, do not redo them: classified the 9 REVIEW edges (CLASSIFY); moved two methods to UNREACHABLE closed_by_configuration (SharedPreferencesSettings.setRefreshSelectedFileStatus and getThemeAnalogue: only a pre-seeded preferences file opens them) and removed their two edges; rewrote the App.onTerminate reason with Android 8.1 lines (already printed and checked); removed the baseline wording from the ENV texts.
App source: final_java_only/hash-checker/app/hash-checker-#v3.7.3/app/src/main/java/com/smlnskgmail/jaman/hashchecker/ (always quote this path, it contains a #). Citations in graph_def.py use the file name only, e.g. SRC HashCalculatorFragment.java:573-582.
Framework source: only the folder fw_src/android-8.1.0_r1/ (no .plan folder for this app). Cite its files as FW-SRC <path below that folder>:<lines>, same style as the two existing FW-SRC citations in graph_def.py. The app uses androidx (fragments, RecyclerView, AppCompat, material) and ORMLite: their sources are NOT held, so claims about them stay INFERRED (that is expected: do not try to cite the AOSP android.app.Fragment instead).

YOU MAY EDIT ONLY: graphs/hash-checker/graph_def.py, graphs/hash-checker/verification.csv, graphs/hash-checker/readme_notes.md. Files in graphs/hash-checker/out/ change only by running the tools. Not tools/, not KIRO_WORKLIST.md, not other apps, not final_java_only/, not ../work-emulator/.

NEVER: download anything; run adb, an emulator or gradle; use tool coverage (monkey_hit, ape_hit, coverage_baseline.json, sanity_check.csv) as evidence for a label; cite a line you did not print; write FW-SRC from memory; create any other file, script or note; refactor or reformat graph_def.py; "improve" the model of the app; start another app; commit or push.

STEPS

1. EVIDENCE. Go through every claim row of KIRO_WORKLIST.md in order and edit graph_def.py as the Action column says:
   S = cite. First print the lines: sed -n "A,Bp" fw_src/android-8.1.0_r1/<path> (framework) or on the app file (app lines). If they show what the claim says, cite as FW-SRC <path>:A-B or SRC File.java:A-B. If they do not support it, make the claim INFERRED and say why.
   I = keep the claim, make the text start with INFERRED, and say what was not read (library name, "source not read").
   S/I = two parts, see the row; write both segments.
   R = delete the DYN segment (there should be none).
   Three claims are Python constants near line 99 (FW_LC, FW_ADAPTER, FW_TW): edit the constant once. Edges whose evidence is only the bare word FW-MEMORY or INFERRED need a real text: write what the edge claims, then the citation or INFERRED.
   Also reword the FW-MEMORY words that sit in a note= or NOTES text (find them with grep -n "FW-MEMORY" graphs/hash-checker/graph_def.py): INFERRED + what was not read, or a citation you printed. At the end that grep must print nothing.
   After every 10 rows run: python3 -I tools/build_graph.py graphs/hash-checker hash-checker (errors must stay 0, warnings 0) and python3 -I tools/check_citations.py hash-checker (must say 0 problems).
   Done when check_citations shows "evidence with FW-MEMORY / DYN / UNVERIFIED: 0".

2. STRICT. Confirm the build still prints errors 0 and warnings 0. If a "TO CLASSIFY" line or a REVIEW warning appears, classify the listed edges (kinds and rules in SCHEMA_V2.md) and change nothing else.

3. READ PATHS. Run python3 -I tools/verify_sample.py hash-checker 30. For each method it lists run: python3 -I tools/show_route.py hash-checker "<method>" --dedupe --max 8
   Read every step against the printed source lines, including guards and ENV/STATE gates. Result per path:
   correct = every step is supported.
   fixed = a step was wrong or a guard/context was missing; you corrected graph_def.py, rebuilt, and the new route is right. Fix by splitting a node into @CONTEXT variants (example in Currency: onActivityResult@OK and @CANCEL).
   wrong = wrong and not fixed.
   unclear = depends on another app, the IME, the WebView engine, or something you cannot read.
   Watch for: a step that needs state no in-app action can create (a preference nothing writes, an item no code adds): that path is wrong, say so in the note and list the method in your final message (do not invent a fix). Also a Back/Up step whose fragment or back stack does not exist at that moment, and a route that assumes a successful result where the guard needs the cancelled one.
   Then run python3 -I tools/check_routes.py hash-checker and read every route it flags.

4. LOG (do this last, after the final build, because edge ids change when evidence text changes). Write graphs/hash-checker/verification.csv with the header exactly: type,item,result,confirmed_by,ref,edges,note
   - one path row per sampled method: item = method, edges = its route_edge_ids from out/methods.csv, ref = the key file:line, confirmed_by = SOURCE (INFERRED for unclear), result as above;
   - one label row per UNREACHABLE method (the 22 in the second table of the work list): result correct, ref = its source_ref, after you grep its call sites once more. Two special checks: (a) SettingsFragment.lambda$initRate$7: read final_java_only/hash-checker/app/DATASET.txt and the productFlavors in the app build.gradle and confirm the dataset APK is the thirdPartyStores flavor; if not, fix the reason and kind; (b) BaseFragment.setAllowBackAction and AppTextWatcher.onTextChanged: confirm every subclass really overrides them (print the lines);
   - one label row per sampled reachable method: correct or fixed;
   - one edge row per distinct framework claim you verified (the edge id is in out/*_trigger_graph.json).
   Rebuild. No STALE warning may remain.

5. NOTES. Write graphs/hash-checker/readme_notes.md with exactly these headings: "## What the re-audit changed (compared with the schema 1 graph)", "## How the checked paths were chosen", "## What waits for a device (API 27)", "## Hazard candidates (from reading the code, not reproduced)" (copy the hazards from archive/graphs_v1_2026-10-25/hash-checker/out/README.md, section "Hazard candidates"), "## Limits". Every number must come from out/build_report.txt or from the table in out/README.md. Mention in the first section: DEAD, FRAMEWORK_ONLY and REACHABLE_AFTER_SETUP are gone; the two pre-seeded-preference methods are now UNREACHABLE closed_by_configuration; the 9 Dagger/lifecycle REVIEW edges were decided as standard/explicit/page. In "Limits" say that the androidx and ORMLite sources were not read, so those claims (and every label whose best route uses them) are INFERRED. Then run python3 -I tools/gen_readme_v2.py hash-checker

6. FINAL CHECKS, all must hold: build_graph.py errors 0 and warnings 0; check_citations.py 0 problems and "FW-MEMORY / DYN / UNVERIFIED: 0"; grep -n "FW-MEMORY" graphs/hash-checker/graph_def.py prints nothing; check_routes.py 0 flagged, or each flagged route explained in readme_notes.md; python3 tools/tests/check_v2.py ends with "apps with problems: 0".

STOP AND REPORT if a step needs a file or fact you do not have, if you cannot fix a build error in 3 tries, or if you are tempted to do anything not listed. Write what blocked you under "## Blocked" at the end of readme_notes.md and stop.

FINAL MESSAGE, max 12 lines, nothing else: the counts from out/build_report.txt (verdicts, labels confirmed SOURCE and INFERRED, path status); the verification table (rows, correct, errors found, unclear); one line per edge or route you changed in graph_def.py and why; every method whose path you found wrong and did not fix.
