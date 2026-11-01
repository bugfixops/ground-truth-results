**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 15 — merge-ready file (UNVERIFIED proposal)

Scope: Mediarss remainder (Hash/MediaRss/PeerLink) + NanoHTTPD core, ClientHandler, Cookie/CookieHandler.

## Conventions used in this file (recorded, not decided)

- Status: UNVERIFIED proposal only. NOT verified for merge. No row in this file has passed spot-check, py_compile, build, or C1.
- confirmed_by is only SOURCE or INFERRED, never DYN / FW-MEMORY / UNVERIFIED.
- Batch 14 rule: every REACHABLE row is INFERRED because the route crosses two unprinted framework dispatches (WorkManager
  enqueue -> doWork, and SAX parser.parse -> FeedHandler.startElement). Batch 15/16 rule: SOURCE means a printed line names the
  method as a direct callee on a printed chain from the TorrentStreamServer anchor (ctor/start/stop/setter chains); INFERRED means
  the only printed path crosses Thread.start, a virtual/framework dispatch, or JVM class-load. The merger must reconcile the
  batch-14 whole-route rule with the batch-15/16 printed-callee rule project-wide; the two rules are NOT silently mixed here.
- Strict-entry caveat (undecided, applies to every REACHABLE row in this file): routes are anchored at FeedSettingsFragment
  preference change (batch 14) and TorrentEngine streaming start (batches 15/16). No launcher -> settings-page and no
  launcher -> TorrentService/TorrentEngine step was printed in this pass. Under a strict printed-launcher-entry rule, all
  REACHABLE rows in this file revert to OPEN. Recorded, not decided.
- UNREACHABLE proposed rows are all INFERRED and grep-owed: a saved full-repo grep (rule-F/C5 form) for the method name must be
  run before merge. A saved grep hit for a live caller flips that row to REACHABLE; a grep hit for a trigger of
  BaseItem.equals/hashCode flips batch 14 rows 11/24 to REACHABLE. No connector search_code 0-result was used as absence evidence
  anywhere in this file, and no row was flipped from OPEN to UNREACHABLE on absence alone without a named grep target.
- Plan labels were NOT adopted: every batch 14-16 plan row is TODO_CANDIDATE_REACHABLE with the generator label
  "REACHABLE (generator candidate, no hand route yet)". Verdicts below were re-derived from printed source, not copied from the
  plan, from prior proposals, or from corrected files (those were leads only; where this file agrees with a corrected file, the
  agreement is a check result, not a copy).
