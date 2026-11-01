# Spot-check — batch 45 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 45/1 SettingsRepositoryImpl.maxConnectionsPerTorrent() — REACHABLE SOURCE — PASS. readSessionSettings:216; TorrentEngine.java:1490 (handleSettingsChanged, key pref_key_max_connections_per_torrent); LimitationsSettingsFragment.java:149 display; definition :864.
- 45/6 SettingsRepositoryImpl.maxLogSize(int) — REACHABLE SOURCE — PASS. LogSettingsFragment.java:95 (onPreferenceChange); definition :1325.
- 45/11 SettingsRepositoryImpl.moveAfterDownload() — REACHABLE SOURCE — PASS. TorrentEngine.java:1315 (onTorrentFinished); StorageSettingsFragment.java:115 display; definition :721.
- 45/16 SettingsRepositoryImpl.notifySound(String) — UNREACHABLE closed_by_api_level INFERRED — PASS. Definition :270; ONLY printed call site: AppearanceSettingsFragment.java:213 (ringtonePicker result handler); the picker is launched only from the click listener registered at :144-168, inside initLegacyNotifySettings (gate :118-119); at API 27 the picker is never launched, so the handler never runs.
- 45/21 SettingsRepositoryImpl.playSoundNotify(boolean) — UNREACHABLE closed_by_api_level INFERRED — PASS. Definition :296; ONLY printed call site: AppearanceSettingsFragment.java:241 (onPreferenceChange branch); that branch can fire only if the listener was bound, and it is bound only inside initLegacyNotifySettings (:134), gated at SDK < O (:118-119); at API 27 the branch never fires.
- 45/26 SettingsRepositoryImpl.posixDiskIo() — REACHABLE SOURCE — PASS. readSessionSettings:241; StorageSettingsFragment.java:203 display; definition :812.
- 45/31 SettingsRepositoryImpl.proxyLogin(String) — REACHABLE SOURCE — PASS. ProxySettingsFragment.java:227 (onPreferenceChange); definition :1065.
- 45/36 SettingsRepositoryImpl.proxyPort() — REACHABLE SOURCE — PASS. readSessionSettings:245; TorrentEngine.java:1099 (setProxy); ProxySettingsFragment.java:126 display; definition :1020.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
