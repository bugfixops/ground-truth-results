# Omni-Notes — agent notes (LOCAL MIRROR, stream D overnight run 2026-11-01; NOT pushed, NOT the branch file)

Branch: work-2026-10-31, repo bugfixops/ground-truth-results. All work local under ~/workspace/overnight/stream-D/Omni-Notes/. No pushes. Never write the tick marker.

## 2026-11-01 ~07:19 UTC — setup / reconstruction
- Connector listings: graphs/Omni-Notes holds graph_def.py (286778 B), method_list.json (307758 B, 1456 methods), auto_calls.json (677830 B, 1795 calls), coverage_baseline.json (278583 B), verification.csv (196534 B, 370 rows: 288 label, 49 edge, 33 path), readme_notes.md (14208 B, five headings), out/ (README.md, build_report.txt, methods.csv, trigger_graph.html, trigger_graph.json, sanity_check.csv).
- tools/ listing: build_graph.py, verify_sample.py, check_citations.py, check_routes.py, check_bytecode_lines.py, scan_unreachable.py, gen_readme_v2.py present. make_verification.py NOT in tools/ root; tools_dev/ holds only DESIGN.md/design_review files. Scoped code search for make_verification in this repo: 0 hits, incomplete_results=true (not proof of absence elsewhere, but no locatable copy).
- Fetch method: GitHub connector, one file at a time, ~30 s pauses, raw MCP JSON to /tmp/omni_fetch/, decoded locally. One false stop: first bulk script grepped for "429" and graph_def.py legitimately contains "429" twice as numbers; fixed to check ok:false only. No 429 hit on any fetch so far.
- Java 21.0.12.1 available (java/javac).

## 2026-11-01 ~07:30 UTC — step 1: build (PASS)
- Command (from ~/workspace/overnight/stream-D/Omni-Notes/): python3 -I tools/build_graph.py graphs/Omni-Notes omni-notes
- Exit 0. Printed: methods 1456, pages 68, edges 3803; REACHABLE 1202, UNREACHABLE 254 (no_trigger_in_app 194, framework_never_calls 34, closed_by_configuration 21, branch_never_taken 5); errors 0, warnings 0; STRICT=True (graph_def.py:2422); UNRESOLVED 0 (methods.csv recount).
- Local out/build_report.txt is byte-identical to branch out/build_report.txt; methods.csv/json/sanity_check.csv sizes match branch exactly. Handover count 1456 CONFIRMED by own build.
- Viewer HTML not regenerated locally (tools/viewer_template.html not fetched; build skips HTML when template absent) — presentation artifact only, not a label check.
- Output saved: scratch/build_omni-notes.txt (+ .err, empty).

## 2026-11-01 ~07:32 UTC — step 2: sample drawn
- Command: python3 -I tools/verify_sample.py Omni-Notes 30 20261025 > scratch/sample_30.txt
- 30 of 1202 reachable methods, 267 distinct edges on their routes (seed 20261025).
- Overlap with branch verification.csv path rows: 19 of 30 already path-checked; 11 never path-checked (SqlParser.removeComments, NotificationsHelper.updateMessage, NotificationsHelper.show, StorageHelper.getMimeTypeInternal, SnoozeActivity.updateNoteReminder, ListRemoteViewsFactory.color, PermissionsHelper.lambda$requestPermissionExecute$1, StorageHelper.createAttachmentFromUri, DetailFragment$3.onClick, IntroActivity.mustRun, OmniNotes.enableStrictMode).
- All 30 routes printed step by step: scratch/sample_30_routes.txt (526 steps).
- Next: fetch app sources cited on the routes + fw_src files cited, then judge each route step by step.

## 2026-11-01 ~07:53 UTC — restart + re-fetch plan
- Runtime restarted ~07:52 UTC; /tmp wiped. Workspace intact (build, sample, routes, digest, greps, checks, 28 decoded app sources). Big fetch dead at ~33/67. Re-fetching remaining 39 files via scratch/fetch_big2.sh (raw JSON to scratch/raw/, decoded immediately per file into final_java_only/ or fw_src/ trees).
- Java lost in restart (command not found); TOOLS.md warned apt installs may not survive a VM replacement. No remaining step strictly needs javac; reinstall attempt pending, recorded as missing until then.

