# Batch 18 part (MainApplication, FeedParser helpers, HttpConnection, InputFilterRange
# and its Builder, RepositoryHelper accessors, TorrentBuilder). Hand-written edges and
# UNREACHABLE entries only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b018_printed.txt. Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# Routes into batch-18 methods that already exist in graph_def.py (not repeated here):
#   S_ENTRY -> MainApplication.<clinit> / <init> / onCreate (100, 102, 104)
#   MainApplication.onCreate -> increaseCursorWindowSize (112)
#   FeedViewModel.runFetchWorker -> FeedFetcherWorker.doWork (2703) -> fetchChannels (2705) -> fetchChannel (2707)
#   FeedFetcherWorker.fetchChannel -> FeedParser.<init> (2709), FeedParser.getItems (2711), FeedParser.getTitle (2713)
#   FeedParser.getItems -> FeedParser.findDownloadUrl (2781)
#   FeedParser.findDownloadUrl -> watchEnclosure (2783), watchTorrentInfoHash (2785), watchMediaContent (3595), watchGuid (3597)
#   FeedParser.watchMediaContent -> FeedParser.watchMediaHash (3611)
#   SettingsFragment.setFragment -> NetworkSettingsFragment.onCreate (2594)
#   NetworkSettingsFragment.onCreate -> NetworkSettingsFragment.lambda$onCreate$0 (2320, 2322)
#   MainActivity.onCreate -> TorrentInfoProvider.getInstance(Context) (116)
#   TorrentEngine.getInstance -> TorrentEngine.<init> (120)
#   CreateTorrentDialog.buildTorrent -> CreateTorrentViewModel.buildTorrent (776) -> CreateTorrentViewModel.makeBuilder (778)
#
# OPEN, no edge and no UNREACHABLE entry here (recorded in parts/b018.md):
#   DataBinderMapperImpl$InnerBrLookup.<clinit>, DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>:
#     generated code, not in the upload (scratch/b018_generated_grep.txt).
#   MainApplication.lambda$onCreate$0: registered only when
#     Thread.getDefaultUncaughtExceptionHandler() is null at MainApplication.java:61. The framework
#     code that sets the default handler is not in the upload (fw_src grep: no file names).

# FeedParser: the constructor download and the item-link helpers, which the existing feed route does not reach.
e('FeedParser.<init>', 'Utils.fetchHttpUrl', 'CALL', 'Download the feed body before parsing it',
  cls='explicit', evidence='SRC core/FeedParser.java:62-67; SRC core/utils/Utils.java:462-466')
e('FeedParser.getItems', 'FeedParser.getFirstNotNullLink', 'CALL', 'Pick the first non-empty item link as the article URL',
  cls='explicit', evidence='SRC core/FeedParser.java:97,118-126')
e('FeedParser.getItems', 'FeedParser.watchDownloadableLink', 'CALL', 'Look for a magnet or torrent link among the item links',
  cls='explicit', evidence='SRC core/FeedParser.java:98,128-139')
e('FeedParser.watchDownloadableLink', 'FeedParser.isMagnetOrTorrent', 'CALL', 'Test each item link for a magnet URI or .torrent suffix',
  cls='explicit', evidence='SRC core/FeedParser.java:134,263-266')

# HttpConnection: reached from Utils.fetchHttpUrl after the connectivity check.
e('Utils.fetchHttpUrl', 'HttpConnection.<init>', 'CALL', 'Create the HTTP connection once the network check passes',
  env='Utils.checkConnectivity(context)', env_kinds=('network',), cls='explicit',
  note='Reached only when the throw at Utils.java:466-467 does not fire: if (!Utils.checkConnectivity(context)) throw new FetchLinkException("No network connection");',
  evidence='SRC core/utils/Utils.java:466-467,472; SRC core/HttpConnection.java:66-70')
e('Utils.fetchHttpUrl', 'HttpConnection.setListener', 'CALL', 'Attach the response listener to the connection',
  cls='explicit', evidence='SRC core/utils/Utils.java:477; SRC core/HttpConnection.java:72-75')
e('Utils.fetchHttpUrl', 'HttpConnection.run', 'CALL', 'Run the HTTP request synchronously',
  cls='explicit', evidence='SRC core/utils/Utils.java:512; SRC core/HttpConnection.java:78-124')

