# LibreTorrent batch 34 source audit

Membership is exactly the 40 batch 34 rows printed in `batch_034_helper_printed.txt` from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The table below has one row per plan method. Source and candidate call sites were printed in that evidence file, but a local call is not a complete method route: a route must begin at a registered app entry and preserve any callback/library dispatch. Since this batch audit did not establish complete hand-written entry paths for these methods, each remains **OPEN**; no UNREACHABLE label is inferred from a missing grep result.

| # | Method | Finding | Basis / printed evidence |
|---:|---|---|---|
| 1 | `FileTree.setType(I)V` | OPEN | `FileTree.java` body printed; no complete entry route verified. |
| 2 | `FileTree.size()J` | OPEN | `FileTree.java` body and tree recursion printed; complete entry route not verified. |
| 3 | `FileTree.toString()Ljava/lang/String;` | OPEN | `FileTree.java` body printed; only candidate use through another target's `toString`; entry route not verified. |
| 4 | `TorrentContentFileTree.<init>(int,String,long,int,TorrentContentFileTree)` | OPEN | Constructor and candidate construction sites printed; complete entry route not verified. |
| 5 | `TorrentContentFileTree.<init>(String,long,int)` | OPEN | Constructor and candidate construction sites printed; complete entry route not verified. |
| 6 | `TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree)` | OPEN | Constructor and candidate construction sites printed; complete entry route not verified. |
| 7 | `TorrentContentFileTree.changePriority(FilePriority,ZZ)` | OPEN | Method and local callers printed; complete UI-to-entry route not verified. |
| 8 | `TorrentContentFileTree.getAvailability()D` | OPEN | Method and candidate UI caller printed; complete entry route not verified. |
| 9 | `TorrentContentFileTree.getFilePriority()FilePriority` | OPEN | Method and candidate UI callers printed; complete entry route not verified. |
| 10 | `TorrentContentFileTree.getReceivedBytes()J` | OPEN | Method and candidate UI callers printed; complete entry route not verified. |
| 11 | `TorrentContentFileTree.nonIgnoreFileSize()J` | OPEN | Method and candidate UI callers printed; complete entry route not verified. |
| 12 | `TorrentContentFileTree.onChangePriority(FilePriority,Z)` | OPEN | Method and local invocation printed; complete route not verified. |
| 13 | `TorrentContentFileTree.setAvailability(D)V` | OPEN | Setter body printed; no complete entry route verified. |
| 14 | `TorrentContentFileTree.setPriority(FilePriority,Z)` | OPEN | Setter and local callers printed; complete UI-to-entry route not verified. |
| 15 | `TorrentContentFileTree.setReceivedBytes(J)V` | OPEN | Setter body printed; no complete entry route verified. |
| 16 | `TorrentContentFileTree.toString()Ljava/lang/String;` | OPEN | Method body printed; no complete entry route verified. |
| 17 | `AdvancedPeerInfo.<init>(swig peer_info)` | OPEN | Constructor and `TorrentDownloadImpl` construction site printed; upstream native/library callback route not verified. |
| 18 | `AdvancedPeerInfo.isUtp()Z` | OPEN | Getter body printed; no app caller found in saved search; absence alone does not prove no route. |
| 19 | `AdvancedPeerInfo.pieces()PieceIndexBitfield` | OPEN | Getter body printed; no app caller found in saved search; absence alone does not prove no route. |
| 20 | `AdvancedPeerInfo.port()I` | OPEN | Getter body printed; no app caller found in saved search; absence alone does not prove no route. |
| 21 | `IPFilterImpl.<init>()V` | OPEN | Constructor and session construction/bridge evidence printed; complete startup route not verified. |
| 22 | `IPFilterImpl.addRange(String,String)V` | OPEN | Method body printed; parser/bridge dispatch route not verified. |
| 23 | `IPFilterImpl.getFilter()ip_filter` | OPEN | Method body printed; parser/bridge dispatch route not verified. |
| 24 | `IPFilterParser.<clinit>()V` | OPEN | Static initializer printed; parser invocation depends on an unverified session/configuration path. |
| 25 | `IPFilterParser.<init>()V` | OPEN | Constructor and `TorrentSessionImpl` call site printed; complete session route not verified. |
| 26 | `IPFilterParser.errLog(int,String,String)V` | OPEN | Method body printed; parser error path depends on an unverified parser invocation. |
| 27 | `IPFilterParser.parseDAT(InputStream,IPFilter)I` | OPEN | Parser body printed; no complete source-to-input entry route verified. |
| 28 | `IPFilterParser.parseFile(Uri,FileSystemFacade,IPFilter)I` | OPEN | Parser body and session call site printed; complete startup/configuration route not verified. |
| 29 | `IPFilterParser.parseIpAddress(String)String` | OPEN | Parser helper body printed; complete parser entry route not verified. |
| 30 | `IPFilterParser.parseP2P(InputStream,IPFilter)I` | OPEN | Parser body printed; no complete source-to-input entry route verified. |
| 31 | `PriorityConverter.<clinit>()V` | OPEN | Static initializer and converter call sites printed; full caller-to-entry routes not verified. |
| 32 | `PriorityConverter.convert(Priority)#2` | OPEN | Overload body and app call sites printed; complete caller-to-entry routes not verified. |
| 33 | `PriorityConverter.convert(Priority[])` | OPEN | Overload body and call sites printed; complete caller-to-entry routes not verified. |
| 34 | `PriorityConverter.convert(Priority[])#2` | OPEN | Overload body and call sites printed; complete caller-to-entry routes not verified. |
| 35 | `SessionErrors.<clinit>()V` | OPEN | Static initializer and error-helper call sites printed; event/error delivery path not verified. |
| 36 | `SessionErrors.getErrorMsg(ErrorCode)String` | OPEN | Method body and `TorrentDownloadImpl` caller printed; callback/event entry path not verified. |
| 37 | `SessionErrors.isNonCritical(ErrorCode)Z` | OPEN | Method body and `TorrentDownloadImpl` caller printed; callback/event entry path not verified. |
| 38 | `SessionErrors$Error.<init>(int,String)V` | OPEN | Constructor and related source printed; complete construction route not verified. |
| 39 | `SessionLogger.<clinit>()V` | OPEN | Static initializer printed; complete session construction route not verified. |
| 40 | `SessionLogger.<init>()V` | OPEN | Constructor and `TorrentSessionImpl` construction site printed; complete session entry route not verified. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or build/coverage evidence were used.
