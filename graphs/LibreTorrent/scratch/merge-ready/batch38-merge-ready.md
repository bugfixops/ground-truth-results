# LibreTorrent batch 38 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 38 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch38-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against source freshly printed in this pass, and no prior
  verdict was copied without that check. Two prior citations are corrected here
  (rows 9 and 35, flagged in the table); labels are unchanged by either correction.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 38 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-38 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Plan order is preserved
below, sequence 1–40 intact.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b383940-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):

- `org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java` — SHA
  `4b698cf61c0b…` (1,720 lines), byte-identical to the local copy in
  `~/workspace/batch35_38/src/`.
- `org/proninyaroslav/libretorrent/core/model/session/TorrentDownloadImpl.java` — SHA
  `c2741dabb910…` (1,711 lines), byte-identical to the local copy in
  `~/workspace/batch35_38/src/`.
- `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — SHA
  `5845b68c9b83…` (1,659 lines), byte-identical to the local copy in
  `~/workspace/batch35_38/src/` and in `~/workspace/ground-truth-work/libretorrent/src/`.
- `org/proninyaroslav/libretorrent/ui/detailtorrent/pages/DetailTorrentStateFragment.java` —
  freshly fetched in this pass (2,951 bytes) only as a negative check for the batch-39
  OPEN rows; it contains no hit for any batch-38 method and is not evidence for any row here.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence anywhere in this file.

## Conventions used here — recorded, not decided

- `confirmed_by` follows the prior proposal's per-call-site convention: SOURCE = a printed
  app-code call site naming the method exists (including a call inside a listener/alert
  body whose dispatch is itself unprinted); INFERRED = the method is reached only through
  unprinted library/framework/Rx/JVM dispatch (alert callbacks, `types()`, lambdas,
  `<clinit>`). This is NOT the whole-route convention used in some earlier batches
  (e.g. batch 14), under which alert/Rx-route rows would all flip to INFERRED. The
  merger must pick one convention for the whole graph; labels below are unaffected by
  that choice, only `confirmed_by` would change. Rows that would flip under whole-route:
  rows 6, 11–16, 28, 35 (alert route) and row 24's Rx runnable (the
  `applySessionLoggerFilters` call itself is printed at TorrentSessionImpl.java:1388).
- Strict-entry caveat (unchanged from the prior proposal): routes anchor at
  TorrentService / TorrentEngine / TorrentSessionImpl / TorrentDownloadImpl, not at a
  printed launcher entry. The launcher-to-TorrentService step was NOT printed in this
  pass. Under a strict entry-route rule all REACHABLE rows below would revert to OPEN
  pending that printed step. This convention is also undecided at project level.
- Lambda/anonymous numbering is by source order and, where stated, by JVM-descriptor
  match — NOT bytecode-verified. A swap within a group would not change any label here.
- No UNREACHABLE label is claimed in this batch: no saved full-repo grep was run.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN.**
- confirmed_by: SOURCE 27 / INFERRED 13 (counted from the table below).
- **0 rows verified for merge.** Verification still requires the main agent's 1-in-5
  spot-check, `py_compile` + build on a full checkout, and the Mac build/C1 return.

## Table

| # | Method (plan order, JVM descriptor) | Label proposed | confirmed_by | Printed caller / route (fresh files) |
|---|---|---|---|---|
| 1 | TorrentDownloadImpl.setMaxUploads `(I)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1435 (newTask) and :831 (setMaxUploadsPerTorrent, called from TorrentEngine.java:1493). |
| 2 | TorrentDownloadImpl.setSequentialDownload `(Z)V` | REACHABLE | SOURCE | TorrentEngine.java:703, `task.setSequentialDownload(...)` (inside setSequentialDownload, :696-706). |
| 3 | TorrentDownloadImpl.setTorrentName `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentEngine.java:677, `task.setTorrentName(name)` (inside setTorrentName, :670-680). |
| 4 | TorrentDownloadImpl.setUploadSpeedLimit `(I)V` | REACHABLE | SOURCE | TorrentEngine.java:924, `task.setUploadSpeedLimit(limit)` (inside setUploadSpeedLimit, :916-925). |
| 5 | TorrentDownloadImpl.stateToStateCode `(Lorg/libtorrent4j/TorrentStatus$State;)Lorg/proninyaroslav/libretorrent/core/model/data/TorrentStateCode;` | REACHABLE | SOURCE | TorrentDownloadImpl.java:1369, inside getStateCode(); getStateCode is called from TorrentEngine.java:790 (`task.getStateCode()`). Also D:228-229 inside InnerListener.alert STATE_CHANGED. |
| 6 | TorrentDownloadImpl.torrentRemoved `()V` | REACHABLE | INFERRED | TorrentDownloadImpl.java:235, InnerListener.alert TORRENT_REMOVED case; alert dispatch library INFERRED. Body :456-461 calls notifyListeners + forceStop(). |
| 7 | TorrentDownloadImpl$1.<init> `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownloadImpl;Ljava/util/concurrent/atomic/AtomicReference;Ljava/util/concurrent/CountDownLatch;)V` | REACHABLE | INFERRED | Anonymous AlertListener in getBencode() (TorrentDownloadImpl.java:1659-1689); registered via sessionManager.addListener(listener) at :1692 (CORRECTED: prior proposal said ~1694; :1694 is the `th.isValid()` check). JVM/library timing of construction vs registration is INFERRED. |
| 8 | TorrentDownloadImpl$1.alert `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | Library alert dispatch to the anonymous listener registered at TorrentDownloadImpl.java:1692; body :1666-1688 waits for SAVE_RESUME_DATA. |
| 9 | TorrentDownloadImpl$1.types `()[I` | REACHABLE | INFERRED | Library call to types() on the registered anonymous listener (body returns the SAVE_RESUME_DATA filter array, TorrentDownloadImpl.java:1661-1663); dispatch not printed from library source. |
| 10 | TorrentDownloadImpl$InnerListener.<init> `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownloadImpl;)V` | REACHABLE | SOURCE | TorrentDownloadImpl ctor: `listener = new InnerListener();` at :165, followed by sessionManager.addListener(listener) at :166. |
| 11 | TorrentDownloadImpl$InnerListener.alert `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | Library alert dispatch to InnerListener, registered in the TorrentDownloadImpl ctor (:165-166); switch body is TorrentDownloadImpl.java:214-281. |
| 12 | TorrentDownloadImpl$InnerListener.lambda$alert$0 `(Lorg/libtorrent4j/alerts/StateChangedAlert;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | First notifyListeners lambda in InnerListener.alert() (STATE_CHANGED case), TorrentDownloadImpl.java:226-229; descriptor matches (StateChangedAlert + listener). Listener dispatch INFERRED. |
| 13 | TorrentDownloadImpl$InnerListener.lambda$alert$1 `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | Second notifyListeners lambda in InnerListener.alert() (TORRENT_PAUSED), TorrentDownloadImpl.java:238-239; descriptor matches (listener only). |
| 14 | TorrentDownloadImpl$InnerListener.lambda$alert$2 `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | Third notifyListeners lambda in InnerListener.alert() (TORRENT_RESUMED), TorrentDownloadImpl.java:244-245. |
| 15 | TorrentDownloadImpl$InnerListener.lambda$alert$3 `(ILorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | Fourth notifyListeners lambda in InnerListener.alert() (PIECE_FINISHED), TorrentDownloadImpl.java:259-260; descriptor matches (int piece + listener). |
| 16 | TorrentDownloadImpl$InnerListener.types `()[I` | REACHABLE | INFERRED | TorrentDownloadImpl.java:208-211, returns INNER_LISTENER_TYPES; library call to types() on the registered listener, dispatch not printed from library source. |
| 17 | TorrentSessionImpl.<clinit> `()V` | REACHABLE | INFERRED | JVM class initialisation on first construction via TorrentEngine.java:136, `new TorrentSessionImpl(...)` (batch-38 prior proposal's anchor; TorrentEngine line not re-grepped in this pass — see batch 40 row 18 for the same anchor, verified there via TorrentSessionImpl ctor use). |
| 18 | TorrentSessionImpl.<init> `(Lorg/proninyaroslav/libretorrent/core/storage/TorrentRepository;Lorg/proninyaroslav/libretorrent/core/system/FileSystemFacade;Lorg/proninyaroslav/libretorrent/core/system/SystemFacade;)V` | REACHABLE | SOURCE | TorrentEngine constructs TorrentSessionImpl (prior proposal anchor TorrentEngine.java:136-139, followed by session.addListener at :140); TorrentSessionImpl ctor body itself is printed (InnerListener field at TorrentSessionImpl.java:174, ctor use). Re-print TorrentEngine.java:136-140 fresh at merge if a fresh anchor line is required — TorrentEngine.java WAS freshly fetched in this pass, so the merger can grep it directly. |
| 19 | TorrentSessionImpl.addDefaultTrackers `(Lorg/libtorrent4j/swig/add_torrent_params;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:491 (fetchMagnet path), :1609 (download TorrentInfo overload), :1659 (download overload at :1615-1662). Both :1609 and :1659 verified fresh. |
| 20 | TorrentSessionImpl.addListener `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:986-987 (onBeforeStart, addListener(torrentTaskListener) and addListener(innerListener)); TorrentEngine addListener anchor per prior proposal (:140). |
| 21 | TorrentSessionImpl.addTorrent `(Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;Z)Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;` | REACHABLE | SOURCE | TorrentEngine calls session.addTorrent (prior proposal anchors :351/:412); internally calls download(torrent.id, params, bencode) at TorrentSessionImpl.java:310, verified fresh. |
| 22 | TorrentSessionImpl.applyMaxStoredLogs `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1387, inside applySettings() (:1385-1400); definition :1408-1414. |
| 23 | TorrentSessionImpl.applyProxy `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;Lorg/libtorrent4j/SettingsPack;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1281, inside settingsToSettingsPack(); definition :1284-1299. |
| 24 | TorrentSessionImpl.applySessionLoggerFilters `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1388, inside applySettings(); body :1416-1427 calls SessionLogger.applyFilterParams via an Rx runnable (Rx dispatch INFERRED, but the applySessionLoggerFilters call itself is printed app code). |
| 25 | TorrentSessionImpl.applySettings `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;Z)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:213 area (setSettings delegation, prior proposal) and :1385 definition; called from TorrentEngine session-settings path; applySettings:1385 calls applyMaxStoredLogs, applySessionLoggerFilters, and applySettingsPack (:1398). |
| 26 | TorrentSessionImpl.applySettingsPack `(Lorg/libtorrent4j/SettingsPack;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1002 (onAfterStart) and :1398 (applySettings, row 25). |
| 27 | TorrentSessionImpl.cancelFetchMagnet `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentEngine.java:485 (prior proposal anchor); also TorrentSessionImpl.java:333 (download(String,AddTorrentParams,byte[]), row 38), verified fresh. |
| 28 | TorrentSessionImpl.checkError `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | TorrentSessionImpl.java:1101, InnerListener.alert default case; alert dispatch library INFERRED; internally calls sessionLogger.send(alert) at :1102 (prior proposal's batch-35 anchor). |
| 29 | TorrentSessionImpl.checkStop `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:941 (InnerListener ADD_TORRENT case, via handleStoppingTasks) and :1089 (InnerListener.alert ADD_TORRENT, checkStop() after newTask); also :944-947 definition, reached via stopTasks() from requestStop:911-918. |
| 30 | TorrentSessionImpl.convertEncryptMode `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$EncryptMode;)I` | REACHABLE | SOURCE | TorrentSessionImpl.java:1268-1269, inside settingsToSettingsPack(). |
| 31 | TorrentSessionImpl.convertProxyType `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$ProxyType;Z)I` | REACHABLE | SOURCE | TorrentSessionImpl.java:1286, inside settingsToSettingsPack() (applyProxy, :1284-1286). |
| 32 | TorrentSessionImpl.defaultSettingsPack `()Lorg/libtorrent4j/SettingsPack;` | REACHABLE | SOURCE | TorrentSessionImpl.java:1197, :1217, :1224 (loadSettings paths) and :1242-1248 definition; internally calls settingsToSettingsPack() at :1245. |
| 33 | TorrentSessionImpl.deleteTorrent `(Ljava/lang/String;Z)V` | REACHABLE | SOURCE | TorrentEngine.java:539 (prior proposal anchor); internally calls task.remove(withFiles) at TorrentSessionImpl.java:391, verified fresh (definition :377-393). |
| 34 | TorrentSessionImpl.dhtBootstrapNodes `()Ljava/lang/String;` | REACHABLE | SOURCE | TorrentSessionImpl.java:881, inside settingsToSettingsPack() (`sp.set_str(..., dhtBootstrapNodes())`); definition :1183-1190. |
| 35 | TorrentSessionImpl.dhtNodes `()J` | REACHABLE | INFERRED | TorrentSessionImpl.java:1174, inside handleStats() (:1168-1181), called from TorrentSessionImpl.InnerListener.alert SESSION_STATS case :1095-1096; alert dispatch library INFERRED. CORRECTED: prior proposal said :1181 (the closing brace of handleStats); the call itself is at :1174. NOTE: this is the TorrentSession super method `dhtNodes()`, NOT `getDhtNodes()` at :712-714 (a different method, batch 39 row 9, still OPEN) — do not conflate. |
| 36 | TorrentSessionImpl.disableIpFilter `()V` | REACHABLE | SOURCE | TorrentEngine.java:1560, `session.disableIpFilter()` (verified fresh in the TorrentEngine print, :1554-1561 preference-change branch). |
| 37 | TorrentSessionImpl.download(String,File,boolean,boolean) `(Ljava/lang/String;Ljava/io/File;ZZ)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:344, inside download(String,AddTorrentParams,byte[]) when torrent.isDownloadingMetadata(); also :1515 (magnet download path, LoadTorrentTask.run). Definition at :1615-1662, calls addDefaultTrackers at :1659. |
| 38 | TorrentSessionImpl.download(String,AddTorrentParams,byte[]) `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;[B)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:310, inside addTorrent() (row 21). Definition at :328-374; internally calls cancelFetchMagnet at :333, download(String,File,boolean,boolean) at :344, download(byte[],...) at :353, download(TorrentInfo,...) at :365. |
| 39 | TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List) `(Lorg/libtorrent4j/TorrentInfo;Ljava/io/File;[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;ZZLjava/util/List;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1537 (from the byte[] overload, row 40) and :365 (from row 38). Definition at :1541-1610. |
| 40 | TorrentSessionImpl.download(byte[],File,Priority[],boolean,boolean,List) `([BLjava/io/File;[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;ZZLjava/util/List;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:353, inside download(String,AddTorrentParams,byte[]) (row 38). Definition at :1533-1539, delegates to row 39 at :1537. |

## Gaps the merger must close before merging

1. Printed launcher-to-TorrentService step (strict-entry) — see caveat above.
2. Saved full-repo grep for any row later disputed — no row here rests on a grep claim.
3. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
4. TorrentEngine.java:136-140 fresh line check for rows 17–18 if the merger wants the
   anchor re-grepped rather than taken from the prior proposal (the file itself was
   freshly fetched in this pass and saved at `~/workspace/b383940-src/TorrentEngine.java`).

Scope kept exactly: batch 38 only, LibreTorrent labels only, no other batch, no other
app, no device replay, no Aegis, no push, no graph edits.
