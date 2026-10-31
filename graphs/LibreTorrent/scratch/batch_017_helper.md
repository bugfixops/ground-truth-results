# LibreTorrent batch 17 helper audit

Membership comes only from batch 17 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the query printed 40 rows. Printed evidence and the generated-class grep are in `scratch/batch_017_helper_printed.txt`.

OPEN means a possible source route exists but the full route is not established. No graph, notes, output, or coverage files were changed.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `NanoHTTPD$Response.getData` | UNREACHABLE `no_trigger_in_app` | Declaration returns stored data (`NanoHTTPD.java:1147-1149`); focused caller search found no call from request handling or the only app subclass. |
| 2 | `NanoHTTPD$Response.getHeader(String)` | OPEN | Called by `HTTPSession.execute` to check connection header (`NanoHTTPD.java:720-734`); request route depends on unresolved server thread/socket callback path. |
| 3 | `NanoHTTPD$Response.getMimeType` | OPEN | Called in `useGzipWhenAccepted` (`NanoHTTPD.java:1660-1662`), itself called during request response setup (`NanoHTTPD.java:726-731`); callback route remains open. |
| 4 | `NanoHTTPD$Response.getRequestMethod` | UNREACHABLE `no_trigger_in_app` | Getter body printed (`NanoHTTPD.java:1161-1163`); no call site found in NanoHTTPD or app source. |
| 5 | `NanoHTTPD$Response.getStatus` | UNREACHABLE `no_trigger_in_app` | Getter body printed (`NanoHTTPD.java:1164-1166`); Response.send reads the `status` field directly (`NanoHTTPD.java:1188-1192`), and no call site was found. |
| 6 | `NanoHTTPD$Response.headerAlreadySent(Map,String)` | OPEN | Called in `Response.send` (`NanoHTTPD.java:1205-1219`); response send depends on request handling path. |
| 7 | `NanoHTTPD$Response.send(OutputStream)` | OPEN | Called by `HTTPSession.execute` (`NanoHTTPD.java:731`); request callback/entry path remains open. |
| 8 | `NanoHTTPD$Response.sendBody(OutputStream,long)` | OPEN | Called by `sendBodyWithCorrectEncoding` (`NanoHTTPD.java:1239-1246`); a response send path is visible, but its upstream request route is open. |
| 9 | `NanoHTTPD$Response.sendBodyWithCorrectEncoding(OutputStream,long)` | OPEN | Called from transfer encoding helper (`NanoHTTPD.java:1230-1246`); request route remains open. |
| 10 | `NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding(OutputStream,long)` | OPEN | Directly called by `Response.send` (`NanoHTTPD.java:1215-1224`); request route remains open. |
| 11 | `NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent(PrintWriter,Map,long)` | OPEN | Called from `Response.send` (`NanoHTTPD.java:1215-1220`); request route remains open. |
| 12 | `NanoHTTPD$Response.setChunkedTransfer(boolean)` | OPEN | Called in the gzip branch of `Response.send` (`NanoHTTPD.java:1208-1214`); app response paths include text/plain error responses, so no source proof makes the branch impossible. |
| 13 | `NanoHTTPD$Response.setData(InputStream)` | UNREACHABLE `no_trigger_in_app` | Declaration/body printed (`NanoHTTPD.java:1293-1295`); focused source search found no call; app builds responses with constructors instead. |
| 14 | `NanoHTTPD$Response.setGzipEncoding(boolean)` | OPEN | Called by `HTTPSession.execute` (`NanoHTTPD.java:726-731`); request route remains open. |
| 15 | `NanoHTTPD$Response.setKeepAlive(boolean)` | OPEN | Called by `HTTPSession.execute` (`NanoHTTPD.java:726-731`); request route remains open. |
| 16 | `NanoHTTPD$Response.setMimeType(String)` | OPEN | `TorrentStreamServer.DLNAFileType.setHeaders` calls it (`TorrentStreamServer.java:281`); entry depends on the unresolved server request route. |
| 17 | `NanoHTTPD$Response.setRequestMethod(Method)` | OPEN | Called from `HTTPSession.execute` (`NanoHTTPD.java:726-731`); request route remains open. |
| 18 | `NanoHTTPD$Response.setStatus(IStatus)` | UNREACHABLE `no_trigger_in_app` | Declaration/body printed (`NanoHTTPD.java:1302-1304`); no call site found in NanoHTTPD or app source. |
| 19 | `NanoHTTPD$Response$ChunkedOutputStream.<init>(OutputStream)` | OPEN | Constructed only by response body transfer when chunked (`NanoHTTPD.java:1230-1234`); request path and chunking branch remain uncertain. |
| 20 | `NanoHTTPD$Response$ChunkedOutputStream.finish()` | OPEN | Called after chunked body send (`NanoHTTPD.java:1230-1234`); request path and chunking branch remain uncertain. |
| 21 | `NanoHTTPD$Response$ChunkedOutputStream.write(int)` | OPEN | Body printed (`NanoHTTPD.java:1069-1075`); stream API dispatch can reach it on chunked response path, which is not fully established. |
| 22 | `NanoHTTPD$Response$ChunkedOutputStream.write(byte[])` | OPEN | Body printed (`NanoHTTPD.java:1077-1079`); possible stream API dispatch on chunked response path is not ruled out. |
| 23 | `NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int)` | OPEN | Called by response body copy when chunked (`NanoHTTPD.java:1230-1234,1261-1275`); upstream response route remains open. |
| 24 | `NanoHTTPD$Response$Status.<clinit>` | OPEN | Enum constants initialize status values used throughout response construction (`NanoHTTPD.java:1023-1044`); request route is not independently completed. |
| 25 | `NanoHTTPD$Response$Status.<init>(String,int,int,String)` | OPEN | Enum constant construction at `NanoHTTPD.java:1023-1044` reaches this constructor (`NanoHTTPD.java:1047-1050`); status use depends on open response routes. |
| 26 | `NanoHTTPD$Response$Status.getDescription` | OPEN | Called by `Response.send` through `IStatus` (`NanoHTTPD.java:1051-1054,1188-1192`); request route remains open. |
| 27 | `NanoHTTPD$Response$Status.getRequestStatus` | UNREACHABLE `no_trigger_in_app` | Getter body printed (`NanoHTTPD.java:1055-1058`); focused source search found no caller. |
| 28 | `NanoHTTPD$ResponseException.<init>(Status,String)` | OPEN | Constructed by HTTP request parsing error branches (`NanoHTTPD.java:503-507,710`); client request path remains open. |
| 29 | `NanoHTTPD$ResponseException.<init>(Status,String,Exception)` | OPEN | Constructed in request decoding error handling (`NanoHTTPD.java:538`); client request path remains open. |
| 30 | `NanoHTTPD$ResponseException.getStatus` | OPEN | Used by request error response handler (`NanoHTTPD.java:748-750`); request path remains open. |
| 31 | `NanoHTTPD$SecureServerSocketFactory.create()` | UNREACHABLE `no_trigger_in_app` | It is installed only by `NanoHTTPD.makeSecure` (`NanoHTTPD.java:1684-1685`); caller search found no app call to `makeSecure` or `setServerSocketFactory`. |
| 32 | `NanoHTTPD$ServerRunnable.<init>(NanoHTTPD,int)` | OPEN | Created by `createServerRunnable` in `NanoHTTPD.start(int,boolean)` (`NanoHTTPD.java:1813-1817`); server activation chain to an app entry remains open. |
| 33 | `NanoHTTPD$ServerRunnable.run()` | OPEN | Run through a `Thread` started by `NanoHTTPD.start` (`NanoHTTPD.java:1816-1820`); thread callback dispatch and upstream activation are not evidenced here. |
| 34 | `libretorrent.DataBinderMapperImpl.<clinit>` | OPEN | Generated implementation has no source match in the saved grep over the Java source root; mapper loading route and generated code are not available for verification. |
| 35 | `libretorrent.DataBinderMapperImpl.<init>` | OPEN | Generated implementation source absent from source-root grep; no hand source route established. |
| 36 | `libretorrent.DataBinderMapperImpl.collectDependencies` | OPEN | Generated implementation source absent from source-root grep; dependency mapper invocation would require library/generated-code evidence. |
| 37 | `libretorrent.DataBinderMapperImpl.convertBrIdToString` | OPEN | Generated implementation source absent from source-root grep; no direct app caller established. |
| 38 | `libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)` | OPEN | Generated implementation source absent from source-root grep; Data Binding library dispatch is not source-verified. |
| 39 | `libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)` | OPEN | Generated implementation source absent from source-root grep; Data Binding library dispatch is not source-verified. |
| 40 | `libretorrent.DataBinderMapperImpl.getLayoutId(String)` | OPEN | Generated implementation source absent from source-root grep; no hand source route established. |

The table has 40 rows: 33 OPEN and 7 UNREACHABLE (`no_trigger_in_app`). I did not claim framework callback dispatch or generated-code behavior without source evidence.
