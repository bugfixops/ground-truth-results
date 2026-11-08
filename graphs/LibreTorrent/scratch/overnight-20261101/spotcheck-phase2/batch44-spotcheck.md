# LibreTorrent batch 44 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch44-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b444546-src/` (SettingsRepositoryImpl, TorrentEngine, Utils, fragments) and
  `~/workspace/b444748-openclose-src/LogViewModel.java`. No connector fetch was needed;
  no merge-ready file was edited; no label was flipped.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1 (2026-11-01 open-close)
  changed rows 22, 24, 28, 30, 32 (26 already in the sample).
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.feedRemoveDuplicates(boolean) | REACHABLE SOURCE | PASS | FeedSettingsFragment.java:158 `pref.feedRemoveDuplicates((boolean)newValue)` in onPreferenceChange; listener bound ungated at :109; getter also :108. |
| 6 | SettingsRepositoryImpl.foregroundNotifySorting() | REACHABLE SOURCE | PASS | Utils.java:896 `String val = pref.foregroundNotifySorting()` inside getForegroundNotifySorting, reached from TorrentService.java:139; also AppearanceSettingsFragment.java:106 display. |
| 11 | SettingsRepositoryImpl.ipFilteringFile(String) | REACHABLE SOURCE | PASS | NetworkSettingsFragment.java:390 `pref.ipFilteringFile(path.toString())` in the file-choose result handler (launcher :284-296, click listener in ungated onCreate :213-214). Getter also TorrentEngine.java:1048,:1556,:1564. |
| 16 | SettingsRepositoryImpl.lambda$observeSettingsChanged$2 | REACHABLE INFERRED | PASS | ObserveSettingsChanged body SettingsRepositoryImpl.java:195-211; subscribed at TorrentEngine.java:240-241 and TorrentService.java:125-126. Rx dispatch INFERRED, as filed. Caveat carried from the file: $ numbering is descriptor-matched, not bytecode-verified; the label (not the number) is what passes here. |
| 21 | SettingsRepositoryImpl.logDhtFilter() | REACHABLE SOURCE | PASS | TorrentEngine.java:1624 (handleSettingsChanged) and internally readSessionSettings:254. |
| 22 | SettingsRepositoryImpl.logDhtFilter(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:125 (paramsCallback, BR.logDhtFilter branch) `pref.logDhtFilter(mutableParams.isLogDhtFilter())`; callback registered :89, ctor :77. Filed line :125 matches the local copy exactly. |
| 24 | SettingsRepositoryImpl.logPeerFilter(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:128 (BR.logPeerFilter branch) `pref.logPeerFilter(mutableParams.isLogPeerFilter())`. Filed line :128 matches. |
| 26 | SettingsRepositoryImpl.logPortmapFilter(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:131 (BR.logPortmapFilter branch) `pref.logPortmapFilter(mutableParams.isLogPortmapFilter())`. Filed line :131 matches. |
| 28 | SettingsRepositoryImpl.logSessionFilter(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:122 (BR.logSessionFilter branch) `pref.logSessionFilter(mutableParams.isLogSessionFilter())`. Filed line :122 matches. |
| 30 | SettingsRepositoryImpl.logTorrentFilter(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:134 (BR.logTorrentFilter branch) `pref.logTorrentFilter(mutableParams.isLogTorrentFilter())`. Filed line :134 matches. |
| 31 | SettingsRepositoryImpl.logging() | REACHABLE SOURCE | PASS | TorrentEngine.java:1614 (handleSettingsChanged) and internally readSessionSettings:251. |
| 32 | SettingsRepositoryImpl.logging(boolean) | REACHABLE SOURCE (Phase 1 open-close) | PASS | LogViewModel.java:119 (BR.logging branch) `pref.logging(logging)`. Filed line :119 matches. |
| 36 | SettingsRepositoryImpl.maxActiveTorrents(int) | REACHABLE SOURCE | PASS | LimitationsSettingsFragment.java:230 `pref.maxActiveTorrents(value)` in onPreferenceChange; listener bound in ungated onCreate at :142. |

## Totals

- Checked: 13. PASS: 13. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: the file's UNREACHABLE rows 17-20 (ledIndicator, closed_by_api_level) were not in
  this batch's check set (sample + Phase 1 open-close rows only) and were not re-judged here.
  The gates cited for them were, however, seen in the same prints (AppearanceSettingsFragment
  :118-119 SDK < O gate; TorrentNotifier.java:276 early return, :289-:290 gated reads).
