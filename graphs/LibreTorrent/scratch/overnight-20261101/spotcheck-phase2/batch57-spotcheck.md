# Batch 57 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch57-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b565758-openclose-src/`, `~/workspace/b565758-openclose2-src/`,
  `~/workspace/b5354-openclose-src/`, `~/workspace/ruleF-src/`, `~/workspace/overnight/stream-A/corpus/`).
  No connector fetch was needed; no 429; no missing file.
- Rows checked (9): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1 flip 5.
- Batch Counts verified mechanically from the label column AND against the Counts section: 39 REACHABLE / 1 UNREACHABLE / 0 OPEN.
  The stale Counts lines the task mentions were corrected in Phase 1 — the section now states 39/1/0 and matches the table.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `DateUtils.startOfYesterday(J)J` | REACHABLE SOURCE | PASS | DateUtils.java:135-138 (`return startOfToday(timeMillis) - secondsInDay * 1000`, verified); TorrentFilterCollection.java:62 inside dateAddedYesterday() (:57-63); Utils.getDrawerGroupDateAddedFilter returns it (:862 region, def :854); MainActivity :596 and :623 (both verified). |
| 5 `Utils.buildExactAlarmPermissionRequest(Context)Intent` | UNREACHABLE SOURCE `closed_by_api_level` | PASS | Utils.java:665 `@RequiresApi(S)`, :666 (def); exactly two call sites confirmed in the saved 252-file grep (`grep-full-tree-252.txt`: TorrentNotifier :251, Utils :673) and in ruleF-src: TorrentNotifier.makeExactAlarmPermissionNotify :244, early-return `SDK_INT < S` :245-246 (true at API 27, so :251 unreachable); Utils.requestExactAlarmPermission guarded `SDK_INT >= S` :672 (false at API 27). Both gates off at API 27 — no live call site at the target API. The Phase 1 re-check survival claim holds. |
| 6 `Utils.checkConnectivity(Context)Z` | REACHABLE SOURCE | PASS | Utils.java:157-162 (def, `isNetworkTypeAllowed` :161 verified); called internally from fetchHttpUrl :466 (verified). |
| 11 `Utils.fetchHttpUrl(Context,String)[B` | REACHABLE SOURCE | PASS* | Utils.java:462-475 (def), listener :477-514, `connection.run()` :512 (verified). *Upstream route (AddTorrentViewModel.startDecode → TorrentDecodeTask http/https branch) is carried from batch 19, not re-printed in this spot-check: AddTorrentViewModel startDecode :182 and startDecodeTask/new TorrentDecodeTask :197-198 verified to exist, but the http/https branch step was not re-derived here. The file itself flags "merger to re-verify" for this row — preserved, not hidden. |
| 16 `Utils.getClipData(Context)ClipData` | REACHABLE SOURCE | PASS | Utils.java:290-301 (def verified); caller AddLinkDialog.java:165 `Utils.getClipData(activity.getApplicationContext())` — inside the file's cited :163-167 range, verified in the corpus copy. (The row's own note that getClipboardText :305 calling getClipData does not make row 17 reachable is correct and is not relied on here.) |
| 21 `Utils.getDrawerGroupStatusFilter(Context,long)TorrentFilter` | REACHABLE SOURCE | PASS | Utils.java:837-852 (def :837 verified); MainActivity :591 and :615 (both verified). |
| 26 `Utils.getNavigationDrawerItems(Context,SharedPreferences)List` | REACHABLE SOURCE | PASS | Utils.java:720-802 (def :720 verified); MainActivity :248-250 (call at :248 verified). |
| 31 `Utils.getTorrentDownloadPath(Context)Uri` | REACHABLE SOURCE | PASS | Utils.java:638-647 (def :638, return :647 verified); FeedDownloaderWorker.java:114 `Utils.getTorrentDownloadPath(getApplicationContext())` (verified). |
| 36 `Utils.isBatteryCharging(Context)Z` | REACHABLE SOURCE | PASS | Utils.java:352-360 (def verified); TorrentEngine checkPauseTorrents :1037 `stop |= !Utils.isBatteryCharging(appContext)` — verified in both the fresh b5354 TE print and ruleF copy. |

## Totals

- PASS: 9, FAIL: 0 (of 9 checked).
- Proposed corrections: none to any label. One preserved caveat: row 11's upstream chain beyond fetchHttpUrl itself remains
  carried from batch 19 (the file flags it for merger re-verification); rows 1, 5, 6, 16, 21, 26, 31, 36 are fully re-derived.
