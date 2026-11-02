# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C16 delivery (2026-11-01): audited A3 base part kept as audited; no label flipped.
# Verification: base part checked against clone graphs/LibreTorrent/scratch/merge-ready/batch096-merge-ready.md
# (labels/kinds match exactly; see REPORT-b096.md). Stronger-evidence rule (b): tree holds no grade for this
# batch's UNREACHABLE keys (tree MERGED_PARTS ends b007; keys occur only in auto_calls.json CHA entries), so no
# grade change. Greps: parts-staging/grep/b096/. Pre-test: private copy on the b007 base; check-2 delta 0 (see report).
# Merger note (recorded, NOT applied by converter): b096/b097 carry the remaining G19 SUPPRESS callee strings
# (FeedItemsAdapter getItemKey/getItemPosition); the merger unions all four G19 strings (b094/b096/b097) so the
# cross-group TorrentListAdapter/FeedChannelListAdapter callers are covered. Kept as audited.
# Batch 96 part (TrackerListAdapter rest + ErrorReport + FeedItems head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b096_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch96-merge-ready.md (verified identical to the
# helper input copy; batches 93-97 are not A1-affected, so the clone copy is current).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# SUPPRESS: callee-string entries for this batch's UNREACHABLE methods. They suppress
# the CHA interface-dispatch auto edges from every KeyProvider.getKey/getPosition into
# these Selectable methods (intra-group pairs from batches 93/96 plus the cross-group
# CHA pairs from TorrentListAdapter and FeedChannelListAdapter KeyProviders, all listed
# in REPORT.md for merger reconciliation). No other auto edge is suppressed.

e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter.setSelectionTracker', 'CALL', 'Trackers fragment hands its SelectionTracker to the adapter', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:224; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:63-65')
e('TrackerListAdapter.<clinit>', 'TrackerListAdapter$1.<init>', 'FRAMEWORK', 'Static diffCallback field initialisation creates the anonymous DiffUtil callback', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:115-132')
e('TrackerListAdapter.submitList', 'TrackerListAdapter$1.areContentsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil contents check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:92-99; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:118-123')
e('TrackerListAdapter.submitList', 'TrackerListAdapter$1.areItemsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil identity check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:92-99; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:125-130')
e('TrackerListAdapter$ViewHolder.getItemDetails', 'TrackerListAdapter$ItemDetails.<init>', 'CALL', 'ViewHolder builds its ItemDetails from the selection key and adapter position', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:216-219; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:256-260')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$ItemDetails.getPosition', 'FRAMEWORK', 'SelectionTracker reads ItemDetails positions for the tracker built here', cls='non_standard', via='SelectionTracker ItemDetails dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:270-273')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$ItemDetails.getSelectionKey', 'FRAMEWORK', 'SelectionTracker reads ItemDetails selection keys for the tracker built here', cls='non_standard', via='SelectionTracker ItemDetails dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:264-268')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$ItemLookup.<init>', 'CALL', 'Trackers fragment builds the ItemLookup for its tracker', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:280-283')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$ItemLookup.getItemDetails', 'FRAMEWORK', 'SelectionTracker touch dispatch through the registered ItemLookup', cls='non_standard', via='SelectionTracker ItemDetailsLookup dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:287-295')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$KeyProvider.<init>', 'CALL', 'Trackers fragment builds the KeyProvider for its tracker', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:181; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:230-236')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$KeyProvider.getKey', 'FRAMEWORK', 'SelectionTracker dispatch through the registered KeyProvider', cls='non_standard', via='SelectionTracker ItemKeyProvider dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:239-242')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter$KeyProvider.getPosition', 'FRAMEWORK', 'SelectionTracker dispatch through the registered KeyProvider', cls='non_standard', via='SelectionTracker ItemKeyProvider dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:178-182; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:245-248')
e('TrackerListAdapter.onCreateViewHolder', 'TrackerListAdapter$ViewHolder.<init>', 'CALL', 'ViewHolder construction on holder creation', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:78; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:145-150')
e('TrackerListAdapter$ItemLookup.getItemDetails', 'TrackerListAdapter$ViewHolder.getItemDetails', 'CALL', 'ItemLookup delegates to the row ViewHolder for its details', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:293; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:216-219')
e('TrackerListAdapter.onBindViewHolder', 'TrackerListAdapter$ViewHolder.setSelected', 'CALL', 'Bind marks the holder selected from the tracker state', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:86; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:210-213')
e('MainApplication.onCreate', 'ErrorReportActivity.<clinit>', 'FRAMEWORK', 'ACRA report-dialog class reference initialises the activity class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC MainApplication.java:58; SRC ui/errorreport/ErrorReportActivity.java:46')
e('MainApplication.onCreate', 'ErrorReportActivity.<init>', 'FRAMEWORK', 'ACRA starts the manifest-declared report-dialog activity on crash', cls='non_standard', via='ACRA report-dialog dispatch', evidence='INFERRED ACRA report-dialog dispatch; SRC MainApplication.java:58; SRC ui/errorreport/ErrorReportActivity.java:55-72')
e('ErrorReportActivity.<init>', 'ErrorReportActivity.onCreate', 'LIFECYCLE', 'Framework instantiates the activity then creates it', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/errorreport/ErrorReportActivity.java:55-72')
e('ErrorReportDialog.newInstance', 'ErrorReportDialog.<clinit>', 'FRAMEWORK', 'First dialog construction initialises the dialog class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/errorreport/ErrorReportDialog.java:39-49; SRC ui/errorreport/ErrorReportDialog.java:33-35')
e('FeedActivity.showFeedItems', 'FeedItemsActivity.<clinit>', 'FRAMEWORK', 'Intent class reference initialises the activity class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/feeds/FeedActivity.java:221-222; SRC ui/feeditems/FeedItemsActivity.java:37-39')
e('FeedItemsFragment.finish', 'FeedItemsActivity.onFragmentFinished', 'CALL', 'Fragment finish callback notifies the hosting activity', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:325-328; SRC ui/feeditems/FeedItemsActivity.java:62-66')
e('FeedItemsFragment.onViewCreated', 'FeedItemsAdapter.<clinit>', 'FRAMEWORK', 'First adapter construction initialises the adapter class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/feeditems/FeedItemsFragment.java:152; SRC ui/feeditems/FeedItemsAdapter.java:51')
e('FeedItemsFragment.onViewCreated', 'FeedItemsAdapter.<init>', 'CALL', 'Feed items fragment builds its adapter', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:152; SRC ui/feeditems/FeedItemsAdapter.java:55-57')

UNREACHABLE.update({
    'FeedItemsAdapter.getItemKey': ('no_trigger_in_app',
        'Selectable implementation, FeedItemsAdapter.java:91-97. The feed items fragment builds no SelectionTracker/KeyProvider (fresh fragment grep zero hits for SelectionTracker/KeyProvider/getItemKey/getItemPosition/Selectable); the fragment uses the adapter only via construction :152, setAdapter :153 and submitList references :218/:233. The only selectable.getItemKey call sites in the saved full-tree grep are the four KeyProvider getKey methods.',
        'Saved full-tree greps grep_selectable_methods.txt, grep_Selectable_all.txt, grep_selectiontracker.txt; batch-96 ROUND 2 flip together with batch 97 row 1',
        'INFERRED'),
})

SUPPRESS.update({
    'FeedItemsAdapter.getItemKey',
})
