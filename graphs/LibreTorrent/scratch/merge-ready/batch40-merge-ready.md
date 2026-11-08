**REVISION 2026-11-01 (grep-flip re-check, Stream A Phase 1) — UNVERIFIED.** Re-checked row 3 (the batch's sole UNREACHABLE row; it was re-verified, not flipped, in the OPEN-closing pass, which had 0 OPEN rows) against the complete tree: SURVIVED, no label change. Counts UNCHANGED: 39 REACHABLE proposed / 1 UNREACHABLE proposed / 0 OPEN. Grep: `~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt` §G4 (281 main Java files = 252 ruleF + 28 feedparser + NanoHTTPD, plus 20 test/androidTest) — only the :556 call inside `if (false)` and the :570 definition; a private method has no caller outside its file. CAVEAT (disclosed, not hidden): two fresh connector 429s stopped the final ui-subtree listings, so the feedparser files used are the missing-29 worker's branch copies (18/28 byte-identical to independently printed b1-src copies) and NanoHTTPD is the b394142 branch copy (sidecar SHA bdb2ab67); menu/xml-v26/debug/release XML were NOT grepped. Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 — OPEN-closing pass (this task, batches 39-42).** No label changed (batch 40 had 0 OPEN rows). Row 3 re-verified fresh: TorrentSessionImpl.java (1720 lines, SHA `aef9618c…`, branch `work-2026-10-31`, in `~/workspace/b394142-openclose-src/`) shows `private void mergeTrackersAndSeeds` at :570 with its sole call at :556 inside `if (false)` at :554 (TODO comment at :553, same bug link) — a complete within-file proof, since a private method has no caller outside its file. Line numbers match the prior file's citations exactly (prior copy SHA `4b698cf6…`; the SHA difference is formatting-only per the sibling batches 28/29 finding — byte-identical after stripping line-number prefixes). Counts unchanged: 39/1/0. Build: not run. C1: not run.

# LibreTorrent batch 40 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 40 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch40-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against source freshly printed in this pass. No prior
  verdict was changed in this pass; the TorrentEngine line lists that were not
  individually re-grepped in the prior proposal were re-grepped here where stated.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 40 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-40 rows are `TODO_CANDIDATE_REACHABLE` in the plan: TorrentSessionImpl
rows 1–35, TorrentSessionImpl$1 rows 36–37, TorrentSessionImpl$InnerListener rows 38–40.
Plan order is preserved below, sequence 1–40 intact.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b383940-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):

- `org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java` — SHA
  `4b698cf61c0b…` (1,720 lines), byte-identical to the local copy in
  `~/workspace/batch35_38/src/`.
