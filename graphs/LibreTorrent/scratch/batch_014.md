# Batch 14 source audit

Membership is the 40 rows in `batch_014_plan.txt`; printed parser source and helper caller audit are in `batch_014_helper_printed.txt`, with independent targeted prints/search in `batch_014_independent_printed.txt`.

I independently confirmed the parser's local MediaRSS and RSS1/RSS2 call paths. The complete path into callback-created feeds/items is still OPEN because SAX dispatch is not yet evidenced by printed AOSP source, and complete entry routes have not been hand-written in graph_def.py. Eight methods have no caller in the app/bundled parser source and are labeled UNREACHABLE `no_trigger_in_app`.

| Method | Label | Reason / evidence |
|---|---|---|
| `MediaRssParser.isMediaRssElement` | OPEN | Internal parser call; enclosing route depends on callback-created RSS2 item. `MediaRssParser.java:40-97` |
| `MediaRssParser.parse` | OPEN | Called by `Rss2Item.getMediaRss`; complete item route remains OPEN. `Rss2Item.java:113-116`; `FeedParser.java:151-157,188-192` |
| `MediaRssParser.parseContent` | OPEN | Internal call from parse; callback-created item route remains OPEN. `MediaRssParser.java:29-56` |
| `MediaRssParser.parseHash` | OPEN | Internal call from parse; callback-created item route remains OPEN. `MediaRssParser.java:29-37,58-74` |
| `MediaRssParser.parsePeerLinks` | OPEN | Internal call from parse; callback-created item route remains OPEN. `MediaRssParser.java:29-37,76-92` |
| `Rss1Feed.<init>` | OPEN | Constructed in FeedHandler callback body; callback dispatch unverified. `FeedHandler.java:60-65`; `Rss1Feed.java:36-38` |
| `Rss1Feed.getItemList` | OPEN | Core parser calls it; feed callback route remains OPEN. `FeedParser.java:89-96`; `Rss1Feed.java:103-115` |
| `Rss1Feed.getTitle` | OPEN | Core parser calls it; feed callback route remains OPEN. `FeedParser.java:84-87`; `Rss1Feed.java:45-50` |
| `Rss1Feed.toString` | UNREACHABLE | no_trigger_in_app. `Rss1Feed.java:118-122`; `batch_014_helper_printed.txt` |
| `Rss1Item.<init>` | OPEN | Constructed in FeedHandler callback body; callback dispatch unverified. `FeedHandler.java:81-92`; `Rss1Item.java:29-31` |
| `Rss1Item.getDescription` | UNREACHABLE | no_trigger_in_app; core parser consumes other item fields. `Rss1Item.java:56-59`; `FeedParser.java:89-160` |
| `Rss1Item.getEnclosures` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:147,168-176`; `Rss1Item.java:88-105` |
| `Rss1Item.getEzRssTorrentItem` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:151,236-240`; `Rss1Item.java:120-123` |
| `Rss1Item.getGuid` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:159,254-261`; `Rss1Item.java:69-73` |
| `Rss1Item.getLinks` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:95-102`; `Rss1Item.java:45-53` |
| `Rss1Item.getMediaRss` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:155-157,188-192`; `Rss1Item.java:111-114` |
| `Rss1Item.getPubDate` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:104-107`; `Rss1Item.java:75-80` |
| `Rss1Item.getTitle` | OPEN | Core parser calls it; RSS1 item callback route remains OPEN. `FeedParser.java:109-110`; `Rss1Item.java:39-42` |
| `Rss2Feed.<init>` | OPEN | Constructed in FeedHandler callback body; callback dispatch unverified. `FeedHandler.java:67-72`; `Rss2Feed.java:37-39` |
| `Rss2Feed.getItemList` | OPEN | Core parser calls it; feed callback route remains OPEN. `FeedParser.java:89-96`; `Rss2Feed.java:113-129` |
| `Rss2Feed.getTitle` | OPEN | Core parser calls it; feed callback route remains OPEN. `FeedParser.java:84-87`; `Rss2Feed.java:47-51` |
| `Rss2Feed.toString` | UNREACHABLE | no_trigger_in_app. `Rss2Feed.java:132-136`; `batch_014_helper_printed.txt` |
| `Rss2Item.<init>` | OPEN | Constructed in FeedHandler callback body; callback dispatch unverified. `FeedHandler.java:81-92`; `Rss2Item.java:30-32` |
| `Rss2Item.getDescription` | UNREACHABLE | no_trigger_in_app; core parser consumes other item fields. `Rss2Item.java:57-60`; `FeedParser.java:89-160` |
| `Rss2Item.getEnclosures` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:147,168-176`; `Rss2Item.java:94-111` |
| `Rss2Item.getEzRssTorrentItem` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:151,236-242`; `Rss2Item.java:118-121` |
| `Rss2Item.getGuid` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:159,254-261`; `Rss2Item.java:69-72` |
| `Rss2Item.getLinks` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:95-102`; `Rss2Item.java:46-54` |
| `Rss2Item.getMediaRss` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:155-157,188-192`; `Rss2Item.java:113-116` |
| `Rss2Item.getPubDate` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:104-107`; `Rss2Item.java:74-78` |
| `Rss2Item.getTitle` | OPEN | Core parser calls it; RSS2 item callback route remains OPEN. `FeedParser.java:109-110`; `Rss2Item.java:40-43` |
| `Content.<init>` | OPEN | Constructed in MediaRssParser, whose entry route remains OPEN. `MediaRssParser.java:40-53`; `Content.java:36-39` |
| `Content.equals` | UNREACHABLE | no_trigger_in_app. `Content.java:63-73`; caller audit in `batch_014_helper_printed.txt` |
| `Content.getType` | OPEN | Core parser calls it; callback-created RSS2 item route remains OPEN. `FeedParser.java:194-204`; `Content.java:59-61` |
| `Content.getUrl` | OPEN | Core parser calls it; callback-created RSS2 item route remains OPEN. `FeedParser.java:194-204`; `Content.java:48-50` |
| `Content.hashCode` | UNREACHABLE | no_trigger_in_app. `Content.java:75-80`; caller audit in `batch_014_helper_printed.txt` |
| `Content.toString` | UNREACHABLE | no_trigger_in_app. `Content.java:82-89`; caller audit in `batch_014_helper_printed.txt` |
| `Hash.<init>` | OPEN | Constructed in MediaRssParser, whose entry route remains OPEN. `MediaRssParser.java:58-73`; `Hash.java:21-23` |
| `Hash.equals` | UNREACHABLE | no_trigger_in_app. `Hash.java:54-64`; caller audit in `batch_014_helper_printed.txt` |
| `Hash.getAlgorithm` | OPEN | Core parser calls it; callback-created RSS2 item route remains OPEN. `FeedParser.java:215-226`; `Hash.java:44-46` |

Count: 40 plan rows; 0 REACHABLE; 8 `UNREACHABLE/no_trigger_in_app`; 32 OPEN. No coverage evidence was used.
