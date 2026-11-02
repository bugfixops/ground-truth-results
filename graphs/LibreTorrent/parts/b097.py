# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C16 delivery (2026-11-01): audited A3 base part kept as audited; no label flipped.
# Verification: base part checked against clone graphs/LibreTorrent/scratch/merge-ready/batch097-merge-ready.md
# (labels/kinds match exactly; see REPORT-b097.md). Stronger-evidence rule (b): tree holds no grade for this
# batch's UNREACHABLE keys (tree MERGED_PARTS ends b007; keys occur only in auto_calls.json CHA entries), so no
# grade change. Greps: parts-staging/grep/b097/. Pre-test: private copy on the b007 base; check-2 delta 0 (see report).
# Merger note (recorded, NOT applied by converter): b096/b097 carry the remaining G19 SUPPRESS callee strings
# (FeedItemsAdapter getItemKey/getItemPosition); the merger unions all four G19 strings (b094/b096/b097) so the
# cross-group TorrentListAdapter/FeedChannelListAdapter callers are covered. Kept as audited.
# Batch 97 part (FeedItemsAdapter rest + FeedItemsFragment). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b097_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch97-merge-ready.md (verified identical to the
# helper input copy; batches 93-97 are not A1-affected, so the clone copy is current).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# SUPPRESS: callee-string entries for this batch's UNREACHABLE methods. They suppress
# the CHA interface-dispatch auto edges from every KeyProvider.getKey/getPosition into
# these Selectable methods (intra-group pairs from batches 93/96 plus the cross-group
# CHA pairs from TorrentListAdapter and FeedChannelListAdapter KeyProviders, all listed
# in REPORT.md for merger reconciliation). No other auto edge is suppressed.

