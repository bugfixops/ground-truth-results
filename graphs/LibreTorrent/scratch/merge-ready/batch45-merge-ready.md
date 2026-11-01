# LibreTorrent batch 45 — MERGE-READY — UNVERIFIED

- Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only (never main, never result).
- Membership: exactly the 40 rows of batch 45 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
  (git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92; local copy
  ~/workspace/agent27-plan.tsv; plan extract saved at ~/workspace/b444546-src/batch45_plan.tsv).
  All 40 rows are SettingsRepositoryImpl methods, all plan status TODO_CANDIDATE_REACHABLE
  (generator candidates, not evidence).
- Status: **UNVERIFIED merge-ready part. NOT verified for merge. NOT pushed.**
  Pushes are held until verified and merged to [L]. No edit to graph_def.py, out/,
  PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.
- Prior proposal (~/workspace/libretorrent-batch45-proposal.md, 36/4/0) was used as a
  lead list only. Every row below was re-judged against source freshly fetched in this
  pass. Labels are UNCHANGED vs that proposal (36/4/0); the evidence base is upgraded
  from local copies to fresh connector fetches for every cited file, and confirmed_by
  changes from all-INFERRED to per-row SOURCE (see convention note — labels unaffected).
- Build: **not run**. C1: **not run** (both run on the user's Mac after a push, never
  claimed passed). No sampler, no saved full-repo grep, no py_compile by this helper
  (main-agent step). Main-agent spot-check 1 in 5 still outstanding.
- No search_code result was used as evidence anywhere, and no search_code 0 was used
  as evidence of absence. No true git clone was attempted: a true git clone fails in
  this VM (no credential device) — that check is named missing, never passed; all
  source below came via the GitHub connector only.
- No fresh HTTP 429 was hit in this pass (16 connector fetches, one at a time with
  ~25 s pauses, all succeeded).

## Printed source used (fresh, branch work-2026-10-31, saved in ~/workspace/b444546-src/)

- SettingsRepositoryImpl.java — 1,435 lines (all definitions below; observeSettingsChanged
  :195-211, readSessionSettings :212-261).
- TorrentEngine.java — 1,658 lines (pref :104/:133; observeSettingsChanged subscription
  :240-241; handleAutoStop :144; switchPowerReceiver :992; switchConnectionReceiver :1010;
  checkPauseTorrents :1027-1028; startStreamingServer :1066-1067; setProxy :1097-1103;
  addTorrentSync :1185; setRandomPortRange :1236-1237; onTorrentAdded :1273/:1275;
  onTorrentFinished :1315/:1317; onNatError :1395; onTorrentMetadataLoaded :1431;
  handleSettingsChanged :1456-1652, key-guarded per preference key).
- TorrentService.java — 525 lines (observeSettingsChanged subscription :125-126).
- TorrentNotifier.java — 294 lines (makeTorrentFinishedNotify :212-213;
  applyLegacyNotifySettings :275-291, early return `SDK_INT >= O` at :276, playSoundNotify
  :281, notifySound :282).
- AppearanceSettingsFragment.java — 271 lines (SDK < O gate at :118-119 →
  initLegacyNotifySettings :128-192: playSound display :133, listener bound :134,
  notifySound display :139, click listener :144-168 with notifySound re-read :151,
  ringtonePicker result handler :206-213 with notifySound setter :213;
  onPreferenceChange playSoundNotify branch :241).
- LimitationsSettingsFragment.java — 257 lines (displays :76/:87/:149/:160;
  onPreferenceChange setters :189/:199/:209/:237).
- StorageSettingsFragment.java — 296 lines (displays :95/:115/:122/:203;
  directory-picker result handler :261/:264/:267; onPreferenceChange :283/:289).
- NetworkSettingsFragment.java — 414 lines (displays :153/:162/:172;
  onPreferenceChange setters :309/:316).
- ProxySettingsFragment.java — 247 lines (displays :106/:115/:126/:138/:146/:154/:163;
  onPreferenceChange setters :210/:218/:223/:227/:231/:237/:240).
- BehaviorSettingsFragment.java — 285 lines (displays :88/:102/:136;
  onPreferenceChange setters :206/:223/:232).
- LogSettingsFragment.java — 101 lines (maxLogSize display :69, setter :95).
- FeedSettingsFragment.java, SchedulingSettingsFragment.java, StreamingSettingsFragment.java,
  Utils.java, AddTorrentViewModel.java — also freshly fetched and grepped in this pass
  (no batch-45 call site found in them beyond the rows cited).
- RepositoryHelper.java was NOT freshly fetched in this pass: the claim that
  getSettingsRepository() returns the singleton `new SettingsRepositoryImpl` rests on
  the local copy ~/workspace/agent9/src/RepositoryHelper.java (:61-64) — flagged here
  (see confirmed_by convention below).

