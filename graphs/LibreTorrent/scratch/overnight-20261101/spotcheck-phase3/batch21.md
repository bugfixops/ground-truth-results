# Spot-check — batch 21 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (2)

Both labels/kinds/confirmed_by are correct per L1 (full-scope greps as in batch 10); both FAIL on stale prose only.

- 21/39 AddTorrentParams.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "stays OPEN pending the project-wide hashCode rule — see conditional flip table in round-2 note above" and "REVISION 2026-11-01 Phase 1c (D6 printed-trigger rule): stays OPEN — no printed trigger". (L1 basis: definition AddTorrentParams.java:123-125, a String call inside the body; zero external .hashCode() in grep_all_calls.txt; zero hash collection in grep_hash_collections.txt; consumers use List/ArrayList only.)
- 21/40 AddTorrentParams.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "stays OPEN pending the project-wide toString rule — see conditional flip table in round-2 note above" and "REVISION 2026-11-01 Phase 1c (D7 parallel printed-trigger rule): stays OPEN — no printed trigger outside any OPEN toString body". (L1 basis: definition :129-142; zero explicit .toString()/log/concat/format/setText/binding site naming an AddTorrentParams in the L1 greps; its body's `", tags=" + tags` is a trigger for TagInfo.toString (31/25), not for this row.)

## Sample rows (8)

- 21/1 LogEntry.toStringWithTimeStamp — REACHABLE SOURCE — PASS. Definition LogEntry.java:103-106; call site Logger.java:437 in private write :425-443.
- 21/6 Logger.clean — REACHABLE SOURCE — PASS. Definition Logger.java:475-485; external caller TorrentSessionImpl.java:1023 inside enableSessionLogger(false) :1015-1025, itself called from onBeforeStop.
- 21/11 Logger.getNumEntries — REACHABLE SOURCE — PASS. Definition Logger.java:445-458; call sites LogDataSource.java:66, :104 and LogViewModel.java:164.
- 21/16 Logger.lazyGetOutputBuf — REACHABLE SOURCE — PASS. Definition Logger.java:86-92 (private); internal callers Logger.java:147, :281, :306, :337, :385, :416, :450, all in REACHABLE rows.
- 21/21 Logger.resume — REACHABLE SOURCE — PASS. Definition Logger.java:465-468; call sites LogDataSource.java:88, :115, LogViewModel.java:153, SaveLogWorker.java:106.
- 21/26 Logger.stopRecording(OutputStream,boolean) — REACHABLE SOURCE — PASS. Definition Logger.java:372-398; call site SaveLogWorker.java:93 (WorkManager dispatch for SaveLogWorker INFERRED; the call site naming the method is printed).
- 21/31 Logger$DataSetChange.\<init\>(Reason) — REACHABLE SOURCE — PASS. Definition Logger.java:527-530; construction sites Logger.java:256 and :498.
- 21/36 AddTorrentParams.\<init\>(Parcel) — OPEN — PASS. Definition AddTorrentParams.java:77-88; route passes through batch 22 row 3 (createFromParcel), which is OPEN for lack of a printed marshalling site — the dependency premise is unchanged by Phase 3 (22/3 was not flipped). OPEN confirmed_by is —, as required.

Totals: checked 10 (2 changed + 8 sample-only) — PASS 8, FAIL-prose 2, FAIL-label 0.
