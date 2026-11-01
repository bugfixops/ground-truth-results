# UNVERIFIED merge-ready part — NOT merged, NOT verified for merge

# LibreTorrent batch 120 — merge-ready part

**UNVERIFIED — NOT merged. No build, sampler, grep, or C1 count is claimed. Build: not run. C1: not run (Mac after push, never claimed passed).**
Connector-only work (GitHub connector, branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`). No token, no local checkout, no push, no edit to `graph_def.py` / `out` / progress / `tools` / another helper's file. Fresh source saved in `~/workspace/b119120-src/` (connector JSON kept alongside each file). No `search_code` result was used anywhere, and no `search_code` 0 was used as evidence of absence. No row is UNREACHABLE: no saved full-repo grep was run in this pass, so absence of a printed caller would be OPEN, never `no_trigger_in_app`.

## Membership

All 3 rows below are batch 120 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (git blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), each `TODO_CANDIDATE_REACHABLE`, in plan-file order. Method names and JVM descriptors were generated from the plan file, so they cannot drift from it. Batch 120 is the final partial batch (3 rows, not 40); there is no batch 121 in the plan.

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
| 1 | TorrentTagsList.lambda$buildChip$0 | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;Landroid/view/View;)V` | REACHABLE | INFERRED | Close-icon click lambda TTL :69-73 (setOnCloseIconClickListener, calls listener.onTagRemoved(info) :71 -> DTIF :169); chip built by buildChip :54-76, called from submit :49; Material Chip close-icon dispatch not printed. |
| 2 | TorrentTagsList.setListener | `(Lorg/proninyaroslav/libretorrent/ui/tag/TorrentTagsList$Listener;)V` | REACHABLE | SOURCE | TTL :40-42; called directly at DTIF.onCreateView :112 `binding.tagsList.setListener(tagsListener)`. |
| 3 | TorrentTagsList.submit | `(Ljava/util/List;)V` | REACHABLE | INFERRED | TTL :44-52; reached only via Rx method reference binding.tagsList::submit at DTIF.subscribeTags :181 (called from DTIF.onStart :201); Rx dispatch not printed. Body :49 calls buildChip per tag, :51 re-adds the add-tag button. |

## Counts

- **3 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN** (REACHABLE: SOURCE 1 / INFERRED 2).
- Verified for merge: **0 / 3** (merge-ready part only; build/sampler/grep/C1 not run).

## Changes vs input proposals

- **No label changed vs the input proposal (3/0/0, SOURCE 1 / INFERRED 2, unchanged).** Every proposal citation was re-checked against the fresh prints and held exactly (TTL :69-73, :40-42, :44-52; DTIF :112, :181, :201).
- Same evidence strengthening as batch 119: the fresh layout print confirms the `tagsList` attachment anchoring the `submit`/`setListener` routes, but the strict-entry (launcher) gap remains open (see caveats).

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

Scope kept exactly: batch 120 only, LibreTorrent labels only, branch `work-2026-10-31` only, no device replay, no Aegis.
