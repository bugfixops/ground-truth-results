# Citation-form rework 2026-11-01: evidence paths with a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS, line ranges unchanged (full paths remain in untouched .md/printed files).
# Converter C09 delivery (2026-11-01): base = audited A3 output helper a3-g12 parts b058.
# Labels, kinds, grades, edges and SUPPRESS are unchanged from the audited base
# (verified by the official harness against the authoritative merge-ready batch file).
# Stronger-evidence rule (step b): all UNREACHABLE keys of this batch were checked
# against the merger tree graph_def.py (read-only); the tree holds none of them, so
# no grade changes; all grades remain as audited.
# Merger notes recorded in the converter report (not applied here): the G12 F4
# SUPPRESS pairs for rows 58/11 and 58/15 are merger-added SUPPRESS entries at
# merge, not part content.
# Printed evidence: the delivered printed file carries the base printed content plus
# a converter header; the G12 -c key-dispatch excerpts are NOT relied on (auditor
# finding: they repeat ctor-body lines and do not demonstrate dispatch); the -p
# signature blocks and printed source lines are the relied evidence.
# Batch 58 part (Utils, ActivityAddTorrentBinding, ActivityAddTorrentBindingImpl, ActivityFilemanagerDialogBinding, ActivityFilemanagerDialogBindingImpl). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b058_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated databinding Impl evidence is javap -c -p output: generated Impl source is
# absent from final_java_only, so the printed file carries the javap dump under a
# .java-named header for that class (labelled as javap, not source).
# Pre-existing routes NOT repeated here (listed in parts/b058.md Dependencies):
# TorrentEngine.start -> Utils.startServiceBackground (graph_def:180),
# Utils.startServiceBackground -> Utils.lambda$startServiceBackground$0 (graph_def:182),
# MainActivity.onCreate -> Utils.showManageAllFilesWarningDialog (graph_def:238).

e('TorrentEngine.checkPauseTorrents', 'Utils.isMetered', 'CALL', 'Pause check reads whether the connection is metered',
  evidence='SRC TorrentEngine.java:1033-1035; SRC Utils.java:196-202')
e('Utils.checkConnectivity', 'Utils.isNetworkTypeAllowed', 'CALL', 'Connectivity check requires an allowed network type',
  evidence='SRC Utils.java:157-161; SRC Utils.java:164-195')
e('TorrentEngine.checkPauseTorrents', 'Utils.isRoaming', 'CALL', 'Pause check reads whether the connection is roaming',
  evidence='SRC TorrentEngine.java:1033-1035; SRC Utils.java:204-213')
e('FsModuleResolverImpl.resolveFsByUri', 'Utils.isSafPath', 'CALL', 'Filesystem resolution checks for a SAF path',
  evidence='SRC FsModuleResolverImpl.java:43; SRC Utils.java:657-658')
e('AddTorrentActivity.initLayout', 'Utils.isTwoPane', 'CALL', 'Add-torrent layout selection checks two-pane mode',
  evidence='SRC ui/addtorrent/AddTorrentActivity.java:284; SRC Utils.java:241-242')
