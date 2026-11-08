# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 73 part (BaseAlertDialog, ClipboardDialog, FileItem, FragmentCallback,
# ManageAllFilesWarningDialog). Hand-written edges only; UNREACHABLE entries for
# the 7 UNREACHABLE rows; no SUPPRESS entries (see note below).
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b073_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: merger staging-A1
# graphs/LibreTorrent/scratch/merge-ready/batch73-merge-ready.md (33 REACHABLE /
# 7 UNREACHABLE / 0 OPEN, counted from the table labels; the file's header
# counts are stale pre-A1/pre-Phase-3 prose and are NOT used).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here: buildDialog, lambda$buildDialog$0/$1/$3,
# newInstance, onCreateDialog, SharedViewModel.observeEvents/sendEvent.
# SUPPRESS: recomputed from auto_calls.json + javap for this batch (see REPORT.md).
# No auto CALL edge runs from a REACHABLE method in batches 73-77 into a batch-73
# UNREACHABLE method, so no intra-group SUPPRESS entry applies. The one
# cross-group candidate (Utils.showManageAllFilesWarningDialog, batch 58
# REACHABLE, -> ManageAllFilesWarningDialog.newInstance) is reported in
# REPORT.md for merger reconciliation, not suppressed here.

# BaseAlertDialog button lambdas: bytecode-verified (javap -c -p) that
# $0/$1/$2 each call makeEvent + sendEvent + dismiss; $3 is the onShow
# listener that installs the three button listeners. The positive/negative/
# neutral assignment follows the batch file's source order (positive,
# negative, neutral); a swap within the group would not change any label.
e('BaseAlertDialog.lambda$buildDialog$3', 'BaseAlertDialog.lambda$buildDialog$2', 'FRAMEWORK', 'Neutral-button click dispatch installed by the onShow listener',
  cls='non_standard', via='Dialog button click dispatch',
  evidence='INFERRED button click dispatch; SRC ui/BaseAlertDialog.java:167-194')
e('BaseAlertDialog.lambda$buildDialog$0', 'BaseAlertDialog.makeEvent', 'CALL', 'Positive-button lambda builds its click event',
  cls='explicit', evidence='SRC ui/BaseAlertDialog.java:173-177; SRC ui/BaseAlertDialog.java:138-141')
e('BaseAlertDialog.makeEvent', 'BaseAlertDialog$Event.<init>', 'CALL', 'makeEvent constructs the click event',
  cls='explicit', evidence='SRC ui/BaseAlertDialog.java:138-141; SRC ui/BaseAlertDialog.java:79-91')
e('BaseAlertDialog.buildDialog', 'BaseAlertDialog$EventType.<clinit>', 'FRAMEWORK', 'First use of an EventType constant initialises the enum',
  cls='non_standard', via='JVM enum initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/BaseAlertDialog.java:71-77; SRC ui/BaseAlertDialog.java:167-194')
e('BaseAlertDialog.onCreateDialog', 'BaseAlertDialog$SharedViewModel.<init>', 'CALL', 'onCreateDialog obtains the SharedViewModel from the provider',
  cls='non_standard', via='ViewModelProvider.get dispatch',
  evidence='INFERRED provider dispatch; SRC ui/BaseAlertDialog.java:116-118')

# ClipboardDialog.
e('ClipboardDialog.newInstance', 'ClipboardDialog.<init>', 'CALL', 'newInstance constructs the dialog',
  cls='explicit', evidence='SRC ui/ClipboardDialog.java:73-77')
e('ClipboardDialog.newInstance', 'ClipboardDialog.<clinit>', 'FRAMEWORK', 'First use of the dialog class initialises its TAG field',
  cls='non_standard', via='JVM class initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/ClipboardDialog.java:40; SRC ui/ClipboardDialog.java:73-77')
e('ClipboardDialog.newInstance', 'ClipboardDialog.onAttach', 'LIFECYCLE', 'Attach the dialog when FragmentManager shows it',
  evidence='SRC ui/ClipboardDialog.java:73-77; SRC ui/ClipboardDialog.java:84-90')
e('ClipboardDialog.onAttach', 'ClipboardDialog.onCreateDialog', 'LIFECYCLE', 'Create the dialog after attachment',
  evidence='SRC ui/ClipboardDialog.java:84-90; SRC ui/ClipboardDialog.java:94-116')
