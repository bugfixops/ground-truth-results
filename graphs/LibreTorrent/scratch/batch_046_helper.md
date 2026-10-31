# LibreTorrent batch 46 source audit

Membership is exactly the 40 plan rows printed at the top of `batch_046_helper_printed.txt`. That file includes all of `SettingsRepositoryImpl`, its interface declarations, and an in-source call-site search. I leave these rows OPEN: preference bodies and local uses are printed, but complete entry-to-method routes through preferences, scheduling, storage selection, and settings consumers have not been traced in this audit. No absent caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `SettingsRepositoryImpl.proxyType(int)V` | OPEN | `SettingsRepositoryImpl.java:1000+`; mutator/call-site search printed; full settings UI route unresolved. |
| 2 | `SettingsRepositoryImpl.readSessionSettings()SessionSettings` | OPEN | `SettingsRepositoryImpl.java:212+`; aggregate getter and callers printed; complete session startup route unresolved. |
| 3 | `SettingsRepositoryImpl.refreshFeedsInterval()long` | OPEN | `SettingsRepositoryImpl.java:1202+`; accessor/call-site search printed; feed scheduling route unresolved. |
| 4 | `SettingsRepositoryImpl.refreshFeedsInterval(long)V` | OPEN | `SettingsRepositoryImpl.java:1208+`; mutator/call-site search printed; feed settings route unresolved. |
| 5 | `SettingsRepositoryImpl.saveTorrentFiles()Z` | OPEN | `SettingsRepositoryImpl.java:747+`; accessor/call-site search printed; storage preference route unresolved. |
| 6 | `SettingsRepositoryImpl.saveTorrentFiles(boolean)V` | OPEN | `SettingsRepositoryImpl.java:753+`; mutator/call-site search printed; storage preference route unresolved. |
| 7 | `SettingsRepositoryImpl.saveTorrentFilesIn()String` | OPEN | `SettingsRepositoryImpl.java:760+`; accessor/call-site search printed; storage location selection route unresolved. |
| 8 | `SettingsRepositoryImpl.saveTorrentFilesIn(String)V` | OPEN | `SettingsRepositoryImpl.java:766+`; mutator/call-site search printed; storage location selection route unresolved. |
| 9 | `SettingsRepositoryImpl.saveTorrentsIn()String` | OPEN | `SettingsRepositoryImpl.java:708+`; accessor/call-site search printed; storage location selection route unresolved. |
| 10 | `SettingsRepositoryImpl.saveTorrentsIn(String)V` | OPEN | `SettingsRepositoryImpl.java:714+`; mutator/call-site search printed; storage location selection route unresolved. |
| 11 | `SettingsRepositoryImpl.schedulingRunOnlyOnce()Z` | OPEN | `SettingsRepositoryImpl.java:1150+`; accessor/call-site search printed; scheduler settings entry route unresolved. |
| 12 | `SettingsRepositoryImpl.schedulingRunOnlyOnce(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1156+`; mutator/call-site search printed; scheduler settings entry route unresolved. |
| 13 | `SettingsRepositoryImpl.schedulingShutdownTime()int` | OPEN | `SettingsRepositoryImpl.java:1137+`; accessor/call-site search printed; scheduler settings entry route unresolved. |
| 14 | `SettingsRepositoryImpl.schedulingShutdownTime(int)V` | OPEN | `SettingsRepositoryImpl.java:1143+`; mutator/call-site search printed; scheduler settings entry route unresolved. |
| 15 | `SettingsRepositoryImpl.schedulingStartTime()int` | OPEN | `SettingsRepositoryImpl.java:1124+`; accessor/call-site search printed; scheduler settings entry route unresolved. |
| 16 | `SettingsRepositoryImpl.schedulingStartTime(int)V` | OPEN | `SettingsRepositoryImpl.java:1130+`; mutator/call-site search printed; scheduler settings entry route unresolved. |
| 17 | `SettingsRepositoryImpl.schedulingSwitchWiFi()Z` | OPEN | `SettingsRepositoryImpl.java:1163+`; accessor/call-site search printed; scheduler settings entry route unresolved. |
| 18 | `SettingsRepositoryImpl.schedulingSwitchWiFi(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1169+`; mutator/call-site search printed; scheduler settings entry route unresolved. |
| 19 | `SettingsRepositoryImpl.seedingOutgoingConnections()Z` | OPEN | `SettingsRepositoryImpl.java:942+`; accessor/call-site search printed; session settings route unresolved. |
| 20 | `SettingsRepositoryImpl.seedingOutgoingConnections(boolean)V` | OPEN | `SettingsRepositoryImpl.java:948+`; mutator/call-site search printed; session settings route unresolved. |
| 21 | `SettingsRepositoryImpl.showManageAllFilesWarningDialog()Z` | OPEN | `SettingsRepositoryImpl.java:1410+`; accessor/call-site search printed; permission warning UI route unresolved. |
| 22 | `SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1418+`; mutator/call-site search printed; permission warning UI route unresolved. |
| 23 | `SettingsRepositoryImpl.showNatErrors()Z` | OPEN | `SettingsRepositoryImpl.java:695+`; accessor/call-site search printed; error/settings route unresolved. |
| 24 | `SettingsRepositoryImpl.showNatErrors(boolean)V` | OPEN | `SettingsRepositoryImpl.java:701+`; mutator/call-site search printed; error/settings route unresolved. |
| 25 | `SettingsRepositoryImpl.shutdownDownloadsComplete()Z` | OPEN | `SettingsRepositoryImpl.java:435+`; accessor/call-site search printed; scheduler/shutdown route unresolved. |
| 26 | `SettingsRepositoryImpl.shutdownDownloadsComplete(boolean)V` | OPEN | `SettingsRepositoryImpl.java:441+`; mutator/call-site search printed; scheduler/settings route unresolved. |
| 27 | `SettingsRepositoryImpl.streamingHostname()String` | OPEN | `SettingsRepositoryImpl.java:1280+`; accessor/call-site search printed; streaming server/settings route unresolved. |
| 28 | `SettingsRepositoryImpl.streamingHostname(String)V` | OPEN | `SettingsRepositoryImpl.java:1286+`; mutator/call-site search printed; streaming server/settings route unresolved. |
| 29 | `SettingsRepositoryImpl.streamingPort()int` | OPEN | `SettingsRepositoryImpl.java:1293+`; accessor/call-site search printed; streaming server/settings route unresolved. |
| 30 | `SettingsRepositoryImpl.streamingPort(int)V` | OPEN | `SettingsRepositoryImpl.java:1299+`; mutator/call-site search printed; streaming server/settings route unresolved. |
| 31 | `SettingsRepositoryImpl.theme()int` | OPEN | `SettingsRepositoryImpl.java:329+`; accessor/call-site search printed; app startup/settings route unresolved. |
| 32 | `SettingsRepositoryImpl.theme(int)V` | OPEN | `SettingsRepositoryImpl.java:335+`; mutator/call-site search printed; theme settings route unresolved. |
| 33 | `SettingsRepositoryImpl.torrentFinishNotify()Z` | OPEN | `SettingsRepositoryImpl.java:277+`; accessor/call-site search printed; notification settings route unresolved. |
| 34 | `SettingsRepositoryImpl.torrentFinishNotify(boolean)V` | OPEN | `SettingsRepositoryImpl.java:283+`; mutator/call-site search printed; notification settings route unresolved. |
| 35 | `SettingsRepositoryImpl.unmeteredConnectionsOnly()Z` | OPEN | `SettingsRepositoryImpl.java:513+`; accessor/call-site search printed; feed/network settings route unresolved. |
| 36 | `SettingsRepositoryImpl.unmeteredConnectionsOnly(boolean)V` | OPEN | `SettingsRepositoryImpl.java:519+`; mutator/call-site search printed; feed/network settings route unresolved. |
| 37 | `SettingsRepositoryImpl.useRandomPort()Z` | OPEN | `SettingsRepositoryImpl.java:630+`; accessor/call-site search printed; session settings route unresolved. |
| 38 | `SettingsRepositoryImpl.useRandomPort(boolean)V` | OPEN | `SettingsRepositoryImpl.java:636+`; mutator/call-site search printed; session settings route unresolved. |
| 39 | `SettingsRepositoryImpl.validateHttpsTrackers()Z` | OPEN | `SettingsRepositoryImpl.java:968+`; accessor/call-site search printed; tracker settings route unresolved. |
| 40 | `SettingsRepositoryImpl.validateHttpsTrackers(boolean)V` | OPEN | `SettingsRepositoryImpl.java:974+`; mutator/call-site search printed; tracker settings route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