## Shared trunks (printed fresh)

- Engine trunk: TorrentService.onCreate → TorrentEngine.getInstance → TorrentEngine.<init>
  :133/:139 → readSessionSettings() :212-261, which internally calls maxUploadSpeedLimit
  :214, maxConnectionsPerTorrent :216, maxUploadsPerTorrent :217, portRangeFirst :221,
  portRangeSecond :222, posixDiskIo :241, proxyType :243, proxyAddress :244, proxyPort :245,
  proxyPeersToo :246, proxyRequiresAuth :247, proxyLogin :248, proxyPassword :249,
  maxLogSize :252 (plus batch-44/46 getters).
- Settings-change trunk: TorrentService.init :125-126 / TorrentEngine.doStart :240-241 →
  observeSettingsChanged() (row 17) → handleSettingsChanged(key) → key-guarded getters.
  A key guard is the route's dispatch condition (the getter runs when that preference
  changes), not a project GATE; labels are unaffected by it.
- Settings-UI trunk: user opens Settings → section fragment → onPreferenceChange
  (standard callback, listeners bound in ungated onCreate for every setter row marked
  REACHABLE below) → setter rows. The fragment-display step (Settings navigation) was
  NOT printed — see strict-entry caveat.

## Conventions recorded per row, NOT decided

- confirmed_by, per-row (this file): SOURCE = a printed app-code line naming the method;
  INFERRED = the route crosses unprinted framework/library/Rx dispatch (row 17, Rx
  subscription) or rests on a printed gate with no ungated caller (UNREACHABLE rows).
  This DIFFERS from the prior batch-45 proposal, which marked every row INFERRED on the
  ground that all `pref` variables are typed to the SettingsRepository interface
  (TorrentEngine :104, TorrentService :82, TorrentNotifier :63, Utils :167/:639) and
  only the (not freshly fetched) RepositoryHelper local copy shows the singleton is a
  SettingsRepositoryImpl. Under that interface-dispatch convention, all SOURCE rows here
  would read INFERRED; labels are unaffected. Batch 43 merge-ready used SOURCE for the
  same pref.* pattern. The merger must pick one convention and apply it across
  batches 43-46. This file uses SOURCE, consistent with batch 43 and batch 44.
- Strict-entry: routes anchor at TorrentEngine/TorrentService/fragments, not at a printed
  launcher step, and fragment-anchored rows assume the fragment is displayed from
  Settings (that step was NOT printed). Under a strict printed-launcher rule all
  REACHABLE rows revert to OPEN. This does not change the UNREACHABLE rows.
- Method-vs-call-site rule for the API-gated rows (15, 16, 20, 21): identical to batch 44
  rows 17-20. A method is closed_by_api_level here only because its ONLY printed call
  statements never execute at API 27 — inside a method that returns early at SDK >= O
  (TorrentNotifier :276, before :281-282), inside a block that only runs at SDK < O
  (Appearance initLegacy, gate :118-119), in a click listener registered only inside
  that gated block (notifySound picker launch, :144-168), or in an onPreferenceChange
  branch whose listener is bound only inside that gated block (:134). The methods' own
  bodies are ordinary getters/setters; it is their call statements that are unreachable
  at API 27. A saved full-repo grep is still required before merge (see below).

