# hash-checker — local mirror AGENT_NOTES (Stream D, overnight, NO PUSH)
Branch work-2026-10-31, repo bugfixops/ground-truth-results. All work local only.

## Step 1 — build (2026-11-01 ~07:25 UTC local)
Command: python3 -I tools/build_graph.py graphs/hash-checker hash-checker
Output saved: scratch/build_1.txt. methods 529, edges 1314, REACHABLE 507, UNREACHABLE 22
(closed_by_configuration 3, framework_never_calls 3, no_trigger_in_app 16), errors 0, warnings 0.
STRICT=True set in graph_def.py (line 791); build printed no STALE line and no UNRESOLVED line.
Labels confirmed: SOURCE 76, INFERRED 453. verification path rows 37, errors found 13 (rate 0.351, historical).

## Step 2 — route sample drawn (2026-11-01 ~07:30 UTC local)
Command: python3 -I tools/verify_sample.py hash-checker 30 20261025 > scratch/sample_30.txt
Sample: 30 of 507 reachable, 213 distinct edges (seed 20261025). Strata: NONSTD 4, INFERRED 4, STATE 3, ENV 6, LONG 6, PLAIN 7.
Full step dump (edges, triggers, guards, evidence; source snippets pending source fetch): scratch/routes_30_steps.txt (2599 lines).
Worksheet: scratch/routes_worksheet.txt. Source fetch loop running in background (36 files, 30 s pauses): scratch/fetch_sources.log.

## Step 3 — eight checks, partial (2026-11-01 ~07:35 UTC local)
(3) check_routes.py: 0 routes flagged -> scratch/check_routes.txt.
(5)-(7) greps on local graph_def.py: FW-MEMORY 0. DEAD|FRAMEWORK_ONLY hits = legacy dict definitions (lines 63, 79) + conversion code (684-706) that build_graph reads as UNREACHABLE and then clears; built JSON has no DEAD/FRAMEWORK_ONLY keys, 22 UNREACHABLE in labels. PENDING hits = only the S_MAIN_EXIT_PENDING screen name (4 occurrences in JSON), not a pending status. These are explained, not hidden; see DECISIONS.md.
Remaining checks (1) build done above; (2) check_citations, (4) check_bytecode_lines, (8) scan_unreachable need source/fw_src mirrors — pending fetch loop.

## Step 2 — route judgments complete (2026-11-01, after source fetch)
Sample redrawn (scratch/sample_30.txt) = branch final 30, 213 distinct edges. Every step printed: scratch/routes_30_with_source.txt (4149 lines, all app sources freshly fetched via connector; only FW AsyncTask snippets missing pending fw_src).
Judgment, per method (all steps read against freshly printed source; CALL citations range-aware checked: 211 ok, 2 explained App$1 javac attribution/$-vs-dot, 3 Dagger non-standard verified at inject() lines):
HistoryItem.<init>() correct; DatabaseHelperModule.databaseHelper correct; LangHelperModule.langHelper correct; ThemeHelperModule.themeHelper correct; Blake2B.littleEndianToInt correct; FNV1a.update256 correct; WebFragment.getMenuResId correct; JdkHashCalculator.inputStreamsFormFolder correct; HistoryFragment.refreshHistory correct; OrmLiteLocalDataStorage.getDatabaseFileName correct; HashCalculatorFragment.writeHashToFile correct; MainActivity.getConfiguredBundleWithDataUri correct; Clipboard.clear correct; Blake2B.update correct; SettingsFragment.copyFile correct; HashCalculatorTask.<init> correct; HashCalculatorFragment.folderNameFromUri correct; FeedbackFragment.sendEmail correct; SharedPreferencesSettings.saveTheme correct; AppSnackbar.lambda$show$0 correct; HashType.getTitle correct; Language.getPrimaryIconResId correct; Action.getAdditionalIconResId correct; SharedPreferencesSettings.saveStringPreference correct; App.getShortcut correct; SharedPreferencesSettings.getStringPreference correct; SharedPreferencesSettings.getLanguage correct; SharedPreferencesSettings.containsPreference correct; SharedPreferencesSettings$SharedPreferencesSettingsKeyExtractor.<init> correct; SharedPreferencesSettings.getBooleanPreference correct.
Result: correct 30, fixed 0, wrong 0, unclear 0. Error rate = (0+0)/(30+0+0) = 0. No graph change; final sample = same sample (scratch/sample_30.txt). Branch historical 8 fixed / 0.351 over 37 rows are NOT counted here (fixes already in graph_def.py; see DECISIONS.md D3).

