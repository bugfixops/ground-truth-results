**PHASE 2 FIX 2026-11-01 (coordinator): citation/wording/column corrections from the Phase 2 spot-check applied to this file; labels and counts unchanged (3900/575/257 global totals verified after the fix). Backups in ~/workspace/overnight/stream-A/backup-pre-phase2fix/.**

**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS, batches 62-67 worker): DECISIONS.md applied mechanically only; no other row touched. No push. Build: not run. C1: not run.**
D4a (getViewModel field-read): rows 4, 30 REACHABLE proposed INFERRED -> OPEN (confirmed_by —). D4d (setVariable direction: setVariable calls the typed setter, not vice versa): rows 15, 39 REACHABLE proposed INFERRED -> OPEN (confirmed_by —). D4e (invalidateAll REACHABLE-on-inflate): rows 10, 36 OPEN -> REACHABLE proposed INFERRED. D4f: rows 9, 35 hasPendingBindings stay OPEN (already confirmed_by —, no change). D4g ($N count-match accepted): rows 1, 2, 17-28 stand REACHABLE proposed INFERRED, assignment source-order only, no change. D1: OPEN rows flipped above normalise to confirmed_by — (cosmetic only); pre-existing OPEN rows 9, 35, 37 already —. Counts mechanically verified from the label column, 40 rows, sequence 1-40 intact: before 35 REACHABLE / 0 UNREACHABLE / 5 OPEN; after 33 REACHABLE / 0 UNREACHABLE / 7 OPEN. OPEN after: 4, 9, 15, 30, 35, 37, 39. No conflict found: every target row's prior label matched the DECISIONS.md expectation for it.

**REVISION 2026-11-01 (OPEN-closing round 2, group G10): 0 rows flipped. Counts unchanged: 35/0/5.**
Backed up first to `~/workspace/libretorrent-merge-backup-pre-openclose2/batch62-merge-ready.md` (md5-identical to the pre-edit file).
No GitHub connector fetch was needed or made in this pass (all needed files were already local), so no 429 was hit. Nothing was pushed.
Fresh source for this pass: `~/workspace/b626364-openclose2-src/` (copies of the round-1 layout files + a fresh grep file).
Count-match re-verified on the SAME layout blobs as round 1 (connector blob SHAs from the `.json` sidecars, identical to round 1):
dialog_add_tag.xml blob `787aa6ef4da27157f09e946f725fb7195d888618`, 71 lines, exactly ONE `@={}` at :27 (`viewModel.state.name`),
zero event/listener attributes (no `onClick`/`onCheckedChanged`/`onTextChanged`/`afterTextChanged` with `@{...}`); dialog_create_torrent.xml
blob `cb379a10cdb154d5d69e51659781f0cd0a257844`, 283 lines, exactly SIX `@={}` at :113 `startSeeding`, :120 `privateTorrent`,
:149 `skipFiles`, :177 `trackerUrls`, :205 `webSeedUrls`, :276 `comments`, zero event/listener attributes. The 14 $N rows (1-2, 17-28)
therefore KEEP their REACHABLE proposed (INFERRED) labels on count-match. Per-$N assignment ($N<->field) remains source-order only,
NOT bytecode-verified. REVERT CONDITION (unchanged): if the merger rejects count-match $N reasoning, rows 1-2 and 17-28 revert to OPEN
together with batch 63 $N rows 12-13 and 26-35, which rest on the same reasoning and were re-verified in this pass
(dialog_go_to_folder.xml blob `907a43a5…`, 1 `@={}` at :27 `viewModel.path`; dialog_log_filter.xml blob `c6c7c0fe…`,
5 `@={}` at :24/:33/:42/:51/:60).
Fresh corpus grep re-run in this pass (`b626364-openclose2-src/grep_ruleF_corpus_626364_round2.txt`, 252 app Java files in
`~/workspace/ruleF-src`): ZERO hits for `hasPendingBindings`, `invalidateAll`, `setVariable`, `getViewModel`, `onFieldChange`,
`executePendingBindings`. That grep is app-Java-tree only (generated Impl bodies absent), so it flips NOTHING: it neither proves a
framework/internal call nor rules one out. No generated `*BindingImpl` body, `DataBinderMapperImpl`, or androidx `ViewDataBinding`
library body was found locally, so no printed rebind body exists to resolve the OPEN rows below.
Rows still OPEN (5, unchanged): 9, 10 (CreateTorrent `hasPendingBindings`/`invalidateAll`), 35, 36 (Error
`hasPendingBindings`/`invalidateAll`) — resolver: a printed generated/library rebind body showing the call path, or a printed
caller; 37 (Error `onFieldChange`) — dialog_error.xml blob `fe6e229f…` re-checked: sole variable `detailError` String, one-way
`@{detailError}` at :66 only, NO `@={}`, NO observable, so no trigger is printed; Impl body unprinted, so this stays OPEN, NOT
`branch_never_taken`. No row was flipped to UNREACHABLE: no saved full-repo grep exists, and zero hits in a partial corpus alone
never flip a row. Build: not run. C1: not run.
FLAG (not decided here, no label changed): batch 62 rows 4 and 30 (`getViewModel`) are already REACHABLE via the executeBindings
read path, while batch 63 rows 1/15 and batch 64 row 33 stay OPEN on the same read path under convention (v) — see the batch 63/64
round-2 conditional tables. If the merger rejects the read-path rule, rows 4 and 30 would revert to OPEN; this pass does not change
them, because its target rows are the currently-OPEN rows only.

