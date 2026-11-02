# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g6/parts/b029.py; labels/kinds verified
# against staging-A1 merge-ready batch 29 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/029/ (one file per row).
# STRONGER-EVIDENCE UPGRADES (rule b): the merger-tree graph_def.py holds these keys
# with SOURCE evidence while the base part graded them INFERRED; the delivered part
# records SOURCE (never a downgrade). NOTE: merge-ready batch 29 grades them INFERRED,
# so the official harness reports a confirmed_by mismatch for exactly these keys;
# that mismatch is the deliberate, flagged override, for merger/auditor ruling:
#   UPGRADED to SOURCE: MagnetInfo.writeToParcel
#   UPGRADED to SOURCE: MagnetInfo$1.createFromParcel
#   UPGRADED to SOURCE: MagnetInfo$1.newArray
# Batch 29 part (MagnetInfo, PeerInfo, Priority, ReadPieceInfo, SessionStats).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b029_printed.txt. Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# SUPPRESS is empty by recomputation: auto_calls.json contains exactly 4 bytecode
# calls into this batch's UNREACHABLE rows, all from the UNREACHABLE own-CREATOR
# createFromParcel methods (MagnetInfo, PeerInfo, SessionStats Parcel ctors);
# no REACHABLE method calls any UNREACHABLE row of this batch. See REPORT.md.

