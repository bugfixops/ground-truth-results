# LibreTorrent batch 46 — MERGE-READY — UNVERIFIED

- Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only (never main, never result).
- Membership: exactly the 40 rows of batch 46 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
  (git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92; local copy
  ~/workspace/agent27-plan.tsv; plan extract saved at ~/workspace/b444546-src/batch46_plan.tsv).
  All 40 rows are SettingsRepositoryImpl methods, all plan status TODO_CANDIDATE_REACHABLE
  (generator candidates, not evidence). Batch 46 starts with the proxyType(int) setter
  (the proxyType() getter is batch 45 row 40) and then runs through readSessionSettings
  and the remaining settings pairs.
- Status: **UNVERIFIED merge-ready part. NOT verified for merge. NOT pushed.**
  Pushes are held until verified and merged to [L]. No edit to graph_def.py, out/,
  PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.
- Prior proposal (~/workspace/libretorrent-batch46-proposal.md, 40/0/0) was used as a
  lead list only. Every row below was re-judged against source freshly fetched in this
  pass. Labels CHANGED vs that proposal: 38/2/0 (rows 21-22 flip REACHABLE →
  UNREACHABLE closed_by_api_level — the prior proposal cited Utils :706/:711 without
  analysing the gate; the gate analysis is in rows 21-22 below). The evidence base is
  upgraded from local copies to fresh connector fetches for every cited file, and
  confirmed_by changes from all-INFERRED to per-row SOURCE (see convention note —
  labels unaffected apart from rows 21-22).
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

- SettingsRepositoryImpl.java — 1,435 lines (all definitions below; readSessionSettings
  :212-261).
- TorrentEngine.java — 1,658 lines (pref :104/:133; readSessionSettings :139;
  handleAutoStop :144; switchConnectionReceiver :1010; checkPauseTorrents :1027-1028;
  startStreamingServer :1066-1067; addTorrentSync :1185; onTorrentAdded :1273/:1275;
  onTorrentMetadataLoaded :1431-1432; onNatError :1395; handleSettingsChanged :1456-1652).
- ProxySettingsFragment.java — 247 lines (onPreferenceChange setter :210).
- FeedSettingsFragment.java — 163 lines (refreshFeedsInterval display :67, :133;
  setter :141, feeding Scheduler.runPeriodicalRefreshFeeds at :134).
- StorageSettingsFragment.java — 296 lines (displays :95/:142/:149;
  directory-picker result handler :264/:267; onPreferenceChange :285).
- SchedulingSettingsFragment.java — 242 lines (displays :86/:93/:100/:107, plus
  re-reads :199/:212; onPreferenceChange :222/:228/:234/:237, with
  Scheduler.setStartAppAlarm :223 / setStopAppAlarm :229).
- NetworkSettingsFragment.java — 414 lines (displays :153/:223/:267/:274;
  onPreferenceChange :335/:338/:352/:355).
- BehaviorSettingsFragment.java — 285 lines (displays :88/:136;
  onPreferenceChange :223/:232).
- StreamingSettingsFragment.java — 118 lines (displays :68/:78;
  onPreferenceChange :102/:108).
- AppearanceSettingsFragment.java — 271 lines (theme display :83, setter :229;
  torrentFinishNotify display :91, setter :238; both listeners bound in ungated onCreate
  at :85/:92 — NOT inside the SDK < O initLegacy block, gate :118-119).
- Utils.java — 926 lines (isNetworkTypeAllowed :164-169, reads
  pref.unmeteredConnectionsOnly() at :169; getThemePreference :370-371, returns
  `...theme()`; getTorrentDownloadPath :638-640, reads pref.saveTorrentsIn();
  showManageAllFilesWarningDialog :699-711, reads pref.showManageAllFilesWarningDialog()
  at :706 and calls the setter at :711).
- TorrentNotifier.java — 294 lines (makeTorrentFinishedNotify :212-213, reads
  pref.torrentFinishNotify() at :213).
