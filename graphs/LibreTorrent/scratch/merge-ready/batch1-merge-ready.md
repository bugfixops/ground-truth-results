# LibreTorrent batch 1 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 1 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior work (Agent 50's batches 1–12
  audit) was used as an INPUT / lead list only; every row below was re-judged from the
  source printed in this pass, and no audit verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 1 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-1 rows are `DONE_RECHECK` in the plan with `current_label`
`UNREACHABLE no_trigger_in_app`. That plan label is NOT adopted wholesale below:
rows 2–40 are proposed UNREACHABLE on the printed evidence in this pass, row 1 is
left OPEN (see below) — the plan's UNREACHABLE claim for a generated/library
constants-class constructor rests on absence alone, which is not enough for
generated code under rule F / C5.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b1-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):

- `com/ernieyu/feedparser/impl/AtomFeed.java` — SHA `1ca685b734e5675074b3211b17f98655c8d27afd`, 115 lines.
- `com/ernieyu/feedparser/impl/AtomItem.java` — SHA `0e3d1cfb780139a02d945a2c343e8599c518a1ca`, 140 lines.
- `com/ernieyu/feedparser/impl/Rss1Feed.java` — SHA `23be5f997391b2d2b6ff1d5bd76b1ad1c1cba150`, 124 lines.
- `com/ernieyu/feedparser/impl/Rss1Item.java` — SHA `e46cea499eb9dd67ffba80f9916047c4e1a5aa26`, 125 lines.
- `com/ernieyu/feedparser/impl/Rss2Feed.java` — SHA `2051ebd60e9e0132e561c12281d6ee4544f834d4`, 138 lines.
- `com/ernieyu/feedparser/impl/BaseElement.java` — SHA `e7d5205a3b247c863d1a011eceee6a62a85abdf0`, 101 lines.
- `com/ernieyu/feedparser/impl/BaseItem.java` — SHA `70fa1de0ccf1ad29a79990c13e3a5b4ef3a520e2`, 71 lines.
- `com/ernieyu/feedparser/impl/EzRss01Parser.java` — SHA `5b68409579462e6cbac5ad7f46eb66753d0fa7ee`, 123 lines.
- `com/ernieyu/feedparser/impl/FeedHandler.java` — SHA `a5bb6f13841ffb0ad7894f1af7e024842775c86a`, 133 lines.
- `com/ernieyu/feedparser/impl/DefaultFeedParser.java` — SHA `ef21998eaf9e4170eb8a6400d5c2c7e3ec24deea`, 49 lines.
- `com/ernieyu/feedparser/Enclosure.java` — SHA `39e7b3c59578659748917bb703f60dab6d507361`, 87 lines.
- `com/ernieyu/feedparser/EzRssTorrentItem.java` — SHA `83b0f11af273369674d29e9791ea307d3dc6f6ca`, 141 lines.
- `com/ernieyu/feedparser/FeedException.java` — SHA `6667f68ef26a6b1af4e6770625213fa45e8c32b2`, 24 lines.
- `com/ernieyu/feedparser/FeedParserFactory.java` — SHA `33fc7bfa0c80893f8a3b218929278b77c0d9ee4a`, 28 lines.
- `com/ernieyu/feedparser/FeedUtils.java` — SHA `39c64f2432566bf604b7644ce72a7121fa949edd`, 120 lines.
- `com/ernieyu/feedparser/XML.java` — SHA `57eacc77c3dc3ce68df37e2dbdf0e6d761046584`, 278 lines.
- `com/ernieyu/feedparser/Feed.java` (interface) — SHA `c0d4b1899e5411ff346cf0b42ffd5373ff960334`, 56 lines.
- `com/ernieyu/feedparser/Item.java` (interface) — SHA `67a0aa56b34fe1b741524631994540ea009247de`, 81 lines.
- `org/proninyaroslav/libretorrent/core/FeedParser.java` (the app's parser; the file
  is named `FeedParser.java`, not `CoreFeedParser.java`) — SHA `99c05d886bd9fb5824a05efdaf176d4b87b637d8`, 268 lines.

One path guess failed cleanly (file-not-found, not a 429): `com/ernieyu/feedparser/impl/XML.java`
does not exist; the `XML` class lives at `com/ernieyu/feedparser/XML.java`, fetched above.
No connector `search_code` result was used as evidence of absence anywhere in this file.
No fresh HTTP 429 was hit in this pass.

## The printed caller set — the whole argument for rows 2–40

The app consumes the feed-parser library almost entirely through the app's
`core/FeedParser.java`. Its printed call sites on library interfaces/objects are,
in full:

- `feed.getTitle()` at CoreFeedParser.java:86 (inside its own `getTitle()` wrapper);
  `feed.getItemList()` at :95.
