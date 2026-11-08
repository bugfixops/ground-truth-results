# Batch 13 source audit

Membership: the 40 rows in `batch_013_plan.txt`, extracted from the sole membership source `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. Printed source evidence and caller searches are in `batch_013_helper_printed.txt`.

Independent integration decision: all 40 remain OPEN. The two helper REACHABLE recommendations (`DefaultFeedParser.<init>` and `DefaultFeedParser.parse`) have source-local callers from `FeedParserFactory` and the app wrapper, but the complete route from a graph entry point is not represented by hand-written edges. `FeedHandler.getFeed` has an explicit source caller only after SAX parsing; its full app route likewise depends on the not-yet-certified parser callback path. Callback methods and callback-dependent objects remain OPEN because their framework dispatch is not supported by printed AOSP source in this audit. The helper itself retains OPEN for remaining indirect collection/stringification uncertainty. No coverage evidence was used.

| # | Method | Label | Reason / printed evidence |
|---:|---|---|---|
| 1 | `AtomItem.getEzRssTorrentItem` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 2 | `AtomItem.getGuid` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 3 | `AtomItem.getLinks` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 4 | `AtomItem.getMediaRss` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 5 | `AtomItem.getPubDate` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 6 | `AtomItem.getTitle` | OPEN | App call exists; AtomItem delivery depends on OPEN SAX callback route. `batch_013_helper_printed.txt` |
| 7 | `BaseElement.<init>(String,String,Attributes)` | OPEN | Downstream of callback-created objects or constructors whose full route is OPEN. `BaseElement.java:39-42`; `FeedHandler.java:81-101` |
| 8 | `BaseElement.addElement` | OPEN | Called by `FeedHandler.endElement`; framework callback dispatch is not certified. `FeedHandler.java:110-127` |
| 9 | `BaseElement.getAttributes` | OPEN | Called through AtomItem getter, whose callback-created object route is OPEN. `AtomItem.java:46-53` |
| 10 | `BaseElement.getContent` | OPEN | Called by AtomItem getters, whose callback-created object route is OPEN. `AtomItem.java:39-43,73-83` |
| 11 | `BaseElement.getElement` | OPEN | Called by AtomItem getters, whose callback-created object route is OPEN. `AtomItem.java:40-42,74-82` |
| 12 | `BaseElement.getElementList` | OPEN | Called by AtomItem getter; callback-created object route is OPEN. `AtomItem.java:46-49` |
| 13 | `BaseElement.getUri` | OPEN | Only downstream of EzRSS parsing on callback-created RSS2 items. `EzRss01Parser.java:118-121` |
| 14 | `BaseElement.setContent` | OPEN | Called in `FeedHandler.endElement`; framework callback dispatch is not certified. `FeedHandler.java:110-122` |
| 15 | `BaseItem.<init>` | OPEN | Called by item subclass constructors reached in callback body; dispatch unverified. `BaseItem.java:21-22`; `FeedHandler.java:81-96` |
| 16 | `BaseItem.equals` | OPEN | No app caller found; broader indirect calls not ruled out. `BaseItem.java:52-62`; helper search in `batch_013_helper_printed.txt` |
| 17 | `BaseItem.getUniqueId` | OPEN | Only called by equals/hashCode, whose trigger remains unresolved. `BaseItem.java:30-44,56-57,67-68` |
| 18 | `BaseItem.hashCode` | OPEN | No app caller found; collection dispatch not ruled out. `BaseItem.java:64-69` |
| 19 | `BaseItem.toString` | OPEN | No app caller found; implicit stringification not ruled out. `BaseItem.java:46-50` |
| 20 | `DefaultFeedParser.<init>` | OPEN | Factory constructs it, but complete app entry route is not handwritten. `FeedParserFactory.java:23-25`; `core/FeedParser.java:71` |
| 21 | `DefaultFeedParser.parse(InputStream)` | OPEN | App wrapper calls it, but complete app entry route is not handwritten. `core/FeedParser.java:70-71`; `DefaultFeedParser.java:22-47` |
| 22 | `EzRss01Parser.<init>(Rss2Item)` | OPEN | Downstream of callback-created RSS2 item; route remains OPEN. `Rss2Item.java:119-120` |
| 23 | `EzRss01Parser.isEzRssElement(Element)` | OPEN | Called by parser helpers, whose RSS2 item route remains OPEN. `EzRss01Parser.java:39-42,118-121` |
| 24 | `EzRss01Parser.parse` | OPEN | Called by RSS2 item getter; RSS2 item route remains OPEN. `Rss2Item.java:119-120`; `EzRss01Parser.java:26-36` |
| 25 | `EzRss01Parser.parseContentLength` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,63-77` |
| 26 | `EzRss01Parser.parseFileName` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,39-45` |
| 27 | `EzRss01Parser.parseInfoHash` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,55-61` |
| 28 | `EzRss01Parser.parseInt(String)` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:63-103,105-116` |
| 29 | `EzRss01Parser.parseMagnetUri` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,47-53` |
| 30 | `EzRss01Parser.parsePeers` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,87-93` |
| 31 | `EzRss01Parser.parseSeeds` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,79-85` |
| 32 | `EzRss01Parser.parseVerified` | OPEN | Internal parser call, with parser entry route OPEN. `EzRss01Parser.java:26-36,95-103` |
| 33 | `FeedHandler.<init>` | OPEN | Explicit parser construction exists, but complete app entry route is not handwritten. `DefaultFeedParser.java:34,37`; `core/FeedParser.java:71` |
| 34 | `FeedHandler.characters(char[],int,int)` | OPEN | SAX callback dispatch lacks printed AOSP source. `DefaultFeedParser.java:34-37`; `FeedHandler.java:36-38` |
| 35 | `FeedHandler.endDocument` | OPEN | SAX callback dispatch lacks printed AOSP source. `DefaultFeedParser.java:34-37`; `FeedHandler.java:48-49` |
| 36 | `FeedHandler.endElement(String,String,String)` | OPEN | SAX callback dispatch lacks printed AOSP source. `FeedHandler.java:110-127` |
| 37 | `FeedHandler.getFeed` | OPEN | Explicit post-parse call exists; complete app entry route is not handwritten. `DefaultFeedParser.java:37-38`; `core/FeedParser.java:71` |
| 38 | `FeedHandler.startDocument` | OPEN | SAX callback dispatch lacks printed AOSP source. `DefaultFeedParser.java:34-37`; `FeedHandler.java:42-44` |
| 39 | `FeedHandler.startElement(String,String,String,Attributes)` | OPEN | SAX callback dispatch lacks printed AOSP source. `DefaultFeedParser.java:34-37`; `FeedHandler.java:54-103` |
| 40 | `MediaRssParser.<init>(Rss2Item)` | OPEN | Downstream of callback-created RSS2 item; route remains OPEN. `Rss2Item.java:114-115` |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No graph labels or edges were added in this batch.
