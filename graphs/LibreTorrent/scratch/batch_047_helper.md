# Batch 47 helper report

Membership is exactly the 40 rows with `batch==47` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; that TSV is the sole membership source. Definitions and focused app-use evidence are in `scratch/batch_047_helper_printed.txt`. Some members are created or invoked in settings and sorting code, but this bounded review did not verify complete app-entry routes, so uncertain methods remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `SettingsRepositoryImpl.vibrationNotify()` | OPEN | — | Preference getter used by notifier/settings UI; complete entry route not established. | `SettingsRepositoryImpl.java:315-319`; `TorrentNotifier.java:286` |
| `SettingsRepositoryImpl.vibrationNotify(boolean)` | OPEN | — | Setter used by appearance UI; full callback route not established. | `SettingsRepositoryImpl.java:321-326`; usage search |
| `SettingsRepositoryImpl.watchDir()` | OPEN | — | Getter used by engine; full service/session entry route not traced. | `SettingsRepositoryImpl.java:772-776`; `TorrentEngine.java:1053,1582-1588` |
| `SettingsRepositoryImpl.watchDir(boolean)` | OPEN | — | Setter used by storage settings UI; complete callback route not established. | `SettingsRepositoryImpl.java:778-783`; usage search |
| `SettingsRepositoryImpl.watchDirDeleteFile()` | OPEN | — | Getter used by engine scan handling; full route not established. | `SettingsRepositoryImpl.java:798-802`; `TorrentEngine.java:1152` |
| `SettingsRepositoryImpl.watchDirDeleteFile(boolean)` | OPEN | — | Setter used by storage UI; full callback route not established. | `SettingsRepositoryImpl.java:804-809`; usage search |
| `SettingsRepositoryImpl$Default.<clinit>` | OPEN | — | Static defaults initialize on first class use; complete entry route not recorded. | `SettingsRepositoryImpl.java:41-168` |
| `SettingsRepositoryImpl$Default.dirToWatch(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:120-122`; `SettingsRepositoryImpl.java:786-789` |
| `SettingsRepositoryImpl$Default.encryptInConnectionsMode(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:88-90`; `SettingsRepositoryImpl.java:642-646` |
| `SettingsRepositoryImpl$Default.encryptOutConnectionsMode(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:92-94`; `SettingsRepositoryImpl.java:655-659` |
| `SettingsRepositoryImpl$Default.foregroundNotifySorting(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:61-63`; focused usage search |
| `SettingsRepositoryImpl$Default.foregroundNotifyStatusFilter(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:57-59`; focused usage search |
| `SettingsRepositoryImpl$Default.ledIndicatorColorNotify(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:53-55`; focused usage search |
| `SettingsRepositoryImpl$Default.moveAfterDownloadIn(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:108-110`; `SettingsRepositoryImpl.java:733-737` |
| `SettingsRepositoryImpl$Default.saveTorrentFilesIn(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:114-116`; focused usage search |
| `SettingsRepositoryImpl$Default.saveTorrentsIn(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:102-104`; focused usage search |
| `SettingsRepositoryImpl$Default.theme(Context)` | OPEN | — | Called as a preference fallback; complete entry route not established. | `SettingsRepositoryImpl.java:49-51`; focused usage search |
| `BaseSorting.<init>(String,Direction)` | OPEN | — | Called by TorrentSorting constructor; complete sorting entry route not traced. | `BaseSorting.java:52-56`; `TorrentSorting.java:113-116` |
| `BaseSorting.getColumnName` | OPEN | — | Used by comparator; complete UI/notification sorting route not traced. | `BaseSorting.java:63-66`; `TorrentSortingComparator.java:41-45` |
| `BaseSorting.getDirection` | OPEN | — | Used by comparator; complete sorting entry route not traced. | `BaseSorting.java:58-61`; `TorrentSortingComparator.java:41-45` |
| `BaseSorting.toString` | OPEN | — | No hand-written string conversion route established. | `BaseSorting.java:68-76`; focused usage search |
| `BaseSorting$Direction.<clinit>` | OPEN | — | Enum initialization is visible; complete sorting entry route not established. | `BaseSorting.java:26-40`; `Utils.java:804-834,892-924` |
| `TorrentSorting.<init>` | OPEN | — | Constructed by sorting utility methods; complete UI/notification entry route not traced. | `TorrentSorting.java:113-116`; `Utils.java:804-834,892-924` |
| `TorrentSorting$SortingColumns.<clinit>` | OPEN | — | Enum constants initialize on sorting use; complete entry route not established. | `TorrentSorting.java:26-101` |
| `TorrentSorting$SortingColumns.fromValue` | OPEN | — | Comparator calls this method; full caller route not traced. | `TorrentSorting.java:103-110`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$1.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:28-35` |
| `TorrentSorting$SortingColumns$1.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:28-35`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$2.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:36-46` |
| `TorrentSorting$SortingColumns$2.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:36-46`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$3.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:47-57` |
| `TorrentSorting$SortingColumns$3.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:47-57`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$4.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:58-68` |
| `TorrentSorting$SortingColumns$4.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:58-68`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$5.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:69-79` |
| `TorrentSorting$SortingColumns$5.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:69-79`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$6.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:80-90` |
| `TorrentSorting$SortingColumns$6.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:80-90`; `TorrentSortingComparator.java:41-45` |
| `TorrentSorting$SortingColumns$7.<init>` | OPEN | — | Anonymous enum-constant construction occurs during enum initialization; complete route not established. | `TorrentSorting.java:91-101` |
| `TorrentSorting$SortingColumns$7.compare` | OPEN | — | Comparator dispatches through SortingColumns; full app entry route not traced. | `TorrentSorting.java:91-101`; `TorrentSortingComparator.java:41-45` |
| `TorrentSortingComparator.<init>` | OPEN | — | Constructed by Utils sorting factories, but complete UI entry route is not recorded. | `TorrentSortingComparator.java:26-33`; `Utils.java:804-834,892-924` |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
