# Spot-check — LibreTorrent batch 74 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch74-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` and the saved greps `~/workspace/b727374-openclose2-src/full_grep_apigate_20261101.txt` and `~/workspace/overnight/stream-A/greps/grep_recheck_7374_apigate_complete.txt` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS Phase 1 flipped row 23 (OPEN → REACHABLE, open-closing pass) and must-include row 9 (OPEN → UNREACHABLE, round 2; row 1 also a round-2 flip and already in sample). Phase 1c flipped 0 rows in this batch. Total 10 rows.
- Filed labels: 8 REACHABLE, 2 UNREACHABLE (rows 1, 9) among checked rows.

## Per-row verdicts

- Row 1 — ManageAllFilesWarningDialog.onCreateDialog — PASS. Filed UNREACHABLE INFERRED, kind closed_by_api_level (Phase 1 round-2 flip, kept; 2026-11-01 re-check survived). Definition ManageAllFilesWarningDialog.java:44–65 (`super.onCreateDialog` :45, `buildDialog(...)` :56–64). Creation is closed at API 27 via batch 73 rows 39–40: sole newInstance caller Utils.java:713, behind the early return at Utils.java:704–707 (`SDK_INT < R` true at API 27, R = 30). The complete-tree re-check grep confirms the sole caller and zero hits in the 29 missing files and in XML. API-gate evidence verified as filed.
- Row 6 — PermissionManager.checkNotificationsPermissions — PASS. Filed REACHABLE SOURCE. Called PermissionManager.java:147 (checkPermissions, itself reached from MainActivity.java:177) and :110 (requestPermissions). Direct printed calls = SOURCE as filed.
- Row 9 — PermissionManager.lambda$new$0 — PASS. Filed UNREACHABLE INFERRED, kind closed_by_api_level (Phase 1 round-2 flip, kept; 2026-11-01 re-check survived). The StartActivityForResult result lambda is at PermissionManager.java:63–66 (calls `callback.onStorageResult(...)`); its field `manageExternalStoragePermission` (declared :44, private) has exactly one registration, :61–67, gated at :60 on `SDK_INT >= R && hasManageExternalStoragePermission` — the SDK term is false at API 27 (R = 30) — and exactly one launch, :100–104, behind the same `SDK_INT >= R` gate at :99. The complete-tree re-check grep confirms the sole registration/launch and zero hits in the 29 missing files and in XML; other registerForActivityResult hits are unrelated launchers in other classes. API-gate evidence verified as filed.
- Row 11 — PermissionManager.requestPermissions — PASS. Filed REACHABLE SOURCE. Called MainActivity.java:178 and :427. Direct printed calls = SOURCE as filed.
- Row 16 — TorrentNotifier.<init> — PASS. Filed REACHABLE SOURCE. Single construction site TorrentNotifier.java:69 (`INSTANCE = new TorrentNotifier(appContext)`) inside getInstance; private constructor at :75. Direct printed construction = SOURCE as filed.
- Row 21 — TorrentNotifier.makeMovingTorrentNotify — PASS. Filed REACHABLE SOURCE. Called TorrentEngine.java:1340 (torrent-moved listener branch). Direct printed call = SOURCE as filed.
- Row 23 — TorrentNotifier.makeNotifyChans — PASS. Filed REACHABLE SOURCE (Phase 1 flip, kept). Printed caller MainApplication.java:70 `TorrentNotifier.getInstance(this).makeNotifyChans()` inside onCreate (:46); MainApplication is the manifest application class (AndroidManifest.xml:32 `android:name="MainApplication"`). Body runs at API 27 (SDK >= O gate at TorrentNotifier.java:82 is true). Direct printed call = SOURCE as filed.
- Row 26 — TorrentNotifier.makeTorrentFinishedNotify — PASS. Filed REACHABLE SOURCE. Called TorrentEngine.java:1311 (onTorrentFinished listener). Direct printed call = SOURCE as filed.
- Row 31 — AddFeedActivity.onCreate — PASS. Filed REACHABLE INFERRED. Body AddFeedActivity.java:47–68 (finds or creates and shows the AddFeedDialog at :61/:63/:66). Framework activity lifecycle dispatch unprinted = INFERRED as filed.
- Row 36 — AddFeedDialog.checkUrlField — PASS. Filed REACHABLE SOURCE. Called AddFeedDialog.java:381 (inside addChannel) and :397 (inside updateChannel). Direct printed calls = SOURCE as filed.

## Totals

- Rows checked: 10. PASS: 10. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited. Rows 1 and 9 stay UNREACHABLE closed_by_api_level under D10 Group Y as filed, with the API-gate evidence verified above.
