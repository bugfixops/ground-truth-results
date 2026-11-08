LibreTorrent: continue the conversion (session 2)

You are continuing ONE job: converting the Android app LibreTorrent to the "schema 2" ground-truth trigger graph. Work only on LibreTorrent. Other apps belong to other agents: do not read them as work, do not write to them. The full brief is in CHATGPT_BRIEF_LIBRETORRENT.md. If this prompt and the brief disagree, this prompt wins.

The work folder is the one that holds tools/ and graphs/. The app folder is graphs/LibreTorrent/.

WHAT "DONE" MEANS (for the whole app; this session does only part of it)
1. Every one of the 4,732 methods in method_list.json has exactly one label, from source you printed and read.
2. Every REACHABLE method has a route from an entry point, made of edges you wrote by hand, with printed source lines.
3. Build: 0 errors, 0 warnings, STRICT = True.
4. A 30-path check: every step read against printed lines, errors fixed, all logged.
5. Files: verification.csv (written by make_verification.py), readme_notes.md (five headings), LESSONS.md, AGENT_NOTES.md.
Until all five hold, the app is NOT DONE. Do not write "done" anywhere.

CURRENT STATE (checked 2026-10-28, 23:53)
- S1 done: dataset, manifest, entry points. S2 done: the old draft is kept as generated_draft_graph_def.py.txt.
- 80 of 4,732 methods labelled UNREACHABLE: batch 1 and batch 2, in graph_def.py.
- graph_def.py has NO hand-written edges. Its edges come from the generator (gen_edges.apply) and the bytecode scan. That is not evidence. This is the main defect to fix.
- Build: 0 errors, 210 warnings: 201 gates with no kind, 8 UNREACHABLE methods that still have incoming edges, and 1 REVIEW item (2,870 default-class edges that may be library links). STRICT = False.
- Route checks, verification.csv, readme_notes.md and LESSONS.md: not started.

ENTRY POINTS (from the S1 notes; check each one against AndroidManifest.xml)
- Application: MainApplication.
- Launcher activity: .ui.main.MainActivity (MAIN, LAUNCHER, LEANBACK_LAUNCHER); also exported for SEARCH.
- Other exported activities: .ui.addtorrent.AddTorrentActivity (SEND; VIEW for file, content, http and https torrent data and magnet URIs); .ui.SendTextToClipboard (SEND text); .ui.settings.SettingsActivity (APPLICATION_PREFERENCES); .ui.addfeed.AddFeedActivity (SEND; VIEW for http and https feed URLs).
- Service: .service.TorrentService (not exported; foreground dataSync).
- Exported receiver: .receiver.BootReceiver (boot, quickboot, exact-alarm-permission actions). Also JacocoInstrument.SMSInstrumentedReceiver: check whether it is part of the app or only of the coverage build.
- Provider: androidx.core.content.FileProvider (not exported).

RULES (strict)
A. Evidence. A label or an edge is written only after you have printed the source lines (for example with sed -n) and read them. Generator output, bytecode-scan output, the old draft and the build's REACHABLE count are candidates only. They are never evidence.
B. Candidate lists. Keep generator output as a to-do list in graphs/LibreTorrent/scratch/candidates_<batch>.txt. Each candidate ends as one of: confirmed (you write the e(...) edge by hand, citing printed lines), rejected (reason written), or open (reason written). Never copy a candidate into graph_def.py without confirming it.
C. Tool coverage (Monkey, APE, coverage_baseline.json, sanity_check.csv, JaCoCo reports) is never evidence, and never a reason to add or remove a label. Do not open those files to decide a label.
D. Labels. REACHABLE: a route from an entry point exists, and every step is a hand-written edge. UNREACHABLE: exactly one kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), a reason, and a source reference. Never give UNREACHABLE to a method that has a route.
E. confirmed_by. SOURCE: you printed the lines. INFERRED: library or generated code that is not in the upload, or code you did not read. Never write FW-MEMORY, DYN or UNVERIFIED.
F. Generated classes (the BR classes, the DataBinderMapperImpl inner classes, DataBindingTriggerClass): the citation is the output of a grep over the source for the class name, saved in the scratch folder. Do not cite "method_list.json:1".
G. Edge classes. explicit: app code calls app code. standard: the framework calls a callback the app registered (lifecycle, listeners, menu callbacks, AsyncTask, activity results, the launcher entry). non_standard, with a via: a library or reflection makes the link, and no app code calls or registers the target (EventBus, data binding, dependency injection, Rx, reflection, XML android:onClick, intents resolved by action name, receivers reached by name).
H. Gates. ENV kinds: network, tls_chain, permission, hardware, other_app, system_event, time, other. STATE kinds: data, settings, account, file, session. Copy each gate text exactly from the code. An ordinary program condition is not a gate.
I. Standard configuration: the debug build (package org.proninyaroslav.libretorrent.debug), a fresh install, API 27, runtime permissions granted only where a route needs them.
J. No waivers. If a check fails, say so. Never write "passed" for a check you did not run.
K. At most 40 methods per batch.
L. Do not edit handoff/PROGRESS_V2.md, tools/, the memory folder, or any other app. No push, no commit, no package installs. No network use except the AOSP 8.1.0_r1 files, and only if your environment allows it.

