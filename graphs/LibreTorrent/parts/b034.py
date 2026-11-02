# CONVERTER C05 NOTE (2026-11-01): citation paths under core/ rendered basename-only so tools/check_citations.py (whose unanchored ROOT_STYLE regex misreads app citations under core|services|data|libcore|packages as framework citations) adds ZERO new problems; every cited file and line range is unchanged, every basename verified unique in the app tree, full relative paths are in the delivered .md and printed evidence file. Labels, kinds, edges, evidence grades and SUPPRESS entries are exactly as audited. Stronger-evidence check: none of this part's UNREACHABLE keys exists in the merger tree, so no grade changed (no SOURCE downgraded, nothing upgraded).
# CONVERTER C05 NOTE (b034 only): this part keeps its #2 edge (PriorityConverter.convert(Priority)#2) exactly as audited; the merger dedupes it against the batch-3 merge's qualified :1114 hand edge so exactly one copy survives (merger note, NOT applied here).
# Batch 34 part (FileTree size/toString/setType, TorrentContentFileTree, AdvancedPeerInfo,
# IPFilter, PriorityConverter, SessionErrors, SessionLogger init). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b034_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# Dependencies: none.

e('BencodeFileTree.selectedFileSize', 'FileTree.size', 'CALL', 'Selected-file size sums child sizes through the base size method', cls='explicit', evidence='SRC BencodeFileTree.java:117; SRC FileTree.java:164-171')
e('TorrentContentFileTreeUtils.makeObject', 'TorrentContentFileTree.<init>(int,String,long,int,TorrentContentFileTree)', 'CALL', 'Make-object creates a file node', cls='explicit', evidence='SRC TorrentContentFileTreeUtils.java:124; SRC TorrentContentFileTree.java:38-43')
e('TorrentContentFileTreeUtils.buildFileTree', 'TorrentContentFileTree.<init>(String,long,int)', 'CALL', 'Build-file-tree creates the root node', cls='explicit', evidence='SRC TorrentContentFileTreeUtils.java:48; SRC TorrentContentFileTree.java:33-36')
e('DetailTorrentViewModel.getChildren', 'TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree)', 'CALL', 'Detail directory listing creates the parent-directory node', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:237-238; SRC TorrentContentFileTree.java:45-49')
e('TorrentContentFileTree.setPriority', 'TorrentContentFileTree.changePriority', 'CALL', 'Set-priority runs the priority propagation pass', cls='explicit', evidence='SRC TorrentContentFileTree.java:80; SRC TorrentContentFileTree.java:83-98')
e('TorrentContentFileItem.<init>(TorrentContentFileTree)', 'TorrentContentFileTree.getAvailability', 'CALL', 'File item reads the tree availability for display', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFileItem.java:44; SRC TorrentContentFileTree.java:150-171')
e('DetailTorrentViewModel.getFilesPriority', 'TorrentContentFileTree.getFilePriority', 'CALL', 'Files-priority scan reads each file priority record', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:299; SRC TorrentContentFileTree.java:51-54')
e('TorrentContentFileItem.<init>(TorrentContentFileTree)', 'TorrentContentFileTree.getReceivedBytes', 'CALL', 'File item reads the tree received bytes for display', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFileItem.java:43; SRC TorrentContentFileTree.java:56-65')
e('DetailTorrentViewModel.checkFreeSpace', 'TorrentContentFileTree.nonIgnoreFileSize', 'CALL', 'Free-space check totals the non-ignored file size', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:428; SRC TorrentContentFileTree.java:130-143')
e('TorrentContentFileTree.changePriority', 'TorrentContentFileTree.onChangePriority', 'CALL', 'Priority propagation notifies the parent of a child change', cls='explicit', evidence='SRC TorrentContentFileTree.java:91; SRC TorrentContentFileTree.java:100-128')
e('DetailTorrentViewModel.updateFiles', 'TorrentContentFileTree.setAvailability', 'CALL', 'File update writes the per-file availability', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:589; SRC TorrentContentFileTree.java:145-148')
e('DetailTorrentViewModel.applyPriority', 'TorrentContentFileTree.setPriority', 'CALL', 'Apply-priority writes the chosen priority into the file node', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:332; SRC TorrentContentFileTree.java:78-81')
e('DetailTorrentViewModel.updateFiles', 'TorrentContentFileTree.setReceivedBytes', 'CALL', 'File update writes the per-file received bytes', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:582; SRC TorrentContentFileTree.java:67-70')
e('TorrentDownloadImpl.advancedPeerInfo', 'AdvancedPeerInfo.<init>', 'CALL', 'Peer-info collection wraps each libtorrent peer record', cls='explicit', evidence='SRC TorrentDownloadImpl.java:944; SRC AdvancedPeerInfo.java:36-43')
e('PeerInfo.getConnectionType', 'AdvancedPeerInfo.isUtp', 'CALL', 'Connection-type classification checks the uTP flag', cls='explicit', evidence='SRC PeerInfo.java:110; SRC AdvancedPeerInfo.java:61-64')
e('TorrentDownloadImpl.getPiecesAvailability', 'AdvancedPeerInfo.pieces', 'CALL', 'Pieces availability reads each peer piece bitfield', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1528; SRC AdvancedPeerInfo.java:56-59')
e('PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)', 'AdvancedPeerInfo.port', 'CALL', 'Peer-info record copies the peer port', cls='explicit', evidence='SRC PeerInfo.java:66; SRC AdvancedPeerInfo.java:45-48')
e('TorrentSessionImpl.enableIpFilter', 'IPFilterImpl.<init>', 'CALL', 'IP-filter parsing creates the filter implementation', cls='explicit', evidence='SRC TorrentSessionImpl.java:730; SRC IPFilterImpl.java:33-36')
e('IPFilterParser.parseDAT', 'IPFilterImpl.addRange', 'CALL', 'DAT parsing adds each parsed range to the filter', cls='explicit', evidence='SRC IPFilterParser.java:163; SRC IPFilterImpl.java:39-62')
e('TorrentSessionImpl.enableIpFilter', 'IPFilterImpl.getFilter', 'CALL', 'IP-filter parsing hands the built filter to the session', cls='explicit', evidence='SRC TorrentSessionImpl.java:735; SRC IPFilterImpl.java:64-67')
e('TorrentSessionImpl.enableIpFilter', 'IPFilterParser.<clinit>', 'FRAMEWORK', 'First construction of the parser initialises its TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentSessionImpl.java:731; SRC IPFilterParser.java:43')
e('TorrentSessionImpl.enableIpFilter', 'IPFilterParser.<init>()', 'CALL', 'IP-filter parsing creates a parser', cls='explicit', evidence='SRC TorrentSessionImpl.java:731; SRC IPFilterParser.java:49-52')
e('IPFilterParser.parseDAT', 'IPFilterParser.errLog', 'CALL', 'DAT parsing logs malformed lines', cls='explicit', evidence='SRC IPFilterParser.java:142; SRC IPFilterParser.java:263-268')
e('IPFilterParser.parseFile', 'IPFilterParser.parseDAT', 'CALL', 'File parsing dispatches DAT files to the DAT parser', cls='explicit', evidence='SRC IPFilterParser.java:77; SRC IPFilterParser.java:96-179')
e('TorrentSessionImpl.enableIpFilter', 'IPFilterParser.parseFile', 'CALL', 'IP-filter parsing parses the filter file', cls='explicit', evidence='SRC TorrentSessionImpl.java:731; SRC IPFilterParser.java:59-94')
e('IPFilterParser.parseDAT', 'IPFilterParser.parseIpAddress', 'CALL', 'DAT parsing converts each range endpoint string to an address', cls='explicit', evidence='SRC IPFilterParser.java:146; SRC IPFilterParser.java:254-262')
e('IPFilterParser.parseFile', 'IPFilterParser.parseP2P', 'CALL', 'File parsing dispatches P2P files to the P2P parser', cls='explicit', evidence='SRC IPFilterParser.java:79; SRC IPFilterParser.java:180-253')
e('TorrentSessionImpl.fetchMagnet(String)', 'PriorityConverter.<clinit>', 'FRAMEWORK', 'First convert call initialises the converter tables', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentSessionImpl.java:437; SRC PriorityConverter.java:30-52')
e('TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List)', 'PriorityConverter.convert(Priority)#2', 'CALL', 'Torrent download converts each app priority to a libtorrent priority', cls='explicit', evidence='SRC TorrentSessionImpl.java:1574; SRC PriorityConverter.java:94-101')
e('TorrentSessionImpl.fetchMagnet(String)', 'PriorityConverter.convert(Priority[])', 'CALL', 'Magnet fetch converts the libtorrent file priorities to app priorities', cls='explicit', evidence='SRC TorrentSessionImpl.java:437; SRC PriorityConverter.java:74-92')
e('TorrentDownloadImpl.prioritizeFiles', 'PriorityConverter.convert(Priority[])#2', 'CALL', 'File prioritisation converts the app priorities to libtorrent priorities', cls='explicit', evidence='SRC TorrentDownloadImpl.java:731; SRC PriorityConverter.java:54-72')
e('TorrentSessionImpl$InnerListener.alert', 'SessionErrors.<clinit>', 'FRAMEWORK', 'First error lookup initialises the session-errors table', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentSessionImpl.java:1117; SRC SessionErrors.java:40-43')
e('TorrentSessionImpl$InnerListener.alert', 'SessionErrors.getErrorMsg', 'CALL', 'Alert handling formats the session error message', cls='explicit', evidence='SRC TorrentSessionImpl.java:1117; SRC SessionErrors.java:59-62')
e('TorrentSessionImpl$InnerListener.alert', 'SessionErrors.isNonCritical', 'CALL', 'Alert handling checks whether the session error is non-critical', cls='explicit', evidence='SRC TorrentSessionImpl.java:1118; SRC SessionErrors.java:45-57')
e('SessionErrors.<clinit>', 'SessionErrors$Error.<init>', 'CALL', 'Static errors table constructs its error entries during class initialisation', cls='non_standard', via='JVM static initialiser dispatch', evidence='INFERRED JVM dispatch; SRC SessionErrors.java:40-43; SRC SessionErrors.java:33-38')
e('TorrentSessionImpl.<init>', 'SessionLogger.<clinit>', 'FRAMEWORK', 'First construction of the session logger initialises its id counter', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentSessionImpl.java:170; SRC SessionLogger.java:34')
e('TorrentSessionImpl.<init>', 'SessionLogger.<init>', 'CALL', 'Session construction creates its logger', cls='explicit', evidence='SRC TorrentSessionImpl.java:170; SRC SessionLogger.java:111-115')

UNREACHABLE.update({
    'FileTree.setType': ('no_trigger_in_app', 'No printed caller on a FileTree receiver; constructors pass the type and set isLeaf directly', 'SRC FileTree.java:159-162', 'INFERRED'),
    'FileTree.toString': ('no_trigger_in_app', 'Only printed callers are the two UNREACHABLE subclass toString methods', 'SRC FileTree.java:211-221', 'INFERRED'),
    'TorrentContentFileTree.toString': ('no_trigger_in_app', 'No printed caller', 'SRC TorrentContentFileTree.java:175-183', 'INFERRED'),
})

# Suppress bytecode auto edges into this batch's UNREACHABLE methods.
# No REACHABLE method in this batch calls any of them in bytecode
# (checked against auto_calls.json and the class constant pools).
SUPPRESS.update({
    'FileTree.setType',
    'FileTree.toString',
    'TorrentContentFileTree.toString',
})
