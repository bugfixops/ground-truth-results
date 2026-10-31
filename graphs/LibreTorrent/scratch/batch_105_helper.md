# LibreTorrent batch 105 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 105 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. GoToFolderDialog source includes TextWatcher and dialog callbacks; LogActivity source includes lifecycle, menu, ActivityResult, and delayed FAB behavior. This bounded review did not complete the entry route and callback/result branches for every target. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `GoToFolderDialog.initAlertDialog` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 2 | `GoToFolderDialog.initLayoutView` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 3 | `GoToFolderDialog.lambda$initAlertDialog$1` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 4 | `GoToFolderDialog.lambda$initAlertDialog$2` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 5 | `GoToFolderDialog.lambda$initAlertDialog$3` | `(Landroid/content/DialogInterface;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 6 | `GoToFolderDialog.lambda$onResume$0` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 7 | `GoToFolderDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/filemanager/GoToFolderDialog;` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 8 | `GoToFolderDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 9 | `GoToFolderDialog.onBackPressed` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 10 | `GoToFolderDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 11 | `GoToFolderDialog.onResume` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 12 | `GoToFolderDialog$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/GoToFolderDialog;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 13 | `GoToFolderDialog$1.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 14 | `GoToFolderDialog$1.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 15 | `GoToFolderDialog$1.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 16 | `GoToFolderViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 17 | `LogActivity.<init>` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 18 | `LogActivity.hideFabDown` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 19 | `LogActivity.hideFabUp` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 20 | `LogActivity.lambda$new$4` | `(Landroidx/activity/result/ActivityResult;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 21 | `LogActivity.lambda$new$5` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 22 | `LogActivity.lambda$new$6` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 23 | `LogActivity.lambda$new$7` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 24 | `LogActivity.lambda$onCreate$0` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 25 | `LogActivity.lambda$onCreate$1` | `(Landroidx/paging/PagedList;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 26 | `LogActivity.lambda$onCreate$2` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 27 | `LogActivity.lambda$onCreate$3` | `(Landroid/view/View;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 28 | `LogActivity.onCreate` | `(Landroid/os/Bundle;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 29 | `LogActivity.onCreateOptionsMenu` | `(Landroid/view/Menu;)Z` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 30 | `LogActivity.onDestroy` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 31 | `LogActivity.onItemClicked` | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 32 | `LogActivity.onOptionsItemSelected` | `(Landroid/view/MenuItem;)Z` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 33 | `LogActivity.onPrepareOptionsMenu` | `(Landroid/view/Menu;)Z` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 34 | `LogActivity.onSaveInstanceState` | `(Landroid/os/Bundle;)V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 35 | `LogActivity.onStart` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 36 | `LogActivity.onStop` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 37 | `LogActivity.pauseResumeLog` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 38 | `LogActivity.resumeLog` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 39 | `LogActivity.saveLogPathChooseDialog` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |
| 40 | `LogActivity.scrollLogList` | `()V` | OPEN | Dialog/activity source and local callbacks exist; complete app-entry and framework/result route was not audited row by row. |

## Evidence
- `GoToFolderDialog.java:55-128`: factory/lifecycle, view creation, TextWatcher and dialog setup.
- `LogActivity.java:77-195`: activity creation/lifecycle/state/menu; result launcher around 304-331; FAB scheduling and handlers around 348-436; scroll/item handling around 439-461.
- Local code paths are partial; full callback framework and app-entry routing are not established for all rows.

