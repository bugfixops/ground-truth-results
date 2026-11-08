# Diary — Stream D leaf notes (LOCAL MIRROR, not a branch file)

Branch work-2026-10-31, repo bugfixops/ground-truth-results. NO PUSHES. No branch file edited. Never write the tick marker.

## Step 1 — reconstruct + build
- Fetched via GitHub connector, one file at a time with ~30 s pauses: graphs/Diary/graph_def.py (187,523 chars, 1,711 lines), graphs/Diary/method_list.json (286 methods — matches handover count, re-verified, not trusted), graphs/Diary/verification.csv (128 rows + header), tools/build_graph.py, verify_sample.py, check_citations.py, check_routes.py, check_bytecode_lines.py, scan_unreachable.py, gen_readme_v2.py, show_route.py.
- tools/make_verification.py does NOT exist on the branch (get_file_contents: path does not exist). No verification.csv regeneration was attempted; the branch verification.csv is used unchanged. See DECISIONS.md.
- Command run: `python3 -I tools/build_graph.py graphs/Diary diary` (from ~/workspace/overnight/stream-D/Diary)
- Printed: methods 286, pages 34, edges 1435; verdicts REACHABLE 265, UNREACHABLE 21 (framework_never_calls 4, no_trigger_in_app 17); errors 0, warnings 0; STRICT = True (graph_def.py:1711); no STALE / UNRESOLVED strings in build output or build_report.txt.
- Labels confirmed by: SOURCE 257, INFERRED 29. Evidence: SRC 1028, FW-SRC 387, INFERRED 20 (edge evidence tokens: SRC 1368, FW-SRC 405, INFERRED 52 — counting differs because one edge can carry several citations).
- Build verification block: label checked 51, errors 7 (rate 0.137); edge checked 37, errors 0, unclear 10; path checked 25, errors 7 (rate 0.28), unclear 5; path status SOURCE_OK 25, UNCHECKED 240.

## Step 2 — route checks (sample 30, seed 20261025)
- Command: `python3 -I tools/verify_sample.py Diary 30 20261025 > scratch/sample_30.txt`
- Sample: 30 of 265 reachable methods, 195 distinct edges. Every step of all 30 routes printed in scratch/route_steps.txt (370 steps total).
- Every stored path row in verification.csv matches the current derived route edge-for-edge (30/30, edge lists identical), so the branch path judgments transfer to the current build unchanged.
- Judgments: correct 18, fixed 7, wrong 0, unclear 5. Error rate = (7+0)/(18+7+0) = 0.28.
- Fresh spot-check (this session, upstream source at pinned commit 07bb05c3b7a8ea90db5efdc8f574b9f334402a71, fetched via connector): Diary.java:305-306 (sortFiles comparator), 314-315 (listYears filter), 2819-2844 (addLink dialog lambda), 3186-3188 (alertDialog call in ZipTask catch) and FileUtils.java:633 (getFile calls isLocal) all match the cited lines exactly. The 5 unclear routes stay unclear only because their last step rests on picker-app / libcore / java.io behaviour not read — that is the INFERRED confirmed_by, not a route error. No route fix was needed; the redrawn sample is identical to scratch/sample_30.txt (deterministic seed), so no new sample file was invented.
- Fixed routes (7) were already fixed in graph_def.py on the branch (e.g. widget routes carry STATE session gates; see verification.csv notes).

## Step 3 — eight checks (outputs in scratch/)
1. build_graph.py: PASS — 0 errors, 0 warnings, no STALE, STRICT=True.
2. check_citations.py: first run 81 distinct citations, 81 "file not held" problems, 0 line-range problems, 0 FW-MEMORY/DYN/UNVERIFIED evidence (no fw_src cache locally — not 81 citation errors). After fetching 32 of the 33 distinct cited framework files from aosp-mirror/platform_frameworks_base at android-8.1.0_r1 into fw_src/android-8.1.0_r1/: final run 81 distinct, 1 problem, 0 line-range errors. The 1 remaining problem is services/core/java/com/android/server/am/ActivityManagerService.java:19198-19224 (cited by 4 widget edges, same citation): the file cannot be fetched via the connector — both aosp-mirror and android mirrors return "failed to inspect repository file: Invalid object requested. SHA must identify a commit or a tree" — while BroadcastQueue.java and ActivityStarter.java from the same tree fetched fine, so this is a file-specific connector limit, not a citation error. Check (2) is therefore NEAR-PASS with 1 file-not-held blocker, NOT 0; no line-range error was found in any of the 80 checkable citations.
3. check_routes.py: PASS — 0 routes flagged.
4. check_bytecode_lines.py: PASS (vacuous) — 0 bad; 0 bytecode-cited edges checked, 0 skipped, 0 implicit. Consistent with auto edges 0/1435: Diary has no "(bytecode)" citations to check.
5. grep DEAD|FRAMEWORK_ONLY on graph_def.py: 0 PASS.
6. grep FW-MEMORY on graph_def.py: 0 PASS.
7. grep PENDING on graph_def.py: 0 PASS.
8. scan_unreachable.py --all: first run VACUOUS (no final_java_only source tree locally, so every method showed "no other mention" with no files searched — that output is not evidence). --callers: no auto_calls.json, tool reports "no bytecode edges to compare" — not applicable, not a label failure. Remediation in progress: fetching the 11 app source files + AndroidManifest.xml + 4 res xml files from billthefarmer/diary at the pinned commit into final_java_only/Diary/app/diary-src/ and re-running --all.

