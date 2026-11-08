# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys, so no grade change.
# Batch 45 part (SettingsRepositoryImpl max/move/observe/only-charging/port/proxy settings). Hand-written edges only, plus Dependencies for rows already covered by graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b045_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Routes into the Dependencies rows already exist in graph_def.py and are not
# repeated here; they are named in the .md Dependencies line.

e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxConnectionsPerTorrent()', 'CALL', 'Settings-change dispatch reads the max connections per torrent', cls='explicit', evidence='SRC TorrentEngine.java:1490; SRC SettingsRepositoryImpl.java:864')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxDownloadSpeedLimit()', 'CALL', 'Settings-change dispatch reads the max download speed', cls='explicit', evidence='SRC TorrentEngine.java:1475; SRC SettingsRepositoryImpl.java:825')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxLogSize()', 'CALL', 'Settings-change dispatch reads the max log size', cls='explicit', evidence='SRC TorrentEngine.java:1644; SRC SettingsRepositoryImpl.java:1319')
e('LogSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxLogSize(int)', 'CALL', 'Log section persists the max log size', cls='explicit', evidence='SRC ui/log/LogSettingsFragment.java:95; SRC SettingsRepositoryImpl.java:1325')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxUploadSpeedLimit()', 'CALL', 'Settings-change dispatch reads the max upload speed', cls='explicit', evidence='SRC TorrentEngine.java:1480; SRC SettingsRepositoryImpl.java:838')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxUploadsPerTorrent()', 'CALL', 'Settings-change dispatch reads the max uploads per torrent', cls='explicit', evidence='SRC TorrentEngine.java:1493; SRC SettingsRepositoryImpl.java:877')
e('TorrentEngine$5.onTorrentFinished', 'SettingsRepositoryImpl.moveAfterDownload()', 'CALL', 'Finished torrent moves its files when move-after-download is set', cls='explicit', evidence='SRC TorrentEngine.java:1315; SRC SettingsRepositoryImpl.java:721')
e('TorrentEngine$5.onTorrentFinished', 'SettingsRepositoryImpl.moveAfterDownloadIn()', 'CALL', 'Finished torrent reads the move-after-download destination', cls='explicit', evidence='SRC TorrentEngine.java:1317; SRC SettingsRepositoryImpl.java:734')
e('TorrentService.init', 'SettingsRepositoryImpl.observeSettingsChanged', 'CALL', 'Service init subscribes to the settings-change flowable', cls='explicit', evidence='SRC service/TorrentService.java:125-126; SRC SettingsRepositoryImpl.java:195-211')
e('TorrentEngine.switchPowerReceiver', 'SettingsRepositoryImpl.onlyCharging()', 'CALL', 'Power-receiver switch reads the only-charging flag', cls='explicit', evidence='SRC TorrentEngine.java:992; SRC SettingsRepositoryImpl.java:461')
e('TorrentEngine.setRandomPortRange', 'SettingsRepositoryImpl.portRangeFirst()', 'CALL', 'Random-port setup reads the first port bound', cls='explicit', evidence='SRC TorrentEngine.java:1236; SRC SettingsRepositoryImpl.java:539')
e('TorrentEngine.setRandomPortRange', 'SettingsRepositoryImpl.portRangeSecond()', 'CALL', 'Random-port setup reads the second port bound', cls='explicit', evidence='SRC TorrentEngine.java:1237; SRC SettingsRepositoryImpl.java:552')
e('SettingsRepositoryImpl.readSessionSettings', 'SettingsRepositoryImpl.posixDiskIo()', 'CALL', 'Session-settings builder reads the POSIX disk I/O flag', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:241; SRC SettingsRepositoryImpl.java:812')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyAddress()', 'CALL', 'Proxy setup reads the proxy address', cls='explicit', evidence='SRC TorrentEngine.java:1098; SRC SettingsRepositoryImpl.java:1007')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyAddress(String)', 'CALL', 'Proxy section persists the proxy address', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:223; SRC SettingsRepositoryImpl.java:1013')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyLogin()', 'CALL', 'Proxy setup reads the proxy login', cls='explicit', evidence='SRC TorrentEngine.java:1102; SRC SettingsRepositoryImpl.java:1059')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyLogin(String)', 'CALL', 'Proxy section persists the proxy login', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:227; SRC SettingsRepositoryImpl.java:1065')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyPassword()', 'CALL', 'Proxy setup reads the proxy password', cls='explicit', evidence='SRC TorrentEngine.java:1103; SRC SettingsRepositoryImpl.java:1072')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyPassword(String)', 'CALL', 'Proxy section persists the proxy password', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:231; SRC SettingsRepositoryImpl.java:1078')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyPeersToo()', 'CALL', 'Proxy setup reads the proxy-peers flag', cls='explicit', evidence='SRC TorrentEngine.java:1100; SRC SettingsRepositoryImpl.java:1033')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyPeersToo(boolean)', 'CALL', 'Proxy section persists the proxy-peers flag', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:237; SRC SettingsRepositoryImpl.java:1039')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyPort()', 'CALL', 'Proxy setup reads the proxy port', cls='explicit', evidence='SRC TorrentEngine.java:1099; SRC SettingsRepositoryImpl.java:1020')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyPort(int)', 'CALL', 'Proxy section persists the proxy port', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:218; SRC SettingsRepositoryImpl.java:1026')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyRequiresAuth()', 'CALL', 'Proxy setup reads the proxy-auth flag', cls='explicit', evidence='SRC TorrentEngine.java:1101; SRC SettingsRepositoryImpl.java:1046')
e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyRequiresAuth(boolean)', 'CALL', 'Proxy section persists the proxy-auth flag', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:240; SRC SettingsRepositoryImpl.java:1052')
e('TorrentEngine.setProxy', 'SettingsRepositoryImpl.proxyType()', 'CALL', 'Proxy setup reads the proxy type', cls='explicit', evidence='SRC TorrentEngine.java:1097; SRC SettingsRepositoryImpl.java:994')

