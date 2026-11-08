# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C01 converter delivery (2026-11-01): base part verified against its authoritative
# batch file with the official harness (base PASS, labels/kinds unchanged).
# DELIVERED harness: FAIL ONLY on the grade upgrades below — check_part.py demands
# part grade == merge-ready grade, and merge-ready grades these keys INFERRED while
# the merger tree grades them SOURCE (see REPORT-b015.md for the (b)/(c) conflict
# note). No other FAILs; labels/kinds unchanged.
# Full-repo greps: parts-staging/grep/15/grep_15_*.txt (one file per UNREACHABLE row).
# STRONGER-EVIDENCE upgrades (grade field only; evidence text unchanged, and every
# upgraded entry already cites SRC lines): the merger tree holds these keys SOURCE
# while the base part graded them INFERRED, so the delivered part records SOURCE to
# avoid repeating the SOURCE 617->578->503 downgrade from the b001/b002 merges:
#   SOURCE (was INFERRED): NanoHTTPD.serve(String,Method,Map,Map,Map)
#   SOURCE (was INFERRED): NanoHTTPD.serve(IHTTPSession)
#   SOURCE (was INFERRED): NanoHTTPD$CookieHandler.delete
#   SOURCE (was INFERRED): NanoHTTPD$CookieHandler.iterator
#   SOURCE (was INFERRED): NanoHTTPD$CookieHandler.read
# Labels/kinds are exactly the base part's (and the batch file's); nothing flipped.

# Batch 15 part (mediarss remainder: Hash, MediaRss, PeerLink; NanoHTTPD
# core, ClientHandler, Cookie, CookieHandler). Hand-written edges,
# UNREACHABLE entries and SUPPRESS strings only. Each evidence string cites
# lines printed in graphs/LibreTorrent/scratch/b015_printed.txt.
#
# Pre-existing routes are NOT repeated here; they are listed with line refs
# in parts/b015.md Dependencies (none: no batch-15 REACHABLE row already has
# an incoming edge in graph_def.py).

# Mediarss trunk: MediaRssParser.parse -> parseContent/parseHash/
# parsePeerLinks; core FeedParser.watchMediaContent/watchMediaHash read the
# parsed MediaRss.
e('FeedParser.watchMediaHash', 'Hash.getValue', 'CALL', 'Read the media hash value',
  cls='explicit', evidence='SRC FeedParser.java:221; com/ernieyu/feedparser/mediarss/Hash.java:32-34')
e('MediaRssParser.parseHash', 'Hash.setAlgorithm', 'CALL', 'Store the hash algorithm attribute',
  guard='algo attribute present', cls='explicit', evidence='SRC com/ernieyu/feedparser/impl/MediaRssParser.java:71; com/ernieyu/feedparser/mediarss/Hash.java:48-52')
e('MediaRssParser.parse', 'MediaRss.<init>', 'CALL', 'Build the parsed media RSS object',
  cls='explicit', evidence='SRC com/ernieyu/feedparser/impl/MediaRssParser.java:37; com/ernieyu/feedparser/mediarss/MediaRss.java:21-28')
e('FeedParser.watchMediaContent', 'MediaRss.getContent', 'CALL', 'Read the media content list',
  cls='explicit', evidence='SRC FeedParser.java:194; com/ernieyu/feedparser/mediarss/MediaRss.java:30-32')
e('FeedParser.watchMediaHash', 'MediaRss.getHash', 'CALL', 'Read the media hash object',
  cls='explicit', evidence='SRC FeedParser.java:217; com/ernieyu/feedparser/mediarss/MediaRss.java:34-36')
e('MediaRssParser.parsePeerLinks', 'PeerLink.<init>', 'CALL', 'Build a peer link for each media peer-link element',
  cls='explicit', evidence='SRC com/ernieyu/feedparser/impl/MediaRssParser.java:88; com/ernieyu/feedparser/mediarss/PeerLink.java:15-18')

