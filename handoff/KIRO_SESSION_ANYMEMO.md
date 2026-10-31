# KIRO SESSION: finish the schema 2 conversion of AnyMemo

One app only. Do the steps in order. Do nothing else. If a step is not written here, do not do it.

Workspace: /Users/darshan/Desktop/yang/work. Run every command from that folder.
App name in every command: AnyMemo (folder graphs/AnyMemo, build prefix anymemo).

LOCK RULE: every bash command you run starts with this text:
touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;

Another agent is working on graphs/Aegis at the same time. Do not open, build, or edit anything in graphs/Aegis or graphs/Markor.

## Files you may read
- handoff/SCHEMA_V2.md (the format; read only the sections you need)
- graphs/AnyMemo/scratch/fix_round1.md (what was already fixed; read the sections "Placeholders still pending", the line starting "- Still-dropped auto edges", and "Round 1b")
- graphs/AnyMemo/AGENT_NOTES.md (section "PAUSE POINT" only)
- handoff/examples/make_vlog_hash_checker.py (the pattern for step 5)
- The app source, always quoted because the folder name contains a #:
  "final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/"
  (the ui files are in its ui/ subfolder, for example ui/CategoryEditorFragment.java)

## Files you may edit
- graphs/AnyMemo/graph_def.py
- graphs/AnyMemo/make_verification.py (new)
- graphs/AnyMemo/verification.csv (new)
- graphs/AnyMemo/readme_notes.md (new)
- graphs/AnyMemo/LESSONS.md (new)
- graphs/AnyMemo/scratch/fix_round2.md (new; your log)
- graphs/AnyMemo/scratch/kiro_*.txt (new; command outputs)
- graphs/AnyMemo/AGENT_NOTES.md: append one line at the end only (step 9)
Files in graphs/AnyMemo/out/ are written by the tools only.

## Never
- Edit tools/, any file in handoff/ except what step 9 says, any other app folder, final_java_only/, the zip files, the memory folder, or any git repository. Do not push, commit, or install anything.
- Download anything. No adb, emulator, or gradle.
- Use tool coverage as evidence for a label. Never cite coverage_baseline.json, sanity_check.csv, monkey, or ape. A tool run only shows that a method ran; the label must come from the source.
- Delete any file, including graphs/AnyMemo/scratch/.
- Change text outside the pieces named in the steps. No refactoring, no reformatting, no renaming.
- Tick PROGRESS_V2.md. Ticking AnyMemo is the user's decision.
- Check other apps, the queue, or anything not listed here.

## STEP 0: start check (no edits)
1. touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK; stat -f '%Sm' -t '%Y-%m-%d %H:%M:%S' graphs/AnyMemo/graph_def.py
   Expected: 2026-10-26 23:04:53. If it is different, STOP (see the STOP section).
2. touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK; grep -n "^STRICT = True" graphs/AnyMemo/graph_def.py
   Expected: a line 39 with STRICT = True.
3. touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK; python3 -I tools/build_graph.py graphs/AnyMemo anymemo > graphs/AnyMemo/scratch/kiro_build_0.txt 2>&1; grep -m1 "^methods" graphs/AnyMemo/scratch/kiro_build_0.txt; grep -m1 "^verdicts" graphs/AnyMemo/scratch/kiro_build_0.txt; grep -m1 "^errors" graphs/AnyMemo/scratch/kiro_build_0.txt; grep -m1 "^warnings" graphs/AnyMemo/scratch/kiro_build_0.txt
   Expected: methods 2207; verdicts REACHABLE 1960, UNREACHABLE 247; errors 0; warnings 0. If not, STOP.

## STEP 1: the six placeholder methods
In graph_def.py, find the comment "# ---- round 1 PENDING" (about line 1823). Below it is a loop, "for _n, _what in (", with six tuples. These six methods are UNREACHABLE with the text "PENDING (round 1)". Each one must end with a real verdict:
- REACHABLE, with a route through a real trigger that you cite from source; or
- UNREACHABLE, with a kind, a reason, and a source reference, and no "PENDING" or "round 1" text.

