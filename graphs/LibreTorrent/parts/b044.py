# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys, so no grade change.
# Batch 44 part (SettingsRepositoryImpl feed/foreground/IP-filter/keep-alive/log/max settings + observeSettingsChanged lambdas). Hand-written edges only, plus Dependencies for rows already covered by graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b044_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Routes into the Dependencies rows already exist in graph_def.py and are not
# repeated here; they are named in the .md Dependencies line.

e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.feedRemoveDuplicates(boolean)', 'CALL', 'Feed section persists the remove-duplicates toggle', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:158; SRC SettingsRepositoryImpl.java:1260')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.feedStartTorrents()', 'CALL', 'Feed section binds the start-torrents switch from the getter', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:101; SRC SettingsRepositoryImpl.java:1241')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.feedStartTorrents(boolean)', 'CALL', 'Feed section persists the start-torrents toggle', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:155; SRC SettingsRepositoryImpl.java:1247')
e('TorrentService.handleSettingsChanged', 'SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton()', 'CALL', 'Service settings dispatch reads the combined pause-button flag', cls='explicit', evidence='SRC service/TorrentService.java:273; SRC SettingsRepositoryImpl.java:401')
e('Utils.getForegroundNotifySorting', 'SettingsRepositoryImpl.foregroundNotifySorting()', 'CALL', 'Foreground-notify sorting helper reads the sorting value', cls='explicit', evidence='SRC Utils.java:896; SRC SettingsRepositoryImpl.java:373')
e('Utils.getForegroundNotifyFilter', 'SettingsRepositoryImpl.foregroundNotifyStatusFilter()', 'CALL', 'Foreground-notify filter helper reads the status filter', cls='explicit', evidence='SRC Utils.java:877; SRC SettingsRepositoryImpl.java:355')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.ipFilteringFile()', 'CALL', 'Settings-change dispatch reads the IP-filter file path', cls='explicit', evidence='SRC TorrentEngine.java:1556; SRC TorrentEngine.java:1564; SRC SettingsRepositoryImpl.java:682')
e('TorrentEngine.requestStop', 'SettingsRepositoryImpl.keepAlive()', 'CALL', 'Engine stop request reads the keep-alive flag', cls='explicit', evidence='SRC TorrentEngine.java:276; SRC SettingsRepositoryImpl.java:422')
e('SettingsRepositoryImpl.observeSettingsChanged', 'SettingsRepositoryImpl.lambda$observeSettingsChanged$0', 'CALL', 'Preference-change listener lambda runs on a preference change', cls='non_standard', via='SharedPreferences OnSharedPreferenceChangeListener dispatch inside observeSettingsChanged', evidence='SRC SettingsRepositoryImpl.java:195-211')
e('SettingsRepositoryImpl.observeSettingsChanged', 'SettingsRepositoryImpl.lambda$observeSettingsChanged$1', 'CALL', 'Unregister lambda runs when the settings subscription is disposed', cls='non_standard', via='Rx Disposables.fromAction unregister dispatch inside observeSettingsChanged', evidence='SRC SettingsRepositoryImpl.java:195-211')
e('SettingsRepositoryImpl.observeSettingsChanged', 'SettingsRepositoryImpl.lambda$observeSettingsChanged$2', 'CALL', 'Flowable emitter lambda runs on subscription', cls='non_standard', via='Rx Flowable.create emitter dispatch inside observeSettingsChanged', evidence='SRC SettingsRepositoryImpl.java:195-211')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logDhtFilter()', 'CALL', 'Settings-change dispatch reads the DHT log filter', cls='explicit', evidence='SRC TorrentEngine.java:1624; SRC SettingsRepositoryImpl.java:1345')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logDhtFilter(boolean)', 'CALL', 'Log params callback persists the DHT log filter', cls='explicit', evidence='SRC ui/log/LogViewModel.java:125; SRC SettingsRepositoryImpl.java:1351')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logPeerFilter()', 'CALL', 'Settings-change dispatch reads the peer log filter', cls='explicit', evidence='SRC TorrentEngine.java:1629; SRC SettingsRepositoryImpl.java:1358')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logPeerFilter(boolean)', 'CALL', 'Log params callback persists the peer log filter', cls='explicit', evidence='SRC ui/log/LogViewModel.java:128; SRC SettingsRepositoryImpl.java:1364')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logPortmapFilter()', 'CALL', 'Settings-change dispatch reads the portmap log filter', cls='explicit', evidence='SRC TorrentEngine.java:1634; SRC SettingsRepositoryImpl.java:1371')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logPortmapFilter(boolean)', 'CALL', 'Log params callback persists the portmap log filter', cls='explicit', evidence='SRC ui/log/LogViewModel.java:131; SRC SettingsRepositoryImpl.java:1377')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logSessionFilter()', 'CALL', 'Settings-change dispatch reads the session log filter', cls='explicit', evidence='SRC TorrentEngine.java:1619; SRC SettingsRepositoryImpl.java:1332')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logSessionFilter(boolean)', 'CALL', 'Log params callback persists the session log filter', cls='explicit', evidence='SRC ui/log/LogViewModel.java:122; SRC SettingsRepositoryImpl.java:1338')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logTorrentFilter()', 'CALL', 'Settings-change dispatch reads the torrent log filter', cls='explicit', evidence='SRC TorrentEngine.java:1639; SRC SettingsRepositoryImpl.java:1384')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logTorrentFilter(boolean)', 'CALL', 'Log params callback persists the torrent log filter', cls='explicit', evidence='SRC ui/log/LogViewModel.java:134; SRC SettingsRepositoryImpl.java:1390')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.logging()', 'CALL', 'Settings-change dispatch reads the logging flag', cls='explicit', evidence='SRC TorrentEngine.java:1614; SRC SettingsRepositoryImpl.java:1306')
e('LogViewModel$1.onPropertyChanged', 'SettingsRepositoryImpl.logging(boolean)', 'CALL', 'Log params callback persists the logging flag', cls='explicit', evidence='SRC ui/log/LogViewModel.java:119; SRC SettingsRepositoryImpl.java:1312')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxActiveDownloads()', 'CALL', 'Settings-change dispatch reads the max active downloads', cls='explicit', evidence='SRC TorrentEngine.java:1497; SRC SettingsRepositoryImpl.java:903')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxActiveTorrents()', 'CALL', 'Settings-change dispatch reads the max active torrents', cls='explicit', evidence='SRC TorrentEngine.java:1507; SRC SettingsRepositoryImpl.java:916')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxActiveUploads()', 'CALL', 'Settings-change dispatch reads the max active uploads', cls='explicit', evidence='SRC TorrentEngine.java:1502; SRC SettingsRepositoryImpl.java:890')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.maxConnections()', 'CALL', 'Settings-change dispatch reads the max connections', cls='explicit', evidence='SRC TorrentEngine.java:1485; SRC SettingsRepositoryImpl.java:851')

