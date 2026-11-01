# LibreTorrent batch 16 — Phase 2 spot-check (UNVERIFIED proposal, labels only)

- Work file checked: `~/workspace/overnight/stream-A/work/batch16-merge-ready.md` (40 rows).
- Spot-check date: 2026-11-01. No merge-ready file was edited, no label was changed by this check, no push was made, no build/sampler/C1 was run (not this task).
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (281-file Java tree). No GitHub connector fetch was needed; no 429 was hit.
- Verdict rule: PASS requires the label AND the cited definition/caller lines to identify the right method and caller. A range running past the closing brace onto a blank line or the class-close brace is a nit, not a FAIL. A range that starts on the wrong line, ends mid-method, or names the wrong caller line is a FAIL.
- Phase 1 note: this file carries no dated 2026-11-01 Phase 1c revision (it was not in a Phase 1c application group), so there are no additional Phase 1 changed rows beyond the sample.

## Rows checked (8 of 40)

Sample rows 1, 6, 11, 16, 21, 26, 31, 36.

## Per-row verdicts

- Row 1 — NanoHTTPD$CookieHandler.set(String,String,int) — UNREACHABLE — **PASS (as proposed)**. Def `NanoHTTPD.java:283-285` verified (`queue.add(new Cookie(name, value, Cookie.getHTTPTime(expires)))` :284). Only printed caller is `delete` at :253 (`set(name, "-delete-", -30)`), and `delete` itself has no printed caller (batch 15 row 38; corpus-wide grep finds no `CookieHandler` delete call outside `NanoHTTPD.java`). The file's still-owed saved full-repo grep remains owed before merge.
- Row 6 — NanoHTTPD$DefaultAsyncRunner.closed — REACHABLE INFERRED — **PASS**. Def `NanoHTTPD.java:326-328` verified (`running.remove(clientHandler)` :327). Call at `ClientHandler.run` finally :192 (`NanoHTTPD.this.asyncRunner.closed(this)`) verified; `run` itself is Thread-dispatched, hence INFERRED.
- Row 11 — NanoHTTPD$DefaultTempFile.delete — UNREACHABLE branch_never_taken — **PASS (as proposed)**. Def `NanoHTTPD.java:355-360` verified (`safeClose(fstream)` :356, `file.delete()` :357). The caller `DefaultTempFileManager.clear()` :391-401 does run (`HTTPSession.execute` finally :754, `tempFileManager.clear()`), but its loop iterates `tempFiles`, and corpus-wide grep shows the only `tempFiles.add` is at :404 inside `createTempFile` — the dead parseBody-subtree path (row 15 / row 33). The loop therefore never iterates in the printed app path, so `branch_never_taken` (not `no_trigger_in_app`) is the correct kind. The file's still-owed saved full-repo grep remains owed before merge.
- Row 16 — NanoHTTPD$DefaultTempFileManagerFactory.\<init\> — REACHABLE SOURCE — **PASS**. Construction at `NanoHTTPD` ctor :1560 (`setTempFileManagerFactory(new DefaultTempFileManagerFactory())`) verified; the factory ctor takes the enclosing `NanoHTTPD`, matching the `(Lorg/nanohttpd/NanoHTTPD;)V` descriptor.
- Row 21 — NanoHTTPD$HTTPSession.decodeParms — REACHABLE INFERRED — **PASS**. Def `NanoHTTPD.java:637-653` verified (`decodePercent` :648/:650). Live caller `decodeHeader` :513 verified (the other caller, `parseBody` :921, is in the dead subtree, but the live caller alone suffices). `execute` runs only on a ClientHandler thread, hence INFERRED.
- Row 26 — NanoHTTPD$HTTPSession.getBoundaryPositions — UNREACHABLE — **PASS (as proposed)**. Def `NanoHTTPD.java:781` verified. Only printed caller is `decodeMultipartFormData` :546, which is itself called only from `parseBody` :913 — the row-33 dead subtree (base `serve` is overridden by `TorrentStreamServer.serve` :111 with no `super.serve` call). The file's still-owed saved full-repo grep remains owed before merge.
- Row 31 — NanoHTTPD$HTTPSession.getTmpBucket — UNREACHABLE — **PASS (as proposed)**. Def `NanoHTTPD.java:840-844` verified (`createTempFile` :842, `getName` :843). Only printed caller is `parseBody` :876, in the same dead subtree as row 26. The file's still-owed saved full-repo grep remains owed before merge.
- Row 36 — NanoHTTPD$Method.\<clinit\> — REACHABLE INFERRED — **PASS**. `Method` is an enum at `NanoHTTPD.java:993`; first live use is `HTTPSession.execute` :708 (`Method.lookup(pre.get("method"))`), which triggers JVM enum initialisation. INFERRED is correct (no source line for `<clinit>` itself).

## Totals

- Checked: 8. **PASS: 8. FAIL: 0.**
- No label found wrong, no citation found wrong, no correction proposed.
