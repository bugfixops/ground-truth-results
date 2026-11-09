# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b049 — converter C07 delivery.
# Base: audited A3 output helper/a3-g10/parts/b049.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# clone/graphs/LibreTorrent/scratch/merge-ready/batch49-merge-ready.md).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/49/ (see REPORT-b049.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Batch 49 part (RoomDatabaseMigration chain, FeedRepositoryImpl, TagRepositoryImpl).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b049_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# RoomDatabaseMigration chain (STATE gate: pre-existing v4 database; row 1 is fresh-install-safe).
e('DatabaseMigration.getMigrations', 'DatabaseMigration$RoomDatabaseMigration.<init>', 'CALL', 'Migration list construction creates the 4-to-5 migration', cls='explicit', evidence='SRC DatabaseMigration.java:49; SRC DatabaseMigration.java:131-136')
e('DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'DatabaseMigration$RoomDatabaseMigration.addFastResume', 'CALL', 'Fast-resume copy writes each restored fast-resume row', cls='explicit', evidence='SRC DatabaseMigration.java:206-208; SRC DatabaseMigration.java:290-295')
e('DatabaseMigration$RoomDatabaseMigration.migrate', 'DatabaseMigration$RoomDatabaseMigration.advancedMigration', 'CALL', 'Migration runs its advanced step after creating and copying tables', cls='explicit', evidence='SRC DatabaseMigration.java:172; SRC DatabaseMigration.java:179-183')
e('DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'DatabaseMigration$RoomDatabaseMigration.backupTorrent', 'CALL', 'Fast-resume copy backs up a torrent without a fast-resume file', cls='explicit', evidence='SRC DatabaseMigration.java:202,211; SRC DatabaseMigration.java:259-275')
e('DatabaseMigration$RoomDatabaseMigration.advancedMigration', 'DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'CALL', 'Advanced migration copies fast-resume data after removing the session file', cls='explicit', evidence='SRC DatabaseMigration.java:182; SRC DatabaseMigration.java:185-227')
e('DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'DatabaseMigration$RoomDatabaseMigration.findTorrentDataDir', 'CALL', 'Fast-resume copy locates each torrent data directory', cls='explicit', evidence='SRC DatabaseMigration.java:195; SRC DatabaseMigration.java:246-257')
e('DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'DatabaseMigration$RoomDatabaseMigration.getTorrentIdList', 'CALL', 'Fast-resume copy lists the old torrent ids first', cls='explicit', evidence='SRC DatabaseMigration.java:187; SRC DatabaseMigration.java:277-288')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$RoomDatabaseMigration.migrate', 'CALL', 'Room invokes the registered Migration on version step 4 to 5', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: pre-existing v4 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,49; SRC AppDatabase.java:81-85')
e('DatabaseMigration$RoomDatabaseMigration.advancedMigration', 'DatabaseMigration$RoomDatabaseMigration.removeSessionFile', 'CALL', 'Advanced migration removes the session file first', cls='explicit', evidence='SRC DatabaseMigration.java:181; SRC DatabaseMigration.java:229-236')
e('DatabaseMigration$RoomDatabaseMigration.copyFastResumeData', 'DatabaseMigration$RoomDatabaseMigration.torrentDataExists', 'CALL', 'Fast-resume copy checks each torrent data directory exists', cls='explicit', evidence='SRC DatabaseMigration.java:192; SRC DatabaseMigration.java:238-244')

# FeedRepositoryImpl construction and class init.
e('RepositoryHelper.getFeedRepository', 'FeedRepositoryImpl.<clinit>', 'FRAMEWORK', 'First feed-repository construction initialises the class constants', cls='non_standard', via='JVM class initialization on first active use of FeedRepositoryImpl', evidence='INFERRED JVM dispatch; SRC RepositoryHelper.java:52-56; SRC FeedRepositoryImpl.java:50-54; SRC ui/feeds/FeedActivity.java:271-272,286')
e('RepositoryHelper.getFeedRepository', 'FeedRepositoryImpl.<init>', 'CALL', 'Feed repository getter constructs the implementation', cls='explicit', evidence='SRC RepositoryHelper.java:55-56; SRC FeedRepositoryImpl.java:59-63')

# FeedRepositoryImpl methods from their printed ViewModel/Worker callers.
e('AddFeedViewModel.applyParams', 'FeedRepositoryImpl.addFeed', 'CALL', 'Add-feed apply writes the new channel', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:189; SRC FeedRepositoryImpl.java:84-87')
e('FeedViewModel.restoreFeedsSync', 'FeedRepositoryImpl.addFeeds', 'CALL', 'Feed restore writes the imported channels', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:144; SRC FeedRepositoryImpl.java:90-93')
e('FeedFetcherWorker.fetchChannel', 'FeedRepositoryImpl.addItems', 'CALL', 'Feed fetch stores the fetched items', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:172; SRC FeedRepositoryImpl.java:168-171')
e('AddFeedViewModel.deleteChannel', 'FeedRepositoryImpl.deleteFeed', 'CALL', 'Feed delete removes the channel', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:133; SRC FeedRepositoryImpl.java:102-105')
e('FeedViewModel.deleteFeeds', 'FeedRepositoryImpl.deleteFeeds', 'CALL', 'Feed list delete removes the selected channels', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:87; SRC FeedRepositoryImpl.java:108-111')
e('FeedFetcherWorker.deleteOldItems', 'FeedRepositoryImpl.deleteItemsOlderThan', 'CALL', 'Feed fetch prunes items older than the keep border', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:209; SRC FeedRepositoryImpl.java:174-177')
e('FeedViewModel.restoreFeedsSync', 'FeedRepositoryImpl.deserializeFeeds', 'CALL', 'Feed restore parses the imported file', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:142; SRC FeedRepositoryImpl.java:151-165')
e('FeedFetcherWorker.filterItemDuplicates', 'FeedRepositoryImpl.findItemsExistingTitles', 'CALL', 'Feed fetch filters titles already stored', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:202; SRC FeedRepositoryImpl.java:216-219')
e('FeedFetcherWorker.doWork', 'FeedRepositoryImpl.getAllFeeds', 'CALL', 'Feed fetch worker reads all channels', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:100; SRC FeedRepositoryImpl.java:132-135')
e('FeedViewModel.getAllFeedsSingle', 'FeedRepositoryImpl.getAllFeedsSingle', 'CALL', 'Feed screen reads all channels as a single', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:77; SRC FeedRepositoryImpl.java:138-141')
e('AddFeedViewModel.deleteChannel', 'FeedRepositoryImpl.getFeedById', 'CALL', 'Feed delete loads the channel first', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:131; SRC FeedRepositoryImpl.java:114-117')
e('AddFeedViewModel.fetchParams', 'FeedRepositoryImpl.getFeedByIdSingle', 'CALL', 'Feed params fetch loads the channel as a single', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:151; SRC FeedRepositoryImpl.java:120-123')
e('FeedFetcherWorker.isMatch', 'FeedRepositoryImpl.getFilterSeparator', 'CALL', 'Feed filter matching splits on the repository separator', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:261; SRC FeedRepositoryImpl.java:78-81')
e('FeedItemsViewModel.getItemsByFeedIdSingle', 'FeedRepositoryImpl.getItemsByFeedIdSingle', 'CALL', 'Feed items screen reads one feed items as a single', cls='explicit', evidence='SRC ui/feeditems/FeedItemsViewModel.java:89; SRC FeedRepositoryImpl.java:204-207')
e('FeedDownloaderWorker.fetchTorrents', 'FeedRepositoryImpl.getItemsById', 'CALL', 'Feed downloader loads items by id', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:100; SRC FeedRepositoryImpl.java:222-224')
e('FeedFetcherWorker.filterItems', 'FeedRepositoryImpl.getItemsIdByFeedId', 'CALL', 'Feed fetch lists stored item ids for the feed', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:191; SRC FeedRepositoryImpl.java:210-213')
e('FeedFetcherWorker.sendFetchedItems', 'FeedRepositoryImpl.markAsRead', 'CALL', 'Fetched items are marked read on send', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:221; SRC FeedRepositoryImpl.java:180-183')
e('FeedItemsViewModel.markAllAsRead', 'FeedRepositoryImpl.markAsReadByFeedId', 'CALL', 'Mark-all-read marks the feed items read', cls='explicit', evidence='SRC ui/feeditems/FeedItemsViewModel.java:118; SRC FeedRepositoryImpl.java:192-195')
e('FeedItemsViewModel.markAsUnread', 'FeedRepositoryImpl.markAsUnread', 'CALL', 'Mark-unread clears the item read flag', cls='explicit', evidence='SRC ui/feeditems/FeedItemsViewModel.java:131; SRC FeedRepositoryImpl.java:186-189')
e('FeedViewModel.observerAllFeeds', 'FeedRepositoryImpl.observeAllFeeds', 'CALL', 'Feed screen observes all channels', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:82; SRC FeedRepositoryImpl.java:126-129')
e('FeedItemsViewModel.observeItemsByFeedId', 'FeedRepositoryImpl.observeItemsByFeedId', 'CALL', 'Feed items screen observes one feed items', cls='explicit', evidence='SRC ui/feeditems/FeedItemsViewModel.java:84; SRC FeedRepositoryImpl.java:198-201')
e('FeedViewModel.saveFeedsSync', 'FeedRepositoryImpl.serializeAllFeeds', 'CALL', 'Feed save writes all channels to file', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:137; SRC FeedRepositoryImpl.java:144-148')
e('AddFeedViewModel.applyParams', 'FeedRepositoryImpl.updateFeed', 'CALL', 'Add-feed apply updates the channel', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:190; SRC FeedRepositoryImpl.java:96-99')
e('FeedRepositoryImpl.deserializeFeeds', 'FeedRepositoryImpl$1.<init>', 'CALL', 'Feed deserialisation creates the anonymous TypeToken subclass', cls='explicit', evidence='SRC FeedRepositoryImpl.java:160; SRC FeedRepositoryImpl.java:151-165')

# TagRepositoryImpl construction and methods.
e('RepositoryHelper.getTagRepository', 'TagRepositoryImpl.<init>', 'CALL', 'Tag repository getter constructs the implementation', cls='explicit', evidence='SRC RepositoryHelper.java:69-72; SRC TagRepositoryImpl.java:34-36')
e('MainViewModel.deleteTag', 'TagRepositoryImpl.delete', 'CALL', 'Main screen tag delete removes the tag', cls='explicit', evidence='SRC ui/main/MainViewModel.java:187; SRC TagRepositoryImpl.java:49-51')
# Review of 6d94e9c4 item 2: AddTagViewModel.setRandomColor -> TagRepositoryImpl.getByName removed. Line 65 is in the
# Completable.fromCallable lambda of saveTag (AddTagViewModel.java:55-75, read); the bytecode edge
# AddTagViewModel.lambda$saveTag$0 -> TagRepositoryImpl.getByName is the real step.
e('TorrentEngine.makeInfoSync', 'TagRepositoryImpl.getByTorrentId', 'CALL', 'Torrent info build reads the torrent tags', cls='explicit', evidence='SRC TorrentEngine.java:771; SRC TagRepositoryImpl.java:74-76')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan — no REACHABLE method in this batch calls an
# UNREACHABLE method in bytecode, and this batch has no UNREACHABLE
# methods of its own. See REPORT.md for the full recomputation.
SUPPRESS.update(set())