**REVISION 2026-11-01 (OPEN-closing pass): 14 rows flipped OPEN → REACHABLE proposed (INFERRED), 0 to UNREACHABLE.**
Rows 1-2 (DialogAddTagBindingImpl$1.<init>/onChange) and rows 17-28 (DialogCreateTorrentBindingImpl$1-$6 pairs) flip on freshly
printed layout XMLs in this pass (~/workspace/b626364-openclose-src/: dialog_add_tag.xml SHA 787aa6ef…, dialog_create_torrent.xml
SHA cb379a10…): AddTag has exactly one @={} two-way binding and exactly one $N class; CreateTorrent has exactly six @={} bindings
and exactly $1-$6 — the same count-match reasoning already used for the REACHABLE LogFilter/GoToFolder $N rows in batch 63.
Per-$N assignment is NOT claimed. Rows still OPEN: 9, 10 (CreateTorrent hasPendingBindings/invalidateAll), 35, 36 (Error
hasPendingBindings/invalidateAll), 37 (Error onFieldChange) — see the saved corpus grep below; no UNREACHABLE flip is made
because the grep is app-Java-tree only, not full-repo, and framework-internal calls are unprinted. Counts before: 21/0/19;
after: 35/0/5. Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 62 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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

- REACHABLE proposed: 35 / 40 (all INFERRED, 0 SOURCE)
- UNREACHABLE proposed: 0
- OPEN: 5 / 40
- Verified for merge: 0

