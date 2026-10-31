# LibreTorrent batch 87 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 87 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. DetailTorrentFragment source exposes candidate menu, observer, dialog, and lifecycle chains. This bounded scan did not verify the full activity/fragment entry path and all branches for each method, so uncertainty stays OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `DetailTorrentFragment.addTrackersDialog` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 2 | `DetailTorrentFragment.checkAddTrackersField` | `(Ljava/util/List;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputEditText;)Z` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 3 | `DetailTorrentFragment.deleteTorrent` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 4 | `DetailTorrentFragment.deleteTorrentDialog` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 5 | `DetailTorrentFragment.finish` | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 6 | `DetailTorrentFragment.getTorrentId` | `()Ljava/lang/String;` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 7 | `DetailTorrentFragment.handleTorrentInfo` | `(Landroidx/core/util/Pair;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 8 | `DetailTorrentFragment.initAddTrackersDialog` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 9 | `DetailTorrentFragment.initSpeedLimitDialog` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 10 | `DetailTorrentFragment.lambda$addTrackers$10` | `(Ljava/lang/String;)Z` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 11 | `DetailTorrentFragment.lambda$new$11` | `(Landroidx/activity/result/ActivityResult;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 12 | `DetailTorrentFragment.lambda$onViewCreated$0` | `(Landroid/view/View;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 13 | `DetailTorrentFragment.lambda$onViewCreated$1` | `(Lcom/google/android/material/tabs/TabLayout$Tab;I)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 14 | `DetailTorrentFragment.lambda$subscribeAlertDialog$9` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 15 | `DetailTorrentFragment.lambda$subscribeFreeSpaceError$8` | `(Ljava/lang/Boolean;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 16 | `DetailTorrentFragment.lambda$subscribeMsgViewModel$7` | `(Ljava/lang/Boolean;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 17 | `DetailTorrentFragment.lambda$subscribeTorrentInfo$2` | `(Lorg/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 18 | `DetailTorrentFragment.lambda$subscribeTorrentInfo$3` | `(Ljava/lang/Throwable;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 19 | `DetailTorrentFragment.lambda$subscribeTorrentInfo$4` | `(Ljava/lang/Throwable;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 20 | `DetailTorrentFragment.lambda$subscribeTorrentInfo$5` | `(Lorg/proninyaroslav/libretorrent/core/model/data/AdvancedTorrentInfo;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 21 | `DetailTorrentFragment.lambda$subscribeTorrentInfo$6` | `(Ljava/lang/Throwable;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 22 | `DetailTorrentFragment.newInstance` | `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentFragment;` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 23 | `DetailTorrentFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 24 | `DetailTorrentFragment.onBackPressed` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 25 | `DetailTorrentFragment.onCreateOptionsMenu` | `(Landroid/view/Menu;Landroid/view/MenuInflater;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 26 | `DetailTorrentFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 27 | `DetailTorrentFragment.onOptionsItemSelected` | `(Landroid/view/MenuItem;)Z` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 28 | `DetailTorrentFragment.onPrepareOptionsMenu` | `(Landroid/view/Menu;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 29 | `DetailTorrentFragment.onSaveInstanceState` | `(Landroid/os/Bundle;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 30 | `DetailTorrentFragment.onStart` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 31 | `DetailTorrentFragment.onStop` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 32 | `DetailTorrentFragment.onViewCreated` | `(Landroid/view/View;Landroid/os/Bundle;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 33 | `DetailTorrentFragment.prepareOptionsMenu` | `(Landroid/view/Menu;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 34 | `DetailTorrentFragment.saveErrorTorrentFileDialog` | `(Ljava/lang/Exception;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 35 | `DetailTorrentFragment.setSpeedLimit` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 36 | `DetailTorrentFragment.setTabLayoutColor` | `(I)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 37 | `DetailTorrentFragment.setTorrentId` | `(Ljava/lang/String;)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 38 | `DetailTorrentFragment.shareMagnet` | `(Z)V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 39 | `DetailTorrentFragment.shareMagnetDialog` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |
| 40 | `DetailTorrentFragment.showFiles` | `()V` | OPEN | Detail fragment local callers and dialog handlers are visible; full entry-to-method route/condition audit is incomplete. |

## Evidence
- `DetailTorrentFragment.java:115-129`: factory and torrent-id setup.
- Lifecycle/view setup at lines 139-183; subscriptions at 224-356; dialog event dispatch at 297-349.
- Menu handlers at 413-470; dialog builders at 478-531; torrent and share helpers at 586-644; tracker validation/add at 689-739.
These local source calls are candidate routes, not complete route verification.

