# Batch 15 source audit

Membership is the exact 40 rows in `batch_015_plan.txt`. Printed source and helper caller findings are in `batch_015_helper_printed.txt`; independently printed method dispatch and declarations are in `batch_015_independent_printed.txt`.

Five methods are source-supported `UNREACHABLE/no_trigger_in_app`: NanoHTTPD's base `serve` overloads are bypassed by the uploaded `TorrentStreamServer.serve(IHTTPSession)` override, and three CookieHandler APIs have no app/parser call site. The other 35 remain OPEN because their local paths do not establish a complete route from an app entry, or because a thread/socket callback is delegated to library/framework code whose dispatch is not fully sourced here.

| Method | Label | Evidence / reason |
|---|---|---|
| `Hash.getValue` | OPEN | App call exists; MediaRSS object route is OPEN. `FeedParser.java:215-224`; `batch_015_helper_printed.txt` |
| `Hash.hashCode` | OPEN | No direct app caller; indirect collection use not ruled out. `Hash.java:66-71` |
| `Hash.setAlgorithm` | OPEN | Parser invokes it, but parent SAX route is OPEN. `MediaRssParser.java:68-73` |
| `Hash.toString` | OPEN | No explicit call; implicit stringification not ruled out. `Hash.java:73-80` |
| `MediaRss.<init>` | OPEN | Constructed through parser whose parent callback route is OPEN. `MediaRssParser.java:29-37` |
| `MediaRss.getContent` | OPEN | App calls it; MediaRSS object route is OPEN. `FeedParser.java:188-207` |
| `MediaRss.getHash` | OPEN | App calls it; MediaRSS object route is OPEN. `FeedParser.java:215-224` |
| `MediaRss.toString` | OPEN | No explicit call; implicit stringification not ruled out. `MediaRss.java:42-49` |
| `PeerLink.<init>` | OPEN | Constructed through parser whose parent callback route is OPEN. `MediaRssParser.java:76-90` |
| `PeerLink.equals` | OPEN | No direct caller; indirect collection use not ruled out. `PeerLink.java:42-52` |
| `PeerLink.hashCode` | OPEN | No direct caller; indirect collection use not ruled out. `PeerLink.java:54-59` |
| `PeerLink.toString` | OPEN | No explicit call; implicit stringification not ruled out. `PeerLink.java:61-68` |
| `NanoHTTPD.<clinit>` | OPEN | Local route through TorrentStreamServer exists, but full engine entry path remains unchecked. `TorrentEngine.java:1063-1071`; helper print |
| `NanoHTTPD.<init>(String,int)` | OPEN | App subclass calls super; complete entry route remains unchecked. `TorrentStreamServer.java:67-70` |
| `NanoHTTPD.createClientHandler` | OPEN | Called after socket accept; socket route remains OPEN. `NanoHTTPD.java:1332-1347` |
| `NanoHTTPD.createServerRunnable` | OPEN | Internal server start path; app entry route remains OPEN. `NanoHTTPD.java:1813-1817` |
| `NanoHTTPD.decodePercent` | OPEN | Request parsing path depends on socket callback route. `NanoHTTPD.java:494-517,637-651` |
| `NanoHTTPD.getServerSocketFactory` | OPEN | Internal server start path; app entry route remains OPEN. `NanoHTTPD.java:1813-1816` |
| `NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long)` | OPEN | App subclass and request paths call this API; server/request route remains OPEN. `batch_015_helper_printed.txt` |
| `NanoHTTPD.newFixedLengthResponse(IStatus,String,String)` | OPEN | Request response path is not yet connected to an audited entry. `batch_015_helper_printed.txt` |
| `NanoHTTPD.safeClose` | OPEN | Cleanup/request/server paths exist; upstream server route remains OPEN. `NanoHTTPD.java:163-165,188-192,747,751,753,1837-1842` |
| `NanoHTTPD.serve(String,Method,Map,Map,Map)` | UNREACHABLE | Only base serve(IHTTPSession) calls it; app override does not call super. `NanoHTTPD.java:1732-1746,1750-1770`; `TorrentStreamServer.java:110-121` |
| `NanoHTTPD.serve(IHTTPSession)` | UNREACHABLE | ClientHandler's virtual call dispatches to app override; override does not call super. `NanoHTTPD.java:720`; `TorrentStreamServer.java:110-121` |
| `NanoHTTPD.setAsyncRunner(AsyncRunner)` | OPEN | Constructor caller exists, but constructor route is OPEN. `NanoHTTPD.java:1557-1562` |
| `NanoHTTPD.setTempFileManagerFactory(TempFileManagerFactory)` | OPEN | Constructor caller exists, but constructor route is OPEN. `NanoHTTPD.java:1557-1562` |
| `NanoHTTPD.start()` | OPEN | App wrapper calls super; engine entry route remains unchecked. `TorrentStreamServer.java:72-79`; `TorrentEngine.java:1069-1071` |
| `NanoHTTPD.start(int)` | OPEN | Internal call from start; outer route remains OPEN. `NanoHTTPD.java:1794-1801` |
| `NanoHTTPD.start(int,boolean)` | OPEN | Internal call from start; outer route remains OPEN. `NanoHTTPD.java:1800-1821` |
| `NanoHTTPD.stop()` | OPEN | App wrapper calls super; engine entry route remains unchecked. `TorrentStreamServer.java:81-87`; `TorrentEngine.java:1079-1082` |
| `NanoHTTPD.useGzipWhenAccepted(Response)` | OPEN | Called in HTTP session handling; request route remains OPEN. `NanoHTTPD.java:720-731` |
| `NanoHTTPD$ClientHandler.<init>` | OPEN | Created after socket accept; socket callback route remains OPEN. `NanoHTTPD.java:1579-1581,1342-1347` |
| `NanoHTTPD$ClientHandler.close` | OPEN | Cleanup body known; async runner invocation not ruled out. `NanoHTTPD.java:163-165` |
| `NanoHTTPD$ClientHandler.run` | OPEN | Passed as Runnable; async invocation needs source/framework evidence. `NanoHTTPD.java:1342-1347` |
| `NanoHTTPD$Cookie.<init>(String,String,String)` | OPEN | CookieHandler.set constructs it; app cookie route not established. `NanoHTTPD.java:213-217,283-285` |
| `NanoHTTPD$Cookie.getHTTPHeader` | OPEN | Called while unloading response cookie queue; request route remains OPEN. `NanoHTTPD.java:294-297,713-728` |
| `NanoHTTPD$Cookie.getHTTPTime(int)` | OPEN | Called by cookie constructors/set; app cookie route not established. `NanoHTTPD.java:197-211,283-285` |
| `NanoHTTPD$CookieHandler.<init>` | OPEN | Constructed during session execution; request route remains OPEN. `NanoHTTPD.java:713` |
| `NanoHTTPD$CookieHandler.delete(String)` | UNREACHABLE | Only its body delegates to set; no source caller found. `NanoHTTPD.java:252-254`; `batch_015_independent_printed.txt` |
| `NanoHTTPD$CookieHandler.iterator` | UNREACHABLE | Declaration/body only; no source caller found. `NanoHTTPD.java:255-259`; `batch_015_independent_printed.txt` |
| `NanoHTTPD$CookieHandler.read(String)` | UNREACHABLE | No source call found. `NanoHTTPD.java:260-269`; `batch_015_independent_printed.txt` |

Count: 40 plan rows; 0 REACHABLE; 5 `UNREACHABLE/no_trigger_in_app`; 35 OPEN. No coverage evidence was used.
