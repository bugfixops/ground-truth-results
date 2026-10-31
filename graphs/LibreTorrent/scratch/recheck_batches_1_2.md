# Recheck of batches 1 and 2

Every cited Java declaration/body below was printed and read. Feed-parser candidates were checked against the app parser call path in `core/FeedParser.java:71-105,175-202`, `FeedParserFactory.java:16-27`, `impl/DefaultFeedParser.java:15-43`, and `impl/FeedHandler.java:26-112`; those sources construct/consume the selected feed types but do not call the listed accessors or unused overloads. NanoHTTPD calls were checked against the printed source references and the app subclass; the eight remaining intra-NanoHTTPD callers are logged with their edge IDs in `conflicts.md` and suppressed because those callers have no route. `result` means the cited declaration/body matches and the no-trigger reason holds under those inspected call paths.

| method | cited lines | printed (yes or no) | result |
|---|---|---|---|
| baseAdapters.BR.<init> | scratch/generated_class_grep.txt:1-2 | yes | confirmed; INFERRED (no source declaration in grep) |
| Enclosure.getLength | com/ernieyu/feedparser/Enclosure.java:52 | yes | confirmed |
| EzRssTorrentItem.getContentLength | com/ernieyu/feedparser/EzRssTorrentItem.java:69 | yes | confirmed |
| EzRssTorrentItem.getFileName | com/ernieyu/feedparser/EzRssTorrentItem.java:45 | yes | confirmed |
| EzRssTorrentItem.getMagnetUri | com/ernieyu/feedparser/EzRssTorrentItem.java:53 | yes | confirmed |
| EzRssTorrentItem.getPeers | com/ernieyu/feedparser/EzRssTorrentItem.java:85 | yes | confirmed |
| EzRssTorrentItem.getSeeds | com/ernieyu/feedparser/EzRssTorrentItem.java:77 | yes | confirmed |
| EzRssTorrentItem.isVerified | com/ernieyu/feedparser/EzRssTorrentItem.java:93 | yes | confirmed |
| FeedException.<init>() | com/ernieyu/feedparser/FeedException.java:8 | yes | confirmed |
| FeedException.<init>(String,Throwable) | com/ernieyu/feedparser/FeedException.java:19 | yes | confirmed |
| FeedParserFactory.<init> | com/ernieyu/feedparser/FeedParserFactory.java:16 | yes | confirmed |
| FeedUtils.<init> | com/ernieyu/feedparser/FeedUtils.java:12 | yes | confirmed |
| XML.<init> | com/ernieyu/feedparser/XML.java:7 | yes | confirmed |
| AtomFeed.getCategories | com/ernieyu/feedparser/impl/AtomFeed.java:81 | yes | confirmed |
| AtomFeed.getCopyright | com/ernieyu/feedparser/impl/AtomFeed.java:69 | yes | confirmed |
| AtomFeed.getDescription | com/ernieyu/feedparser/impl/AtomFeed.java:56 | yes | confirmed |
| AtomFeed.getLanguage | com/ernieyu/feedparser/impl/AtomFeed.java:62 | yes | confirmed |
| AtomFeed.getLink | com/ernieyu/feedparser/impl/AtomFeed.java:50 | yes | confirmed |
| AtomFeed.getPubDate | com/ernieyu/feedparser/impl/AtomFeed.java:75 | yes | confirmed |
| AtomFeed.getType | com/ernieyu/feedparser/impl/AtomFeed.java:39 | yes | confirmed |
| AtomItem.getAuthor | com/ernieyu/feedparser/impl/AtomItem.java:64 | yes | confirmed |
| AtomItem.getCategories | com/ernieyu/feedparser/impl/AtomItem.java:86 | yes | confirmed |
| AtomItem.getType | com/ernieyu/feedparser/impl/AtomItem.java:35 | yes | confirmed |
| BaseElement.<init>(String,String) | com/ernieyu/feedparser/impl/BaseElement.java:29 | yes | confirmed |
| BaseElement.getElementKeys | com/ernieyu/feedparser/impl/BaseElement.java:84 | yes | confirmed |
| BaseElement.getName | com/ernieyu/feedparser/impl/BaseElement.java:51 | yes | confirmed |
| Rss1Feed.getCategories | com/ernieyu/feedparser/impl/Rss1Feed.java:98 | yes | confirmed |
| Rss1Feed.getCopyright | com/ernieyu/feedparser/impl/Rss1Feed.java:82 | yes | confirmed |
| Rss1Feed.getDescription | com/ernieyu/feedparser/impl/Rss1Feed.java:67 | yes | confirmed |
| Rss1Feed.getLanguage | com/ernieyu/feedparser/impl/Rss1Feed.java:74 | yes | confirmed |
| Rss1Feed.getLink | com/ernieyu/feedparser/impl/Rss1Feed.java:53 | yes | confirmed |
| Rss1Feed.getPubDate | com/ernieyu/feedparser/impl/Rss1Feed.java:90 | yes | confirmed |
| Rss1Feed.getType | com/ernieyu/feedparser/impl/Rss1Feed.java:41 | yes | confirmed |
| Rss1Item.getAuthor | com/ernieyu/feedparser/impl/Rss1Item.java:62 | yes | confirmed |
| Rss1Item.getCategories | com/ernieyu/feedparser/impl/Rss1Item.java:83 | yes | confirmed |
| Rss1Item.getType | com/ernieyu/feedparser/impl/Rss1Item.java:34 | yes | confirmed |
| Rss2Feed.getCategories | com/ernieyu/feedparser/impl/Rss2Feed.java:100 | yes | confirmed |
| Rss2Feed.getCopyright | com/ernieyu/feedparser/impl/Rss2Feed.java:82 | yes | confirmed |
| Rss2Feed.getDescription | com/ernieyu/feedparser/impl/Rss2Feed.java:68 | yes | confirmed |
| Rss2Feed.getLanguage | com/ernieyu/feedparser/impl/Rss2Feed.java:75 | yes | confirmed |
| Rss2Feed.getLink | com/ernieyu/feedparser/impl/Rss2Feed.java:54 | yes | confirmed |
| Rss2Feed.getPubDate | com/ernieyu/feedparser/impl/Rss2Feed.java:89 | yes | confirmed |
| Rss2Feed.getType | com/ernieyu/feedparser/impl/Rss2Feed.java:42 | yes | confirmed |
| Rss2Item.getAuthor | com/ernieyu/feedparser/impl/Rss2Item.java:63 | yes | confirmed |
| Rss2Item.getCategories | com/ernieyu/feedparser/impl/Rss2Item.java:81 | yes | confirmed |
| Rss2Item.getType | com/ernieyu/feedparser/impl/Rss2Item.java:35 | yes | confirmed |
| MediaRss.getPeerLinks | com/ernieyu/feedparser/mediarss/MediaRss.java:38 | yes | confirmed |
| PeerLink.getHref | com/ernieyu/feedparser/mediarss/PeerLink.java:27 | yes | confirmed |
| PeerLink.getType | com/ernieyu/feedparser/mediarss/PeerLink.java:38 | yes | confirmed |
| NanoHTTPD.<init>(int) | org/nanohttpd/NanoHTTPD.java:1544 | yes | confirmed |
| NanoHTTPD.closeAllConnections | org/nanohttpd/NanoHTTPD.java:1566 | yes | confirmed |
| NanoHTTPD.decodeParameters(String) | org/nanohttpd/NanoHTTPD.java:1619 | yes | confirmed after conflict suppression |
| NanoHTTPD.decodeParameters(Map) | org/nanohttpd/NanoHTTPD.java:1604 | yes | confirmed |
| NanoHTTPD.getHostname | org/nanohttpd/NanoHTTPD.java:1675 | yes | confirmed |
| NanoHTTPD.getListeningPort | org/nanohttpd/NanoHTTPD.java:1663 | yes | confirmed |
| NanoHTTPD.getMimeTypeForFile | org/nanohttpd/NanoHTTPD.java:1503 | yes | confirmed after conflict suppression |
| NanoHTTPD.getTempFileManagerFactory | org/nanohttpd/NanoHTTPD.java:1678 | yes | confirmed |
| NanoHTTPD.isAlive | org/nanohttpd/NanoHTTPD.java:1666 | yes | confirmed |
| NanoHTTPD.loadMimeTypes | org/nanohttpd/NanoHTTPD.java:1429 | yes | confirmed after conflict suppression |
| NanoHTTPD.makeSSLSocketFactory(String,char[]) | org/nanohttpd/NanoHTTPD.java:1484 | yes | confirmed |
| NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory) | org/nanohttpd/NanoHTTPD.java:1473 | yes | confirmed after conflict suppression |
| NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManager[]) | org/nanohttpd/NanoHTTPD.java:1455 | yes | confirmed after conflict suppression |
| NanoHTTPD.makeSecure | org/nanohttpd/NanoHTTPD.java:1684 | yes | confirmed |
| NanoHTTPD.mimeTypes | org/nanohttpd/NanoHTTPD.java:1418 | yes | confirmed after conflict suppression |
| NanoHTTPD.newChunkedResponse | org/nanohttpd/NanoHTTPD.java:1690 | yes | confirmed |
| NanoHTTPD.newFixedLengthResponse(String) | org/nanohttpd/NanoHTTPD.java:1719 | yes | confirmed |
| NanoHTTPD.setServerSocketFactory | org/nanohttpd/NanoHTTPD.java:1672 | yes | confirmed |
| NanoHTTPD.wasStarted | org/nanohttpd/NanoHTTPD.java:1848 | yes | confirmed after conflict suppression |
| NanoHTTPD$Cookie.<init>(String,String) | org/nanohttpd/NanoHTTPD.java:205 | yes | confirmed |
| NanoHTTPD$Cookie.<init>(String,String,int) | org/nanohttpd/NanoHTTPD.java:208 | yes | confirmed after conflict suppression |
| NanoHTTPD$DefaultAsyncRunner.getRunning | org/nanohttpd/NanoHTTPD.java:315 | yes | confirmed |
| NanoHTTPD$DefaultTempFile.open | org/nanohttpd/NanoHTTPD.java:366 | yes | confirmed |
| NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream) | org/nanohttpd/NanoHTTPD.java:479 | yes | confirmed |
| NanoHTTPD$HTTPSession.getCookies | org/nanohttpd/NanoHTTPD.java:817 | yes | confirmed |
| NanoHTTPD$HTTPSession.getInputStream | org/nanohttpd/NanoHTTPD.java:825 | yes | confirmed |
| NanoHTTPD$SecureServerSocketFactory.<init> | org/nanohttpd/NanoHTTPD.java:436 | yes | confirmed after conflict suppression |
| libretorrent.BR.<init> | scratch/generated_class_grep.txt:1-2 | yes | confirmed; INFERRED (no source declaration in grep) |
| libretorrent.DataBinderMapperImpl$InnerBrLookup.<init> | scratch/generated_class_grep.txt:1-2 | yes | confirmed; INFERRED (no source declaration in grep) |
| libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<init> | scratch/generated_class_grep.txt:1-2 | yes | confirmed; INFERRED (no source declaration in grep) |
| DataBindingTriggerClass.<init> | scratch/generated_class_grep.txt:1-2 | yes | confirmed; INFERRED (no source declaration in grep) |
