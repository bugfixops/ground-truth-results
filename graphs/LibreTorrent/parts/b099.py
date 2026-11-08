# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C16 delivery (2026-11-01): audited A3 base part kept as audited; no label flipped.
# Verification: base part checked against clone graphs/LibreTorrent/scratch/merge-ready/batch099-merge-ready.md
# (labels/kinds match exactly; see REPORT-b099.md). Stronger-evidence rule (b): no UNREACHABLE keys in this
# batch, so no grade comparison applies; no change. Greps: parts-staging/grep/b099/ (supplementary hashCode
# file only; zero UNREACHABLE rows, so no mandatory grep file). Pre-test: private copy on the b007 base;
# check-2 delta 0 (see report).
# MERGER CONDITION C1: row 18 FeedChannelItem.hashCode stands as REACHABLE/INFERRED only under the
# MutableSelection lead (tracker built in FeedFragment onViewCreated, copySelection in deleteFeeds).
# The merger must accept that lead or revert the row to OPEN and change the batch file. Kept as audited.
# Batch 99 part (FeedActivity menu/lifecycle, FeedChannelItem, FeedChannelListAdapter
# and its selection-support classes). Hand-written edges only. Each evidence string
# cites lines printed in graphs/LibreTorrent/scratch/b099_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# No UNREACHABLE rows in this batch, so no SUPPRESS entries apply.
# FLAG (see REPORT.md): row 18 FeedChannelItem.hashCode is REACHABLE here only
# under the batch file's label cells (Phase-3 verdict applied); its earlier prose
# says it stays OPEN pending printed androidx MutableSelection dispatch, and the
# edge below is the conditional-table lead, not printed app-Java dispatch.