THIS SESSION (do these steps in order; do not start batch 4)

Step 1. Re-check the 80 existing labels. For each one, print the cited lines and confirm that the method matches and the reason holds. Fix or remove any that fail. Fix the generated-class citations under rule F. Write the result to graphs/LibreTorrent/scratch/recheck_batches_1_2.md as a table: method | cited lines | result.

Step 2. Resolve the 8 warnings. Each is an UNREACHABLE method that still has an incoming edge. The team has already checked these facts, and you must confirm them in the source yourself:
- NanoHTTPD.decodeParameters(Map) has no caller in NanoHTTPD.java. decodeParameters(String) is called only by decodeParameters(Map).
- NanoHTTPD.mimeTypes is called only by getMimeTypeForFile, which is UNREACHABLE. loadMimeTypes is called only by mimeTypes.
- makeSSLSocketFactory(KeyStore,KeyManagerFactory) and makeSSLSocketFactory(KeyStore,KeyManager[]) are called only from other UNREACHABLE methods of NanoHTTPD.
- NanoHTTPD.wasStarted is called only by isAlive, which is UNREACHABLE. SecureServerSocketFactory.<init> is called only from makeSecure. Cookie.<init>(String,String,int) is called only from Cookie.<init>(String,String).
- The app code (core/model/stream/TorrentStreamServer.java) calls super(host, port), start(), stop(), and newFixedLengthResponse with the (Status, String, String) and (Status, String, InputStream, long) overloads. Print those lines yourself.
For each warning, choose one: (a) the caller has no route: remove that edge from graph_def.py, and record the edge id, the caller and the printed lines in graphs/LibreTorrent/scratch/conflicts.md; or (b) the caller has a route: the callee is not UNREACHABLE and needs a route. Do not leave a warning unexplained.

Step 3. Gate kinds. The build report lists 201 gates under "TO CLASSIFY". Group the distinct gate texts. For each text, choose an ENV kind or a STATE kind from the printed source, and write the choice in graphs/LibreTorrent/scratch/gates.md. If the text is an ordinary program condition, remove it from the gate and log that in gates.md.

Step 4. Batch 3: 40 methods, from RepositoryHelper.<init> to TorrentDownloadImpl.isAutoManaged (the range is in AGENT_NOTES.md; check it against method_list.json). Label each method: a route built from hand-written edges, or UNREACHABLE with kind, reason and source. Write graphs/LibreTorrent/scratch/batch_003.md with the rows: method | label | kind | reason | printed file:lines. If you cannot finish the batch, write the finished rows and mark the rest OPEN with the reason.

Step 5. Build. From the work folder, run: python3 -I tools/build_graph.py graphs/LibreTorrent libretorrent. Save the output. If you cannot run Python, write "build not run" and do not report counts from memory.

Step 6. Update graphs/LibreTorrent/AGENT_NOTES.md with: the date and time (from the date command), the batches done, batch 4 as the next batch, the open warnings, the open gates, the build counts, and the commands you ran.

Step 7. Stop. Do not start batch 4 in this session.

WHAT TO RETURN AT THE END
1. Status: NOT DONE, and the open step.
2. Build counts (methods, REACHABLE, UNREACHABLE, UNRESOLVED, errors, warnings) and the build output, or "build not run".
3. Every file you changed or created, with its full text in a separate block labelled by its path. If you can write files yourself, list the paths instead.
4. Anything blocked, and any input you did not have. Do not guess the content of a file you have not read.
Keep the status part under 12 lines.
