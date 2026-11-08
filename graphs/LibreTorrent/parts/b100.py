# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C16 delivery (2026-11-01): audited A3 base part kept as audited; no label flipped.
# Verification: base part checked against clone graphs/LibreTorrent/scratch/merge-ready/batch100-merge-ready.md
# (labels/kinds match exactly; see REPORT-b100.md). Stronger-evidence rule (b): no UNREACHABLE keys in this
# batch, so no grade comparison applies; no change. Greps: parts-staging/grep/b100/ (note file: zero UNREACHABLE
# rows, so no mandatory grep file). Pre-test: private copy on the b007 base; check-2 delta 0 (see report).
# Merger note: the $11/$12 mapping is BYTECODE-CONFIRMED ($10 FeedChannelItem outer map, $11 FeedChannel to
# Long inner map, $12 List to SingleSource flatMap). Kept as audited. Layout xml evidence for the FeedFragment
# attachment is cited in the .md prose and held in the helper scratch printed file (see REPORT-b100.md).
# Batch 100 part (FeedChannelListAdapter.ViewHolder, FeedFragment). Hand-written
# edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b100_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# No UNREACHABLE rows in this batch, so no SUPPRESS entries apply.
# FeedFragment attachment: FeedActivity.onCreate sets content view
# R.layout.activity_feed, which the res/values/layouts.xml alias resolves to
# activity_feed_portrait / activity_feed_two_pane, both carrying a
# FragmentContainerView with class FeedFragment (see b100.md); the .py
# evidence below cites the Java anchor lines, and the layout lines are
# printed in b100_printed.txt and cited in b100.md.

