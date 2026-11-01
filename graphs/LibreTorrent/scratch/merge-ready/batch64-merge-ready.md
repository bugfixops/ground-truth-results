**REVISION 2026-11-01 (OPEN-closing round 2, group G10): 0 rows flipped. Counts unchanged: 21/0/19.**
Backed up first to `~/workspace/libretorrent-merge-backup-pre-openclose2/batch64-merge-ready.md` (md5-identical to the pre-edit file).
No GitHub connector fetch was needed or made in this pass (all needed files were already local), so no 429 was hit. Nothing was pushed.
Fresh source for this pass: `~/workspace/b626364-openclose2-src/` (copies of the round-1 layout files + a fresh grep file).
Layouts re-verified on the SAME blobs as round 1 (connector blob SHAs, identical to round 1): dialog_select_tag.xml blob
`cf0ea57e234559a5d672b2c46799e6831906b5e`, 25 lines, NO `<data>` block, 0 `@={}`; drawer_empty_tags_list_item.xml blob
`9047da67d793119752ffc8820d34f83ef190c2e4`, 34 lines, NO `<data>` block; drawer_no_tags_list_item.xml blob
`dedb665d326cdd64d563428de28d4bbe26233f2c`, 34 lines, NO `<data>` block; drawer_tags_list_item.xml blob
`e37cfcce9a2e9d75a395a92182d884702eb01ac0`, 50 lines, NO `<data>` block; fragment_add_torrent_files.xml blob
`68e992ff7822c03d8a62c51484e014c8807ef7b7`, 59 lines, `viewModel` variable declared, ONE-WAY bindings only
(`viewModel.info.fileCount` at :25/:49/:57, `viewModel.mutableParams.storageFreeSpace` at :33), 0 `@={}` — consistent with this
Impl having no $N rows in batch 64.
Fresh corpus grep re-run in this pass (`b626364-openclose2-src/grep_ruleF_corpus_626364_round2.txt`, 252 app Java files in
`~/workspace/ruleF-src`): ZERO hits for `hasPendingBindings`, `invalidateAll`, `setVariable`, `getViewModel`, `onFieldChange`,
`executePendingBindings`. That grep is app-Java-tree only (generated Impl bodies absent), so it flips NOTHING. No generated
`*BindingImpl` body, `DataBinderMapperImpl`, or androidx `ViewDataBinding` library body was found locally.
Rows still OPEN (19, unchanged): 1, 2, 3, 4 (SelectTag); 10, 11, 12, 13 (Empty drawer); 19, 20, 21, 22 (NoTags drawer);
28, 29, 30, 31 (Tags drawer); 33 (`getViewModel`, convention (v)); 38, 39 (AddTorrentFiles `hasPendingBindings`/`invalidateAll`).
Full conditional tables are in the appendix — `setVariable` contradiction (xv) and `getViewModel` convention (v) are NOT decided
here. No row was flipped to UNREACHABLE: no saved full-repo grep exists, and zero hits in a partial corpus alone never flip a row.
DEPENDENCY (unchanged, recorded not decided): row 40 (`onChangeViewModelInfo`, REACHABLE proposed, INFERRED) routes through
FragmentAddTorrentFilesBindingImpl.`onFieldChange`, which is batch 65 row 2 (currently REACHABLE proposed, INFERRED, on
AddTorrentFilesFragment:81 inflate + :135 `setViewModel` + the layout bindings above). If batch 65 row 2 reverts to OPEN for any
reason, row 40 reverts to OPEN with it. Row 40 does NOT independently support batch 65 row 2. Build: not run. C1: not run.
FLAG (not decided here): batches 63/64/65 MUST use ONE `setVariable` rule, and the merger should also settle ONE `invalidateAll`
rule — batch 65 marks `invalidateAll` REACHABLE on inflate (batch 65 rows 12, 23, 34) while batch 64 keeps `invalidateAll` OPEN on
the same inflate evidence. This pass changes neither side.

