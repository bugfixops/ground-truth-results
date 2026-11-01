# LibreTorrent batch 112 - merge-ready - UNVERIFIED

Status: MERGE-READY PROPOSAL ONLY, UNVERIFIED. Not verified for merge. No build, sampler,
real full-repo grep, or C1 check was run in this pass, and no counts are claimed from any of
those. Nothing was pushed (push held until verified and merged to [L]). Saved locally only.

Source root (branch work-2026-10-31, repo bugfixops/ground-truth-results):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`
(AndroidManifest.xml at `.../app/src/main/AndroidManifest.xml`).

Membership: exactly the 40 rows for batch 112 in
`handoff/LIBRETORRENT_BATCH_PLAN.tsv` (git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92),
all TODO_CANDIDATE_REACHABLE in the plan. Plan order preserved below; method names and JVM
descriptors were matched row-for-row against the plan by the generator script
(`~/workspace/libretorrent-merge/gen111112.py`); any mismatch would have failed the run.

## Files printed fresh in this pass

Same fresh corpus as batch 111 (see that file): MainFragment.java (637 lines),
MainViewModel.java (189), MsgMainViewModel.java (52), MainActivity.java (811),
TorrentListAdapter.java (402), TorrentListItem.java (82),
DrawerExpandableAdapter.java (250), AbstractTagItem.java (26),
AndroidManifest.xml (295). All fetched via the GitHub connector from branch
work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429. Saved
under `~/workspace/b111112-src/`. Git blob SHAs are listed in the batch 111 file.

## Conventions used (recorded, NOT decided)

- SOURCE = a printed app-code line names the method, including a printed call site
  inside another app method body, a method reference, or a printed construction
  site - the same per-row convention as batches 87-88 and 95-96. INFERRED = only
  framework/library/Rx/JVM dispatch invokes the method, with definition +
  registration printed. Under a whole-route INFERRED convention, SOURCE rows crossing
  unprinted dispatch would read INFERRED; labels are unaffected.
- Strict-entry: same narrowed caveat as batch 111 - launcher -> MainActivity is
  freshly printed (AndroidManifest.xml:43, MAIN/LAUNCHER :53-55) and
  MainActivity -> MainFragment via findFragmentById is freshly printed
  (MainActivity.java:184-185); only the `activity_main.xml` layout declaration is
  unprinted. Under a strict rule requiring that layout step, all REACHABLE rows
  revert to OPEN; under the container convention used by sibling batches, all stand.
- TorrentListAdapter$1 identity: the diffCallback anonymous DiffUtil.ItemCallback
  at TorrentListAdapter.java:308 is the ONLY anonymous class in that file, so the $1
  assignment holds by elimination - still NOT bytecode-verified.
- ViewHolder bind lambdas $0/$1 (TorrentListAdapter.java:189 and :199) have
  identical plan descriptors, so their assignment is source-order only, NOT
  bytecode-verified; labels do not depend on it (both bodies sit inside printed bind).
- Drawer lambda$onBindChildViewHolder$0 is the only lambda in onBindChildViewHolder
  (DrawerExpandableAdapter.java:116), so its assignment holds by elimination - still
  NOT bytecode-verified.
- `<clinit>` / implicit-ctor family: batch 111 row 40 and batch 112 row 9 both rest on
  the same diffCallback class-initialiser evidence; row 31 (AbstractTagItem.<init>)
  rests on printed subclass constructions with unprinted subclass ctor bodies - see
  its row citation. Neither convention is decided project-wide.

## Shared trunk

MainFragment.onViewCreated: `adapter = new TorrentListAdapter(this)` (:136),
`binding.torrentList.setAdapter(adapter)` (:155), `adapter.setSelectionTracker(selectionTracker)`
(:198), SelectionTracker built with `new TorrentListAdapter.KeyProvider(adapter)`
(:160) and `new TorrentListAdapter.ItemLookup(binding.torrentList)` (:161), plus
`StorageStrategy.createParcelableStorage(TorrentListItem.class)` (:163).
Torrent lists are submitted via `adapter::submitList` (MainFragment.java:297 and
:345, in observeTorrents / getAllTorrentsSingle), which is what drives
ListAdapter/DiffUtil binding.

MainActivity drawer trunk: `drawerAdapter = new DrawerExpandableAdapter(groups,
drawerItemManager, this::onDrawerItemSelected)` (MainActivity.java:250),
`wrappedDrawerAdapter = drawerItemManager.createWrappedAdapter(drawerAdapter)`
(:251), `drawerItemsList.setAdapter(wrappedDrawerAdapter)` (:255),
`drawerItemManager.attachRecyclerView(drawerItemsList)` (:259).

## Changes vs the input proposal

- LABELS UNCHANGED: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN, same as the proposal.
  Row 30 (TorrentListItem.hashCode) stays OPEN for the same reason (no printed
  caller in the fresh corpus; see its row citation).
- CONFIRMED_BY CORRECTIONS (labels unaffected): the proposal's own table marks 9
  rows SOURCE but its header claims SOURCE 7 / INFERRED 32 - the header was a
  miscount. This file corrects the count and additionally upgrades 11 rows from
  INFERRED to SOURCE under the per-row convention stated above (a printed app-code
  line names the method), matching the batches 95-96 treatment of the same adapter
  family: rows 2 (KeyProvider.getKey :344), 3 (markAsOpen :129/:134, KeyProvider
  :350), 12 (ViewHolder.getItemDetails :285), 20 (onCreateViewHolder :84),
  21 (onBindViewHolder :102), 22 (ItemLookup.getItemDetails :396), 25 (bind :198/:260),
  26 (onBindViewHolder :95), 27 (TorrentListItem::new :292/:340), 28
  (areItemsTheSame :321), 29 (areContentsTheSame :314). Every other row keeps the
  proposal's confirmed_by. If the merger instead requires a direct caller outside
  the adapter for SOURCE, those 11 rows revert to INFERRED and the split returns to
  SOURCE 9 / INFERRED 30 - no label changes either way.
- All proposal line numbers were re-checked against the fresh prints and held
  exactly, except that the drawer wrap/attach lines are :251/:255/:259 (the proposal
  cited :251/:259 for wrap/attach, consistent with the fresh file).

## Still owed before merge

1. Saved full-repo grep for row 30 (TorrentListItem.hashCode) before any flip to
   UNREACHABLE. Note the hashCode question is shared with batch 3 (TagInfo.hashCode),
   batch 10 (drawer TagItem.hashCode) and batch 95 row 35 (TrackerItem.hashCode) - a
   project rule must be applied consistently, not decided here.
2. Printed `activity_main.xml` layout declaration, if the merger applies the strict
   entry rule (see above).
3. Lambda/anonymous numbering confirmed against bytecode, if the merger requires it;
   subclass ctor bodies (TagItem, EmptyTagItem, NoTagsItem) freshly printed, if the
   merger requires them for row 31.
4. Main-agent spot-check (1 in 5), py_compile, build, sampler, Mac build/C1 - all
   NOT run, never claimed passed. Build and C1 are marked "not run" (they run on the
   user's Mac after a push). No push was made (held until verified and merged to [L]).


## Rows (40)

| # | Method | JVM descriptor | Proposed label | confirmed_by | Printed citation / route |
|---|---|---|---|---|---|
| 1 | TorrentListAdapter.<init> | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ClickListener;)V` | REACHABLE | SOURCE | MainFragment.java:136: new TorrentListAdapter(this); body TorrentListAdapter.java:62-67 (super(diffCallback)). |
| 2 | TorrentListAdapter.getItemKey | `(I)Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;` | REACHABLE | SOURCE | Selectable override, TorrentListAdapter.java:108-114; printed caller KeyProvider.getKey at :344 (see also batch 95 convention: printed KeyProvider call = SOURCE). SelectionTracker invocation of KeyProvider itself is library dispatch. |
| 3 | TorrentListAdapter.getItemPosition | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)I` | REACHABLE | SOURCE | Selectable override, TorrentListAdapter.java:117-120; printed callers markAsOpen at :129/:134 and KeyProvider.getPosition at :350. |
| 4 | TorrentListAdapter.getOpenedItem | `()Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;` | REACHABLE | SOURCE | MainFragment.java:355: adapter.getOpenedItem() (torrents-deleted filter). |
| 5 | TorrentListAdapter.markAsOpen | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)V` | REACHABLE | SOURCE | MainFragment.java:382 (onItemClicked) and :364/:374 (torrents-deleted / msg closed, with null). |
| 6 | TorrentListAdapter.onBindViewHolder | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ViewHolder;I)V` | REACHABLE | INFERRED | RecyclerView override, TorrentListAdapter.java:88-105 (calls holder.setSelected :95 and holder.bind :102); invoked by RecyclerView when the adapter is bound - library dispatch, not printed. |
| 7 | TorrentListAdapter.onCreateViewHolder | `(Landroid/view/ViewGroup;I)Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ViewHolder;` | REACHABLE | INFERRED | RecyclerView override, TorrentListAdapter.java:76-85 (inflates item_torrent_list, new ViewHolder(binding) :84); invoked by RecyclerView - library dispatch, not printed. |
| 8 | TorrentListAdapter.setSelectionTracker | `(Landroidx/recyclerview/selection/SelectionTracker;)V` | REACHABLE | SOURCE | MainFragment.java:198: adapter.setSelectionTracker(selectionTracker). |
| 9 | TorrentListAdapter$1.<init> | `()V` | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback class for diffCallback, TorrentListAdapter.java:308-323; instance created by the adapter class initialiser on first use (MainFragment.java:136 new TorrentListAdapter); construction is JVM-implicit. Only anonymous class in the file (see caveats). |
| 10 | TorrentListAdapter$1.areContentsTheSame | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)Z` | REACHABLE | INFERRED | TorrentListAdapter.java:311-315 (oldItem.equalsContent(newItem)); invoked by DiffUtil/ListAdapter on submitList (MainFragment.java:297/:345) - library dispatch, not printed. |
| 11 | TorrentListAdapter$1.areItemsTheSame | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)Z` | REACHABLE | INFERRED | TorrentListAdapter.java:318-322 (oldItem.equals(newItem)); invoked by DiffUtil/ListAdapter on submitList - library dispatch, not printed. |
| 12 | TorrentListAdapter$ItemDetails.<init> | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;I)V` | REACHABLE | SOURCE | Constructor TorrentListAdapter.java:359-363; printed construction site ViewHolder.getItemDetails at :285 (new ItemDetails(selectionKey, getBindingAdapterPosition())). |
| 13 | TorrentListAdapter$ItemDetails.getPosition | `()I` | REACHABLE | INFERRED | TorrentListAdapter.java:372-376 (returns adapterPosition); read by SelectionTracker (androidx) - library dispatch, no app call site printed. |
| 14 | TorrentListAdapter$ItemDetails.getSelectionKey | `()Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;` | REACHABLE | INFERRED | TorrentListAdapter.java:367-370 (returns selectionKey); read by SelectionTracker - library dispatch, no app call site printed. |
| 15 | TorrentListAdapter$ItemLookup.<init> | `(Landroidx/recyclerview/widget/RecyclerView;)V` | REACHABLE | SOURCE | MainFragment.java:161: new TorrentListAdapter.ItemLookup(binding.torrentList); body TorrentListAdapter.java:383-386. |
| 16 | TorrentListAdapter$ItemLookup.getItemDetails | `(Landroid/view/MotionEvent;)Landroidx/recyclerview/selection/ItemDetailsLookup$ItemDetails;` | REACHABLE | INFERRED | TorrentListAdapter.java:390-400 (findChildViewUnder, getChildViewHolder, ViewHolder.getItemDetails :396); invoked by SelectionTracker on touch - library dispatch, not printed. |
| 17 | TorrentListAdapter$KeyProvider.<init> | `(Lorg/proninyaroslav/libretorrent/ui/Selectable;)V` | REACHABLE | SOURCE | MainFragment.java:160: new TorrentListAdapter.KeyProvider(adapter); body TorrentListAdapter.java:333-338. |
| 18 | TorrentListAdapter$KeyProvider.getKey | `(I)Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;` | REACHABLE | INFERRED | TorrentListAdapter.java:342-345 (selectable.getItemKey(position)); invoked by SelectionTracker - library dispatch, not printed. |
| 19 | TorrentListAdapter$KeyProvider.getPosition | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)I` | REACHABLE | INFERRED | TorrentListAdapter.java:348-351 (selectable.getItemPosition(key)); invoked by SelectionTracker - library dispatch, not printed. |
| 20 | TorrentListAdapter$ViewHolder.<init> | `(Lorg/proninyaroslav/libretorrent/databinding/ItemTorrentListBinding;)V` | REACHABLE | SOURCE | Constructor TorrentListAdapter.java:161-169; printed construction site onCreateViewHolder at :84 (new ViewHolder(binding)). |
| 21 | TorrentListAdapter$ViewHolder.bind | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;ZLorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ClickListener;)V` | REACHABLE | SOURCE | TorrentListAdapter.java:171-275; printed caller onBindViewHolder at :102 (holder.bind(item, isOpened, listener)). |
| 22 | TorrentListAdapter$ViewHolder.getItemDetails | `()Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ItemDetails;` | REACHABLE | SOURCE | TorrentListAdapter.java:283-286 (new ItemDetails(selectionKey, getBindingAdapterPosition())); printed caller ItemLookup.getItemDetails at :396. |
| 23 | TorrentListAdapter$ViewHolder.lambda$bind$0 | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ClickListener;Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;Landroid/view/View;)V` | REACHABLE | INFERRED | Item-view click listener set in bind, TorrentListAdapter.java:189-196 (listener.onItemClicked(item)); invoked by View click dispatch (framework), not by printed app code. |
| 24 | TorrentListAdapter$ViewHolder.lambda$bind$1 | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListAdapter$ClickListener;Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;Landroid/view/View;)V` | REACHABLE | INFERRED | Pause-button click listener set in bind, TorrentListAdapter.java:199-202 (listener.onItemPauseClicked(item)); invoked by View click dispatch (framework), not by printed app code. |
| 25 | TorrentListAdapter$ViewHolder.setPauseButtonState | `(Z)V` | REACHABLE | SOURCE | TorrentListAdapter.java:288-298; printed callers bind at :198 and :260. |
| 26 | TorrentListAdapter$ViewHolder.setSelected | `(Z)V` | REACHABLE | SOURCE | TorrentListAdapter.java:277-280 (private); printed caller onBindViewHolder at :95. |
| 27 | TorrentListItem.<init> | `(Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)V` | REACHABLE | SOURCE | Constructor TorrentListItem.java (super call with all TorrentInfo fields); method reference TorrentListItem::new in Rx .map(...) at MainFragment.java:292 and :340 - cf. batch 95 TrackerItem <init> SOURCE via ::new. |
| 28 | TorrentListItem.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | TorrentListItem.java (torrentId comparison); printed callers DiffUtil areItemsTheSame at TorrentListAdapter.java:321 and List.indexOf in getItemPosition at :119. |
| 29 | TorrentListItem.equalsContent | `(Lorg/proninyaroslav/libretorrent/ui/main/TorrentListItem;)Z` | REACHABLE | SOURCE | TorrentListItem.java (super.equals(item)); printed caller DiffUtil areContentsTheSame at TorrentListAdapter.java:314. |
| 30 | TorrentListItem.hashCode | `()I` | OPEN |  | Definition printed (TorrentListItem.java:56-58, torrentId.hashCode()), but NO printed app call site in the freshly fetched corpus: grep over all 9 fresh files finds only the definition itself. getItemPosition uses List.indexOf (equals only, not hashCode); the SelectionTracker storage at MainFragment.java:163 is StorageStrategy.createParcelableStorage (Parcelable, not hash storage). Do NOT mark UNREACHABLE on this evidence: hashCode may be used by hash-based collections elsewhere. Needs a saved full-repo grep before any UNREACHABLE verdict. |
| 31 | AbstractTagItem.<init> | `()V` | REACHABLE | INFERRED | AbstractTagItem.java declares only two abstract methods, so this is the implicit default constructor; it runs as the super-call of every subclass construction. Subclass constructions printed in MainActivity.java: new EmptyTagItem() (:332, :475, :498, :509), new NoTagsItem() (:476, :501), TagItem::new map (:477); TagItem is used as an AbstractTagItem (onTagSelected(AbstractTagItem) at :297). The super-call itself is implicit in the subclass constructors, whose bodies were NOT freshly printed - hence INFERRED, not SOURCE; flips to SOURCE if the merger counts a printed subclass construction as the site. |
| 32 | DrawerExpandableAdapter.<init> | `(Ljava/util/List;Lcom/h6ah4i/android/widget/advrecyclerview/expandable/RecyclerViewExpandableItemManager;Lorg/proninyaroslav/libretorrent/ui/main/drawer/DrawerExpandableAdapter$SelectionListener;)V` | REACHABLE | SOURCE | MainActivity.java:250: new DrawerExpandableAdapter(groups, drawerItemManager, this::onDrawerItemSelected); body DrawerExpandableAdapter.java:59-71. |
| 33 | DrawerExpandableAdapter.getChildCount | `(I)I` | REACHABLE | INFERRED | Override DrawerExpandableAdapter.java:141-148; called by the advrecyclerview item manager after wrap/attach (MainActivity.java:251/:259) - library dispatch, no app call site printed. |
| 34 | DrawerExpandableAdapter.getChildId | `(II)J` | REACHABLE | INFERRED | Override DrawerExpandableAdapter.java:161-171; called by the advrecyclerview item manager (stable IDs enabled at :70) - library dispatch, no app call site printed. |
| 35 | DrawerExpandableAdapter.getChildItemViewType | `(II)I` | REACHABLE | INFERRED | Override DrawerExpandableAdapter.java:180-183 (returns 0); called by the advrecyclerview item manager - library dispatch, no app call site printed. |
| 36 | DrawerExpandableAdapter.getGroup | `(I)Lorg/proninyaroslav/libretorrent/ui/main/drawer/DrawerGroup;` | REACHABLE | SOURCE | MainActivity.java:560 (saveGroupExpandState) and :584 (onDrawerGroupsCreated loop). |
| 37 | DrawerExpandableAdapter.getGroupCount | `()I` | REACHABLE | SOURCE | MainActivity.java:583: drawerAdapter.getGroupCount() (onDrawerGroupsCreated loop); also called by the item manager as an override at DrawerExpandableAdapter.java:135-138. |
| 38 | DrawerExpandableAdapter.getGroupId | `(I)J` | REACHABLE | INFERRED | Override DrawerExpandableAdapter.java:151-158; called by the advrecyclerview item manager (stable IDs at :70) - library dispatch, no app call site printed. |
| 39 | DrawerExpandableAdapter.getGroupItemViewType | `(I)I` | REACHABLE | INFERRED | Override DrawerExpandableAdapter.java:174-177 (returns 0); called by the advrecyclerview item manager - library dispatch, no app call site printed. |
| 40 | DrawerExpandableAdapter.lambda$onBindChildViewHolder$0 | `(Lorg/proninyaroslav/libretorrent/ui/main/drawer/DrawerGroup;Lorg/proninyaroslav/libretorrent/ui/main/drawer/DrawerGroupItem;ILandroid/view/View;)V` | REACHABLE | INFERRED | Click listener registered in onBindChildViewHolder, DrawerExpandableAdapter.java:116-123 (selectItem, notifyChildrenOfGroupItemChanged, listener.onItemSelected); onBindChildViewHolder itself is manager-invoked and the click is framework-dispatched - neither step is printed app code. Only lambda in that method (see caveats). |

## Counts

- **Counts: 39 REACHABLE proposed / 0 UNREACHABLE proposed / 1 OPEN** (REACHABLE: SOURCE 20 / INFERRED 19).
- Total: 40/40 rows. 0/40 verified for merge.
