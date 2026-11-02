# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch57 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 57 part (DateUtils tail, TorrentContentFileTreeUtils, Utils head).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b057_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# DateUtils tail and TorrentContentFileTreeUtils through the detail ViewModel.
e('TorrentFilterCollection.dateAddedYesterday', 'DateUtils.startOfYesterday', 'CALL', 'Yesterday filter reads the yesterday start through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:57-63; SRC DateUtils.java:135-138')
e('DetailTorrentViewModel.makeFileTree', 'TorrentContentFileTreeUtils.buildFileTree', 'CALL', 'Detail file-tree build runs the content tree builder', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:529-551; SRC TorrentContentFileTreeUtils.java:46')
e('TorrentContentFileTreeUtils.buildFileTree', 'TorrentContentFileTreeUtils.makeObject', 'CALL', 'Content tree build creates a node object for each new path node', cls='explicit', evidence='SRC TorrentContentFileTreeUtils.java:101; SRC TorrentContentFileTreeUtils.java:119-126')

# Utils: class initialisation and the launcher/service/session routes.
e('MainActivity.onCreate', 'Utils.<clinit>', 'CALL', 'First Utils use in the launcher activity initialises the Utils class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/main/MainActivity.java:136-137; SRC Utils.java:105-128')
e('Utils.fetchHttpUrl', 'Utils.checkConnectivity', 'CALL', 'HTTP fetch checks connectivity before opening the connection', cls='explicit', evidence='SRC Utils.java:462-475; SRC Utils.java:157-162')
e('TorrentListAdapter$ViewHolder.<init>', 'Utils.colorizeProgressBar', 'CALL', 'Torrent list rows colour their progress bars through Utils', cls='explicit', evidence='SRC ui/main/TorrentListAdapter.java:161-166; SRC Utils.java:129-136')
e('PiecesView.create', 'Utils.dpToPx', 'CALL', 'Pieces view creation converts dp to px through Utils', cls='explicit', evidence='SRC ui/detailtorrent/pages/pieces/PiecesView.java:71-74; SRC Utils.java:327-331')
e('BehaviorSettingsFragment.onPreferenceChange', 'Utils.enableBootReceiver', 'CALL', 'Behaviour autostart preference toggles the boot receiver through Utils', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:199-202; SRC Utils.java:436-447')
e('SchedulingSettingsFragment.onPreferenceChange', 'Utils.enableBootReceiver', 'CALL', 'Scheduling autostart preference toggles the boot receiver through Utils', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:191-206; SRC Utils.java:436-447')
e('TorrentService.init', 'Utils.enableBootReceiverIfNeeded', 'CALL', 'Service initialisation enables the boot receiver when needed', cls='explicit', evidence='SRC service/TorrentService.java:116-128; SRC Utils.java:449-460')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'Utils.fetchHttpUrl', 'CALL', 'Torrent decode task fetches http torrent bytes through Utils', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:217-254; SRC Utils.java:462-475')
e('FeedDownloaderWorker.fetchTorrent', 'Utils.fetchHttpUrl', 'CALL', 'Feed download worker fetches feed torrent bytes through Utils', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:109-140; SRC Utils.java:462-475')
e('MainActivity.onCreate', 'Utils.getAppTheme', 'CALL', 'Launcher activity reads the app theme through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:136-137; SRC Utils.java:374-385')
e('TorrentSessionImpl.start', 'Utils.getAppVersionNumber', 'CALL', 'Session start reads the app version number through Utils', cls='explicit', evidence='SRC TorrentSessionImpl.java:895; SRC Utils.java:532-541')
e('FileManagerAdapter$ViewHolder.bind', 'Utils.getAttributeColor', 'CALL', 'File-manager rows read attribute colours through Utils', cls='explicit', evidence='SRC ui/filemanager/FileManagerAdapter.java:126-139; SRC Utils.java:618-635')
e('DetailTorrentFragment.subscribeMsgViewModel', 'Utils.getAttributeColor', 'CALL', 'Detail fragment reads attribute colours through Utils', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:278-283; SRC Utils.java:618-635')
e('Utils.isBatteryLow', 'Utils.getBatteryLevel', 'CALL', 'Battery-low check reads the battery level through Utils', cls='explicit', evidence='SRC Utils.java:362-364; SRC Utils.java:338-350')
e('Utils.isBatteryBelowThreshold', 'Utils.getBatteryLevel', 'CALL', 'Battery-threshold check reads the battery level through Utils', cls='explicit', evidence='SRC Utils.java:366-368; SRC Utils.java:338-350')
e('AddLinkDialog.switchClipboardButton', 'Utils.getClipData', 'CALL', 'Add-link dialog reads the clipboard data through Utils', cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:163-167; SRC Utils.java:290-301')
e('Utils.getClipboardText', 'Utils.getClipData', 'CALL', 'Clipboard text read reads the clipboard data through Utils', cls='explicit', evidence='SRC Utils.java:302-317; SRC Utils.java:290-301')
e('AddFeedViewModel.initAddModeFromClipboard', 'Utils.getClipboardText', 'CALL', 'Add-feed clipboard mode reads clipboard text through Utils', cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:87-89; SRC Utils.java:302-317')
e('AddLinkViewModel.initLinkFromClipboard', 'Utils.getClipboardText', 'CALL', 'Add-link clipboard mode reads clipboard text through Utils', cls='explicit', evidence='SRC ui/addlink/AddLinkViewModel.java:45-47; SRC Utils.java:302-317')
e('ClipboardDialog.onCreateDialog', 'Utils.getClipboardText', 'CALL', 'Clipboard dialog reads clipboard text through Utils', cls='explicit', evidence='SRC ui/ClipboardDialog.java:94-105; SRC Utils.java:302-317')
e('Utils.isBatteryLow', 'Utils.getDefaultBatteryLowLevel', 'CALL', 'Battery-low check reads the default low level through Utils', cls='explicit', evidence='SRC Utils.java:362-364; SRC Utils.java:333-336')
e('MainActivity.onDrawerGroupsCreated', 'Utils.getDrawerGroupDateAddedFilter', 'CALL', 'Drawer group creation reads the date-added filter through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:582-596; SRC Utils.java:854-871')
e('MainActivity.onDrawerItemSelected', 'Utils.getDrawerGroupDateAddedFilter', 'CALL', 'Drawer item selection reads the date-added filter through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-623; SRC Utils.java:854-871')
e('MainActivity.onDrawerGroupsCreated', 'Utils.getDrawerGroupItemSorting', 'CALL', 'Drawer group creation reads the group sorting through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:582-596; SRC Utils.java:804-835')
e('MainActivity.onDrawerItemSelected', 'Utils.getDrawerGroupItemSorting', 'CALL', 'Drawer item selection reads the group sorting through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-623; SRC Utils.java:804-835')
e('MainActivity.onDrawerGroupsCreated', 'Utils.getDrawerGroupStatusFilter', 'CALL', 'Drawer group creation reads the status filter through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:582-596; SRC Utils.java:837-852')
e('MainActivity.onDrawerItemSelected', 'Utils.getDrawerGroupStatusFilter', 'CALL', 'Drawer item selection reads the status filter through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-623; SRC Utils.java:837-852')
e('TorrentMetaInfo.getMetaInfo', 'Utils.getFileList', 'CALL', 'Meta-info read lists the torrent files through Utils', cls='explicit', evidence='SRC TorrentMetaInfo.java:98-108; SRC Utils.java:142-151')
e('TorrentService.setFilterAndSorting', 'Utils.getForegroundNotifyFilter', 'CALL', 'Service filter setup reads the foreground notify filter through Utils', cls='explicit', evidence='SRC service/TorrentService.java:136-138; SRC Utils.java:873-891')
e('TorrentService.setFilterAndSorting', 'Utils.getForegroundNotifySorting', 'CALL', 'Service filter setup reads the foreground notify sorting through Utils', cls='explicit', evidence='SRC service/TorrentService.java:136-139; SRC Utils.java:892-926')
e('DetailTorrentFragment.addTrackers', 'Utils.getLineSeparator', 'CALL', 'Detail tracker editing reads the line separator through Utils', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:689-704; SRC Utils.java:285-287')
e('DetailTorrentTrackersFragment.shareUrl', 'Utils.getLineSeparator', 'CALL', 'Tracker sharing reads the line separator through Utils', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:374-391; SRC Utils.java:285-287')
e('MainActivity.initDrawer', 'Utils.getNavigationDrawerItems', 'CALL', 'Drawer setup reads the navigation drawer items through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:230-250; SRC Utils.java:720-802')
e('AddTagViewModel.setRandomColor', 'Utils.getRandomColor', 'CALL', 'Tag colour setup reads a random colour through Utils', cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:51-52; SRC Utils.java:661-663')
e('HttpConnection.<init>', 'Utils.getSSLContext', 'CALL', 'HTTP connection construction builds its SSL context through Utils', cls='explicit', evidence='SRC HttpConnection.java:66-69; SRC Utils.java:585-612')
e('LogSettingsActivity.onCreate', 'Utils.getSettingsTheme', 'CALL', 'Log settings activity reads the settings theme through Utils', cls='explicit', evidence='SRC ui/log/LogSettingsActivity.java:37-39; SRC Utils.java:400-411')
e('SettingsActivity.onCreate', 'Utils.getSettingsTheme', 'CALL', 'Settings activity reads the settings theme through Utils', cls='explicit', evidence='SRC ui/settings/SettingsActivity.java:42-44; SRC Utils.java:400-411')
e('Utils.getAppTheme', 'Utils.getThemePreference', 'CALL', 'App theme lookup reads the theme preference through Utils', cls='explicit', evidence='SRC Utils.java:374-385; SRC Utils.java:370-372')
e('FeedDownloaderWorker.fetchTorrent', 'Utils.getTorrentDownloadPath', 'CALL', 'Feed download worker reads the torrent download path through Utils', cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:109-114; SRC Utils.java:638-647')
e('AddFeedActivity.onCreate', 'Utils.getTranslucentAppTheme', 'CALL', 'Add-feed activity reads the translucent theme through Utils', cls='explicit', evidence='SRC ui/addfeed/AddFeedActivity.java:47-49; SRC Utils.java:387-398')
e('AddLinkActivity.onCreate', 'Utils.getTranslucentAppTheme', 'CALL', 'Add-link activity reads the translucent theme through Utils', cls='explicit', evidence='SRC ui/addlink/AddLinkActivity.java:23-25; SRC Utils.java:387-398')
e('SelectTagActivity.onCreate', 'Utils.getTranslucentAppTheme', 'CALL', 'Select-tag activity reads the translucent theme through Utils', cls='explicit', evidence='SRC ui/tag/SelectTagActivity.java:42-43; SRC Utils.java:387-398')
e('AddTagActivity.onCreate', 'Utils.getTranslucentAppTheme', 'CALL', 'Add-tag activity reads the translucent theme through Utils', cls='explicit', evidence='SRC ui/addtag/AddTagActivity.java:47-48; SRC Utils.java:387-398')
e('CreateTorrentActivity.onCreate', 'Utils.getTranslucentAppTheme', 'CALL', 'Create-torrent activity reads the translucent theme through Utils', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:55-64; SRC Utils.java:387-398')
e('TorrentSessionImpl.start', 'Utils.getVersionComponents', 'CALL', 'Session start reads the version components through Utils', cls='explicit', evidence='SRC TorrentSessionImpl.java:889; SRC Utils.java:544-565')
e('PermissionManager.<init>', 'Utils.hasManageExternalStoragePermission', 'CALL', 'Permission manager construction checks the manage-storage permission through Utils', cls='explicit', evidence='SRC ui/PermissionManager.java:50-58; SRC Utils.java:677-697')
e('TorrentEngine.checkPauseTorrents', 'Utils.isBatteryBelowThreshold', 'CALL', 'Engine pause check reads the battery threshold through Utils', cls='explicit', evidence='SRC TorrentEngine.java:1023-1041; SRC Utils.java:366-368')
e('TorrentEngine.checkPauseTorrents', 'Utils.isBatteryCharging', 'CALL', 'Engine pause check reads the charging state through Utils', cls='explicit', evidence='SRC TorrentEngine.java:1023-1041; SRC Utils.java:352-360')
e('TorrentEngine.checkPauseTorrents', 'Utils.isBatteryLow', 'CALL', 'Engine pause check reads the battery-low state through Utils', cls='explicit', evidence='SRC TorrentEngine.java:1023-1041; SRC Utils.java:362-364')
e('TorrentEngine.startWatchDir', 'Utils.isFileSystemPath', 'CALL', 'Engine watch-dir start tests the path scheme through Utils', cls='explicit', evidence='SRC TorrentEngine.java:1116-1119; SRC Utils.java:649-655')
e('AddLinkViewModel.initLinkFromClipboard', 'Utils.isHash', 'CALL', 'Add-link clipboard mode tests the clipboard text as a hash through Utils', cls='explicit', evidence='SRC ui/addlink/AddLinkViewModel.java:45-55; SRC Utils.java:271-279')
e('AddLinkViewModel.normalizeUrl', 'Utils.isHash', 'CALL', 'Add-link URL normalisation tests the link as a hash through Utils', cls='explicit', evidence='SRC ui/addlink/AddLinkViewModel.java:60-63; SRC Utils.java:271-279')
e('FeedParser.watchTorrentInfoHash', 'Utils.isHash', 'CALL', 'Feed parsing tests the torrent info hash through Utils', cls='explicit', evidence='SRC FeedParser.java:236-243; SRC Utils.java:271-279')
e('MainActivity.cleanGarbageFragments', 'Utils.isLargeScreenDevice', 'CALL', 'Main activity fragment cleanup tests the screen size through Utils', cls='explicit', evidence='SRC ui/main/MainActivity.java:640-642; SRC Utils.java:251-254')

UNREACHABLE.update({
    'Utils.buildExactAlarmPermissionRequest': ('closed_by_api_level',
        'API 27; S = 31. Exactly two call sites, both gated off at API 27: TorrentNotifier.makeExactAlarmPermissionNotify :251, inside a method that early-returns when SDK_INT < S (:245-246, true at API 27); and Utils.requestExactAlarmPermission :673, guarded SDK_INT >= S (:672, false at API 27). Definition Utils :666-670, @RequiresApi(S) :665.',
        'SRC Utils.java:665-675; SRC ui/TorrentNotifier.java:244-251',
        'INFERRED'),
})

# No SUPPRESS entries from this batch's own callers: recomputed 2026-11-01
# from auto_calls.json plus a bytecode invoke scan of this batch's classes
# — no REACHABLE method in this batch calls an UNREACHABLE method in
# bytecode. The one REACHABLE caller pair for this batch's UNREACHABLE
# row lives in other batches (TorrentNotifier batch 74, Utils
# requestExactAlarmPermission batch 58) and is reported in REPORT.md as a
# cross-group candidate for reconciliation.
SUPPRESS.update(set())
