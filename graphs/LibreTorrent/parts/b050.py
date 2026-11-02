# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b050 — converter C07 delivery.
# Base: audited A3 output helper/a3-g10/parts/b050.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# clone/graphs/LibreTorrent/scratch/merge-ready/batch50-merge-ready.md).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/50/ (see REPORT-b050.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Batch 50 part (TagRepositoryImpl tail, TorrentRepositoryImpl, UriConverter,
# FastResumeDao_Impl + adapter, FeedDao_Impl head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b050_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated Room source (*_Impl) is absent from final_java_only (generated at
# build time), so every _Impl edge below is INFERRED generated dispatch, never
# SOURCE. No pre-existing route is relied on; every REACHABLE row below has an
# edge here.

# TagRepositoryImpl tail from printed callers.
e('DetailTorrentViewModel.getTags', 'TagRepositoryImpl.getByTorrentIdAsync', 'CALL', 'Detail tags load reads tags asynchronously', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:144; SRC TagRepositoryImpl.java:69-70')
e('AddTagViewModel.setRandomColor', 'TagRepositoryImpl.insert', 'CALL', 'Tag colour assignment inserts the tag', cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:69; SRC TagRepositoryImpl.java:39-41')
e('MainViewModel.observeTags', 'TagRepositoryImpl.observeAll', 'CALL', 'Main screen observes all tags', cls='explicit', evidence='SRC ui/main/MainViewModel.java:183; SRC TagRepositoryImpl.java:59-61')
e('DetailTorrentViewModel.observeTags', 'TagRepositoryImpl.observeByTorrentId', 'CALL', 'Detail screen observes one torrent tags', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:148; SRC TagRepositoryImpl.java:64-66')
e('AddTagViewModel.setRandomColor', 'TagRepositoryImpl.update', 'CALL', 'Tag colour assignment updates the tag', cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:71; SRC TagRepositoryImpl.java:44-46')

# TorrentRepositoryImpl construction and class init.
e('RepositoryHelper.getTorrentRepository', 'TorrentRepositoryImpl.<clinit>', 'FRAMEWORK', 'First torrent-repository construction initialises the class', cls='non_standard', via='JVM class initialization on first active use of TorrentRepositoryImpl', evidence='SRC RepositoryHelper.java:43-47; SRC TorrentRepositoryImpl.java:41')
e('RepositoryHelper.getTorrentRepository', 'TorrentRepositoryImpl.<init>', 'CALL', 'Torrent repository getter constructs the implementation', cls='explicit', evidence='SRC RepositoryHelper.java:46-47; SRC TorrentRepositoryImpl.java:50-53')

# TorrentRepositoryImpl methods from their printed callers.
e('TorrentDownloadImpl.serializeResumeData', 'TorrentRepositoryImpl.addFastResume', 'CALL', 'Resume serialisation stores the fast-resume row', cls='explicit', evidence='SRC TorrentDownloadImpl.java:520; SRC TorrentRepositoryImpl.java:91-93')
e('DetailTorrentViewModel.addTag', 'TorrentRepositoryImpl.addTag', 'CALL', 'Detail screen adds a tag to the torrent', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:152; SRC TorrentRepositoryImpl.java:131-133')
e('TorrentSessionImpl.addTorrent', 'TorrentRepositoryImpl.addTorrent', 'CALL', 'Session add stores the torrent row', cls='explicit', evidence='SRC TorrentSessionImpl.java:285; SRC TorrentRepositoryImpl.java:56-58')
e('DetailTorrentViewModel.removeTag', 'TorrentRepositoryImpl.deleteTag', 'CALL', 'Detail screen removes a tag from the torrent', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:156; SRC TorrentRepositoryImpl.java:136-138')
e('TorrentSessionImpl.addTorrent', 'TorrentRepositoryImpl.deleteTorrent', 'CALL', 'Session add replaces a stored torrent row', cls='explicit', evidence='SRC TorrentSessionImpl.java:313; SRC TorrentRepositoryImpl.java:66-68')
e('TorrentEngine.makeInfoListSync', 'TorrentRepositoryImpl.getAllTorrents', 'CALL', 'Info list build reads all stored torrents', cls='explicit', evidence='SRC TorrentEngine.java:817; SRC TorrentRepositoryImpl.java:86-88')
e('TorrentSessionImpl.restoreDownload', 'TorrentRepositoryImpl.getFastResumeById', 'CALL', 'Download restore reads the fast-resume row', cls='explicit', evidence='SRC TorrentSessionImpl.java:1686; SRC TorrentRepositoryImpl.java:96-98')
e('TorrentSessionImpl.loadSettings', 'TorrentRepositoryImpl.getSessionFile', 'CALL', 'Session settings load reads the session file path', cls='explicit', evidence='SRC TorrentSessionImpl.java:1195; SRC TorrentRepositoryImpl.java:109-119')
e('TorrentEngine.makeInfoSync', 'TorrentRepositoryImpl.getTorrentById', 'CALL', 'Info build reads the stored torrent', cls='explicit', evidence='SRC TorrentEngine.java:767; SRC TorrentRepositoryImpl.java:71-73')
e('TorrentEngine$5.onTorrentFinished', 'TorrentRepositoryImpl.getTorrentByIdSingle', 'CALL', 'Finished torrent reload reads the stored torrent as a single', cls='explicit', evidence='SRC TorrentEngine.java:1307; SRC TorrentRepositoryImpl.java:76-78')
e('DetailTorrentViewModel.observeTorrent', 'TorrentRepositoryImpl.observeTorrentById', 'CALL', 'Detail screen observes the stored torrent', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:176; SRC TorrentRepositoryImpl.java:81-83')
e('TorrentSessionImpl.addTorrent', 'TorrentRepositoryImpl.replaceTags', 'CALL', 'Session add replaces the torrent tag links', cls='explicit', evidence='SRC TorrentSessionImpl.java:287; SRC TorrentRepositoryImpl.java:122-128')
e('TorrentSessionImpl.saveSettings', 'TorrentRepositoryImpl.saveSession', 'CALL', 'Session settings save writes the session bytes', cls='explicit', evidence='SRC TorrentSessionImpl.java:1234; SRC TorrentRepositoryImpl.java:101-106')
e('TorrentEngine.markAsHiddenSync', 'TorrentRepositoryImpl.updateTorrent', 'CALL', 'Hidden marking writes the updated torrent row', cls='explicit', evidence='SRC TorrentEngine.java:1262; SRC TorrentRepositoryImpl.java:61-63')

# UriConverter: Room TypeConverter dispatch on the Torrent.downloadPath Uri field.
e('TorrentRepositoryImpl.addTorrent', 'UriConverter.fromUri', 'CALL', 'Torrent write converts the download-path Uri to a string column', cls='non_standard', via='Room TypeConverter dispatch when writing a Uri-typed entity field', evidence='INFERRED Room dispatch; SRC Torrent.java:57; SRC TorrentRepositoryImpl.java:56-58; SRC AppDatabase.java:53; SRC UriConverter.java:36-39')
e('TorrentRepositoryImpl.getTorrentById', 'UriConverter.toUri', 'CALL', 'Torrent read converts the download-path string column back to a Uri', cls='non_standard', via='Room TypeConverter dispatch when reading a Uri-typed entity field', evidence='INFERRED Room dispatch; SRC Torrent.java:57; SRC TorrentRepositoryImpl.java:71-73; SRC AppDatabase.java:53; SRC UriConverter.java:30-33')

# FastResumeDao_Impl and its insertion adapter (bytecode SQL: INSERT INTO FastResume).
e('AppDatabase_Impl.fastResumeDao', 'FastResumeDao_Impl.<init>', 'CALL', 'Room constructs the generated DAO implementation on first accessor call', cls='non_standard', via='Room constructs the generated DAO implementation on first accessor call', evidence='INFERRED Room dispatch; SRC AppDatabase.java:63; SRC TorrentRepositoryImpl.java:92,97')
e('TorrentRepositoryImpl.addFastResume', 'FastResumeDao_Impl.add', 'CALL', 'Fast-resume write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:91-93; SRC FastResumeDao.java:14')
e('TorrentRepositoryImpl.getFastResumeById', 'FastResumeDao_Impl.getByTorrentId', 'CALL', 'Fast-resume read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:96-98; SRC FastResumeDao.java:17')
e('AppDatabase_Impl.getRequiredTypeConverters', 'FastResumeDao_Impl.getRequiredConverters', 'CALL', 'Room generated converter validation aggregates each DAO converters list at database build', cls='non_standard', via='Room generated converter validation aggregates each DAO converters list at database build', evidence='INFERRED Room dispatch; SRC AppDatabase.java:53,81-87')
e('FastResumeDao_Impl.<init>', 'FastResumeDao_Impl$1.<init>', 'CALL', 'Room creates the insertion adapter in the DAO Impl constructor', cls='non_standard', via='Room creates the insertion adapter in the DAO Impl constructor (bytecode: NEW in <init>; SQL INSERT INTO FastResume)', evidence='INFERRED Room dispatch; SRC FastResumeDao.java:14; SRC TorrentRepositoryImpl.java:91-93')
e('FastResumeDao_Impl.add', 'FastResumeDao_Impl$1.bind', 'CALL', 'Insert binds the fast-resume row through the adapter', cls='non_standard', via='Room insertion-adapter template dispatch binds the entity on insert', evidence='INFERRED Room dispatch; SRC FastResumeDao.java:14; SRC TorrentRepositoryImpl.java:91-93')
e('FastResumeDao_Impl$1.<init>', 'FastResumeDao_Impl$1.createQuery', 'CALL', 'Adapter creation builds its INSERT statement', cls='non_standard', via='Room adapter superclass constructor invokes the overridden createQuery', evidence='INFERRED Room dispatch; SRC FastResumeDao.java:14')

# FeedDao_Impl head (accessor dispatch through FeedRepositoryImpl).
e('AppDatabase_Impl.feedDao', 'FeedDao_Impl.<init>', 'CALL', 'Room constructs the generated DAO implementation on first accessor call', cls='non_standard', via='Room constructs the generated DAO implementation on first accessor call', evidence='INFERRED Room dispatch; SRC AppDatabase.java:65; SRC FeedRepositoryImpl.java:86,92,104')
e('FeedRepositoryImpl.addFeed', 'FeedDao_Impl.addFeed', 'CALL', 'Feed write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:84-87; SRC FeedDao.java:52')
e('FeedRepositoryImpl.addFeeds', 'FeedDao_Impl.addFeeds', 'CALL', 'Feed batch write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:90-93; SRC FeedDao.java:55')
e('FeedRepositoryImpl.addItems', 'FeedDao_Impl.addItems', 'CALL', 'Feed items write goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:168-171; SRC FeedDao.java:82')
e('FeedRepositoryImpl.deleteFeed', 'FeedDao_Impl.deleteFeed', 'CALL', 'Feed delete goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:102-105; SRC FeedDao.java:61')
e('FeedRepositoryImpl.deleteFeeds', 'FeedDao_Impl.deleteFeeds', 'CALL', 'Feed batch delete goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:108-111; SRC FeedDao.java:64')
e('FeedRepositoryImpl.deleteItemsOlderThan', 'FeedDao_Impl.deleteItemsOlderThan', 'CALL', 'Feed prune goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:174-177; SRC FeedDao.java:85')
e('FeedRepositoryImpl.findItemsExistingTitles', 'FeedDao_Impl.findItemsExistingTitles', 'CALL', 'Feed title lookup goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:216-219; SRC FeedDao.java:106')
e('FeedRepositoryImpl.getAllFeeds', 'FeedDao_Impl.getAllFeeds', 'CALL', 'Feed read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:132-135; SRC FeedDao.java:76')
e('FeedRepositoryImpl.getAllFeedsSingle', 'FeedDao_Impl.getAllFeedsSingle', 'CALL', 'Feed single read goes through the generated DAO implementation', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:138-141; SRC FeedDao.java:79')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan — no REACHABLE method in this batch calls an
# UNREACHABLE method in bytecode, and this batch has no UNREACHABLE
# methods of its own. See REPORT.md for the full recomputation.
SUPPRESS.update(set())