# Streaming trunk: TorrentStreamServer construction loads NanoHTTPD and
# calls its 2-arg ctor; TorrentStreamServer.start/stop delegate to
# NanoHTTPD.start/stop; NanoHTTPD.start builds the listener thread.
e('TorrentStreamServer.<init>', 'NanoHTTPD.<clinit>', 'FRAMEWORK', 'JVM class initialization before first NanoHTTPD use',
  cls='non_standard', via='JVM class initialization before first superclass use',
  evidence='INFERRED JVM class initialization; SRC TorrentStreamServer.java:67-69; org/nanohttpd/NanoHTTPD.java:1396-1417')
e('TorrentStreamServer.<init>', 'NanoHTTPD.<init>(String,int)', 'CALL', 'Construct the NanoHTTPD base server with host and port',
  cls='explicit', evidence='SRC TorrentStreamServer.java:67-69; org/nanohttpd/NanoHTTPD.java:1557-1562')
e('NanoHTTPD$ServerRunnable.run', 'NanoHTTPD.createClientHandler', 'CALL', 'Create a client handler for each accepted socket',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1347; org/nanohttpd/NanoHTTPD.java:1579-1580')
e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD.createServerRunnable', 'CALL', 'Create the server runnable for the listener thread',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1816; org/nanohttpd/NanoHTTPD.java:1590-1592')
e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD.decodePercent', 'CALL', 'Decode the request URI percent-escapes',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:514,516; org/nanohttpd/NanoHTTPD.java:1646-1655')
e('NanoHTTPD$HTTPSession.decodeParms', 'NanoHTTPD.decodePercent', 'CALL', 'Decode query parameter names and values',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:648,650; org/nanohttpd/NanoHTTPD.java:1646-1655')
e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD.getServerSocketFactory', 'CALL', 'Read the installed server socket factory',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1814; org/nanohttpd/NanoHTTPD.java:1669-1671')
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long)', 'CALL', 'Build a fixed-length streaming response from a torrent input stream',
  cls='explicit', evidence='SRC TorrentStreamServer.java:209,244; org/nanohttpd/NanoHTTPD.java:1696-1698')
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD.newFixedLengthResponse(IStatus,String,String)', 'CALL', 'Build a fixed-length text error/status response',
  cls='explicit', evidence='SRC TorrentStreamServer.java:127,130,134,196,231,239,256; org/nanohttpd/NanoHTTPD.java:1702-1715')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD.newFixedLengthResponse(IStatus,String,String)', 'CALL', 'Build a fixed-length error response in the catch paths',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:745,749; org/nanohttpd/NanoHTTPD.java:1702-1715')
