# UNVERIFIED RE-CHECK — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a re-check part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged. Batches 13-18 were unverified when the Claude run stopped.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# LibreTorrent batch 13 — INDEPENDENT RE-CHECK (proposed part only, NOT merged, NOT verified by build/C1)

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31`, connector only.
- Membership: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, filtered `batch == 13` in this
  session: exactly **40 rows**, all status `TODO_CANDIDATE_REACHABLE`, current label
  `REACHABLE (generator candidate, no hand route yet)` — candidate only, not evidence.
- Rules read in this session: `handoff/MUSE_HANDOVER.md` (full), plus the six rules files
  as delivered by a background connector call (`KIRO_CONVERT_APPS.md` delivered truncated
  mid-section-10 by the 12,000-char per-file cap in that call; `KIRO_CORRECTIONS.md`,
  `SCHEMA_V2.md`, `AGENT_BRIEF_V2.md`, `CONVERSION_RECIPE.md`,
  `CHATGPT_PROMPT_LIBRETORRENT_3.md` delivered in full).
- `graphs/LibreTorrent/AGENT_NOTES.md` section `## Stopped by the user` (lines 268–272,
  2026-10-31 ~18:10 EDT) read in this session: batches 13–18 are unverified, re-check
  before relying on them. Prior labels were treated as candidates only.
- Prior proposal `graphs/LibreTorrent/scratch/proposals/batch13_proposal_UNVERIFIED.md`
  read for context only, NOT as evidence. Every label below was re-derived from source
  printed in this session via the connector. `scratch/b013*` files were NOT used as evidence.
- Source root (confirmed by successful fetches under it):
  `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`
  (no separate directory-listing tool exists in the connector's read set; the root is
  confirmed by the files below all fetching successfully under it).
- No tool coverage, old generated graphs, or build REACHABLE counts were used as evidence.
- No build, sampler, grep, or C1 check was run in this session (connector-only, no local
  checkout). No count is claimed for any of those. Nothing was pushed; nothing on any
  branch was edited; `graph_def.py`, `out/` were not touched. No Yang/user decision made.

## Counts judged in this session

- Judged: 40 / 40. **REACHABLE: 36. UNREACHABLE: 4** (all `no_trigger_in_app`).
- confirmed_by: SOURCE 29, INFERRED 11 (7 SAX-dispatch REACHABLE + 4 UNREACHABLE).
- OPEN: 0 rows left unjudged — but every row carries a "remains unverified" caveat below
  (trunk-entry gap, dispatch inference, and for UNREACHABLE rows the pending full-repo grep).
  This is therefore a PROPOSED part, not a verified/mergeable part, until a full-checkout
  agent runs the build and C1 checks and a real full-repo grep for the 4 UNREACHABLE rows.

## Shared route trunk (all steps printed in this session unless marked INFERRED)

Abbreviations: `FP = com/ernieyu/feedparser/impl/`, `F = com/ernieyu/feedparser/`,
`C = org/proninyaroslav/libretorrent/core/FeedParser.java`,
`W = org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java`,
`S = org/proninyaroslav/libretorrent/service/Scheduler.java`.

- T1. `S:112-125` — `Scheduler.runPeriodicalRefreshFeeds` builds a
  `PeriodicWorkRequest` for `FeedFetcherWorker` (`S:116`, action
  `ACTION_FETCH_ALL_CHANNELS` at `S:113-114`) and enqueues it (`S:124-125`).
- T2. WorkManager dispatch `S:124-125 → W:74` (`FeedFetcherWorker.doWork`) — **INFERRED**,
  WorkManager library source not read; no FW-SRC citation claimed.
- T3. `W:74-105` — `doWork` switch: `ACTION_FETCH_CHANNEL` `W:93-95`,
  `ACTION_FETCH_CHANNEL_LIST` `W:96-98`, `ACTION_FETCH_ALL_CHANNELS` `W:99-101`,
  all → `fetchChannel` (`W:144`); `fetchChannel` does `new FeedParser(...)` at `W:156`
  and `parser.getItems()` at `W:165`.
