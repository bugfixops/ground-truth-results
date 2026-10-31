# LibreTorrent batch 103 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 103 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. FileManagerDialog source includes user-input, spinner, adapter, media receiver, and URI-return logic; FileManagerNode and spinner adapter provide local model/adapter operations. Dynamic media registration and full opening/caller route, including all branches, were not audited for each target. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `FileManagerDialog.openHomeDirectory` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 2 | `FileManagerDialog.permissionDeniedToast` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 3 | `FileManagerDialog.refreshDir` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 4 | `FileManagerDialog.registerMediaReceiver` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 5 | `FileManagerDialog.reloadSpinner` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 6 | `FileManagerDialog.returnDirectoryUri` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 7 | `FileManagerDialog.returnFileUri` | `(Ljava/lang/String;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 8 | `FileManagerDialog.saveCurDirectoryPath` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 9 | `FileManagerDialog.showCreateFolderErrDialog` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 10 | `FileManagerDialog.showInputNameDialog` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 11 | `FileManagerDialog.showReplaceFileDialog` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 12 | `FileManagerDialog.showSendErrorDialog` | `(Ljava/lang/Exception;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 13 | `FileManagerDialog.subscribeAdapter` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 14 | `FileManagerDialog.subscribeAlertDialog` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 15 | `FileManagerDialog.unregisterMediaReceiver` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 16 | `FileManagerDialog$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerDialog;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 17 | `FileManagerDialog$1.afterTextChanged` | `(Landroid/text/Editable;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 18 | `FileManagerDialog$1.beforeTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 19 | `FileManagerDialog$1.onTextChanged` | `(Ljava/lang/CharSequence;III)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 20 | `FileManagerDialog$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerDialog;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 21 | `FileManagerDialog$2.onItemSelected` | `(Landroid/widget/AdapterView;Landroid/view/View;IJ)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 22 | `FileManagerDialog$2.onNothingSelected` | `(Landroid/widget/AdapterView;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 23 | `FileManagerDialog$3.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerDialog;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 24 | `FileManagerDialog$3.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 25 | `FileManagerDialog$MediaReceiver.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerDialog;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 26 | `FileManagerDialog$MediaReceiver.onReceive` | `(Landroid/content/Context;Landroid/content/Intent;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 27 | `FileManagerNode.<init>` | `(Ljava/lang/String;IZ)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 28 | `FileManagerNode.compareTo` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerNode;)I` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 29 | `FileManagerNode.equals` | `(Ljava/lang/Object;)Z` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 30 | `FileManagerNode.getName` | `()Ljava/lang/String;` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 31 | `FileManagerNode.getType` | `()I` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 32 | `FileManagerNode.isDirectory` | `()Z` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 33 | `FileManagerNode.isEnabled` | `()Z` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 34 | `FileManagerNode.setEnabled` | `(Z)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 35 | `FileManagerNode.setName` | `(Ljava/lang/String;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 36 | `FileManagerNode.setType` | `(I)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 37 | `FileManagerNode.toString` | `()Ljava/lang/String;` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 38 | `FileManagerSpinnerAdapter.<clinit>` | `()V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 39 | `FileManagerSpinnerAdapter.<init>` | `(Landroid/content/Context;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |
| 40 | `FileManagerSpinnerAdapter.addItem` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerSpinnerAdapter$StorageSpinnerItem;)V` | OPEN | Dialog/listener/receiver and node implementation are visible; complete entry and dynamic receiver route not audited for every target. |

## Evidence
- `FileManagerDialog.java:172-240`: click/text/spinner callbacks and media receiver registration.
- `FileManagerDialog.java:276-341`: subscriptions, receiver methods and adapter observer.
- `FileManagerDialog.java:370-464`: errors, file callbacks, refresh and path save.
- `FileManagerDialog.java:518-689`: navigation/URI return, replace dialog, spinner reload and receiver.
- `FileManagerNode.java:30-109`: fields, compare/equality and accessors.
- `FileManagerSpinnerAdapter.java:40-110`: adapter and add-item operations.

