# LibreTorrent batch 107 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 107 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-107 proposal
  (`~/workspace/libretorrent-batch107-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-checked against source freshly printed in this pass (see below),
  and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 107 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-107 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence),
in plan order. Method names and JVM descriptors in the table below match the plan row for row.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b107-108-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/` unless noted):

- `ui/main/MainActivity.java` — SHA `b98a504934ed4480…`, 811 lines. Trunk only:
  log-menu branch :754-755 → `showLog()` :801-803 → `startActivity(LogActivity)`.
- `ui/log/LogActivity.java` — SHA `d91948db981d67d0…`, 470 lines. Key sites verified fresh:
  `ViewModelProvider.get(LogViewModel.class)` :92; `observeLog` :119; `pauseLog` :125/:135/:299;
  `pauseLogManually` :268; `resumeLogManually` :270; `resumeLog` wrapper :275-278 (calls
  `viewModel.resumeLog()` :278); `logPausedManually` :209/:266/:285; `logRecording` :219/:283;
  `startLogRecording` :294; `stopLogRecording` :330; `getSaveLogFileName` :311;
  `saveLog` :327; `getLogEntriesCount` :445; `copyLogEntryToClipboard` :463;
  `showFilterDialog` :250-256 (`SessionLogFilterDialog.newInstance()` :254, `show` :255);
  `showLogSettings` :259-261 (`startActivity(LogSettingsActivity)` :261).
- `ui/log/LogViewModel.java` — SHA `eb78f0d42e4fa0a2…`, 227 lines (byte-identical to the
  local copy in `~/workspace/batch20_21/src/`; the prior proposal's "221 lines" was a miscount,
  not a line shift — method line numbers below agree with the fresh file).
  `LogSourceFactory` construction :75; `initMutableParams` :77; `initMutableParams` body :80-90
  (registers `paramsCallback` :89); `observeLog` :92-96; `onCleared` :100-105;
  `paramsCallback` field :107-110; `pauseLog` :140-143; `pauseLogManually` :145-149;
  `resumeLog` :151-154; `resumeLogManually` :156-160; `getLogEntriesCount` :162-165;
  `logPausedManually` :167-170; `startLogRecording` :172-177; `stopLogRecording` :179-184;
  `logRecording` :186-189; `getSaveLogFileName` :191-197; `saveLog` :199-213;
  `copyLogEntryToClipboard` :215-228.
- `ui/log/LogSettingsActivity.java` — SHA `e4f48757fa25b8ac…`, 51 lines, printed in full fresh:
  static `TAG` :32; `onCreate` :37-50 (`setContentView` :42, toolbar :44-49,
  navigation lambda :47 `(v) -> finish()`).
- `ui/log/LogSettingsFragment.java` — SHA `7cceab74df1851be…`, 101 lines, printed in full fresh
  (byte-identical to the local copy): static `TAG` :39; `onCreate` :52-74 (maxFilter :59-64,
  `setOnBindEditTextListener` :70, `bindOnPreferenceChangeListener` :73);
  `onCreatePreferences` :78-81; `bindOnPreferenceChangeListener` :83-86;
  `onPreferenceChange` :89-101.
- `ui/log/LogSourceFactory.java` — SHA `1b2c489938463a23…`, 43 lines, printed in full fresh:
  `<init>` :32-35; `create()` :39-42 returning `new LogDataSource(logger)`.
- `ui/log/SessionLogFilterDialog.java` — SHA `54f31c23062f5352…`, 120 lines, printed in full fresh:
  static `TAG` :42; `newInstance` :49-57 (`new SessionLogFilterDialog()` :51);
  `onAttach` :60-66; `onResume` :69-86 (back-key listener :74, calls `onBackPressed` :79);
  `onCreateDialog` :90-104 (`ViewModelProvider` :95, binding inflate :98-99,
  `initLayoutView` :101); `initLayoutView` :106-114 (negative button :110);
  `onBackPressed` :116-119.
