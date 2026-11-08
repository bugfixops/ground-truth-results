# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g6/parts/b032.py; labels/kinds verified
# against staging-A1 merge-ready batch 32 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/032/ (one file per row).
# STRONGER-EVIDENCE UPGRADES (rule b): the merger-tree graph_def.py holds these keys
# with SOURCE evidence while the base part graded them INFERRED; the delivered part
# records SOURCE (never a downgrade). NOTE: merge-ready batch 32 grades them INFERRED,
# so the official harness reports a confirmed_by mismatch for exactly these keys;
# that mismatch is the deliberate, flagged override, for merger/auditor ruling:
#   UPGRADED to SOURCE: Torrent.writeToParcel
#   UPGRADED to SOURCE: Torrent$1.createFromParcel
#   UPGRADED to SOURCE: Torrent$1.newArray
# FLAG for merger/auditor: batch32-merge-ready.md header prose (line 7) says rows 2, 22, 37
# stay OPEN, but the file's final per-row table (last occurrence) marks all three REACHABLE
# INFERRED ("L2 verdict applied"); this part follows the final table, as the harness does.
# Batch 32 part (Torrent, TorrentTagInfo, BencodeFileItem, TorrentMetaInfo, BencodeFileTree).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b032_printed.txt. Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# SUPPRESS is empty by recomputation: auto_calls.json contains exactly 2 bytecode
# calls into this batch's UNREACHABLE rows, both from the UNREACHABLE own-CREATOR
# createFromParcel methods (BencodeFileItem, TorrentMetaInfo Parcel ctors);
# no REACHABLE method calls any UNREACHABLE row of this batch. See REPORT.md.

