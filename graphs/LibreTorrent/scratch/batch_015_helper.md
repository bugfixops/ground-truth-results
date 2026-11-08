# LibreTorrent batch 15 helper audit

Membership is limited to batch 15 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the membership command printed exactly 40 rows. Printed source and call-site evidence are saved in `scratch/batch_015_helper_printed.txt`.

OPEN means the source shows a candidate path but the full entry route is not established. No graph edits or coverage evidence were used.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `Hash.getValue` | OPEN | App `FeedParser.watchMediaHash` calls it (`FeedParser.java:215-224`); the Media RSS result originates through callback-created feed items and that parser route is not proven here. |
| 2 | `Hash.hashCode` | OPEN | Body printed (`Hash.java:66-71`); no direct app call found; indirect collection invocation was not exhaustively excluded. |
| 3 | `Hash.setAlgorithm` | OPEN | `MediaRssParser.parseHash` calls it when an algo attribute exists (`MediaRssParser.java:68-73`); the parent item route depends on SAX callback delivery. |
| 4 | `Hash.toString` | OPEN | Body printed (`Hash.java:73-80`); no explicit app call found, and implicit stringification route was not established. |
| 5 | `MediaRss.<init>` | OPEN | Created in `MediaRssParser.parse` (`MediaRssParser.java:29-37`); the parser is called by RSS2 items but feed item delivery depends on unverified SAX callbacks. |
| 6 | `MediaRss.getContent` | OPEN | Called by app `FeedParser.watchMediaContent` (`FeedParser.java:188-207`); object route depends on the unverified RSS2 item callback path. |
| 7 | `MediaRss.getHash` | OPEN | Called by app `FeedParser.watchMediaHash` (`FeedParser.java:215-224`); object route depends on the unverified RSS2 item callback path. |
| 8 | `MediaRss.toString` | OPEN | Body printed (`MediaRss.java:42-49`); no app call found and implicit stringification was not ruled out. |
| 9 | `PeerLink.<init>` | OPEN | Created by `MediaRssParser.parsePeerLinks` (`MediaRssParser.java:76-90`); parser parent item route depends on unverified SAX callbacks. |
| 10 | `PeerLink.equals` | OPEN | Body printed (`PeerLink.java:42-52`); no direct app caller found, but indirect collection usage was not excluded. |
| 11 | `PeerLink.hashCode` | OPEN | Body printed (`PeerLink.java:54-59`); no direct app caller found, but indirect collection usage was not excluded. |
| 12 | `PeerLink.toString` | OPEN | Body printed (`PeerLink.java:61-68`); no app caller found, and implicit stringification was not ruled out. |
| 13 | `NanoHTTPD.<clinit>` | OPEN | Class has a source route through `TorrentStreamServer` construction (`TorrentEngine.java:1063-1071`), but the engine entry path was not followed to its app entry. |
| 14 | `NanoHTTPD.<init>(String,int)` | OPEN | `TorrentStreamServer` invokes `super(host,port)` (`TorrentStreamServer.java:67-70`); its construction is in `TorrentEngine.startStreamingServer` (`TorrentEngine.java:1063-1071`), whose full entry route remains to verify. |
| 15 | `NanoHTTPD.createClientHandler(Socket,InputStream)` | OPEN | Called from `ServerRunnable.run` after socket accept (`NanoHTTPD.java:1332-1347`); server runnable callback/entry evidence is unresolved. |
| 16 | `NanoHTTPD.createServerRunnable(int)` | OPEN | Called by `NanoHTTPD.start(int,boolean)` (`NanoHTTPD.java:1813-1817`); activation chain to an established app entry is unresolved. |
| 17 | `NanoHTTPD.decodePercent(String)` | OPEN | Called in URI/header parameter decoding (`NanoHTTPD.java:494-517,637-651`); requests depend on unresolved server/socket callback route. |
| 18 | `NanoHTTPD.getServerSocketFactory()` | OPEN | Called by `NanoHTTPD.start(int,boolean)` (`NanoHTTPD.java:1813-1816`); activation chain remains unresolved. |
| 19 | `NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long)` | OPEN | `TorrentStreamServer.handleTorrent` creates streamed responses and Nano HTTP error paths also call the overload; those response paths require server request handling not proved here. |
| 20 | `NanoHTTPD.newFixedLengthResponse(IStatus,String,String)` | OPEN | Called by `TorrentStreamServer.handleTorrent` and NanoHTTPD request error paths; entry depends on incoming request route. |
| 21 | `NanoHTTPD.safeClose(Object)` | OPEN | Called inside request/client/server cleanup and stop paths (`NanoHTTPD.java:163-165,188-192,747,751,753,1837-1842`); server entry route unresolved. |
| 22 | `NanoHTTPD.serve(String,Method,Map,Map,Map)` | UNREACHABLE `no_trigger_in_app` | Only found as called by base `serve(IHTTPSession)` (`NanoHTTPD.java:1732-1746`); the only uploaded subclass overrides `serve(IHTTPSession)` (`TorrentStreamServer.java:110-121`) and does not call `super.serve`; caller search found no app direct call. |
| 23 | `NanoHTTPD.serve(IHTTPSession)` | UNREACHABLE `no_trigger_in_app` | The sole subclass `TorrentStreamServer` overrides the method (`TorrentStreamServer.java:110-121`); NanoHTTPD's client handler uses virtual `serve(this)` (`NanoHTTPD.java:720`), dispatching to the override. No `super.serve` call found. |
| 24 | `NanoHTTPD.setAsyncRunner(AsyncRunner)` | OPEN | Called from NanoHTTPD constructor (`NanoHTTPD.java:1557-1562`); the constructor route remains OPEN. |
| 25 | `NanoHTTPD.setTempFileManagerFactory(TempFileManagerFactory)` | OPEN | Called from NanoHTTPD constructor (`NanoHTTPD.java:1557-1562`); the constructor route remains OPEN. |
| 26 | `NanoHTTPD.start()` | OPEN | `TorrentStreamServer.start` calls `super.start()` (`TorrentStreamServer.java:72-79`); caller in engine exists (`TorrentEngine.java:1069-1071`), but the full engine entry route was not verified. |
| 27 | `NanoHTTPD.start(int)` | OPEN | Called internally by `start()` (`NanoHTTPD.java:1794-1801`); outer start route remains OPEN. |
| 28 | `NanoHTTPD.start(int,boolean)` | OPEN | Called internally by `start(int)` and directly initializes server socket and runnable (`NanoHTTPD.java:1800-1821`); outer start route remains OPEN. |
| 29 | `NanoHTTPD.stop()` | OPEN | `TorrentStreamServer.stop` calls `super.stop()` (`TorrentStreamServer.java:81-87`); engine calls the wrapper (`TorrentEngine.java:1079-1082`), but its entry route was not traced. |
| 30 | `NanoHTTPD.useGzipWhenAccepted(Response)` | OPEN | Called by `HTTPSession.execute` (`NanoHTTPD.java:720-731`); request handling depends on unresolved server callback route. |
| 31 | `NanoHTTPD$ClientHandler.<init>` | OPEN | Created by `createClientHandler` (`NanoHTTPD.java:1579-1581`), itself called from server runnable after accept (`NanoHTTPD.java:1342-1347`); callback route unresolved. |
| 32 | `NanoHTTPD$ClientHandler.close()` | OPEN | Body closes its streams/socket (`NanoHTTPD.java:163-165`); no direct call identified in focused search, and indirect async-runner invocation not excluded. |
| 33 | `NanoHTTPD$ClientHandler.run()` | OPEN | Passed as Runnable to the async runner through `createClientHandler` (`NanoHTTPD.java:1342-1347`); framework/thread invocation requires source evidence not printed. |
| 34 | `NanoHTTPD$Cookie.<init>(String,String,String)` | OPEN | Public constructor body printed (`NanoHTTPD.java:213-217`); internal `CookieHandler.set` constructs this overload (`NanoHTTPD.java:283-285`), but no app cookie route was established. |
| 35 | `NanoHTTPD$Cookie.getHTTPHeader()` | OPEN | Called by `CookieHandler.unloadQueue` (`NanoHTTPD.java:294-297`), itself called during request handling (`NanoHTTPD.java:713-728`); request route unresolved. |
| 36 | `NanoHTTPD$Cookie.getHTTPTime(int)` | OPEN | Called by Cookie constructors and `CookieHandler.set` (`NanoHTTPD.java:197-203,205-211,283-285`); no established app cookie path. |
| 37 | `NanoHTTPD$CookieHandler.<init>` | OPEN | Constructed in `HTTPSession.execute` (`NanoHTTPD.java:713`); client request execution route unresolved. |
| 38 | `NanoHTTPD$CookieHandler.delete(String)` | UNREACHABLE `no_trigger_in_app` | Only its own body delegates to `set` (`NanoHTTPD.java:252-254`); no call from NanoHTTPD request handling or the only app subclass was found. |
| 39 | `NanoHTTPD$CookieHandler.iterator()` | UNREACHABLE `no_trigger_in_app` | Only declaration/body found (`NanoHTTPD.java:255-259`); no call from request handling or the only app subclass was found. |
| 40 | `NanoHTTPD$CookieHandler.read(String)` | UNREACHABLE `no_trigger_in_app` | Only declaration/body found (`NanoHTTPD.java:260-269`); no call from request handling or the only app subclass was found. |

The definite NanoHTTPD candidates flow from `TorrentEngine` into `TorrentStreamServer`, then into the superclass start/stop code. The full engine activation path was not independently audited. Thread `Runnable` callback dispatch and the socket request path remain OPEN. Base `serve` overloads are the narrow source-supported unreachable cases because the sole subclass overrides the dispatch target and contains no `super.serve` call.
