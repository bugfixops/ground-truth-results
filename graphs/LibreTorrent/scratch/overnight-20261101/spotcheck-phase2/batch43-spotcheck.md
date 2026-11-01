# LibreTorrent batch 43 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch43-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b4143-src/` settings fragments and `~/workspace/b444546-src/TorrentEngine.java`.
  No connector fetch was needed; no merge-ready file was edited; no label was flipped.
- Rows checked (8): sample 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated
  2026-11-01 Phase 1 revision note listing label changes, so no extra Phase 1 rows apply.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.autostart(boolean) | REACHABLE SOURCE | PASS | BehaviorSettingsFragment.java:203 `pref.autostart((boolean)newValue)` in onPreferenceChange; getter also :74. |
| 6 | SettingsRepositoryImpl.customBatteryControl() | REACHABLE SOURCE | PASS | TorrentEngine.java:991 and :1025 `pref.customBatteryControl()`; also BehaviorSettingsFragment.java:120 display. |
| 11 | SettingsRepositoryImpl.defaultTrackersList(String) | REACHABLE SOURCE | PASS | BehaviorSettingsFragment.java:241 `pref.defaultTrackersList((String)newValue)` in onPreferenceChange; getter also :154 and TorrentEngine.java:1648. |
| 16 | SettingsRepositoryImpl.enableIpFiltering() | REACHABLE SOURCE | PASS | TorrentEngine.java:1047 and :1555 `pref.enableIpFiltering()`; also NetworkSettingsFragment.java:198 display. |
| 21 | SettingsRepositoryImpl.enableNatPmp(boolean) | REACHABLE SOURCE | PASS | NetworkSettingsFragment.java:332 `pref.enableNatPmp((boolean) newValue)` in onPreferenceChange; getter also :142. |
| 26 | SettingsRepositoryImpl.enableSchedulingStart() | REACHABLE SOURCE | PASS | SchedulingSettingsFragment.java:72 `enableStart.setChecked(pref.enableSchedulingStart())` in bind. |
| 31 | SettingsRepositoryImpl.enableUpnp(boolean) | REACHABLE SOURCE | PASS | NetworkSettingsFragment.java:329 `pref.enableUpnp((boolean) newValue)` in onPreferenceChange; getter also :135. |
| 36 | SettingsRepositoryImpl.encryptOutConnectionsMode() | REACHABLE SOURCE | PASS | NetworkSettingsFragment.java:190 `var type = pref.encryptOutConnectionsMode()`; also TorrentEngine.java:1113. |

## Totals

- Checked: 8. PASS: 8. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: `confirmed_by` SOURCE here follows the file's per-row convention (a printed `pref.*`
  call site counts as SOURCE for the Impl method via the RepositoryHelper singleton). The
  spot-check confirms the call sites; it does not decide the interface-dispatch convention
  question recorded in the file (batches 43-46 must match at merge).
