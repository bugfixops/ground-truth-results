# LibreTorrent batch 15 — Phase 2 spot-check (UNVERIFIED proposal, labels only)

- Work file checked: `~/workspace/overnight/stream-A/work/batch15-merge-ready.md` (40 rows).
- Spot-check date: 2026-11-01. No merge-ready file was edited, no label was changed by this check, no push was made, no build/sampler/C1 was run (not this task).
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (281-file Java tree). No GitHub connector fetch was needed; no 429 was hit.
- Verdict rule: PASS requires the label AND the cited definition/caller lines to identify the right method and caller. A range running past the closing brace onto a blank line or the class-close brace is a nit, not a FAIL. A range that starts on the wrong line, ends mid-method, or names the wrong caller line is a FAIL (label may still stand; the correction is then citation-only).
- Phase 1 note: this file carries no dated 2026-11-01 Phase 1c revision (it was not in a Phase 1c application group), so there are no additional Phase 1 changed rows beyond the sample.

## Rows checked (8 of 40)

Sample rows 1, 6, 11, 16, 21, 26, 31, 36.

## Per-row verdicts

- Row 1 — Hash.getValue — REACHABLE INFERRED — **PASS**. Def `mediarss/Hash.java:32-34` verified. Call at core `FeedParser.java:221` (`hash.getValue()` inside `watchMediaHash`) verified. INFERRED is correct under the file's whole-route rule (WorkManager + SAX dispatch unprinted).
- Row 6 — MediaRss.getContent — REACHABLE INFERRED — **PASS**. Def `mediarss/MediaRss.java:30-32` verified. Call at core `FeedParser.java:194` (`media.getContent()` inside `watchMediaContent`) verified.
- Row 11 — PeerLink.hashCode — UNREACHABLE — **PASS (as proposed)**. Def `mediarss/PeerLink.java:55-59` verified. Corpus-wide grep finds no `hashCode()` caller on a `PeerLink` and no hash collection holding one (the only `PeerLink` mentions outside its definition file are the `MediaRss` field/getter and the `MediaRssParser` construction site). The file's still-owed saved full-repo grep remains owed before merge.
- Row 16 — NanoHTTPD.createServerRunnable — REACHABLE SOURCE — **PASS**. Def `NanoHTTPD.java:1590-1592` verified (def :1590, `return new ServerRunnable(timeout)` :1591, close :1592). Call at `NanoHTTPD.start(int,boolean)` :1816 verified.
- Row 21 — NanoHTTPD.safeClose — REACHABLE SOURCE — **FAIL, citation only; label stands, no label change by this check**. The label is correct: the synchronous stop path exists (`NanoHTTPD.stop` :1837-1845, `safeClose(this.myServerSocket)` :1839, reached from `TorrentStreamServer.stop` :82), plus `ClientHandler.close` :164-165. The cited def range is wrong: the file cites :1511-1519, but the method spans :1511-1527 (def :1511, `try` :1512, if-chain :1513-1522, `catch (IOException e)` :1524-1525, close :1527); :1519 ends mid-method inside the `ServerSocket` branch, before the `else`, the catch, and the close. Proposed correction: cite `NanoHTTPD.java:1511-1527`.
- Row 26 — NanoHTTPD.start() — REACHABLE SOURCE — **FAIL, citation only; label stands, no label change by this check**. The label is correct: def `NanoHTTPD.java:1794-1795` verified (`start(SOCKET_READ_TIMEOUT)`), and `TorrentStreamServer.start` does call `super.start()`. The cited caller line is wrong: the file cites `TorrentStreamServer.start :77`, but in the corpus copy `super.start()` is at :78 (`start` method def :72, body :73-78, close :79; :77 is a blank line). This is not corpus drift: the corpus `TorrentStreamServer.java` is 284 lines, exactly matching the file's own fresh-print claim of 284 lines, and neighbouring citations (serve :111, setHeaders :119, setMimeType :281) all match the corpus exactly. Proposed correction: cite `TorrentStreamServer.java:78`.
- Row 31 — NanoHTTPD$ClientHandler.\<init\> — REACHABLE INFERRED — **PASS**. Def `NanoHTTPD.java:159-162` verified (private ctor, fields assigned :160-161). Call at `createClientHandler` :1580 (`new ClientHandler(inputStream, finalAccept)`) verified; that factory is reached only via the listener thread (`ServerRunnable.run` :1347), hence INFERRED.
- Row 36 — NanoHTTPD$Cookie.getHTTPTime — UNREACHABLE — **PASS (as proposed)**. Def `NanoHTTPD.java:197-203` verified. Printed callers are exactly the two the file names, both on dead paths: the `(String,String,int)` Cookie ctor body at :211 (that ctor is never constructed in printed code — the only `new Cookie(` site is `CookieHandler.set` at :284, which uses the 3-arg String ctor) and `CookieHandler.set` at :284 (itself uncalled; its only printed caller is `delete` :253, which is itself uncalled per batch 15 row 38). The file's still-owed saved full-repo grep remains owed before merge.

## Totals

- Checked: 8. **PASS: 6. FAIL: 2** (rows 21, 26 — both citation-only).
- No label was found wrong. No proposed label correction. Two citation corrections proposed (row 21: safeClose 1511-1519 → 1511-1527; row 26: TorrentStreamServer super.start() :77 → :78).