e('FeedItemsFragment.onViewCreated', 'FeedItemsAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView binds feed item rows for the adapter set on the list', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/feeditems/FeedItemsFragment.java:152-153; SRC ui/feeditems/FeedItemsAdapter.java:76-79')
e('FeedItemsFragment.onViewCreated', 'FeedItemsAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView creates feed item rows for the adapter set on the list', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/feeditems/FeedItemsFragment.java:152-153; SRC ui/feeditems/FeedItemsAdapter.java:64-73')
e('FeedItemsAdapter.<clinit>', 'FeedItemsAdapter$1.<init>', 'FRAMEWORK', 'Static diffCallback field initialisation creates the anonymous DiffUtil callback', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/feeditems/FeedItemsAdapter.java:105-120')
e('FeedItemsAdapter.submitList', 'FeedItemsAdapter$1.areContentsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil contents check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/feeditems/FeedItemsAdapter.java:82-88; SRC ui/feeditems/FeedItemsAdapter.java:108-112')
e('FeedItemsAdapter.submitList', 'FeedItemsAdapter$1.areItemsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil identity check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/feeditems/FeedItemsAdapter.java:82-88; SRC ui/feeditems/FeedItemsAdapter.java:115-119')
e('FeedItemsAdapter.onCreateViewHolder', 'FeedItemsAdapter$ViewHolder.<init>', 'CALL', 'ViewHolder construction on holder creation', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:72; SRC ui/feeditems/FeedItemsAdapter.java:133-138')
e('FeedItemsAdapter.onBindViewHolder', 'FeedItemsAdapter$ViewHolder.bind', 'CALL', 'Bind feeds the row view from the item and listener', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:78; SRC ui/feeditems/FeedItemsAdapter.java:140-182')
e('FeedItemsAdapter$ViewHolder.lambda$bind$1', 'FeedItemsAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'PopupMenu item-click dispatch for the listener set in the menu-button lambda', cls='non_standard', via='PopupMenu item-click dispatch', evidence='INFERRED PopupMenu dispatch; SRC ui/feeditems/FeedItemsAdapter.java:156-160; SRC ui/feeditems/FeedItemsAdapter.java:156-160')
e('FeedItemsAdapter$ViewHolder.bind', 'FeedItemsAdapter$ViewHolder.lambda$bind$1', 'FRAMEWORK', 'View click dispatch for the menu-button listener', cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/feeditems/FeedItemsAdapter.java:144; SRC ui/feeditems/FeedItemsAdapter.java:144-162')
e('FeedItemsAdapter$ViewHolder.bind', 'FeedItemsAdapter$ViewHolder.lambda$bind$2', 'FRAMEWORK', 'View click dispatch for the item-row listener', cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/feeditems/FeedItemsAdapter.java:164; SRC ui/feeditems/FeedItemsAdapter.java:164-167')
e('FeedItemsFragment.newInstance', 'FeedItemsFragment.<clinit>', 'FRAMEWORK', 'First fragment construction initialises the fragment class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/feeditems/FeedItemsFragment.java:80-87; SRC ui/feeditems/FeedItemsFragment.java:66')
e('FeedItemsFragment.onBackPressed', 'FeedItemsFragment.finish', 'CALL', 'Back press finishes the fragment with BACK result', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:322; SRC ui/feeditems/FeedItemsFragment.java:325-328')
e('FeedItemsFragment.subscribeAdapter', 'FeedItemsFragment.getAllFeedItemsSingle', 'CALL', 'Subscription setup loads all feed items once', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:204; SRC ui/feeditems/FeedItemsFragment.java:223-235')
e('FeedActivity.showFeedItems', 'FeedItemsFragment.getFeedId', 'CALL', 'Two-pane same-feed check reads the current fragment feed id', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:211; SRC ui/feeditems/FeedItemsFragment.java:89-92')
e('FeedItemsFragment.getAllFeedItemsSingle', 'FeedItemsFragment.lambda$getAllFeedItemsSingle$4', 'FRAMEWORK', 'Rx flatMap dispatch inside getAllFeedItemsSingle', cls='non_standard', via='Rx flatMap dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsFragment.java:227-231')
e('FeedItemsFragment.getAllFeedItemsSingle', 'FeedItemsFragment.lambda$getAllFeedItemsSingle$5', 'FRAMEWORK', 'Rx error dispatch inside getAllFeedItemsSingle', cls='non_standard', via='Rx error dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsFragment.java:234-235')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsFragment.lambda$observeFeedItems$2', 'FRAMEWORK', 'Rx flatMapSingle dispatch inside observeFeedItems', cls='non_standard', via='Rx flatMapSingle dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsFragment.java:212-216')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsFragment.lambda$observeFeedItems$3', 'FRAMEWORK', 'Rx error dispatch inside observeFeedItems', cls='non_standard', via='Rx error dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsFragment.java:219-220')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.lambda$onViewCreated$0', 'FRAMEWORK', 'Toolbar navigation click dispatch for the listener set here', cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/feeditems/FeedItemsFragment.java:143')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.lambda$onViewCreated$1', 'FRAMEWORK', 'Swipe-refresh dispatch for the listener set here', cls='non_standard', via='SwipeRefreshLayout dispatch', evidence='INFERRED SwipeRefreshLayout dispatch; SRC ui/feeditems/FeedItemsFragment.java:155')
e('FeedItemsFragment.lambda$onViewCreated$0', 'FeedItemsFragment.onBackPressed', 'CALL', 'Toolbar navigation click runs back-press handling', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:143; SRC ui/feeditems/FeedItemsFragment.java:320-323')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.onCreateOptionsMenu', 'FRAMEWORK', 'Options-menu dispatch for the fragment that opted in via setHasOptionsMenu', cls='non_standard', via='Framework options-menu dispatch', evidence='INFERRED framework menu dispatch; SRC ui/feeditems/FeedItemsFragment.java:139; SRC ui/feeditems/FeedItemsFragment.java:298-303')
e('FeedItemsAdapter$ViewHolder.lambda$bind$2', 'FeedItemsFragment.onItemClicked', 'CALL', 'Item-row click opens the download URL path', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:166; SRC ui/feeditems/FeedItemsFragment.java:246-249')
e('FeedItemsAdapter$ViewHolder.lambda$bind$0', 'FeedItemsFragment.onItemMenuClicked', 'CALL', 'Popup menu click runs the item-menu branch', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:158; SRC ui/feeditems/FeedItemsFragment.java:252-261')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.onOptionsItemSelected', 'FRAMEWORK', 'Toolbar menu-item dispatch for the method reference registered here', cls='non_standard', via='Toolbar menu-item dispatch', evidence='INFERRED toolbar menu dispatch; SRC ui/feeditems/FeedItemsFragment.java:134; SRC ui/feeditems/FeedItemsFragment.java:306-318')
e('FeedItemsFragment.onStart', 'FeedItemsFragment.onResume', 'LIFECYCLE', 'Fragment resumes after start', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/feeditems/FeedItemsFragment.java:159-165; SRC ui/feeditems/FeedItemsFragment.java:176-182')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.onSaveInstanceState', 'LIFECYCLE', 'Fragment saves its instance state after view creation', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/feeditems/FeedItemsFragment.java:117-156; SRC ui/feeditems/FeedItemsFragment.java:185-191')
e('FeedItemsFragment.onResume', 'FeedItemsFragment.onStop', 'LIFECYCLE', 'Fragment stops after resume', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/feeditems/FeedItemsFragment.java:176-182; SRC ui/feeditems/FeedItemsFragment.java:168-173')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.onViewStateRestored', 'LIFECYCLE', 'Fragment restores its view state after view creation', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/feeditems/FeedItemsFragment.java:117-156; SRC ui/feeditems/FeedItemsFragment.java:194-200')

UNREACHABLE.update({
    'FeedItemsAdapter.getItemPosition': ('no_trigger_in_app',
        'Definition FeedItemsAdapter.java:100-103 (indexOf, equals-only). No KeyProvider ever holds a FeedItemsAdapter: the feed items fragment builds no SelectionTracker/KeyProvider, and the only selectable.getItemPosition call sites in the saved full-tree grep are the four KeyProvider getPosition methods of adapters that own one.',
        'Saved full-tree greps grep_selectable_methods.txt, grep_Selectable_all.txt, grep_selectiontracker.txt; batch-97 ROUND 2 flip together with batch 96 row 40',
        'INFERRED'),
})

SUPPRESS.update({
    'FeedItemsAdapter.getItemPosition',
})
