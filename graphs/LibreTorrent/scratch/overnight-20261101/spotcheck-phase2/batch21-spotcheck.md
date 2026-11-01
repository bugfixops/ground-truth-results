# LibreTorrent batch 21 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch21-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): 1, 6, 11, 16, 21, 26, 31, 36. Row 36 is the Phase 1c label change (D5b, REACHABLE SOURCE → OPEN); it is also a sample row, so the check set is 8 rows, not 9.
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (Logger, LogEntry, TorrentSessionImpl, LogDataSource, LogViewModel, SaveLogWorker, AddTorrentParams), `~/workspace/b202122-openclose2-src/grep_parcel_sites_ruleF.txt` as a lead. No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | LogEntry.toStringWithTimeStamp | REACHABLE / SOURCE | PASS | Def LogEntry.java:103-106 (`getTimeStampAsString() + " " + toString()`); call site Logger.java:437 (`entry.toStringWithTimeStamp()` inside write). |
| 6 | Logger.clean | REACHABLE / SOURCE | PASS | Def Logger.java:475-485 (via doClean); caller TorrentSessionImpl.java:1023 (`sessionLogger.clean()` inside enableSessionLogger :1015-1025), itself called from onBeforeStop :1032 (`enableSessionLogger(false)`). |
| 11 | Logger.getNumEntries | REACHABLE / SOURCE | PASS | Def Logger.java:445-458; callers LogDataSource.java:66, :104 and LogViewModel.java:164 — all verified in the local corpus. |
| 16 | Logger.lazyGetOutputBuf | REACHABLE / SOURCE | PASS (citation note) | Def Logger.java:86-92 (private). Every cited internal caller verified: :147, :281, :306, :337, :385, :416, :450. Note: the corpus also has a caller at :247, omitted from the file's list; label unaffected. Proposed correction: add :247 to the caller list, no label change. |
| 21 | Logger.resume | REACHABLE / SOURCE | PASS | Def Logger.java:465-468; callers LogDataSource.java:88, :115, LogViewModel.java:153, SaveLogWorker.java:106 — all verified. |
| 26 | Logger.stopRecording(OutputStream,boolean) | REACHABLE / SOURCE | PASS | Def Logger.java:372-398; call site SaveLogWorker.java:93 (`logger.stopRecording(fout, true)`). |
| 31 | Logger$DataSetChange.<init>(Reason) | REACHABLE / SOURCE | PASS | Def Logger.java:527-530 (delegates to 2-arg ctor :529); construction sites Logger.java:256 (`new DataSetChange(Reason.FILTER)`) and :498 (`new DataSetChange(Reason.NEW_ENTRIES)`). |
| 36 | AddTorrentParams.<init>(Parcel) | OPEN / — | PASS (must-include D5b check) | Def AddTorrentParams.java:77-88. Its only printed construction site is AddTorrentParams.java:112 (`return new AddTorrentParams(source)` inside CREATOR.createFromParcel), i.e. inside batch 22 row 3, which is OPEN; no AddTorrentParams marshalling site (putExtra/getParcelableExtra naming it) appears in the corpus tree — the only putExtra/getParcelableExtra sites are DetailTorrentFragment.java:544 (FileManagerConfig) and AddTorrentActivity.java:359 (a Uri). The D5b revert REACHABLE → OPEN is therefore consistent with the filed dependency rule. The Parcelable convention itself is undecided project-wide; this spot-check does not decide it, it only confirms the filed OPEN follows from the filed rule. |

## Totals

- PASS: 8 / 8. FAIL: 0.
- Proposed corrections: one citation addition only (row 16: add Logger.java:247 to the caller list). No label or confirmed_by correction proposed.
