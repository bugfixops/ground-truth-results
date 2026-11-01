# Batch 59 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch59-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b596061-openclose-src/`, `~/workspace/b596061-openclose2-src/`,
  `~/workspace/b5354-openclose-src/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1c flips 3, 14, 28 (D4e), 5, 17 (D4d).
- Batch Counts verified mechanically from the label column AND against the Counts section: 33 REACHABLE / 0 UNREACHABLE / 7 OPEN
  (Phase 1c arithmetic holds: before 32/8, +3 D4e REACHABLE, −2 D4d to OPEN = 33/7).
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `ActivityFilemanagerDialogBindingImpl.executeBindings()V` | REACHABLE proposed INFERRED | PASS | FileManagerDialog.java:142 setContentView + :143 setViewModel (both verified in the fresh print). Generated lifecycle callback for the binding created there; generated dispatch unprinted, so INFERRED is correct. |
| 3 `ActivityFilemanagerDialogBindingImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | Label matches Phase 1c D4e (invalidateAll REACHABLE-on-inflate: generated Impl ctor calls invalidateAll on construction). *Conditional on D4e standing. Pre-flip "stays OPEN" sentence remains alongside the [APPLIED D4e] tag — text cleanup only. |
| 5 `ActivityFilemanagerDialogBindingImpl.setVariable(int,Object)Z` | OPEN | PASS* | Label matches Phase 1c D4d (setVariable direction: generated setVariable CALLS the typed setter, so the printed setViewModel call at FileManagerDialog :143 is zero evidence setVariable ran). *Conditional on D4d standing. Layout declares the viewModel variable (activity_filemanager_dialog.xml:8, verified). |
| 6 `ActivityFilemanagerDialogBindingImpl.setViewModel(FileManagerViewModel)V` | REACHABLE proposed INFERRED | PASS | FileManagerDialog.java:143 `binding.setViewModel(viewModel)` (verified). Generated dispatch to the Impl method unprinted, so INFERRED is correct. |
| 11 `ActivityLogBindingImpl.<init>(DataBindingComponent,View,Object[])` | REACHABLE proposed INFERRED | PASS | LogActivity.java:93 `DataBindingUtil.setContentView(this, R.layout.activity_log)` creates the binding (verified); generated 2-arg ctor delegating to this 3-arg ctor is unprinted generated code, so INFERRED is correct. |
| 14 `ActivityLogBindingImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | Same D4e application as row 3 (LogActivity :93 creation path verified). *Conditional on D4e. Same stale "stays OPEN" text note. |
| 16 `ActivityLogBindingImpl.onFieldChange(int,Object,int)Z` | REACHABLE proposed INFERRED | PASS | LogActivity.java:94 `binding.setViewModel(viewModel)` (verified); activity_log.xml:33 two-way `@{viewModel.mutableParams.logging}` (verified); variable block at :7-9 (viewModel, verified). Generated callback dispatch unprinted, so INFERRED is correct. |
| 17 `ActivityLogBindingImpl.setVariable(int,Object)Z` | OPEN | PASS* | Same D4d application as row 5, on the LogActivity :94 setViewModel dispatch. *Conditional on D4d standing. |
| 21 `AddTorrentInfoBinding.<init>(...)` | REACHABLE proposed INFERRED | FAIL (citation; label stands) | The route is real — AddTorrentInfoFragment.java:93 `DataBindingUtil.inflate(inflater, R.layout.fragment_add_torrent_info, ...)` (verified) and :103 `binding.setViewModel(viewModel)` (verified), and the included binding is reached via the super-call — but the cited ":104 binding.info access" is wrong: line 104 is blank and the first `binding.info` access is at :105 (`binding.info.folderChooserButton...`, verified). Proposed correction: citation ":93 inflate + :104 binding.info" → ":93 inflate + :105 binding.info". Label REACHABLE INFERRED unchanged. |
| 26 `AddTorrentInfoBindingImpl.executeBindings()V` | REACHABLE proposed INFERRED | PASS | Generated lifecycle callback for the included binding created at AddTorrentInfoFragment :93 (verified). Same wave convention as batch-58 row 31; INFERRED correct. |
| 28 `AddTorrentInfoBindingImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | Same D4e application as row 3 (fragment :93 creation path verified). *Conditional on D4e. Same stale "stays OPEN" text note. |
| 31 `AddTorrentInfoBindingImpl.onFieldChange(int,Object,int)Z` | REACHABLE proposed INFERRED | PASS | AddTorrentInfoFragment.java:103 setViewModel (verified); add_torrent_info.xml declares the viewModel variable (:8-10, verified) with five two-way `@{viewModel.mutableParams...}` bindings (see row 36). Generated callback dispatch unprinted, so INFERRED is correct. Note: the row's "(info + mutableParams)" phrasing is loose — the printed add_torrent_info.xml declares only the viewModel variable; the onFieldChange route stands on the mutableParams bindings alone, and no label change follows. |
| 36 `AddTorrentInfoBindingImpl$2.<init>(...)` | REACHABLE proposed INFERRED | PASS | Count correspondence verified exactly: add_torrent_info.xml declares exactly 5 two-way bindings — name :43, sequentialDownload :101, startAfterAdd :109, ignoreFreeSpace :116, firstLastPiecePriority :123 — matching the plan's 5 $N rows for AddTorrentInfoBindingImpl ($1-$5 across batches 59-61; $1/$2/$3/$4 rows present in this batch's table). Route: fragment :93 inflate + :103 setViewModel, then user edit/toggle in the shown fragment, framework dispatch INFERRED. $N-to-field assignment is source-order only (not bytecode-verified) as the row itself states; the revert condition (if the merger rejects the inverse-listener identification, all $N flips in 59-61 revert to OPEN together) is recorded, not decided here. |

## Totals

- PASS: 12, FAIL: 1 (of 13 checked). The single FAIL is citation-only; no label is wrong in this batch.
- Proposed corrections:
  1. Row 21: citation ":104 binding.info access" → ":105 binding.info access". Label REACHABLE INFERRED unchanged.
  2. Text cleanups (no label changes): delete superseded "stays OPEN" sentences in rows 3, 14, 28.