**REVISION 2026-11-01 (OPEN-closing pass): 0 rows flipped. Counts unchanged: 21/0/19.**
Fresh layouts printed in this pass (~/workspace/b626364-openclose-src/): dialog_select_tag.xml (25 lines, SHA cf0ea57e…;
NO <data> block — batch 63 rows 36-40 + these rows 1-4 form one SelectTag Impl group, judged consistently: hasPendingBindings /
invalidateAll / onFieldChange / setVariable all stay OPEN), drawer_empty_tags_list_item.xml (34 lines, SHA 9047da67…),
drawer_no_tags_list_item.xml (34 lines, SHA dedb665d…), drawer_tags_list_item.xml (50 lines, SHA e37cfcce…; all three with
NO <data> block — drawer onFieldChange rows 12, 21, 30 and setVariable rows 13, 22, 31 have no observable/variable trigger
printed, but per the undecided no-variable-layout rule (xv) they stay OPEN, not UNREACHABLE), fragment_add_torrent_files.xml
(59 lines, SHA 68e992ff…; viewModel variable, one-way bindings only: info.fileCount :25/:49/:57, mutableParams.storageFreeSpace :33,
no @={} — consistent with this Impl having no $N rows in the plan).
Corpus grep (grep_ruleF_corpus_626364.txt, full 252-file app-Java tree, NOT full-repo): zero hits for `.hasPendingBindings(`,
`.invalidateAll(`, `.setVariable(`, `.getViewModel()`. This confirms no printed app caller for rows 1, 2, 4, 10, 11, 13, 19, 20,
22, 28, 29, 31, 33, 38, 39, but does NOT flip them: framework-internal calls are unprinted; row 33 additionally rests on the
undecided binding-getViewModel convention (v), NOT decided here. Note for the merger: batch 65 treats this Impl family's
setVariable as REACHABLE via "dispatch behind setViewModel", which is mechanically backwards (generated setVariable CALLS
the typed setter, not vice versa); batches 63-64 keep setVariable OPEN, and the merger must pick ONE rule for all.
Host step: AddTorrentActivity:288-289 sets AddTorrentPagerAdapter on the viewpager; the adapter creates
AddTorrentFilesFragment at FILES_FRAG_POS (corpus AddTorrentPagerAdapter.java:41-46). Counts before and after: 21/0/19.
Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 64 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
5. No build/sampler/grep/C1 is claimed. 0/40 verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]), nothing merged.

## Appendix — OPEN-closing round 2 (2026-11-01, group G10): CONDITIONAL flip tables (NOT decisions)

No convention is decided in this file. Each table states exactly which rows flip under each option, so the merger can apply ONE
rule project-wide. On current evidence (no printed generated/library body, no saved full-repo grep) every OPEN row below stays OPEN.

### (v) Binding `getViewModel` — row 33 (FragmentAddTorrentFilesBinding.getViewModel)

| Merger option | Row 33 becomes | Companion rows affected |
|---|---|---|
| Adopt the executeBindings-read-path rule | REACHABLE proposed, INFERRED | Batch 63 rows 1, 15 flip the same way; batch 62 rows 4, 30 are ALREADY REACHABLE on this rule (no change there) |
| Reject the read-path rule, keep OPEN (current position of this file) | OPEN (no change) | Batch 62 rows 4, 30 would revert to OPEN if the rule is rejected project-wide (merger decision, not made here) |
| Reject the read-path rule AND accept a saved full-repo grep showing zero `.getViewModel()` callers as trigger-absence | UNREACHABLE, `no_trigger_in_app` | NOT available now: no full-repo grep has been saved; the 252-file app-Java-tree zero alone is insufficient |

Resolver for (v): a printed generated Impl body showing whether `executeBindings` calls the getter or reads the field directly, or a
printed `.getViewModel()` caller, or a saved full-repo grep — plus one project-wide merger decision. Printed app code for this
binding uses its own `viewModel` field (AddTorrentFilesFragment:61/:134, `setViewModel` at :135), never `binding.getViewModel()`.

### (xv) `setVariable` — rows 4 (SelectTag), 13 (Empty drawer), 22 (NoTags drawer), 31 (Tags drawer)

These four Impls have NO variable set in printed app code at all: SelectTagDialog sets no variable (it uses binding fields only,
:139-141), and TagsAdapter sets no variable (it reads `binding.name`/`color`/`menu` directly, :190-198). Their layouts declare NO
`<data>` block (verified above). Zero `.setVariable(` hits in the 252-file corpus.

