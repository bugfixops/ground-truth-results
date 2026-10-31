# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# WP1 LibreTorrent — Batch 13 PROPOSED labels only (NOT verified, NOT merged, NOT pushed)

- Repo: bugfixops/ground-truth-results, source branch work-2026-10-31.
- Membership: handoff/LIBRETORRENT_BATCH_PLAN.tsv, batch == 13, exactly 40 rows, all status TODO_CANDIDATE_REACHABLE / current_label "REACHABLE (generator candidate, no hand route yet)" — those plan labels are candidates, not evidence, and were NOT used as evidence.
- Source root printed in this session (via github get_file_contents, branch work-2026-10-31):
  final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
  Short citations below are relative to that root.
- No tool coverage, old generated graphs, or build REACHABLE counts were used as evidence.
- This VM has no local clone and tools/build_graph.py was NOT run on a full checkout in this session; no build count is reported.
- Push rule (follow-up): do NOT push directly. This part is PROPOSED / PENDING, not pushable, because C1 verification (full-app grep for the 4 UNREACHABLE rows, plus a build) has not been done. If/when verified, the parent merges and pushes it as a separate commit to branch 'result' only, naming LibreTorrent batch 13 — never to work-2026-10-31 or main.

## Shared route trunk (printed in this session)

1. Scheduler.runPeriodicalRefreshFeeds — service/Scheduler.java:112-125 — builds a PeriodicWorkRequest for FeedFetcherWorker and enqueues it with WorkManager.
2. [WorkManager dispatch to FeedFetcherWorker.doWork — INFERRED, library source not read.]
3. FeedFetcherWorker.doWork:74 → fetchChannel (93/99/101 → 144) → new core FeedParser at service/FeedFetcherWorker.java:156 → parser.getItems() at :165.
4. core FeedParser.<init> — org/proninyaroslav/libretorrent/core/FeedParser.java:62-71 — fetches the feed URL (:67); only if the HTTP response is non-null does it call FeedParserFactory.newParser().parse(bsStream) at :71.
5. FeedParserFactory.newParser — com/ernieyu/feedparser/FeedParserFactory.java:23-25 — returns new DefaultFeedParser().
6. DefaultFeedParser.parse — com/ernieyu/feedparser/impl/DefaultFeedParser.java:22-38 — creates FeedHandler at :34, calls parser.parse(..., handler) at :37, then handler.getFeed() at :38.
7. [SAX dispatch to FeedHandler callbacks — INFERRED, JDK/SAX source not read; no FW-SRC citation is claimed. Registration itself is printed at DefaultFeedParser.java:37.]
8. FeedHandler.startElement — impl/FeedHandler.java:54-103 — ENTRY branch :94-96 creates AtomItem; ITEM+RSS_2_0 branch :87-88 creates Rss2Item; generic branch :100 creates BaseElement. endElement :110-126 calls setContent (:121) and addElement (:126).
9. core FeedParser.getItems — core/FeedParser.java:89-115 — loops feed.getItemList() (:95); AtomFeed.getItemList (impl/AtomFeed.java:94-102) returns the AtomItems, Rss2Feed.getItemList (impl/Rss2Feed.java:113-125) returns the Rss2Items.
10. Download-URL branch — core/FeedParser.java:101-102: only if no magnet/torrent link was found, findDownloadUrl (:141) runs watchMediaContent (:190, item.getMediaRss()), watchTorrentInfoHash (:238, item.getEzRssTorrentItem()) and watchGuid (:256, item.getGuid()).

Explicit app/library steps above are SOURCE (printed); steps 2 and 7 are INFERRED.

## Proposed labels (36 REACHABLE, 4 UNREACHABLE)

