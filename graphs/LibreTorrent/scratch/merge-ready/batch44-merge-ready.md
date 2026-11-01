# LibreTorrent batch 44 — MERGE-READY — UNVERIFIED

- Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only (never main, never result).
- Membership: exactly the 40 rows of batch 44 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
  (git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92; local copy
  ~/workspace/agent27-plan.tsv; plan extract saved at ~/workspace/b444546-src/batch44_plan.tsv).
  All 40 rows are SettingsRepositoryImpl methods, all plan status TODO_CANDIDATE_REACHABLE
  (generator candidates, not evidence).
- Status: **UNVERIFIED merge-ready part. NOT verified for merge. NOT pushed.**
  Pushes are held until verified and merged to [L]. No edit to graph_def.py, out/,
  PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.
- Prior proposal (~/workspace/libretorrent-batch44-proposal.md, 21/0/19) was used as a
  lead list only. Every row below was re-judged against source freshly fetched in this
  pass. Changes vs that proposal: rows 5, 7, 9, 11, 13, 34, 36, 38, 40 OPEN → REACHABLE
  (newly printed setter call sites, see table); rows 17, 18, 19, 20 OPEN → UNREACHABLE
  closed_by_api_level (TorrentNotifier + Appearance fragment now freshly printed, both
  gated — see rows 17–20); rows 6, 8 REACHABLE INFERRED → REACHABLE SOURCE (fresh Utils
  bodies print the getter calls). Rows 22, 24, 26, 28, 30, 32 stay OPEN.
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
- TorrentEngine.java — 1,658 lines (pref = RepositoryHelper.getSettingsRepository :133;
  readSessionSettings :139; observeSettingsChanged subscription :240-241; keepAlive :276;
  ipFilteringFile :1048/:1556/:1564; handleSettingsChanged :1456-1652).
- TorrentService.java — 525 lines (observeSettingsChanged subscription :125-126;
  setFilterAndSorting :137-140; foregroundNotifyCombinedPauseButton :273/:325/:361).
- Utils.java — 926 lines (getForegroundNotifyFilter :873-891, reads
  pref.foregroundNotifyStatusFilter() at :877; getForegroundNotifySorting :892-911, reads
  pref.foregroundNotifySorting() at :896; showManageAllFilesWarningDialog :699-711).
- TorrentNotifier.java — 294 lines (applyLegacyNotifySettings :275-291, early return
  `SDK_INT >= O` at :276; ledIndicatorNotify :289, ledIndicatorColorNotify :290).
- FeedSettingsFragment.java — 163 lines (display :101/:108, listeners bound :102/:109,
  onPreferenceChange :155/:158).
- LimitationsSettingsFragment.java — 257 lines (onPreferenceChange setters :184/:216/:223/:230).
- NetworkSettingsFragment.java — 414 lines (ipFilteringFile display :205, click listener
  :213-214 → fileChooseDialog :284 → fileChoose.launch :296 → result handler :390).
- BehaviorSettingsFragment.java — 285 lines (keepAlive display :81, listener bound :82,
  onPreferenceChange :229).
- AppearanceSettingsFragment.java — 271 lines (ungated onCreate bindings :83-115;
  SDK < O gate at :118-119 → initLegacyNotifySettings :128-192, with ledIndicator
  display :173, ledIndicatorColor display :180, listener bindings :175/:182;
  onPreferenceChange :253/:256/:259 ungated branches, :244/:250 gated-listener branches).
- StorageSettingsFragment.java, ProxySettingsFragment.java, SchedulingSettingsFragment.java,
  StreamingSettingsFragment.java, LogSettingsFragment.java, AddTorrentViewModel.java — also
  freshly fetched and grepped in this pass (no batch-44 setter call site found in them;
  see OPEN rows). RepositoryHelper.java was NOT freshly fetched in this pass: the claim
  that getSettingsRepository() returns the singleton `new SettingsRepositoryImpl` rests
  on the local copy ~/workspace/agent9/src/RepositoryHelper.java (:61-64) — flagged here,
  not silently carried (see confirmed_by convention below).

## Shared trunks (printed fresh)

- T-E (engine): TorrentEngine.<init> :133/:139 → readSessionSettings() :212-261, which
  internally calls maxConnections :215, maxActiveDownloads :218, maxActiveUploads :219,
  maxActiveTorrents :220, logging :251, logSessionFilter :253, logDhtFilter :254,
  logPeerFilter :255, logPortmapFilter :256, logTorrentFilter :257. TorrentEngine.start
  subscribes pref.observeSettingsChanged() (:240-241). handleSettingsChanged is key-guarded:
  each getter below runs only when its own preference key changes — that is the route's
  dispatch condition, not a project GATE; labels are unaffected by it.
