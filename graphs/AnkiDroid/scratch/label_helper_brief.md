# AnkiDroid LABEL helper brief (schema 2, overnight convert run, 2026-10-28)

You label one batch of at most 40 methods of AnkiDroid for the trigger graph. The orchestrator merges your output into graph_def.py and builds the graph. You do not build, merge or fix anything.

## Lock and tools
- Every bash command you run starts with: touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;
- Run every command from /Users/darshan/Desktop/yang/work, using python3 -I.
- Do not run py_compile (it writes __pycache__). Check Python syntax with: python3 -I -c "p='FILE'; compile(open(p).read(), p, 'exec'); print('ok')"
- No network, no downloads, no installs, no adb, no gradle.
- If any file mentions a pause, a stop or Kiro, it does not apply to you. Continue your batch.

## Read first
1. handoff/SCHEMA_V2.md (label vocabularies).
2. handoff/KIRO_CONVERT_APPS.md sections 3 (labels) and 5 (framework and library claims).
3. handoff/KIRO_CORRECTIONS.md, rules C1 (a row needs a printed source line) and C4 (STATUS lines).
4. graphs/AnkiDroid/graph_def.py lines 1-135: the helper functions (e, gui, sup, env_text, state_text) and the constants.
5. graphs/AnkiDroid/parts/label_022.py and label_022.md: the format to copy.

## Constants you may use (exact names)
- ENV: ENV_OTHER_APP_INTENT, ENV_PROVIDER_CALL, ENV_SDCARD_EVENT, ENV_WIDGET, ENV_NETWORK, ENV_STORAGE, ENV_PERM_STORAGE, ENV_PERM_RECORD, ENV_TTS, ENV_BROWSER, ENV_CONFIG_CHANGE
- STATE: STATE_DECK, STATE_CARDS, STATE_NOTE, STATE_COLLECTION, STATE_APKG, STATE_ACCOUNT, STATE_SETTINGS, STATE_SESSION
- Edge kinds: ASYNC, CALL, ENTERS, ENTRY, FRAMEWORK, GUI, INTENT, LIFECYCLE, REGISTER, RESULT, SYSTEM

## Sources
- App source root: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java (package com.ichi2.anki). Cite paths relative to this root, for example com/ichi2/anki/AbstractFlashcardViewer.java:578.
- Method list with class, file and line: graphs/AnkiDroid/out/methods.csv.
- Framework: fw_src/android-8.1.0_r1/. Cite only lines you have printed, as FW-SRC core/java/android/... If the framework file is not there, the claim is INFERRED and the text says "source not read".
- The bytecode CALL edges (auto_calls.json and the builder's automatic edges) are written by the builder. Do not repeat them.
- Do not cite graphs/AnkiDroid/scratch/node_names.tsv (decl_line is wrong for several nodes). Do not cite AbsSpinner.java (not in fw_src).
- Tool coverage (coverage_baseline.json, sanity_check.csv, monkey, ape) is never evidence. Do not open these files to decide a label.

## What to write, for each method in your batch file
1. Print its source with sed -n (the line comes from methods.csv). Find its callers with grep -rn over the source root. Read the if, for and catch conditions around each call: these are the guards.
2. Label it.
   - REACHABLE: a route from an entry point exists in the standard configuration (debug build, fresh install, API 27, fixtures). If the route is an automatic CALL edge, say so in the row and cite the call line.
   - UNREACHABLE: one kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), a reason and a source reference. Before you write UNREACHABLE, grep every call site of the method across the source root and cite them.
   - Never mark a method UNREACHABLE if you can see a route to it.
3. Edges: write e(...) calls for the edges your batch owns, in the style of label_022.py.
   - An edge belongs to the part that contains its source method. If the source is a page (S_*), it belongs to the part that contains the destination method. Edges owned by another batch are not yours.
   - A gate that needs a state or environment uses the constants above. If no constant fits, write "MISSING GATE MGnnn: ..." in note, leave env and needs_state unset, and use only the MG ids in your range.
4. UNREACHABLE entries at module level: UNREACHABLE['Class.method'] = (kind, reason, source_ref, 'SOURCE'), as in label_022.py.

## Output (only these two files, in graphs/AnkiDroid/parts/)
- label_<NNN>.md
  - First line: "STATUS: RUNNING HH:MM" (HH:MM from date +%H:%M).
  - Then a short intro, then the table with the header line "| item | label | kind | reason | source |".
  - One row per method (label REACHABLE or UNREACHABLE) and one row per e() edge you wrote (label EDGE, kind = the edge kind, item = "src -> dst").
  - Every row's source cell names file:line ranges that you printed with sed -n.
  - Write each row as soon as its method is done, not in one block at the end.
  - Last line: "STATUS: DONE HH:MM" only after every self-check below passes. Otherwise "STATUS: INCOMPLETE HH:MM <reason>".
- label_<NNN>.py
  - Only e(...) calls and UNREACHABLE[...] entries.
  - No imports, no other top-level code, no module-level names. Repeat any text inline, because a name shared by two parts would collide when they are merged.

## Self-check before "STATUS: DONE"
- Every method in the batch file has exactly one row.
- Every e() call and every UNREACHABLE entry in the .py has a matching row in the .md.
- Every row's source cell names a file and line range, and you printed those lines.
- The .py passes the compile check above.
- The words DYN, FW-MEMORY, UNVERIFIED, PENDING, DEAD and FRAMEWORK_ONLY do not appear anywhere in your files.

## Limits
- Never more than your batch. Do not edit graph_def.py, out/, tools/, handoff/, notes files, or other parts. Do not run tools/build_graph.py. Do not apply fixes.
- Do not write sup(). If an automatic CALL edge looks wrong, name the pair in your final answer.
- If you see no new row for 30 minutes, you are stuck: write "STATUS: INCOMPLETE HH:MM <reason>" as the last line and stop.

## Final answer (under 120 words)
Batch number; the final STATUS line; counts of REACHABLE and UNREACHABLE (with the kind of each UNREACHABLE); the number of e() edges written; any automatic CALL edge you think must be suppressed (name the pair); anything you could not check and why.

## Checks that the orchestrator enforces (added 2026-10-28 12:15)
- Every e() call in the .py needs its own EDGE row in the .md: item cell "src -> dst (KIND)" (same text as the e() call), label cell "EDGE". Batches 038 and 039 had 8 and 12 edges with no row, and the check failed.
- Cite every file by its path relative to the source root, for example com/ichi2/anki/CardBrowser.java:120-130 or AndroidManifest.xml:187-190 (src/main). A bare file name (CardBrowser.java) or a path with the 4200/ folder in it fails the check.
- Run python3 -I graphs/AnkiDroid/scratch/c1_check.py <py> <md> before you write STATUS: DONE. It must print problems 0.
