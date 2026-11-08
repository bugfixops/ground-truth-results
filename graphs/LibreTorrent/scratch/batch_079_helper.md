# LibreTorrent batch 79 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 79 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch spans AddTorrentActivity and its files/info fragments. Printed source reveals lifecycle, decode-state, observer, and fragment callback chains, but this bounded review did not verify every method end-to-end against the full entry route and conditional branches. All rows remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `AddTorrentActivity.lambda$initLayout$0` | `(Lcom/google/android/material/tabs/TabLayout$Tab;I)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 2 | `AddTorrentActivity.lambda$observeDecodeState$1` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel$DecodeState;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 3 | `AddTorrentActivity.observeDecodeState` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 4 | `AddTorrentActivity.onBackPressed` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 5 | `AddTorrentActivity.onCreate` | `(Landroid/os/Bundle;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 6 | `AddTorrentActivity.onOptionsItemSelected` | `(Landroid/view/MenuItem;)Z` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 7 | `AddTorrentActivity.onPrepareOptionsMenu` | `(Landroid/view/Menu;)Z` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 8 | `AddTorrentActivity.onStart` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 9 | `AddTorrentActivity.onStartDecode` | `(Z)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 10 | `AddTorrentActivity.onStop` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 11 | `AddTorrentActivity.onStopDecode` | `(Ljava/lang/Throwable;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 12 | `AddTorrentActivity.showAddErrorDialog` | `(Ljava/lang/String;Ljava/lang/Throwable;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 13 | `AddTorrentActivity.subscribeAlertDialog` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 14 | `AddTorrentActivity.subscribeParamsChanged` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 15 | `AddTorrentActivity.unsubscribeParamsChanged` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 16 | `AddTorrentActivity$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 17 | `AddTorrentActivity$1.onNotificationResult` | `(ZZ)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 18 | `AddTorrentActivity$1.onStorageResult` | `(ZZ)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 19 | `AddTorrentActivity$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 20 | `AddTorrentActivity$2.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 21 | `AddTorrentFilesFragment.<clinit>` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 22 | `AddTorrentFilesFragment.<init>` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 23 | `AddTorrentFilesFragment.lambda$subscribeAdapter$0` | `(Ljava/util/List;)Lio/reactivex/SingleSource;` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 24 | `AddTorrentFilesFragment.lambda$subscribeAdapter$1` | `(Ljava/util/List;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 25 | `AddTorrentFilesFragment.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentFilesFragment;` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 26 | `AddTorrentFilesFragment.onAttach` | `(Landroid/content/Context;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 27 | `AddTorrentFilesFragment.onCreateView` | `(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 28 | `AddTorrentFilesFragment.onItemCheckedChanged` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/DownloadableFileItem;Z)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 29 | `AddTorrentFilesFragment.onItemClicked` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/DownloadableFileItem;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 30 | `AddTorrentFilesFragment.onResume` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 31 | `AddTorrentFilesFragment.onSaveInstanceState` | `(Landroid/os/Bundle;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 32 | `AddTorrentFilesFragment.onStart` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 33 | `AddTorrentFilesFragment.onStop` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 34 | `AddTorrentFilesFragment.onViewCreated` | `(Landroid/view/View;Landroid/os/Bundle;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 35 | `AddTorrentFilesFragment.onViewStateRestored` | `(Landroid/os/Bundle;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 36 | `AddTorrentFilesFragment.subscribeAdapter` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 37 | `AddTorrentFilesFragment.updateFileSize` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 38 | `AddTorrentInfoFragment.<clinit>` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 39 | `AddTorrentInfoFragment.<init>` | `()V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |
| 40 | `AddTorrentInfoFragment.checkNameField` | `(Landroid/text/Editable;)V` | OPEN | Candidate lifecycle/callback calls are visible, but complete entry-to-method route was not verified row by row. |

## Evidence
- `AddTorrentActivity`: `onCreate` line 97, observers at 139/305, lifecycle hooks at 170/179, decode handler calls at 317/323, error handlers at 419+, menu handlers at 540/552.
- `AddTorrentFilesFragment`: fragment creation/view lifecycle at 68/79/104/128; adapter subscription at 111; click/check callbacks at 183/192.
- `AddTorrentInfoFragment`: factory and view lifecycle at 74/92/99; text watcher invokes `checkNameField` at 117; method at 234.
This is local route evidence only; complete manifest-to-screen and callback route proof is not captured here.

