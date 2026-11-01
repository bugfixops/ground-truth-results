**REVISION 2026-11-01 (grep-flip re-check, Stream A Phase 1) — UNVERIFIED.** Re-checked all 5 OPEN-closing flips (rows 9, 11, 23, 28, 29) against the complete tree: ALL SURVIVED, no label change. Counts UNCHANGED: 33 REACHABLE proposed / 7 UNREACHABLE proposed / 0 OPEN (rows 3-4 are pre-existing branch_never_taken rows, not flips, and were not re-judged). Grep: `~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt` §§G2-G3 (281 main Java files = 252 ruleF + 28 feedparser + NanoHTTPD, plus 20 test/androidTest, plus 87 res layout/xml files). CAVEAT (disclosed, not hidden): two fresh connector 429s stopped the final ui-subtree listings, so the feedparser files used are the missing-29 worker's branch copies (18/28 byte-identical to independently printed b1-src copies, packages verified, app imports match) and NanoHTTPD is the b394142 branch copy (sidecar SHA bdb2ab67, byte-identical to b2-src); menu (16 files), xml-v26, debug/release XML were NOT grepped (layout/xml were). Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 — OPEN-closing pass (this task, batches 39-42).** All 5 OPEN rows closed to UNREACHABLE on freshly printed source + a saved complete-tree grep; no other row changed. Fresh source in `~/workspace/b394142-openclose-src/` (TorrentSessionImpl.java 1720 lines SHA `aef9618c…`, TorrentEngine.java 1659 lines SHA `17d06efe…`, TorrentSession.java 136 lines SHA `d5d74e46…`, DetailTorrentStateFragment.java 88 lines SHA `b01a6a20…`, all branch `work-2026-10-31`, connector only, no fresh 429). Saved grep: `b394142-openclose-src/full_tree_grep_394142.txt` — §§A-B over all 252 app Java files (parent `ruleF-src` reconstruction, complete 252/252 at grep time) + §H (debug/play/release source sets contain no .java; test 7 + androidTest 13 files, zero hits) + §I (87 res layout/xml files, zero hits). Caller-set argument for all five rows: TorrentSession is an app-defined interface whose only holder in the shipped code is app code (TorrentEngine creates TorrentSessionImpl; it is never passed to a framework/library object), and no layout expression names these methods, so the app-Java census is exhaustive for them; the per-task Engine namesakes are different methods (different descriptors and receivers) and are distinguished in each row. `confirmed_by` for the five flips is INFERRED (no printed call site exists to be SOURCE; the verdict rests on the saved grep + printed definitions) — recorded, not decided, per the per-row vs whole-route convention. Each row flips back to REACHABLE on any single printed caller. Build: not run. C1: not run.

# LibreTorrent batch 39 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 39 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior proposal
  (`~/workspace/libretorrent-batch39-proposal.md`) was used as an INPUT / lead list only;
  every row below was checked against source freshly printed in this pass. No prior
  verdict was changed in this pass except for the line-range clarifications noted
  (row 2, row 32's lambda-order support); the five OPEN rows remain OPEN, for the
  reasons given — no new caller for any of them was printed in this pass.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 39 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-39 rows are `TODO_CANDIDATE_REACHABLE` in the plan, all class
TorrentSessionImpl. Plan order is preserved below, sequence 1–40 intact.

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
- `org/proninyaroslav/libretorrent/ui/detailtorrent/pages/DetailTorrentStateFragment.java` —
  freshly fetched in this pass (2,951 bytes); grep for `getDhtNodes|isDHT|isPeX|SpeedLimit|dht`
  returns NO hit. This is a checked file, not a full-repo grep, and does not prove
  absence anywhere else — it only removes the state fragment as a candidate caller
  for rows 9, 11, 23, 28, 29.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence anywhere in this file. A local-corpus grep (other proposals and
local copies) was used only to find positive leads, never as absence evidence; it
found only definitions for the five OPEN rows and the per-task Engine methods
described below.

## Conventions used here — recorded, not decided

- `confirmed_by` follows the prior proposal's per-call-site convention (see batch 38
  file for the full statement and the whole-route alternative). Under whole-route,
  alert/Rx-route rows (24–27, 32–40) would flip to INFERRED; labels are unaffected.
- Strict-entry caveat: routes anchor at TorrentService / TorrentEngine, as in batches
  16–22. The launcher-to-TorrentService step was NOT printed in this pass; under a
  strict entry-route rule all REACHABLE rows below would revert to OPEN pending that
  printed step. Undecided at project level.
