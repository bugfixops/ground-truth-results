# LibreTorrent batch 95 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 95 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. DetailTorrentTrackersFragment contains selection/action-mode handlers and TrackerListAdapter contains item binding/key methods. This bounded pass does not verify full parent-fragment route or AndroidX selection/RecyclerView dispatch for each target, so all remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `DetailTorrentTrackersFragment.lambda$deleteTrackers$4` | `(Ljava/util/List;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 2 | `DetailTorrentTrackersFragment.lambda$shareUrl$5` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)Ljava/lang/String;` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 3 | `DetailTorrentTrackersFragment.lambda$shareUrl$6` | `(Ljava/util/List;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 4 | `DetailTorrentTrackersFragment.lambda$subscribeAdapter$0` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 5 | `DetailTorrentTrackersFragment.lambda$subscribeAdapter$1` | `(Ljava/util/List;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 6 | `DetailTorrentTrackersFragment.lambda$subscribeAlertDialog$2` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 7 | `DetailTorrentTrackersFragment.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 8 | `DetailTorrentTrackersFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 9 | `DetailTorrentTrackersFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 10 | `DetailTorrentTrackersFragment.onDetach` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 11 | `DetailTorrentTrackersFragment.onResume` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 12 | `DetailTorrentTrackersFragment.onSaveInstanceState` | `(Landroid/os/Bundle;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 13 | `DetailTorrentTrackersFragment.onStart` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 14 | `DetailTorrentTrackersFragment.onStop` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 15 | `DetailTorrentTrackersFragment.onViewCreated` | `(Landroid/view/View;Landroid/os/Bundle;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 16 | `DetailTorrentTrackersFragment.onViewStateRestored` | `(Landroid/os/Bundle;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 17 | `DetailTorrentTrackersFragment.selectAllTrackers` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 18 | `DetailTorrentTrackersFragment.setActionModeTitle` | `(I)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 19 | `DetailTorrentTrackersFragment.shareUrl` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 20 | `DetailTorrentTrackersFragment.subscribeAdapter` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 21 | `DetailTorrentTrackersFragment.subscribeAlertDialog` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 22 | `DetailTorrentTrackersFragment$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 23 | `DetailTorrentTrackersFragment$1.canReuseUpdatedViewHolder` | `(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 24 | `DetailTorrentTrackersFragment$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 25 | `DetailTorrentTrackersFragment$2.onSelectionChanged` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 26 | `DetailTorrentTrackersFragment$2.onSelectionRestored` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 27 | `DetailTorrentTrackersFragment$3.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 28 | `DetailTorrentTrackersFragment$3.onActionItemClicked` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/MenuItem;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 29 | `DetailTorrentTrackersFragment$3.onCreateActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 30 | `DetailTorrentTrackersFragment$3.onDestroyActionMode` | `(Landroidx/appcompat/view/ActionMode;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 31 | `DetailTorrentTrackersFragment$3.onPrepareActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 32 | `TrackerItem.<init>` | `(Lorg/proninyaroslav/libretorrent/core/model/data/TrackerInfo;)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 33 | `TrackerItem.equals` | `(Ljava/lang/Object;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 34 | `TrackerItem.equalsContent` | `(Ljava/lang/Object;)Z` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 35 | `TrackerItem.hashCode` | `()I` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 36 | `TrackerListAdapter.<clinit>` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 37 | `TrackerListAdapter.<init>` | `()V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 38 | `TrackerListAdapter.getItemKey` | `(I)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 39 | `TrackerListAdapter.getItemPosition` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerItem;)I` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |
| 40 | `TrackerListAdapter.onBindViewHolder` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/trackers/TrackerListAdapter$ViewHolder;I)V` | OPEN | Fragment/adapter/local selection callbacks exist; full host route and AndroidX selection dispatch were not verified for each target. |

## Evidence
- `DetailTorrentTrackersFragment.java:93-147`: factory and lifecycle/view setup; adapter/dialog subscriptions.
- Selection callbacks at lines 189-218; action-mode handlers at 298-330; dialog/share/select functions at 345-398.
- `TrackerListAdapter.java:51-128`: adapter, bind/key methods, diff callbacks.
- `TrackerItem.java:26-53`: equality and hash methods.
Local code confirms relationships, not complete framework/library routes.

