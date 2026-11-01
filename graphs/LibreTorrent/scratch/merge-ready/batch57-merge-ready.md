# LibreTorrent batch 57 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **18 REACHABLE proposed / 0 UNREACHABLE proposed / 22 OPEN.**
- REACHABLE confirmed_by: SOURCE 17 / INFERRED 1 (row 4 `<clinit>` only).
- **0 rows verified for merge** until main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | DateUtils.startOfYesterday (J)J | REACHABLE | SOURCE | Fresh DateUtils :135-138 (`return startOfToday(timeMillis) - secondsInDay * 1000`). Called from TorrentFilterCollection (fresh) :62 inside `dateAddedYesterday()` lambda (:57-63), returned by Utils :862 `getDrawerGroupDateAddedFilter` (prior print) and called from MainActivity (fresh) :596 and :623. Predicate.test dispatch is library dispatch, but the call site is printed. |
| 2 | TorrentContentFileTreeUtils.buildFileTree (List)Pair | OPEN | — | Prior print :46-117. No caller printed in this pass (fresh greps of Utils/MainActivity/TFC/DetailTorrentFragment/AddTorrentViewModel/TorrentEngine contain no such call). Do NOT conflate with `BencodeFileTreeUtils.buildFileTree` (batch 56 row 18, AddTorrentViewModel fresh :379) — different class. Pending full-repo grep / printed caller. NOT UNREACHABLE. |
| 3 | TorrentContentFileTreeUtils.makeObject (int,String,long,TorrentContentFileTree,boolean) | OPEN | — | Prior print :119-126 (private). Called internally from `buildFileTree` :101-104, so inherits row 2 OPEN. |
| 4 | Utils.<clinit> ()V | REACHABLE | INFERRED | Fresh Utils :105-128 (constants only, no explicit static block). JVM initialisation, INFERRED, runs before first Utils use; first use in launcher MainActivity (fresh) :137 `Utils.getAppTheme(...)` in `onCreate`. |
| 5 | Utils.buildExactAlarmPermissionRequest (Context)Intent | OPEN | — | Fresh Utils :666-670, `@RequiresApi(S)`. Sole printed caller is fresh Utils :673 `requestExactAlarmPermission`, guarded `SDK_INT >= S`; on standard API 27 that guard is false, so that call does not run. No other printed caller. OPEN, not `closed_by_api_level` on this evidence alone — pending full-repo grep for other callers. |
| 6 | Utils.checkConnectivity (Context)Z | REACHABLE | SOURCE | Fresh Utils :157-162 (calls `isNetworkTypeAllowed` :161). Called internally from fresh Utils :466 inside `fetchHttpUrl`; upstream `fetchHttpUrl` route carried from batch 19 (see Carried above). |
| 7 | Utils.colorizeProgressBar (Context,ProgressBar)V | OPEN | — | Fresh Utils :129-136 (calls `getAttributeColor` :133). No printed caller in fresh files. |
| 8 | Utils.dpToPx (Context,float)I | OPEN | — | Fresh Utils :327-331. No printed caller in fresh files. |
| 9 | Utils.enableBootReceiver (Context,boolean)V | OPEN | — | Fresh Utils :436-447. No printed caller in fresh files. |
| 10 | Utils.enableBootReceiverIfNeeded (Context)V | OPEN | — | Fresh Utils :449-460. No printed caller in fresh files. |
| 11 | Utils.fetchHttpUrl (Context,String)[B | REACHABLE | SOURCE | Fresh Utils :462-475 (listener :477-514, `connection.run()` :515). Upstream route carried from batch 19: AddTorrentViewModel.startDecode → TorrentDecodeTask http/https branch → here. Not re-printed here; merger to re-verify. |
| 12 | Utils.getAppTheme (Context)I | REACHABLE | SOURCE | Fresh Utils :374-385 (calls `getThemePreference` :375). Called from MainActivity (fresh) :137 `setTheme(Utils.getAppTheme(...))` in `onCreate` (launcher activity). |
| 13 | Utils.getAppVersionNumber (String)String | OPEN | — | Fresh Utils :532-541. Sole printed caller is `getVersionComponents` fresh :549, itself OPEN (row 33), so inherits OPEN. |
| 14 | Utils.getAttributeColor (Context,int)I | OPEN | — | Fresh Utils :618-635. Printed callers are `colorizeProgressBar` fresh :133 and `showActionModeStatusBar` fresh :615, both OPEN, so inherits OPEN. |
| 15 | Utils.getBatteryLevel (Context)F | REACHABLE | SOURCE | Fresh Utils :338-350. Called from fresh Utils :363 (`isBatteryLow`) and :367 (`isBatteryBelowThreshold`), both REACHABLE via fresh TorrentEngine `checkPauseTorrents` (rows 35/37). |
| 16 | Utils.getClipData (Context)ClipData | REACHABLE | SOURCE | Fresh Utils :290-301. Caller carried from batch 77: AddLinkDialog:163-167. Not re-printed here. (`getClipboardText` calling `getClipData` at fresh :305 does not make row 17 reachable.) |
| 17 | Utils.getClipboardText (Context)List | OPEN | — | Fresh Utils :302-317 (calls `getClipData` :305). No printed caller of `getClipboardText` itself in fresh files. |
| 18 | Utils.getDefaultBatteryLowLevel ()I | REACHABLE | SOURCE | Fresh Utils :333-336. Called from fresh Utils :363 inside `isBatteryLow`, REACHABLE via fresh TorrentEngine chain (row 37). |
| 19 | Utils.getDrawerGroupDateAddedFilter (Context,long)TorrentFilter | REACHABLE | SOURCE | Prior print Utils :854-871. Called from MainActivity (fresh) :596 and :623 (drawer handlers). |
| 20 | Utils.getDrawerGroupItemSorting (Context,long)TorrentSortingComparator | REACHABLE | SOURCE | Prior print Utils :804-835. Called from MainActivity (fresh) :594 and :619. |
| 21 | Utils.getDrawerGroupStatusFilter (Context,long)TorrentFilter | REACHABLE | SOURCE | Prior print Utils :837-852. Called from MainActivity (fresh) :591 and :615. |
| 22 | Utils.getFileList (FileStorage)ArrayList | OPEN | — | Fresh Utils :142-151. No printed caller in fresh files. |
| 23 | Utils.getForegroundNotifyFilter (Context,SettingsRepository)TorrentFilter | OPEN | — | Fresh Utils :873-891. No printed caller in fresh files. |
| 24 | Utils.getForegroundNotifySorting (Context,SettingsRepository)TorrentSortingComparator | OPEN | — | Fresh Utils :892-926. No printed caller in fresh files. |
| 25 | Utils.getLineSeparator ()String | OPEN | — | Fresh Utils :285-287. No printed caller in fresh files. |
| 26 | Utils.getNavigationDrawerItems (Context,SharedPreferences)List | REACHABLE | SOURCE | Prior print Utils :720-802. Called from MainActivity (fresh) :248-250 (drawer setup, `new DrawerExpandableAdapter(groups, ...)`). |
| 27 | Utils.getRandomColor ()I | OPEN | — | Fresh Utils :661-663. No printed caller in fresh files. |
| 28 | Utils.getSSLContext ()SSLContext | OPEN | — | Fresh Utils :585-612 (anonymous trust manager :595-609). No printed caller in fresh files. Batch-58 rows 23-26 inherit this status. |
| 29 | Utils.getSettingsTheme (Context)I | OPEN | — | Fresh Utils :400-411 (calls `getThemePreference` :403). No printed caller (unlike `getAppTheme`, row 12). Fresh MainActivity grep found no `getSettingsTheme` call. |
| 30 | Utils.getThemePreference (Context)I | REACHABLE | SOURCE | Fresh Utils :370-372. Called internally from `getAppTheme` fresh :375, REACHABLE via MainActivity (fresh) :137. |
| 31 | Utils.getTorrentDownloadPath (Context)Uri | OPEN | — | Fresh Utils :638-647. No printed caller in fresh files. Note: batch 55 cites this method as a *caller* of SystemFacadeHelper.getFileSystemFacade — reverse direction, does not make this row reachable. |
| 32 | Utils.getTranslucentAppTheme (Context)I | OPEN | — | Fresh Utils :387-398 (calls `getThemePreference` :390). No printed caller in fresh files (fresh MainActivity grep found no call). |
| 33 | Utils.getVersionComponents (String)[I | OPEN | — | Fresh Utils :544-565 (calls `getAppVersionNumber` :549). No printed caller in fresh files. |
| 34 | Utils.hasManageExternalStoragePermission (Context)Z | OPEN | — | Fresh Utils :677-697. Sole printed caller is fresh Utils :705 `showManageAllFilesWarningDialog`, inside an `||` whose first term is `SDK_INT < R` — true on API 27, so short-circuit means this call is NOT evaluated on API 27 via that caller. No other printed caller. OPEN, not `closed_by_api_level` on this evidence alone — pending full-repo grep. |
| 35 | Utils.isBatteryBelowThreshold (Context,int)Z | REACHABLE | SOURCE | Fresh Utils :366-368 (calls `getBatteryLevel` :367). Called from TorrentEngine (fresh) `checkPauseTorrents` :1039 (`customBatteryControl` branch). STATE settings gate: `customBatteryControl` must be true (else row 37's branch runs). |
| 36 | Utils.isBatteryCharging (Context)Z | REACHABLE | SOURCE | Fresh Utils :352-360. Called from TorrentEngine (fresh) `checkPauseTorrents` :1037 (`onlyCharging` branch, negated). |
| 37 | Utils.isBatteryLow (Context)Z | REACHABLE | SOURCE | Fresh Utils :362-364 (calls `getBatteryLevel` and `getDefaultBatteryLowLevel` :363). Called from TorrentEngine (fresh) `checkPauseTorrents` :1041 (`batteryControl` branch, when `customBatteryControl` is false). |
| 38 | Utils.isFileSystemPath (Uri)Z | REACHABLE | SOURCE | Fresh Utils :649-655. Called from TorrentEngine (fresh) `startWatchDir` :1119, reached via `handleOnSessionStarted` :1046-1054 (prior print, TorrentEngine fresh file contains the call at :1054) and watch-dir branches :1583/:1590 (fresh). |
| 39 | Utils.isHash (String)Z | OPEN | — | Fresh Utils :271-279. No printed caller in fresh files. |
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

- Saved full-repo grep for the 22 OPEN rows, priority: `buildFileTree`/`makeObject` for
  TorrentContentFileTreeUtils (rows 2-3, distinct from batch 56), `getSSLContext` + Utils$2 quartet
  (row 28 → batch 58 rows 23-26), `getTorrentDownloadPath`, theme methods (rows 29, 32),
  `getSettingsTheme`/`getTranslucentAppTheme` callers, `buildExactAlarmPermissionRequest` and
  `hasManageExternalStoragePermission` non-gated callers (rows 5, 34).
- Fresh prints for the two carried routes (rows 6/11 `fetchHttpUrl` upstream, row 16 `getClipData`
  caller) and for the TorrentService → TorrentEngine step, if the merger requires them fresh.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass (10 fresh connector fetches across batches 56-58, one at a time
  with 20-25 s pauses, all succeeded).
