# R28 citation-form rework (2026-11-02): evidence citations under tripping components rendered basename-only; labels, kinds, edges, grades, line ranges unchanged; full relative paths remain in the .md and printed files.
# C04 conversion note (2026-11-01): base = audited A3 part helper/a3-g6/parts/b030.py; labels/kinds verified
# against staging-A1 merge-ready batch 30 (exact match, no label flipped).
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/030/ (one file per row).
# Stronger-evidence check (rule b): no UNREACHABLE key of this batch is held in
# the merger-tree graph_def.py or merged parts with a conflicting grade; no grade changed.
# Batch 30 part (TorrentInfo, TorrentStateCode, TrackerInfo, FastResume, FeedChannel).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b030_printed.txt. Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# The SelectionTracker parcel edges (L2) rest on the recorded Phase-3 L2 decision:
# createParcelableStorage(TorrentListItem / TrackerItem / FeedChannelItem) counts as
# a printed marshalling site for the inherited parcel methods of TorrentInfo,
# TrackerInfo and FeedChannel. See REPORT.md.
# SUPPRESS is empty by recomputation: auto_calls.json contains no bytecode call
# from a REACHABLE method into any UNREACHABLE row of this batch. See REPORT.md.

e('TorrentEngine.makeInfo', 'TorrentInfo.<clinit>', 'FRAMEWORK', 'First TorrentInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentEngine.java:779-787; TorrentInfo.java:173-183')
e('TorrentInfo$1.createFromParcel', 'TorrentInfo.<init>(Parcel)', 'CALL', 'CREATOR createFromParcel constructs the Parcel form', cls='explicit', evidence='SRC TorrentInfo.java:175-177')
e('TorrentEngine.makeInfo', 'TorrentInfo.<init>(String,String,long,String,List)', 'CALL', 'Stopped-task branch builds the 5-arg TorrentInfo', cls='explicit', evidence='SRC TorrentEngine.java:779-785; TorrentInfo.java:61-76')
e('TorrentEngine.makeInfo', 'TorrentInfo.<init>(String,String,TorrentStateCode,int,long,long,long,long,long,long,long,int,int,String,boolean,Priority[],List,boolean)', 'CALL', 'Running-task branch builds the 18-arg TorrentInfo', cls='explicit', evidence='SRC TorrentEngine.java:787-806; TorrentInfo.java:78-118')
e('MainFragment.onViewCreated', 'TorrentInfo.describeContents', 'FRAMEWORK', 'SelectionTracker Parcelable storage for TorrentListItem calls describeContents on save', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/main/MainFragment.java:157-162; TorrentInfo.java:145-146')
e('TorrentInfoProvider.makeInfoFlowable', 'TorrentInfo.equals', 'CALL', 'Info flowable compares the new info with the previous one', cls='explicit', evidence='SRC TorrentInfoProvider.java:138-140; TorrentInfo.java:217-244')
e('MainFragment.onViewCreated', 'TorrentInfo.writeToParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage for TorrentListItem writes the item through writeToParcel', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/main/MainFragment.java:157-162; TorrentInfo.java:150-171')
e('TorrentInfo.<clinit>', 'TorrentInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC TorrentInfo.java:173-183')
e('MainFragment.onViewCreated', 'TorrentInfo$1.createFromParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage restores the item through the CREATOR', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/main/MainFragment.java:157-162; TorrentInfo.java:175-177')
e('TorrentInfo.<init>(String,String,long,String,List)', 'TorrentStateCode.<clinit>', 'FRAMEWORK', '5-arg ctor assigns TorrentStateCode.STOPPED, loading the enum', cls='non_standard', via='JVM class initialization on first constant reference', evidence='INFERRED JVM class initialization; SRC TorrentInfo.java:72; TorrentStateCode.java:28-59')
e('TorrentStateCode.<clinit>', 'TorrentStateCode.<init>', 'CALL', 'Enum initialisation constructs each TorrentStateCode constant', cls='non_standard', via='JVM enum constant construction during <clinit>', evidence='INFERRED JVM enum construction; SRC TorrentStateCode.java:28-66')
e('TorrentInfo.<init>(Parcel)', 'TorrentStateCode.fromValue', 'CALL', 'Parcel ctor restores the state code through fromValue', cls='explicit', evidence='SRC TorrentInfo.java:125; TorrentStateCode.java:68-75')
e('TorrentInfo.writeToParcel', 'TorrentStateCode.value', 'CALL', 'writeToParcel writes the state code value', cls='explicit', evidence='SRC TorrentInfo.java:155; TorrentStateCode.java:77-80')
e('TorrentDownloadImpl.getTrackerInfoList', 'TrackerInfo.<clinit>', 'FRAMEWORK', 'First TrackerInfo construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC TorrentDownloadImpl.java:896-905; TrackerInfo.java:193-204')
e('TrackerInfo$1.createFromParcel', 'TrackerInfo.<init>(Parcel)', 'CALL', 'CREATOR createFromParcel constructs the Parcel form', cls='explicit', evidence='SRC TrackerInfo.java:196-198')
e('TrackerItem.<init>', 'TrackerInfo.<init>(String,String,int,int)', 'CALL', 'TrackerItem ctor passes its fields to the 4-arg TrackerInfo super ctor', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerItem.java:26-30; TrackerInfo.java:79-86')
e('TorrentDownloadImpl.getTrackerInfoList', 'TrackerInfo.<init>(AnnounceEntry)', 'CALL', 'Tracker list builder constructs a TrackerInfo per announce entry', cls='explicit', evidence='SRC TorrentDownloadImpl.java:896-905; TrackerInfo.java:67-77')
e('TrackerInfo.getMessageAndStatus', 'TrackerInfo.calcStatusCount', 'CALL', 'Message-and-status loop counts each endpoint infohash', cls='explicit', evidence='SRC TrackerInfo.java:97-98; TrackerInfo.java:147-155')
e('TrackerListAdapter.submitList', 'TrackerInfo.compareTo', 'CALL', 'Sorting the tracker-item list dispatches to TrackerInfo.compareTo (TrackerItem does not override it)', cls='non_standard', via='Collections.sort dispatch to Comparable.compareTo', evidence='INFERRED sort dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:92-95; TrackerInfo.java:208-209')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerInfo.describeContents', 'FRAMEWORK', 'SelectionTracker Parcelable storage for TrackerItem calls describeContents on save', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-183; TrackerInfo.java:179-181')
e('TorrentInfoProvider.makeTrackersInfoFlowable', 'TrackerInfo.equals', 'CALL', 'Tracker-list containsAll check dispatches to element equals', cls='non_standard', via='List.containsAll dispatch to element equals', evidence='INFERRED library dispatch; SRC TorrentInfoProvider.java:363-366; TrackerInfo.java:225-238')
e('TrackerInfo.<init>(AnnounceEntry)', 'TrackerInfo.getMessageAndStatus', 'CALL', 'AnnounceEntry ctor derives message and status from the endpoints', cls='explicit', evidence='SRC TrackerInfo.java:74; TrackerInfo.java:88-145')
e('TrackerInfo.calcStatusCount', 'TrackerInfo.infoHashStatus', 'CALL', 'Status counter reads the infohash status', cls='explicit', evidence='SRC TrackerInfo.java:152; TrackerInfo.java:157-167')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerInfo.writeToParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage for TrackerItem writes the item through writeToParcel', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-183; TrackerInfo.java:184-191')
e('TrackerInfo.<clinit>', 'TrackerInfo$1.<init>', 'CALL', 'Class initialisation creates the CREATOR anonymous instance', cls='explicit', evidence='SRC TrackerInfo.java:193-204')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerInfo$1.createFromParcel', 'FRAMEWORK', 'SelectionTracker Parcelable storage restores the item through the CREATOR', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-183; TrackerInfo.java:196-198')
e('TrackerInfo.getMessageAndStatus', 'TrackerInfo$Result.<init>', 'CALL', 'Message-and-status builds Result records for the endpoints', cls='explicit', evidence='SRC TrackerInfo.java:90,126,128,130-133,137-140,144; TrackerInfo.java:61-64')
e('TorrentDownloadImpl.serializeResumeData', 'FastResume.<init>', 'CALL', 'Resume-data save stores a FastResume record', cls='explicit', evidence='SRC TorrentDownloadImpl.java:516-520; FastResume.java:52-56')
e('AddFeedViewModel.applyParams', 'FeedChannel.<clinit>', 'FRAMEWORK', 'First FeedChannel construction initialises the class and its CREATOR field', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM class initialization; SRC ui/addfeed/AddFeedViewModel.java:173-179; FeedChannel.java:104-118')
e('FeedChannel$1.createFromParcel', 'FeedChannel.<init>(Parcel)', 'CALL', 'CREATOR createFromParcel constructs the Parcel form', cls='explicit', evidence='SRC FeedChannel.java:108-111')
e('AddFeedViewModel.applyParams', 'FeedChannel.<init>(String,String,long,boolean,String,boolean,String)', 'CALL', 'Add-feed params build the 7-arg FeedChannel', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:173-179; FeedChannel.java:52-64')
e('FeedFragment.onViewCreated', 'FeedChannel.describeContents', 'FRAMEWORK', 'SelectionTracker Parcelable storage for FeedChannelItem calls describeContents on save', cls='non_standard', via='SelectionTracker Parcelable storage framework dispatch (L2)', evidence='INFERRED framework parcel dispatch (L2); SRC ui/feeds/FeedFragment.java:137-142; FeedChannel.java:86-89')
e('FeedChannelItem.equals', 'FeedChannel.equals', 'CALL', 'FeedChannelItem equals delegates to super.equals', cls='explicit', evidence='SRC ui/feeds/FeedChannelItem.java:55-57; FeedChannel.java:127-130')

UNREACHABLE.update({
    'TorrentInfo.compareTo': ('no_trigger_in_app',
        'No printed sort of TorrentInfo as Comparable; the main list sorts TorrentListItem by its own path, not this compareTo.',
        'SRC TorrentInfo.java:185-188',
        'INFERRED'),
    'TorrentInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a TorrentInfo (TorrentListItem overrides hashCode separately).',
        'SRC TorrentInfo.java:190-214',
        'INFERRED'),
    'TorrentInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a TorrentInfo value.',
        'SRC TorrentInfo.java:246-269',
        'INFERRED'),
    'TorrentInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only; no printed unparcel site that would need an array form.',
        'SRC TorrentInfo.java:180-182',
        'INFERRED'),
    'TrackerInfo.hashCode': ('no_trigger_in_app',
        'No printed hash-collection use of a TrackerInfo (TrackerItem overrides hashCode separately).',
        'SRC TrackerInfo.java:213-222',
        'INFERRED'),
    'TrackerInfo.toString': ('no_trigger_in_app',
        'No printed logging or concatenation caller for a TrackerInfo value.',
        'SRC TrackerInfo.java:240-268',
        'INFERRED'),
    'TrackerInfo$1.newArray': ('no_trigger_in_app',
        'Framework dispatch only; no printed unparcel site that would need an array form.',
        'SRC TrackerInfo.java:201-203',
        'INFERRED'),
})

# No REACHABLE method calls any UNREACHABLE row of this batch in auto_calls.json
# (recomputed), so no SUPPRESS entries apply.
SUPPRESS.update(set())
