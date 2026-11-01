# Stream A Phase 2 spot-check — batch 3 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch3-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS row 35 (discussed in the dated 2026-11-01 Phase 1c note: D11, "stands UNREACHABLE as tabled"). Phase 1c flipped NO label in this batch (row 26 only: OPEN `confirmed_by` INFERRED → —, cosmetic, D1; D6 keeps row 26 OPEN). Row 26 is also the must-include extra and a sample row; row 31 is the batch's only OPEN-closing flip, re-checked in Phase 1 and survived. Total checked: 9 rows.
- Method: re-derived each label from printed source in the already-fetched local corpus (`~/workspace/overnight/stream-A/corpus/java`, 281 main Java files, plus `corpus/other-sourcesets-src`, 20 test/other files = 301 files grepped). No connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived main-app evidence. PASS* = same, but the label also depends on a named undecided convention (label left as-is, no decision made here). FAIL = main-app evidence contradicts the label. No FAILs in this batch.
- Scope limit: whether test/other-source-set callers count as in-app triggers is NOT decided in DECISIONS.md (no test-scope ruling found there) — see the PASS* caveats on rows 16 and 21.

## Per-row verdicts

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | RepositoryHelper.\<init\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | RepositoryHelper.java:36, :43, :52, :61, :69 confirmed — class with only static accessors, no explicit ctor. Corpus grep `new RepositoryHelper\(` = 0 hits. |
| 6 | FileAlreadyExistsException.\<init\>() | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition FileAlreadyExistsException.java:24 confirmed. Corpus grep `new FileAlreadyExistsException` = 0 hits (main + test trees). |
| 11 | NoFilesSelectedException.\<init\>(String) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NoFilesSelectedException.java:26 confirmed. Only construction in corpus is the 0-arg form at AddTorrentViewModel.java:493 (`throw new NoFilesSelectedException();`); zero String-arg constructions. Overload distinction holds. |
| 16 | Logger.getEntry(int) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS* | Definition Logger.java:301 confirmed. Main-tree grep `\.getEntry\(` = 0 call hits (file's cited app callers use getNumEntries/pause/resume/start/stop/write, not getEntry). CAVEAT (undecided convention, label left as-is): test-source-set callers DO exist — LoggerTest.java (other-sourcesets) calls `logger.getEntry(i)` at lines 47-51, 71, 88, 99, 110, 185, 189. If the project counts test callers as triggers, this row flips to REACHABLE; if (as the file's `no_trigger_in_app` kind implies) only in-app triggers count, it stands. Coordinator/user decision needed; no correction made here. |
| 21 | TorrentInfoProvider.getInstance(TorrentEngine, TagRepository) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS* | Definitions TorrentInfoProvider.java:63-75 (Engine overload) and :76- (Context overload) confirmed. Main-tree callers all use the Context overload (TorrentService.java:110, DetailTorrentActivity.java:65, DetailTorrentViewModel.java:107, MainActivity.java:146, MainViewModel.java:72). CAVEAT (same undecided convention, label left as-is): test-source-set callers of the Engine overload DO exist — AbstractTest.java:72 and TorrentEngineTest.java:181 (`getInstance(engine, tagRepo)`). Same decision as row 16 applies; no correction made here. |
| 26 | TagInfo.hashCode | OPEN, — | PASS | Definition TagInfo.java:94-99 confirmed. Both delegators confirmed in corpus: drawer TagItem.java:51 `return info.hashCode();` and tag TagItem.java:50 `return info.hashCode();`. Neither delegator is REACHABLE (tag TagItem.hashCode is UNREACHABLE-proposed in batch 11; drawer TagItem.hashCode is OPEN in batch 10 row 39 — independently confirmed OPEN below in the batch 10 spot-check, with no hash caller). Corpus grep for HashSet/HashMap holding TagInfo = 0 hits. Under D6 (app-tree zero alone does not close a hashCode row; no printed trigger), OPEN is correct. |
| 31 | PriorityConverter.convert(Priority lib→app single) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition PriorityConverter.java:103-110 (lib→app single) confirmed. Corpus grep `PriorityConverter\.convert\(` = exactly 6 sites, all other overloads, including test files: TorrentDownloadImpl.java:731 (array), :1139 (app Priority `newPriority`), :1646 (array), TorrentSessionImpl.java:437/:451 (arrays), :1574 (app Priority + `.swig()`). Zero single-lib-Priority-arg calls — the Phase 1 complete-tree re-check survives on this corpus too. |
| 35 | TorrentCriticalWork$Type.\<clinit\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Enum TorrentCriticalWork.java:32-36 (MOVING, SAVE_RESUME) confirmed. Corpus `Type\.(MOVING\|SAVE_RESUME)` hits are all libtorrent `AlertType.SAVE_RESUME_DATA` — a different enum. Only other TorrentCriticalWork mention is its instantiation at TorrentDownloadImpl.java:139, which does not reference the nested Type constants. No first-use print for the enum, so D11 converse case stands: UNREACHABLE as tabled. |
| 36 | TorrentDownloadImpl.getMaxConnections | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition TorrentDownloadImpl.java:1436-1448 confirmed. Corpus grep `\.getMaxConnections\(` = 0 hits. Internal code uses the setter, not the getter, as the file states. |

## Totals

- Rows checked: 9. PASS: 9 (of which PASS* caveated: 2 — rows 16 and 21, test-caller convention). FAIL: 0.
- Batch label counts re-verified from the row list: 40 rows = 0 REACHABLE / 39 UNREACHABLE / 1 OPEN (row 26). Consistent with the file header.
- Proposed corrections: none. Rows 16 and 21 are explicitly NOT corrected here: their labels turn on the undecided test-caller convention and are left as-is for the coordinator/user to decide.

## Notes for the coordinator

- Decision owed (not made here): do test/other-source-set direct callers count as in-app triggers? It affects batch 3 rows 16 and 21 only in this batch's checked set.
- Build/sampler/C1: not run (not this task).
