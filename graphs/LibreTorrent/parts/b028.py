# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g6/parts/b028.py; labels/kinds verified
# against staging-A1 merge-ready batch 28 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/028/ (one file per row).
# Stronger-evidence check (rule b): no UNREACHABLE key of this batch is held in
# the merger-tree graph_def.py or merged parts with a conflicting grade; no grade changed.
# Batch 28 part (TorrentInfoProvider listeners, AbstractInfoParcel, AdvancedTorrentInfo, MagnetInfo).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b028_printed.txt. Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# SUPPRESS is empty by recomputation, not by omission: auto_calls.json contains
# exactly 8 bytecode calls into this batch's UNREACHABLE rows, all from the
# UNREACHABLE own-CREATOR createFromParcel methods (AdvancedTorrentInfo, MagnetInfo
# Parcel ctors); no REACHABLE method calls any UNREACHABLE row of this batch
# in auto_calls.json, and javap spot-checks confirm the same pairs. See REPORT.md.

e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.<init>', 'CALL', 'Info flowable creates its engine listener', cls='explicit', evidence='SRC TorrentInfoProvider.java:147')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.onRestoreSessionError', 'CALL', 'Registered listener receives restore-session-error events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentSessionImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:173-182,214; TorrentSessionImpl.java:1527-1529')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.onSessionStats', 'CALL', 'Registered listener receives session-stats events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentSessionImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:195-204,214; TorrentSessionImpl.java:1168-1178')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.onTorrentError', 'CALL', 'Registered listener receives torrent-error events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:184-194,214; TorrentDownloadImpl.java:333-336,421-424')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.onTorrentPaused', 'CALL', 'Registered listener receives torrent-paused events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:162-172,214; TorrentDownloadImpl.java:237-240')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfoProvider$1.onTorrentStateChanged', 'CALL', 'Registered listener receives torrent-state-changed events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:149-161,214; TorrentDownloadImpl.java:224-230')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.<init>', 'CALL', 'Info-list flowable creates its engine listener', cls='explicit', evidence='SRC TorrentInfoProvider.java:253')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onRestoreSessionError', 'CALL', 'Registered listener receives restore-session-error events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentSessionImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:272-276,293; TorrentSessionImpl.java:1527-1529')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onSessionStats', 'CALL', 'Registered listener receives session-stats events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentSessionImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:282-286,293; TorrentSessionImpl.java:1168-1178')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onTorrentError', 'CALL', 'Registered listener receives torrent-error events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:277-281,293; TorrentDownloadImpl.java:333-336,421-424')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onTorrentPaused', 'CALL', 'Registered listener receives torrent-paused events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:262-266,293; TorrentDownloadImpl.java:237-240')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onTorrentRemoved', 'CALL', 'Registered listener receives torrent-removed events', cls='non_standard', via='TorrentEngineListener dispatch through notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:267-271,293; TorrentSessionImpl.java:388-390; TorrentDownloadImpl.java:456-460')
e('TorrentInfoProvider.makeInfoListFlowable', 'TorrentInfoProvider$2.onTorrentStateChanged', 'CALL', 'Registered listener receives torrent-state-changed events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentDownloadImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:255-261,293; TorrentDownloadImpl.java:224-230')
e('TorrentInfoProvider.makeTorrentsDeletedFlowable', 'TorrentInfoProvider$3.<init>', 'CALL', 'Deleted-torrents flowable creates its engine listener', cls='explicit', evidence='SRC TorrentInfoProvider.java:457')
e('TorrentInfoProvider.makeTorrentsDeletedFlowable', 'TorrentInfoProvider$3.onTorrentRemoved', 'CALL', 'Registered listener receives torrent-removed events', cls='non_standard', via='TorrentEngineListener dispatch through notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:459-463,466; TorrentSessionImpl.java:388-390; TorrentDownloadImpl.java:456-460')
e('TorrentInfoProvider.makeSessionStatsFlowable', 'TorrentInfoProvider$4.<init>', 'CALL', 'Session-stats flowable creates its engine listener', cls='explicit', evidence='SRC TorrentInfoProvider.java:478')
e('TorrentInfoProvider.makeSessionStatsFlowable', 'TorrentInfoProvider$4.onSessionStats', 'CALL', 'Registered listener receives session-stats events', cls='non_standard', via='TorrentEngineListener dispatch through TorrentSessionImpl.notifyListeners', evidence='INFERRED listener dispatch; SRC TorrentInfoProvider.java:480-488,491; TorrentSessionImpl.java:1168-1178')
e('SessionStats.<init>(long,long,long,long,long,int)', 'AbstractInfoParcel.<init>()', 'CALL', 'SessionStats ctor runs the compiler-inserted no-arg super call', cls='non_standard', via='Compiler-inserted super call (no explicit super in source)', evidence='INFERRED compiler-inserted super call; SRC SessionStats.java:36-47; AbstractInfoParcel.java:36-39')
e('TorrentInfo.<init>(Parcel)', 'AbstractInfoParcel.<init>(Parcel)', 'CALL', 'TorrentInfo Parcel ctor calls super(source)', cls='explicit', evidence='SRC TorrentInfo.java:120-121; AbstractInfoParcel.java:46-49')
e('TorrentInfo.<init>(String,String,long,String,List)', 'AbstractInfoParcel.<init>(String)', 'CALL', 'TorrentInfo 5-arg ctor calls super(torrentId)', cls='explicit', evidence='SRC TorrentInfo.java:61-68; AbstractInfoParcel.java:41-44')
e('TorrentInfo.writeToParcel', 'AbstractInfoParcel.writeToParcel', 'CALL', 'TorrentInfo writeToParcel calls super.writeToParcel first', cls='explicit', evidence='SRC TorrentInfo.java:150-151; AbstractInfoParcel.java:52-55')
e('TorrentEngine.makeAdvancedInfoSync', 'AdvancedTorrentInfo.<clinit>', 'FRAMEWORK', 'First AdvancedTorrentInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentEngine.java:846-860; AdvancedTorrentInfo.java:119-134')
e('TorrentEngine.makeAdvancedInfoSync', 'AdvancedTorrentInfo.<init>(String,long[],int,int,int,double,long,long,double,double[],int,int)', 'CALL', 'Advanced-info sync builds the 12-arg AdvancedTorrentInfo', cls='explicit', evidence='SRC TorrentEngine.java:846-860; AdvancedTorrentInfo.java:54-75')
e('TorrentInfoProvider.makeAdvancedInfoFlowable', 'AdvancedTorrentInfo.equals', 'CALL', 'Advanced-info flowable compares the new info with the previous one', cls='explicit', evidence='SRC TorrentInfoProvider.java:323-331; AdvancedTorrentInfo.java:165-187')
e('AdvancedTorrentInfo.<clinit>', 'AdvancedTorrentInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC AdvancedTorrentInfo.java:119-134')
e('TorrentEngine.fetchMagnet', 'MagnetInfo.<clinit>', 'FRAMEWORK', 'First MagnetInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentEngine.java:415-419; MagnetInfo.java:79-93')
e('TorrentSessionImpl.fetchMagnet(String)', 'MagnetInfo.<init>(String,String,String,List)', 'CALL', 'Magnet fetch builds the MagnetInfo record', cls='explicit', evidence='SRC TorrentSessionImpl.java:439-440; MagnetInfo.java:48-54')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'MagnetInfo.getFilePriorities', 'CALL', 'Magnet decode branch reads the magnet file priorities', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:245-246; MagnetInfo.java:110-112')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'MagnetInfo.getName', 'CALL', 'Magnet decode branch reads the magnet name', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:242; MagnetInfo.java:105-107')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'MagnetInfo.getSha1hash', 'CALL', 'Magnet decode branch reads the magnet sha1 hash', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:242; MagnetInfo.java:100-102')