# ViewHolder rows.
e('FeedChannelListAdapter.onBindViewHolder', 'FeedChannelListAdapter$ViewHolder.bind', 'CALL', 'Row binding binds the holder with item, opened flag and listener', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:91-104; SRC ui/feeds/FeedChannelListAdapter.java:198')
e('FeedChannelListAdapter$ItemLookup.getItemDetails', 'FeedChannelListAdapter$ViewHolder.getItemDetails', 'CALL', 'Item lookup asks the holder for its selection details', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:335-341; SRC ui/feeds/FeedChannelListAdapter.java:264-267')
e('FeedChannelListAdapter$ViewHolder.bind', 'FeedChannelListAdapter$ViewHolder.lambda$bind$0', 'CALL', 'Row click listener lambda is registered in bind', cls='non_standard', via='View click dispatch', evidence='INFERRED View dispatch; SRC ui/feeds/FeedChannelListAdapter.java:217-223')
e('FeedChannelListAdapter.onBindViewHolder', 'FeedChannelListAdapter$ViewHolder.setSelected', 'CALL', 'Row binding marks the holder selected per the selection tracker', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:91-97; SRC ui/feeds/FeedChannelListAdapter.java:258-261')

# FeedFragment rows.
e('FeedActivity.onCreate', 'FeedFragment.<clinit>', 'FRAMEWORK', 'First active use of the fragment class runs its static initialisers', cls='non_standard', via='JVM class initialization on first active use (layout inflation)', evidence='INFERRED JVM dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:73-77')
e('FeedActivity.onCreate', 'FeedFragment.<init>', 'FRAMEWORK', 'Fragment manager instantiates the layout-declared fragment', cls='non_standard', via='FragmentManager layout inflation dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:95-99')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.copyChannelUrl', 'CALL', 'Copy menu item copies the selected channel URL', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-389; SRC ui/feeds/FeedFragment.java:464-478')
e('FeedFragment.lambda$subscribeAlertDialog$9', 'FeedFragment.deleteFeeds', 'CALL', 'Delete-dialog positive button deletes the selected feeds', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:310-320; SRC ui/feeds/FeedFragment.java:444-462')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.deleteFeedsDialog', 'CALL', 'Delete menu item shows the delete-feeds dialog', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-384; SRC ui/feeds/FeedFragment.java:412-431')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.editChannel', 'CALL', 'Edit menu item edits the selected channel', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-386; SRC ui/feeds/FeedFragment.java:494-505')
e('FeedFragment.subscribeAdapter', 'FeedFragment.getAllFeedsSingle', 'CALL', 'Adapter subscription loads the single-shot feed list', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:250-252; SRC ui/feeds/FeedFragment.java:271-282')
e('FeedFragment.deleteFeeds', 'FeedFragment.lambda$deleteFeeds$10', 'CALL', 'Delete chain maps each selection to its channel', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:444-453')
e('FeedFragment.deleteFeeds', 'FeedFragment.lambda$deleteFeeds$11', 'CALL', 'Delete chain maps each channel to its id inside the flatMap', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:444-456')
e('FeedFragment.deleteFeeds', 'FeedFragment.lambda$deleteFeeds$12', 'CALL', 'Delete chain flatMaps the channel list to its ids', cls='non_standard', via='Rx flatMap dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:444-458')
e('FeedFragment.getAllFeedsSingle', 'FeedFragment.lambda$getAllFeedsSingle$4', 'CALL', 'Single-shot load flatMaps the channel list to item list', cls='non_standard', via='Rx flatMap dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:271-282')
e('FeedFragment.getAllFeedsSingle', 'FeedFragment.lambda$getAllFeedsSingle$5', 'CALL', 'Single-shot load error consumer logs a feed-list error', cls='non_standard', via='Rx error dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:271-282')
e('FeedFragment.markAsReadFeeds', 'FeedFragment.lambda$markAsReadFeeds$13', 'CALL', 'Mark-as-read chain maps each selection to its id', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:509-517')
e('FeedFragment.observeFeeds', 'FeedFragment.lambda$observeFeeds$2', 'CALL', 'Feed observation flatMaps the channel list to an item flowable', cls='non_standard', via='Rx flatMapSingle dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:256-269')
e('FeedFragment.observeFeeds', 'FeedFragment.lambda$observeFeeds$3', 'CALL', 'Feed observation error consumer logs a feed-list error', cls='non_standard', via='Rx error dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:256-269')
e('FeedFragment.onViewCreated', 'FeedFragment.lambda$onViewCreated$0', 'CALL', 'Swipe-refresh listener refreshes all feeds', cls='non_standard', via='SwipeRefreshLayout listener dispatch', evidence='INFERRED listener dispatch; SRC ui/feeds/FeedFragment.java:185')
e('FeedFragment.onViewCreated', 'FeedFragment.lambda$onViewCreated$1', 'CALL', 'Add-channel click starts the add-feed activity', cls='non_standard', via='View click dispatch', evidence='INFERRED View dispatch; SRC ui/feeds/FeedFragment.java:187-188')
e('FeedFragment.subscribeAlertDialog', 'FeedFragment.lambda$subscribeAlertDialog$9', 'CALL', 'Alert-dialog event subscription runs the event lambda', cls='non_standard', via='Rx subscribe event dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:310-313; SRC ui/feeds/FeedFragment.java:313-320')
e('FeedFragment.subscribeMsgViewModel', 'FeedFragment.lambda$subscribeMsgViewModel$6', 'CALL', 'Feed-items-closed subscription runs its lambda', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:286-292')
e('FeedFragment.subscribeMsgViewModel', 'FeedFragment.lambda$subscribeMsgViewModel$7', 'CALL', 'Feeds-deleted filter runs its predicate lambda', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:295-301')
e('FeedFragment.subscribeMsgViewModel', 'FeedFragment.lambda$subscribeMsgViewModel$8', 'CALL', 'Feeds-deleted subscription runs its lambda', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:295-307')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.markAsReadFeeds', 'CALL', 'Mark-as-read menu item marks the selected feeds read', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-397; SRC ui/feeds/FeedFragment.java:509-518')
e('FeedFragment.subscribeAdapter', 'FeedFragment.observeFeeds', 'CALL', 'Adapter subscription observes the feed stream', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:250-253; SRC ui/feeds/FeedFragment.java:256-269')
e('FeedActivity.onCreate', 'FeedFragment.onAttach', 'FRAMEWORK', 'Framework attaches the layout-declared fragment to its host', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:195-200')
e('FeedActivity.onCreate', 'FeedFragment.onCreateView', 'FRAMEWORK', 'Framework inflates the fragment view', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:95-99')
e('FeedChannelListAdapter$ViewHolder.lambda$bind$0', 'FeedFragment.onItemClicked', 'CALL', 'Row click listener forwards the click to the fragment', cls='explicit', evidence='SRC ui/feeds/FeedChannelListAdapter.java:217-223; SRC ui/feeds/FeedFragment.java:341-345')
e('FeedActivity.onCreate', 'FeedFragment.onResume', 'FRAMEWORK', 'Framework resumes the layout-declared fragment', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:223-228')
e('FeedActivity.onCreate', 'FeedFragment.onSaveInstanceState', 'FRAMEWORK', 'Framework saves the fragment instance state', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:241-247')
e('FeedActivity.onCreate', 'FeedFragment.onStart', 'FRAMEWORK', 'Framework starts the layout-declared fragment', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:204-211')
e('FeedActivity.onCreate', 'FeedFragment.onStop', 'FRAMEWORK', 'Framework stops the layout-declared fragment', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:215-219')
e('FeedActivity.onCreate', 'FeedFragment.onViewCreated', 'FRAMEWORK', 'Framework delivers view creation for the layout-declared fragment', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:105-192')
e('FeedActivity.onCreate', 'FeedFragment.onViewStateRestored', 'FRAMEWORK', 'Framework restores the fragment view state', cls='non_standard', via='Android fragment lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/feeds/FeedActivity.java:101; SRC ui/feeds/FeedFragment.java:232-237')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.refreshSelectedFeeds', 'CALL', 'Refresh menu item refreshes the selected feeds', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-392; SRC ui/feeds/FeedFragment.java:481-491')
e('FeedFragment$3.onActionItemClicked', 'FeedFragment.selectAllFeeds', 'CALL', 'Select-all menu item selects all feeds', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:380-395; SRC ui/feeds/FeedFragment.java:435-442')
e('FeedFragment$2.onSelectionChanged', 'FeedFragment.setActionModeTitle', 'CALL', 'Selection change updates the action-mode title', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:148-162; SRC ui/feeds/FeedFragment.java:348-350')
e('FeedFragment.onStart', 'FeedFragment.subscribeAdapter', 'CALL', 'Fragment start subscribes the adapter', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:204-208; SRC ui/feeds/FeedFragment.java:250-254')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in this batch
# (this batch has no UNREACHABLE methods), so no intra-group SUPPRESS
# entries apply. Cross-group auto-call candidates are reported in
# REPORT.md, not suppressed here.
SUPPRESS.update(set())
