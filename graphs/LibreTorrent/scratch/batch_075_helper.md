# LibreTorrent batch 75 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, exact batch 75 members only. Count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch covers AddFeedDialog lifecycle, dialog setup, listener lambdas, clipboard integration, and mutable view state. Source search shows a plausible AddFeedActivity-to-dialog launch and local listener calls, but this bounded review did not verify every row against the full entry route and its conditions. Mark all OPEN pending that audit.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `AddFeedDialog.initAlertDialog` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 2 | `AddFeedDialog.initLayoutView` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 3 | `AddFeedDialog.initParams` | `(Landroid/net/Uri;J)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 4 | `AddFeedDialog.lambda$initAlertDialog$4` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 5 | `AddFeedDialog.lambda$initAlertDialog$5` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 6 | `AddFeedDialog.lambda$initAlertDialog$6` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 7 | `AddFeedDialog.lambda$initAlertDialog$7` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 8 | `AddFeedDialog.lambda$initAlertDialog$8` | `(Landroid/content/DialogInterface;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 9 | `AddFeedDialog.lambda$initLayoutView$2` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 10 | `AddFeedDialog.lambda$initLayoutView$3` | `(Landroid/view/View;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 11 | `AddFeedDialog.lambda$new$0` | `(Z)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 12 | `AddFeedDialog.lambda$onResume$1` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 13 | `AddFeedDialog.lambda$subscribeAlertDialog$10` | `(Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog$Item;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 14 | `AddFeedDialog.lambda$subscribeAlertDialog$9` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 15 | `AddFeedDialog.newInstance(long)` | `(J)Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 16 | `AddFeedDialog.newInstance(Uri)` | `(Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 17 | `AddFeedDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 18 | `AddFeedDialog.onBackPressed` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 19 | `AddFeedDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 20 | `AddFeedDialog.onDestroyView` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 21 | `AddFeedDialog.onResume` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 22 | `AddFeedDialog.onStart` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 23 | `AddFeedDialog.onStop` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 24 | `AddFeedDialog.showClipboardDialog` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 25 | `AddFeedDialog.subscribeAlertDialog` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 26 | `AddFeedDialog.subscribeClipboardManager` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 27 | `AddFeedDialog.switchClipboardButton` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 28 | `AddFeedDialog.unsubscribeClipboardManager` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 29 | `AddFeedDialog.updateChannel` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 30 | `AddFeedDialog$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 31 | `AddFeedDialog$1.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 32 | `AddFeedDialog$1.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 33 | `AddFeedDialog$1.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 34 | `AddFeedDialog$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 35 | `AddFeedDialog$2.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 36 | `AddFeedDialog$2.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 37 | `AddFeedDialog$2.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 38 | `AddFeedMutableParams.<init>` | `()V` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 39 | `AddFeedMutableParams.getFeedId` | `()J` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |
| 40 | `AddFeedMutableParams.getFilter` | `()Ljava/lang/String;` | OPEN | Local dialog/listener/lifecycle implementation is visible; complete source-verified entry routes were not audited for each target. |

## Evidence
- `AddFeedDialog.java`: factories at lines 78 and 89; lifecycle methods at 122, 141, 161, 170, 180, 213; local setup/listener methods at 220, 258, 291, 303; update flow at 395.
- Search found `AddFeedActivity` calling `AddFeedDialog.newInstance(...)` around lines 61-63.
- `AddFeedMutableParams.java` contains `getFeedId` and `getFilter`.
These findings indicate candidate routes, but are not a complete method-by-method route verification.

