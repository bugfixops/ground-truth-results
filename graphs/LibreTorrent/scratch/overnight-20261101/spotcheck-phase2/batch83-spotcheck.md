# LibreTorrent batch 83 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 83. Work file checked: `~/workspace/overnight/stream-A/work/batch83-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus row 25, the one verdict changed in the file (OPEN → REACHABLE SOURCE on fresh evidence, listed in its Changes section).
- Method: re-derived from already-fetched source on disk (`~/workspace/b83-src/`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: the dialog-display step is printed (Activity:83-86) but the starter of CreateTorrentActivity itself is not; under a strict launcher-entry rule all REACHABLE rows would revert to OPEN. That convention is undecided and NOT decided here.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | CreateTorrentDialog.<init> | REACHABLE / SOURCE | PASS | Invoked by newInstance() CreateTorrentDialog.java:87-89 (`new CreateTorrentDialog()`), itself called at CreateTorrentActivity.java:85. |
| 6 | CreateTorrentDialog.errorReportDialog | REACHABLE / SOURCE | PASS | Called by handleBuildError CreateTorrentDialog.java:374 and :376; def :465-478. |
| 11 | CreateTorrentDialog.initAlertDialog | REACHABLE / SOURCE | PASS | Called by initLayoutView CreateTorrentDialog.java:277; def :280-323. |
| 16 | CreateTorrentDialog.lambda$initAlertDialog$6 | REACHABLE / INFERRED | PASS | Add-button click body CreateTorrentDialog.java:313-321 (seed-path check, else choosePathToSaveDialog); framework click dispatch unprinted → INFERRED correct. |
| 21 | CreateTorrentDialog.lambda$new$11 | REACHABLE / INFERRED | PASS | choosePathToSave callback CreateTorrentDialog.java:534-548 (RESULT_OK check, createFileErrorDialog or setSavePath + buildTorrent :545-546); ActivityResult dispatch unprinted → INFERRED correct. Assignment by declaration order, not bytecode-verified (label unaffected, as the file notes). |
| 25 | CreateTorrentDialog.newInstance | REACHABLE / SOURCE | PASS | Printed direct call CreateTorrentActivity.java:85 `createTorrentDialog = CreateTorrentDialog.newInstance();` then show :86; def CreateTorrentDialog.java:87-94. The OPEN → REACHABLE change is supported. |
| 26 | CreateTorrentDialog.onAttach | REACHABLE / INFERRED | PASS | Def CreateTorrentDialog.java:96-103 (super + activity capture); standard DialogFragment lifecycle dispatch unprinted → INFERRED correct. |
| 31 | CreateTorrentDialog.onStop | REACHABLE / INFERRED | PASS | Def CreateTorrentDialog.java:125-131 (super + disposables.clear()); lifecycle dispatch unprinted → INFERRED correct. |
| 36 | CreateTorrentDialog$1.beforeTextChanged | REACHABLE / INFERRED | PASS | First (trackerUrls) TextWatcher registered CreateTorrentDialog.java:197; empty beforeTextChanged :199-200; framework dispatch unprinted → INFERRED correct. |

## Totals

- PASS: 9 / 9. FAIL: 0 / 9.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked.
