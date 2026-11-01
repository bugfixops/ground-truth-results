# LibreTorrent batch 64 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 64 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposal (Agent 21,
  `~/workspace/libretorrent-batch64-proposal.md`) was used as an INPUT / lead list only;
  every anchor citation below was re-checked against a fresh connector fetch in this pass,
  and every OPEN row was re-judged against that fresh print (see "Fresh re-check" below).
  No proposal verdict was copied as a result without that re-check.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 64 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/crosscheck/batch_plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-64 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence).
Method names, JVM descriptors, and plan order were checked row-for-row against the table
below in this pass: 40 rows, sequence 1-40 intact, zero mismatches vs the plan.
Groups: DialogSelectTagBindingImpl tail (rows 1-4, continuation of batch 63 rows 36-40),
DrawerEmptyTagsListItemBinding/Impl (rows 5-13), DrawerNoTagsListItemBinding/Impl (rows 14-22),
DrawerTagsListItemBinding/Impl (rows 23-31), FragmentAddTorrentFilesBinding/Impl (rows 32-40).

## Fresh re-check in this pass (branch work-2026-10-31, connector, one file at a time, 20 s pauses)

All paths under `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`,
saved in `~/workspace/b626364-src/`:
- `ui/tag/SelectTagDialog.java` — fresh SHA `a8b228f9…`, 196 lines: DataBindingUtil.inflate dialog_select_tag at :128, initAlertDialog(binding.getRoot()) at :133, binding.tagsList/emptyListView at :139-141. No `setViewModel` / `setVariable` call in the file. Matches the proposal exactly.
- `ui/main/drawer/TagsAdapter.java` — fresh SHA `7fdf6a00…`, 317 lines: onCreateViewHolder at :60, TYPE_EMPTY_ITEM inflate drawer_empty_tags_list_item at :64-69, TYPE_TAG_ITEM inflate drawer_tags_list_item at :73-78, TYPE_NO_TAGS_ITEM inflate drawer_no_tags_list_item at :82-87; ItemViewHolder.bind uses binding.name at :190, binding.color at :191, binding.menu at :198. No `setVariable` or `binding.getViewModel()` call in the file. Matches the proposal exactly.
- `ui/addtorrent/AddTorrentFilesFragment.java` — fresh SHA `2a24bc1e…`, 198 lines: onCreateView at :79, DataBindingUtil.inflate fragment_add_torrent_files at :81, binding.getRoot() at :83, onViewCreated at :128, viewModel field at :61/:134, binding.setViewModel(viewModel) at :135. The fragment uses its own `viewModel` field, never `binding.getViewModel()`. Matches the proposal exactly (proposal cited fileList use at :138/:140, not re-checked line-by-line here; the load-bearing inflate/setViewModel lines are confirmed).
- No fresh HTTP 429 was hit in this pass. Generated Impl bodies, DataBinderMapperImpl, and layout XML are not in `final_java_only`, so every REACHABLE below is INFERRED via standard DataBindingUtil.inflate dispatch, never SOURCE from a printed Impl body.

## Judgement rule (same as the proposal, aligned with batches 63 and 67-68)