- `src/main/AndroidManifest.xml` — SHA `b011d74750a72c16…`, 295 lines. MainActivity declared :43
  with MAIN :53 / LAUNCHER :54; LogActivity declared :239; LogSettingsActivity declared :242.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence anywhere in this file.

## Trunk (printed)

MainActivity log-menu :754-755 → `showLog()` :801-803 → LogActivity → LogActivity.onCreate :92
`ViewModelProvider.get(LogViewModel.class)` → LogViewModel.`<init>`. LogActivity menu →
`showLogSettings()` :259-261 → LogSettingsActivity; LogActivity menu → `showFilterDialog()`
:250-256 → SessionLogFilterDialog.

## Conventions recorded, not decided

- `confirmed_by` in this file is per-row: SOURCE = a printed direct in-app call site naming
  the method (including a printed listener/field body that calls it, and, for row 30,
  the printed field initializer in LogViewModel :107-110 executed on LogViewModel construction,
  itself SOURCE-anchored at LogActivity :92); INFERRED = reached only through unprinted
  framework/library dispatch (activity/fragment lifecycle, DialogFragment lifecycle,
  preference-change dispatch, Rx/databinding dispatch, JVM class initialisation) where the
  registration, show, or entry site is printed. Labels are unaffected; only `confirmed_by`
  would change at merge under a whole-route INFERRED convention.
- **Fragment-attach caveat (rows 5, 6, 9, 10, and, by dispatch, 8, 11):** LogSettingsActivity
  sets `activity_log_settings` as content view (:42), but the step attaching LogSettingsFragment
  to that activity (layout fragment declaration / transaction) was NOT printed in this session.
  The fragment lifecycle rows are therefore INFERRED for the framework dispatch step, with the
  in-app registration/activity-start sites printed. Under a strict rule requiring a printed
  attach step, those rows revert to OPEN — the merger must pick one strict-entry/attach
  convention for all batches. This caveat does not change any label below.
- Lambda numbering is by source order / registration order, not bytecode-verified; labels
  are unaffected by any numbering swap within a group.

## Row verdicts (plan order)

