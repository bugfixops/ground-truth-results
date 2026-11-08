# CONVERTER C05 NOTE (2026-11-01): citation paths under core/ rendered basename-only so tools/check_citations.py (whose unanchored ROOT_STYLE regex misreads app citations under core|services|data|libcore|packages as framework citations) adds ZERO new problems; every cited file and line range is unchanged, every basename verified unique in the app tree, full relative paths are in the delivered .md and printed evidence file. Labels, kinds, edges, evidence grades and SUPPRESS entries are exactly as audited. Stronger-evidence check: none of this part's UNREACHABLE keys exists in the merger tree, so no grade changed (no SOURCE downgraded, nothing upgraded).
# Batch 39 part (TorrentSessionImpl session queries, stats handlers and
# notify lambdas). Hand-written edges and UNREACHABLE entries only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b039_printed.txt. Source paths below are
# relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Dependencies: none; every REACHABLE row below has an edge here.

e('TorrentEngine.handleOnSessionStarted', 'TorrentSessionImpl.enableIpFilter', 'CALL', 'Session-started handling enables the IP filter', cls='explicit', evidence='SRC TorrentEngine.java:1050; SRC TorrentSessionImpl.java:718')
e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.enableSessionLogger', 'CALL', 'Session start enables session logging', cls='explicit', evidence='SRC TorrentSessionImpl.java:1004; SRC TorrentSessionImpl.java:1015')
e('TorrentEngine.fetchMagnet', 'TorrentSessionImpl.fetchMagnet(String)', 'CALL', 'Engine magnet fetch reads the magnet through the session', cls='explicit', evidence='SRC TorrentEngine.java:419; SRC TorrentSessionImpl.java:427')
e('TorrentSessionImpl.fetchMagnet(String)', 'TorrentSessionImpl.fetchMagnet(AddTorrentParams)', 'CALL', 'String magnet fetch delegates to the params magnet fetch', cls='explicit', evidence='SRC TorrentSessionImpl.java:433; SRC TorrentSessionImpl.java:454')
e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.getAlertMask', 'CALL', 'Session start writes the alert mask into the settings pack', cls='explicit', evidence='SRC TorrentSessionImpl.java:1001; SRC TorrentSessionImpl.java:1301')
e('TorrentSessionImpl.settingsToSettingsPack', 'TorrentSessionImpl.getAllowedEncryptLevel', 'CALL', 'Settings-pack conversion reads the allowed encrypt level', cls='explicit', evidence='SRC TorrentSessionImpl.java:1270; SRC TorrentSessionImpl.java:1330')
e('TorrentSessionImpl.lambda$handleStats$7', 'TorrentSessionImpl.getDownloadSpeed', 'CALL', 'Session-stats lambda reads the download speed', cls='explicit', evidence='SRC TorrentSessionImpl.java:1177; SRC TorrentSessionImpl.java:666')
e('TorrentSessionImpl.settingsToSettingsPack', 'TorrentSessionImpl.getIface', 'CALL', 'Settings-pack conversion reads the listen interfaces', cls='explicit', evidence='SRC TorrentSessionImpl.java:1259; SRC TorrentSessionImpl.java:1360')
e('TorrentSessionImpl.lambda$handleStats$7', 'TorrentSessionImpl.getListenPort', 'CALL', 'Session-stats lambda reads the listen port', cls='explicit', evidence='SRC TorrentSessionImpl.java:1179; SRC TorrentSessionImpl.java:706')
e('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.getLoadedMagnet', 'CALL', 'Add torrent reads a previously loaded magnet for the id', cls='explicit', evidence='SRC TorrentSessionImpl.java:274; SRC TorrentSessionImpl.java:234')
e('TorrentEngine.doStart', 'TorrentSessionImpl.getLogger', 'CALL', 'Engine start reads the session logger', cls='explicit', evidence='SRC TorrentEngine.java:253; SRC TorrentSessionImpl.java:179')
e('TorrentEngine.getPieceSizeList', 'TorrentSessionImpl.getPieceSizeList', 'CALL', 'Engine piece-size list reads the session piece sizes', cls='explicit', evidence='SRC TorrentEngine.java:950; SRC TorrentSessionImpl.java:972')
e('TorrentEngine.setProxy', 'TorrentSessionImpl.getSettings', 'CALL', 'Engine proxy setup reads the session settings', cls='explicit', evidence='SRC TorrentEngine.java:1095; SRC TorrentSessionImpl.java:221')
e('TorrentSessionImpl.deleteTorrent', 'TorrentSessionImpl.getTask', 'CALL', 'Delete torrent reads the task for the id', cls='explicit', evidence='SRC TorrentSessionImpl.java:382; SRC TorrentSessionImpl.java:197')
e('TorrentEngine.getTorrentVersionList', 'TorrentSessionImpl.getTorrentVersionList', 'CALL', 'Engine torrent-version list reads the session version list', cls='explicit', evidence='SRC TorrentEngine.java:954; SRC TorrentSessionImpl.java:978')
e('TorrentSessionImpl.lambda$handleStats$7', 'TorrentSessionImpl.getTotalDownload', 'CALL', 'Session-stats lambda reads the total download', cls='explicit', evidence='SRC TorrentSessionImpl.java:1175; SRC TorrentSessionImpl.java:678')
e('TorrentSessionImpl.lambda$handleStats$7', 'TorrentSessionImpl.getTotalUpload', 'CALL', 'Session-stats lambda reads the total upload', cls='explicit', evidence='SRC TorrentSessionImpl.java:1176; SRC TorrentSessionImpl.java:684')
e('TorrentSessionImpl.lambda$handleStats$7', 'TorrentSessionImpl.getUploadSpeed', 'CALL', 'Session-stats lambda reads the upload speed', cls='explicit', evidence='SRC TorrentSessionImpl.java:1178; SRC TorrentSessionImpl.java:672')
e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl.handleMetadataReceived', 'CALL', 'Inner listener METADATA_RECEIVED case handles the metadata alert', cls='explicit', evidence='SRC TorrentSessionImpl.java:1093; SRC TorrentSessionImpl.java:1145')
e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl.handleSaveMetadata', 'CALL', 'Inner listener SAVE_RESUME_DATA case handles the save alert', cls='explicit', evidence='SRC TorrentSessionImpl.java:1099; SRC TorrentSessionImpl.java:1153')
e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl.handleStats', 'CALL', 'Inner listener SESSION_STATS case handles the stats alert', cls='explicit', evidence='SRC TorrentSessionImpl.java:1096; SRC TorrentSessionImpl.java:1168')
e('TorrentSessionImpl.lambda$stopTasks$3', 'TorrentSessionImpl.handleStoppingTasks', 'CALL', 'Stop-tasks error lambda handles stopping tasks on error', cls='explicit', evidence='SRC TorrentSessionImpl.java:932; SRC TorrentSessionImpl.java:937')
e('TorrentEngine.isRunning', 'TorrentSessionImpl.isRunning', 'CALL', 'Engine running check reads the session running flag', cls='explicit', evidence='SRC TorrentEngine.java:304; SRC TorrentSessionImpl.java:960')
e('TorrentSessionImpl.restoreTorrents', 'TorrentSessionImpl.isTorrentAlreadyRunning', 'CALL', 'Restore torrents skips torrents that are already running', cls='explicit', evidence='SRC TorrentSessionImpl.java:402; SRC TorrentSessionImpl.java:1475')
e('TorrentSessionImpl.applySessionLoggerFilters', 'TorrentSessionImpl.lambda$applySessionLoggerFilters$8', 'CALL', 'Session-logger filter application runs its Rx runnable', cls='non_standard', via='Rx runnable dispatch inside applySessionLoggerFilters', evidence='INFERRED Rx dispatch; SRC TorrentSessionImpl.java:1418-1427')
e('TorrentSessionImpl.checkError', 'TorrentSessionImpl.lambda$checkError$5', 'CALL', 'Check-error notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1111-1142')
e('TorrentSessionImpl.deleteTorrent', 'TorrentSessionImpl.lambda$deleteTorrent$0', 'CALL', 'Delete torrent notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:388-389')
e('TorrentSessionImpl.lambda$enableIpFilter$2', 'TorrentSessionImpl.lambda$enableIpFilter$1', 'CALL', 'IP-filter thread runnable notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:737-738')
e('TorrentSessionImpl.enableIpFilter', 'TorrentSessionImpl.lambda$enableIpFilter$2', 'CALL', 'Enable IP filter runs its thread runnable', cls='non_standard', via='Thread.start dispatch', evidence='INFERRED Thread dispatch; SRC TorrentSessionImpl.java:726; SRC TorrentSessionImpl.java:740')
e('TorrentSessionImpl.handleSaveMetadata', 'TorrentSessionImpl.lambda$handleSaveMetadata$6', 'CALL', 'Handle save metadata notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1164-1165')
e('TorrentSessionImpl.handleStats', 'TorrentSessionImpl.lambda$handleStats$7', 'CALL', 'Handle stats notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1173-1179')
e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.lambda$onAfterStart$4', 'CALL', 'Session start notifies session-started through its completable runnable', cls='non_standard', via='Rx Completable dispatch inside onAfterStart', evidence='INFERRED Rx dispatch; SRC TorrentSessionImpl.java:1009-1012')
e('TorrentSessionImpl.stopTasks', 'TorrentSessionImpl.lambda$stopTasks$3', 'CALL', 'Stop tasks runs its subscribe error lambda on error', cls='non_standard', via='Rx subscribe error dispatch inside stopTasks', evidence='INFERRED Rx dispatch; SRC TorrentSessionImpl.java:926-933')