UNREACHABLE.update({
    'SettingsRepositoryImpl.ledIndicatorColorNotify()': ('closed_by_api_level',
        'Only printed call sites never execute at API 27: AppearanceSettingsFragment.java:180 inside initLegacyNotifySettings (SDK < O gate :118-119) and TorrentNotifier.java:290 inside applyLegacyNotifySettings (early return :276 at SDK >= O).',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:180; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:290; SRC SettingsRepositoryImpl.java:342-344',
        'INFERRED'),
    'SettingsRepositoryImpl.ledIndicatorColorNotify(int)': ('closed_by_api_level',
        'Only printed call site is AppearanceSettingsFragment.java:250 (onPreferenceChange branch) whose listener is bound only inside initLegacyNotifySettings (:181), gated at SDK < O (:118-119); at API 27 the branch never fires.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:181; SRC ui/settings/sections/AppearanceSettingsFragment.java:250; SRC SettingsRepositoryImpl.java:348',
        'INFERRED'),
    'SettingsRepositoryImpl.ledIndicatorNotify()': ('closed_by_api_level',
        'Only printed call sites never execute at API 27: AppearanceSettingsFragment.java:173 inside initLegacyNotifySettings (SDK < O gate :118-119) and TorrentNotifier.java:289 inside applyLegacyNotifySettings (early return :276 at SDK >= O).',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:173; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:289; SRC SettingsRepositoryImpl.java:303',
        'INFERRED'),
    'SettingsRepositoryImpl.ledIndicatorNotify(boolean)': ('closed_by_api_level',
        'Only printed call site is AppearanceSettingsFragment.java:244 (onPreferenceChange branch) whose listener is bound only inside initLegacyNotifySettings (:174), gated at SDK < O (:118-119); at API 27 the branch never fires.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:174; SRC ui/settings/sections/AppearanceSettingsFragment.java:244; SRC SettingsRepositoryImpl.java:309',
        'INFERRED'),
})

# Suppress bytecode auto edges into the UNREACHABLE methods below.
# Each entry is a method a REACHABLE method calls in bytecode
# (auto_calls.json + class-file invoke scan); the call sites are
# gated at API 27, so the auto edge must not revive the method.
# SettingsRepositoryImpl.ledIndicatorColorNotify(): bytecode caller TorrentNotifier.applyLegacyNotifySettings (REACHABLE, batch 74) + AppearanceSettingsFragment.onPreferenceChange setter branch for the (int) overload; gated at API 27, see UNREACHABLE evidence
# SettingsRepositoryImpl.ledIndicatorColorNotify(int): bytecode caller AppearanceSettingsFragment.onPreferenceChange (REACHABLE) :250
# SettingsRepositoryImpl.ledIndicatorNotify(): bytecode caller TorrentNotifier.applyLegacyNotifySettings (REACHABLE, batch 74)
# SettingsRepositoryImpl.ledIndicatorNotify(boolean): bytecode caller AppearanceSettingsFragment.onPreferenceChange (REACHABLE) :244
SUPPRESS.update({
    'SettingsRepositoryImpl.ledIndicatorColorNotify()',
    'SettingsRepositoryImpl.ledIndicatorColorNotify(int)',
    'SettingsRepositoryImpl.ledIndicatorNotify()',
    'SettingsRepositoryImpl.ledIndicatorNotify(boolean)',
})