- Impl `<clinit>`, both `<init>` overloads, and `executeBindings`: REACHABLE INFERRED whenever the layout's DataBindingUtil.inflate is printed (standard databinding dispatch; framework rebind → executeBindings).
- Abstract `Binding.<init>`: REACHABLE INFERRED (super-call from the Impl constructor, generated pattern).
- `onChangeViewModelInfo` (AddTorrentFiles, row 40): REACHABLE INFERRED — the layout binds `viewModel.info`, `setViewModel` is printed at AddTorrentFilesFragment:135, and the generated field-change chain fires on info notify. NOTE: the Impl's own `onFieldChange` row is NOT in batch 64 (it falls in a later batch, batch 65); the merger must cross-check that row — if it is judged OPEN there, row 40 weakens to OPEN with it. Recorded here, not decided.
- `hasPendingBindings`, `invalidateAll`, `setVariable`: OPEN everywhere in this batch — no printed call to any of them, and their library dispatch was not printed from library source.
- `onFieldChange` for SelectTag and the three drawer Impls: OPEN — those layouts, as used in the freshly printed code, bind no observable variable (SelectTag: view fields only; drawer: direct field reads in bind), so no trigger for `onFieldChange` is printed.
- **UNDECIDED CONVENTION — binding getViewModel (recorded, NOT decided here):** row 33 (FragmentAddTorrentFilesBinding.getViewModel) is left OPEN in this file, because `executeBindings` reads the `mViewModel` field directly, not the getter, and no printed `.getViewModel()` call exists in the freshly printed fragment file. Sibling batches 65-66 marked binding `getViewModel` rows REACHABLE via the generated `executeBindings` read path, flagged weakest by that agent. The merger must pick ONE convention for all binding getters and apply it to batch 63 rows 1/15 and this row 33 together; flipping the convention flips those three rows together and changes no other row's label. This file does NOT decide it.
- Cross-batch consistency: batch 63 rows 36-40 + this batch's rows 1-4 form one DialogSelectTag Impl group — judged together here (Impl creation/rebind REACHABLE INFERRED, hasPendingBindings/invalidateAll/onFieldChange/setVariable OPEN); batch 65's FragmentAddTorrentFiles continuation (including that Impl's `onFieldChange` and any `$N` callback) must agree with row 40 here.
- OPEN is not UNREACHABLE: no Impl body and no full-repo grep was printed.

## Counts — proposed, not verified

- REACHABLE proposed: 21 / 40 (all INFERRED, 0 SOURCE)
- UNREACHABLE proposed: 0
- OPEN: 19 / 40
- Verified for merge: 0

## Per-method table (plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | DialogSelectTagBindingImpl.hasPendingBindings | OPEN | — | No printed caller; see convention above. |
| 2 | DialogSelectTagBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 3 | DialogSelectTagBindingImpl.onFieldChange | OPEN | — | No observable variable set in SelectTagDialog (fields only, :139–141). |
| 4 | DialogSelectTagBindingImpl.setVariable | OPEN | — | No printed `setVariable` call; SelectTagDialog never sets a variable. |
| 5 | DrawerEmptyTagsListItemBinding.<init> | REACHABLE proposed | INFERRED | Super-call from Impl constructor (inflate at TagsAdapter:64–69, TYPE_EMPTY_ITEM). |
| 6 | DrawerEmptyTagsListItemBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, TagsAdapter:64–69. |
| 7 | DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate. |
| 8 | DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 9 | DrawerEmptyTagsListItemBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate. |
| 10 | DrawerEmptyTagsListItemBindingImpl.hasPendingBindings | OPEN | — | No printed caller. |
| 11 | DrawerEmptyTagsListItemBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 12 | DrawerEmptyTagsListItemBindingImpl.onFieldChange | OPEN | — | No observable bound in this layout as used; holder uses binding fields directly (TagsAdapter ItemViewHolder pattern; Empty holder at :227–229). |
| 13 | DrawerEmptyTagsListItemBindingImpl.setVariable | OPEN | — | No printed `setVariable` call in TagsAdapter. |
| 14 | DrawerNoTagsListItemBinding.<init> | REACHABLE proposed | INFERRED | Super-call from Impl constructor (inflate at TagsAdapter:82–87, TYPE_NO_TAGS_ITEM). |
| 15 | DrawerNoTagsListItemBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, TagsAdapter:82–87. |
| 16 | DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate. |
| 17 | DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 18 | DrawerNoTagsListItemBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate. |
| 19 | DrawerNoTagsListItemBindingImpl.hasPendingBindings | OPEN | — | No printed caller. |
| 20 | DrawerNoTagsListItemBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 21 | DrawerNoTagsListItemBindingImpl.onFieldChange | OPEN | — | No observable bound in this layout as used. |
| 22 | DrawerNoTagsListItemBindingImpl.setVariable | OPEN | — | No printed `setVariable` call in TagsAdapter. |
| 23 | DrawerTagsListItemBinding.<init> | REACHABLE proposed | INFERRED | Super-call from Impl constructor (inflate at TagsAdapter:73–78, TYPE_TAG_ITEM). |
| 24 | DrawerTagsListItemBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, TagsAdapter:73–78. |
| 25 | DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate. |
| 26 | DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 27 | DrawerTagsListItemBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate; binding fields used at TagsAdapter:190–198. |
| 28 | DrawerTagsListItemBindingImpl.hasPendingBindings | OPEN | — | No printed caller. |
| 29 | DrawerTagsListItemBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 30 | DrawerTagsListItemBindingImpl.onFieldChange | OPEN | — | No observable bound; bind() reads `binding.name`/`color`/`menu` directly (:190–198). |
| 31 | DrawerTagsListItemBindingImpl.setVariable | OPEN | — | No printed `setVariable` call in TagsAdapter. |
| 32 | FragmentAddTorrentFilesBinding.<init> | REACHABLE proposed | INFERRED | Super-call from Impl constructor (inflate at AddTorrentFilesFragment:81). |
| 33 | FragmentAddTorrentFilesBinding.getViewModel | OPEN | — | No printed `.getViewModel()` call; fragment uses its own `viewModel` field (:113, :134). See getViewModel convention conflict above. |
| 34 | FragmentAddTorrentFilesBindingImpl.<clinit> | REACHABLE proposed | INFERRED | Class load on inflate, AddTorrentFilesFragment:81. |
| 35 | FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View) | REACHABLE proposed | INFERRED | Mapper dispatch on inflate. |
| 36 | FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE proposed | INFERRED | Called by the 2-arg generated constructor. |
| 37 | FragmentAddTorrentFilesBindingImpl.executeBindings | REACHABLE proposed | INFERRED | Framework rebind after inflate / info notify. |
| 38 | FragmentAddTorrentFilesBindingImpl.hasPendingBindings | OPEN | — | No printed caller. |
| 39 | FragmentAddTorrentFilesBindingImpl.invalidateAll | OPEN | — | No printed caller. |
| 40 | FragmentAddTorrentFilesBindingImpl.onChangeViewModelInfo | REACHABLE proposed | INFERRED | Fires on `viewModel.info` ObservableField notify; `setViewModel` printed at AddTorrentFilesFragment:135. Route passes through the Impl's `onFieldChange` row in a later batch — cross-check at merge. |

