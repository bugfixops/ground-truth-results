# LibreTorrent batch 46 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch46-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b444546-src/`. No connector fetch was needed; no merge-ready file was
  edited; no label was flipped.
- Rows checked (10): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS rows 21, 22 (already in the
  sample for 21; 22 added) — the two rows the file flags as changed vs the prior proposal
  (REACHABLE -> UNREACHABLE closed_by_api_level on the Utils gate analysis).
- D10 FLAG (per task, not decided here): rows 21 and 22 are closed_by_api_level rows whose
  verdict turns on the owed D10 API-gate extension to batches 45/46, which DECISIONS.md
  records as not yet applied to this batch's own file. They are marked PASS-as-filed below
  (the gate analysis re-derives exactly as filed), but the extension itself is NOT decided
  by this spot-check.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.proxyType(int) | REACHABLE SOURCE | PASS | ProxySettingsFragment.java:210 `pref.proxyType(type)` in onPreferenceChange; getter is batch 45 row 40 (TorrentEngine.java:1097). |
| 6 | SettingsRepositoryImpl.saveTorrentFiles(boolean) | REACHABLE SOURCE | PASS | StorageSettingsFragment.java:285 `pref.saveTorrentFiles((boolean) newValue)` in onPreferenceChange; getter also :142 and TorrentEngine.java:1273,:1431. |
| 11 | SettingsRepositoryImpl.schedulingRunOnlyOnce() | REACHABLE SOURCE | PASS | SchedulingSettingsFragment.java:100 `runOnlyOnce.setChecked(pref.schedulingRunOnlyOnce())` display. |
| 16 | SettingsRepositoryImpl.schedulingStartTime(int) | REACHABLE SOURCE | PASS | SchedulingSettingsFragment.java:222 `pref.schedulingStartTime((int)newValue)` in onPreferenceChange (then Scheduler.setStartAppAlarm); getter also :86,:199,:212. |
| 21 | SettingsRepositoryImpl.showManageAllFilesWarningDialog() | UNREACHABLE closed_by_api_level INFERRED | PASS-as-filed, D10-EXTENSION FLAG | Utils.java:704-707 early return `SDK_INT < R \|\| hasPermission \|\| !pref.showManageAllFilesWarningDialog()`; at API 27 the first disjunct (27 < 30) is true, so `||` short-circuits and the :706 getter call is never evaluated. No other printed call site in the fetched corpus. Same D10-extension caveat as batch 45. |
| 22 | SettingsRepositoryImpl.showManageAllFilesWarningDialog(boolean) | UNREACHABLE closed_by_api_level INFERRED | PASS-as-filed, D10-EXTENSION FLAG | Utils.java:711 `pref.showManageAllFilesWarningDialog(false)` sits after the :704-707 early return, which is always taken at API 27, so :711 is never reached. No other printed call site. Same D10-extension caveat as row 21. |
| 26 | SettingsRepositoryImpl.shutdownDownloadsComplete(boolean) | REACHABLE SOURCE | PASS | BehaviorSettingsFragment.java:232 `pref.shutdownDownloadsComplete((boolean)newValue)` in onPreferenceChange; getter also TorrentEngine.java:144 and BehaviorSettingsFragment.java:88. |
| 31 | SettingsRepositoryImpl.theme() | REACHABLE SOURCE | PASS | Utils.java:371 `return RepositoryHelper.getSettingsRepository(context).theme()` (getThemePreference); also AppearanceSettingsFragment.java:83 display. |
| 36 | SettingsRepositoryImpl.unmeteredConnectionsOnly(boolean) | REACHABLE SOURCE | PASS | BehaviorSettingsFragment.java:223 `pref.unmeteredConnectionsOnly((boolean)newValue)` in onPreferenceChange; getter also TorrentEngine.java:1010,:1028 and Utils.java:169. |

## Totals

- Checked: 10. PASS: 10 (of which 2 conditional on the owed D10 extension: rows 21, 22). FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: the file itself flags that the enclosing method Utils.showManageAllFilesWarningDialog
  still runs at API 27 (its MainActivity:180 caller was not re-fetched here); only the two
  pref.* call statements inside it are dead at API 27. That distinction was preserved in
  this re-derivation and is not a correction.
