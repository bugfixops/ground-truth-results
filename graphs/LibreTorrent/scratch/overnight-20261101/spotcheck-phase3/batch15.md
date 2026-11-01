# Spot-check — batch 15 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 15/1 Hash.getValue — REACHABLE INFERRED — PASS. Definition Hash :32-34; caller core watchMediaHash :221 ← watchMediaContent :201/:207 ← core getItems; WorkManager+SAX dispatch INFERRED.
- 15/6 MediaRss.getContent — REACHABLE INFERRED — PASS. Definition :30-32; caller core watchMediaContent :194.
- 15/11 PeerLink.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :55-59; no printed caller in the fresh corpus (proposal; saved full-repo grep owed before merge, noted in row).
- 15/16 NanoHTTPD.createServerRunnable — REACHABLE SOURCE — PASS. Definition :1590-1592; caller NanoHTTPD.start(int,boolean) :1816 (printed direct call).
- 15/21 NanoHTTPD.safeClose — REACHABLE SOURCE — PASS. Definition :1511-1527; printed callers include the synchronous stop path NanoHTTPD.stop :1839 ← TorrentStreamServer.stop :82, plus ClientHandler.close :164-165 and execute finally :753.
- 15/26 NanoHTTPD.start() — REACHABLE SOURCE — PASS. Definition :1794-1795 (start(SOCKET_READ_TIMEOUT)); caller TorrentStreamServer.start :78 super.start() (printed direct call).
- 15/31 NanoHTTPD$ClientHandler.\<init\> — REACHABLE INFERRED — PASS. Definition ClientHandler :159-162; caller createClientHandler :1580, reached only via ServerRunnable.run :1347 on the listener thread.
- 15/36 NanoHTTPD$Cookie.getHTTPTime — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :197-203; printed callers are Cookie(String,String,int) :211 and CookieHandler.set :284, both on dead paths (proposal; saved full-repo grep owed before merge, noted in row).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
