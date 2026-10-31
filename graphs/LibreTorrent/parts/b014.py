# Batch 14 part (com.ernieyu.feedparser impl and mediarss: Rss1Feed, Rss2Feed,
# Rss1Item, Rss2Item, MediaRssParser, Content, Hash). Hand-written edges and
# UNREACHABLE entries only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b014_printed.txt.
#
# Route steps owned by other batches are written here so that the routes of
# batch-14 methods are complete: FeedParser.findDownloadUrl -> watchMediaContent
# and watchGuid, FeedParser.watchMediaContent -> watchMediaHash. If another part
# writes the same edge, the merge keeps one copy.

# FeedHandler creates the RSS feed roots (impl/FeedHandler.java:60-62, 67-69).
e('FeedHandler.startElement', 'Rss1Feed.<init>', 'CALL', 'Create an RSS 1.0 feed for the RDF root element',
  guard='localName equals RDF', cls='explicit', evidence='SRC impl/FeedHandler.java:60-62')
e('FeedHandler.startElement', 'Rss2Feed.<init>', 'CALL', 'Create an RSS 2.0 feed for the rss root element',
  guard='localName equals RSS', cls='explicit', evidence='SRC impl/FeedHandler.java:67-69')

# core/FeedParser.getItems reads item accessors (core/FeedParser.java:95-110).
e('FeedParser.getItems', 'Rss1Item.getLinks', 'CALL', 'Read RSS 1.0 item links',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/Rss1Item.java:45-52')
e('FeedParser.getItems', 'Rss2Item.getLinks', 'CALL', 'Read RSS 2.0 item links',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/Rss2Item.java:46-54')
e('FeedParser.getItems', 'Rss1Item.getTitle', 'CALL', 'Read RSS 1.0 item title',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/Rss1Item.java:39-42')
e('FeedParser.getItems', 'Rss2Item.getTitle', 'CALL', 'Read RSS 2.0 item title',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/Rss2Item.java:40-43')

# findDownloadUrl checks the remaining sources in order (core/FeedParser.java:147-160).
e('FeedParser.findDownloadUrl', 'FeedParser.watchMediaContent', 'CALL', 'Check media:content entries when no enclosure or EzRSS hash matched',
  guard='watchEnclosure and watchTorrentInfoHash returned null', cls='explicit', evidence='SRC core/FeedParser.java:155-157')
e('FeedParser.findDownloadUrl', 'FeedParser.watchGuid', 'CALL', 'Use the item guid when no earlier source matched',
  guard='watchMediaContent returned null', cls='explicit', evidence='SRC core/FeedParser.java:159-160')
e('FeedParser.watchTorrentInfoHash', 'Rss1Item.getEzRssTorrentItem', 'CALL', 'Read EzRSS metadata from an RSS 1.0 item',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:238; impl/Rss1Item.java:120-123')

# watchMediaContent and the media:hash fallback (core/FeedParser.java:188-229).
e('FeedParser.watchMediaContent', 'Rss1Item.getMediaRss', 'CALL', 'Read the media RSS block of an RSS 1.0 item',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/Rss1Item.java:111-114')
e('FeedParser.watchMediaContent', 'Rss2Item.getMediaRss', 'CALL', 'Parse the media RSS block of an RSS 2.0 item',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/Rss2Item.java:113-116')
e('FeedParser.watchMediaContent', 'Content.getUrl', 'CALL', 'Read the URL of a media:content entry',
  guard='content is not null', cls='explicit', evidence='SRC core/FeedParser.java:195-199; mediarss/Content.java:48-50')
e('FeedParser.watchMediaContent', 'Content.getType', 'CALL', 'Read the MIME type of a media:content entry that has a URL',
  guard='content URL is not null', cls='explicit', evidence='SRC core/FeedParser.java:200-202; mediarss/Content.java:59-61')
e('FeedParser.watchMediaContent', 'FeedParser.watchMediaHash', 'CALL', 'Check the media:hash fallback when a URL is null or no content matched',
  guard='content URL is null, or the content list ends without a match', cls='explicit', evidence='SRC core/FeedParser.java:200-201,207')
e('FeedParser.watchMediaHash', 'Hash.getAlgorithm', 'CALL', 'Read the algorithm of a media:hash value',
  guard='hash value is not null', cls='explicit', evidence='SRC core/FeedParser.java:217-224; mediarss/Hash.java:44-46')

# watchGuid reads the guid of the item (core/FeedParser.java:254-260).
e('FeedParser.watchGuid', 'Rss1Item.getGuid', 'CALL', 'Read the RSS 1.0 item identifier used as a fallback URL',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/Rss1Item.java:69-72')
e('FeedParser.watchGuid', 'Rss2Item.getGuid', 'CALL', 'Read the RSS 2.0 item guid used as a fallback URL',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/Rss2Item.java:69-72')

# Rss2Item.getMediaRss runs the Media RSS parser (impl/Rss2Item.java:113-116).
e('Rss2Item.getMediaRss', 'MediaRssParser.<init>', 'CALL', 'Create the Media RSS parser bound to this item',
  cls='explicit', evidence='SRC impl/Rss2Item.java:115; impl/MediaRssParser.java:25-27')
e('Rss2Item.getMediaRss', 'MediaRssParser.parse', 'CALL', 'Parse the media:* elements of this item',
  cls='explicit', evidence='SRC impl/Rss2Item.java:115; impl/MediaRssParser.java:29-38')
e('MediaRssParser.parse', 'MediaRssParser.<init>', 'CALL', 'Create a parser bound to the item',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:31; impl/MediaRssParser.java:25-27')
e('MediaRssParser.parse', 'MediaRssParser.parseContent', 'CALL', 'Parse media:content entries',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:33; impl/MediaRssParser.java:40-56')
e('MediaRssParser.parse', 'MediaRssParser.parseHash', 'CALL', 'Parse the media:hash element',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:34; impl/MediaRssParser.java:58-74')
e('MediaRssParser.parse', 'MediaRssParser.parsePeerLinks', 'CALL', 'Parse media:peerLink entries',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:35; impl/MediaRssParser.java:76-92')
e('MediaRssParser.parseContent', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept only media-namespace media:content elements',
  guard='each media:content element', cls='explicit', evidence='SRC impl/MediaRssParser.java:45; impl/MediaRssParser.java:94-97')
e('MediaRssParser.parseContent', 'Content.<init>', 'CALL', 'Create a Content value for each accepted media:content element',
  guard='element is in the media namespace', cls='explicit', evidence='SRC impl/MediaRssParser.java:52; mediarss/Content.java:36-39')
e('MediaRssParser.parseHash', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept the media:hash element only in the media namespace',
  guard='media:hash element found', cls='explicit', evidence='SRC impl/MediaRssParser.java:60; impl/MediaRssParser.java:94-97')
e('MediaRssParser.parseHash', 'Hash.<init>', 'CALL', 'Create a Hash value from the media:hash text',
  guard='hash text is not null', cls='explicit', evidence='SRC impl/MediaRssParser.java:68; mediarss/Hash.java:21-23')
e('MediaRssParser.parsePeerLinks', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept only media-namespace media:peerLink elements',
  guard='each media:peerLink element', cls='explicit', evidence='SRC impl/MediaRssParser.java:81; impl/MediaRssParser.java:94-97')

# UNREACHABLE: no app or feed-parser path converts these values to text or compares them.
# core/FeedParser.java keeps the Feed in one field and reads only getTitle and getItemList.
_B14_FEED_TEXT = 'No app or feed-parser path converts this Feed to text: core/FeedParser.java keeps the feed in one field and reads only getTitle and getItemList.'
_B14_ITEM_DESCRIPTION = 'Its only caller is BaseItem.getUniqueId, which runs only from BaseItem.equals and hashCode; no app or feed-parser code compares or hashes Item values, and core/FeedParser.java never reads the description.'
_B14_MEDIA_VALUE = 'Content and Hash values are only read through getters in core/FeedParser.java; no app or feed-parser code compares, hashes or converts them to text, and MediaRss has no equals.'
UNREACHABLE.update({
    'Rss1Feed.toString': ('no_trigger_in_app', _B14_FEED_TEXT, 'SRC impl/Rss1Feed.java:118-122; core/FeedParser.java:60,86,92-95', 'SOURCE'),
    'Rss2Feed.toString': ('no_trigger_in_app', _B14_FEED_TEXT, 'SRC impl/Rss2Feed.java:132-136; core/FeedParser.java:60,86,92-95', 'SOURCE'),
    'Rss1Item.getDescription': ('no_trigger_in_app', _B14_ITEM_DESCRIPTION, 'SRC impl/Rss1Item.java:56-59; impl/BaseItem.java:30-44,53-69; core/FeedParser.java:95-110', 'SOURCE'),
    'Rss2Item.getDescription': ('no_trigger_in_app', _B14_ITEM_DESCRIPTION, 'SRC impl/Rss2Item.java:57-60; impl/BaseItem.java:30-44,53-69; core/FeedParser.java:95-110', 'SOURCE'),
    'Content.equals': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:63-73; core/FeedParser.java:194-199', 'SOURCE'),
    'Content.hashCode': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:75-80; core/FeedParser.java:194-199', 'SOURCE'),
    'Content.toString': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:82-89; mediarss/MediaRss.java:44-49', 'SOURCE'),
    'Hash.equals': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Hash.java:54-64; core/FeedParser.java:217-224', 'SOURCE'),
})

# Bytecode auto edges whose caller is an UNREACHABLE batch-14 method above, or
# BaseItem.getUniqueId (its only callers are BaseItem.equals and hashCode, which
# nothing invokes; that label is owned by the BaseItem batch).
SUPPRESS.update({
    ('Rss1Feed.toString', 'Rss1Feed.getTitle'),
    ('Rss2Feed.toString', 'Rss2Feed.getTitle'),
    ('Rss1Item.getDescription', 'BaseElement.getElement'),
    ('Rss1Item.getDescription', 'BaseElement.getContent'),
    ('Rss2Item.getDescription', 'BaseElement.getElement'),
    ('Rss2Item.getDescription', 'BaseElement.getContent'),
    ('BaseItem.getUniqueId', 'Rss1Item.getDescription'),
    ('BaseItem.getUniqueId', 'Rss2Item.getDescription'),
    ('BaseItem.getUniqueId@Rss1Item', 'Rss1Item.getDescription'),
    ('BaseItem.getUniqueId@Rss2Item', 'Rss2Item.getDescription'),
})