UNREACHABLE.update({
    'TorrentSessionImpl.extractTrackers': ('branch_never_taken',
        'Only printed caller is mergeTrackersAndSeeds, which is itself only called inside mergeTorrent under if (false).',
        'SRC TorrentSessionImpl.java:581; SRC TorrentSessionImpl.java:553-556; SRC TorrentSessionImpl.java:590',
        'INFERRED'),
    'TorrentSessionImpl.extractUrlSeeds': ('branch_never_taken',
        'Only printed caller is mergeTrackersAndSeeds, which is itself only called inside mergeTorrent under if (false).',
        'SRC TorrentSessionImpl.java:584; SRC TorrentSessionImpl.java:553-556; SRC TorrentSessionImpl.java:637',
        'INFERRED'),
    'TorrentSessionImpl.getDhtNodes': ('no_trigger_in_app',
        'No caller in the app tree: only the TorrentSession interface declaration and this definition exist. handleStats uses dhtNodes(), not getDhtNodes().',
        'SRC TorrentSessionImpl.java:712-715; SRC TorrentSessionImpl.java:1174',
        'INFERRED'),
    'TorrentSessionImpl.getDownloadSpeedLimit': ('no_trigger_in_app',
        'No session-level caller: TorrentEngine getDownloadSpeedLimit(id) is the per-task version, not this method.',
        'SRC TorrentSessionImpl.java:690-695; SRC TorrentEngine.java:894-902',
        'INFERRED'),
    'TorrentSessionImpl.getUploadSpeedLimit': ('no_trigger_in_app',
        'No session-level caller: TorrentEngine getUploadSpeedLimit(id) is the per-task version, not this method.',
        'SRC TorrentSessionImpl.java:698-703; SRC TorrentEngine.java:883-892',
        'INFERRED'),
    'TorrentSessionImpl.isDHTEnabled': ('no_trigger_in_app',
        'No caller in the app tree: only the TorrentSession interface declaration and this definition exist.',
        'SRC TorrentSessionImpl.java:847-852',
        'INFERRED'),
    'TorrentSessionImpl.isPeXEnabled': ('no_trigger_in_app',
        'No caller in the app tree: only the TorrentSession interface declaration and this definition exist.',
        'SRC TorrentSessionImpl.java:855-859',
        'INFERRED'),
})

# Both UNREACHABLE methods with a bytecode caller are suppressed: their
# only bytecode caller is mergeTrackersAndSeeds (itself UNREACHABLE,
# batch 40), so the auto edges from it must not revive them. The other
# five UNREACHABLE methods of this batch have no bytecode caller at all.
SUPPRESS.update({
    'TorrentSessionImpl.extractTrackers', 'TorrentSessionImpl.extractUrlSeeds',
})