UNREACHABLE.update({
    'SettingsRepositoryImpl.notifySound()': ('closed_by_api_level',
        'Only printed call sites never execute at API 27: AppearanceSettingsFragment.java:139 and :151 inside initLegacyNotifySettings (SDK < O gate :118-119) and TorrentNotifier.java:282 inside applyLegacyNotifySettings (early return :276 at SDK >= O).',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:139; SRC ui/settings/sections/AppearanceSettingsFragment.java:151; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:282; SRC SettingsRepositoryImpl.java:264',
        'INFERRED'),
    'SettingsRepositoryImpl.notifySound(String)': ('closed_by_api_level',
        'Only printed call site is AppearanceSettingsFragment.java:213 (ringtone-picker result handler); the picker is launched only from the click listener registered at :144-168, inside initLegacyNotifySettings (SDK < O gate :118-119). At API 27 the picker is never launched.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:144-168; SRC ui/settings/sections/AppearanceSettingsFragment.java:213; SRC SettingsRepositoryImpl.java:270',
        'INFERRED'),
    'SettingsRepositoryImpl.playSoundNotify()': ('closed_by_api_level',
        'Only printed call sites never execute at API 27: AppearanceSettingsFragment.java:133 inside initLegacyNotifySettings (SDK < O gate :118-119) and TorrentNotifier.java:281 inside applyLegacyNotifySettings (early return :276 at SDK >= O).',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:133; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:281; SRC SettingsRepositoryImpl.java:290',
        'INFERRED'),
    'SettingsRepositoryImpl.playSoundNotify(boolean)': ('closed_by_api_level',
        'Only printed call site is AppearanceSettingsFragment.java:241 (onPreferenceChange branch) whose listener is bound only inside initLegacyNotifySettings (:134), gated at SDK < O (:118-119); at API 27 the branch never fires.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:134; SRC ui/settings/sections/AppearanceSettingsFragment.java:241; SRC SettingsRepositoryImpl.java:296',
        'INFERRED'),
})

# Suppress bytecode auto edges into the UNREACHABLE methods below.
# Each entry is a method a REACHABLE method calls in bytecode
# (auto_calls.json + class-file invoke scan); the call sites are
# gated at API 27, so the auto edge must not revive the method.
# SettingsRepositoryImpl.notifySound(): bytecode caller TorrentNotifier.applyLegacyNotifySettings (REACHABLE, batch 74); gated at API 27, see UNREACHABLE evidence
# SettingsRepositoryImpl.playSoundNotify(): bytecode caller TorrentNotifier.applyLegacyNotifySettings (REACHABLE, batch 74); gated at API 27, see UNREACHABLE evidence
# SettingsRepositoryImpl.playSoundNotify(boolean): bytecode caller AppearanceSettingsFragment.onPreferenceChange (REACHABLE) :241
SUPPRESS.update({
    'SettingsRepositoryImpl.notifySound()',
    'SettingsRepositoryImpl.playSoundNotify()',
    'SettingsRepositoryImpl.playSoundNotify(boolean)',
})