| # | Method | Proposed label | Kind | Reason / route / printed citation |
|---:|---|---|---|---|
| 1 | AtomItem.getEzRssTorrentItem | REACHABLE | — | Interface call core/FeedParser.java:238 via watchTorrentInfoHash; AtomItem body impl/AtomItem.java:136-137 returns null (caller :239 checks null). Trunk steps 1-10. |
| 2 | AtomItem.getGuid | REACHABLE | — | Interface call core/FeedParser.java:256 via watchGuid; body impl/AtomItem.java:74-76 calls getElement(ID) + getContent(). |
| 3 | AtomItem.getLinks | REACHABLE | — | Interface call core/FeedParser.java:96 in getItems loop; body impl/AtomItem.java:46-50 calls getElementList(LINK) + getAttributes(). |
| 4 | AtomItem.getMediaRss | REACHABLE | — | Interface call core/FeedParser.java:190 via watchMediaContent; AtomItem body impl/AtomItem.java:127-128 returns null (caller :191 checks null). |
| 5 | AtomItem.getPubDate | REACHABLE | — | Interface call core/FeedParser.java:104 in getItems loop; body impl/AtomItem.java:80-82 calls getElement(UPDATED) + getContent(). |
| 6 | AtomItem.getTitle | REACHABLE | — | Interface call core/FeedParser.java:110 in getItems loop; body impl/AtomItem.java:40-42 calls getElement(TITLE) + getContent(). |
| 7 | BaseElement.<init>(String,String,Attributes) | REACHABLE | — | Direct: FeedHandler.java:100 (generic element). Via super: BaseItem.java:21-22, AtomItem.java:30-31, Rss2Item.java:30-31. Body impl/BaseElement.java:39-42. |
| 8 | BaseElement.addElement | REACHABLE | — | FeedHandler.endElement impl/FeedHandler.java:124-126 (parent.addElement). Body impl/BaseElement.java:91-97. Via SAX dispatch (INFERRED). |
| 9 | BaseElement.getAttributes | REACHABLE | — | AtomItem.getLinks impl/AtomItem.java:50 (element.getAttributes()). Body impl/BaseElement.java:56-57. |
| 10 | BaseElement.getContent | REACHABLE | — | AtomItem getters impl/AtomItem.java:42,76,82; EzRss parsers impl/EzRss01Parser.java:44,52,60,70. Body impl/BaseElement.java:61-62. |
| 11 | BaseElement.getElement | REACHABLE | — | AtomItem getters impl/AtomItem.java:41,75,81; EzRss parsers impl/EzRss01Parser.java:40,48,56,64,80,88,96. Body impl/BaseElement.java:73-75. |
| 12 | BaseElement.getElementList | REACHABLE | — | AtomItem.getLinks impl/AtomItem.java:48. Body impl/BaseElement.java:79-80. |
| 13 | BaseElement.getUri | REACHABLE | — | EzRss01Parser.isEzRssElement impl/EzRss01Parser.java:118-120 (element.getUri()). Body impl/BaseElement.java:46-47. |
| 14 | BaseElement.setContent | REACHABLE | — | FeedHandler.endElement impl/FeedHandler.java:121 (currentElement.setContent). Body impl/BaseElement.java:68-69. Via SAX dispatch (INFERRED). |
| 15 | BaseItem.<init> | REACHABLE | — | Super-call from AtomItem.java:30-31 and Rss2Item.java:30-31, constructed in FeedHandler.java:85-96. Body impl/BaseItem.java:21-22, which calls BaseElement.<init> at :22. |
| 16 | BaseItem.equals | UNREACHABLE | no_trigger_in_app | No call in any printed feed-path file (full core/FeedParser.java, full FeedFetcherWorker.java, FeedHandler, parsers, AtomItem/Rss2Item). Its only printed callers are internal: it calls getUniqueId at impl/BaseItem.java:56-57. Duplicate filtering in FeedFetcherWorker.java:196-203 uses app FeedItem.title strings, not library Items. PENDING a full-app grep before C1 — see caveats. confirmed_by: INFERRED (absence over code not all read). |
| 17 | BaseItem.getUniqueId | UNREACHABLE | no_trigger_in_app | Private (impl/BaseItem.java:30). Only printed callers are equals :56-57 and hashCode :67, both proposed UNREACHABLE above. PENDING full-app grep (private, so no external caller is possible, but equals/hashCode triggers still need the grep). confirmed_by: INFERRED. |
| 18 | BaseItem.hashCode | UNREACHABLE | no_trigger_in_app | No call in any printed feed-path file; no library Item is placed in a hash collection in printed code (FeedFetcherWorker duplicates use String titles, :196-203). It calls getUniqueId at impl/BaseItem.java:67. PENDING full-app grep. confirmed_by: INFERRED. |
| 19 | BaseItem.toString | UNREACHABLE | no_trigger_in_app | No call, string concatenation, or log call on a library Item in any printed feed-path file (full core/FeedParser.java, full FeedFetcherWorker.java). Body impl/BaseItem.java:48-49 returns getTitle(). PENDING full-app grep. confirmed_by: INFERRED. |
| 20 | DefaultFeedParser.<init> | REACHABLE | — | Implicit default constructor (no explicit constructor in impl/DefaultFeedParser.java; class at :19). Called by FeedParserFactory.java:25 (new DefaultFeedParser()). |
| 21 | DefaultFeedParser.parse | REACHABLE | — | Called core/FeedParser.java:71 (FeedParserFactory.newParser().parse(bsStream)). Body impl/DefaultFeedParser.java:22-38. |
| 22 | EzRss01Parser.<init>(Rss2Item) | REACHABLE | — | Called Rss2Item.java:119-120 (new EzRss01Parser(this).parse(), RSS 2.0 items only). Body impl/EzRss01Parser.java:22-23. |
| 23 | EzRss01Parser.isEzRssElement | REACHABLE | — | Called by parseFileName/MagnetUri/InfoHash/ContentLength/Seeds/Peers/Verified at impl/EzRss01Parser.java:41,49,57,65,81,89,97. Body :118-120 calls getUri(). |
| 24 | EzRss01Parser.parse | REACHABLE | — | Called Rss2Item.java:120. Body impl/EzRss01Parser.java:26-36 unconditionally calls parseFileName, parseMagnetUri, parseInfoHash, parseContentLength, parseSeeds, parsePeers, parseVerified (:27-33). |
| 25 | EzRss01Parser.parseContentLength | REACHABLE | — | Called by parse() at impl/EzRss01Parser.java:30. Body :63-76. |
| 26 | EzRss01Parser.parseFileName | REACHABLE | — | Called by parse() at :27. Body :39-44 calls getElement + isEzRssElement + getContent. |
| 27 | EzRss01Parser.parseInfoHash | REACHABLE | — | Called by parse() at :29. Body :55-60. |
| 28 | EzRss01Parser.parseInt | REACHABLE | — | Called by parseSeeds :84, parsePeers :92, parseVerified :100. Body :105-115. (parseContentLength uses Long.parseLong directly, :70.) |
| 29 | EzRss01Parser.parseMagnetUri | REACHABLE | — | Called by parse() at :28. Body :47-52. |
| 30 | EzRss01Parser.parsePeers | REACHABLE | — | Called by parse() at :32. Body :87-92 calls getElement, isEzRssElement, parseInt. |
| 31 | EzRss01Parser.parseSeeds | REACHABLE | — | Called by parse() at :31. Body :79-84 calls getElement, isEzRssElement, parseInt. |
| 32 | EzRss01Parser.parseVerified | REACHABLE | — | Called by parse() at :33. Body :95-102 calls getElement, isEzRssElement, parseInt. |
| 33 | FeedHandler.<init> | REACHABLE | — | Implicit default constructor (no explicit constructor in impl/FeedHandler.java; class at :16). Called DefaultFeedParser.java:34 (new FeedHandler()). |
| 34 | FeedHandler.characters | REACHABLE | — | SAX callback; handler registered DefaultFeedParser.java:37. Body impl/FeedHandler.java:36-38 appends to buffer. Dispatch INFERRED. |
| 35 | FeedHandler.endDocument | REACHABLE | — | SAX callback; registered :37. Body impl/FeedHandler.java:48-50 clears elementStack. Dispatch INFERRED. |
| 36 | FeedHandler.endElement | REACHABLE | — | SAX callback; registered :37. Body impl/FeedHandler.java:110-126 calls setContent + addElement. Dispatch INFERRED. |
| 37 | FeedHandler.getFeed | REACHABLE | — | Explicit post-parse call DefaultFeedParser.java:38 (handler.getFeed()). Body impl/FeedHandler.java:31-32. |
| 38 | FeedHandler.startDocument | REACHABLE | — | SAX callback; registered :37. Body impl/FeedHandler.java:42-44 initialises elementStack. Dispatch INFERRED. |
| 39 | FeedHandler.startElement | REACHABLE | — | SAX callback; registered :37. Body impl/FeedHandler.java:54-103 creates AtomItem/Rss2Item/BaseElement per branch. Dispatch INFERRED. |
| 40 | MediaRssParser.<init>(Rss2Item) | REACHABLE | — | Called Rss2Item.java:114-115 (new MediaRssParser(this).parse(), RSS 2.0 items only, via core/FeedParser.java:190 interface call). Body impl/MediaRssParser.java:25-26. Note: MediaRssParser.parse itself is NOT a batch-13 row. |