- T4. `C:62-71` — core `FeedParser.<init>` fetches the URL (`C:67`); only if the HTTP
  response is non-null does it call `FeedParserFactory.newParser().parse(bsStream)` (`C:71`).
  If the response is null it returns early (`C:68-69`); `getItems` returns empty if
  `feed == null` (`C:92-93`).
- T5. `F/FeedParserFactory.java:23-25` — `newParser()` returns `new DefaultFeedParser()`.
- T6. `FP/DefaultFeedParser.java:22-47` — `parse` creates the SAX parser, `new FeedHandler()`
  at `:34`, `parser.parse(new XMLInputStream(inStream), handler)` at `:37`, then
  `handler.getFeed()` at `:38`.
- T7. SAX dispatch `DefaultFeedParser.java:37 → FeedHandler` callbacks — **INFERRED**,
  JDK/SAX source not read; no FW-SRC citation claimed. Registration itself is printed at `:37`.
- T8. `FP/FeedHandler.java:54-103` — `startElement`: `ENTRY` branch `:94-96` creates
  `AtomItem`; `ITEM` + `RSS_2_0` branch `:87-88` creates `Rss2Item`; generic branch `:100`
  creates `BaseElement`. `endElement` `:110-131` calls `setContent` (`:121`) and
  `addElement` (`:126`).
- T9. `C:89-115` — core `getItems` loops `feed.getItemList()` (`C:95`);
  `FP/AtomFeed.java:94-107` returns the AtomItems (cast at `:102`);
  `FP/Rss2Feed.java:113-130` returns the Rss2Items (cast at `:125`).
- T10. Unconditional in the `getItems` loop: `item.getLinks()` `C:96`, `item.getPubDate()`
  `C:104`, `item.getTitle()` `C:110`. Download-URL branch `C:101-102`: only if no
  magnet/torrent link was found, `findDownloadUrl` (`C:141-161`) runs, in this order,
  `watchEnclosure` (`:147`), `watchTorrentInfoHash` (`:151`), `watchMediaContent` (`:155`),
  `watchGuid` (`:159`); `watchMediaContent` calls `item.getMediaRss()` at `C:190`,
  `watchTorrentInfoHash` calls `item.getEzRssTorrentItem()` at `C:238`,
  `watchGuid` calls `item.getGuid()` at `C:256`. A later watcher is reached only when
  every earlier watcher returned null.

Corrections to the prior proposal's line numbers found by re-printing (steps themselves
unchanged): `DefaultFeedParser.parse` runs `:22-47` (not `:22-38`; `:34/:37/:38` steps
match); `FeedHandler.endElement` runs `:110-131` (`:121`/`:126` steps match);
`findDownloadUrl` order is enclosure → infoHash → media → guid (prior trunk listed
media before infoHash); `Scheduler.runPeriodicalRefreshFeeds` runs `:112-126`.

Trunk gaps (apply to every REACHABLE row): the caller of
`Scheduler.runPeriodicalRefreshFeeds` was NOT printed in this session, so the route is
anchored at Scheduler, not at a launcher entry; WorkManager dispatch (T2) and SAX dispatch
(T7) are INFERRED. The periodic refresh also carries a network constraint
(`S:128-140`, `NetworkType.CONNECTED` unless settings change it) — an ENV `network` gate
that changes which route is chosen, not the verdict.

## Per-method table

Citations are `file:lines` relative to the source root above. "Def" = definition lines
printed; "Call" = printed caller/route step(s). `confirmed_by` = SOURCE where definition
and direct printed caller are both in printed app/library code; INFERRED where the route
depends on an unread dispatch step or, for UNREACHABLE rows, on absence over code not all read.