e('MagnetInfo.<clinit>', 'MagnetInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC MagnetInfo.java:79-93')
e('TorrentDownloadImpl.getPeerInfoList', 'PeerInfo.<clinit>', 'FRAMEWORK', 'First PeerInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentDownloadImpl.java:911-924; PeerInfo.java:166-180')
e('PeerItem.<init>', 'PeerInfo.<init>(String,String,long,long,double,int,int,int,int,int)', 'CALL', 'PeerItem ctor passes its 10 fields to the 10-arg PeerInfo super ctor', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerItem.java:26-31; PeerInfo.java:72-91')
e('TorrentDownloadImpl.getPeerInfoList', 'PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)', 'CALL', 'Peer list builder constructs a PeerInfo per advanced peer', cls='explicit', evidence='SRC TorrentDownloadImpl.java:911-924; PeerInfo.java:56-70')
e('PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)', 'PeerInfo.calcRelevance', 'CALL', '2-arg PeerInfo ctor computes relevance from peer and status', cls='explicit', evidence='SRC PeerInfo.java:64,122-141')
e('PeerListAdapter.submitList', 'PeerInfo.compareTo', 'CALL', 'Sorting the peer-item list dispatches to PeerInfo.compareTo (PeerItem does not override it)', cls='non_standard', via='Collections.sort dispatch to Comparable.compareTo', evidence='INFERRED sort dispatch; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:77-80; PeerInfo.java:183-185')
e('TorrentInfoProvider.makePeersInfoFlowable', 'PeerInfo.equals', 'CALL', 'Peer-list containsAll check dispatches to element equals', cls='non_standard', via='List.containsAll dispatch to element equals', evidence='INFERRED library dispatch; SRC TorrentInfoProvider.java:396-399; PeerInfo.java:209-229')
e('PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)', 'PeerInfo.getConnectionType', 'CALL', '2-arg PeerInfo ctor derives the connection type from the peer', cls='explicit', evidence='SRC PeerInfo.java:65,108-120')
e('PeerInfo.<clinit>', 'PeerInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC PeerInfo.java:166-180')
e('PriorityConverter.<clinit>', 'Priority.<clinit>', 'FRAMEWORK', 'PriorityConverter static initialisers reference Priority constants, loading the Priority enum', cls='non_standard', via='JVM class initialization on first constant reference', evidence='INFERRED JVM class initialization; SRC PriorityConverter.java:31-52; Priority.java:27-56')
e('Priority.<clinit>', 'Priority.<init>', 'CALL', 'Enum initialisation constructs each Priority constant', cls='non_standard', via='JVM enum constant construction during <clinit>', evidence='INFERRED JVM enum construction; SRC Priority.java:27-61')
e('FilePriority.getPriority', 'Priority.fromValue', 'CALL', 'File priority converts its stored int through Priority.fromValue', cls='explicit', evidence='SRC FilePriority.java:48-51; Priority.java:70-78')
e('PriorityConverter.convert(Priority)', 'Priority.value', 'CALL', 'Priority-to-library conversion reads the app priority value', cls='explicit', evidence='SRC PriorityConverter.java:94-101; Priority.java:65-68')
e('TorrentDownloadImpl.handleReadPiece', 'ReadPieceInfo.<init>', 'CALL', 'Read-piece alert handler builds a ReadPieceInfo for listeners', cls='explicit', evidence='SRC TorrentDownloadImpl.java:442-450; ReadPieceInfo.java:31-37')
e('TorrentSessionImpl.handleStats', 'SessionStats.<clinit>', 'FRAMEWORK', 'First SessionStats construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentSessionImpl.java:1168-1179; SessionStats.java:79-93')
e('TorrentSessionImpl.handleStats', 'SessionStats.<init>(long,long,long,long,long,int)', 'CALL', 'Stats handler builds a SessionStats for listeners', cls='explicit', evidence='SRC TorrentSessionImpl.java:1173-1174; SessionStats.java:36-46')
e('TorrentInfoProvider.makeSessionStatsFlowable', 'SessionStats.equals', 'CALL', 'Session-stats flowable compares the new stats with the previous ones', cls='explicit', evidence='SRC TorrentInfoProvider.java:480-482; SessionStats.java:116-133')
e('SessionStats.<clinit>', 'SessionStats$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC SessionStats.java:79-93')

UNREACHABLE.update({
    'MagnetInfo.getUri': ('no_trigger_in_app',
        'All getUri hits are other classes; MagnetInfo callers use getName, getSha1hash and getFilePriorities instead; auto_calls.json has 0 hits.',
        'SRC MagnetInfo.java:95-98',
        'INFERRED'),
    'MagnetInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a MagnetInfo.',
        'SRC MagnetInfo.java:115-119',
        'INFERRED'),
    'MagnetInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a MagnetInfo value.',
        'SRC MagnetInfo.java:121-131',
        'INFERRED'),
    'MagnetInfo.writeToParcel': ('no_trigger_in_app',
        'No site parcels a MagnetInfo; live uses are fetchMagnet and parseMagnet returns, never a parcel argument.',
        'SRC MagnetInfo.java:70-77',
        'SOURCE'),
    'MagnetInfo$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no getParcelable read of a MagnetInfo and no CREATOR reference outside MagnetInfo.java.',
        'SRC MagnetInfo.java:82-86',
        'SOURCE'),
    'MagnetInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC MagnetInfo.java:88-92',
        'SOURCE'),
    'PeerInfo.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in this batch); no marshalling site for PeerInfo.',
        'SRC PeerInfo.java:92-106',
        'INFERRED'),
    'PeerInfo.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels a PeerInfo.',
        'SRC PeerInfo.java:143-147',
        'INFERRED'),
    'PeerInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a PeerInfo.',
        'SRC PeerInfo.java:188-206',
        'INFERRED'),
    'PeerInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a PeerInfo value.',
        'SRC PeerInfo.java:231-247',
        'INFERRED'),
    'PeerInfo.writeToParcel': ('no_trigger_in_app',
        'No site parcels a PeerInfo.',
        'SRC PeerInfo.java:149-164',
        'INFERRED'),
    'PeerInfo$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no printed unparcel site for PeerInfo.',
        'SRC PeerInfo.java:170-173',
        'INFERRED'),
    'PeerInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC PeerInfo.java:176-179',
        'INFERRED'),
    'ReadPieceInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a ReadPieceInfo value.',
        'SRC ReadPieceInfo.java:39-49',
        'INFERRED'),
    'SessionStats.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in this batch); no marshalling site for SessionStats.',
        'SRC SessionStats.java:48-58',
        'INFERRED'),
    'SessionStats.compareTo': ('no_trigger_in_app',
        'No printed sort or comparison site for SessionStats objects.',
        'SRC SessionStats.java:110-114',
        'INFERRED'),
    'SessionStats.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels a SessionStats.',
        'SRC SessionStats.java:60-64',
        'INFERRED'),
    'SessionStats.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a SessionStats.',
        'SRC SessionStats.java:95-109',
        'INFERRED'),
    'SessionStats.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a SessionStats value.',
        'SRC SessionStats.java:135-147',
        'INFERRED'),
    'SessionStats.writeToParcel': ('no_trigger_in_app',
        'No site parcels a SessionStats.',
        'SRC SessionStats.java:66-77',
        'INFERRED'),
    'SessionStats$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no printed unparcel site for SessionStats.',
        'SRC SessionStats.java:82-86',
        'INFERRED'),
    'SessionStats$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC SessionStats.java:88-92',
        'INFERRED'),
})

# No REACHABLE method calls any UNREACHABLE row of this batch in auto_calls.json
# (recomputed), so no SUPPRESS entries apply.
SUPPRESS.update(set())