## Rows (plan order)

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.maxConnectionsPerTorrent() | REACHABLE | SOURCE | readSessionSettings:216; TorrentEngine.java:1490 (handleSettingsChanged, key pref_key_max_connections_per_torrent); LimitationsSettingsFragment.java:149 display. Definition :864. |
| 2 | SettingsRepositoryImpl.maxConnectionsPerTorrent(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:189 (onPreferenceChange). Definition :870. |
| 3 | SettingsRepositoryImpl.maxDownloadSpeedLimit() | REACHABLE | SOURCE | TorrentEngine.java:1475 (handleSettingsChanged, key pref_key_max_download_speed); LimitationsSettingsFragment.java:76 display. Definition :825. |
| 4 | SettingsRepositoryImpl.maxDownloadSpeedLimit(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:209 (onPreferenceChange). Definition :831. |
| 5 | SettingsRepositoryImpl.maxLogSize() | REACHABLE | SOURCE | readSessionSettings:252; TorrentEngine.java:1644 (handleSettingsChanged); LogSettingsFragment.java:69 display. Definition :1319. |
| 6 | SettingsRepositoryImpl.maxLogSize(int) | REACHABLE | SOURCE | LogSettingsFragment.java:95 (onPreferenceChange). Definition :1325. |
| 7 | SettingsRepositoryImpl.maxUploadSpeedLimit() | REACHABLE | SOURCE | readSessionSettings:214; TorrentEngine.java:1480 (handleSettingsChanged). Definition :838. |
| 8 | SettingsRepositoryImpl.maxUploadSpeedLimit(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:199 (onPreferenceChange). Definition :844. |
| 9 | SettingsRepositoryImpl.maxUploadsPerTorrent() | REACHABLE | SOURCE | readSessionSettings:217; TorrentEngine.java:1493 (handleSettingsChanged). Definition :877. |
| 10 | SettingsRepositoryImpl.maxUploadsPerTorrent(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:237 (onPreferenceChange). Definition :883. |
| 11 | SettingsRepositoryImpl.moveAfterDownload() | REACHABLE | SOURCE | TorrentEngine.java:1315 (onTorrentFinished); StorageSettingsFragment.java:115 display. Definition :721. |
| 12 | SettingsRepositoryImpl.moveAfterDownload(boolean) | REACHABLE | SOURCE | StorageSettingsFragment.java:283 (onPreferenceChange). Definition :727. |
| 13 | SettingsRepositoryImpl.moveAfterDownloadIn() | REACHABLE | SOURCE | TorrentEngine.java:1317 (onTorrentFinished); StorageSettingsFragment.java:122 display. Definition :734. |
| 14 | SettingsRepositoryImpl.moveAfterDownloadIn(String) | REACHABLE | SOURCE | StorageSettingsFragment.java:261 (directory-picker result handler). Definition :740. |
| 15 | SettingsRepositoryImpl.notifySound() | UNREACHABLE closed_by_api_level | INFERRED | Definition :264. ONLY printed call sites in the 16 freshly fetched files: AppearanceSettingsFragment.java:139 and :151, both inside initLegacyNotifySettings, which runs only at SDK < O (gate :118-119); and TorrentNotifier.java:282, inside applyLegacyNotifySettings, which returns early at SDK >= O (:276) before reaching :282. At standard API 27 (O = 26, device 27) neither statement executes. PROPOSED only, pending saved full-repo grep: any non-gated caller flips this row to REACHABLE. |
| 16 | SettingsRepositoryImpl.notifySound(String) | UNREACHABLE closed_by_api_level | INFERRED | Definition :270. ONLY printed call site: AppearanceSettingsFragment.java:213 (ringtonePicker result handler); the picker is launched only from the click listener registered at :144-168, inside initLegacyNotifySettings (gate :118-119). At API 27 the picker is never launched, so the handler never runs. PROPOSED only, pending saved full-repo grep. |
| 17 | SettingsRepositoryImpl.observeSettingsChanged() | REACHABLE | INFERRED | Definition :195-211 (registers a SharedPreferences.OnSharedPreferenceChangeListener, :195-210). Subscribed by TorrentEngine.java:240-241 and TorrentService.java:125-126. Rx/Flowable dispatch not printed, hence INFERRED (the method body itself is printed; its three lambdas are batch 44 rows 14-16). |
| 18 | SettingsRepositoryImpl.onlyCharging() | REACHABLE | SOURCE | TorrentEngine.java:992 (switchPowerReceiver), :1027 (checkPauseTorrents); BehaviorSettingsFragment.java:102 display. Definition :461. |
| 19 | SettingsRepositoryImpl.onlyCharging(boolean) | REACHABLE | SOURCE | BehaviorSettingsFragment.java:206 (onPreferenceChange). Definition :467. |
| 20 | SettingsRepositoryImpl.playSoundNotify() | UNREACHABLE closed_by_api_level | INFERRED | Definition :290. ONLY printed call sites: AppearanceSettingsFragment.java:133, inside initLegacyNotifySettings (gate :118-119); and TorrentNotifier.java:281, inside applyLegacyNotifySettings (early return :276). At API 27 neither statement executes. PROPOSED only, pending saved full-repo grep. |
| 21 | SettingsRepositoryImpl.playSoundNotify(boolean) | UNREACHABLE closed_by_api_level | INFERRED | Definition :296. ONLY printed call site: AppearanceSettingsFragment.java:241 (onPreferenceChange branch); that branch can fire only if the listener was bound, and it is bound only inside initLegacyNotifySettings (:134), gated at SDK < O (:118-119). At API 27 the branch never fires. PROPOSED only, pending saved full-repo grep. |
| 22 | SettingsRepositoryImpl.portRangeFirst() | REACHABLE | SOURCE | readSessionSettings:221; TorrentEngine.java:1236 (setRandomPortRange), :1550 (handleSettingsChanged); NetworkSettingsFragment.java:162 display. Definition :539. |
| 23 | SettingsRepositoryImpl.portRangeFirst(int) | REACHABLE | SOURCE | NetworkSettingsFragment.java:309 (onPreferenceChange). Definition :545. |
| 24 | SettingsRepositoryImpl.portRangeSecond() | REACHABLE | SOURCE | readSessionSettings:222; TorrentEngine.java:1237 (setRandomPortRange), :1551 (handleSettingsChanged); NetworkSettingsFragment.java:172 display. Definition :552. |
| 25 | SettingsRepositoryImpl.portRangeSecond(int) | REACHABLE | SOURCE | NetworkSettingsFragment.java:316 (onPreferenceChange). Definition :558. |
| 26 | SettingsRepositoryImpl.posixDiskIo() | REACHABLE | SOURCE | readSessionSettings:241; StorageSettingsFragment.java:203 display. Definition :812. |
| 27 | SettingsRepositoryImpl.posixDiskIo(boolean) | REACHABLE | SOURCE | StorageSettingsFragment.java:289 (onPreferenceChange). Definition :818. |
| 28 | SettingsRepositoryImpl.proxyAddress() | REACHABLE | SOURCE | readSessionSettings:244; TorrentEngine.java:1098 (setProxy); ProxySettingsFragment.java:115 display. Definition :1007. |
| 29 | SettingsRepositoryImpl.proxyAddress(String) | REACHABLE | SOURCE | ProxySettingsFragment.java:223 (onPreferenceChange). Definition :1013. |
| 30 | SettingsRepositoryImpl.proxyLogin() | REACHABLE | SOURCE | readSessionSettings:248; TorrentEngine.java:1102 (setProxy); ProxySettingsFragment.java:154 display. Definition :1059. |
| 31 | SettingsRepositoryImpl.proxyLogin(String) | REACHABLE | SOURCE | ProxySettingsFragment.java:227 (onPreferenceChange). Definition :1065. |
| 32 | SettingsRepositoryImpl.proxyPassword() | REACHABLE | SOURCE | readSessionSettings:249; TorrentEngine.java:1103 (setProxy); ProxySettingsFragment.java:163 display. Definition :1072. |
| 33 | SettingsRepositoryImpl.proxyPassword(String) | REACHABLE | SOURCE | ProxySettingsFragment.java:231 (onPreferenceChange). Definition :1078. |
| 34 | SettingsRepositoryImpl.proxyPeersToo() | REACHABLE | SOURCE | readSessionSettings:246; TorrentEngine.java:1100 (setProxy); ProxySettingsFragment.java:138 display. Definition :1033. |
| 35 | SettingsRepositoryImpl.proxyPeersToo(boolean) | REACHABLE | SOURCE | ProxySettingsFragment.java:237 (onPreferenceChange). Definition :1039. |
| 36 | SettingsRepositoryImpl.proxyPort() | REACHABLE | SOURCE | readSessionSettings:245; TorrentEngine.java:1099 (setProxy); ProxySettingsFragment.java:126 display. Definition :1020. |
| 37 | SettingsRepositoryImpl.proxyPort(int) | REACHABLE | SOURCE | ProxySettingsFragment.java:218 (onPreferenceChange). Definition :1026. |
| 38 | SettingsRepositoryImpl.proxyRequiresAuth() | REACHABLE | SOURCE | readSessionSettings:247; TorrentEngine.java:1101 (setProxy); ProxySettingsFragment.java:146 display. Definition :1046. |
| 39 | SettingsRepositoryImpl.proxyRequiresAuth(boolean) | REACHABLE | SOURCE | ProxySettingsFragment.java:240 (onPreferenceChange). Definition :1052. |
| 40 | SettingsRepositoryImpl.proxyType() | REACHABLE | SOURCE | readSessionSettings:243; TorrentEngine.java:1097 (setProxy); ProxySettingsFragment.java:106 display. Definition :994. Setter is batch 46 row 1. |

## Counts

- REACHABLE proposed: 36 (SOURCE 35 / INFERRED 1: row 17)
- UNREACHABLE proposed: 4 (rows 15, 16, 20, 21 — all closed_by_api_level, all INFERRED)
- OPEN: 0
- Total: 40. 0 rows verified for merge.

## Still owed before merge

1. Saved full-repo grep (rule F/C5, class-name based) for notifySound / playSoundNotify
   callers: the 4 UNREACHABLE rows flip to REACHABLE if any non-gated caller is found.
   The two gated sites are printed evidence, not absence, but the grep is still required
   because the printed corpus this pass is 16 files, not the whole repo.
2. Printed launcher → TorrentService step and Settings-navigation step (strict-entry caveat).
3. Fresh print of RepositoryHelper.java (singleton construction lead).
4. Merger decisions (recorded, not decided): interface-dispatch vs per-row confirmed_by
   (batches 43-46 must match); strict-entry rule; API-gate reading (batches 44/45/47 must match).
5. Main-agent spot-check 1 in 5, py_compile, build, Mac build/C1 — all not run, never
   claimed passed.

## Scope

Batch 45 only in this file. LibreTorrent labels only, branch work-2026-10-31 only,
no other batch/app, no device replay, no Aegis, no push, no graph edits.
