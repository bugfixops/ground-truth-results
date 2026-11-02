# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys, so no grade change. Merger note (NOT applied here): the merger dedupes batch-74 REACHABLE PermissionManager callers against this part's SUPPRESS callees at the b074 merge; this part keeps its SUPPRESS as audited.
# Batch 42 part (TorrentStream creator tail; TorrentStreamServer;
# SessionSettings and enums; SettingsRepositoryImpl settings head).
# Hand-written edges and UNREACHABLE entries only. Each evidence
# string cites lines printed in
# graphs/LibreTorrent/scratch/b042_printed.txt. Source paths below are
# relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Dependencies: none; every REACHABLE row below has an edge here.

e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.<clinit>', 'CALL', 'First streaming-server start runs the server class initialisation', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentEngine.java:1069; SRC TorrentStreamServer.java:58-63')
e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.<init>', 'CALL', 'Streaming-server start constructs the torrent stream server', cls='explicit', evidence='SRC TorrentEngine.java:1069; SRC TorrentStreamServer.java:67')
e('TorrentStreamServer.serve', 'TorrentStreamServer.handleTorrent', 'CALL', 'Serve dispatches stream requests to the torrent handler', cls='explicit', evidence='SRC TorrentStreamServer.java:117; SRC TorrentStreamServer.java:124')
e('DetailTorrentViewModel.getStreamUrl', 'TorrentStreamServer.makeStreamUrl', 'CALL', 'Detail stream URL builds the stream URL through the server', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:342; SRC TorrentStreamServer.java:93')
e('NanoHTTPD$HTTPSession.execute', 'TorrentStreamServer.serve', 'CALL', 'HTTP session execution dispatches to the server serve override', cls='non_standard', via='NanoHTTPD virtual serve dispatch', evidence='INFERRED library dispatch; SRC org/nanohttpd/NanoHTTPD.java:720; SRC TorrentStreamServer.java:111')
e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.start', 'CALL', 'Streaming-server start starts the torrent stream server', cls='explicit', evidence='SRC TorrentEngine.java:1071; SRC TorrentStreamServer.java:72')
e('TorrentEngine.stopStreamingServer', 'TorrentStreamServer.stop', 'CALL', 'Streaming-server stop stops the torrent stream server', cls='explicit', evidence='SRC TorrentEngine.java:1081; SRC TorrentStreamServer.java:82')
e('TorrentStreamServer.<clinit>', 'TorrentStreamServer$DLNAFileType.<init>', 'CALL', 'Server class initialisation creates the DLNA file types', cls='explicit', evidence='SRC TorrentStreamServer.java:60-62; SRC TorrentStreamServer.java:267')
e('TorrentStreamServer.serve', 'TorrentStreamServer$DLNAFileType.setHeaders', 'CALL', 'Serve sets the DLNA headers for a known file type', cls='explicit', evidence='SRC TorrentStreamServer.java:119; SRC TorrentStreamServer.java:275')
e('TorrentSessionImpl.<init>', 'SessionSettings.<clinit>', 'CALL', 'First session construction runs the settings class initialisation', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentSessionImpl.java:143; SRC SessionSettings.java:50')
e('TorrentSessionImpl.<init>', 'SessionSettings.<init>()', 'CALL', 'Session constructor field initialiser creates the default settings', cls='explicit', evidence='SRC TorrentSessionImpl.java:143; SRC SessionSettings.java:118')
e('TorrentSessionImpl.getSettings', 'SessionSettings.<init>(SessionSettings)', 'CALL', 'Session settings getter copies the settings', cls='explicit', evidence='SRC TorrentSessionImpl.java:226; SRC SessionSettings.java:120')
e('TorrentSessionImpl.setRandomPort', 'SessionSettings.getRandomRangePort', 'CALL', 'Random-port setup reads the random port range', cls='explicit', evidence='SRC TorrentSessionImpl.java:1403; SRC SessionSettings.java:234')
e('SessionSettings.<clinit>', 'SessionSettings$EncryptMode.<clinit>', 'CALL', 'Settings initialisation loads the encrypt-mode enum', cls='non_standard', via='JVM enum initialisation on first use', evidence='INFERRED JVM dispatch; SRC SessionSettings.java:50; SRC SessionSettings.java:168-172')
e('SessionSettings$EncryptMode.<clinit>', 'SessionSettings$EncryptMode.<init>', 'CALL', 'Enum initialisation constructs each encrypt-mode constant', cls='non_standard', via='JVM enum constant construction during <clinit>', evidence='INFERRED JVM dispatch; SRC SessionSettings.java:168-172; SRC SessionSettings.java:174-177')
e('TorrentEngine.getEncryptInConnectionsMode', 'SessionSettings$EncryptMode.fromValue', 'CALL', 'Engine encrypt-in mode reads the enum value', cls='explicit', evidence='SRC TorrentEngine.java:1109; SRC SessionSettings.java:186')
e('SessionSettings$EncryptMode.fromValue', 'SessionSettings$EncryptMode.value', 'CALL', 'Enum lookup reads each constant value', cls='explicit', evidence='SRC SessionSettings.java:190; SRC SessionSettings.java:181')
e('SessionSettings.<clinit>', 'SessionSettings$ProxyType.<clinit>', 'CALL', 'Settings initialisation loads the proxy-type enum', cls='non_standard', via='JVM enum initialisation on first use', evidence='INFERRED JVM dispatch; SRC SessionSettings.java:55; SRC SessionSettings.java:199-202')
e('SessionSettings$ProxyType.<clinit>', 'SessionSettings$ProxyType.<init>', 'CALL', 'Enum initialisation constructs each proxy-type constant', cls='non_standard', via='JVM enum constant construction during <clinit>', evidence='INFERRED JVM dispatch; SRC SessionSettings.java:199-202; SRC SessionSettings.java:206-209')
e('TorrentEngine.setProxy', 'SessionSettings$ProxyType.fromValue', 'CALL', 'Engine proxy setup reads the proxy type enum value', cls='explicit', evidence='SRC TorrentEngine.java:1097; SRC SessionSettings.java:211')
e('SessionSettings$ProxyType.fromValue', 'SessionSettings$ProxyType.value', 'CALL', 'Enum lookup reads each constant value', cls='explicit', evidence='SRC SessionSettings.java:215; SRC SessionSettings.java:223')
e('RepositoryHelper.getSettingsRepository', 'SettingsRepositoryImpl.<init>', 'CALL', 'Settings repository getter constructs the repository on first use', cls='explicit', evidence='SRC RepositoryHelper.java:61-64; SRC SettingsRepositoryImpl.java:184')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.anonymousMode()', 'CALL', 'Settings conversion reads the anonymous-mode preference', cls='explicit', evidence='SRC TorrentEngine.java:1604; SRC SettingsRepositoryImpl.java:929')
e('AnonymousModeSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.anonymousMode(boolean)', 'CALL', 'Anonymous-mode preference change writes the preference', cls='explicit', evidence='SRC ui/settings/sections/AnonymousModeSettingsFragment.java:79; SRC SettingsRepositoryImpl.java:935')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.applyProxy()', 'CALL', 'Preference-change handling reads the apply-proxy flag', cls='explicit', evidence='SRC TorrentEngine.java:1569; SRC SettingsRepositoryImpl.java:1085')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.applyProxy(boolean)', 'CALL', 'Preference-change handling clears the apply-proxy flag', cls='explicit', evidence='SRC TorrentEngine.java:1570; SRC SettingsRepositoryImpl.java:1091')
e('LimitationsSettingsFragment.onCreate', 'SettingsRepositoryImpl.autoManage()', 'CALL', 'Limitations settings bind reads the auto-manage preference', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:108; SRC SettingsRepositoryImpl.java:981')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autoManage(boolean)', 'CALL', 'Limitations preference change writes the auto-manage preference', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:241; SRC SettingsRepositoryImpl.java:987')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.autoRefreshFeeds()', 'CALL', 'Feed settings bind reads the auto-refresh preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:60; SRC SettingsRepositoryImpl.java:1189')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autoRefreshFeeds(boolean)', 'CALL', 'Feed preference change writes the auto-refresh preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:130; SRC SettingsRepositoryImpl.java:1195')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming()', 'CALL', 'Feed settings bind reads the roaming preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:84; SRC SettingsRepositoryImpl.java:1228')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming(boolean)', 'CALL', 'Feed preference change writes the roaming preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:152; SRC SettingsRepositoryImpl.java:1234')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly()', 'CALL', 'Feed settings bind reads the unmetered-only preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:77; SRC SettingsRepositoryImpl.java:1215')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly(boolean)', 'CALL', 'Feed preference change writes the unmetered-only preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:149; SRC SettingsRepositoryImpl.java:1221')
e('BehaviorSettingsFragment.onCreate', 'SettingsRepositoryImpl.autostart()', 'CALL', 'Behavior settings bind reads the autostart preference', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:74; SRC SettingsRepositoryImpl.java:409')
e('PermissionManager.lambda$new$1', 'SettingsRepositoryImpl.askNotificationPermission()', 'CALL', 'Notification-permission result lambda reads the ask flag', cls='explicit', evidence='SRC ui/PermissionManager.java:89; SRC SettingsRepositoryImpl.java:1425')

UNREACHABLE.update({
    'TorrentStream$1.newArray': ('no_trigger_in_app',
        'Framework Parcelable dispatch only; no parcel/unparcel site for a TorrentStream exists in the app tree. Flips together with the batch-41 Parcelable quartet on one printed parceling site.',
        'SRC TorrentStream.java:102-106',
        'INFERRED'),
    'SettingsRepositoryImpl.askManageAllFilesPermission()': ('closed_by_api_level',
        'Only call sites are inside R-gated PermissionManager blocks (registration :60-67 and branch :99-104), both false at API 27.',
        'SRC ui/PermissionManager.java:60-67; SRC ui/PermissionManager.java:99-104; SRC SettingsRepositoryImpl.java:1397-1399',
        'INFERRED'),
    'SettingsRepositoryImpl.askManageAllFilesPermission(boolean)': ('closed_by_api_level',
        'Only call site is inside setDoNotAskStorage, R-gated at PermissionManager :117, false at API 27.',
        'SRC ui/PermissionManager.java:117-118; SRC SettingsRepositoryImpl.java:1403-1407',
        'INFERRED'),
    'SettingsRepositoryImpl.askNotificationPermission(boolean)': ('closed_by_api_level',
        'Only call site is inside setDoNotAskNotifications, TIRAMISU-gated at PermissionManager :123, false at API 27.',
        'SRC ui/PermissionManager.java:123-124; SRC SettingsRepositoryImpl.java:1431-1435',
        'INFERRED'),
})

# Three of this batch's UNREACHABLE methods have REACHABLE bytecode
# callers in batch 74 (PermissionManager): requestPermissions and the
# (itself UNREACHABLE) lambda$new$0 call the getter; setDoNotAskStorage
# calls the boolean setter; setDoNotAskNotifications calls the
# notification setter. They are suppressed here and listed as
# cross-group pairs in REPORT.md for merger reconciliation. newArray
# has no bytecode caller.
SUPPRESS.update({
    'SettingsRepositoryImpl.askManageAllFilesPermission()',
    'SettingsRepositoryImpl.askManageAllFilesPermission(boolean)',
    'SettingsRepositoryImpl.askNotificationPermission(boolean)',
})
