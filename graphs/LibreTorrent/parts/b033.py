# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g7/parts/b033.py; labels/kinds verified
# against staging-A1 merge-ready batch 33 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/033/ (one file per row).
# Stronger-evidence check (rule b): no UNREACHABLE key of this batch is held in
# the merger-tree graph_def.py or merged parts with a conflicting grade; no grade changed.
# Batch 33 part (BencodeFileTree, FilePriority, FileTree). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b033_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# Dependencies: none.

e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileTree.<init>(String,long,int)', 'CALL', 'Build-file-tree creates the root node', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:48; SRC BencodeFileTree.java:35-38')
e('BencodeFileTreeUtils.makeObject', 'BencodeFileTree.<init>(String,long,int,BencodeFileTree)', 'CALL', 'Make-object creates a directory node', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:125; SRC BencodeFileTree.java:45-48')
e('BencodeFileTree.select', 'BencodeFileTree.doSelect', 'CALL', 'Select runs the recursive selection pass', cls='explicit', evidence='SRC BencodeFileTree.java:63; SRC BencodeFileTree.java:66-79')
e('AddTorrentViewModel.getSelectedFileIndexes', 'BencodeFileTree.isSelected', 'CALL', 'Selected-file indexes read each leaf selection flag', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:460; SRC BencodeFileTree.java:50-53')
e('BencodeFileTree.doSelect', 'BencodeFileTree.onChildSelectChange', 'CALL', 'Selection pass notifies the parent of a child change', cls='explicit', evidence='SRC BencodeFileTree.java:72; SRC BencodeFileTree.java:85-87')
e('AddTorrentViewModel.makeFileTree', 'BencodeFileTree.select', 'CALL', 'Add-torrent file tree selects all files by default', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:384; SRC BencodeFileTree.java:61-64')
e('AddTorrentViewModel.checkFreeSpace', 'BencodeFileTree.selectedFileSize', 'CALL', 'Free-space check totals the selected file size', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:553; SRC BencodeFileTree.java:107-121')
e('BencodeFileTreeUtils.buildFileTree', 'FileNode$Type.<clinit>', 'FRAMEWORK', 'First use of the DIR constant initialises the file-node type class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC BencodeFileTreeUtils.java:48; SRC FileNode.java:32-36')
e('DetailTorrentViewModel.makeFileTree', 'FilePriority.<init>(Priority)', 'CALL', 'Detail file tree builds a priority record per torrent priority', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:549; SRC FilePriority.java:36-40')
e('DetailTorrentViewModel.getFilesPriority', 'FilePriority.<init>(Type)', 'CALL', 'Mixed-priority result builds a MIXED priority record', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:323; SRC FilePriority.java:42-46')
e('DetailTorrentViewModel.getFilesPriority', 'FilePriority.equals', 'CALL', 'Files-priority scan compares the random priority against each file priority', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:313; SRC FilePriority.java:92-103')
e('DetailTorrentViewModel.getFilePriorities', 'FilePriority.getPriority', 'CALL', 'File-priorities array reads each file priority value', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:420; SRC FilePriority.java:48-51')
e('TorrentContentFileTree.changePriority', 'FilePriority.getType', 'CALL', 'Priority propagation reads each child priority type', cls='explicit', evidence='SRC TorrentContentFileTree.java:96; SRC FilePriority.java:53-56')
e('FilePriority.<init>(Type)', 'FilePriority.priorityFrom', 'CALL', 'Type constructor derives the numeric priority from the type', cls='explicit', evidence='SRC FilePriority.java:44; SRC FilePriority.java:77-89')
e('FilePriority.<init>(Priority)', 'FilePriority.typeFrom', 'CALL', 'Priority constructor derives the type from the priority', cls='explicit', evidence='SRC FilePriority.java:39; SRC FilePriority.java:58-75')
e('DetailTorrentViewModel.getFilesPriority', 'FilePriority$Type.<clinit>', 'FRAMEWORK', 'First use of the MIXED constant initialises the priority-type enum', cls='non_standard', via='JVM enum initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/detailtorrent/DetailTorrentViewModel.java:323; SRC FilePriority.java:34')
e('BencodeFileTreeUtils.buildFileTree', 'FileTree.<clinit>', 'FRAMEWORK', 'First use of the ROOT constant initialises the file-tree class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC BencodeFileTreeUtils.java:48; SRC FileTree.java:40-42')
e('BencodeFileTree.<init>(int,String,long,int,BencodeFileTree)', 'FileTree.<init>(int,String,long,int,FileTree)', 'CALL', 'Five-arg bencode node passes its fields to the file-tree base constructor', cls='explicit', evidence='SRC BencodeFileTree.java:42; SRC FileTree.java:66-73')
e('BencodeFileTree.<init>(String,long,int)', 'FileTree.<init>(String,long,int)', 'CALL', 'Three-arg bencode node passes its fields to the file-tree base constructor', cls='explicit', evidence='SRC BencodeFileTree.java:37; SRC FileTree.java:51-54')
e('BencodeFileTree.<init>(String,long,int,BencodeFileTree)', 'FileTree.<init>(String,long,int,FileTree)', 'CALL', 'Four-arg bencode node passes its fields and parent to the file-tree base constructor', cls='explicit', evidence='SRC BencodeFileTree.java:47; SRC FileTree.java:56-59')
e('BencodeFileTreeUtils.buildFileTree', 'FileTree.addChild', 'CALL', 'Build-file-tree attaches each new leaf to its parent tree', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:106; SRC FileTree.java:75-78')
e('BencodeFileTreeUtils.buildFileTree', 'FileTree.contains', 'CALL', 'Build-file-tree checks whether a path node already exists', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:100; SRC FileTree.java:80-83')
e('BencodeFileTreeUtils.buildFileTree', 'FileTree.getChild', 'CALL', 'Build-file-tree walks down to the child node for the next path segment', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:109; SRC FileTree.java:85-88')
e('AddTorrentViewModel.getChildren', 'FileTree.getChildren', 'CALL', 'Add-torrent directory listing reads the current directory children', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:420; SRC FileTree.java:90-93')
e('BencodeFileTree.doSelect', 'FileTree.getChildrenCount', 'CALL', 'Selection pass checks whether the node has children before recursing', cls='explicit', evidence='SRC BencodeFileTree.java:75; SRC FileTree.java:110-113')
e('AddTorrentViewModel.getSelectedFileIndexes', 'FileTree.getIndex', 'CALL', 'Selected-file indexes read each leaf file index', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:461; SRC FileTree.java:147-150')
e('FileTree.addChild', 'FileTree.getName', 'CALL', 'Add-child keys the child by its name', cls='explicit', evidence='SRC FileTree.java:77; SRC FileTree.java:137-140')
e('AddTorrentViewModel.getChildren', 'FileTree.getParent', 'CALL', 'Add-torrent directory listing checks the current directory parent', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:417; SRC FileTree.java:120-123')
e('DetailTorrentViewModel.getFilePath', 'FileTree.getPath', 'CALL', 'Detail file path walks the node parents to build the relative path', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:268; SRC FileTree.java:173-184')
e('BencodeFileTreeUtils.buildFileTree', 'FileTree.isFile', 'CALL', 'Build-file-tree skips descending into leaf nodes', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:111; SRC FileTree.java:115-118')

UNREACHABLE.update({
    'BencodeFileTree.toString': ('no_trigger_in_app', 'No printed caller; its body calls FileTree.toString, not vice versa', 'SRC BencodeFileTree.java:125-131', 'INFERRED'),
    'FilePriority.toString': ('no_trigger_in_app', 'No printed caller', 'SRC FilePriority.java:107-113', 'INFERRED'),
    'FileTree.compareTo': ('no_trigger_in_app', 'No printed sort or comparison of FileTree objects; nearby sorts sort BencodeFileItem lists', 'SRC FileTree.java:187-190', 'INFERRED'),
    'FileTree.equals': ('no_trigger_in_app', 'No printed caller on a FileTree receiver; contains(String) is a String-key map lookup', 'SRC FileTree.java:193-207', 'INFERRED'),
    'FileTree.getChildrenIndexes': ('no_trigger_in_app', 'Definition only; callers use getChildren() plus per-child getIndex()', 'SRC FileTree.java:100-108', 'INFERRED'),
    'FileTree.getChildrenName': ('no_trigger_in_app', 'Definition only; callers use getChildren()', 'SRC FileTree.java:95-98', 'INFERRED'),
    'FileTree.getType': ('no_trigger_in_app', 'No printed caller on a FileTree receiver; in-tree code reads isFile() instead', 'SRC FileTree.java:153-156', 'INFERRED'),
    'FileTree.setIndex': ('no_trigger_in_app', 'No printed caller; constructors set the field directly', 'SRC FileTree.java:142-145', 'INFERRED'),
    'FileTree.setName': ('no_trigger_in_app', 'No printed caller on a FileTree receiver; constructors set the field directly', 'SRC FileTree.java:131-134', 'INFERRED'),
    'FileTree.setParent': ('no_trigger_in_app', 'No printed caller; constructors set the field directly', 'SRC FileTree.java:125-128', 'INFERRED'),
})

# Suppress bytecode auto edges into this batch's UNREACHABLE methods.
# No REACHABLE method in this batch calls any of them in bytecode
# (checked against auto_calls.json and the class constant pools; the only
# bytecode callers of FileTree.toString are the two UNREACHABLE toString
# methods themselves, which this bare-name set also covers).
SUPPRESS.update({
    'BencodeFileTree.toString',
    'FilePriority.toString',
    'FileTree.compareTo',
    'FileTree.equals',
    'FileTree.getChildrenIndexes',
    'FileTree.getChildrenName',
    'FileTree.getType',
    'FileTree.setIndex',
    'FileTree.setName',
    'FileTree.setParent',
})