## Still owed before merge

1. **Strict-entry caveat:** who shows SelectTagDialog, who hosts TagsAdapter
   (drawer fragment/activity step), and who hosts AddTorrentFilesFragment
   (pager/activity step) were NOT printed in this pass, so under a strict
   entry-route rule all 21 REACHABLE rows revert to OPEN.
2. Impl bodies, `DataBinderMapperImpl`, and layout XML were not printed;
   INFERRED labels rest on standard databinding dispatch + generated
   signatures. Re-check `fragment_add_torrent_files.xml` (info binding)
   and the drawer item layouts at merge.
3. Cross-batch consistency required: batch 63 rows 36-40 + this batch's rows 1-4 are one
   SelectTag Impl group, judged together; batch 65's FragmentAddTorrentFiles continuation
   (including that Impl's `onFieldChange` and any `$N` callback) must agree with row 40 here;
   and the `getViewModel` convention (row 33 here, batch 63 rows 1/15, batches 65-66 getters)
   must be settled once for all.
4. Saved full-repo grep for the 19 OPEN rows (`.hasPendingBindings()`, `.invalidateAll()`,
   `.setVariable(...)`, `.getViewModel()`, plus any observable registration that would trigger
   the OPEN `onFieldChange` rows) before any OPEN row is flipped.
5. No build/sampler/grep/C1 is claimed. 0/40 verified for merge. Nothing was pushed, nothing merged.

