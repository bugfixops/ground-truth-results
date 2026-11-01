**REVISION 2026-11-01 (OPEN-closing round 2) — UNVERIFIED.** Original for this round backed up in `~/workspace/libretorrent-merge-backup-pre-openclose2/batch2-merge-ready.md` (verified identical before editing). Counts UNCHANGED: 0 REACHABLE / 36 UNREACHABLE proposed / 4 OPEN. No label flipped. What was checked: fresh round-2 grep over the 252 app Java files (`~/workspace/b12341112-openclose2-src/round2_grep_20261101.txt`, sections G1–G2, G4, G11) re-confirms round 1 — zero hits for `DataBinderMapperImpl`, `InnerBrLookup`, `InnerLayoutIdLookup`, `DataBindingTriggerClass`; zero `new BR(` sites; `BR.<field>` reads exist but do not invoke `<init>`; `DataBindingUtil` is used in 30 app files (the printed databinding-use premise for the conditional table below). No generated source was printed in this round and no GitHub connector fetch was needed. Rows 37–40 therefore stay OPEN: their flip conditions are the conditional table below, not this grep. Rows 1–36 were NOT re-judged in round 2 (only the OPEN rows were in scope) and are unchanged. Build: not run. C1: not run.

**REVISION 2026-11-01 (OPEN-closing) — UNVERIFIED.** Original backed up in `~/workspace/libretorrent-merge-backup-pre-openclose/batch2-merge-ready.md`. Counts UNCHANGED: 0 REACHABLE / 36 UNREACHABLE proposed / 4 OPEN. No label flipped. What changed: (a) Rows 1-9 "local reprint" gap CLOSED: the parser is now freshly printed from the branch — `core/FeedParser.java`, 267 lines, SHA `99c05d88bd9fb5824a05efdaf176d4b87b637d8` (saved in `~/workspace/b12341112-openclose-src/` with connector JSON) — and its caller set matches the local reprint exactly (`feed.getTitle()`:86, `feed.getItemList()`:95, `item.getLinks()`:96, `item.getPubDate()`:104, `item.getTitle()`:110, `item.getEnclosures()`:170, `enclosure.getUrl()`:174 / `getType()`:175, `item.getMediaRss()`:190, `media.getContent()`:194, content `getType()`:202, `media.getHash()`:217, `item.getEzRssTorrentItem()`:238, `torrentItem.getInfoHash()`:242). Rows 1-9 stay UNREACHABLE proposed: the saved grep adds no app-code caller for any of them. (b) Rows 1-36 UNREACHABLE-proposed re-verified against the saved grep, including the internal chains re-checked in Corpus B (makeSSLSocketFactory 20->21->22 chain, makeSecure definition only, newChunkedResponse definition only, wasStarted called only by isAlive row 18, mimeTypes called only by getMimeTypeForFile row 16, getCookies/getRunning/setServerSocketFactory definitions only; TorrentStreamServer newFixedLengthResponse calls inspected manually — all multi-arg, so the single-arg overload row 26 still has no caller; the dot-pattern grep misses unqualified subclass calls, and that manual inspection closes that gap for this method). (c) Rows 37-40 stay OPEN, evidence upgraded: saved grep has ZERO hits for `DataBinderMapperImpl`, `InnerBrLookup`, `InnerLayoutIdLookup`, `DataBindingTriggerClass` and zero `new BR(` in the app tree; libretorrent BR field reads exist (BR.xxx in MutableParams/Activity files) but prove class loading, not `<init>` invocation; generated mapper/Impl sources are absent, so convention (x) still decides these rows. Build: not run. C1: not run. Saved grep: saved grep `~/workspace/b12341112-openclose-src/ruleF_grep_20261101.txt` (2,043 lines; Corpus A: 252 app Java files in `~/workspace/ruleF-src`, connector-reconstructed from branch work-2026-10-31 and verified 252/252 against the walk list; Corpus B: printed library files in `~/workspace/b1-src` + `~/workspace/b2-src`; scope: res/ XML, generated sources and library sources outside Corpus B are NOT in the grep — see caveats).

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 2 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 2 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior work (Agent 50's batches 1–12
  audit) was used as an INPUT / lead list only; every row below was re-judged from the
  source printed in this pass, and no audit verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 2 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-2 rows are `DONE_RECHECK` in the plan with `current_label`
