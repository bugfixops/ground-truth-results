# Kiro k02 (2026-11-03, handover Step 7): name the bytecode caller in every check-8 reason (rule B4).
# Each sentence is put in front of the existing reason, which is kept unchanged; the caller line is
# appended to the source refs. Printed caller lines: graphs/LibreTorrent/scratch/kiro/prints/step7_callers.txt.
# Explanation table: graphs/LibreTorrent/scratch/check8_explained.md.

_LEGACY_NOTIFY = ('Caller: TorrentNotifier.applyLegacyNotifySettings (TorrentNotifier.java:%d), which returns early at '
                  ':276 when SDK >= O, so on API 27 this call never runs.')
_LEGACY_PREF = ('Caller: AppearanceSettingsFragment.onPreferenceChange (AppearanceSettingsFragment.java:%d), in the branch '
                'for a legacy preference whose change listener is bound only inside initLegacyNotifySettings, which runs '
                'only when SDK < O (:118-119), so on API 27 this branch never runs.')
_KEYS = ('Callers: FeedChannelListAdapter$KeyProvider.%s (FeedChannelListAdapter.java:%d), TorrentListAdapter$KeyProvider.%s '
         '(TorrentListAdapter.java:%d) and TrackerListAdapter$KeyProvider.%s (TrackerListAdapter.java:%d) call '
         'selectable.%s; each KeyProvider is built only with its own adapter (FeedFragment.java:140, MainFragment.java:160, '
         'DetailTorrentTrackersFragment.java:181), never with this adapter, so the interface call never reaches this method.')

