**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 83 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 83 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels re-derived from printed source. The earlier batch 83 proposal
  (`~/workspace/libretorrent-batch83-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against source re-read in this pass, and two of its
  verdicts changed on fresh printed evidence (see Changes vs prior proposal).

## Membership — verified first, not guessed

Exactly the 40 rows of batch 83 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
taken from the local plan copy `~/workspace/agent27-plan.tsv` (lines 3251–3290,
plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92` as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan — a candidate, not evidence.
Plan order, with descriptors, is reproduced in the table below (all rows are
`CreateTorrentDialog` or its anonymous classes `$1`/`$2`).

## Printed source used in this pass

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

- `ui/createtorrent/CreateTorrentDialog.java` — 561 lines, re-read in full this pass
  from `~/workspace/b83-src/CreateTorrentDialog.java` (local copy from the earlier
  proposal session; its line numbers were re-verified by grep in this pass and match
  every citation below).
- `ui/createtorrent/CreateTorrentViewModel.java` — 406 lines, re-read in full this pass
  from `~/workspace/b83-src/CreateTorrentViewModel.java` (the earlier proposal said 407;
  the file on disk is 406 lines — a one-line counting difference, no citation changes).
- `ui/createtorrent/CreateTorrentMutableParams.java` — 190 lines (proposal said 191;
  same one-line counting difference), re-read in full this pass.
- `ui/createtorrent/CreateTorrentActivity.java` — 140 lines, FRESH connector fetch
  this session from branch `work-2026-10-31`, saved at
  `~/workspace/b83-src/CreateTorrentActivity.java`. This is the new evidence that
  closes the dialog-display gap (see below).
- `src/main/res/layout/dialog_create_torrent.xml` — 283 lines, FRESH connector fetch
  this session from branch `work-2026-10-31` (SHA `cb379a10cdb154d5d69e51659781f0cd0a257844`),
  saved at `~/workspace/b83-src/dialog_create_torrent.xml`. Used for batch 84;
  for batch 83 it confirms the dialog layout variable is `viewModel` and the dialog
  is inflated at Dialog:186–188.

Line numbers below are "Dialog:" = CreateTorrentDialog.java, "Activity:" =
CreateTorrentActivity.java, "ViewModel:" = CreateTorrentViewModel.java,
"Params:" = CreateTorrentMutableParams.java, "Layout:" = dialog_create_torrent.xml.

## Changes vs prior proposal (the only two verdict changes)

1. **Row 25, `CreateTorrentDialog.newInstance`: OPEN → REACHABLE SOURCE.**
   The prior proposal left this OPEN because no caller was printed in its three files.
   Freshly printed this pass: `CreateTorrentActivity.onCreate` at Activity:83–86 —
   `createTorrentDialog = (CreateTorrentDialog)fm.findFragmentByTag(TAG_CREATE_TORRENT_DIALOG);`
   `if (createTorrentDialog == null) { createTorrentDialog = CreateTorrentDialog.newInstance();`
   `createTorrentDialog.show(fm, TAG_CREATE_TORRENT_DIALOG); }`.
   That is a printed direct call site plus the show step, so the row is SOURCE, not INFERRED.
   A connector `search_code` call for `CreateTorrentDialog.newInstance` was tried only
   as a locator: it returned 7 global non-repo results (other forks), which were
   DISREGARDED entirely — the verdict rests only on the freshly printed branch file above.
2. **Strict-entry caveat, narrowed (not removed).** The prior caveat said the dialog-display
   step was not printed, so all REACHABLE rows reverted to OPEN under a strict rule.
   The display step IS now printed (Activity:83–86). What is still NOT printed in this
   pass is the step that starts `CreateTorrentActivity` itself (launcher / intent /
   menu step). So under a strict launcher-entry rule, all 40 REACHABLE rows still revert
   to OPEN — but the missing link is now the activity starter, not the dialog display.
   Under the dialog-anchored convention used by sibling detail/dialog batches, all 40 stand.

## confirmed_by convention used here

- SOURCE: a caller site naming the method is printed in app source in one of the files above.
- INFERRED: the method is a framework/library callback (DialogFragment lifecycle,
  TextWatcher, OnItemSelectedListener, button click, LiveData observer, Rx subscribe,
  ActivityResult callback) whose dispatch code was NOT printed from `fw_src`; the method
  body itself is printed, and its registration site is printed. This follows the batch 14
  correction (SOURCE → INFERRED where dispatch is unprinted).
- Compiler-generated `<init>` rows are SOURCE only where a printed construction site
  (`new …()`) exists in app source; otherwise they would be INFERRED. Both anonymous
  `<init>` rows here have printed construction sites (see table).

## Lambda / anonymous-class numbering (flagged, not bytecode-verified)

- Anonymous classes by construction order: $1 = trackerUrls TextWatcher (Dialog:197),
  $2 = webSeedUrls TextWatcher (Dialog:212). $3/$4 listeners are batch 84 rows 2–7.
- Lambdas, global order with inner lambdas before their enclosing lambda (this ordering
  reproduces every plan signature exactly):
  $0 = onResume key listener (Dialog:105–122); $1 = subscribeAlertDialog event subscriber
  (Dialog:140–169); $2 = fileChooser click (Dialog:257); $3 = folderChooser click
  (Dialog:267); $4 = BuildState observer, signature (Button; BuildState) — captures addButton
  and takes the state (Dialog:295–309); $5 = cancel click (View) (Dialog:311);
  $6 = add click (View) (Dialog:313); $7 = onShow listener (DialogInterface) (Dialog:291);
  $8 = handleFinish subscribe lambda `() -> finish(OK)` (Dialog:394). Field-result lambdas
  $9/$10/$11 are assigned by field declaration order: $9 = chooseDir (Dialog:500),
  $10 = chooseFile (Dialog:517), $11 = choosePathToSave (Dialog:534). All three have the
  identical descriptor `(ActivityResult;)V`, so the $9/$10/$11 assignment must be confirmed
  against bytecode at merge; the REACHABLE verdict for each of the three callbacks does not
  depend on the assignment, since all three callback bodies exist and are registered via
  `registerForActivityResult` (Dialog:500/517/534).

## Judgements — 40 REACHABLE proposed / 0 UNREACHABLE / 0 OPEN

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | CreateTorrentDialog.<init> | REACHABLE | SOURCE | Default constructor; invoked by `newInstance()` Dialog:87–89 (`new CreateTorrentDialog()`), itself called at Activity:85. |
| 2 | CreateTorrentDialog.buildTorrent | REACHABLE | SOURCE | Called by choosePathToSave callback Dialog:546; body Dialog:338–346 calls `viewModel.buildTorrent()` (Dialog:345). |
| 3 | CreateTorrentDialog.choosePathToSaveDialog | REACHABLE | SOURCE | Called by add-button click lambda$initAlertDialog$6 Dialog:319; body Dialog:325–336 launches choosePathToSave. |
| 4 | CreateTorrentDialog.createFileErrorDialog | REACHABLE | SOURCE | Called by choosePathToSave callback Dialog:541; body Dialog:480–498. |
| 5 | CreateTorrentDialog.emptyFolderErrorDialog | REACHABLE | SOURCE | Called by handleBuildError Dialog:372; body Dialog:445–462. |
| 6 | CreateTorrentDialog.errorReportDialog | REACHABLE | SOURCE | Called by handleBuildError Dialog:374,376; body Dialog:465–478 sets `viewModel.errorReport` and shows ErrorReportDialog. |
| 7 | CreateTorrentDialog.fileOrFolderNotFoundDialog | REACHABLE | SOURCE | Called by handleBuildError Dialog:368; body Dialog:425–443. |
| 8 | CreateTorrentDialog.finish | REACHABLE | SOURCE | Called by onBackPressed Dialog:552, handleFinish Dialog:394,401, cancel click Dialog:312; body Dialog:555–559 calls `viewModel.finish()` and `FragmentCallback.onFragmentFinished`. |
| 9 | CreateTorrentDialog.handleBuildError | REACHABLE | SOURCE | Called by BuildState observer lambda$initAlertDialog$4 Dialog:308 and handleFinish catch Dialog:398; body Dialog:348–378 dispatches to rows 5–7 above. |
| 10 | CreateTorrentDialog.handleFinish | REACHABLE | SOURCE | Called by BuildState observer Dialog:305; body Dialog:380–403 (save-path toast, isStartSeeding branch, downloadTorrent subscribe or finish OK). |
| 11 | CreateTorrentDialog.initAlertDialog | REACHABLE | SOURCE | Called by initLayoutView Dialog:277; body Dialog:280–323 builds AlertDialog and sets onShow listener. |
| 12 | CreateTorrentDialog.initLayoutView | REACHABLE | SOURCE | Called by onCreateDialog Dialog:189; body Dialog:194–278 registers both TextWatchers, both spinners, both chooser buttons, then initAlertDialog. |
| 13 | CreateTorrentDialog.lambda$handleFinish$8 | REACHABLE | INFERRED | Body Dialog:394 `() -> finish(OK)` passed to Rx subscribe in handleFinish Dialog:391–395; Rx dispatch not printed. |
| 14 | CreateTorrentDialog.lambda$initAlertDialog$4 | REACHABLE | INFERRED | BuildState observer body Dialog:295–309 (BUILDING/FINISHED/ERROR dispatch to handleFinish/handleBuildError); registered via `viewModel.getState().observe(this, …)` Dialog:295; LiveData dispatch not printed. |
| 15 | CreateTorrentDialog.lambda$initAlertDialog$5 | REACHABLE | INFERRED | Cancel-button click body Dialog:311–312 → finish(CANCEL); framework click dispatch not printed. |
| 16 | CreateTorrentDialog.lambda$initAlertDialog$6 | REACHABLE | INFERRED | Add-button click body Dialog:313–321 (seed-path check, else choosePathToSaveDialog); framework click dispatch not printed. |
| 17 | CreateTorrentDialog.lambda$initAlertDialog$7 | REACHABLE | INFERRED | onShow listener body Dialog:291–322 (wires cancel/add buttons and state observer); AlertDialog framework dispatch not printed. |
| 18 | CreateTorrentDialog.lambda$initLayoutView$2 | REACHABLE | INFERRED | fileChooser click body Dialog:257–265 launches FileManagerDialog via chooseFile; framework click dispatch not printed. |
| 19 | CreateTorrentDialog.lambda$initLayoutView$3 | REACHABLE | INFERRED | folderChooser click body Dialog:267–275 launches FileManagerDialog via chooseDir; framework click dispatch not printed. |
| 20 | CreateTorrentDialog.lambda$new$10 | REACHABLE | INFERRED | Assigned by declaration order to chooseFile callback, body Dialog:517–532 (RESULT_OK check, openPathErrorDialog(true) or seedPath.set); ActivityResult dispatch not printed. Assignment not bytecode-verified. |
| 21 | CreateTorrentDialog.lambda$new$11 | REACHABLE | INFERRED | Assigned by declaration order to choosePathToSave callback, body Dialog:534–548 (RESULT_OK check, createFileErrorDialog or setSavePath + buildTorrent); ActivityResult dispatch not printed. Assignment not bytecode-verified. |
| 22 | CreateTorrentDialog.lambda$new$9 | REACHABLE | INFERRED | Assigned by declaration order to chooseDir callback, body Dialog:500–515 (RESULT_OK check, openPathErrorDialog(false) or seedPath.set); ActivityResult dispatch not printed. Assignment not bytecode-verified. |
| 23 | CreateTorrentDialog.lambda$onResume$0 | REACHABLE | INFERRED | Dialog key-listener body Dialog:105–122 (BACK key → onBackPressed); framework key dispatch not printed. Registered in onResume Dialog:107. |
| 24 | CreateTorrentDialog.lambda$subscribeAlertDialog$1 | REACHABLE | INFERRED | Event-subscriber body Dialog:140–169 (error-report positive/negative handling); registered via `dialogViewModel.observeEvents().subscribe(…)` Dialog:141; Rx dispatch not printed. |
| 25 | CreateTorrentDialog.newInstance | REACHABLE | SOURCE | Called by CreateTorrentActivity.onCreate Activity:85 (`createTorrentDialog = CreateTorrentDialog.newInstance();`), then shown Activity:86. Body Dialog:87–94 (`new CreateTorrentDialog()`, setArguments). Changed from OPEN in the prior proposal — see Changes above. |
| 26 | CreateTorrentDialog.onAttach | REACHABLE | INFERRED | Body Dialog:96–103 (super + activity capture); standard DialogFragment lifecycle dispatch not printed from fw_src. Reached once the dialog is shown (Activity:86). |
| 27 | CreateTorrentDialog.onBackPressed | REACHABLE | SOURCE | Called by onResume key lambda Dialog:115; body Dialog:550–553 → finish(BACK). |
| 28 | CreateTorrentDialog.onCreateDialog | REACHABLE | INFERRED | Body Dialog:172–192 (ViewModelProvider, binding inflate, initLayoutView); standard DialogFragment lifecycle dispatch not printed. Reached once the dialog is shown (Activity:86). |
| 29 | CreateTorrentDialog.onResume | REACHABLE | INFERRED | Body Dialog:105–123 (registers key listener); standard lifecycle dispatch not printed. |
| 30 | CreateTorrentDialog.onStart | REACHABLE | INFERRED | Body Dialog:133–138 (super + subscribeAlertDialog); standard lifecycle dispatch not printed. |
| 31 | CreateTorrentDialog.onStop | REACHABLE | INFERRED | Body Dialog:125–131 (super + disposables.clear()); standard lifecycle dispatch not printed. |
| 32 | CreateTorrentDialog.openPathErrorDialog | REACHABLE | SOURCE | Called by chooseDir callback Dialog:507 and chooseFile callback Dialog:524; body Dialog:405–423. |
| 33 | CreateTorrentDialog.subscribeAlertDialog | REACHABLE | SOURCE | Called by onStart Dialog:137; body Dialog:140–170. |
| 34 | CreateTorrentDialog$1.<init> | REACHABLE | SOURCE | Compiler-generated; construction site `new TextWatcher()` for trackerUrls Dialog:197. |
| 35 | CreateTorrentDialog$1.afterTextChanged | REACHABLE | INFERRED | Body Dialog:203–208 (clears trackerUrls error); registered Dialog:197; TextWatcher framework dispatch not printed. |
| 36 | CreateTorrentDialog$1.beforeTextChanged | REACHABLE | INFERRED | Body Dialog:199–200 (empty); registered Dialog:197; framework dispatch not printed. |
| 37 | CreateTorrentDialog$1.onTextChanged | REACHABLE | INFERRED | Body Dialog:202 (empty); registered Dialog:197; framework dispatch not printed. |
| 38 | CreateTorrentDialog$2.<init> | REACHABLE | SOURCE | Compiler-generated; construction site `new TextWatcher()` for webSeedUrls Dialog:212. |
| 39 | CreateTorrentDialog$2.afterTextChanged | REACHABLE | INFERRED | Body Dialog:218–223 (clears webSeedUrls error); registered Dialog:212; framework dispatch not printed. |
| 40 | CreateTorrentDialog$2.beforeTextChanged | REACHABLE | INFERRED | Body Dialog:214–215 (empty); registered Dialog:212; framework dispatch not printed. |

## Counts

- 40 rows judged: 40 REACHABLE proposed, 0 UNREACHABLE, 0 OPEN.
- confirmed_by split: SOURCE 18 (rows 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 25, 27, 32, 33, 34, 38), INFERRED 22 (all other rows).
- 0 rows verified for merge. Main-agent spot-check (1 in 5), `py_compile`, build, and Mac build/C1 are all NOT RUN here.

## Still owed before merge

1. Printed starter of CreateTorrentActivity (launcher / intent / menu step) — the remaining
   strict-entry link; under a strict launcher-entry rule all 40 rows revert to OPEN until it is printed.
2. Bytecode confirmation of lambda $9/$10/$11 and $4–$7 assignments.
3. Build, sampler, and C1 on a full checkout (clone still unavailable in this VM — named missing
   check, not passed; build/C1 run on the user's Mac after push, marked not run here).
4. No saved full-repo grep was run, so no row here was flipped to UNREACHABLE and none needs one
   (there are no UNREACHABLE rows in this batch).
