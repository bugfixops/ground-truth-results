# LibreTorrent batch 77 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 77 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. The batch includes AddLinkDialog callbacks/lifecycle, AddLinkViewModel helpers, AddTagActivity/ AddTagDialog methods. Source search reveals concrete local calls and a candidate activity/dialog path, but this bounded pass does not verify every edge/condition end-to-end. Keep all rows OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `AddLinkDialog.lambda$initAlertDialog$4` | `(Landroid/view/View;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 2 | `AddLinkDialog.lambda$initAlertDialog$5` | `(Landroid/view/View;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 3 | `AddLinkDialog.lambda$initAlertDialog$6` | `(Landroid/content/DialogInterface;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 4 | `AddLinkDialog.lambda$initLayoutView$3` | `(Landroid/view/View;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 5 | `AddLinkDialog.lambda$new$2` | `(Z)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 6 | `AddLinkDialog.lambda$onResume$0` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 7 | `AddLinkDialog.lambda$subscribeAlertDialog$1` | `(Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog$Item;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 8 | `AddLinkDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/addlink/AddLinkDialog;` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 9 | `AddLinkDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 10 | `AddLinkDialog.onBackPressed` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 11 | `AddLinkDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 12 | `AddLinkDialog.onDestroyView` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 13 | `AddLinkDialog.onResume` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 14 | `AddLinkDialog.onStart` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 15 | `AddLinkDialog.onStop` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 16 | `AddLinkDialog.showClipboardDialog` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 17 | `AddLinkDialog.subscribeAlertDialog` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 18 | `AddLinkDialog.subscribeClipboardManager` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 19 | `AddLinkDialog.switchClipboardButton` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 20 | `AddLinkDialog.unsubscribeClipboardManager` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 21 | `AddLinkDialog$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addlink/AddLinkDialog;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 22 | `AddLinkDialog$1.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 23 | `AddLinkDialog$1.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 24 | `AddLinkDialog$1.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 25 | `AddLinkViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 26 | `AddLinkViewModel.initLinkFromClipboard` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 27 | `AddLinkViewModel.normalizeUrl` | `(Ljava/lang/String;)Ljava/lang/String;` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 28 | `AddTagActivity.<init>` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 29 | `AddTagActivity.onBackPressed` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 30 | `AddTagActivity.onColorSelected` | `(II)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 31 | `AddTagActivity.onCreate` | `(Landroid/os/Bundle;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 32 | `AddTagActivity.onDialogDismissed` | `(I)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 33 | `AddTagActivity.onFragmentFinished` | `(Landroidx/fragment/app/Fragment;Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 34 | `AddTagDialog.<clinit>` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 35 | `AddTagDialog.<init>` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 36 | `AddTagDialog.addTag` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 37 | `AddTagDialog.checkName` | `()Z` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 38 | `AddTagDialog.finish` | `(Landroid/content/Intent;Lorg/proninyaroslav/libretorrent/ui/FragmentCallback$ResultCode;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 39 | `AddTagDialog.initAlertDialog` | `(Landroid/view/View;)V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |
| 40 | `AddTagDialog.initLayoutView` | `()V` | OPEN | Local dialog/activity/view-model code exists; complete source-verified route for each target has not been established. |

## Evidence
- `AddLinkDialog.java`: lifecycle and setup methods, clipboard listener, click callbacks, and view-model URL normalization calls are present (lines noted in printed evidence).
- `AddTagActivity.java` calls `AddTagDialog.newInstance`; `AddTagDialog.onCreateDialog` calls view and alert setup; button lambda calls `addTag`, which checks name and reports via `finish`.
- These local chains are partial; no row is upgraded without complete route verification.

