# Batch 45 helper report

Membership is exactly the 40 rows with `batch==45` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the plan TSV is the sole membership source. Definitions and caller search evidence are recorded in `scratch/batch_045_helper_printed.txt`. Preference accessors have local app callers, but this audit did not establish complete entry routes for every member, so uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `SettingsRepositoryImpl.maxConnectionsPerTorrent()` | OPEN | — | Getter used by engine/settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:863-867`; `TorrentEngine.java:1490` |
| `SettingsRepositoryImpl.maxConnectionsPerTorrent(int)` | OPEN | — | Setter used by limitations UI; full preference callback route not traced. | `SettingsRepositoryImpl.java:869-874`; usage search |
| `SettingsRepositoryImpl.maxDownloadSpeedLimit()` | OPEN | — | Getter used by engine/settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:824-828`; `TorrentEngine.java:1473-1476` |
| `SettingsRepositoryImpl.maxDownloadSpeedLimit(int)` | OPEN | — | Setter used by limitations UI; complete callback route not traced. | `SettingsRepositoryImpl.java:830-835`; usage search |
| `SettingsRepositoryImpl.maxLogSize()` | OPEN | — | Getter used by engine/log UI; complete entry route not established. | `SettingsRepositoryImpl.java:1318-1322`; `TorrentEngine.java:1644` |
| `SettingsRepositoryImpl.maxLogSize(int)` | OPEN | — | Setter used by log settings UI; full callback route not traced. | `SettingsRepositoryImpl.java:1324-1329`; usage search |
| `SettingsRepositoryImpl.maxUploadSpeedLimit()` | OPEN | — | Getter used by engine/settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:837-841`; `TorrentEngine.java:1478-1481` |
| `SettingsRepositoryImpl.maxUploadSpeedLimit(int)` | OPEN | — | Setter used by limitations UI; complete callback route not traced. | `SettingsRepositoryImpl.java:843-848`; usage search |
| `SettingsRepositoryImpl.maxUploadsPerTorrent()` | OPEN | — | Getter used by engine/settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:876-880`; `TorrentEngine.java:1492-1494` |
| `SettingsRepositoryImpl.maxUploadsPerTorrent(int)` | OPEN | — | Setter used by limitations UI; complete callback route not traced. | `SettingsRepositoryImpl.java:882-887`; usage search |
| `SettingsRepositoryImpl.moveAfterDownload()` | OPEN | — | Getter used by engine and storage UI; complete entry route not established. | `SettingsRepositoryImpl.java:720-724`; `TorrentEngine.java:1315` |
| `SettingsRepositoryImpl.moveAfterDownload(boolean)` | OPEN | — | Setter used by storage UI; complete preference callback route not traced. | `SettingsRepositoryImpl.java:726-731`; usage search |
| `SettingsRepositoryImpl.moveAfterDownloadIn()` | OPEN | — | Getter used by engine and storage UI; complete entry route not established. | `SettingsRepositoryImpl.java:733-737`; `TorrentEngine.java:1317` |
| `SettingsRepositoryImpl.moveAfterDownloadIn(String)` | OPEN | — | Setter used by storage UI; complete callback route not traced. | `SettingsRepositoryImpl.java:739-744`; usage search |
| `SettingsRepositoryImpl.notifySound()` | OPEN | — | Getter used by notifier and appearance UI; complete entry route not established. | `SettingsRepositoryImpl.java:263-267`; `TorrentNotifier.java:281-282` |
| `SettingsRepositoryImpl.notifySound(String)` | OPEN | — | Setter used by appearance UI; complete callback route not traced. | `SettingsRepositoryImpl.java:269-274`; usage search |
| `SettingsRepositoryImpl.observeSettingsChanged` | OPEN | — | Emits SharedPreferences callbacks; subscription/lifecycle entry route not fully traced. | `SettingsRepositoryImpl.java:194-209`; `TorrentEngine.java:239-241` |
| `SettingsRepositoryImpl.onlyCharging()` | OPEN | — | Getter used by engine power policy; complete entry route not established. | `SettingsRepositoryImpl.java:460-464`; `TorrentEngine.java:992,1027` |
| `SettingsRepositoryImpl.onlyCharging(boolean)` | OPEN | — | Setter used by behavior UI; complete callback route not traced. | `SettingsRepositoryImpl.java:466-471`; usage search |
| `SettingsRepositoryImpl.playSoundNotify()` | OPEN | — | Getter used by notifier and appearance UI; complete entry route not established. | `SettingsRepositoryImpl.java:289-293`; `TorrentNotifier.java:281` |
| `SettingsRepositoryImpl.playSoundNotify(boolean)` | OPEN | — | Setter used by appearance UI; complete callback route not traced. | `SettingsRepositoryImpl.java:295-300`; usage search |
| `SettingsRepositoryImpl.portRangeFirst()` | OPEN | — | Getter used by engine settings; complete entry route not established. | `SettingsRepositoryImpl.java:538-542`; `TorrentEngine.java:1236` |
| `SettingsRepositoryImpl.portRangeFirst(int)` | OPEN | — | Setter used by network settings UI; full callback route not traced. | `SettingsRepositoryImpl.java:544-549`; usage search |
| `SettingsRepositoryImpl.portRangeSecond()` | OPEN | — | Getter used by engine settings; complete entry route not established. | `SettingsRepositoryImpl.java:551-555`; `TorrentEngine.java:1237` |
| `SettingsRepositoryImpl.portRangeSecond(int)` | OPEN | — | Setter used by network settings UI; full callback route not traced. | `SettingsRepositoryImpl.java:557-562`; usage search |
| `SettingsRepositoryImpl.posixDiskIo()` | OPEN | — | Getter used by storage settings UI and session initialization; entry route not established. | `SettingsRepositoryImpl.java:811-815`; `StorageSettingsFragment.java:203` |
| `SettingsRepositoryImpl.posixDiskIo(boolean)` | OPEN | — | Setter used by storage UI; full callback route not traced. | `SettingsRepositoryImpl.java:817-822`; usage search |
| `SettingsRepositoryImpl.proxyAddress()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1006-1010`; `TorrentEngine.java:1098` |
| `SettingsRepositoryImpl.proxyAddress(String)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1012-1017`; usage search |
| `SettingsRepositoryImpl.proxyLogin()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1058-1062`; `TorrentEngine.java:1102` |
| `SettingsRepositoryImpl.proxyLogin(String)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1064-1069`; usage search |
| `SettingsRepositoryImpl.proxyPassword()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1071-1075`; `TorrentEngine.java:1103` |
| `SettingsRepositoryImpl.proxyPassword(String)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1077-1082`; usage search |
| `SettingsRepositoryImpl.proxyPeersToo()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1032-1036`; `TorrentEngine.java:1100` |
| `SettingsRepositoryImpl.proxyPeersToo(boolean)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1038-1043`; usage search |
| `SettingsRepositoryImpl.proxyPort()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1019-1023`; `TorrentEngine.java:1099` |
| `SettingsRepositoryImpl.proxyPort(int)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1025-1030`; usage search |
| `SettingsRepositoryImpl.proxyRequiresAuth()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:1045-1049`; `TorrentEngine.java:1101` |
| `SettingsRepositoryImpl.proxyRequiresAuth(boolean)` | OPEN | — | Setter used by proxy UI; full callback route not traced. | `SettingsRepositoryImpl.java:1051-1056`; usage search |
| `SettingsRepositoryImpl.proxyType()` | OPEN | — | Getter used by engine and proxy UI; complete entry route not established. | `SettingsRepositoryImpl.java:993-997`; `TorrentEngine.java:1097` |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
