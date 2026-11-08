# LibreTorrent batch 83 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 83 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. Source shows CreateTorrentDialog lifecycle, UI callbacks, registered ActivityResult launchers, and local build/error handlers; CreateTorrentActivity constructs the dialog. However the complete route and branch conditions for every target were not verified in this bounded pass. All remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `CreateTorrentDialog.<init>` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 2 | `CreateTorrentDialog.buildTorrent` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 3 | `CreateTorrentDialog.choosePathToSaveDialog` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 4 | `CreateTorrentDialog.createFileErrorDialog` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 5 | `CreateTorrentDialog.emptyFolderErrorDialog` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 6 | `CreateTorrentDialog.errorReportDialog` | `(Ljava/lang/Throwable;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 7 | `CreateTorrentDialog.fileOrFolderNotFoundDialog` | `(Ljava/io/FileNotFoundException;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 8 | `CreateTorrentDialog.finish` | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 9 | `CreateTorrentDialog.handleBuildError` | `(Ljava/lang/Throwable;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 10 | `CreateTorrentDialog.handleFinish` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 11 | `CreateTorrentDialog.initAlertDialog` | `(Landroid/view/View;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 12 | `CreateTorrentDialog.initLayoutView` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 13 | `CreateTorrentDialog.lambda$handleFinish$8` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 14 | `CreateTorrentDialog.lambda$initAlertDialog$4` | `(Landroid/widget/Button;Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentViewModel$BuildState;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 15 | `CreateTorrentDialog.lambda$initAlertDialog$5` | `(Landroid/view/View;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 16 | `CreateTorrentDialog.lambda$initAlertDialog$6` | `(Landroid/view/View;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 17 | `CreateTorrentDialog.lambda$initAlertDialog$7` | `(Landroid/content/DialogInterface;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 18 | `CreateTorrentDialog.lambda$initLayoutView$2` | `(Landroid/view/View;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 19 | `CreateTorrentDialog.lambda$initLayoutView$3` | `(Landroid/view/View;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 20 | `CreateTorrentDialog.lambda$new$10` | `(Landroidx/activity/result/ActivityResult;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 21 | `CreateTorrentDialog.lambda$new$11` | `(Landroidx/activity/result/ActivityResult;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 22 | `CreateTorrentDialog.lambda$new$9` | `(Landroidx/activity/result/ActivityResult;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 23 | `CreateTorrentDialog.lambda$onResume$0` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 24 | `CreateTorrentDialog.lambda$subscribeAlertDialog$1` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 25 | `CreateTorrentDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentDialog;` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 26 | `CreateTorrentDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 27 | `CreateTorrentDialog.onBackPressed` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 28 | `CreateTorrentDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 29 | `CreateTorrentDialog.onResume` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 30 | `CreateTorrentDialog.onStart` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 31 | `CreateTorrentDialog.onStop` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 32 | `CreateTorrentDialog.openPathErrorDialog` | `(Z)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 33 | `CreateTorrentDialog.subscribeAlertDialog` | `()V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 34 | `CreateTorrentDialog$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentDialog;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 35 | `CreateTorrentDialog$1.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 36 | `CreateTorrentDialog$1.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 37 | `CreateTorrentDialog$1.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 38 | `CreateTorrentDialog$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentDialog;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 39 | `CreateTorrentDialog$2.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |
| 40 | `CreateTorrentDialog$2.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/listener/activity-result source shows local calls, but full hand-authored route and branch verification was not completed. |

## Evidence
- `CreateTorrentActivity.java:83-85` finds/creates `CreateTorrentDialog`; lifecycle subscription at lines 96-109.
- `CreateTorrentDialog.java`: factory at 87; lifecycle at 96-140; dialog setup at 172-194; build/error paths around 280-401; ActivityResult launchers around 500-546.
- This establishes candidate caller chains, not complete row-by-row route verification.

