**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 111 - merge-ready - UNVERIFIED

Status: MERGE-READY PROPOSAL ONLY, UNVERIFIED. Not verified for merge. No build, sampler,
real full-repo grep, or C1 check was run in this pass, and no counts are claimed from any of
those. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (pushed UNVERIFIED before [L] at user request 2026-11-01). Saved locally and pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]).

Source root (branch work-2026-10-31, repo bugfixops/ground-truth-results):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`
(AndroidManifest.xml at `.../app/src/main/AndroidManifest.xml`).

Membership: exactly the 40 rows for batch 111 in
`handoff/LIBRETORRENT_BATCH_PLAN.tsv` (git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92),
all TODO_CANDIDATE_REACHABLE in the plan. Plan order preserved below; method names and JVM
descriptors were matched row-for-row against the plan by the generator script
(`~/workspace/libretorrent-merge/gen111112.py`); any mismatch would have failed the run.

## Files printed fresh in this pass

All fetched via the GitHub connector from branch work-2026-10-31, one file at a
time with ~25 s pauses, no fresh HTTP 429. Saved under `~/workspace/b111112-src/`.
Line counts below are `wc -l`; git blob SHAs computed locally with `git hash-object`
match the connector SHAs quoted by prior passes where those files were fetched before.

- `ui/main/MainFragment.java` - 637 lines, blob `1fd79b7a...` (byte-identical to the batch 109-110 copy)
- `ui/main/MainViewModel.java` - 189 lines, blob `73938fbb...`
- `ui/main/MsgMainViewModel.java` - 52 lines, blob `9d5b73b4...`
- `ui/main/MainActivity.java` - 811 lines, blob `d21f8b70...` (byte-identical to the batch 109-110 copy)
- `ui/main/TorrentListAdapter.java` - 402 lines, blob `e3c225c5...`
- `ui/main/TorrentListItem.java` - 82 lines, blob `60ece4b5...`
- `ui/main/drawer/DrawerExpandableAdapter.java` - 250 lines, blob `cb21c054...`
- `ui/main/drawer/AbstractTagItem.java` - 26 lines, blob `5ca6e47d...`
- `AndroidManifest.xml` - 295 lines, blob `875a8aa7...` (byte-identical to the batch 109-110 copy)

## Conventions used (recorded, NOT decided)

- SOURCE = a printed app-code line names the method, including a printed call site
  inside another app method body, a method reference (`TorrentListItem::new`), or a
  printed construction site. INFERRED = execution depends on an unprinted dispatch
  step (framework/library callback invocation, ViewModelProvider instantiation, Rx
  operator invoking a lambda, JVM class initialisation), even though the surrounding
  app code is printed. Under a whole-route INFERRED convention, SOURCE rows crossing
  unprinted dispatch would read INFERRED; labels are unaffected.
- Strict-entry: NARROWED, not removed, by this pass. Freshly printed: manifest
  MainActivity block (AndroidManifest.xml:43, MAIN/LAUNCHER :53-55) and
  MainActivity.onCreate :182 `setContentView(R.layout.activity_main)` plus :184-185
  `findFragmentById(R.id.main_fragmentContainer)` recovering mainFragment. The only
  step NOT printed is the `activity_main.xml` layout declaration placing MainFragment
  in that container. Under a strict rule requiring that printed layout step, the
  MainFragment-anchored rows revert to OPEN; under the lifecycle/container convention
  used by sibling batches, all stand. The prior proposal's broader caveat (launcher
  step not printed) no longer applies.
- MainFragment$3 identity: anonymous classes in MainFragment.java in source order
  are $1 DefaultItemAnimator (:142), $2 SelectionObserver (:166), $3
  ActionMode.Callback (:457). So plan rows `MainFragment$3.*` are the
  ActionMode.Callback methods at MainFragment.java:457-498 (lines 460, 466, 475, 494).
  Numbering is source-order, NOT bytecode-verified.
- MainViewModel lambda numbering ($0 searchFilter field lambda :60-67, $1 getFilter
  lambda :118-123, $2 deleteTag runnable :187) follows the proposal's mapping and is
  NOT bytecode-verified; labels do not depend on it (each body sits on a printed route).
- `<clinit>` on first use (convention ix): row 40 rests on the non-constant static
  `diffCallback` field (TorrentListAdapter.java:308) plus first use via
  `new TorrentListAdapter(this)` at MainFragment.java:136. Whether that suffices
  project-wide is undecided; the row reverts to OPEN if the merger requires more.

## Shared trunk

MainActivity hosts the drawer and the MainViewModel/MsgMainViewModel instances
(MainActivity.java:250 drawer construction; ViewModelProvider use in MainFragment).
MainFragment.onViewCreated obtains both ViewModels (MainFragment.java:131-133:
`provider.get(MainViewModel.class)`, `provider.get(MsgMainViewModel.class)`),
creates the torrent list adapter (:136), the selection tracker (:158-165), and
starts the ActionMode callback on selection (:173, :191:
`activity.startSupportActionMode(actionModeCallback)`).

## Change vs the input proposal

Labels unchanged: 40/0/0, same as the input proposal. Every citation was re-checked
against the freshly fetched prints; all proposal line numbers held exactly (the
only corrections are the narrowed strict-entry caveat above and the MainFragment$3
line pins, which match the proposal). No row changed label or confirmed_by.

## Still owed before merge

1. Printed `activity_main.xml` layout declaration, if the merger applies the strict
   entry rule (see above).
2. Saved full-repo grep consistency check for the batch (no OPEN -> UNREACHABLE flip
   is pending, since no OPEN rows remain and no UNREACHABLE is claimed).
3. Lambda/anonymous numbering confirmed against bytecode, if the merger requires it.
4. Main-agent spot-check (1 in 5), py_compile, build, sampler, Mac build/C1 - all
   NOT run, never claimed passed. Build and C1 are marked "not run" (they run on the
   user's Mac after a push). Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (pushed UNVERIFIED before [L] at user request 2026-11-01).


## Rows (40)

| # | Method | JVM descriptor | Proposed label | confirmed_by | Printed citation / route |
|---|---|---|---|---|---|
| 1 | MainFragment$3.<init> | `(Lorg/proninyaroslav/libretorrent/ui/main/MainFragment;)V` | REACHABLE | INFERRED | Field actionModeCallback declared MainFragment.java:457; instance created with its enclosing MainFragment (field initialiser; fragment-manager creation step is the layout declaration, see caveats). |
| 2 | MainFragment$3.onActionItemClicked | `(Landroidx/appcompat/view/ActionMode;Landroid/view/MenuItem;)Z` | REACHABLE | INFERRED | Body MainFragment.java:475-492 (delete/select-all/force-recheck/force-announce, calling viewModel.deleteTorrents/forceRecheckTorrents/forceAnnounceTorrents); invoked by the framework ActionMode, no app call site names it. |
| 3 | MainFragment$3.onCreateActionMode | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | REACHABLE | INFERRED | Body MainFragment.java:466-473 (inflates R.menu.main_action_mode); framework-invoked after startSupportActionMode at MainFragment.java:173/:191. |
| 4 | MainFragment$3.onDestroyActionMode | `(Landroidx/appcompat/view/ActionMode;)V` | REACHABLE | INFERRED | Body MainFragment.java:494-498 (clears selection, restores status bar); framework-invoked on actionMode.finish(). |
| 5 | MainFragment$3.onPrepareActionMode | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | REACHABLE | INFERRED | Body MainFragment.java:460-463 (returns false); framework-invoked callback, no app call site. |
| 6 | MainViewModel.<init> | `(Landroid/app/Application;)V` | REACHABLE | INFERRED | Constructor body MainViewModel.java:69-76 (TorrentInfoProvider/TorrentEngine/TagRepository getInstance); instantiation by ViewModelProvider.get at MainFragment.java:132 is library code, not printed. |
| 7 | MainViewModel.deleteTag | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lio/reactivex/Completable;` | REACHABLE | SOURCE | MainActivity.java:326: viewModel.deleteTag(item.info) in onTagMenuClicked delete branch, subscribed :326-329. |
| 8 | MainViewModel.deleteTorrents | `(Ljava/util/List;Z)V` | REACHABLE | SOURCE | MainFragment.java:581: .subscribe((ids) -> viewModel.deleteTorrents(ids, withFiles)). |
| 9 | MainViewModel.forceAnnounceTorrents | `(Ljava/util/List;)V` | REACHABLE | SOURCE | MainFragment.java:616: .subscribe((ids) -> viewModel.forceAnnounceTorrents(ids)). |
| 10 | MainViewModel.forceRecheckTorrents | `(Ljava/util/List;)V` | REACHABLE | SOURCE | MainFragment.java:605: .subscribe((ids) -> viewModel.forceRecheckTorrents(ids)). |
| 11 | MainViewModel.getAllTorrentsInfoSingle | `()Lio/reactivex/Single;` | REACHABLE | SOURCE | MainFragment.java:335: viewModel.getAllTorrentsInfoSingle(). |
| 12 | MainViewModel.getFilter | `()Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;` | REACHABLE | SOURCE | MainFragment.java:291 and :339: .filter(viewModel.getFilter()). |
| 13 | MainViewModel.getSorting | `()Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;` | REACHABLE | SOURCE | MainFragment.java:293 and :341: .sorted(viewModel.getSorting()). |
| 14 | MainViewModel.lambda$deleteTag$2 | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Completable runnable at MainViewModel.java:187 (() -> tagRepo.delete(info)); it runs only when the Completable from row 7 is subscribed (MainActivity.java:326-329) - Rx dispatch not printed. |
| 15 | MainViewModel.lambda$getFilter$1 | `(Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)Z` | REACHABLE | INFERRED | Filter lambda returned by getFilter, MainViewModel.java:118-123; its test() runs only via the Rx .filter(...) operators at MainFragment.java:291/:339 - Rx dispatch not printed. |
| 16 | MainViewModel.lambda$new$0 | `(Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)Z` | REACHABLE | INFERRED | SearchFilter field lambda, MainViewModel.java:60-67; invoked as searchFilter.test(state) inside the row-15 lambda at :121, hence downstream of the same unprinted Rx filter dispatch. |
| 17 | MainViewModel.observeAllTorrentsInfo | `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | MainFragment.java:287: viewModel.observeAllTorrentsInfo(). |
| 18 | MainViewModel.observeForceSortAndFilter | `()Lio/reactivex/Observable;` | REACHABLE | SOURCE | MainFragment.java:327: viewModel.observeForceSortAndFilter(). |
| 19 | MainViewModel.observeNeedStartEngine | `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | MainActivity.java:464: viewModel.observeNeedStartEngine(). |
| 20 | MainViewModel.observeTags | `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | MainActivity.java:471: viewModel.observeTags(). |
| 21 | MainViewModel.observeTorrentsDeleted | `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | MainFragment.java:352 and MainActivity.java:446. |
| 22 | MainViewModel.pauseAll | `()V` | REACHABLE | SOURCE | MainActivity.java:751: viewModel.pauseAll() (pause_all_menu handler). |
| 23 | MainViewModel.pauseResumeTorrent | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | MainFragment.java:389: viewModel.pauseResumeTorrent(item.torrentId) (onItemPauseClicked). |
| 24 | MainViewModel.requestStopEngine | `()V` | REACHABLE | SOURCE | MainActivity.java:401: viewModel.requestStopEngine(). |
| 25 | MainViewModel.resetSearch | `()V` | REACHABLE | SOURCE | MainActivity.java:227 (after initDrawer) and :710 (SearchView onCloseListener). |
| 26 | MainViewModel.restartForegroundNotification | `()V` | REACHABLE | SOURCE | MainActivity.java:170: viewModel.restartForegroundNotification() (notification-permission grant callback body; call site itself is printed app code). |
| 27 | MainViewModel.resumeAll | `()V` | REACHABLE | SOURCE | MainActivity.java:753: viewModel.resumeAll() (resume_all_menu handler). |
| 28 | MainViewModel.setDateAddedFilter | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | REACHABLE | SOURCE | MainActivity.java:596 (onDrawerGroupsCreated) and :623 (onDrawerItemSelected). |
| 29 | MainViewModel.setSearchQuery | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | MainActivity.java:717 (onQueryTextSubmit) and :726 (onQueryTextChange). |
| 30 | MainViewModel.setSort | `(Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;Z)V` | REACHABLE | SOURCE | MainActivity.java:594 (onDrawerGroupsCreated) and :619 (onDrawerItemSelected). |
| 31 | MainViewModel.setStatusFilter | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | REACHABLE | SOURCE | MainActivity.java:590 (onDrawerGroupsCreated) and :615 (onDrawerItemSelected). |
| 32 | MainViewModel.setTagFilter | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | REACHABLE | SOURCE | MainActivity.java:299, :304, :306, :335, :499, :502, :510, :520 (tag selection / tag-menu / init-selection paths). |
| 33 | MainViewModel.startEngine | `()V` | REACHABLE | SOURCE | MainActivity.java:467: .subscribe((needStart) -> viewModel.startEngine()) - call site is printed app code in subscribeNeedStartEngine (gated by the row-19 Flowable's needStart filter at :466). |
| 34 | MainViewModel.stopEngine | `()V` | REACHABLE | SOURCE | MainActivity.java:748: viewModel.stopEngine() (shutdown_app_menu handler). |
| 35 | MsgMainViewModel.<init> | `()V` | REACHABLE | INFERRED | Implicit default constructor (no explicit constructor in MsgMainViewModel.java); instantiation by ViewModelProvider.get at MainFragment.java:133 is library code, not printed. |
| 36 | MsgMainViewModel.observeTorrentDetailsClosed | `()Lio/reactivex/Observable;` | REACHABLE | SOURCE | MainFragment.java:370 and MainActivity.java:442. |
| 37 | MsgMainViewModel.observeTorrentDetailsOpened | `()Lio/reactivex/Observable;` | REACHABLE | SOURCE | MainActivity.java:438: msgViewModel.observeTorrentDetailsOpened() (subscribed to showDetailTorrent). |
| 38 | MsgMainViewModel.torrentDetailsClosed | `()V` | REACHABLE | SOURCE | MainActivity.java:809: msgViewModel.torrentDetailsClosed() (onFragmentFinished, DetailTorrentFragment, two-pane). |
| 39 | MsgMainViewModel.torrentDetailsOpened | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | MainFragment.java:383: msgViewModel.torrentDetailsOpened(item.torrentId) (onItemClicked). |
| 40 | TorrentListAdapter.<clinit> | `()V` | REACHABLE | INFERRED | Static field diffCallback (TorrentListAdapter.java:308-323) is initialised by the class initialiser, triggered by first use - new TorrentListAdapter(this) at MainFragment.java:136; the initialiser invocation itself is JVM-implicit, not a printed call. |

## Counts

- **Counts: 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN** (REACHABLE: SOURCE 29 / INFERRED 11).
- Total: 40/40 rows. 0/40 verified for merge.