- AddTorrentViewModel.java — 574 lines (saveTorrentsIn read at :145).
- TorrentService.java, LimitationsSettingsFragment.java, LogSettingsFragment.java — also
  freshly fetched and grepped in this pass (no batch-46 call site found in them beyond
  the rows cited; TorrentService init subscribes observeSettingsChanged, batch 45 row 17).
- RepositoryHelper.java was NOT freshly fetched in this pass: the claim that
  getSettingsRepository() returns the singleton `new SettingsRepositoryImpl` rests on
  the local copy ~/workspace/agent9/src/RepositoryHelper.java (:61-64) — flagged here
  (see confirmed_by convention below).

## Shared trunks (printed fresh)

- Engine trunk: TorrentService.onCreate → TorrentEngine.getInstance → TorrentEngine.<init>
  :133/:139 → readSessionSettings() :212-261, which internally calls
  seedingOutgoingConnections :232, useRandomPort :233, validateHttpsTrackers :240,
  posixDiskIo :241 (batch 45 row 26), proxyType :243 (batch 45 row 40), plus batch-44/45
  getters. handleSettingsChanged (:1456-1652) is key-guarded per preference key — that
  is the route's dispatch condition, not a project GATE; labels are unaffected by it.
- Settings-UI trunk: user opens Settings → section fragment → onPreferenceChange
  (standard callback, listeners bound in ungated onCreate for every setter row marked
  REACHABLE below) → setter rows. The fragment-display step (Settings navigation) was
  NOT printed — see strict-entry caveat.

## Conventions recorded per row, NOT decided

- confirmed_by, per-row (this file): SOURCE = a printed app-code line naming the method.
  This DIFFERS from the prior batch-46 proposal, which marked every row INFERRED on the
  ground that all `pref` variables are typed to the SettingsRepository interface
  (TorrentEngine :104, Utils :167/:639/:703) and only the (not freshly fetched)
  RepositoryHelper local copy shows the singleton is a SettingsRepositoryImpl. Under
  that interface-dispatch convention, all SOURCE rows here would read INFERRED; labels
  are unaffected. Batch 43 merge-ready used SOURCE for the same pref.* pattern. The
  merger must pick one convention and apply it across batches 43-46. This file uses
  SOURCE, consistent with batch 43 and batches 44-45.
- Strict-entry: routes anchor at TorrentEngine/Utils/fragments, not at a printed launcher
  step, and fragment-anchored rows assume the fragment is displayed from Settings (that
  step was NOT printed). Under a strict printed-launcher rule all REACHABLE rows revert
  to OPEN.
- API-gate reading (rows 21-22, and why torrentFinishNotify rows 33/34 are NOT gated):
  torrentFinishNotify is NOT gated — its Appearance fragment calls at :91/:238 sit
  outside the SDK < O initLegacyNotifySettings block (gate :118-119), and the notifier
  call at :213 is ungated. The showManageAllFilesWarningDialog rows (21/22) ARE gated,
  by short-circuit, not just by the early return: Utils.showManageAllFilesWarningDialog
  :704-707 is `if (SDK_INT < R || hasPermission || !pref.showManageAllFilesWarningDialog())
  return;`. At standard API 27, the first disjunct SDK < R (27 < 30) is TRUE, so Java
  `||` short-circuits: the :706 getter is not even evaluated, and the :711 setter
  (after the return) is never reached. Both rows' only printed call sites are therefore
  dead at API 27, exactly as in batch 44 rows 17-20 / batch 45 rows 15/16/20/21 — hence
  closed_by_api_level proposed, pending a saved full-repo grep (an ungated caller flips
  either row to REACHABLE). This is consistent with the batch 73-74 lead that the
  ManageAllFilesWarningDialog rows on this same Utils method are closed_by_api_level
  candidates. Note the method itself (Utils.showManageAllFilesWarningDialog) still RUNS
  at API 27 via its MainActivity:180 caller (batch 73-74 print, not re-fetched here);
  it is the two pref.* call statements inside it that never execute at API 27.