| Merger option | Rows 4, 13, 22, 31 become | Why |
|---|---|---|
| Rule A — current batches 63/64 rule: `setVariable` needs a printed `.setVariable(` call site | OPEN (no change) | Batch 63 `setVariable` rows 10, 24 stay OPEN too; batch 65 `setVariable` rows 3, 16, 27, 38 would revert to OPEN |
| Rule B — batch 65 rule as written: "`setVariable` is the generated dispatch point behind `binding.setViewModel`" | OPEN (no change — NONE of the four flips) | Rule B requires a printed `setViewModel` call for the same Impl, and none exists for SelectTag or any drawer Impl. Applying Rule B to batch 64 therefore flips nothing here, even though it would flip batch 63 rows 10, 24 — the ONE-rule decision has different effects per batch, and the merger must not apply Rule B blindly to batch 64 |
| Rule C — generic-framework-callback rule: any Impl `setVariable` is reachable via framework/generated dispatch despite zero app calls | REACHABLE proposed, INFERRED (all four) | Broader than Rule B; must be adopted explicitly. Note the mechanical objection to Rule B still stands: in generated code `setVariable` CALLS the typed setter, not vice versa |

Batches 63, 64, and 65 MUST use ONE `setVariable` rule. This file does not pick one. Batch 65 `setVariable` rows 3, 16, 27, 38 use the
Rule-B wording ("generated dispatch point behind binding.setViewModel(:135/:103)"); under Rule A they revert to OPEN, under Rule B
they stay REACHABLE, under Rule C they stay REACHABLE.

### `onFieldChange` for no-variable layouts — rows 3 (SelectTag), 12 (Empty drawer), 21 (NoTags drawer), 30 (Tags drawer)

Layouts declare NO `<data>` block and bind no observable variable, so no trigger for `onFieldChange` is printed. Current position:
OPEN (not UNREACHABLE — the Impl body is unprinted, and no saved full-repo grep exists). Under the generic-framework-callback rule
(Rule C above) all four would flip to REACHABLE proposed, INFERRED as framework callbacks. Under a no-trigger rule backed by a saved
full-repo grep + printed Impl body they could flip to UNREACHABLE `no_trigger_in_app` — that evidence does not exist now, so no
UNREACHABLE flip is made. The merger must judge these four together with batch 66 rows 5/7/8/10 and batch 67 row 40 / batch 68
row 1 (same no-variable question, recorded in batch 65's caveats).

### `hasPendingBindings` / `invalidateAll` — rows 1, 2, 10, 11, 19, 20, 28, 29, 38, 39: NO conditional flip on current evidence

No merger option flips these rows without new printed evidence: zero corpus hits prove no app caller, but framework-internal calls
are unprinted, and no generated/library body was found locally. Resolver: a printed generated Impl body or printed androidx
`ViewDataBinding` library body showing the `hasPendingBindings`/`invalidateAll` call path, or a printed caller. Separately, the
merger must pick ONE `invalidateAll` rule: batch 65 treats `invalidateAll` as REACHABLE on inflate, this batch treats it as OPEN.

### DEPENDENCY — row 40 (`FragmentAddTorrentFilesBindingImpl.onChangeViewModelInfo`, REACHABLE proposed, INFERRED, UNCHANGED)

Row 40's route passes through the same Impl's `onFieldChange`, which is batch 65 row 2 (currently REACHABLE proposed, INFERRED:
AddTorrentFilesFragment:81 `DataBindingUtil.inflate(fragment_add_torrent_files)`, :135 `binding.setViewModel(viewModel)`, layout
binds `viewModel.info.fileCount` and `viewModel.mutableParams.storageFreeSpace`; observables are `AddTorrentViewModel.info`
(ObservableField) and `mutableParams` (BaseObservable) per batch 65 row 2). Companion batch 65 rows: row 1
(`onChangeViewModelMutableParams`, REACHABLE) and row 3 (`setVariable`, REACHABLE under Rule B, OPEN under Rule A — see above).
If batch 65 row 2 reverts to OPEN (strict-entry revert, convention change, or re-check), batch 64 row 40 reverts to OPEN with it.
This pass does not change row 40 or any batch 65 row.

### Cross-batch consistency (unchanged)

Batch 63 rows 36-40 + this batch's rows 1-4 are one DialogSelectTag Impl group, judged together (Impl creation/rebind REACHABLE
INFERRED in batch 63, `hasPendingBindings`/`invalidateAll`/`onFieldChange`/`setVariable` OPEN here). Counts mechanically
re-verified after this edit: 40 rows, sequence 1-40 intact, 21 REACHABLE proposed / 0 UNREACHABLE / 19 OPEN. Build: not run.
C1: not run.
