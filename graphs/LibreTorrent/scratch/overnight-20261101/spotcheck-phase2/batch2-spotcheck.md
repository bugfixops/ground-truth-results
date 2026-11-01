# Stream A Phase 2 spot-check — batch 2 — UNVERIFIED (spot-check only, not a merge verdict)

- Source checked: `~/workspace/overnight/stream-A/work/batch2-merge-ready.md` (UNVERIFIED proposal, not a result).
- Branch: `work-2026-10-31`, repo `bugfixops/ground-truth-results`. Labels only; no device checks.
- Checked set (per task): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS must-include rows 37, 38, 39, 40 (also the rows discussed in the dated 2026-11-01 Phase 1c note). Phase 1c flipped NO label in this batch (rows 37–40 only: OPEN `confirmed_by` INFERRED → —, cosmetic, D1; D8 keeps all four OPEN, each for its own reason). Total checked: 12 rows.
- Method: re-derived each label from printed source in the already-fetched local corpus (`~/workspace/overnight/stream-A/corpus/java`, 281 main Java files, plus `corpus/other-sourcesets-src`, 20 test/other files = 301 files grepped). No connector fetch was needed; no 429 encountered. No merge-ready file was edited; no tick written.
- Verdict vocabulary: PASS = label consistent with the re-derived main-app evidence. FAIL = main-app evidence contradicts the label. No FAILs in this batch.
- Scope limit: generated sources are not in the corpus; rows 37–40 (generated mapper classes) therefore stay OPEN rather than being closed by grep alone.

## Per-row verdicts

| Row | Method (short) | Label in file | Verdict | Evidence (re-derived) |
|---|---|---|---|---|
| 1 | Rss2Feed.getLink | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition Rss2Feed.java:54-65 confirmed (getLink at :54). Corpus grep `\.getLink\(` = 0 hits. |
| 6 | Rss2Item.getType | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition Rss2Item.java:35-37 confirmed (`FeedType.RSS_2_0`). Corpus getType hits are other classes; within feedparser + CoreFeedParser.java only `enclosure.getType()` (FeedParser.java:175) and `content.getType()` (:202) — different classes, as the file states. |
| 11 | NanoHTTPD.closeAllConnections | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:1566-1568 confirmed (body calls `stop()`). Corpus grep `closeAllConnections\(` = 1 hit only: the definition itself. No caller. |
| 16 | NanoHTTPD.getMimeTypeForFile(String) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:1503-1511 confirmed. Corpus grep `getMimeTypeForFile\(` = 1 hit only: the definition itself. No caller; it is a chain entry, not a callee, as the file states. |
| 21 | NanoHTTPD.makeSSLSocketFactory(KeyStore, KeyManagerFactory) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:1473-1478 confirmed (body calls the KeyManager[] overload at :1475). The only caller in the corpus is row 20, the (String, char[]) overload, at NanoHTTPD.java:1491 (`return makeSSLSocketFactory(keystore, keyManagerFactory)` with a KeyManagerFactory variable, lines 1484-1491 confirmed) — and row 20 is itself UNREACHABLE-proposed with no printed caller, so the SSL chain (rows 20–22, 23, 36) has no entry. The file's wording ("no external printed caller beyond row 20") is accurate. |
| 26 | NanoHTTPD.newFixedLengthResponse(String) | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:1719-1721 confirmed (delegates to the 3-arg overload at :1720). Proper arg-count parse of every `newFixedLengthResponse` call in NanoHTTPD.java and TorrentStreamServer.java: all calls are 3- or 4-arg; zero single-String-arg calls. Overload-level distinction in the file holds. |
| 31 | NanoHTTPD$DefaultAsyncRunner.getRunning | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:315-317 confirmed. Corpus grep `\.getRunning\(` = 0 hits. |
| 36 | NanoHTTPD$SecureServerSocketFactory.\<init\> | UNREACHABLE proposed, no_trigger_in_app, INFERRED | PASS | Definition NanoHTTPD.java:436 confirmed. Only construction site is inside `makeSecure` at NanoHTTPD.java:1685, and row 23 (`makeSecure`) is itself UNREACHABLE-proposed with no printed caller (definition :1684-1686 confirmed) — inheritance argument in the file holds. |
| 37 | libretorrent.BR.\<init\> | OPEN, — | PASS | Generated class, no source in corpus. Corpus grep `new BR\(` = 0 hits and no DataBinderMapperImpl/InnerBrLookup/InnerLayoutIdLookup/DataBindingTriggerClass hits; libretorrent.BR field reads exist (e.g. `BR.url`, `BR.name` via `notifyPropertyChanged` in AddFeedMutableParams etc.) but field reads do not invoke `<init>`. OPEN correct under D8; not conflated with batch 1's baseAdapters.BR row. |
| 38 | libretorrent.DataBinderMapperImpl$InnerBrLookup.\<init\> | OPEN, — | PASS | Generated class, no source in corpus; no printed lookup-instantiation site in the corpus greps above. The batch-18 `<clinit>` flip does not imply `<init>`, as the Phase 1c note states. OPEN correct under D8; distinct from batch 12's databinding mapper row. |
| 39 | libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.\<init\> | OPEN, — | PASS | Same as row 38: generated class, no source, no printed instantiation site. OPEN correct under D8. |
| 40 | DataBindingTriggerClass.\<init\> | OPEN, — | PASS | Generated class, no source, no printed site of any kind in the corpus greps above. OPEN correct under D8. |

## Totals

- Rows checked: 12. PASS: 12 (of which PASS* caveated: 0). FAIL: 0.
- Batch label counts re-verified from the row list: 40 rows = 0 REACHABLE / 36 UNREACHABLE / 4 OPEN (rows 37–40). Consistent with the file header.
- Proposed corrections: none. No label change proposed; no file edited.

## Notes for the coordinator

- The file's "Grep owed" caveats on rows 1, 6, 11, 16, 21, 26, 31, 36 are now discharged for the main+test Java tree by the corpus greps above (301 files).
- Build/sampler/C1: not run (not this task).
