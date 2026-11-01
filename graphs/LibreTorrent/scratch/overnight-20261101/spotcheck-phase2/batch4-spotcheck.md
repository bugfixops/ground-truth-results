# Stream A Phase 2 spot-check — batch 4 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch4-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task): sample rows 1, 6, 11, 16, 21, 26, 31, 36. Row 11 is also the must-include extra and the row discussed in the dated 2026-11-01 Phase 1c note (D3c/D5e keep it OPEN; D1 cosmetic only). Phase 1c flipped NO label in this batch. Total checked: 8 rows.
- Method: re-derived each label from printed source in the already-fetched local corpus (`~/workspace/overnight/stream-A/corpus/java`, 281 main Java files, plus `corpus/other-sourcesets-src`, 20 test/other files = 301 files grepped). No connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived main-app evidence. FAIL = main-app evidence contradicts the label. No FAILs in this batch.
- Scope limit: Room generated code is not in the corpus; row 11 (Room converter ctor) therefore stays OPEN rather than being closed by grep alone.

## Per-row verdicts

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentDownloadImpl.isDownloading | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition TorrentDownloadImpl.java:1416-1419 confirmed (`getDownloadSpeed() > 0`). Corpus grep `\.isDownloading\(` = 0 hits. |
| 6 | FeedRepositoryImpl.getSerializeFileFormat | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition FeedRepositoryImpl.java:65-69 confirmed; interface declaration FeedRepository.java:38 confirmed. Corpus grep `getSerializeFileFormat\(` = 2 hits only: those two declarations. No caller. |
| 11 | UriConverter.\<init\> | OPEN, — | PASS | UriConverter.java:27-39 confirmed (class, no explicit ctor; static `@TypeConverter toUri` :30-32 and static `fromUri` :36-38). AppDatabase.java:53 `@TypeConverters({UriConverter.class})` and import :36 confirmed. Corpus grep: no `new UriConverter` anywhere (only the import, the registration, and the class definition). D3c covers only the `getRequiredConverters`/`getRequiredTypeConverters` methods, not this ctor, and Room generated instantiation code is unprinted — OPEN is correct under D3c/D5e as the Phase 1c note states. |
| 16 | FileSystemFacadeImpl.lastModified(Uri) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition FileSystemFacadeImpl.java:161-166 confirmed (dispatches `fsModule.lastModified(filePath)` at :165). Corpus `\.lastModified\(` hits outside the facade are only `File.lastModified()` (DefaultFsModule.java:117, SafFileSystem.java:492) — different receivers. No facade-method caller. The file's "rows 13 and 29 stand or fall with this one" is consistent: batch 4 rows 13 (DefaultFsModule.lastModified) and 29 (SafFsModule.lastModified) are both UNREACHABLE-proposed with the facade as their only dispatcher. |
| 21 | SafFileSystem.openFD(Uri, String, String) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition SafFileSystem.java:382-391 confirmed (3-arg overload delegating to the 2-arg form at :390). Corpus `openFD\(` hits are the 1-arg interface forms (FsModule, SafFsModule, DefaultFsModule, FakeFsModule), the FakePath 2-arg form (:394), the 2-arg form (:404), and definitions — no caller of the 3-arg (Uri, String, String) overload. |
| 26 | SafFileSystem$FakePath.isFakePath(String) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition SafFileSystem.java:157-160 confirmed. Corpus grep `isFakePath\(` = 1 hit only: the definition itself. Distinct from Utils.isSafPath, as the file warns. |
| 31 | NormalizeUrl.\<init\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | NormalizeUrl.java is 423 lines (matches the file's "423-line fresh print"); line 33 `public class NormalizeUrl` confirmed, no explicit ctor, static normalize overloads only. Corpus grep `new NormalizeUrl\(` = 0 hits. The file's correction (audit's "private constructor" reason does not hold; verdict rests on all-static use + no printed construction) is consistent with the print. |
| 36 | BindingAdapterUtils.\<init\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | BindingAdapterUtils.java is 112 lines (matches the file); line 36 `public class BindingAdapterUtils` confirmed, no explicit ctor, static methods only. Corpus grep `new BindingAdapterUtils\(` = 0 hits. Distinct from batch 56's BindingAdapterUtils method rows, as the file notes. |

## Totals

- Rows checked: 8. PASS: 8 (of which PASS* caveated: 0). FAIL: 0.
- Batch label counts re-verified from the row list: 40 rows = 0 REACHABLE / 39 UNREACHABLE / 1 OPEN (row 11). Consistent with the file header.
- Proposed corrections: none. No label change proposed; no file edited.

## Notes for the coordinator

- Build/sampler/C1: not run (not this task).