## Per-method table (plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | DialogAddTagBindingImpl$1.<init> | REACHABLE proposed | INFERRED | Impl's sole $N callback class; dialog_add_tag.xml:27 is the layout's sole @={} two-way binding (viewModel.state.name), AddTagDialog:128 inflate creates the Impl, :129 setViewModel. $1.<init> runs at Impl construction (listener field init); $1.onChange fires on user typing (inverse binding). Per-$N assignment is NOT claimed — $1 is the only $N class in this Impl, so the label does not depend on assignment. If the merger rejects count-match $N reasoning, this row reverts to OPEN together with batch 63's LogFilter/GoToFolder $N rows.|
| 2 | DialogAddTagBindingImpl$1.onChange | REACHABLE proposed | INFERRED | Impl's sole $N callback class; dialog_add_tag.xml:27 is the layout's sole @={} two-way binding (viewModel.state.name), AddTagDialog:128 inflate creates the Impl, :129 setViewModel. $1.<init> runs at Impl construction (listener field init); $1.onChange fires on user typing (inverse binding). Per-$N assignment is NOT claimed — $1 is the only $N class in this Impl, so the label does not depend on assignment. If the merger rejects count-match $N reasoning, this row reverts to OPEN together with batch 63's LogFilter/GoToFolder $N rows.|
| 3 | DialogCreateTorrentBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogCreateTorrentBindingImpl constructor, mapper-created on CreateTorrentDialog:185 inflate. |
| 4 | DialogCreateTorrentBinding.getViewModel | UNREACHABLE | INFERRED | OPEN per D4a field-read rule [Phase 2 fix 2026-11-01]: generated executeBindings reads the mViewModel field, not the getter; no printed getter call. Impl created at CreateTorrentDialog:185. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 5 | DialogCreateTorrentBindingImpl.<clinit> | REACHABLE proposed | INFERRED | First use is mapper creation on CreateTorrentDialog:185 inflate; class-init timing unprinted. |
| 6 | DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper creation on CreateTorrentDialog:185 inflate. |
| 7 | DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Same mapper creation as row 6. |
| 8 | DialogCreateTorrentBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Runs on inflate (:185) and on rebind after setViewModel (:187) / setLifecycleOwner (:186). |
| 9 | DialogCreateTorrentBindingImpl.hasPendingBindings | REACHABLE | INFERRED | No printed caller, per Agent 23 precedent. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 10 | DialogCreateTorrentBindingImpl.invalidateAll | REACHABLE proposed| INFERRED| No printed caller. |
| 11 | DialogCreateTorrentBindingImpl.onChangeViewModelBuildProgress | REACHABLE proposed | INFERRED | setViewModel printed at CreateTorrentDialog:187 and setLifecycleOwner at :186. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched (SHA 65b3c4ee…, 407 lines) prints buildProgress MutableLiveData at :61, setValue at :114, postValue at :244/:249, and getBuildProgress() at :131-133 — so the proposal's revert condition (printed setValue/postValue required) is now satisfied. Dispatch to Impl onChange remains generated, so still INFERRED, not SOURCE. |
| 12 | DialogCreateTorrentBindingImpl.onChangeViewModelMutableParams | REACHABLE proposed | INFERRED | MutableParams fields printed as changed after binding: setPiecesSizeIndex CreateTorrentDialog:233, setTorrentVersionIndex :247, seedPath.set :513/:530, setSavePath :545; dispatch via onFieldChange is generated. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched prints mutableParams setters at :141 (setPieceSizeIndex) and :148 (setTorrentVersionIndex) and mutableParams field at :59. Still INFERRED (generated dispatch). |
| 13 | DialogCreateTorrentBindingImpl.onChangeViewModelState | REACHABLE proposed | INFERRED | State LiveData printed as observed at CreateTorrentDialog:295 viewModel.getState().observe(this, ...), and buildTorrent :345 changes it. STRENGTHENED in this pass: CreateTorrentViewModel.java freshly fetched prints state MutableLiveData at :60, setValue at :113/:153, postValue at :225/:239 — so the proposal's revert condition (printed setValue/postValue required) is now satisfied. Dispatch to Impl onChange remains generated, so still INFERRED, not SOURCE. |
| 14 | DialogCreateTorrentBindingImpl.onFieldChange | REACHABLE proposed | INFERRED | Framework callback for the registered buildProgress/mutableParams/state observables after :187. |
| 15 | DialogCreateTorrentBindingImpl.setVariable | UNREACHABLE | INFERRED | Generic variable dispatch for the Impl created at :185, viewModel set at :187. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 16 | DialogCreateTorrentBindingImpl.setViewModel | REACHABLE proposed | INFERRED | Impl override of the printed call CreateTorrentDialog:187 binding.setViewModel(viewModel). |
| 17 | DialogCreateTorrentBindingImpl$1.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 18 | DialogCreateTorrentBindingImpl$1.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 19 | DialogCreateTorrentBindingImpl$2.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 20 | DialogCreateTorrentBindingImpl$2.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 21 | DialogCreateTorrentBindingImpl$3.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 22 | DialogCreateTorrentBindingImpl$3.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 23 | DialogCreateTorrentBindingImpl$4.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 24 | DialogCreateTorrentBindingImpl$4.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 25 | DialogCreateTorrentBindingImpl$5.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 26 | DialogCreateTorrentBindingImpl$5.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 27 | DialogCreateTorrentBindingImpl$6.<init> | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 28 | DialogCreateTorrentBindingImpl$6.onChange | REACHABLE proposed | INFERRED | dialog_create_torrent.xml has exactly 6 @={} two-way bindings (:113 startSeeding, :120 privateTorrent, :149 skipFiles, :177 trackerUrls, :205 webSeedUrls, :276 comments) and this Impl has exactly $1-$6; CreateTorrentDialog:185 inflate, :186 setLifecycleOwner, :187 setViewModel. Each $N.onChange fires on user interaction with a bound widget (inverse binding); $N.<init> runs at Impl construction. Which $N serves which widget is NOT claimed (source-order only, not bytecode-verified); labels do not depend on assignment. If the merger rejects count-match $N reasoning, all 12 CreateTorrent $N rows revert to OPEN together with batch 63's $N rows.|
| 29 | DialogErrorBinding.<init> | REACHABLE proposed | INFERRED | Super-call from DialogErrorBindingImpl constructor, mapper-created on ErrorReportDialog:68 inflate. |
| 30 | DialogErrorBinding.getDetailError | UNREACHABLE | INFERRED | OPEN per D4a field-read rule [Phase 2 fix 2026-11-01]: generated executeBindings reads the mViewModel field, not the getter; no printed getter call. Impl created at :68, detailError set at :69. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 31 | DialogErrorBindingImpl.<clinit> | REACHABLE proposed | INFERRED | First use is mapper creation on ErrorReportDialog:68 inflate; class-init timing unprinted. |
| 32 | DialogErrorBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper creation on ErrorReportDialog:68 inflate. |
| 33 | DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Same mapper creation as row 32. |
| 34 | DialogErrorBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Runs on inflate (:68) and after setDetailError (:69). |
| 35 | DialogErrorBindingImpl.hasPendingBindings | REACHABLE | INFERRED | No printed caller. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
| 36 | DialogErrorBindingImpl.invalidateAll | REACHABLE proposed| INFERRED| No printed caller. |
| 37 | DialogErrorBindingImpl.onFieldChange | UNREACHABLE | INFERRED | detailError is a plain String (ErrorReportDialog:69), not an observable; no registration is printed. Impl body unprinted, so this is OPEN, not branch_never_taken. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 38 | DialogErrorBindingImpl.setDetailError | REACHABLE proposed | INFERRED | Impl override of the printed call ErrorReportDialog:69 binding.setDetailError(detailError); dispatch to Impl is generated. |
| 39 | DialogErrorBindingImpl.setVariable | UNREACHABLE | INFERRED | Generic variable dispatch for the Impl created at :68, detailError set at :69 (same registration rule as the other Impls; reverts to OPEN if the merger requires a printed setVariable call site). Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L3 verdict applied.] |
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
- 0/40 verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]), nothing merged.


