# Citation-form rework 2026-11-01: evidence paths with a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS, line ranges unchanged (full paths remain in untouched .md/printed files).
# Batch 74 part (ManageAllFilesWarningDialog, PermissionDeniedDialog,
# PermissionManager, SendTextToClipboard, TorrentNotifier, AddFeedActivity,
# AddFeedDialog). Hand-written edges only; UNREACHABLE entries for the 2
# UNREACHABLE rows; no SUPPRESS entries (see note below).
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b074_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch74-merge-ready.md (38 REACHABLE /
# 2 UNREACHABLE / 0 OPEN, counted from the table labels).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# SUPPRESS: recomputed from auto_calls.json + javap for this batch (see REPORT.md).
# ManageAllFilesWarningDialog.onCreateDialog has 0 auto callers and
# PermissionManager.lambda$new$0 has only a REGISTER entry from
# PermissionManager.<init> (REGISTER edges do not confer reachability in the
# build), so no intra-group SUPPRESS entry applies.

# PermissionManager internal calls.
e('PermissionManager.checkPermissions', 'PermissionManager.checkNotificationsPermissions', 'CALL', 'checkPermissions checks the notification permission',
  cls='explicit', evidence='SRC ui/PermissionManager.java:146-148; SRC ui/PermissionManager.java:137-144')
e('PermissionManager.checkPermissions', 'PermissionManager.checkStoragePermissions', 'CALL', 'checkPermissions checks the storage permission',
  cls='explicit', evidence='SRC ui/PermissionManager.java:146-148; SRC ui/PermissionManager.java:128-135')

# TorrentNotifier: singleton construction, legacy settings, and the
# TorrentEngine / SchedulerReceiver call sites.
e('TorrentNotifier.getInstance', 'TorrentNotifier.<init>', 'CALL', 'getInstance constructs the singleton notifier',
  cls='explicit', evidence='SRC ui/TorrentNotifier.java:65-73; SRC ui/TorrentNotifier.java:75-79')
e('TorrentNotifier.makeTorrentFinishedNotify', 'TorrentNotifier.applyLegacyNotifySettings', 'CALL', 'Finished notification applies the legacy settings unconditionally',
  cls='explicit', evidence='SRC ui/TorrentNotifier.java:212-228; SRC ui/TorrentNotifier.java:275-278')
e('TorrentEngine.startStreamingServer', 'TorrentNotifier.makeErrorNotify', 'CALL', 'Streaming-server start failure notifies the error',
  cls='explicit', evidence='SRC TorrentEngine.java:1070-1076; SRC ui/TorrentNotifier.java:148-162')
e('SchedulerReceiver.onStartApp', 'TorrentNotifier.makeExactAlarmPermissionNotify', 'CALL', 'Scheduled start without an exact-alarm grant notifies the permission state',
  cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:65-75; SRC ui/TorrentNotifier.java:244-258')
e('TorrentEngine$5.onTorrentMoving', 'TorrentNotifier.makeMovingTorrentNotify', 'CALL', 'Torrent-moved listener notifies the move',
  cls='explicit', evidence='SRC TorrentEngine.java:1329-1341; SRC ui/TorrentNotifier.java:196-210')
e('TorrentEngine$5.onNatError', 'TorrentNotifier.makeNatErrorNotify', 'CALL', 'NAT error listener notifies when NAT errors are shown',
  cls='explicit', evidence='SRC TorrentEngine.java:1392-1397; SRC ui/TorrentNotifier.java:180-194')
e('TorrentEngine$5.onSessionError', 'TorrentNotifier.makeSessionErrorNotify', 'CALL', 'Session error listener notifies after the error filter',
  cls='explicit', evidence='SRC TorrentEngine.java:1384-1390; SRC ui/TorrentNotifier.java:164-178')
e('TorrentEngine.handleAddTorrentError', 'TorrentNotifier.makeTorrentErrorNotify', 'CALL', 'Add-torrent error path notifies the error',
  cls='explicit', evidence='SRC TorrentEngine.java:1207-1221; SRC ui/TorrentNotifier.java:116-130')
e('TorrentEngine$5.onTorrentFinished', 'TorrentNotifier.makeTorrentFinishedNotify', 'CALL', 'Torrent-finished listener notifies on the Rx subscribe path',
  cls='non_standard', via='Rx subscribe dispatch inside onTorrentFinished',
  evidence='INFERRED Rx dispatch; SRC TorrentEngine.java:1305-1314; SRC ui/TorrentNotifier.java:212-228')
e('TorrentEngine.handleAddTorrentError', 'TorrentNotifier.makeTorrentInfoNotify', 'CALL', 'Already-exists add-torrent branch notifies the info',
  cls='explicit', evidence='SRC TorrentEngine.java:1207-1210; SRC ui/TorrentNotifier.java:132-146')

# AddFeedDialog: class initialisation and the dialog-button / Rx routes.
# Button-lambda mapping is bytecode-verified (javap -c -p): $6 calls
# addChannel, $5 calls deleteFeedDialog, $4 calls updateChannel, $7 calls finish.
e('AddFeedActivity.onCreate', 'AddFeedDialog.<clinit>', 'FRAMEWORK', 'First AddFeedDialog use initialises the dialog class',
  cls='non_standard', via='JVM class initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/addfeed/AddFeedDialog.java:61; SRC ui/addfeed/AddFeedActivity.java:61-66')
e('AddFeedDialog.lambda$initAlertDialog$6', 'AddFeedDialog.addChannel', 'CALL', 'Add-button click adds the channel',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:282-283; SRC ui/addfeed/AddFeedDialog.java:379-393')
e('AddFeedDialog.addChannel', 'AddFeedDialog.checkUrlField', 'CALL', 'addChannel validates the URL field first',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:379-382; SRC ui/addfeed/AddFeedDialog.java:360-377')
e('AddFeedDialog.lambda$subscribeAlertDialog$9', 'AddFeedDialog.deleteChannel', 'CALL', 'Delete-confirmation event deletes the channel',
  cls='non_standard', via='Rx subscribe dispatch inside subscribeAlertDialog',
  evidence='INFERRED Rx dispatch; SRC ui/addfeed/AddFeedDialog.java:303-315; SRC ui/addfeed/AddFeedDialog.java:411-422')
e('AddFeedDialog.lambda$initAlertDialog$5', 'AddFeedDialog.deleteFeedDialog', 'CALL', 'Delete-button click opens the delete-confirmation dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:279-280; SRC ui/addfeed/AddFeedDialog.java:340-358')
e('AddFeedDialog.lambda$subscribeAlertDialog$10', 'AddFeedDialog.handleUrlClipItem', 'CALL', 'Clipboard-item event handles the clipped URL',
  cls='non_standard', via='Rx subscribe dispatch inside subscribeAlertDialog',
  evidence='INFERRED Rx dispatch; SRC ui/addfeed/AddFeedDialog.java:325-328; SRC ui/addfeed/AddFeedDialog.java:332-338')

UNREACHABLE.update({
    'ManageAllFilesWarningDialog.onCreateDialog': ('closed_by_api_level',
        'Definition ManageAllFilesWarningDialog:44-65. It runs only after the dialog is created and shown, and creation is closed at API 27 (batch 73 rows 39-40, same route): saved full-tree grep confirms the only newInstance caller is Utils:713, behind the early return at Utils:704-707 (SDK_INT < R true at API 27). Flips together with batch 73 rows 39-40 on any printed non-gated newInstance caller.',
        'INFERRED saved full-tree grep over 252 app Java files + complete-tree re-check (281 Java + 73 XML); sole newInstance caller Utils:713',
        'INFERRED'),
    'PermissionManager.lambda$new$0': ('closed_by_api_level',
        'The StartActivityForResult result lambda at PermissionManager:63-66 (calls callback.onStorageResult(checkStoragePermissions(), ...)). Saved full-tree grep: the field manageExternalStoragePermission is private with exactly one registration, at PermissionManager:61-67, gated at :60 on SDK_INT >= R (false at API 27), and exactly one launch, at requestPermissions:100-104, behind the same gate. Descriptor (Callback,ActivityResult) matches this lambda, not $1; bytecode-verified ($0 calls checkStoragePermissions, $1 takes Map). Flips on any printed non-gated registration of this launcher.',
        'INFERRED saved full-tree grep over 252 app Java files + complete-tree re-check (281 Java + 73 XML); sole registration PermissionManager:61-67, sole launch :100-104',
        'INFERRED'),
})

# No intra-group SUPPRESS entry: onCreateDialog has 0 auto callers and
# lambda$new$0 has only a REGISTER entry (REGISTER edges do not confer
# reachability), so no auto CALL edge from a REACHABLE method needs
# suppressing for this batch (see REPORT.md).
SUPPRESS.update(set())
