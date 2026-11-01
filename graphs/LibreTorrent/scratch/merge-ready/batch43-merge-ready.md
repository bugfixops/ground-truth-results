# LibreTorrent batch 43 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 43 only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for batch 43 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
  `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
  All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order, method names and
  JVM descriptors matched row for row against the plan in this pass.
- Prior work used as INPUT only: `~/workspace/libretorrent-batch43-proposal.md`
  (19 REACHABLE proposed / 0 UNREACHABLE / 21 OPEN). In this pass ALL 21 OPEN rows were
  closed to REACHABLE on freshly printed source (see "Changes in this pass" below).
  No verdict below is copied as a result without a printed citation.
- Printed source in this pass, fresh connector fetches from branch `work-2026-10-31`,
  one file at a time with 20 s pauses, no fresh HTTP 429 hit, saved in
  `~/workspace/b4143-src/`: BehaviorSettingsFragment.java (286 lines),
  FeedSettingsFragment.java (164), LimitationsSettingsFragment.java (258),
  NetworkSettingsFragment.java (415), SchedulingSettingsFragment.java (243),
  StorageSettingsFragment.java (297), StreamingSettingsFragment.java (119),
  PermissionManager.java (156), DetailTorrentViewModel.java (611),
  AnonymousModeSettingsFragment.java (84). The settings fragments are the files that
  close the 21 OPEN rows; their line numbers below are from these fresh copies and
  match the prior session's local copies line for line.
- Carried-forward printed source (prior proposal session, printed in full then, NOT
  freshly re-printed in this pass — merger should re-verify line numbers against a fresh
  fetch if it requires it): SettingsRepositoryImpl.java (SHA
  `a8b6f542132b58949709dc466ace278efd28ccf3`, 1436 lines, all definitions below),
  TorrentEngine.java (1659 lines, pref.* call sites), TorrentService.java (525 lines),
  Scheduler.java (145 lines, printed in full in the prior session; contains NO call to any
  batch-43 method — only autoRefreshFeeds* getters at :132/:134, which are batch-42 rows).
- `confirmed_by` convention in this file: SOURCE = a direct app-to-app call site naming
  the method is printed in app source. Every REACHABLE row in this batch has such a site,
  so INFERRED is not used here. This is the per-row convention, not the whole-route
  convention used in some earlier batches; labels are unaffected, only `confirmed_by`
  would change at merge if the merger adopts the whole-route convention.
  SettingsRepositoryImpl methods are called through the SettingsRepository interface
  (`pref.*`); the implementation is the singleton built by RepositoryHelper.getSettingsRepository
  (carried-forward: called from TorrentEngine ctor TorrentEngine.java:133) — that interface
  dispatch is the reason a fragment `pref.setter(...)` line is SOURCE for the Impl method.
- No connector `search_code` result was used as evidence of absence anywhere in this file,
  and no row is labelled UNREACHABLE in this batch.

## Changes in this pass (vs the prior proposal) — all on freshly printed source, all SOURCE

Every OPEN row in the prior proposal was a setter (or, for scheduling, a getter/setter
pair) whose writer/reader had not been printed because that session printed only
TorrentEngine, TorrentService, FeedSettingsFragment, and Scheduler. The settings
fragments freshly printed here supply the missing writers/readers, and none of them
is API-gated (grep of the fresh fragments returns no `SDK_INT`/`Build.VERSION` lines
at all — the only gated file in this pass is PermissionManager, which holds no
batch-43 row):

- Row 1, autostart(boolean): BehaviorSettingsFragment.java:203
  (`pref.autostart((boolean)newValue)` in onPreferenceChange; getter also at :74).
- Row 3, batteryControl(boolean): BehaviorSettingsFragment.java:212 (and :273
  `pref.batteryControl(false)` reset).
- Row 5, cpuDoNotSleep(boolean): BehaviorSettingsFragment.java:235.
- Row 7, customBatteryControl(boolean): BehaviorSettingsFragment.java:218 (and :283
  `pref.customBatteryControl(false)` reset).
- Row 9, customBatteryControlValue(int): BehaviorSettingsFragment.java:238.
- Row 11, defaultTrackersList(String): BehaviorSettingsFragment.java:241.
- Row 13, dirToWatch(String): StorageSettingsFragment.java:258
  (`pref.dirToWatch(path.toString())` in the dir-chooser result handling; getter at :176).
- Row 15, enableDht(boolean): NetworkSettingsFragment.java:320.
- Row 17, enableIpFiltering(boolean): NetworkSettingsFragment.java:349.
- Row 19, enableLsd(boolean): NetworkSettingsFragment.java:323.
- Row 21, enableNatPmp(boolean): NetworkSettingsFragment.java:332.
- Row 23, enableRoaming(boolean): BehaviorSettingsFragment.java:226.
- Row 24, enableSchedulingShutdown(): SchedulingSettingsFragment.java:79
  (`enableStop.setChecked(pref.enableSchedulingShutdown())` in bind).
- Row 25, enableSchedulingShutdown(boolean): SchedulingSettingsFragment.java:209.
- Row 26, enableSchedulingStart(): SchedulingSettingsFragment.java:72
  (`enableStart.setChecked(pref.enableSchedulingStart())` in bind).
- Row 27, enableSchedulingStart(boolean): SchedulingSettingsFragment.java:196.
- Row 29, enableStreaming(boolean): StreamingSettingsFragment.java:113
  (getter also at :61).
- Row 31, enableUpnp(boolean): NetworkSettingsFragment.java:329.
- Row 33, enableUtp(boolean): NetworkSettingsFragment.java:326.
- Row 35, encryptInConnectionsMode(int): NetworkSettingsFragment.java:342
  (`pref.encryptInConnectionsMode(type)`; getter at :182).
- Row 37, encryptOutConnectionsMode(int): NetworkSettingsFragment.java:346
  (getter at :190).

## Shared trunks (prior proposal, carried-forward except FeedSettingsFragment rows below)

- T-E (engine): TorrentEngine.<init> gets pref via RepositoryHelper
  (TorrentEngine.java:133), calls pref.readSessionSettings() at :139.
  SettingsRepositoryImpl.readSessionSettings (:212-261) internally calls:
  maxConnections :215, enableDht :223, enableLsd :224, enableUtp :225,
  enableUpnp :226, enableNatPmp :227, encryptInConnectionsMode :228,
  encryptOutConnectionsMode :229, defaultTrackersList :234.
- T-S (service): TorrentService init calls pref.observeSettingsChanged() (:125),
  setKeepCpuAwake(pref.cpuDoNotSleep()) (:129); handleSettingsChanged calls
  pref.cpuDoNotSleep() again (:267).
- T-F (feed fragment): FeedSettingsFragment binds preferences and calls getters
  in its bind block and setters in onPreferenceChange (:125-158). Freshly verified
  in this pass: feedItemKeepTime getter :91, setter :146; feedRemoveDuplicates
  getter :108, setter :158 — matching the prior proposal's lines exactly.
- Strict-entry caveat: TorrentEngine/TorrentService routes anchor at
  TorrentEngine.<init> (:133 RepositoryHelper.getSettingsRepository; :139
  readSessionSettings) / TorrentService init / TorrentEngine.start, and at
  FeedSettingsFragment and the other settings fragments' preference handling. The
  launcher -> MainActivity -> TorrentService step was NOT printed in the prior
  proposal or in this pass, and the SettingsFragment -> section-fragment display
  step was printed in the batch 117-118 pass, not freshly re-printed here. Under a
  strict launcher-entry rule these REACHABLE rows are conditional on those unprinted
  steps. The merger must pick one strict-entry convention for all batches; it is
  recorded here, not decided.

## Table (plan order)

| # | Method | JVM descriptor | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.autostart(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:203 pref.autostart((boolean)newValue) in onPreferenceChange (getter also :74). Definition SettingsRepositoryImpl.java:415. Prior proposal: OPEN (no caller in its 5 files); closed here. |
| 2 | SettingsRepositoryImpl.batteryControl() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:990 (switchPowerReceiver) and :1024 (checkPauseTorrents): `pref.batteryControl()`. Definition :474. Carried-forward; also fresh BehaviorSettingsFragment.java:111 setChecked(pref.batteryControl()). |
| 3 | SettingsRepositoryImpl.batteryControl(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:212 pref.batteryControl((boolean)newValue) in onPreferenceChange; also :273 pref.batteryControl(false) reset. Definition :480. Prior proposal: OPEN; closed here. |
| 4 | SettingsRepositoryImpl.cpuDoNotSleep() | ()Z | REACHABLE | SOURCE | TorrentService.java:129 (init) and :267 (handleSettingsChanged): `pref.cpuDoNotSleep()`. Definition :448. Carried-forward; also fresh BehaviorSettingsFragment.java:95 setChecked(pref.cpuDoNotSleep()). |
| 5 | SettingsRepositoryImpl.cpuDoNotSleep(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:235 pref.cpuDoNotSleep((boolean)newValue) in onPreferenceChange. Definition :454. Prior proposal: OPEN; closed here. |
| 6 | SettingsRepositoryImpl.customBatteryControl() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:991 and :1025: `pref.customBatteryControl()`. Definition :487. Carried-forward; also fresh BehaviorSettingsFragment.java:120 setChecked(pref.customBatteryControl()). |
| 7 | SettingsRepositoryImpl.customBatteryControl(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:218 pref.customBatteryControl((boolean)newValue) in onPreferenceChange; also :283 pref.customBatteryControl(false) reset. Definition :493. Prior proposal: OPEN; closed here. |
| 8 | SettingsRepositoryImpl.customBatteryControlValue() | ()I | REACHABLE | SOURCE | TorrentEngine.java:1026 (checkPauseTorrents): `pref.customBatteryControlValue()`. Definition :500. Carried-forward; also fresh BehaviorSettingsFragment.java:127 setValue(pref.customBatteryControlValue()). |
| 9 | SettingsRepositoryImpl.customBatteryControlValue(int) | (I)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:238 pref.customBatteryControlValue((int)newValue) in onPreferenceChange. Definition :506. Prior proposal: OPEN; closed here. |
| 10 | SettingsRepositoryImpl.defaultTrackersList() | ()Ljava/lang/String; | REACHABLE | SOURCE | TorrentEngine.java:1648 `pref.defaultTrackersList().split(...)`, and internally SettingsRepositoryImpl.readSessionSettings:234. Definition :955. Carried-forward; also fresh BehaviorSettingsFragment.java:154 setText(pref.defaultTrackersList()). |
| 11 | SettingsRepositoryImpl.defaultTrackersList(String) | (Ljava/lang/String;)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:241 pref.defaultTrackersList((String)newValue) in onPreferenceChange. Definition :961. Prior proposal: OPEN; closed here. |
| 12 | SettingsRepositoryImpl.dirToWatch() | ()Ljava/lang/String; | REACHABLE | SOURCE | TorrentEngine.java:1117 (makeTorrentFileObserver path): `pref.dirToWatch()`. Definition :786. Carried-forward; also fresh StorageSettingsFragment.java:176 String path = pref.dirToWatch(). |
| 13 | SettingsRepositoryImpl.dirToWatch(String) | (Ljava/lang/String;)V | REACHABLE | SOURCE | FRESH: StorageSettingsFragment.java:258 pref.dirToWatch(path.toString()) in dir-chooser result handling. Definition :792. Prior proposal: OPEN; closed here. |
| 14 | SettingsRepositoryImpl.enableDht() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1512 (applySessionSettings) and internally readSessionSettings:223. Definition :565. Carried-forward; also fresh NetworkSettingsFragment.java:114 setChecked(pref.enableDht()). |
| 15 | SettingsRepositoryImpl.enableDht(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:320 pref.enableDht((boolean) newValue) in onPreferenceChange. Definition :571. Prior proposal: OPEN; closed here. |
| 16 | SettingsRepositoryImpl.enableIpFiltering() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1047 (handleOnSessionStarted) and :1555: `pref.enableIpFiltering()`. Definition :669. Carried-forward; also fresh NetworkSettingsFragment.java:198 setChecked(pref.enableIpFiltering()). |
| 17 | SettingsRepositoryImpl.enableIpFiltering(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:349 pref.enableIpFiltering((boolean) newValue) in onPreferenceChange. Definition :675. Prior proposal: OPEN; closed here. |
| 18 | SettingsRepositoryImpl.enableLsd() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1517 and internally readSessionSettings:224. Definition :578. Carried-forward; also fresh NetworkSettingsFragment.java:121 setChecked(pref.enableLsd()). |
| 19 | SettingsRepositoryImpl.enableLsd(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:323 pref.enableLsd((boolean) newValue) in onPreferenceChange. Definition :584. Prior proposal: OPEN; closed here. |
| 20 | SettingsRepositoryImpl.enableNatPmp() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1532 and internally readSessionSettings:227. Definition :617. Carried-forward; also fresh NetworkSettingsFragment.java:142 setChecked(pref.enableNatPmp()). |
| 21 | SettingsRepositoryImpl.enableNatPmp(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:332 pref.enableNatPmp((boolean) newValue) in onPreferenceChange. Definition :623. Prior proposal: OPEN; closed here. |
| 22 | SettingsRepositoryImpl.enableRoaming() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1011 and :1029 (checkPauseTorrents): `pref.enableRoaming()`. Definition :526. Carried-forward; also fresh BehaviorSettingsFragment.java:143 setChecked(pref.enableRoaming()). |
| 23 | SettingsRepositoryImpl.enableRoaming(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: BehaviorSettingsFragment.java:226 pref.enableRoaming((boolean)newValue) in onPreferenceChange. Definition :532. Prior proposal: OPEN; closed here. |
| 24 | SettingsRepositoryImpl.enableSchedulingShutdown() | ()Z | REACHABLE | SOURCE | FRESH: SchedulingSettingsFragment.java:79 enableStop.setChecked(pref.enableSchedulingShutdown()) in bind. Definition :1111. Prior proposal: OPEN (Scheduler.java does not call it); closed here via the scheduling fragment, not Scheduler. |
| 25 | SettingsRepositoryImpl.enableSchedulingShutdown(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: SchedulingSettingsFragment.java:209 pref.enableSchedulingShutdown((boolean)newValue) in onPreferenceChange. Definition :1117. Prior proposal: OPEN; closed here. |
| 26 | SettingsRepositoryImpl.enableSchedulingStart() | ()Z | REACHABLE | SOURCE | FRESH: SchedulingSettingsFragment.java:72 enableStart.setChecked(pref.enableSchedulingStart()) in bind. Definition :1098. Prior proposal: OPEN (Scheduler.java does not call it); closed here via the scheduling fragment. |
| 27 | SettingsRepositoryImpl.enableSchedulingStart(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: SchedulingSettingsFragment.java:196 pref.enableSchedulingStart((boolean)newValue) in onPreferenceChange. Definition :1104. Prior proposal: OPEN; closed here. |
| 28 | SettingsRepositoryImpl.enableStreaming() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1056 (handleOnSessionStarted, gate for startStreamingServer) and :1593: `pref.enableStreaming()`. Definition :1267. Carried-forward; also fresh StreamingSettingsFragment.java:61 setChecked(pref.enableStreaming()). |
| 29 | SettingsRepositoryImpl.enableStreaming(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: StreamingSettingsFragment.java:113 pref.enableStreaming((boolean)newValue) in onPreferenceChange. Definition :1273. Prior proposal: OPEN; closed here. |
| 30 | SettingsRepositoryImpl.enableUpnp() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1527 and internally readSessionSettings:226. Definition :604. Carried-forward; also fresh NetworkSettingsFragment.java:135 setChecked(pref.enableUpnp()). |
| 31 | SettingsRepositoryImpl.enableUpnp(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:329 pref.enableUpnp((boolean) newValue) in onPreferenceChange. Definition :610. Prior proposal: OPEN; closed here. |
| 32 | SettingsRepositoryImpl.enableUtp() | ()Z | REACHABLE | SOURCE | TorrentEngine.java:1522 and internally readSessionSettings:225. Definition :591. Carried-forward; also fresh NetworkSettingsFragment.java:128 setChecked(pref.enableUtp()). |
| 33 | SettingsRepositoryImpl.enableUtp(boolean) | (Z)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:326 pref.enableUtp((boolean) newValue) in onPreferenceChange. Definition :597. Prior proposal: OPEN; closed here. |
| 34 | SettingsRepositoryImpl.encryptInConnectionsMode() | ()I | REACHABLE | SOURCE | TorrentEngine.java:1109 and internally readSessionSettings:228. Definition :643. Carried-forward; also fresh NetworkSettingsFragment.java:182 var type = pref.encryptInConnectionsMode(). |
| 35 | SettingsRepositoryImpl.encryptInConnectionsMode(int) | (I)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:342 pref.encryptInConnectionsMode(type) in onPreferenceChange. Definition :649. Prior proposal: OPEN; closed here. |
| 36 | SettingsRepositoryImpl.encryptOutConnectionsMode() | ()I | REACHABLE | SOURCE | TorrentEngine.java:1113 and internally readSessionSettings:229. Definition :656. Carried-forward; also fresh NetworkSettingsFragment.java:190 var type = pref.encryptOutConnectionsMode(). |
| 37 | SettingsRepositoryImpl.encryptOutConnectionsMode(int) | (I)V | REACHABLE | SOURCE | FRESH: NetworkSettingsFragment.java:346 pref.encryptOutConnectionsMode(type) in onPreferenceChange. Definition :662. Prior proposal: OPEN; closed here. |
| 38 | SettingsRepositoryImpl.feedItemKeepTime() | ()J | REACHABLE | SOURCE | FRESH (verified this pass, matches prior): FeedSettingsFragment.java:91 pref.feedItemKeepTime() while binding the keep-time preference. Definition :1176. |
| 39 | SettingsRepositoryImpl.feedItemKeepTime(long) | (J)V | REACHABLE | SOURCE | FRESH (verified this pass, matches prior): FeedSettingsFragment.java:146 (onPreferenceChange, pref_key_feed_keep_items_time branch): `pref.feedItemKeepTime(keepTime)`. Definition :1182. |
| 40 | SettingsRepositoryImpl.feedRemoveDuplicates() | ()Z | REACHABLE | SOURCE | FRESH (verified this pass, matches prior): FeedSettingsFragment.java:108 pref.feedRemoveDuplicates() while binding the switch preference. Definition :1254. (Its setter is batch 44 row 1, not judged here.) |

## Counts (mechanically verified in this pass: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 40 (SOURCE 40, INFERRED 0)
- UNREACHABLE proposed: 0
- OPEN: 0
- Total: 40. **0 rows verified for merge** — main-agent spot-check 1 in 5, py_compile,
  build, and Mac build/C1 are all still outstanding and are marked not run, never passed.

## Still owed before merge

1. Printed launcher -> MainActivity -> TorrentService step (strict-entry caveat above),
   and a fresh re-print of the TorrentEngine/TorrentService/SettingsRepositoryImpl line
   numbers carried forward from the prior proposal, if the merger requires fresh numbers
   for those rows (the FeedSettingsFragment rows and all 21 newly closed rows are already
   fresh in this pass).
2. Build / sampler / C1 on a full checkout (clone still unavailable in this VM; build and
   C1 run on the user's Mac after push, marked not run here).
3. No saved full-repo grep is owed for this batch: there are no OPEN rows left. That does
   NOT make the batch verified — the spot-check, py_compile, build, and Mac build/C1
   above are still outstanding.
