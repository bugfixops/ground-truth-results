# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g6/parts/b031.py; labels/kinds verified
# against staging-A1 merge-ready batch 31 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/031/ (one file per row).
# Stronger-evidence check (rule b): no UNREACHABLE key of this batch is held in
# the merger-tree graph_def.py or merged parts with a conflicting grade; no grade changed.
# NOTE for merger/auditor: batch-31's merge-ready file also contains conditional-table rows
# that reuse row numbers; this part follows the final per-row table (last occurrence per row),
# as the harness counter does — no conditional-table row was treated as a method row.
# Batch 31 part (FeedChannel, FeedItem, TagInfo, Torrent).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b031_printed.txt. Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# The FeedChannel SelectionTracker edges rest on the recorded Phase-3 L2 decision
# (createParcelableStorage(FeedChannelItem) counts as a printed marshalling site
# for the inherited FeedChannel parcel methods); the TagInfo parcel edges rest on
# printed putParcelable/getParcelable sites. See REPORT.md.
# SUPPRESS is empty by recomputation: auto_calls.json contains exactly 2 bytecode
# calls into this batch's UNREACHABLE rows, both from the UNREACHABLE own-CREATOR
# createFromParcel methods (FeedItem, Torrent Parcel ctors); no REACHABLE method
# calls any UNREACHABLE row of this batch. See REPORT.md.

