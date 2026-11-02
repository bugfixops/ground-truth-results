# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys, so no grade change.
# Batch 40 part (TorrentSessionImpl lifecycle callbacks, torrent
# management and settings setters). Hand-written edges and one
# UNREACHABLE entry only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b040_printed.txt. Source paths below are
# relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Dependencies: none; every REACHABLE row below has an edge here.

e('TorrentSessionImpl.start', 'TorrentSessionImpl.loadSettings', 'CALL', 'Session start loads the saved settings', cls='explicit', evidence='SRC TorrentSessionImpl.java:867; SRC TorrentSessionImpl.java:1192')
e('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.mergeTorrent', 'CALL', 'Add torrent merges an existing torrent when the id is known', cls='explicit', evidence='SRC TorrentSessionImpl.java:281; SRC TorrentSessionImpl.java:537')
e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl.newTask', 'CALL', 'Inner listener ADD_TORRENT case creates the download task', cls='explicit', evidence='SRC TorrentSessionImpl.java:1081; SRC TorrentSessionImpl.java:1430')
e('TorrentSessionImpl.deleteTorrent', 'TorrentSessionImpl.notifyListeners', 'CALL', 'Delete torrent notifies listeners of the removal', cls='explicit', evidence='SRC TorrentSessionImpl.java:388; SRC TorrentSessionImpl.java:1445')
e('TorrentSessionImpl.start', 'TorrentSessionImpl.onAfterStart', 'FRAMEWORK', 'Library session start dispatches to the onAfterStart callback', cls='non_standard', via='libtorrent4j SessionManager lifecycle callback', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:907; SRC TorrentSessionImpl.java:991-1013')
e('TorrentSessionImpl.checkStop', 'TorrentSessionImpl.onAfterStop', 'FRAMEWORK', 'Library session stop dispatches to the onAfterStop callback', cls='non_standard', via='libtorrent4j SessionManager lifecycle callback', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:947; SRC TorrentSessionImpl.java:1041-1045')
e('TorrentSessionImpl.applySettingsPack', 'TorrentSessionImpl.onApplySettings', 'FRAMEWORK', 'Library settings application dispatches to the onApplySettings callback', cls='non_standard', via='libtorrent4j SessionManager lifecycle callback', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:1381; SRC TorrentSessionImpl.java:1048-1051')
e('TorrentSessionImpl.start', 'TorrentSessionImpl.onBeforeStart', 'FRAMEWORK', 'Library session start dispatches to the onBeforeStart callback', cls='non_standard', via='libtorrent4j SessionManager lifecycle callback', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:907; SRC TorrentSessionImpl.java:984-988')
e('TorrentSessionImpl.checkStop', 'TorrentSessionImpl.onBeforeStop', 'FRAMEWORK', 'Library session stop dispatches to the onBeforeStop callback', cls='non_standard', via='libtorrent4j SessionManager lifecycle callback', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:947; SRC TorrentSessionImpl.java:1028-1038')
e('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.operationNotAllowed', 'CALL', 'Add torrent guards on the session state', cls='explicit', evidence='SRC TorrentSessionImpl.java:260; SRC TorrentSessionImpl.java:245')
e('TorrentEngine.parseMagnet', 'TorrentSessionImpl.parseMagnet', 'CALL', 'Engine magnet parsing reads the magnet info through the session', cls='explicit', evidence='SRC TorrentEngine.java:428; SRC TorrentSessionImpl.java:444')
e('TorrentSessionImpl.fetchMagnet(String)', 'TorrentSessionImpl.parseMagnetUri', 'CALL', 'String magnet fetch parses the magnet URI', cls='explicit', evidence='SRC TorrentSessionImpl.java:432; SRC TorrentSessionImpl.java:514')
e('TorrentEngine.lambda$rescheduleTorrents$7', 'TorrentSessionImpl.pauseAll', 'CALL', 'Reschedule runnable pauses all torrents through the session', cls='explicit', evidence='SRC TorrentEngine.java:321; SRC TorrentSessionImpl.java:756')
e('TorrentEngine.lambda$pauseAll$19', 'TorrentSessionImpl.pauseAllManually', 'CALL', 'Pause-all runnable pauses all torrents manually through the session', cls='explicit', evidence='SRC TorrentEngine.java:655; SRC TorrentSessionImpl.java:782')
e('TorrentEngine.removeListener', 'TorrentSessionImpl.removeListener', 'CALL', 'Engine listener removal removes the session listener', cls='explicit', evidence='SRC TorrentEngine.java:312; SRC TorrentSessionImpl.java:191')
e('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.removeLoadedMagnet', 'CALL', 'Add torrent drops the loaded magnet for the new torrent', cls='explicit', evidence='SRC TorrentSessionImpl.java:275; SRC TorrentSessionImpl.java:240')
e('TorrentEngine.doStop', 'TorrentSessionImpl.requestStop', 'CALL', 'Engine stop requests the session to stop', cls='explicit', evidence='SRC TorrentEngine.java:299; SRC TorrentSessionImpl.java:911')
e('TorrentSessionImpl$LoadTorrentTask.run', 'TorrentSessionImpl.restoreDownload', 'CALL', 'Load task restores a non-magnet torrent from its download', cls='explicit', evidence='SRC TorrentSessionImpl.java:1517; SRC TorrentSessionImpl.java:1681')
e('TorrentEngine.lambda$loadTorrents$26', 'TorrentSessionImpl.restoreTorrents', 'CALL', 'Load-torrents runnable restores the saved torrents through the session', cls='explicit', evidence='SRC TorrentEngine.java:1088; SRC TorrentSessionImpl.java:396')
e('TorrentEngine.lambda$rescheduleTorrents$7', 'TorrentSessionImpl.resumeAll', 'CALL', 'Reschedule runnable resumes all torrents through the session', cls='explicit', evidence='SRC TorrentEngine.java:323; SRC TorrentSessionImpl.java:769')
e('TorrentEngine.lambda$resumeAll$20', 'TorrentSessionImpl.resumeAllManually', 'CALL', 'Resume-all runnable resumes all torrents manually through the session', cls='explicit', evidence='SRC TorrentEngine.java:664; SRC TorrentSessionImpl.java:795')
e('TorrentSessionImpl.restoreTorrents', 'TorrentSessionImpl.runNextLoadTorrentTask', 'CALL', 'Restore torrents runs the next queued load task', cls='explicit', evidence='SRC TorrentSessionImpl.java:423; SRC TorrentSessionImpl.java:1453')
e('TorrentSessionImpl.requestStop', 'TorrentSessionImpl.saveAllResumeData', 'CALL', 'Stop request saves resume data for all torrents', cls='explicit', evidence='SRC TorrentSessionImpl.java:916; SRC TorrentSessionImpl.java:950')
e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.saveSettings', 'CALL', 'Session start saves the settings', cls='explicit', evidence='SRC TorrentSessionImpl.java:1007; SRC TorrentSessionImpl.java:1228')
e('TorrentEngine.handleSettingsChanged', 'TorrentSessionImpl.setAutoManaged', 'CALL', 'Preference-change handling sets the auto-managed flag', cls='explicit', evidence='SRC TorrentEngine.java:1579; SRC TorrentSessionImpl.java:836')
e('TorrentEngine.handleSettingsChanged', 'TorrentSessionImpl.setDefaultTrackersList', 'CALL', 'Preference-change handling sets the default trackers list', cls='explicit', evidence='SRC TorrentEngine.java:1648; SRC TorrentSessionImpl.java:1677')
e('TorrentEngine.handleSettingsChanged', 'TorrentSessionImpl.setMaxConnectionsPerTorrent', 'CALL', 'Preference-change handling sets the max connections per torrent', cls='explicit', evidence='SRC TorrentEngine.java:1490; SRC TorrentSessionImpl.java:808')
e('TorrentEngine.handleSettingsChanged', 'TorrentSessionImpl.setMaxUploadsPerTorrent', 'CALL', 'Preference-change handling sets the max uploads per torrent', cls='explicit', evidence='SRC TorrentEngine.java:1493; SRC TorrentSessionImpl.java:822')
e('TorrentSessionImpl.start', 'TorrentSessionImpl.setRandomPort', 'CALL', 'Session start picks a random port when configured', cls='explicit', evidence='SRC TorrentSessionImpl.java:903; SRC TorrentSessionImpl.java:1402')
e('TorrentEngine.setProxy', 'TorrentSessionImpl.setSettings(SessionSettings)', 'CALL', 'Engine proxy setup sets the session settings', cls='explicit', evidence='SRC TorrentEngine.java:1105; SRC TorrentSessionImpl.java:202')
e('TorrentEngine.<init>', 'TorrentSessionImpl.setSettings(SessionSettings,boolean)', 'CALL', 'Engine constructor sets the session settings from preferences', cls='explicit', evidence='SRC TorrentEngine.java:139; SRC TorrentSessionImpl.java:207')
e('TorrentSessionImpl.start', 'TorrentSessionImpl.settingsToSettingsPack', 'CALL', 'Session start converts the settings into a settings pack', cls='explicit', evidence='SRC TorrentSessionImpl.java:905; SRC TorrentSessionImpl.java:1250')
e('TorrentEngine.doStart', 'TorrentSessionImpl.start', 'CALL', 'Engine start starts the session', cls='explicit', evidence='SRC TorrentEngine.java:259; SRC TorrentSessionImpl.java:862')
e('TorrentSessionImpl.requestStop', 'TorrentSessionImpl.stopTasks', 'CALL', 'Stop request stops the running tasks', cls='explicit', evidence='SRC TorrentSessionImpl.java:917; SRC TorrentSessionImpl.java:920')
e('TorrentSessionImpl.<init>', 'TorrentSessionImpl$1.<init>', 'CALL', 'Session constructor runs the anonymous task-listener field initialiser', cls='explicit', evidence='SRC TorrentSessionImpl.java:1053-1059; SRC TorrentSessionImpl.java:162')
e('TorrentSessionImpl.lambda$deleteTorrent$0', 'TorrentSessionImpl$1.onTorrentRemoved', 'CALL', 'Delete-torrent notify lambda tells the task listener a torrent was removed', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:389; SRC TorrentSessionImpl.java:1053-1059')
e('TorrentSessionImpl.<init>', 'TorrentSessionImpl$InnerListener.<init>', 'CALL', 'Session constructor creates its inner alert listener', cls='explicit', evidence='SRC TorrentSessionImpl.java:174; SRC TorrentSessionImpl.java:1061')
e('TorrentSessionImpl.onBeforeStart', 'TorrentSessionImpl$InnerListener.alert', 'FRAMEWORK', 'Library alert dispatch to the inner listener registered on session start', cls='non_standard', via='libtorrent alert dispatch to a registered AlertListener', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:987; SRC TorrentSessionImpl.java:1070-1107')
e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl$InnerListener.lambda$alert$0', 'CALL', 'ADD_TORRENT case notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1083-1084')

UNREACHABLE.update({
    'TorrentSessionImpl.mergeTrackersAndSeeds': ('branch_never_taken',
        'Sole printed call is inside mergeTorrent under if (false) (TODO temporary disable); private method, no other caller.',
        'SRC TorrentSessionImpl.java:553-556; SRC TorrentSessionImpl.java:570-588',
        'INFERRED'),
})

# This batch's single UNREACHABLE method has no bytecode incoming
# edge: its only source call site sits under if (false), which javac
# eliminates, so auto_calls.json records no caller for it. Hence no
# SUPPRESS entry applies.
SUPPRESS.update(set())