- T-S (service): TorrentService init subscribes pref.observeSettingsChanged() (:125-126);
  setFilterAndSorting (:137-140) passes pref to Utils.getForegroundNotifyFilter /
  getForegroundNotifySorting, whose bodies are now freshly printed (Utils :877/:896).
- T-F (fragments): section fragments bind onPreferenceChange listeners in ungated
  onCreate for every setter row marked REACHABLE below, EXCEPT the legacy-notify rows
  (17-20), whose listeners/bindings sit only inside the SDK < O initLegacy block.

## Conventions recorded per row, NOT decided

- confirmed_by, per-row (this file): SOURCE = a printed app-code line naming the method
  (including a pref.* call site and an internal readSessionSettings call from the
  REACHABLE readSessionSettings route); INFERRED = the route crosses unprinted
  framework/library/Rx dispatch (observeSettingsChanged lambdas, rows 14-16) or rests
  on a printed gate with no ungated caller (UNREACHABLE rows, all INFERRED).
  Alternative convention, recorded not decided: every `pref` variable in the fetched
  files is typed to the SettingsRepository INTERFACE (TorrentEngine :104,
  TorrentService :82, TorrentNotifier :63, Utils :167/:639/:875/:894), and only the
  (not freshly fetched) RepositoryHelper local copy shows the singleton is a
  SettingsRepositoryImpl. Under an interface-dispatch convention, all SOURCE rows in
  this file would read INFERRED; labels are unaffected. Batch 43 merge-ready used
  SOURCE for the same pref.* pattern; batches 45/46 proposals used INFERRED. The
  merger must pick one convention and apply it across batches 43-46.
- Strict-entry: routes anchor at TorrentEngine/TorrentService/ViewModels/fragments, not
  at a printed launcher step, and fragment-anchored rows assume the fragment is
  displayed from Settings (that step was NOT printed). Under a strict printed-launcher
  rule all REACHABLE rows revert to OPEN. This does not change the UNREACHABLE rows
  (they have no route at any entry) or the OPEN rows.
- Lambda $ numbering (rows 14-16): matched by plan JVM descriptor, not by source order
  alone and not bytecode-verified: $0 (FlowableEmitter, SharedPreferences, String) is
  the OnSharedPreferenceChangeListener lambda (captured emitter, takes prefs + key);
  $1 (OnSharedPreferenceChangeListener) is the Disposables.fromAction unregister lambda
  (captures the listener); $2 (FlowableEmitter) is the Flowable.create emitter lambda.
  All three stand or fall with observeSettingsChanged (batch 45 row 17).
- Method-vs-call-site rule for the API-gated rows (17-20): applied exactly as in batch 45
  (notifySound/playSoundNotify). A method is closed_by_api_level here only because its
  ONLY printed call statements never execute at API 27 — either they sit inside a
  method that returns early at SDK >= O (TorrentNotifier :276, before :289-290), or
  inside a block that only runs at SDK < O (Appearance initLegacy, gate :118-119), or
  in an onPreferenceChange branch whose listener is bound only inside that gated block.
  This is not the "body returns early" case: these methods' own bodies are ordinary
  getters/setters; it is their call statements that are unreachable at API 27.
- Preference-persistence note (OPEN setters, rows 22/24/26/28/30/32): AndroidX preferences
  persist their own toggled values directly to SharedPreferences via the framework, so a
  changed preference value does NOT imply the app's programmatic setter ran. Only a
  printed programmatic setter call site counts as a route; none was printed for these six.

