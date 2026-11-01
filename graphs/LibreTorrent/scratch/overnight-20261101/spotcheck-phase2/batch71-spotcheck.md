# Spot-check — LibreTorrent batch 71 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch71-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE proposed.

## Per-row verdicts

- Row 1 — PowerReceiver.getFilter — PASS. Filed REACHABLE SOURCE. Definition PowerReceiver.java:53–64. Printed caller TorrentEngine.java:1005 `registerReceiver(powerReceiver, PowerReceiver.getFilter())`, inside the `batteryControl || onlyCharging` branch at :1004–1005 (custom-filter branch at :1001 is the other arm). Direct printed call = SOURCE as filed.
- Row 6 — SchedulerReceiver.onStopApp — PASS. Filed REACHABLE INFERRED. Direct call SchedulerReceiver.java:59 from onReceive; body :84–103, gate `enableSchedulingShutdown()` at :86, `setStartAppAlarm` at :92 (the file's note that onStopApp calls setStartAppAlarm, not setStopAppAlarm, is correct). INFERRED because onReceive is broadcast dispatch, unprinted.
- Row 11 — FeedDownloaderWorker.fetchTorrent — PASS. Filed REACHABLE INFERRED. Call FeedDownloaderWorker.java:101 inside fetchTorrents; body :109–190. Chain via doWork (WorkManager dispatch unprinted) = INFERRED as filed.
- Row 16 — FeedFetcherWorker.doWork — PASS. Filed REACHABLE INFERRED. Body FeedFetcherWorker.java:74–105: deleteOldItems :83, action switch FETCH_CHANNEL :94–95, FETCH_CHANNEL_LIST :97–98, FETCH_ALL_CHANNELS :100–101. WorkManager dispatch unprinted = INFERRED as filed.
- Row 21 — FeedFetcherWorker.filterItems — PASS. Filed REACHABLE INFERRED. Call FeedFetcherWorker.java:167 from fetchChannel; body :189–194. Chain via doWork = INFERRED as filed.
- Row 26 — SaveLogWorker.<clinit> — PASS. Filed REACHABLE INFERRED. Static TAG at SaveLogWorker.java:47 (`getSimpleName()`, not a compile-time constant), so a <clinit> exists; first printed class reference LogViewModel.java:208 `OneTimeWorkRequest.Builder(SaveLogWorker.class)`. Class-init dispatch unprinted = INFERRED as filed.
- Row 31 — SaveLogWorker.saveLog — PASS. Filed REACHABLE INFERRED. Call SaveLogWorker.java:81 from doWork; body :84–110, showSuccessToast :97, resume in finally :105–106. Chain via doWork = INFERRED as filed.
- Row 36 — Scheduler.cancelStopAppAlarm — PASS. Filed REACHABLE SOURCE. Direct call SchedulingSettingsFragment.java:217; body Scheduler.java:70–78 (PendingIntent for SchedulerReceiver, AlarmManager.cancel :77). Direct printed call = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited.