- Lambda numbering (rows 32–40) is by source order and JVM-descriptor match — NOT
  bytecode-verified. Support found in this pass: the first lambda in
  TorrentSessionImpl.java is deleteTorrent's notifyListeners lambda at :388, and the
  outer-class lambdas then occur in exactly the order deleteTorrent $0 (:388),
  enableIpFilter Thread $1 (:726) / notify $2 (:737), stopTasks $3 (:929),
  onAfterStart $4 (:1009), checkError $5 (:1111), handleSaveMetadata $6 (:1164),
  handleStats $7 (:1173), applySessionLoggerFilters $8 (:1418). The InnerListener.alert
  lambdas at :1083/:1086 belong to the inner class, not this numbering. A later
  outer-class lambda at :1527 (LoadTorrentTask.run) would be $9 or later and is not a
  batch-39 row. This ordering support does NOT replace a bytecode check.
- The `if (false)` UNREACHABLE rows (3–4) rest on a printed branch, not on absence —
  see table. They flip to REACHABLE only if the guard is removed or a second caller
  is printed.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **33 REACHABLE proposed / 7 UNREACHABLE proposed / 0 OPEN (2026-11-01 revision; was 33/2/5).**
- confirmed_by among REACHABLE/UNREACHABLE: SOURCE 26 / INFERRED 14 (counted from the
  table below; the five 2026-11-01 flips are INFERRED, see revision note).
- **0 rows verified for merge.** Verification still requires the main agent's 1-in-5
  spot-check, `py_compile` + build on a full checkout, and the Mac build/C1 return.

## Table

