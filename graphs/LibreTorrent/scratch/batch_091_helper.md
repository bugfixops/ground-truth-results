# LibreTorrent batch 91 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, exact batch 91 members only. Count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch spans DetailTorrentInfo, State, and Files fragments. Source search shows button/listener, tag subscription, fragment lifecycle, adapter and dialog callbacks, but complete host-fragment entry and callback dispatch routes were not verified row by row. Keep every row OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `DetailTorrentInfoFragment.onStart` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 2 | `DetailTorrentInfoFragment.onStop` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 3 | `DetailTorrentInfoFragment.showChooseDirDialog` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 4 | `DetailTorrentInfoFragment.showEditNameDialog` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 5 | `DetailTorrentInfoFragment.showOpenDirErrorDialog` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 6 | `DetailTorrentInfoFragment.subscribeAlertDialog` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 7 | `DetailTorrentInfoFragment.subscribeTags` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 8 | `DetailTorrentInfoFragment$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/DetailTorrentInfoFragment;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 9 | `DetailTorrentInfoFragment$1.lambda$onAddTagClick$0` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Ljava/lang/Long;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 10 | `DetailTorrentInfoFragment$1.lambda$onAddTagClick$1` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 11 | `DetailTorrentInfoFragment$1.lambda$onAddTagClick$2` | `(Ljava/util/List;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 12 | `DetailTorrentInfoFragment$1.onAddTagClick` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 13 | `DetailTorrentInfoFragment$1.onTagRemoved` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 14 | `DetailTorrentInfoFragment$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/DetailTorrentInfoFragment;Lcom/google/android/material/textfield/TextInputLayout;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 15 | `DetailTorrentInfoFragment$2.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 16 | `DetailTorrentInfoFragment$2.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 17 | `DetailTorrentInfoFragment$2.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 18 | `DetailTorrentStateFragment.<clinit>` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 19 | `DetailTorrentStateFragment.<init>` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 20 | `DetailTorrentStateFragment.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/DetailTorrentStateFragment;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 21 | `DetailTorrentStateFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 22 | `DetailTorrentStateFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 23 | `DetailTorrentStateFragment.onViewCreated` | `(Landroid/view/View;Landroid/os/Bundle;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 24 | `DetailTorrentFilesFragment.<clinit>` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 25 | `DetailTorrentFilesFragment.<init>` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 26 | `DetailTorrentFilesFragment.changePriority` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 27 | `DetailTorrentFilesFragment.handleOpenFileError` | `(Ljava/lang/Throwable;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 28 | `DetailTorrentFilesFragment.initPriorityDialog` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 29 | `DetailTorrentFilesFragment.lambda$changePriority$6` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/TorrentContentFileItem;)Ljava/lang/String;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 30 | `DetailTorrentFilesFragment.lambda$changePriority$7` | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/FilePriority;Ljava/util/List;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 31 | `DetailTorrentFilesFragment.lambda$initPriorityDialog$4` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/TorrentContentFileItem;)Ljava/lang/String;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 32 | `DetailTorrentFilesFragment.lambda$initPriorityDialog$5` | `(Ljava/util/List;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 33 | `DetailTorrentFilesFragment.lambda$onItemClicked$3` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/TorrentContentFileItem;Landroid/net/Uri;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 34 | `DetailTorrentFilesFragment.lambda$subscribeAdapter$0` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 35 | `DetailTorrentFilesFragment.lambda$subscribeAdapter$1` | `(Ljava/util/List;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 36 | `DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 37 | `DetailTorrentFilesFragment.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/detailtorrent/pages/files/DetailTorrentFilesFragment;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 38 | `DetailTorrentFilesFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 39 | `DetailTorrentFilesFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |
| 40 | `DetailTorrentFilesFragment.onDetach` | `()V` | OPEN | Fragment/UI/Rx callback code is present; full host fragment and dispatch routes were not verified for every target. |

## Evidence
- `DetailTorrentInfoFragment.java`: buttons call dialog methods (110-111); error path at 125; tag callbacks/subscription at 149-200; dialog subscription/constructors at 211-275; text watcher callbacks at 311-319.
- `DetailTorrentStateFragment.java`: factory and lifecycle methods at 51-80.
- `DetailTorrentFilesFragment.java`: factory/view lifecycle and subscriptions at 101-181; item click at 333; priority dialog and change handlers at 423-477; error callback at 535.
These are local links; full routes from DetailTorrentFragment were not traced for all targets.

