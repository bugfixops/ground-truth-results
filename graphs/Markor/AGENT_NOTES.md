# Markor 2.16.1 - schema 2 conversion: agent notes

Started 2026-10-26 (unattended agent job, brief AGENT_BRIEF_V2.md).

## Current status (2026-10-27, round 8 Limits pass; supersedes the earlier status blocks)
- Final draw logged: make_verification.py runs `python3 -I tools/verify_sample.py Markor 30` itself (seed 20261025) and checks the 30 path rows against that draw. Logged path set = final draw set: 30 of 30; none only logged; none only drawn.
- Sample equality with the final draw re-checked after the cold-start pass: 30 of 30, same order (tools/verify_sample.py Markor 30).
- Path rows: 13 correct, 17 fixed, 0 wrong (the wrong count must be 0: met). Round 8: the logged path list equals the draw (30 of 30, same order). Against the list before round 8, three rows left (SyntaxHighlighterBase.clearAdditional(SpanGroup), TodoWidgetRemoteViewsFactory.getViewTypeCount, WrFilesWidgetFactory.getItemId) and three entered (SyntaxHighlighterBase$SpanGroup.compareTo, TodoWidgetRemoteViewsFactory.getCount, WrFilesWidgetFactory.getLoadingView). Two rows were rewritten and stay in the list: AppSettings.lambda$getPopularDocumentsSorted$1 (todo Info route, 19 steps) and DocumentEditAndViewFragment$2.lambda$search$0 (search guards added; now fixed).
- Cold start (this pass): all 30 routes start S_ENTRY -> ApplicationObject.<init> -> ApplicationObject.onCreate (30 of 30); every activity constructor is followed by onCreate (30 of 30); skip hits 0. The five routes that took MainActivity.<init> -> onResume now run through MainActivity.onCreate (FileSearchEngine.isEncryptedFile, StoragePermissionActivity.processPermissionState, WrFilesWidgetFactory.getCount, TodoWidgetRemoteViewsFactory.getViewTypeCount, MarkorContextUtils.getIntentFile). The direct edges are not kept (graph_def.py:125-134, 478-480). Judgement tags, counted not failed: J_RESUME 1, J_NOTEBOOK 1, J_SHARE 2 (readme_notes.md, Cold start; J_SERVICE was removed).
- Route-level change for the notebook judgement: the notebook is the default startup tab (AppSettings.java:781), and the J_NOTEBOOK note now says so.
- Guards added or confirmed for this pass (graph_def.py, scratch/route_guards.json):
  - ActionButtonBase displayMode guard (`_ABM`, ActionButtonBase.java:305) on the four loop GUI edges and the two S_TODO GUI edges.
  - resolveSystemFilePath edge in the attach dialog: wikitext branch taken (AttachLinkOrFileDialog.java:381); call cite 397.
  - `_LISTENER_GUARDS` table (graph_def.py, 14 keyed listener edges), passed by `_wire_listeners`.
  - MoreInfoFragment -> SettingsActivity.<init>: keyResId == pref_key__more_info__settings (MoreInfoFragment.java:66-67).
  - DocumentActivity.launch -> DocumentActivity.<init>: three early returns (DocumentActivity.java:71-83).
  - DocumentActivity.handleLaunchingIntent -> S_DOCUMENT: five guards, including not (frag != null).
  - ShareInto.<init> FRAMEWORK edge: _savedInstanceState == null (DocumentShareIntoFragment.java:95-97).
  - MainActivity onViewPagerPageSelected edges: _sectionsAdapter != null (MainActivity.java:445-446) and the tab branches (515-520).
  - TextConverterBase.convertMarkupShowInWebView -> CsvTextConverter.convertMarkup: not (_webView == null) (DocumentEditAndViewFragment.java:988-990).
  - SyntaxHighlighterBase.compute and compute@ edges: not (TextUtils.isEmpty(_spannable)) (SyntaxHighlighterBase.java:437-439).
  - Route-level listener guards (this pass): scrollToAndFlash chain pos >= 0 and _layoutManager != null (GsFileBrowserListAdapter.java:628-630); search-files dialog chain early return and isSearchExecuting (MarkorDialogFactory.java:149-153); picker callback sel is not null and isDirectory (DocumentShareIntoFragment.java:469); getFormatted asLink (DocumentShareIntoFragment.java:385); set-password listener API level (MarkorDialogFactory.java:1024).
  - Receiver check (this segment): route_guards.json key GsActivityBase.onToolbarClick|GsFileBrowserFragment.onToolbarClicked|120 now has a second guard, the first visible resumed GsFragmentBase is the notebook fragment (GsActivityBase.java:118-122).
  - Earlier in the pass: four Wikitext route_guards.json keys, _LIFT_SKIP, and the share-into hand edits.