e('FeedFragment.onViewCreated', 'FeedChannel.writeToParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage for FeedChannelItem writes the item through writeToParcel', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/feeds/FeedFragment.java:137-142; FeedChannel.java:92-102')
e('FeedChannel.<clinit>', 'FeedChannel$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC FeedChannel.java:104-118')
e('FeedFragment.onViewCreated', 'FeedChannel$1.createFromParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage restores the item through the CREATOR', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/feeds/FeedFragment.java:137-142; FeedChannel.java:108-111')
e('FeedParser.getItems', 'FeedItem.<clinit>', 'FRAMEWORK', 'First FeedItem construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC FeedParser.java:109-110; FeedItem.java:114-128')
e('FeedParser.getItems', 'FeedItem.<init>(long,String,String,String,long)', 'CALL', 'Feed parser builds a FeedItem per feed entry', cls='explicit', evidence='SRC FeedParser.java:109-110; FeedItem.java:75-80')
e('FeedItem.<init>(long,String,String,String,long)', 'FeedItem.<init>(String,long,String,String,String,long)', 'CALL', '5-arg FeedItem ctor delegates to the primary 6-arg ctor', cls='explicit', evidence='SRC FeedItem.java:79; FeedItem.java:62-72')
e('FeedItemsListItem.equals', 'FeedItem.equals', 'CALL', 'FeedItemsListItem equals delegates to super.equals', cls='explicit', evidence='SRC ui/feeditems/FeedItemsListItem.java:51-53; FeedItem.java:136-140')
e('FeedItem.<clinit>', 'FeedItem$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC FeedItem.java:114-128')
e('AddTagViewModel.saveTag', 'TagInfo.<clinit>', 'FRAMEWORK', 'First TagInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC ui/addtag/AddTagViewModel.java:59-61; TagInfo.java:69-79')
e('AddTagViewModel.saveTag', 'TagInfo.<init>(long,String,int)', 'CALL', 'Save-tag for an existing tag builds the 3-arg TagInfo', cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:61; TagInfo.java:38-42')
e('TagInfo$1.createFromParcel', 'TagInfo.<init>(Parcel)', 'CALL', 'CREATOR createFromParcel constructs the Parcel form', cls='explicit', evidence='SRC TagInfo.java:71-73')
e('AddTagViewModel.saveTag', 'TagInfo.<init>(String,int)', 'CALL', 'Save-tag for a new tag builds the 2-arg TagInfo', cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:59; TagInfo.java:45-48')
e('AddTagDialog.newInstance', 'TagInfo.describeContents', 'FRAMEWORK', 'Putting a TagInfo into a Bundle calls describeContents on parcel', cls='non_standard', via='Parcelable framework dispatch on putParcelable', evidence='INFERRED framework parcel dispatch; SRC ui/addtag/AddTagDialog.java:67-71; TagInfo.java:58-60')
e('AddTorrentViewModel.removeTag', 'TagInfo.equals', 'CALL', 'Removing a tag from the list dispatches to element equals', cls='non_standard', via='List.remove dispatch to element equals', evidence='INFERRED library dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:162-163; TagInfo.java:82-91')
e('AddTagDialog.newInstance', 'TagInfo.writeToParcel', 'FRAMEWORK', 'Putting a TagInfo into a Bundle writes it through writeToParcel', cls='non_standard', via='Parcelable framework dispatch on putParcelable', evidence='INFERRED framework parcel dispatch; SRC ui/addtag/AddTagDialog.java:67-71; TagInfo.java:63-67')
e('TagInfo.<clinit>', 'TagInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC TagInfo.java:69-79')
e('AddTagDialog.onCreateDialog', 'TagInfo$1.createFromParcel', 'FRAMEWORK', 'Reading a TagInfo from the arguments Bundle dispatches through the CREATOR', cls='non_standard', via='Parcelable framework dispatch on getParcelable', evidence='INFERRED framework parcel dispatch; SRC ui/addtag/AddTagDialog.java:112-119; TagInfo.java:71-73')
e('TorrentSessionImpl.addTorrent', 'Torrent.<clinit>', 'FRAMEWORK', 'First Torrent construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentSessionImpl.java:263-270; Torrent.java:157-170')
e('TorrentSessionImpl.addTorrent', 'Torrent.<init>(String,Uri,String,boolean,long,boolean,boolean)', 'CALL', 'Add-torrent builds the 7-arg Torrent entity', cls='explicit', evidence='SRC TorrentSessionImpl.java:263-270; Torrent.java:72-87')
e('TorrentDao_Impl.getAllTorrents', 'Torrent.<init>(String,String,Uri,String,boolean,long,boolean,boolean)', 'CALL', 'Generated Room code constructs the entity 8-arg ctor when reading torrents', cls='non_standard', via='Generated Room DAO dispatch from TorrentRepositoryImpl.getAllTorrents', evidence='INFERRED generated Room code; SRC TorrentRepositoryImpl.java:86-87; Torrent.java:89-101')
e('TorrentSessionImpl.restoreTorrents', 'Torrent.getMagnet', 'CALL', 'Restore path reads the torrent magnet for the load task', cls='explicit', evidence='SRC TorrentSessionImpl.java:413-415; Torrent.java:124-127')
e('TorrentSessionImpl.restoreTorrents', 'Torrent.isDownloadingMetadata', 'CALL', 'Restore path checks whether the torrent is still downloading metadata', cls='explicit', evidence='SRC TorrentSessionImpl.java:413; Torrent.java:119-122')
e('TorrentSessionImpl.addTorrent', 'Torrent.setMagnetUri', 'CALL', 'Magnet add without loaded bencode stores the magnet URI on the entity', cls='explicit', evidence='SRC TorrentSessionImpl.java:273-277; Torrent.java:129-133')

UNREACHABLE.update({
    'FeedChannel.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a FeedChannel (FeedChannelItem overrides hashCode separately).',
        'SRC FeedChannel.java:120-124',
        'INFERRED'),
    'FeedChannel.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a FeedChannel value.',
        'SRC FeedChannel.java:132-146',
        'INFERRED'),
    'FeedChannel$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only; no printed unparcel site that would need an array form.',
        'SRC FeedChannel.java:113-117',
        'INFERRED'),
    'FeedItem.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in this batch); no marshalling site for FeedItem.',
        'SRC FeedItem.java:83-93',
        'INFERRED'),
    'FeedItem.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels a FeedItem.',
        'SRC FeedItem.java:95-99',
        'INFERRED'),
    'FeedItem.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a FeedItem.',
        'SRC FeedItem.java:130-134',
        'INFERRED'),
    'FeedItem.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a FeedItem value.',
        'SRC FeedItem.java:142-156',
        'INFERRED'),
    'FeedItem.writeToParcel': ('no_trigger_in_app',
        'No site parcels a FeedItem.',
        'SRC FeedItem.java:101-112',
        'INFERRED'),
    'FeedItem$1.createFromParcel': ('no_trigger_in_app',
        'Called only by Parcel framework dispatch; no printed unparcel site for FeedItem.',
        'SRC FeedItem.java:118-121',
        'INFERRED'),
    'FeedItem$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only, as for createFromParcel; no printed unparcel site.',
        'SRC FeedItem.java:124-127',
        'INFERRED'),
    'TagInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a TagInfo value.',
        'SRC TagInfo.java:101-109',
        'INFERRED'),
    'TagInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only; no printed unparcel site that would need an array form.',
        'SRC TagInfo.java:75-78',
        'INFERRED'),
    'Torrent.<init>(Parcel)': ('no_trigger_in_app',
        'Only caller is its own CREATOR createFromParcel (UNREACHABLE in batch 32); no marshalling site for Torrent.',
        'SRC Torrent.java:103-117',
        'INFERRED'),
    'Torrent.describeContents': ('framework_never_calls',
        'Framework calls describeContents only when parcelling, and no site parcels a Torrent.',
        'SRC Torrent.java:135-139',
        'INFERRED'),
    'Torrent.equals': ('no_trigger_in_app',
        'No printed collection or comparison use of a Torrent entity; repository lookups use id strings.',
        'SRC Torrent.java:178-182',
        'INFERRED'),
    'Torrent.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a Torrent entity.',
        'SRC Torrent.java:172-176',
        'INFERRED'),
    'Torrent.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a Torrent value.',
        'SRC Torrent.java:184-200',
        'INFERRED'),
})

# No REACHABLE method calls any UNREACHABLE row of this batch in auto_calls.json
# (recomputed), so no SUPPRESS entries apply.
SUPPRESS.update(set())
