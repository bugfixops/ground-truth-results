# Spot-check — batch 13 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 13/1 AtomItem.getEzRssTorrentItem — REACHABLE SOURCE — PASS. Definition AtomItem.java:136-138 (returns null, "Not supported"); interface call at C:238 via watchTorrentInfoHash; trunk T10.
- 13/6 AtomItem.getTitle — REACHABLE SOURCE — PASS. Definition AtomItem.java:40-43; unconditional call at C:110 in the getItems loop; trunk T0–T9.
- 13/11 BaseElement.getElement — REACHABLE SOURCE — PASS. Definition BaseElement.java:73-76; calls at AtomItem.java:41, 75, 81 and EzRss01Parser.java:40, 48, 56, 64, 80, 88, 96; trunk T0–T10.
- 13/16 BaseItem.equals — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition BaseItem.java:53-62; no trigger of equals on a library Item in any file printed in this pass.
- 13/21 DefaultFeedParser.parse — REACHABLE SOURCE — PASS. Definition DefaultFeedParser.java:22-47; call at C:71 (FeedParserFactory.newParser().parse(bsStream)); trunk T0–T6.
- 13/26 EzRss01Parser.parseFileName — REACHABLE SOURCE — PASS. Definition EzRss01Parser.java:39-45; call at EzRss01Parser.java:27 from parse.
- 13/31 EzRss01Parser.parseSeeds — REACHABLE SOURCE — PASS. Definition EzRss01Parser.java:79-85; call at EzRss01Parser.java:31 from parse.
- 13/36 FeedHandler.endElement — REACHABLE INFERRED — PASS. Definition FeedHandler.java:110-131; registration at DefaultFeedParser.java:37; SAX dispatch INFERRED (T7).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
