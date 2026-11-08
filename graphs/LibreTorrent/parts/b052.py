# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch52 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 52 part (FeedDao_Impl Callable $8 call/finalize + $9, TagInfoDao_Impl +
# adapters $1-$3 + Callables $4-$6, TorrentDao + TorrentDao_Impl head).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b052_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated Room source (*_Impl) is absent from final_java_only (generated at
# build time), so every _Impl edge below is INFERRED generated dispatch, never
# SOURCE. The $N assignment below is pinned by bytecode: Callable creation
# sites read from Impl method bodies (NEW in Rx method), adapter SQL strings
# read from the generated class files.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# Callable $8 call/finalize: created in getFeedByIdSingle (batch 51 row 40 is its <init>).
e('FeedDao_Impl.getFeedByIdSingle', 'FeedDao_Impl$8.call', 'CALL', 'Subscription runs the Callable that reads the single feed channel', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:122; SRC FeedDao.java:70')
e('FeedDao_Impl$8.<init>', 'FeedDao_Impl$8.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC FeedRepositoryImpl.java:122; SRC FeedDao.java:70')

# Callable $9: created in observeAllFeeds (bytecode: NEW in observeAllFeeds).
e('FeedDao_Impl.observeAllFeeds', 'FeedDao_Impl$9.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in observeAllFeeds)', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:128; SRC FeedDao.java:73')
e('FeedDao_Impl.observeAllFeeds', 'FeedDao_Impl$9.call', 'CALL', 'Subscription runs the Callable that reads the feed list', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:128; SRC FeedDao.java:73')
e('FeedDao_Impl$9.<init>', 'FeedDao_Impl$9.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC FeedRepositoryImpl.java:128; SRC FeedDao.java:73')

# TagInfoDao_Impl methods through TagRepositoryImpl (virtual dispatch to the Impl override).
e('AppDatabase_Impl.tagInfoDao', 'TagInfoDao_Impl.<init>', 'CALL', 'Room constructs the generated DAO implementation on first accessor call', cls='non_standard', via='Room constructs the generated DAO implementation on first accessor call', evidence='INFERRED Room dispatch; SRC AppDatabase.java:67; SRC TagRepositoryImpl.java:40,45,50')
e('TagRepositoryImpl.delete', 'TagInfoDao_Impl.delete', 'CALL', 'Tag delete goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:49-51; SRC TagInfoDao.java:45')
e('TagRepositoryImpl.getByName', 'TagInfoDao_Impl.getByName', 'CALL', 'Tag lookup by name goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:54-56; SRC TagInfoDao.java:48')
e('TagRepositoryImpl.getByTorrentId', 'TagInfoDao_Impl.getByTorrentId', 'CALL', 'Tag lookup by torrent goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:74-76; SRC TagInfoDao.java:63')
e('TagRepositoryImpl.getByTorrentIdAsync', 'TagInfoDao_Impl.getByTorrentIdAsync', 'CALL', 'Tag async lookup goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:69-70; SRC TagInfoDao.java:59')
e('AppDatabase_Impl.getRequiredTypeConverters', 'TagInfoDao_Impl.getRequiredConverters', 'CALL', 'Room generated converter validation aggregates each DAO converters list at database build', cls='non_standard', via='Room generated converter validation aggregates each DAO converters list at database build', evidence='INFERRED Room dispatch; SRC AppDatabase.java:53,81-87')
e('TagRepositoryImpl.insert', 'TagInfoDao_Impl.insert', 'CALL', 'Tag insert goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:39-41; SRC TagInfoDao.java:39')
e('TagRepositoryImpl.observeAll', 'TagInfoDao_Impl.observeAll', 'CALL', 'Tag observation goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:59-61; SRC TagInfoDao.java:51')
e('TagRepositoryImpl.observeByTorrentId', 'TagInfoDao_Impl.observeByTorrentId', 'CALL', 'Tag observation by torrent goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:64-66; SRC TagInfoDao.java:55')
e('TagRepositoryImpl.update', 'TagInfoDao_Impl.update', 'CALL', 'Tag update goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:44-46; SRC TagInfoDao.java:42')

# Bind adapter $1: INSERT INTO TagInfo (serves insert).
e('TagInfoDao_Impl.<init>', 'TagInfoDao_Impl$1.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO TagInfo)', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:39; SRC TagRepositoryImpl.java:40')
e('TagInfoDao_Impl.insert', 'TagInfoDao_Impl$1.bind', 'CALL', 'Tag insert binds the tag row through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:40; SRC TagInfoDao.java:39')
e('TagInfoDao_Impl$1.<init>', 'TagInfoDao_Impl$1.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:39')

# Bind adapter $2: DELETE FROM TagInfo (serves delete).
e('TagInfoDao_Impl.<init>', 'TagInfoDao_Impl$2.<init>', 'CALL', 'Room creates the deletion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the deletion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM TagInfo)', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:45; SRC TagRepositoryImpl.java:50')
e('TagInfoDao_Impl.delete', 'TagInfoDao_Impl$2.bind', 'CALL', 'Tag delete binds the tag row through the adapter', cls='non_standard', via='Room deletion-adapter template dispatch binds the entity on delete', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:50; SRC TagInfoDao.java:45')
e('TagInfoDao_Impl$2.<init>', 'TagInfoDao_Impl$2.createQuery', 'CALL', 'Adapter creation builds its DELETE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:45')

# Bind adapter $3: UPDATE TagInfo (serves update).
e('TagInfoDao_Impl.<init>', 'TagInfoDao_Impl$3.<init>', 'CALL', 'Room creates the update adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the update adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL UPDATE TagInfo)', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:42; SRC TagRepositoryImpl.java:45')
e('TagInfoDao_Impl.update', 'TagInfoDao_Impl$3.bind', 'CALL', 'Tag update binds the tag row through the adapter', cls='non_standard', via='Room update-adapter template dispatch binds the entity on update', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:45; SRC TagInfoDao.java:42')
e('TagInfoDao_Impl$3.<init>', 'TagInfoDao_Impl$3.createQuery', 'CALL', 'Adapter creation builds its UPDATE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TagInfoDao.java:42')

# Callable $4: created in observeAll (bytecode: NEW in observeAll).
e('TagInfoDao_Impl.observeAll', 'TagInfoDao_Impl$4.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in observeAll)', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:60; SRC TagInfoDao.java:51')
e('TagInfoDao_Impl.observeAll', 'TagInfoDao_Impl$4.call', 'CALL', 'Subscription runs the Callable that reads the tag list', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:60; SRC TagInfoDao.java:51')
e('TagInfoDao_Impl$4.<init>', 'TagInfoDao_Impl$4.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC TagRepositoryImpl.java:60; SRC TagInfoDao.java:51')

# Callable $5: created in observeByTorrentId (bytecode: NEW in observeByTorrentId).
e('TagInfoDao_Impl.observeByTorrentId', 'TagInfoDao_Impl$5.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in observeByTorrentId)', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:65; SRC TagInfoDao.java:55')
e('TagInfoDao_Impl.observeByTorrentId', 'TagInfoDao_Impl$5.call', 'CALL', 'Subscription runs the Callable that reads the torrent tags', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:65; SRC TagInfoDao.java:55')
e('TagInfoDao_Impl$5.<init>', 'TagInfoDao_Impl$5.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC TagRepositoryImpl.java:65; SRC TagInfoDao.java:55')

# Callable $6: created in getByTorrentIdAsync (bytecode: NEW in getByTorrentIdAsync).
e('TagInfoDao_Impl.getByTorrentIdAsync', 'TagInfoDao_Impl$6.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in getByTorrentIdAsync)', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:70; SRC TagInfoDao.java:59')
e('TagInfoDao_Impl.getByTorrentIdAsync', 'TagInfoDao_Impl$6.call', 'CALL', 'Subscription runs the Callable that reads the torrent tags', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:70; SRC TagInfoDao.java:59')
e('TagInfoDao_Impl$6.<init>', 'TagInfoDao_Impl$6.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC TagRepositoryImpl.java:70; SRC TagInfoDao.java:59')

# TorrentDao (abstract class) and TorrentDao_Impl head.
e('TorrentDao_Impl.<init>', 'TorrentDao.<init>', 'CALL', 'Generated subclass constructor calls the abstract-class super constructor', cls='explicit', evidence='INFERRED compiler-inserted super call (generated source unprinted); SRC TorrentDao.java:38')
e('TorrentRepositoryImpl.replaceTags', 'TorrentDao.replaceTags', 'CALL', 'Session tag replacement runs the DAO transaction method', cls='explicit', evidence='SRC TorrentRepositoryImpl.java:127; SRC TorrentDao.java:67-70')
e('AppDatabase_Impl.torrentDao', 'TorrentDao_Impl.<init>', 'CALL', 'Room constructs the generated DAO implementation on first accessor call', cls='non_standard', via='Room constructs the generated DAO implementation on first accessor call', evidence='INFERRED Room dispatch; SRC AppDatabase.java:61; SRC TorrentRepositoryImpl.java:57,62,67')
e('TorrentRepositoryImpl.addTorrent', 'TorrentDao_Impl.add', 'CALL', 'Torrent write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:56-58; SRC TorrentDao.java:40')
e('TorrentRepositoryImpl.addTag', 'TorrentDao_Impl.addTag', 'CALL', 'Torrent tag link write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:131-133; SRC TorrentDao.java:73')
e('TorrentDao.replaceTags', 'TorrentDao_Impl.addTags', 'CALL', 'Transaction body inserts the new tag links', cls='non_standard', via='virtual dispatch to the generated Impl override of the transaction body', evidence='INFERRED Room dispatch; SRC TorrentDao.java:67-70; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentRepositoryImpl.deleteTorrent', 'TorrentDao_Impl.delete', 'CALL', 'Torrent delete goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:66-68; SRC TorrentDao.java:46')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan — no REACHABLE method in this batch calls an
# UNREACHABLE method in bytecode, and this batch has no UNREACHABLE
# methods of its own. See REPORT.md for the full recomputation.
SUPPRESS.update(set())
