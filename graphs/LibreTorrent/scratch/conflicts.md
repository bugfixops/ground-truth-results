# Batch 2 incoming-edge conflicts

Decision for all eight warnings: (a), suppress the incoming edge because its caller has no route. The caller methods below are already labelled `UNREACHABLE`; their printed source lines contain only the intra-library call. The app source `org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:69-84,127-256` was printed and read: it calls the host/port superclass constructor, `start()`, `stop()`, and the status/string and status/input-stream/length response overloads.

| edge id | caller | printed caller line | edge suppressed |
|---|---|---|---|
| E49248ffb | NanoHTTPD.decodeParameters(Map) | NanoHTTPD.java:1604-1605 | decodeParameters(Map) → decodeParameters(String) |
| Ebcdd403c | NanoHTTPD.mimeTypes | NanoHTTPD.java:1418-1422 | mimeTypes → loadMimeTypes |
| Ec0690361 | NanoHTTPD.makeSSLSocketFactory(String,char[]) | NanoHTTPD.java:1484-1491 | String overload → KeyManagerFactory overload |
| E7b0e9320 | NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory) | NanoHTTPD.java:1473-1475 | KeyManagerFactory overload → KeyManager[] overload |
| E3efb530c | NanoHTTPD.getMimeTypeForFile | NanoHTTPD.java:1503-1507 | getMimeTypeForFile → mimeTypes |
| Ef4f17911 | NanoHTTPD.isAlive | NanoHTTPD.java:1666-1667 | isAlive → wasStarted |
| Ed884f696 | NanoHTTPD$Cookie.<init>(String,String) | NanoHTTPD.java:205-206 | two-argument Cookie constructor → three-argument constructor |
| E013fb9d4 | NanoHTTPD.makeSecure | NanoHTTPD.java:1684-1685 | makeSecure → SecureServerSocketFactory constructor |

The printed source confirms these are calls, and the resulting graph reachability confirms none of the eight callers has a route. The corresponding auto-generated edges are excluded by exact caller/callee pairs in `graph_def.py` `SUPPRESS`; this does not alter any app call site.
