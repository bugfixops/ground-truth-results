# Batch 17 source audit

Membership is the 40 rows in `batch_017_plan.txt`. Source excerpts and the generated-class grep are saved in `batch_017_helper_printed.txt`.

Seven methods have source-supported no-trigger findings. The 33 remaining entries include response-send paths whose complete app entry route is not handwritten, thread/socket callbacks, and generated Data Binding mapper methods lacking source. Those remain OPEN. No coverage evidence was used.

| Method | Label | Evidence / reason |
|---|---|---|
| `NanoHTTPD$Response.getData` | UNREACHABLE/no_trigger_in_app | No request-path or app caller; `NanoHTTPD.java:1147-1149`. |
| `NanoHTTPD$Response.getHeader(String)` | OPEN | Called from session execute; request route not yet handwritten; `NanoHTTPD.java:720-734`. |
| `NanoHTTPD$Response.getMimeType` | OPEN | Called during gzip response setup; request route remains OPEN; `NanoHTTPD.java:1660-1662,726-731`. |
| `NanoHTTPD$Response.getRequestMethod` | UNREACHABLE/no_trigger_in_app | No source caller; `NanoHTTPD.java:1161-1163`. |
| `NanoHTTPD$Response.getStatus` | UNREACHABLE/no_trigger_in_app | Response.send reads field directly; `NanoHTTPD.java:1164-1166,1188-1192`. |
| `NanoHTTPD$Response.headerAlreadySent(Map,String)` | OPEN | Called by Response.send; request route remains OPEN; `NanoHTTPD.java:1205-1219`. |
| `NanoHTTPD$Response.send(OutputStream)` | OPEN | Called by session execute; entry route remains OPEN; `NanoHTTPD.java:731`. |
| `NanoHTTPD$Response.sendBody(OutputStream,long)` | OPEN | Called by body encoding helpers; request route remains OPEN; `NanoHTTPD.java:1239-1246`. |
| `NanoHTTPD$Response.sendBodyWithCorrectEncoding(OutputStream,long)` | OPEN | Internal response path; request route remains OPEN; `NanoHTTPD.java:1230-1246`. |
| `NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding(OutputStream,long)` | OPEN | Called by Response.send; route remains OPEN; `NanoHTTPD.java:1215-1224`. |
| `NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent(PrintWriter,Map,long)` | OPEN | Called by Response.send; route remains OPEN; `NanoHTTPD.java:1215-1220`. |
| `NanoHTTPD$Response.setChunkedTransfer(boolean)` | OPEN | Response branch is reachable candidate, but complete route is not handwritten; `NanoHTTPD.java:1208-1214`. |
| `NanoHTTPD$Response.setData(InputStream)` | UNREACHABLE/no_trigger_in_app | No source call; app constructs responses with constructors; `NanoHTTPD.java:1293-1295`. |
| `NanoHTTPD$Response.setGzipEncoding(boolean)` | OPEN | Session response setup call; route remains OPEN; `NanoHTTPD.java:726-731`. |
| `NanoHTTPD$Response.setKeepAlive(boolean)` | OPEN | Session response setup call; route remains OPEN; `NanoHTTPD.java:726-731`. |
| `NanoHTTPD$Response.setMimeType(String)` | OPEN | App's DLNA header helper calls it; request route remains OPEN; `TorrentStreamServer.java:281`. |
| `NanoHTTPD$Response.setRequestMethod(Method)` | OPEN | Session response setup call; route remains OPEN; `NanoHTTPD.java:726-731`. |
| `NanoHTTPD$Response.setStatus(IStatus)` | UNREACHABLE/no_trigger_in_app | No source caller; `NanoHTTPD.java:1302-1304`. |
| `NanoHTTPD$Response$ChunkedOutputStream.<init>(OutputStream)` | OPEN | Constructed for chunked response; route/branch remain OPEN; `NanoHTTPD.java:1230-1234`. |
| `NanoHTTPD$Response$ChunkedOutputStream.finish` | OPEN | Chunked response helper; route/branch remain OPEN; `NanoHTTPD.java:1230-1234`. |
| `NanoHTTPD$Response$ChunkedOutputStream.write(int)` | OPEN | Possible stream dispatch during chunked response; `NanoHTTPD.java:1069-1075`. |
| `NanoHTTPD$Response$ChunkedOutputStream.write(byte[])` | OPEN | Possible stream dispatch during chunked response; `NanoHTTPD.java:1077-1079`. |
| `NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int)` | OPEN | Called by chunked body copy; upstream route remains OPEN; `NanoHTTPD.java:1230-1234,1261-1275`. |
| `NanoHTTPD$Response$Status.<clinit>` | OPEN | Enum is used in response construction; full route remains OPEN; `NanoHTTPD.java:1023-1044`. |
| `NanoHTTPD$Response$Status.<init>(String,int,int,String)` | OPEN | Enum constant constructor; response route remains OPEN; `NanoHTTPD.java:1023-1050`. |
| `NanoHTTPD$Response$Status.getDescription` | OPEN | Called by Response.send; request route remains OPEN; `NanoHTTPD.java:1051-1054,1188-1192`. |
| `NanoHTTPD$Response$Status.getRequestStatus` | UNREACHABLE/no_trigger_in_app | No source caller; `NanoHTTPD.java:1055-1058`. |
| `NanoHTTPD$ResponseException.<init>(Status,String)` | OPEN | Request parsing error branch; request route remains OPEN; `NanoHTTPD.java:503-507,710`. |
| `NanoHTTPD$ResponseException.<init>(Status,String,Exception)` | OPEN | Request decoding error branch; request route remains OPEN; `NanoHTTPD.java:538`. |
| `NanoHTTPD$ResponseException.getStatus` | OPEN | Read in request error response handler; request route remains OPEN; `NanoHTTPD.java:748-750`. |
| `NanoHTTPD$SecureServerSocketFactory.create` | UNREACHABLE/no_trigger_in_app | Only installed via makeSecure; app has no call to makeSecure or setServerSocketFactory. `NanoHTTPD.java:1684-1685`. |
| `NanoHTTPD$ServerRunnable.<init>(NanoHTTPD,int)` | OPEN | Created during server start; complete engine entry route remains OPEN; `NanoHTTPD.java:1813-1817`. |
| `NanoHTTPD$ServerRunnable.run` | OPEN | Thread callback and server activation path remain OPEN; `NanoHTTPD.java:1816-1820`. |
| `libretorrent.DataBinderMapperImpl.<clinit>` | OPEN | Generated source absent in rule-F grep; mapper loading route unavailable. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.<init>` | OPEN | Generated source absent in rule-F grep; no hand route. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.collectDependencies` | OPEN | Generated source and library invocation absent. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.convertBrIdToString` | OPEN | Generated source and direct app caller absent. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)` | OPEN | Generated mapper dispatch not source-verified. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)` | OPEN | Generated mapper dispatch not source-verified. `batch_017_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl.getLayoutId(String)` | OPEN | Generated source and hand route absent. `batch_017_helper_printed.txt` |

Count: 40 plan rows; 0 REACHABLE; 7 `UNREACHABLE/no_trigger_in_app`; 33 OPEN. No coverage evidence was used.
