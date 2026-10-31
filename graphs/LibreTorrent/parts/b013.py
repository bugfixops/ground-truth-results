# Batch 13 part (com.ernieyu.feedparser impl: FeedHandler, BaseElement, BaseItem,
# AtomItem getters, EzRss01Parser). Hand-written edges, UNREACHABLE entries and
# SUPPRESS strings only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b013_printed.txt.
#
# Routes into batch-13 methods that already exist in graph_def.py and are not
# repeated here: FeedFetcherWorker.fetchChannel -> FeedParser.getItems (2711),
# FeedParser.getItems -> findDownloadUrl (2781), findDownloadUrl -> watchTorrentInfoHash
# (2785), -> watchGuid (3597), -> watchMediaContent (3595), watchTorrentInfoHash ->
# AtomItem.getEzRssTorrentItem (2799) and -> Rss2Item.getEzRssTorrentItem (2801),
# Rss2Item.getEzRssTorrentItem -> EzRss01Parser.<init> / parse (2805, 2807),
# getItems -> AtomItem.getPubDate (2811), FeedParser.<init> -> newParser (2715),
# newParser -> DefaultFeedParser.<init> (2717), FeedParser.<init> -> DefaultFeedParser.parse
# (2719), DefaultFeedParser.parse -> FeedHandler.<init> / startElement / endElement /
# getFeed (2723-2729), FeedHandler.startElement -> AtomItem.<init> (2767),
# watchMediaContent -> Rss2Item.getMediaRss (3605), Rss2Item.getMediaRss ->
# MediaRssParser.<init> (3623).

# SAX callbacks made by the JDK parser for parser.parse(..., handler) (impl/DefaultFeedParser.java:37).
e('DefaultFeedParser.parse', 'FeedHandler.startDocument', 'FRAMEWORK', 'SAX parser sends the start-document event to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:41-45')
e('DefaultFeedParser.parse', 'FeedHandler.characters', 'FRAMEWORK', 'SAX parser sends element text to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:36-39')
e('DefaultFeedParser.parse', 'FeedHandler.endDocument', 'FRAMEWORK', 'SAX parser sends the end-document event to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:47-51')

# FeedHandler builds the element tree (impl/FeedHandler.java:94-131).
e('FeedHandler.startElement', 'BaseElement.<init>(String,String,Attributes)', 'CALL', 'Create a generic XML element for a tag that is not a feed root, item or entry',
  guard='no earlier branch matched localName', cls='explicit',
  evidence='SRC impl/FeedHandler.java:98-100; impl/BaseElement.java:39-43')
e('FeedHandler.endElement', 'BaseElement.setContent', 'CALL', 'Store the collected text in the element that is closing',
  cls='explicit', evidence='SRC impl/FeedHandler.java:115-121; impl/BaseElement.java:68-70')
e('FeedHandler.endElement', 'BaseElement.addElement', 'CALL', 'Add the closed element to its parent element',
  guard='elementStack is not empty after the pop', cls='explicit',
  evidence='SRC impl/FeedHandler.java:124-126; impl/BaseElement.java:91-99')

# Item constructor chain (impl/AtomItem.java:30-32; impl/BaseItem.java:21-23).
e('AtomItem.<init>', 'BaseItem.<init>', 'CALL', 'Pass the entry uri, name and attributes to the item base class',
  cls='explicit', evidence='SRC impl/AtomItem.java:31; impl/BaseItem.java:21-23')
e('BaseItem.<init>', 'BaseElement.<init>(String,String,Attributes)', 'CALL', 'Pass the uri, name and attributes to the element base class',
  cls='explicit', evidence='SRC impl/BaseItem.java:22; impl/BaseElement.java:39-43')

