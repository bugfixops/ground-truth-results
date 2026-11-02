# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch53 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 53 part (TorrentDao_Impl methods + $1-$8 adapters/callables, DefaultFsModule).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b053_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated Room source (*_Impl) is absent from final_java_only (generated at
# build time), so every _Impl edge below is INFERRED generated dispatch, never
# SOURCE, except the explicitly constructed DefaultFsModule edge. The $N
# assignment below is pinned by bytecode (work-emulator classes): $1 INSERT
# Torrent, $2 INSERT TorrentTagInfo, $3 DELETE Torrent, $4 DELETE
# TorrentTagInfo, $5 UPDATE Torrent, $6 SharedSQLiteStatement DELETE FROM
# TorrentTagInfo WHERE torrentId, $7 created in getTorrentByIdSingle
# (RxRoom.createSingle), $8 created in observeTorrentById
# (RxRoom.createFlowable); AppDatabase_Impl.getRequiredTypeConverters calls
# TorrentDao_Impl.getRequiredConverters in bytecode.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# TorrentDao_Impl methods through TorrentRepositoryImpl (virtual dispatch to
# the Impl override) and the Room transaction body.
e('TorrentRepositoryImpl.deleteTag', 'TorrentDao_Impl.deleteTag', 'CALL', 'Tag delete goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:136-138; SRC TorrentDao.java:76')
e('TorrentDao.replaceTags', 'TorrentDao_Impl.deleteTagsByTorrentId', 'CALL', 'Transaction body deletes the old tag links before inserting the new ones', cls='non_standard', via='virtual dispatch to the generated Impl override of the transaction body', evidence='INFERRED Room dispatch; SRC TorrentDao.java:67-70; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentRepositoryImpl.getAllTorrents', 'TorrentDao_Impl.getAllTorrents', 'CALL', 'Torrent list read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:86-88; SRC TorrentDao.java:49')
e('AppDatabase_Impl.getRequiredTypeConverters', 'TorrentDao_Impl.getRequiredConverters', 'CALL', 'Room generated converter validation aggregates each DAO converters list at database build', cls='non_standard', via='Room generated converter validation aggregates each DAO converters list at database build', evidence='INFERRED Room dispatch; SRC AppDatabase.java:61,81-87')
e('TorrentRepositoryImpl.getTorrentById', 'TorrentDao_Impl.getTorrentById', 'CALL', 'Torrent lookup by id goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:71-73; SRC TorrentDao.java:52')
e('TorrentRepositoryImpl.getTorrentByIdSingle', 'TorrentDao_Impl.getTorrentByIdSingle', 'CALL', 'Single torrent lookup goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:76-78; SRC TorrentDao.java:55')
e('TorrentRepositoryImpl.observeTorrentById', 'TorrentDao_Impl.observeTorrentById', 'CALL', 'Torrent observation goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:81-83; SRC TorrentDao.java:58')
e('TorrentRepositoryImpl.replaceTags', 'TorrentDao_Impl.replaceTags', 'CALL', 'Session tag replacement runs the DAO transaction method', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:122-128; SRC TorrentDao.java:67-70')
e('TorrentRepositoryImpl.updateTorrent', 'TorrentDao_Impl.update', 'CALL', 'Torrent update goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:61-63; SRC TorrentDao.java:43')

# Bind adapter $1: INSERT INTO Torrent (serves add).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$1.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO Torrent)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:40; SRC TorrentRepositoryImpl.java:56-58')
e('TorrentDao_Impl.add', 'TorrentDao_Impl$1.bind', 'CALL', 'Torrent insert binds the torrent row through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:56-58; SRC TorrentDao.java:40')
e('TorrentDao_Impl$1.<init>', 'TorrentDao_Impl$1.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TorrentDao.java:40')

# Bind adapter $2: INSERT INTO TorrentTagInfo (serves addTags and addTag, one shared adapter).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$2.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO TorrentTagInfo)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:61; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentDao_Impl.addTags', 'TorrentDao_Impl$2.bind', 'CALL', 'Tag-link insert binds the tag-link rows through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC TorrentDao.java:67-70; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentDao_Impl.addTag', 'TorrentDao_Impl$2.bind', 'CALL', 'Single tag-link insert binds the tag-link row through the shared adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:131-133; SRC TorrentDao.java:73')
e('TorrentDao_Impl$2.<init>', 'TorrentDao_Impl$2.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TorrentDao.java:61')

# Bind adapter $3: DELETE FROM Torrent (serves delete).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$3.<init>', 'CALL', 'Room creates the deletion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the deletion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM Torrent)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:46; SRC TorrentRepositoryImpl.java:66-68')
e('TorrentDao_Impl.delete', 'TorrentDao_Impl$3.bind', 'CALL', 'Torrent delete binds the torrent row through the adapter', cls='non_standard', via='Room deletion-adapter template dispatch binds the entity on delete', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:66-68; SRC TorrentDao.java:46')
e('TorrentDao_Impl$3.<init>', 'TorrentDao_Impl$3.createQuery', 'CALL', 'Adapter creation builds its DELETE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TorrentDao.java:46')

# Bind adapter $4: DELETE FROM TorrentTagInfo (serves deleteTag).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$4.<init>', 'CALL', 'Room creates the deletion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the deletion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM TorrentTagInfo)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:76; SRC TorrentRepositoryImpl.java:136-138')
e('TorrentDao_Impl.deleteTag', 'TorrentDao_Impl$4.bind', 'CALL', 'Tag-link delete binds the tag-link row through the adapter', cls='non_standard', via='Room deletion-adapter template dispatch binds the entity on delete', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:136-138; SRC TorrentDao.java:76')
e('TorrentDao_Impl$4.<init>', 'TorrentDao_Impl$4.createQuery', 'CALL', 'Adapter creation builds its DELETE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TorrentDao.java:76')

# Bind adapter $5: UPDATE Torrent (serves update).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$5.<init>', 'CALL', 'Room creates the update adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the update adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL UPDATE Torrent)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:43; SRC TorrentRepositoryImpl.java:61-63')
e('TorrentDao_Impl.update', 'TorrentDao_Impl$5.bind', 'CALL', 'Torrent update binds the torrent row through the adapter', cls='non_standard', via='Room update-adapter template dispatch binds the entity on update', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:61-63; SRC TorrentDao.java:43')
e('TorrentDao_Impl$5.<init>', 'TorrentDao_Impl$5.createQuery', 'CALL', 'Adapter creation builds its UPDATE statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC TorrentDao.java:43')

# Statement $6: DELETE FROM TorrentTagInfo WHERE torrentId (serves deleteTagsByTorrentId; no bind row).
e('TorrentDao_Impl.<init>', 'TorrentDao_Impl$6.<init>', 'CALL', 'Room creates the shared statement in the DAO Impl constructor', cls='non_standard', via='Room creates the shared statement in the DAO Impl constructor (bytecode: NEW in <init>; SQL DELETE FROM TorrentTagInfo WHERE torrentId)', evidence='INFERRED Room dispatch; SRC TorrentDao.java:64; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentDao_Impl.deleteTagsByTorrentId', 'TorrentDao_Impl$6.createQuery', 'CALL', 'Statement acquisition builds its DELETE statement', cls='non_standard', via='Room SharedSQLiteStatement acquisition builds the DELETE statement', evidence='INFERRED Room dispatch; SRC TorrentDao.java:64; SRC TorrentRepositoryImpl.java:122-128')

# Callable $7: created in getTorrentByIdSingle (bytecode: NEW in getTorrentByIdSingle; RxRoom.createSingle).
e('TorrentDao_Impl.getTorrentByIdSingle', 'TorrentDao_Impl$7.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in getTorrentByIdSingle)', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:76-78; SRC TorrentDao.java:55')
e('TorrentDao_Impl.getTorrentByIdSingle', 'TorrentDao_Impl$7.call', 'CALL', 'Subscription runs the Callable that reads the single torrent', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:76-78; SRC TorrentDao.java:55')
e('TorrentDao_Impl$7.<init>', 'TorrentDao_Impl$7.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC TorrentRepositoryImpl.java:76-78; SRC TorrentDao.java:55')

# Callable $8: created in observeTorrentById (bytecode: NEW in observeTorrentById; RxRoom.createFlowable).
e('TorrentDao_Impl.observeTorrentById', 'TorrentDao_Impl$8.<init>', 'CALL', 'Room creates the Rx Callable in the DAO method', cls='non_standard', via='Room creates the Rx Callable in the DAO method (bytecode: NEW in observeTorrentById)', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:81-83; SRC TorrentDao.java:58')
e('TorrentDao_Impl.observeTorrentById', 'TorrentDao_Impl$8.call', 'CALL', 'Subscription runs the Callable that reads the torrent', cls='non_standard', via='Rx subscription dispatch to the Room Callable', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:81-83; SRC TorrentDao.java:58')
e('TorrentDao_Impl$8.<init>', 'TorrentDao_Impl$8.finalize', 'CALL', 'Garbage collection finalizes the Callable instance', cls='non_standard', via='JVM garbage-collector finalization dispatch on the Callable instance', evidence='INFERRED JVM dispatch; SRC TorrentRepositoryImpl.java:81-83; SRC TorrentDao.java:58')

# DefaultFsModule through the FileSystemFacadeImpl dispatcher (FsModule interface dispatch; file-URI branch).
e('FsModuleResolverImpl.<init>', 'DefaultFsModule.<init>', 'CALL', 'Resolver construction builds the default module', cls='explicit', evidence='SRC FsModuleResolverImpl.java:35-39; SRC SystemFacadeHelper.java:39-46')
e('FileSystemFacadeImpl.deleteFile', 'DefaultFsModule.delete', 'CALL', 'Facade delete dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:110-115; SRC DefaultFsModule.java:79-82')
e('FileSystemFacadeImpl.fileExists', 'DefaultFsModule.fileExists', 'CALL', 'Facade file-exists check dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:153-158; SRC DefaultFsModule.java:109-112')
e('FileSystemFacadeImpl.getDirAvailableBytes', 'DefaultFsModule.getDirAvailableBytes', 'CALL', 'Facade dir-bytes query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:268-282; SRC DefaultFsModule.java:91-106')
e('FileSystemFacadeImpl.getDirPath', 'DefaultFsModule.getDirPath', 'CALL', 'Facade dir-path query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:418-423; SRC DefaultFsModule.java:47-50')
e('FileSystemFacadeImpl.getFilePath', 'DefaultFsModule.getFilePath', 'CALL', 'Facade file-path query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:430-435; SRC DefaultFsModule.java:53-56')
e('FileSystemFacadeImpl.createFile', 'DefaultFsModule.getFileUri(Uri,String,boolean)', 'CALL', 'Facade file creation calls the module method directly', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:199-218; SRC DefaultFsModule.java:59-66')
e('FileSystemFacadeImpl.getFileUri(String,Uri)', 'DefaultFsModule.getFileUri(String,Uri)', 'CALL', 'Facade file-uri query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:144-150; SRC DefaultFsModule.java:69-76')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan of this batch's classes — no REACHABLE method in
# this batch calls an UNREACHABLE method in bytecode. See REPORT.md.
SUPPRESS.update(set())
