# LibreTorrent batch 44 source audit

Membership is exactly the 40 batch 44 rows printed at the top of `batch_044_helper_printed.txt`. The evidence file contains the `SettingsRepositoryImpl` bodies, `SettingsRepository` declarations, observed-settings lambdas, defaults, and an in-source call-site search. I leave these methods OPEN because complete entry-to-method paths through settings screens, feed preferences, notification settings, and Rx observer registration have not been traced here. Preference accessors and local lambdas are not by themselves proof of a complete route. No missing caller match is used as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `SettingsRepositoryImpl.feedRemoveDuplicates(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1260+`; preference mutator body/call-site search printed; full settings route unresolved. |
| 2 | `SettingsRepositoryImpl.feedStartTorrents()Z` | OPEN | `SettingsRepositoryImpl.java:1241+`; accessor body/call-site search printed; full feed settings route unresolved. |
| 3 | `SettingsRepositoryImpl.feedStartTorrents(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1247+`; mutator body/call-site search printed; full feed settings route unresolved. |
| 4 | `SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton()Z` | OPEN | `SettingsRepositoryImpl.java:401+`; accessor body/call-site search printed; notification settings entry route unresolved. |
| 5 | `SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton(boolean)V` | OPEN | `SettingsRepositoryImpl.java:391+`; mutator body/call-site search printed; notification settings entry route unresolved. |
| 6 | `SettingsRepositoryImpl.foregroundNotifySorting()String` | OPEN | `SettingsRepositoryImpl.java:373+`; accessor and callers searched; settings screen route unresolved. |
| 7 | `SettingsRepositoryImpl.foregroundNotifySorting(String)V` | OPEN | `SettingsRepositoryImpl.java:381+`; mutator and callers searched; settings screen route unresolved. |
| 8 | `SettingsRepositoryImpl.foregroundNotifyStatusFilter()String` | OPEN | `SettingsRepositoryImpl.java:355+`; accessor and callers searched; settings screen route unresolved. |
| 9 | `SettingsRepositoryImpl.foregroundNotifyStatusFilter(String)V` | OPEN | `SettingsRepositoryImpl.java:363+`; mutator and callers searched; settings screen route unresolved. |
| 10 | `SettingsRepositoryImpl.ipFilteringFile()String` | OPEN | `SettingsRepositoryImpl.java:682+`; accessor and callers searched; complete settings/file selection route unresolved. |
| 11 | `SettingsRepositoryImpl.ipFilteringFile(String)V` | OPEN | `SettingsRepositoryImpl.java:688+`; mutator and callers searched; complete settings/file selection route unresolved. |
| 12 | `SettingsRepositoryImpl.keepAlive()Z` | OPEN | `SettingsRepositoryImpl.java:422+`; accessor and callers searched; preference UI route unresolved. |
| 13 | `SettingsRepositoryImpl.keepAlive(boolean)V` | OPEN | `SettingsRepositoryImpl.java:428+`; mutator and callers searched; preference UI route unresolved. |
| 14 | `SettingsRepositoryImpl.lambda$observeSettingsChanged$0(FlowableEmitter,SharedPreferences,String)V` | OPEN | `SettingsRepositoryImpl.java:195+`; observer callback lambda printed; Rx subscription/delivery path unresolved. |
| 15 | `SettingsRepositoryImpl.lambda$observeSettingsChanged$1(OnSharedPreferenceChangeListener)V` | OPEN | `SettingsRepositoryImpl.java:195+`; disposal lambda printed; Rx disposal route unresolved. |
| 16 | `SettingsRepositoryImpl.lambda$observeSettingsChanged$2(FlowableEmitter)V` | OPEN | `SettingsRepositoryImpl.java:195+`; observer registration lambda printed; Rx subscription path unresolved. |
| 17 | `SettingsRepositoryImpl.ledIndicatorColorNotify()I` | OPEN | `SettingsRepositoryImpl.java:342+`; accessor body/call-site search printed; notification settings route unresolved. |
| 18 | `SettingsRepositoryImpl.ledIndicatorColorNotify(int)V` | OPEN | `SettingsRepositoryImpl.java:348+`; mutator body/call-site search printed; notification settings route unresolved. |
| 19 | `SettingsRepositoryImpl.ledIndicatorNotify()Z` | OPEN | `SettingsRepositoryImpl.java:303+`; accessor body/call-site search printed; notification settings route unresolved. |
| 20 | `SettingsRepositoryImpl.ledIndicatorNotify(boolean)V` | OPEN | `SettingsRepositoryImpl.java:309+`; mutator body/call-site search printed; notification settings route unresolved. |
| 21 | `SettingsRepositoryImpl.logDhtFilter()Z` | OPEN | `SettingsRepositoryImpl.java:1345+`; accessor body/call-site search printed; log settings route unresolved. |
| 22 | `SettingsRepositoryImpl.logDhtFilter(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1351+`; mutator body/call-site search printed; log settings route unresolved. |
| 23 | `SettingsRepositoryImpl.logPeerFilter()Z` | OPEN | `SettingsRepositoryImpl.java:1358+`; accessor body/call-site search printed; log settings route unresolved. |
| 24 | `SettingsRepositoryImpl.logPeerFilter(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1364+`; mutator body/call-site search printed; log settings route unresolved. |
| 25 | `SettingsRepositoryImpl.logPortmapFilter()Z` | OPEN | `SettingsRepositoryImpl.java:1371+`; accessor body/call-site search printed; log settings route unresolved. |
| 26 | `SettingsRepositoryImpl.logPortmapFilter(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1377+`; mutator body/call-site search printed; log settings route unresolved. |
| 27 | `SettingsRepositoryImpl.logSessionFilter()Z` | OPEN | `SettingsRepositoryImpl.java:1332+`; accessor body/call-site search printed; log settings route unresolved. |
| 28 | `SettingsRepositoryImpl.logSessionFilter(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1338+`; mutator body/call-site search printed; log settings route unresolved. |
| 29 | `SettingsRepositoryImpl.logTorrentFilter()Z` | OPEN | `SettingsRepositoryImpl.java:1384+`; accessor body/call-site search printed; log settings route unresolved. |
| 30 | `SettingsRepositoryImpl.logTorrentFilter(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1390+`; mutator body/call-site search printed; log settings route unresolved. |
| 31 | `SettingsRepositoryImpl.logging()Z` | OPEN | `SettingsRepositoryImpl.java:1306+`; accessor body/call-site search printed; log settings route unresolved. |
| 32 | `SettingsRepositoryImpl.logging(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1312+`; mutator body/call-site search printed; log settings route unresolved. |
| 33 | `SettingsRepositoryImpl.maxActiveDownloads()I` | OPEN | `SettingsRepositoryImpl.java:903+`; accessor body/call-site search printed; session settings route unresolved. |
| 34 | `SettingsRepositoryImpl.maxActiveDownloads(int)V` | OPEN | `SettingsRepositoryImpl.java:909+`; mutator body/call-site search printed; session settings route unresolved. |
| 35 | `SettingsRepositoryImpl.maxActiveTorrents()I` | OPEN | `SettingsRepositoryImpl.java:916+`; accessor body/call-site search printed; session settings route unresolved. |
| 36 | `SettingsRepositoryImpl.maxActiveTorrents(int)V` | OPEN | `SettingsRepositoryImpl.java:922+`; mutator body/call-site search printed; session settings route unresolved. |
| 37 | `SettingsRepositoryImpl.maxActiveUploads()I` | OPEN | `SettingsRepositoryImpl.java:890+`; accessor body/call-site search printed; session settings route unresolved. |
| 38 | `SettingsRepositoryImpl.maxActiveUploads(int)V` | OPEN | `SettingsRepositoryImpl.java:896+`; mutator body/call-site search printed; session settings route unresolved. |
| 39 | `SettingsRepositoryImpl.maxConnections()I` | OPEN | `SettingsRepositoryImpl.java:851+`; accessor body/call-site search printed; session settings route unresolved. |
| 40 | `SettingsRepositoryImpl.maxConnections(int)V` | OPEN | `SettingsRepositoryImpl.java:857+`; mutator body/call-site search printed; session settings route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
