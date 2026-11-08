# Spot-check — batch 12 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Note on schema: this file's rows carry the confirmed_by in a trailing cell (e.g. row 16's trailing INFERRED); a naive first-match parse that picks up the intervening "—" cell is a parser artefact, not a row error. No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 12/1 databinding.DataBinderMapperImpl.\<init\> — OPEN — PASS. No definition printed; generated class source absent from the upload; row correctly distinguishes this class from batch 17's libretorrent.DataBinderMapperImpl.
- 12/6 Enclosure.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition FPI/Enclosure.java:70-75; no printed hash-based collection use in this pass (proposal; saved full-repo grep pending, noted in row).
- 12/11 EzRssTorrentItem.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition FPI/EzRssTorrentItem.java:116-125; no printed hash-based collection use in this pass (proposal; saved full-repo grep pending, noted in row).
- 12/16 FeedType.\<clinit\> — REACHABLE INFERRED — PASS. Enum class initialisation on first use: FeedHandler.java:64, 71, 78 and AtomItem.java:35-36 reference FeedType constants; first use via the SAX parse path (T4); INFERRED because the initialiser has no printed call site.
- 12/21 FeedUtils.equalsOrNull — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed caller is BaseItem.java:58 inside BaseItem.equals, itself proposed UNREACHABLE in batch 13.
- 12/26 XMLInputStream.isAlphaNumeric — REACHABLE SOURCE — PASS. Definition :157 (private); call at XMLInputStream.java:100 in readAmpersand; trunk T4.
- 12/31 XMLInputStream.read(byte[],int,int) — REACHABLE INFERRED — PASS. Definition :135-144 (overrides FilterInputStream.read); reached only via SAX/JDK dispatch on the stream registered at DefaultFeedParser.java:37.
- 12/36 AtomFeed.getTitle — REACHABLE SOURCE — PASS. Definition AtomFeed.java:44; calls at C:86 and, via the worker, W:176; trunk T0–T3.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
