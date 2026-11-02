# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b046 — converter C07 delivery.
# Base: audited A3 output helper/a3-g9/parts/b046.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# clone/graphs/LibreTorrent/scratch/merge-ready/batch46-merge-ready.md).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/46/ (see REPORT-b046.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Merger notes (NOT applied in this part): the G12 F4 SUPPRESS pairs naming this
# batch's rows 21-22 (showManageAllFilesWarningDialog) as callers of batch-58 row 15's
# callee are added by the merger at merge (caller-part convention); they are NOT in
# this part's SUPPRESS set, which holds only this batch's own two keys.
# Batch 46 part (SettingsRepositoryImpl proxy/read-session/refresh/save/scheduling/streaming/theme/notify settings). Hand-written edges only, plus Dependencies for rows already covered by graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b046_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Routes into the Dependencies rows already exist in graph_def.py and are not
# repeated here; they are named in the .md Dependencies line.

e('ProxySettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.proxyType(int)', 'CALL', 'Proxy section persists the proxy type', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:210; SRC SettingsRepositoryImpl.java:1000')
e('TorrentEngine.<init>', 'SettingsRepositoryImpl.readSessionSettings', 'CALL', 'Engine construction builds the session settings', cls='explicit', evidence='SRC TorrentEngine.java:139; SRC SettingsRepositoryImpl.java:212-260')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.refreshFeedsInterval()', 'CALL', 'Feed section reads the refresh interval to reschedule feeds', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:133-134; SRC SettingsRepositoryImpl.java:1202')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.refreshFeedsInterval(long)', 'CALL', 'Feed section persists the refresh interval', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:141; SRC SettingsRepositoryImpl.java:1208')
e('TorrentEngine$5.onTorrentAdded', 'SettingsRepositoryImpl.saveTorrentFiles()', 'CALL', 'Added torrent is saved when torrent-file saving is enabled', cls='explicit', evidence='SRC TorrentEngine.java:1273; SRC SettingsRepositoryImpl.java:747')
e('TorrentEngine$5.onTorrentAdded', 'SettingsRepositoryImpl.saveTorrentFilesIn()', 'CALL', 'Added torrent reads the torrent-file destination', cls='explicit', evidence='SRC TorrentEngine.java:1275; SRC SettingsRepositoryImpl.java:760')
e('TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)', 'SettingsRepositoryImpl.saveTorrentsIn()', 'CALL', 'Adding a torrent reads the torrent save directory', cls='explicit', evidence='SRC TorrentEngine.java:1185; SRC SettingsRepositoryImpl.java:708')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.schedulingRunOnlyOnce()', 'CALL', 'Scheduling section binds the run-only-once toggle from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:100; SRC SettingsRepositoryImpl.java:1150')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.schedulingRunOnlyOnce(boolean)', 'CALL', 'Scheduling section persists the run-only-once toggle', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:234; SRC SettingsRepositoryImpl.java:1156')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.schedulingShutdownTime()', 'CALL', 'Scheduling section binds the shutdown time from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:93; SRC SettingsRepositoryImpl.java:1137')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.schedulingShutdownTime(int)', 'CALL', 'Scheduling section persists the shutdown time', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:228; SRC SettingsRepositoryImpl.java:1143')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.schedulingStartTime()', 'CALL', 'Scheduling section binds the start time from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:86; SRC SettingsRepositoryImpl.java:1124')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.schedulingStartTime(int)', 'CALL', 'Scheduling section persists the start time', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:222; SRC SettingsRepositoryImpl.java:1130')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.schedulingSwitchWiFi()', 'CALL', 'Scheduling section binds the switch-WiFi toggle from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:107; SRC SettingsRepositoryImpl.java:1163')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.schedulingSwitchWiFi(boolean)', 'CALL', 'Scheduling section persists the switch-WiFi toggle', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:237; SRC SettingsRepositoryImpl.java:1169')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.seedingOutgoingConnections()', 'CALL', 'Settings-change dispatch reads the seeding outgoing-connections flag', cls='explicit', evidence='SRC TorrentEngine.java:1609; SRC SettingsRepositoryImpl.java:942')
e('TorrentEngine$5.onNatError', 'SettingsRepositoryImpl.showNatErrors()', 'CALL', 'NAT error handler reads the show-NAT-errors flag', cls='explicit', evidence='SRC TorrentEngine.java:1395; SRC SettingsRepositoryImpl.java:695')
e('TorrentEngine.handleAutoStop', 'SettingsRepositoryImpl.shutdownDownloadsComplete()', 'CALL', 'Auto-stop handler reads the shutdown-on-complete flag', cls='explicit', evidence='SRC TorrentEngine.java:144; SRC SettingsRepositoryImpl.java:435')
e('TorrentEngine.startStreamingServer', 'SettingsRepositoryImpl.streamingHostname()', 'CALL', 'Streaming server start reads the streaming hostname', cls='explicit', evidence='SRC TorrentEngine.java:1066; SRC SettingsRepositoryImpl.java:1280')
e('StreamingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.streamingHostname(String)', 'CALL', 'Streaming section persists the streaming hostname', cls='explicit', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:102; SRC SettingsRepositoryImpl.java:1286')
e('TorrentEngine.startStreamingServer', 'SettingsRepositoryImpl.streamingPort()', 'CALL', 'Streaming server start reads the streaming port', cls='explicit', evidence='SRC TorrentEngine.java:1067; SRC SettingsRepositoryImpl.java:1293')
e('StreamingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.streamingPort(int)', 'CALL', 'Streaming section persists the streaming port', cls='explicit', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:108; SRC SettingsRepositoryImpl.java:1299')
e('Utils.getThemePreference', 'SettingsRepositoryImpl.theme()', 'CALL', 'Theme helper reads the theme preference', cls='explicit', evidence='SRC Utils.java:371; SRC SettingsRepositoryImpl.java:329')
e('TorrentNotifier.makeTorrentFinishedNotify', 'SettingsRepositoryImpl.torrentFinishNotify()', 'CALL', 'Finished-torrent notification reads the finish-notify flag', cls='explicit', evidence='SRC ui/TorrentNotifier.java:213; SRC SettingsRepositoryImpl.java:277')
e('TorrentEngine.switchConnectionReceiver', 'SettingsRepositoryImpl.unmeteredConnectionsOnly()', 'CALL', 'Connection-receiver switch reads the unmetered-only flag', cls='explicit', evidence='SRC TorrentEngine.java:1010; SRC SettingsRepositoryImpl.java:513')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.useRandomPort()', 'CALL', 'Settings-change dispatch reads the random-port flag', cls='explicit', evidence='SRC TorrentEngine.java:1546; SRC SettingsRepositoryImpl.java:630')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.validateHttpsTrackers()', 'CALL', 'Settings-change dispatch reads the validate-trackers flag', cls='explicit', evidence='SRC TorrentEngine.java:1652; SRC SettingsRepositoryImpl.java:968')

UNREACHABLE.update({
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog()': ('closed_by_api_level',
        'Only printed call site is Utils.java:706, the third disjunct of the early-return condition at :704-707 (SDK_INT < R || hasPermission || !pref.showManageAllFilesWarningDialog()). At API 27 the first disjunct is TRUE (27 < 30), so || short-circuits and :706 is never evaluated.',
        'SRC Utils.java:704-707; SRC SettingsRepositoryImpl.java:1410',
        'INFERRED'),
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean)': ('closed_by_api_level',
        'Only printed call site is Utils.java:711, after the early return at :704-707. At API 27 the return is always taken (SDK_INT < R true), so :711 is never reached.',
        'SRC Utils.java:704-707; SRC Utils.java:711; SRC SettingsRepositoryImpl.java:1418',
        'INFERRED'),
})

# Suppress bytecode auto edges into the UNREACHABLE methods below.
# Each entry is a method a REACHABLE method calls in bytecode
# (auto_calls.json + class-file invoke scan); the call sites are
# gated at API 27, so the auto edge must not revive the method.
# SettingsRepositoryImpl.showManageAllFilesWarningDialog(): bytecode caller Utils.showManageAllFilesWarningDialog (REACHABLE) :706, short-circuited at API 27, see UNREACHABLE evidence
# SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean): bytecode caller Utils.showManageAllFilesWarningDialog (REACHABLE) :711, after the API-27 early return, see UNREACHABLE evidence
SUPPRESS.update({
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog()',
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean)',
})
