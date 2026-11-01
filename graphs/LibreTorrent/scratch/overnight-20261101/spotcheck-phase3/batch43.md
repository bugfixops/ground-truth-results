# Spot-check — batch 43 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 43/1 SettingsRepositoryImpl.autostart(boolean) — REACHABLE SOURCE — PASS. Fresh: BehaviorSettingsFragment.java:203 pref.autostart((boolean)newValue) in onPreferenceChange (getter also :74); definition SettingsRepositoryImpl.java:415. Prior proposal: OPEN; closed here.
- 43/6 SettingsRepositoryImpl.customBatteryControl() — REACHABLE SOURCE — PASS. TorrentEngine.java:991 and :1025; definition :487; also fresh BehaviorSettingsFragment.java:120 setChecked(pref.customBatteryControl()).
- 43/11 SettingsRepositoryImpl.defaultTrackersList(String) — REACHABLE SOURCE — PASS. Fresh: BehaviorSettingsFragment.java:241 pref.defaultTrackersList((String)newValue) in onPreferenceChange; definition :961. Prior proposal: OPEN; closed here.
- 43/16 SettingsRepositoryImpl.enableIpFiltering() — REACHABLE SOURCE — PASS. TorrentEngine.java:1047 (handleOnSessionStarted) and :1555; definition :669; also fresh NetworkSettingsFragment.java:198 setChecked(pref.enableIpFiltering()).
- 43/21 SettingsRepositoryImpl.enableNatPmp(boolean) — REACHABLE SOURCE — PASS. Fresh: NetworkSettingsFragment.java:332 pref.enableNatPmp((boolean) newValue) in onPreferenceChange; definition :623. Prior proposal: OPEN; closed here.
- 43/26 SettingsRepositoryImpl.enableSchedulingStart() — REACHABLE SOURCE — PASS. Fresh: SchedulingSettingsFragment.java:72 enableStart.setChecked(pref.enableSchedulingStart()) in bind; definition :1098. Prior proposal: OPEN (Scheduler.java does not call it); closed here via the scheduling fragment.
- 43/31 SettingsRepositoryImpl.enableUpnp(boolean) — REACHABLE SOURCE — PASS. Fresh: NetworkSettingsFragment.java:329 pref.enableUpnp((boolean) newValue) in onPreferenceChange; definition :610. Prior proposal: OPEN; closed here.
- 43/36 SettingsRepositoryImpl.encryptOutConnectionsMode() — REACHABLE SOURCE — PASS. TorrentEngine.java:1113 and internally readSessionSettings:229; definition :656; also fresh NetworkSettingsFragment.java:190 var type = pref.encryptOutConnectionsMode().

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