e('NanoHTTPD.stop', 'NanoHTTPD.safeClose', 'CALL', 'Close the server socket on stop',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1839; org/nanohttpd/NanoHTTPD.java:1511-1527')
e('NanoHTTPD$ClientHandler.close', 'NanoHTTPD.safeClose', 'CALL', 'Close the client input stream and socket',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:164-165; org/nanohttpd/NanoHTTPD.java:1511-1527')
e('NanoHTTPD.<init>(String,int)', 'NanoHTTPD.setAsyncRunner', 'CALL', 'Install the default async runner',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1561; org/nanohttpd/NanoHTTPD.java:1776-1778')
e('NanoHTTPD.<init>(String,int)', 'NanoHTTPD.setTempFileManagerFactory', 'CALL', 'Install the default temp file manager factory',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1560; org/nanohttpd/NanoHTTPD.java:1785-1787')
e('TorrentStreamServer.start', 'NanoHTTPD.start()', 'CALL', 'Start the NanoHTTPD base server',
  cls='explicit', evidence='SRC TorrentStreamServer.java:72-78; org/nanohttpd/NanoHTTPD.java:1794-1795')
e('NanoHTTPD.start()', 'NanoHTTPD.start(int)', 'CALL', 'Start with the default socket read timeout',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1795; org/nanohttpd/NanoHTTPD.java:1800-1801')
e('NanoHTTPD.start(int)', 'NanoHTTPD.start(int,boolean)', 'CALL', 'Start with the daemon flag',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1801; org/nanohttpd/NanoHTTPD.java:1813-1820')
e('TorrentStreamServer.stop', 'NanoHTTPD.stop', 'CALL', 'Stop the NanoHTTPD base server',
  cls='explicit', evidence='SRC TorrentStreamServer.java:81-84; org/nanohttpd/NanoHTTPD.java:1837-1845')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD.useGzipWhenAccepted', 'CALL', 'Decide whether the response may use gzip encoding',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:729; org/nanohttpd/NanoHTTPD.java:1660-1661')
e('NanoHTTPD.createClientHandler', 'NanoHTTPD$ClientHandler.<init>', 'CALL', 'Construct the client handler for an accepted socket',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1580; org/nanohttpd/NanoHTTPD.java:159-162')
e('NanoHTTPD$DefaultAsyncRunner.closeAll', 'NanoHTTPD$ClientHandler.close', 'CALL', 'Close each running client handler on stop',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:322; org/nanohttpd/NanoHTTPD.java:163-166')
e('NanoHTTPD$DefaultAsyncRunner.exec', 'NanoHTTPD$ClientHandler.run', 'FRAMEWORK', 'Run the client handler on its request-processor thread',
  cls='non_standard', via='java.lang.Thread(Runnable).start() calls run()',
  evidence='INFERRED Thread dispatch; SRC org/nanohttpd/NanoHTTPD.java:332-336; org/nanohttpd/NanoHTTPD.java:168-195')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$CookieHandler.<init>', 'CALL', 'Parse the request cookies for this session',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:713; org/nanohttpd/NanoHTTPD.java:233-244')

UNREACHABLE.update({
    'Hash.hashCode': ('no_trigger_in_app',
        'Definition at Hash.java:67-71. No printed caller in the fresh corpus; no hash-based collection use of a Hash is printed.',
        'SRC com/ernieyu/feedparser/mediarss/Hash.java:67-71',
        'INFERRED'),
    'Hash.toString': ('no_trigger_in_app',
        'Definition at Hash.java:75-80. No printed caller in the fresh corpus.',
        'SRC com/ernieyu/feedparser/mediarss/Hash.java:75-80',
        'INFERRED'),
    'MediaRss.toString': ('no_trigger_in_app',
        'Definition at MediaRss.java:44-49. No printed caller in the fresh corpus.',
        'SRC com/ernieyu/feedparser/mediarss/MediaRss.java:44-49',
        'INFERRED'),
    'PeerLink.equals': ('no_trigger_in_app',
        'Definition at PeerLink.java:43-52. No printed caller in the fresh corpus.',
        'SRC com/ernieyu/feedparser/mediarss/PeerLink.java:43-52',
        'INFERRED'),
    'PeerLink.hashCode': ('no_trigger_in_app',
        'Definition at PeerLink.java:55-59. No printed caller in the fresh corpus.',
        'SRC com/ernieyu/feedparser/mediarss/PeerLink.java:55-59',
        'INFERRED'),
    'PeerLink.toString': ('no_trigger_in_app',
        'Definition at PeerLink.java:63-68. No printed caller in the fresh corpus.',
        'SRC com/ernieyu/feedparser/mediarss/PeerLink.java:63-68',
        'INFERRED'),
    'NanoHTTPD.serve(String,Method,Map,Map,Map)': ('no_trigger_in_app',
        'Definition at NanoHTTPD.java:1767-1768 (NOT_FOUND stub). Its only printed caller is base serve(IHTTPSession) at :1746, which TorrentStreamServer overrides and never calls via super; no printed caller of the 5-arg overload itself exists.',
        'SRC org/nanohttpd/NanoHTTPD.java:1767-1768,1732-1746; TorrentStreamServer.java:111-120',
        'SOURCE'),
    'NanoHTTPD.serve(IHTTPSession)': ('no_trigger_in_app',
        'Definition at NanoHTTPD.java:1732-1746. The live dispatch is virtual serve(this) at HTTPSession.execute :720, which resolves to TorrentStreamServer.serve :111; TorrentStreamServer contains no super.serve call, so the base body never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:1732-1746,720; TorrentStreamServer.java:111-120',
        'SOURCE'),
    'NanoHTTPD$Cookie.<init>(String,String,String)': ('no_trigger_in_app',
        'Definition at Cookie.java:213-217. The only printed constructor use is CookieHandler.set(String,String,int) at :284, and set itself has no printed caller (only delete :253 calls it; delete is UNREACHABLE in this batch).',
        'SRC org/nanohttpd/NanoHTTPD.java:213-217,283-285,252-254',
        'INFERRED'),
    'NanoHTTPD$Cookie.getHTTPHeader': ('branch_never_taken',
        'Definition at Cookie.java:218-221. The loop that calls it, CookieHandler.unloadQueue :294-297, does run (HTTPSession.execute :727), but its queue is populated only by set (batch 16 rows 1-2), which has no printed caller in the app path, so the loop body never iterates in the printed app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:218-221,294-297,727',
        'INFERRED'),
    'NanoHTTPD$Cookie.getHTTPTime': ('no_trigger_in_app',
        'Definition at Cookie.java:197-203. Printed callers are Cookie(String,String,int) :211 and CookieHandler.set :284; both are on dead paths (the int ctor is never constructed in printed code; set is uncalled).',
        'SRC org/nanohttpd/NanoHTTPD.java:197-203,211,284',
        'INFERRED'),
    'NanoHTTPD$CookieHandler.delete': ('no_trigger_in_app',
        'Definition at CookieHandler.java:252-254 (set(name, -delete-, -30) at :253). No printed caller in the fresh corpus: TorrentStreamServer and NanoHTTPD contain no delete( call.',
        'SRC org/nanohttpd/NanoHTTPD.java:252-254',
        'SOURCE'),
    'NanoHTTPD$CookieHandler.iterator': ('no_trigger_in_app',
        'Definition at CookieHandler.java:257-259 (cookies.keySet().iterator()). No printed for-each or iterator() call on a CookieHandler in the fresh corpus; unloadQueue iterates the queue list directly, not the handler.',
        'SRC org/nanohttpd/NanoHTTPD.java:257-259,294-297',
        'SOURCE'),
    'NanoHTTPD$CookieHandler.read': ('no_trigger_in_app',
        'Definition at CookieHandler.java:267-269 (cookies.get(name)). No printed caller in the fresh corpus.',
        'SRC org/nanohttpd/NanoHTTPD.java:267-269',
        'SOURCE'),
})

# TorrentStreamServer extends NanoHTTPD and overrides only
# serve(IHTTPSession), so it inherits the 5-arg serve overload: its
# generated copy is suppressed as well. No other batch-15 UNREACHABLE class
# has a subclass in the app source. SUPPRESS also covers the bytecode auto
# edges into these methods, including base serve -> 5-arg serve (:1746),
# base serve -> parseBody (:1737, batch 16), and unloadQueue ->
# Cookie.getHTTPHeader (:296, from the REACHABLE batch-16 unloadQueue).
SUPPRESS.update({
    'Hash.hashCode',
    'Hash.toString',
    'MediaRss.toString',
    'PeerLink.equals',
    'PeerLink.hashCode',
    'PeerLink.toString',
    'NanoHTTPD.serve(String,Method,Map,Map,Map)',
    'NanoHTTPD.serve(String,Method,Map,Map,Map)@TorrentStreamServer',
    'NanoHTTPD.serve(IHTTPSession)',
    'NanoHTTPD$Cookie.<init>(String,String,String)',
    'NanoHTTPD$Cookie.getHTTPHeader',
    'NanoHTTPD$Cookie.getHTTPTime',
    'NanoHTTPD$CookieHandler.delete',
    'NanoHTTPD$CookieHandler.iterator',
    'NanoHTTPD$CookieHandler.read',
})
