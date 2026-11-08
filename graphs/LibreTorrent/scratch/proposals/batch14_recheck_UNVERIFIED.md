# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 14 — RE-CHECK, proposed part only, NOT verified, NOT merged

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. No token, no clone, no push by this helper.
Membership: batch 14 = exactly 40 rows in handoff/LIBRETORRENT_BATCH_PLAN.tsv, all TODO_CANDIDATE_REACHABLE (candidates, not evidence), as listed in ~/workspace/wp1_batch14/batch14_list.txt.
Source printed in this session from local copies of the connector-fetched files in ~/workspace/wp1_batch14/src (MediaRssParser, Rss1Feed, Rss1Item, Rss2Feed, Rss2Item, Content, Hash, MediaRss, FeedHandler, DefaultFeedParser, BaseItem, BaseElement, CoreFeedParser, FeedFetcherWorker, Scheduler). No tool coverage, old generated graphs, or build REACHABLE counts used as evidence. confirmed_by SOURCE where lines printed, INFERRED where framework/library dispatch mechanics were not printed. Never DYN, FW-MEMORY, UNVERIFIED.

## Dispatch-standard resolution (this is what moves 32 rows from OPEN to REACHABLE)

Previous batch 14 proposal left the chain OPEN because WorkManager and SAX dispatch were unprinted. That is now resolved as a standard-registration route, consistent with batch 13:
- Scheduler.runPeriodicalRefreshFeeds (Scheduler.java:112-125) builds a PeriodicWorkRequest for FeedFetcherWorker.class and calls WorkManager.getInstance(appContext).enqueueUniquePeriodicWork(...) — the worker is registered by that enqueue, so FeedFetcherWorker.doWork is a standard framework callback, with only the WorkManager internal dispatch mechanics INFERRED.
- DefaultFeedParser:34 creates new FeedHandler(), :37 calls parser.parse(..., handler), :38 calls handler.getFeed() — the SAX handler is registered explicitly, so FeedHandler.startElement/endElement/characters are standard callbacks, with only SAX internal dispatch mechanics INFERRED.
- FeedFetcherWorker: parser = new FeedParser(...), parser.getItems(), parser.getTitle() when channel name is empty — printed in FeedFetcherWorker.java.
- Core FeedParser:71 FeedParserFactory.newParser().parse, :86 feed.getTitle(), :95 feed.getItemList(), :96 item.getLinks(), :104 item.getPubDate(), :110 item.getTitle(), :170 item.getEnclosures(), :190 item.getMediaRss(), :238 item.getEzRssTorrentItem(), :256 item.getGuid().

Therefore a chain method with a printed local caller/constructor/interface dispatch on this trunk is REACHABLE, not OPEN. A method with no printed caller at all, and no printed hash/concatenation/log use, is proposed UNREACHABLE, pending a real full-repo grep — connector search_code 0/incomplete is NOT evidence of absence, and no such grep is claimed here.

## Counts judged in this session

- Judged: 40 / 40. REACHABLE proposed: 32. UNREACHABLE proposed: 8, all no_trigger_in_app, all INFERRED, all pending full-repo grep. OPEN: 0.
- This agrees in UNREACHABLE count with the AGENT_NOTES prior claim (8 UNREACHABLE), but for a corrected reason on getDescription (see below), and disagrees with the prior claim that the other 32 were OPEN: they are now REACHABLE on the standard-registration trunk above.

## Per-method table