| # | Method | Verdict | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | LogSettingsActivity.<clinit> | REACHABLE proposed | INFERRED | Class load when LogActivity.showLogSettings :261 starts the activity; static TAG :32 runs at class init. JVM step not printed. |
| 2 | LogSettingsActivity.<init> | REACHABLE proposed | INFERRED | Implicit default constructor; framework instantiates the activity after the :261 intent. Framework step not printed. |
| 3 | LogSettingsActivity.lambda$onCreate$0 | REACHABLE proposed | INFERRED | Registered LogSettingsActivity.java:47 toolbar.setNavigationOnClickListener((v) -> finish()); framework click dispatch not printed. |
| 4 | LogSettingsActivity.onCreate | REACHABLE proposed | INFERRED | Framework lifecycle; intent site LogActivity.java:261 startActivity(new Intent(this, LogSettingsActivity.class)); body LogSettingsActivity.java:37-50. |
| 5 | LogSettingsFragment.<clinit> | REACHABLE proposed | INFERRED | Class load on fragment creation; static TAG LogSettingsFragment.java:39 runs at class init. JVM step not printed. Attach step not printed (see caveat). |
| 6 | LogSettingsFragment.<init> | REACHABLE proposed | INFERRED | Implicit default constructor; framework fragment instantiation. Instantiation/attach step not printed (see caveat). |
| 7 | LogSettingsFragment.bindOnPreferenceChangeListener | REACHABLE proposed | SOURCE | Called LogSettingsFragment.java:73 from onCreate; definition :83-86 preference.setOnPreferenceChangeListener(this). |
| 8 | LogSettingsFragment.lambda$onCreate$0 | REACHABLE proposed | INFERRED | Registered LogSettingsFragment.java:70 setOnBindEditTextListener((editText) -> editText.setFilters(maxFilter)); framework EditText-bind dispatch not printed. |
| 9 | LogSettingsFragment.onCreate | REACHABLE proposed | INFERRED | Framework PreferenceFragmentCompat lifecycle; body :52-74 builds maxFilter :59-64 and binds maxLogSize. Attach step not printed (see caveat). |
| 10 | LogSettingsFragment.onCreatePreferences | REACHABLE proposed | INFERRED | Framework PreferenceFragmentCompat dispatch; body :78-81 setPreferencesFromResource(R.xml.pref_log, rootKey). |
| 11 | LogSettingsFragment.onPreferenceChange | REACHABLE proposed | INFERRED | Listener registered via row 7 (:73, :83-86); framework preference-change dispatch not printed. Body :89-101 handles pref_key_max_log_size. |
| 12 | LogSourceFactory.<init> | REACHABLE proposed | SOURCE | new LogSourceFactory(sessionLogger) LogViewModel.java:75; definition LogSourceFactory.java:32-35. |
| 13 | LogSourceFactory.create | REACHABLE proposed | INFERRED | Factory passed to LivePagedListBuilder LogViewModel.java:92-94 (observeLog); androidx paging calls create() :39-42 returning new LogDataSource(logger). Library dispatch not printed. |
| 14 | LogViewModel.<init> | REACHABLE proposed | SOURCE | ViewModelProvider(this).get(LogViewModel.class) LogActivity.java:92; body LogViewModel.java:65-78 (LogSourceFactory :75, initMutableParams :77). |
| 15 | LogViewModel.copyLogEntryToClipboard | REACHABLE proposed | SOURCE | LogActivity.java:463 onItemClicked calls viewModel.copyLogEntryToClipboard(entry); definition LogViewModel.java:215-228. |
| 16 | LogViewModel.getLogEntriesCount | REACHABLE proposed | SOURCE | LogActivity.java:445 updateToolbarSubtitle calls viewModel.getLogEntriesCount(); definition :162-165. |
| 17 | LogViewModel.getSaveLogFileName | REACHABLE proposed | SOURCE | LogActivity.java:311 saveLogPathChooseDialog sets config.fileName = viewModel.getSaveLogFileName(); definition :191-197. |
| 18 | LogViewModel.initMutableParams | REACHABLE proposed | SOURCE | Called from <init> LogViewModel.java:77; definition :80-90 (sets logging/filters from pref, registers paramsCallback :89). |
| 19 | LogViewModel.logPausedManually | REACHABLE proposed | SOURCE | LogActivity.java:209 (onPrepareOptionsMenu), :266 (pauseResumeLog), :275-278 (resumeLog wrapper), :285 (toggleRecord); definition :167-170. |
| 20 | LogViewModel.logRecording | REACHABLE proposed | SOURCE | LogActivity.java:219 (onPrepareOptionsMenu), :283 (toggleRecord); definition :186-189. |
| 21 | LogViewModel.observeLog | REACHABLE proposed | SOURCE | LogActivity.java:119 viewModel.observeLog().observe(...); definition :92-96 (LivePagedListBuilder over sourceFactory). |
| 22 | LogViewModel.onCleared | REACHABLE proposed | INFERRED | AndroidViewModel lifecycle: framework/ViewModelStore clears the LogViewModel obtained at LogActivity.java:92; super.onCleared() + callback removal :100-105 printed, dispatch not printed. |
| 23 | LogViewModel.pauseLog | REACHABLE proposed | SOURCE | LogActivity.java:125 (fabUp), :135 (fabDown), :299 (toggleRecord stop path); definition :140-143. |
| 24 | LogViewModel.pauseLogManually | REACHABLE proposed | SOURCE | LogActivity.java:268 pauseResumeLog (newPausedState true branch); definition :145-149 (pauseLog() + logPaused = true). |
| 25 | LogViewModel.resumeLog | REACHABLE proposed | SOURCE | LogActivity.java:278 resumeLog wrapper (guarded by !logPausedManually); definition :151-154. |
| 26 | LogViewModel.resumeLogManually | REACHABLE proposed | SOURCE | LogActivity.java:270 pauseResumeLog (newPausedState false branch); definition :156-160 (resumeLog() + logPaused = false). |
| 27 | LogViewModel.saveLog | REACHABLE proposed | SOURCE | LogActivity.java:327 saveLogPathChoose launcher callback (RESULT_OK branch) viewModel.saveLog(filePath); definition :199-213 (SaveLogWorker enqueue). |
| 28 | LogViewModel.startLogRecording | REACHABLE proposed | SOURCE | LogActivity.java:294 toggleRecord (recording true branch); definition :172-177. |
| 29 | LogViewModel.stopLogRecording | REACHABLE proposed | SOURCE | LogActivity.java:330 saveLogPathChoose launcher callback (non-OK branch); definition :179-184. |
| 30 | LogViewModel$1.<init> | REACHABLE proposed | SOURCE | Anonymous OnPropertyChangedCallback field LogViewModel.java:107-110; instantiated as part of LogViewModel construction (row 14, LogActivity.java:92). |
| 31 | LogViewModel$1.onPropertyChanged | REACHABLE proposed | INFERRED | Registered LogViewModel.java:89 addOnPropertyChangedCallback(paramsCallback); databinding observable dispatch to :110-137 (BR.logging / filter switch) not printed. |
| 32 | SessionLogFilterDialog.<clinit> | REACHABLE proposed | INFERRED | Class load on newInstance/show; static TAG SessionLogFilterDialog.java:42. JVM step not printed. |
| 33 | SessionLogFilterDialog.<init> | REACHABLE proposed | SOURCE | new SessionLogFilterDialog() SessionLogFilterDialog.java:51 inside newInstance; implicit default constructor. |
| 34 | SessionLogFilterDialog.initLayoutView | REACHABLE proposed | SOURCE | Called SessionLogFilterDialog.java:101 from onCreateDialog; definition :106-114 (AlertDialog.Builder, negative button, alert = builder.create()). |
| 35 | SessionLogFilterDialog.lambda$initLayoutView$1 | REACHABLE proposed | INFERRED | Registered SessionLogFilterDialog.java:110 setNegativeButton(..., (dialog, which) -> onBackPressed()); dialog button dispatch not printed. Body calls row 39. |
| 36 | SessionLogFilterDialog.lambda$onResume$0 | REACHABLE proposed | INFERRED | Registered SessionLogFilterDialog.java:74 setOnKeyListener inside onResume; back-key dispatch not printed. Body calls row 39 on KEYCODE_BACK ACTION_DOWN (:79). |
| 37 | SessionLogFilterDialog.newInstance | REACHABLE proposed | SOURCE | LogActivity.java:254 showFilterDialog (after findFragmentByTag null check :253); definition :49-57. |
| 38 | SessionLogFilterDialog.onAttach | REACHABLE proposed | INFERRED | Framework DialogFragment lifecycle on filterDialog.show(fm, TAG_FILTER_DIALOG) LogActivity.java:255; body :60-66 captures AppCompatActivity. Dispatch not printed. |
| 39 | SessionLogFilterDialog.onBackPressed | REACHABLE proposed | SOURCE | Called from row 35 (:110) and row 36 (:79); definition :116-119 alert.dismiss(). |
| 40 | SessionLogFilterDialog.onCreateDialog | REACHABLE proposed | INFERRED | Framework DialogFragment dispatch on show() LogActivity.java:255; body :90-104 (ViewModelProvider :95, binding inflate :98-99, initLayoutView :101, return alert :103). |

## Totals — mechanically verified

- Total: 40 rows, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 40 (SOURCE 22, INFERRED 18).
- UNREACHABLE proposed: 0.
- OPEN: 0.
- SOURCE rows: 7, 12, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 37, 39 = 22.
- INFERRED rows: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 22, 31, 32, 35, 36, 38, 40 = 18.
- 22 + 18 = 40. Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. Fragment-attach step for LogSettingsFragment (see caveat) — print `activity_log_settings.xml`
   or the transaction that hosts the fragment, or adopt the non-strict attach convention.
2. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
3. No row in this batch was flipped to UNREACHABLE, so no full-repo grep is owed for a
   UNREACHABLE claim in this batch; a grep would still be the way to close the attach caveat
   if the merger requires a printed attach site and the layout does not supply one.