`UNREACHABLE no_trigger_in_app`. That plan label is NOT adopted wholesale below:
rows 1–36 are proposed UNREACHABLE on the printed evidence in this pass, rows 37–40
are left OPEN (see below) — the plan's UNREACHABLE claim for the generated ctors
rests on absence alone, which is not enough for generated code.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time, saved in
`~/workspace/b2-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):

- `com/ernieyu/feedparser/impl/Rss2Feed.java` — SHA `2051ebd60e9e0132e561c12281d6ee4544f834d4`,
  137 lines, byte-identical to the local copy `~/workspace/wp1_batch14/src/Rss2Feed.java`.
- `com/ernieyu/feedparser/impl/Rss2Item.java` — SHA `2b36387bc13b9c5ac5ec7088bc3bd56bb85eb0e0`,
  122 lines, byte-identical to the local copy.
- `com/ernieyu/feedparser/mediarss/MediaRss.java` — SHA `d65278dab14dd7fdb7dbca94a22fce20f86e0a04`,
  50 lines, byte-identical to the local copy.
- `com/ernieyu/feedparser/mediarss/PeerLink.java` — SHA `b495e7cb17c0899cd45567ccb716b7f71b69b072`,
  69 lines, byte-identical to the local copy.
- `org/nanohttpd/NanoHTTPD.java` — SHA `bdb2ab6792848f05fedf1b5d7f31abe4b49878fb`,
  1,851 lines, byte-identical to the local copy
  `~/workspace/ground-truth-work/libretorrent/src/NanoHTTPD.java`.
- `org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java` — SHA
  `d69e997fdd03b1337d33d60b8a5399b72d052ff9`, 284 lines, byte-identical to the local copy.

Re-read in full from a previously printed local copy, NOT freshly fetched in this pass
(path guesses failed cleanly — see "Gaps" below), saved as
`~/workspace/b2-src/CoreFeedParser-LOCAL-REPRINT.java`:

- `CoreFeedParser.java` (package `org.proninyaroslav.libretorrent.core`, local copy
  `~/workspace/wp1_batch14/src/CoreFeedParser.java`). The caller set cited for rows 1–9
  comes from this reprint and must be re-printed fresh by the merger before merging
  rows 1–9 (see "Gaps"). The fact that every freshly fetched definition file above
  matched its local copy byte-for-byte raises confidence in this corpus, but it does
  not replace a fresh CoreFeedParser print.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run; a saved full-repo grep is still owed for every
UNREACHABLE-proposed row below, and a single grep hit for a row flips that row to
REACHABLE. That is why every UNREACHABLE row here is `confirmed_by` INFERRED, never
SOURCE: printed definitions plus a printed disjoint caller set do not, on their own,
prove absence from the whole repo.

## confirmed_by convention in this file

- `INFERRED` for every row below. For UNREACHABLE-proposed rows it means: the definition
  is printed, the printed app/library caller set is disjoint from the method (or, for
  the NanoHTTPD internal chains, the only printed caller is itself uncalled), and the
  label is a proposal pending the saved full-repo grep. For OPEN rows it means: at best
  an inference, because the source is absent (generated code) — see rows 37–40.
- No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## The two caller sets that decide most rows

**Feed parser (CoreFeedParser, local reprint).** The app-side parser calls, on the
interfaces, exactly: `feed.getTitle()` (:86), `feed.getItemList()` (:95),
`item.getLinks()` (:96), `item.getPubDate()` — item-level — (:104), `item.getTitle()` (:110),
`item.getEnclosures()` (:170), `enclosure.getUrl()` (:174) / `enclosure.getType()` (:175),
`item.getMediaRss()` (:190), `media.getContent()` (:194), `content.getType()` (:202),
`media.getHash()` (:217), `item.getEzRssTorrentItem()` (:238),
`torrentItem.getInfoHash()` (:242). It does NOT call `feed.getLink()`,
`feed.getPubDate()` (feed-level), `feed.getCategories()`, `feed.getType()`,
`item.getAuthor()`, `item.getCategories()`, `item.getType()`, `media.getPeerLinks()`,
or any `PeerLink` accessor. Traps avoided: `item.getPubDate()` (:104) is item-level and
does not touch feed-level row 2; `enclosure.getType()` (:175) and `content.getType()` (:202)
are different classes and do not touch item-level row 6.

**Streaming server (TorrentStreamServer, fresh).** `TorrentStreamServer extends NanoHTTPD`
(:51). Its ctor calls `super(host, port)` (:69); its `start()` calls `super.start()` (:78);
its `stop()` calls `super.stop()` (:84); its `serve()` calls only multi-arg
`newFixedLengthResponse(...)` (:127, :130, :134, :144, :147, :196, :209, :222, :231, :239,
:244, :256) and, on the session, `getUri()` (:113), `getParms()` (:132), `getHeaders()` (:150).
It never calls `newChunkedResponse`, the single-arg `newFixedLengthResponse`, or any
other NanoHTTPD row in this batch.

## Table — 40 rows in plan order

| # | Method (descriptor) | Label proposed | confirmed_by | Printed citation / reason |
|---|---------------------|----------------|--------------|---------------------------|
| 1 | Rss2Feed.getLink ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:54-65 (fresh). Parser caller set above contains no `feed.getLink()` call. Grep owed; a hit flips to REACHABLE. |
| 2 | Rss2Feed.getPubDate ()Ljava/util/Date; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:89-97 (fresh). Parser never calls feed-level `getPubDate()`; `item.getPubDate()` at CoreFeedParser:104 is item-level, a different receiver. Grep owed. |
| 3 | Rss2Feed.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:42-44 (fresh). Parser never calls `feed.getType()`. Grep owed. |
| 4 | Rss2Item.getAuthor ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Item.java:63-66 (fresh). Parser never calls `item.getAuthor()`. Grep owed. |
| 5 | Rss2Item.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Item.java:81-91 (fresh). Parser never calls `item.getCategories()`. Grep owed. |
| 6 | Rss2Item.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Item.java:35-37 (fresh). Parser never calls `item.getType()`; `enclosure.getType()` (CoreFeedParser:175) and `content.getType()` (:202) are different classes. Grep owed. |
| 7 | MediaRss.getPeerLinks ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition MediaRss.java:38-40 (fresh). Parser calls `media.getContent()` (:194) and `media.getHash()` (:217), never `getPeerLinks()`. Rows 8-9 inherit this gap (their only route is through this list). Grep owed. |
| 8 | PeerLink.getHref ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition PeerLink.java:27-29 (fresh). No printed caller in the printed corpus; the only printed producer of PeerLink objects is `getPeerLinks()` (row 7, itself uncalled). Grep owed. |
| 9 | PeerLink.getType ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition PeerLink.java:38-40 (fresh). Same as row 8. Grep owed. |
| 10 | NanoHTTPD.<init>(int) (I)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Strongest row in the batch. Definition NanoHTTPD.java:1544-1546 (fresh) delegates `this(null, port)` to the 2-arg ctor at :1557-1562. TorrentStreamServer ctor calls `super(host, port)` at TorrentStreamServer.java:69 — the 2-arg form only. No other printed `new NanoHTTPD(` site. Full grep still owed for any other construction site. |
| 11 | NanoHTTPD.closeAllConnections ()V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1566-1568 (fresh), body calls `stop()`. No printed caller of `closeAllConnections` itself; TorrentStreamServer.stop() calls `super.stop()` (:84), not this. Grep owed. |
| 12 | NanoHTTPD.decodeParameters(String) (Ljava/lang/String;)Ljava/util/Map; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1619 (fresh). Its only printed caller is `decodeParameters(Map)` at :1605, which itself has no printed caller (row 13). Session code uses a different private method, `decodeParms` (:637, called :513, :921), not this. Grep owed. |
| 13 | NanoHTTPD.decodeParameters(Map) (Ljava/lang/Map;)Ljava/util/Map; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1604-1606 (fresh), body calls row 12. No printed caller of the Map overload in the printed corpus. Grep owed. |
| 14 | NanoHTTPD.getHostname ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1675-1677 (fresh). No printed caller; server code reads the `hostname` field directly (e.g. ServerRunnable bind at :1334). Grep owed. |
| 15 | NanoHTTPD.getListeningPort ()I | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1663-1665 (fresh). No printed caller; server code reads the `myPort` field directly (e.g. bind at :1334). Grep owed. |
| 16 | NanoHTTPD.getMimeTypeForFile (Ljava/lang/String;)Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1503-1511 (fresh). No printed caller; it is the entry of the mime chain (row 16 -> row 24 -> row 19), not a callee of any printed code. Grep owed. |
| 17 | NanoHTTPD.getTempFileManagerFactory ()Lorg/nanohttpd/NanoHTTPD$TempFileManagerFactory; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1678-1680 (fresh). No printed caller; internal code accesses the `tempFileManagerFactory` field directly (e.g. ClientHandler at :172). Grep owed. |
| 18 | NanoHTTPD.isAlive ()Z | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1666-1668 (fresh), body calls `wasStarted()` (row 28). No printed caller of `isAlive` itself. Grep owed. |
| 19 | NanoHTTPD.loadMimeTypes (Ljava/util/Map;Ljava/lang/String;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1429 (fresh, private static). Its only printed caller is `mimeTypes()` at :1421-1422 (row 24), which is itself entered only via row 16. Grep owed. |
| 20 | NanoHTTPD.makeSSLSocketFactory(String,char[]) (Ljava/lang/String;[C)Ljavax/net/ssl/SSLServerSocketFactory; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1484-1492 (fresh), body calls row 21 at :1491. No external printed caller; the SSL chain (rows 20-22, 23, 36) has no printed entry. Grep owed. |
| 21 | NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory) (Ljava/security/KeyStore;Ljavax/net/ssl/KeyManagerFactory;)Ljavax/net/ssl/SSLServerSocketFactory; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1473-1478 (fresh), body calls row 22 at :1475. No external printed caller beyond row 20. Grep owed. |
| 22 | NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManager[]) (Ljava/security/KeyStore;[Ljavax/net/ssl/KeyManager;)Ljavax/net/ssl/SSLServerSocketFactory; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1455 (fresh), base of the chain. No printed caller except row 21. Grep owed. |
| 23 | NanoHTTPD.makeSecure (Ljavax/net/ssl/SSLServerSocketFactory;[Ljava/lang/String;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1684-1686 (fresh). No printed caller. Note: it does NOT call `makeSSLSocketFactory` — it takes an already-created factory as an argument and wraps it in `SecureServerSocketFactory` at :1685. Grep owed (for `makeSecure`, which is also row 36's entry). |
| 24 | NanoHTTPD.mimeTypes ()Ljava/util/Map; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1418-1427 (fresh). Its only printed caller is `getMimeTypeForFile` at :1507 (row 16), which has no printed caller. Grep owed. |
| 25 | NanoHTTPD.newChunkedResponse (Lorg/nanohttpd/NanoHTTPD$Response$IStatus;Ljava/lang/String;Ljava/io/InputStream;)Lorg/nanohttpd/NanoHTTPD$Response; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1690-1692 (fresh). No printed caller; TorrentStreamServer.serve and HTTPSession.execute use only `newFixedLengthResponse`. Consistent with the batch-16 correction removing the `newChunkedResponse` claim for TorrentStreamServer. Grep owed. |
| 26 | NanoHTTPD.newFixedLengthResponse(String) (Ljava/lang/String;)Lorg/nanohttpd/NanoHTTPD$Response; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1719-1721 (fresh), body calls the multi-arg overload at :1720. The multi-arg overloads ARE called (TorrentStreamServer.serve :127-256; HTTPSession.execute :745, :749, :1739, :1741, :1768), but the single-arg overload itself has no printed caller. Overload-level distinction, not a blanket claim about `newFixedLengthResponse`. Grep owed. |
| 27 | NanoHTTPD.setServerSocketFactory (Lorg/nanohttpd/NanoHTTPD$ServerSocketFactory;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1672-1674 (fresh). No printed caller; `start()` uses `getServerSocketFactory()` at :1814, and the 2-arg ctor installs the default factories directly at :1560-1561, not via this setter. Grep owed. |
| 28 | NanoHTTPD.wasStarted ()Z | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:1848-1850 (fresh). Its only printed caller is `isAlive()` at :1667 (row 18), which has no printed caller. Grep owed. |
| 29 | NanoHTTPD$Cookie.<init>(String,String) (Ljava/lang/String;Ljava/lang/String;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:205-207 (fresh). No printed construction site; `CookieHandler.set(String,int)` at :284 calls the (String,String,String) overload at :213, not this one. Grep owed. |
| 30 | NanoHTTPD$Cookie.<init>(String,String,int) (Ljava/lang/String;Ljava/lang/String;I)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:208-210 (fresh). Same as row 29: `CookieHandler.set` converts the int to a time string via `Cookie.getHTTPTime(expires)` and calls the String overload, not this one. Grep owed. |
| 31 | NanoHTTPD$DefaultAsyncRunner.getRunning ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:315-317 (fresh). No printed caller; NanoHTTPD code uses `asyncRunner.exec()` / `closed()` / `closeAll()` (e.g. ServerRunnable :1347, stop() :1840), never `getRunning()`. The runner is installed in the 2-arg ctor at :1561. Grep owed. |
| 32 | NanoHTTPD$DefaultTempFile.open ()Ljava/io/OutputStream; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:366-368 (fresh). No printed caller; TempFile use inside HTTPSession uses `getName()` only (:843, :951, :955), never `open()`. Grep owed. |
| 33 | NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream) (Lorg/nanohttpd/NanoHTTPD;Lorg/nanohttpd/NanoHTTPD$TempFileManager;Ljava/io/InputStream;Ljava/io/OutputStream;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Source 3-arg ctor NanoHTTPD.java:479-483 (fresh); HTTPSession is an inner class, so the JVM descriptor's first `NanoHTTPD` argument is the outer `this`. The only printed session creation site is the 4-arg ctor at :173 (`new HTTPSession(tempFileManager, inputStream, outputStream, inetAddress)`), not this 3-arg form. Grep owed for any other creation site. |
| 34 | NanoHTTPD$HTTPSession.getCookies ()Lorg/nanohttpd/NanoHTTPD$CookieHandler; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:817-819 (fresh, IHTTPSession implementation). No printed caller; TorrentStreamServer.serve uses `getUri()` (:113), `getParms()` (:132), `getHeaders()` (:150) only, and HTTPSession.execute reads the `cookies` field directly. Grep owed. |
| 35 | NanoHTTPD$HTTPSession.getInputStream ()Ljava/io/InputStream; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:825-827 (fresh). Same as row 34: no printed caller; session code reads the `inputStream` field directly. Grep owed. |
| 36 | NanoHTTPD$SecureServerSocketFactory.<init> (Ljavax/net/ssl/SSLServerSocketFactory;[Ljava/lang/String;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition NanoHTTPD.java:436 (fresh). Its only printed caller is `makeSecure` at :1685 (row 23), which itself has no printed caller — this row inherits row 23's grep target. If a `makeSecure` caller is found, both rows flip. |
| 37 | libretorrent.BR.<init> ()V | OPEN | INFERRED | Generated class: no source in the upload, no generated file printed in this pass. The plan's UNREACHABLE claim rests on absence alone and is NOT adopted. REVISION 2026-11-01: saved grep (app tree) has zero hits for DataBinderMapperImpl/InnerBrLookup/InnerLayoutIdLookup/DataBindingTriggerClass and zero `new BR(`; BR field reads exist but do not invoke `<init>`. Still OPEN under convention (x); do not merge as UNREACHABLE on this evidence. Round-2 conditional table: see the CONDITIONAL flip tables section (rows 37–40). |
| 38 | libretorrent.DataBinderMapperImpl$InnerBrLookup.<init> ()V | OPEN | INFERRED | Generated class, same as row 37. Note: this is the `libretorrent` mapper, NOT batch 12's `databinding.DataBinderMapperImpl` — do not conflate the two; the batch-12 mapper row is itself OPEN elsewhere, and generated mapper dispatch is unresolved in this project. Grep / generated-source evidence owed. |
| 39 | libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<init> ()V | OPEN | INFERRED | Generated class, same as rows 37-38. Grep / generated-source evidence owed. |
| 40 | DataBindingTriggerClass.<init> ()V | OPEN | INFERRED | Generated class, same as rows 37-39: no source printed, no dispatch evidence printed. Grep / generated-source evidence owed. |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **36 UNREACHABLE proposed / 0 REACHABLE proposed / 4 OPEN.**
- All 36 UNREACHABLE-proposed rows are `confirmed_by` INFERRED; all 4 OPEN rows are
  `confirmed_by` INFERRED (at best, source absent).
- **0 rows verified for merge.** Verification requires, in order: the main agent's
  1-in-5 spot-check of this part, `py_compile` + build on a full checkout, and the
  Mac build/C1 return — none of which has happened here. The saved full-repo grep for
  rows 1–36 is also still owed before any of them may be merged as UNREACHABLE.

## Internal-call chains — so the merger does not mistake them for reachability

These internal calls were checked and deliberately NOT treated as routes, because the
entry method of each chain has no printed caller:

- `isAlive` (:1666) -> `wasStarted` (:1848): rows 18, 28.
- `getMimeTypeForFile` (:1503) -> `mimeTypes` (:1418) -> `loadMimeTypes` (:1429): rows 16, 24, 19.
- `makeSSLSocketFactory(String,char[])` (:1484) -> `(KeyStore,KeyManagerFactory)` (:1473)
  -> `(KeyStore,KeyManager[])` (:1455): rows 20, 21, 22.
- `makeSecure` (:1684) -> `SecureServerSocketFactory.<init>` (:436): rows 23, 36.
- `decodeParameters(Map)` (:1604) -> `decodeParameters(String)` (:1619): rows 13, 12.
- `newFixedLengthResponse(String)` (:1719) -> multi-arg overload (:1720): row 26 only;
  the multi-arg overloads are genuinely called, the single-arg one is not.
- `closeAllConnections` (:1566) -> `stop()`: row 11 only; `stop()` itself is called,
  `closeAllConnections` is not.
- `NanoHTTPD(int)` (:1544) -> `NanoHTTPD(String,int)` (:1557): row 10 only; the 2-arg
  ctor is genuinely called via `super(host, port)`, the 1-arg one is not.
- `CookieHandler.set(String,int)` (:284) -> `Cookie(String,String,String)` (:213):
  rows 29, 30 are the two overloads that are NOT the one called.

## Strict-entry caveat

No launcher entry was printed in this pass. That does not change any label here,
because there are zero REACHABLE-proposed rows to revert: UNREACHABLE-proposed means
"no trigger in the app on the printed evidence", and the missing launcher step is
already covered by the grep-owed flag on every such row — a caller found by the grep,
at any entry depth, flips the row. The TorrentEngine -> TorrentStreamServer step
(TorrentEngine creates the server and starts it) was checked only in a local copy
(`~/workspace/ground-truth-work/libretorrent/src/TorrentEngine.java`, creation/start
around :1069-1071), not freshly fetched in this pass; the merger should re-print it
if it wants a fresh anchor for rows 10–36.

## Gaps / what the merger must still do (do not skip)

1. **Saved full-repo grep for rows 1–36** (highest value first: `new NanoHTTPD(`,
   `makeSecure`, `newChunkedResponse`, `getMimeTypeForFile`, `closeAllConnections`,
   `feed.getLink` / `feed.getPubDate` / `feed.getType` / `item.getAuthor` /
   `item.getCategories` / `item.getType` / `getPeerLinks` / `PeerLink` accessors).
   Any hit flips that row to REACHABLE.
2. **Fresh CoreFeedParser print** for rows 1–9: two branch-path guesses failed cleanly
   in this pass (`.../core/utils/CoreFeedParser.java` and `.../core/CoreFeedParser.java`
   both returned "path does not point to a file"), so the caller set rests on the
   local reprint. Do not merge rows 1–9 until that file is printed fresh from the branch.
3. **Generated evidence for rows 37–40**: printed generated source, or a saved
   class-name grep (rule F / C5), or a framework-dispatch citation from `fw_src/`.
   Until then they stay OPEN — they must not be merged as UNREACHABLE, and they must
   not be copied from batch 12's different mapper class.
4. **Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1** — all not run here.
5. **No 429 was hit in this pass.** The only failed fetches were the two clean
   CoreFeedParser path guesses above (file-not-found, not rate-limit), which were
   not retried in a loop.

## CONDITIONAL flip tables — OPEN-closing round 2 (rows 37–40 only; do not apply without the named decision)

Convention dependency: generated-mapper-load convention (x). Printed premise
already established in round 2 (not a decision): the app inflates databinding
layouts from 30 files via `DataBindingUtil` (e.g. MainFragment.java:119,
LogActivity.java:93, AddTorrentActivity.java:102) — so IF the merger decides that
databinding use loads the generated mapper, the mapper-load premise is satisfied
for the `libretorrent` mapper family. Each row still flips on its own class's
evidence; rows 37–40 are NOT the batch-12 `databinding` mapper and NOT batch 1's
`baseAdapters.BR` — no conclusion transfers between those classes.

| Row | If (x) says mapper load counts as invocation (on the printed DataBindingUtil use) | If (x) requires printed generated source / printed library dispatch | If a printed construction/dispatch site for that class appears |
|---|---|---|---|
| 37 `libretorrent.BR.<init>` | stays OPEN — field reads trigger `<clinit>`, not `<init>`; mapper loading does not construct BR (same reasoning as batch 1 row 1) | stays OPEN | → REACHABLE on a printed `new BR(` site for this class (none known); → UNREACHABLE `no_trigger_in_app` INFERRED only if the merger separately accepts the app-tree grep (zero `new BR(`) + constants-class structure as sufficient |
| 38 `libretorrent.DataBinderMapperImpl$InnerBrLookup.<init>` | → REACHABLE INFERRED (mapper-load premise + inner lookup constructed by the mapper's generated code; the mapper step itself is unprinted, hence INFERRED, never SOURCE) | stays OPEN | → REACHABLE on the printed site (SOURCE if printed); a printed generated mapper body showing the inner lookup is NOT constructed would instead support UNREACHABLE |
| 39 `libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<init>` | → REACHABLE INFERRED, same as row 38 | stays OPEN | same as row 38 |
| 40 `DataBindingTriggerClass.<init>` | → REACHABLE INFERRED only if the merger treats trigger-class loading as part of mapper load; otherwise stays OPEN even under the mapper-load decision (its own dispatch is the least understood of the four — flag it, do not silently bundle it) | stays OPEN | → REACHABLE on a printed construction/dispatch site for this class |

## What this part is not

- Not a merge: `graph_def.py` is untouched, and this file is not in `graph_def.py` format.
  The merger converts rows 1–36 (if the grep clears them) to UNREACHABLE entries with
  kind `no_trigger_in_app` and the citations above, and leaves rows 37–40 out until
  generated evidence exists.
- Not a claim about batches 1 or 3–120, about any other app, or about device replay.
- Not a claim that the plan's DONE_RECHECK labels are verified: they happen to agree
  with the proposals for rows 1–36 and disagree in form for rows 37–40, but agreement
  with the plan is not verification.
