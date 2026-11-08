# Batch 16 source audit

Membership is exactly the 40 rows in `batch_016_plan.txt`; helper source excerpts and caller searches are in `batch_016_helper_printed.txt`.

The NanoHTTPD base `serve(IHTTPSession)` path is bypassed because `TorrentStreamServer` overrides it and does not call `super.serve(session)`. Sixteen methods whose only source callers are on that body/multipart path, or unused CookieHandler APIs, are labeled UNREACHABLE `no_trigger_in_app`. The other methods have source-local calls in the stream server or HTTP framework but lack a complete hand-authored graph route from an entry point; they remain OPEN.

| Method | Label | Reason / source evidence |
|---|---|---|
| `NanoHTTPD$CookieHandler.set(String,String,int)` | UNREACHABLE | Only caller is the unused `delete`; `NanoHTTPD.java:252-254,283-285`. |
| `NanoHTTPD$CookieHandler.set(Cookie)` | UNREACHABLE | No app call; `NanoHTTPD.java:270-272`. |
| `NanoHTTPD$CookieHandler.unloadQueue` | OPEN | HTTP response path local caller, but entry route not handwritten; `NanoHTTPD.java:723-728`. |
| `NanoHTTPD$DefaultAsyncRunner.<init>` | OPEN | Constructed in HTTPD constructor; entry route not handwritten; `NanoHTTPD.java:1557-1562`. |
| `NanoHTTPD$DefaultAsyncRunner.closeAll` | OPEN | Called during stop; complete graph route not handwritten; `NanoHTTPD.java:1837-1842`. |
| `NanoHTTPD$DefaultAsyncRunner.closed` | OPEN | ClientHandler finally block; async route not handwritten; `NanoHTTPD.java:188-193`. |
| `NanoHTTPD$DefaultAsyncRunner.exec` | OPEN | Accept loop submits client handler; complete route not handwritten; `NanoHTTPD.java:1340-1348,330-336`. |
| `NanoHTTPD$DefaultServerSocketFactory.<init>` | OPEN | Default field initialization; complete stream-server route not handwritten; `NanoHTTPD.java:1531`. |
| `NanoHTTPD$DefaultServerSocketFactory.create` | OPEN | Server start path; complete route not handwritten; `NanoHTTPD.java:1813-1818`. |
| `NanoHTTPD$DefaultTempFile.<init>` | UNREACHABLE | Only constructed through body parsing bypassed by app override; `NanoHTTPD.java:402-405,865-877,1732-1747`. |
| `NanoHTTPD$DefaultTempFile.delete` | UNREACHABLE | Reached only for files appended by unreachable createTempFile; `NanoHTTPD.java:391-405,865-877`. |
| `NanoHTTPD$DefaultTempFile.getName` | UNREACHABLE | Only in body parsing paths bypassed by app override; `NanoHTTPD.java:362-364,840-844,944-956`. |
| `NanoHTTPD$DefaultTempFileManager.<init>` | OPEN | Per-client manager creation; complete route not handwritten; `NanoHTTPD.java:172-175,411-415`. |
| `NanoHTTPD$DefaultTempFileManager.clear` | OPEN | Session cleanup calls it; complete route not handwritten; `NanoHTTPD.java:750-755,391-400`. |
| `NanoHTTPD$DefaultTempFileManager.createTempFile` | UNREACHABLE | Only called on body parsing path bypassed by override; `NanoHTTPD.java:402-405,865-877,1732-1747`. |
| `NanoHTTPD$DefaultTempFileManagerFactory.<init>` | OPEN | Constructed by HTTPD constructor; route not handwritten; `NanoHTTPD.java:1557-1562`. |
| `NanoHTTPD$DefaultTempFileManagerFactory.create` | OPEN | Called by client handler; route not handwritten; `NanoHTTPD.java:172-175,411-415`. |
| `NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream,InetAddress)` | OPEN | Called by ClientHandler; socket/async route not handwritten; `NanoHTTPD.java:172-175,484-490`. |
| `NanoHTTPD$HTTPSession.decodeHeader` | OPEN | Called within execute; full entry route not handwritten; `NanoHTTPD.java:702-704,494-542`. |
| `NanoHTTPD$HTTPSession.decodeMultipartFormData` | UNREACHABLE | Called only from body parser bypassed by app override; `NanoHTTPD.java:544-547,907-915,1732-1747`. |
| `NanoHTTPD$HTTPSession.decodeParms` | OPEN | Called by decodeHeader; full entry route not handwritten; `NanoHTTPD.java:510-515,637-654`. |
| `NanoHTTPD$HTTPSession.execute` | OPEN | ClientHandler calls it; async/socket entry route not handwritten; `NanoHTTPD.java:172-175,655-760`. |
| `NanoHTTPD$HTTPSession.findHeaderEnd` | OPEN | Called by execute; full route not handwritten; `NanoHTTPD.java:680-687,761-779`. |
| `NanoHTTPD$HTTPSession.getAttributeFromContentHeader` | UNREACHABLE | Only body multipart caller; `NanoHTTPD.java:907-915,936-939,1732-1747`. |
| `NanoHTTPD$HTTPSession.getBodySize` | UNREACHABLE | Only executable caller is unreachable body parsing; `NanoHTTPD.java:717,856-868`. |
| `NanoHTTPD$HTTPSession.getBoundaryPositions` | UNREACHABLE | Only called by unreachable multipart parser; `NanoHTTPD.java:544-547,781-805`. |
| `NanoHTTPD$HTTPSession.getHeaders` | OPEN | App stream handler uses it; full entry route not handwritten; `TorrentStreamServer.java:150-166`. |
| `NanoHTTPD$HTTPSession.getMethod` | UNREACHABLE | Only executable caller is base serve bypassed by override; `NanoHTTPD.java:829-831,1732-1747`. |
| `NanoHTTPD$HTTPSession.getParms` | OPEN | App stream handler uses it; full entry route not handwritten; `TorrentStreamServer.java:129-142`. |
| `NanoHTTPD$HTTPSession.getQueryParameterString` | UNREACHABLE | Only called by base serve bypassed by override; `NanoHTTPD.java:837-839,1732-1747`. |
| `NanoHTTPD$HTTPSession.getTmpBucket` | UNREACHABLE | Only body parsing caller; `NanoHTTPD.java:840-847,865-877,1732-1747`. |
| `NanoHTTPD$HTTPSession.getUri` | OPEN | App stream handler uses it; full entry route not handwritten; `TorrentStreamServer.java:110-115,129-131`. |
| `NanoHTTPD$HTTPSession.parseBody` | UNREACHABLE | Base serve path bypassed by app override; `NanoHTTPD.java:865-935,1732-1747`; `TorrentStreamServer.java:110-121`. |
| `NanoHTTPD$HTTPSession.saveTmpFile` | UNREACHABLE | Only multipart/PUT branches of unreachable parseBody; `NanoHTTPD.java:606,929-930,944-960`. |
| `NanoHTTPD$HTTPSession.scipOverNewLine` | UNREACHABLE | Only multipart parser caller; `NanoHTTPD.java:590-592,625-630,544-547`. |
| `NanoHTTPD$Method.<clinit>` | OPEN | Method lookup reads enum values; full request route not handwritten; `NanoHTTPD.java:708-710,993-1010`. |
| `NanoHTTPD$Method.lookup` | OPEN | Called by session execute; full request route not handwritten; `NanoHTTPD.java:708-710,1003-1010`. |
| `NanoHTTPD$Response.<init>` | OPEN | Stream server and HTTP response helpers construct responses; full route not handwritten; helper print. |
| `NanoHTTPD$Response.addHeader` | OPEN | Stream server adds response headers; full route not handwritten; helper print. |
| `NanoHTTPD$Response.close` | OPEN | Session cleanup closes response; full route not handwritten; `NanoHTTPD.java:750-755,1015,1135-1140`. |

Count: 40 plan rows; 0 REACHABLE; 16 `UNREACHABLE/no_trigger_in_app`; 24 OPEN. No coverage evidence was used.
