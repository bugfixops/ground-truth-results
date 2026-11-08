# Batch 121 (Kiro, 2026-11-03): the last 86 UNRESOLVED methods (handover Step 1, case C).
# Path A: each group is reached by adding the missing delivery edge from a caller that is already
# REACHABLE; the REGISTER edges already in the graph record the registration, these edges record
# the framework/library delivering the callback. Rulings D2 and D3 are applied as ordered.
# Every cited line is printed in graphs/LibreTorrent/scratch/b121_printed.txt; see parts/b121.md.
# Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

_CLICK = 'FW-SRC core/java/android/view/View.java:6289-6305'

# ---- G1. TorrentService start (Utils.startServiceBackground posts the start on API >= O).
e('Utils.startServiceBackground', 'Utils.lambda$startServiceBackground$0', 'FRAMEWORK',
  'Main-thread Handler runs the posted startForegroundService runnable',
  guard='Build.VERSION.SDK_INT >= Build.VERSION_CODES.O', cls='standard',
  evidence='SRC Utils.java:426-430; FW-SRC core/java/android/os/Handler.java:95-106,355-358,789-791')

# ---- G2. SchedulerReceiver: the exact alarm set by Scheduler.setStartStopAppAlarm fires.
e('Scheduler.setStartStopAppAlarm', 'SchedulerReceiver.<init>', 'FRAMEWORK',
  'AlarmManager fires the scheduled start/stop alarm and instantiates the receiver',
  env='calendar.getTimeInMillis()', cls='standard',
  evidence='SRC service/Scheduler.java:80-104; FW-SRC services/core/java/com/android/server/AlarmManagerService.java:3117-3126; core/java/android/app/ActivityThread.java:3162-3166')
e('Scheduler.setStartStopAppAlarm', 'SchedulerReceiver.onReceive', 'FRAMEWORK',
  'AlarmManager fires the scheduled start/stop alarm and delivers the broadcast',
  env='calendar.getTimeInMillis()', cls='standard',
  evidence='SRC service/Scheduler.java:80-104; receiver/SchedulerReceiver.java:43-63; FW-SRC services/core/java/com/android/server/AlarmManagerService.java:3117-3126; core/java/android/app/ActivityThread.java:3186-3187')

# ---- G3. Text watchers (user edits a text field).
e('AddTagDialog.initLayoutView', 'AddTagDialog$1.afterTextChanged', 'FRAMEWORK',
  'User edits the tag name; the TextView notifies its TextWatcher',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:137-152; FW-SRC core/java/android/widget/TextView.java:9375-9382')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment$1.afterTextChanged', 'FRAMEWORK',
  'User edits the torrent name; the TextView notifies its TextWatcher',
  cls='standard', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:106-119; FW-SRC core/java/android/widget/TextView.java:9375-9382')

# ---- G4. Data-binding Observable callbacks.
e('AddTorrentActivity.subscribeParamsChanged', 'AddTorrentActivity$2.onPropertyChanged', 'FRAMEWORK',
  'User toggles an add-torrent option; the mutable params notify the registered callback',
  cls='non_standard', via='androidx.databinding BaseObservable property-changed dispatch',
  evidence='INFERRED Observable dispatch; SRC ui/addtorrent/AddTorrentActivity.java:193-195,201-215; ui/addtorrent/AddTorrentMutableParams.java:112-115')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$2.onPropertyChanged', 'FRAMEWORK',
  'The constructor sets the download dir right after registering the dir-path callback',
  cls='non_standard', via='androidx.databinding ObservableField property-changed dispatch',
  evidence='INFERRED Observable dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:141,145-146,348-366')
e('AddTorrentViewModel$2.onPropertyChanged', 'AddTorrentViewModel$2.lambda$onPropertyChanged$0', 'FRAMEWORK',
  'RxJava runs the free-space/dir-name runnable on the io scheduler',
  guard='dirPath != null', cls='non_standard', via='RxJava Completable.fromRunnable subscribeOn(io)',
  evidence='INFERRED RxJava subscribe dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:350-364')
e('AddTorrentViewModel$TorrentDecodeTask.readTorrentFile', 'AddTorrentViewModel$1.onPropertyChanged', 'FRAMEWORK',
  'info.set with the decoded torrent notifies the info callback',
  cls='non_standard', via='androidx.databinding ObservableField property-changed dispatch',
  evidence='INFERRED Observable dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:140,281-294,337-345')

# ---- G5. Add-torrent files page (Rx subscription and row clicks).
e('AddTorrentFilesFragment.subscribeAdapter', 'AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'FRAMEWORK',
  'RxJava maps each emitted children list to file items',
  cls='non_standard', via='RxJava Flowable.flatMapSingle', evidence='INFERRED RxJava dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:111-119')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'DownloadableFileItem.<init>(BencodeFileTree)', 'FRAMEWORK',
  'RxJava map applies the DownloadableFileItem constructor reference',
  cls='non_standard', via='RxJava Flowable.map constructor reference', evidence='INFERRED RxJava dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:115-118')
e('AddTorrentFilesFragment.subscribeAdapter', 'AddTorrentFilesFragment.lambda$subscribeAdapter$1', 'FRAMEWORK',
  'RxJava delivers the file-item list on the main thread',
  cls='non_standard', via='RxJava observeOn(mainThread).subscribe', evidence='INFERRED RxJava dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:120-124')