| # | Method | Label | Kind / confirmed_by | Printed citations |
|---|---|---|---|---|
| 1 | MediaRssParser.isMediaRssElement | REACHABLE | SOURCE | Def MediaRssParser.java:94-97; called :45, :60, :81 from parseContent/parseHash/parsePeerLinks |
| 2 | MediaRssParser.parse | REACHABLE | SOURCE | Def :29-38, calls parseContent :33, parseHash :34, parsePeerLinks :35; called Rss2Item.java:115 via new MediaRssParser(this).parse() |
| 3 | MediaRssParser.parseContent | REACHABLE | SOURCE | Def :40-56; called :33 from parse; constructs new Content :52 |
| 4 | MediaRssParser.parseHash | REACHABLE | SOURCE | Def :58-74; called :34 from parse; constructs new Hash :68 |
| 5 | MediaRssParser.parsePeerLinks | REACHABLE | SOURCE | Def :76-92; called :35 from parse |
| 6 | Rss1Feed.<init> | REACHABLE | SOURCE | Def Rss1Feed.java:36-38; constructed FeedHandler.java:62 for rdf |
| 7 | Rss1Feed.getItemList | REACHABLE | SOURCE | Def Rss1Feed.java:103-115; interface dispatch CoreFeedParser.java:95 |
| 8 | Rss1Feed.getTitle | REACHABLE | SOURCE | Def Rss1Feed.java:46-50; interface dispatch CoreFeedParser.java:86 |
| 9 | Rss1Feed.toString | UNREACHABLE | no_trigger_in_app / INFERRED | Def Rss1Feed.java:120-122; no call, concatenation, or log on a feed in printed files. Pending full-repo grep. |
| 10 | Rss1Item.<init> | REACHABLE | SOURCE | Def Rss1Item.java:29-31; constructed FeedHandler.java:85 for RSS_1_0 item |
| 11 | Rss1Item.getDescription | UNREACHABLE | no_trigger_in_app / INFERRED | Def Rss1Item.java:56-59; only printed caller path is BaseItem.getUniqueId:41, called by BaseItem.equals:56-57 and hashCode:67, which are themselves proposed UNREACHABLE in batch 13, pending the same grep. If that grep finds a trigger for equals/hashCode, this flips to REACHABLE with them. Do NOT treat BaseItem.equals as a reachable caller on current evidence. |
| 12 | Rss1Item.getEnclosures | REACHABLE | SOURCE | Def Rss1Item.java:88-105; interface dispatch CoreFeedParser.java:170 |
| 13 | Rss1Item.getEzRssTorrentItem | REACHABLE | SOURCE | Def Rss1Item.java:121-123 returns null; interface dispatch CoreFeedParser.java:238; returning null is not unreachability |
| 14 | Rss1Item.getGuid | REACHABLE | SOURCE | Def Rss1Item.java:69-73; interface dispatch CoreFeedParser.java:256 |
| 15 | Rss1Item.getLinks | REACHABLE | SOURCE | Def Rss1Item.java:45-53; interface dispatch CoreFeedParser.java:96 |
| 16 | Rss1Item.getMediaRss | REACHABLE | SOURCE | Def Rss1Item.java:112-114 returns null; interface dispatch CoreFeedParser.java:190 |
| 17 | Rss1Item.getPubDate | REACHABLE | SOURCE | Def Rss1Item.java:76-80; interface dispatch CoreFeedParser.java:104 |
| 18 | Rss1Item.getTitle | REACHABLE | SOURCE | Def Rss1Item.java:39-42; interface dispatch CoreFeedParser.java:110 |
| 19 | Rss2Feed.<init> | REACHABLE | SOURCE | Def Rss2Feed.java:37-39; constructed FeedHandler.java:69 for rss |
| 20 | Rss2Feed.getItemList | REACHABLE | SOURCE | Def Rss2Feed.java:113-129; interface dispatch CoreFeedParser.java:95 |
| 21 | Rss2Feed.getTitle | REACHABLE | SOURCE | Def Rss2Feed.java:47-51; interface dispatch CoreFeedParser.java:86 |
| 22 | Rss2Feed.toString | UNREACHABLE | no_trigger_in_app / INFERRED | Def Rss2Feed.java:134-136; no call in printed files. Pending full-repo grep. |
| 23 | Rss2Item.<init> | REACHABLE | SOURCE | Def Rss2Item.java:30-32; constructed FeedHandler.java:88 for RSS_2_0 item |
| 24 | Rss2Item.getDescription | UNREACHABLE | no_trigger_in_app / INFERRED | Def Rss2Item.java:57-60; same BaseItem.getUniqueId/equals/hashCode path as #11, pending the same grep. Flips with equals/hashCode. |
| 25 | Rss2Item.getEnclosures | REACHABLE | SOURCE | Def Rss2Item.java:94-111; interface dispatch CoreFeedParser.java:170 |
| 26 | Rss2Item.getEzRssTorrentItem | REACHABLE | SOURCE | Def Rss2Item.java:119-121 calls new EzRss01Parser(this).parse(); interface dispatch CoreFeedParser.java:238 |
| 27 | Rss2Item.getGuid | REACHABLE | SOURCE | Def Rss2Item.java:69-72; interface dispatch CoreFeedParser.java:256 |
| 28 | Rss2Item.getLinks | REACHABLE | SOURCE | Def Rss2Item.java:46-54; interface dispatch CoreFeedParser.java:96 |
| 29 | Rss2Item.getMediaRss | REACHABLE | SOURCE | Def Rss2Item.java:114-116 calls new MediaRssParser(this).parse(); interface dispatch CoreFeedParser.java:190 |
| 30 | Rss2Item.getPubDate | REACHABLE | SOURCE | Def Rss2Item.java:75-78; interface dispatch CoreFeedParser.java:104 |
| 31 | Rss2Item.getTitle | REACHABLE | SOURCE | Def Rss2Item.java:40-43; interface dispatch CoreFeedParser.java:110 |
| 32 | Content.<init> | REACHABLE | SOURCE | Def Content.java:36-39; constructed MediaRssParser.java:52 |
| 33 | Content.equals | UNREACHABLE | no_trigger_in_app / INFERRED | Def Content.java:64-74; CORE uses Content only via getUrl():199 and getType():202, never compares Content in printed files. Pending full-repo grep incl. Set/Map use. |
| 34 | Content.getType | REACHABLE | SOURCE | Def Content.java:59-61; called CoreFeedParser.java:202 |
| 35 | Content.getUrl | REACHABLE | SOURCE | Def Content.java:48-50; called CoreFeedParser.java:199 |
| 36 | Content.hashCode | UNREACHABLE | no_trigger_in_app / INFERRED | Def Content.java:76-80; no hashed collection of Content printed. Pending full-repo grep. |
| 37 | Content.toString | UNREACHABLE | no_trigger_in_app / INFERRED | Def Content.java:84-89; no call in printed files. MediaRss.toString:44 concatenates its content list, which would invoke it if MediaRss.toString were called — no caller of MediaRss.toString printed, so that audit is also pending. Pending full-repo grep. |
| 38 | Hash.<init> | REACHABLE | SOURCE | Def Hash.java:21-23; constructed MediaRssParser.java:68 |
| 39 | Hash.equals | UNREACHABLE | no_trigger_in_app / INFERRED | Def Hash.java:55-65; CORE uses Hash only via getValue()/getAlgorithm() (:221, :224), never compares Hash in printed files. Pending full-repo grep. |
| 40 | Hash.getAlgorithm | REACHABLE | SOURCE | Def Hash.java:44-46; called CoreFeedParser.java:224 |

## What remains unverified for merge

- Real full-repo grep for all 8 UNREACHABLE rows, including implicit toString/equals/hashCode uses, Set/Map storage, MediaRss.toString callers, and BaseItem.equals/hashCode triggers (which decide #11/#24 and batch 13 rows 16-19 together).
- Build, sampler, and C1 checks on a full local checkout — not run here, no count claimed.
- Branch provenance: these local src files were connector-fetched earlier for work-2026-10-31; re-confirm work vs result branch agreement on these files before merging, as the prior batch 14 helper flagged.
- No Yang/user decision needed for any batch 14 row on this evidence.
