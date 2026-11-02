# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b051 — converter C07 delivery.
# Base: audited A3 output helper/a3-g10/parts/b051.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# clone/graphs/LibreTorrent/scratch/merge-ready/batch51-merge-ready.md).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/51/ (see REPORT-b051.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Batch 51 part (FeedDao_Impl methods, bind adapters $1-$4, statements $5-$7,
# Callables $10-$12, Callable $8 <init>). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b051_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated Room source (FeedDao_Impl, FeedDao_Impl$N) is absent from
# final_java_only (generated at build time), so every _Impl edge below is
# INFERRED generated dispatch, never SOURCE. The $N assignment below is
# pinned by bytecode, not by the batch file's SET guess: adapter/statement
# SQL strings read from the generated class files, and Callable creation
# sites read from FeedDao_Impl method bodies (NEW in <init> / Rx method).
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# FeedDao_Impl methods through FeedRepositoryImpl (virtual dispatch to the Impl override).
e('FeedRepositoryImpl.getFeedById', 'FeedDao_Impl.getFeedById', 'CALL', 'Feed read by id goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:114-117; SRC FeedDao.java:67')
e('FeedRepositoryImpl.getFeedByIdSingle', 'FeedDao_Impl.getFeedByIdSingle', 'CALL', 'Feed single read by id goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:120-123; SRC FeedDao.java:70')
e('FeedRepositoryImpl.getItemsByFeedIdSingle', 'FeedDao_Impl.getItemsByFeedIdSingle', 'CALL', 'Feed items single read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:204-207; SRC FeedDao.java:100')
e('FeedRepositoryImpl.getItemsById', 'FeedDao_Impl.getItemsById', 'CALL', 'Feed items read by id goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:222-224; SRC FeedDao.java:109')
e('FeedRepositoryImpl.getItemsIdByFeedId', 'FeedDao_Impl.getItemsIdByFeedId', 'CALL', 'Feed item ids read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:210-213; SRC FeedDao.java:103')
e('AppDatabase_Impl.getRequiredTypeConverters', 'FeedDao_Impl.getRequiredConverters', 'CALL', 'Room generated converter validation aggregates each DAO converters list at database build', cls='non_standard', via='Room generated converter validation aggregates each DAO converters list at database build', evidence='INFERRED Room dispatch; SRC AppDatabase.java:53,81-87')
e('FeedRepositoryImpl.markAsRead', 'FeedDao_Impl.markAsRead', 'CALL', 'Mark-read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:180-183; SRC FeedDao.java:88')
e('FeedRepositoryImpl.markAsReadByFeedId', 'FeedDao_Impl.markAsReadByFeedId', 'CALL', 'Mark-read-by-feed goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:192-195; SRC FeedDao.java:94')
e('FeedRepositoryImpl.markAsUnread', 'FeedDao_Impl.markAsUnread', 'CALL', 'Mark-unread goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:186-189; SRC FeedDao.java:91')
e('FeedRepositoryImpl.observeAllFeeds', 'FeedDao_Impl.observeAllFeeds', 'CALL', 'Feed observation goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:126-129; SRC FeedDao.java:73')
e('FeedRepositoryImpl.observeItemsByFeedId', 'FeedDao_Impl.observeItemsByFeedId', 'CALL', 'Feed items observation goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:198-201; SRC FeedDao.java:97')
e('FeedRepositoryImpl.updateFeed', 'FeedDao_Impl.updateFeed', 'CALL', 'Feed update goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:96-99; SRC FeedDao.java:58')

# Bind adapter $1: INSERT INTO FeedChannel (serves addFeed and addFeeds).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$1.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO FeedChannel)', evidence='INFERRED Room dispatch; SRC FeedDao.java:52,55; SRC FeedRepositoryImpl.java:86,92')
e('FeedDao_Impl.addFeed', 'FeedDao_Impl$1.bind', 'CALL', 'Feed insert binds the channel row through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert (serves addFeed and addFeeds)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:86,92; SRC FeedDao.java:52,55')
e('FeedDao_Impl$1.<init>', 'FeedDao_Impl$1.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:52,55')

