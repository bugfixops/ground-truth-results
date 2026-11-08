# Spot-check — batch 46 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 46/1 SettingsRepositoryImpl.proxyType(int) — REACHABLE SOURCE — PASS. ProxySettingsFragment.java:210 (onPreferenceChange); definition :1000. Getter is batch 45 row 40.
- 46/6 SettingsRepositoryImpl.saveTorrentFiles(boolean) — REACHABLE SOURCE — PASS. StorageSettingsFragment.java:285 (onPreferenceChange); definition :753.
- 46/11 SettingsRepositoryImpl.schedulingRunOnlyOnce() — REACHABLE SOURCE — PASS. SchedulingSettingsFragment.java:100 display; definition :1150.
- 46/16 SettingsRepositoryImpl.schedulingStartTime(int) — REACHABLE SOURCE — PASS. SchedulingSettingsFragment.java:222 (onPreferenceChange, then Scheduler.setStartAppAlarm); definition :1130.
- 46/21 SettingsRepositoryImpl.showManageAllFilesWarningDialog() — UNREACHABLE closed_by_api_level INFERRED — PASS. Definition :1410; ONLY printed call site in the 16 freshly fetched files: Utils.java:706, the third disjunct of the early-return condition at :704-707; at standard API 27 the first disjunct is TRUE (27 < 30), so the method's callers never reach it.
- 46/26 SettingsRepositoryImpl.shutdownDownloadsComplete(boolean) — REACHABLE SOURCE — PASS. BehaviorSettingsFragment.java:232 (onPreferenceChange); definition :441.
- 46/31 SettingsRepositoryImpl.theme() — REACHABLE SOURCE — PASS. Utils.java:371 (getThemePreference returns `...theme()`); AppearanceSettingsFragment.java:83 display; definition :329.
- 46/36 SettingsRepositoryImpl.unmeteredConnectionsOnly(boolean) — REACHABLE SOURCE — PASS. BehaviorSettingsFragment.java:223 (onPreferenceChange); definition :519.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
