# UNVERIFIED merge-ready part — NOT merged, NOT verified for merge

# LibreTorrent batch 119 — merge-ready part

**UNVERIFIED — NOT merged. No build, sampler, grep, or C1 count is claimed. Build: not run. C1: not run (Mac after push, never claimed passed).**
Connector-only work (GitHub connector, branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`). No token, no local checkout, no push, no edit to `graph_def.py` / `out` / progress / `tools` / another helper's file. Fresh source saved in `~/workspace/b119120-src/` (connector JSON kept alongside each file). No `search_code` result was used anywhere, and no `search_code` 0 was used as evidence of absence. No row is UNREACHABLE: no saved full-repo grep was run in this pass, so absence of a printed caller would be OPEN, never `no_trigger_in_app`.

## Membership

All 40 rows below are batch 119 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (git blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), each `TODO_CANDIDATE_REACHABLE`, in plan-file order. Method names and JVM descriptors were generated from the plan file, so they cannot drift from it. Batch 120 is the final partial batch (3 rows, not 40); there is no batch 121 in the plan.

## Source files printed fresh in this pass (branch `work-2026-10-31`, one file at a time with ~25 s pauses, no fresh HTTP 429)

Base path `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`:

- `ui/tag/SelectTagDialog.java` — 195 lines, SHA-256 `6bd18c14d10c…` (`STD`)
- `ui/tag/SelectTagViewModel.java` — 65 lines, SHA-256 `33400e242548…` (`STVM`)
- `ui/tag/TagItem.java` — 60 lines, SHA-256 `f66d426d3885…` (`TI`)
- `ui/tag/TagsAdapter.java` — 111 lines, SHA-256 `bc9e1999802d…` (`TA`)
- `ui/tag/TorrentTagsList.java` — 94 lines, SHA-256 `212d270d1c9e…` (`TTL`)
- `ui/tag/SelectTagActivity.java` — 71 lines, SHA-256 `e9b089e670a3…` (`STA`)
- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` — 323 lines, SHA-256 `d7d8ba7388df…` (`DTIF`)
- `ui/detailtorrent/DetailPagerAdapter.java` — 76 lines, SHA-256 `4b86db783c80…` (`DPA`)
- Layout `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/res/layout/fragment_detail_torrent_info.xml` — 346 lines, SHA-256 `eab667fec562…`

Line-count differences of 1 vs the input proposals (196/72/324) are trailing-newline counting differences only; every cited line was re-checked against the fresh files, and every proposal citation held exactly (see "Changes vs input proposals" below).

## Printed route anchors (re-derived fresh, not copied)

**Tags-list direction (detail screen):** `DPA.createFragment` INFO_FRAG_POS (:39, case :55-56) returns `DetailTorrentInfoFragment.newInstance()` → `DTIF.onCreateView` :100 inflates `R.layout.fragment_detail_torrent_info` → fresh layout :150-154 declares `TorrentTagsList` with `android:id="@+id/tags_list"` (:151), so `binding.tagsList` is the layout-inflated `TorrentTagsList` → DTIF :112 `binding.tagsList.setListener(tagsListener)` → `DTIF.onStart` :197-201 calls `subscribeTags()` :201 → :181 `.subscribe(binding.tagsList::submit)` → `TTL.submit` → `TTL.buildChip`.

**Tag-pick direction (dialog):** `DTIF.tagsListener.onAddTagClick` :149-165 builds an Intent for `SelectTagActivity` (:158) and launches it via `selectTag` :163 → `STA.onCreate` :42-53: :51 `SelectTagDialog.newInstance(excludeTagsId)`, :52 `dialog.show(fm, TAG_DIALOG)` → DialogFragment lifecycle (`STD.onAttach`, `onCreateDialog`, `onResume`, `onStart`, `onStop`) → `STD.onCreateDialog` :130 `new TagsAdapter(this)`, :132 `initLayoutView()`, :133 `initAlertDialog(...)` → `STD.onStart` :103 `subscribeTags()` → `STVM.observeTags()` → Rx `filter(viewModel::filterExcludeTags)` → `map(TagItem::new)` → `adapter::submitList` (ListAdapter) → DiffUtil → `TA.$1.areItemsTheSame/areContentsTheSame` → `TI.isSame/equals` → row click → `TA.ViewHolder.lambda$bind$0` → `STD.onTagClicked` :179-184 → `finish(...)` → `STA.onFragmentFinished` :57-66 (RESULT_OK, finish). `STA.onBackPressed` :70 also calls `STD.onBackPressed` directly. The pick result returns to `DTIF.selectTag` :132-145, which reads `SelectTagActivity.TAG_RESULT_SELECTED_TAG` :137 and calls `viewModel.addTag(tag)` :139 (that ViewModel method is not a batch-119/120 row).

**Strict-entry caveat (explicit, recorded not decided):** who starts `DetailTorrentActivity` / `DetailTorrentFragment`, and the launcher step into it, were NOT printed in this pass. Under a strict launcher-entry rule all REACHABLE rows below revert to OPEN. The labels below are proposed under the anchor-at-detail-fragment convention used by the sibling detail batches, not under the strict rule. The fresh layout print narrows but does not close this gap: it proves the `tagsList` attachment, not the launcher step.

## confirmed_by convention (stated, so the merger can reconcile it)

- **SOURCE** = at least one direct app-to-app call site for the method is printed in app source (including a printed lambda body calling it).
- **INFERRED** = the method is only reached through a dispatch not printed from app/fw source: DialogFragment/Activity/Fragment lifecycle, RecyclerView, DiffUtil, view-click / key / show listeners, Rx method references and lambdas, `ViewModelProvider.get`, or layout inflation. Framework/library source itself was not printed, so those steps are INFERRED, not SOURCE.
- This is the per-row convention; it differs from whole-route INFERRED used in some earlier batches (e.g. batch 14). Labels are unaffected by the difference; only `confirmed_by` would change at merge if the merger adopts the whole-route convention.

## Lambda / anonymous-class numbering (NOT bytecode-verified)

- `STD`: `lambda$onResume$0` = key listener (:87, `(DialogInterface,int,KeyEvent)Z`); `lambda$initAlertDialog$3` = `OnShowListener` (:153, `(DialogInterface)V`, the only DialogInterface lambda in that method — descriptor-pinned); `lambda$initAlertDialog$1` = new-tag button click (:156-158, registered first) and `$2` = cancel button click (:159-161, registered second), both `(View)V` — `$1`/`$2` assignment is by registration order, merger must confirm against bytecode. Note the OnShowListener lambda is registered before the button lambdas in source (:153 vs :156/:159) yet carries the higher number $3; the $1/$2 swap, if wrong, changes no label (both are click lambdas on the same dialog).
  `lambda$subscribeTags$4` = `flatMapSingle` function (:169, `(List)SingleSource`).
- `TA.$1` = the anonymous `DiffUtil.ItemCallback` in the static `diffCallback` field (:65-82); its two methods are the plan rows.
- `TA.ViewHolder.lambda$bind$0` = the only lambda in `bind` (:104-108).
- `TTL`: `lambda$buildChip$0` = close-icon click lambda (:69-73); `lambda$buildAddTagButton$1` = add-tag button click lambda (:80-84). File order (buildChip before buildAddTagButton) matches $0 before $1.

## Per-row verdicts (plan order)

| # | Method | Descriptor | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|---|
| 1 | SelectTagDialog.<init> | `()V` | REACHABLE | SOURCE | Implicit default ctor; STD.newInstance :64 `new SelectTagDialog()`; newInstance called from STA.onCreate :51. |
| 2 | SelectTagDialog.finish | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | REACHABLE | SOURCE | Private method STD :191-194; direct callers :160 (cancel lambda, via finish CANCEL), :183 (onTagClicked), :188 (onBackPressed). |
| 3 | SelectTagDialog.initAlertDialog | `(Landroid/view/View;)V` | REACHABLE | SOURCE | STD :144-163; called from onCreateDialog :133. |
| 4 | SelectTagDialog.initLayoutView | `()V` | REACHABLE | SOURCE | STD :138-142; called from onCreateDialog :132. |
| 5 | SelectTagDialog.lambda$initAlertDialog$1 | `(Landroid/view/View;)V` | REACHABLE | INFERRED | New-tag click lambda STD :156-158 (setOnClickListener, starts AddTagActivity); view-click dispatch not printed. |
| 6 | SelectTagDialog.lambda$initAlertDialog$2 | `(Landroid/view/View;)V` | REACHABLE | INFERRED | Cancel click lambda STD :159-161 (setOnClickListener, calls finish(..., CANCEL)); view-click dispatch not printed. |
| 7 | SelectTagDialog.lambda$initAlertDialog$3 | `(Landroid/content/DialogInterface;)V` | REACHABLE | INFERRED | OnShowListener lambda STD :153-162 (setOnShowListener); framework show dispatch not printed. Descriptor-pinned: only (DialogInterface)V lambda in the method. |
| 8 | SelectTagDialog.lambda$onResume$0 | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | REACHABLE | INFERRED | Key listener lambda STD :87-96 (setOnKeyListener); calls onBackPressed() :90 on BACK + ACTION_DOWN; framework key dispatch not printed. |
| 9 | SelectTagDialog.lambda$subscribeTags$4 | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | REACHABLE | INFERRED | flatMapSingle lambda STD :169-173 (filter + TagItem::new + toList); Rx dispatch not printed. |
| 10 | SelectTagDialog.newInstance | `([J)Lorg/proninyaroslav/libretorrent/ui/tag/SelectTagDialog;` | REACHABLE | SOURCE | STD :63-71; called from STA.onCreate :51. |
| 11 | SelectTagDialog.onAttach | `(Landroid/content/Context;)V` | REACHABLE | INFERRED | STD :74-80; DialogFragment lifecycle, no app call site printed. |
| 12 | SelectTagDialog.onBackPressed | `()V` | REACHABLE | SOURCE | STD :186-189; direct callers STA.onBackPressed :70 and key lambda :90. |
| 13 | SelectTagDialog.onCreateDialog | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | REACHABLE | INFERRED | STD :115-136; DialogFragment lifecycle, no app call site printed; body calls provider.get(SelectTagViewModel.class) :121, setExcludeTagsId :123, new TagsAdapter :130, init methods :132-133. |
| 14 | SelectTagDialog.onResume | `()V` | REACHABLE | INFERRED | STD :83-97; DialogFragment lifecycle; body registers key listener :87. |
| 15 | SelectTagDialog.onStart | `()V` | REACHABLE | INFERRED | STD :100-104; DialogFragment lifecycle; body calls subscribeTags() :103. |
| 16 | SelectTagDialog.onStop | `()V` | REACHABLE | INFERRED | STD :107-111; DialogFragment lifecycle; body disposables.clear() :110. |
| 17 | SelectTagDialog.onTagClicked | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)V` | REACHABLE | SOURCE | STD :179-184; called from TA.ViewHolder.bind lambda body :106 `listener.onTagClicked(item)` (listener = this dialog, passed at STD :130). |
| 18 | SelectTagDialog.subscribeTags | `()V` | REACHABLE | SOURCE | STD :165-176; called from onStart :103; body :166 viewModel.observeTags(), :174 adapter::submitList. |
| 19 | SelectTagViewModel.<init> | `(Landroid/app/Application;)V` | REACHABLE | INFERRED | STVM :41-45; reached only via ViewModelProvider.get(SelectTagViewModel.class) at STD :121 — library dispatch, no app `new` printed. |
| 20 | SelectTagViewModel.filterExcludeTags | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Z` | REACHABLE | INFERRED | STVM :58-60; reached only via Rx method reference viewModel::filterExcludeTags at STD :170; Rx dispatch not printed. |
| 21 | SelectTagViewModel.observeTags | `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | STVM :62-64 (tagRepo.observeAll()); called directly at STD :166. |
| 22 | SelectTagViewModel.setExcludeTagsId | `([J)V` | REACHABLE | SOURCE | STVM :47-56; called directly at STD :123-124 from arguments. |
| 23 | tag.TagItem.<init> | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | TI :30-32; reached only via Rx method reference TagItem::new at STD :171; Rx dispatch not printed. ui/tag TagItem, NOT drawer.TagItem (batch 113) and NOT tag.TagItem of batch 11. |
| 24 | tag.TagItem.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | TI :39-46; called directly at TA :72 `oldItem.equals(newItem)` in areContentsTheSame. |
| 25 | tag.TagItem.isSame | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | REACHABLE | SOURCE | TI :34-36; called directly at TA :80 `oldItem.isSame(newItem)` in areItemsTheSame. |
| 26 | tag.TagsAdapter.<clinit> | `()V` | REACHABLE | INFERRED | Static diffCallback field TA :65-82; runs on class load, triggered by `new TagsAdapter(this)` at STD :130; no source method body printed for <clinit> itself. First-use convention (ix) — recorded, not decided. |
| 27 | tag.TagsAdapter.<init> | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;)V` | REACHABLE | SOURCE | TA :38-42 (super(diffCallback)); called at STD :130. |
| 28 | tag.TagsAdapter.onBindViewHolder | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$ViewHolder;I)V` | REACHABLE | INFERRED | TA :58-63; RecyclerView framework call, no app call site printed; body :61 holder.bind(item, listener). |
| 29 | tag.TagsAdapter.onCreateViewHolder | `(Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$ViewHolder;` | REACHABLE | INFERRED | TA :46-55; RecyclerView framework call, no app call site printed; body :54 new ViewHolder(binding). |
| 30 | tag.TagsAdapter$1.<init> | `()V` | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback TA :65-66; instantiated implicitly by the static field initialiser; no explicit `new $1()` printed. |
| 31 | tag.TagsAdapter$1.areContentsTheSame | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | REACHABLE | INFERRED | TA :68-73; called only by DiffUtil during submitList (from STD :174); DiffUtil dispatch not printed; body calls TagItem.equals :72. |
| 32 | tag.TagsAdapter$1.areItemsTheSame | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;)Z` | REACHABLE | INFERRED | TA :76-81; called only by DiffUtil during submitList; DiffUtil dispatch not printed; body calls TagItem.isSame :80. |
| 33 | tag.TagsAdapter$ViewHolder.<init> | `(Lorg/proninyaroslav/libretorrent/databinding/TagsListItemBinding;)V` | REACHABLE | SOURCE | TA :92-96; called at onCreateViewHolder :54. |
| 34 | tag.TagsAdapter$ViewHolder.bind | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;)V` | REACHABLE | SOURCE | TA :98-109; called at onBindViewHolder :61; body :104 registers click listener, :106 calls listener.onTagClicked. |
| 35 | tag.TagsAdapter$ViewHolder.lambda$bind$0 | `(Lorg/proninyaroslav/libretorrent/ui/tag/TagsAdapter$OnClickListener;Lorg/proninyaroslav/libretorrent/ui/tag/TagItem;Landroid/view/View;)V` | REACHABLE | INFERRED | Click lambda TA :104-108; view-click dispatch not printed. |
| 36 | TorrentTagsList.<init>(Context,AttributeSet) | `(Landroid/content/Context;Landroid/util/AttributeSet;)V` | REACHABLE | INFERRED | TTL :29-33 (super(context, attrs), init(context) :32); layout-inflation ctor — fresh layout fragment_detail_torrent_info.xml:150-154 declares TorrentTagsList with android:id=@+id/tags_list (:151), and DTIF :100 inflates that layout, :112 uses binding.tagsList; the ctor call itself is LayoutInflater framework dispatch, not printed app code, so INFERRED (evidence strengthened vs the proposal, which had no layout print; label unchanged). (The 1-arg ctor TTL :23-27 is NOT a batch-119 row and is not judged here.) |
| 37 | TorrentTagsList.buildAddTagButton | `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/ui/tag/AddTagButton;` | REACHABLE | SOURCE | TTL :78-87; called from init :36. |
| 38 | TorrentTagsList.buildChip | `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lcom/google/android/material/chip/Chip;` | REACHABLE | SOURCE | TTL :54-76; called from submit :49. |
| 39 | TorrentTagsList.init | `(Landroid/content/Context;)V` | REACHABLE | SOURCE | TTL :35-38; called from the 2-arg ctor :32 (and from the 1-arg ctor :26, not judged here). |
| 40 | TorrentTagsList.lambda$buildAddTagButton$1 | `(Landroid/view/View;)V` | REACHABLE | INFERRED | Click lambda TTL :80-84 (setOnClickListener, calls listener.onAddTagClick() :82 -> DTIF.tagsListener :149); view-click dispatch not printed. |

## Counts

- **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN** (REACHABLE: SOURCE 18 / INFERRED 22).
- Verified for merge: **0 / 40** (merge-ready part only; build/sampler/grep/C1 not run).

## Changes vs input proposals

- **No label changed vs the input proposal (40/0/0, SOURCE 18 / INFERRED 22, unchanged).** Every proposal citation was re-checked against the fresh prints and held exactly — including all SelectTagDialog, TagsAdapter, TagItem, SelectTagViewModel, TorrentTagsList, SelectTagActivity, DetailTorrentInfoFragment, and DetailPagerAdapter line numbers.
- **Evidence strengthened, label and confirmed_by unchanged:** the input proposal's blocker 1 is resolved — `fragment_detail_torrent_info.xml` was fetched fresh in this pass (:150-154 declares `TorrentTagsList` with `android:id="@+id/tags_list"` :151), confirming the `binding.tagsList` attachment for batch 119 row 36. Row 36 stays INFERRED (LayoutInflater framework dispatch, not printed app code), consistent with the batch 94 PiecesView 2-arg precedent.
- **Numbering note added (labels unaffected):** the OnShowListener lambda is registered before the button lambdas in source (:153 vs :156/:159) yet carries number $3; $3 is descriptor-pinned (only `(DialogInterface)V` lambda in the method), while $1/$2 rest on registration order and need bytecode confirmation.

## Not judged here (do not merge from this file)

- `tag.TagItem.hashCode` / `toString` (`TI` :49-51, :55-60): not batch-119/120 rows; no verdict is offered for them. In particular `TagItem.equals` being REACHABLE does not by itself make `hashCode` reachable, and no printed caller for `hashCode`/`toString` was sought in this pass.
- `TorrentTagsList.<init>(Context)` (1-arg, `TTL` :23-27): not a batch-119/120 row; not judged here. (Batch 11 judged it separately; do not copy that verdict here.)
- `SelectTagDialog.finish`'s downstream `FragmentCallback.onFragmentFinished` and `DetailTorrentViewModel.addTag/removeTag/getTags/observeTags`: not batch-119/120 rows; cited only as route context.
- `drawer.TagItem` (batch 113 special item) and batch 11's `tag.TagItem` rows: different classes from batch 119's ui/tag `TagItem`; no verdict was copied between any of them.

## Caveats the merger must see (recorded, NOT decided)

1. Strict-entry (see route anchors above): under a strict launcher-entry rule all REACHABLE rows revert to OPEN.
2. confirmed_by per-row vs whole-route (see convention above): under whole-route INFERRED, SOURCE rows crossing unprinted dispatch would read INFERRED; labels unaffected.
3. Lambda/anonymous `$` numbering is source-order / registration-order / descriptor only, NOT bytecode-verified (see numbering section above).
4. `<clinit>` on first use (convention ix): batch 119 row 26 rests on the static `diffCallback` field plus first use via `new TagsAdapter` (STD :130); whether that suffices project-wide is undecided.
5. FragmentCallback interface-cast dispatch: `STD.finish` :191-194 dispatches via `((FragmentCallback) activity).onFragmentFinished(...)`; the host implementations are printed (STA :57-66), but the cast step itself is unprinted. Batch 119's `finish` row is SOURCE on its printed callers, not on the cast alone — same family as batches 82/86/108, recorded not decided.
6. Batch 119 row 36 (2-arg ctor) stays INFERRED despite the freshly printed layout declaration: the layout names the class and id, but the ctor call itself is LayoutInflater framework dispatch, not printed app code — consistent with the batch 94 PiecesView 2-arg precedent (INFERRED on a printed layout).

## Still owed before merge

- Printed launcher → DetailTorrentActivity step, if the merger applies the strict-entry rule.
- Lambda/anonymous numbering confirmed against bytecode, if the merger requires it.
- Merger's usual full-repo consistency grep for the batch (no OPEN → UNREACHABLE flip is pending, since no OPEN rows remain and no UNREACHABLE is claimed).
- Main-agent spot-check (1 in 5), `py_compile`, build, sampler, Mac build/C1 — all not run, never claimed passed.
- No push was made; pushes are held until verified and merged to [L].

Scope kept exactly: batch 119 only, LibreTorrent labels only, branch `work-2026-10-31` only, no device replay, no Aegis.