- Build (tools/build_graph.py, round 8): methods 2864, pages 19, edges 6891, REACHABLE 2450, UNREACHABLE 414 (404 no_trigger_in_app, 9 closed_by_configuration, 1 closed_by_api_level), errors 0, warnings 0. verification.csv regenerated (562 rows: label 445 with 397 correct / 48 fixed; edge 87 with 42 / 40 / 5 unclear; path 30 with 13 / 17 / 0 wrong).
- Step-9 checks on Markor (round 8, after the rebuild): check_citations 36 distinct, 0 problems; check_routes 0 flagged; check_bytecode_lines 4352 checked, 0 bad; tools/tests/check_v2.py Markor skipped (schema 2; apps with problems 0); DEAD/FRAMEWORK_ONLY grep on graph_def.py 0.
- Gates: bytecode gate 129 cites, 3 flagged (classified in readme_notes.md Limits); all-kind gate 12 missing items (classified, same list); unconditional-return flags 0. (Carried from the earlier pass; not rerun in round 8.)
- Documents updated: readme_notes.md (How the checked paths were chosen; hazard 1 corrected; Limits), out/README.md (tools/gen_readme_v2.py Markor), LESSONS.md (cold-start and tap bullets added this pass), this status block. out/README.md is regenerated after these notes (see below).
- Open items: hazard 2 (key press) still ungated, no drawn route uses it; the notebook toolbar route runs S_NOTEBOOK before the toolbar tap (GsActivityBase.java:116-124), so the notebook page being on screen at the tap is a stated assumption (hazard 1); FAB edge INFERRED (two routes); share-intent routes need another app; widget provider ENV notes.
- Round 8 (coordinator Limits list): items 1-4 fixed in the graph (info guard, search guards with NEED_PREVIEW, widget service lifecycle nodes, row listener citations); item 5 done in this file (open items above). Accepted limits kept: getStringListOne fragment-view timing, dialog row taps, notebook fragment view created from onCreate, menu order.
- Not done by design: PROGRESS_V2.md not ticked; HANDOFF_V2.md not written; no commits; no helper agents; no Claude Docs or artifacts.
- Remaining step: the final SubagentHandback to the coordinator.

## State (history, written 2026-10-26; out of date, see Current status above)
- DONE: step 0 - moved old schema 1 graph_def.py to generated_draft_graph_def.py.txt; copied show_route_fixed.py from openlauncher; created scratch/.
- Old v1 files kept in place for inventory: out/ (old run), method_list.json (2859 methods, 283 classes), auto_calls.json, coverage_baseline.json, review_notes.md.
- Step in progress: 1 (entry and framework layer of graph_def.py).
  - Section A written (ENTRY launcher -> ApplicationObject / MainActivity, lifecycle, bottom navigation, startup tab, first-visible post).
  - Section B WRITTEN (DocumentActivity from other apps; StoragePermissionActivity; WrMarkorWidgetProvider and TodoWidgetProvider with their RemoteViewsService chains; WrWidgetConfigure with its folder browser; OpenFromShortcutOrWidgetActivity via recent-file shortcut).
  - CLASSIFY written: ENTRY/SYSTEM/INTENT edges to a manifest component <init> (AndroidManifest evidence, not ApplicationObject) -> non_standard with the reason as via. Removed a bad `re` rule (no import in graph_def.py).
  - Section C NOT written yet: MainActivity callbacks (onNewIntent 223, onResume 279, onClickFab 343, newItemCallback 364, onBackPressed 374, onPause 569, onActivityResult 585, onKeyDown 591), every launch site (list below), IntroActivity, SettingsActivity, MoreFragment/MoreInfoFragment, DocumentEditAndViewFragment, file browser, TextSearch, DocumentShareIntoFragment, MarkorDialogFactory, ActionButton classes, MarkorWebViewClient.
