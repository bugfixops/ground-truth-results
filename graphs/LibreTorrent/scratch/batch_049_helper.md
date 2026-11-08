# Batch 49 helper report

Membership is exactly the 40 rows with `batch==49` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; that TSV is the sole membership source. Definitions and repository/migration callers are recorded in `scratch/batch_049_helper_printed.txt`. The source shows migration framework callbacks and repository entry points, but this review did not complete the routes from application entry points; uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `DatabaseMigration$RoomDatabaseMigration.<init>` | OPEN | — | Migration object is supplied to Room's migration builder; complete app startup path not traced. | `DatabaseMigration.java:120-136`; `AppDatabase.java:84` |
| `DatabaseMigration$RoomDatabaseMigration.addFastResume` | OPEN | — | Called by resume-data migration helper; full upgrade entry path not audited. | `DatabaseMigration.java:179-208,290-295` |
| `DatabaseMigration$RoomDatabaseMigration.advancedMigration` | OPEN | — | Called by migrate after schema transaction; complete framework upgrade route not verified. | `DatabaseMigration.java:138-177,179-183` |
| `DatabaseMigration$RoomDatabaseMigration.backupTorrent` | OPEN | — | Called during migration fallback handling; full upgrade route not established. | `DatabaseMigration.java:199-218,259-275` |
| `DatabaseMigration$RoomDatabaseMigration.copyFastResumeData` | OPEN | — | Called by advancedMigration; complete Room migration route not established. | `DatabaseMigration.java:179-183,185-227` |
| `DatabaseMigration$RoomDatabaseMigration.findTorrentDataDir` | OPEN | — | Called by copyFastResumeData; complete migration entry path not traced. | `DatabaseMigration.java:191-197,246-257` |
| `DatabaseMigration$RoomDatabaseMigration.getTorrentIdList` | OPEN | — | Called by copyFastResumeData; complete migration entry path not traced. | `DatabaseMigration.java:185-188,277-288` |
| `DatabaseMigration$RoomDatabaseMigration.migrate` | OPEN | — | Room framework callback is registered, but upgrade callback route is not verified here. | `DatabaseMigration.java:138-177`; `AppDatabase.java:84` |
| `DatabaseMigration$RoomDatabaseMigration.removeSessionFile` | OPEN | — | Called by advancedMigration; complete Room upgrade route not established. | `DatabaseMigration.java:179-183,229-236` |
| `DatabaseMigration$RoomDatabaseMigration.torrentDataExists` | OPEN | — | Called by copyFastResumeData; complete migration entry path not traced. | `DatabaseMigration.java:191-194,238-244` |
| `FeedRepositoryImpl.<clinit>` | OPEN | — | Class initialization occurs on repository use; full repository consumer entry route not traced. | `FeedRepositoryImpl.java:48-57`; `RepositoryHelper.java:52-56` |
| `FeedRepositoryImpl.<init>` | OPEN | — | Created by RepositoryHelper; complete caller lifecycle not established. | `FeedRepositoryImpl.java:59-63`; `RepositoryHelper.java:52-56` |
| `FeedRepositoryImpl.addFeed` | OPEN | — | Repository operation delegates to FeedDao; complete app caller route not audited. | `FeedRepositoryImpl.java:83-87`; FeedViewModel/AddFeedViewModel call paths |
| `FeedRepositoryImpl.addFeeds` | OPEN | — | Repository operation delegates to FeedDao; complete app caller route not audited. | `FeedRepositoryImpl.java:89-93`; `FeedViewModel` usage search |
| `FeedRepositoryImpl.addItems` | OPEN | — | Called by feed download worker; full scheduled-worker entry route not traced. | `FeedRepositoryImpl.java:167-171`; `FeedDownloaderWorker` usage search |
| `FeedRepositoryImpl.deleteFeed` | OPEN | — | Repository operation delegates to FeedDao; complete UI callback route not audited. | `FeedRepositoryImpl.java:101-105`; `FeedViewModel` usage search |
| `FeedRepositoryImpl.deleteFeeds` | OPEN | — | Repository operation delegates to FeedDao; complete UI callback route not audited. | `FeedRepositoryImpl.java:107-111`; usage search |
| `FeedRepositoryImpl.deleteItemsOlderThan` | OPEN | — | Used in feed retention logic; complete worker entry route not established. | `FeedRepositoryImpl.java:173-177`; `FeedFetcherWorker` usage search |
| `FeedRepositoryImpl.deserializeFeeds` | OPEN | — | Called from feed import workflow; complete activity-to-import route not traced. | `FeedRepositoryImpl.java:150-165`; `FeedViewModel` usage search |
| `FeedRepositoryImpl.findItemsExistingTitles` | OPEN | — | Called by feed processing to filter duplicates; complete worker entry route not established. | `FeedRepositoryImpl.java:215-219`; `FeedFetcherWorker` usage search |
| `FeedRepositoryImpl.getAllFeeds` | OPEN | — | Used by serializeAllFeeds; complete user export entry route not established. | `FeedRepositoryImpl.java:132-135,143-148` |
| `FeedRepositoryImpl.getAllFeedsSingle` | OPEN | — | Definition read; no complete app route established. | `FeedRepositoryImpl.java:137-141`; focused usage search |
| `FeedRepositoryImpl.getFeedById` | OPEN | — | Definition read; complete app route not established. | `FeedRepositoryImpl.java:113-117`; focused usage search |
| `FeedRepositoryImpl.getFeedByIdSingle` | OPEN | — | Definition read; complete app route not established. | `FeedRepositoryImpl.java:119-123`; focused usage search |
| `FeedRepositoryImpl.getFilterSeparator` | OPEN | — | Definition read; no complete app caller route established. | `FeedRepositoryImpl.java:77-81`; focused usage search |
| `FeedRepositoryImpl.getItemsByFeedIdSingle` | OPEN | — | Used by feed item UI model; full screen entry path not traced. | `FeedRepositoryImpl.java:203-207`; `FeedItemsViewModel` usage search |
| `FeedRepositoryImpl.getItemsById` | OPEN | — | Definition read; complete app caller route not established. | `FeedRepositoryImpl.java:221-225`; focused usage search |
| `FeedRepositoryImpl.getItemsIdByFeedId` | OPEN | — | Used in feed fetching logic; full worker route not established. | `FeedRepositoryImpl.java:209-213`; `FeedFetcherWorker` usage search |
| `FeedRepositoryImpl.markAsRead` | OPEN | — | Used by feed item UI; complete view/event entry path not established. | `FeedRepositoryImpl.java:179-183`; `FeedItemsViewModel` usage search |
| `FeedRepositoryImpl.markAsReadByFeedId` | OPEN | — | Used in feed UI/model flows; complete entry route not established. | `FeedRepositoryImpl.java:191-195`; usage search |
| `FeedRepositoryImpl.markAsUnread` | OPEN | — | Used by feed item UI; complete view/event entry path not established. | `FeedRepositoryImpl.java:185-189`; `FeedItemsViewModel` usage search |
| `FeedRepositoryImpl.observeAllFeeds` | OPEN | — | Used by feed ViewModel; complete activity lifecycle route not traced. | `FeedRepositoryImpl.java:125-129`; `FeedViewModel` usage search |
| `FeedRepositoryImpl.observeItemsByFeedId` | OPEN | — | Definition read; complete UI subscriber route not established. | `FeedRepositoryImpl.java:197-201`; focused usage search |
| `FeedRepositoryImpl.serializeAllFeeds` | OPEN | — | Export flow reads all feeds, but complete user export route not established. | `FeedRepositoryImpl.java:143-148`; `FeedActivity` usage search |
| `FeedRepositoryImpl.updateFeed` | OPEN | — | Repository operation delegates to FeedDao; complete UI callback route not audited. | `FeedRepositoryImpl.java:95-99`; `FeedViewModel` usage search |
| `FeedRepositoryImpl$1.<init>` | OPEN | — | Anonymous Gson TypeToken is instantiated during deserialization; complete import entry route not traced. | `FeedRepositoryImpl.java:150-165` |
| `TagRepositoryImpl.<init>` | OPEN | — | Created through RepositoryHelper; full application consumer lifecycle not traced. | `TagRepositoryImpl.java:31-36`; `RepositoryHelper.java:69-73` |
| `TagRepositoryImpl.delete` | OPEN | — | Called through main ViewModel tag removal; complete app entry route not audited. | `TagRepositoryImpl.java:48-51`; `MainViewModel.java:183-187` |
| `TagRepositoryImpl.getByName` | OPEN | — | Called by AddTagViewModel; complete activity/viewmodel entry route not established. | `TagRepositoryImpl.java:53-56`; `AddTagViewModel.java:65-71` |
| `TagRepositoryImpl.getByTorrentId` | OPEN | — | Called by TorrentEngine; complete UI/engine entry route not traced. | `TagRepositoryImpl.java:73-76`; `TorrentEngine.java:771,821` |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
