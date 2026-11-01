# LibreTorrent batch 42 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 42 only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for batch 42 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
  `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
  All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order, method names and
  JVM descriptors matched row for row against the plan in this pass.
- Prior work used as INPUT only: `~/workspace/libretorrent-batch42-proposal.md`
  (26 REACHABLE proposed / 0 UNREACHABLE / 14 OPEN). In this pass 10 of those 14 OPEN rows
  were closed to REACHABLE on freshly printed source (see "Changes in this pass" below);
  the other 4 OPEN rows were re-examined and stay OPEN for the reasons given. No verdict
  below is copied as a result without a printed citation.
- Printed source in this pass, fresh connector fetches from branch `work-2026-10-31`,
  one file at a time with 20 s pauses, no fresh HTTP 429 hit, saved in
  `~/workspace/b4143-src/`: BehaviorSettingsFragment.java (286 lines),
  FeedSettingsFragment.java (164), LimitationsSettingsFragment.java (258),
  NetworkSettingsFragment.java (415), SchedulingSettingsFragment.java (243),
  StorageSettingsFragment.java (297), StreamingSettingsFragment.java (119),
  PermissionManager.java (156), DetailTorrentViewModel.java (611),
  AnonymousModeSettingsFragment.java (84).
- Carried-forward printed source (prior proposal session, printed in full then, NOT
  freshly re-printed in this pass — merger should re-verify line numbers against a fresh
  fetch if it requires it): TorrentStreamServer.java (284 lines),
  SessionSettings.java (10,192 bytes, core/settings/SessionSettings.java),
  SettingsRepositoryImpl.java (49,048 bytes, core/settings/SettingsRepositoryImpl.java),
  RepositoryHelper.java (full), TorrentEngine.java (sections, incl. startStreamingServer
  :1063-1083, setProxy :1095-1115, preference-change branches :1560-1585, getStream :747-755),
  Utils.java autostart sites (:440,:453, from batch 20/21 local copy).
- `confirmed_by` convention in this file: SOURCE = a direct app-to-app call site naming
  the method is printed in app source (including a printed listener body that calls it);
  INFERRED = the method is reached only through unprinted framework/library dispatch
  (lifecycle, NanoHTTPD dispatch, JVM class/enum initialisation) where the registration or
  first use is printed. This is the per-row convention, not the whole-route convention used
  in some earlier batches; labels are unaffected, only `confirmed_by` would change at merge
  if the merger adopts the whole-route convention. SettingsRepositoryImpl methods are called
  through the SettingsRepository interface (`pref.*`); the implementation is the singleton
  built by RepositoryHelper.getSettingsRepository (carried-forward: RepositoryHelper.java,
  called from TorrentEngine ctor TorrentEngine.java:133) — that interface dispatch is the
  reason a fragment `pref.setter(...)` line is SOURCE for the Impl method.
- No connector `search_code` result was used as evidence of absence anywhere in this file.

## Changes in this pass (vs the prior proposal) — all on freshly printed source

- Row 5, TorrentStreamServer.makeStreamUrl: OPEN -> REACHABLE SOURCE.
  Fresh DetailTorrentViewModel.java:338-342, `getStreamUrl(int fileIndex)` returns
  `TorrentStreamServer.makeStreamUrl(hostname, port, torrentId, fileIndex)`.
  Caveat: getStreamUrl's own caller (the detail fragment/UI that asks for a stream URL)
  was not printed in this pass, so this row is anchored at getStreamUrl; under a strict
  rule requiring a printed caller for getStreamUrl itself, it reverts to OPEN. Recorded,
  not decided.
- Row 25, SettingsRepositoryImpl.anonymousMode(boolean): OPEN -> REACHABLE SOURCE.
  Fresh AnonymousModeSettingsFragment.java:79, `pref.anonymousMode((boolean)newValue)` in
  onPreferenceChange; getter at :59. The fragment itself is reached fresh from
  NetworkSettingsFragment.java:246-257 (click listener -> setFragment(newInstance()) on
  large screens, or startActivity(PreferenceActivity) with an AnonymousMode config on
  small screens).
- Row 30, SettingsRepositoryImpl.askNotificationPermission(): OPEN -> REACHABLE SOURCE.
  Fresh PermissionManager.java:89, `pref.askNotificationPermission()` inside the
  RequestMultiplePermissions result lambda (registration at :70-93 is ungated; the
  TIRAMISU branch at :75-79 only sets notificationsResult=true off-API-33, it does not
  gate the :89 call). The :110 call is T-gated and is NOT relied on.
- Row 33, SettingsRepositoryImpl.autoManage(boolean): OPEN -> REACHABLE SOURCE.
  Fresh LimitationsSettingsFragment.java:241, `pref.autoManage((boolean)newValue)` in
  onPreferenceChange.
- Rows 34-39, autoRefreshFeeds family: OPEN -> REACHABLE SOURCE.
  Fresh FeedSettingsFragment.java: getter autoRefreshFeeds :60, setter :130;
  getter autoRefreshFeedsUnmeteredConnectionsOnly :77, setter :149;
  getter autoRefreshFeedsEnableRoaming :84, setter :152. All in bind/onPreferenceChange.
  (Note: the prior proposal said Scheduler/FeedSettingsFragment were not printed in that
  session; FeedSettingsFragment is freshly printed here, and its lines match the
  batch-43 proposal's Scheduler note that Scheduler calls autoRefreshFeeds getters — that
  Scheduler route is a second, carried-forward lead, not relied on here.)
- Rows 28, 29, 31 stay OPEN for an API-27 reason, not for want of a printed line (see table).
  Their only printed call sites are API-gated false at API 27 (R = 30, TIRAMISU = 33):
  row 28 getter sites PermissionManager.java:65 (inside the R-gated StartActivityForResult
  registration at :60) and :100 (inside the R-gated branch at :99); row 29 setter site
  :118 (inside setDoNotAskStorage, R-gated at :117); row 31 setter site :124 (inside
  setDoNotAskNotifications, TIRAMISU-gated at :123). They are therefore strong
  `closed_by_api_level` LEADS, not verdicts: a saved full-repo grep finding any ungated
  caller flips them to REACHABLE; finding none would support `closed_by_api_level`.
  They are NOT labelled UNREACHABLE here, because no saved full-repo grep was run.
  This is the method-vs-branch distinction from batches 73-74: a method whose *call site
  itself* never runs at API 27 is a closed_by_api_level candidate, whereas a method whose
  body merely returns early at API 27 (e.g. batch 74's applyLegacyNotifySettings) stays
  REACHABLE if its call site runs.

## Shared trunk (carried-forward, prior proposal)

Rows 2-10: batch 39/40 trunk -> TorrentEngine.handleOnSessionStarted
(TorrentEngine.java:1046-1058, gate pref.enableStreaming()) ->
startStreamingServer (:1063-1071, new TorrentStreamServer :1069,
torrentStreamServer.start(appContext) :1071) -> TorrentStreamServer.start ->
super.start() (NanoHTTPD) -> ServerRunnable/ClientHandler/HTTPSession.execute
virtual serve(this) -> TorrentStreamServer.serve. Strict-entry caveat as in
batches 39-41 (launcher -> TorrentService not printed): under a strict launcher-entry
rule the streaming-anchored REACHABLE rows revert to OPEN. Settings-anchored rows
anchor at TorrentEngine.<init> (:133 RepositoryHelper.getSettingsRepository; :139
readSessionSettings) and at the settings fragments (display step via SettingsFragment,
printed in the batch 117-118 pass, not freshly re-printed here, except the
Network -> AnonymousMode step above, which IS fresh). The merger must pick one
strict-entry convention for all batches; it is recorded here, not decided.

## Table (plan order)

| # | Method | JVM descriptor | Label proposed | confirmed_by | Printed citation / note |
|---|---|---|---|---|---|
| 1 | TorrentStream$1.newArray | (I)[Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream; | OPEN | — | TorrentStream.java:112-115 return new TorrentStream[size]. Framework Parcelable dispatch only; no printed unparcel/array site in the prior corpus or the fresh files in this pass. Needs a printed read site or a saved full-repo grep. NOT UNREACHABLE on absence alone. See batch 41 row 40 (createFromParcel, also OPEN) — flips together with the batch-41 Parcelable quartet on one printed parceling site. Carried-forward definition. |
| 2 | TorrentStreamServer.<clinit> | ()V | REACHABLE | INFERRED | Static DLNA_FILE_TYPES block (TorrentStreamServer.java:55-62, new DLNAFileType for mp4/avi/mkv). JVM class initialisation on first use via TorrentEngine.startStreamingServer :1069. Carried-forward. |
| 3 | TorrentStreamServer.<init> | (Ljava/lang/String;I)V | REACHABLE | SOURCE | TorrentEngine.java:1069 torrentStreamServer = new TorrentStreamServer(hostname, port) in startStreamingServer. Def TorrentStreamServer.java:67-70 (super(host, port)). Carried-forward. |
| 4 | TorrentStreamServer.handleTorrent | (Lorg/nanohttpd/NanoHTTPD$IHTTPSession;)Lorg/nanohttpd/NanoHTTPD$Response; | REACHABLE | SOURCE | TorrentStreamServer.java:110-121 serve() calls handleTorrent(session) :119 area. Def :127-260 (engine.getStream :142, engine.getTorrentInputStream :206,:243, newFixedLengthResponse overloads). Carried-forward. |
| 5 | TorrentStreamServer.makeStreamUrl | (Ljava/lang/String;ILjava/lang/String;I)Ljava/lang/String; | REACHABLE | SOURCE | FRESH: DetailTorrentViewModel.java:338-342 getStreamUrl returns TorrentStreamServer.makeStreamUrl(hostname, port, torrentId, fileIndex). Def TorrentStreamServer.java:93-110 (static, builds /stream?file=%d&torrent=%s URI). Caveat: getStreamUrl's own caller not printed in this pass; see "Changes in this pass". |
| 6 | TorrentStreamServer.serve | (Lorg/nanohttpd/NanoHTTPD$IHTTPSession;)Lorg/nanohttpd/NanoHTTPD$Response; | REACHABLE | INFERRED | Overrides NanoHTTPD serve. Dispatch: HTTPSession.execute virtual serve(this) (batch 16/17 trunk, NanoHTTPD.java:720-733 area) — library dispatch INFERRED, body SOURCE (TorrentStreamServer.java:110-121: getUri, DLNA_FILE_TYPES.get, handleTorrent, fileType.setHeaders). Carried-forward. |
| 7 | TorrentStreamServer.start | (Landroid/content/Context;)V | REACHABLE | SOURCE | TorrentEngine.java:1071 torrentStreamServer.start(appContext) in startStreamingServer. Def TorrentStreamServer.java:72-79 (engine = TorrentEngine.getInstance(appContext), super.start()). Carried-forward. |
| 8 | TorrentStreamServer.stop | ()V | REACHABLE | SOURCE | TorrentEngine.java:1081 torrentStreamServer.stop() in stopStreamingServer (:1078-1083, guard torrentStreamServer != null). Def TorrentStreamServer.java:81-87 (super.stop()). Carried-forward. |
| 9 | TorrentStreamServer$DLNAFileType.<init> | (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V | REACHABLE | INFERRED | TorrentStreamServer.java:57-59 new DLNAFileType(...) x3 in the static block (row 2). Runs on TorrentStreamServer class load; numbering/ordering is JVM static-init semantics, not a printed call line. Carried-forward. |
| 10 | TorrentStreamServer$DLNAFileType.setHeaders | (Lorg/nanohttpd/NanoHTTPD$Response;)V | REACHABLE | SOURCE | TorrentStreamServer.java:119-120 fileType.setHeaders(res) in serve, gate fileType != null (extension in DLNA_FILE_TYPES: mp4/avi/mkv). Def :277-284. Carried-forward. |
| 11 | SessionSettings.<clinit> | ()V | REACHABLE | INFERRED | Static DEFAULT_* constants (SessionSettings.java:40-115 area, incl. DEFAULT_ENCRYPT_MODE = EncryptMode.ENABLED, DEFAULT_PROXY_TYPE = ProxyType.NONE). JVM initialisation on first use via TorrentSessionImpl field :143 new SessionSettings(). Carried-forward. |
| 12 | SessionSettings.<init>() | ()V | REACHABLE | SOURCE | TorrentSessionImpl.java:143 private SessionSettings settings = new SessionSettings() (field initialiser, runs on TorrentSessionImpl construction, TorrentEngine.java:136). Def SessionSettings.java:118 (empty ctor). Carried-forward. |
| 13 | SessionSettings.<init>(SessionSettings) | (Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V | REACHABLE | SOURCE | TorrentSessionImpl.java:226 return new SessionSettings(settings) in getSettings(). Def SessionSettings.java:120-165 (copy ctor). Carried-forward. |
| 14 | SessionSettings.getRandomRangePort | ()Lorg/libtorrent4j/Pair; | REACHABLE | SOURCE | TorrentSessionImpl.java:1403 SessionSettings.getRandomRangePort() in setRandomPort. Def SessionSettings.java:234-245 (port in [37000, 57000], second = first + 10). Carried-forward. |
| 15 | SessionSettings$EncryptMode.<clinit> | ()V | REACHABLE | INFERRED | Enum constants ENABLED(0)/FORCED(1)/DISABLED(2) (SessionSettings.java:166-172). JVM enum initialisation on first use (DEFAULT_ENCRYPT_MODE, TorrentEngine.fromValue calls rows 17). Carried-forward. |
| 16 | SessionSettings$EncryptMode.<init> | (Ljava/lang/String;II)V | REACHABLE | INFERRED | Implicit enum ctor (SessionSettings.java:174-177, EncryptMode(int val)). Invoked once per constant at class load; JVM semantics, not a printed call line. Carried-forward. |
| 17 | SessionSettings$EncryptMode.fromValue | (I)Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$EncryptMode; | REACHABLE | SOURCE | TorrentEngine.java:1109 SessionSettings.EncryptMode.fromValue(pref.encryptInConnectionsMode()); :1113 fromValue(pref.encryptOutConnectionsMode()). Def SessionSettings.java:186-194. Carried-forward. |
| 18 | SessionSettings$EncryptMode.value | ()I | REACHABLE | SOURCE | SessionSettings.java:190 ev.value() inside fromValue's loop (row 17). Def :181-184 (return val). Internal call, printed. Carried-forward. |
| 19 | SessionSettings$ProxyType.<clinit> | ()V | REACHABLE | INFERRED | Enum constants NONE(0)/SOCKS4(1)/SOCKS5(2)/HTTP(3) (SessionSettings.java:197-202). Same caveat as row 15. Carried-forward. |
| 20 | SessionSettings$ProxyType.<init> | (Ljava/lang/String;II)V | REACHABLE | INFERRED | Implicit enum ctor (SessionSettings.java:206-210). Same caveat as row 16. Carried-forward. |
| 21 | SessionSettings$ProxyType.fromValue | (I)Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$ProxyType; | REACHABLE | SOURCE | TorrentEngine.java:1097 s.proxyType = SessionSettings.ProxyType.fromValue(pref.proxyType()) in setProxy. Def SessionSettings.java:211-221 (returns NONE on no match). Carried-forward. |
| 22 | SessionSettings$ProxyType.value | ()I | REACHABLE | SOURCE | SessionSettings.java:215 ev.value() inside fromValue's loop (row 21). Def :223-226. Carried-forward. |
| 23 | SettingsRepositoryImpl.<init> | (Landroid/content/Context;)V | REACHABLE | SOURCE | RepositoryHelper.java: getSettingsRepository (synchronized, if settingsRepo == null settingsRepo = new SettingsRepositoryImpl(appContext)). Called from TorrentEngine ctor (TorrentEngine.java:133 pref = RepositoryHelper.getSettingsRepository(appContext)). Carried-forward. |
| 24 | SettingsRepositoryImpl.anonymousMode() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1604 s.anonymousMode = pref.anonymousMode() in settings-to-SessionSettings conversion. Def SettingsRepositoryImpl.java:929-931 (pref.getBoolean(pref_key_anonymous_mode, Default.anonymousMode)). Carried-forward; also fresh AnonymousModeSettingsFragment.java:59 setChecked(pref.anonymousMode()). |
| 25 | SettingsRepositoryImpl.anonymousMode(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: AnonymousModeSettingsFragment.java:79 pref.anonymousMode((boolean)newValue) in onPreferenceChange (bind at :60, preference from R.xml.pref_anonymous_mode). Def SettingsRepositoryImpl.java:935-939 (putBoolean). Fragment reached fresh from NetworkSettingsFragment.java:246-257. |
| 26 | SettingsRepositoryImpl.applyProxy() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1569 if (pref.applyProxy()) in preference-change handling (pref_key_apply_proxy branch). Def SettingsRepositoryImpl.java:1085-1087. Carried-forward. |
| 27 | SettingsRepositoryImpl.applyProxy(boolean) | (Z)V | REACHABLE | SOURCE | TorrentEngine.java:1570 pref.applyProxy(false) in the same branch (after applying proxy, clears the flag, then setProxy()). Def SettingsRepositoryImpl.java:1091-1095. Carried-forward. |
| 28 | SettingsRepositoryImpl.askManageAllFilesPermission() | ()Z | OPEN | — | Def SettingsRepositoryImpl.java:1397-1399. Printed call sites in this pass are ALL API-gated false at API 27: fresh PermissionManager.java:65 (inside R-gated StartActivityForResult registration at :60) and :100 (inside R-gated branch at :99). No ungated caller printed in the prior corpus or the fresh files. Strong `closed_by_api_level` LEAD, not a verdict: a saved full-repo grep finding any ungated caller flips to REACHABLE; finding none would support `closed_by_api_level`. NOT UNREACHABLE on this evidence. |
| 29 | SettingsRepositoryImpl.askManageAllFilesPermission(boolean) | (Z)V | OPEN | — | Def SettingsRepositoryImpl.java:1403-1407. Only printed call site: fresh PermissionManager.java:118 pref.askManageAllFilesPermission(!doNotAsk) inside setDoNotAskStorage, R-gated at :117 — false at API 27. Same closed_by_api_level lead as row 28; needs a saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 30 | SettingsRepositoryImpl.askNotificationPermission() | ()Z | REACHABLE | SOURCE | FRESH: PermissionManager.java:89 pref.askNotificationPermission() inside the RequestMultiplePermissions result lambda (registration :70-93 ungated; the TIRAMISU branch at :75-79 only sets notificationsResult=true off-API-33 and does not gate :89). Def SettingsRepositoryImpl.java:1425-1427. The :110 call is T-gated and is NOT relied on. |
| 31 | SettingsRepositoryImpl.askNotificationPermission(boolean) | (Z)V | OPEN | — | Def SettingsRepositoryImpl.java:1431-1435. Only printed call site: fresh PermissionManager.java:124 pref.askNotificationPermission(!doNotAsk) inside setDoNotAskNotifications, TIRAMISU-gated at :123 — false at API 27. Strong `closed_by_api_level` LEAD, not a verdict: needs a saved full-repo grep for an ungated caller. NOT UNREACHABLE on this evidence. |
| 32 | SettingsRepositoryImpl.autoManage() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1579 session.setAutoManaged(pref.autoManage()) in preference-change handling (pref_key_auto_manage branch). Def SettingsRepositoryImpl.java:981-983. Carried-forward; also fresh LimitationsSettingsFragment.java:108 setChecked(pref.autoManage()). |
| 33 | SettingsRepositoryImpl.autoManage(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: LimitationsSettingsFragment.java:241 pref.autoManage((boolean)newValue) in onPreferenceChange. Def SettingsRepositoryImpl.java:987-991. |
| 34 | SettingsRepositoryImpl.autoRefreshFeeds() | ()Z | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:60 autoRefresh.setChecked(pref.autoRefreshFeeds()) in bind. Def SettingsRepositoryImpl.java:1189-1191 (pref_key_feed_auto_refresh). |
| 35 | SettingsRepositoryImpl.autoRefreshFeeds(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:130 pref.autoRefreshFeeds((boolean)newValue) in onPreferenceChange (which then runs/cancels Scheduler.runPeriodicalRefreshFeeds). Def SettingsRepositoryImpl.java:1195-1199. |
| 36 | SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming() | ()Z | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:84 roaming.setChecked(pref.autoRefreshFeedsEnableRoaming()) in bind. Def SettingsRepositoryImpl.java:1228-1230. |
| 37 | SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:152 pref.autoRefreshFeedsEnableRoaming((boolean)newValue) in onPreferenceChange. Def SettingsRepositoryImpl.java:1234-1238. |
| 38 | SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly() | ()Z | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:77 unmeteredOnly.setChecked(pref.autoRefreshFeedsUnmeteredConnectionsOnly()) in bind. Def SettingsRepositoryImpl.java:1215-1217. |
| 39 | SettingsRepositoryImpl.autoRefreshFeedsUnmeteredConnectionsOnly(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: FeedSettingsFragment.java:149 pref.autoRefreshFeedsUnmeteredConnectionsOnly((boolean)newValue) in onPreferenceChange. Def SettingsRepositoryImpl.java:1221-1225. |
| 40 | SettingsRepositoryImpl.autostart() | ()Z | REACHABLE | SOURCE | Utils.java:440 and :453 boolean autostart = pref.autostart() (batch 20/21 local copy, printed in that session and re-grepped in the prior proposal). Def SettingsRepositoryImpl.java:409-411 (pref_key_autostart, Default.autostart=false). Carried-forward; also fresh BehaviorSettingsFragment.java:74 setChecked(pref.autostart()). |

## Counts (mechanically verified in this pass: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 36 (SOURCE 28, INFERRED 8)
- UNREACHABLE proposed: 0
- OPEN: 4 (rows 1, 28, 29, 31)
- Total: 40. **0 rows verified for merge** — main-agent spot-check 1 in 5, py_compile,
  build, and Mac build/C1 are all still outstanding and are marked not run, never passed.

## OPEN items and what resolves them

- Row 1 (TorrentStream$1.newArray): a printed unparcel/array site, or a saved full-repo
  grep — flips together with batch 41 rows 31/34/38/40.
- Rows 28, 29, 31 (ask* getter/setter): a saved full-repo grep for an ungated caller.
  If none exists, the merger (with the API-27 standard config) would have the printed
  R/T-gating evidence for `closed_by_api_level`; that kind is NOT assigned here because
  the grep has not been run.
- No row in this batch is labelled UNREACHABLE: none meets the bar of exactly one kind
  + reason + source reference on printed evidence. In particular, the SettingsRepositoryImpl
  setters are interface implementations of a SharedPreferences repository; the newly
  closed setters above show the normal pattern is a settings fragment writing them, and
  the three remaining OPEN setters have only API-gated printed sites, which is a gate
  argument, not an absence argument.