e('ClipboardDialog.onCreateDialog', 'ClipboardDialog.lambda$onCreateDialog$0', 'FRAMEWORK', 'Negative-button (cancel) click dismisses the dialog',
  cls='non_standard', via='Dialog button click dispatch',
  evidence='INFERRED click dispatch; SRC ui/ClipboardDialog.java:102-103')
e('ClipboardDialog.onCreateDialog', 'ClipboardDialog.lambda$onCreateDialog$1', 'FRAMEWORK', 'Adapter item click selects the clipboard item',
  cls='non_standard', via='Dialog list-item click dispatch',
  evidence='INFERRED click dispatch; SRC ui/ClipboardDialog.java:109-113')
e('ClipboardDialog.lambda$onCreateDialog$1', 'ClipboardDialog$Item.<init>', 'CALL', 'Item click builds the selected item',
  cls='explicit', evidence='SRC ui/ClipboardDialog.java:109-113; SRC ui/ClipboardDialog.java:64-70')
e('ClipboardDialog.onCreateDialog', 'ClipboardDialog$SharedViewModel.<init>', 'CALL', 'onCreateDialog obtains the SharedViewModel from the provider',
  cls='non_standard', via='ViewModelProvider.get dispatch',
  evidence='INFERRED provider dispatch; SRC ui/ClipboardDialog.java:99')
e('ClipboardDialog.lambda$onCreateDialog$1', 'ClipboardDialog$SharedViewModel.sendSelectedItem', 'CALL', 'Item click sends the selected item',
  cls='explicit', evidence='SRC ui/ClipboardDialog.java:109-113; SRC ui/ClipboardDialog.java:55-58')
