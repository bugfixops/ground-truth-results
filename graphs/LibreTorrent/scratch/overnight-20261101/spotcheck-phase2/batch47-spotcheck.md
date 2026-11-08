# LibreTorrent batch 47 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch47-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only — the 281-file
  corpus in `~/workspace/overnight/stream-A/corpus/java/` and
  `~/workspace/b444748-openclose-src/StorageSettingsFragment.java`. No connector fetch was
  needed; no merge-ready file was edited; no label was flipped.
- Rows checked (11): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1 changed rows 2, 4, 13
  (1, 6, 21 already in the sample), plus must-include row 21.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.vibrationNotify() | UNREACHABLE closed_by_api_level INFERRED (Phase 1 round 2 flip) | PASS | Corpus-wide grep: only call statements are AppearanceSettingsFragment.java:187 inside initLegacyNotifySettings (gate :118-119, SDK < O, false at API 27) and TorrentNotifier.java:286 inside applyLegacyNotifySettings (early return :276 at SDK >= O, before :286). Neither executes at API 27. Def SettingsRepositoryImpl.java:316-318. |
| 2 | SettingsRepositoryImpl.vibrationNotify(boolean) | UNREACHABLE closed_by_api_level INFERRED (Phase 1 round 2 flip) | PASS | Corpus-wide grep: only call statement AppearanceSettingsFragment.java:247 (onPreferenceChange branch); listener bound only inside initLegacyNotifySettings (:188, vibration binding), gated at :118-119. Branch never fires at API 27. Def SettingsRepositoryImpl.java:322-328. |
| 4 | SettingsRepositoryImpl.watchDir(boolean) | REACHABLE SOURCE (Phase 1 round 1 flip) | PASS | StorageSettingsFragment.java:281 `pref.watchDir((boolean) newValue)` in onPreferenceChange; listener bound in ungated onCreate at :170. Filed lines match the local copy exactly. |
| 6 | SettingsRepositoryImpl.watchDirDeleteFile(boolean) | REACHABLE SOURCE (Phase 1 round 1 flip) | PASS | StorageSettingsFragment.java:287 `pref.watchDirDeleteFile((boolean) newValue)`; listener bound in ungated onCreate at :197. Filed lines match exactly. |
| 11 | SettingsRepositoryImpl$Default.foregroundNotifySorting(Context) | REACHABLE SOURCE | PASS | Fallback argument in getter SettingsRepositoryImpl.java:373-376; getter called at Utils.java:896 (getForegroundNotifySorting), called from TorrentService.java:139. |
| 13 | SettingsRepositoryImpl$Default.ledIndicatorColorNotify(Context) | UNREACHABLE closed_by_api_level INFERRED (Phase 1 round 2 flip) | PASS | Def SettingsRepositoryImpl.java:53. Corpus-wide grep: sole call statement is the fallback argument inside getter ledIndicatorColorNotify() at :342-344; the :250 site calls the (int) setter, not this overload. The getter is itself closed_by_api_level (batch 44 row 17: AppearanceSettingsFragment.java:180 gated :118-119; TorrentNotifier.java:290 after early return :276), so the fallback is never evaluated at API 27. Flips together with batch 44 row 17, as filed. |
| 16 | SettingsRepositoryImpl$Default.saveTorrentsIn(Context) | REACHABLE SOURCE | PASS | Fallback in getter SettingsRepositoryImpl.java:708-710; getter called at TorrentEngine.java:1185 and Utils.java:640. |
| 21 | BaseSorting.toString() | OPEN — MUST-INCLUDE, left OPEN under D7 | PASS (OPEN stands, not flipped) | Def BaseSorting.java:70-76. Corpus grep: no explicit `.toString()` on a BaseSorting/TorrentSorting object and no Log/concat/String.valueOf site for a sorting object (the only toString hits in the sorting files are enum toStrings: BaseSorting.java:33 Direction.toString, TorrentSorting.java:106 column.toString). Left OPEN as filed; this spot-check does not decide the implicit/framework-toString question. |
| 26 | TorrentSorting$SortingColumns$1.<init> | REACHABLE INFERRED | PASS | Anonymous enum subclass for `none`, the first SortingColumns constant (TorrentSorting.java:28+); created at enum <clinit>. Numbering by declaration order, not bytecode-verified (caveat carried from the file; label passes). |
| 31 | TorrentSorting$SortingColumns$3.compare | REACHABLE INFERRED | PASS | `size` branch (third constant, after none/name) TorrentSorting.java:47-57; reached via fromValue("size").compare(...) (TorrentSortingComparator.java:43-44) and Utils size branches. |
| 36 | TorrentSorting$SortingColumns$6.<init> | REACHABLE INFERRED | PASS | Anonymous enum subclass for `peers`, the sixth SortingColumns constant (TorrentSorting.java:80+); created at enum <clinit>. Same numbering caveat as row 26. |

## Totals

- Checked: 11. PASS: 11. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: row 21 stays OPEN by design; it is counted as PASS here only in the sense that
  "OPEN as filed" re-derives (no printed caller was found, and no convention deciding it
  was adopted by this spot-check).
