**REVISION 2026-11-01 (OPEN-closing round 2, group G8 — batches 56/57/58 only). Status remains UNVERIFIED, NOT verified for merge. Build: not run. C1: not run. Nothing pushed.**
Flip in this revision (1): row 5 OPEN -> UNREACHABLE, kind `closed_by_api_level`, on the saved full-repo grep in `~/workspace/b565758-openclose2-src/grep-full-tree-252.txt` + `grep-full-tree-252b.txt` over the 252-file app Java tree (`~/workspace/ruleF-src/`; Utils SHA `e2ca2ece8da2673be4c388d733f250d36c061dd231fac71889311e6ea0afd0e9`, TorrentNotifier SHA `4b81c32b17e5c1ae1b61c9c187f6db8764fb59656d2607152843f2b7634ddc2f`) confirming exactly the two already-printed call sites and no other, plus the printed API gates below. Corpus caveat: reconstructed Java tree, not a git-checkout grep; res XML checked separately for this name (0 hits). If the merger adopts a stricter grep rule, row 5 reverts to OPEN. Row 24 (`Utils.getForegroundNotifySorting`, TorrentService :139) is UNCHANGED in this revision — the grep-family flip is preserved exactly as written. No other row changed. Counts: 39/0/1 -> 39/1/0.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 57 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they
are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run
or is claimed in this file. No connector `search_code` 0-result was used as evidence of
absence. No row was flipped to UNREACHABLE: no saved full-repo grep exists.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 57 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Membership: exactly the 40 rows of batch 57 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  local copy `~/workspace/agent27-plan.tsv`, plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`,
  all `TODO_CANDIDATE_REACHABLE`, in plan order. Method names/descriptors checked against that copy.
- Prior proposal (`~/workspace/libretorrent-batch57-proposal.md`) was used as a lead list only;
  every row below was re-checked in this pass against the printed source listed below.

## Printed source in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b565758-src/` (base
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/utils/Utils.java` (926 lines) — fresh definitions for all Utils rows; grep of this fresh file
  confirms no new internal caller for any OPEN Utils row beyond the internal callers already known
  (see rows 13, 14, 17, 33).
- `ui/main/MainActivity.java` (811 lines) — fresh anchors: :137 `Utils.getAppTheme`, :180
  `Utils.showManageAllFilesWarningDialog`, :248 `Utils.getNavigationDrawerItems`, :591/:615 drawer
  status filters, :594/:619 drawer sorting, :596/:623 drawer date-added filters, :642
  `Utils.isLargeScreenDevice` (inside `cleanGarbageFragments`, called :187), and no call to any
  other batch-57 Utils method (grep of the fresh file for the OPEN names returned only the
  unrelated `shouldRequestStoragePermission` local variable at :155-156).
- `core/utils/DateUtils.java` — fresh, :135-138 `startOfYesterday`.
- `core/filter/TorrentFilterCollection.java` (104 lines) — fresh, :62 `DateUtils.startOfYesterday`.
- `core/model/TorrentEngine.java` — fresh, upgrading the previously carried engine citations to
  fresh: `handleAutoStop` :143-146 → `forceStop()` :282-285 → `Utils.startServiceBackground` :285;
  `checkPauseTorrents()` :1023-1043 with `isRoaming` :1033, `isMetered` :1035, `isBatteryCharging` :1037,
  `isBatteryBelowThreshold` :1039, `isBatteryLow` :1041; `startWatchDir()` :1116-1119 with
  `Utils.isFileSystemPath` :1119; watch-dir branches :1583/:1590.
- `core/system/FsModuleResolverImpl.java` — fresh (batch-58 row, cited in batch-57 notes only where relevant).

Still carried (NOT freshly printed this pass, flagged, merger must re-verify):
- `Utils.fetchHttpUrl` upstream route (batch 19): AddTorrentViewModel.startDecode → TorrentDecodeTask
  http/https branch → `fetchHttpUrl`. Rows 6 and 11 rest on it in part.
- `Utils.getClipData` caller (batch 77): AddLinkDialog:163-167. Row 16 rests on it.
- TorrentService → TorrentEngine step: engine rows below are service-anchored, not launcher-anchored
  (strict-entry caveat).

## Revision note — OPEN-closing pass, 2026-11-01 (UNVERIFIED)

Counts before this revision: 19 REACHABLE / 0 UNREACHABLE / 21 OPEN (row 24 already flipped to
REACHABLE SOURCE by the 2026-11-01 grep-family pass, preserved here and re-verified on the fresh
TorrentService print). Counts after: 39 / 0 / 1.
Flips, all OPEN → REACHABLE SOURCE on freshly printed source in `~/workspace/b565758-openclose-src/`:
rows 2-3 (`TorrentContentFileTreeUtils.buildFileTree`/`makeObject`, DetailTorrentViewModel:551 and
internal :101-104); row 7 (`colorizeProgressBar`, three adapter ViewHolder ctors); row 8 (`dpToPx`,
PiecesView:73/:74); rows 9-10 (`enableBootReceiver` via Behavior:202 + Scheduling:206/:219,
`enableBootReceiverIfNeeded` via TorrentService:128); rows 13/33 (`getAppVersionNumber`/
`getVersionComponents`, TorrentSessionImpl:895/:889); row 14 (`getAttributeColor`,
FileManagerAdapter:139 + DetailTorrentFragment:283); row 17 (`getClipboardText`, three call sites);
row 22 (`getFileList`, TorrentMetaInfo:108); row 23 (`getForegroundNotifyFilter`,
TorrentService:138); row 25 (`getLineSeparator`, DetailTorrentFragment:704 + Trackers:391);
row 27 (`getRandomColor`, AddTagViewModel:52); row 28 (`getSSLContext`, HttpConnection:69 — the
`fetchHttpUrl` upstream step is carried from batch 19, flagged); rows 29/32 (theme methods, five
activity `onCreate` sites); row 31 (`getTorrentDownloadPath`, FeedDownloaderWorker:114);
row 34 (`hasManageExternalStoragePermission` — CORRECTION: the prior 'sole caller' claim missed the
ungated PermissionManager ctor assignment at :58, which runs in AddTorrentActivity.onCreate:105 and
CreateTorrentActivity.onCreate:64); row 39 (`isHash`, AddLinkViewModel:55/:63 + FeedParser:225/:243).
Still OPEN (1): row 5 (`buildExactAlarmPermissionRequest` — both printed call sites gated off at
API 27; NOT upgraded on a gated caller, per brief). No row flipped to UNREACHABLE (no saved
full-repo grep). Build: not run. C1: not run. Nothing merged, nothing pushed. Also corrected:
`fetchHttpUrl`'s `connection.run()` is at fresh Utils :512, not :515 as the prior file said
(row 11 citation, label unchanged).

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **39 REACHABLE proposed / 0 UNREACHABLE proposed / 1 OPEN.**
- REACHABLE confirmed_by: SOURCE 38 / INFERRED 1 (row 4 `<clinit>` only).
- **0 rows verified for merge** until main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | DateUtils.startOfYesterday (J)J | REACHABLE | SOURCE | Fresh DateUtils :135-138 (`return startOfToday(timeMillis) - secondsInDay * 1000`). Called from TorrentFilterCollection (fresh) :62 inside `dateAddedYesterday()` lambda (:57-63), returned by Utils :862 `getDrawerGroupDateAddedFilter` (prior print) and called from MainActivity (fresh) :596 and :623. Predicate.test dispatch is library dispatch, but the call site is printed. |
| 2 | TorrentContentFileTreeUtils.buildFileTree (List)Pair | REACHABLE | SOURCE | Fresh `DetailTorrentViewModel.java`:551 `TorrentContentFileTreeUtils.buildFileTree(files)` inside `makeFileTree()` (:529), reached from `startMakeFileTree()` (:522-526) called by `updateInfo(TorrentMetaInfo)` :203 and `updateInfo(Torrent,TorrentInfo)` :215; those updateInfo methods are called from DetailTorrentFragment subscriptions (fresh) :256-274. Distinct from `BencodeFileTreeUtils.buildFileTree` (batch 56 row 18). |
| 3 | TorrentContentFileTreeUtils.makeObject (int,String,long,TorrentContentFileTree,boolean) | REACHABLE | SOURCE | Fresh `TorrentContentFileTreeUtils.java`:101-104, called internally from `buildFileTree` whenever a path node is not already in the parent tree. Inherits row 2 route. |
| 4 | Utils.<clinit> ()V | REACHABLE | INFERRED | Fresh Utils :105-128 (constants only, no explicit static block). JVM initialisation, INFERRED, runs before first Utils use; first use in launcher MainActivity (fresh) :137 `Utils.getAppTheme(...)` in `onCreate`. |
| 5 | Utils.buildExactAlarmPermissionRequest (Context)Intent | UNREACHABLE | SOURCE | Kind `closed_by_api_level` (API 27; S = 31). Saved 252-file grep confirms exactly two call sites and no other: `TorrentNotifier.java` :251 inside `makeExactAlarmPermissionNotify()` (:244), which early-returns when `SDK_INT < S` (:245-246) — true at API 27, so line :251 is never reached; and Utils :673 inside `requestExactAlarmPermission`, guarded `SDK_INT >= S` (:672) — false at API 27. Definition Utils :666-670, `@RequiresApi(S)` :665. Both gates are off at API 27, so the method has no live call site at the target API. |
| 6 | Utils.checkConnectivity (Context)Z | REACHABLE | SOURCE | Fresh Utils :157-162 (calls `isNetworkTypeAllowed` :161). Called internally from fresh Utils :466 inside `fetchHttpUrl`; upstream `fetchHttpUrl` route carried from batch 19 (see Carried above). |
| 7 | Utils.colorizeProgressBar (Context,ProgressBar)V | REACHABLE | SOURCE | Fresh Utils :129-136. Called from ViewHolder constructors: `TorrentListAdapter.java` (fresh) :166, `PeerListAdapter.java` (fresh) :131, `TorrentContentFilesAdapter.java` (fresh) :144. ViewHolders are created by adapter `onCreateViewHolder` (framework dispatch); the call sites themselves are printed app code. |
| 8 | Utils.dpToPx (Context,float)I | REACHABLE | SOURCE | Fresh Utils :327-331. Called from `PiecesView.java` (fresh) :73/:74 inside `create()` (:71), called from the PiecesView ctors (:57/:64); the 2-arg ctor is REACHABLE via the freshly printed `fragment_detail_torrent_pieces.xml` layout (batch 94 precedent). |
| 9 | Utils.enableBootReceiver (Context,boolean)V | REACHABLE | SOURCE | Fresh Utils :436-447. Called from `BehaviorSettingsFragment.java` (fresh) :202 (`onPreferenceChange`, autostart key; listener bound by `bindOnPreferenceChangeListener`) and `SchedulingSettingsFragment.java` (fresh) :206/:219 (`onPreferenceChange`, scheduling start/shutdown keys). `enableBootReceiverIfNeeded` (row 10) does NOT call it — it duplicates the logic (fresh Utils :449-460). |
| 10 | Utils.enableBootReceiverIfNeeded (Context)V | REACHABLE | SOURCE | Fresh Utils :449-460. Called from `TorrentService.java` (fresh) :128 inside `init()` (:116), called from `onStartCommand` :191. Service-anchored (strict-entry caveat below). |
| 11 | Utils.fetchHttpUrl (Context,String)[B | REACHABLE | SOURCE | Fresh Utils :462-475 (listener :477-514, `connection.run()` :512). Upstream route carried from batch 19: AddTorrentViewModel.startDecode → TorrentDecodeTask http/https branch → here. Not re-printed here; merger to re-verify. |
| 12 | Utils.getAppTheme (Context)I | REACHABLE | SOURCE | Fresh Utils :374-385 (calls `getThemePreference` :375). Called from MainActivity (fresh) :137 `setTheme(Utils.getAppTheme(...))` in `onCreate` (launcher activity). |
| 13 | Utils.getAppVersionNumber (String)String | REACHABLE | SOURCE | Fresh Utils :532-541. Called from `TorrentSessionImpl.java` (fresh) :895 inside `start()` → `loadSettings()` (session-start route, batch 17 trunk: TorrentEngine `session.start`). |
| 14 | Utils.getAttributeColor (Context,int)I | REACHABLE | SOURCE | Fresh Utils :618-635. Called from `FileManagerAdapter.java` (fresh) :139 (`ViewHolder.bind`) and `DetailTorrentFragment.java` (fresh) :283 (`subscribeMsgViewModel` region); also internally from `showActionModeStatusBar` (fresh :615, now batch 58 row 14 REACHABLE). No longer inherits OPEN from rows 7/14's callers — both now have direct printed callers. |
| 15 | Utils.getBatteryLevel (Context)F | REACHABLE | SOURCE | Fresh Utils :338-350. Called from fresh Utils :363 (`isBatteryLow`) and :367 (`isBatteryBelowThreshold`), both REACHABLE via fresh TorrentEngine `checkPauseTorrents` (rows 35/37). |
| 16 | Utils.getClipData (Context)ClipData | REACHABLE | SOURCE | Fresh Utils :290-301. Caller carried from batch 77: AddLinkDialog:163-167. Not re-printed here. (`getClipboardText` calling `getClipData` at fresh :305 does not make row 17 reachable.) |
| 17 | Utils.getClipboardText (Context)List | REACHABLE | SOURCE | Fresh Utils :302-317. Called from `AddFeedViewModel.java` (fresh) :89 (`initAddModeFromClipboard`), `AddLinkViewModel.java` (fresh) :47 (`initLinkFromClipboard`), and `ClipboardDialog.java` (fresh) :105 (`onCreateDialog`). |
| 18 | Utils.getDefaultBatteryLowLevel ()I | REACHABLE | SOURCE | Fresh Utils :333-336. Called from fresh Utils :363 inside `isBatteryLow`, REACHABLE via fresh TorrentEngine chain (row 37). |
| 19 | Utils.getDrawerGroupDateAddedFilter (Context,long)TorrentFilter | REACHABLE | SOURCE | Prior print Utils :854-871. Called from MainActivity (fresh) :596 and :623 (drawer handlers). |
| 20 | Utils.getDrawerGroupItemSorting (Context,long)TorrentSortingComparator | REACHABLE | SOURCE | Prior print Utils :804-835. Called from MainActivity (fresh) :594 and :619. |
| 21 | Utils.getDrawerGroupStatusFilter (Context,long)TorrentFilter | REACHABLE | SOURCE | Prior print Utils :837-852. Called from MainActivity (fresh) :591 and :615. |
| 22 | Utils.getFileList (FileStorage)ArrayList | REACHABLE | SOURCE | Fresh Utils :142-151. Called from `TorrentMetaInfo.java` (fresh) :108 inside `getMetaInfo()` (:98), called from the `TorrentMetaInfo` ctors (:73/:83), which are REACHABLE (batches 32/33). |
| 23 | Utils.getForegroundNotifyFilter (Context,SettingsRepository)TorrentFilter | REACHABLE | SOURCE | Fresh Utils :873-891. Called from `TorrentService.java` (fresh) :138 inside `setFilterAndSorting()` (:136), called from `init()` :122. Service-anchored (strict-entry caveat below). |
| 24 | Utils.getForegroundNotifySorting (Context,SettingsRepository)TorrentSortingComparator | REACHABLE | SOURCE | Fresh Utils :892-926. Caller (fresh) `TorrentService.java`:139 `itemsSorting = Utils.getForegroundNotifySorting(this, pref)` inside `setFilterAndSorting()` (:136), called from `init()` :122. Flipped 2026-11-01 by the grep-family pass and re-verified on the fresh TorrentService print in this open-close pass. Service-anchored (strict-entry caveat below). |
| 25 | Utils.getLineSeparator ()String | REACHABLE | SOURCE | Fresh Utils :285-287. Called from `DetailTorrentFragment.java` (fresh) :704 and `DetailTorrentTrackersFragment.java` (fresh) :391; a third site, `ManageAllFilesWarningDialog.java` (fresh) :49, is inside the API-gated dialog (batch 74 row 1) and is not needed for this verdict. |
| 26 | Utils.getNavigationDrawerItems (Context,SharedPreferences)List | REACHABLE | SOURCE | Prior print Utils :720-802. Called from MainActivity (fresh) :248-250 (drawer setup, `new DrawerExpandableAdapter(groups, ...)`). |
| 27 | Utils.getRandomColor ()I | REACHABLE | SOURCE | Fresh Utils :661-663. Called from `AddTagViewModel.java` (fresh) :52 (`setRandomColor()`). |
| 28 | Utils.getSSLContext ()SSLContext | REACHABLE | SOURCE | Fresh Utils :585-612 (anonymous trust manager :595-609). Called from `HttpConnection.java` (fresh) :69 (ctor), constructed by `fetchHttpUrl` at fresh Utils :472 and run at :512; `fetchHttpUrl` upstream route carried from batch 19 (see Carried above). Batch-58 rows 23-26 inherit this route. |
| 29 | Utils.getSettingsTheme (Context)I | REACHABLE | SOURCE | Fresh Utils :400-411. Called from `LogSettingsActivity.java` (fresh) :39 (`onCreate`, `setTheme(...)`) and `SettingsActivity.java` (fresh) :44 (`onCreate`, `setTheme(...)`). |
| 30 | Utils.getThemePreference (Context)I | REACHABLE | SOURCE | Fresh Utils :370-372. Called internally from `getAppTheme` fresh :375, REACHABLE via MainActivity (fresh) :137. |
| 31 | Utils.getTorrentDownloadPath (Context)Uri | REACHABLE | SOURCE | Fresh Utils :638-647. Called from `FeedDownloaderWorker.java` (fresh) :114 inside `fetchTorrent()` (worker route, batch 23). |
| 32 | Utils.getTranslucentAppTheme (Context)I | REACHABLE | SOURCE | Fresh Utils :387-398. Called from five activity `onCreate` `setTheme(...)` sites (all fresh): `AddFeedActivity.java`:49, `AddLinkActivity.java`:25, `SelectTagActivity.java`:43, `AddTagActivity.java`:48, `CreateTorrentActivity.java`:57. |
| 33 | Utils.getVersionComponents (String)[I | REACHABLE | SOURCE | Fresh Utils :544-565. Called from `TorrentSessionImpl.java` (fresh) :889 inside `start()` → `loadSettings()` (same route as row 13). |
| 34 | Utils.hasManageExternalStoragePermission (Context)Z | REACHABLE | SOURCE | Fresh Utils :677-697. CORRECTION to the prior 'sole caller' claim: besides the API-27-short-circuited `showManageAllFilesWarningDialog` site (fresh Utils :705, first `||` term `SDK_INT < R` true at API 27), there is a second, UNGATED call site — `PermissionManager.java` (fresh) :58, an unconditional assignment in the constructor body. That constructor runs ungated at API 27 in `AddTorrentActivity.onCreate` (fresh) :105 and `CreateTorrentActivity.onCreate` (fresh) :64. This printed ungated caller is what flips the row; the Utils:705 site alone would not. |
| 35 | Utils.isBatteryBelowThreshold (Context,int)Z | REACHABLE | SOURCE | Fresh Utils :366-368 (calls `getBatteryLevel` :367). Called from TorrentEngine (fresh) `checkPauseTorrents` :1039 (`customBatteryControl` branch). STATE settings gate: `customBatteryControl` must be true (else row 37's branch runs). |
| 36 | Utils.isBatteryCharging (Context)Z | REACHABLE | SOURCE | Fresh Utils :352-360. Called from TorrentEngine (fresh) `checkPauseTorrents` :1037 (`onlyCharging` branch, negated). |
| 37 | Utils.isBatteryLow (Context)Z | REACHABLE | SOURCE | Fresh Utils :362-364 (calls `getBatteryLevel` and `getDefaultBatteryLowLevel` :363). Called from TorrentEngine (fresh) `checkPauseTorrents` :1041 (`batteryControl` branch, when `customBatteryControl` is false). |
| 38 | Utils.isFileSystemPath (Uri)Z | REACHABLE | SOURCE | Fresh Utils :649-655. Called from TorrentEngine (fresh) `startWatchDir` :1119, reached via `handleOnSessionStarted` :1046-1054 (prior print, TorrentEngine fresh file contains the call at :1054) and watch-dir branches :1583/:1590 (fresh). |
| 39 | Utils.isHash (String)Z | REACHABLE | SOURCE | Fresh Utils :271-279. Called from `AddLinkViewModel.java` (fresh) :55/:63 and `FeedParser.java` (fresh) :225 (inside `watchMediaHash`) / :243 (inside `watchTorrentInfoHash`). |
| 40 | Utils.isLargeScreenDevice (Context)Z | REACHABLE | SOURCE | Fresh Utils :251-254. Called from MainActivity (fresh) :642 (`cleanGarbageFragments`, called :187). |

## Undecided conventions recorded, not decided

- **Strict-entry:** TorrentEngine-anchored rows (15, 18, 35-38, and via `fetchHttpUrl` rows 6/11) revert
  to OPEN if the merger requires a printed launcher → TorrentService → TorrentEngine step; that step
  was not freshly printed here. MainActivity-anchored rows (1, 4, 12, 19-21, 26, 30, 40) carry no such
  caveat (launcher activity printed fresh). Merger must pick one strict-entry convention for all batches.
- **Confirmed_by:** per-row convention — SOURCE = a printed direct app-code call site naming the method
  (including internal calls from a SOURCE-anchored method); INFERRED = JVM/framework dispatch where
  registration or first use is printed. Labels unaffected; only `confirmed_by` would change under a
  whole-route convention.
- **API-27-sensitive OPEN rows (5, 34):** both stay OPEN pending a full-repo grep. A grep finding a
  non-gated caller flips them to REACHABLE; finding none would be needed before any
  `closed_by_api_level` claim, and no such claim is made here. Do not conflate "method body returns
  early on API 27" with "call site never runs on API 27" (see batch 58 row 15, which runs but whose
  dialog branch does not).

## Still owed before merge

- [SUPERSEDED by ROUND 2: row 5 flipped OPEN -> UNREACHABLE `closed_by_api_level` on the saved
  full-repo grep; batch 57 now has 0 OPEN rows. A printed ungated caller would flip it back to
  REACHABLE.]
- Fresh prints for the two carried routes (rows 6/11 `fetchHttpUrl` upstream, row 16 `getClipData`
  caller) and for the TorrentService → TorrentEngine step, if the merger requires them fresh.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass or in the 2026-11-01 open-close revision (70 fresh
  connector fetches across batches 56-58, one at a time with 25 s pauses, all succeeded).
