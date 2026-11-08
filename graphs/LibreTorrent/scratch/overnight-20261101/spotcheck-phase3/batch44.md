# Spot-check — batch 44 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 44/1 SettingsRepositoryImpl.feedRemoveDuplicates(boolean) — REACHABLE SOURCE — PASS. FeedSettingsFragment.java:158 (onPreferenceChange, pref_key_feed_remove_duplicates branch); listener bound ungated at :109; definition :1260.
- 44/6 SettingsRepositoryImpl.foregroundNotifySorting() — REACHABLE SOURCE — PASS. Utils.java:896 inside getForegroundNotifySorting (:892-911), reached from TorrentService.java:139 setFilterAndSorting; also AppearanceSettingsFragment.java:106 display binding; definition :373.
- 44/11 SettingsRepositoryImpl.ipFilteringFile(String) — REACHABLE SOURCE — PASS. NetworkSettingsFragment.java:390 (fileChoose result handler); launcher launched by fileChooseDialog :284-296, called from the click listener registered in ungated onCreate at :213-214; definition :688.
- 44/16 SettingsRepositoryImpl.lambda$observeSettingsChanged$2 — REACHABLE INFERRED — PASS. Compiler-generated lambda inside observeSettingsChanged (:195-211), descriptor-matched: the Flowable.create emitter lambda; runs on subscription at TorrentEngine.java:240-241 / TorrentService.java:125-126; Rx dispatch not printed, hence INFERRED.
- 44/21 SettingsRepositoryImpl.logDhtFilter() — REACHABLE SOURCE — PASS. TorrentEngine.java:1624 (handleSettingsChanged) and internally readSessionSettings:254; definition :1345.
- 44/26 SettingsRepositoryImpl.logPortmapFilter(boolean) — REACHABLE SOURCE — PASS. LogViewModel.java:131 (paramsCallback, BR.logPortmapFilter branch); definition SettingsRepositoryImpl.java:1377. CHANGED 2026-11-01 OPEN → REACHABLE; LogViewModel.java paramsCallback onPropertyChanged (callback registered LogViewModel.java:89).
- 44/31 SettingsRepositoryImpl.logging() — REACHABLE SOURCE — PASS. TorrentEngine.java:1614 and internally readSessionSettings:251; definition :1306.
- 44/36 SettingsRepositoryImpl.maxActiveTorrents(int) — REACHABLE SOURCE — PASS. LimitationsSettingsFragment.java:230 (onPreferenceChange, pref_key_max_active_torrents branch); listener bound in ungated onCreate at :142; definition :922.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
