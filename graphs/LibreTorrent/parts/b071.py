# Citation-form rework 2026-11-01: evidence paths with a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS, line ranges unchanged (full paths remain in untouched .md/printed files).
# Batch 71 part (receivers PowerReceiver, SchedulerReceiver; workers FeedDownloaderWorker, FeedFetcherWorker, SaveLogWorker; Scheduler).
# Hand-written edges only; rows covered by a pre-existing trunk edge are
# named on the .md Dependencies line and get no duplicate edge here.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b071_printed.txt (this helper's copy:
# scratch/b071_printed.txt).
# Labels/kinds come from the authoritative clone merge-ready batch file;
# nothing is flipped here (see REPORT.md for flagged rows).

e('TorrentEngine.switchPowerReceiver', 'PowerReceiver.getFilter', 'CALL', 'Battery-control branch registers with the standard filter', cls='explicit', evidence='SRC TorrentEngine.java:1005; SRC receiver/PowerReceiver.java:53-64')
e('TorrentEngine.switchPowerReceiver', 'PowerReceiver.onReceive', 'CALL', 'Dynamically registered receiver delivers power and battery broadcasts', cls='non_standard', via='framework broadcast delivery after dynamic registration', evidence='INFERRED framework dispatch; SRC TorrentEngine.java:1001,1005; SRC receiver/PowerReceiver.java:36-50')
e('FeedFetcherWorker.sendFetchedItems', 'FeedDownloaderWorker.<clinit>', 'CALL', 'First reference to the worker class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through the enqueued work request', evidence='INFERRED class-init rule; SRC service/FeedFetcherWorker.java:232-236')
e('FeedFetcherWorker.sendFetchedItems', 'FeedDownloaderWorker.<init>', 'CALL', 'WorkManager instantiates the enqueued feed-downloader worker', cls='non_standard', via='WorkManager instantiates enqueued worker', evidence='INFERRED WorkManager dispatch; SRC service/FeedFetcherWorker.java:232-236')
e('FeedFetcherWorker.sendFetchedItems', 'FeedDownloaderWorker.doWork', 'CALL', 'WorkManager runs the enqueued feed-downloader work', cls='non_standard', via='WorkManager dispatch of enqueued work', evidence='INFERRED WorkManager dispatch; SRC service/FeedFetcherWorker.java:232-236')
e('FeedDownloaderWorker.doWork', 'FeedDownloaderWorker.addTorrents', 'CALL', 'Download-torrent-list action adds the fetched torrents', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:89')
e('FeedDownloaderWorker.doWork', 'FeedDownloaderWorker.fetchTorrents', 'CALL', 'Download-torrent-list action fetches the listed items', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:89')
e('FeedDownloaderWorker.fetchTorrents', 'FeedDownloaderWorker.fetchTorrent', 'CALL', 'Fetch loop resolves each item id to a torrent', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:101')
e('Scheduler.runPeriodicalRefreshFeeds', 'FeedFetcherWorker.<clinit>', 'CALL', 'First reference to the worker class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through the periodic work request', evidence='INFERRED class-init rule; SRC service/Scheduler.java:116')
e('Scheduler.runPeriodicalRefreshFeeds', 'FeedFetcherWorker.<init>', 'CALL', 'WorkManager instantiates the enqueued feed-fetcher worker', cls='non_standard', via='WorkManager instantiates enqueued worker', evidence='INFERRED WorkManager dispatch; SRC service/Scheduler.java:116-125')
e('FeedFetcherWorker.doWork', 'FeedFetcherWorker.fetchChannelsByUrl', 'CALL', 'Fetch-channel-list action fetches each listed channel', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:97-98')
e('FeedFetcherWorker.fetchChannel', 'FeedFetcherWorker.filterItemDuplicates', 'CALL', 'Channel fetch removes duplicate items when duplicate removal is enabled', cls='explicit', guard='pref.feedRemoveDuplicates()', evidence='SRC service/FeedFetcherWorker.java:169-170')
e('FeedFetcherWorker.fetchChannel', 'FeedFetcherWorker.filterItems', 'CALL', 'Channel fetch filters items by date and known ids', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:167')
e('FeedFetcherWorker.sendFetchedItems', 'FeedFetcherWorker.isMatch', 'CALL', 'Fetched-items send tests each item against the channel filter', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:219')
e('FeedFetcherWorker.filterItemDuplicates', 'FeedFetcherWorker.lambda$filterItemDuplicates$1', 'CALL', 'Duplicate filter runs its removeIf predicate', cls='non_standard', via='removeIf predicate dispatch', evidence='INFERRED removeIf dispatch; SRC service/FeedFetcherWorker.java:203')
e('FeedFetcherWorker.filterItems', 'FeedFetcherWorker.lambda$filterItems$0', 'CALL', 'Item filter runs its removeIf predicate', cls='non_standard', via='removeIf predicate dispatch', evidence='INFERRED removeIf dispatch; SRC service/FeedFetcherWorker.java:193')
e('FeedFetcherWorker.fetchChannel', 'FeedFetcherWorker.sendFetchedItems', 'CALL', 'Channel fetch sends fetched items when auto-download applies', cls='explicit', guard='!noAutoDownload && channel.autoDownload', evidence='SRC service/FeedFetcherWorker.java:183-184')
e('FeedFetcherWorker.doWork', 'FeedFetcherWorker.deleteOldItems', 'CALL', 'Work run deletes items older than the keep border', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:83')
e('LogViewModel.saveLog', 'SaveLogWorker.<clinit>', 'CALL', 'First reference to the worker class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through the enqueued work request', evidence='INFERRED class-init rule; SRC ui/log/LogViewModel.java:208-212')
e('LogViewModel.saveLog', 'SaveLogWorker.<init>', 'CALL', 'WorkManager instantiates the enqueued save-log worker', cls='non_standard', via='WorkManager instantiates enqueued worker', evidence='INFERRED WorkManager dispatch; SRC ui/log/LogViewModel.java:208-212')
e('LogViewModel.saveLog', 'SaveLogWorker.doWork', 'CALL', 'WorkManager runs the enqueued save-log work', cls='non_standard', via='WorkManager dispatch of enqueued work', evidence='INFERRED WorkManager dispatch; SRC ui/log/LogViewModel.java:208-212')
e('SaveLogWorker.doWork', 'SaveLogWorker.saveLog', 'CALL', 'Work run saves the log file when a file path is present', cls='explicit', evidence='SRC service/SaveLogWorker.java:81')
e('SaveLogWorker.doWork', 'SaveLogWorker.showFailToast', 'CALL', 'Null file path shows the save-failed toast', cls='explicit', evidence='SRC service/SaveLogWorker.java:74')
e('SaveLogWorker.saveLog', 'SaveLogWorker.showSuccessToast', 'CALL', 'Successful save shows the save-success toast', cls='explicit', evidence='SRC service/SaveLogWorker.java:97')
e('SaveLogWorker.showFailToast', 'SaveLogWorker.lambda$showFailToast$0', 'CALL', 'Fail toast posts its toast runnable on the handler', cls='non_standard', via='handler.post dispatch', evidence='INFERRED handler dispatch; SRC service/SaveLogWorker.java:114-118')
e('SaveLogWorker.showSuccessToast', 'SaveLogWorker.lambda$showSuccessToast$1', 'CALL', 'Success toast posts its toast runnable on the handler', cls='non_standard', via='handler.post dispatch', evidence='INFERRED handler dispatch; SRC service/SaveLogWorker.java:123-127')
e('FeedSettingsFragment.onPreferenceChange', 'Scheduler.cancelPeriodicalRefreshFeeds', 'CALL', 'Auto-refresh turned off cancels the periodic feed refresh', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:136')
e('SchedulingSettingsFragment.onPreferenceChange', 'Scheduler.cancelStartAppAlarm', 'CALL', 'Scheduling-start turned off cancels the start alarm', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:204')
e('SchedulingSettingsFragment.onPreferenceChange', 'Scheduler.cancelStopAppAlarm', 'CALL', 'Scheduling-shutdown turned off cancels the stop alarm', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:217')
e('Scheduler.runPeriodicalRefreshFeeds', 'Scheduler.getRefreshFeedsConstraints', 'CALL', 'Periodic refresh builds its network constraints', cls='explicit', evidence='SRC service/Scheduler.java:120')
e('FeedSettingsFragment.onPreferenceChange', 'Scheduler.runPeriodicalRefreshFeeds', 'CALL', 'Auto-refresh on, or interval changed, schedules the periodic feed refresh', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:134,142')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# SUPPRESS: recomputed from auto_calls.json + javap scan for this batch's
# rows; the recomputation and any cross-group candidates are recorded in
# REPORT.md. No intra-group pair was found, so no entries apply here.
SUPPRESS.update(set())