Count check: 36 REACHABLE + 4 UNREACHABLE = 40. No row left OPEN in this proposal, but see caveats — the 4 UNREACHABLE rows and the two INFERRED dispatch steps are the verification gaps.

## Caveats / blockers / decisions needed (all block pushability, none was hidden)

1. NOT VERIFIED / NOT PUSHABLE under the updated push rule: C1 checks were not run, and tools/build_graph.py was not run — this VM has no local clone and I cannot run it on a full checkout from the connector-only working copy. Do not mark this batch pushable until the parent (or an eligible agent with a checkout) runs the build and C1 checks.
2. Full-app grep missing for BaseItem.equals/hashCode/toString: connector code search does not index bugfixops/ground-truth-results (repo-scoped search returned 0/incomplete; global search ignores the repo), and no local clone exists here. A real grep over the source root for `.equals(`, `hashCode`, `toString` on library Items, and for collections containing library Items, is still required before merging the 4 UNREACHABLE rows. If that grep finds any trigger, those rows flip to REACHABLE.
3. SAX dispatch (DefaultFeedParser.java:37 → FeedHandler callbacks) and WorkManager dispatch (Scheduler.java:124 → FeedFetcherWorker.doWork) are INFERRED — "source not read". No FW-SRC citation is claimed for either. The caller of Scheduler.runPeriodicalRefreshFeeds was also not printed in this session, so the trunk is anchored at Scheduler, not at a launcher entry, in this proposal.
4. Prior-note conflict, flagged not resolved by this proposal: graphs/LibreTorrent/AGENT_NOTES.md contains both an older helper audit (batch 13 all OPEN) and a later 2026-10-31 17:45 progress line claiming batch 13 was merged as parts/b013.py (36 REACHABLE, 4 UNREACHABLE), followed by a "Stopped by the user" note saying batches 13–18 are unverified and must be re-checked. This proposal was derived independently from printed source in this session and happens to give the same 36/4 split, but it does NOT confirm that parts/b013.py matches this table, and it does NOT claim batch 13 is merged or done.
5. AtomItem.getMediaRss / getEzRssTorrentItem return null for Atom items (AtomItem.java:127-128, 136-137); they are REACHABLE because the interface calls at core/FeedParser.java:190,238 do dispatch to them for Atom feeds — returning null is not unreachability. The non-null MediaRss/EzRss results come from the Rss2Item overrides (Rss2Item.java:114-115, 119-120), which are not batch-13 rows.

## Separately reported, NOT folded into batch 13 — batch 12 OPEN_NO_SOURCE row

- databinding.DataBinderMapperImpl.<init> (batch 12, plan status OPEN_NO_SOURCE): per graphs/LibreTorrent/AGENT_NOTES.md "Blocked" section, the build labels it UNREACHABLE unclassified with 0 incoming edges; the upload has no databinding/DataBinderMapperImpl.java; libretorrent.DataBinderMapperImpl exists only in build output (1 incoming edge). It needs a source file, or a decision on whether it is generated code outside the upload. Left unresolved here, as instructed.
- Also noted in AGENT_NOTES.md "Blocked": drawer.TagItem.equals (batch 113) needs a DiffUtil route via ui/main/drawer/TagsAdapter.java:137 and must not get no_trigger_in_app — not batch 13, not addressed here.
