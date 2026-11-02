# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C16 delivery (2026-11-01): audited A3 base part kept as audited; no label flipped.
# Verification: base part checked against clone graphs/LibreTorrent/scratch/merge-ready/batch098-merge-ready.md
# (labels/kinds match exactly; see REPORT-b098.md). Stronger-evidence rule (b): no UNREACHABLE keys in this
# batch, so no grade comparison applies; no change. Greps: parts-staging/grep/b098/ (note file: zero UNREACHABLE
# rows, so no mandatory grep file). Pre-test: private copy on the b007 base; check-2 delta 0 (see report).
# No merger note for this batch; no UNREACHABLE rows.
# Batch 98 part (FeedItemsFragment, FeedItemsListItem, FeedItemsViewModel,
# FeedActivity). Hand-written edges only. Each evidence string cites lines
# printed in graphs/LibreTorrent/scratch/b098_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# No UNREACHABLE rows in this batch, so no SUPPRESS entries apply.

# FeedItemsFragment rows.
e('FeedItemsFragment.newInstance', 'FeedItemsFragment.setFeedId', 'CALL', 'newInstance sets the feed id on the new fragment', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:80-83; SRC ui/feeditems/FeedItemsFragment.java:94-97')
e('FeedItemsFragment.onStart', 'FeedItemsFragment.subscribeAdapter', 'CALL', 'Fragment start subscribes the list adapter', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:159-164; SRC ui/feeditems/FeedItemsFragment.java:202-206')
e('FeedItemsFragment.onStart', 'FeedItemsFragment.subscribeRefreshStatus', 'CALL', 'Fragment start subscribes the refresh status', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:159-164; SRC ui/feeditems/FeedItemsFragment.java:238-243')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsListItem.<init>', 'CALL', 'Feed-item stream maps each FeedItem through the list-item constructor', cls='non_standard', via='Rx map method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsFragment.java:208-215; SRC ui/feeditems/FeedItemsListItem.java:28-35')
e('FeedItemsAdapter$1.areItemsTheSame', 'FeedItemsListItem.equals', 'CALL', 'DiffUtil item comparison delegates to list-item equals', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:115-118; SRC ui/feeditems/FeedItemsListItem.java:51-54')
e('FeedItemsAdapter$1.areContentsTheSame', 'FeedItemsListItem.equalsContent', 'CALL', 'DiffUtil contents comparison delegates to list-item equalsContent', cls='explicit', evidence='SRC ui/feeditems/FeedItemsAdapter.java:108-111; SRC ui/feeditems/FeedItemsListItem.java:56-74')
e('FeedItemsFragment.onViewCreated', 'FeedItemsViewModel.<init>', 'FRAMEWORK', 'ViewModelProvider instantiates the view model for the fragment', cls='non_standard', via='ViewModelProvider instantiation dispatch', evidence='INFERRED ViewModelProvider dispatch; SRC ui/feeditems/FeedItemsFragment.java:123; SRC ui/feeditems/FeedItemsViewModel.java:55-61')
e('FeedItemsFragment.onViewCreated', 'FeedItemsViewModel.clearData', 'CALL', 'Two-pane view creation clears previous view-model data', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:126-128; SRC ui/feeditems/FeedItemsViewModel.java:71-75')
e('FeedItemsFragment.getAllFeedItemsSingle', 'FeedItemsViewModel.getItemsByFeedIdSingle', 'CALL', 'Single-shot list load reads the view-model single', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:223-225; SRC ui/feeditems/FeedItemsViewModel.java:87-90')
e('FeedItemsViewModel.markAllAsRead', 'FeedItemsViewModel.lambda$markAllAsRead$0', 'CALL', 'Mark-all-as-read completable runs its repository runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsViewModel.java:113-120')
e('FeedItemsViewModel.markAsRead', 'FeedItemsViewModel.lambda$markAsRead$1', 'CALL', 'Mark-as-read completable runs its repository runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsViewModel.java:122-127')
e('FeedItemsViewModel.markAsUnread', 'FeedItemsViewModel.lambda$markAsUnread$2', 'CALL', 'Mark-as-unread completable runs its repository runnable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeditems/FeedItemsViewModel.java:129-134')
e('FeedItemsFragment.onOptionsItemSelected', 'FeedItemsViewModel.markAllAsRead', 'CALL', 'Mark-as-read menu item marks all items read', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:306-314; SRC ui/feeditems/FeedItemsViewModel.java:113-120')
e('FeedItemsFragment.onItemMenuClicked', 'FeedItemsViewModel.markAsRead', 'CALL', 'Item menu mark-as-read marks the item read', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:252-257; SRC ui/feeditems/FeedItemsViewModel.java:122-127')
e('FeedItemsFragment.onItemMenuClicked', 'FeedItemsViewModel.markAsUnread', 'CALL', 'Item menu mark-as-unread marks the item unread', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:252-259; SRC ui/feeditems/FeedItemsViewModel.java:129-134')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsViewModel.observeItemsByFeedId', 'CALL', 'Feed-item stream observes items by feed id', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:208-210; SRC ui/feeditems/FeedItemsViewModel.java:82-85')
e('FeedItemsFragment.subscribeRefreshStatus', 'FeedItemsViewModel.observeRefreshStatus', 'CALL', 'Refresh-status subscription observes the view-model status subject', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:238-240; SRC ui/feeditems/FeedItemsViewModel.java:92-95')
e('FeedItemsViewModel.runFetchWorker', 'FeedItemsViewModel.observeWorkResult', 'CALL', 'Fetch worker registers the work-result observer on its LiveData', cls='non_standard', via='LiveData observeForever method-reference dispatch', evidence='INFERRED LiveData dispatch; SRC ui/feeditems/FeedItemsViewModel.java:136-143; SRC ui/feeditems/FeedItemsViewModel.java:146-154')
e('FeedItemsFragment.onViewCreated', 'FeedItemsViewModel.onCleared', 'FRAMEWORK', 'ViewModel lifecycle clears the view model when its provider is cleared', cls='non_standard', via='ViewModel lifecycle dispatch', evidence='INFERRED ViewModel lifecycle dispatch; SRC ui/feeditems/FeedItemsFragment.java:123; SRC ui/feeditems/FeedItemsViewModel.java:64-69')
e('FeedItemsFragment.onOptionsItemSelected', 'FeedItemsViewModel.refreshChannel', 'CALL', 'Refresh menu item refreshes the channel', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:306-312; SRC ui/feeditems/FeedItemsViewModel.java:97-111')
e('FeedItemsViewModel.refreshChannel', 'FeedItemsViewModel.runFetchWorker', 'CALL', 'Channel refresh enqueues the fetch worker', cls='explicit', evidence='SRC ui/feeditems/FeedItemsViewModel.java:97-110; SRC ui/feeditems/FeedItemsViewModel.java:136-144')
e('FeedItemsFragment.onViewCreated', 'FeedItemsViewModel.setFeedId', 'CALL', 'View creation sets the view-model feed id', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:126-128; SRC ui/feeditems/FeedItemsViewModel.java:77-80')

# FeedActivity rows.
e('FeedActivity.onCreate', 'FeedActivity.<clinit>', 'FRAMEWORK', 'First active use of the activity class runs its static initialiser', cls='non_standard', via='JVM class initialization on first active use', evidence='INFERRED JVM dispatch; SRC ui/feeds/FeedActivity.java:75; SRC ui/feeds/FeedActivity.java:91-107')
e('MainActivity.onOptionsItemSelected', 'FeedActivity.<init>', 'FRAMEWORK', 'Framework instantiates the manifest-declared activity for the feed Intent', cls='non_standard', via='Android framework activity instantiation', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:740-741; SRC ui/feeds/FeedActivity.java:91-107')
e('FeedActivity.lambda$new$8', 'FeedActivity.backupFeeds', 'CALL', 'Backup chooser result calls backupFeeds with the chosen data', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:375-385; SRC ui/feeds/FeedActivity.java:346-357')
e('FeedActivity.onOptionsItemSelected', 'FeedActivity.backupFeedsChooseDialog', 'CALL', 'Backup menu item opens the backup chooser dialog', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:248-254; SRC ui/feeds/FeedActivity.java:262-276')
e('FeedActivity.restoreFeedsBackup', 'FeedActivity.backupFeedsErrorDialog', 'CALL', 'Restore subscribe error handler shows the backup error dialog', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:359-370; SRC ui/feeds/FeedActivity.java:292-304')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.getCurrentFeedItemsFragment', 'CALL', 'Feeds-deleted handling reads the current feed-items fragment', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:182-185; SRC ui/feeds/FeedActivity.java:227-236')
e('FeedActivity.onCreate', 'FeedActivity.initLayout', 'CALL', 'Activity creation initialises the layout', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:91-102; SRC ui/feeds/FeedActivity.java:109-119')
e('FeedActivity.backupFeeds', 'FeedActivity.lambda$backupFeeds$4', 'CALL', 'Backup callable runs the save-feeds-sync lambda', cls='non_standard', via='Rx Completable.fromCallable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:346-350')
e('FeedActivity.backupFeeds', 'FeedActivity.lambda$backupFeeds$5', 'CALL', 'Backup success runs the success-toast lambda', cls='non_standard', via='Rx subscribe success dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:346-356')
e('FeedActivity.initLayout', 'FeedActivity.lambda$initLayout$0', 'CALL', 'Toolbar navigation click runs the finish lambda', cls='non_standard', via='View click dispatch', evidence='INFERRED View dispatch; SRC ui/feeds/FeedActivity.java:109-116')
e('FeedActivity.backupFeedsChooseDialog', 'FeedActivity.lambda$new$8', 'CALL', 'Backup chooser launch delivers its result to the registered callback', cls='non_standard', via='ActivityResult delivery dispatch', evidence='INFERRED ActivityResult dispatch; SRC ui/feeds/FeedActivity.java:262-275; SRC ui/feeds/FeedActivity.java:373-385')
e('FeedActivity.restoreFeedsChooseDialog', 'FeedActivity.lambda$new$9', 'CALL', 'Restore chooser launch delivers its result to the registered callback', cls='non_standard', via='ActivityResult delivery dispatch', evidence='INFERRED ActivityResult dispatch; SRC ui/feeds/FeedActivity.java:278-289; SRC ui/feeds/FeedActivity.java:389-401')
e('FeedActivity.restoreFeedsBackup', 'FeedActivity.lambda$restoreFeedsBackup$6', 'CALL', 'Restore callable runs the restore-feeds-sync lambda', cls='non_standard', via='Rx Observable.fromCallable dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:359-361')
e('FeedActivity.restoreFeedsBackup', 'FeedActivity.lambda$restoreFeedsBackup$7', 'CALL', 'Restore success runs the success-toast and refresh lambda', cls='non_standard', via='Rx subscribe success dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:359-370')
e('FeedActivity.subscribeAlertDialog', 'FeedActivity.lambda$subscribeAlertDialog$1', 'CALL', 'Alert-dialog event subscription runs the event lambda', cls='non_standard', via='Rx subscribe event dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:138-141; SRC ui/feeds/FeedActivity.java:141-168')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.lambda$subscribeMsgViewModel$2', 'CALL', 'Feed-items-closed subscription runs the blank-fragment lambda', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:178-180')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.lambda$subscribeMsgViewModel$3', 'CALL', 'Feeds-deleted subscription runs the deleted-feeds lambda', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/feeds/FeedActivity.java:182-188')
e('MainActivity.onOptionsItemSelected', 'FeedActivity.onCreate', 'FRAMEWORK', 'Framework delivers onCreate for the activity started from the main menu', cls='non_standard', via='Android activity lifecycle dispatch', evidence='INFERRED framework dispatch; SRC ui/main/MainActivity.java:740-741; SRC ui/feeds/FeedActivity.java:91-107')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in this batch
# (this batch has no UNREACHABLE methods), and no bytecode call from a
# batch-98 REACHABLE method into a batch-98 UNREACHABLE method exists,
# so no SUPPRESS entries apply. Cross-group auto-call candidates are
# reported in REPORT.md, not suppressed here.
SUPPRESS.update(set())