## 2026-11-01 ~08:05-08:20 UTC — fetch 2 done, route verification, checker first runs
- fetch_big2.sh: 39/39 OK, all main path (4 res XMLs, 13 fw files, branch AGENT_NOTES.md). No 429, no FAIL.
- Branch root AGENT_NOTES.md fetched as scratch/branch_AGENT_NOTES.md turns out to be AmazeFileManager's notes, not Omni-Notes' — no Omni-Notes branch notes existed to mirror; local AGENT_NOTES.md (this file) stays the Omni-Notes mirror.
- Gap fetch: ConstantsBase OK (SWIPE_MARGIN=30, SWIPE_OFFSET=100 — exact match to the onLocationUnavailable route guard); SketchFragment OK (save(): getBitmap() :209, sketchUri set :219 — confirms sketch-route guard + link). IntroActivity FAILED on root path (file does not exist there); method_list.json gives package intro/ — correct path queued in fetch3.
- Route verification (fresh printed reads this session): cold-start trunk, all PLAIN routes, RecurrenceHelper, Snooze/updateNoteReminder, service routes, DbHelper chains, NoteLoader/EventBus, drawer/menu, location/geocoder, widget/sketch/count, Fab, manifest/menu XMLs, ListFragment CAB/merge/filter/delete flows, DetailFragment menu/attachment/location/sketch/save/merge/categorize blocks, SettingsFragment wiring, NavigationDrawerFragment drawer step, CategoryMenuTask long-press, CategoryActivity save/delete, MainActivity.onBackPressed branches, updateNavigation chain, all 5 sample FW-SRC steps (IntentService, AppWidgetProvider, SQLiteOpenHelper, AsyncTask, Parcel — Parcel cited ranges match fetched file exactly: writeParcelable :1785-1791, readParcelableCreator :2867-2900).
- DbHelper.deleteNote(long,boolean) judged WRONG on fresh evidence: mergedNotesIds set only from "merged_notes" intent extra (DetailFragment.java:508; put by ListFragment.java:1755 in the Merge flow); FAB-created new note never sets it, so FAB steps 9-11 + merged-note STATE at step 18 are mutually exclusive. Label REACHABLE still right (real Merge path exists); this drawn route is inconsistent. No local graph fix attempted (documented limitation; branch readme "Limits" agrees).
- Tag$1 / Attachment$1 clinit steps: modelling convention (first use triggers class init; CREATOR anon class instantiated in static init — Tag.java:65, Attachment.java:85); reachability holds; judged correct with a written note, not errors.
- check_citations.py first run: exit 1, 18 distinct, 1 problem (AdapterView.java not held). 0 FW-MEMORY/DYN/UNVERIFIED evidence.
- check_bytecode_lines.py first run: exit 1, 1084 checked, 114 skipped, 32 implicit, 297 bad — ALL 297 are "file not found" for 10 unheld app files; ZERO genuine line mismatches among held files.
- fetch3 launched (12 files): intro/IntroActivity.java + 10 bytecode-missing app files + fw AdapterView.java; re-run both checkers after for clean 0s.
- Checks already passed: (1) build 0/0/no STALE/STRICT=True; (3) check_routes 0 flagged; (8-callers) scan_unreachable --callers 5/254, each explained in its reason. Greps: FW-MEMORY 0, PENDING 0, DYN 0, DEAD|FRAMEWORK_ONLY literal 11 = conversion mechanism only (dicts reset to {} at graph_def.py:2145; build verdict kinds contain no 'unclassified').

## 2026-11-01 ~08:25-08:35 UTC — checker re-runs, miscount corrected, fetch4
- check_citations re-run: exit 0, 18 distinct, 0 problems. CHECK (2) PASSES.
- check_routes re-run: exit 0, 0 flagged. CHECK (3) PASSES.
- scan --callers re-run: exit 0, 5/254, same explained callers. CHECK (8-callers) PASSES.
- check_bytecode_lines re-run: exit 1, 1165 checked, 216 bad. CORRECTION: the earlier "10 missing files" was counted from the capped 60-line output, not the full --all output. Full --all output: all 216 bad are "file not found" across 45 distinct basenames, ZERO genuine line mismatches. fetch4 launched for all 45 + DATASET.txt; re-run check (4) after.
- Judgment file written (scratch/sample_30_judgment.md): 29 correct / 0 fixed / 1 wrong / 0 unclear; error rate 1/30 = 0.0333. Redrawn sample byte-identical to original (no fixes).
- DECISIONS.md (D1-D11), LESSONS.md (7 bullets) written. gen_readme exit 0 (local out/README.md 19,377 B; re-run pending after DATASET fetch).
- Remaining to close: fetch4 completion, check_bytecode_lines clean re-run, gen_readme re-run, RUN_LOG/AGENT_NOTES close-out, final report. Still BLOCKED (not gate-blocking, just pending): verification.csv regeneration (make_verification.py not locatable); scan --all not runnable without full tree; one documented wrong route (parent decides if it blocks the gate).

## 2026-11-01 ~08:47 UTC — close-out
- fetch4: 46/46 OK (45 app files + DATASET.txt), zero FAILs. Reconstructed total: 108 app .java files + manifest + 5 res XMLs + 14 fw files + DATASET.txt.
- check_bytecode_lines final: exit 0, 1381 checked, 0 bad (default and --all). CHECK (4) PASSES.
- gen_readme re-run with DATASET: local out/README.md 19,475 B, BYTE-IDENTICAL to branch out/README.md (fetched and diffed).
- Eight checks final: (1) PASS, (2) PASS, (3) PASS, (4) PASS, (5) literal 11/effective 0 (D1), (6) 0 PASS, (7) 0 PASS, (8-callers) PASS 5/254 explained, (8-all) NOT RUN (D7).
- Sample final: 29 correct / 0 fixed / 1 wrong / 0 unclear; error rate 0.0333; redraw identical.
- Gate: NOT fully reached — labels PASS; route checks 29/30 with 1 documented wrong route (parent decides, D3); logs complete except verification.csv regeneration blocked (make_verification.py not locatable, D2). Nothing pushed; no branch file edited; no device work.
