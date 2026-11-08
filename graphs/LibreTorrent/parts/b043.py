# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys (batch has no UNREACHABLE rows), so no grade change.
# Batch 43 part (SettingsRepositoryImpl getters/setters: behavior, network, scheduling, streaming, feed). Hand-written edges only, plus Dependencies for rows already covered by graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b043_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Routes into the Dependencies rows already exist in graph_def.py and are not
# repeated here; they are named in the .md Dependencies line.

e('TorrentEngine.switchPowerReceiver', 'SettingsRepositoryImpl.batteryControl()', 'CALL', 'Power-receiver switch reads the battery-control flag', cls='explicit', evidence='SRC TorrentEngine.java:990; SRC SettingsRepositoryImpl.java:474')
e('TorrentService.init', 'SettingsRepositoryImpl.cpuDoNotSleep()', 'CALL', 'Service init reads the CPU-do-not-sleep flag', cls='explicit', evidence='SRC service/TorrentService.java:129; SRC SettingsRepositoryImpl.java:448')
e('TorrentEngine.switchPowerReceiver', 'SettingsRepositoryImpl.customBatteryControl()', 'CALL', 'Power-receiver switch reads the custom battery-control flag', cls='explicit', evidence='SRC TorrentEngine.java:991; SRC SettingsRepositoryImpl.java:487')
e('TorrentEngine.checkPauseTorrents', 'SettingsRepositoryImpl.customBatteryControlValue()', 'CALL', 'Pause check reads the custom battery threshold', cls='explicit', evidence='SRC TorrentEngine.java:1026; SRC SettingsRepositoryImpl.java:500')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.defaultTrackersList()', 'CALL', 'Settings-change dispatch reads the default tracker list', cls='explicit', evidence='SRC TorrentEngine.java:1648; SRC SettingsRepositoryImpl.java:955')
e('TorrentEngine.startWatchDir', 'SettingsRepositoryImpl.dirToWatch()', 'CALL', 'Watch-dir start reads the watched directory path', cls='explicit', evidence='SRC TorrentEngine.java:1117; SRC SettingsRepositoryImpl.java:786')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.enableDht()', 'CALL', 'Settings-change dispatch reads the DHT flag', cls='explicit', evidence='SRC TorrentEngine.java:1512; SRC SettingsRepositoryImpl.java:565')
e('TorrentEngine.handleOnSessionStarted', 'SettingsRepositoryImpl.enableIpFiltering()', 'CALL', 'Session-started handler reads the IP-filtering flag', cls='explicit', evidence='SRC TorrentEngine.java:1047; SRC SettingsRepositoryImpl.java:669')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.enableLsd()', 'CALL', 'Settings-change dispatch reads the LSD flag', cls='explicit', evidence='SRC TorrentEngine.java:1517; SRC SettingsRepositoryImpl.java:578')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.enableNatPmp()', 'CALL', 'Settings-change dispatch reads the NAT-PMP flag', cls='explicit', evidence='SRC TorrentEngine.java:1532; SRC SettingsRepositoryImpl.java:617')
e('TorrentEngine.checkPauseTorrents', 'SettingsRepositoryImpl.enableRoaming()', 'CALL', 'Pause check reads the roaming flag', cls='explicit', evidence='SRC TorrentEngine.java:1029; SRC SettingsRepositoryImpl.java:526')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.enableSchedulingShutdown()', 'CALL', 'Scheduling section binds the shutdown toggle from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:79; SRC SettingsRepositoryImpl.java:1111')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableSchedulingShutdown(boolean)', 'CALL', 'Scheduling section persists the shutdown toggle', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:209; SRC SettingsRepositoryImpl.java:1117')
e('SchedulingSettingsFragment.onCreate', 'SettingsRepositoryImpl.enableSchedulingStart()', 'CALL', 'Scheduling section binds the start toggle from the getter', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:72; SRC SettingsRepositoryImpl.java:1098')
e('SchedulingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableSchedulingStart(boolean)', 'CALL', 'Scheduling section persists the start toggle', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:196; SRC SettingsRepositoryImpl.java:1104')
e('TorrentEngine.handleOnSessionStarted', 'SettingsRepositoryImpl.enableStreaming()', 'CALL', 'Session-started handler reads the streaming flag', cls='explicit', evidence='SRC TorrentEngine.java:1056; SRC SettingsRepositoryImpl.java:1267')
e('StreamingSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableStreaming(boolean)', 'CALL', 'Streaming section persists the streaming toggle', cls='explicit', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:113; SRC SettingsRepositoryImpl.java:1273')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.enableUpnp()', 'CALL', 'Settings-change dispatch reads the UPnP flag', cls='explicit', evidence='SRC TorrentEngine.java:1527; SRC SettingsRepositoryImpl.java:604')
e('TorrentEngine.handleSettingsChanged', 'SettingsRepositoryImpl.enableUtp()', 'CALL', 'Settings-change dispatch reads the uTP flag', cls='explicit', evidence='SRC TorrentEngine.java:1522; SRC SettingsRepositoryImpl.java:591')
e('TorrentEngine.getEncryptInConnectionsMode', 'SettingsRepositoryImpl.encryptInConnectionsMode()', 'CALL', 'Incoming-encryption mode helper reads the preference', cls='explicit', evidence='SRC TorrentEngine.java:1109; SRC SettingsRepositoryImpl.java:643')
e('TorrentEngine.getEncryptOutConnectionsMode', 'SettingsRepositoryImpl.encryptOutConnectionsMode()', 'CALL', 'Outgoing-encryption mode helper reads the preference', cls='explicit', evidence='SRC TorrentEngine.java:1113; SRC SettingsRepositoryImpl.java:656')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.feedItemKeepTime()', 'CALL', 'Feed section binds the keep-time preference from the getter', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:91; SRC SettingsRepositoryImpl.java:1176')
e('FeedSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.feedItemKeepTime(long)', 'CALL', 'Feed section persists the keep-time preference', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:146; SRC SettingsRepositoryImpl.java:1182')
e('FeedSettingsFragment.onCreate', 'SettingsRepositoryImpl.feedRemoveDuplicates()', 'CALL', 'Feed section binds the remove-duplicates switch from the getter', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:108; SRC SettingsRepositoryImpl.java:1254')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: no UNREACHABLE method of this batch has a
# REACHABLE bytecode caller (checked in auto_calls.json + class files).
SUPPRESS.update(set())
