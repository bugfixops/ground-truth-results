# Spot-check — LibreTorrent batch 72 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch72-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` and the saved grep `~/workspace/b727374-openclose2-src/full_grep_bindservice_20261101.txt` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS Phase 1 round-1 flipped rows 13, 15 named in the file's 2026-11-01 revision notes, PLUS must-include row 21 (already in sample). Phase 1c flipped 0 rows in this batch, as the file states. Total 10 rows.
- Filed labels: 9 REACHABLE proposed, 1 OPEN (row 21).

## Per-row verdicts

- Row 1 — Scheduler.setStopAppAlarm — PASS. Filed REACHABLE SOURCE. Direct calls SchedulingSettingsFragment.java:213 and :229; body Scheduler.java:56–58 delegates to setStartStopAppAlarm with SCHEDULER_WORK_STOP_APP. Direct printed calls = SOURCE as filed.
- Row 6 — TorrentService.handleActions — PASS. Filed REACHABLE SOURCE. Direct call TorrentService.java:194 from onStartCommand; body :214–233 (PAUSE_ALL/RESUME_ALL/PAUSE_RESUME_ALL branches). Direct printed call = SOURCE as filed.
- Row 11 — TorrentService.lambda$forceClearForeground$7 — PASS. Filed REACHABLE INFERRED. Body TorrentService.java:331 `Completable.fromRunnable(() -> updateForegroundNotify(...))` inside forceClearForeground (:329–334). Rx/Completable dispatch unprinted = INFERRED as filed. ($n-to-body mapping not bytecode-verified, as the file itself notes; label does not turn on it.)
- Row 13 — TorrentService.lambda$getInfoListSingle$3 — PASS. Filed REACHABLE INFERRED (Phase 1 round-1 flip, kept). Error lambda TorrentService.java:309–311 inside getInfoListSingle's subscribe (:308). Runs only on an info-list error — a condition, not a blocker, per D12 as cited. Rx dispatch unprinted = INFERRED as filed.
- Row 15 — TorrentService.lambda$startUpdateForegroundNotify$1 — PASS. Filed REACHABLE INFERRED (Phase 1 round-1 flip, kept). Error lambda TorrentService.java:293–295 inside startUpdateForegroundNotify's subscribe (:292). Same D12 condition note as row 13. Rx dispatch unprinted = INFERRED as filed.
- Row 16 — TorrentService.lambda$subscribeCombinedPauseButtonState$6 — PASS. Filed REACHABLE INFERRED. Body TorrentService.java:324–326 `subscribe((paused) -> updateForegroundNotifyActions(...))` inside subscribeCombinedPauseButtonState. Rx dispatch unprinted = INFERRED as filed.
- Row 21 — TorrentService.onBind — PASS AS FILED (OPEN, no flip). Definition TorrentService.java:100–103 returns null. Saved full-tree grep over all 252 app Java files (`full_grep_bindservice_20261101.txt`) shows 0 bindService, 0 unbindService / ServiceConnection hits; only start-service sites for TorrentService (NotificationReceiver, TorrentEngine) plus a comment-only hit. Manifest declaration (checked in `~/workspace/b73-74-src/AndroidManifest.xml`:253–254, `.service.TorrentService`, foregroundServiceType only — no `android:exported`, no intent filter) matches the file's account. OPEN status is correct as filed: no decision flip was ordered for this row, and none is made here.
- Row 26 — TorrentService.setForegroundNotifyActions — PASS. Filed REACHABLE SOURCE. Direct calls TorrentService.java:361 (makeForegroundNotify) and :493 (updateForegroundNotifyActions); body :455–490. Direct printed call = SOURCE as filed.
- Row 31 — TorrentService.stopService — PASS. Filed REACHABLE INFERRED. Only printed caller TorrentService.java:260 (`TorrentService$1.onSessionStopped`); body :164–173. Session dispatch unprinted = INFERRED as filed.
- Row 36 — TorrentService.updateForegroundNotifyActions — PASS. Filed REACHABLE INFERRED. Only printed callers are row 16's Rx lambda (TorrentService.java:324–326) and handleSettingsChanged :273 (itself Rx-subscribed, :126); body :492–495. INFERRED as filed.

## Totals

- Rows checked: 10. PASS: 10. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited. Row 21 stays OPEN pending a merger judgement, exactly as filed.
