# LibreTorrent batch 73 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, exact batch 73 rows only. Count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. The rows span alert/clipboard dialogs, Parcel model methods, an enum, and a warning dialog. Source includes local dialog listener-to-event calls and Parcelable implementations, but this bounded review did not establish complete entry routes, framework dispatch, or all relevant callers. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `BaseAlertDialog.buildDialog` | `(Ljava/lang/String;Ljava/lang/String;Landroid/view/View;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Landroidx/appcompat/app/AlertDialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 2 | `BaseAlertDialog.lambda$buildDialog$0` | `(ZLandroid/view/View;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 3 | `BaseAlertDialog.lambda$buildDialog$1` | `(ZLandroid/view/View;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 4 | `BaseAlertDialog.lambda$buildDialog$2` | `(ZLandroid/view/View;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 5 | `BaseAlertDialog.lambda$buildDialog$3` | `(Landroidx/appcompat/app/AlertDialog;ZLandroid/content/DialogInterface;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 6 | `BaseAlertDialog.makeEvent` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$EventType;)Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 7 | `BaseAlertDialog.newInstance` | `(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 8 | `BaseAlertDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 9 | `BaseAlertDialog$Event.<init>` | `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$EventType;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 10 | `BaseAlertDialog$EventType.<clinit>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 11 | `BaseAlertDialog$SharedViewModel.<init>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 12 | `BaseAlertDialog$SharedViewModel.observeEvents` | `()Lio/reactivex/Observable;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 13 | `BaseAlertDialog$SharedViewModel.sendEvent` | `(Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 14 | `ClipboardDialog.<clinit>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 15 | `ClipboardDialog.<init>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 16 | `ClipboardDialog.lambda$onCreateDialog$0` | `(Landroid/content/DialogInterface;I)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 17 | `ClipboardDialog.lambda$onCreateDialog$1` | `(Landroid/content/DialogInterface;I)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 18 | `ClipboardDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 19 | `ClipboardDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 20 | `ClipboardDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 21 | `ClipboardDialog$Item.<init>` | `(Ljava/lang/String;Ljava/lang/String;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 22 | `ClipboardDialog$SharedViewModel.<init>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 23 | `ClipboardDialog$SharedViewModel.observeSelectedItem` | `()Lio/reactivex/Observable;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 24 | `ClipboardDialog$SharedViewModel.sendSelectedItem` | `(Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog$Item;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 25 | `FileItem.<clinit>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 26 | `FileItem.<init>(int,String,boolean,long)` | `(ILjava/lang/String;ZJ)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 27 | `FileItem.<init>(Parcel)` | `(Landroid/os/Parcel;)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 28 | `FileItem.compareTo` | `(Lorg/proninyaroslav/libretorrent/ui/FileItem;)I` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 29 | `FileItem.describeContents` | `()I` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 30 | `FileItem.equals` | `(Ljava/lang/Object;)Z` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 31 | `FileItem.hashCode` | `()I` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 32 | `FileItem.toString` | `()Ljava/lang/String;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 33 | `FileItem.writeToParcel` | `(Landroid/os/Parcel;I)V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 34 | `FileItem$1.<init>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 35 | `FileItem$1.createFromParcel` | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/ui/FileItem;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 36 | `FileItem$1.newArray` | `(I)[Lorg/proninyaroslav/libretorrent/ui/FileItem;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 37 | `FragmentCallback.<clinit>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 38 | `FragmentCallback$ResultCode.<clinit>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 39 | `ManageAllFilesWarningDialog.<init>` | `()V` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |
| 40 | `ManageAllFilesWarningDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/ManageAllFilesWarningDialog;` | OPEN | Source definition/local callback exists, but complete route from app entry is not established in this bounded pass. |

## Evidence
- `BaseAlertDialog.java` contains event observable and button listeners (`observeEvents`, `sendEvent`, `buildDialog`, lines around 60-194).
- `ClipboardDialog.java` contains `observeSelectedItem`, `sendSelectedItem`, dialog construction/listeners (around lines 50-112).
- `FileItem.java` implements Parcelable/Comparable, including `describeContents`, `writeToParcel`, and `compareTo` (lines 32-117).
- `ManageAllFilesWarningDialog.java` creates a subclass dialog through `buildDialog` (lines 32-56).
These local code facts do not establish full app-entry routes for the complete target list.

