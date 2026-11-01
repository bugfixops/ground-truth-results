# Spot-check — batch 47 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 21 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 47/21 BaseSorting.toString() — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L1: definition BaseSorting.java:70-76; zero outside trigger in greps/L1/grep_all_calls.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt; TorrentSorting instances are constructed widely but only getColumnName()/getDirection() are read (TorrentSortingComparator.java:43-44); Utils.java:924 concats a String `val`, not a sorting object — near-miss rejected; the batch-file settings-family caveat is answered in the verdict: no library in scope receives sorting objects). Stale prose: "stays OPEN IF the merger holds the settings-family caveat that an implicit/framework toString (…". The Phase 3 verdict did not hold that caveat; it flipped the row.

## Sample rows (7 sample-only)

- 47/1 SettingsRepositoryImpl.vibrationNotify() — UNREACHABLE closed_by_api_level INFERRED — PASS. Definition :316-318 freshly confirmed; saved full-tree grep §A (252 app Java files): the ONLY call statements are GATED — AppearanceSettingsFragment.java:187 inside initLegacyNotifySettings (gate :118-119, SDK < O, false at API 27).
- 47/6 SettingsRepositoryImpl.watchDirDeleteFile(boolean) — REACHABLE SOURCE — PASS. StorageSettingsFragment.java:287 (onPreferenceChange, pref_key_watch_dir_delete_file branch); listener bound in ungated onCreate at :197; definition SettingsRepositoryImpl.java:805. CHANGED 2026-11-01 OPEN → REACHABLE.
- 47/11 SettingsRepositoryImpl$Default.foregroundNotifySorting(Context) — REACHABLE SOURCE — PASS. Fallback in getter :373-376; getter called at Utils.java:896 (getForegroundNotifySorting), called from TorrentService.java:139.
- 47/16 SettingsRepositoryImpl$Default.saveTorrentsIn(Context) — REACHABLE SOURCE — PASS. Fallback in getter :708-710; getter called at TorrentEngine.java:1185.
- 47/26 TorrentSorting$SortingColumns$1.\<init\>(String,int) — REACHABLE INFERRED — PASS. Anonymous enum subclass for `none`; instances created at enum \<clinit\> (row 24). Numbering by declaration order, NOT verified against bytecode — merger must confirm (stated in row).
- 47/31 TorrentSorting$SortingColumns$3.compare(TorrentInfo,TorrentInfo,Direction) — REACHABLE INFERRED — PASS. `size` branch :47-57; reached via fromValue("size").compare(…); Utils size asc/desc branches.
- 47/36 TorrentSorting$SortingColumns$6.\<init\>(String,int) — REACHABLE INFERRED — PASS. Anonymous enum subclass for `peers`; created at enum \<clinit\>.

Totals: checked 8 (1 changed + 7 sample-only) — PASS 7, FAIL-prose 1, FAIL-label 0.
