**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 16 — merge-ready file (UNVERIFIED proposal)

Scope: NanoHTTPD remainder: CookieHandler setters, DefaultAsyncRunner, DefaultServerSocketFactory, DefaultTempFile(Manager/Factory), HTTPSession, Method, Response.

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

## Shared trunk (freshly printed this session)

Same streaming trunk as batch 15: TorrentEngine :1056-1059 STATE settings gate (enableStreaming) -> startStreamingServer
:1063-1071 (new TorrentStreamServer :1069, start :1071) -> TorrentStreamServer.start :72-78 (super.start() :77) ->
NanoHTTPD.start chain :1794-1820 -> ServerRunnable.run :1347 -> DefaultAsyncRunner.exec :330-336 (Thread.start :336) ->
ClientHandler.run :168-195 (factory.create :172, new HTTPSession :173, session.execute :175, finally asyncRunner.closed :192) ->
HTTPSession.execute :655-760 (see batch 15 trunk for the full call list) -> virtual serve(this) :720 ->
TorrentStreamServer.serve :111 / handleTorrent :124-258. Base NanoHTTPD.serve(IHTTPSession) :1732-1746 is DEAD in the app path
(TSS overrides it and never calls super.serve); consequently base-serve-only callees (getMethod, getQueryParameterString,
parseBody and the whole parseBody subtree) are proposed UNREACHABLE, while TSS-called session methods (getUri, getParms,
getHeaders) are REACHABLE. Stop path: TorrentStreamServer.stop :81-84 -> NanoHTTPD.stop :1837-1845 (safeClose :1839,
asyncRunner.closeAll() :1840, myThread.join() :1842).

## Table (plan order)