e('AddFeedDialog.showClipboardDialog', 'ClipboardDialog.newInstance', 'CALL', 'Feed dialog shows the clipboard dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:291-301')
e('AddFeedDialog.subscribeAlertDialog', 'ClipboardDialog$SharedViewModel.observeSelectedItem', 'CALL', 'Feed dialog subscribes to clipboard selections',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:325-328')

# FileItem: subclass-anchored routes (TorrentContentFileItem /
# DownloadableFileItem both extend FileItem; printed super calls).
e('DetailTorrentFilesFragment.subscribeAdapter', 'FileItem.<clinit>', 'FRAMEWORK', 'First subclass construction initialises the FileItem superclass',
  cls='non_standard', via='JVM superclass initialisation on first subclass construction',
  evidence='INFERRED JVM dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:154-167; SRC ui/FileItem.java:70-84')
e('TorrentContentFileItem.<init>(TorrentContentFileTree)', 'FileItem.<init>(int,String,boolean,long)', 'CALL', 'Subclass tree constructor passes fields to the FileItem constructor',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFileItem.java:38-41; SRC ui/FileItem.java:39-46')
e('TorrentContentFileItem.<init>(Parcel)', 'FileItem.<init>(Parcel)', 'CALL', 'Subclass parcel constructor passes the parcel to the FileItem parcel constructor',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFileItem.java:47-50; SRC ui/FileItem.java:47-54')
e('TorrentContentFilesAdapter$1.areItemsTheSame', 'FileItem.equals', 'CALL', 'DiffUtil item comparison delegates to FileItem equals',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:118-123; SRC ui/FileItem.java:86-100')
e('TorrentContentFilesAdapter.onBindViewHolder', 'FileItem.hashCode', 'CALL', 'SelectionTracker key lookup hashes the file item',
  cls='non_standard', via='SelectionTracker key hashCode dispatch on isSelected',
  evidence='INFERRED library dispatch; SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:85-91; SRC ui/FileItem.java:102-112')
e('TorrentContentFileItem.writeToParcel', 'FileItem.writeToParcel', 'CALL', 'Subclass parceling writes the base fields first',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFileItem.java:62-66; SRC ui/FileItem.java:61-68')
e('FileItem.<clinit>', 'FileItem$1.<init>', 'CALL', 'CREATOR field initialiser constructs the anonymous creator',
  cls='explicit', evidence='SRC ui/FileItem.java:70-84')

# FragmentCallback: first printed active use is AddFeedDialog.finish.
e('AddFeedDialog.finish', 'FragmentCallback.<clinit>', 'FRAMEWORK', 'First FragmentCallback use initialises the interface',
  cls='non_standard', via='JVM interface initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/FragmentCallback.java:31-33; SRC ui/addfeed/AddFeedDialog.java:429-433')
e('AddFeedDialog.finish', 'FragmentCallback$ResultCode.<clinit>', 'FRAMEWORK', 'First ResultCode value use initialises the enum',
  cls='non_standard', via='JVM enum initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/FragmentCallback.java:35-37; SRC ui/addfeed/AddFeedDialog.java:429-433')

UNREACHABLE.update({
    'FileItem.compareTo': ('no_trigger_in_app',
        'Definition FileItem:115-118. Saved full-tree grep over all 252 app Java files: zero sort sites for a FileItem-typed list and zero explicit compareTo calls on a FileItem receiver; both file-list adapters submit unsorted lists and neither subclass overrides compareTo. Flips on any printed sort of a FileItem-typed list or explicit compareTo call on a FileItem receiver.',
        'INFERRED saved full-tree grep 2026-11-01 over 252 app Java files + complete-tree re-check (281 Java + 73 XML): zero FileItem/compareTo/sort hits',
        'INFERRED'),
    'FileItem.describeContents': ('framework_never_calls',
        'A1 2026-11-01: full-tree grep over src/main (633 files): 13 putParcelable sites, 0 putParcelableArrayList, no site parcels a plain FileItem; only parcel-storage site names TorrentContentFileItem (DetailTorrentFilesFragment:227), which overrides describeContents, so framework dispatch never reaches FileItem.describeContents. auto_calls.json: 0 edges into this method. Definition FileItem:56-59.',
        'INFERRED A1 full-tree grep (633 files) + auto_calls.json 0 edges',
        'INFERRED'),
    'FileItem.toString': ('no_trigger_in_app',
        'Definition FileItem:122-130. No printed caller; the only super-calls sit inside DownloadableFileItem.toString (batch 82 row 13) and TorrentContentFileItem.toString (batch 92 row 35), both themselves UNREACHABLE no_trigger_in_app. Phase-3 L1 verdict applied. Flips if either subclass toString flips to REACHABLE.',
        'INFERRED Phase-3 L1 verdict; subclass super-call sites DownloadableFileItem:82, TorrentContentFileItem:105',
        'INFERRED'),
    'FileItem$1.createFromParcel': ('no_trigger_in_app',
        'A1 2026-11-01: full-tree grep (633 files): no unparcel site for FileItem, no createParcelableStorage(FileItem.class), no FileItem.CREATOR reference outside ui/FileItem.java; the DetailTorrentFilesFragment:227 storage site dispatches through TorrentContentFileItem.CREATOR. auto_calls.json: 0 edges. Definition FileItem:74-77.',
        'INFERRED A1 full-tree grep (633 files) + auto_calls.json 0 edges',
        'INFERRED'),
    'FileItem$1.newArray': ('no_trigger_in_app',
        'Body FileItem:80-83, framework CREATOR dispatch only, no printed parceling context for a plain FileItem. Phase-3 L2 verdict applied.',
        'INFERRED Phase-3 L2 verdict; definition FileItem:80-83',
        'INFERRED'),
    'ManageAllFilesWarningDialog.<init>': ('closed_by_api_level',
        'Only construction is new ManageAllFilesWarningDialog() at ManageAllFilesWarningDialog:34 inside newInstance (row 40), itself closed at API 27. Saved full-tree grep: no other construction site. Flips together with row 40 and batch 74 row 1 on any printed non-gated newInstance caller.',
        'INFERRED saved full-tree grep over 252 app Java files + complete-tree re-check (281 Java + 73 XML)',
        'INFERRED'),
    'ManageAllFilesWarningDialog.newInstance': ('closed_by_api_level',
        'Definition ManageAllFilesWarningDialog:33-40. Exactly one caller in the whole tree, Utils.showManageAllFilesWarningDialog at Utils:713, behind the early return at Utils:704-707 (SDK_INT < R true at API 27), so the call site itself never runs at API 27. Flips together with row 39 and batch 74 row 1 on any printed non-gated caller.',
        'INFERRED saved full-tree grep over 252 app Java files + complete-tree re-check (281 Java + 73 XML); sole caller Utils:713',
        'INFERRED'),
})

# No intra-group SUPPRESS entry: recomputed from auto_calls.json + javap, no
# auto CALL edge runs from a REACHABLE method in batches 73-77 into a batch-73
# UNREACHABLE method (see REPORT.md; the cross-group Utils -> newInstance
# candidate is left for merger reconciliation).
SUPPRESS.update(set())