| # | Method (plan order, JVM descriptor) | Label proposed | confirmed_by | Printed caller / route (fresh files) |
|---|---|---|---|---|
| 1 | TorrentSessionImpl.enableIpFilter `(Landroid/net/Uri;)V` | REACHABLE | SOURCE | TorrentEngine.java:1050, `session.enableIpFilter(Uri.parse(path))` in handleOnSessionStarted (gate pref.enableIpFiltering(), path != null); also :1558, :1566 on preference change. Definition TorrentSessionImpl.java:718-760. |
| 2 | TorrentSessionImpl.enableSessionLogger `(Z)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1004, `enableSessionLogger(true)` in onAfterStart (:991-1013); :1032 in onBeforeStop; :1389 in applySettings (:1385-1400). Definition :1015-1025. Prior proposal's ranges (:991-1010, :1029-1038, :1385-1392) are the enclosing methods, not the call lines — call lines above are the precise citations. |
| 3 | TorrentSessionImpl.extractTrackers `(Lorg/libtorrent4j/swig/bdecode_node;Z)Ljava/util/List;` | UNREACHABLE | INFERRED | Kind: `branch_never_taken`. Only printed caller is mergeTrackersAndSeeds at TorrentSessionImpl.java:581, and mergeTrackersAndSeeds is itself only called inside mergeTorrent under `if (false)` at :553-556 (TODO "temporary disable due to the bug: https://github.com/aldenml/libtorrent4j/pull/244", call at :556). Definition :590. Flips to REACHABLE if the guard is removed or a second caller is printed. |
| 4 | TorrentSessionImpl.extractUrlSeeds `(Lorg/libtorrent4j/swig/bdecode_node;)Ljava/util/List;` | UNREACHABLE | INFERRED | Kind: `branch_never_taken`. Same as row 3: only caller mergeTrackersAndSeeds at TorrentSessionImpl.java:584, itself only under `if (false)` at :553-556. |
| 5 | TorrentSessionImpl.fetchMagnet(String) `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/MagnetInfo;` | REACHABLE | SOURCE | TorrentEngine.java:419 (prior proposal anchor); definition TorrentSessionImpl.java:427-441, internally calls parseMagnetUri at :432 and fetchMagnet(AddTorrentParams) at :433. |
| 6 | TorrentSessionImpl.fetchMagnet(AddTorrentParams) `(Lorg/libtorrent4j/AddTorrentParams;)Lorg/libtorrent4j/AddTorrentParams;` | REACHABLE | SOURCE | Private. Called inside fetchMagnet(String) at TorrentSessionImpl.java:433 (`resParams = fetchMagnet(params)`); definition :454. NOTE: the prior proposal's table header showed the return as MagnetInfo; the plan descriptor (AddTorrentParams) is reproduced here and is the authoritative membership descriptor — the merger should check it against bytecode, but the call site and method identity are unambiguous. |
| 7 | TorrentSessionImpl.getAlertMask `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)Lorg/libtorrent4j/swig/alert_category_t;` | REACHABLE | SOURCE | TorrentSessionImpl.java:1001 (onAfterStart) and :1278 (settingsToSettingsPack, called from start :905, saveSettings :1245, applySettings :1397). |
| 8 | TorrentSessionImpl.getAllowedEncryptLevel `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$EncryptMode;Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings$EncryptMode;)I` | REACHABLE | SOURCE | TorrentSessionImpl.java:1270, inside settingsToSettingsPack (:1250-1282). |
| 9 | TorrentSessionImpl.getDhtNodes `()J` | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition TorrentSessionImpl.java:712-715 (`return stats().dhtNodes();`). Saved full-tree grep §A: the only `getDhtNodes` hits in all 252 app Java files are the TorrentSession interface declaration (:92) and this definition — zero callers; res grep §I zero; test/androidTest §H zero. handleStats (:1168-1181) uses `dhtNodes()` (the TorrentSession super method, :1174), NOT getDhtNodes() — do not conflate. Flips to REACHABLE on any printed caller. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G2 (281 Java + tests) still shows only the TorrentSession declaration (:92) and this definition — zero callers; res layout/xml §G12 zero. Label stands. |
| 10 | TorrentSessionImpl.getDownloadSpeed `()J` | REACHABLE | SOURCE | TorrentSessionImpl.java:1177, inside handleStats (:1168-1181). Per-call-site convention; whole-route would be INFERRED (alert dispatch). |
| 11 | TorrentSessionImpl.getDownloadSpeedLimit `()I` | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition TorrentSessionImpl.java:690-695. Saved full-tree grep §B: zero session-level callers. TorrentEngine.java:894-902 `getDownloadSpeedLimit(id)` is the PER-TASK version (`task.getDownloadSpeedLimit()` at :902), not this method — do not conflate; DetailTorrentViewModel:377-379 and DetailTorrentFragment:754 call the per-task chain, not this method. Res grep §I zero; test/androidTest §H zero. Flips to REACHABLE on any printed session-level caller. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G3 (281 Java + tests) still shows zero session-level callers; only the per-task chain (TorrentEngine :894-902, ViewModel :377-379, Fragment :754) plus declarations/definitions. Res layout/xml §G12 zero. Label stands. |
| 12 | TorrentSessionImpl.getIface `(Ljava/lang/String;I)Ljava/lang/String;` | REACHABLE | SOURCE | TorrentSessionImpl.java:1259, `sp.listenInterfaces(getIface(settings.inetAddress, settings.portRangeFirst))` in settingsToSettingsPack. |
| 13 | TorrentSessionImpl.getListenPort `()I` | REACHABLE | SOURCE | TorrentSessionImpl.java:1179, inside handleStats. Per-call-site convention; whole-route would be INFERRED. |
| 14 | TorrentSessionImpl.getLoadedMagnet `(Ljava/lang/String;)[B` | REACHABLE | SOURCE | TorrentSessionImpl.java:274, `getLoadedMagnet(params.sha1hash)` in addTorrent (:272-278). |
| 15 | TorrentSessionImpl.getLogger `()Lorg/proninyaroslav/libretorrent/core/model/session/SessionLogger;` | REACHABLE | SOURCE | TorrentEngine.java:253 (prior proposal anchor, doStart) and :958 (getSessionLogger). |
| 16 | TorrentSessionImpl.getPieceSizeList `()[I` | REACHABLE | SOURCE | TorrentEngine.java:950 (prior proposal anchor, `return session.getPieceSizeList()`); definition TorrentSessionImpl.java:972-975. |
| 17 | TorrentSessionImpl.getSettings `()Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;` | REACHABLE | SOURCE | TorrentEngine.java:1095, 1233, 1250, 1474-1653 (many session.getSettings() sites, prior proposal list, not individually re-grepped here); TorrentSessionImpl.java:1665-equivalent use in addDefaultTrackers path (settings read). The TorrentEngine call sites are in the freshly fetched file and can be grepped at merge. |
| 18 | TorrentSessionImpl.getTask `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownload;` | REACHABLE | SOURCE | TorrentEngine.java session.getTask(id) sites (prior proposal list, e.g. :490, :514, :675, :701); TorrentSessionImpl.java:382 in deleteTorrent (`TorrentDownload task = getTask(id)`), verified fresh. |
| 19 | TorrentSessionImpl.getTorrentVersionList `()[I` | REACHABLE | SOURCE | TorrentEngine.java:954 (prior proposal anchor, `return session.getTorrentVersionList()`). |
| 20 | TorrentSessionImpl.getTotalDownload `()J` | REACHABLE | SOURCE | TorrentSessionImpl.java:1175, inside handleStats. Per-call-site convention; whole-route would be INFERRED. |
| 21 | TorrentSessionImpl.getTotalUpload `()J` | REACHABLE | SOURCE | TorrentSessionImpl.java:1176, inside handleStats. Per-call-site convention; whole-route would be INFERRED. |
| 22 | TorrentSessionImpl.getUploadSpeed `()J` | REACHABLE | SOURCE | TorrentSessionImpl.java:1178, inside handleStats. Per-call-site convention; whole-route would be INFERRED. |
| 23 | TorrentSessionImpl.getUploadSpeedLimit `()I` | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition TorrentSessionImpl.java:698-703. Saved full-tree grep §B: zero session-level callers. TorrentEngine.java:883-892 `getUploadSpeedLimit(id)` is the PER-TASK version (`task.getUploadSpeedLimit()` at :891), not this method — do not conflate; DetailTorrentViewModel:373-375 and DetailTorrentFragment:753 call the per-task chain. Res grep §I zero; test/androidTest §H zero. Flips to REACHABLE on any printed session-level caller. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G3 (281 Java + tests) still shows zero session-level callers; only the per-task chain (TorrentEngine :883-892, ViewModel :373-375, Fragment :753) plus declarations/definitions. Res layout/xml §G12 zero. Label stands. |
| 24 | TorrentSessionImpl.handleMetadataReceived `(Lorg/libtorrent4j/alerts/MetadataReceivedAlert;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1093, handleMetadataReceived in InnerListener.alert (METADATA_RECEIVED case). Per-call-site convention; alert dispatch to InnerListener is INFERRED (see batch 40 rows 38-39). |
| 25 | TorrentSessionImpl.handleSaveMetadata `(Lorg/libtorrent4j/alerts/SaveResumeDataAlert;)V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1099, handleSaveMetadata in InnerListener.alert (SAVE_RESUME_DATA case). Per-call-site convention; alert dispatch INFERRED. |
| 26 | TorrentSessionImpl.handleStats `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:1096, handleStats() in InnerListener.alert (SESSION_STATS case). Per-call-site convention; alert dispatch INFERRED. |
| 27 | TorrentSessionImpl.handleStoppingTasks `()V` | REACHABLE | SOURCE | TorrentSessionImpl.java:928, `this::handleStoppingTasks` method reference in stopTasks() subscribe (:920-935), and :932 in the error lambda; Rx dispatch INFERRED, method-reference call printed. |
| 28 | TorrentSessionImpl.isDHTEnabled `()Z` | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition TorrentSessionImpl.java:847-852 (`sp != null && sp.isEnableDht()`). Saved full-tree grep §A: the only `isDHTEnabled` hits in all 252 app Java files are the TorrentSession interface declaration (:112) and this definition — zero callers; res grep §I zero; test/androidTest §H zero. DetailTorrentStateFragment freshly fetched (88 lines): no hit. Flips to REACHABLE on any printed caller. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G2 (281 Java + tests) still shows only the TorrentSession declaration (:112) and this definition — zero callers; res layout/xml §G12 zero. Label stands. |
| 29 | TorrentSessionImpl.isPeXEnabled `()Z` | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition TorrentSessionImpl.java:855-859 (body returns constant true). Saved full-tree grep §A: the only `isPeXEnabled` hits in all 252 app Java files are the TorrentSession interface declaration (:114) and this definition — zero callers; res grep §I zero; test/androidTest §H zero. Flips to REACHABLE on any printed caller. RE-CHECK 2026-11-01 (SURVIVED): complete-tree grep ~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt §G2 (281 Java + tests) still shows only the TorrentSession declaration (:114) and this definition — zero callers; res layout/xml §G12 zero. Label stands. |
| 30 | TorrentSessionImpl.isRunning `()Z` | REACHABLE | SOURCE | TorrentEngine.java:304 (prior proposal anchor, `return session.isRunning()`); TorrentSessionImpl.java:864, `isRunning()` guard in start(). |
| 31 | TorrentSessionImpl.isTorrentAlreadyRunning `(Ljava/lang/String;)Z` | REACHABLE | SOURCE | TorrentSessionImpl.java:402, `isTorrentAlreadyRunning(torrent.id)` in restoreTorrents (:396-424); :1511 in LoadTorrentTask.run. |
| 32 | TorrentSessionImpl.lambda$applySessionLoggerFilters$8 `(Lorg/proninyaroslav/libretorrent/core/settings/SessionSettings;)V` | REACHABLE | INFERRED | Runnable inside applySessionLoggerFilters (TorrentSessionImpl.java:1418-1427), called from applySettings :1388. Lambda index supported by file order (see Conventions: $8 is the 9th outer-class lambda, after $0-$7 listed there); NOT bytecode-verified. Rx dispatch INFERRED. |
| 33 | TorrentSessionImpl.lambda$checkError$5 `(Lorg/libtorrent4j/alerts/Alert;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | notifyListeners lambda inside checkError (TorrentSessionImpl.java:1111-1142), called from InnerListener.alert default case :1101. Notify loop printed (:1445-1451); alert dispatch INFERRED. Index per Conventions. |
| 34 | TorrentSessionImpl.lambda$deleteTorrent$0 `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | notifyListeners lambda inside deleteTorrent (TorrentSessionImpl.java:388-389). Notify loop printed; listener callback dispatch INFERRED. Index $0 = first lambda in the file (:388). |
| 35 | TorrentSessionImpl.lambda$enableIpFilter$1 `(ILorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | Thread runnable inside enableIpFilter (TorrentSessionImpl.java:726-760 area, Thread at :726). Thread.start -> run() dispatch INFERRED, as in batch 16. Index $1 = Thread lambda at :726 (descriptor: int param in the notify lambda at :737 is $2, see next row — the $1/$2 split follows the prior proposal's descriptor match, not a bytecode check). |
| 36 | TorrentSessionImpl.lambda$enableIpFilter$2 `(Landroid/net/Uri;)V` | REACHABLE | INFERRED | notifyListeners lambda inside the enableIpFilter thread runnable (TorrentSessionImpl.java:737). Notify loop printed; thread + notify dispatch INFERRED. |
| 37 | TorrentSessionImpl.lambda$handleSaveMetadata$6 `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | notifyListeners lambda inside handleSaveMetadata (TorrentSessionImpl.java:1164-1165). Notify loop printed; alert dispatch INFERRED. |
| 38 | TorrentSessionImpl.lambda$handleStats$7 `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | notifyListeners lambda inside handleStats (TorrentSessionImpl.java:1173-1179). Same caveats as row 37. |
| 39 | TorrentSessionImpl.lambda$onAfterStart$4 `()V` | REACHABLE | INFERRED | Completable runnable in onAfterStart (TorrentSessionImpl.java:1009-1012, notifyListeners(TorrentEngineListener::onSessionStarted)). Rx dispatch INFERRED. |
| 40 | TorrentSessionImpl.lambda$stopTasks$3 `(Ljava/lang/Throwable;)V` | REACHABLE | INFERRED | Error lambda in stopTasks subscribe (TorrentSessionImpl.java:929-933, `(err) -> handleStoppingTasks()`). Runs only on stop error, but the route exists; Rx dispatch INFERRED. |

## OPEN items and what resolves them

Rows 9, 11, 23, 28, 29 — CLOSED 2026-11-01 (see revision note and table): saved complete-tree grep + caller-set argument, distinguishing session-level from per-task methods. Rows 3–4 flip to REACHABLE only if the `if (false)` guard at TorrentSessionImpl.java:554 is removed or a second caller is printed.

Rows 3–4 rest on a printed `if (false)` block, not on absence. Rows 9, 11, 23, 28, 29 rest on the saved complete-tree grep in `b394142-openclose-src/full_tree_grep_394142.txt` (§§A-B, H, I) plus the caller-set argument in the revision note — not on a partial-copy grep.

## Gaps the merger must close before merging

1. Printed launcher-to-TorrentService step (strict-entry) — see caveat above.
2. Saved full-repo grep for the five OPEN rows — DONE 2026-11-01 (`b394142-openclose-src/full_tree_grep_394142.txt`); rows closed on it, see revision note.
3. Bytecode confirmation of lambda $ numbering (rows 32–40).
4. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.

Scope kept exactly: batch 39 only, LibreTorrent labels only, no other batch, no other
app, no device replay, no Aegis, no push, no graph edits.