- `item.getLinks()` at :96; `item.getPubDate()` at :104 (item-level, not feed-level);
  `item.getTitle()` at :110; `item.getEnclosures()` at :170.
- `enclosure.getUrl()` at :174; `enclosure.getType()` at :175.
- `item.getMediaRss()` at :190; `media.getContent()` at :194; `content.getUrl()` at :199;
  `content.getType()` at :202; `media.getHash()` at :217; `hash.getValue()` / `hash.getAlgorithm()` at :221/:224.
- `item.getEzRssTorrentItem()` at :238; `torrentItem.getInfoHash()` at :242.
- `item.getGuid()` at :256.
- Inside the library itself: `BaseItem.getUniqueId()` calls `getGuid()` / `getLinks()` /
  `getTitle()` / `getDescription()` (BaseItem.java:31/:33/:38/:41); `FeedHandler`
  constructs all three feed/item families with the 3-arg constructor
  (FeedHandler.java:62 Rss1Feed, :69 Rss2Feed, :76 AtomFeed, :85 Rss1Item, :88 Rss2Item,
  :96 AtomItem, :100 generic `BaseElement`); `EzRss01Parser` builds an
  `EzRssTorrentItem` from parsed element content (EzRss01Parser.java:35-36) and never
  reads its getters back; `DefaultFeedParser` throws only the 1-arg `FeedException`
  forms (DefaultFeedParser.java:40 `new FeedException("Invalid RSS/Atom feed")`,
  :45 `new FeedException(ex)`).

No call site in any file printed above invokes any batch-1 method in rows 2–40.
That disjointness is the evidence for the UNREACHABLE proposals — but it is not a
full-repo grep, so every UNREACHABLE row below is `confirmed_by` INFERRED, never
SOURCE, and a saved full-repo grep is still owed for every one of them (see Gaps).
A single grep hit for a row flips that row to REACHABLE.

Traps avoided (each is a different method from a same-named called method):
- Feed-level `getPubDate()` (rows 19, 32) is NOT item-level `getPubDate()`
  (CoreFeedParser.java:104, called). Feed-level `getLink()` / `getType()` are NOT
  `enclosure.getType()` (:175) or `content.getType()` (:202). Item-level `getType()`
  (rows 23, 36) is NOT `enclosure.getType()` / `content.getType()`.
  `EzRssTorrentItem.getInfoHash()` (:242, called) is NOT the other EzRss getters.
  `BaseElement.getName()` / `getElementKeys()` are NOT `getElement()` / `getElementList()`
  / `getUri()` / `getContent()`, which are the methods the printed code actually uses
  (EzRss01Parser.java:119-120 uses `getUri()`; FeedHandler.java:121 uses `setContent()`).
- The app's entity class `FeedItem` (core/model/data/entity) is a different class
  from the library `Item`; CoreFeedParser maps a library `Item` to an entity
  `FeedItem` using only title, links, pubDate and download URL (:95-:110), so entity
  use does not rescue any library accessor.

## confirmed_by convention in this file

- `INFERRED` for every row below. For UNREACHABLE-proposed rows it means: the
  definition is printed and the printed caller set above is disjoint from the row,
  but a full-repo grep has not been run, so absence elsewhere is inferred, not shown.
- `OPEN` for row 1 only, where even the definition is not in the printed upload
  (generated/library constants class), so no printed definition + caller-set
  argument can be made at all.
- No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## Table — 40 rows, plan order

