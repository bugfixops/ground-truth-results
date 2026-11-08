# Batch 43 helper report

Membership is exactly the 40 rows with `batch==43` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the TSV is the sole membership source. Definitions and focused usage searches are recorded in `scratch/batch_043_helper_printed.txt`. The implementation clearly reads/writes preferences and some methods are referenced by UI/service code, but this audit did not establish complete entry routes for each method, so uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `SettingsRepositoryImpl.autostart()` | OPEN | — | Preference getter read; complete app-entry route not established. | `SettingsRepositoryImpl.java:408-412`; usage search |
| `SettingsRepositoryImpl.autostart(boolean)` | OPEN | — | Preference setter read; complete app-entry route not established. | `SettingsRepositoryImpl.java:414-419`; usage search |
| `SettingsRepositoryImpl.batteryControl()` | OPEN | — | Preference getter read; complete app-entry route not established. | `SettingsRepositoryImpl.java:473-477`; usage search |
| `SettingsRepositoryImpl.batteryControl(boolean)` | OPEN | — | Preference setter read; complete app-entry route not established. | `SettingsRepositoryImpl.java:479-484`; usage search |
| `SettingsRepositoryImpl.cpuDoNotSleep()` | OPEN | — | Preference getter used by service, but full service-entry route not audited. | `SettingsRepositoryImpl.java:447-451`; `TorrentService.java:129,267` |
| `SettingsRepositoryImpl.cpuDoNotSleep(boolean)` | OPEN | — | Preference setter; complete UI callback route not established. | `SettingsRepositoryImpl.java:453-458`; usage search |
| `SettingsRepositoryImpl.customBatteryControl()` | OPEN | — | Preference getter used in engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:486-490`; `TorrentEngine.java:990,1024` |
| `SettingsRepositoryImpl.customBatteryControl(boolean)` | OPEN | — | Preference setter; complete UI callback route not established. | `SettingsRepositoryImpl.java:492-497`; usage search |
| `SettingsRepositoryImpl.customBatteryControlValue()` | OPEN | — | Preference getter used in engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:499-503`; `TorrentEngine.java:1026` |
| `SettingsRepositoryImpl.customBatteryControlValue(int)` | OPEN | — | Preference setter; complete UI callback route not established. | `SettingsRepositoryImpl.java:505-510`; usage search |
| `SettingsRepositoryImpl.defaultTrackersList()` | OPEN | — | Getter used by engine and settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:954-958`; `TorrentEngine.java:1648` |
| `SettingsRepositoryImpl.defaultTrackersList(String)` | OPEN | — | Setter used by settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:960-965`; usage search |
| `SettingsRepositoryImpl.dirToWatch()` | OPEN | — | Getter used in engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:785-789`; `TorrentEngine.java:1117` |
| `SettingsRepositoryImpl.dirToWatch(String)` | OPEN | — | Setter used by storage settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:791-796`; usage search |
| `SettingsRepositoryImpl.enableDht()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:564-568`; `TorrentEngine.java:1512` |
| `SettingsRepositoryImpl.enableDht(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:570-575`; usage search |
| `SettingsRepositoryImpl.enableIpFiltering()` | OPEN | — | Getter used by engine; complete app-entry route not traced. | `SettingsRepositoryImpl.java:668-672`; `TorrentEngine.java:1047,1555` |
| `SettingsRepositoryImpl.enableIpFiltering(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:674-679`; usage search |
| `SettingsRepositoryImpl.enableLsd()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:577-581`; `TorrentEngine.java:1517` |
| `SettingsRepositoryImpl.enableLsd(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:583-588`; usage search |
| `SettingsRepositoryImpl.enableNatPmp()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:616-620`; `TorrentEngine.java:1532` |
| `SettingsRepositoryImpl.enableNatPmp(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:622-627`; usage search |
| `SettingsRepositoryImpl.enableRoaming()` | OPEN | — | Getter used by engine/utility code; complete entry route not traced. | `SettingsRepositoryImpl.java:525-529`; `TorrentEngine.java:1011,1029` |
| `SettingsRepositoryImpl.enableRoaming(boolean)` | OPEN | — | Setter used by behavior settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:531-536`; usage search |
| `SettingsRepositoryImpl.enableSchedulingShutdown()` | OPEN | — | Getter used in receiver and UI flows; complete entry route not audited. | `SettingsRepositoryImpl.java:1110-1114`; usage search |
| `SettingsRepositoryImpl.enableSchedulingShutdown(boolean)` | OPEN | — | Setter used in receiver and UI flows; complete entry route not audited. | `SettingsRepositoryImpl.java:1116-1121`; usage search |
| `SettingsRepositoryImpl.enableSchedulingStart()` | OPEN | — | Getter used in receiver and UI flows; complete entry route not audited. | `SettingsRepositoryImpl.java:1097-1101`; usage search |
| `SettingsRepositoryImpl.enableSchedulingStart(boolean)` | OPEN | — | Setter used in receiver and UI flows; complete entry route not audited. | `SettingsRepositoryImpl.java:1103-1108`; usage search |
| `SettingsRepositoryImpl.enableStreaming()` | OPEN | — | Getter used by engine and settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:1266-1270`; `TorrentEngine.java:1056,1593` |
| `SettingsRepositoryImpl.enableStreaming(boolean)` | OPEN | — | Setter used by settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:1272-1277`; usage search |
| `SettingsRepositoryImpl.enableUpnp()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:603-607`; `TorrentEngine.java:1527` |
| `SettingsRepositoryImpl.enableUpnp(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:609-614`; usage search |
| `SettingsRepositoryImpl.enableUtp()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:590-594`; `TorrentEngine.java:1522` |
| `SettingsRepositoryImpl.enableUtp(boolean)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:596-601`; usage search |
| `SettingsRepositoryImpl.encryptInConnectionsMode()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:642-646`; `TorrentEngine.java:1109` |
| `SettingsRepositoryImpl.encryptInConnectionsMode(int)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:648-653`; usage search |
| `SettingsRepositoryImpl.encryptOutConnectionsMode()` | OPEN | — | Getter used by engine settings; complete entry route not traced. | `SettingsRepositoryImpl.java:655-659`; `TorrentEngine.java:1113` |
| `SettingsRepositoryImpl.encryptOutConnectionsMode(int)` | OPEN | — | Setter used by network settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:661-666`; usage search |
| `SettingsRepositoryImpl.feedItemKeepTime()` | OPEN | — | Getter used by FeedFetcherWorker and settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:1175-1179`; usage search |
| `SettingsRepositoryImpl.feedRemoveDuplicates()` | OPEN | — | Getter used by FeedFetcherWorker and settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:1253-1257`; usage search |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