## Rows (plan order)

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.feedRemoveDuplicates(boolean) | REACHABLE | SOURCE | FeedSettingsFragment.java:158 (onPreferenceChange, pref_key_feed_remove_duplicates branch): `pref.feedRemoveDuplicates((boolean)newValue)`; listener bound ungated at :109. Definition :1260. Getter is batch 43 row 40; display also at Feed :108. |
| 2 | SettingsRepositoryImpl.feedStartTorrents() | REACHABLE | SOURCE | FeedSettingsFragment.java:101: `startTorrents.setChecked(pref.feedStartTorrents())` in onCreate display binding. Definition :1241. |
| 3 | SettingsRepositoryImpl.feedStartTorrents(boolean) | REACHABLE | SOURCE | FeedSettingsFragment.java:155 (onPreferenceChange, pref_key_feed_start_torrents branch); listener bound ungated at :102. Definition :1247. |
| 4 | SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton() | REACHABLE | SOURCE | TorrentService.java:273, :325, :361: `pref.foregroundNotifyCombinedPauseButton()`; also AppearanceSettingsFragment.java:114 display binding. Definition :401. |
| 5 | SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton(boolean) | REACHABLE | SOURCE | AppearanceSettingsFragment.java:259 (onPreferenceChange, pref_key_foreground_notify_combined_pause_button branch); listener bound in ungated onCreate at :115. Definition :391. UPGRADED vs prior proposal (was OPEN): this call site was not printed in that pass. |
| 6 | SettingsRepositoryImpl.foregroundNotifySorting() | REACHABLE | SOURCE | Utils.java:896 inside getForegroundNotifySorting (:892-911): `String val = pref.foregroundNotifySorting();`, reached from TorrentService.java:139 setFilterAndSorting; also AppearanceSettingsFragment.java:106 display binding. Definition :373. UPGRADED confirmed_by vs prior proposal (was INFERRED): Utils body is now freshly printed. |
| 7 | SettingsRepositoryImpl.foregroundNotifySorting(String) | REACHABLE | SOURCE | AppearanceSettingsFragment.java:256 (onPreferenceChange, pref_key_foreground_notify_sorting branch); listener bound in ungated onCreate at :108. Definition :381. UPGRADED vs prior proposal (was OPEN). |
| 8 | SettingsRepositoryImpl.foregroundNotifyStatusFilter() | REACHABLE | SOURCE | Utils.java:877 inside getForegroundNotifyFilter (:873-891): `String val = pref.foregroundNotifyStatusFilter();`, reached from TorrentService.java:138 setFilterAndSorting; also AppearanceSettingsFragment.java:98 display binding. Definition :355. UPGRADED confirmed_by vs prior proposal (was INFERRED): Utils body is now freshly printed. |
| 9 | SettingsRepositoryImpl.foregroundNotifyStatusFilter(String) | REACHABLE | SOURCE | AppearanceSettingsFragment.java:253 (onPreferenceChange, pref_key_foreground_notify_status_filter branch); listener bound in ungated onCreate at :100. Definition :363. UPGRADED vs prior proposal (was OPEN). |
| 10 | SettingsRepositoryImpl.ipFilteringFile() | REACHABLE | SOURCE | TorrentEngine.java:1048, :1556, :1564: `pref.ipFilteringFile()`; also NetworkSettingsFragment.java:205 display. Definition :682. |
| 11 | SettingsRepositoryImpl.ipFilteringFile(String) | REACHABLE | SOURCE | NetworkSettingsFragment.java:390 (fileChoose result handler): `pref.ipFilteringFile(path.toString())`; launcher launched by fileChooseDialog :284-296, called from the click listener registered in ungated onCreate at :213-214. Definition :688. UPGRADED vs prior proposal (was OPEN). |
| 12 | SettingsRepositoryImpl.keepAlive() | REACHABLE | SOURCE | TorrentEngine.java:276 (requestStop): `if (pref.keepAlive()) return;`; also BehaviorSettingsFragment.java:81 display. Definition :422. |
| 13 | SettingsRepositoryImpl.keepAlive(boolean) | REACHABLE | SOURCE | BehaviorSettingsFragment.java:229 (onPreferenceChange, pref_key_keep_alive branch); listener bound in ungated onCreate at :82. Definition :428. UPGRADED vs prior proposal (was OPEN). |
| 14 | SettingsRepositoryImpl.lambda$observeSettingsChanged$0 | REACHABLE | INFERRED | Compiler-generated lambda inside observeSettingsChanged (:195-211), descriptor-matched: the OnSharedPreferenceChangeListener lambda `(sharedPreferences, key) -> emitter.onNext(key)` (captured emitter). Runs on a preference change once observeSettingsChanged is subscribed — printed subscribers TorrentEngine.java:240-241 and TorrentService.java:125-126. SharedPreferences listener dispatch not printed from fw_src, hence INFERRED. Numbering by descriptor; confirm against bytecode at merge if disputed. |
| 15 | SettingsRepositoryImpl.lambda$observeSettingsChanged$1 | REACHABLE | INFERRED | Compiler-generated lambda inside observeSettingsChanged (:195-211), descriptor-matched: the Disposables.fromAction unregister lambda capturing the listener. Runs on disposal of the subscriptions at TorrentEngine.java:240-241 / TorrentService.java:125-126. Rx/Disposable dispatch not printed, hence INFERRED. |
| 16 | SettingsRepositoryImpl.lambda$observeSettingsChanged$2 | REACHABLE | INFERRED | Compiler-generated lambda inside observeSettingsChanged (:195-211), descriptor-matched: the Flowable.create emitter lambda. Runs on subscription at TorrentEngine.java:240-241 / TorrentService.java:125-126. Rx dispatch not printed, hence INFERRED. These three lambdas stand or fall with observeSettingsChanged (batch 45 row 17). |
| 17 | SettingsRepositoryImpl.ledIndicatorColorNotify() | UNREACHABLE closed_by_api_level | INFERRED | Definition :342. ONLY printed call sites in the 16 freshly fetched files: AppearanceSettingsFragment.java:180, inside initLegacyNotifySettings, which runs only at SDK < O (gate :118-119); and TorrentNotifier.java:290, inside applyLegacyNotifySettings, which returns early at SDK >= O (:276) before reaching :290. At standard API 27 neither statement executes. CHANGED vs prior proposal (was OPEN: TorrentNotifier was not printed there). PROPOSED only, pending saved full-repo grep: an ungated caller flips this row to REACHABLE. |
| 18 | SettingsRepositoryImpl.ledIndicatorColorNotify(int) | UNREACHABLE closed_by_api_level | INFERRED | Definition :348. ONLY printed call site: AppearanceSettingsFragment.java:250 (onPreferenceChange branch); that branch can fire only if the listener was bound, and it is bound only inside initLegacyNotifySettings (:181), gated at SDK < O (:118-119). At API 27 the branch never fires. CHANGED vs prior proposal (was OPEN). PROPOSED only, pending saved full-repo grep. |
| 19 | SettingsRepositoryImpl.ledIndicatorNotify() | UNREACHABLE closed_by_api_level | INFERRED | Definition :303. ONLY printed call sites: AppearanceSettingsFragment.java:173 (initLegacy, gated :118-119) and TorrentNotifier.java:289 (applyLegacyNotifySettings, early return :276). At API 27 neither statement executes. CHANGED vs prior proposal (was OPEN: TorrentNotifier was not printed there; prior note "likely read by TorrentNotifier" is now confirmed — and gated). PROPOSED only, pending saved full-repo grep. |
| 20 | SettingsRepositoryImpl.ledIndicatorNotify(boolean) | UNREACHABLE closed_by_api_level | INFERRED | Definition :309. ONLY printed call site: AppearanceSettingsFragment.java:244 (onPreferenceChange branch); listener bound only inside initLegacyNotifySettings (:174), gated at SDK < O (:118-119). At API 27 the branch never fires. CHANGED vs prior proposal (was OPEN). PROPOSED only, pending saved full-repo grep. |
| 21 | SettingsRepositoryImpl.logDhtFilter() | REACHABLE | SOURCE | TorrentEngine.java:1624 (handleSettingsChanged) and internally readSessionSettings:254. Definition :1345. |
| 22 | SettingsRepositoryImpl.logDhtFilter(boolean) | OPEN | — | Definition :1351. No setter call site in any of the 16 freshly fetched files; LogSettingsFragment prints only maxLogSize (:69/:95). Framework persistence writes the toggled value directly, not via this setter. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 23 | SettingsRepositoryImpl.logPeerFilter() | REACHABLE | SOURCE | TorrentEngine.java:1629 and internally readSessionSettings:255. Definition :1358. |
| 24 | SettingsRepositoryImpl.logPeerFilter(boolean) | OPEN | — | Definition :1364. No setter call site in the fresh corpus. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 25 | SettingsRepositoryImpl.logPortmapFilter() | REACHABLE | SOURCE | TorrentEngine.java:1634 and internally readSessionSettings:256. Definition :1371. |
| 26 | SettingsRepositoryImpl.logPortmapFilter(boolean) | OPEN | — | Definition :1377. No setter call site in the fresh corpus. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 27 | SettingsRepositoryImpl.logSessionFilter() | REACHABLE | SOURCE | TorrentEngine.java:1619 and internally readSessionSettings:253. Definition :1332. |
| 28 | SettingsRepositoryImpl.logSessionFilter(boolean) | OPEN | — | Definition :1338. No setter call site in the fresh corpus. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 29 | SettingsRepositoryImpl.logTorrentFilter() | REACHABLE | SOURCE | TorrentEngine.java:1639 and internally readSessionSettings:257. Definition :1384. |
| 30 | SettingsRepositoryImpl.logTorrentFilter(boolean) | OPEN | — | Definition :1390. No setter call site in the fresh corpus. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 31 | SettingsRepositoryImpl.logging() | REACHABLE | SOURCE | TorrentEngine.java:1614 and internally readSessionSettings:251. Definition :1306. |
| 32 | SettingsRepositoryImpl.logging(boolean) | OPEN | — | Definition :1312. No setter call site in the fresh corpus. Pending saved full-repo grep; NOT UNREACHABLE on absence. |
| 33 | SettingsRepositoryImpl.maxActiveDownloads() | REACHABLE | SOURCE | TorrentEngine.java:1497 and internally readSessionSettings:218. Definition :903. |
| 34 | SettingsRepositoryImpl.maxActiveDownloads(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:216 (onPreferenceChange, pref_key_max_active_downloads branch); listener bound in ungated onCreate at :131. Definition :909. UPGRADED vs prior proposal (was OPEN). |
| 35 | SettingsRepositoryImpl.maxActiveTorrents() | REACHABLE | SOURCE | TorrentEngine.java:1507 and internally readSessionSettings:220. Definition :916. |
| 36 | SettingsRepositoryImpl.maxActiveTorrents(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:230 (onPreferenceChange, pref_key_max_active_torrents branch); listener bound in ungated onCreate at :142. Definition :922. UPGRADED vs prior proposal (was OPEN). |
| 37 | SettingsRepositoryImpl.maxActiveUploads() | REACHABLE | SOURCE | TorrentEngine.java:1502 and internally readSessionSettings:219. Definition :890. |
| 38 | SettingsRepositoryImpl.maxActiveUploads(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:223 (onPreferenceChange, pref_key_max_active_uploads branch); listener bound in ungated onCreate at :120. Definition :896. UPGRADED vs prior proposal (was OPEN). |
| 39 | SettingsRepositoryImpl.maxConnections() | REACHABLE | SOURCE | TorrentEngine.java:1485 and internally readSessionSettings:215. Definition :851. |
| 40 | SettingsRepositoryImpl.maxConnections(int) | REACHABLE | SOURCE | LimitationsSettingsFragment.java:184 (onPreferenceChange, pref_key_max_connections branch); listener bound in ungated onCreate at :102. Definition :857. UPGRADED vs prior proposal (was OPEN). |

## Counts

- REACHABLE proposed: 30 (SOURCE 27 / INFERRED 3: rows 14, 15, 16)
- UNREACHABLE proposed: 4 (rows 17, 18, 19, 20 — all closed_by_api_level, all INFERRED)
- OPEN: 6 (rows 22, 24, 26, 28, 30, 32 — the six log/logging setters)
- Total: 40. 0 rows verified for merge.

## Cross-batch notes for the merger (leads only, not verdicts for other batches)

- Batch 47 rows 1-2 (vibrationNotify()/vibrationNotify(boolean)) sit in the SAME gated
  pattern as rows 17-20 here: getter call sites TorrentNotifier.java:288 (inside
  applyLegacyNotifySettings, early return :276) and AppearanceSettingsFragment.java:187
  (inside initLegacyNotifySettings, gate :118-119); setter call site
  AppearanceSettingsFragment.java:247, listener bound only in initLegacy (:188). If the
  merger adopts the closed_by_api_level reading used here and in batch 45, those two
  batch-47 rows flip the same way — but that decision belongs to the batch-47 file/merger,
  not this file.
- Batch 45 rows 15, 16, 20, 21 (notifySound/playSoundNotify) use the identical gate
  (Appearance initLegacy + TorrentNotifier applyLegacyNotifySettings); rows 17-20 here
  are consistent with them.

## Still owed before merge

1. Saved full-repo grep for all 4 UNREACHABLE-proposed rows and all 6 OPEN rows. Any
   ungated caller flips an UNREACHABLE row to REACHABLE; any setter caller flips an OPEN
   row to REACHABLE. No OPEN row may be flipped to UNREACHABLE without that grep.
2. Printed launcher → TorrentService step and Settings-navigation step (strict-entry caveat).
3. Fresh print of RepositoryHelper.java (singleton construction lead, see above).
4. Bytecode confirmation of the observeSettingsChanged lambda $ numbering if disputed.
5. Merger decisions (recorded, not decided): interface-dispatch vs per-row confirmed_by
   (batches 43-46 must match); strict-entry rule; API-gate reading (batches 44/45/47 must match).
6. Main-agent spot-check 1 in 5, py_compile, build, Mac build/C1 — all not run, never
   claimed passed.

## Scope

Batches 44 only in this file. LibreTorrent labels only, branch work-2026-10-31 only,
no other batch/app, no device replay, no Aegis, no push, no graph edits.
