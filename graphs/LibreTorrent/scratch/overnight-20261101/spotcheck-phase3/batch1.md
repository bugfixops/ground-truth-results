# Spot-check — batch 1 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). A row in both sets is checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided; FAIL here means the application is wrong. No work file edited.

## Changed rows (1)

- 1/1 baseAdapters.BR.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L4 D13: zero `new BR(` in greps/L4/grep_D13_newBR.txt, BR field reads only). Stale prose contradicts the new label: "generated source still unprinted, so the row stays OPEN" and "REVISION 2026-11-01 (D8/D1): D8 decides this row stays OPEN for its own reason (field reads prove class loading, not \<init\> invocation)". The Phase 3 note is appended but the stays-OPEN sentences were not removed.

## Sample rows (7 sample-only)

- 1/6 EzRssTorrentItem.getPeers — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :85-87; field parsed, never read back (proposal; "grep owed" noted in row).
- 1/11 FeedParserFactory.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only member is static newParser(); no `new FeedParserFactory()` printed (proposal; "grep owed" noted in row).
- 1/16 AtomFeed.getDescription — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :56-59; printed element access never calls getName/getDescription on this receiver (proposal; "grep owed" noted in row).
- 1/21 AtomItem.getAuthor — UNREACHABLE no_trigger_in_app INFERRED — PASS. Parser item-call set listed (CoreFeedParser :96/:104/:110/:170/:190/:238/:256); never getAuthor() (proposal; "grep owed" noted in row).
- 1/26 BaseElement.getName — UNREACHABLE no_trigger_in_app INFERRED — PASS. Printed element access uses getUri/getContent/getElement; never getName() (proposal; "grep owed" noted in row).
- 1/31 Rss1Feed.getLink — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :53-66; same feed-caller-set argument as row 14 (proposal; "grep owed" noted in row).
- 1/36 Rss1Item.getType — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :34-37; same item-caller-set argument as row 21 (proposal; "grep owed" noted in row).

Totals: checked 8 (1 changed + 7 sample-only) — PASS 7, FAIL-prose 1, FAIL-label 0.