| # | Method | JVM descriptor | Proposed label | Kind | Reason / route (printed citations) | confirmed_by | What remains unverified, and why |
|---:|---|---|---|---|---|---|---|
| 1 | AtomItem.getEzRssTorrentItem | ()Lcom/ernieyu/feedparser/EzRssTorrentItem; | REACHABLE | — | Def `FP/AtomItem.java:136-137` returns null ("Not supported"). Call: interface call `C:238` via `watchTorrentInfoHash`, reached via T10 only when `watchEnclosure` returned null. Returning null is not unreachability; the interface call dispatches to this Atom override for Atom feeds. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch (see trunk gaps). Needs an Atom feed whose items have no enclosure download URL (T10 ordering). No build/C1 run. |
| 2 | AtomItem.getGuid | ()Ljava/lang/String; | REACHABLE | — | Def `FP/AtomItem.java:74-76` (`getElement(ID)` + `getContent()`). Call: interface call `C:256` via `watchGuid`, reached via T10 only when enclosure, infoHash and media watchers returned null. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch. Needs an Atom feed item reaching `watchGuid`. No build/C1 run. |
| 3 | AtomItem.getLinks | ()Ljava/util/List; | REACHABLE | — | Def `FP/AtomItem.java:46-50` (`getElementList(LINK)` + `getAttributes()`). Call: unconditional `C:96` in the `getItems` loop. Trunk T1–T9. | SOURCE | Entry gap + WorkManager dispatch. Needs an Atom feed with ≥1 entry. No build/C1 run. |
| 4 | AtomItem.getMediaRss | ()Lcom/ernieyu/feedparser/mediarss/MediaRss; | REACHABLE | — | Def `FP/AtomItem.java:127-128` returns null ("Not supported"). Call: interface call `C:190` via `watchMediaContent`, reached via T10 only when enclosure and infoHash watchers returned null. Returning null is not unreachability. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch. Needs an Atom feed item reaching `watchMediaContent`. No build/C1 run. |
| 5 | AtomItem.getPubDate | ()Ljava/util/Date; | REACHABLE | — | Def `FP/AtomItem.java:80-82` (`getElement(UPDATED)` + `getContent()`). Call: unconditional `C:104` in the `getItems` loop. Trunk T1–T9. | SOURCE | Entry gap + WorkManager dispatch. Needs an Atom feed with ≥1 entry. No build/C1 run. |
| 6 | AtomItem.getTitle | ()Ljava/lang/String; | REACHABLE | — | Def `FP/AtomItem.java:40-42` (`getElement(TITLE)` + `getContent()`). Call: unconditional `C:110` in the `getItems` loop. Trunk T1–T9. | SOURCE | Entry gap + WorkManager dispatch. Needs an Atom feed with ≥1 entry. No build/C1 run. |
| 7 | BaseElement.<init>(String,String,Attributes) | (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | REACHABLE | — | Def `FP/BaseElement.java:39-43`. Calls: `FP/FeedHandler.java:100` (generic element); via `super` from `FP/BaseItem.java:21-22`, `FP/AtomItem.java:30-31`, `FP/Rss2Item.java:30-31`. Trunk T1–T8. | SOURCE | Entry gap + WorkManager dispatch; the FeedHandler construction step also passes through SAX dispatch (T7). No build/C1 run. |
| 8 | BaseElement.addElement | (Ljava/lang/String;Lcom/ernieyu/feedparser/Element;)V | REACHABLE | — | Def `FP/BaseElement.java:91-99`. Call: `FP/FeedHandler.java:124-126` (`parent.addElement`, in `endElement`). Trunk T1–T8. | INFERRED | `endElement` itself is only reached by SAX dispatch (T7, source not read). Otherwise as for row 7. No build/C1 run. |
| 9 | BaseElement.getAttributes | ()Lorg/xml/sax/Attributes; | REACHABLE | — | Def `FP/BaseElement.java:56-57`. Call: `FP/AtomItem.java:50` (`element.getAttributes()` in `getLinks`, itself called at `C:96`). Also `FP/Rss2Item.java:99`, `FP/MediaRssParser.java:48`. Trunk T1–T9. | SOURCE | Entry gap + WorkManager dispatch; Atom construction passes through SAX dispatch (T7). No build/C1 run. |
| 10 | BaseElement.getContent | ()Ljava/lang/String; | REACHABLE | — | Def `FP/BaseElement.java:61-62`. Calls: `FP/AtomItem.java:42,76,82`; `FP/EzRss01Parser.java:44,52,60,70`. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch; construction passes through SAX dispatch (T7). No build/C1 run. |
| 11 | BaseElement.getElement | (Ljava/lang/String;)Lcom/ernieyu/feedparser/Element; | REACHABLE | — | Def `FP/BaseElement.java:73-75`. Calls: `FP/AtomItem.java:41,75,81`; `FP/EzRss01Parser.java:40,48,56,64,80,88,96`. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch; construction passes through SAX dispatch (T7). No build/C1 run. |
| 12 | BaseElement.getElementList | (Ljava/lang/String;)Ljava/util/List; | REACHABLE | — | Def `FP/BaseElement.java:79-80`. Call: `FP/AtomItem.java:48` (`getElementList(LINK)` in `getLinks`, called at `C:96`); also `FP/AtomFeed.java:96`, `FP/Rss2Feed.java:119`. Trunk T1–T9. | SOURCE | Entry gap + WorkManager dispatch; construction passes through SAX dispatch (T7). No build/C1 run. |
| 13 | BaseElement.getUri | ()Ljava/lang/String; | REACHABLE | — | Def `FP/BaseElement.java:46-47`. Call: `FP/EzRss01Parser.java:118-120` (`isEzRssElement`, `element.getUri()`), itself called from `EzRss01Parser.parse*` (rows 26–32). Trunk T1–T10, RSS 2.0 branch. | SOURCE | Entry gap + WorkManager dispatch; construction passes through SAX dispatch (T7). Needs an RSS 2.0 item with an EzRSS element. No build/C1 run. |
| 14 | BaseElement.setContent | (Ljava/lang/String;)V | REACHABLE | — | Def `FP/BaseElement.java:68-69`. Call: `FP/FeedHandler.java:121` (`currentElement.setContent`, in `endElement`). Trunk T1–T8. | INFERRED | `endElement` itself is only reached by SAX dispatch (T7, source not read). Otherwise as for row 7. No build/C1 run. |
| 15 | BaseItem.<init> | (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | REACHABLE | — | Def `FP/BaseItem.java:21-22`, which calls `BaseElement.<init>` at `:22`. Calls (super): `FP/AtomItem.java:30-31`, `FP/Rss2Item.java:30-31`, constructed in `FP/FeedHandler.java:87-88,94-96`. Trunk T1–T8. | SOURCE | Entry gap + WorkManager dispatch; construction passes through SAX dispatch (T7). No build/C1 run. |
| 16 | BaseItem.equals | (Ljava/lang/Object;)Z | UNREACHABLE | no_trigger_in_app | Def `FP/BaseItem.java:53-62`; it calls `getUniqueId` at `:56-57` (outgoing, not a trigger). No caller of `equals` on a library `Item` appears in any file printed in this session (full `FeedFetcherWorker.java`, core `FeedParser.java`, `FeedHandler`, parsers, `AtomItem`/`Rss2Item`). Duplicate filtering in `W:196-203` compares app `FeedItem.title` strings, not library Items, and no library Item is placed in a hash/equals-based collection in printed code (`ArrayList` only: `FP/AtomFeed.java:97`, `FP/Rss2Feed.java:120`, `C:91`). | INFERRED | **A real full-repo grep is still required before merging** — absence is over code not all read. Connector `search_code` cannot substitute: repo-scoped query returned `total_count 0, incomplete_results true`; unscoped query returned 703,488 hits in unrelated repos. If a grep finds any trigger (explicit call, collection use, or string/concatenation use), this row flips to REACHABLE. No build/C1 run. |
| 17 | BaseItem.getUniqueId | ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app | Def `FP/BaseItem.java:30-44`, `private`. Only printed callers are `equals` (`FP/BaseItem.java:56-57`) and `hashCode` (`:67`), both proposed UNREACHABLE here. Private, so no external caller is possible in Java, but its only triggers are those two methods. | INFERRED | Same pending full-repo grep as row 16 (to confirm no other in-class trigger and that equals/hashCode truly have no trigger); if either flips, this flips with it. No build/C1 run. |
| 18 | BaseItem.hashCode | ()I | UNREACHABLE | no_trigger_in_app | Def `FP/BaseItem.java:65-69`; it calls `getUniqueId` at `:67` (outgoing). No call, and no hash collection containing a library Item, in any file printed in this session (collections are `ArrayList`: `FP/AtomFeed.java:97`, `FP/Rss2Feed.java:120`, `C:91`). | INFERRED | Same pending full-repo grep as row 16; a hash-based collection holding library Items would flip this to REACHABLE. No build/C1 run. |
| 19 | BaseItem.toString | ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app | Def `FP/BaseItem.java:48-49` returns `getTitle()`. No call, string concatenation, or log/print on a library Item in any file printed in this session; core code reads `item.getTitle()` etc. explicitly (`C:96,104,110`). (The `toString` overrides in `FP/AtomFeed.java:111` and `FP/Rss2Feed.java:135` are different methods, not batch-13 rows.) | INFERRED | Same pending full-repo grep as row 16; any concatenation/log/print of a library Item would flip this to REACHABLE. No build/C1 run. |
| 20 | DefaultFeedParser.<init> | ()V | REACHABLE | — | Implicit default constructor: `FP/DefaultFeedParser.java` printed in full (48 lines) contains no explicit constructor (class at `:19`, `parse` at `:22`). Call: `F/FeedParserFactory.java:25` (`new DefaultFeedParser()`). Trunk T1–T5. | SOURCE | Entry gap + WorkManager dispatch. No build/C1 run. |
| 21 | DefaultFeedParser.parse | (Ljava/io/InputStream;)Lcom/ernieyu/feedparser/Feed; | REACHABLE | — | Def `FP/DefaultFeedParser.java:22-47`. Call: `C:71` (`FeedParserFactory.newParser().parse(bsStream)`). Trunk T1–T6. | SOURCE | Entry gap + WorkManager dispatch. Needs a non-null HTTP response (`C:68-69`). No build/C1 run. |
| 22 | EzRss01Parser.<init> | (Lcom/ernieyu/feedparser/impl/Rss2Item;)V | REACHABLE | — | Def `FP/EzRss01Parser.java:22-23`. Call: `FP/Rss2Item.java:119-120` (`new EzRss01Parser(this).parse()`), itself reached via `C:238` for RSS 2.0 items when `watchEnclosure` returned null (T10). Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch. Needs an RSS 2.0 item reaching `watchTorrentInfoHash`. No build/C1 run. |
| 23 | EzRss01Parser.isEzRssElement | (Lcom/ernieyu/feedparser/Element;)Z | REACHABLE | — | Def `FP/EzRss01Parser.java:118-120` (calls `getUri()`). Calls: `FP/EzRss01Parser.java:41,49,57,65,81,89,97` (every `parse*` method). Via row 24. | SOURCE | Entry gap + WorkManager dispatch; via row 24's conditions. No build/C1 run. |
| 24 | EzRss01Parser.parse | ()Lcom/ernieyu/feedparser/EzRssTorrentItem; | REACHABLE | — | Def `FP/EzRss01Parser.java:26-36`; unconditionally calls `parseFileName, parseMagnetUri, parseInfoHash, parseContentLength, parseSeeds, parsePeers, parseVerified` at `:27-33`. Call: `FP/Rss2Item.java:120`. Trunk T1–T10. | SOURCE | Entry gap + WorkManager dispatch; via row 22's conditions. No build/C1 run. |
| 25 | EzRss01Parser.parseContentLength | ()J | REACHABLE | — | Def `FP/EzRss01Parser.java:63-76` (uses `Long.parseLong` directly at `:70`, not `parseInt`). Call: `FP/EzRss01Parser.java:30` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 26 | EzRss01Parser.parseFileName | ()Ljava/lang/String; | REACHABLE | — | Def `FP/EzRss01Parser.java:39-44` (calls `getElement` + `isEzRssElement` + `getContent`). Call: `FP/EzRss01Parser.java:27` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 27 | EzRss01Parser.parseInfoHash | ()Ljava/lang/String; | REACHABLE | — | Def `FP/EzRss01Parser.java:55-60`. Call: `FP/EzRss01Parser.java:29` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 28 | EzRss01Parser.parseInt | (Ljava/lang/String;)I | REACHABLE | — | Def `FP/EzRss01Parser.java:105-115`. Calls: `FP/EzRss01Parser.java:84` (`parseSeeds`), `:92` (`parsePeers`), `:100` (`parseVerified`). (`parseContentLength` does not use it, `:70`.) | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 29 | EzRss01Parser.parseMagnetUri | ()Ljava/lang/String; | REACHABLE | — | Def `FP/EzRss01Parser.java:47-52`. Call: `FP/EzRss01Parser.java:28` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 30 | EzRss01Parser.parsePeers | ()I | REACHABLE | — | Def `FP/EzRss01Parser.java:87-92` (calls `getElement`, `isEzRssElement`, `parseInt`). Call: `FP/EzRss01Parser.java:32` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 31 | EzRss01Parser.parseSeeds | ()I | REACHABLE | — | Def `FP/EzRss01Parser.java:79-84` (calls `getElement`, `isEzRssElement`, `parseInt`). Call: `FP/EzRss01Parser.java:31` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 32 | EzRss01Parser.parseVerified | ()Z | REACHABLE | — | Def `FP/EzRss01Parser.java:95-102` (calls `getElement`, `isEzRssElement`, `parseInt`). Call: `FP/EzRss01Parser.java:33` (from `parse`). | SOURCE | Entry gap + WorkManager dispatch; via row 24. No build/C1 run. |
| 33 | FeedHandler.<init> | ()V | REACHABLE | — | Implicit default constructor: `FP/FeedHandler.java` printed in full (132 lines) contains no explicit constructor (class at `:16`, `getFeed` at `:31`). Call: `FP/DefaultFeedParser.java:34` (`new FeedHandler()`). Trunk T1–T6. | SOURCE | Entry gap + WorkManager dispatch. No build/C1 run. |
| 34 | FeedHandler.characters | ([CII)V | REACHABLE | — | Def `FP/FeedHandler.java:36-38` (appends to buffer). Registration: `FP/DefaultFeedParser.java:37` (`parser.parse(..., handler)`). Dispatch INFERRED (T7). | INFERRED | SAX dispatch source not read (no FW-SRC claimed). Otherwise trunk gaps. No build/C1 run. |
| 35 | FeedHandler.endDocument | ()V | REACHABLE | — | Def `FP/FeedHandler.java:48-50` (clears `elementStack`). Registration: `FP/DefaultFeedParser.java:37`. Dispatch INFERRED (T7). | INFERRED | SAX dispatch source not read (no FW-SRC claimed). Otherwise trunk gaps. No build/C1 run. |
| 36 | FeedHandler.endElement | (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V | REACHABLE | — | Def `FP/FeedHandler.java:110-131` (calls `setContent` `:121`, `addElement` `:126`). Registration: `FP/DefaultFeedParser.java:37`. Dispatch INFERRED (T7). | INFERRED | SAX dispatch source not read (no FW-SRC claimed). Otherwise trunk gaps. No build/C1 run. |
| 37 | FeedHandler.getFeed | ()Lcom/ernieyu/feedparser/Feed; | REACHABLE | — | Def `FP/FeedHandler.java:31-32`. Call (explicit, not SAX): `FP/DefaultFeedParser.java:38` (`handler.getFeed()`). Trunk T1–T6. | SOURCE | Entry gap + WorkManager dispatch. No build/C1 run. |
| 38 | FeedHandler.startDocument | ()V | REACHABLE | — | Def `FP/FeedHandler.java:42-44` (initialises `elementStack`). Registration: `FP/DefaultFeedParser.java:37`. Dispatch INFERRED (T7). | INFERRED | SAX dispatch source not read (no FW-SRC claimed). Otherwise trunk gaps. No build/C1 run. |
| 39 | FeedHandler.startElement | (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | REACHABLE | — | Def `FP/FeedHandler.java:54-103` (creates `AtomItem`/`Rss2Item`/`BaseElement` per branch, T8). Registration: `FP/DefaultFeedParser.java:37`. Dispatch INFERRED (T7). | INFERRED | SAX dispatch source not read (no FW-SRC claimed). Otherwise trunk gaps. No build/C1 run. |
| 40 | MediaRssParser.<init> | (Lcom/ernieyu/feedparser/impl/Rss2Item;)V | REACHABLE | — | Def `FP/MediaRssParser.java:25-26`. Call: `FP/Rss2Item.java:114-115` (`new MediaRssParser(this).parse()`), itself reached via `C:190` for RSS 2.0 items when `watchEnclosure` and `watchTorrentInfoHash` returned null (T10). Trunk T1–T10. (`MediaRssParser.parse` itself is NOT a batch-13 row.) | SOURCE | Entry gap + WorkManager dispatch. Needs an RSS 2.0 item reaching `watchMediaContent`. No build/C1 run. |

## Files printed in this session (all via the connector, branch work-2026-10-31)

`FP/AtomItem.java` (139 lines), `FP/BaseElement.java` (100), `FP/BaseItem.java` (70),
`FP/FeedHandler.java` (132), `FP/DefaultFeedParser.java` (48),
`F/FeedParserFactory.java` (27), `FP/EzRss01Parser.java` (122), `FP/MediaRssParser.java` (98),
`FP/Rss2Item.java` (122), `FP/AtomFeed.java` (114), `FP/Rss2Feed.java` (137),
`org/proninyaroslav/libretorrent/core/FeedParser.java` (267),
`org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java` (270),
`org/proninyaroslav/libretorrent/service/Scheduler.java` (145) — all under the source root above.

## Connector search limitation (explicit)

- Repo-scoped `search_code` query `repo:bugfixops/ground-truth-results BaseItem` returned
  `total_count 0, incomplete_results true` — the connector's code search does not index this repo.
- Unscoped `search_code` query `BaseItem` returned `total_count 703488` hits in unrelated
  repositories — unusable for this repo.
- Neither result is used as evidence, and neither substitutes for a real full-repo grep.
  **The 4 UNREACHABLE rows must not be merged until that grep is run on a full checkout.**

## Framework claims

None. No `fw_src/android-8.1.0_r1/` lines were printed in this session, so no FW-SRC
citation is claimed. WorkManager dispatch and SAX dispatch are recorded as INFERRED /
"source not read", not as framework facts.

## What this part still needs before it is mergeable (for the parent)

1. A full-checkout agent runs the build and C1 checks (not done here; connector-only).
2. A real full-repo grep over the source root for triggers of `BaseItem.equals`,
   `hashCode`, `toString`, and `getUniqueId` (explicit calls, hash/equals collections,
   concatenation/log/print on library Items). If it finds a trigger, flip that row.
3. Optionally, print the caller of `Scheduler.runPeriodicalRefreshFeeds` to anchor the
   trunk at a launcher entry rather than at Scheduler.
4. No Yang/user decision is involved in any row above.