| # | Method | JVM descriptor | Proposed label | confirmed_by | Route / reason |
|---:|--------|---------------|----------------|--------------|----------------|
| 1 | NanoHTTPD$CookieHandler.set(String,String,int) | `(Ljava/lang/String;Ljava/lang/String;I)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def CookieHandler.set(String,String,int) :283-285 (new Cookie + getHTTPTime :284). Only printed caller is delete :253, and delete has no printed caller (batch 15 row 38). Proposed only; saved full-repo grep owed before merge. |
| 2 | NanoHTTPD$CookieHandler.set(Cookie) | `(Lorg/nanohttpd/NanoHTTPD$Cookie;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def CookieHandler.set(Cookie) :270-272 (queue.add). No printed caller at all in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 3 | NanoHTTPD$CookieHandler.unloadQueue | `(Lorg/nanohttpd/NanoHTTPD$Response;)V` | REACHABLE proposed | INFERRED | Def :294-297 (addHeader :296); caller HTTPSession.execute :727 (cookies.unloadQueue(r)). INFERRED: execute runs only on a ClientHandler thread. |
| 4 | NanoHTTPD$DefaultAsyncRunner.<init> | `()V` | REACHABLE proposed | SOURCE | Def DefaultAsyncRunner (no explicit ctor; field init only); constructed NanoHTTPD ctor :1561 (setAsyncRunner(new DefaultAsyncRunner())). Printed direct call. |
| 5 | NanoHTTPD$DefaultAsyncRunner.closeAll | `()V` | REACHABLE proposed | SOURCE | Def :319-324 (clientHandler.close() :322); caller NanoHTTPD.stop :1840 <- TorrentStreamServer.stop :82. Printed direct call chain. |
| 6 | NanoHTTPD$DefaultAsyncRunner.closed | `(Lorg/nanohttpd/NanoHTTPD$ClientHandler;)V` | REACHABLE proposed | INFERRED | Def :326-328 (running.remove); caller ClientHandler.run finally :192 (asyncRunner.closed(this)). INFERRED: run is Thread-dispatched (exec :336). |
| 7 | NanoHTTPD$DefaultAsyncRunner.exec | `(Lorg/nanohttpd/NanoHTTPD$ClientHandler;)V` | REACHABLE proposed | INFERRED | Def :330-336 (new Thread :332, t.start() :336); caller ServerRunnable.run :1347, which runs only on the listener thread started at NanoHTTPD.start :1820. INFERRED: only printed path crosses Thread.start. |
| 8 | NanoHTTPD$DefaultServerSocketFactory.<init> | `()V` | REACHABLE proposed | SOURCE | Def DefaultServerSocketFactory (no explicit ctor); field initialiser NanoHTTPD :1531 (serverSocketFactory = new DefaultServerSocketFactory()). Runs at NanoHTTPD/TorrentStreamServer construction. Printed direct construction. |
| 9 | NanoHTTPD$DefaultServerSocketFactory.create | `()Ljava/net/ServerSocket;` | REACHABLE proposed | SOURCE | Def :426-428 (new ServerSocket()); caller NanoHTTPD.start(int,boolean) :1814 (getServerSocketFactory().create()). Printed direct call. |
| 10 | NanoHTTPD$DefaultTempFile.<init> | `(Ljava/io/File;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def DefaultTempFile :347-353 (File.createTempFile :351). Only constructed by DefaultTempFileManager.createTempFile :402-406, which is called only from the parseBody subtree (getTmpBucket :842, saveTmpFile :949); parseBody never runs in the app path (row 33). Proposed only; saved full-repo grep owed before merge. |
| 11 | NanoHTTPD$DefaultTempFile.delete | `()V` | UNREACHABLE proposed branch_never_taken | INFERRED | Def :355-360 (safeClose fstream, file.delete). Its caller DefaultTempFileManager.clear() :391-401 DOES run (HTTPSession.execute finally :754), but clear's loop iterates tempFiles, which gains entries only via createTempFile (row 15, dead path above), so the loop never iterates in the printed app path. Kind is branch_never_taken, not no_trigger_in_app. Proposed only; grep owed. |
| 12 | NanoHTTPD$DefaultTempFile.getName | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :362-364 (file.getAbsolutePath()). Printed callers are getTmpBucket :843 and saveTmpFile :951/:955, both in the dead parseBody subtree (row 33). Proposed only; saved full-repo grep owed before merge. |
| 13 | NanoHTTPD$DefaultTempFileManager.<init> | `()V` | REACHABLE proposed | INFERRED | Def DefaultTempFileManager (ctor :380-390 region; tmpdir + tempFiles list); constructed DefaultTempFileManagerFactory.create :413-415 <- ClientHandler.run :172. INFERRED: run is Thread-dispatched. |
| 14 | NanoHTTPD$DefaultTempFileManager.clear | `()V` | REACHABLE proposed | INFERRED | Def :391-401 (file.delete() loop); caller HTTPSession.execute finally :754 (tempFileManager.clear()). INFERRED: execute runs only on a ClientHandler thread. Note: the loop body is dead (see row 11); clear() itself runs. |
| 15 | NanoHTTPD$DefaultTempFileManager.createTempFile | `(Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$TempFile;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :402-406 (new DefaultTempFile, tempFiles.add). Printed callers are getTmpBucket :842 and saveTmpFile :949, both in the dead parseBody subtree (row 33). Proposed only; saved full-repo grep owed before merge. |
| 16 | NanoHTTPD$DefaultTempFileManagerFactory.<init> | `(Lorg/nanohttpd/NanoHTTPD;)V` | REACHABLE proposed | SOURCE | Def DefaultTempFileManagerFactory (private inner class; ctor takes enclosing NanoHTTPD, hence the (Lorg/nanohttpd/NanoHTTPD;)V descriptor); constructed NanoHTTPD ctor :1560 (setTempFileManagerFactory(new DefaultTempFileManagerFactory())). Printed direct call. |
| 17 | NanoHTTPD$DefaultTempFileManagerFactory.create | `()Lorg/nanohttpd/NanoHTTPD$TempFileManager;` | REACHABLE proposed | INFERRED | Def :413-415 (new DefaultTempFileManager()); caller ClientHandler.run :172 (tempFileManagerFactory.create()). INFERRED: run is Thread-dispatched. |
| 18 | NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream,InetAddress) | `(Lorg/nanohttpd/NanoHTTPD;Lorg/nanohttpd/NanoHTTPD$TempFileManager;Ljava/io/InputStream;Ljava/io/OutputStream;Ljava/net/InetAddress;)V` | REACHABLE proposed | INFERRED | Def HTTPSession (class :461); constructed ClientHandler.run :173 (new HTTPSession(tempFileManager, inputStream, outputStream, inetAddress)). INFERRED: run is Thread-dispatched. |
| 19 | NanoHTTPD$HTTPSession.decodeHeader | `(Ljava/io/BufferedReader;Ljava/util/Map;Ljava/util/Map;Ljava/util/Map;)V` | REACHABLE proposed | INFERRED | Def :494-540 (decodeParms :513, decodePercent :514/:516); caller HTTPSession.execute :703. INFERRED: execute runs only on a ClientHandler thread. |
| 20 | NanoHTTPD$HTTPSession.decodeMultipartFormData | `(Ljava/lang/String;Ljava/lang/String;Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/util/Map;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :544+. Only printed caller is parseBody :913, which never runs in the app path (row 33). Proposed only; saved full-repo grep owed before merge. |
| 21 | NanoHTTPD$HTTPSession.decodeParms | `(Ljava/lang/String;Ljava/util/Map;)V` | REACHABLE proposed | INFERRED | Def :637-653 (decodePercent :648/:650); live caller decodeHeader :513 (parseBody :921 is dead). INFERRED as row 19. |
| 22 | NanoHTTPD$HTTPSession.execute | `()V` | REACHABLE proposed | INFERRED | Def :655-760 (findHeaderEnd :683, decodeHeader :703, Method.lookup :708, new CookieHandler :713, serve(this) :720, unloadQueue :727, useGzipWhenAccepted :729, send :731, finally safeClose(r) :753, tempFileManager.clear() :754); caller ClientHandler.run :175 (session.execute(), in the keep-alive loop). INFERRED: run is Thread-dispatched. |
| 23 | NanoHTTPD$HTTPSession.findHeaderEnd | `([BI)I` | REACHABLE proposed | INFERRED | Def :761+; caller execute :683 (splitbyte = findHeaderEnd(buf, rlen)). INFERRED as row 19. |
| 24 | NanoHTTPD$HTTPSession.getAttributeFromContentHeader | `(Ljava/lang/String;Ljava/util/regex/Pattern;Ljava/lang/String;)Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :936+; only printed callers are parseBody :913/:914, which never runs in the app path (row 33). Proposed only; saved full-repo grep owed before merge. |
| 25 | NanoHTTPD$HTTPSession.getBodySize | `()J` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :856+; only printed caller is parseBody :868 (the :717 TODO comment is not a call). parseBody never runs in the app path (row 33). Proposed only; saved full-repo grep owed before merge. |
| 26 | NanoHTTPD$HTTPSession.getBoundaryPositions | `(Ljava/nio/ByteBuffer;[B)[I` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :781+; only printed caller is decodeMultipartFormData :546, which is itself parseBody-only (row 20). Proposed only; saved full-repo grep owed before merge. |
| 27 | NanoHTTPD$HTTPSession.getHeaders | `()Ljava/util/Map;` | REACHABLE proposed | INFERRED | Def :821+; caller TorrentStreamServer.handleTorrent :150 (httpSession.getHeaders()). INFERRED: handleTorrent runs via virtual serve dispatch on a ClientHandler thread. (Base serve :1746 is dead; this row is saved by the TSS caller.) |
| 28 | NanoHTTPD$HTTPSession.getMethod | `()Lorg/nanohttpd/NanoHTTPD$Method;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :829+. Only printed caller is base serve(IHTTPSession) :1734, which TorrentStreamServer overrides (:111) and never calls via super; TorrentStreamServer.handleTorrent never calls getMethod. Proposed only; saved full-repo grep owed before merge. |
| 29 | NanoHTTPD$HTTPSession.getParms | `()Ljava/util/Map;` | REACHABLE proposed | INFERRED | Def :833+; caller TorrentStreamServer.handleTorrent :132 (httpSession.getParms()). INFERRED as row 27. (Base serve :1744 is dead; this row is saved by the TSS caller.) |
| 30 | NanoHTTPD$HTTPSession.getQueryParameterString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :837+. Only printed caller is base serve(IHTTPSession) :1745, which TorrentStreamServer overrides (:111) and never calls via super; TorrentStreamServer parses params via getParms, not the query string. Proposed only; saved full-repo grep owed before merge. |
| 31 | NanoHTTPD$HTTPSession.getTmpBucket | `()Ljava/io/RandomAccessFile;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :840-844 (createTempFile :842, getName :843); only printed caller is parseBody :876, which never runs in the app path (row 33). Proposed only; saved full-repo grep owed before merge. |
| 32 | NanoHTTPD$HTTPSession.getUri | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :849+; callers TorrentStreamServer.serve :112 (session.getUri()) and handleTorrent :129 (httpSession.getUri()). INFERRED: serve runs via virtual dispatch on a ClientHandler thread. |
| 33 | NanoHTTPD$HTTPSession.parseBody | `(Ljava/util/Map;)V` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :865+ (getBodySize :868, getTmpBucket :876, decodeMultipartFormData :913, decodeParms :921, saveTmpFile :930, createTempFile :949). Only printed caller is base serve(IHTTPSession) :1737 (PUT/POST branch), which TorrentStreamServer overrides (:111) and never calls via super; the full TorrentStreamServer.java (284 lines, freshly printed) contains no parseBody call. Proposed only; saved full-repo grep owed before merge. Consequence: rows 10, 12, 15, 20, 24, 25, 26, 31, 34, 35 are UNREACHABLE only because this row is; if a saved grep finds a live parseBody caller, that whole subtree must be re-judged together. |
| 34 | NanoHTTPD$HTTPSession.saveTmpFile | `(Ljava/nio/ByteBuffer;IILjava/lang/String;)Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :944+ (createTempFile :949, getName :951/:955); printed callers are decodeMultipartFormData :606 and parseBody :930, both in the dead parseBody subtree (row 33). Proposed only; saved full-repo grep owed before merge. |
| 35 | NanoHTTPD$HTTPSession.scipOverNewLine | `([BI)I` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :625+; only printed caller is decodeMultipartFormData :590, which is itself parseBody-only (row 20). Proposed only; saved full-repo grep owed before merge. |
| 36 | NanoHTTPD$Method.<clinit> | `()V` | REACHABLE proposed | INFERRED | Method enum <clinit> (implicit static initialisation of enum constants). Runs on first Method class use in the live path, HTTPSession.execute :708 (Method.lookup). INFERRED: JVM class-load dispatch, not a printed call. |
| 37 | NanoHTTPD$Method.lookup | `(Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$Method;` | REACHABLE proposed | INFERRED | Def :1003+; caller HTTPSession.execute :708 (Method.lookup(pre.get("method"))). INFERRED as row 19. |
| 38 | NanoHTTPD$Response.<init> | `(Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/io/InputStream;J)V` | REACHABLE proposed | INFERRED | Def Response :1122 (protected 4-arg ctor); constructed by newFixedLengthResponse :1697 (live via TorrentStreamServer.handleTorrent and execute catch :745/:749) and newChunkedResponse :1691 (itself uncalled in the app path; the claim that TorrentStreamServer calls newChunkedResponse is FALSE — the full TSS file contains zero newChunkedResponse calls, only newFixedLengthResponse). INFERRED: reached via the static factory on a ClientHandler thread. |
| 39 | NanoHTTPD$Response.addHeader | `(Ljava/lang/String;Ljava/lang/String;)V` | REACHABLE proposed | INFERRED | Def :1144+; live callers CookieHandler.unloadQueue :296 (via execute :727) and TorrentStreamServer.handleTorrent res.addHeader sites plus DLNAFileType.setHeaders. INFERRED as row 27. |
| 40 | NanoHTTPD$Response.close | `()V` | REACHABLE proposed | INFERRED | Def Response.close :1136+; caller is HTTPSession.execute finally :753 safeClose(r), where safeClose :1511-1519 calls Closeable.close() virtually. INFERRED: virtual dispatch target is not named by a printed call site. |

Counts: 24 REACHABLE proposed / 16 UNREACHABLE proposed / 0 OPEN, out of 40. Sequence 1-40 intact, plan order, names + descriptors from the plan TSV.

## Still owed before any merge (not claimed done)

- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1.
- Saved full-repo grep for every UNREACHABLE-proposed row and every OPEN row (none in this batch) before any merge.
- Strict-entry decision (see conventions) and batch-14 vs batch-15/16 confirmed_by reconciliation.
- For batch 14 rows 11/24: saved grep for a BaseItem.equals/hashCode trigger.
