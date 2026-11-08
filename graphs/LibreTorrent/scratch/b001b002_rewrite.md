# b001/b002 rewrite (2026-11-01, coordinator user order 18:41 EST)

Rule: when a key already exists in graph_def.py with stronger evidence, KEEP the stronger one, never downgrade (SOURCE > INFERRED).

## 1. Stronger-evidence restoration

Audit: A1-base inline entries from clone graph_def.py (head 6805252; A1 did not touch graph_def.py) vs part entries.
For each restored key the part grade is now SOURCE and the part evidence now LEADS with the inline SOURCE citation, followed by the part evidence. Kinds, labels, and part reasons are untouched (except owed-grep sentences, section 2).

### b001: 39 restored

- Enclosure.getLength: inline evidence `SRC Enclosure.java:52`
- EzRssTorrentItem.getContentLength: inline evidence `SRC EzRssTorrentItem.java:69`
- EzRssTorrentItem.getFileName: inline evidence `SRC EzRssTorrentItem.java:45`
- EzRssTorrentItem.getMagnetUri: inline evidence `SRC EzRssTorrentItem.java:53`
- EzRssTorrentItem.getPeers: inline evidence `SRC EzRssTorrentItem.java:85`
- EzRssTorrentItem.getSeeds: inline evidence `SRC EzRssTorrentItem.java:77`
- EzRssTorrentItem.isVerified: inline evidence `SRC EzRssTorrentItem.java:93`
- FeedException.<init>(): inline evidence `SRC FeedException.java:8`
- FeedException.<init>(String,Throwable): inline evidence `SRC FeedException.java:19`
- FeedParserFactory.<init>: inline evidence `SRC FeedParserFactory.java:16`
- FeedUtils.<init>: inline evidence `SRC FeedUtils.java:12`
- XML.<init>: inline evidence `SRC XML.java:7`
- AtomFeed.getCategories: inline evidence `SRC AtomFeed.java:81`
- AtomFeed.getCopyright: inline evidence `SRC AtomFeed.java:69`
- AtomFeed.getDescription: inline evidence `SRC AtomFeed.java:56`
- AtomFeed.getLanguage: inline evidence `SRC AtomFeed.java:62`
- AtomFeed.getLink: inline evidence `SRC AtomFeed.java:50`
- AtomFeed.getPubDate: inline evidence `SRC AtomFeed.java:75`
- AtomFeed.getType: inline evidence `SRC AtomFeed.java:39`
- AtomItem.getAuthor: inline evidence `SRC AtomItem.java:64`
- AtomItem.getCategories: inline evidence `SRC AtomItem.java:86`
- AtomItem.getType: inline evidence `SRC AtomItem.java:35`
- BaseElement.<init>(String,String): inline evidence `SRC BaseElement.java:29`
- BaseElement.getElementKeys: inline evidence `SRC BaseElement.java:84`
- BaseElement.getName: inline evidence `SRC BaseElement.java:51`
- Rss1Feed.getCategories: inline evidence `SRC Rss1Feed.java:98`
- Rss1Feed.getCopyright: inline evidence `SRC Rss1Feed.java:82`
- Rss1Feed.getDescription: inline evidence `SRC Rss1Feed.java:67`
- Rss1Feed.getLanguage: inline evidence `SRC Rss1Feed.java:74`
- Rss1Feed.getLink: inline evidence `SRC Rss1Feed.java:53`
- Rss1Feed.getPubDate: inline evidence `SRC Rss1Feed.java:90`
- Rss1Feed.getType: inline evidence `SRC Rss1Feed.java:41`
- Rss1Item.getAuthor: inline evidence `SRC Rss1Item.java:62`
- Rss1Item.getCategories: inline evidence `SRC Rss1Item.java:83`
- Rss1Item.getType: inline evidence `SRC Rss1Item.java:34`
- Rss2Feed.getCategories: inline evidence `SRC Rss2Feed.java:100`
- Rss2Feed.getCopyright: inline evidence `SRC Rss2Feed.java:82`
- Rss2Feed.getDescription: inline evidence `SRC Rss2Feed.java:68`
- Rss2Feed.getLanguage: inline evidence `SRC Rss2Feed.java:75`

### b002: 36 restored

