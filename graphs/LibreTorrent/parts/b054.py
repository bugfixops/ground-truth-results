# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch54 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 54 part (DefaultFsModule tail, FileDescriptorWrapperImpl, FileSystemFacadeImpl, FsModuleResolverImpl, SafFileSystem head).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b054_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# DefaultFsModule tail through the FileSystemFacadeImpl dispatcher (FsModule interface dispatch; file-URI branch).
e('FileSystemFacadeImpl.getParentDirUri', 'DefaultFsModule.getParentDirUri', 'CALL', 'Facade parent-dir query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:438-443; SRC DefaultFsModule.java:127-132')
e('FileSystemFacadeImpl.makeFileSystemPath(Uri,String)', 'DefaultFsModule.makeFileSystemPath', 'CALL', 'Facade path query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:254-260; SRC DefaultFsModule.java:121-124')
e('FileSystemFacadeImpl.getFD', 'DefaultFsModule.openFD', 'CALL', 'Facade fd query dispatches to the default module on the file-URI branch', cls='non_standard', via='FsModule interface dispatch on the file-URI branch', evidence='SRC FileSystemFacadeImpl.java:60-65; SRC DefaultFsModule.java:85-88')

# FileDescriptorWrapperImpl: constructed by both modules, opened by the facade writers, closed by try-with-resources.
e('DefaultFsModule.openFD', 'FileDescriptorWrapperImpl.<init>', 'CALL', 'Default module opens a descriptor wrapper for the path', cls='explicit', evidence='SRC DefaultFsModule.java:85-88; SRC FileDescriptorWrapperImpl.java:39-43')
e('FileSystemFacadeImpl.write(byte[],Uri)', 'FileDescriptorWrapperImpl.close', 'CALL', 'Facade byte writer closes its descriptor wrapper when the try block ends', cls='non_standard', via='Java try-with-resources close dispatch', evidence='SRC FileSystemFacadeImpl.java:221-229; SRC FileDescriptorWrapperImpl.java:54-58')
e('FileSystemFacadeImpl.write(byte[],Uri)', 'FileDescriptorWrapperImpl.open', 'CALL', 'Facade byte writer opens the descriptor wrapper for writing', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:221-229; SRC FileDescriptorWrapperImpl.java:46-51')
e('FileSystemFacadeImpl.write(CharSequence,Charset,Uri)', 'FileDescriptorWrapperImpl.open', 'CALL', 'Facade text writer opens the descriptor wrapper for writing', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:232-241; SRC FileDescriptorWrapperImpl.java:46-51')

# FileSystemFacadeImpl: construction, class initialisation, and its facade methods.
e('SystemFacadeHelper.getFileSystemFacade', 'FileSystemFacadeImpl.<clinit>', 'CALL', 'First facade construction initialises the facade class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC SystemFacadeHelper.java:39-46; SRC FileSystemFacadeImpl.java:44-47')
e('SystemFacadeHelper.getFileSystemFacade', 'FileSystemFacadeImpl.<init>', 'CALL', 'Facade helper constructs the facade with its module resolver', cls='explicit', evidence='SRC SystemFacadeHelper.java:39-46; SRC FileSystemFacadeImpl.java:52-57')
e('FileManagerViewModel.createFile', 'FileSystemFacadeImpl.buildValidFatFilename', 'CALL', 'File-manager file creation validates the file name through the facade', cls='explicit', evidence='SRC ui/filemanager/FileManagerViewModel.java:248-253; SRC FileSystemFacadeImpl.java:343-363')
e('TorrentEngine.cleanTemp', 'FileSystemFacadeImpl.cleanTempDir', 'CALL', 'Engine temp cleanup clears the facade temp directory', cls='explicit', evidence='SRC TorrentEngine.java:1223-1225; SRC FileSystemFacadeImpl.java:296-303')
e('TorrentEngine.saveTorrentFile', 'FileSystemFacadeImpl.createFile', 'CALL', 'Engine torrent-file save creates the destination file through the facade', cls='explicit', evidence='SRC TorrentEngine.java:973-987; SRC FileSystemFacadeImpl.java:199-218')
e('TorrentEngine.startWatchDir', 'FileSystemFacadeImpl.deleteFile', 'CALL', 'Engine watch-dir delete removes the watched file through the facade', cls='explicit', evidence='SRC TorrentEngine.java:1154; SRC FileSystemFacadeImpl.java:110-115')
e('IPFilterParser.parseFile', 'FileSystemFacadeImpl.fileExists', 'CALL', 'IP filter parsing checks the filter file through the facade', cls='explicit', evidence='SRC IPFilterParser.java:59-63; SRC FileSystemFacadeImpl.java:153-158')
e('Utils.getTorrentDownloadPath', 'FileSystemFacadeImpl.getDefaultDownloadPath', 'CALL', 'Download-path lookup falls back to the facade default path', cls='explicit', evidence='SRC Utils.java:638-647; SRC FileSystemFacadeImpl.java:80-90')
e('TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)', 'FileSystemFacadeImpl.getDirAvailableBytes', 'CALL', 'Engine torrent add checks the download directory space through the facade', cls='explicit', evidence='SRC TorrentEngine.java:1200; SRC FileSystemFacadeImpl.java:268-282')
e('StorageSettingsFragment.onCreate', 'FileSystemFacadeImpl.getDirPath', 'CALL', 'Storage settings summaries read directory paths through the facade', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:81-99; SRC FileSystemFacadeImpl.java:418-423')
e('DetailTorrentViewModel.makeOpenFileIntent', 'FileSystemFacadeImpl.getExtension', 'CALL', 'Detail open-file intent reads the file extension through the facade', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:398-399; SRC FileSystemFacadeImpl.java:312-325')
e('FileManagerViewModel.appendExtension', 'FileSystemFacadeImpl.getExtensionSeparator', 'CALL', 'File-manager name editing reads the extension separator through the facade', cls='explicit', evidence='SRC ui/filemanager/FileManagerViewModel.java:229-243; SRC FileSystemFacadeImpl.java:68-71')
e('TorrentEngine.addTorrentCompletable(Uri,Uri)', 'FileSystemFacadeImpl.getFD', 'CALL', 'Engine torrent add opens the torrent file through the facade', cls='explicit', evidence='SRC TorrentEngine.java:374-381; SRC FileSystemFacadeImpl.java:60-65')
e('FileSystemFacadeImpl.write(byte[],Uri)', 'FileSystemFacadeImpl.getFD', 'CALL', 'Facade byte writer opens its destination through the facade fd query', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:221-229; SRC FileSystemFacadeImpl.java:60-65')
e('NetworkSettingsFragment.onCreate', 'FileSystemFacadeImpl.getFilePath', 'CALL', 'Network settings summaries read file paths through the facade', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:208; SRC FileSystemFacadeImpl.java:430-435')
e('TorrentDownloadImpl.getPartsFile', 'FileSystemFacadeImpl.getFileUri(Uri,String)', 'CALL', 'Parts-file lookup builds the parts file uri through the facade', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1284-1299; SRC FileSystemFacadeImpl.java:122-136')
e('DetailTorrentViewModel.getFilePath', 'FileSystemFacadeImpl.getFileUri(String,Uri)', 'CALL', 'Detail file-path lookup builds the file uri through the facade', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:262-275; SRC FileSystemFacadeImpl.java:144-150')
e('CreateTorrentViewModel.downloadTorrent', 'FileSystemFacadeImpl.getParentDirUri', 'CALL', 'Create-torrent download reads the seed parent directory through the facade', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:352-357; SRC FileSystemFacadeImpl.java:438-443')
e('FileSystemFacadeImpl.cleanTempDir', 'FileSystemFacadeImpl.getTempDir', 'CALL', 'Facade temp cleanup reads the temp directory through the facade', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:296-303; SRC FileSystemFacadeImpl.java:285-293')
e('FeedActivity.backupFeedsChooseDialog', 'FileSystemFacadeImpl.getUserDirPath', 'CALL', 'Feed backup dialog reads the user directory through the facade', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:262-266; SRC FileSystemFacadeImpl.java:98-107')
e('FeedActivity.restoreFeedsChooseDialog', 'FileSystemFacadeImpl.getUserDirPath', 'CALL', 'Feed restore dialog reads the user directory through the facade', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:278-282; SRC FileSystemFacadeImpl.java:98-107')
e('TorrentRepositoryImpl.getSessionFile', 'FileSystemFacadeImpl.isStorageReadable', 'CALL', 'Session-file lookup checks storage readability through the facade', cls='explicit', evidence='SRC TorrentRepositoryImpl.java:109-110; SRC FileSystemFacadeImpl.java:185-191')
e('TorrentRepositoryImpl.getTorrentDataDir', 'FileSystemFacadeImpl.isStorageReadable', 'CALL', 'Torrent data-dir lookup checks storage readability through the facade', cls='explicit', evidence='SRC TorrentRepositoryImpl.java:145-146; SRC FileSystemFacadeImpl.java:185-191')
e('FileSystemFacadeImpl.buildValidFatFilename', 'FileSystemFacadeImpl.isValidFatFilenameChar', 'CALL', 'Fat file-name validation tests each character through the facade', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:343-363; SRC FileSystemFacadeImpl.java:365-384')
e('TorrentSessionImpl.download(String,AddTorrentParams,byte[])', 'FileSystemFacadeImpl.makeFileSystemPath(Uri)', 'CALL', 'Session download builds the torrent file-system path through the facade', cls='explicit', evidence='SRC TorrentSessionImpl.java:328-341; SRC FileSystemFacadeImpl.java:248-251')
e('TorrentSessionImpl.restoreTorrents', 'FileSystemFacadeImpl.makeFileSystemPath(Uri)', 'CALL', 'Session restore builds torrent file-system paths through the facade', cls='explicit', evidence='SRC TorrentSessionImpl.java:396-407; SRC FileSystemFacadeImpl.java:248-251')
e('TorrentDownloadImpl.setDownloadPath', 'FileSystemFacadeImpl.makeFileSystemPath(Uri)', 'CALL', 'Download path change builds the file-system path through the facade', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1215-1229; SRC FileSystemFacadeImpl.java:248-251')
e('FileSystemFacadeImpl.makeFileSystemPath(Uri)', 'FileSystemFacadeImpl.makeFileSystemPath(Uri,String)', 'CALL', 'One-arg path query delegates to the two-arg path query', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:248-260; SRC FileSystemFacadeImpl.java:254-260')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'FileSystemFacadeImpl.makeTempFile', 'CALL', 'Torrent decode task stages the download in a facade temp file', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:253; SRC FileSystemFacadeImpl.java:306-309')
e('Utils.getTorrentDownloadPath', 'FileSystemFacadeImpl.normalizeFileSystemPath', 'CALL', 'Download-path lookup normalises the stored path through the facade', cls='explicit', evidence='SRC Utils.java:638-647; SRC FileSystemFacadeImpl.java:404-411')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'FileSystemFacadeImpl.normalizeFileSystemPath', 'CALL', 'Torrent decode task normalises the staged file path through the facade', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:259; SRC FileSystemFacadeImpl.java:404-411')
e('FileSystemFacadeImpl.buildValidFatFilename', 'FileSystemFacadeImpl.trimFilename', 'CALL', 'Fat file-name validation trims the result through the facade', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:343-363; SRC FileSystemFacadeImpl.java:386-397')
e('FeedRepositoryImpl.serializeAllFeeds', 'FileSystemFacadeImpl.write(CharSequence,Charset,Uri)', 'CALL', 'Feed serialisation writes the feeds file through the facade text writer', cls='explicit', evidence='SRC FeedRepositoryImpl.java:144-147; SRC FileSystemFacadeImpl.java:232-241')
e('TorrentEngine.saveTorrentFile', 'FileSystemFacadeImpl.write(byte[],Uri)', 'CALL', 'Engine torrent-file save writes the bencode through the facade byte writer', cls='explicit', evidence='SRC TorrentEngine.java:973-987; SRC FileSystemFacadeImpl.java:221-229')

# FsModuleResolverImpl: constructed by the facade helper, queried by every facade dispatch.
e('SystemFacadeHelper.getFileSystemFacade', 'FsModuleResolverImpl.<init>', 'CALL', 'Facade helper constructs the module resolver', cls='explicit', evidence='SRC SystemFacadeHelper.java:39-46; SRC FsModuleResolverImpl.java:35-39')
e('FileSystemFacadeImpl.getFD', 'FsModuleResolverImpl.resolveFsByUri', 'CALL', 'Facade fd query resolves the module for the uri', cls='explicit', evidence='SRC FileSystemFacadeImpl.java:60-65; SRC FsModuleResolverImpl.java:42-50')

# SafFileSystem head: class initialisation, singleton construction, and the SAF branch of the facade.
e('SafFsModule.delete', 'SafFileSystem.<clinit>', 'CALL', 'First SAF use initialises the SAF file-system class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC SafFsModule.java:84-89; SRC SafFileSystem.java:66-70')
e('SafFileSystem.getInstance', 'SafFileSystem.<init>', 'CALL', 'SAF singleton accessor constructs the SAF file system', cls='explicit', evidence='SRC SafFileSystem.java:72-82; SRC SafFileSystem.java:84-87')
e('SafFsModule.delete', 'SafFileSystem.delete(Uri)', 'CALL', 'SAF module delete delegates to the SAF file system on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:84-89; SRC SafFileSystem.java:310-313')
e('SafFsModule.fileExists', 'SafFileSystem.exists(Uri)', 'CALL', 'SAF module file-exists check delegates to the SAF file system on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:136-139; SRC SafFileSystem.java:330-341')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan of this batch's classes — no REACHABLE method in
# this batch calls an UNREACHABLE method in bytecode. See REPORT.md.
SUPPRESS.update(set())