- `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — SHA
  `5845b68c9b83…` (1,659 lines), byte-identical to the local copies in
  `~/workspace/batch35_38/src/` and `~/workspace/ground-truth-work/libretorrent/src/`.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence anywhere in this file.

## Conventions used here — recorded, not decided

- `confirmed_by` follows the prior proposal's per-call-site convention (see batch 38
  file for the full statement and the whole-route alternative). Under whole-route,
  lifecycle-callback rows (6–10), alert-route rows (4, 39–40), and Rx/executor-route
  rows (14, 15, 19–21, 35) would flip to INFERRED; labels are unaffected.
- Strict-entry caveat: shared trunk is TorrentService/init -> TorrentEngine.doStart
  (TorrentEngine.java:259, `session.start()`) -> TorrentSessionImpl.start()
  (TorrentSessionImpl.java:862-908) -> onBeforeStart/onAfterStart (:983-1013), and
  TorrentEngine.doStop (TorrentEngine.java:299, `session.requestStop()`) ->
  requestStop/stopTasks/checkStop/super.stop() (TorrentSessionImpl.java:911-948) ->
  onBeforeStop/onAfterStop (:1028-1045). SessionManager lifecycle callbacks are
  INFERRED dispatch (super.start()/super.stop() printed, library call into the
  override not printed). The launcher-to-TorrentService step was NOT printed in this
  pass; under a strict entry-route rule all REACHABLE rows below would revert to OPEN
  pending that printed step. Undecided at project level.
- Lambda/anonymous numbering is by source order and JVM-descriptor match — NOT
  bytecode-verified. For row 40: InnerListener.alert's first lambda is at
  TorrentSessionImpl.java:1083 (`listener.onTorrentAdded(hash)`), descriptor
  (String, Listener) matches row 40 exactly; the second alert lambda at :1086
  (`onTorrentLoaded`) is a different row in a later batch. For rows 36–37: $1 is the
  first anonymous class in TorrentSessionImpl.java, the torrentTaskListener field
  initialiser at :1053-1059; no earlier anonymous class was found in the file.
- The single UNREACHABLE row (3) rests on a printed `if (false)` block, not on
  absence — see table. It flips only if the guard is removed or a second caller
  is printed.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **39 REACHABLE proposed / 1 UNREACHABLE proposed / 0 OPEN.**
- confirmed_by: SOURCE 31 / INFERRED 9 (counted from the table below).
- **0 rows verified for merge.** Verification still requires the main agent's 1-in-5
  spot-check, `py_compile` + build on a full checkout, and the Mac build/C1 return.

## Table

| # | Method (plan order, JVM descriptor) | Label proposed | confirmed_by | Printed caller / route (fresh files) |
|---|---|---|---|---|
| 1 | TorrentSessionImpl.loadSettings `()Lorg/libtorrent4j/SessionParams;` | REACHABLE | SOURCE | TorrentSessionImpl.java:867, `loadSettings()` in start() (:862-908). Definition :1192-1226. |
| 2 | TorrentSessionImpl.mergeTorrent `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;[B)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:281, `mergeTorrent(torrent.id, params, bencode)` in addTorrent. Definition :537-568. NOTE: mergeTorrent itself runs; only its internal mergeTrackersAndSeeds call is dead (row 3). |
| 3 | TorrentSessionImpl.mergeTrackersAndSeeds `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;[B)V` | UNREACHABLE | INFERRED | Kind: `branch_never_taken`. Sole printed call is inside mergeTorrent under `if (false)` (TorrentSessionImpl.java:553-556, TODO "temporary disable due to the bug: https://github.com/aldenml/libtorrent4j/pull/244", call at :556). Definition :570-588. Its own callees extractTrackers/extractUrlSeeds (batch 39 rows 3–4) are UNREACHABLE for the same reason. Flips only if the guard is removed or a second caller is printed. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G4 (281 Java + tests) still shows only the :556 call (inside `if (false)`) and the :570 definition; private method, no other mention anywhere. Label stands. |
| 4 | TorrentSessionImpl.newTask `(Lorg/libtorrent4j/TorrentHandle;Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownload;` | REACHABLE | SOURCE | TorrentSessionImpl.java:1081, `torrentTasks.put(hash, newTask(th, hash))` in InnerListener.alert (ADD_TORRENT case). Per-call-site convention; alert dispatch INFERRED. Definition :1430-1438. |
| 5 | TorrentSessionImpl.notifyListeners `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl$CallListener;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1445-1451 definition (for loop over listeners, `l.apply(listener)`); called from InnerListener.alert, checkError, handleSaveMetadata, handleStats, LoadTorrentTask.run, onAfterStart — including deleteTorrent at :388, which is SOURCE-anchored via TorrentEngine. |
| 6 | TorrentSessionImpl.onAfterStart `()V` | REACHABLE | INFERRED | SessionManager callback. Trigger chain printed: TorrentEngine.doStart :259 `session.start()` -> TorrentSessionImpl.start :907 `super.start(params)` -> library dispatch to onAfterStart (TorrentSessionImpl.java:991-1013) INFERRED. Body is printed (enableSessionLogger, saveSettings, notify onSessionStarted via Rx). |
| 7 | TorrentSessionImpl.onAfterStop `()V` | REACHABLE | INFERRED | SessionManager callback. Chain: requestStop -> stopTasks -> handleStoppingTasks -> checkStop :944-948 `super.stop()` -> library dispatch to onAfterStop (TorrentSessionImpl.java:1041-1045, notify onSessionStopped) INFERRED. |
| 8 | TorrentSessionImpl.onApplySettings `(Lorg/libtorrent4j/SettingsPack;)V` | REACHABLE | INFERRED | SessionManager callback (TorrentSessionImpl.java:1048-1051, saveSettings()). In-app trigger printed is applySettingsPack (:1379-1383, applySettings(sp) + saveSettings()), called from onAfterStart :1002 and applySettings :1398. Library dispatch into the override INFERRED — do not upgrade to SOURCE without a printed libtorrent dispatch line. |
| 9 | TorrentSessionImpl.onBeforeStart `()V` | REACHABLE | INFERRED | SessionManager callback (TorrentSessionImpl.java:983-988, addListener(torrentTaskListener) + addListener(innerListener)). Chain as row 6, library dispatch INFERRED. |
| 10 | TorrentSessionImpl.onBeforeStop `()V` | REACHABLE | INFERRED | SessionManager callback (TorrentSessionImpl.java:1028-1038, disposables.clear(), enableSessionLogger(false), removeListener(torrentTaskListener/innerListener)). Chain as row 7, library dispatch INFERRED. |
| 11 | TorrentSessionImpl.operationNotAllowed `()Z` | REACHABLE | SOURCE | TorrentSessionImpl.java:398 (restoreTorrents guard); :1455 (runNextLoadTorrentTask guard); also in fetchMagnet, addTorrent, deleteTorrent guards (e.g. :260, :330, :379). |
| 12 | TorrentSessionImpl.parseMagnet `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | REACHABLE | SOURCE | TorrentEngine.java:428 (prior proposal anchor, `session.parseMagnet(uri)`); definition TorrentSessionImpl.java:444-452. NOTE: this is a different method from TorrentSessionImpl.parseMagnetUri (row 13) and from TorrentEngine's own parse path — do not conflate. |
| 13 | TorrentSessionImpl.parseMagnetUri `(Ljava/lang/String;)Lorg/libtorrent4j/AddTorrentParams;` | REACHABLE | SOURCE | TorrentSessionImpl.java:432, `parseMagnetUri(uri)` inside fetchMagnet(String) (:427-441). |
| 14 | TorrentSessionImpl.pauseAll `()V` | REACHABLE | SOURCE | TorrentEngine.java:321, `session.pauseAll()` in rescheduleTorrents (inside Rx runnable; dispatch INFERRED, call printed). Definition TorrentSessionImpl.java:756 (prior proposal anchor; S grep in this pass shows pauseAll at :756 and pauseAllManually at :782 — definitions, call sites are in TorrentEngine). |
| 15 | TorrentSessionImpl.pauseAllManually `()V` | REACHABLE | SOURCE | TorrentEngine.java:655, `session.pauseAllManually()` in TorrentEngine.pauseAll (inside Rx runnable; dispatch INFERRED, call printed). |
| 16 | TorrentSessionImpl.removeListener `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | SOURCE | TorrentEngine.java:312, `session.removeListener(listener)` (re-grepped fresh: also :453, :616); TorrentSessionImpl.java:1036-1037 removeListener calls in onBeforeStop. |
| 17 | TorrentSessionImpl.removeLoadedMagnet `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:275, `removeLoadedMagnet(params.sha1hash)` in addTorrent (:272-278). |
| 18 | TorrentSessionImpl.requestStop `()V` | REACHABLE | SOURCE | TorrentEngine.java:299, `session.requestStop()` in doStop (re-grepped fresh). Definition TorrentSessionImpl.java:911-918 (saveAllResumeData + stopTasks). |
| 19 | TorrentSessionImpl.restoreDownload `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1517, `restoreDownload(torrentId)` in LoadTorrentTask.run (non-magnet branch, :1508-1530). Executor dispatch for run is INFERRED (see batch 41 row 6 in the prior proposal set). |
| 20 | TorrentSessionImpl.restoreTorrents `()V` | REACHABLE | SOURCE | TorrentEngine.java:1088, `session.restoreTorrents()` in loadTorrents (inside Completable runnable :1086-1091; dispatch INFERRED, call printed). Definition TorrentSessionImpl.java:396-424, internally calls runNextLoadTorrentTask at :423. |
| 21 | TorrentSessionImpl.resumeAll `()V` | REACHABLE | SOURCE | TorrentEngine.java:323, `session.resumeAll()` in rescheduleTorrents. |
| 22 | TorrentSessionImpl.resumeAllManually `()V` | REACHABLE | SOURCE | TorrentEngine.java:664, `session.resumeAllManually()` in TorrentEngine.resumeAll. |
| 23 | TorrentSessionImpl.runNextLoadTorrentTask `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:423, `runNextLoadTorrentTask()` in restoreTorrents; :1090 in InnerListener.alert (ADD_TORRENT case). Definition :1453-1473 (`loadTorrentsExec.execute(task)` at :1472). |
| 24 | TorrentSessionImpl.saveAllResumeData `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:916, `saveAllResumeData()` in requestStop. Definition :950-955. |
| 25 | TorrentSessionImpl.saveSettings `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1007 (onAfterStart); :1050 (onApplySettings); :1382 (applySettingsPack). Definition :1228-1240. |
| 26 | TorrentSessionImpl.setAutoManaged `(Z)V` | REACHABLE | SOURCE | TorrentEngine.java:1579, `session.setAutoManaged(pref.autoManage())` on preference change (pref_key_auto_manage branch, :1578-1579). |
| 27 | TorrentSessionImpl.setDefaultTrackersList `([Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentEngine.java:1648, `session.setDefaultTrackersList(pref.defaultTrackersList().split("\n"))` (re-grepped fresh). |
| 28 | TorrentSessionImpl.setMaxConnectionsPerTorrent `(I)V` | REACHABLE | SOURCE | TorrentEngine.java:1490, `session.setMaxConnectionsPerTorrent(pref.maxConnectionsPerTorrent())` (re-grepped fresh). |
| 29 | TorrentSessionImpl.setMaxUploadsPerTorrent `(I)V` | REACHABLE | SOURCE | TorrentEngine.java:1493, `session.setMaxUploadsPerTorrent(pref.maxUploadsPerTorrent())` (re-grepped fresh). |
| 30 | TorrentSessionImpl.setRandomPort `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:903, `setRandomPort(settings)` in start (gate settings.useRandomPort); :1392 in applySettings (gate !keepPort && settings.useRandomPort). Definition :1402-1406. |
| 31 | TorrentSessionImpl.setSettings(SessionSettings) `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V` | REACHABLE | SOURCE | TorrentEngine.java session.setSettings(s) sites re-grepped fresh: :1105, :1476, :1481, :1487, :1498, :1503, :1508, :1513, :1518, :1523, :1528, :1533, :1538, :1543, :1605, :1610, :1615, :1620, :1625, :1630, :1635, :1640, :1645, :1653 (plus :139 in the 2-arg form, row 32). Definition TorrentSessionImpl.java:202, delegates to 2-arg overload with keepPort=true. |
| 32 | TorrentSessionImpl.setSettings(SessionSettings,boolean) `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;Z)V` | REACHABLE | SOURCE | TorrentEngine.java:139, `session.setSettings(pref.readSessionSettings(), false)` in TorrentEngine ctor; :1243, :1253 in settings-change handling (re-grepped fresh). Definition TorrentSessionImpl.java:207. |
| 33 | TorrentSessionImpl.settingsToSettingsPack `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;Lorg/libtorrent4j/SettingsPack;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:905 in start; :1245 in saveSettings (via defaultSettingsPack); :1397 in applySettings. Definition :1250-1282. |
| 34 | TorrentSessionImpl.start `()V` | REACHABLE | SOURCE | TorrentEngine.java:259, `session.start()` in doStart (re-grepped fresh). Definition TorrentSessionImpl.java:862-908 (loadSettings, setRandomPort, settingsToSettingsPack, super.start). |
| 35 | TorrentSessionImpl.stopTasks `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:917, `stopTasks()` in requestStop. Definition :920-935 (Observable -> requestStop per task -> subscribe handleStoppingTasks). |
| 36 | TorrentSessionImpl$1.<init> `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl;)V` | REACHABLE | INFERRED | Anonymous TorrentEngineListener torrentTaskListener, field initialiser at TorrentSessionImpl.java:1053-1059. Field initialisers run when a TorrentSessionImpl is constructed (TorrentEngine constructs it, prior proposal anchor :136); anonymous-class numbering inferred from source order (first anonymous class in the file) — merger must confirm against bytecode. |
| 37 | TorrentSessionImpl$1.onTorrentRemoved `(Ljava/lang/String;)V` | REACHABLE | INFERRED | torrentTaskListener callback (TorrentSessionImpl.java:1053-1059, `torrentTasks.remove(id)`). Registered in onBeforeStart :986 (`addListener(torrentTaskListener)`), removed in onBeforeStop :1036. Specific removal trigger (a TorrentDownload notifying its listeners on removal) was not printed in fetched corpus, so dispatch is INFERRED, not SOURCE. |
| 38 | TorrentSessionImpl$InnerListener.<init> `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:174, `innerListener = new InnerListener()` in TorrentSessionImpl ctor (prior proposal anchor; S grep in this pass shows InnerListener class at :1061 and its use in onBeforeStart :987). |
| 39 | TorrentSessionImpl$InnerListener.alert `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | AlertListener callback (TorrentSessionImpl.java:1070-1107). Registered in onBeforeStart :987 (`addListener(innerListener)`, SessionManager AlertListener overload); libtorrent alert dispatch INFERRED. Body is printed (ADD_TORRENT / METADATA_RECEIVED / SESSION_STATS / SAVE_RESUME_DATA / default checkError branches). |
| 40 | TorrentSessionImpl$InnerListener.lambda$alert$0 `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | notifyListeners lambda in ADD_TORRENT branch (TorrentSessionImpl.java:1083-1084, `listener.onTorrentAdded(hash)`). Notify loop printed (:1445-1451); alert dispatch INFERRED. Lambda index is per-inner-class numbering (first lambda in InnerListener.alert), distinct from the outer-class $0 in deleteTorrent. Descriptor (String, Listener) matches :1083 exactly; the second alert lambda at :1086 (`onTorrentLoaded`) is a different row in a later batch. |

No OPEN rows in batch 40. The single UNREACHABLE row rests on a printed
`if (false)` block, not on absence of a caller in a partial copy.

## Gaps the merger must close before merging

1. Printed launcher-to-TorrentService step (strict-entry) — see caveat above.
2. Bytecode confirmation of $1 / lambda$alert$0 numbering (rows 36–37, 40).
3. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.

Scope kept exactly: batch 40 only, LibreTorrent labels only, no other batch, no other
app, no device replay, no Aegis, no push, no graph edits.