e('Torrent.<clinit>', 'Torrent$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC Torrent.java:157-170')
e('TorrentRepositoryImpl.replaceTags', 'TorrentTagInfo.<init>', 'CALL', 'Tag replacement builds TorrentTagInfo records', cls='explicit', evidence='SRC TorrentRepositoryImpl.java:125; TorrentTagInfo.java:54-60')
e('Utils.getFileList', 'BencodeFileItem.<clinit>', 'FRAMEWORK', 'First BencodeFileItem construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC Utils.java:142-145; BencodeFileItem.java:95-109')
e('Utils.getFileList', 'BencodeFileItem.<init>(String,int,long)', 'CALL', 'File listing builds a BencodeFileItem per storage file', cls='explicit', evidence='SRC Utils.java:142-145; BencodeFileItem.java:37-42')
e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileItem.compareTo', 'CALL', 'Sorting the file list dispatches to BencodeFileItem.compareTo', cls='non_standard', via='Collections.sort dispatch to Comparable.compareTo', evidence='INFERRED sort dispatch; SRC BencodeFileTreeUtils.java:55; BencodeFileItem.java:111-115')
e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileItem.getIndex', 'CALL', 'File-tree builder reads each file index', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:102-105; BencodeFileItem.java:71-74')
e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileItem.getPath', 'CALL', 'File-tree builder reads each file path', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:73-96; BencodeFileItem.java:51-54')
e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileItem.getSize', 'CALL', 'File-tree builder reads each file size', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:102-103; BencodeFileItem.java:61-64')
e('BencodeFileItem.<clinit>', 'BencodeFileItem$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC BencodeFileItem.java:95-109')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'TorrentMetaInfo.<clinit>', 'FRAMEWORK', 'First TorrentMetaInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC ui/addtorrent/AddTorrentViewModel.java:242; TorrentMetaInfo.java:149-163')
e('TorrentSessionImpl.addTorrent', 'TorrentMetaInfo.<init>(FileInputStream)', 'CALL', 'Add-torrent reads a torrent file into a TorrentMetaInfo', cls='explicit', evidence='SRC TorrentSessionImpl.java:299; TorrentMetaInfo.java:83-96')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'TorrentMetaInfo.<init>(String,String)', 'CALL', 'Magnet decode builds a TorrentMetaInfo from name and hash', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:242; TorrentMetaInfo.java:57-61')
e('TorrentDownloadImpl.handleMetadata', 'TorrentMetaInfo.<init>(TorrentInfo)', 'CALL', 'Metadata-received handler builds a TorrentMetaInfo from the torrent file', cls='explicit', evidence='SRC TorrentDownloadImpl.java:391-406; TorrentMetaInfo.java:73-81')
e('TorrentEngine.sendInfoToEmitter', 'TorrentMetaInfo.<init>(byte[])', 'CALL', 'Magnet bencode is decoded into a TorrentMetaInfo', cls='explicit', evidence='SRC TorrentEngine.java:461-464; TorrentMetaInfo.java:63-71')
e('TorrentMetaInfo.<init>(byte[])', 'TorrentMetaInfo.getMetaInfo', 'CALL', 'Byte-array ctor decodes the bencode through getMetaInfo', cls='explicit', evidence='SRC TorrentMetaInfo.java:66; TorrentMetaInfo.java:98-111')
e('TorrentMetaInfo.<clinit>', 'TorrentMetaInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC TorrentMetaInfo.java:149-163')
e('BencodeFileTreeUtils.makeObject', 'BencodeFileTree.<init>(int,String,long,int,BencodeFileTree)', 'CALL', 'File-tree object builder creates the file-node form', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:119-125; BencodeFileTree.java:40-44')

UNREACHABLE.update({
    'Torrent.writeToParcel': ('no_trigger_in_app',
        'No site parcels a Torrent; the dest.writeParcelable inside it parcels its Uri field, not a Torrent.',
        'SRC Torrent.java:142-155',
        'SOURCE'),
    'Torrent$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no printed unparcel site for Torrent.',
        'SRC Torrent.java:160-163',
        'SOURCE'),
    'Torrent$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC Torrent.java:166-169',
        'SOURCE'),
    'TorrentTagInfo.equals': ('no_trigger_in_app',
        'Objects are built only for DAO insert and delete; Room delete matches by primary key, not this equals.',
        'SRC TorrentTagInfo.java:63-71',
        'INFERRED'),
    'TorrentTagInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a TorrentTagInfo.',
        'SRC TorrentTagInfo.java:74-78',
        'INFERRED'),
    'TorrentTagInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a TorrentTagInfo value.',
        'SRC TorrentTagInfo.java:82-87',
        'INFERRED'),
    'BencodeFileItem.<init>(Parcel)': ('no_trigger_in_app',
        'Printed callers are only its own CREATOR and the never-invoked TorrentMetaInfo Parcel ctor via readTypedList.',
        'SRC BencodeFileItem.java:44-49',
        'INFERRED'),
    'BencodeFileItem.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no BencodeFileItem is ever marshalled app-side.',
        'SRC BencodeFileItem.java:82-85',
        'INFERRED'),
    'BencodeFileItem.setIndex': ('no_trigger_in_app',
        'Construction sets fields via the ctor; callers use getIndex, never setIndex.',
        'SRC BencodeFileItem.java:76-79',
        'INFERRED'),
    'BencodeFileItem.setPath': ('no_trigger_in_app',
        'Construction sets fields via the ctor; callers use getPath, never setPath.',
        'SRC BencodeFileItem.java:56-59',
        'INFERRED'),
    'BencodeFileItem.setSize': ('no_trigger_in_app',
        'Construction sets fields via the ctor; callers use getSize, never setSize.',
        'SRC BencodeFileItem.java:66-69',
        'INFERRED'),
    'BencodeFileItem.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a BencodeFileItem value.',
        'SRC BencodeFileItem.java:119-126',
        'INFERRED'),
    'BencodeFileItem.writeToParcel': ('no_trigger_in_app',
        'Only typed-list write is inside TorrentMetaInfo.writeToParcel, itself UNREACHABLE; no direct parcel site.',
        'SRC BencodeFileItem.java:88-93',
        'INFERRED'),
    'BencodeFileItem$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch, plus the dead-chain reference in TorrentMetaInfo Parcel ctor.',
        'SRC BencodeFileItem.java:99-102',
        'INFERRED'),
    'BencodeFileItem$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC BencodeFileItem.java:105-108',
        'INFERRED'),
    'TorrentMetaInfo.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in this batch); live constructions are non-parcel.',
        'SRC TorrentMetaInfo.java:113-127',
        'INFERRED'),
    'TorrentMetaInfo.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no TorrentMetaInfo is ever marshalled.',
        'SRC TorrentMetaInfo.java:129-132',
        'INFERRED'),
    'TorrentMetaInfo.equals': ('no_trigger_in_app',
        'Travels singly via Flowables; no List or Set of TorrentMetaInfo, no sort or contains use, no source call site.',
        'SRC TorrentMetaInfo.java:172-191',
        'INFERRED'),
    'TorrentMetaInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a TorrentMetaInfo.',
        'SRC TorrentMetaInfo.java:166-169',
        'INFERRED'),
    'TorrentMetaInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a TorrentMetaInfo value.',
        'SRC TorrentMetaInfo.java:195-209',
        'INFERRED'),
    'TorrentMetaInfo.writeToParcel': ('no_trigger_in_app',
        'No site parcels a TorrentMetaInfo; its writeTypedList is the dead-chain counterpart of BencodeFileItem.writeToParcel.',
        'SRC TorrentMetaInfo.java:135-147',
        'INFERRED'),
    'TorrentMetaInfo$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no printed unparcel site for TorrentMetaInfo.',
        'SRC TorrentMetaInfo.java:153-156',
        'INFERRED'),
    'TorrentMetaInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC TorrentMetaInfo.java:159-162',
        'INFERRED'),
})

# No REACHABLE method calls any UNREACHABLE row of this batch in auto_calls.json
# (recomputed), so no SUPPRESS entries apply.
SUPPRESS.update(set())
