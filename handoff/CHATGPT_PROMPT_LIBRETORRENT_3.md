LibreTorrent: corrected instruction (session 2, part 2)

You are continuing ONE job: converting the Android app LibreTorrent to the "schema 2" ground-truth trigger graph. Work only on LibreTorrent. Do not read or write other apps. The brief is CHATGPT_BRIEF_LIBRETORRENT.md. If this text and the brief disagree, this text wins.

The work folder is the one that holds tools/ and graphs/. The app folder is graphs/LibreTorrent/. The batch list is handoff/LIBRETORRENT_BATCH_PLAN.tsv: 4,732 rows, 120 batches of at most 40 methods. Use it as the only source of batch membership.

PART 1: WHAT WAS WRONG IN THE LAST SESSION (fix these first)
1. graph_def.py still calls gen_edges.apply(...). The generator supplies all 12,561 edges. Generator output is never evidence, so this must be removed.
2. The gate count was wrong. There are 54 gate edges with 4 distinct texts (step 4). The other 329 unlabelled methods are UNREACHABLE "unclassified" (build verdict line: unclassified 329). Those are real work items, not gates.
3. scratch/generated_class_grep.txt is empty. The "grep: no match" citations have no output behind them. Redo them (rule F).
4. The recheck table marks 80 labels "confirmed", but the printed lines were not saved. Save the printed output.
5. AGENT_NOTES.md was not updated after the last edit, and the build report is older than the last edit to graph_def.py. A build is valid only if it runs after your last edit.
6. Batch 3 was described by name only. Use the plan file.
7. Gate decisions go in scratch/gates.md (not gates_helper.md).

PART 2: DEFINITION OF DONE (for the whole app; this session does only part of it)
- Every method in method_list.json has exactly one label, from source you printed and read.
- Every REACHABLE method has a route from an entry point, made of hand-written edges with printed source lines.
- Build: 0 errors, 0 warnings, STRICT = True.
- A 30-path check: every step read against printed lines, errors fixed, all logged.
- Files: verification.csv (written by make_verification.py), readme_notes.md (five headings), LESSONS.md, AGENT_NOTES.md.
Until all of these hold, the app is NOT DONE. Do not write "done" anywhere. The plan has 120 batches, so this takes several sessions.

PART 3: RULES (strict)
A. A label or an edge is written only after you print the source lines (save the command and its output in scratch/) and read them. Generator output, the bytecode scan, the old draft and the build's REACHABLE count are candidates only.
B. Candidates stay in scratch/candidate_edges_snapshot.json (step 1). A candidate becomes an edge only as a hand-written e(...) that cites lines you printed. A rejected or open candidate is logged with its reason.
C. Tool coverage (Monkey, APE, coverage_baseline.json, sanity_check.csv, JaCoCo reports) is never evidence. Do not open these files to decide a label.
D. REACHABLE: a route from an entry point, and every step is a hand-written edge. UNREACHABLE: exactly one kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), a reason, and a source reference. Never give UNREACHABLE to a method that has a route.
E. confirmed_by: SOURCE (you printed the lines) or INFERRED (library or generated code that is not in the upload, or code you did not read). Never write FW-MEMORY, DYN or UNVERIFIED.
F. Generated classes (the BR classes, the DataBinderMapperImpl inner classes, DataBindingTriggerClass): the citation is the saved output of a real grep over the source root. Write the exact command in the file. "method_list.json:1" is not a citation.
G. Edge classes: explicit (app code calls app code); standard (the framework calls a callback the app registered: lifecycle, listeners, menu callbacks, AsyncTask, activity results, the launcher entry); non_standard, with a via (a library or reflection makes the link, and no app code calls or registers the target).
H. Gates: ENV kinds (network, tls_chain, permission, hardware, other_app, system_event, time, other) or STATE kinds (data, settings, account, file, session). Copy each gate text exactly from the code. An ordinary program condition is not a gate.
I. Standard configuration: the debug build (package org.proninyaroslav.libretorrent.debug), a fresh install, API 27, runtime permissions granted only where a route needs them.
J. No waivers. If a check fails, say so. Never write "passed" for a check you did not run.
K. At most 40 methods per batch.
L. Do not edit handoff/PROGRESS_V2.md, tools/, other apps, or the memory folder. No push, no commit, no package installs. No network use except the AOSP 8.1.0_r1 files, and only if your environment allows it.

PART 4: STEPS (in this order; update AGENT_NOTES.md after each step)

Step 1. Snapshot. Copy out/libretorrent_trigger_graph.json to scratch/candidate_edges_snapshot.json, and out/methods.csv to scratch/candidate_methods_snapshot.csv. These are candidates only.

Step 2. Recheck batches 1 and 2 (the 80 plan rows with status DONE_RECHECK). For each method, print the cited lines, save the printed output to scratch/recheck_printed.txt, and write scratch/recheck_batches_1_2.md as a table: method | cited lines | printed (yes or no) | result. Fix or remove any label that fails. Redo the generated-class rows under rule F.

Step 3. Remove the generator. Delete the import of gen_edges and the gen_edges.apply line from graph_def.py. Keep the EDIT, SUPPRESS and label code. Run the build once and save the output as scratch/build_after_generator_removed.txt. Expect most methods to be unlabelled now. That is the honest remaining work. Do not add labels to make the counts look better.

Step 4. Gates. The build flagged 54 gate edges with 4 distinct texts:
- T1 (42 edges): "The list / adapter shows at least one row (some user data exists: add an item first)". The earlier helper suggested STATE data (EmptyRecyclerView.java:69-76 checks the item count). Verify it yourself.
- T2 (5 edges): "outside package: the notification shade, an alarm, a launcher widget or shortcut starts it".
- T3 (4 edges): "outside package: another app, the system or adb sends the intent / broadcast / content call".
- T4 (3 edges): "outside package: the device reboots (BOOT_COMPLETED) or another system broadcast arrives".
For each text, decide the kind (an ENV kind or a STATE kind, or remove it as an ordinary program condition), from printed source. Find the 54 edge ids in the snapshot, and note any edge where the text does not fit. Write scratch/gates.md with: text | decision | printed lines | edge ids | reason.

Step 5. Batch 3: the 40 plan rows with batch 3, from RepositoryHelper.<init> to TorrentDownloadImpl.isAutoManaged. For each method, decide from printed source: a route built from hand-written edges, or UNREACHABLE with kind, reason and source reference. Write scratch/batch_003.md with: method | label | kind | reason | printed file:lines. Save the printed output in scratch/batch_003_printed.txt. A method you cannot finish is marked OPEN with the reason. Do not start batch 4.

Step 6. Build. From the work folder, run: python3 -I tools/build_graph.py graphs/LibreTorrent libretorrent. Save the output as scratch/build_<n>.txt. Report: methods, REACHABLE, UNREACHABLE by kind, UNRESOLVED, errors, warnings. This build must run after your last edit. If it does not, say so.

Step 7. Update graphs/LibreTorrent/AGENT_NOTES.md with: the time (from the date command); the status of batches 1, 2 and 3; the gate decisions; the build counts and the build file name; the open items; and "next: batch 4".

Step 8. Stop.

PART 5: RETURN
1. Status: NOT DONE, and the open step.
2. Build counts and the build output, or "build not run". Never report counts from memory.
3. Every changed or new file, with its full text in a separate block labelled by its path (or list the paths if you can write files yourself).
4. Anything blocked, and any input you did not have. Do not guess the content of a file you have not read.
Keep the status part under 12 lines.