- Rss2Feed.getLink: inline evidence `SRC Rss2Feed.java:54`
- Rss2Feed.getPubDate: inline evidence `SRC Rss2Feed.java:89`
- Rss2Feed.getType: inline evidence `SRC Rss2Feed.java:42`
- Rss2Item.getAuthor: inline evidence `SRC Rss2Item.java:63`
- Rss2Item.getCategories: inline evidence `SRC Rss2Item.java:81`
- Rss2Item.getType: inline evidence `SRC Rss2Item.java:35`
- MediaRss.getPeerLinks: inline evidence `SRC MediaRss.java:38`
- PeerLink.getHref: inline evidence `SRC PeerLink.java:27`
- PeerLink.getType: inline evidence `SRC PeerLink.java:38`
- NanoHTTPD.<init>(int): inline evidence `SRC NanoHTTPD.java:1544`
- NanoHTTPD.closeAllConnections: inline evidence `SRC NanoHTTPD.java:1566`
- NanoHTTPD.decodeParameters(String): inline evidence `SRC NanoHTTPD.java:1619`
- NanoHTTPD.decodeParameters(Map): inline evidence `SRC NanoHTTPD.java:1604`
- NanoHTTPD.getHostname: inline evidence `SRC NanoHTTPD.java:1675`
- NanoHTTPD.getListeningPort: inline evidence `SRC NanoHTTPD.java:1663`
- NanoHTTPD.getMimeTypeForFile: inline evidence `SRC NanoHTTPD.java:1503`
- NanoHTTPD.getTempFileManagerFactory: inline evidence `SRC NanoHTTPD.java:1678`
- NanoHTTPD.isAlive: inline evidence `SRC NanoHTTPD.java:1666`
- NanoHTTPD.loadMimeTypes: inline evidence `SRC NanoHTTPD.java:1429`
- NanoHTTPD.makeSSLSocketFactory(String,char[]): inline evidence `SRC NanoHTTPD.java:1484`
- NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory): inline evidence `SRC NanoHTTPD.java:1473`
- NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManager[]): inline evidence `SRC NanoHTTPD.java:1455`
- NanoHTTPD.makeSecure: inline evidence `SRC NanoHTTPD.java:1684`
- NanoHTTPD.mimeTypes: inline evidence `SRC NanoHTTPD.java:1418`
- NanoHTTPD.newChunkedResponse: inline evidence `SRC NanoHTTPD.java:1690`
- NanoHTTPD.newFixedLengthResponse(String): inline evidence `SRC NanoHTTPD.java:1719`
- NanoHTTPD.setServerSocketFactory: inline evidence `SRC NanoHTTPD.java:1672`
- NanoHTTPD.wasStarted: inline evidence `SRC NanoHTTPD.java:1848`
- NanoHTTPD$Cookie.<init>(String,String): inline evidence `SRC NanoHTTPD.java:205`
- NanoHTTPD$Cookie.<init>(String,String,int): inline evidence `SRC NanoHTTPD.java:208`
- NanoHTTPD$DefaultAsyncRunner.getRunning: inline evidence `SRC NanoHTTPD.java:315`
- NanoHTTPD$DefaultTempFile.open: inline evidence `SRC NanoHTTPD.java:366`
- NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream): inline evidence `SRC NanoHTTPD.java:479`
- NanoHTTPD$HTTPSession.getCookies: inline evidence `SRC NanoHTTPD.java:817`
- NanoHTTPD$HTTPSession.getInputStream: inline evidence `SRC NanoHTTPD.java:825`
- NanoHTTPD$SecureServerSocketFactory.<init>: inline evidence `SRC NanoHTTPD.java:436`

Not restored: b001 baseAdapters.BR.<init> (INFERRED in both) and b002 libretorrent.BR.<init>, DataBinderMapperImpl$InnerBrLookup.<init>, DataBinderMapperImpl$InnerLayoutIdLookup.<init>, DataBindingTriggerClass.<init> (INFERRED in both, A1 mapper-room evidence).

## 2. Owed greps

73 rows said "Grep owed" (b001: 39, b002: 34). Full-repo fixed-string greps over final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main are saved in scratch/b001_greps/ (39 files) and scratch/b002_greps/ (34 files); summary in scratch/b001b002_greps_summary.md. Every "Grep owed" sentence in the .py and .md reasons now cites its grep file.

49 rows: 0 hits — supports UNREACHABLE.

24 rows: hits, ALL adjudicated as false positives (other-class same-name methods, or other overloads). No label flipped; the flip conditions in the old reason texts were evaluated and none fired:

