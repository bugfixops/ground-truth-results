# Spot-check — batch 19 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 19/1 TorrentBuilder.lambda$build$0 — REACHABLE INFERRED — PASS. TorrentBuilder.java:177 Single.fromCallable body printed; execution on Rx subscription (CreateTorrentViewModel.java:171-173) through unprinted Rx dispatch, hence INFERRED.
- 19/6 TorrentBuilder.setFileNameFilter — REACHABLE SOURCE — PASS. Definition TorrentBuilder.java:155-160; call CreateTorrentViewModel.java:198+ in makeBuilder().
- 19/11 TorrentBuilder$1.\<init\> — REACHABLE SOURCE — PASS. Anonymous Listener constructed at TorrentBuilder.java:182 inside subscribeProgress() (row 10); implicit ctor invoked by that `new` expression.
- 19/16 TorrentBuilder$TorrentVersion.\<init\> — REACHABLE INFERRED — PASS. Definition TorrentBuilder.java:83-85; invoked implicitly once per constant during row 15's \<clinit\> (INFERRED JVM step).
- 19/21 FixedRingBuffer.add(Iterable) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Prior OPEN verdict superseded on a saved full-tree grep (fresh FixedRingBuffer.java, 230 lines, SHA 0a1ac818…).
- 19/26 FixedRingBuffer.getAllocatedSize — UNREACHABLE no_trigger_in_app INFERRED — PASS. Same saved full-tree grep basis as row 21.
- 19/31 FixedRingBuffer.remove — UNREACHABLE no_trigger_in_app INFERRED — PASS. Same saved full-tree grep basis as row 21.
- 19/36 FixedRingBuffer$FixedRingBufferIterator.\<init\> — REACHABLE SOURCE — PASS. Private class FixedRingBuffer.java:214+; ctor invoked at FixedRingBuffer.java:211 inside iterator() (row 30), reached via Logger.java:250 for-loop.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
