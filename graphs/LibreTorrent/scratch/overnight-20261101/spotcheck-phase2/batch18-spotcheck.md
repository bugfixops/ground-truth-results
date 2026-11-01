# LibreTorrent batch 18 — Phase 2 spot-check (UNVERIFIED proposal, labels only)

- Work file checked: `~/workspace/overnight/stream-A/work/batch18-merge-ready.md` (40 rows, 38 REACHABLE / 2 UNREACHABLE / 0 OPEN after Phase 1c).
- Spot-check date: 2026-11-01. No merge-ready file was edited, no label was changed by this check, no push was made, no build/sampler/C1 was run (not this task).
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (281-file Java tree). No GitHub connector fetch was needed; no 429 was hit.
- Verdict rule: PASS requires the label AND the cited definition/caller lines to identify the right method and caller. A range running past the closing brace onto a blank line or the class-close brace is a nit, not a FAIL. A range that starts on the wrong line, ends mid-method, or names the wrong caller line is a FAIL (label may still stand; the correction is then citation-only).
- Convention note: rows 1-2 turn on decision D8 (M-dispatch); see the batch 17 spot-check note. This check verifies the D8 application and does not re-decide D8.

## Rows checked (9 of 40)

Sample rows 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1c changed rows 1, 2 (D8 flips) + must-include rows 1, 2. Union: 1, 2, 6, 11, 16, 21, 26, 31, 36.

## Per-row verdicts

- Row 1 — libretorrent.DataBinderMapperImpl$InnerBrLookup.\<clinit\> — REACHABLE INFERRED (D8 flip, must-include) — **PASS as D8-application**. Trigger side verified: 33 files in the corpus use `DataBindingUtil`; no generated mapper file exists in the corpus and the corpus-wide grep for `DataBinderMapperImpl|InnerBrLookup|InnerLayoutIdLookup` returns zero hits, matching the file's clean connector file-not-found. Under D8, first `DataBindingUtil` use loads the mapper class, which loads its inner lookup classes, so `<clinit>` is a dispatch-entry method: REACHABLE INFERRED (never SOURCE) is the correct mechanical application. Same revert condition as batch 17 rows 34-40 if the merger rejects D8. This row is a different class from batch 12's `databinding.DataBinderMapperImpl`; no conclusion was copied from batch 12.
- Row 2 — libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.\<clinit\> — REACHABLE INFERRED (D8 flip, must-include) — **PASS as D8-application**. Same evidence and reasoning as row 1 for the `$InnerLayoutIdLookup` inner class. Same revert condition.
- Row 6 — MainApplication.lambda$onCreate$0 — REACHABLE INFERRED — **PASS**. Lambda body at `MainApplication.java:62-64` verified (`Thread.setDefaultUncaughtExceptionHandler((t, e) -> Log.e(…))` :62-63, close :64). Registration condition at :61 (`Thread.getDefaultUncaughtExceptionHandler() == null`) verified. Dispatch (invocation on an uncaught exception) is unprinted, hence INFERRED. Lambda numbering is source-order as filed.
- Row 11 — FeedParser.getItems — REACHABLE SOURCE — **PASS**. Def `core/FeedParser.java:89-116` verified (def :89, close :116). External call at `FeedFetcherWorker.java:165` (`parser.getItems()`) verified.
- Row 16 — FeedParser.watchGuid — REACHABLE SOURCE — **PASS**. Def `core/FeedParser.java:254-261` verified. Internal call at `findDownloadUrl` :159 (`watchGuid(item)`) verified.
- Row 21 — HttpConnection.run — REACHABLE SOURCE — **FAIL, citation only; label stands, no label change by this check**. The label and the SOURCE reasoning are correct: def `HttpConnection.java:78` (`public void run()`) verified, and `Utils` calls `connection.run()` directly (not via a Thread start), so SOURCE (not INFERRED) is right. The cited caller line is wrong: the file cites `Utils.java:516`, but in the corpus copy `connection.run()` is at `Utils.java:512` (listener block :477-511, `connection.run()` :512, error handling :514-522). This is not corpus drift: the corpus `Utils.java` is 926 lines, exactly matching the batch 20 file's own fresh-print claim of 926 lines, and neighbouring citations from the same region all match the corpus exactly (`new HttpConnection` :472, `setListener` :477, `throw new FetchLinkException` :467/:474/:522, `fetchHttpUrl` :462-475). The :516 figure appears to have been carried from the batch 18 pass into batch 19 row 40's "closes batch 18's chain" note, not re-derived. Proposed correction: cite `Utils.java:512`.
- Row 26 — InputFilterRange.getMax — UNREACHABLE — **PASS (as proposed)**. Def `core/InputFilterRange.java:59-62` verified (`return max` :61). `filter()` :65-81 calls `inRange()` :73, and `inRange()` :83-86 reads the `min`/`max` fields directly — neither ever calls this getter. Corpus-wide grep finds no `.getMax()` caller on an `InputFilterRange` receiver (the only `.getMax()`-shaped lines are the definition itself). The getter is not an `InputFilter` interface method (the interface method is `filter()`), so framework dispatch cannot reach it. The file's still-owed saved full-repo grep remains owed before merge.
- Row 31 — InputFilterRange$Builder.setMax — REACHABLE SOURCE — **PASS**. Call chain verified in `ui/log/LogSettingsFragment.java:60-63`: `new InputFilterRange.Builder()` :60, `.setMin(1)` :61, `.setMax(Integer.MAX_VALUE)` :62, `.build()` :63.
- Row 36 — RepositoryHelper.getTorrentRepository — REACHABLE SOURCE — **PASS**. Def `core/RepositoryHelper.java:43` verified. Call at `core/model/TorrentEngine.java:130` (`RepositoryHelper.getTorrentRepository(appContext)`) verified.

## Totals

- Checked: 9. **PASS: 8. FAIL: 1** (row 21, citation-only).
- No label was found wrong. No proposed label correction. One citation correction proposed (row 21: Utils.java:516 → :512).
