# LibreTorrent batch 42 source audit

The batch plan contains **40 rows**. The helper report has only 38 rows, so I reconciled membership against `scratch/batch_042_plan.txt` and independently checked the two omitted preference setters in `SettingsRepositoryImpl.java` and `FeedSettingsFragment.java`. They are also OPEN because their settings-screen call paths have not been represented with hand-authored entry routes. The helper's printed source excerpts and caller searches are in `scratch/batch_042_helper_printed.txt`.

All targets remain OPEN: the stream-server methods depend on HTTP/NanoHTTPD dispatch; settings methods have local UI or session callers but no complete hand-authored route from app entry. Missing call-site matches are not used to infer unreachability.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentStream$1.newArray(int)` | OPEN | Creator at `TorrentStream.java:93-112`; framework Parcel dispatch unresolved. |
| 2 | `TorrentStreamServer.<clinit>` | OPEN | Static initialization/use path not complete. |
| 3 | `TorrentStreamServer.<init>(String,int)` | OPEN | Stream server construction route unresolved. |
| 4 | `TorrentStreamServer.handleTorrent(IHTTPSession)` | OPEN | Called via serve; NanoHTTPD request dispatch unresolved. |
| 5 | `TorrentStreamServer.makeStreamUrl(String,int,String,int)` | OPEN | Caller path incomplete. |
| 6 | `TorrentStreamServer.serve(IHTTPSession)` | OPEN | Override body printed; HTTP library dispatch unresolved. |
| 7 | `TorrentStreamServer.start(Context)` | OPEN | App stream action route incomplete. |
| 8 | `TorrentStreamServer.stop()` | OPEN | Lifecycle route incomplete. |
| 9 | `TorrentStreamServer$DLNAFileType.<init>(String,String,String,String)` | OPEN | Enum initialization/use path incomplete. |
| 10 | `TorrentStreamServer$DLNAFileType.setHeaders(Response)` | OPEN | HTTP response route incomplete. |
| 11 | `SessionSettings.<clinit>` | OPEN | App class-init route not traced. |
| 12 | `SessionSettings.<init>()` | OPEN | Settings/session callers printed; entry route unresolved. |
| 13 | `SessionSettings.<init>(SessionSettings)` | OPEN | Copy constructor callers; full route unresolved. |
| 14 | `SessionSettings.getRandomRangePort()` | OPEN | Settings caller shown; entry route unresolved. |
| 15 | `SessionSettings$EncryptMode.<clinit>` | OPEN | Enum use/init route unresolved. |
| 16 | `SessionSettings$EncryptMode.<init>(String,int,int)` | OPEN | Enum initialization route unresolved. |
| 17 | `SessionSettings$EncryptMode.fromValue(int)` | OPEN | Settings read/use route unresolved. |
| 18 | `SessionSettings$EncryptMode.value()` | OPEN | Complete settings route unresolved. |
| 19 | `SessionSettings$ProxyType.<clinit>` | OPEN | Enum use/init route unresolved. |
| 20 | `SessionSettings$ProxyType.<init>(String,int,int)` | OPEN | Enum initialization route unresolved. |
| 21 | `SessionSettings$ProxyType.fromValue(int)` | OPEN | Settings read/use route unresolved. |
| 22 | `SessionSettings$ProxyType.value()` | OPEN | Complete settings route unresolved. |
| 23 | `SettingsRepositoryImpl.<init>(Context)` | OPEN | Constructor callers printed; app construction route unresolved. |
| 24 | `SettingsRepositoryImpl.anonymousMode()` | OPEN | Accessor callers printed; settings UI route unresolved. |
| 25 | `SettingsRepositoryImpl.anonymousMode(boolean)` | OPEN | Mutator callers printed; settings UI route unresolved. |
| 26 | `SettingsRepositoryImpl.applyProxy()` | OPEN | Accessor route through settings unresolved. |
| 27 | `SettingsRepositoryImpl.applyProxy(boolean)` | OPEN | Mutator route through settings unresolved. |
| 28 | `SettingsRepositoryImpl.askManageAllFilesPermission()` | OPEN | Permission prompt route unresolved. |
| 29 | `SettingsRepositoryImpl.askManageAllFilesPermission(boolean)` | OPEN | UI/settings route unresolved. |
| 30 | `SettingsRepositoryImpl.askNotificationPermission()` | OPEN | Permission prompt route unresolved. |
| 31 | `SettingsRepositoryImpl.askNotificationPermission(boolean)` | OPEN | UI/settings route unresolved. |
| 32 | `SettingsRepositoryImpl.autoManage()` | OPEN | Settings caller route unresolved. |
| 33 | `SettingsRepositoryImpl.autoManage(boolean)` | OPEN | Settings caller route unresolved. |
| 34 | `SettingsRepositoryImpl.autoRefreshFeeds()` | OPEN | Feed/settings route unresolved. |
| 35 | `SettingsRepositoryImpl.autoRefreshFeeds(boolean)` | OPEN | Feed/settings route unresolved. |
| 36 | `SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming()` | OPEN | `FeedSettingsFragment` reads it; complete settings-screen entry path not authored. |
| 37 | `SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming(boolean)` | OPEN | Called from `FeedSettingsFragment.java:152`; full settings-screen route not authored. |
| 38 | `SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly()` | OPEN | `FeedSettingsFragment` reads it; complete settings-screen entry path not authored. |
| 39 | `SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly(boolean)` | OPEN | Called from `FeedSettingsFragment.java:149`; full settings-screen route not authored. |
| 40 | `SettingsRepositoryImpl.autostart()` | OPEN | Preference/boot route not complete. |

Totals: 40 plan rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