UNREACHABLE.update({
    'AdvancedTorrentInfo.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in this batch); no marshalling site for AdvancedTorrentInfo.',
        'SRC AdvancedTorrentInfo.java:76-93',
        'INFERRED'),
    'AdvancedTorrentInfo.compareTo': ('no_trigger_in_app',
        'No sort or comparison site passes an AdvancedTorrentInfo receiver; auto_calls.json has 0 hits.',
        'SRC AdvancedTorrentInfo.java:136-139',
        'INFERRED'),
    'AdvancedTorrentInfo.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels an AdvancedTorrentInfo.',
        'SRC AdvancedTorrentInfo.java:95-98',
        'INFERRED'),
    'AdvancedTorrentInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-map or hash-set use of an AdvancedTorrentInfo; its equals use does not call hashCode.',
        'SRC AdvancedTorrentInfo.java:142-163',
        'INFERRED'),
    'AdvancedTorrentInfo.toString': ('no_trigger_in_app',
        'No printed logging or string-concatenation caller for an AdvancedTorrentInfo value.',
        'SRC AdvancedTorrentInfo.java:191-207',
        'INFERRED'),
    'AdvancedTorrentInfo.writeToParcel': ('no_trigger_in_app',
        'No site parcels an AdvancedTorrentInfo; the definition itself calls super.writeToParcel but is never invoked.',
        'SRC AdvancedTorrentInfo.java:101-117',
        'INFERRED'),
    'AdvancedTorrentInfo$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch on unparcel; no printed unparcel site for AdvancedTorrentInfo.',
        'SRC AdvancedTorrentInfo.java:123-126',
        'INFERRED'),
    'AdvancedTorrentInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC AdvancedTorrentInfo.java:129-132',
        'INFERRED'),
    'MagnetInfo.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in batch 29); no marshalling site for MagnetInfo.',
        'SRC MagnetInfo.java:56-63',
        'INFERRED'),
    'MagnetInfo.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels a MagnetInfo.',
        'SRC MagnetInfo.java:65-68',
        'INFERRED'),
})

# No REACHABLE method calls any UNREACHABLE row of this batch in auto_calls.json
# (recomputed; the only bytecode calls into this batch's UNREACHABLE rows come
# from their own UNREACHABLE CREATOR methods), so no SUPPRESS entries apply.
SUPPRESS.update(set())
