# Spot-check — batch 16 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 16/1 NanoHTTPD$CookieHandler.set(String,String,int) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :283-285; only printed caller is delete :253, and delete has no printed caller (batch 15 row 38) (proposal; saved full-repo grep owed before merge, noted in row).
- 16/6 NanoHTTPD$DefaultAsyncRunner.closed — REACHABLE INFERRED — PASS. Definition :326-328; caller ClientHandler.run finally :192; run is Thread-dispatched (exec :336).
- 16/11 NanoHTTPD$DefaultTempFile.delete — UNREACHABLE branch_never_taken INFERRED — PASS. Caller DefaultTempFileManager.clear() :391-401 does run (HTTPSession.execute finally :754), but clear's loop iterates tempFiles, which gain entries only via createTempFile (dead path), so the loop never executes the delete.
- 16/16 NanoHTTPD$DefaultTempFileManagerFactory.\<init\> — REACHABLE SOURCE — PASS. Constructed at NanoHTTPD ctor :1560 (setTempFileManagerFactory(new DefaultTempFileManagerFactory())) (printed direct call).
- 16/21 NanoHTTPD$HTTPSession.decodeParms — REACHABLE INFERRED — PASS. Definition :637-653; live caller decodeHeader :513 (parseBody :921 is dead).
- 16/26 NanoHTTPD$HTTPSession.getBoundaryPositions — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed caller is decodeMultipartFormData :546, itself parseBody-only (proposal; saved full-repo grep owed before merge, noted in row).
- 16/31 NanoHTTPD$HTTPSession.getTmpBucket — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only printed caller is parseBody :876, which never runs in the app path (proposal; saved full-repo grep owed before merge, noted in row).
- 16/36 NanoHTTPD$Method.\<clinit\> — REACHABLE INFERRED — PASS. Enum \<clinit\> runs on first Method class use in the live path, HTTPSession.execute :708 (Method.lookup); JVM class-load dispatch, not a printed call.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