- Builder run 2 (A+B, after CLASSIFY fix): methods 2859, pages 16, edges 5950; REACHABLE 405, UNRESOLVED 2454; errors 2462 (2454 "no path", 8 "page not reachable"), warnings 0; NO other error kinds. Output: scratchpad build2.txt; report graphs/Markor/out/build_report.txt.
- Launch sites in app (net/gsantner/markor, grep checked): MarkorContextUtils:126; StoragePermissionActivity:20, 52; IntroActivity:28; DocumentShareIntoFragment:292, 328; MarkorDialogFactory:1057, 1059; DocumentEditAndViewFragment:630; SettingsActivity:371; OpenFromShortcutOrWidgetActivity:19; MarkorWebViewClient:51; DocumentActivity:116, 125; OpenShareIntoActivity:25; OpenEditorActivity:38; MainActivity:120 (debug-looking launch, check guard), 243, 262, 292, 366, 490; ActionButtonBase:716; MoreInfoFragment:67; MarkdownActionButtons:280; WikitextActionButtons:194.
- Not yet grepped: thirdparty (writeily), opoc, and other packages for launch sites.
- The 18 edges without a source line are the INFERRED constants FW_BIND, FW_FRAG, FW_APPINTRO, FW_VIEWPAGER (expected; go in Limits).

