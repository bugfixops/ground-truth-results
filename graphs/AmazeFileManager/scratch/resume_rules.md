BINDING FILES (read first; on conflict these win): /Users/darshan/Desktop/yang/work/handoff/KIRO_CONVERT_APPS.md (sections 1,3,5,8,10,11,12), /Users/darshan/Desktop/yang/work/handoff/KIRO_CORRECTIONS.md (C1-C8). Helper output format reference: /Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/HELPER_INSTRUCTIONS.md.
SCOPE: LABELING ONLY. Do NOT draw the route sample, start route verification, write verification.csv/readme_notes.md/LESSONS.md, or edit handoff/PROGRESS_V2.md or handoff/PAUSE_KIRO.md. No worktree, edit in place. No waivers, no decisions in anyone's name, no unprinted counts.
CWD for every command: /Users/darshan/Desktop/yang/work. Every bash command MUST start with exactly: touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;  Run tools with python3 -I. Build: python3 -I tools/build_graph.py graphs/AmazeFileManager amazefilemanager > graphs/AmazeFileManager/scratch/build_resume_NN.txt 2>&1 (NN = next unused number, starting 02; build_resume_01 exists: methods 2981, REACHABLE 1655, UNREACHABLE 263, UNRESOLVED 1063, errors 2448, warnings 87).
APP SOURCE ROOT (contains '#', always quote): "final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java" (package com.amaze.filemanager). Manifest: "final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml". Framework source: fw_src/android-8.1.0_r1/.
INPUT QUEUE: graphs/AmazeFileManager/scratch/resume_batches/rb_01.txt..rb_30.txt (<=40 fully-qualified short names Class.method per line, first line a # header). Ignore old scratch/batches/.

## HELPER (LABEL step; READ-ONLY producer)
- For every method in the batch file, read the source and label it: REACHABLE (real route from an entry point or from an already-REACHABLE caller; standard configuration: debug APK, API 27, src/main only) emitted as e(...) edges, or UNREACHABLE with one kind from {no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level}, a reason, and a source reference.
- Every claim must carry PRINTED source lines (sed -n), including the if/catch/for conditions around each call. A row without printed lines is rejected.
- Edge KIND tokens must be FULL schema-2 names exactly as existing e() calls in graph_def.py spell them (check the file): FRAMEWORK, EXPLICIT, LIFECYCLE, SYSTEM, INTENT, RESULT, ENTERS, CALL, ASYNC, GUI. Never DIRECT, CONSTRUCTED, ENTRY_POINT, CALLS, FW, UI, or INFERRED as a kind.
- Every e(...) has a non-empty evidence string. If a real citation can't be printed, don't emit the edge; mark the method INCOMPLETE.
- UNREACHABLE entries ONLY as individual assignments: UNREACHABLE['Class.method'] = ('kind', 'reason', 'SRC file.java:lines', 'SOURCE' or 'INFERRED'). NEVER define a separate dict (no UNREACHABLE_PART_x = {...}); NEVER write UNREACHABLE = {} or reassign UNREACHABLE.
- Short Class.method names matching method_list.json 'short'.
- confirmed_by is SOURCE or INFERRED only, never DYN/FW-MEMORY/UNVERIFIED. Tool coverage (coverage_baseline.json, sanity_check.csv, monkey, ape) is never evidence and must not be opened.
- Framework claims only from printed fw_src/android-8.1.0_r1/ lines (FW-SRC path:lines); otherwise INFERRED 'source not read'.
- Library/generated classes (Glide*, Generated*, SevenZ*/Commons Compress, nanohttpd stream servers, etc.) are INFERRED. An UNREACHABLE label for them needs grep -rn output over the app source showing no app call site (paste into graphs/AmazeFileManager/scratch/conflicts.md or the row). If the app calls them, route from the printed app call site. 'The framework calls it at init' with no printed app site is not a reason.
- Many methods belong to partly labeled classes (MainActivity, RecyclerAdapter, MainFragment...). Check graph_def.py first so you add only missing routes, never duplicates.
- Write exactly two files: graphs/AmazeFileManager/parts/resume_<part>.py (e() edges plus individual UNREACHABLE['...'] assignments, no new constants, must pass python3 -m py_compile) and graphs/AmazeFileManager/parts/resume_<part>.md (table: method | label | kind | reason | printed file:lines; first line 'STATUS: RUNNING <HH:MM from date>', rows written as each method finishes, last line 'STATUS: DONE <HH:MM>' or 'STATUS: INCOMPLETE <HH:MM> <method list>').
- Edit nothing else. Never graph_def.py, out/, AGENT_NOTES.md, handoff/, tools/, other apps, other helpers' files. Never run build_graph.py. Do not guess: unsettleable methods are INCOMPLETE.

## MERGE (the SINGLE WRITER; earlier merges failed three ways)
- Process each finished part (STATUS: DONE, or DONE rows of an INCOMPLETE part) ONE AT A TIME.
- Back up graph_def.py first: cp to graphs/AmazeFileManager/scratch/graph_def_before_<part>.py.
- C1 gate: every .py edge and UNREACHABLE entry has a matching .md row and vice versa. Every row cites file:lines; spot-check at least 1 claim in 5 with sed -n against quoted source. Reject unsupported rows and record their methods for requeue.
- Append the part to graph_def.py verbatim as a block headed '# ---- part <part> (<date>)'. INCLUDE ALL ITS REACHABLE e() EDGES. Never skip a REACHABLE edge because its target is not labeled yet (resolves later). Treat an edge as duplicate only if the exact same (src,dst,kind) already exists. Never delete existing edges to reduce errors.
- UNREACHABLE must remain ONE dict. grep -n '^UNREACHABLE *=' must show only the single original definition. Convert any separate dict a helper wrote into individual UNREACHABLE['x'] = assignments. If a method has both a real route and an UNREACHABLE entry, keep the route, drop the UNREACHABLE entry, log in conflicts.md.
- Then python3 -m py_compile graphs/AmazeFileManager/graph_def.py and build.
- REGRESSION CHECK after every part vs previous build: REACHABLE + UNREACHABLE must not fall; UNRESOLVED must not rise. If it does, or py_compile/build breaks, restore that part's backup, log reason in conflicts.md, requeue its methods, move on. Never revert earlier good parts.
- Append one C7 line to AGENT_NOTES.md after each build: time, REACHABLE, UNREACHABLE, UNRESOLVED, errors, warnings, merged part. Keep 'Current step' current.
- Keep a running list of rejected/requeued methods in graphs/AmazeFileManager/scratch/resume_requeue.txt (append, one per line).

## STOP RULES
If a cited source file does not exist, or a rule would have to be broken, write the blocker under '## Blocked' in AGENT_NOTES.md and stop that item; continue others. On any session/usage/rate-limit message: start no new helpers, record the current step in AGENT_NOTES.md, and stop.

## Added by the orchestrator (2026-10-28): flavor-only methods
Some methods in method_list.json have source only in src/fdroid or src/play, not in src/main/java. For example, AboutActivity's methods (found by helper h01).
- Do NOT read src/fdroid or src/play. DATASET.txt names no flavor, and KIRO_CONVERT_APPS section 2.3 allows src/main only.
- Do NOT label these methods REACHABLE, UNREACHABLE, or INFERRED. Mark each one INCOMPLETE with the reason: "source only in flavor folder(s); DATASET.txt names no flavor (section 2.3)".
- Log each one once in scratch/conflicts.md under "Flavor-only methods (open decision for the user)", with the path(s) where its source exists.
- MERGE and EXTRA ROUNDS: do not requeue flavor-only methods. They wait on a user decision, so retrying them is pointless. List them separately in the final report as "open decision: flavor".

## Added by the orchestrator (2026-10-28 22:30): error-growth gate for every merge
Measured state: from build_repair_14 to build_repair_28, unknown-node errors rose from 692 to 973, GUI-edge errors from 77 to 119, bad kind from 5 to 39, bad confirmed_by from 0 to 18, and warnings from 100 to 173. Merged label parts are adding broken edges. From now on, EVERY merge must also pass this gate:
- Compare the build after the part with the build before it. These counts must NOT rise: 'unknown src node', 'unknown dst node', 'GUI edge must', 'bad kind', 'bad confirmed_by', 'missing/invalid evidence', and the 'is UNREACHABLE but has incoming edges' warnings.
- If a count rises, find the new offending lines that the part added and FIX them before keeping the part:
  - canonical node names via scratch/resolve_names.py;
  - kinds from the valid set FRAMEWORK, EXPLICIT, LIFECYCLE, SYSTEM, INTENT, RESULT, ENTERS, CALL, ASYNC, GUI;
  - GUI only for page -> method edges;
  - confirmed_by only SOURCE or INFERRED.
  If a line can't be fixed from the printed source, drop that edge or entry and requeue its method.
- Re-run the gate. Keep the part only when the gate holds AND R+U did not fall.
- Log what you fixed or dropped in scratch/repair_log.md.
