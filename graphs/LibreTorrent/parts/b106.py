# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 106 part (LogActivity remainder, LogAdapter, LogDataSource and LogMutableParams). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b106_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

e('LogActivity$2.onScrolled', 'LogActivity.showFabDown', 'CALL', 'Downward scroll shows the down fab', evidence='SRC ui/log/LogActivity.java:349,367; SRC ui/log/LogActivity.java:421-426')
e('LogActivity$2.onScrolled', 'LogActivity.showFabUp', 'CALL', 'Upward scroll shows the up fab', evidence='SRC ui/log/LogActivity.java:352,370; SRC ui/log/LogActivity.java:408-413')
e('LogActivity.onOptionsItemSelected', 'LogActivity.showFilterDialog', 'CALL', 'Filter menu item shows the session-log filter dialog', evidence='SRC ui/log/LogActivity.java:242; SRC ui/log/LogActivity.java:250-257')
e('LogActivity.onOptionsItemSelected', 'LogActivity.showLogSettings', 'CALL', 'Log-settings menu item starts the settings activity', evidence='SRC ui/log/LogActivity.java:244; SRC ui/log/LogActivity.java:259-262')
e('LogActivity.onOptionsItemSelected', 'LogActivity.toggleRecord', 'CALL', 'Record menu item toggles log recording', evidence='SRC ui/log/LogActivity.java:238; SRC ui/log/LogActivity.java:281-302')
e('LogActivity.onCreate', 'LogActivity.updateToolbarSubtitle', 'CALL', 'onCreate sets the initial toolbar subtitle', evidence='SRC ui/log/LogActivity.java:102; SRC ui/log/LogActivity.java:443-450')
e('LogActivity.<init>', 'LogActivity$1.<init>', 'CALL', 'Field initialiser constructs the params callback', evidence='SRC ui/log/LogActivity.java:175-183')
e('LogActivity.onStart', 'LogActivity$1.onPropertyChanged', 'FRAMEWORK', 'Observable dispatch invalidates the menu on logging change', cls='non_standard', via='Observable dispatch', evidence='INFERRED Observable dispatch; SRC ui/log/LogActivity.java:172; SRC ui/log/LogActivity.java:178-182')
e('LogActivity.<init>', 'LogActivity$2.<init>', 'CALL', 'Field initialiser constructs the scroll callback', evidence='SRC ui/log/LogActivity.java:338-406')
e('LogActivity.onCreate', 'LogActivity$2.onScrollStateChanged', 'FRAMEWORK', 'RecyclerView dispatch reports scroll-state changes', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/log/LogActivity.java:122; SRC ui/log/LogActivity.java:359-405')
e('LogActivity.onCreate', 'LogActivity$2.onScrolled', 'FRAMEWORK', 'RecyclerView dispatch reports scrolling', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/log/LogActivity.java:122; SRC ui/log/LogActivity.java:343-356')
e('LogActivity.onCreate', 'LogAdapter.<clinit>', 'FRAMEWORK', 'First LogAdapter construction initialises the adapter class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/log/LogActivity.java:116; SRC ui/log/LogAdapter.java:67')
e('LogActivity.onCreate', 'LogAdapter.<init>', 'CALL', 'onCreate constructs the log adapter', evidence='SRC ui/log/LogActivity.java:116; SRC ui/log/LogAdapter.java:39-44')
e('LogActivity.onCreate', 'LogAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView dispatch binds each visible log row', cls='non_standard', via='RecyclerView/PagedListAdapter dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/log/LogActivity.java:117; SRC ui/log/LogAdapter.java:60-65')
e('LogActivity.onCreate', 'LogAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView dispatch creates log row holders', cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/log/LogActivity.java:117; SRC ui/log/LogAdapter.java:48-57')
e('LogAdapter.<clinit>', 'LogAdapter$1.<init>', 'CALL', 'Static field initialiser constructs the diff callback', evidence='SRC ui/log/LogAdapter.java:67; SRC ui/log/LogAdapter.java:67-82')
e('LogActivity.lambda$onCreate$1', 'LogAdapter$1.areContentsTheSame', 'FRAMEWORK', 'DiffUtil dispatch compares submitted list contents', cls='non_standard', via='DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/log/LogActivity.java:119-120; SRC ui/log/LogAdapter.java:70-74')
e('LogActivity.lambda$onCreate$1', 'LogAdapter$1.areItemsTheSame', 'FRAMEWORK', 'DiffUtil dispatch compares submitted list identities', cls='non_standard', via='DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/log/LogActivity.java:119-120; SRC ui/log/LogAdapter.java:77-81')
e('LogAdapter.onCreateViewHolder', 'LogAdapter$ViewHolder.<init>', 'CALL', 'onCreateViewHolder constructs the row holder', evidence='SRC ui/log/LogAdapter.java:56; SRC ui/log/LogAdapter.java:93-98')
e('LogAdapter.onBindViewHolder', 'LogAdapter$ViewHolder.bind', 'CALL', 'onBindViewHolder binds the entry to the holder', evidence='SRC ui/log/LogAdapter.java:64; SRC ui/log/LogAdapter.java:100-110')
e('LogAdapter$ViewHolder.bind', 'LogAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Row click runs the bind click lambda', cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/log/LogAdapter.java:102; SRC ui/log/LogAdapter.java:102-105')
e('LogSourceFactory.create', 'LogDataSource.<init>', 'CALL', 'Factory create constructs the log data source', evidence='SRC ui/log/LogSourceFactory.java:41; SRC ui/log/LogDataSource.java:38-44')
e('LogDataSource.lambda$new$0', 'LogDataSource.invalidate', 'CALL', 'Data-set-change lambda invalidates the source', evidence='SRC ui/log/LogDataSource.java:43; SRC ui/log/LogDataSource.java:47-52')
e('LogDataSource.<init>', 'LogDataSource.lambda$new$0', 'FRAMEWORK', 'Rx subscribe dispatch runs the invalidate lambda on data-set change', cls='non_standard', via='Rx dispatch', evidence='INFERRED Rx dispatch; SRC ui/log/LogDataSource.java:42-43')
e('LogSourceFactory.create', 'LogDataSource.loadInitial', 'FRAMEWORK', 'Paging dispatch loads the initial log page', cls='non_standard', via='Paging dispatch', evidence='INFERRED Paging dispatch; SRC ui/log/LogSourceFactory.java:41; SRC ui/log/LogDataSource.java:55-90')
e('LogSourceFactory.create', 'LogDataSource.loadRange', 'FRAMEWORK', 'Paging dispatch loads further log pages', cls='non_standard', via='Paging dispatch', evidence='INFERRED Paging dispatch; SRC ui/log/LogSourceFactory.java:41; SRC ui/log/LogDataSource.java:93-117')
e('LogViewModel.<init>', 'LogMutableParams.<init>', 'CALL', 'Field initialiser constructs the mutable log params', evidence='SRC ui/log/LogViewModel.java:56; SRC ui/log/LogMutableParams.java:27-35')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogDhtFilter', 'CALL', 'Params callback persists the DHT filter flag', evidence='SRC ui/log/LogViewModel.java:125; SRC ui/log/LogMutableParams.java:60-64')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogPeerFilter', 'CALL', 'Params callback persists the peer filter flag', evidence='SRC ui/log/LogViewModel.java:128; SRC ui/log/LogMutableParams.java:72-76')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogPortmapFilter', 'CALL', 'Params callback persists the portmap filter flag', evidence='SRC ui/log/LogViewModel.java:131; SRC ui/log/LogMutableParams.java:84-88')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogSessionFilter', 'CALL', 'Params callback persists the session filter flag', evidence='SRC ui/log/LogViewModel.java:122; SRC ui/log/LogMutableParams.java:49-52')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogTorrentFilter', 'CALL', 'Params callback persists the torrent filter flag', evidence='SRC ui/log/LogViewModel.java:134; SRC ui/log/LogMutableParams.java:96-100')
e('LogViewModel$1.onPropertyChanged', 'LogMutableParams.isLogging', 'CALL', 'Params callback reads the logging flag', evidence='SRC ui/log/LogViewModel.java:114; SRC ui/log/LogMutableParams.java:37-40')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogDhtFilter', 'CALL', 'initMutableParams restores the DHT filter flag', evidence='SRC ui/log/LogViewModel.java:84; SRC ui/log/LogMutableParams.java:66-70')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogPeerFilter', 'CALL', 'initMutableParams restores the peer filter flag', evidence='SRC ui/log/LogViewModel.java:85; SRC ui/log/LogMutableParams.java:78-82')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogPortmapFilter', 'CALL', 'initMutableParams restores the portmap filter flag', evidence='SRC ui/log/LogViewModel.java:86; SRC ui/log/LogMutableParams.java:90-94')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogSessionFilter', 'CALL', 'initMutableParams restores the session filter flag', evidence='SRC ui/log/LogViewModel.java:83; SRC ui/log/LogMutableParams.java:54-58')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogTorrentFilter', 'CALL', 'initMutableParams restores the torrent filter flag', evidence='SRC ui/log/LogViewModel.java:87; SRC ui/log/LogMutableParams.java:102-106')
e('LogViewModel.initMutableParams', 'LogMutableParams.setLogging', 'CALL', 'initMutableParams restores the logging flag', evidence='SRC ui/log/LogViewModel.java:82; SRC ui/log/LogMutableParams.java:42-46')

UNREACHABLE.update({
    'LogMutableParams.toString': ('no_trigger_in_app',
        'Definition LogMutableParams.java:110-120 printed. No caller printed in any file fetched in this pass (LogActivity, LogAdapter, LogDataSource, LogSourceFactory, LogMutableParams, LogViewModel, GoToFolderDialog, GoToFolderViewModel, FileManagerDialog, MainActivity - grep of those files finds only LogEntry.toString() at LogViewModel.java:222 and unrelated String toString() calls, never LogMutableParams.toString). auto_calls.json: exact dst LogMutableParams.toString 0 edges.',
        'SRC ui/log/LogMutableParams.java:110-120',
        'INFERRED'),
})

# No part edge points at a method that is UNREACHABLE in this batch, and
# auto_calls.json + javap show no bytecode caller of this batch's
# UNREACHABLE methods, so no SUPPRESS entries apply.
SUPPRESS.update(set())
