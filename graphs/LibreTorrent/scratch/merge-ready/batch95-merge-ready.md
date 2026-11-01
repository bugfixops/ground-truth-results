# LibreTorrent batch 95 — MERGE-READY — UNVERIFIED

Branch: work-2026-10-31, repo bugfixops/ground-truth-results. Local only — NO push
(pushes are held until verified and merged to [L]), no edit to graph_def.py, out/,
PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.

Membership: exactly the 40 plan rows of handoff/LIBRETORRENT_BATCH_PLAN.tsv batch 95
(local copy ~/workspace/agent27-plan.tsv, git blob SHA
0104806dd666c840049b3db52823d4b384fa1c92), all TODO_CANDIDATE_REACHABLE, sequence
1–40 intact, in plan order. Prior proposal (~/workspace/libretorrent-batch95-proposal.md)
was used as a lead list only; every row below was re-judged against source freshly
fetched in this pass. No row is copied on the proposal's authority alone.

Counts: 40 rows judged: **39 REACHABLE proposed (SOURCE 14 / INFERRED 25),
0 UNREACHABLE, 1 OPEN. 0/40 verified for merge.**

## Printed sources used (all freshly connector-fetched this pass, branch work-2026-10-31, one file at a time with ~25 s pauses, no fresh HTTP 429)

Saved in ~/workspace/b9596-src/:

- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java` — 406 lines,
  connector SHA 48d5a5360febbf5e8ac10f6b08d106d88aff0126.
- `ui/detailtorrent/pages/trackers/TrackerListAdapter.java` — 299 lines, connector SHA
  320b9e7722766b56e3aba2ddeabd593356cedec1 (byte-identical SHA to the prior
  proposal's fetch).
- `ui/detailtorrent/pages/trackers/TrackerItem.java` — 55 lines, connector SHA
  1ddb82a8b962bb63b5f510fa1ca3de60f348693f.
- `ui/detailtorrent/DetailPagerAdapter.java` — 76 lines, connector SHA
  df5ff38c24b0661b60b64357ac8cec1ae7235224.
- `ui/detailtorrent/DetailTorrentFragment.java` — 832 lines, connector SHA
  c24e0912e62088e962894f04ee427bbe317e83e7 (same SHA as the batch 65–67 pass).
- `ui/feeditems/FeedItemsFragment.java` — 329 lines, connector SHA
  c612894b16f58bf5c7780fa683a4a8cbcefda97f (read for batch 96; also confirms no
  TrackerItem use in the feed-items path).

Abbreviations in citations: "fragment" = DetailTorrentTrackersFragment.java,
"adapter" = TrackerListAdapter.java, "pager" = DetailPagerAdapter.java,
"DetailFrag" = DetailTorrentFragment.java. Line numbers are fresh-file lines.

## Entry trunk (printed fresh)

DetailFrag:185 `adapter = new DetailPagerAdapter(this);` → pager.createFragment
:53–66, `case TRACKERS_FRAG_POS` (:42 `TRACKERS_FRAG_POS = 3`) :61–62
`return DetailTorrentTrackersFragment.newInstance();` → fragment lifecycle
(framework dispatch, INFERRED) → onViewCreated builds the adapter and selection
machinery. The step that puts DetailTorrentFragment itself on screen was not
re-printed in this pass; under a strict launcher-entry rule all REACHABLE rows
below revert to OPEN (convention recorded, not decided). The pager → newInstance
link itself IS printed, unlike the launcher-to-service gap in earlier batches.

## confirmed_by convention used (per-row, recorded not decided)

SOURCE = a printed app-code line names the method (direct call, construction, or
method reference). INFERRED = the method runs only through unprinted
framework/library/Rx dispatch (Fragment lifecycle, RecyclerView, SelectionTracker,
AppCompat ActionMode, Rx subscription) where definition and registration are
printed. Under a whole-route INFERRED convention, SOURCE rows whose route crosses
unprinted framework dispatch would read INFERRED; labels are unaffected. OPEN rows
carry no confirmed_by (shown as —), consistent with sibling merge-ready files.

## Rows

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | DetailTorrentTrackersFragment.lambda$deleteTrackers$4 (Ljava/util/List;)V | REACHABLE | INFERRED | Rx subscribe lambda inside deleteTrackers() (fragment :360–368, subscribe at :368 `(urls) -> viewModel.deleteTrackers(urls)`); deleteTrackers called from subscribeAlertDialog POSITIVE_BUTTON_CLICKED branch :279. $ index by enclosing method, NOT bytecode-verified; the map lambda inside the same method (selection -> selection.url, :366) is a different lambda and is not a row in this batch. |
| 2 | DetailTorrentTrackersFragment.lambda$shareUrl$5 (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)Ljava/lang/String; | REACHABLE | INFERRED | Rx map lambda inside shareUrl() (fragment :374–396, map at :380 `(selection -> selection.url)`); shareUrl called from actionModeCallback.onActionItemClicked :320. $ index by enclosing method, NOT bytecode-verified. |
| 3 | DetailTorrentTrackersFragment.lambda$shareUrl$6 (Ljava/util/List;)V | REACHABLE | INFERRED | Rx subscribe lambda inside shareUrl() (fragment :382–395, builds ACTION_SEND chooser intent); same caller chain as row 2. $ index by enclosing method, NOT bytecode-verified. |
| 4 | DetailTorrentTrackersFragment.lambda$subscribeAdapter$0 (Ljava/util/List;)Lio/reactivex/SingleSource; | REACHABLE | INFERRED | Rx flatMapSingle lambda inside subscribeAdapter() (fragment :258–269, flatMap at :262–266 `Flowable.fromIterable(children).map(TrackerItem::new).toList()`); subscribeAdapter called from onStart :141. $ index by enclosing method, NOT bytecode-verified. |
| 5 | DetailTorrentTrackersFragment.lambda$subscribeAdapter$1 (Ljava/util/List;)V | REACHABLE | INFERRED | Rx subscribe lambda inside subscribeAdapter() (fragment :268 `subscribe((children) -> adapter.submitList(children))`); same chain as row 4. $ index by enclosing method, NOT bytecode-verified. |
| 6 | DetailTorrentTrackersFragment.lambda$subscribeAlertDialog$2 (Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V | REACHABLE | INFERRED | Rx subscribe lambda inside subscribeAlertDialog() (fragment :271–287, dialog-tag guard + POSITIVE/NEGATIVE switch); subscribeAlertDialog called from onStart :142. $ index by enclosing method, NOT bytecode-verified. |
| 7 | DetailTorrentTrackersFragment.newInstance ()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment; | REACHABLE | SOURCE | pager.createFragment :61–62 returns it for TRACKERS_FRAG_POS; definition fragment :93–99 (`new DetailTorrentTrackersFragment()`, setArguments). |
| 8 | DetailTorrentTrackersFragment.onAttach (Landroid/content/Context;)V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch (framework, not printed from fw_src); definition fragment :111–118. Reached via trunk above. |
| 9 | DetailTorrentTrackersFragment.onCreateView (Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View; | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :103–109 (DataBindingUtil.inflate fragment_detail_torrent_tracker_list). |
| 10 | DetailTorrentTrackersFragment.onDetach ()V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :120–127 (finishes actionMode). |
| 11 | DetailTorrentTrackersFragment.onResume ()V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :250–256 (restores listTrackerState). |
| 12 | DetailTorrentTrackersFragment.onSaveInstanceState (Landroid/os/Bundle;)V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :231–239 (saves layoutManager + selectionTracker state). |
| 13 | DetailTorrentTrackersFragment.onStart ()V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :137–144 (calls subscribeAdapter :141 + subscribeAlertDialog :142). |
| 14 | DetailTorrentTrackersFragment.onStop ()V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :129–135 (disposables.clear()). |
| 15 | DetailTorrentTrackersFragment.onViewCreated (Landroid/view/View;Landroid/os/Bundle;)V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :146–229 (builds ViewModel, adapter, selectionTracker, dialogs). |
| 16 | DetailTorrentTrackersFragment.onViewStateRestored (Landroid/os/Bundle;)V | REACHABLE | INFERRED | Standard Fragment lifecycle dispatch; definition fragment :241–248 (restores TAG_LIST_TRACKER_STATE). |
| 17 | DetailTorrentTrackersFragment.selectAllTrackers ()V | REACHABLE | SOURCE | Called from actionModeCallback.onActionItemClicked fragment :323 (select_all_trackers_menu); definition :398–405 (startRange/extendRange). |
| 18 | DetailTorrentTrackersFragment.setActionModeTitle (I)V | REACHABLE | SOURCE | Called from SelectionObserver onSelectionChanged :195/:203 and onSelectionRestored :218; definition :290–293 (actionMode.setTitle). |
| 19 | DetailTorrentTrackersFragment.shareUrl ()V | REACHABLE | SOURCE | Called from actionModeCallback.onActionItemClicked :320 (share_url_menu); definition :374–396 (ACTION_SEND chooser). |
| 20 | DetailTorrentTrackersFragment.subscribeAdapter ()V | REACHABLE | SOURCE | Called from onStart :141; definition :258–269 (viewModel.observeTrackers → TrackerItem::new → adapter.submitList). |
| 21 | DetailTorrentTrackersFragment.subscribeAlertDialog ()V | REACHABLE | SOURCE | Called from onStart :142; definition :271–287 (dialogViewModel.observeEvents, delete-trackers dialog switch). |
| 22 | DetailTorrentTrackersFragment$1.<init> (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V | REACHABLE | SOURCE | Anonymous DefaultItemAnimator subclass instantiated in onViewCreated (fragment :167–172, `new DefaultItemAnimator() {...}`); passed to setItemAnimator :172. |
| 23 | DetailTorrentTrackersFragment$1.canReuseUpdatedViewHolder (Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)Z | REACHABLE | INFERRED | RecyclerView framework dispatch to the animator (definition fragment :168–171, returns true); framework code not printed from fw_src. |
| 24 | DetailTorrentTrackersFragment$2.<init> (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V | REACHABLE | SOURCE | Anonymous SelectionObserver instantiated in onViewCreated and passed to selectionTracker.addObserver (fragment :188–222). |
| 25 | DetailTorrentTrackersFragment$2.onSelectionChanged ()V | REACHABLE | INFERRED | SelectionTracker framework dispatch (definition fragment :189–211, starts/finishes action mode, setActionModeTitle); framework code not printed. |
| 26 | DetailTorrentTrackersFragment$2.onSelectionRestored ()V | REACHABLE | INFERRED | SelectionTracker framework dispatch (definition fragment :213–220, re-starts action mode); framework code not printed. |
| 27 | DetailTorrentTrackersFragment$3.<init> (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V | REACHABLE | INFERRED | Anonymous ActionMode.Callback field actionModeCallback (fragment :295); instance is created by field initialisation when the fragment is constructed via the newInstance trunk, but no separate construction site is printed — so INFERRED, not SOURCE, under the per-row rule used here. If the merger counts a printed field declaration as an instantiation site, this row alone flips to SOURCE; label unaffected. |
| 28 | DetailTorrentTrackersFragment$3.onActionItemClicked (Landroidx/appcompat/view/ActionMode;Landroid/view/MenuItem;)Z | REACHABLE | INFERRED | AppCompat ActionMode framework dispatch (definition fragment :314–328: delete_tracker_url → deleteTrackersDialog, share_url_menu → shareUrl, select_all → selectAllTrackers); framework code not printed. |
| 29 | DetailTorrentTrackersFragment$3.onCreateActionMode (Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z | REACHABLE | INFERRED | AppCompat ActionMode framework dispatch (definition fragment :304–312, inflates detail_torrent_trackers_action_mode menu); framework code not printed. |
| 30 | DetailTorrentTrackersFragment$3.onDestroyActionMode (Landroidx/appcompat/view/ActionMode;)V | REACHABLE | INFERRED | AppCompat ActionMode framework dispatch (definition fragment :330–336, clears selection, fragmentInActionMode(false)); framework code not printed. |
| 31 | DetailTorrentTrackersFragment$3.onPrepareActionMode (Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z | REACHABLE | INFERRED | AppCompat ActionMode framework dispatch (definition fragment :298–302, returns false); framework code not printed. |
| 32 | TrackerItem.<init> (Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo;)V | REACHABLE | SOURCE | Method reference `TrackerItem::new` in subscribeAdapter (fragment :264); definition TrackerItem.java :28–31 (super(url,message,tier,status)). |
| 33 | TrackerItem.equals (Ljava/lang/Object;)Z | REACHABLE | SOURCE | Called by adapter diffCallback.areItemsTheSame (adapter :125–130, `oldItem.equals(newItem)`); definition TrackerItem.java :45–53 (url equality). Second, independent route: adapter.getItemPosition :110–113 uses getCurrentList().indexOf(key), which compares via equals. |
| 34 | TrackerItem.equalsContent (Ljava/lang/Object;)Z | REACHABLE | SOURCE | Called by adapter diffCallback.areContentsTheSame (adapter :118–123, `oldItem.equalsContent(newItem)`); definition TrackerItem.java :39–42 (super.equals). |
| 35 | TrackerItem.hashCode ()I | OPEN | — | No printed caller in this pass. Definition TrackerItem.java :34–37 (url.hashCode()). Grep over all freshly fetched files in this pass finds no hashCode call on a TrackerItem: the only hashCode occurrences are the definition itself and url.hashCode() inside it; adapter diffing uses equals/equalsContent, submitList sorts (Collections.sort, adapter :94–95), and getItemPosition uses indexOf (equals only, not hashCode). NOT labelled UNREACHABLE: no saved full-repo grep was run, and hash-based collection use elsewhere in the app is unprinted. Highest-priority grep target before merge. Cross-note: same question as batch 3 TagInfo.hashCode and batch 10 drawer TagItem.hashCode — a project rule on hashCode dispatch must be applied consistently, not decided here. |
| 36 | TrackerListAdapter.<clinit> ()V | REACHABLE | INFERRED | Static field initialisation (adapter :54 TAG = getSimpleName(), non-constant; :115 diffCallback); runs on first class use, i.e. `new TrackerListAdapter()` in onViewCreated (fragment :160). Class-init dispatch not printed; <clinit>-on-first-use convention recorded, not decided (see convention (ix) in the project notes). |
| 37 | TrackerListAdapter.<init> ()V | REACHABLE | SOURCE | `adapter = new TrackerListAdapter()` in onViewCreated (fragment :160); definition adapter :58–61 (super(diffCallback)). |
| 38 | TrackerListAdapter.getItemKey (I)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem; | REACHABLE | SOURCE | Called by KeyProvider.getKey (adapter :239–242, `selectable.getItemKey(position)`); KeyProvider is built in onViewCreated (fragment :181). Definition adapter :101–108. Contrast batch 96 row 40 (FeedItemsAdapter.getItemKey), which has NO printed KeyProvider caller. |
| 39 | TrackerListAdapter.getItemPosition (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)I | REACHABLE | SOURCE | Called by KeyProvider.getPosition (adapter :245–248, `selectable.getItemPosition(key)`); definition adapter :110–113 (getCurrentList().indexOf). |
| 40 | TrackerListAdapter.onBindViewHolder (Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter$ViewHolder;I)V | REACHABLE | INFERRED | RecyclerView framework dispatch (standard adapter callback); definition adapter :82–90 (setSelected + holder.bind). Framework code not printed from fw_src. |

## Counts (mechanically verified, see verification below)

- REACHABLE proposed: 39 (SOURCE 14: rows 7, 17, 18, 19, 20, 21, 22, 24, 32, 33, 34, 37, 38, 39; INFERRED 25: rows 1–6, 8–16, 23, 25–31, 36, 40)
- UNREACHABLE proposed: 0
- OPEN: 1 (row 35 TrackerItem.hashCode)

## Still owed before merge

1. Saved full-repo grep for TrackerItem.hashCode (row 35) — the only OPEN row. A
   printed hash-collection use flips it to REACHABLE; a saved full-repo grep with
   no such use would support UNREACHABLE (kind to be decided at merge, not here).
2. Bytecode confirmation of lambda/anonymous $ numbering (rows 1–6, 22–31).
3. Printed step putting DetailTorrentFragment on screen (strict-entry completeness).
4. Main-agent spot-check (1 in 5), py_compile, build, sampler, C1 — build: not run,
   C1: not run (both run on the user's Mac after a push, never claimed passed).
   No sampler or full-repo grep was run in this pass. No search_code result was
   used anywhere, and no search_code 0 was used as evidence of absence.
5. True git clone: NOT attempted — it fails in this VM (no credential device);
   that check is named missing, never passed. All source above came via the
   GitHub connector from branch work-2026-10-31.

## Scope

Batches 95 only in this file. LibreTorrent labels only. No other batch/app, no
device replay, no Aegis. No push. Nothing merged.
