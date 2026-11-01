# Spot-check — batch 3 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 26 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 3/26 TagInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per coordinator D36: no SelectionTracker\<TagItem\> site in greps/L1/grep_selectiontracker.txt; both delegators UNREACHABLE in current work — 10/39 drawer TagItem.hashCode and 11/7 tag TagItem.hashCode; zero other triggers in the L1 full-scope grep). Stale prose: "REVISION 2026-11-01 (D6/D1): D6 decides this row stays OPEN (neither delegator REACHABLE …)". Note: this row was a stays-OPEN entry in the L1 table and is flipped only by the coordinator verdict; the coordinator verdict is the one applied in the work file.

## Sample rows (7 sample-only)

- 3/1 RepositoryHelper.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — PASS. No explicit ctor; only static accessors; no construction printed.
- 3/6 FileAlreadyExistsException.\<init\>() — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :24; no `new FileAlreadyExistsException` in fresh prints (weakest in batch; "grep owed" noted in row).
- 3/11 NoFilesSelectedException.\<init\>(String) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed construction is the 0-arg overload (AddTorrentViewModel:493).
- 3/16 Logger.getEntry — UNREACHABLE no_trigger_in_app INFERRED — PASS. Printed logger callers use getNumEntries/pause/resume/startRecording/stopRecording/write, never getEntry(int).
- 3/21 TorrentInfoProvider.getInstance(TorrentEngine,TagRepository) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Printed service caller uses the Context overload (TorrentService:110), never this overload.
- 3/31 PriorityConverter.convert(Priority) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Saved full-repo grep finds six convert call sites, all other overloads, zero with a single org.libtorrent4j.Priority argument.
- 3/36 TorrentDownloadImpl.getMaxConnections — UNREACHABLE no_trigger_in_app INFERRED — PASS. No printed caller via the interface in fresh files; internal code uses the setter, not the getter.

Totals: checked 8 (1 changed + 7 sample-only) — PASS 7, FAIL-prose 1, FAIL-label 0.