| # | Method (descriptor) | Label proposed | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | baseAdapters.BR.<init> ()V | OPEN | INFERRED | No definition printed in this pass; this is `androidx.databinding.library.baseAdapters.BR`, a library constants class whose source is not in the upload. The prior graph claim (UNREACHABLE INFERRED citing a generated-class grep) is a lead only and is NOT adopted here. Needs printed generated/library source or a saved class-name grep (rule F / C5) before any UNREACHABLE label; must not be conflated with the libretorrent databinding `BR` in batch 2's OPEN rows. |
| 2 | Enclosure.getLength ()J | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Enclosure.java:52-54. Parser reads `enclosure.getUrl()` / `getType()` (CoreFeedParser.java:174-175) only; never `getLength()`. Grep owed; a hit flips to REACHABLE. |
| 3 | EzRssTorrentItem.getContentLength ()J | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:69-71. EzRss01Parser parses the field into the constructor (:35-36, :63-77) and never reads it back; parser reads only `getInfoHash()` (CoreFeedParser.java:242). Grep owed. |
| 4 | EzRssTorrentItem.getFileName ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:45-47. Same as row 3; field parsed at EzRss01Parser.java:39-45, never read back. Grep owed. |
| 5 | EzRssTorrentItem.getMagnetUri ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:53-55. Same as row 3; field parsed at EzRss01Parser.java:47-53, never read back. Grep owed. |
| 6 | EzRssTorrentItem.getPeers ()I | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:85-87. Same as row 3; field parsed at EzRss01Parser.java:87-93, never read back. Grep owed. |
| 7 | EzRssTorrentItem.getSeeds ()I | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:77-79. Same as row 3; field parsed at EzRss01Parser.java:79-85, never read back. Grep owed. |
| 8 | EzRssTorrentItem.isVerified ()Z | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition EzRssTorrentItem.java:93-95. Same as row 3; field parsed at EzRss01Parser.java:95-103, never read back. Grep owed. |
| 9 | FeedException.<init>() ()V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition FeedException.java:8-9. DefaultFeedParser throws only `new FeedException(String)` (:40) and `new FeedException(Throwable)` (:45) in the printed corpus; never the no-arg form. Grep owed. |
| 10 | FeedException.<init>(String,Throwable) (Ljava/lang/String;Ljava/lang/Throwable;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition FeedException.java:19-21. Same as row 9; neither printed throw site uses the 2-arg form. Grep owed. |
| 11 | FeedParserFactory.<init> ()V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition FeedParserFactory.java:16-26: the class has no explicit constructor and exactly one member, the static `newParser()` (:23-26) returning `new DefaultFeedParser()`. No `new FeedParserFactory()` is printed anywhere in this pass. Grep owed. |
| 12 | FeedUtils.<init> ()V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition FeedUtils.java:12: a static-utility class with no explicit constructor. Printed uses are all static: `convertAtomDate` (AtomFeed.java:77), `convertRss2Date` (Rss2Feed.java:96), `equalsOrNull` (BaseItem.java:58). No `new FeedUtils()` printed. Grep owed. |
| 13 | XML.<init> ()V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition XML.java:7-15: a static-only class (only member is static `hash()` at :9, plus the static `SPECIALS` table at :17-19); no explicit constructor, no `new XML()` printed. Note: `XML.hash()` itself is a different method and is not a batch-1 row. Grep owed. |
| 14 | AtomFeed.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:81-91. Interface method Feed.java:49. Parser calls `feed.getTitle()` / `feed.getItemList()` only on a Feed (CoreFeedParser.java:86/:95); never `feed.getCategories()`. Grep owed. |
| 15 | AtomFeed.getCopyright ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:69-72. Interface method Feed.java:39. Same feed-caller-set argument as row 14. Grep owed. |
| 16 | AtomFeed.getDescription ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:56-59. Interface method Feed.java:29. Same feed-caller-set argument as row 14. Note: `item.getDescription()` via BaseItem is a different receiver and is not this row. Grep owed. |
| 17 | AtomFeed.getLanguage ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:62-66 (body returns null, "Not implemented"). Interface method Feed.java:34. Same feed-caller-set argument as row 14. Grep owed. |
| 18 | AtomFeed.getLink ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:50-53. Interface method Feed.java:24. Same feed-caller-set argument as row 14; `item.getLinks()` (CoreFeedParser.java:96) is a different method. Grep owed. |
| 19 | AtomFeed.getPubDate ()Ljava/util/Date; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:75-78. Interface method Feed.java:44. Same feed-caller-set argument as row 14; `item.getPubDate()` (CoreFeedParser.java:104) is item-level, a different receiver. Grep owed. |
| 20 | AtomFeed.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomFeed.java:39-41. Interface method Feed.java:14. Same feed-caller-set argument as row 14; `enclosure.getType()` / `content.getType()` are different classes. Grep owed. |
| 21 | AtomItem.getAuthor ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomItem.java:64-66. Interface method Item.java:36. Parser item calls are getLinks / getPubDate / getTitle / getEnclosures / getMediaRss / getEzRssTorrentItem / getGuid (CoreFeedParser.java:96/:104/:110/:170/:190/:238/:256); never `getAuthor()`. Grep owed. |
| 22 | AtomItem.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomItem.java:86-91. Interface method Item.java:51. Same item-caller-set argument as row 21. Grep owed. |
| 23 | AtomItem.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition AtomItem.java:35-37. Interface method Item.java:16. Same item-caller-set argument as row 21; `enclosure.getType()` / `content.getType()` are different classes. Grep owed. |
| 24 | BaseElement.<init>(String,String) (Ljava/lang/String;Ljava/lang/String;)V | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition BaseElement.java:29-33 (2-arg form). Every printed subclass super-call uses the 3-arg form: AtomFeed.java:35, BaseItem.java:22, Rss1Feed.java:37, Rss2Feed.java:38; FeedHandler's generic-element construction is also 3-arg (FeedHandler.java:100). No 2-arg construction printed. Grep owed. |
| 25 | BaseElement.getElementKeys ()Ljava/util/Set; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition BaseElement.java:84-86. Printed element access uses `getElement()` / `getElementList()` / `getUri()` / `getContent()` (e.g. EzRss01Parser.java:40/:119, FeedHandler.java:121); never `getElementKeys()`. Grep owed. |
| 26 | BaseElement.getName ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition BaseElement.java:51-53. Printed element access uses `getUri()` (EzRss01Parser.java:119-120), `getContent()`, `getElement()`; never `getName()`. Grep owed. |
| 27 | Rss1Feed.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:98-102. Interface method Feed.java:49. Same feed-caller-set argument as row 14. Grep owed. |
| 28 | Rss1Feed.getCopyright ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:82-86. Interface method Feed.java:39. Same feed-caller-set argument as row 14. Grep owed. |
| 29 | Rss1Feed.getDescription ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:67-73. Interface method Feed.java:29. Same feed-caller-set argument as row 14. Grep owed. |
| 30 | Rss1Feed.getLanguage ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:74-81. Interface method Feed.java:34. Same feed-caller-set argument as row 14. Grep owed. |
| 31 | Rss1Feed.getLink ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:53-66. Interface method Feed.java:24. Same feed-caller-set argument as row 14. Grep owed. |
| 32 | Rss1Feed.getPubDate ()Ljava/util/Date; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:90-97. Interface method Feed.java:44. Same feed-caller-set argument as row 14; `item.getPubDate()` is item-level. Grep owed. |
| 33 | Rss1Feed.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Feed.java:41-44. Interface method Feed.java:14. Same feed-caller-set argument as row 14. Grep owed. |
| 34 | Rss1Item.getAuthor ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Item.java:62-68. Interface method Item.java:36. Same item-caller-set argument as row 21. Grep owed. |
| 35 | Rss1Item.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Item.java:83-87. Interface method Item.java:51. Same item-caller-set argument as row 21. Grep owed. |
| 36 | Rss1Item.getType ()Lcom/ernieyu/feedparser/FeedType; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss1Item.java:34-37. Interface method Item.java:16. Same item-caller-set argument as row 21. Grep owed. |
| 37 | Rss2Feed.getCategories ()Ljava/util/List; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:100-110. Interface method Feed.java:49. Same feed-caller-set argument as row 14. Grep owed. |
| 38 | Rss2Feed.getCopyright ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:82-86. Interface method Feed.java:39. Same feed-caller-set argument as row 14. Grep owed. |
| 39 | Rss2Feed.getDescription ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:68-74. Interface method Feed.java:29. Same feed-caller-set argument as row 14. Grep owed. |
| 40 | Rss2Feed.getLanguage ()Ljava/lang/String; | UNREACHABLE proposed, kind `no_trigger_in_app` | INFERRED | Definition Rss2Feed.java:75-81. Interface method Feed.java:34. Same feed-caller-set argument as row 14. Grep owed. |

## Counts — mechanically verified

- Rows in table: 40, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 0.
- UNREACHABLE proposed (`no_trigger_in_app`): 39 (rows 2–40).
- OPEN: 1 (row 1).
- confirmed_by: INFERRED 40 / SOURCE 0.
- **Verified for merge: 0 rows.** This part is UNVERIFIED until the main agent
  spot-checks 1 in 5, runs `py_compile`, and the Mac build/C1 return.

## Strict-entry caveat

No REACHABLE rows are proposed, so no row reverts under a strict launcher-entry
rule. For completeness: the launcher → FeedFetcherWorker → app `FeedParser` trunk
was NOT freshly printed in this pass (the app parser file itself was printed fresh;
its upstream starter was not), so if any future revision flips a row to REACHABLE,
that row must carry the strict-entry caveat until the starter is printed.

## Gaps the merger must close before merging

1. **Saved full-repo grep for rows 2–40** — any hit flips that row to REACHABLE.
   No `search_code` 0-result was used as absence evidence; the grep must be run on
   a full checkout (Mac) and its output saved in `scratch/`.
2. **Row 1 (`baseAdapters.BR.<init>`)** — printed generated/library source for
   `androidx.databinding.library.baseAdapters.BR`, or a saved class-name grep
   (rule F / C5), before any UNREACHABLE label. Until then it stays OPEN and must
   not be merged as UNREACHABLE. Do not copy the prior graph_def claim for this row
   without that evidence.
3. **No other gap:** all 40 plan rows are judged (39 proposed, 1 OPEN); no row was
   guessed, no row rests on a 429 response, and no row rests on the Agent 50 audit
   alone — the audit's caller-set claims were re-checked against the fresh prints
   above and held (CoreFeedParser caller set, FeedHandler 3-arg constructions,
   EzRss01Parser build-only use of EzRssTorrentItem).

## Not claimed

No build, sampler, grep, or C1 check was run — a true git clone of the repo fails
in this VM with no credential device (named missing check, not passed); build and
C1 run on the user's Mac after a push, so both are marked "not run" here.
No push was made (task instruction). Nothing was edited in `graph_def.py`, `out/`,
`PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.