## Layout facts (checked)
- Method universe: method_list.json, 2859 methods, 283 classes. Packages: net/gsantner/markor 1705, net/gsantner/opoc 975, other/* (com/vladsch flexmark 69, writeily 26+22+19+13, de/stanetz 24, so/AndroidBug5497Workaround 4+2).
- App module source: /Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app/src/main (548 files, 128 .java).
- Writeily widget sources are under app/thirdparty/java/other/writeily/widget (not under src/main/java).
- Built flavor: flavorAtest (applicationId net.gsantner.markor_test, debug build, testCoverageEnabled). BuildConfig IS_TEST_BUILD = true in atest; IS_GPLAY_BUILD false.
- Manifest lines (checked): application 39-40; MainActivity 61-71; SettingsActivity 73-76; StoragePermissionActivity 78-81; ActionButtonSettingsActivity 83-89; WrWidgetConfigure 91-97; WrMarkorWidgetProvider receiver 99-108; WrFilesWidgetService 110-112; TodoWidgetProvider 114-123; TodoWidgetService 125-127; FileProvider 129-137; OpenEditorTodoActivity 139-151 (disabled); IntroActivity 152-155; OpenEditorQuickNoteActivity 156-168 (disabled); OpenShareIntoActivity 169-181 (disabled); OpenFromShortcutOrWidgetActivity 182-185; DocumentActivity 187 (SEND 195-206, VIEW/EDIT 208-225); AliasDocumentProcessText 1091-1105 (disabled, PROCESS_TEXT); SMSInstrumentedReceiver 1106-1111 (COLLECT_COVERAGE).
- Framework: AOSP 8.1.0_r1 is under work/fw_src/android-8.1.0_r1/core/java/android (line numbers in graph_def.py FW_* constants are from grep this session).
- MainActivity callbacks (checked): onCreate 76; onSaveInstanceState 154; onRestoreInstanceState 171; onNewIntent 223; static launch(Activity,File,boolean) 238; onOptionsItemSelected 259; onCreateOptionsMenu 269; onResume 279; onLongClickFab 322; onClickFab 343; newItemCallback 364; onBackPressed 374; onViewPagerPageSelected 443; ensureRealized 548; restoreFragment 556; onPause 569; onStop 579; onActivityResult 585; onKeyDown 591.
- DocumentActivity (checked): launch(Activity,Intent) 48; launch(...) 55 and private launch 64; launch body startActivity 116; onCreate 135 (StoragePermissionActivity.requestPermissions at 137); onNewIntent 153; handleLaunchingIntent 158; dispatchTouchEvent 258; onActivityResult 285; showShareInto 304; onResume 310; onBackPressed 317; onKeyDown 338.
- IntroActivity (checked): optStart 25 (startActivityForResult at 28, REQ_CODE_APPINTRO 61234); isFirstStart 33; onCreate 39; onSkipPressed 59; onNextPressed 65; onDonePressed 70; onSlideChanged 77.
- StoragePermissionActivity (checked): requestPermissions 18 (startActivity at 20); onActivityFirstTimeVisible 27; askForPermissions 32; processPermissionState 44; onRequestPermissionsResult 64; onActivityResult 70; animateToActivity(MainActivity) at 52.
- OpenEditorActivity onCreate 24; OpenEditorQuickNoteActivity onCreate 17; OpenEditorTodoActivity onCreate 17; OpenShareIntoActivity onCreate 18; OpenFromShortcutOrWidgetActivity onCreate 16 (DocumentActivity.launch(this, getIntent()) at 19).
- GsActivityBase (checked): onCreate 45; onRestoreInstanceState 81; onResume 87; onPostResume 101-108 (posts onActivityFirstTimeVisible); onActivityFirstTimeVisible 113; onToolbarClick 116.

## Last command
- Read graph_def.py (section A) and grep of MainActivity, DocumentActivity, IntroActivity, StoragePermissionActivity and OpenEditor* declarations (line numbers above).
- Next: names.py check for widget, service, receiver and intro node names, then write section B.

## Status (2026-10-26, after section C)
- Section C WRITTEN (graph_def.py, after CLASSIFY): MainActivity pager and fragments, FAB and NewFileDialog, Back and keys, lifecycle, self-restart, launch INTENTs, RESULT edges (intro, settings, SAF picker via GsContextUtils.showMountSdDialog), intro, settings, action-button screen, DocumentActivity and editor, More page.
- Edge wrapper e() records hand edges in _HAND. C6 loop: one FRAMEWORK edge from each bytecode lambda registrar to its body (evidence INFERRED: the listener type is not read per lambda). Builder dedupes REGISTER edges against these hand FRAMEWORK edges (build 5 edge count 6032, checked in out/build_report.txt).
- Citation fixes this session: removed a SAF result edge from DocumentActivity (no caller exists); the SAF caller is GsContextUtils.showMountSdDialog (lambda at 2271); MainActivity.java 391-393 was not verified and was removed; several line ranges narrowed to verified lines.
- Build 5: methods 2859, pages 16, edges 6032, REACHABLE 1694, UNRESOLVED 1165, errors 1165 (all "no path and no UNREACHABLE entry"), warnings 0. UNREACHABLE: none written yet.
- Unresolved split (build 5): no bytecode caller (non-lambda) 552 + 73 init; caller exists but unreached 391 + 56 init; lambdas 91 whose registrar is unreached; 2 clinit.
- Dead-code finding: AppSettings.getRating, getLastEditScrollY, getFileBrowserLastBrowsedFolder, isEditorStartOnBotttom have no call site in src/main (grep). Candidates for no_trigger_in_app after a reference check.
- Next: per class, decide wire (framework callback, layout inflation, listener, adapter, dialog) or UNREACHABLE (no reference in src/main, confirmed by grep), then build until only true UNREACHABLE remain.

## Status (2026-10-27, section E: reachability-driven callbacks)
- Builds 6-7: the evidence prefix must be "INFERRED " (no colon); build_graph counted "INFERRED:" separately.
- Section D1 (static `_INC` skip) replaced by section E in graph_def.py: a search from S_ENTRY (same rule as the builder: no REGISTER edges) runs inside graph_def; each framework or library callback (name in _CB_NAMES, class with an external supertype or an app override) is wired from the bytecode creators of the class and its non-overriding subclasses, only once a creator is reached (fixpoint, <= 60 passes). Menu placeholder methods are wired only when the app text calls the name with a dot (scratch/dotcount.json).
- Build 11 figures: REACHABLE 2166, UNRESOLVED 693, edges 6287, warnings 0. The graph_def run raised NameError twice (missing _CREATORS, then candidate node names from method_list 'short' lack the parameter list for overloads: use AUTO['impl'][simple][name][desc]). LESSON: check for "Traceback" in the build output before reading out/ files, because out/build_report.txt from an earlier build stays on disk.
- Roots now (scratch/status.py): 407 with no non-REGISTER incoming edge (plain 138, ext_ancestor 133, init 73, static 48, private 8, app_override 6, clinit 1); 252 of them have no identifier occurrence in app text beyond declarations; 155 have some.
- Tool gap found: method references (`this::name`, `Class::name`, 29 app files) are not in AUTO['lambdas'] (only lambda$ bodies are), so their targets get no REGISTER edge. To handle with FRAMEWORK edges from the enclosing method (INFERRED), listed by grep.
- Dead chains: SUPPRESS in the builder drops an auto edge when (src, dst) is in the set; to keep the "UNREACHABLE but has incoming edges" warning meaningful, suppress only (src, dst) pairs whose src is UNREACHABLE (not bare names: a bare dst name would hide live callers of a wrongly dead method).
- Still to do: decide the 155 roots with references (interface dispatch of GsPropertyBackend implementations, XML-inflated views and preferences, action-button lists, Fragment and Preference callbacks, method references); then mark the textually dead roots UNREACHABLE (kind, reason, declaration ref, confirmed_by SOURCE); then closure for chains; then verification steps.

## T7 + D1 + D7 (finish run, 2026-11-01, merger session)

- Private tree: graphs/Markor copied from the clone (branch work-2026-10-31, HEAD 6805252 at clone time);
  tools/, handoff/, fw_src/, final_java_only/, work-emulator symlinked read-only. graph_def.py untouched
  (ticked app: logs only). PROGRESS line untouched. verification.csv unchanged by design (see below).
- T7 writer rewrite (graphs/Markor/make_verification.py, portable; old lines 8-13 absolute paths, line 20
  missing methods_before_refs.csv, line 23 unseeded verify_sample call):
  * Root resolved repo-relatively (cwd if it holds tools/ + graphs/, else above graphs/Markor/); G/SCR/APP/FW
    all derived from it. sys.path uses repo tools/.
  * Pre-ref-fix citations seeded once from the current verification.csv FIXED notes into
    graphs/Markor/scratch/methods_before_refs.json (48 entries: the 47 ref_fix keys + onActivityResult;
    keyToStringResId overlaps ref_fix, old ends :215). All old != current refs; all ref_fix news equal
    current methods.csv refs. Same seed pattern as T1. All writer assertions preserved.
  * Sample drawn live with the seed passed explicitly (verify_sample.py Markor 30 20261025). The tool's
    default seed is already 20261025, so the draw is unchanged: verified equal to the current 30 path
    rows, same order, before the rewrite.
  * Cold-start table now written to graphs/Markor/scratch/cold_start_table.txt (31 lines: header + 30).
  * Proof (all printed this session): run 1 output byte-identical to the current verification.csv
    (562 rows: path 13 correct/17 fixed; label 397/48; edge 42/40/5; FW-SRC edges 102, distinct
    citations 34, chain claims 72, ref_fix name check 47 True, cold start 30/30/0, tags J_RESUME 1,
    J_NOTEBOOK 1, J_SHARE 2); run 2 byte-identical to run 1; fresh local build
    (python3 -I tools/build_graph.py graphs/Markor markor: methods 2864, REACHABLE 2450, UNREACHABLE 414,
    errors 0, warnings 0) + writer re-run still byte-identical.
  * Local eight checks (bash handoff/ci/rebuild.sh Markor, private scratch/ci_latest only, never pushed):
    check 2: 0 problems; check 3: 0 flagged; check 4: 0 not-show; checks 5-7: 0/0/0, STRICT line 1;
    check 8: 0 of 414; verification.csv rows: path 30, DEVICE 0. Unreachable kinds: closed_by_api_level 1,
    closed_by_configuration 9, no_trigger_in_app 404. CI acceptance needs the coordinator's
    REBUILD_REQUEST (coordinator-only); local evidence above is the readiness report.
  * No row failed validation, so no scratch/fix_log.md entry was needed.
  * LESSONS.md (8 bullets) and readme_notes.md (five headings in order) reviewed, complete, unchanged.
    scratch/{hier,textcount,dotcount,route_guards}.json kept (graph_def.py reads them).
- D1 (device/routes/Markor/ROUTES.csv, from the device lead's wave-2 helper, verified by the merger):
  30 rows, route_01..30 in verification.csv path order, methods + edges exact, env/state kinds equal to
  out/methods.csv, all 30 scripted (0 unscriptable), fixtures Documents/notes.md, Documents/table.csv,
  Documents/todo.txt all exist under work-emulator/fixtures, route_05 WRITE_EXTERNAL_STORAGE declared
  in the manifest, setup verbatim from ci/apps.csv Markor row, package net.gsantner.markor_test.
  graphs/Markor/scratch/route_print/route_NN.txt (30 prints, generated from methods.csv + trigger JSON)
  staged as the D3 reference. ROUTES_NOTES.md pushed alongside as judgment documentation.
- D7 (DEVICE rows in make_verification.py): if graphs/Markor/device/results.csv exists, one row per
  results row is appended after the edge rows (type=path, result correct iff reached==yes else unclear,
  confirmed_by=DEVICE, ref "device run <run>/<script>", edges from the results row, note = script status
  + ": " + reason for unclear: unscriptable / script failed / not run / not reached). A not-reached route
  never becomes wrong; no label changes. Proof: without the file, output is byte-identical to today's
  (cmp, after the extension); with a synthetic 5-row results file in an isolated copy (reached yes/ok,
  no/ok, no/failed_at_step_4, no/unscriptable, not_run/not_run), exactly the 5 expected DEVICE rows were
  appended and the 562-row prefix was identical. No real graphs/Markor/device/results.csv written.
- D3: 6 helpers fanned out (5 routes each, route_01-05 .. route_26-30), scripts + REPORT.md per helper,
  each script dry-run tested by its helper. Scripts are NOT pushed here: they await the coordinator's
  independent auditor PASS (audit-before-merge rule).

## Current step

- T7 + D1 + D7 complete locally, staged for push under the push lock (push record appended below
  once each push lands). D3 scripts delivered, pending auditor
  PASS, then push + full run_app.sh --dry-run for Markor. F1 readiness for Markor = T7 accepted (local
  evidence above; CI SUMMARY pending coordinator REBUILD_REQUEST) + D1/D3/D7 done (D3 pending audit) +
  D9 CI dry run (coordinator sends DEVICE_DRYRUN_REQUEST at the end). PROGRESS line stays as it is
  (ticked app); F1 state reported to the coordinator, never edited here.

## Decisions made by Muse (for the user and Yang to review)

- T7-D1 (seed source): pre-ref-fix citations come from the current verification.csv FIXED notes, saved
  as graphs/Markor/scratch/methods_before_refs.json (48 entries). Alternative was dropping the old-vs-new
  assertions; rejected, because the assertions still validate the current graph against ref_fix.json.
  Reversal: replace the JSON with any other source of the same 48 old refs; output is unchanged as long
  as old != new and uref == new hold.
- T7-D2 (explicit seed): verify_sample.py is called with seed 20261025 explicitly. No behaviour change
  (the tool defaults to that seed); the explicit argument makes the draw reproducible from the command.
- T7-D3 (cold-start table): written under graphs/Markor/scratch/ instead of the vanished session folder.
  Content identical in form (header + 30 rows).
- D7-D1 (DEVICE row placement): appended after the edge rows, so all 562 existing rows keep their
  positions; without a results file the output is byte-identical. Alternative (after the path rows) was
  rejected to avoid shifting existing rows.
- D1-D1 (notes file): ROUTES_NOTES.md is pushed with ROUTES.csv under device/** as the judgment record
  for the permission/fixture/setup choices. Reversal: delete the notes file; ROUTES.csv stands alone.

## D3 scripts delivered + merger dry run (2026-11-01, merger session)

- All 6 helpers delivered scripts + REPORT.md (d3-01 route_01-05, d3-02 route_06-10, d3-03
  route_11-15, d3-04 route_16-20, d3-05 route_21-25, d3-06 route_26-30). No helper flipped any
  ROUTES.csv row; all 30 rows remain scripted there.
- Merger verification (independent of helper claims): all 30 scripts py_compile OK; a first-
  occurrence edge-id scan of every script matches ROUTES.csv edges exactly, in order, for all 30
  routes; full run_app.sh --dry-run for Markor (stage harness + run_app.sh + drycheck.py +
  route_info.py, ROUTES.csv + all 30 helper scripts, graphs/ + handoff/ + tools/ +
  final_java_only/ symlinked from the private tree, WEMU = work-emulator) prints "Markor: 30
  PASS, 0 FAIL", exit 0. Two early "no manifest found" / missing-trigger-graph failures were
  test-layout gaps (symlinks missing), fixed in the layout, not script defects. Test layout
  removed afterwards; result recorded in the merger report.
- DECISION OWED (coordinator + auditor, not decided here): d3-03 reports step-level
  unscriptable-candidates without changing ROUTES.csv — route_12 launcher-bind edge E48e0024a
  and route_13 launcher-bind edge E27dc1291 (both need a pre-placed widget; placement needs a
  launcher drag the harness cannot express), route_14 camera-return edge Ec0b77f96 (shutter/
  accept UI belongs to the emulator camera app). If pre-placement / operator camera steps count
  as setup, all three rows stay scripted; if they count as part of the route, routes 12/13 (and
  possibly 14) become unscriptable rows (2/30 = 6.7%, or 3/30 = 10% at the cap) and ROUTES.csv
  must be updated before the D3 push. Note the tension: d3-04 route_16 also assumes a pre-placed
  todo widget but was not flagged as a candidate (ROUTES_NOTES route_16 calls it scripted via
  launcher UI automation) — the auditor should rule routes 12/13/16 consistently. D3 scripts are
  NOT pushed until the auditor writes PASS (audit-before-merge rule) and this ruling is made.
- Other auditor notes carried from the helper reports: d3-02/d3-05 scripts also accept --adb
  (run_app.sh live path passes it; contracted args present); d3-01 live-run risks (first-run
  tutorial trap, notebook root vs pushed fixtures, API 30+ permission-dialog wording, share-entry
  permission gate); d3-04 route_16 pre-placed-widget assumption, route_19/20 "More options"
  content-desc, route_20 checkbox toggle; d3-06 fully qualified launch component
  (net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity); d3-05 route_22 ".."
  go-up judgment; d3-03 route_11 9-call E2090721b block.
