# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** Not passed build, sampler, full-repo grep, or C1 checks. Re-check from printed source before merging.

---

# LibreTorrent batch 15 — proposed part only, NOT merged, NOT verified by build/C1

Repo: bugfixops/ground-truth-results, branch work-2026-10-31, connector only, no token, no clone.
Membership: handoff/LIBRETORRENT_BATCH_PLAN.tsv, batch == 15, exactly 40 rows, all TODO_CANDIDATE_REACHABLE / "REACHABLE (generator candidate, no hand route yet)" — candidates only, not evidence.
Source root: final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
Rules: no tool coverage, old generated graphs, or build REACHABLE counts as evidence. confirmed_by only SOURCE (lines printed) or INFERRED, never DYN/FW-MEMORY/UNVERIFIED.
No build, sampler, grep, or C1 check was run in this session (connector-only). No such count is claimed. Nothing was pushed in this file's creation; nothing on any branch was edited; graph_def.py and out/ were not touched.

## Shared routes

Feed/mediarss trunk (printed, same as batches 13/14, with INFERRED dispatch steps):
Scheduler.runPeriodicalRefreshFeeds (service/Scheduler.java:112-125) → [WorkManager dispatch to FeedFetcherWorker.doWork — INFERRED] → FeedFetcherWorker.doWork:74 → fetchChannel → new core FeedParser (FeedFetcherWorker.java:156) → parser.getItems() (:165) → core FeedParser.<init> (:62-71) → FeedParserFactory.newParser → DefaultFeedParser.parse (:22-47) → [SAX dispatch to FeedHandler callbacks — INFERRED] → FeedHandler.startElement (:54-103) → core getItems (:89-115) → watchMediaContent (:190) → watchMediaHash (:215-221) → MediaRss.getHash / Hash.getValue, and watchMediaContent → MediaRss.getContent (:194).

Streaming trunk (printed, gated):
TorrentEngine.handleOnSessionStarted (core/model/TorrentEngine.java:1056-1059, STATE settings gate pref.enableStreaming()) → startStreamingServer (:1063-1075) → new TorrentStreamServer(hostname, port) (:1069) → TorrentStreamServer constructor super(host, port) (core/model/stream/TorrentStreamServer.java:67-69) → NanoHTTPD.<init>(String,int) → setTempFileManagerFactory / setAsyncRunner → TorrentStreamServer.start(appContext) (:72-78) → super.start() = NanoHTTPD.start() → start(timeout) → start(timeout, daemon) → getServerSocketFactory().create() + createServerRunnable(timeout) → ServerRunnable.run → asyncRunner.exec(createClientHandler) → ClientHandler.run → HTTPSession.execute → serve(this) (virtual dispatch to TorrentStreamServer.serve, TorrentStreamServer.java:111, NOT to NanoHTTPD base serve).

## Judged: 40/40 — REACHABLE 26, UNREACHABLE 8, OPEN 6

