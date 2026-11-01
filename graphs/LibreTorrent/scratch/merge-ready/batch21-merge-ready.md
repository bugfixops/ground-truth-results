# LibreTorrent batch 21 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 21 only, 40 methods, no other batch, no other app, no device replay, no Aegis.
- Source: existing proposal `~/workspace/libretorrent-batch21-proposal.md` (plus its Agent 4 update header: 37/0/3) used as an INPUT / lead list only. Every row below was re-derived in this pass against source freshly fetched from branch `work-2026-10-31` via the GitHub connector, one file at a time with pauses. No verdict was copied without that re-check. In particular, the four Agent 4 resolutions (clean, doClean, getMaxStoredLogs, setMaxStoredLogs) are now confirmed against freshly fetched `TorrentSessionImpl.java`, not carried from the local corpus.
- Membership verified first, not guessed: exactly the 40 batch-21 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (local plan copy `~/workspace/agent27-plan.tsv`, plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order. Plan status is a generator candidate, not evidence.
- Printed source freshly fetched in this pass, saved in `~/workspace/b202122-src/`, no fresh HTTP 429 hit, no `search_code` result used as evidence for any row:
  - `org/proninyaroslav/libretorrent/core/logger/Logger.java` — SHA `97ab16a7…`, 539 lines.
  - `org/proninyaroslav/libretorrent/core/logger/LogEntry.java` — SHA `c0418b28…`, 115 lines.
  - `org/proninyaroslav/libretorrent/core/model/session/SessionLogger.java` — SHA `f51ba318…`, 203 lines.
  - `org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java` — SHA `aef9618c…`, 1721 lines.
  - `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — SHA `17d06efe…`, 1659 lines.
  - `org/proninyaroslav/libretorrent/core/model/AddTorrentParams.java` — SHA `7e349c3d…`, 144 lines.
  - `org/proninyaroslav/libretorrent/ui/log/LogDataSource.java` — SHA `db760e76…`, 119 lines.
  - `org/proninyaroslav/libretorrent/ui/log/LogViewModel.java` — SHA `f6374daf…`, 228 lines.
  - `org/proninyaroslav/libretorrent/service/SaveLogWorker.java` — SHA `6020734d…`, 130 lines.
  - `org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel.java` — SHA `bec2f6ee…`, 575 lines.
- `confirmed_by` convention used here, per row (not decided project-wide): SOURCE = a printed app-code line names the method (direct call, construction, or an internal call from a REACHABLE method printed in this pass); INFERRED = unprinted framework/library/Rx/JVM dispatch where the definition plus registration, thread creation, or first use is printed. Under a whole-route INFERRED convention, SOURCE rows whose routes pass through unprinted dispatch would flip to INFERRED; labels are unaffected. This convention is recorded, not decided.

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **REACHABLE proposed: 37 / 40 (SOURCE 33 / INFERRED 4)**
- **UNREACHABLE proposed: 0**
- **OPEN: 3 / 40 (rows 38, 39, 40 — the AddTorrentParams describeContents/hashCode/toString trio)**
- **Verified for merge: 0**

## Trunks (fresh prints)

- Logger trunk: `SessionLogger` extends `Logger` (SessionLogger.java:111-115 `SessionLogger() { super(1); }`, constructed at TorrentSessionImpl.java:170, `getLogger` at :181); `TorrentSessionImpl` calls `sessionLogger.send(alert)` at :1103, `enableSessionLogger` at :1015-1025, `applyMaxStoredLogs` at :1408-1413. Log UI trunk: `LogViewModel` obtains the logger at :72 (`engine.getSessionLogger()`); `LogDataSource` (Paging `PositionalDataSource`) subscribes at :42 and calls logger methods in `loadInitial`/`loadRange`. Save trunk: `LogViewModel.saveLog` → WorkManager `SaveLogWorker` (WorkManager dispatch INFERRED, standard registration as in batch 14) → `SaveLogWorker.saveLog` lines :87-106.
- AddTorrentParams trunk: constructed at `AddTorrentViewModel.java:510` (10-arg ctor) and `TorrentEngine.java:1187` (inside `addTorrentSync(Uri, TorrentMetaInfo, Uri)`); `CREATOR` field at AddTorrentParams.java:109-119.

## Table — 40 rows, plan order

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | LogEntry.toStringWithTimeStamp | REACHABLE | SOURCE | Def LogEntry.java:103-106 (calls getTimeStampAsString + toString). Call site Logger.java:437 (`entry.toStringWithTimeStamp() : entry.toString()` in private write :425-443). |
| 2 | Logger.<init> | REACHABLE | SOURCE | Def Logger.java:57-64 (int maxStoredLogs). Construction via subclass: SessionLogger.java:111-115 (`SessionLogger() { super(1); }`); SessionLogger constructed at TorrentSessionImpl.java:170. |
| 3 | Logger.addFilter | REACHABLE | SOURCE | Def Logger.java:202-221. Call site SessionLogger.java:200 (`addFilter(addFilters)` in applyFilterParams). |
| 4 | Logger.applyFilters | REACHABLE | SOURCE | Def Logger.java:319-327 (private). Internal callers Logger.java:152 (swapBuffers) and :251 (forceFilterBuf), both REACHABLE rows. |
| 5 | Logger.calcInitBufCapacity | REACHABLE | SOURCE | Def Logger.java:94-97 (private). Internal callers Logger.java:68 (lazyGetInputBuf) and :89 (lazyGetOutputBuf), both REACHABLE rows. |
| 6 | Logger.clean | REACHABLE | SOURCE | Def Logger.java:475-485. External caller freshly printed: TorrentSessionImpl.java:1023 (`sessionLogger.clean()` inside enableSessionLogger(false) :1015-1025, itself called from onBeforeStop). This confirms the Agent 4 resolution on fresh evidence. |
| 7 | Logger.doClean | REACHABLE | SOURCE | Def Logger.java:487-499 (private). Internal callers Logger.java:182 (setMaxStoredLogs) and :480 (clean), both REACHABLE rows. |
| 8 | Logger.forceFilterBuf | REACHABLE | SOURCE | Def Logger.java:244-257 (private). Internal callers Logger.java:216 (addFilter) and :237 (removeFilter), both REACHABLE rows. |
| 9 | Logger.getEntries | REACHABLE | SOURCE | Def Logger.java:271-298. Call sites LogDataSource.java:70, :74, :78 (loadInitial/loadRange). |
| 10 | Logger.getMaxStoredLogs | REACHABLE | SOURCE | Def Logger.java:190-200. External caller freshly printed: TorrentSessionImpl.java:1410 (`sessionLogger.getMaxStoredLogs()` in applyMaxStoredLogs :1408-1413). This confirms the Agent 4 resolution on fresh evidence. Note: the log-settings preference `pref.maxLogSize()` is a different method and is not cited here. |
| 11 | Logger.getNumEntries | REACHABLE | SOURCE | Def Logger.java:445-458. Call sites LogDataSource.java:66, :104 and LogViewModel.java:164. |
| 12 | Logger.isPaused | REACHABLE | SOURCE | Def Logger.java:470-473. Call sites LogDataSource.java:59, :97 and LogViewModel.java:73. |
| 13 | Logger.isRecording | REACHABLE | SOURCE | Def Logger.java:345-355. Call sites LogViewModel.java:74, :188 and SaveLogWorker.java:92. |
| 14 | Logger.lambda$submitDataSetChanged$0 | REACHABLE | INFERRED | Lambda body Logger.java:170 (`sender.submit(() -> dataSetChangedPublish.onNext(change))` inside submitDataSetChanged). Executor dispatch unprinted, hence INFERRED. $n numbering source-order, NOT bytecode-verified. |
| 15 | Logger.lazyGetInputBuf | REACHABLE | SOURCE | Def Logger.java:65-84 (private). Internal callers Logger.java:104 (send), :144 (swapBuffers), :246 (forceFilterBuf), all REACHABLE rows. Also starts pendingThread (row 19). |
| 16 | Logger.lazyGetOutputBuf | REACHABLE | SOURCE | Def Logger.java:86-92 (private). Internal callers Logger.java:147, :281, :306, :337, :385, :416, :450, all in REACHABLE rows. |
| 17 | Logger.observeDataSetChanged | REACHABLE | SOURCE | Def Logger.java:259-262. Call site LogDataSource.java:42 (`logger.observeDataSetChanged().subscribe(...)` in ctor). Rx subscribe dispatch INFERRED; the call site naming the method is printed. |
| 18 | Logger.pause | REACHABLE | SOURCE | Def Logger.java:460-463. Call sites LogDataSource.java:60, :98, LogViewModel.java:142, SaveLogWorker.java:87. |
| 19 | Logger.periodicSwapBuffers | REACHABLE | INFERRED | Def Logger.java:113-137 (private loop, calls swapBuffers :122). Started via method reference Logger.java:71 (`new Thread(this::periodicSwapBuffers)`) + `pendingThread.start()` :72; Thread.start → run dispatch unprinted, hence INFERRED. Same caveat as batch 16's ServerRunnable thread dispatch. |
| 20 | Logger.removeFilter | REACHABLE | SOURCE | Def Logger.java:223-242. Call site SessionLogger.java:199 (`removeFilter(removeFilters)` in applyFilterParams). |
| 21 | Logger.resume | REACHABLE | SOURCE | Def Logger.java:465-468. Call sites LogDataSource.java:88, :115, LogViewModel.java:153, SaveLogWorker.java:106. |
| 22 | Logger.send | REACHABLE | SOURCE | Def Logger.java:99-111 (protected, calls lazyGetInputBuf().add(entry) :104). Call site SessionLogger.java:166 (`send(entry)` at end of send(Alert)), itself called from TorrentSessionImpl.java:1103. |
| 23 | Logger.setMaxStoredLogs | REACHABLE | SOURCE | Def Logger.java:177-188. External caller freshly printed: TorrentSessionImpl.java:1413 (`sessionLogger.setMaxStoredLogs(settings.maxLogSize)` in applyMaxStoredLogs). This confirms the Agent 4 resolution on fresh evidence. |
| 24 | Logger.startRecording | REACHABLE | SOURCE | Def Logger.java:329-343. Call site LogViewModel.java:176. |
| 25 | Logger.stopRecording() | REACHABLE | SOURCE | Def Logger.java:362-365 (delegates to 2-arg overload :364). Call site LogViewModel.java:183. Note: the 1-arg overloads `stopRecording(OutputStream)` :367-370 and `write(OutputStream)` :405-408 are NOT batch 21 rows — do not conflate with rows 26/29. |
| 26 | Logger.stopRecording(OutputStream,boolean) | REACHABLE | SOURCE | Def Logger.java:372-398. Call site SaveLogWorker.java:93 (`logger.stopRecording(fout, true)`). WorkManager dispatch for SaveLogWorker INFERRED; the call site naming the method is printed. |
| 27 | Logger.submitDataSetChanged | REACHABLE | SOURCE | Def Logger.java:168-171 (private). Internal callers Logger.java:165 (swapBuffers), :256 (forceFilterBuf), :498 (doClean), all REACHABLE rows. |
| 28 | Logger.swapBuffers | REACHABLE | SOURCE | Def Logger.java:139-166 (private). Internal callers Logger.java:122 (periodicSwapBuffers), :282 (getEntries), :307 (getEntry), :335 (startRecording), :380 (stopRecording 2-arg), :415 (write 2-arg), all REACHABLE rows. |
| 29 | Logger.write(OutputStream,boolean) | REACHABLE | SOURCE | Def Logger.java:410-423 (delegates to private write :418). Call site SaveLogWorker.java:95 (`logger.write(fout, true)`). Same WorkManager note as row 26. |
| 30 | Logger.write(FixedRingBuffer,OutputStream,int,int,boolean) | REACHABLE | SOURCE | Def Logger.java:425-443 (private). Internal callers Logger.java:387 (stopRecording 2-arg) and :418 (write 2-arg), both REACHABLE rows. Its body at :437 calls entry.toStringWithTimeStamp()/toString(), confirming batch 21 row 1 and batch 20 row 40. |
| 31 | Logger$DataSetChange.<init>(Reason) | REACHABLE | SOURCE | Def Logger.java:527-530 (delegates to 2-arg ctor :529). Construction sites Logger.java:256 (`new DataSetChange(Reason.FILTER)` in forceFilterBuf) and :498 (`new DataSetChange(Reason.NEW_ENTRIES)` in doClean). |
| 32 | Logger$DataSetChange.<init>(Reason,List) | REACHABLE | SOURCE | Def Logger.java:532-536. Construction site Logger.java:165 (`new DataSetChange(Reason.NEW_ENTRIES, newEntries)` in swapBuffers). |
| 33 | Logger$DataSetChange$Reason.<clinit> | REACHABLE | INFERRED | Enum constants Logger.java:515-520 (NEW_ENTRIES, CLEAN, FILTER), used at Logger.java:165, :256, :498. JVM enum initialisation unprinted, hence INFERRED. If the merger requires an explicit static block, this row reverts to OPEN (no explicit static block is written in the file). |
| 34 | Logger$NewFilter.<init> | REACHABLE | SOURCE | Def Logger.java:506-510. Construction site SessionLogger.java:80 (`new NewFilter(name(), filter)` inside SessionLogFilter.filter()). |
| 35 | AddTorrentParams.<clinit> | REACHABLE | INFERRED | Static `CREATOR` field AddTorrentParams.java:109-119 initialised on class load; class loaded via AddTorrentViewModel.java:510 and TorrentEngine.java:1187 construction sites. JVM class-initialisation dispatch unprinted, hence INFERRED. |
| 36 | AddTorrentParams.<init>(Parcel) | REACHABLE | SOURCE | Def AddTorrentParams.java:77-88. Construction site AddTorrentParams.java:112 (`return new AddTorrentParams(source)` inside CREATOR.createFromParcel). FLAG — consistency: this row's route passes through batch 22 row 3 (`createFromParcel`), which is OPEN in this pass for lack of a printed marshalling site. If the merger requires a printed marshalling site for the Parcelable entry, rows 21/36 and 22/2–4 must be judged together (see batch 22 file); under that stricter rule row 36 reverts to OPEN. The merger must pick one Parcelable convention for all AddTorrentParams parcel rows. |
| 37 | AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean) | REACHABLE | SOURCE | Def AddTorrentParams.java:53-75 (10-arg ctor). Construction site AddTorrentViewModel.java:510 (`new AddTorrentParams(...)` in add-torrent path). A second construction site, TorrentEngine.java:1187, is in the same overload. |
| 38 | AddTorrentParams.describeContents | OPEN | — | Def AddTorrentParams.java:91-93 only. No printed parceling site for AddTorrentParams in any file freshly fetched in this pass; the framework calls describeContents only when the object is actually parcelled, which was not printed. Pending printed marshalling site or saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 39 | AddTorrentParams.hashCode | OPEN | — | Def AddTorrentParams.java:123-125 (`return sha1hash.hashCode()`) only. No hashCode caller in any file freshly fetched in this pass. Pending saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 40 | AddTorrentParams.toString | OPEN | — | Def AddTorrentParams.java:129-142 only. No toString/log/concatenation caller in any file freshly fetched in this pass. Pending saved full-repo grep. NOT UNREACHABLE on this evidence. |

## OPEN rows — what resolves them (all stay OPEN, none flipped to UNREACHABLE)

- Rows 38–40 (describeContents / hashCode / toString): one printed caller each (a marshalling site for 38; a hash use or explicit call for 39; a log/concatenation site for 40), or a saved full-repo grep for the exact method. Row 38's resolution is shared with batch 22 rows 1, 3, 4 (the writeToParcel/createFromParcel/newArray trio) — see batch 22 file.

## Caveats the merger must see (recorded, not decided)

1. **Strict-entry:** no launcher step was printed in this pass. Logger rows anchor at TorrentSessionImpl/SessionLogger/LogViewModel/LogDataSource/SaveLogWorker; AddTorrentParams rows at AddTorrentViewModel/TorrentEngine. Under a strict launcher-entry rule all 37 REACHABLE rows revert to OPEN on that point alone.
2. **Parcelable convention (rows 36–38 + batch 22 rows 1–4):** row 36 is kept REACHABLE on its printed internal construction site (CREATOR.createFromParcel :112), while batch 22 rows 1, 3, 4 are OPEN for lack of a printed marshalling site. The merger must pick one convention and apply it consistently; the stricter alternative flips row 36 to OPEN as well.
3. **confirmed_by:** per-row convention stated at the top. Under a whole-route INFERRED convention, SOURCE rows reached only through internal calls from REACHABLE methods would still read SOURCE under this file's rule (internal call printed) but INFERRED under a whole-route rule; labels unaffected.
4. **Lambda/thread numbering:** row 14's executor lambda and row 19's thread method reference are source-order, NOT bytecode-verified. Row 33's `<clinit>` has no explicit static block (enum constants only).
5. **Overload traps avoided:** Logger 1-arg `stopRecording(OutputStream)` / `write(OutputStream)` are not rows 26/29; `Logger.getEntry(int)` (not a batch 21 row) is not row 9; `pref.maxLogSize()` is not row 10.

## Not claimed / still owed before merge

- No build, sampler, full-repo grep, or C1 — build and C1 marked **not run** (Mac after push, never claimed passed). No push made. Main-agent spot-check (1 in 5) and `py_compile` remain outstanding.
- Saved full-repo grep for the 3 OPEN rows before any flip to UNREACHABLE.
- Scope strictly batch 21, LibreTorrent labels only, branch `work-2026-10-31` only, no other batch/app, no device replay, no Aegis.
