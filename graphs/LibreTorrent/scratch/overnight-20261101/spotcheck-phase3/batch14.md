# Spot-check — batch 14 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 14/1 MediaRssParser.isMediaRssElement — REACHABLE INFERRED — PASS. Callers MediaRssParser.parseContent :45 / parseHash :60 / parsePeerLinks :81, reached via parse :29-38 ← Rss2Item.getMediaRss :115 ← core getItems :190; WorkManager+SAX dispatch unprinted, hence INFERRED.
- 14/6 Rss1Feed.\<init\> — REACHABLE INFERRED — PASS. Definition Rss1Feed :36-38; constructed at FeedHandler.startElement :62 (SAX dispatch INFERRED).
- 14/11 Rss1Item.getDescription — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed caller path is BaseItem.getUniqueId :41, which runs only via BaseItem.equals :56-57 / hashCode :67, both proposed UNREACHABLE in batch 13 with no printed trigger.
- 14/16 Rss1Item.getMediaRss — REACHABLE INFERRED — PASS. Definition :112-114 (returns null); caller core getItems :190.
- 14/21 Rss2Feed.getTitle — REACHABLE INFERRED — PASS. Definition :47-51; caller core getTitle :86.
- 14/26 Rss2Item.getEzRssTorrentItem — REACHABLE INFERRED — PASS. Definition :119-121 (new EzRss01Parser(this).parse()); caller core getItems :238.
- 14/31 Rss2Item.getTitle — REACHABLE INFERRED — PASS. Definition :40-43; caller core getItems :110.
- 14/36 Content.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :76-80; no printed caller in the fresh corpus (proposal; saved full-repo grep owed before merge, noted in row).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