| # | Method | Descriptor | Label | Kind / confirmed_by | Printed citations |
|---|---|---|---|---|---|
| 1 | Hash.getValue | ()Ljava/lang/String; | REACHABLE | — / SOURCE | Def mediarss/Hash.java:32-34; call core/FeedParser.java:221 in watchMediaHash, via MediaRss.getHash :217, via watchMediaContent :190 |
| 2 | Hash.hashCode | ()I | UNREACHABLE | no_trigger_in_app / INFERRED | Def Hash.java:67-71; no printed caller, no hash collection holding a Hash in printed files. Pending real full-repo grep; flips if found. |
| 3 | Hash.setAlgorithm | (Ljava/lang/String;)V | REACHABLE | — / SOURCE | Def Hash.java:48-52; call impl/MediaRssParser.java:71 in parseHash, via parse :34, via Rss2Item.java:115, via core :190 |
| 4 | Hash.toString | ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app / INFERRED | Def Hash.java:75-80; no printed caller. MediaRss.toString concatenates hash (:47), but MediaRss.toString itself has no printed caller, so that is not a route. Pending full grep. |
| 5 | MediaRss.<init> | (Ljava/util/List;Lcom/ernieyu/feedparser/mediarss/Hash;Ljava/util/List;)V | REACHABLE | — / SOURCE | Def mediarss/MediaRss.java:21-28; call MediaRssParser.java:37, via parse :29-37 |
| 6 | MediaRss.getContent | ()Ljava/util/List; | REACHABLE | — / SOURCE | Def MediaRss.java:30-32; call core/FeedParser.java:194 in watchMediaContent |
| 7 | MediaRss.getHash | ()Lcom/ernieyu/feedparser/mediarss/Hash; | REACHABLE | — / SOURCE | Def MediaRss.java:34-36; call core/FeedParser.java:217 in watchMediaHash |
| 8 | MediaRss.toString | ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app / INFERRED | Def MediaRss.java:44-49; no printed caller. Pending full grep. |
| 9 | PeerLink.<init> | (Ljava/lang/String;Ljava/lang/String;)V | REACHABLE | — / SOURCE | Def mediarss/PeerLink.java:15-18; call MediaRssParser.java:88, via parsePeerLinks :76-88, via parse :35 |
| 10 | PeerLink.equals | (Ljava/lang/Object;)Z | UNREACHABLE | no_trigger_in_app / INFERRED | Def PeerLink.java:43-52; no printed caller. Pending full grep. |
| 11 | PeerLink.hashCode | ()I | UNREACHABLE | no_trigger_in_app / INFERRED | Def PeerLink.java:55-59; no printed caller, no hash collection. Pending full grep. |
| 12 | PeerLink.toString | ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app / INFERRED | Def PeerLink.java:63-68; no printed caller. MediaRss.toString does not include peerLinks (MediaRss.java:45-48). Pending full grep. |
| 13 | NanoHTTPD.<clinit> | ()V | REACHABLE | — / INFERRED | Implicit static init (LOG, constants, NanoHTTPD.java:1392-1417); class loads when TorrentStreamServer is created, TorrentEngine.java:1069. JVM loading step INFERRED, not a printed framework line. |
| 14 | NanoHTTPD.<init>(String,int) | (Ljava/lang/String;I)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1557-1562; call TorrentStreamServer.java:69 super(host, port), via TorrentEngine.java:1069, gated enableStreaming TorrentEngine.java:1056-1059 |
| 15 | NanoHTTPD.createClientHandler | (Ljava/net/Socket;Ljava/io/InputStream;)Lorg/nanohttpd/NanoHTTPD$ClientHandler; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1579-1580; call ServerRunnable :1347 asyncRunner.exec(createClientHandler(...)), via start chain |
| 16 | NanoHTTPD.createServerRunnable | (I)Lorg/nanohttpd/NanoHTTPD$ServerRunnable; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1590-; call start(timeout, daemon) :1816, via start chain |
| 17 | NanoHTTPD.decodePercent | (Ljava/lang/String;)Ljava/lang/String; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1646-; calls HTTPSession :514,516,648,650,1626,1630, via ClientHandler.run → session.execute |
| 18 | NanoHTTPD.getServerSocketFactory | ()Lorg/nanohttpd/NanoHTTPD$ServerSocketFactory; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1669-; call start(timeout, daemon) :1814, via start chain |
| 19 | NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long) | (Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/io/InputStream;J)Lorg/nanohttpd/NanoHTTPD$Response; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1696-1699; calls TorrentStreamServer.java:209,244 |
| 20 | NanoHTTPD.newFixedLengthResponse(IStatus,String,String) | (Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$Response; | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1702-1715; calls TorrentStreamServer.java:127,130,134,144,147,196,222,231,239,256 |
| 21 | NanoHTTPD.safeClose | (Ljava/lang/Object;)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1511-; calls e.g. stop :1839, ClientHandler.run finally, HTTPSession finally, via start/stop chain |
| 22 | NanoHTTPD.serve(String,Method,Map,Map,Map) | (Ljava/lang/String;Lorg/nanohttpd/NanoHTTPD$Method;Ljava/util/Map;Ljava/util/Map;Ljava/util/Map;)Lorg/nanohttpd/NanoHTTPD$Response; | UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1767-1768; only printed caller is base serve(IHTTPSession) :1746, which is overridden by TorrentStreamServer.java:111 and never called for that subclass; no super.serve call printed. Pending full grep for any other subclass. |
| 23 | NanoHTTPD.serve(IHTTPSession) | (Lorg/nanohttpd/NanoHTTPD$IHTTPSession;)Lorg/nanohttpd/NanoHTTPD$Response; | UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1732-; ClientHandler calls serve(this) virtually (HTTPSession :720), which dispatches to TorrentStreamServer.serve, not the base body. Pending full grep for any other subclass. |
| 24 | NanoHTTPD.setAsyncRunner | (Lorg/nanohttpd/NanoHTTPD$AsyncRunner;)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1776-; call NanoHTTPD constructor :1561, via TorrentStreamServer super |
| 25 | NanoHTTPD.setTempFileManagerFactory | (Lorg/nanohttpd/NanoHTTPD$TempFileManagerFactory;)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1785-; call NanoHTTPD constructor :1560, via TorrentStreamServer super |
| 26 | NanoHTTPD.start() | ()V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1794-1795; call TorrentStreamServer.start :78 super.start(), via TorrentEngine.java:1071, gated enableStreaming |
| 27 | NanoHTTPD.start(int) | (I)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1800-1801; call start() :1795 start(SOCKET_READ_TIMEOUT) |
| 28 | NanoHTTPD.start(int,boolean) | (IZ)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1813-1820; call start(int) :1801, chain above; creates socket :1814, server runnable :1816, thread start :1820 |
| 29 | NanoHTTPD.stop | ()V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1839-; call TorrentStreamServer.stop :84 super.stop(), via TorrentEngine.java:1081 stopStreamingServer, via startStreamingServer :1064 |
| 30 | NanoHTTPD.useGzipWhenAccepted | (Lorg/nanohttpd/NanoHTTPD$Response;)Z | REACHABLE | — / SOURCE | Def NanoHTTPD.java:1660-; call HTTPSession.execute :729, via ClientHandler.run |
| 31 | NanoHTTPD$ClientHandler.<init> | (Lorg/nanohttpd/NanoHTTPD;Ljava/io/InputStream;Ljava/net/Socket;)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:159-162, private; call createClientHandler :1580, via ServerRunnable :1347 |
| 32 | NanoHTTPD$ClientHandler.close | ()V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:163-166; call DefaultAsyncRunner.closeAll :322, via stop() asyncRunner.closeAll() |
| 33 | NanoHTTPD$ClientHandler.run | ()V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:168-; Thread.start in DefaultAsyncRunner.exec :336, via ServerRunnable |
| 34 | NanoHTTPD$Cookie.<init>(String,String,String) | (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V | OPEN | — / none | Def NanoHTTPD.java:213-216; only printed caller is CookieHandler.set(String,String,int) :284, which is only called by delete() :252, which has no printed caller. Full grep needed; do not call UNREACHABLE. |
| 35 | NanoHTTPD$Cookie.getHTTPHeader | ()Ljava/lang/String; | OPEN | — / none | Def NanoHTTPD.java:218-221; call unloadQueue :296, via HTTPSession.execute :727, but queue is empty in printed code (only populated by set/delete, neither printed as called). |
| 36 | NanoHTTPD$Cookie.getHTTPTime | (I)Ljava/lang/String; | OPEN | — / none | Def NanoHTTPD.java:197-; calls Cookie int constructor :211 and set() :284, both conditional on the Cookie/delete chain above. No direct printed route to a Cookie creation in app code. |
| 37 | NanoHTTPD$CookieHandler.<init> | (Lorg/nanohttpd/NanoHTTPD;Ljava/util/Map;)V | REACHABLE | — / SOURCE | Def NanoHTTPD.java:233-; call HTTPSession.execute :713 new CookieHandler(this.headers), via ClientHandler.run |
| 38 | NanoHTTPD$CookieHandler.delete | (Ljava/lang/String;)V | OPEN | — / none | Def NanoHTTPD.java:252-254; no printed caller. |
| 39 | NanoHTTPD$CookieHandler.iterator | ()Ljava/util/Iterator; | OPEN | — / none | Def NanoHTTPD.java:257-259; no printed caller; HTTPSession does not iterate it. |
| 40 | NanoHTTPD$CookieHandler.read | (Ljava/lang/String;)Ljava/lang/String; | OPEN | — / none | Def NanoHTTPD.java:267-269; no printed caller; TorrentStreamServer.serve does not call it. |

## Counts
- Judged: 40/40 (all rows given a label or OPEN, with reasons above)
- REACHABLE: 26
- UNREACHABLE: 8 (all no_trigger_in_app, all pending real full-repo grep)
- OPEN: 6 (all Cookie/CookieHandler rows above, pending full grep / printed attach or caller)

## Blockers before merge
1. Real full-repo grep over the source root for: Hash/MediaRss/PeerLink equals/hashCode/toString triggers; any other NanoHTTPD subclass (for serve rows); any CookieHandler.delete/read/iterator or Cookie creation caller in app code.
2. Build / C1 checks on a full local checkout — not run here, no count claimed.
3. TorrentEngine entry: handleOnSessionStarted is itself a session listener callback; its caller was not printed in this session, but TorrentEngine.getInstance is printed from SchedulerReceiver and TorrentService in batch 18 work, so the streaming route is anchored at TorrentEngine, not at a launcher entry in this file. Record that gap; do not claim a launcher route.
4. Streaming gate: STATE settings pref.enableStreaming() (TorrentEngine.java:1056-1059) — recorded, does not change the REACHABLE verdict for the server methods when enabled.