Three of them ran in a tool run (the build's sanity check says so). That means the current label is wrong. Find the real trigger in the source. The tool run tells you only that they ran.

For each method, print the source lines with sed -n before you decide:

1a. CategoryEditorFragment.onDestroy. File: ui/CategoryEditorFragment.java. Find its host activity, the dialog dismiss calls, and any finish() or dismiss() that destroys it.
1b. PreviewEditActivity.onDestroy. File: ui/PreviewEditActivity.java. Find the finish() calls (Back, menu items, dialogs).
1c. QuizLauncherDialogFragment.onDestroy. File: ui/QuizLauncherDialogFragment.java. Find the dismiss() calls (its buttons) and the host.
1d. CardListActivity.onDestroy. File: ui/CardListActivity.java. Find the finish() calls.
1e. CardEditor.onConfigurationChanged. File: ui/CardEditor.java. Run grep -n onConfigurationChanged on that file. If the class declares it, model a rotation edge from page S_CARD_EDITOR (graph_def.py about line 226) like the one for OptionScreen at graph_def.py line 1124 (SYSTEM, "rotate the device", evidence cites the declaration lines). If the class does not declare it, STOP and report the grep output.
1f. SettingsScreen.onConfigurationChanged. Same as 1e, with ui/SettingsScreen.java and page S_SETTINGS (about line 237).

For 1a to 1d, model exit edges like the pattern at graph_def.py about lines 1796 to 1812 (e('X', 'Y.onDestroy', 'LIFECYCLE', '...', evidence='SRC ...; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')). The fragment destroy steps are androidx and not in the source set: label them INFERRED and say so in the evidence text, the same way the RecentListFragment.onDestroy entry does (about line 1818).

After you decide each method:
- REACHABLE: delete its tuple from the loop and add the edges. Do not also keep it in UNREACHABLE (an UNREACHABLE entry overrides any path in build_graph.py).
- UNREACHABLE: replace its tuple with an UNREACHABLE[...] entry with a real kind (no_trigger_in_app, closed_by_configuration, framework_never_calls, or branch_never_taken) and a reason written from the source lines you printed.

When all six are done: grep -c "PENDING" graphs/AnyMemo/graph_def.py must print 0. Then build (step 4 rules).

## STEP 2: ten automatic edges that the earlier fix dropped
The earlier fixer dropped these automatic CALL edges (the list is in scratch/fix_round1.md, the line starting "- Still-dropped auto edges"). Each pair must be shown as one of: present, added, or not a call.

1. AbstractDownloaderFragment$DownloadListAdapter$1.onClick -> showFetchDatabaseDialog (line 434)
2. AbstractDownloaderFragment$DownloadListAdapter$1$1.call -> openCategory (line 422)
3. AbstractDownloaderFragment$DownloadListAdapter$1.call -> initialRetrieve (line 185)
4. FetchDatabaseTask.doInBackground -> fetchDatabase (line 319)
5. onViewCreated -> refreshList (line 173)
6. RetrieveTask.onPostExecute -> hasMore (line 231)
7. AbstractDownloaderFragment$DownloadListAdapter$1$2.call -> goBack (line 430)
8. AbstractDownloaderFragment$DownloadListAdapter$2.onClick -> startFetchDatabaseTask (line 287)
9. DropboxListActivity.refreshList -> AbstractDownloaderFragment.refreshList (DropboxListActivity.java:95)
10. DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onCreate (DropboxOauth2AccountActivity.java:21)

The class names of items 1 to 8 are shortened in the log. For each item:
a. Find the caller and callee in graphs/AnyMemo/auto_calls.json. If the name is ambiguous, search graphs/AnyMemo/method_list.json.
b. Open graphs/AnyMemo/out/anymemo_trigger_graph.json. Print one edge first (python3 -I -c with json.load) to see the key names, then search the edges for this caller and callee.
c. Write the result in scratch/fix_round2.md as one of:
   - "present: edge id" (the edge exists in the build);
   - "added: edge id, source lines printed" (the call is real and was missing; you added a CALL edge with its citation);
   - "not a call: the source lines show why".
If you add a hand edge: build_graph.py line 223 drops any automatic CALL on the same pair. After the next build, check that the pair has exactly one CALL edge with the citation you intend.

## STEP 3: sample and route check
1. touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK; python3 -I tools/verify_sample.py AnyMemo 30 20261025 > graphs/AnyMemo/scratch/kiro_sample_30.txt
2. For each method in that sample, run: python3 -I tools/show_route.py AnyMemo "<method>" --dedupe --max 8
3. Read every step against the printed source lines, including the if, catch, and for conditions around each call. Use sed -n to print the lines. Judge each path:
   - correct: every step is supported by the source, guards and gates included
   - fixed: a step or a guard was wrong or missing; you corrected graph_def.py, rebuilt, and the route is now right
   - wrong: wrong and not fixed
   - unclear: depends on another app, the keyboard, a WebView engine, or code you cannot read
4. show_route.py has a known bug: an evidence citation with a comma (for example "SRC File.java:403, 408-424") is cut at the comma. When a step's citation has a comma, print each range yourself with sed -n before you judge the step.
5. Fix each wrong route in graph_def.py. After each fix, build (errors 0, warnings 0) and read the route again. Log each fix in scratch/fix_round2.md: the method, the step, the source lines you printed, and what changed (the block and line).
6. A route that needs a state no in-app action can create is wrong. List it in the log. Do not invent a fix for it.
7. After the last fix, draw the sample again with the same command, written to graphs/AnyMemo/scratch/kiro_sample_30_final.txt. Re-read every route whose steps changed. The logged sample is the final draw.
8. Count over the final draw: correct, fixed, wrong, unclear. Error rate = (fixed + wrong) / (correct + fixed + wrong).

## STEP 4: build
Build after every change to graph_def.py: errors 0 and warnings 0. Use the command from STEP 0, item 3, and write the output to graphs/AnyMemo/scratch/kiro_build_final.txt at the end.

## STEP 5: verification.csv
1. Read handoff/examples/make_vlog_hash_checker.py. Write graphs/AnyMemo/make_verification.py with the same structure. Write AnyMemo's own notes; do not copy notes text from the example. Paths used by the script must be inside graphs/AnyMemo/ or tools/. No /private/tmp and no session folders. Read the final sample from scratch/kiro_sample_30_final.txt.
2. The header line must be exactly: type,item,result,confirmed_by,ref,edges,note
3. Rows:
   - path: one per sampled method. item = the method; result = correct, fixed, wrong, or unclear; confirmed_by = SOURCE (INFERRED if the route relies on an inferred claim); ref = the key file:lines; edges = the route edge ids from out/methods.csv.
   - label: one per UNREACHABLE method (247 rows) and one per sampled reachable method. Result correct or fixed.
   - edge: one per edge that you corrected or added in steps 1 and 2, and one per framework claim you checked. Edge ids come from out/anymemo_trigger_graph.json.
4. The script must check every note against the graph and stop if one does not match.
5. Run from the work folder: python3 -I graphs/AnyMemo/make_verification.py. Then rebuild. There must be no STALE warning.

## STEP 6: readme_notes.md
Write graphs/AnyMemo/readme_notes.md with exactly these five headings, in this order:
## What the re-audit changed (compared with the schema 1 graph)
## How the checked paths were chosen
## What waits for a device (API 27)
## Hazard candidates (from reading the code, not reproduced)
## Limits
Hazard candidates: only items whose source lines you printed. Keep the list short.
Then run: python3 -I tools/gen_readme_v2.py AnyMemo (this writes out/README.md).

## STEP 7: LESSONS.md
Write graphs/AnyMemo/LESSONS.md with 3 to 8 short bullets: what found real errors in this app.

## STEP 8: final checks (all must pass)
1. python3 -I tools/build_graph.py graphs/AnyMemo anymemo: errors 0, warnings 0
2. python3 -I tools/check_citations.py AnyMemo: 0 problems, and "FW-MEMORY / DYN / UNVERIFIED: 0"
3. python3 -I tools/check_routes.py AnyMemo: 0 flagged. Any flagged route must be explained in readme_notes.md.
4. python3 -I tools/check_bytecode_lines.py AnyMemo: 0 bad
5. python3 -I tools/tests/check_v2.py: copy its last lines into your log. It does not cover hand-written apps (it skipped Markor), so say that in your final message.
6. grep -c "DEAD\|FRAMEWORK_ONLY" graphs/AnyMemo/graph_def.py: must print 0
7. grep -c "PENDING" graphs/AnyMemo/graph_def.py: must print 0
Every command starts with the LOCK RULE text.

## STEP 9: close
1. Append one line at the end of graphs/AnyMemo/AGENT_NOTES.md with a heredoc (cat >>). Do not edit older text. The line gives the date, the status (DONE or NOT DONE), and "see scratch/fix_round2.md".
2. Do not delete graphs/AnyMemo/scratch/. The graph's comments refer to files there, and the user decides when it goes.

## STOP AND REPORT
Stop and change nothing more if:
- the STEP 0 check differs from the expected values;
- a build error cannot be fixed in 3 tries;
- a step needs a file or fact you do not have;
- you are tempted to do anything not written in this file.
Write the blocker under "## Blocked" at the end of graphs/AnyMemo/scratch/fix_round2.md, then stop.

## FINAL MESSAGE (at most 12 lines, nothing else)
1. App AnyMemo; status DONE or NOT DONE, and the open step.
2. Build counts: methods, REACHABLE, UNREACHABLE by kind, errors, warnings.
3. Labels: SOURCE and INFERRED counts (from out/build_report.txt).
4. Sample: size, correct, fixed, wrong, unclear, error rate.
5. The six placeholders: one short verdict each.
6. The ten automatic edges: present, added, or not a call.
7. Files changed.
8. Blockers, if any.
