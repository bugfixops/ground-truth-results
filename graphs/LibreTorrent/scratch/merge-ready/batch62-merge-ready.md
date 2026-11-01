# LibreTorrent batch 62 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 62 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposal (Agent 20,
  `~/workspace/libretorrent-batch62-proposal.md`) was used as an INPUT / lead list only;
  every anchor citation below was re-checked against a fresh connector fetch in this pass,
  and every OPEN row was re-judged against that fresh print (see "Fresh re-check" below).
  No proposal verdict was copied as a result without that re-check.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 62 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/crosscheck/batch_plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-62 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence).
Method names, JVM descriptors, and plan order were checked row-for-row against the table
below in this pass: 40 rows, sequence 1-40 intact, zero mismatches vs the plan.
Classes: DialogAddTagBindingImpl$1 (rows 1-2, tail of that Impl),
DialogCreateTorrentBinding + DialogCreateTorrentBindingImpl (rows 3-28),
DialogErrorBinding + DialogErrorBindingImpl (rows 29-39),
DialogGoToFolderBinding (row 40, <init> only).

## Fresh re-check in this pass (branch work-2026-10-31, connector, one file at a time, 20 s pauses)

All paths under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`,
saved in `~/workspace/b626364-src/`:
- `ui/addtag/AddTagDialog.java` — fresh SHA `a8fd5111…`, 234 lines: DataBindingUtil.inflate dialog_add_tag at :128, binding.setViewModel(viewModel) at :129. Matches the proposal exactly. No `binding.getViewModel()` call in the file.
- `ui/createtorrent/CreateTorrentDialog.java` — fresh SHA `011fed03…`, 561 lines: inflate dialog_create_torrent at :185, setLifecycleOwner at :186, setViewModel at :187; piecesSize selection at :227, setPiecesSizeIndex at :233, setTorrentVersionIndex at :247, getState().observe at :295, buildTorrent() at :338-346 (viewModel.buildTorrent() at :345), seedPath.set at :513/:530, setSavePath at :545. Matches the proposal exactly.
- `ui/createtorrent/CreateTorrentViewModel.java` — fresh SHA `65b3c4ee…`, 407 lines, NEW in this pass (not in the proposal): mutableParams field at :59, state MutableLiveData at :60, buildProgress MutableLiveData at :61, state.setValue at :113/:153, buildProgress.setValue at :114, state.postValue at :225/:239, buildProgress.postValue at :244/:249, getState() at :126, getBuildProgress() at :131-133, setPieceSizeIndex at :141, setTorrentVersionIndex at :148. This satisfies the proposal's revert condition for rows 11 and 13 (printed setValue/postValue required); those rows stay INFERRED only because dispatch to the generated Impl onChange is unprinted, not because the LiveData values are unprinted.
- `ui/errorreport/ErrorReportDialog.java` — fresh SHA `9c7c5c9b…`, 85 lines: inflate dialog_error at :68, setDetailError(detailError) at :69, expansionHeader/expandableLayout use at :79-81. Matches the proposal exactly (proposal cited :79-81 for initLayoutView; fresh file shows the same lines in onCreateDialog layout use).
- `ui/filemanager/GoToFolderDialog.java` — fresh SHA `3d0f97b4…`, 167 lines: inflate dialog_go_to_folder at :99, setViewModel at :100, binding.path TextWatcher at :109, initAlertDialog(binding.getRoot()) at :125. Matches the proposal exactly.
- No fresh HTTP 429 was hit in this pass. No generated `*BindingImpl.java` body, DataBinderMapperImpl, or layout XML is in `final_java_only`, so every Impl dispatch below is INFERRED, never SOURCE, exactly as in the proposal.

## Judgement rule (same as the proposal, consistent with batches 67-68)

- REACHABLE proposed, INFERRED, where a dialog prints DataBindingUtil.inflate for that
  layout AND a variable setter (setViewModel, or setDetailError for Error): the generated
  mapper returns the Impl, its constructor runs, executeBindings runs on inflate, the
  setter runs the Impl override, onFieldChange runs when a registered observable notifies,
  and onChangeViewModel* runs for the named observable. Abstract Binding <init> runs via
  the Impl super-call; abstract getters are read by generated executeBindings.
- OPEN where no printed caller/registration exists: hasPendingBindings, invalidateAll
  (no printed caller), every $N.<init>/onChange (observable mapping unprinted — Impl bodies
  absent), and DialogErrorBindingImpl.onFieldChange (detailError is a plain String argument
  at ErrorReportDialog:69, not an observable — no registration is printed, and without the
  Impl body this cannot be upgraded to a branch_never_taken claim, so it stays OPEN).
- OPEN is not UNREACHABLE: no Impl body and no full-repo grep was printed.
- Dialog-anchored caveat: the step that SHOWS each dialog was NOT printed in this pass,
  so under a strict entry-route rule every REACHABLE below reverts to OPEN. Routes are
  anchored at the dialog's onCreateDialog, not at the launcher. (A sibling agent's
  FileManagerDialog -> GoToFolderDialog route is NOT used as evidence here, as it was
  not printed in this session.)

## Counts — proposed, not verified

- REACHABLE proposed: 21 / 40 (all INFERRED, 0 SOURCE)
- UNREACHABLE proposed: 0
- OPEN: 19 / 40
- Verified for merge: 0

## Per-method table (plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | DialogAddTagBindingImpl$1.<init> | OPEN | — | Impl body unprinted; which observable $1 registers for is unprinted (see batch 61, rows 27-28 rule). |
| 2 | DialogAddTagBindingImpl$1.onChange | OPEN | — | Same as row 1; no printed change event assignable to $1. |
| 3 | DialogCreateTorrentBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogCreateTorrentBindingImpl constructor, mapper-created on CreateTorrentDialog:185 inflate. |
| 4 | DialogCreateTorrentBinding.getViewModel | REACHABLE proposed | INFERRED | Read by generated executeBindings of the Impl created at CreateTorrentDialog:185. |
| 5 | DialogCreateTorrentBindingImpl.<clinit> | REACHABLE proposed | INFERRED | First use is mapper creation on CreateTorrentDialog:185 inflate; class-init timing unprinted. |
| 6 | DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper creation on CreateTorrentDialog:185 inflate. |
| 7 | DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Same mapper creation as row 6. |
| 8 | DialogCreateTorrentBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Runs on inflate (:185) and on rebind after setViewModel (:187) / setLifecycleOwner (:186). |
| 9 | DialogCreateTorrentBindingImpl.hasPendingBindings | OPEN | — | No printed caller, per Agent 23 precedent. |
| 10 | DialogCreateTorrentBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 11 | DialogCreateTorrentBindingImpl.onChangeViewModelBuildProgress | REACHABLE proposed | INFERRED | setViewModel printed at CreateTorrentDialog:187 and setLifecycleOwner at :186. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched (SHA 65b3c4ee…, 407 lines) prints buildProgress MutableLiveData at :61, setValue at :114, postValue at :244/:249, and getBuildProgress() at :131-133 — so the proposal's revert condition (printed setValue/postValue required) is now satisfied. Dispatch to Impl onChange remains generated, so still INFERRED, not SOURCE. |
| 12 | DialogCreateTorrentBindingImpl.onChangeViewModelMutableParams | REACHABLE proposed | INFERRED | MutableParams fields printed as changed after binding: setPiecesSizeIndex CreateTorrentDialog:233, setTorrentVersionIndex :247, seedPath.set :513/:530, setSavePath :545; dispatch via onFieldChange is generated. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched prints mutableParams setters at :141 (setPieceSizeIndex) and :148 (setTorrentVersionIndex) and mutableParams field at :59. Still INFERRED (generated dispatch). |
| 13 | DialogCreateTorrentBindingImpl.onChangeViewModelState | REACHABLE proposed | INFERRED | State LiveData printed as observed at CreateTorrentDialog:295 viewModel.getState().observe(this, ...), and buildTorrent :345 changes it. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched prints state MutableLiveData at :60, setValue at :113/:153, postValue at :225/:239 — so the proposal's revert condition (printed setValue/postValue required) is now satisfied. Dispatch to Impl onChange remains generated, so still INFERRED, not SOURCE. |
| 14 | DialogCreateTorrentBindingImpl.onFieldChange | REACHABLE proposed | INFERRED | Framework callback for the registered buildProgress/mutableParams/state observables after :187. |
| 15 | DialogCreateTorrentBindingImpl.setVariable | REACHABLE proposed | INFERRED | Generic variable dispatch for the Impl created at :185, viewModel set at :187. |
| 16 | DialogCreateTorrentBindingImpl.setViewModel | REACHABLE proposed | INFERRED | Impl override of the printed call CreateTorrentDialog:187 binding.setViewModel(viewModel). |
| 17 | DialogCreateTorrentBindingImpl$1.<init> | OPEN | — | Impl body unprinted; observable mapping for $1 unprinted. |
| 18 | DialogCreateTorrentBindingImpl$1.onChange | OPEN | — | Same as row 17. |
| 19 | DialogCreateTorrentBindingImpl$2.<init> | OPEN | — | Same as row 17. |
| 20 | DialogCreateTorrentBindingImpl$2.onChange | OPEN | — | Same as row 17. |
| 21 | DialogCreateTorrentBindingImpl$3.<init> | OPEN | — | Same as row 17. |
| 22 | DialogCreateTorrentBindingImpl$3.onChange | OPEN | — | Same as row 17. |
| 23 | DialogCreateTorrentBindingImpl$4.<init> | OPEN | — | Same as row 17. |
| 24 | DialogCreateTorrentBindingImpl$4.onChange | OPEN | — | Same as row 17. |
| 25 | DialogCreateTorrentBindingImpl$5.<init> | OPEN | — | Same as row 17. |
| 26 | DialogCreateTorrentBindingImpl$5.onChange | OPEN | — | Same as row 17. |
| 27 | DialogCreateTorrentBindingImpl$6.<init> | OPEN | — | Same as row 17. |
| 28 | DialogCreateTorrentBindingImpl$6.onChange | OPEN | — | Same as row 17. |
| 29 | DialogErrorBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogErrorBindingImpl constructor, mapper-created on ErrorReportDialog:68 inflate. |
| 30 | DialogErrorBinding.getDetailError | REACHABLE proposed | INFERRED | Read by generated executeBindings of the Impl created at :68, to bind the detailError set at :69. |
| 31 | DialogErrorBindingImpl.<clinit> | REACHABLE proposed | INFERRED | First use is mapper creation on ErrorReportDialog:68 inflate; class-init timing unprinted. |
| 32 | DialogErrorBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper creation on ErrorReportDialog:68 inflate. |
| 33 | DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Same mapper creation as row 32. |
| 34 | DialogErrorBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Runs on inflate (:68) and after setDetailError (:69). |
| 35 | DialogErrorBindingImpl.hasPendingBindings | OPEN | — | No printed caller. |
| 36 | DialogErrorBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 37 | DialogErrorBindingImpl.onFieldChange | OPEN | — | detailError is a plain String (ErrorReportDialog:69), not an observable; no registration is printed. Impl body unprinted, so this is OPEN, not branch_never_taken. |
| 38 | DialogErrorBindingImpl.setDetailError | REACHABLE proposed | INFERRED | Impl override of the printed call ErrorReportDialog:69 binding.setDetailError(detailError); dispatch to Impl is generated. |
| 39 | DialogErrorBindingImpl.setVariable | REACHABLE proposed | INFERRED | Generic variable dispatch for the Impl created at :68, detailError set at :69 (same registration rule as the other Impls; reverts to OPEN if the merger requires a printed setVariable call site). |
| 40 | DialogGoToFolderBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogGoToFolderBindingImpl constructor, mapper-created on GoToFolderDialog:99 inflate (setViewModel at :100). Only the abstract <init> is in this batch; the Impl rows fall in a later batch and must be judged consistently with this row. |

## Still owed before merge

- Printed Impl bodies or DataBinderMapperImpl (not in final_java_only) to confirm $N mapping,
  hasPendingBindings/invalidateAll callers, Error onFieldChange registration, and the
  2-arg vs 3-arg <init> choice.
- Printed dialog-show steps for a launcher-anchored route; strict-entry rule reverts all
  21 REACHABLE to OPEN until then.
- Rows 11/13 revert condition from the proposal is now satisfied (printed setValue/postValue
  in CreateTorrentViewModel, fresh fetch this pass); rows 11-13 remain INFERRED only because
  generated dispatch is unprinted, not because the LiveData values are unprinted.
- Saved full-repo grep before any OPEN row is flipped to UNREACHABLE; none is flipped here.
- Build, sampler, and C1 on a full checkout (clone still fails in this VM) — none claimed;
  build/C1 marked "not run" pending the user's Mac run after a push.
- Main-agent spot-check (1 in 5) and py_compile — not run here.
- 0/40 verified for merge. Nothing was pushed, nothing merged.