# core/FeedParser.getItems and its watchers read Atom items through the Item interface.
e('FeedParser.getItems', 'AtomItem.getLinks', 'CALL', 'Read Atom entry links',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/AtomItem.java:46-54')
e('FeedParser.getItems', 'AtomItem.getTitle', 'CALL', 'Read the Atom entry title for the feed item',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/AtomItem.java:40-43')
e('FeedParser.watchGuid', 'AtomItem.getGuid', 'CALL', 'Read the Atom entry id used as a fallback URL',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/AtomItem.java:74-77')
e('FeedParser.watchMediaContent', 'AtomItem.getMediaRss', 'CALL', 'Read the media RSS block of an Atom entry (always null)',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/AtomItem.java:127-129')

# Atom getters read child elements through BaseElement (impl/AtomItem.java:41-82).
e('AtomItem.getTitle', 'BaseElement.getElement', 'CALL', 'Find the title child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:41; impl/BaseElement.java:72-76')
e('AtomItem.getTitle', 'BaseElement.getContent', 'CALL', 'Read the title text',
  guard='title element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:42; impl/BaseElement.java:60-63')
e('AtomItem.getLinks', 'BaseElement.getElementList', 'CALL', 'Find all link child elements',
  cls='explicit', evidence='SRC impl/AtomItem.java:48; impl/BaseElement.java:78-81')
e('AtomItem.getLinks', 'BaseElement.getAttributes', 'CALL', 'Read the attributes of each link element',
  cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:50; impl/BaseElement.java:55-58')
e('AtomItem.getGuid', 'BaseElement.getElement', 'CALL', 'Find the id child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:75; impl/BaseElement.java:72-76')
e('AtomItem.getGuid', 'BaseElement.getContent', 'CALL', 'Read the id text',
  guard='id element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:76; impl/BaseElement.java:60-63')
e('AtomItem.getPubDate', 'BaseElement.getElement', 'CALL', 'Find the updated child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:81; impl/BaseElement.java:72-76')
e('AtomItem.getPubDate', 'BaseElement.getContent', 'CALL', 'Read the updated text',
  guard='updated element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:82; impl/BaseElement.java:60-63')

# EzRss01Parser.parse calls each field parser (impl/EzRss01Parser.java:26-33).
e('EzRss01Parser.parse', 'EzRss01Parser.parseFileName', 'CALL', 'Read the EzRSS file name',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:27')
e('EzRss01Parser.parse', 'EzRss01Parser.parseMagnetUri', 'CALL', 'Read the EzRSS magnet URI',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:28')
e('EzRss01Parser.parse', 'EzRss01Parser.parseInfoHash', 'CALL', 'Read the EzRSS info hash',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:29')
e('EzRss01Parser.parse', 'EzRss01Parser.parseContentLength', 'CALL', 'Read the EzRSS content length',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:30')
e('EzRss01Parser.parse', 'EzRss01Parser.parseSeeds', 'CALL', 'Read the EzRSS seed count',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:31')
e('EzRss01Parser.parse', 'EzRss01Parser.parsePeers', 'CALL', 'Read the EzRSS peer count',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:32')
e('EzRss01Parser.parse', 'EzRss01Parser.parseVerified', 'CALL', 'Read the EzRSS verified flag',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:33')

# Each field parser reads its child element from the item (impl/EzRss01Parser.java:39-103).
e('EzRss01Parser.parseFileName', 'BaseElement.getElement', 'CALL', 'Find the fileName child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:40; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseMagnetUri', 'BaseElement.getElement', 'CALL', 'Find the magnetURI child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:48; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseInfoHash', 'BaseElement.getElement', 'CALL', 'Find the infoHash child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:56; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseContentLength', 'BaseElement.getElement', 'CALL', 'Find the contentLength child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:64; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseSeeds', 'BaseElement.getElement', 'CALL', 'Find the seeds child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:80; impl/BaseElement.java:72-76')
e('EzRss01Parser.parsePeers', 'BaseElement.getElement', 'CALL', 'Find the peers child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:88; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseVerified', 'BaseElement.getElement', 'CALL', 'Find the verified child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:96; impl/BaseElement.java:72-76')

e('EzRss01Parser.parseFileName', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the fileName element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:41; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseMagnetUri', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the magnetURI element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:49; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseInfoHash', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the infoHash element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:57; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseContentLength', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the contentLength element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:65; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseSeeds', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the seeds element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:81; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parsePeers', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the peers element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:89; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseVerified', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the verified element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:97; impl/EzRss01Parser.java:118-121')

e('EzRss01Parser.parseFileName', 'BaseElement.getContent', 'CALL', 'Read the fileName text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:44; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseMagnetUri', 'BaseElement.getContent', 'CALL', 'Read the magnetURI text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:52; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseInfoHash', 'BaseElement.getContent', 'CALL', 'Read the infoHash text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:60; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseContentLength', 'BaseElement.getContent', 'CALL', 'Read the contentLength text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:70; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseSeeds', 'BaseElement.getContent', 'CALL', 'Read the seeds text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:84; impl/BaseElement.java:60-63')
e('EzRss01Parser.parsePeers', 'BaseElement.getContent', 'CALL', 'Read the peers text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:92; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseVerified', 'BaseElement.getContent', 'CALL', 'Read the verified text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:100; impl/BaseElement.java:60-63')

e('EzRss01Parser.parseSeeds', 'EzRss01Parser.parseInt', 'CALL', 'Convert the seeds text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:84; impl/EzRss01Parser.java:105-116')
e('EzRss01Parser.parsePeers', 'EzRss01Parser.parseInt', 'CALL', 'Convert the peers text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:92; impl/EzRss01Parser.java:105-116')
e('EzRss01Parser.parseVerified', 'EzRss01Parser.parseInt', 'CALL', 'Convert the verified text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:100; impl/EzRss01Parser.java:105-116')

# isEzRssElement reads the namespace uri of the element (impl/EzRss01Parser.java:118-121).
e('EzRss01Parser.isEzRssElement', 'BaseElement.getUri', 'CALL', 'Read the namespace uri of the element',
  cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:119-120; impl/BaseElement.java:45-48')

# Items with no trigger in the app: nothing compares, hashes or converts an Item to text
# (core/FeedParser.java iterates the feed and reads accessors; the feed-parser package and
# service/FeedFetcherWorker.java have no equals, hashCode or toString use on an Item).
UNREACHABLE.update({
    'BaseItem.equals': ('no_trigger_in_app',
        'No app or feed-parser code calls equals on an Item. core/FeedParser.java only iterates getItemList() and reads accessors; its equals calls (lines 176, 203) compare Strings; FeedFetcherWorker removeIf calls (lines 193, 203) compare app FeedItem records.',
        'SRC impl/BaseItem.java:53-62; core/FeedParser.java:89-111,176,203; service/FeedFetcherWorker.java:193,203',
        'SOURCE'),
    'BaseItem.getUniqueId': ('no_trigger_in_app',
        'Private. Its only callers are BaseItem.equals and BaseItem.hashCode, and neither is invoked.',
        'SRC impl/BaseItem.java:30-44 (callers at 56-57 and 67)',
        'SOURCE'),
    'BaseItem.hashCode': ('no_trigger_in_app',
        'No app or feed-parser code hashes an Item. The only hashed collection in the package is BaseElement.elementMap with String keys, and core/FeedParser.java keeps items in a List.',
        'SRC impl/BaseItem.java:64-69; impl/BaseElement.java:23; core/FeedParser.java:95',
        'SOURCE'),
    'BaseItem.toString': ('no_trigger_in_app',
        'No app or feed-parser code converts an Item to text. No string concatenation or log call in core/FeedParser.java or the feed-parser package takes an Item value; the one concatenating log call in FeedFetcherWorker (line 255) does not use an item.',
        'SRC impl/BaseItem.java:48-50; service/FeedFetcherWorker.java:255',
        'SOURCE'),
})

# Suppress bytecode auto edges into and out of the four UNREACHABLE methods and their
# generated copies (tools/build_graph.py add_auto_edges checks src and dst against SUPPRESS).
SUPPRESS.update({
    'BaseItem.equals', 'BaseItem.equals@AtomItem', 'BaseItem.equals@Rss1Item', 'BaseItem.equals@Rss2Item',
    'BaseItem.hashCode', 'BaseItem.hashCode@AtomItem', 'BaseItem.hashCode@Rss1Item', 'BaseItem.hashCode@Rss2Item',
    'BaseItem.toString', 'BaseItem.toString@AtomItem', 'BaseItem.toString@Rss1Item', 'BaseItem.toString@Rss2Item',
    'BaseItem.getUniqueId', 'BaseItem.getUniqueId@AtomItem', 'BaseItem.getUniqueId@Rss1Item', 'BaseItem.getUniqueId@Rss2Item',
})
