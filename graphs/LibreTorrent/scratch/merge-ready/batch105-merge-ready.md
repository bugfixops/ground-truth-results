# LibreTorrent batch 105 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run
or is claimed in this file. No `search_code` result was used as evidence for any row.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 105 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-105 proposal
  (`~/workspace/libretorrent-batch105-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against source freshly fetched in this pass, and no
  prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 105 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from
the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`
(generator candidates, not evidence), in plan order:
16 GoToFolderDialog / GoToFolderDialog$1 rows, 1 GoToFolderViewModel row, 23 LogActivity rows.
Rows 1–40 below are those 40 rows, in plan order. The plan's `current_label`
(REACHABLE, generator candidate) is not adopted wholesale; each row below carries its
own printed citation.

## Printed source used in this pass

All files freshly connector-fetched from branch `work-2026-10-31`, one file at a time
with pauses, saved in `~/workspace/b105-106-src/` (base path
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`).
No fresh HTTP 429 was hit in this pass.

- `ui/filemanager/GoToFolderDialog.java` — 166 lines, SHA `cae36db32c33a12b13ab96639840dfad0b105979`
  (byte-identical to the prior proposal's SHA).
- `ui/filemanager/GoToFolderViewModel.java` — 34 lines (35 with trailing newline),
  SHA `d17177436a487e27eb55d3831bd3e617ce303f9b`.
- `ui/filemanager/FileManagerDialog.java` — 692 lines,
  SHA `62c879b92cff8341dc1f26b1fd235902c6050c8b`.
- `ui/log/LogActivity.java` — 470 lines, SHA `3569e10e4b0dd52e9f5f69dd7b5ee60fdd0116f1`.
- `ui/log/LogViewModel.java` — 227 lines, SHA `f6374daf682f89108f17eb211a0dbefdbb962462`
  (context only; its own rows are not in this batch).
- `ui/main/MainActivity.java` — 811 lines, SHA `d21f8b70fb50fa09c7b3708243c4f251176f4517`
  — **new in this pass**: this is what closes the LogActivity starter that the prior
  proposal had only as a sibling-agent lead.

## Shared routes (printed steps, cited once here and reused by row)

**G — FileManagerDialog menu -> GoToFolderDialog (dialog-anchored, NOT launcher-anchored).**
Freshly printed in this pass: FileManagerDialog.onOptionsItemSelected :511-512
(`R.id.filemanager_go_to_folder_menu` -> goToDirectoryDialog()) ->
goToDirectoryDialog :548-555 (findFragmentByTag :550, else GoToFolderDialog.newInstance() :552,
show(fm, TAG_ERROR_OPEN_DIR_DIALOG) :553) -> framework DialogFragment dispatch
(INFERRED, not printed from fw_src) -> GoToFolderDialog onAttach / onCreateDialog / onResume.
Who starts FileManagerDialog was NOT printed in this pass, so GoTo rows remain anchored
at the FileManagerDialog menu, not at the launcher. Under a strict launcher-to-leaf rule
(rows 1–16) revert to OPEN. This strict-entry convention is UNDECIDED at project level;
it is recorded here per row, not decided.

**G1 — Inside GoToFolderDialog (all steps freshly printed in GoToFolderDialog.java).**
onCreateDialog :91-105: ViewModelProvider.get(GoToFolderViewModel.class) :95-96,
DataBindingUtil.inflate :99, initLayoutView() :102. initLayoutView :107-126:
binding.path.addTextChangedListener(new TextWatcher() {...}) :109, initAlertDialog(binding.getRoot()) :125.
initAlertDialog :128-145: AlertDialog.Builder :129-133, alert = builder.create() :135,
alert.setOnShowListener(...) :137, inside it positive-button setOnClickListener -> goToDir() :139
and negative-button setOnClickListener -> finish(..., CANCEL) :142-143.
onResume :73-87: getDialog().setOnKeyListener(...) :77, inside it KEYCODE_BACK + ACTION_DOWN ->
onBackPressed() :80. onBackPressed :158-160 -> finish(..., BACK).
TextWatcher anonymous class ($1) :109-123: beforeTextChanged :111-112 (empty),
onTextChanged :115-116 (empty), afterTextChanged :119-122 (clears layoutPath error).

Lambda-number note (GoTo, NOT bytecode-verified): plan row 5, lambda$initAlertDialog$3
(DialogInterface), is unambiguously the setOnShowListener lambda at :137. Plan rows 3–4,
lambda$initAlertDialog$1 and $2 (both View), are the two setOnClickListener lambdas at
:139 and :142; the exact positive-vs-negative assignment of $1 vs $2 was NOT verified
against bytecode, but both lambdas are reachable by the same route (dialog shown, button
clicked), so the labels are unaffected. Merger must confirm $1/$2 assignment against
bytecode if it matters.

**L — MainActivity menu -> LogActivity (NEW in this pass, freshly printed).**
MainActivity.onOptionsItemSelected :754-755 (`R.id.log_menu` -> showLog()) ->
showLog() :801-802 (`startActivity(new Intent(this, LogActivity.class))`) ->
framework activity instantiation (INFERRED) -> LogActivity lifecycle.
This replaces the prior proposal's sibling-agent lead ("MainActivity log menu -> showLog ->
LogActivity"), which is now printed evidence, not a lead. The remaining strict-entry gap
for Log rows is only the launcher -> MainActivity step, which was NOT freshly printed in
this pass (AndroidManifest.xml was not fetched here; the batch 107–108 report's
manifest:43, MAIN/LAUNCHER:53-55 is a lead only, not fresh evidence here). Under a strict
launcher-to-leaf rule, Log rows (17–40) revert to OPEN on that single unprinted step alone.
Inside LogActivity (all steps freshly printed): onCreate :77-147: ViewModelProvider(this).get(LogViewModel.class) :92,
toolbar navigation click -> finish() :99, updateToolbarSubtitle() :102,
new LogAdapter(this) :116, observeLog().observe(this, (entries) -> adapter.submitList(entries, handleUpdateAdapter)) :119-120,
addOnScrollListener(scrollCallback) :122, fabUp click :124-132, fabDown click :134-143,
hideFabUp() :145, hideFabDown() :146. onStart :168-173 registers paramsCallback;
onStop :159-165 removes it and clears disposables; onDestroy :150-156 removes handler
callbacks and calls resumeLog(); onSaveInstanceState :186-192; onCreateOptionsMenu :195-201
inflates R.menu.log; onPrepareOptionsMenu :205-229 calls mutableParams.isLogging() :206;
onOptionsItemSelected :232-248 routes pause_resume_log_menu -> pauseResumeLog() :236,
record_log_menu -> toggleRecord() :238, save_log_menu -> saveLogPathChooseDialog() :240,
filter_log_menu -> showFilterDialog() :242, log_settings_menu -> showLogSettings() :244.
Field lambdas: saveLogPathChoose callback :318-335 (only ActivityResult lambda in the
class, so lambda$new$4 is unambiguous); hideFabUpRunnable :434, hideFabDownRunnable :436,
handleUpdateAdapter :438-441 (three () -> lambdas = lambda$new$5/$6/$7; the exact $5/$6/$7
assignment among the three was NOT verified against bytecode, but all three runnables are
reachable — hide runnables via handler.postDelayed at :412/:425, handleUpdateAdapter via
the submitList callback at :120 — so the labels are unaffected).

**confirmed_by convention used here (per-row, not whole-route; UNDECIDED at project level,
recorded not decided):** SOURCE = the row's immediate call site is printed app code;
INFERRED = the row is reached only through a framework/library dispatch step
(lifecycle, menu, click, key, TextWatcher, ViewModelProvider, activity instantiation)
that was not printed from fw_src. A row marked SOURCE still depends on an INFERRED
framework step further upstream where noted in the route above. Under a whole-route
INFERRED convention, SOURCE rows would change confirmed_by only; labels are unaffected.

## Counts — batch 105, proposed not verified

- REACHABLE proposed: 40
  - SOURCE: 11
  - INFERRED: 29
- UNREACHABLE proposed: 0
- OPEN: 0
- Total: 40
- Verified for merge: 0

## Per-method table (all 40 rows, in plan order)

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | GoToFolderDialog.initAlertDialog | REACHABLE | SOURCE | GoToFolderDialog.java:125 initLayoutView calls initAlertDialog; def :128-145; route G1 |
| 2 | GoToFolderDialog.initLayoutView | REACHABLE | SOURCE | GoToFolderDialog.java:102 onCreateDialog calls initLayoutView; def :107-126; route G1 |
| 3 | GoToFolderDialog.lambda$initAlertDialog$1 | REACHABLE | INFERRED | One of the View click lambdas :139/:142 inside the onShow lambda; framework View-click dispatch INFERRED; see lambda-number note |
| 4 | GoToFolderDialog.lambda$initAlertDialog$2 | REACHABLE | INFERRED | The other View click lambda :139/:142; framework View-click dispatch INFERRED; see lambda-number note |
| 5 | GoToFolderDialog.lambda$initAlertDialog$3 | REACHABLE | INFERRED | setOnShowListener lambda :137-144; framework dialog-show dispatch INFERRED; body registers both button clicks |
| 6 | GoToFolderDialog.lambda$onResume$0 | REACHABLE | INFERRED | setOnKeyListener lambda :77-86 in onResume; framework key dispatch INFERRED; body calls onBackPressed :80 |
| 7 | GoToFolderDialog.newInstance | REACHABLE | SOURCE | FileManagerDialog.java:552 goToDirectoryDialog calls newInstance; def GoToFolderDialog.java:55-62; route G |
| 8 | GoToFolderDialog.onAttach | REACHABLE | INFERRED | Framework DialogFragment dispatch after show at FileManagerDialog.java:553; def GoToFolderDialog.java:65-70; route G |
| 9 | GoToFolderDialog.onBackPressed | REACHABLE | SOURCE | GoToFolderDialog.java:80 key-lambda body calls onBackPressed; def :158-160; upstream key dispatch INFERRED |
| 10 | GoToFolderDialog.onCreateDialog | REACHABLE | INFERRED | Framework DialogFragment dispatch after show at FileManagerDialog.java:553; def GoToFolderDialog.java:91-105; route G/G1 |
| 11 | GoToFolderDialog.onResume | REACHABLE | INFERRED | Framework DialogFragment dispatch after show at FileManagerDialog.java:553; def GoToFolderDialog.java:73-87 |
| 12 | GoToFolderDialog$1.<init> | REACHABLE | SOURCE | GoToFolderDialog.java:109 new TextWatcher() in initLayoutView; anonymous class :109-123 |
| 13 | GoToFolderDialog$1.afterTextChanged | REACHABLE | INFERRED | Framework TextWatcher dispatch; registration :109, body :119-122 clears layoutPath error |
| 14 | GoToFolderDialog$1.beforeTextChanged | REACHABLE | INFERRED | Framework TextWatcher dispatch; registration :109, empty body :111-112 |
| 15 | GoToFolderDialog$1.onTextChanged | REACHABLE | INFERRED | Framework TextWatcher dispatch; registration :109, empty body :115-116 |
| 16 | GoToFolderViewModel.<init> | REACHABLE | INFERRED | GoToFolderDialog.java:95-96 ViewModelProvider.get(GoToFolderViewModel.class); framework ViewModel dispatch INFERRED; def GoToFolderViewModel.java:31-33, field path :29 |
| 17 | LogActivity.<init> | REACHABLE | INFERRED | No explicit constructor in LogActivity.java (implicit default); framework activity instantiation INFERRED after MainActivity.showLog :802; route L |
| 18 | LogActivity.hideFabDown | REACHABLE | SOURCE | LogActivity.java:146 onCreate, :353/:367/:402 scroll callbacks; def :429-432 |
| 19 | LogActivity.hideFabUp | REACHABLE | SOURCE | LogActivity.java:145 onCreate, :127 fabUp click, :348/:366/:392/:401 scroll callbacks; def :415-419 |
| 20 | LogActivity.lambda$new$4 | REACHABLE | INFERRED | saveLogPathChoose ActivityResult callback :318-335; framework ActivityResult dispatch INFERRED; body :327 saveLog / :330-331 stopLogRecording+resumeLog |
| 21 | LogActivity.lambda$new$5 | REACHABLE | INFERRED | One of the three () runnables :434/:436/:438-441; Handler postDelayed (:412/:425) or submitList callback (:120) dispatch INFERRED; see lambda-number note |
| 22 | LogActivity.lambda$new$6 | REACHABLE | INFERRED | One of the three () runnables :434/:436/:438-441; dispatch INFERRED as row 21 |
| 23 | LogActivity.lambda$new$7 | REACHABLE | INFERRED | One of the three () runnables :434/:436/:438-441; dispatch INFERRED as row 21; handleUpdateAdapter body :438-441 calls scrollLogList + updateToolbarSubtitle |
| 24 | LogActivity.lambda$onCreate$0 | REACHABLE | INFERRED | Toolbar navigation click lambda :99 (v -> finish()); framework View-click dispatch INFERRED |
| 25 | LogActivity.lambda$onCreate$1 | REACHABLE | INFERRED | observeLog observer lambda :119-120 (PagedList -> adapter.submitList(entries, handleUpdateAdapter)); LiveData dispatch INFERRED |
| 26 | LogActivity.lambda$onCreate$2 | REACHABLE | INFERRED | fabUp click lambda :124-132 (pauseLog, hideFabUp, scroll to 0, resumeLog); framework View-click dispatch INFERRED |
| 27 | LogActivity.lambda$onCreate$3 | REACHABLE | INFERRED | fabDown click lambda :134-143 (pauseLog, hideFabUp, scroll to last, resumeLog); framework View-click dispatch INFERRED |
| 28 | LogActivity.onCreate | REACHABLE | INFERRED | Framework activity lifecycle dispatch INFERRED; def :77-147; route L |
| 29 | LogActivity.onCreateOptionsMenu | REACHABLE | INFERRED | Framework menu dispatch INFERRED; def :195-201 inflates R.menu.log |
| 30 | LogActivity.onDestroy | REACHABLE | INFERRED | Framework lifecycle dispatch INFERRED; def :150-156 (removeCallbacksAndMessages, resumeLog) |
| 31 | LogActivity.onItemClicked | REACHABLE | INFERRED | ClickListener callback via LogAdapter$ViewHolder.lambda$bind$0 (batch 106 row 21, freshly printed LogAdapter.java:102-105); click dispatch INFERRED; def LogActivity.java:461-469 (copyLogEntryToClipboard + Snackbar) |
| 32 | LogActivity.onOptionsItemSelected | REACHABLE | INFERRED | Framework menu dispatch INFERRED; def :232-248 |
| 33 | LogActivity.onPrepareOptionsMenu | REACHABLE | INFERRED | Framework menu dispatch INFERRED; def :205-229, calls mutableParams.isLogging() :206 |
| 34 | LogActivity.onSaveInstanceState | REACHABLE | INFERRED | Framework lifecycle dispatch INFERRED; def :186-192 |
| 35 | LogActivity.onStart | REACHABLE | INFERRED | Framework lifecycle dispatch INFERRED; def :168-173 registers paramsCallback |
| 36 | LogActivity.onStop | REACHABLE | INFERRED | Framework lifecycle dispatch INFERRED; def :159-165 (disposables.clear, removeOnPropertyChangedCallback) |
| 37 | LogActivity.pauseResumeLog | REACHABLE | SOURCE | LogActivity.java:236 onOptionsItemSelected calls pauseResumeLog; def :264-273 |
| 38 | LogActivity.resumeLog | REACHABLE | SOURCE | LogActivity.java:131 fabUp click, :142 fabDown click, :155 onDestroy, :331 save callback; def :275-279 |
| 39 | LogActivity.saveLogPathChooseDialog | REACHABLE | SOURCE | LogActivity.java:240 onOptionsItemSelected, :300 toggleRecord (stop-recording branch); def :304-316 (Intent to FileManagerDialog, SAVE_FILE_MODE, saveLogPathChoose.launch) |
| 40 | LogActivity.scrollLogList | REACHABLE | SOURCE | LogActivity.java:439 handleUpdateAdapter body calls scrollLogList; def :452-458 |

## Remaining before merge

- Printed launcher -> MainActivity step (AndroidManifest.xml, not fetched in this pass),
  if a strict launcher-anchored route is required for Log rows 17–40. The LogActivity
  starter itself is now freshly printed (MainActivity :754-755, :801-802), so it is no
  longer a lead.
- Printed entry into FileManagerDialog, if a strict launcher-anchored route is required
  for GoTo rows 1–16 (currently anchored at the FileManagerDialog menu).
- Bytecode confirmation of GoToFolderDialog lambda$initAlertDialog$1 vs $2
  (positive vs negative button) and LogActivity lambda$new$5/$6/$7 (which runnable is which).
- Saved full-repo grep: not needed for any REACHABLE row above, but no row here was
  judged UNREACHABLE, so no grep obligation arises from this batch.
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — not run, never claimed.