## Step 3 — eight checks, continued
(4) check_bytecode_lines.py re-run after fetching the 15 missing cited files: see scratch/check_bytecode_lines.txt (first run: 73 "bad" were all "(file not found)" for files outside the sample mirror, none on sample routes).
(8) scan_unreachable.py --callers: 4 of 22 UNREACHABLE have a bytecode caller outside the set, all explained in graph_def.py (BaseFragment virtual-override pair; getThemeAnalogue + setRefreshSelectedFileStatus SUPPRESSed closed_by_configuration) -> scratch/scan_callers.txt. --all pending full source mirror (see below).

## Step 3 — eight checks, continued (2)
(2) check_citations.py: exit 1, 15 distinct citations, 1 problem, FW-MEMORY/DYN/UNVERIFIED 0 -> scratch/check_citations.txt. The single problem is NOT a graph error: services/.../ActivityManagerService.java (1,086,106 bytes on branch) exceeds the connector display limit, so the connector returned a placeholder instead of the file; the App.onTerminate AMS citations (6919-6936, 23336-23340) could not be re-verified from this VM. The other 14 citations verify (file exists, cited lines in range), including ActivityThread.java (6502 lines) for the EXIT_APPLICATION side of onTerminate. The placeholder file was deleted from the local mirror, not kept. No token URL from the connector message was used or copied anywhere.
(4) check_bytecode_lines.py (re-run): exit 0, 548 checked, 32 skipped, 90 implicit, 0 bad -> scratch/check_bytecode_lines.txt.
(8) scan --callers done (4 explained); --all pending full java mirror: 74 outer classes, 45 fetched, 29-file fetch loop running (scratch/fetch_alljava.log). MainActivity main-path guess will fail by design (flavor file already fetched); DaggerAppComponent is generated code and is expected to be absent from src/main.

## Step 3 — eight checks, final
(1) build_graph.py: PASS — 529 methods, 1314 edges, REACHABLE 507, UNREACHABLE 22, errors 0, warnings 0, STRICT=True in graph_def.py, UNRESOLVED 0 (507+22=529), STALE 0 (path status SOURCE_OK 37, UNCHECKED 470, no STALE). scratch/build_1.txt.
(2) check_citations.py: 14/15 — exit 1 only for ActivityManagerService.java (1,086,106 bytes, over connector display limit; AMS lines 6919-6936, 23336-23340 unverified by Muse). FW-MEMORY/DYN/UNVERIFIED 0. scratch/check_citations.txt. See DECISIONS.md D5.
(3) check_routes.py: PASS — 0 routes flagged. scratch/check_routes.txt.
(4) check_bytecode_lines.py: PASS — exit 0, 548 checked, 32 skipped, 90 implicit, 0 bad. scratch/check_bytecode_lines.txt.
(5)-(7) greps on graph_def.py: FW-MEMORY 0. DEAD|FRAMEWORK_ONLY hits are legacy dict definitions + conversion code (build clears them; JSON has neither key). PENDING hits are only the S_MAIN_EXIT_PENDING screen name. Explained in DECISIONS.md D2.
(8) scan_unreachable.py --all: RUN over complete main+thirdPartyStores java mirror (73 files) + layout/menu/xml (16 files). All 22 UNREACHABLE triaged, none contradicted: 14 no other mention; 8 with mentions all explained (same-name equals calls; overrides + virtual dispatch for the BaseFragment pair; sole caller App.onTerminate itself unreachable for releaseHelper; suppressed closed_by_configuration branches for getThemeAnalogue and setRefreshSelectedFileStatus, verified at HCF:573-582 and SharedPreferencesSettings:116-139). scratch/scan_all.txt. --callers: 4 flagged, all explained (same two pairs). scratch/scan_callers.txt.

## Step 4 — logs, final
verification.csv: branch file preserved VERBATIM in local mirror (regeneration via make_verification.py BLOCKED — tool absent on branch, DECISIONS.md D1). Validated: header exactly type,item,result,confirmed_by,ref,edges,note; 124 rows (label 50 correct/2 fixed, edge 9/26, path 24/13); confirmed_by only SOURCE (99) / INFERRED (25); no DYN/FW-MEMORY/UNVERIFIED/DEVICE. Build verification counts match (label rate 0.038, edge 0.743, path 0.351 — historical, pre-existing rows).
readme_notes.md: branch file preserved verbatim; five headings in order (What the re-audit changed / How the checked paths were chosen / What waits for a device (API 27) / Hazard candidates / Limits). gen_readme_v2.py ran exit 0, wrote graphs/hash-checker/out/README.md with numbers from files.
LESSONS.md: 7 bullets. AGENT_NOTES.md: this file, updated after every step. DECISIONS.md: D1-D6.
No pushes, no branch edits, no tick marks written anywhere. No device checks performed (no emulator/adb/APKs/new repos).