# InputFilterRange: the port filter is created in NetworkSettingsFragment.onCreate and set on the start-port editor.
e('NetworkSettingsFragment.onCreate', 'InputFilterRange.<clinit>', 'CALL', 'Create the port range filter on its first static read',
  cls='non_standard', via='JVM class initialization on first static field read of InputFilterRange.PORT_FILTER',
  evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:157; SRC core/InputFilterRange.java:33-41; INFERRED JVM class initialization on static field read')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.<init>', 'CALL', 'Create the builder for the port range',
  cls='explicit', evidence='SRC core/InputFilterRange.java:33,38')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.setMin', 'CALL', 'Set the lower bound of the port range',
  cls='explicit', evidence='SRC core/InputFilterRange.java:34,39')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.setMax', 'CALL', 'Set the upper bound of the port range',
  cls='explicit', evidence='SRC core/InputFilterRange.java:35,40')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.build', 'CALL', 'Build the port range filter',
  cls='explicit', evidence='SRC core/InputFilterRange.java:36,41')
e('InputFilterRange$Builder.build', 'InputFilterRange.<init>', 'CALL', 'Construct the range filter from the builder bounds',
  cls='explicit', evidence='SRC core/InputFilterRange.java:107-112')
e('NetworkSettingsFragment.lambda$onCreate$0', 'InputFilterRange.filter', 'FRAMEWORK', 'Filter each start-port edit through the port range',
  cls='standard',
  evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:163; FW-SRC core/java/android/widget/TextView.java:6147-6156; INFERRED InputFilter.filter dispatch (text/InputFilter.java is not in the upload)')
e('InputFilterRange.filter', 'InputFilterRange.inRange', 'CALL', 'Check the parsed number against the range bounds',
  cls='explicit', evidence='SRC core/InputFilterRange.java:65-73,83-85')

# RepositoryHelper accessors that the existing routes do not reach.
e('FeedFetcherWorker.doWork', 'RepositoryHelper.getFeedRepository', 'CALL', 'Obtain the feed repository for the fetch run',
  cls='explicit', evidence='SRC service/FeedFetcherWorker.java:77; SRC core/RepositoryHelper.java:52-59')
e('FeedFetcherWorker.doWork', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain the settings repository for feed fetch options',
  cls='explicit', evidence='SRC service/FeedFetcherWorker.java:78; SRC core/RepositoryHelper.java:61-67')
e('TorrentInfoProvider.getInstance(Context)', 'RepositoryHelper.getTagRepository', 'CALL', 'Obtain the tag repository for the torrent info provider',
  cls='explicit', evidence='SRC core/model/TorrentInfoProvider.java:76-84 (call at 82); SRC core/RepositoryHelper.java:69-75')
e('TorrentEngine.<init>', 'RepositoryHelper.getTorrentRepository', 'CALL', 'Obtain the torrent repository for the engine',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:128-135 (call at 130); SRC core/RepositoryHelper.java:43-50')
e('TorrentEngine.<init>', 'RepositoryHelper.getTagRepository', 'CALL', 'Obtain the tag repository for the engine',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:131')
e('TorrentEngine.<init>', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain the settings repository for the engine',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:133')

# TorrentBuilder: created and configured in the create-torrent view model, then built.
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.<init>', 'CALL', 'Create the torrent builder for the dialog inputs',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:186-189; SRC core/TorrentBuilder.java:88-90')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.addTrackers', 'CALL', 'Attach the validated tracker list to the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:193; SRC core/TorrentBuilder.java:116-125')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.addUrlSeeds', 'CALL', 'Attach the validated web seed list to the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:194; SRC core/TorrentBuilder.java:127-131')
e('CreateTorrentViewModel.buildTorrent', 'TorrentBuilder.build', 'CALL', 'Start building the torrent bytes',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:157,171; SRC core/TorrentBuilder.java:173-176')

# UNREACHABLE: no app source calls the getters; InputFilterRange.inRange reads the fields directly.
UNREACHABLE.update({
    'InputFilterRange.getMin': ('no_trigger_in_app',
        'Source-root grep for getMin() finds only the declaration; inRange reads the min field directly, so no app code calls getMin().',
        'SRC core/InputFilterRange.java:52-56; scratch/b018_printed.txt (grep getMin()/getMax() over the source root)', 'SOURCE'),
    'InputFilterRange.getMax': ('no_trigger_in_app',
        'Source-root grep for getMax() finds only the declaration; inRange reads the max field directly, so no app code calls getMax().',
        'SRC core/InputFilterRange.java:58-62; scratch/b018_printed.txt (grep getMin()/getMax() over the source root)', 'SOURCE'),
})