# Callable $10: created in getAllFeedsSingle (bytecode: NEW in getAllFeedsSingle).
e('FeedDao_Impl.getAllFeedsSingle', 'FeedDao_Impl$10.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in getAllFeedsSingle)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:140; SRC FeedDao.java:79')
e('FeedDao_Impl.getAllFeedsSingle', 'FeedDao_Impl$10.call', 'CALL', 'Subscription runs the Callable that reads the feed list', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:140; SRC FeedDao.java:79')
e('FeedDao_Impl$10.<init>', 'FeedDao_Impl$10.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC FeedRepositoryImpl.java:140; SRC FeedDao.java:79')

# Callable $11: created in observeItemsByFeedId (bytecode: NEW in observeItemsByFeedId).
e('FeedDao_Impl.observeItemsByFeedId', 'FeedDao_Impl$11.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in observeItemsByFeedId)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:200; SRC FeedDao.java:97')
e('FeedDao_Impl.observeItemsByFeedId', 'FeedDao_Impl$11.call', 'CALL', 'Subscription runs the Callable that reads the feed items', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:200; SRC FeedDao.java:97')
e('FeedDao_Impl$11.<init>', 'FeedDao_Impl$11.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC FeedRepositoryImpl.java:200; SRC FeedDao.java:97')

# Callable $12: created in getItemsByFeedIdSingle (bytecode: NEW in getItemsByFeedIdSingle).
e('FeedDao_Impl.getItemsByFeedIdSingle', 'FeedDao_Impl$12.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in getItemsByFeedIdSingle)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:206; SRC FeedDao.java:100')
e('FeedDao_Impl.getItemsByFeedIdSingle', 'FeedDao_Impl$12.call', 'CALL', 'Subscription runs the Callable that reads the feed items', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:206; SRC FeedDao.java:100')
e('FeedDao_Impl$12.<init>', 'FeedDao_Impl$12.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC FeedRepositoryImpl.java:206; SRC FeedDao.java:100')

# Bind adapter $2: INSERT INTO FeedItem (serves addItems).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$2.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO FeedItem)', evidence='INFERRED Room dispatch; SRC FeedDao.java:82; SRC FeedRepositoryImpl.java:170')
e('FeedDao_Impl.addItems', 'FeedDao_Impl$2.bind', 'CALL', 'Feed items insert binds the item row through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:170; SRC FeedDao.java:82')
e('FeedDao_Impl$2.<init>', 'FeedDao_Impl$2.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:82')

# Bind adapter $3: DELETE FROM FeedChannel (serves deleteFeed and deleteFeeds).
# Bytecode pin: $3 SQL is DELETE, $4 SQL is UPDATE — the batch file's SET
# guess had $3/$4 the other way round; labels are unaffected.
e('FeedDao_Impl.<init>', 'FeedDao_Impl$3.<init>', 'CALL', 'Room creates the deletion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the deletion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM FeedChannel)', evidence='INFERRED Room dispatch; SRC FeedDao.java:61,64; SRC FeedRepositoryImpl.java:104,110')
e('FeedDao_Impl.deleteFeed', 'FeedDao_Impl$3.bind', 'CALL', 'Feed delete binds the channel row through the adapter', cls='non_standard', via='Room deletion-adapter template dispatch binds the entity on delete (serves deleteFeed and deleteFeeds)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:104,110; SRC FeedDao.java:61,64')
e('FeedDao_Impl$3.<init>', 'FeedDao_Impl$3.createQuery', 'CALL', 'Adapter creation builds its DELETE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:61,64')

# Bind adapter $4: UPDATE FeedChannel (serves updateFeed).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$4.<init>', 'CALL', 'Room creates the update adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the update adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL UPDATE FeedChannel)', evidence='INFERRED Room dispatch; SRC FeedDao.java:58; SRC FeedRepositoryImpl.java:98')
e('FeedDao_Impl.updateFeed', 'FeedDao_Impl$4.bind', 'CALL', 'Feed update binds the channel row through the adapter', cls='non_standard', via='Room update-adapter template dispatch binds the entity on update', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:98; SRC FeedDao.java:58')
e('FeedDao_Impl$4.<init>', 'FeedDao_Impl$4.createQuery', 'CALL', 'Adapter creation builds its UPDATE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:58')

# Statement $5: DELETE FROM FeedItem WHERE fetchDate < ? (serves deleteItemsOlderThan).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$5.<init>', 'CALL', 'Room creates the shared statement in the DAO Impl constructor', cls='non_standard', via='Room creates the shared statement in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM FeedItem WHERE fetchDate < ?)', evidence='INFERRED Room dispatch; SRC FeedDao.java:85; SRC FeedRepositoryImpl.java:176')
e('FeedDao_Impl$5.<init>', 'FeedDao_Impl$5.createQuery', 'CALL', 'Statement creation builds its DELETE statement', cls='non_standard', via='Room statement superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:85')

# Statement $6: UPDATE FeedItem SET read = 1 WHERE id = ? (serves markAsRead).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$6.<init>', 'CALL', 'Room creates the shared statement in the DAO Impl constructor', cls='non_standard', via='Room creates the shared statement in the DAO Impl constructor (bytecode: NEW in <init>; SQL UPDATE FeedItem SET read = 1)', evidence='INFERRED Room dispatch; SRC FeedDao.java:88; SRC FeedRepositoryImpl.java:182')
e('FeedDao_Impl$6.<init>', 'FeedDao_Impl$6.createQuery', 'CALL', 'Statement creation builds its UPDATE statement', cls='non_standard', via='Room statement superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:88')

# Statement $7: UPDATE FeedItem SET read = 0 WHERE id = ? (serves markAsUnread).
e('FeedDao_Impl.<init>', 'FeedDao_Impl$7.<init>', 'CALL', 'Room creates the shared statement in the DAO Impl constructor', cls='non_standard', via='Room creates the shared statement in the DAO Impl constructor (bytecode: NEW in <init>; SQL UPDATE FeedItem SET read = 0)', evidence='INFERRED Room dispatch; SRC FeedDao.java:91; SRC FeedRepositoryImpl.java:188')
e('FeedDao_Impl$7.<init>', 'FeedDao_Impl$7.createQuery', 'CALL', 'Statement creation builds its UPDATE statement', cls='non_standard', via='Room statement superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FeedDao.java:91')

# Callable $8 <init>: created in getFeedByIdSingle (bytecode: NEW in
# getFeedByIdSingle; pinned: the only Rx method returning a single FeedChannel).
e('FeedDao_Impl.getFeedByIdSingle', 'FeedDao_Impl$8.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in getFeedByIdSingle; pinned: only Rx method returning a single FeedChannel)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:122; SRC FeedDao.java:70')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan — no REACHABLE method in this batch calls an
# UNREACHABLE method in bytecode, and this batch has no UNREACHABLE
# methods of its own. See REPORT.md for the full recomputation.
SUPPRESS.update(set())