## Step 4 — logs (in progress)
- verification.csv: branch file kept unchanged (see make_verification.py note above); header is exactly type,item,result,confirmed_by,ref,edges,note.
- readme_notes.md / gen_readme_v2.py: pending branch readme_notes.md fetch after the framework fetch loop finishes (connector discipline: one fetch at a time).
- LESSONS.md, DECISIONS.md: drafts in this folder, to be finalised after checks 2 and 8 re-run.

## Step 5 — takeover re-verification (2026-11-01, after runtime restart drain)
- Re-ran from ~/workspace/overnight/stream-D/Diary: build (scratch/build_takeover.txt, byte-identical to build.txt), verify_sample Diary 30 20261025 (scratch/sample_30_takeover.txt, identical to sample_30.txt and to sample_30_redraw.txt — redraw verified, no route was fixed after the last fix, so no new sample needed), check_routes (0 flagged), check_bytecode_lines (0 checked, 0 bad, vacuous), check_citations (81 distinct, 1 problem = AMS file-not-held, 0 line-range, 0 unbacked; exit 1), py_compile on all tools + graph_def.py (OK).
- Greps re-run: FW-MEMORY 0, PENDING 0, UNRESOLVED/STALE 0. DEAD/FRAMEWORK_ONLY hits are only the graph's own mechanism (dicts defined :199/:228, comment :1608, conversion loop :1624, cleared :1629) — no leftover labels.
- Verification cross-checks (local, scripted): path rows 30 = redrawn sample in order and set; judgments match 30/30 (0 mismatches); label rows 51 (44 correct, 7 fixed) with confirmed_by matching the trigger-graph JSON 51/51; all 128 rows confirmed_by SOURCE or INFERRED only; JSON verdicts 265/21 match build.
- App source fetch completed: QueryHandler.java + Editor, DiaryWidgetProvider, SettingsFragment, FileProvider (support lib), AndroidManifest.xml, preferences.xml, widget.xml, filepaths.xml — 9 files via GitHub connector, one at a time with 30 s pauses, no 429 encountered. Tree now complete: all 11 java files covering all 20 method-list classes, plus manifest + 4 res xmls.
- Genuine scan_unreachable --all (scratch/scan_unreachable_final.txt): all 21 methods triaged (see DECISIONS.md D8); no label change. --callers still n/a: graphs/Diary/auto_calls.json does not exist on the branch copy (no bytecode edges to compare) — not a label failure.
- Branch re-checks via connector (2026-11-01): tools/make_verification.py still does not exist on work-2026-10-31 (confirmed fresh); final_java_only/Diary/app/DATASET.txt fetched (target_sdk 28 confirmed, source_commit 07bb05c3b7a8ea90db5efdc8f574b9f334402a71, sha256 da194494...); graphs/Diary/out/sanity_check.csv fetched (286 rows, 187 ran, 0 UNREACHABLE-but-ran, 1 ENV_GATED_BUT_HIT: Diary.readAssetFile).
- Logs finished locally: graphs/Diary/readme_notes.md written with the five headings in order; gen_readme_v2.py Diary ran clean (graphs/Diary/out/README.md, 90 lines, all numbers from files, sanity 187 ran / 0 UNREACHABLE); verification.csv kept unchanged (header exactly type,item,result,confirmed_by,ref,edges,note, 128 rows) because make_verification.py does not exist; LESSONS.md now 8 bullets; DECISIONS.md D8-D10 added.
- Gate: BLOCKED on two external items only — (1) check_citations exit 1 on the single AMS file-not-held (D7/D9), (2) verification.csv cannot be regenerated via the missing make_verification.py (D1). Everything else passes. No pushes, no branch edits, no device checks.

## Observations (not label changes)
- final_java_only/Diary/app/DATASET.txt says target_sdk 28, while graph_def.py header says the baseline target API level is 27 (fw_src android-8.1.0_r1). Recorded, not changed: labels and citations were built against the 8.1 source the graph cites.
