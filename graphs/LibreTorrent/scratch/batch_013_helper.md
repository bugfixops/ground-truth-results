# LibreTorrent batch 13 helper audit

Membership comes only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv` rows where `batch=13`. The plan query printed exactly 40 rows. Source snippets and call-site search notes are in `scratch/batch_013_helper_printed.txt`.

Labels below are recommendations for the integrator; OPEN means evidence is insufficient to assign a graph label. No graph edits or coverage evidence were used.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `AtomItem.getEzRssTorrentItem` | OPEN | App calls `Item.getEzRssTorrentItem` from `watchTorrentInfoHash` (`FeedParser.java:236-239`), but creation of the AtomItem and its feed-list availability depend on SAX callbacks left OPEN; Atom override returns null (`AtomItem.java:135-138`). |
| 2 | `AtomItem.getGuid` | OPEN | App `watchGuid` calls `Item.getGuid` (`FeedParser.java:254-260`), but the AtomItem route depends on SAX callbacks left OPEN; body at `AtomItem.java:73-77`. |
| 3 | `AtomItem.getLinks` | OPEN | App loop calls `item.getLinks()` (`FeedParser.java:95-98`), but AtomItem creation and feed-list availability depend on SAX callbacks left OPEN; body at `AtomItem.java:46-54`. |
| 4 | `AtomItem.getMediaRss` | OPEN | App `watchMediaContent` calls `Item.getMediaRss` (`FeedParser.java:188-192`), but AtomItem creation/feed-list route depends on SAX callbacks left OPEN; override returns null (`AtomItem.java:126-129`). |
| 5 | `AtomItem.getPubDate` | OPEN | App loop calls `item.getPubDate()` (`FeedParser.java:104-108`), but AtomItem creation and feed-list availability depend on SAX callbacks left OPEN; body at `AtomItem.java:80-83`. |
| 6 | `AtomItem.getTitle` | OPEN | App loop uses `item.getTitle()` (`FeedParser.java:109-112`), but AtomItem creation and feed-list availability depend on SAX callbacks left OPEN; body at `AtomItem.java:39-43`. |
| 7 | `BaseElement.<init>(String,String,Attributes)` | OPEN | Called by `BaseItem` (`BaseItem.java:21-22`) and callback-created elements (`FeedHandler.java:81-101`); every entry route found depends on SAX callback dispatch, which needs AOSP source citation. |
| 8 | `BaseElement.addElement` | OPEN | Called by callback body `FeedHandler.endElement` (`FeedHandler.java:123-127`); callback dispatch is not certified by the printed upload source alone. |
| 9 | `BaseElement.getAttributes` | OPEN | Used by `AtomItem.getLinks` (`AtomItem.java:46-53`), whose caller is present (`FeedParser.java:95-98`), but AtomItem construction/feed-list availability depends on OPEN SAX callbacks. |
| 10 | `BaseElement.getContent` | OPEN | Used by Atom title/guid/pubDate (`AtomItem.java:39-43,73-83`), whose app callers are visible (`FeedParser.java:104,109-110,254-260`), but callback-created item route is OPEN. |
| 11 | `BaseElement.getElement` | OPEN | Used by Atom title/guid/pubDate (`AtomItem.java:40-42,74-76,81-82`); their app callers do not independently establish callback-created items. |
| 12 | `BaseElement.getElementList` | OPEN | Used by Atom `getLinks` (`AtomItem.java:46-49`), whose app caller is visible (`FeedParser.java:95-98`), but item creation/feed-list route is OPEN. |
| 13 | `BaseElement.getUri` | OPEN | EzRSS parser's `isEzRssElement` calls it (`EzRss01Parser.java:118-121`), but invocation depends on an RSS2 item delivered through OPEN SAX callbacks. |
| 14 | `BaseElement.setContent` | OPEN | Invoked only in printed source by callback body `FeedHandler.endElement` (`FeedHandler.java:114-122`); callback dispatch lacks AOSP source evidence. |
| 15 | `BaseItem.<init>` | OPEN | Called by item subclass constructors (`AtomItem.java:30-32`, `Rss2Item.java:30-32`); those item construction paths are inside callback `startElement` (`FeedHandler.java:81-96`), whose dispatch remains unverified. |
| 16 | `BaseItem.equals` | OPEN | Source body and private helper are printed (`BaseItem.java:52-62`); no app call was found in focused caller search, but broader library/framework invocation was not ruled out. |
| 17 | `BaseItem.getUniqueId` | OPEN | Private; only found inside `BaseItem.equals/hashCode` (`BaseItem.java:30-44,56-57,67-68`). Those callers have no established route; keep OPEN. |
| 18 | `BaseItem.hashCode` | OPEN | Source body printed (`BaseItem.java:64-69`); no app call was found in focused search, and framework collection invocation was not ruled out. |
| 19 | `BaseItem.toString` | OPEN | Source body printed (`BaseItem.java:46-50`); no app call was found in focused search, and implicit stringification callers were not ruled out. |
| 20 | `DefaultFeedParser.<init>` | REACHABLE | App `FeedParser` calls `FeedParserFactory.newParser()` (`FeedParser.java:71`); factory returns `new DefaultFeedParser()` (`FeedParserFactory.java:23-25`). |
| 21 | `DefaultFeedParser.parse(InputStream)` | REACHABLE | Same app call chain reaches `.parse(bsStream)` (`FeedParser.java:70-71`); parser declaration/body at `DefaultFeedParser.java:19-47`. |
| 22 | `EzRss01Parser.<init>(Rss2Item)` | OPEN | App's `watchTorrentInfoHash` calls the Item method (`FeedParser.java:236-239`), then RSS2 constructs this parser (`Rss2Item.java:119-120`); RSS2 item route depends on OPEN callbacks. |
| 23 | `EzRss01Parser.isEzRssElement(Element)` | OPEN | Internally called by parser helpers (`EzRss01Parser.java:39-42,118-121`), but parser entry depends on callback-created RSS2 items. |
| 24 | `EzRss01Parser.parse()` | OPEN | Internal delegate is visible (`Rss2Item.java:119-120`), but the RSS2 item caller route depends on OPEN SAX callbacks. |
| 25 | `EzRss01Parser.parseContentLength()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,63-77`); entry parser route is OPEN. |
| 26 | `EzRss01Parser.parseFileName()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,39-45`); entry parser route is OPEN. |
| 27 | `EzRss01Parser.parseInfoHash()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,55-61`); entry parser route is OPEN. |
| 28 | `EzRss01Parser.parseInt(String)` | OPEN | Called from parser helpers (`EzRss01Parser.java:63-103,105-116`); entry parser route is OPEN. |
| 29 | `EzRss01Parser.parseMagnetUri()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,47-53`); entry parser route is OPEN. |
| 30 | `EzRss01Parser.parsePeers()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,87-93`); entry parser route is OPEN. |
| 31 | `EzRss01Parser.parseSeeds()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,79-85`); entry parser route is OPEN. |
| 32 | `EzRss01Parser.parseVerified()` | OPEN | Called internally by `parse()` (`EzRss01Parser.java:26-36,95-103`); entry parser route is OPEN. |
| 33 | `FeedHandler.<init>` | REACHABLE | Direct `new FeedHandler()` in reachable parser body (`DefaultFeedParser.java:34,37`); parser itself is called from app wrapper (`FeedParser.java:71`). |
| 34 | `FeedHandler.characters(char[],int,int)` | OPEN | Registered SAX handler reaches `parser.parse(..., handler)` (`DefaultFeedParser.java:34-37`) and extends `DefaultHandler` (`FeedHandler.java:16`); dispatch claim requires AOSP 8.1 source citation not read here. |
| 35 | `FeedHandler.endDocument()` | OPEN | Same registered callback evidence; AOSP SAX dispatch source is missing from this printed audit. |
| 36 | `FeedHandler.endElement(String,String,String)` | OPEN | Same registered callback evidence; downstream BaseElement mutation remains OPEN pending callback dispatch evidence. |
| 37 | `FeedHandler.getFeed()` | REACHABLE | Directly called after parse in `DefaultFeedParser.parse` (`DefaultFeedParser.java:37-38`), reachable from app wrapper (`FeedParser.java:71`). |
| 38 | `FeedHandler.startDocument()` | OPEN | Same registered callback evidence; AOSP SAX dispatch source not read. |
| 39 | `FeedHandler.startElement(String,String,String,Attributes)` | OPEN | Same registered callback evidence; construction of Atom/RSS items and BaseElements depends on this callback. |
| 40 | `MediaRssParser.<init>(Rss2Item)` | OPEN | The caller chain is visible (`FeedParser.java:188-190`; `Rss2Item.java:113-116`), but Rss2Item construction/feed-list delivery depends on OPEN SAX callbacks. |

The XML parsing route enters through the app `FeedParser` wrapper and factory into `DefaultFeedParser`. The SAX handler is registered explicitly, but its framework callback dispatch remains OPEN because the corrected rule requires printed AOSP 8.1.0_r1 source for framework callback claims. `BaseItem.equals`, `hashCode`, `toString`, and `getUniqueId` also remain OPEN because no app caller was found and indirect collection/stringification behavior was not exhaustively excluded.