_K7_CALLERS = {
    'AppearanceSettingsFragment.initLegacyNotifySettings': (
        'Caller: AppearanceSettingsFragment.onCreate (AppearanceSettingsFragment.java:119), under if (SDK_INT < O) at :118, '
        'false on API 27.', 'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119'),
    'AtomItem.getDescription': (
        'Caller: BaseItem.getUniqueId (BaseItem.java:41), which runs only from BaseItem.equals/hashCode (UNREACHABLE).',
        'SRC com/ernieyu/feedparser/impl/BaseItem.java:36-58'),
    'FeedItemsAdapter.getItemKey': (_KEYS % ('getKey', 289, 'getKey', 344, 'getKey', 241, 'getItemKey'),
        'SRC ui/feeds/FeedChannelListAdapter.java:289; ui/main/TorrentListAdapter.java:344; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:241'),
    'FeedItemsAdapter.getItemPosition': (_KEYS % ('getPosition', 295, 'getPosition', 350, 'getPosition', 247, 'getItemPosition'),
        'SRC ui/feeds/FeedChannelListAdapter.java:295; ui/main/TorrentListAdapter.java:350; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:247'),
    'PeerListAdapter.getItemKey': (_KEYS % ('getKey', 289, 'getKey', 344, 'getKey', 241, 'getItemKey'),
        'SRC ui/feeds/FeedChannelListAdapter.java:289; ui/main/TorrentListAdapter.java:344; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:241'),
    'PeerListAdapter.getItemPosition': (_KEYS % ('getPosition', 295, 'getPosition', 350, 'getPosition', 247, 'getItemPosition'),
        'SRC ui/feeds/FeedChannelListAdapter.java:295; ui/main/TorrentListAdapter.java:350; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:247'),
    'NanoHTTPD$Cookie.getHTTPHeader': (
        'Caller: NanoHTTPD$CookieHandler.unloadQueue (NanoHTTPD.java:296), inside the loop over the cookie queue (:295), '
        'which stays empty in the app path.', 'SRC org/nanohttpd/NanoHTTPD.java:294-297'),
    'NanoHTTPD$DefaultTempFile.delete': (
        'Caller: NanoHTTPD$DefaultTempFileManager.clear (NanoHTTPD.java:394), inside the loop over tempFiles (:392), '
        'which stays empty in the app path.', 'SRC org/nanohttpd/NanoHTTPD.java:391-396'),
    'NanoHTTPD$SecureServerSocketFactory.create': (
        'Caller: NanoHTTPD.start (NanoHTTPD.java:1814), a virtual getServerSocketFactory().create() call that reaches the '
        'default factory, not this one.', 'SRC org/nanohttpd/NanoHTTPD.java:1813-1814'),
    'NanoHTTPD.serve(IHTTPSession)': (
        'Caller: NanoHTTPD$HTTPSession.execute (NanoHTTPD.java:720), a virtual serve(this) call that resolves to '
        'TorrentStreamServer.serve.', 'SRC org/nanohttpd/NanoHTTPD.java:720'),
    'NormalizeUrl.join': (
        'Caller: NormalizeUrl.doNormalize (NormalizeUrl.java:268), under if (options.removeDirectoryIndex.length > 0) at :263.',
        'SRC core/urlnormalizer/NormalizeUrl.java:263-268'),
    'NormalizeUrl.makeUserInfo': (
        'Caller: NormalizeUrl.urlToString (NormalizeUrl.java:397), under if (user != null && !user.isEmpty()) at :396.',
        'SRC core/urlnormalizer/NormalizeUrl.java:396-397'),
    'PercentEncoder.<clinit>': (
        'Caller: NormalizeUrl.doNormalize (NormalizeUrl.java:217), under if (options.decode) at :216.',
        'SRC core/urlnormalizer/NormalizeUrl.java:216-217'),
    'PercentEncoder.decode': (
        'Caller: NormalizeUrl.doNormalize (NormalizeUrl.java:217), under if (options.decode) at :216.',
        'SRC core/urlnormalizer/NormalizeUrl.java:216-217'),
    'SettingsRepositoryImpl.askManageAllFilesPermission()': (
        'Caller: PermissionManager.requestPermissions (PermissionManager.java:100), inside if (SDK_INT >= R && ...) at :99, '
        'false on API 27.', 'SRC ui/PermissionManager.java:99-100'),
    'SettingsRepositoryImpl.askManageAllFilesPermission(boolean)': (
        'Caller: PermissionManager.setDoNotAskStorage (PermissionManager.java:118), inside if (SDK_INT >= R) at :117, '
        'false on API 27.', 'SRC ui/PermissionManager.java:116-119'),
    'SettingsRepositoryImpl.askNotificationPermission(boolean)': (
        'Caller: PermissionManager.setDoNotAskNotifications (PermissionManager.java:124), inside if (SDK_INT >= TIRAMISU) '
        'at :123, false on API 27.', 'SRC ui/PermissionManager.java:122-125'),
    'SettingsRepositoryImpl.ledIndicatorColorNotify()': (_LEGACY_NOTIFY % 290, 'SRC ui/TorrentNotifier.java:275-292'),
    'SettingsRepositoryImpl.ledIndicatorNotify()': (_LEGACY_NOTIFY % 289, 'SRC ui/TorrentNotifier.java:275-292'),
    'SettingsRepositoryImpl.notifySound()': (_LEGACY_NOTIFY % 282, 'SRC ui/TorrentNotifier.java:275-292'),
    'SettingsRepositoryImpl.playSoundNotify()': (_LEGACY_NOTIFY % 281, 'SRC ui/TorrentNotifier.java:275-292'),
    'SettingsRepositoryImpl.vibrationNotify()': (_LEGACY_NOTIFY % 286, 'SRC ui/TorrentNotifier.java:275-292'),
    'SettingsRepositoryImpl.ledIndicatorColorNotify(int)': (_LEGACY_PREF % 250, 'SRC ui/settings/sections/AppearanceSettingsFragment.java:249-250'),
    'SettingsRepositoryImpl.ledIndicatorNotify(boolean)': (_LEGACY_PREF % 244, 'SRC ui/settings/sections/AppearanceSettingsFragment.java:243-244'),
    'SettingsRepositoryImpl.playSoundNotify(boolean)': (_LEGACY_PREF % 241, 'SRC ui/settings/sections/AppearanceSettingsFragment.java:240-241'),
    'SettingsRepositoryImpl.vibrationNotify(boolean)': (_LEGACY_PREF % 247, 'SRC ui/settings/sections/AppearanceSettingsFragment.java:246-247'),
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog()': (
        'Caller: Utils.showManageAllFilesWarningDialog (Utils.java:706), the third disjunct after SDK_INT < R at :704, '
        'which is true on API 27, so :706 is never evaluated.', 'SRC Utils.java:704-707'),
    'SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean)': (
        'Caller: Utils.showManageAllFilesWarningDialog (Utils.java:711), after the early return at :704-707, which is '
        'always taken on API 27 (SDK_INT < R).', 'SRC Utils.java:704-711'),
}

for _k7_m, (_k7_sentence, _k7_ref) in _K7_CALLERS.items():
    _k7_kind, _k7_reason, _k7_refs, _k7_conf = UNREACHABLE[_k7_m]
    UNREACHABLE[_k7_m] = (_k7_kind, _k7_sentence + ' ' + _k7_reason, _k7_refs + '; ' + _k7_ref, _k7_conf)