e('DownloadableFilesAdapter$ViewHolder.bind', 'DownloadableFilesAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK',
  'User taps a file row', cls='standard', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:102-113; ' + _CLICK)
e('DownloadableFilesAdapter$ViewHolder.bind', 'DownloadableFilesAdapter$ViewHolder.lambda$bind$1', 'FRAMEWORK',
  'User taps a file row check box', guard='!isParentDir (check box VISIBLE)',
  cls='standard', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:114-117,137-145; ' + _CLICK)

# ---- G6. Choose-directory result on the add-torrent info page (mirrors DetailTorrentInfoFragment.lambda$new$2).
e('FileManagerDialog.returnDirectoryUri', 'AddTorrentInfoFragment.lambda$new$2', 'RESULT',
  'Return a chosen save directory through the registered ActivityResult launcher',
  guard='RESULT_OK and AddTorrentInfoFragment launched FileManagerDialog in DIR_CHOOSER_MODE', cls='non_standard',
  via='AndroidX ActivityResultRegistry',
  evidence='INFERRED AndroidX ActivityResult delivery; SRC ui/addtorrent/AddTorrentInfoFragment.java:150-161,192-213; ui/filemanager/FileManagerDialog.java:557-568')

# ---- G7. Add-tag chip -> SelectTagActivity -> SelectTagDialog -> result.
e('TorrentTagsList.buildAddTagButton', 'TorrentTagsList.lambda$buildAddTagButton$1', 'FRAMEWORK',
  'User taps the add-tag chip', cls='standard', evidence='SRC ui/tag/TorrentTagsList.java:78-86; ' + _CLICK)
e('AddTorrentInfoFragment$2.onAddTagClick', 'AddTorrentInfoFragment$2.lambda$onAddTagClick$0', 'FRAMEWORK',
  'RxJava maps the current tags to ids', cls='non_standard', via='RxJava Observable.map',
  evidence='INFERRED RxJava dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:165-168')
e('AddTorrentInfoFragment$2.onAddTagClick', 'AddTorrentInfoFragment$2.lambda$onAddTagClick$1', 'FRAMEWORK',
  'RxJava delivers the id list to the launcher lambda', cls='non_standard', via='RxJava Single.subscribe',
  evidence='INFERRED RxJava dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:166-177')
e('DetailTorrentInfoFragment$1.lambda$onAddTagClick$2', 'SelectTagActivity.<init>', 'INTENT',
  'Launch SelectTagActivity from the torrent detail add-tag chip', cls='standard',
  evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:157-163; AndroidManifest.xml:248-250; FW-SRC core/java/android/app/ActivityThread.java:2665-2671')
e('DetailTorrentInfoFragment$1.lambda$onAddTagClick$2', 'SelectTagActivity.onCreate', 'INTENT',
  'Create SelectTagActivity from the torrent detail add-tag chip', cls='standard',
  evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:157-163; AndroidManifest.xml:248-250; FW-SRC core/java/android/app/ActivityThread.java:2727-2732')
e('SelectTagActivity.onFragmentFinished', 'AddTorrentInfoFragment.lambda$new$1', 'RESULT',
  'Return the selected tag through the registered ActivityResult launcher',
  guard='code == ResultCode.OK (setResult(RESULT_OK, intent))', cls='non_standard', via='AndroidX ActivityResultRegistry',
  evidence='INFERRED AndroidX ActivityResult delivery; SRC ui/tag/SelectTagActivity.java:57-66; ui/addtorrent/AddTorrentInfoFragment.java:137-148')
e('SelectTagDialog.initAlertDialog', 'SelectTagDialog.lambda$initAlertDialog$3', 'FRAMEWORK',
  'The dialog is shown and runs its OnShowListener', cls='non_standard', via='AppCompat AlertDialog OnShowListener',
  evidence='INFERRED AppCompat AlertDialog show dispatch; SRC ui/tag/SelectTagDialog.java:144-162')
e('SelectTagDialog.lambda$initAlertDialog$3', 'SelectTagDialog.lambda$initAlertDialog$1', 'FRAMEWORK',
  'User taps the New tag button', cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:154-158; ' + _CLICK)
e('SelectTagDialog.lambda$initAlertDialog$3', 'SelectTagDialog.lambda$initAlertDialog$2', 'FRAMEWORK',
  'User taps the Cancel button', cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:155,159-161; ' + _CLICK)
e('SelectTagDialog.subscribeTags', 'SelectTagDialog.lambda$subscribeTags$4', 'FRAMEWORK',
  'RxJava maps each emitted tag list to tag items', cls='non_standard', via='RxJava Flowable.flatMapSingle',
  evidence='INFERRED RxJava dispatch; SRC ui/tag/SelectTagDialog.java:165-175')
e('tag.TagsAdapter$ViewHolder.bind', 'tag.TagsAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK',
  'User taps a tag row', needs_state='adapter.getItemCount() > 0', state_kinds=('data',),
  cls='standard', evidence='SRC ui/tag/TagsAdapter.java:98-108; ' + _CLICK)

# ---- D2. TorrentInputStream.toUnsignedByte (ruling D2): same kind as TorrentInputStream.read().
UNREACHABLE.update({
    'TorrentInputStream.toUnsignedByte': ('no_trigger_in_app',
        'Caller: TorrentInputStream.read() (TorrentInputStream.java:234,248), its only caller; read() is UNREACHABLE '
        '(no_trigger_in_app, parts/b041.py), so this private helper never runs (ruling D2).',
        'SRC TorrentInputStream.java:190-196,234,248', 'SOURCE'),
})
