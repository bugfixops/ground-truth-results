# Batch 14 helper report

Membership is exactly the 40 rows with `batch==14` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the exact plan output and source excerpts are in `scratch/batch_014_helper_printed.txt`.

Printed source establishes the parser route: `core.FeedParser.getItems()` reads item fields and, when earlier link candidates are absent, enters `findDownloadUrl`; it then tries enclosure, EZRSS, MediaRSS, and GUID handlers. `Rss2Item.getMediaRss()` constructs `MediaRssParser` and `parse()` unconditionally runs `parseContent`, `parseHash`, and `parsePeerLinks`. Those parsing methods construct Content/Hash values, and the app consumes Content URL/type and Hash algorithm. Rss1/Rss2 feed and item constructors are registered in `FeedHandler` (printed in the batch 12 helper); core FeedParser calls the feed/item methods listed below.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `MediaRssParser.isMediaRssElement` | REACHABLE | — | Called by each MediaRSS parse routine when matching elements are present. | `MediaRssParser.java:40-97` |
| `MediaRssParser.parse` | REACHABLE | — | Called by Rss2Item.getMediaRss on the app's MediaRSS fallback route. | `Rss2Item.java:113-116`; `FeedParser.java:151-157,188-192` |
| `MediaRssParser.parseContent` | REACHABLE | — | Unconditionally invoked by parse; builds Content values for matching media:content elements. | `MediaRssParser.java:29-56` |
| `MediaRssParser.parseHash` | REACHABLE | — | Unconditionally invoked by parse; builds Hash for a matching media:hash element. | `MediaRssParser.java:29-37,58-74` |
| `MediaRssParser.parsePeerLinks` | REACHABLE | — | Unconditionally invoked by parse; processes matching media:peerLink elements. | `MediaRssParser.java:29-37,76-92` |
| `Rss1Feed.<init>` | REACHABLE | — | FeedHandler constructs Rss1Feed for the RDF feed root. | `FeedHandler.java:60-65`; `Rss1Feed.java:36-38` |
| `Rss1Feed.getItemList` | REACHABLE | — | Core FeedParser enumerates parsed feed items. | `FeedParser.java:89-96`; `Rss1Feed.java:103-115` |
| `Rss1Feed.getTitle` | REACHABLE | — | Core FeedParser reads feed title through Feed.getTitle. | `FeedParser.java:84-87`; `Rss1Feed.java:45-50` |
| `Rss1Feed.toString` | UNREACHABLE | no_trigger_in_app | No source parser/app path renders the feed via toString. | `Rss1Feed.java:118-122`; caller search in printed source |
| `Rss1Item.<init>` | REACHABLE | — | FeedHandler constructs Rss1Item for RSS1 item elements. | `FeedHandler.java:81-92`; `Rss1Item.java:29-31` |
| `Rss1Item.getDescription` | UNREACHABLE | no_trigger_in_app | Core FeedParser reads links, title, date, enclosures, MediaRSS, EZRSS, and guid, but not description. | `Rss1Item.java:56-59`; `FeedParser.java:89-110,141-160` |
| `Rss1Item.getEnclosures` | REACHABLE | — | Called by core FeedParser's enclosure fallback. | `FeedParser.java:147,168-176`; `Rss1Item.java:88-105` |
| `Rss1Item.getEzRssTorrentItem` | REACHABLE | — | Called by core FeedParser's EZRSS fallback; Rss1 implementation returns null. | `FeedParser.java:151,236-240`; `Rss1Item.java:120-123` |
| `Rss1Item.getGuid` | REACHABLE | — | Called by core FeedParser's GUID fallback. | `FeedParser.java:159,254-261`; `Rss1Item.java:69-73` |
| `Rss1Item.getLinks` | REACHABLE | — | Core FeedParser reads links for article/download URL selection. | `FeedParser.java:95-102`; `Rss1Item.java:45-53` |
| `Rss1Item.getMediaRss` | REACHABLE | — | Called on the MediaRSS fallback path; Rss1 implementation returns null. | `FeedParser.java:155-157,188-192`; `Rss1Item.java:111-114` |
| `Rss1Item.getPubDate` | REACHABLE | — | Core FeedParser reads item publication date. | `FeedParser.java:104-107`; `Rss1Item.java:75-80` |
| `Rss1Item.getTitle` | REACHABLE | — | Core FeedParser reads each item title. | `FeedParser.java:109-110`; `Rss1Item.java:39-42` |
| `Rss2Feed.<init>` | REACHABLE | — | FeedHandler constructs Rss2Feed for the RSS root. | `FeedHandler.java:67-72`; `Rss2Feed.java:37-39` |
| `Rss2Feed.getItemList` | REACHABLE | — | Core FeedParser enumerates parsed feed items. | `FeedParser.java:89-96`; `Rss2Feed.java:113-129` |
| `Rss2Feed.getTitle` | REACHABLE | — | Core FeedParser reads feed title through Feed.getTitle. | `FeedParser.java:84-87`; `Rss2Feed.java:47-51` |
| `Rss2Feed.toString` | UNREACHABLE | no_trigger_in_app | No source parser/app path renders the feed via toString. | `Rss2Feed.java:132-136`; caller search in printed source |
| `Rss2Item.<init>` | REACHABLE | — | FeedHandler constructs Rss2Item for RSS2 item elements. | `FeedHandler.java:81-92`; `Rss2Item.java:30-32` |
| `Rss2Item.getDescription` | UNREACHABLE | no_trigger_in_app | Core FeedParser does not read item description. | `Rss2Item.java:57-60`; `FeedParser.java:89-110,141-160` |
| `Rss2Item.getEnclosures` | REACHABLE | — | Called by core FeedParser's enclosure fallback. | `FeedParser.java:147,168-176`; `Rss2Item.java:94-111` |
| `Rss2Item.getEzRssTorrentItem` | REACHABLE | — | Called by core FeedParser's EZRSS fallback. | `FeedParser.java:151,236-242`; `Rss2Item.java:118-121` |
| `Rss2Item.getGuid` | REACHABLE | — | Called by core FeedParser's GUID fallback. | `FeedParser.java:159,254-261`; `Rss2Item.java:69-72` |
| `Rss2Item.getLinks` | REACHABLE | — | Core FeedParser reads links for article/download URL selection. | `FeedParser.java:95-102`; `Rss2Item.java:46-54` |
| `Rss2Item.getMediaRss` | REACHABLE | — | Called by core FeedParser; method constructs and runs MediaRssParser. | `FeedParser.java:155-157,188-192`; `Rss2Item.java:113-116` |
| `Rss2Item.getPubDate` | REACHABLE | — | Core FeedParser reads item publication date. | `FeedParser.java:104-107`; `Rss2Item.java:74-78` |
| `Rss2Item.getTitle` | REACHABLE | — | Core FeedParser reads each item title. | `FeedParser.java:109-110`; `Rss2Item.java:40-43` |
| `Content.<init>` | REACHABLE | — | MediaRssParser constructs Content for matching media:content elements. | `MediaRssParser.java:40-53`; `Content.java:36-39` |
| `Content.equals` | UNREACHABLE | no_trigger_in_app | No app/parser path compares Content objects. | `Content.java:63-73`; caller search in printed source |
| `Content.getType` | REACHABLE | — | Core FeedParser checks MediaRSS content MIME type. | `FeedParser.java:194-204`; `Content.java:59-61` |
| `Content.getUrl` | REACHABLE | — | Core FeedParser reads MediaRSS content URL. | `FeedParser.java:194-204`; `Content.java:48-50` |
| `Content.hashCode` | UNREACHABLE | no_trigger_in_app | No app/parser path hashes Content objects. | `Content.java:75-80`; caller search in printed source |
| `Content.toString` | UNREACHABLE | no_trigger_in_app | No app/parser path renders Content via toString. | `Content.java:82-89`; caller search in printed source |
| `Hash.<init>` | REACHABLE | — | MediaRssParser constructs Hash for a matching media:hash element. | `MediaRssParser.java:58-73`; `Hash.java:21-23` |
| `Hash.equals` | UNREACHABLE | no_trigger_in_app | No app/parser path compares Hash objects. | `Hash.java:54-64`; caller search in printed source |
| `Hash.getAlgorithm` | REACHABLE | — | Core FeedParser checks the MediaRSS hash algorithm. | `FeedParser.java:215-226`; `Hash.java:44-46` |

Count: 40 plan rows inspected; 32 REACHABLE; 8 UNREACHABLE (`no_trigger_in_app`); 0 OPEN. No coverage evidence was used.
