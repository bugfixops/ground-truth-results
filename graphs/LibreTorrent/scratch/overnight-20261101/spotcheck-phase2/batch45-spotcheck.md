# LibreTorrent batch 45 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch45-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b444546-src/` and the 281-file corpus in `~/workspace/overnight/stream-A/corpus/java/`.
  No connector fetch was needed; no merge-ready file was edited; no label was flipped.
- Rows checked (8): sample 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 Phase 1 label
  change is listed for this batch (its labels are stated unchanged vs the prior proposal).
- D10 FLAG (per task, not decided here): rows 16 and 21 are closed_by_api_level rows whose
  verdict turns on the owed D10 API-gate extension to batches 45/46, which DECISIONS.md
  records as not yet applied to this batch's own file. They are marked PASS-as-filed below
  (the gates and sole-caller evidence re-derive exactly as filed), but the extension itself
  is NOT decided by this spot-check and the coordinator/merger must not treat these two
  rows as finally decided until D10 is applied to batch 45.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.maxConnectionsPerTorrent() | REACHABLE SOURCE | PASS | TorrentEngine.java:1490 `session.setMaxConnectionsPerTorrent(pref.maxConnectionsPerTorrent())`; also readSessionSettings:216 and LimitationsSettingsFragment.java:149 display. |
| 6 | SettingsRepositoryImpl.maxLogSize(int) | REACHABLE SOURCE | PASS | LogSettingsFragment.java:95 `pref.maxLogSize(value)` in onPreferenceChange; getter also :69 and TorrentEngine.java:1644. |
| 11 | SettingsRepositoryImpl.moveAfterDownload() | REACHABLE SOURCE | PASS | TorrentEngine.java:1315 `if (pref.moveAfterDownload())` (onTorrentFinished); also StorageSettingsFragment.java:115 display. |
| 16 | SettingsRepositoryImpl.notifySound(String) | UNREACHABLE closed_by_api_level INFERRED | PASS-as-filed, D10-EXTENSION FLAG | Corpus-wide grep: only call site AppearanceSettingsFragment.java:213 (ringtonePicker result handler); the picker is launched only from the click listener at :144-168 inside initLegacyNotifySettings, gated at :118-119 (SDK < O). No ungated caller. Def SettingsRepositoryImpl.java:270. Verdict re-derives as filed under the D10 method-vs-branch rule, but D10's extension to batch 45 is owed, not decided here. |
| 21 | SettingsRepositoryImpl.playSoundNotify(boolean) | UNREACHABLE closed_by_api_level INFERRED | PASS-as-filed, D10-EXTENSION FLAG | Corpus-wide grep: only call site AppearanceSettingsFragment.java:241 (onPreferenceChange branch); listener bound only inside initLegacyNotifySettings (:134), gated at :118-119 (SDK < O). No ungated caller. Def SettingsRepositoryImpl.java:296. Same D10-extension caveat as row 16. |
| 26 | SettingsRepositoryImpl.posixDiskIo() | REACHABLE SOURCE | PASS | StorageSettingsFragment.java:203 `posixDiskIo.setChecked(pref.posixDiskIo())` display; also readSessionSettings:241. |
| 31 | SettingsRepositoryImpl.proxyLogin(String) | REACHABLE SOURCE | PASS | ProxySettingsFragment.java:227 `pref.proxyLogin((String)newValue)` in onPreferenceChange; getter also :154 and TorrentEngine.java:1102. |
| 36 | SettingsRepositoryImpl.proxyPort() | REACHABLE SOURCE | PASS | TorrentEngine.java:1099 `s.proxyPort = pref.proxyPort()` (setProxy); also ProxySettingsFragment.java:126 display. |

## Totals

- Checked: 8. PASS: 8 (of which 2 conditional on the owed D10 extension: rows 16, 21). FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Open item for the coordinator: apply D10 to batch 45 rows 15, 16, 20, 21 (sample rows 16, 21
  checked here) before treating their closed_by_api_level verdicts as decided.