- b001 row 08 EzRssTorrentItem.isVerified: 1 hits — 1 hit: AnnounceEntry.isVerified() (TrackerInfo.java:162) — other-class method, not EzRssTorrentItem.
- b001 row 09 FeedException.<init>(): 2 hits — 2 hits: (String) ctor at DefaultFeedParser.java:40 and (Throwable) ctor at :45 — other overloads; () ctor has 0 hits.
- b001 row 10 FeedException.<init>(String,Throwable): 2 hits — 2 hits: (String) ctor at DefaultFeedParser.java:40 and (Throwable) ctor at :45 — other overloads; (String,Throwable) ctor has 0 hits.
- b001 row 16 AtomFeed.getDescription: 1 hits — 1 hit: Response.IStatus.getDescription() (NanoHTTPD.java:1192) — other class.
- b001 row 19 AtomFeed.getPubDate: 1 hits — 1 hit: Item.getPubDate() (FeedParser.java:104, loop over Item) — other class (item, not feed).
- b001 row 20 AtomFeed.getType: 16 hits — 16 hits: receivers are Enclosure, Content, FilePriority, Intent, FileManagerNode, Gson TypeToken — no AtomFeed receiver.
- b001 row 23 AtomItem.getType: 16 hits — 16 hits: same set as row 20 — no AtomItem receiver.
- b001 row 24 BaseElement.<init>(String,String): 1 hits — 1 hit: 3-arg call new BaseElement(uri, localName, attributes) (FeedHandler.java:100) — other overload; 2-arg ctor has 0 hits.
- b001 row 26 BaseElement.getName: 36 hits — 36 hits: receivers are File, FileTree, TorrentHandle, TorrentInfo, MutableParams, TagInfo state, MagnetInfo, FileManagerNode — no BaseElement receiver.
- b001 row 29 Rss1Feed.getDescription: 1 hits — 1 hit: Response.IStatus.getDescription() (NanoHTTPD.java:1192) — other class.
- b001 row 32 Rss1Feed.getPubDate: 1 hits — 1 hit: Item.getPubDate() (FeedParser.java:104) — other class.
- b001 row 33 Rss1Feed.getType: 16 hits — 16 hits: same set as row 20 — no Rss1Feed receiver.
- b001 row 36 Rss1Item.getType: 16 hits — 16 hits: same set as row 20 — no Rss1Item receiver.
- b001 row 39 Rss2Feed.getDescription: 1 hits — 1 hit: Response.IStatus.getDescription() (NanoHTTPD.java:1192) — other class.
- b002 row 02 Rss2Feed.getPubDate: 1 hits — 1 hit: Item.getPubDate() (FeedParser.java:104) — other class.
- b002 row 03 Rss2Feed.getType: 16 hits — 16 hits: same set as b001 row 20 — no Rss2Feed receiver.
- b002 row 06 Rss2Item.getType: 16 hits — 16 hits: same set as b001 row 20 — no Rss2Item receiver.
- b002 row 09 PeerLink.getType: 16 hits — 16 hits: same set as b001 row 20 — no PeerLink receiver.
- b002 row 18 NanoHTTPD.isAlive: 2 hits — 2 hits: Thread.isAlive() (NanoHTTPD.java:1667 myThread, Logger.java:74 pendingThread) — other class.
- b002 row 29 NanoHTTPD$Cookie.<init>(String,String): 1 hits — 1 hit: (String,String,String) call at NanoHTTPD.java:284 (getHTTPTime returns String) — other overload; 2-arg ctor has 0 hits.
- b002 row 30 NanoHTTPD$Cookie.<init>(String,String,int): 1 hits — 1 hit: (String,String,String) call at NanoHTTPD.java:284 — other overload; (String,String,int) ctor has 0 hits.
- b002 row 32 NanoHTTPD$DefaultTempFile.open: 8 hits — 8 hits: FileDescriptorWrapper.open("r"/"rw") — other class, not DefaultTempFile.
- b002 row 33 NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream): 1 hits — 1 hit: 4-source-arg ctor call at NanoHTTPD.java:173 (matches :484 ctor) — other overload; row ctor (3 source args + enclosing) has 0 hits.
- b002 row 35 NanoHTTPD$HTTPSession.getInputStream: 3 hits — 3 hits: Socket.getInputStream() (:1346), javadoc (:1392), HttpURLConnection.getInputStream (Utils.java:486) — other classes.

## 3. Build effect (scratch/build_repair_b001b002.txt)

methods 4732, edges 6234 (unchanged), REACHABLE 2120, UNREACHABLE 481, UNRESOLVED 2131, errors 2131 (did not rise), warnings 21 (identical WARN set to b007). Labels confirmed by: INFERRED 4193, SOURCE 539 (+75 vs b007: 39 b001 + 36 b002 restored; the b007 SOURCE count 464 already reflected the b003–b007 downgrades, which are NOT in this repair — flagged to the coordinator as follow-up).

## 4. Harness note

check_part.py now reports exactly 39 (b001) + 36 (b002) confirmed_by mismatch FAILs: part SOURCE vs merge-ready INFERRED. That is the ORDERED consequence of the stronger-evidence rule, not a part defect: no other FAILs remain on either part. The merge-ready files are not edited (they are the batch record; the parts govern at build time).

## 5. CORRECTION - b002 row 10 residual (merger continuation, 2026-11-01)

The repair's "zero 'Grep owed' sentences" check matched the exact phrase "Grep owed" and missed b002 row 10 NanoHTTPD.<init>(int), whose reason said "Full grep still owed for any other construction site." Full-repo fixed-string grep over final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main for `new NanoHTTPD(`: 0 hits. Subclass enumeration (`extends NanoHTTPD`): exactly one subclass, TorrentStreamServer (:51), whose ctor calls super(host, port) at :69 - the 2-arg form only. No 1-arg construction site exists in the app tree. Grep saved as scratch/b002_greps/b002_row10_NanoHTTPD._init_int_.txt; the .py/.md reason now cites it; summary gains the row-10 line. No label/kind/grade change (row stays UNREACHABLE no_trigger_in_app). Totals: 73->74 greps, 49->50 zero-hit rows. Rebuild from the corrected tree is byte-identical to scratch/build_repair_b001b002.txt (methods 4732, edges 6234, R2120/U481/UNRES 2131, errors 2131, warnings 21 identical set, SOURCE 539).