## Rows (plan order)

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.proxyType(int) | REACHABLE | SOURCE | ProxySettingsFragment.java:210 (onPreferenceChange). Definition :1000. Getter is batch 45 row 40. |
| 2 | SettingsRepositoryImpl.readSessionSettings() | REACHABLE | SOURCE | TorrentEngine.java:139 (`session.setSettings(pref.readSessionSettings(), false)` in <init>). Definition :212-260. Internally calls batch 45/46 getters: maxUploadSpeedLimit :214, maxConnectionsPerTorrent :216, maxUploadsPerTorrent :217, portRangeFirst :221, portRangeSecond :222, seedingOutgoingConnections :232, useRandomPort :233, validateHttpsTrackers :240, posixDiskIo :241, proxyType :243, proxyAddress :244, proxyPort :245, proxyPeersToo :246, proxyRequiresAuth :247, proxyLogin :248, proxyPassword :249, maxLogSize :252. |
| 3 | SettingsRepositoryImpl.refreshFeedsInterval() | REACHABLE | SOURCE | FeedSettingsFragment.java:67 (display) and :133 (onPreferenceChange, feeding Scheduler.runPeriodicalRefreshFeeds(context, interval) at :134). Definition :1202. |
| 4 | SettingsRepositoryImpl.refreshFeedsInterval(long) | REACHABLE | SOURCE | FeedSettingsFragment.java:141 (onPreferenceChange). Definition :1208. |
| 5 | SettingsRepositoryImpl.saveTorrentFiles() | REACHABLE | SOURCE | TorrentEngine.java:1273 (onTorrentAdded), :1431 (onTorrentMetadataLoaded); StorageSettingsFragment.java:142 display. Definition :747. |
| 6 | SettingsRepositoryImpl.saveTorrentFiles(boolean) | REACHABLE | SOURCE | StorageSettingsFragment.java:285 (onPreferenceChange). Definition :753. |
| 7 | SettingsRepositoryImpl.saveTorrentFilesIn() | REACHABLE | SOURCE | TorrentEngine.java:1275 (onTorrentAdded), :1432 (onTorrentMetadataLoaded); StorageSettingsFragment.java:149 display. Definition :760. |
| 8 | SettingsRepositoryImpl.saveTorrentFilesIn(String) | REACHABLE | SOURCE | StorageSettingsFragment.java:264 (directory-picker result handler). Definition :766. |
| 9 | SettingsRepositoryImpl.saveTorrentsIn() | REACHABLE | SOURCE | TorrentEngine.java:1185 (addTorrentSync); Utils.java:640 (getTorrentDownloadPath); AddTorrentViewModel.java:145; StorageSettingsFragment.java:95 display. Definition :708. |
| 10 | SettingsRepositoryImpl.saveTorrentsIn(String) | REACHABLE | SOURCE | StorageSettingsFragment.java:267 (directory-picker result handler). Definition :714. |
| 11 | SettingsRepositoryImpl.schedulingRunOnlyOnce() | REACHABLE | SOURCE | SchedulingSettingsFragment.java:100 display. Definition :1150. |
| 12 | SettingsRepositoryImpl.schedulingRunOnlyOnce(boolean) | REACHABLE | SOURCE | SchedulingSettingsFragment.java:234 (onPreferenceChange). Definition :1156. |
| 13 | SettingsRepositoryImpl.schedulingShutdownTime() | REACHABLE | SOURCE | SchedulingSettingsFragment.java:93 display. Definition :1137. |
| 14 | SettingsRepositoryImpl.schedulingShutdownTime(int) | REACHABLE | SOURCE | SchedulingSettingsFragment.java:228 (onPreferenceChange, then Scheduler.setStopAppAlarm). Definition :1143. |
| 15 | SettingsRepositoryImpl.schedulingStartTime() | REACHABLE | SOURCE | SchedulingSettingsFragment.java:86 display, :199 (enable-start branch), and :212 (enable-shutdown branch, re-reads start time — still a call; genuine second call site, not a copy error — do not "fix" without re-printing). Definition :1124. |
| 16 | SettingsRepositoryImpl.schedulingStartTime(int) | REACHABLE | SOURCE | SchedulingSettingsFragment.java:222 (onPreferenceChange, then Scheduler.setStartAppAlarm). Definition :1130. |
| 17 | SettingsRepositoryImpl.schedulingSwitchWiFi() | REACHABLE | SOURCE | SchedulingSettingsFragment.java:107 display. Definition :1163. |
| 18 | SettingsRepositoryImpl.schedulingSwitchWiFi(boolean) | REACHABLE | SOURCE | SchedulingSettingsFragment.java:237 (onPreferenceChange). Definition :1169. |
| 19 | SettingsRepositoryImpl.seedingOutgoingConnections() | REACHABLE | SOURCE | readSessionSettings:232; TorrentEngine.java:1609 (handleSettingsChanged); NetworkSettingsFragment.java:267 display. Definition :942. |
| 20 | SettingsRepositoryImpl.seedingOutgoingConnections(boolean) | REACHABLE | SOURCE | NetworkSettingsFragment.java:352 (onPreferenceChange). Definition :948. |
| 21 | SettingsRepositoryImpl.showManageAllFilesWarningDialog() | UNREACHABLE closed_by_api_level | INFERRED | Definition :1410. ONLY printed call site in the 16 freshly fetched files: Utils.java:706, the third disjunct of the early-return condition at :704-707 (`SDK_INT < R || hasPermission || !pref.showManageAllFilesWarningDialog()`). At standard API 27 the first disjunct is TRUE (27 < 30), so `||` short-circuits and :706 is never evaluated. The enclosing method itself still runs at API 27 (MainActivity:180 caller per the batch 73-74 pass, not re-fetched here) — but this call statement inside it does not execute. CHANGED vs prior proposal (was REACHABLE: gate not analysed there). PROPOSED only, pending saved full-repo grep: an ungated caller flips this row to REACHABLE. |
| 22 | SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean) | UNREACHABLE closed_by_api_level | INFERRED | Definition :1418. ONLY printed call site: Utils.java:711 (showManageAllFilesWarningDialog body: sets `false` once the warning path has run), AFTER the early return at :704-707. At API 27 the return is always taken (SDK < R true), so :711 is never reached. Same enclosing-method anchor caveat as row 21 (MainActivity:180 lead, not re-fetched here). CHANGED vs prior proposal (was REACHABLE: gate not analysed there). PROPOSED only, pending saved full-repo grep. |
| 23 | SettingsRepositoryImpl.showNatErrors() | REACHABLE | SOURCE | TorrentEngine.java:1395 (onNatError); NetworkSettingsFragment.java:223 display. Definition :695. |
| 24 | SettingsRepositoryImpl.showNatErrors(boolean) | REACHABLE | SOURCE | NetworkSettingsFragment.java:335 (onPreferenceChange). Definition :701. |
| 25 | SettingsRepositoryImpl.shutdownDownloadsComplete() | REACHABLE | SOURCE | TorrentEngine.java:144 (handleAutoStop); BehaviorSettingsFragment.java:88 display. Definition :435. |
| 26 | SettingsRepositoryImpl.shutdownDownloadsComplete(boolean) | REACHABLE | SOURCE | BehaviorSettingsFragment.java:232 (onPreferenceChange). Definition :441. |
| 27 | SettingsRepositoryImpl.streamingHostname() | REACHABLE | SOURCE | TorrentEngine.java:1066 (startStreamingServer); StreamingSettingsFragment.java:68 display. Definition :1280. |
| 28 | SettingsRepositoryImpl.streamingHostname(String) | REACHABLE | SOURCE | StreamingSettingsFragment.java:102 (onPreferenceChange). Definition :1286. |
| 29 | SettingsRepositoryImpl.streamingPort() | REACHABLE | SOURCE | TorrentEngine.java:1067 (startStreamingServer); StreamingSettingsFragment.java:78 display. Definition :1293. |
| 30 | SettingsRepositoryImpl.streamingPort(int) | REACHABLE | SOURCE | StreamingSettingsFragment.java:108 (onPreferenceChange). Definition :1299. |
| 31 | SettingsRepositoryImpl.theme() | REACHABLE | SOURCE | Utils.java:371 (getThemePreference returns `...theme()`); AppearanceSettingsFragment.java:83 display. Definition :329. |
| 32 | SettingsRepositoryImpl.theme(int) | REACHABLE | SOURCE | AppearanceSettingsFragment.java:229 (onPreferenceChange); listener bound in ungated onCreate at :85. Definition :335. |
| 33 | SettingsRepositoryImpl.torrentFinishNotify() | REACHABLE | SOURCE | TorrentNotifier.java:213 (makeTorrentFinishedNotify, ungated) and AppearanceSettingsFragment.java:91 display (ungated onCreate). Definition :277. Weakest link, flagged: the caller of makeTorrentFinishedNotify itself was not printed in this pass — but the Appearance :91 call independently supports the getter, so the row does not rest on that link alone. NOT API-gated (see convention note). |
| 34 | SettingsRepositoryImpl.torrentFinishNotify(boolean) | REACHABLE | SOURCE | AppearanceSettingsFragment.java:238 (onPreferenceChange); listener bound in ungated onCreate at :92. Definition :283. |
| 35 | SettingsRepositoryImpl.unmeteredConnectionsOnly() | REACHABLE | SOURCE | TorrentEngine.java:1010 (switchConnectionReceiver), :1028 (checkPauseTorrents); Utils.java:169 (isNetworkTypeAllowed); BehaviorSettingsFragment.java:136 display. Definition :513. |
| 36 | SettingsRepositoryImpl.unmeteredConnectionsOnly(boolean) | REACHABLE | SOURCE | BehaviorSettingsFragment.java:223 (onPreferenceChange). Definition :519. |
| 37 | SettingsRepositoryImpl.useRandomPort() | REACHABLE | SOURCE | readSessionSettings:233; TorrentEngine.java:1546 (handleSettingsChanged, setRandomPortRange(pref.useRandomPort())); NetworkSettingsFragment.java:153 display. Definition :630. |
| 38 | SettingsRepositoryImpl.useRandomPort(boolean) | REACHABLE | SOURCE | NetworkSettingsFragment.java:338 (onPreferenceChange). Definition :636. |
| 39 | SettingsRepositoryImpl.validateHttpsTrackers() | REACHABLE | SOURCE | readSessionSettings:240; TorrentEngine.java:1652 (handleSettingsChanged); NetworkSettingsFragment.java:274 display. Definition :968. |
| 40 | SettingsRepositoryImpl.validateHttpsTrackers(boolean) | REACHABLE | SOURCE | NetworkSettingsFragment.java:355 (onPreferenceChange). Definition :974. |

## Counts

- REACHABLE proposed: 38 (SOURCE 38 / INFERRED 0)
- UNREACHABLE proposed: 2 (rows 21, 22 — both closed_by_api_level, both INFERRED)
- OPEN: 0
- Total: 40. 0 rows verified for merge.

## Still owed before merge

1. Saved full-repo grep for rows 21-22: an ungated caller flips either row to REACHABLE.
2. Printed launcher → TorrentService step and Settings-navigation step (strict-entry caveat).
3. Fresh print of RepositoryHelper.java (singleton construction lead).
4. Fresh print of the MainActivity:180 caller of Utils.showManageAllFilesWarningDialog
   (rows 21-22 enclosing-method lead from the batch 73-74 pass).
5. Merger decision (recorded, not decided): interface-dispatch vs per-row confirmed_by
   (batches 43-46 must match); strict-entry rule; API-gate reading (batches 44/45/46/73-74
   must match on the Utils.showManageAllFilesWarningDialog gate).
5. Main-agent spot-check 1 in 5, py_compile, build, Mac build/C1 — all not run, never
   claimed passed.

## Scope

Batch 46 only in this file. LibreTorrent labels only, branch work-2026-10-31 only,
no other batch/app, no device replay, no Aegis, no push, no graph edits.
