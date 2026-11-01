**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 91 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file. No tool coverage, old generated graphs,
or build REACHABLE counts used as evidence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 91 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch91-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against source freshly printed in this pass or against
  the proposal's printed citations where a file was not re-fetched (flagged below),
  and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 91 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header, plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-91 rows are `TODO_CANDIDATE_REACHABLE` in the plan with current label
"REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Plan order preserved below; method names below match the plan exactly, in order.

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31, one file at a time with pauses)

All under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`,
saved in `~/workspace/b9192-src/`:

- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` — fresh, 324 lines. Citations below
  match the proposal's lines exactly (click listeners :110/:111, setListener :112,
  choose-dir result lambda :125, subscribeTags :177, showChooseDirDialog :185,
  onStart :197-202, onStop :205, subscribeAlertDialog :211, showOpenDirErrorDialog :240,
  showEditNameDialog :275, TextWatcher :309/:311/:315/:319).
- `ui/detailtorrent/pages/DetailTorrentStateFragment.java` — fresh, 87 lines. TAG :45,
  newInstance :51-60, onAttach :62, onCreateView :71, onViewCreated :79.
- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` — fresh, 543 lines.
  onCreateView :112, onAttach :120, onDetach :129, onStop :138, onStart :146,
  subscribeAdapter :154, subscribeAlertDialog :170, onViewCreated :193,
  changePriority caller :181, initPriorityDialog caller :178, onItemClicked :333,
  initPriorityDialog :436, changePriority :477, handleOpenFileError :535.
- `ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java` — fresh, 337 lines.
  Used only to confirm the FilesFragment adapter registration (adapter constructed at
  FilesFragment :212, listener interface :254-259, click listeners :166-175 in the
  proposal's print; fresh Adapter print confirms diffCallback :109, areContentsTheSame :112,
  equalsContent call :115 — relevant to batch 92 row 34, not to a batch-91 row).
- `ui/detailtorrent/DetailPagerAdapter.java` — fresh, 76 lines. INFO_FRAG_POS :39,
  STATE_FRAG_POS :40, FILES_FRAG_POS :41, createFragment :53, Info newInstance :56,
  State newInstance :58, Files newInstance :60.

NOT freshly fetched in this pass: `DetailTorrentFragment.java` (pager section) and
`DetailTorrentActivity.java`. The pager anchor therefore rests on DetailPagerAdapter
(fresh) plus the proposal's DetailTorrentFragment :185-186 adapter-set citation, flagged
as carried-forward, not fresh evidence. The launcher -> DetailTorrentActivity ->
DetailTorrentFragment step was NOT printed in this pass — see strict-entry caveat.

## Shared trunk

DetailPagerAdapter.createFragment returns DetailTorrentInfoFragment.newInstance()
(INFO_FRAG_POS), DetailTorrentStateFragment.newInstance() (STATE_FRAG_POS), and
DetailTorrentFilesFragment.newInstance() (FILES_FRAG_POS) — fresh, DetailPagerAdapter :53-60.
ViewPager2 instantiates those fragments; their lifecycle methods then run.

## confirmed_by convention used here — recorded, NOT decided (undecided convention)

- SOURCE: a named method with a printed direct in-app call site, or a fragment
  lifecycle method of a fragment whose pager host is printed above.
- INFERRED: compiler-generated `<init>`/`<clinit>`, anonymous-class/listener callbacks,
  Rx lambdas, and framework dispatch (TextWatcher, SelectionTracker, ActionMode),
  where registration/creation is printed but the dispatching call is not.
- This is the per-row convention. If the merger adopts the whole-route INFERRED
  convention used in some earlier batches (e.g. batch 14), labels are unaffected;
  only the confirmed_by of SOURCE rows whose route crosses unprinted framework/Rx
  dispatch would change to INFERRED. The merger must pick one convention for all
  batches; this file does not decide it.

## Strict-entry caveat — recorded, NOT decided (undecided convention)

The step that creates/shows DetailTorrentFragment itself (e.g. DetailTorrentActivity)
was NOT printed in this pass. Under a strict launcher-entry rule every REACHABLE row
below reverts to OPEN. Labels below are proposed on the pager anchor, as prior detail
batches did. Prior batches 87-88 printed DetailTorrentActivity.onCreate :67-71 as a
lead only; it was NOT re-printed here and is NOT used as fresh evidence in this file.

## Lambda / anonymous numbering — NOT bytecode-verified

FilesFragment lambda numbers match source order exactly: subscribeAdapter $0/$1,
subscribeAlertDialog $2, onItemClicked $3, initPriorityDialog $4/$5, changePriority $6/$7.
InfoFragment anonymous classes match source order: $1 = TorrentTagsList.Listener (:147),
$2 = TextWatcher (:309). Confirm against bytecode at merge if disputed; no bytecode was read.
A swap within a lambda group would not change any label.

## Counts — proposed, NOT verified

- REACHABLE proposed: 40 / 40 (SOURCE 18 / INFERRED 22)
- UNREACHABLE proposed: 0
- OPEN: 0
- Verified for merge: 0

Counts were mechanically verified after writing (40 table rows, sequence 1-40 intact,
in plan order). No UNREACHABLE row is claimed: no saved full-repo grep was run
(connector search_code 0 results are not evidence of absence and were not used),
and no row was flipped to UNREACHABLE.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | DetailTorrentInfoFragment.onStart | REACHABLE | SOURCE | InfoFragment.java:197-202: onStart calls subscribeAlertDialog() :200 and subscribeTags() :201. Fragment created by DetailPagerAdapter (see trunk). |
| 2 | DetailTorrentInfoFragment.onStop | REACHABLE | SOURCE | InfoFragment.java:205-209: onStop clears disposables. Standard fragment lifecycle, pager-hosted. |
| 3 | DetailTorrentInfoFragment.showChooseDirDialog | REACHABLE | SOURCE | InfoFragment.java:110: folderChooserButton click listener calls showChooseDirDialog(); definition :185-194 launches FileManagerDialog via chooseDir. |
| 4 | DetailTorrentInfoFragment.showEditNameDialog | REACHABLE | SOURCE | InfoFragment.java:111: editNameButton click listener calls showEditNameDialog(); definition :275-292 shows BaseAlertDialog TAG_EDIT_NAME_DIALOG. |
| 5 | DetailTorrentInfoFragment.showOpenDirErrorDialog | REACHABLE | SOURCE | InfoFragment.java:125: chooseDir activity-result lambda calls showOpenDirErrorDialog() when result data is null; definition :240-257. |
| 6 | DetailTorrentInfoFragment.subscribeAlertDialog | REACHABLE | SOURCE | InfoFragment.java:200: called from onStart; definition :211-238 subscribes dialogViewModel.observeEvents(). |
| 7 | DetailTorrentInfoFragment.subscribeTags | REACHABLE | SOURCE | InfoFragment.java:201: called from onStart; definition :177-183 subscribes viewModel.observeTags() to binding.tagsList::submit. |
| 8 | DetailTorrentInfoFragment$1.<init> | REACHABLE | INFERRED | Anonymous TorrentTagsList.Listener, field initialiser InfoFragment.java:147; instantiated with the fragment; registration :112 setListener(tagsListener). |
| 9 | DetailTorrentInfoFragment$1.lambda$onAddTagClick$0 | REACHABLE | INFERRED | Map lambda (tag -> tag.id) inside onAddTagClick chain, InfoFragment.java:151-154; Rx map dispatch INFERRED. Lambda numbering by source order, confirm against bytecode if disputed. |
| 10 | DetailTorrentInfoFragment$1.lambda$onAddTagClick$1 | REACHABLE | INFERRED | flatMap lambda (tags -> Observable.fromIterable(tags)...) inside onAddTagClick, InfoFragment.java:151-156; Rx dispatch INFERRED. |
| 11 | DetailTorrentInfoFragment$1.lambda$onAddTagClick$2 | REACHABLE | INFERRED | Subscribe consumer (ids -> SelectTagActivity intent + selectTag.launch), InfoFragment.java:157-165; Rx dispatch INFERRED. |
| 12 | DetailTorrentInfoFragment$1.onAddTagClick | REACHABLE | INFERRED | Listener method InfoFragment.java:149-167; called by TorrentTagsList view via listener registered :112; view dispatch INFERRED. |
| 13 | DetailTorrentInfoFragment$1.onTagRemoved | REACHABLE | INFERRED | Listener method InfoFragment.java:169-174; calls viewModel.removeTag(info); view dispatch INFERRED, registration :112. |
| 14 | DetailTorrentInfoFragment$2.<init> | REACHABLE | INFERRED | Anonymous TextWatcher, created in initEditNameDialog, InfoFragment.java:309; instantiated when edit-name dialog is shown (via :211-238 DIALOG_SHOWN -> initEditNameDialog). |
| 15 | DetailTorrentInfoFragment$2.afterTextChanged | REACHABLE | INFERRED | TextWatcher method InfoFragment.java:319-321: calls checkNameField(s, layoutEditText); EditText framework dispatch INFERRED; listener added :309. |
| 16 | DetailTorrentInfoFragment$2.beforeTextChanged | REACHABLE | INFERRED | TextWatcher method InfoFragment.java:311-312, empty body; EditText calls all three TextWatcher methods on text change, so it runs even though empty; dispatch INFERRED. |
| 17 | DetailTorrentInfoFragment$2.onTextChanged | REACHABLE | INFERRED | TextWatcher method InfoFragment.java:315-316, empty body; same EditText dispatch as row 16, INFERRED. |
| 18 | DetailTorrentStateFragment.<clinit> | REACHABLE | INFERRED | Static TAG field, StateFragment.java:45 (`TAG = ….class.getSimpleName()`, non-constant); class initialiser runs on first active use, i.e. newInstance (row 20). |
| 19 | DetailTorrentStateFragment.<init> | REACHABLE | INFERRED | Compiler-generated constructor, called by newInstance :53 (`new DetailTorrentStateFragment()`); construction site printed, constructor itself compiler-generated. |
| 20 | DetailTorrentStateFragment.newInstance | REACHABLE | SOURCE | StateFragment.java:51-60; called by DetailPagerAdapter.createFragment, STATE_FRAG_POS branch (DetailPagerAdapter.java:58, fresh). |
| 21 | DetailTorrentStateFragment.onAttach | REACHABLE | SOURCE | StateFragment.java:62-69; standard fragment lifecycle, pager-hosted (see trunk). |
| 22 | DetailTorrentStateFragment.onCreateView | REACHABLE | SOURCE | StateFragment.java:71-77; inflates fragment_detail_torrent_state; pager-hosted lifecycle. |
| 23 | DetailTorrentStateFragment.onViewCreated | REACHABLE | SOURCE | StateFragment.java:79-87; obtains DetailTorrentViewModel and binds it; pager-hosted lifecycle. |
| 24 | DetailTorrentFilesFragment.<clinit> | REACHABLE | INFERRED | Static TAG / tag constants, FilesFragment.java:81-85; runs on first active use, i.e. newInstance (row 37). |
| 25 | DetailTorrentFilesFragment.<init> | REACHABLE | INFERRED | Compiler-generated constructor, called by newInstance :103 (`new DetailTorrentFilesFragment()`). |
| 26 | DetailTorrentFilesFragment.changePriority | REACHABLE | SOURCE | FilesFragment.java:477-507; called from subscribeAlertDialog POSITIVE_BUTTON_CLICKED branch :184-186 (via :170-191 switch). |
| 27 | DetailTorrentFilesFragment.handleOpenFileError | REACHABLE | SOURCE | FilesFragment.java:535-542; method reference `this::handleOpenFileError` as error consumer in onItemClicked subscribe, :344-348. |
| 28 | DetailTorrentFilesFragment.initPriorityDialog | REACHABLE | SOURCE | FilesFragment.java:436-475; called from subscribeAlertDialog DIALOG_SHOWN branch :178-180. |
| 29 | DetailTorrentFilesFragment.lambda$changePriority$6 | REACHABLE | INFERRED | Map lambda (selection -> selection.name) in changePriority, FilesFragment.java:496-498; Rx map dispatch INFERRED. Numbering by source order (see below). |
| 30 | DetailTorrentFilesFragment.lambda$changePriority$7 | REACHABLE | INFERRED | Subscribe consumer (fileNames -> viewModel.applyPriority) in changePriority, FilesFragment.java:499; Rx dispatch INFERRED. |
| 31 | DetailTorrentFilesFragment.lambda$initPriorityDialog$4 | REACHABLE | INFERRED | Map lambda (selection -> selection.name) in initPriorityDialog, FilesFragment.java:442-444; Rx map dispatch INFERRED. |
| 32 | DetailTorrentFilesFragment.lambda$initPriorityDialog$5 | REACHABLE | INFERRED | Subscribe consumer (fileNames -> getFilesPriority / radio check) in initPriorityDialog, FilesFragment.java:445-473; Rx dispatch INFERRED. |
| 33 | DetailTorrentFilesFragment.lambda$onItemClicked$3 | REACHABLE | INFERRED | Subscribe success consumer (path -> openFile(item.name, path)) in onItemClicked, FilesFragment.java:343-346; Rx dispatch INFERRED. |
| 34 | DetailTorrentFilesFragment.lambda$subscribeAdapter$0 | REACHABLE | INFERRED | flatMapSingle lambda (children -> Flowable.fromIterable.map(TorrentContentFileItem::new).toList()) in subscribeAdapter, FilesFragment.java:156-161 (fresh: map at :160); Rx dispatch INFERRED. |
| 35 | DetailTorrentFilesFragment.lambda$subscribeAdapter$1 | REACHABLE | INFERRED | Subscribe consumer (children -> adapter.submitList + updateFileSize) in subscribeAdapter, FilesFragment.java:162-165; Rx dispatch INFERRED. |
| 36 | DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2 | REACHABLE | INFERRED | Subscribe consumer (event -> dialog switch) in subscribeAlertDialog, FilesFragment.java:171-190; Rx dispatch INFERRED. |
| 37 | DetailTorrentFilesFragment.newInstance | REACHABLE | SOURCE | FilesFragment.java:101-108; called by DetailPagerAdapter.createFragment, FILES_FRAG_POS branch (DetailPagerAdapter.java:60, fresh). |
| 38 | DetailTorrentFilesFragment.onAttach | REACHABLE | SOURCE | FilesFragment.java:120-127; standard fragment lifecycle, pager-hosted. |
| 39 | DetailTorrentFilesFragment.onCreateView | REACHABLE | SOURCE | FilesFragment.java:112-117; inflates fragment_detail_torrent_files; pager-hosted lifecycle. |
| 40 | DetailTorrentFilesFragment.onDetach | REACHABLE | SOURCE | FilesFragment.java:129-135; finishes actionMode if present; pager-hosted lifecycle. |

## What is NOT claimed / still owed

- No UNREACHABLE row: no saved full-repo grep was run (connector search_code 0 results
  are not evidence of absence and were not used).
- Strict-entry step (launcher -> DetailTorrentActivity -> DetailTorrentFragment) not freshly
  printed; see caveat above — under a strict rule all 40 REACHABLE rows revert to OPEN.
- DetailTorrentFragment adapter-set step (:185-186) is carried forward from the prior
  proposal, not freshly printed here; re-print it at merge if the merger requires it fresh.
- Build, sampler, C1, and full-repo grep all still owed on a full checkout (git clone
  fails in this VM; named missing check, not passed).
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — not run.
- 0/40 verified for merge. Nothing merged, nothing pushed. No fresh HTTP 429 was hit
  in this pass.
