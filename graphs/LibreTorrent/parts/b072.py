# Citation-form rework 2026-11-01: evidence paths with a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS, line ranges unchanged (full paths remain in untouched .md/printed files).
# Batch 72 part (Scheduler.setStopAppAlarm; TorrentService + TorrentService$1 listener; BaseAlertDialog).
# Hand-written edges only; rows covered by a pre-existing trunk edge are
# named on the .md Dependencies line and get no duplicate edge here.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b072_printed.txt (this helper's copy:
# scratch/b072_printed.txt).
# Labels/kinds come from the authoritative clone merge-ready batch file;
# nothing is flipped here (see REPORT.md for flagged rows).

e('Utils.lambda$startServiceBackground$0', 'TorrentService.<clinit>', 'CALL', 'First reference to the service class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through the start-service site', evidence='INFERRED class-init rule; SRC Utils.java:426-434; SRC service/TorrentService.java:68-76')
e('TorrentService.stopEngine', 'TorrentService.forceClearForeground', 'CALL', 'Engine stop clears the foreground notification', cls='explicit', evidence='SRC service/TorrentService.java:160')
e('TorrentService.lambda$subscribeForceSortAndFilter$5', 'TorrentService.getInfoListSingle', 'CALL', 'Force-sort-and-filter subscription reloads the info list', cls='explicit', evidence='SRC service/TorrentService.java:318')
e('TorrentService.init', 'TorrentService.handleSettingsChanged', 'CALL', 'Settings-change subscription dispatches to the settings handler', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:125-126')
e('TorrentService.forceClearForeground', 'TorrentService.lambda$forceClearForeground$7', 'CALL', 'Clear-foreground completable runs its empty-notify runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:331')
e('TorrentService.getInfoListSingle', 'TorrentService.lambda$getInfoListSingle$2', 'CALL', 'Info-list single runs its flatMap filter-and-sort stage', cls='non_standard', via='Rx flatMap dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:301-306')
e('TorrentService.getInfoListSingle', 'TorrentService.lambda$getInfoListSingle$3', 'CALL', 'Info-list single runs its error-logging subscriber on error', cls='non_standard', via='Rx subscribe error dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:309-311')
e('TorrentService.startUpdateForegroundNotify', 'TorrentService.lambda$startUpdateForegroundNotify$0', 'CALL', 'Foreground-notify update runs its flatMapSingle filter-and-sort stage', cls='non_standard', via='Rx flatMapSingle dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:284-289')
e('TorrentService.startUpdateForegroundNotify', 'TorrentService.lambda$startUpdateForegroundNotify$1', 'CALL', 'Foreground-notify update runs its error-logging subscriber on error', cls='non_standard', via='Rx subscribe error dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:293-295')
e('TorrentService.subscribeCombinedPauseButtonState', 'TorrentService.lambda$subscribeCombinedPauseButtonState$6', 'CALL', 'Combined-pause-button subscription runs its actions-update consumer', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:324-326')
e('TorrentService.subscribeForceSortAndFilter', 'TorrentService.lambda$subscribeForceSortAndFilter$4', 'CALL', 'Force-sort-and-filter stream runs its force filter', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:316')
e('TorrentService.subscribeForceSortAndFilter', 'TorrentService.lambda$subscribeForceSortAndFilter$5', 'CALL', 'Force-sort-and-filter stream runs its reload subscriber', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:318')
e('TorrentService.updateForegroundNotify', 'TorrentService.makeDetailNotifyInboxStyle', 'CALL', 'Foreground-notify update builds the inbox style for the torrent list', cls='explicit', evidence='SRC service/TorrentService.java:392')
e('TorrentService.stopService', 'TorrentService.onDestroy', 'CALL', 'Service stop ends with stopSelf, after which the framework destroys the service', cls='non_standard', via='framework lifecycle after stopSelf', evidence='INFERRED framework lifecycle; SRC service/TorrentService.java:172')
e('TorrentService.init', 'TorrentService.setFilterAndSorting', 'CALL', 'Service init sets the foreground-notify filter and sorting', cls='explicit', evidence='SRC service/TorrentService.java:122')
e('TorrentService.makeForegroundNotify', 'TorrentService.setForegroundNotifyActions', 'CALL', 'Foreground notification build sets its action buttons', cls='explicit', evidence='SRC service/TorrentService.java:361')
e('TorrentService.init', 'TorrentService.setKeepCpuAwake', 'CALL', 'Service init applies the cpu-do-not-sleep setting', cls='explicit', evidence='SRC service/TorrentService.java:129')
e('TorrentService.handleShutdownActions', 'TorrentService.shutdown', 'CALL', 'Shutdown action runs the service shutdown', cls='explicit', evidence='SRC service/TorrentService.java:204')
e('TorrentService.init', 'TorrentService.startUpdateForegroundNotify', 'CALL', 'Service init starts the foreground-notify updater', cls='explicit', evidence='SRC service/TorrentService.java:134')
e('TorrentService.shutdown', 'TorrentService.stopEngine', 'CALL', 'Shutdown completable runs the engine stop', cls='non_standard', via='Rx Completable method-reference dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:152')
e('TorrentService$1.onSessionStopped', 'TorrentService.stopService', 'CALL', 'Session-stopped listener stops the service', cls='explicit', evidence='SRC service/TorrentService.java:260')
e('TorrentService.updateForegroundNotify', 'TorrentService.stopUpdateForegroundNotify', 'CALL', 'Shutdown branch of the notify update stops the updater', cls='explicit', evidence='SRC service/TorrentService.java:377')
e('TorrentService.init', 'TorrentService.subscribeCombinedPauseButtonState', 'CALL', 'Service init subscribes the combined pause-button state', cls='explicit', evidence='SRC service/TorrentService.java:121')
e('TorrentService.init', 'TorrentService.subscribeForceSortAndFilter', 'CALL', 'Service init subscribes the force-sort-and-filter stream', cls='explicit', evidence='SRC service/TorrentService.java:123')
e('TorrentService.startUpdateForegroundNotify', 'TorrentService.updateForegroundNotify', 'CALL', 'Foreground-notify update subscribes the notify renderer', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:292')
e('TorrentService.getInfoListSingle', 'TorrentService.updateForegroundNotify', 'CALL', 'Info-list single subscribes the notify renderer', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:308')
e('TorrentService.lambda$forceClearForeground$7', 'TorrentService.updateForegroundNotify', 'CALL', 'Clear-foreground runnable renders the empty notify state', cls='explicit', evidence='SRC service/TorrentService.java:331')
e('TorrentService.lambda$subscribeCombinedPauseButtonState$6', 'TorrentService.updateForegroundNotifyActions', 'CALL', 'Pause-button state change updates the notify actions', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:324-326')
e('TorrentService.handleSettingsChanged', 'TorrentService.updateForegroundNotifyActions', 'CALL', 'Combined-pause-button setting change updates the notify actions', cls='explicit', evidence='SRC service/TorrentService.java:273')
e('TorrentService.<init>', 'TorrentService$1.<init>', 'CALL', 'Service field initialiser constructs the engine listener', cls='explicit', evidence='SRC service/TorrentService.java:255')
e('TorrentService.init', 'TorrentService$1.onSessionStopped', 'CALL', 'Registered engine listener delivers the session-stopped event', cls='non_standard', via='engine session dispatch', evidence='INFERRED session dispatch; SRC service/TorrentService.java:132')
e('MainFragment.deleteTorrentsDialog', 'BaseAlertDialog.<clinit>', 'CALL', 'First reference to the dialog class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through newInstance', evidence='INFERRED class-init rule; SRC ui/main/MainFragment.java:508')
e('BaseAlertDialog.newInstance', 'BaseAlertDialog.<init>', 'CALL', 'Dialog factory constructs the dialog fragment', cls='explicit', evidence='SRC ui/BaseAlertDialog.java:98')

# UNREACHABLE rows in this batch (batch labels kept, not flipped).
UNREACHABLE.update({
    'TorrentService.onBind': ('no_trigger_in_app',
        'No bindService site for TorrentService in the whole app tree; framework calls onBind only for a bound service, and this service is started, not bound; manifest declares it with no exported flag and no intent filter. Body returns null.',
        'INFERRED saved full-tree grep over all 252 app Java files finds zero bindService / unbindService / ServiceConnection hits; manifest declares TorrentService with no exported flag and no intent filter, so no external binder can bind it; onBind body returns null (SRC service/TorrentService.java:100-103)',
        'INFERRED'),
})

# SUPPRESS: recomputed from auto_calls.json + javap scan for this batch's
# rows; the recomputation and any cross-group candidates are recorded in
# REPORT.md. No intra-group pair was found, so no entries apply here.
SUPPRESS.update(set())
