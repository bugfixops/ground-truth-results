# Spot-check — batch 42 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 31 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (3, all confirmed_by-only)

All three are L4 D28 normalisations (SOURCE → INFERRED); label and kind unchanged and correct; no stale-prose sentence found.

- 42/28 SettingsRepositoryImpl.askManageAllFilesPermission() — UNREACHABLE closed_by_api_level INFERRED — PASS. Work prose supports the kind: the only call sites in the tree are fresh PermissionManager.java:65 (inside R-gated StartActivityForResult registration at :60) and :100 (inside R-gated branch at :99) — both gates false at API 27 (27 < 30); no ungated caller exists in the tree.
- 42/29 SettingsRepositoryImpl.askManageAllFilesPermission(boolean) — UNREACHABLE closed_by_api_level INFERRED — PASS. Work prose supports the kind: the only call site is fresh PermissionManager.java:118 inside setDoNotAskStorage, R-gated at :117 — false at API 27.
- 42/31 SettingsRepositoryImpl.askNotificationPermission(boolean) — UNREACHABLE closed_by_api_level INFERRED — PASS. Work prose supports the kind: the only call site is fresh PermissionManager.java:124 inside setDoNotAskNotifications, TIRAMISU-gated at :123 — false at API 27.

## Sample rows (7 sample-only)

- 42/1 TorrentStream$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — PASS. TorrentStream.java:102-106 (`return new TorrentStream[size]`); framework Parcelable dispatch only; saved full-tree grep §D shows no printed parcel/unparcel site for a TorrentStream anywhere.
- 42/6 TorrentStreamServer.serve — REACHABLE INFERRED — PASS. Overrides NanoHTTPD serve; dispatch: HTTPSession.execute virtual serve(this) (batch 16/17 trunk, NanoHTTPD.java:720-733 area) — library dispatch INFERRED, body SOURCE (TorrentStreamServer.java:110-121).
- 42/11 SessionSettings.\<clinit\> — REACHABLE INFERRED — PASS. Static DEFAULT_* constants (SessionSettings.java:40-115 area); JVM initialisation on first use via TorrentSessionImpl field :143 new SessionSettings().
- 42/16 SessionSettings$EncryptMode.\<init\> — REACHABLE INFERRED — PASS. Implicit enum ctor (SessionSettings.java:174-177, EncryptMode(int val)); invoked once per constant at class load; JVM semantics, not a printed call line.
- 42/21 SessionSettings$ProxyType.fromValue — REACHABLE SOURCE — PASS. TorrentEngine.java:1097 s.proxyType = SessionSettings.ProxyType.fromValue(pref.proxyType()) in setProxy; definition SessionSettings.java:211-221 (returns NONE on no match).
- 42/26 SettingsRepositoryImpl.applyProxy() — REACHABLE SOURCE — PASS. TorrentEngine.java:1569 if (pref.applyProxy()) in preference-change handling (pref_key_apply_proxy branch); definition SettingsRepositoryImpl.java:1085-1087.
- 42/36 SettingsRepositoryImpl.autoRefreshFeedsEnableRoaming() — REACHABLE SOURCE — PASS. Fresh: FeedSettingsFragment.java:84 roaming.setChecked(pref.autoRefreshFeedsEnableRoaming()) in bind; definition SettingsRepositoryImpl.java:1228-1230.

Totals: checked 10 (3 changed + 7 sample-only) — PASS 10, FAIL-prose 0, FAIL-label 0.