- Build: NOT RUN (runs on the user's Mac after a push). C1: NOT RUN. Never claimed passed.
- Push: 5e0983f (UNVERIFIED, before [L]). Pushes are held until LibreTorrent labels are verified and merged to [L].

## Sources printed fresh in this session (branch work-2026-10-31, GitHub connector, one file at a time)

Root for app sources: final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
- com/ernieyu/feedparser/impl/MediaRssParser.java (98 lines), Rss1Feed.java (123), Rss1Item.java (124), Rss2Feed.java (137),
  Rss2Item.java (122), BaseItem.java (70), FeedHandler.java (132), DefaultFeedParser.java (48)
- com/ernieyu/feedparser/mediarss/Content.java (90), Hash.java (81), MediaRss.java (50), PeerLink.java (69)
- org/proninyaroslav/libretorrent/core/FeedParser.java (267 lines, core parser)
- org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java (270), Scheduler.java (145)
- org/proninyaroslav/libretorrent/ui/settings/sections/FeedSettingsFragment.java (163)
- org/nanohttpd/NanoHTTPD.java (1850 lines)
- org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java (284)
- org/proninyaroslav/libretorrent/core/model/TorrentEngine.java (1658; streaming sections :1050-1085 read in full)
All 19 files fetched via the GitHub connector in this session; the feedparser, NanoHTTPD, TorrentStreamServer and TorrentEngine
files are byte-identical to prior local copies where one existed. No fresh HTTP 429 occurred in this pass.
Plan: handoff/LIBRETORRENT_BATCH_PLAN.tsv, local copy ~/workspace/agent27-plan.tsv, 4732 rows + header.
NOTE on plan hash: the local copy hashes to sha256 f4860569052b365233459da8d527a568fdb54d3f1fa5073e36ac03c4ebe9fd3e
(sha1 afedc8af26fd3564ea03b7197f2a99cf2b7ce8bb), which does NOT match the 0104806d... prefix recorded in handoff memory.
Membership below was verified row-for-row against the local copy (40 rows per batch, plan order, names + descriptors exact);
the main agent should confirm the local copy matches the branch plan before merge. This discrepancy is flagged, not hidden.

## Shared trunks (freshly printed this session)

Mediarss trunk: see batch 14 trunk (same FeedSettingsFragment -> Scheduler -> FeedFetcherWorker -> core FeedParser -> SAX chain).
MediaRssParser.parse :29-38 calls parseContent :33, parseHash :34, parsePeerLinks :35 and constructs MediaRss :37.
Streaming trunk: TorrentEngine streaming start is gated on STATE settings pref.enableStreaming() (:1056-1059);
startStreamingServer :1063-1071 constructs TorrentStreamServer (:1069) and calls torrentStreamServer.start(appContext) (:1071);
stopStreamingServer :1079-1081 calls torrentStreamServer.stop() (:1081). TorrentStreamServer ctor :67-69 calls super(host, port);
start(Context) :72-78 calls TorrentEngine.getInstance (:75) then super.start() (:77); stop() :81-84 calls super.stop() (:82).
NanoHTTPD.start() :1794-1795 -> start(int) :1800-1801 -> start(int,boolean) :1813-1820 (serverSocketFactory.create() :1814,
createServerRunnable :1816, new Thread(serverRunnable) :1817, myThread.start() :1820). ServerRunnable.run :1332-1347 accepts a
socket and calls asyncRunner.exec(createClientHandler(finalAccept, inputStream)) (:1347). DefaultAsyncRunner.exec :330-336 creates
a Thread for the ClientHandler (:332) and starts it (:336). ClientHandler.run :168-195 creates the TempFileManager (:172) and
HTTPSession (:173) and loops session.execute() (:175). HTTPSession.execute :655-760 calls decodeHeader :703, Method.lookup :708,
new CookieHandler :713, virtual serve(this) :720 (dispatches to TorrentStreamServer.serve :111, NOT to base serve :1732),
cookies.unloadQueue(r) :727, useGzipWhenAccepted(r) :729, r.send :731, and finally safeClose(r) :753 + tempFileManager.clear() :754.
TorrentStreamServer.serve(IHTTPSession) :111-122 calls session.getUri() :112 and handleTorrent(session) :116; handleTorrent
:124-258 calls httpSession.getUri() :129, httpSession.getParms() :132, httpSession.getHeaders() :150 and newFixedLengthResponse
at :127/:130/:134/:144/:147/:196/:209/:222/:231/:239/:244/:256. The full TorrentStreamServer.java (284 lines) contains ZERO
newChunkedResponse calls, ZERO parseBody calls, ZERO getMethod calls and ZERO getQueryParameterString calls — do not cite any.
Serve path additionally requires an incoming HTTP request from a client; no gate value is assigned for that here (candidate
ENV other_app) — merger decides, it is recorded not decided.

## Table (plan order)

| # | Method | JVM descriptor | Proposed label | confirmed_by | Route / reason |
|---:|--------|---------------|----------------|--------------|----------------|
| 1 | Hash.getValue | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def Hash :32-34; caller core watchMediaHash :221 (hash.getValue) <- watchMediaContent :201/:207 <- core getItems. INFERRED: whole route crosses WorkManager+SAX dispatch (see batch 14 trunk). |
| 2 | Hash.hashCode | `()I` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :67-71. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 3 | Hash.setAlgorithm | `(Ljava/lang/String;)V` | REACHABLE proposed | INFERRED | Def :48-52; caller MediaRssParser.parseHash :71 (mediaHash.setAlgorithm, only when algo attr present) <- parse :34. INFERRED as row 1. |
| 4 | Hash.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :75-80. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 5 | MediaRss.<init> | `(Ljava/util/List;Lcom/ernieyu/feedparser/mediarss/Hash;Ljava/util/List;)V` | REACHABLE proposed | INFERRED | Def MediaRss :21-28; constructed MediaRssParser.parse :37. INFERRED as row 1. |
| 6 | MediaRss.getContent | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :30-32; caller core watchMediaContent :194 (media.getContent). INFERRED as row 1. |
| 7 | MediaRss.getHash | `()Lcom/ernieyu/feedparser/mediarss/Hash;` | REACHABLE proposed | INFERRED | Def :34-36; caller core watchMediaHash :217 (media.getHash). INFERRED as row 1. |
| 8 | MediaRss.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :44-49 (content concat :46, hash :47). No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 9 | PeerLink.<init> | `(Ljava/lang/String;Ljava/lang/String;)V` | REACHABLE proposed | INFERRED | Def PeerLink :15-18; constructed MediaRssParser.parsePeerLinks :88. INFERRED as row 1. |
| 10 | PeerLink.equals | `(Ljava/lang/Object;)Z` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :43-52. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 11 | PeerLink.hashCode | `()I` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :55-59. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 12 | PeerLink.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :63-68. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 13 | NanoHTTPD.<clinit> | `()V` | REACHABLE proposed | INFERRED | No explicit static{} block in NanoHTTPD.java; <clinit> is the implicit static-field initialisation (SOCKET_READ_TIMEOUT :1396, MIME_* :1400/:1404, QUERY_STRING_PARAMETER :1409, LOG :1413, MIME_TYPES :1417). Runs on first class load via the TorrentStreamServer construction route (TorrentEngine :1069). INFERRED: JVM class-load dispatch, not a printed call. |
| 14 | NanoHTTPD.<init>(String,int) | `(Ljava/lang/String;I)V` | REACHABLE proposed | SOURCE | Def NanoHTTPD :1557-1562; caller TorrentStreamServer ctor :67-69 super(host, port). Printed direct call from the streaming anchor. |
| 15 | NanoHTTPD.createClientHandler | `(Ljava/net/Socket;Ljava/io/InputStream;)Lorg/nanohttpd/NanoHTTPD$ClientHandler;` | REACHABLE proposed | INFERRED | Def :1579-1580 (new ClientHandler :1580); caller ServerRunnable.run :1347, which runs only on the listener thread started at NanoHTTPD.start :1820. INFERRED: only printed path crosses Thread.start. |
| 16 | NanoHTTPD.createServerRunnable | `(I)Lorg/nanohttpd/NanoHTTPD$ServerRunnable;` | REACHABLE proposed | SOURCE | Def :1590-1592; caller NanoHTTPD.start(int,boolean) :1816 (createServerRunnable). Printed direct call. |
| 17 | NanoHTTPD.decodePercent | `(Ljava/lang/String;)Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :1646+; callers decodeHeader :514/:516 and decodeParms :648/:650, both under HTTPSession.execute, which runs only on a ClientHandler thread (t.start :336). INFERRED: only printed path crosses Thread.start. |
| 18 | NanoHTTPD.getServerSocketFactory | `()Lorg/nanohttpd/NanoHTTPD$ServerSocketFactory;` | REACHABLE proposed | SOURCE | Def :1669-1671; caller NanoHTTPD.start(int,boolean) :1814 (getServerSocketFactory().create()). Printed direct call. |
| 19 | NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long) | `(Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/io/InputStream;J)Lorg/nanohttpd/NanoHTTPD$Response;` | REACHABLE proposed | INFERRED | Def :1696-1698 (new Response :1697); live callers TorrentStreamServer.handleTorrent :209/:244 (InputStream overload) and base-serve/execute paths. INFERRED: TSS serve runs on a ClientHandler thread; base-serve call sites are dead (see row 23). |
| 20 | NanoHTTPD.newFixedLengthResponse(IStatus,String,String) | `(Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$Response;` | REACHABLE proposed | INFERRED | Def :1702-1715; live callers TorrentStreamServer.handleTorrent (e.g. :127/:130/:134/:196/:231/:239/:256) and HTTPSession.execute catch :745/:749. INFERRED as row 19. |
| 21 | NanoHTTPD.safeClose | `(Ljava/lang/Object;)V` | REACHABLE proposed | SOURCE | Def :1511-1519; printed callers include the synchronous stop path NanoHTTPD.stop :1839 (safeClose myServerSocket) <- TorrentStreamServer.stop :82, plus ClientHandler.close :164-165 and execute finally :753. SOURCE: a synchronous printed caller exists. |
| 22 | NanoHTTPD.serve(String,Method,Map,Map,Map) | `(Ljava/lang/String;Lorg/nanohttpd/NanoHTTPD$Method;Ljava/util/Map;Ljava/util/Map;Ljava/util/Map;)Lorg/nanohttpd/NanoHTTPD$Response;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :1767-1768 (NOT_FOUND stub). Only printed caller is base serve(IHTTPSession) :1746, which TorrentStreamServer overrides (:111) and never calls via super. No printed caller of the 5-arg overload itself. Proposed only; saved full-repo grep for serve( call sites owed before merge. |
| 23 | NanoHTTPD.serve(IHTTPSession) | `(Lorg/nanohttpd/NanoHTTPD$IHTTPSession;)Lorg/nanohttpd/NanoHTTPD$Response;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def base serve(IHTTPSession) :1732-1746. The live dispatch is virtual serve(this) at HTTPSession.execute :720, which resolves to TorrentStreamServer.serve :111; TSS contains no super.serve call, so the base body never runs in the app path. Proposed only; grep owed (a plain-NanoHTTPD construction would revive it; none is printed). |
| 24 | NanoHTTPD.setAsyncRunner | `(Lorg/nanohttpd/NanoHTTPD$AsyncRunner;)V` | REACHABLE proposed | SOURCE | Def :1776-1778; caller NanoHTTPD ctor :1561 (setAsyncRunner(new DefaultAsyncRunner())). Printed direct call. |
| 25 | NanoHTTPD.setTempFileManagerFactory | `(Lorg/nanohttpd/NanoHTTPD$TempFileManagerFactory;)V` | REACHABLE proposed | SOURCE | Def :1785+; caller NanoHTTPD ctor :1560 (setTempFileManagerFactory(new DefaultTempFileManagerFactory())). Printed direct call. |
| 26 | NanoHTTPD.start() | `()V` | REACHABLE proposed | SOURCE | Def :1794-1795 (start(SOCKET_READ_TIMEOUT)); caller TorrentStreamServer.start :77 super.start(). Printed direct call. |
| 27 | NanoHTTPD.start(int) | `(I)V` | REACHABLE proposed | SOURCE | Def :1800-1801 (start(timeout, true)); caller start() :1795. Printed direct call. |
| 28 | NanoHTTPD.start(int,boolean) | `(IZ)V` | REACHABLE proposed | SOURCE | Def :1813-1820 (getServerSocketFactory().create() :1814, createServerRunnable :1816, new Thread :1817, myThread.start() :1820); caller start(int) :1801. Printed direct call. |
| 29 | NanoHTTPD.stop | `()V` | REACHABLE proposed | SOURCE | Def :1837-1845 (safeClose :1839, asyncRunner.closeAll() :1840, myThread.join() :1842); caller TorrentStreamServer.stop :82 super.stop(). Printed direct call. |
| 30 | NanoHTTPD.useGzipWhenAccepted | `(Lorg/nanohttpd/NanoHTTPD$Response;)Z` | REACHABLE proposed | INFERRED | Def :1660-1661; caller HTTPSession.execute :729 (r.setGzipEncoding(useGzipWhenAccepted(r) ...)). INFERRED: execute runs only on a ClientHandler thread. |
| 31 | NanoHTTPD$ClientHandler.<init> | `(Lorg/nanohttpd/NanoHTTPD;Ljava/io/InputStream;Ljava/net/Socket;)V` | REACHABLE proposed | INFERRED | Def ClientHandler :159-162; caller createClientHandler :1580, itself reached only via ServerRunnable.run :1347 on the listener thread. INFERRED as row 15. |
| 32 | NanoHTTPD$ClientHandler.close | `()V` | REACHABLE proposed | SOURCE | Def :163-166 (safeClose :164-165); caller DefaultAsyncRunner.closeAll :322 <- NanoHTTPD.stop :1840 <- TorrentStreamServer.stop :82. SOURCE: a synchronous printed caller chain exists. |
| 33 | NanoHTTPD$ClientHandler.run | `()V` | REACHABLE proposed | INFERRED | Def :168-195 (factory.create :172, new HTTPSession :173, session.execute :175, finally asyncRunner.closed :192); dispatched by DefaultAsyncRunner.exec :332-336 (new Thread :332, t.start() :336). INFERRED: Thread dispatch unprinted. |
| 34 | NanoHTTPD$Cookie.<init>(String,String,String) | `(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def Cookie :213-217. Only printed constructor is CookieHandler.set(String,String,int) :284, and set itself has no printed caller (only delete :253 calls it; delete is row 38, uncalled). Proposed only; saved full-repo grep owed before merge. |
| 35 | NanoHTTPD$Cookie.getHTTPHeader | `()Ljava/lang/String;` | UNREACHABLE proposed branch_never_taken | INFERRED | Def :218-221. The loop that calls it, CookieHandler.unloadQueue :294-297 (response.addHeader :296), DOES run (HTTPSession.execute :727), but its queue is populated only by set (rows batch16-1/2), which has no printed caller in the app path, so the loop body never iterates in the printed app path. Proposed only; grep owed. |
| 36 | NanoHTTPD$Cookie.getHTTPTime | `(I)Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :197-203. Printed callers are Cookie(String,String,int) :211 and CookieHandler.set :284; both are on dead paths (the int ctor is never constructed in printed code; set is uncalled). Proposed only; saved full-repo grep owed before merge. |
| 37 | NanoHTTPD$CookieHandler.<init> | `(Lorg/nanohttpd/NanoHTTPD;Ljava/util/Map;)V` | REACHABLE proposed | INFERRED | Def CookieHandler :233-244; caller HTTPSession.execute :713 (new CookieHandler(this.headers)). INFERRED: execute runs only on a ClientHandler thread. |
| 38 | NanoHTTPD$CookieHandler.delete | `(Ljava/lang/String;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :252-254 (set(name, '-delete-', -30) :253). No printed caller in the fresh corpus (TorrentStreamServer and NanoHTTPD contain no delete( call). Proposed only; saved full-repo grep owed before merge. |
| 39 | NanoHTTPD$CookieHandler.iterator | `()Ljava/util/Iterator;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :257-259 (cookies.keySet().iterator()). No printed for-each/iterator() call on a CookieHandler in the fresh corpus (unloadQueue iterates the queue list directly, not the handler). Proposed only; saved full-repo grep owed before merge. |
| 40 | NanoHTTPD$CookieHandler.read | `(Ljava/lang/String;)Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :267-269 (cookies.get(name)). No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |

Counts: 26 REACHABLE proposed / 14 UNREACHABLE proposed / 0 OPEN, out of 40. Sequence 1-40 intact, plan order, names + descriptors from the plan TSV.

## Still owed before any merge (not claimed done)

- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1.
- Saved full-repo grep for every UNREACHABLE-proposed row and every OPEN row (none in this batch) before any merge.
- Strict-entry decision (see conventions) and batch-14 vs batch-15/16 confirmed_by reconciliation.
- For batch 14 rows 11/24: saved grep for a BaseItem.equals/hashCode trigger.
