# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch55 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 55 part (SafFileSystem + SafFsModule, SystemFacadeHelper/Impl, NormalizeUrl head).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b055_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# SafFileSystem internals: the FakePath chain and the stat chain.
e('SafFileSystem.getFile(FakePath,boolean)', 'SafFileSystem.getDir', 'CALL', 'FakePath file lookup walks intermediate directories through getDir', cls='explicit', evidence='SRC SafFileSystem.java:262-289; SRC SafFileSystem.java:291-303')
e('SafFileSystem.getFileUri(Uri,String,boolean)', 'SafFileSystem.getFile(DocumentFile,String,boolean)', 'CALL', 'Uri file-uri lookup reads the document tree through getFile', cls='explicit', evidence='SRC SafFileSystem.java:207-222; SRC SafFileSystem.java:248-260')
e('SafFileSystem.getFileUri(FakePath,boolean)', 'SafFileSystem.getFile(FakePath,boolean)', 'CALL', 'FakePath file-uri lookup reads the document tree through getFile', cls='explicit', evidence='SRC SafFileSystem.java:235-246; SRC SafFileSystem.java:262-289')
e('SafFsModule.getFileUri(Uri,String,boolean)', 'SafFileSystem.getFileUri(Uri,String,boolean)', 'CALL', 'SAF module file-uri query delegates to the SAF file system on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:71-74; SRC SafFileSystem.java:207-222')
e('SafFsModule.getFileUri(String,Uri)', 'SafFileSystem.getFileUri(FakePath,boolean)', 'CALL', 'SAF module relative file-uri query delegates to the SAF file system on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:77-81; SRC SafFileSystem.java:235-246')
e('Utils.isSafPath', 'SafFileSystem.getInstance', 'CALL', 'SAF-path test reaches the SAF singleton', cls='explicit', evidence='SRC Utils.java:657-658; SRC SafFileSystem.java:72-82')
e('SafFsModule.getParentDirUri', 'SafFileSystem.getParentDirUri', 'CALL', 'SAF module parent-dir query delegates to the SAF file system on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:158-161; SRC SafFileSystem.java:533-548')
e('Utils.isSafPath', 'SafFileSystem.isSafPath', 'CALL', 'SAF-path test delegates to the SAF file system check', cls='explicit', evidence='SRC Utils.java:657-658; SRC SafFileSystem.java:191-198')
e('SafFsModule.getDirAvailableBytes', 'SafFileSystem.makeSafRootDir', 'CALL', 'SAF module dir-bytes query builds the SAF root directory first', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:98-114; SRC SafFileSystem.java:369-373')
e('SafFsModule.getFilePath', 'SafFileSystem.stat(Uri)', 'CALL', 'SAF module file-path query stats the uri through the SAF file system', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:63-68; SRC SafFileSystem.java:459-470')
e('SafFileSystem.stat(Uri)', 'SafFileSystem.stat(DocumentFile)', 'CALL', 'Uri stat reads the document stat through the document stat', cls='explicit', evidence='SRC SafFileSystem.java:459-470; SRC SafFileSystem.java:487-493')
e('SafFsModule.getDirPath', 'SafFileSystem.statSafRoot', 'CALL', 'SAF module dir-path query stats the SAF root through the SAF file system', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC SafFsModule.java:55-60; SRC SafFileSystem.java:444-455')
e('SafFsModule.getFileUri(String,Uri)', 'SafFileSystem$FakePath.<init>', 'CALL', 'SAF module relative file-uri query builds a FakePath', cls='explicit', evidence='SRC SafFsModule.java:77-81; SRC SafFileSystem.java:98-102')
e('SafFileSystem.getFile(FakePath,boolean)', 'SafFileSystem$FakePath.makeRelativePathNodes', 'CALL', 'FakePath file lookup splits the relative path into nodes', cls='explicit', evidence='SRC SafFileSystem.java:262-289; SRC SafFileSystem.java:140-145')
e('SafFileSystem$FakePath.<init>', 'SafFileSystem$FakePath.normalizeRelativePath', 'CALL', 'FakePath construction normalises its relative path', cls='explicit', evidence='SRC SafFileSystem.java:98-102; SRC SafFileSystem.java:104-110')
e('SafFileSystem.getFile(FakePath,boolean)', 'SafFileSystem$FakePath.safRoot', 'CALL', 'FakePath file lookup reads the SAF root of the path', cls='explicit', evidence='SRC SafFileSystem.java:262-289; SRC SafFileSystem.java:147-150')
e('SafFileSystem$FakePath.toString', 'SafFileSystem$FakePath.serialize', 'CALL', 'FakePath string form serialises the path', cls='explicit', evidence='SRC SafFileSystem.java:164-167; SRC SafFileSystem.java:132-138')
e('SafFileSystem.getFileUri(FakePath,boolean)', 'SafFileSystem$FakePath.toString', 'CALL', 'FakePath file-uri lookup keys its cache on the FakePath string', cls='explicit', evidence='SRC SafFileSystem.java:235-246; SRC SafFileSystem.java:164-167')
e('SafFileSystem.stat(DocumentFile)', 'SafFileSystem$Stat.<init>', 'CALL', 'Document stat builds a Stat record', cls='explicit', evidence='SRC SafFileSystem.java:487-493; SRC SafFileSystem.java:177-184')

# SafFsModule through the FileSystemFacadeImpl dispatcher (FsModule interface dispatch; SAF branch).
e('FsModuleResolverImpl.<init>', 'SafFsModule.<init>', 'CALL', 'Resolver construction builds the SAF module', cls='explicit', evidence='SRC FsModuleResolverImpl.java:35-39; SRC SafFsModule.java:40-43')
e('FileSystemFacadeImpl.deleteFile', 'SafFsModule.delete', 'CALL', 'Facade delete dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:110-115; SRC SafFsModule.java:84-89')
e('FileSystemFacadeImpl.fileExists', 'SafFsModule.fileExists', 'CALL', 'Facade file-exists check dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:153-158; SRC SafFsModule.java:136-139')
e('SafFsModule.getDirAvailableBytes', 'SafFsModule.getAvailableBytes', 'CALL', 'SAF module dir-bytes query stats the volume through fstatvfs', cls='explicit', evidence='SRC SafFsModule.java:98-114; SRC SafFsModule.java:124-133')
e('FileSystemFacadeImpl.getDirAvailableBytes', 'SafFsModule.getDirAvailableBytes', 'CALL', 'Facade dir-bytes query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:268-274; SRC SafFsModule.java:98-114')
e('FileSystemFacadeImpl.getDirPath', 'SafFsModule.getDirPath', 'CALL', 'Facade dir-path query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:418-422; SRC SafFsModule.java:55-60')
e('FileSystemFacadeImpl.getFilePath', 'SafFsModule.getFilePath', 'CALL', 'Facade file-path query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:430-434; SRC SafFsModule.java:63-68')
e('FileSystemFacadeImpl.getFileUri(Uri,String)', 'SafFsModule.getFileUri(Uri,String,boolean)', 'CALL', 'Facade file-uri query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:122-129; SRC SafFsModule.java:71-74')
e('FileSystemFacadeImpl.getFileUri(String,Uri)', 'SafFsModule.getFileUri(String,Uri)', 'CALL', 'Facade relative file-uri query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:144-149; SRC SafFsModule.java:77-81')
e('FileSystemFacadeImpl.getParentDirUri', 'SafFsModule.getParentDirUri', 'CALL', 'Facade parent-dir query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:438-442; SRC SafFsModule.java:158-161')
e('FileSystemFacadeImpl.makeFileSystemPath(Uri,String)', 'SafFsModule.makeFileSystemPath', 'CALL', 'Facade path query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:254-259; SRC SafFsModule.java:151-155')
e('FileSystemFacadeImpl.getFD', 'SafFsModule.openFD', 'CALL', 'Facade fd query dispatches to the SAF module on the SAF branch', cls='non_standard', via='FsModule interface dispatch on the SAF branch', evidence='SRC FileSystemFacadeImpl.java:60-64; SRC SafFsModule.java:92-95')

# SystemFacadeHelper/Impl: construction and the SystemFacade interface dispatch.
e('TorrentEngine.<init>', 'SystemFacadeHelper.getFileSystemFacade', 'CALL', 'Engine construction acquires the file-system facade', cls='explicit', evidence='SRC TorrentEngine.java:128-132; SRC SystemFacadeHelper.java:39-46')
e('TorrentEngine.<init>', 'SystemFacadeHelper.getSystemFacade', 'CALL', 'Engine construction acquires the system facade', cls='explicit', evidence='SRC TorrentEngine.java:128-138; SRC SystemFacadeHelper.java:31-37')
e('SystemFacadeHelper.getSystemFacade', 'SystemFacadeImpl.<init>', 'CALL', 'System facade helper constructs the system facade implementation', cls='explicit', evidence='SRC SystemFacadeHelper.java:31-37; SRC SystemFacadeImpl.java:38-41')
e('Utils.checkConnectivity', 'SystemFacadeImpl.getActiveNetworkInfo', 'CALL', 'Connectivity check reads the active network through the system facade', cls='non_standard', via='SystemFacade interface dispatch', evidence='SRC Utils.java:157-162; SRC SystemFacadeImpl.java:44-49')
e('MainActivity.initAboutDialog', 'SystemFacadeImpl.getAppVersionName', 'CALL', 'About dialog reads the app version through the system facade', cls='explicit', evidence='SRC ui/main/MainActivity.java:776-785; SRC SystemFacadeImpl.java:72-83')
e('Utils.isNetworkTypeAllowed', 'SystemFacadeImpl.getNetworkCapabilities', 'CALL', 'Network-type check reads the network capabilities through the system facade', cls='non_standard', via='SystemFacade interface dispatch', evidence='SRC Utils.java:174; SRC SystemFacadeImpl.java:53-61')
e('Utils.isNetworkTypeAllowed', 'SystemFacadeImpl.isActiveNetworkMetered', 'CALL', 'Network-type check reads the metered state through the system facade', cls='non_standard', via='SystemFacade interface dispatch', evidence='SRC Utils.java:183; SRC SystemFacadeImpl.java:64-69')

# NormalizeUrl head: class initialisation and the doNormalize entry.
e('DetailTorrentFragment.addTrackers', 'NormalizeUrl.<clinit>', 'CALL', 'First URL normalisation initialises the normaliser class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:719-726; SRC NormalizeUrl.java:36-40')
e('NormalizeUrl.normalize(String,Options)', 'NormalizeUrl.doNormalize', 'CALL', 'Two-arg normalise runs the normalisation routine', cls='explicit', evidence='SRC NormalizeUrl.java:178-189; SRC NormalizeUrl.java:191')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# SUPPRESS: bytecode/auto edges from this batch's REACHABLE doNormalize
# into batch-56 UNREACHABLE methods (intra-group G11: batches 53-57).
# doNormalize calls join at NormalizeUrl.java:268 only inside the
# never-taken removeDirectoryIndex branch (default empty), decode at
# :217 only inside the never-taken decode branch (all 3 callers set
# decode=false), and triggers PercentEncoder class initialisation at
# :217 on the same never-taken branch. See REPORT.md.
SUPPRESS.update({
    'NormalizeUrl.join',
    'PercentEncoder.decode',
    'PercentEncoder.<clinit>',
})
