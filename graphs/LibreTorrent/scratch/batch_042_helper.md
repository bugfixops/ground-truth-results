# LibreTorrent batch 42 source audit

Membership is the exact 40 plan rows printed at the top of `batch_042_helper_printed.txt`. The evidence file contains the source bodies for `TorrentStream`, `TorrentStreamServer`, `SessionSettings`, and the target `SettingsRepositoryImpl` methods, plus an in-source caller search. I leave every row OPEN because this pass has not verified complete hand-authored paths from app entry points through the stream and preferences flows. Framework Parcelable dispatch and NanoHTTPD request dispatch also need their external callbacks accounted for before a route can be asserted. No method is labeled UNREACHABLE solely because a caller was not found.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `TorrentStream$1.newArray(int)TorrentStream[]` | OPEN | `TorrentStream.java:93-112`; Parcelable creator body printed, framework parcel dispatch route unresolved. |
| 2 | `TorrentStreamServer.<clinit>()V` | OPEN | `TorrentStreamServer.java:58+`; static initialization body printed, complete construction/use path unresolved. |
| 3 | `TorrentStreamServer.<init>(String,int)V` | OPEN | `TorrentStreamServer.java:51+`; constructor source printed, app stream-server creation route unresolved. |
| 4 | `TorrentStreamServer.handleTorrent(IHTTPSession)Response` | OPEN | `TorrentStreamServer.java:124+`; called through `serve`, NanoHTTPD request dispatch unresolved. |
| 5 | `TorrentStreamServer.makeStreamUrl(String,int,String,int)String` | OPEN | `TorrentStreamServer.java:93+`; implementation/call-site search printed, complete caller path unresolved. |
| 6 | `TorrentStreamServer.serve(IHTTPSession)Response` | OPEN | `TorrentStreamServer.java:111+`; override body printed, library HTTP dispatch unresolved. |
| 7 | `TorrentStreamServer.start(Context)V` | OPEN | `TorrentStreamServer.java:72+`; implementation/call sites printed, complete app stream action route unresolved. |
| 8 | `TorrentStreamServer.stop()V` | OPEN | `TorrentStreamServer.java:82+`; implementation/call sites printed, complete lifecycle route unresolved. |
| 9 | `TorrentStreamServer$DLNAFileType.<init>(String,String,String,String)V` | OPEN | Enum/source declaration printed in `TorrentStreamServer.java`; complete enum initialization/use path unresolved. |
| 10 | `TorrentStreamServer$DLNAFileType.setHeaders(Response)V` | OPEN | `TorrentStreamServer.java` enum method printed; complete HTTP response route unresolved. |
| 11 | `SessionSettings.<clinit>()V` | OPEN | `SessionSettings.java` static fields printed; app class-initialization route not traced. |
| 12 | `SessionSettings.<init>()V` | OPEN | `SessionSettings.java:118`; callers in settings/session code printed, full entry route unresolved. |
| 13 | `SessionSettings.<init>(SessionSettings)V` | OPEN | `SessionSettings.java:120+`; copy constructor and use sites printed, complete caller path unresolved. |
| 14 | `SessionSettings.getRandomRangePort()Pair` | OPEN | `SessionSettings.java:234+`; helper body and settings caller printed, settings entry route unresolved. |
| 15 | `SessionSettings$EncryptMode.<clinit>()V` | OPEN | `SessionSettings.java:166+`; enum constants printed, use/initialization path unresolved. |
| 16 | `SessionSettings$EncryptMode.<init>(String,int,int)V` | OPEN | `SessionSettings.java:166+`; enum declaration printed, complete enum initialization path unresolved. |
| 17 | `SessionSettings$EncryptMode.fromValue(int)EncryptMode` | OPEN | `SessionSettings.java:186+`; method body printed, settings read/use route unresolved. |
| 18 | `SessionSettings$EncryptMode.value()int` | OPEN | `SessionSettings.java:181+`; method body printed, complete settings route unresolved. |
| 19 | `SessionSettings$ProxyType.<clinit>()V` | OPEN | `SessionSettings.java:197+`; enum constants printed, use/initialization path unresolved. |
| 20 | `SessionSettings$ProxyType.<init>(String,int,int)V` | OPEN | `SessionSettings.java:197+`; enum declaration printed, complete enum initialization path unresolved. |
| 21 | `SessionSettings$ProxyType.fromValue(int)ProxyType` | OPEN | `SessionSettings.java:211+`; method body printed, settings read/use route unresolved. |
| 22 | `SessionSettings$ProxyType.value()int` | OPEN | `SessionSettings.java:223+`; method body printed, complete settings route unresolved. |
| 23 | `SettingsRepositoryImpl.<init>(Context)V` | OPEN | `SettingsRepositoryImpl.java:184+`; constructor and callers printed, full app construction route unresolved. |
| 24 | `SettingsRepositoryImpl.anonymousMode()Z` | OPEN | `SettingsRepositoryImpl.java:929+`; accessor and caller search printed, complete UI/settings route unresolved. |
| 25 | `SettingsRepositoryImpl.anonymousMode(boolean)V` | OPEN | `SettingsRepositoryImpl.java:935+`; mutator and caller search printed, complete UI/settings route unresolved. |
| 26 | `SettingsRepositoryImpl.applyProxy()Z` | OPEN | `SettingsRepositoryImpl.java:1085+`; accessor and caller search printed, full settings route unresolved. |
| 27 | `SettingsRepositoryImpl.applyProxy(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1091+`; mutator and caller search printed, full settings route unresolved. |
| 28 | `SettingsRepositoryImpl.askManageAllFilesPermission()Z` | OPEN | `SettingsRepositoryImpl.java:1397+`; accessor printed, permission-prompt route unresolved. |
| 29 | `SettingsRepositoryImpl.askManageAllFilesPermission(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1403+`; mutator printed, complete UI/settings route unresolved. |
| 30 | `SettingsRepositoryImpl.askNotificationPermission()Z` | OPEN | `SettingsRepositoryImpl.java:1425+`; accessor printed, permission-prompt route unresolved. |
| 31 | `SettingsRepositoryImpl.askNotificationPermission(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1431+`; mutator printed, complete UI/settings route unresolved. |
| 32 | `SettingsRepositoryImpl.autoManage()Z` | OPEN | `SettingsRepositoryImpl.java:981+`; accessor and caller search printed, complete settings route unresolved. |
| 33 | `SettingsRepositoryImpl.autoManage(boolean)V` | OPEN | `SettingsRepositoryImpl.java:987+`; mutator and caller search printed, complete settings route unresolved. |
| 34 | `SettingsRepositoryImpl.autoRefreshFeeds()Z` | OPEN | `SettingsRepositoryImpl.java:1189+`; accessor and caller search printed, complete feed/settings route unresolved. |
| 35 | `SettingsRepositoryImpl.autoRefreshFeeds(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1195+`; mutator and caller search printed, complete feed/settings route unresolved. |
| 36 | `SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming()Z` | OPEN | `SettingsRepositoryImpl.java:1228+`; accessor and caller search printed, complete feed/settings route unresolved. |
| 37 | `SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1234+`; mutator and caller search printed, complete feed/settings route unresolved. |
| 38 | `SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly()Z` | OPEN | `SettingsRepositoryImpl.java:1215+`; accessor and caller search printed, complete feed/settings route unresolved. |
| 39 | `SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly(boolean)V` | OPEN | `SettingsRepositoryImpl.java:1221+`; mutator and caller search printed, complete feed/settings route unresolved. |
| 40 | `SettingsRepositoryImpl.autostart()Z` | OPEN | `SettingsRepositoryImpl.java:409+`; accessor and caller search printed, complete preference/boot path unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
