# Stream A Phase 2 spot-check — batch 1 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch1-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS every row discussed in the dated 2026-11-01 Phase 1c revision note. Phase 1c flipped NO label in this batch (row 1 only: OPEN `confirmed_by` INFERRED → —, cosmetic, D1; D8 keeps row 1 OPEN). Row 1 is also the must-include extra and a sample row, so the checked set is exactly the 8 sample rows.
- Method: re-derived each label from printed source in the already-fetched local corpus (`~/workspace/overnight/stream-A/corpus/java`, 281 main Java files, plus `corpus/other-sourcesets-src`, 20 test/other files = 301 files grepped). No connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived main-app evidence. PASS* = same, but the label also depends on a named undecided convention (label left as-is, no decision made here). FAIL = main-app evidence contradicts the label. No FAILs in this batch.
- Scope limit: generated sources and res XML are not in the corpus; OPEN rows that need generated/library dispatch therefore stay OPEN rather than being closed by grep alone.

## Per-row verdicts

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | baseAdapters.BR.\<init\> | OPEN, — | PASS | `androidx.databinding.library.baseAdapters.BR` imported in exactly 5 corpus files (DetailTorrentViewModel.java:33, TorrentDetailsMutableParams.java:27, LogActivity.java:39, LogMutableParams.java:25, LogViewModel.java:29); corpus grep `new BR\(` = 0 hits. Field reads prove class loading, not `<init>` invocation, and no generated/library source is printed — OPEN is correct under D8. No conclusion transferred from the libretorrent mapper rows. |
| 6 | EzRssTorrentItem.getPeers | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition EzRssTorrentItem.java:85-87 confirmed in corpus. Corpus grep `\.getPeers\(` = 0 hits. Field parsed at EzRss01Parser.java:87-93, never read back (matches file). |
| 11 | FeedParserFactory.\<init\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition: FeedParserFactory.java has no explicit ctor; sole member is static `newParser()` returning `new DefaultFeedParser()` (lines 16-26 confirmed). Corpus grep `new FeedParserFactory\(` = 0 hits. |
| 16 | AtomFeed.getDescription | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition AtomFeed.java:56-59 confirmed. Corpus grep `\.getDescription\(` = 1 hit only: NanoHTTPD.java:1192 `status.getDescription()` — a different class, not a Feed/AtomFeed receiver. No AtomFeed/Feed getDescription caller. |
| 21 | AtomItem.getAuthor | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition AtomItem.java:64-66 confirmed. Corpus grep `\.getAuthor\(` = 0 hits. Parser caller set cited in file (CoreFeedParser.java:96/:104/:110/:170/:190/:238/:256) contains no getAuthor call. |
| 26 | BaseElement.getName | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition BaseElement.java:51-53 confirmed. Corpus `\.getName\(` hits (70) are all other receivers (File, FileTree nodes, handles, view-model params); within `com/ernieyu/feedparser` + `core/FeedParser.java` there are 0 getName hits. No BaseElement/Element getName caller. |
| 31 | Rss1Feed.getLink | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition Rss1Feed.java:53-66 confirmed (getLink at :53). Corpus grep `\.getLink\(` = 0 hits. |
| 36 | Rss1Item.getType | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition Rss1Item.java:34-37 confirmed (`FeedType.RSS_1_0`). Corpus `\.getType\(` hits are other classes; within feedparser + CoreFeedParser.java the only hits are `enclosure.getType()` (FeedParser.java:175) and `content.getType()` (:202) — different classes, as the file states. No Rss1Item/Item getType caller. |

## Totals

- Rows checked: 8. PASS: 8 (of which PASS* caveated: 0). FAIL: 0.
- Batch label counts re-verified from the row list: 40 rows = 0 REACHABLE / 39 UNREACHABLE / 1 OPEN (row 1). Consistent with the file header.
- Proposed corrections: none. No label change proposed; no file edited.

## Notes for the coordinator

- The file's original "Grep owed" caveats on rows 6, 11, 16, 21, 26, 31, 36 are now discharged for the main+test Java tree by the corpus greps above (301 files); generated-code dispatch is not in scope for these non-generated rows.
- Build/sampler/C1: not run (not this task).