e('CreateTorrentViewModel.normalizeAndValidateUrl', 'Utils.isValidTrackerUrl', 'CALL', 'Tracker URL validation checks the URL pattern',
  evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:317; SRC Utils.java:261-268')
# Row 7 Utils.lambda.startServiceBackground.0: pre-existing graph_def route, see Dependencies in b058.md.
e('TorrentStream.<init>(String,int,int,int,int,long,long,int)', 'Utils.makeSha1Hash', 'CALL', 'Stream id is the SHA-1 of torrent id plus file index',
  evidence='SRC TorrentStream.java:38-45; SRC Utils.java:567-583')
e('AddLinkViewModel.normalizeUrl', 'Utils.normalizeMagnetHash', 'CALL', 'Link normalization prefixes the magnet info-hash',
  evidence='SRC ui/addlink/AddLinkViewModel.java:64; SRC Utils.java:233-234')
e('AddTorrentActivity.handleAlertDialogEvent', 'Utils.reportError', 'CALL', 'Alert-dialog error path reports the error',
  evidence='SRC ui/addtorrent/AddTorrentActivity.java:251; SRC Utils.java:319-325')
e('SchedulingSettingsFragment.lambda$subscribeAlertDialog$0', 'Utils.requestExactAlarmPermission', 'CALL', 'Dialog-positive callback requests exact-alarm permission',
  evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:137; SRC Utils.java:671-675')
e('SwitchBar.init', 'Utils.setBackground', 'CALL', 'SwitchBar init sets its background drawable',
  evidence='SRC ui/customviews/SwitchBar.java:62; SRC Utils.java:152-155')
e('PermissionManager.lambda$new$1', 'Utils.shouldRequestStoragePermission', 'CALL', 'Permission result handling checks whether to show the rationale',
  evidence='SRC ui/PermissionManager.java:83; SRC Utils.java:413-417')
e('MainFragment$3.onCreateActionMode', 'Utils.showActionModeStatusBar', 'CALL', 'Action-mode creation recolours the status bar',
  evidence='SRC ui/main/MainFragment.java:469; SRC Utils.java:613-616')
# Row 15 Utils.showManageAllFilesWarningDialog: pre-existing graph_def route, see Dependencies in b058.md.
# Row 16 Utils.startServiceBackground: pre-existing graph_def route, see Dependencies in b058.md.
e('Utils.fetchHttpUrl', 'Utils$1.<init>', 'CALL', 'fetchHttpUrl creates the HttpConnection listener',
  evidence='SRC Utils.java:477; SRC HttpConnection.java:55-63')
e('HttpConnection.run', 'Utils$1.onConnectionCreated', 'CALL', 'HttpConnection run loop notifies its listener (onConnectionCreated)',
  evidence='SRC HttpConnection.java:93; SRC Utils.java:477-530')
e('HttpConnection.run', 'Utils$1.onIOException', 'CALL', 'HttpConnection run loop notifies its listener (onIOException)',
  evidence='SRC HttpConnection.java:113; SRC Utils.java:477-530')
e('HttpConnection.run', 'Utils$1.onMovedPermanently', 'CALL', 'HttpConnection run loop notifies its listener (onMovedPermanently)',
  evidence='SRC HttpConnection.java:103; SRC Utils.java:477-530')
e('HttpConnection.run', 'Utils$1.onResponseHandle', 'CALL', 'HttpConnection run loop notifies its listener (onResponseHandle)',
  evidence='SRC HttpConnection.java:107; SRC Utils.java:477-530')
e('HttpConnection.run', 'Utils$1.onTooManyRedirects', 'CALL', 'HttpConnection run loop notifies its listener (onTooManyRedirects)',
  evidence='SRC HttpConnection.java:123; SRC Utils.java:477-530')
e('Utils.getSSLContext', 'Utils$2.<init>', 'CALL', 'getSSLContext creates the wrapping trust manager',
  evidence='SRC Utils.java:585-593')
e('Utils.getSSLContext', 'Utils$2.checkClientTrusted', 'FRAMEWORK', 'TLS stack dispatch: the trust manager checkClientTrusted runs when the getSSLContext result is used for a connection', cls='non_standard', via='TLS stack trust-manager dispatch (SSLContext socket factory -> X509TrustManager callback)',
  evidence='INFERRED TLS dispatch; SRC Utils.java:585-611; SRC HttpConnection.java:87-91')
e('Utils.getSSLContext', 'Utils$2.checkServerTrusted', 'FRAMEWORK', 'TLS stack dispatch: the trust manager checkServerTrusted runs when the getSSLContext result is used for a connection', cls='non_standard', via='TLS stack trust-manager dispatch (SSLContext socket factory -> X509TrustManager callback)',
  evidence='INFERRED TLS dispatch; SRC Utils.java:585-611; SRC HttpConnection.java:87-91')
e('Utils.getSSLContext', 'Utils$2.getAcceptedIssuers', 'FRAMEWORK', 'TLS stack dispatch: the trust manager getAcceptedIssuers runs when the getSSLContext result is used for a connection', cls='non_standard', via='TLS stack trust-manager dispatch (SSLContext socket factory -> X509TrustManager callback)',
  evidence='INFERRED TLS dispatch; SRC Utils.java:585-611; SRC HttpConnection.java:87-91')
e('ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ActivityAddTorrentBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/ActivityAddTorrentBindingImpl.java:javap 3-arg <init> -> ActivityAddTorrentBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'ActivityAddTorrentBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> ActivityAddTorrentBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> ActivityAddTorrentBindingImpl 2-arg <init>')
e('ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View)', 'ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/ActivityAddTorrentBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('ActivityAddTorrentBindingImpl.invalidateAll', 'ActivityAddTorrentBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/ActivityAddTorrentBindingImpl.java:javap invalidateAll -> requestRebind')
e('ActivityAddTorrentBindingImpl.invalidateAll', 'ActivityAddTorrentBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/ActivityAddTorrentBindingImpl.java:javap invalidateAll -> requestRebind')
e('ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ActivityAddTorrentBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/ActivityAddTorrentBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ActivityFilemanagerDialogBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/ActivityFilemanagerDialogBindingImpl.java:javap 3-arg <init> -> ActivityFilemanagerDialogBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'ActivityFilemanagerDialogBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> ActivityFilemanagerDialogBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> ActivityFilemanagerDialogBindingImpl 2-arg <init>')
e('ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View)', 'ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/ActivityFilemanagerDialogBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')

# UNREACHABLE rows: no bytecode caller in auto_calls.json and no printed app trigger
# (recomputed for this batch; see REPORT.md). Labels, kinds and grades are copied
# unchanged from the authoritative merge-ready batch file.
UNREACHABLE.update({
    'ActivityAddTorrentBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No <data> variable in activity_add_torrent.xml and no observable exists for this callback to dispatch on; no printed setVariable or observable trigger.',
        'SRC databinding/ActivityAddTorrentBindingImpl.java:javap onFieldChange (no registration); INFERRED layout analysis in batch file',
        'INFERRED'),
    'ActivityAddTorrentBindingImpl.setVariable': ('no_trigger_in_app',
        'No <data> variable in activity_add_torrent.xml and no printed setVariable call anywhere (252-file grep, 0 hits).',
        'INFERRED zero setVariable grep over the complete app Java tree (batch file)',
        'INFERRED'),
    'ActivityFilemanagerDialogBinding.getViewModel': ('no_trigger_in_app',
        'FileManagerDialog uses binding.setViewModel and binding.getRoot only, never getViewModel; generated executeBindings reads the mViewModel field directly.',
        'SRC ui/filemanager/FileManagerDialog.java:120,143',
        'INFERRED'),
})

# SUPPRESS: no intra-group REACHABLE -> UNREACHABLE bytecode edge exists for this
# batch (recomputed from auto_calls.json + bytecode scan; cross-group candidates are
# listed in REPORT.md for merger reconciliation, not suppressed here).
# MERGER-ADDED at b058 merge (register G12 F4 + G11 C1; audited part otherwise
# unchanged): suppress the two API-gated bytecode callees whose auto edges would
# otherwise warn as UNREACHABLE-with-incoming-edges:
# - 'Utils.buildExactAlarmPermissionRequest' (batch 57 row 5, closed_by_api_level):
#   sole bytecode callers are Utils.requestExactAlarmPermission at Utils.java:673
#   (guarded SDK_INT >= S, false at API 27) and b074 callers (G11 C1).
# - 'ManageAllFilesWarningDialog.newInstance' (batch 73 row 40, closed_by_api_level):
#   sole caller Utils.showManageAllFilesWarningDialog at Utils.java:713, behind the
#   early return at Utils.java:704-707 (SDK_INT < R true at API 27).
# The SettingsRepositoryImpl.showManageAllFilesWarningDialog overloads (batch 46
# rows 21-22) are already suppressed by merged part b046 and are NOT repeated here.
SUPPRESS.update({
    'Utils.buildExactAlarmPermissionRequest',
    'ManageAllFilesWarningDialog.newInstance',
})
