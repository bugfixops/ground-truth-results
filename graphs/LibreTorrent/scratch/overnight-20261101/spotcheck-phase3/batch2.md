# Spot-check — batch 2 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 2/37 libretorrent.BR.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L4 D13: zero `new BR(` in greps/L4/grep_D13_newBR.txt, BR field reads only). Stale prose: "Still OPEN under convention (x)", "do not merge as UNREACHABLE on this evidence", "REVISION 2026-11-01 (D8/D1): D8 decides this row stays OPEN for its own reason (BR field reads prove class loading, not \<init\> invocation)".

## Sample rows (8)

- 2/1 Rss2Feed.getLink — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :54-65; parser caller set contains no feed.getLink() (proposal; "grep owed" noted in row).
- 2/6 Rss2Item.getType — UNREACHABLE no_trigger_in_app INFERRED — PASS. Parser never calls item.getType(); enclosure/content getType() are different classes (proposal; "grep owed" noted in row).
- 2/11 NanoHTTPD.closeAllConnections — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1566-1568; TorrentStreamServer.stop() calls super.stop(), not this (proposal; "grep owed" noted in row).
- 2/16 NanoHTTPD.getMimeTypeForFile — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1503-1511; mime-chain entry, no printed caller (proposal; "grep owed" noted in row).
- 2/21 NanoHTTPD.makeSSLSocketFactory — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1473-1478; no external printed caller beyond row 20 (proposal; "grep owed" noted in row).
- 2/26 NanoHTTPD.newFixedLengthResponse(String) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1719-1721; multi-arg overloads are called, the single-arg overload itself has no printed caller.
- 2/31 NanoHTTPD$DefaultAsyncRunner.getRunning — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :315-317; code uses exec()/closed()/closeAll(), never getRunning() (proposal; "grep owed" noted in row).
- 2/36 NanoHTTPD$SecureServerSocketFactory.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed caller is makeSecure :1685 (row 23), itself uncalled; inherits row 23's grep target.

Totals: checked 9 (1 changed + 8 sample-only) — PASS 8, FAIL-prose 1, FAIL-label 0.
