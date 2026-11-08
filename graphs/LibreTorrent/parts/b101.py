# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 101 part (FeedFragment subscriptions and anonymous classes, FeedViewModel,
# MsgFeedViewModel, FileManagerAdapter head). Hand-written edges only. Each evidence
# string cites lines printed in graphs/LibreTorrent/scratch/b101_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# No UNREACHABLE rows in this batch, so no SUPPRESS entries apply.

# FeedFragment subscription / anonymous-class rows.
e('FeedFragment.onStart', 'FeedFragment.subscribeAlertDialog', 'CALL', 'Fragment start subscribes the alert-dialog events', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:204-209; SRC ui/feeds/FeedFragment.java:310-332')
e('FeedFragment.onStart', 'FeedFragment.subscribeMsgViewModel', 'CALL', 'Fragment start subscribes the message view model', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:204-210; SRC ui/feeds/FeedFragment.java:286-309')
e('FeedFragment.onStart', 'FeedFragment.subscribeRefreshStatus', 'CALL', 'Fragment start subscribes the refresh status', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:204-211; SRC ui/feeds/FeedFragment.java:333-337')
e('FeedFragment.onViewCreated', 'FeedFragment$1.<init>', 'CALL', 'View creation creates the reuse-updated-holder animator', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:122-130')
e('FeedFragment.onViewCreated', 'FeedFragment$1.canReuseUpdatedViewHolder', 'FRAMEWORK', 'RecyclerView asks the animator whether an updated holder can be reused', cls='non_standard', via='RecyclerView animator dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/feeds/FeedFragment.java:122-130; SRC ui/feeds/FeedFragment.java:124-126')
e('FeedFragment.onViewCreated', 'FeedFragment$2.<init>', 'CALL', 'View creation registers the selection observer', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:146')
e('FeedFragment.onViewCreated', 'FeedFragment$2.onSelectionChanged', 'FRAMEWORK', 'Selection tracker reports a selection change to its observer', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:146-169')
e('FeedFragment.onViewCreated', 'FeedFragment$2.onSelectionRestored', 'FRAMEWORK', 'Selection tracker reports a restored selection to its observer', cls='non_standard', via='SelectionTracker dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/feeds/FeedFragment.java:146; SRC ui/feeds/FeedFragment.java:172-178')
e('FeedFragment.<init>', 'FeedFragment$3.<init>', 'CALL', 'Fragment construction creates the action-mode callback field', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:353')
e('FeedFragment$2.onSelectionChanged', 'FeedFragment$3.onActionItemClicked', 'FRAMEWORK', 'Action mode started on selection change dispatches menu clicks to its callback', cls='non_standard', via='ActionMode dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/feeds/FeedFragment.java:148-154; SRC ui/feeds/FeedFragment.java:380-404')
e('FeedFragment$2.onSelectionChanged', 'FeedFragment$3.onCreateActionMode', 'FRAMEWORK', 'Action mode started on selection change creates its mode through the callback', cls='non_standard', via='ActionMode dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/feeds/FeedFragment.java:148-154; SRC ui/feeds/FeedFragment.java:371-378')
e('FeedFragment$2.onSelectionChanged', 'FeedFragment$3.onDestroyActionMode', 'FRAMEWORK', 'Action mode started on selection change destroys through the callback', cls='non_standard', via='ActionMode dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/feeds/FeedFragment.java:148-154; SRC ui/feeds/FeedFragment.java:405-409')
e('FeedFragment$2.onSelectionChanged', 'FeedFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Action mode started on selection change prepares through the callback', cls='non_standard', via='ActionMode dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/feeds/FeedFragment.java:148-154; SRC ui/feeds/FeedFragment.java:356-369')

# FeedViewModel rows.
e('FeedFragment.onViewCreated', 'FeedViewModel.<init>', 'FRAMEWORK', 'ViewModelProvider instantiates the feed view model for the fragment', cls='non_standard', via='ViewModelProvider instantiation dispatch', evidence='INFERRED ViewModelProvider dispatch; SRC ui/feeds/FeedFragment.java:112; SRC ui/feeds/FeedViewModel.java:60-65')
e('FeedFragment.copyChannelUrl', 'FeedViewModel.copyFeedUrlToClipboard', 'CALL', 'Copy-channel-URL copies the selected channel URL through the view model', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:464-473; SRC ui/feeds/FeedViewModel.java:92-103')
e('FeedFragment.deleteFeeds', 'FeedViewModel.deleteFeeds', 'CALL', 'Delete chain deletes the selected feeds through the view model', cls='non_standard', via='Rx doOnSuccess method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:444-452; SRC ui/feeds/FeedViewModel.java:85-90')
e('FeedFragment.getAllFeedsSingle', 'FeedViewModel.getAllFeedsSingle', 'CALL', 'Single-shot load reads the view-model feed single', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:271-273; SRC ui/feeds/FeedViewModel.java:75-78')
e('FeedViewModel.deleteFeeds', 'FeedViewModel.lambda$deleteFeeds$0', 'CALL', 'Delete-feeds completable runs its repository runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedViewModel.java:85-90')
e('FeedViewModel.markAsReadFeeds', 'FeedViewModel.lambda$markAsReadFeeds$1', 'CALL', 'Mark-as-read completable runs its repository runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedViewModel.java:147-151')
e('FeedFragment.markAsReadFeeds', 'FeedViewModel.markAsReadFeeds', 'CALL', 'Mark-as-read chain marks the selected feeds read through the view model', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:509-517; SRC ui/feeds/FeedViewModel.java:147-151')
e('FeedFragment.subscribeRefreshStatus', 'FeedViewModel.observeRefreshStatus', 'CALL', 'Refresh-status subscription observes the view-model status subject', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:333-335; SRC ui/feeds/FeedViewModel.java:130-133')
e('FeedViewModel.runFetchWorker', 'FeedViewModel.observeWorkResult', 'CALL', 'Fetch worker registers the work-result observer on its LiveData', cls='non_standard', via='LiveData observeForever method-reference dispatch', evidence='INFERRED LiveData dispatch; SRC ui/feeds/FeedViewModel.java:153-160; SRC ui/feeds/FeedViewModel.java:163-171')
e('FeedFragment.observeFeeds', 'FeedViewModel.observerAllFeeds', 'CALL', 'Feed observation observes all feeds through the view model', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:256-258; SRC ui/feeds/FeedViewModel.java:80-83')
e('FeedFragment.onViewCreated', 'FeedViewModel.onCleared', 'FRAMEWORK', 'ViewModel lifecycle clears the view model when its provider is cleared', cls='non_standard', via='ViewModel lifecycle dispatch', evidence='INFERRED ViewModel lifecycle dispatch; SRC ui/feeds/FeedFragment.java:112; SRC ui/feeds/FeedViewModel.java:68-73')
e('FeedFragment.lambda$onViewCreated$0', 'FeedViewModel.refreshAllFeeds', 'CALL', 'Swipe-refresh listener refreshes all feeds through the view model', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:185; SRC ui/feeds/FeedViewModel.java:118-128')
e('FeedFragment.refreshSelectedFeeds', 'FeedViewModel.refreshFeeds', 'CALL', 'Refresh-selected-feeds refreshes the selected feed ids through the view model', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:481-491; SRC ui/feeds/FeedViewModel.java:105-116')
e('FeedActivity.restoreFeedsBackup', 'FeedViewModel.restoreFeedsSync', 'CALL', 'Restore backup restores feeds synchronously through the view model', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:359-361; SRC ui/feeds/FeedViewModel.java:140-145')
e('FeedViewModel.refreshFeeds', 'FeedViewModel.runFetchWorker', 'CALL', 'Feed refresh enqueues the fetch worker', cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:105-115; SRC ui/feeds/FeedViewModel.java:153-161')
e('FeedActivity.backupFeeds', 'FeedViewModel.saveFeedsSync', 'CALL', 'Backup saves feeds synchronously through the view model', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:346-349; SRC ui/feeds/FeedViewModel.java:135-139')

# MsgFeedViewModel rows.
e('FeedFragment.onViewCreated', 'MsgFeedViewModel.<init>', 'FRAMEWORK', 'ViewModelProvider instantiates the message view model for the fragment', cls='non_standard', via='ViewModelProvider instantiation dispatch', evidence='INFERRED ViewModelProvider dispatch; SRC ui/feeds/FeedFragment.java:113; SRC ui/feeds/MsgFeedViewModel.java:29-33')
e('FeedActivity.onFragmentFinished', 'MsgFeedViewModel.feedItemsClosed', 'CALL', 'Two-pane fragment finish reports feed items closed', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:406-410; SRC ui/feeds/MsgFeedViewModel.java:45-47')
e('FeedFragment.onItemClicked', 'MsgFeedViewModel.feedItemsOpened', 'CALL', 'Item click reports feed items opened', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:341-345; SRC ui/feeds/MsgFeedViewModel.java:35-38')
e('FeedFragment.deleteFeeds', 'MsgFeedViewModel.feedsDeleted', 'CALL', 'Delete chain reports the deleted feeds through the message view model', cls='non_standard', via='Rx subscribe method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedFragment.java:444-458; SRC ui/feeds/MsgFeedViewModel.java:55-58')
e('FeedFragment.subscribeMsgViewModel', 'MsgFeedViewModel.observeFeedItemsClosed', 'CALL', 'Message subscription observes feed-items-closed events', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:286-289; SRC ui/feeds/MsgFeedViewModel.java:50-53')
e('FeedActivity.subscribeMsgViewModel', 'MsgFeedViewModel.observeFeedItemsOpened', 'CALL', 'Activity message subscription observes feed-items-opened events', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:172-174; SRC ui/feeds/MsgFeedViewModel.java:40-42')
e('FeedFragment.subscribeMsgViewModel', 'MsgFeedViewModel.observeFeedsDeleted', 'CALL', 'Message subscription observes feeds-deleted events', cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:286-295; SRC ui/feeds/MsgFeedViewModel.java:60-63')

# FileManagerAdapter head rows.
e('FileManagerDialog.onCreate', 'FileManagerAdapter.<clinit>', 'FRAMEWORK', 'First active use of the adapter class runs its static initialisers', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM dispatch; SRC ui/filemanager/FileManagerDialog.java:196; SRC ui/filemanager/FileManagerAdapter.java:57; SRC ui/filemanager/FileManagerAdapter.java:96')
e('FileManagerDialog.onCreate', 'FileManagerAdapter.<init>', 'CALL', 'Dialog creation constructs the file-manager adapter', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:196; SRC ui/filemanager/FileManagerAdapter.java:64-70')
e('FileManagerAdapter.submitList', 'FileManagerAdapter.lambda$static$0', 'CALL', 'List submission sorts through the directory-first comparator', cls='non_standard', via='Library sort dispatch to comparator lambda', evidence='INFERRED library dispatch; SRC ui/filemanager/FileManagerAdapter.java:88-94; SRC ui/filemanager/FileManagerAdapter.java:57-62')
e('FileManagerDialog.onCreate', 'FileManagerAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView binds rows of the adapter set on the file list', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/filemanager/FileManagerDialog.java:196-197; SRC ui/filemanager/FileManagerAdapter.java:82-85')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in this batch
# (this batch has no UNREACHABLE methods), so no intra-group SUPPRESS
# entries apply. Cross-group auto-call candidates are reported in
# REPORT.md, not suppressed here.
SUPPRESS.update(set())
