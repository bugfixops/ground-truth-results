# LibreTorrent batch 42 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch42-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only — the 281-file
  complete-tree corpus in `~/workspace/overnight/stream-A/corpus/java/` and
  `~/workspace/b4143-src/PermissionManager.java`. No connector fetch was needed; no
  merge-ready file was edited; no label was flipped.
- Rows checked (10): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1 changed rows 1, 28, 29, 31
  (1 and 31 already in the sample).
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentStream$1.newArray | UNREACHABLE INFERRED (Phase 1 flip) | PASS | Def TorrentStream.java:103-105 (`return new TorrentStream[size]`). Corpus-wide grep: no parcel/unparcel site for a TorrentStream (parcel sites pass other types only); framework dispatch only, together with the batch-41 parcel quartet. |
| 6 | TorrentStreamServer.serve | REACHABLE INFERRED | PASS | Def TorrentStreamServer.java:111 (serve, calls handleTorrent). NanoHTTPD HTTPSession dispatch to virtual serve() is library dispatch, hence INFERRED, as filed. |
| 11 | SessionSettings.<clinit> | REACHABLE INFERRED | PASS | Static DEFAULT_* constants SessionSettings.java:40-115 area (e.g. DEFAULT_ENCRYPT_MODE, DEFAULT_PROXY_TYPE). First use printed: TorrentSessionImpl.java:143 `new SessionSettings()`. JVM init INFERRED, as filed. |
| 16 | SessionSettings$EncryptMode.<init> | REACHABLE INFERRED | PASS | Enum ctor SessionSettings.java:174-177, constants ENABLED/FORCED/DISABLED :166-172; invoked once per constant at class load (JVM semantics, not a printed call line), as filed. |
| 21 | SessionSettings$ProxyType.fromValue | REACHABLE SOURCE | PASS | TorrentEngine.java:1097 `SessionSettings.ProxyType.fromValue(pref.proxyType())` in setProxy. Def SessionSettings.java:211-221. |
| 26 | SettingsRepositoryImpl.applyProxy() | REACHABLE SOURCE | PASS | TorrentEngine.java:1569 `if (pref.applyProxy())` in preference-change handling. Def SettingsRepositoryImpl.java:1085-1087. |
| 28 | SettingsRepositoryImpl.askManageAllFilesPermission() | UNREACHABLE closed_by_api_level SOURCE (Phase 1 flip) | PASS | Corpus-wide grep: only call sites are PermissionManager.java:65 (inside the R-gated registration block at :60) and :100 (inside the R-gated branch at :99); both gates false at API 27 (27 < 30). No ungated caller. Def SettingsRepositoryImpl.java:1397-1399. |
| 29 | SettingsRepositoryImpl.askManageAllFilesPermission(boolean) | UNREACHABLE closed_by_api_level SOURCE (Phase 1 flip) | PASS | Corpus-wide grep: only call site PermissionManager.java:118 inside setDoNotAskStorage, R-gated at :117 — false at API 27. Def SettingsRepositoryImpl.java:1403-1407. Callers of setDoNotAskStorage do not ungate the call, as filed. |
| 31 | SettingsRepositoryImpl.askNotificationPermission(boolean) | UNREACHABLE closed_by_api_level SOURCE (Phase 1 flip) | PASS | Corpus-wide grep: only call site PermissionManager.java:124 inside setDoNotAskNotifications, TIRAMISU-gated at :123 — false at API 27. Def SettingsRepositoryImpl.java:1431-1435. Contrast row 30 getter, which has the ungated lambda site at PermissionManager.java:89 (not checked here, but the contrast holds on the same print). |
| 36 | SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming() | REACHABLE SOURCE | PASS | FeedSettingsFragment.java:84 `roaming.setChecked(pref.autoRefreshFeedsEnableRoaming())` in bind (b4143-src copy). Def SettingsRepositoryImpl.java:1228-1230. |

## Totals

- Checked: 10. PASS: 10. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: rows 28, 29, 31 rest on the method-vs-call-site API-gate reading (call site itself
  never runs at API 27). That reading is the filed convention; the spot-check confirms the
  gates and the absence of any other caller in the 281-file corpus, but does not decide
  the convention project-wide.
