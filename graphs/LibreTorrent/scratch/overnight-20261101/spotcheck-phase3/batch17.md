# Spot-check — batch 17 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 17/1 NanoHTTPD$Response.getData — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1147-1149; sendBody reads this.data directly (:1266-1271), not via getData(); no .getData() caller in freshly printed files (pending saved full-repo grep, noted in row).
- 17/6 NanoHTTPD$Response.headerAlreadySent — REACHABLE SOURCE — PASS. Definition :1173-1179 (private static); calls inside send :1205 and :1208, via trunk step 15.
- 17/11 NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent — REACHABLE SOURCE — PASS. Definition :1277-1288; call at send :1219, non-chunked/non-gzip branch; fixed-length responses from TorrentStreamServer.handleTorrent reach send with encodeAsGzip false.
- 17/16 NanoHTTPD$Response.setMimeType — REACHABLE SOURCE — PASS. Definition :1296-1298; call at DLNAFileType.setHeaders, TorrentStreamServer.java:281, called from TorrentStreamServer.serve :119-120.
- 17/21 NanoHTTPD$Response$ChunkedOutputStream.write(int) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition :1070-1075; body calls write(data, 0, 1) at :1074 (3-arg form); no printed caller calls write(int) in freshly printed files (pending saved full-repo grep, noted in row).
- 17/26 NanoHTTPD$Response$Status.getDescription — REACHABLE SOURCE — PASS. Definition :1052-1054; call at send :1192, via trunk step 15; this is the IStatus.getDescription implementation (:1017).
- 17/31 NanoHTTPD$SecureServerSocketFactory.create — UNREACHABLE no_trigger_in_app INFERRED — PASS. Only installer printed is makeSecure :1684 and setServerSocketFactory :1672; no printed caller of either in freshly printed files (start :1814 calls getServerSocketFactory().create() virtually, but the factory is never installed on the printed path).
- 17/36 libretorrent.DataBinderMapperImpl.collectDependencies — OPEN — PASS. Same as row 34; mapper absence at the app-package path re-confirmed (clean connector file-not-found, not a 429); saved class-name grep over all 252 app Java files for DataBinderMapperImpl/InnerBrLookup/InnerLayoutIdLookup cited. OPEN confirmed_by is —, as required.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