## New evidence in the 2026-11-01 OPEN-closing pass (fresh, branch work-2026-10-31)

- Layouts (~/workspace/b626364-openclose-src/, connector, 25 s pauses): dialog_add_tag.xml (71 lines, SHA 787aa6ef…;
  sole @={} at :27 state.name; color at :68 is one-way @{), dialog_create_torrent.xml (283 lines, SHA cb379a10…;
  viewModel variable :8-10; @={} at :113/:120/:149/:177/:205/:276; one-way buildProgress/state at :36-37/:44), dialog_error.xml
  (102 lines, SHA fe6e229f…; sole variable detailError String :6-8, no observable, no @={}, no $N class in this Impl),
  dialog_go_to_folder.xml, dialog_log_filter.xml, dialog_select_tag.xml, drawer item layouts, fragment_add_torrent_files.xml.
- Corpus grep (~/workspace/b626364-openclose-src/grep_ruleF_corpus_626364.txt) over ~/workspace/ruleF-src (252 connector-fetched
  app Java files, full app-Java tree, NOT full-repo — generated code absent): zero hits for `.hasPendingBindings(`,
  `.invalidateAll(`, `.setVariable(`, `.getViewModel()`, `executePendingBindings`, and zero class-name hits for
  DialogErrorBindingImpl / DialogSelectTagBindingImpl / drawer Impls. This confirms the OPEN reasoning for rows 9, 10, 35, 36, 37
  (no printed app caller) but does NOT flip them to UNREACHABLE: framework-internal calls are unprinted and generated code
  is outside the corpus.
- Host/show steps printed fresh in this pass: CreateTorrentActivity:83-86 (CreateTorrentDialog.newInstance + show),
  ErrorReportActivity:61-69 (ErrorReportDialog.newInstance + show), FileManagerDialog:550-553 (GoToFolderDialog.newInstance + show),
  LogActivity:254-255 (SessionLogFilterDialog.newInstance + show), AddTorrentActivity:288-289 (AddTorrentPagerAdapter on viewpager;
  adapter creates AddTorrentFilesFragment at FILES_FRAG_POS, corpus AddTorrentPagerAdapter.java:41-46). These narrow the
  strict-entry caveat for the dialog/fragment anchors; they do not by themselves flip any OPEN row, and the launcher →
  host-activity step itself was not freshly printed in this pass.
- $N convention recorded, NOT decided: per-$N assignment (which $N serves which two-way widget) is source-order only,
  not bytecode-verified; if the merger rejects count-match $N reasoning, the 14 flipped rows revert to OPEN together with
  batch 63's LogFilter/GoToFolder $N rows, which rest on the same reasoning.

## Appendix — OPEN-closing round 2 (2026-11-01, group G10): what was checked, what stays OPEN, and why

- $N count-match: re-verified above (same blobs as round 1). No new layout, Impl body, or bytecode evidence was printed in this
  pass, so the $N labels are unchanged and their revert condition is unchanged.
- OPEN rows 9, 10, 35, 36, 37: checked against the fresh 252-file grep (zero hits, see revision note) and against the local
  layout prints. No printed caller, no printed generated/library rebind body, no saved full-repo grep — therefore OPEN, not
  REACHABLE and not UNREACHABLE. No conditional flip table applies to these rows on current evidence: the only resolver is new
  printed evidence (generated Impl body, library rebind body, or a printed caller for `hasPendingBindings`/`invalidateAll`, or a
  printed registration for Error `onFieldChange`).
- No other row was changed. Counts mechanically re-verified after this edit: 40 rows, sequence 1-40 intact, 35 REACHABLE proposed /
  0 UNREACHABLE / 5 OPEN. Build: not run. C1: not run.