# FeedActivity rows.
e('FeedActivity.onCreate', 'FeedActivity.onCreateOptionsMenu', 'FRAMEWORK', 'Framework delivers the menu callback for the created activity', cls='non_standard', via='Android framework menu dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:91-107; SRC ui/feeds/FeedActivity.java:239-244')
e('FeedItemsFragment.finish', 'FeedActivity.onFragmentFinished', 'CALL', 'Feed-items fragment finish calls the host callback', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:321-327; SRC ui/feeds/FeedActivity.java:406-410')
e('FeedActivity.onCreateOptionsMenu', 'FeedActivity.onOptionsItemSelected', 'CALL', 'Toolbar menu-item listener dispatches to the options-item handler', cls='non_standard', via='Toolbar menu-item listener dispatch', evidence='INFERRED listener dispatch; SRC ui/feeds/FeedActivity.java:239-242; SRC ui/feeds/FeedActivity.java:248-260')
e('FeedActivity.onCreate', 'FeedActivity.onStart', 'FRAMEWORK', 'Framework delivers onStart for the created activity', cls='non_standard', via='Android activity lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:91-107; SRC ui/feeds/FeedActivity.java:122-128')
e('FeedActivity.onCreate', 'FeedActivity.onStop', 'FRAMEWORK', 'Framework delivers onStop for the created activity', cls='non_standard', via='Android activity lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:91-107; SRC ui/feeds/FeedActivity.java:131-135')
e('FeedActivity.lambda$new$9', 'FeedActivity.restoreFeedsBackup', 'CALL', 'Restore chooser result calls restoreFeedsBackup with the chosen data', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:389-401; SRC ui/feeds/FeedActivity.java:359-370')
e('FeedActivity.backupFeeds', 'FeedActivity.restoreFeedsBackupErrorDialog', 'CALL', 'Backup subscribe error handler shows the restore error dialog', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:346-356; SRC ui/feeds/FeedActivity.java:306-332')
e('FeedActivity.onOptionsItemSelected', 'FeedActivity.restoreFeedsChooseDialog', 'CALL', 'Restore menu item opens the restore chooser dialog', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:248-256; SRC ui/feeds/FeedActivity.java:278-289')
e('FeedActivity.lambda$subscribeAlertDialog$1', 'FeedActivity.sendErrorReport', 'CALL', 'Alert-dialog positive-button handling sends the error report', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:141-154; SRC ui/feeds/FeedActivity.java:334-344')
e('FeedActivity.initLayout', 'FeedActivity.showBlankFragment', 'CALL', 'Layout initialisation shows the blank fragment', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:109-111; SRC ui/feeds/FeedActivity.java:191-201')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.showFeedItems', 'CALL', 'Feed-items-opened subscription dispatches to showFeedItems', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:172-176; SRC ui/feeds/FeedActivity.java:203-224')
e('FeedActivity.onStart', 'FeedActivity.subscribeAlertDialog', 'CALL', 'Activity start subscribes the alert-dialog events', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:122-126; SRC ui/feeds/FeedActivity.java:138-168')
e('FeedActivity.onStart', 'FeedActivity.subscribeMsgViewModel', 'CALL', 'Activity start subscribes the message view model', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:122-127; SRC ui/feeds/FeedActivity.java:172-188')

# FeedChannelItem rows.
e('FeedFragment.observeFeeds', 'FeedChannelItem.<init>', 'CALL', 'Feed stream maps each channel through the list-item constructor', cls='non_standard', via='Rx map method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:256-262; SRC ui/feeds/FeedChannelItem.java:30-38')
e('FeedChannelListAdapter.submitList', 'FeedChannelItem.compareTo', 'CALL', 'List submission sorts the list, comparing channel items', cls='non_standard', via='Library sort dispatch to Comparable', evidence='INFERRED library dispatch; SRC ui/feeds/FeedChannelListAdapter.java:110-116; SRC ui/feeds/FeedChannelItem.java:46-52')
e('FeedChannelListAdapter$1.areItemsTheSame', 'FeedChannelItem.equals', 'CALL', 'DiffUtil item comparison delegates to channel-item equals', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:166-170; SRC ui/feeds/FeedChannelItem.java:55-58')
e('FeedChannelListAdapter$1.areContentsTheSame', 'FeedChannelItem.equalsContent', 'CALL', 'DiffUtil contents comparison delegates to channel-item equalsContent', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:159-164; SRC ui/feeds/FeedChannelItem.java:60-79')
e('FeedFragment.deleteFeeds', 'FeedChannelItem.hashCode', 'CALL', 'Selection copy into a MutableSelection hashes its channel-item keys', cls='non_standard', via='androidx SelectionTracker/MutableSelection dispatch (INFERRED, unprinted library internals)', evidence='INFERRED androidx dispatch; SRC ui/feeds/FeedChannelItem.java:40-43; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedFragment.java:444-447')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter.<clinit>', 'FRAMEWORK', 'First active use of the adapter class runs its static initialisers', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM dispatch; SRC ui/feeds/FeedFragment.java:116; SRC ui/feeds/FeedChannelListAdapter.java:58; SRC ui/feeds/FeedChannelListAdapter.java:156')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter.<init>', 'CALL', 'Fragment view creation constructs the channel list adapter', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:116; SRC ui/feeds/FeedChannelListAdapter.java:65-70')
e('FeedChannelListAdapter$KeyProvider.getKey', 'FeedChannelListAdapter.getItemKey', 'CALL', 'Key provider delegates to the adapter item-key lookup', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:287-290; SRC ui/feeds/FeedChannelListAdapter.java:119-125')
e('FeedChannelListAdapter$KeyProvider.getPosition', 'FeedChannelListAdapter.getItemPosition', 'CALL', 'Key provider delegates to the adapter item-position lookup', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:293-296; SRC ui/feeds/FeedChannelListAdapter.java:128-131')
e('FeedFragment.subscribeMsgViewModel', 'FeedChannelListAdapter.getOpenedItem', 'CALL', 'Feeds-deleted filter reads the opened item from the adapter', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:286-297; SRC ui/feeds/FeedChannelListAdapter.java:151-154')
e('FeedFragment.onItemClicked', 'FeedChannelListAdapter.markAsOpen', 'CALL', 'Item click marks the item open in the adapter', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:341-345; SRC ui/feeds/FeedChannelListAdapter.java:133-148')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView binds rows of the adapter set on the list', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/feeds/FeedFragment.java:135; SRC ui/feeds/FeedChannelListAdapter.java:91-106')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView creates holders for the adapter set on the list', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/feeds/FeedFragment.java:135; SRC ui/feeds/FeedChannelListAdapter.java:79-89')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter.setSelectionTracker', 'CALL', 'Fragment view creation hands the selection tracker to the adapter', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:183; SRC ui/feeds/FeedChannelListAdapter.java:72-75')
e('FeedFragment.observeFeeds', 'FeedChannelListAdapter.submitList', 'CALL', 'Feed stream submits its item list to the adapter', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:256-266; SRC ui/feeds/FeedChannelListAdapter.java:110-116')
e('FeedChannelListAdapter.<clinit>', 'FeedChannelListAdapter$1.<init>', 'CALL', 'Static diff-callback field initialiser creates the DiffUtil callback', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:65-67; SRC ui/feeds/FeedChannelListAdapter.java:156')
e('FeedChannelListAdapter.submitList', 'FeedChannelListAdapter$1.areContentsTheSame', 'FRAMEWORK', 'ListAdapter diffing calls the contents callback for submitted lists', cls='non_standard', via='DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/feeds/FeedChannelListAdapter.java:110-116; SRC ui/feeds/FeedChannelListAdapter.java:159-164')
e('FeedChannelListAdapter.submitList', 'FeedChannelListAdapter$1.areItemsTheSame', 'FRAMEWORK', 'ListAdapter diffing calls the items callback for submitted lists', cls='non_standard', via='DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/feeds/FeedChannelListAdapter.java:110-116; SRC ui/feeds/FeedChannelListAdapter.java:166-170')
e('FeedChannelListAdapter$ViewHolder.getItemDetails', 'FeedChannelListAdapter$ItemDetails.<init>', 'CALL', 'Holder details construction creates the selection item details', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:264-267; SRC ui/feeds/FeedChannelListAdapter.java:304-308')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$ItemDetails.getPosition', 'FRAMEWORK', 'Selection tracker reads the position from holder item details', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:318-321')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$ItemDetails.getSelectionKey', 'FRAMEWORK', 'Selection tracker reads the key from holder item details', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:312-315')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$ItemLookup.<init>', 'CALL', 'Fragment view creation builds the selection item lookup', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:328-332')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$ItemLookup.getItemDetails', 'FRAMEWORK', 'Selection tracker asks the lookup for details on touch', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:335-346')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$KeyProvider.<init>', 'CALL', 'Fragment view creation builds the selection key provider', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:137-141; SRC ui/feeds/FeedChannelListAdapter.java:278-283')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$KeyProvider.getKey', 'FRAMEWORK', 'Selection tracker asks the key provider for the key at a position', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:287-290')
e('FeedFragment.onViewCreated', 'FeedChannelListAdapter$KeyProvider.getPosition', 'FRAMEWORK', 'Selection tracker asks the key provider for the position of a key', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:137-142; SRC ui/feeds/FeedChannelListAdapter.java:293-296')
e('FeedChannelListAdapter.onCreateViewHolder', 'FeedChannelListAdapter$ViewHolder.<init>', 'CALL', 'Holder creation constructs the channel view holder', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:79-87; SRC ui/feeds/FeedChannelListAdapter.java:191-196')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in this batch
# (this batch has no UNREACHABLE methods), so no intra-group SUPPRESS
# entries apply. Cross-group auto-call candidates (KeyProvider interface
# dispatch variants into batches 94/96/97) are reported in REPORT.md,
# not suppressed here.
SUPPRESS.update(set())
