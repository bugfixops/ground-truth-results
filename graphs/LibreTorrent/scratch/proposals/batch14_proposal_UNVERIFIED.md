# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# WP1 LibreTorrent — Batch 14 PROPOSAL ONLY (pending, NOT pushable, NOT merged)

- Repo: bugfixops/ground-truth-results. Source branch given: work-2026-10-31.
- Output branch given: result, head 7a4a73016a43f3336be4a739542ef16157a7d089. **I did not push to result, work-2026-10-31, or main, and I edited nothing.**
- Status of this batch: **PROPOSED / PENDING verification — do NOT mark pushable.** Under the updated push rule, a batch is pushed only after it is verified (C1 checks where applicable). Verification here genuinely requires (a) a full-repo caller grep for the UNREACHABLE claims and (b) running tools/build_graph.py on a full checkout. This VM has no local clone and I cannot run tools/build_graph.py locally on a full checkout, so I report no build count at all and this batch must be reported as pending, not pushed as verified work.
- No tool coverage (Monkey, APE, coverage_baseline.json, sanity_check.csv, JaCoCo), old generated graphs, or build REACHABLE counts were used as evidence.
- confirmed_by: SOURCE means I printed the defining lines in this session from the connector; INFERRED is used only where stated. No DYN, FW-MEMORY, or UNVERIFIED. No framework claim below cites fw_src lines, because no fw_src file was printed in this session; framework/library dispatch is therefore INFERRED / "source not read" where it matters.

## Path shorthand (all under final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/)

- FP = com/ernieyu/feedparser/ ; FPI = FP + impl/ ; FPM = FP + mediarss/
- CORE = org/proninyaroslav/libretorrent/core/FeedParser.java (the app class, NOT the feedparser interface FP/FeedParser.java)
- WORKER = org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java
- SCHED = org/proninyaroslav/libretorrent/service/Scheduler.java
- Printed in full in this session: FPI/MediaRssParser.java, FPI/Rss1Feed.java, FPI/Rss1Item.java, FPI/Rss2Feed.java, FPI/Rss2Item.java, FPM/Content.java, FPM/Hash.java, FPM/MediaRss.java, FPI/FeedHandler.java, FPI/DefaultFeedParser.java, FPI/BaseItem.java, FPI/BaseElement.java, FPI/EzRss01Parser.java, FP/FeedParserFactory.java, FP/FeedParser.java, FP/Feed.java, FP/Item.java, CORE, WORKER, SCHED (enqueue lines only, SCHED:112-124).

## Batch-plan re-check (do not copy AGENT_NOTES blindly)

- handoff/LIBRETORRENT_BATCH_PLAN.tsv, batch 14 = exactly 40 rows, numbered 1–40 below.
- In the plan itself every batch-14 row is status TODO_CANDIDATE_REACHABLE with current_label "REACHABLE (generator candidate, no hand route yet)". Those are candidates, not evidence.
- graphs/LibreTorrent/AGENT_NOTES.md "Current status" (line 9) and its batch log (line 144), and graphs/LibreTorrent/scratch/batch_014.md, all say batch 14 = 8 supported UNREACHABLE + 32 OPEN.
- **My independent re-check does NOT reproduce that composition.** I propose 6 UNREACHABLE (no_trigger_in_app), 34 OPEN, 0 REACHABLE. The difference is the two getDescription methods (see #11/#24): the prior audit missed a caller in the bundled parser source.

## Candidate local chain for the 32 chain-OPEN methods (why they are OPEN, not REACHABLE)

Printed, in order: SCHED:112-124 enqueues a PeriodicWorkRequest for FeedFetcherWorker with ACTION_FETCH_ALL_CHANNELS → [WorkManager dispatch to Worker.doWork: NOT printed, library source not read — INFERRED] → WORKER doWork → fetchChannel → WORKER:156 `new FeedParser(...)` and WORKER:165 `parser.getItems()`, WORKER:176 `parser.getTitle()` → CORE:71 `FeedParserFactory.newParser().parse(bsStream)` → FPI/DefaultFeedParser: parse creates FeedHandler and calls `parser.parse(..., handler)` → [SAX dispatch to FeedHandler.startElement: NOT printed from JDK/AOSP source — INFERRED] → FPI/FeedHandler:62,69,85,88 construct Rss1Feed/Rss2Feed/Rss1Item/Rss2Item → CORE:86 feed.getTitle(), CORE:95 feed.getItemList(), CORE:96/104/110 item.getLinks()/getPubDate()/getTitle(), CORE:170 item.getEnclosures(), CORE:190 item.getMediaRss(), CORE:238 item.getEzRssTorrentItem(), CORE:256 item.getGuid() → FPI/Rss2Item:115 `new MediaRssParser(this).parse()` → FPI/MediaRssParser:33-35 parseContent/parseHash/parsePeerLinks → FPI/MediaRssParser:52 `new Content`, :68 `new Hash` → CORE:199/202 content.getUrl()/getType(), CORE:224 hash.getAlgorithm().
Because the two dispatch steps are unprinted, no method in this chain can yet be labelled REACHABLE with a complete route from an entry point. They are OPEN, not REACHABLE and not UNREACHABLE.

## Proposed labels — batch 14, all 40

| # | Method (JVM descriptor) | Proposed | Kind / reason + printed-source citation |
|---|---|---|---|
| 1 | MediaRssParser.isMediaRssElement (Lcom/ernieyu/feedparser/Element;)Z | OPEN | Local chain only: called FPI/MediaRssParser:45,60,81 from parseContent/parseHash/parsePeerLinks. Complete route OPEN (WorkManager + SAX dispatch unprinted). SOURCE (definition FPI/MediaRssParser:94-97). |
| 2 | MediaRssParser.parse ()Lcom/ernieyu/feedparser/mediarss/MediaRss; | OPEN | Called FPI/Rss2Item:115 via `new MediaRssParser(this).parse()`. Complete route OPEN (see chain). SOURCE (FPI/MediaRssParser:29-38). |
| 3 | MediaRssParser.parseContent ()Ljava/util/List; | OPEN | Called FPI/MediaRssParser:33 from parse(). Complete route OPEN. SOURCE (FPI/MediaRssParser:40-56). |
| 4 | MediaRssParser.parseHash ()Lcom/ernieyu/feedparser/mediarss/Hash; | OPEN | Called FPI/MediaRssParser:34 from parse(). Complete route OPEN. SOURCE (FPI/MediaRssParser:58-74). |
| 5 | MediaRssParser.parsePeerLinks ()Ljava/util/List; | OPEN | Called FPI/MediaRssParser:35 from parse(). Complete route OPEN. SOURCE (FPI/MediaRssParser:76-92). |
| 6 | Rss1Feed.<init> (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | OPEN | Constructed FPI/FeedHandler:62 for an `rdf` element. SAX dispatch to startElement unprinted, so route OPEN. SOURCE (FPI/Rss1Feed:36-38). |
| 7 | Rss1Feed.getItemList ()Ljava/util/List; | OPEN | Interface dispatch from CORE:95 `feed.getItemList()` (polymorphic; Rss1 feed when type is RSS_1_0). Complete route OPEN. SOURCE (FPI/Rss1Feed:103-115). |
| 8 | Rss1Feed.getTitle ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:86 `feed.getTitle()`. Complete route OPEN. SOURCE (FPI/Rss1Feed:46-50). |
| 9 | Rss1Feed.toString ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app. Definition FPI/Rss1Feed:120-122 (`return getTitle()`). No call found in the files printed in full in this session (CORE, FPI/MediaRssParser, FPI/FeedHandler, FPI/DefaultFeedParser, FPI/EzRss01Parser contain no call to it; the `toString` hit in FeedHandler is unrelated string handling). PENDING full-repo caller grep before merge — see Blockers. SOURCE for definition; label pending C1 grep. |
| 10 | Rss1Item.<init> (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | OPEN | Constructed FPI/FeedHandler:85 for RSS_1_0 `item`. SAX dispatch unprinted, so route OPEN. SOURCE (FPI/Rss1Item:29-31). |
| 11 | Rss1Item.getDescription ()Ljava/lang/String; | OPEN — NOT the prior UNREACHABLE | Prior scratch/batch_014.md called this UNREACHABLE/no_trigger_in_app ("core parser consumes other item fields"). That reason is incomplete: FPI/BaseItem:41 calls `getDescription()` polymorphically from `getUniqueId()`, and FPI/BaseItem:56-57 (equals) and :67 (hashCode) call `getUniqueId()`. So getDescription has a bundled-source caller path; whether BaseItem.equals/hashCode are themselves triggered from an entry point was not established in this session (they are not batch-14 rows and their callers were not printed). It cannot be labelled no_trigger_in_app on current evidence. SOURCE (FPI/Rss1Item:56-59; FPI/BaseItem:30-44,53-69). Decision needed: audit BaseItem.equals/hashCode callers. |
| 12 | Rss1Item.getEnclosures ()Ljava/util/List; | OPEN | Interface dispatch from CORE:170 `item.getEnclosures()` via watchEnclosure. Complete route OPEN. SOURCE (FPI/Rss1Item:88-105). |
| 13 | Rss1Item.getEzRssTorrentItem ()Lcom/ernieyu/feedparser/EzRssTorrentItem; | OPEN | Interface dispatch from CORE:238 `item.getEzRssTorrentItem()`; Rss1 implementation returns null (FPI/Rss1Item:121-123, "Not supported"), but the dispatch itself is on the printed route. Complete route OPEN. SOURCE. |
| 14 | Rss1Item.getGuid ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:256 `item.getGuid()` via watchGuid. Complete route OPEN. SOURCE (FPI/Rss1Item:69-73). |
| 15 | Rss1Item.getLinks ()Ljava/util/List; | OPEN | Interface dispatch from CORE:96 `item.getLinks()`. Complete route OPEN. SOURCE (FPI/Rss1Item:45-53). |
| 16 | Rss1Item.getMediaRss ()Lcom/ernieyu/feedparser/mediarss/MediaRss; | OPEN | Interface dispatch from CORE:190 `item.getMediaRss()`; Rss1 implementation returns null (FPI/Rss1Item:112-114, "Not supported"), but the dispatch is on the printed route. Complete route OPEN. SOURCE. |
| 17 | Rss1Item.getPubDate ()Ljava/util/Date; | OPEN | Interface dispatch from CORE:104 `item.getPubDate()`. Complete route OPEN. SOURCE (FPI/Rss1Item:76-80). |
| 18 | Rss1Item.getTitle ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:110 `item.getTitle()`. Complete route OPEN. SOURCE (FPI/Rss1Item:39-42). |
| 19 | Rss2Feed.<init> (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | OPEN | Constructed FPI/FeedHandler:69 for an `rss` element. SAX dispatch unprinted, so route OPEN. SOURCE (FPI/Rss2Feed:37-39). |
| 20 | Rss2Feed.getItemList ()Ljava/util/List; | OPEN | Interface dispatch from CORE:95. Complete route OPEN. SOURCE (FPI/Rss2Feed:113-129). |
| 21 | Rss2Feed.getTitle ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:86. Complete route OPEN. SOURCE (FPI/Rss2Feed:47-51). |
| 22 | Rss2Feed.toString ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app. Definition FPI/Rss2Feed:134-136 (`return getTitle()`). No call found in the files printed in full in this session (same audit as #9). PENDING full-repo caller grep before merge. SOURCE for definition; label pending C1 grep. |
| 23 | Rss2Item.<init> (Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V | OPEN | Constructed FPI/FeedHandler:88 for RSS_2_0 `item`. SAX dispatch unprinted, so route OPEN. SOURCE (FPI/Rss2Item:30-32). |
| 24 | Rss2Item.getDescription ()Ljava/lang/String; | OPEN — NOT the prior UNREACHABLE | Same correction as #11: FPI/BaseItem:41 calls getDescription() from getUniqueId(), called by BaseItem.equals:56-57 and hashCode:67. Whether those are triggered is unestablished. SOURCE (FPI/Rss2Item:57-60; FPI/BaseItem:30-44,53-69). Decision needed: audit BaseItem.equals/hashCode callers. |
| 25 | Rss2Item.getEnclosures ()Ljava/util/List; | OPEN | Interface dispatch from CORE:170. Complete route OPEN. SOURCE (FPI/Rss2Item:94-111). |
| 26 | Rss2Item.getEzRssTorrentItem ()Lcom/ernieyu/feedparser/EzRssTorrentItem; | OPEN | Interface dispatch from CORE:238; implementation FPI/Rss2Item:119-121 calls `new EzRss01Parser(this).parse()`. Complete route OPEN. SOURCE. |
| 27 | Rss2Item.getGuid ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:256. Complete route OPEN. SOURCE (FPI/Rss2Item:69-72). |
| 28 | Rss2Item.getLinks ()Ljava/util/List; | OPEN | Interface dispatch from CORE:96. Complete route OPEN. SOURCE (FPI/Rss2Item:46-54). |
| 29 | Rss2Item.getMediaRss ()Lcom/ernieyu/feedparser/mediarss/MediaRss; | OPEN | Implementation FPI/Rss2Item:114-116 calls `new MediaRssParser(this).parse()`; interface dispatch from CORE:190. Complete route OPEN. SOURCE. |
| 30 | Rss2Item.getPubDate ()Ljava/util/Date; | OPEN | Interface dispatch from CORE:104. Complete route OPEN. SOURCE (FPI/Rss2Item:75-78). |
| 31 | Rss2Item.getTitle ()Ljava/lang/String; | OPEN | Interface dispatch from CORE:110. Complete route OPEN. SOURCE (FPI/Rss2Item:40-43). |
| 32 | Content.<init> (Ljava/lang/String;Ljava/lang/String;)V | OPEN | Constructed FPI/MediaRssParser:52 in parseContent. Complete route OPEN (via #29/#2). SOURCE (FPM/Content:36-39). |
| 33 | Content.equals (Ljava/lang/Object;)Z | UNREACHABLE | no_trigger_in_app. Definition FPM/Content:64-74. No call found in the files printed in full in this session; CORE iterates Content only via getUrl()/getType() (CORE:199,202) and never compares Content objects. PENDING full-repo caller grep (including any Set/Map use) before merge. SOURCE for definition; label pending C1 grep. |
| 34 | Content.getType ()Ljava/lang/String; | OPEN | Called CORE:202 `content.getType()` in watchMediaContent. Complete route OPEN. SOURCE (FPM/Content:59-61). |
| 35 | Content.getUrl ()Ljava/lang/String; | OPEN | Called CORE:199 `content.getUrl()` in watchMediaContent. Complete route OPEN. SOURCE (FPM/Content:48-50). |
| 36 | Content.hashCode ()I | UNREACHABLE | no_trigger_in_app. Definition FPM/Content:76-80. No call found in the files printed in full in this session; no hashed collection of Content is printed. PENDING full-repo caller grep before merge. SOURCE for definition; label pending C1 grep. |
| 37 | Content.toString ()Ljava/lang/String; | UNREACHABLE | no_trigger_in_app. Definition FPM/Content:84-89. No call found in the files printed in full in this session. Note: FPM/MediaRss.toString concatenates its content list, which would invoke Content.toString if MediaRss.toString were called — no caller of MediaRss.toString was printed in this session, so this remains pending that audit too. PENDING full-repo caller grep before merge. SOURCE for definition; label pending C1 grep. |
| 38 | Hash.<init> (Ljava/lang/String;)V | OPEN | Constructed FPI/MediaRssParser:68 in parseHash. Complete route OPEN (via #29/#2). SOURCE (FPM/Hash:21-23). |
| 39 | Hash.equals (Ljava/lang/Object;)Z | UNREACHABLE | no_trigger_in_app. Definition FPM/Hash:55-65. No call found in the files printed in full in this session; CORE uses Hash only via getValue()/getAlgorithm() (CORE:221,224) and never compares Hash objects. PENDING full-repo caller grep before merge. SOURCE for definition; label pending C1 grep. |
| 40 | Hash.getAlgorithm ()Ljava/lang/String; | OPEN | Called CORE:224 `hash.getAlgorithm()` in watchMediaHash. Complete route OPEN. SOURCE (FPM/Hash:44-46). |

Counts proposed: 40 rows total; 0 REACHABLE; 6 UNREACHABLE (all no_trigger_in_app, all pending C1 grep); 34 OPEN (32 with a printed local caller chain + 2 getDescription methods whose only printed caller path is via BaseItem.equals/hashCode).

## Methods I could not label, and why

- All 34 OPEN rows above: I could not label them REACHABLE because two dispatch steps on their only printed route are unprinted — WorkManager dispatch to FeedFetcherWorker.doWork, and SAX dispatch to FeedHandler.startElement — and the Scheduler caller itself was not printed. I could not label them UNREACHABLE because each has a printed local caller/constructor/dispatch on that chain. Forcing either label would invent evidence.
- The 6 UNREACHABLE proposals are also not final: they rest on absence of a call in the files I printed in full, plus upstream search_code spot checks (proninyaroslav/libretorrent, which matched the ground-truth source text for these files). The connector's search_code with repo:bugfixops/ground-truth-results returned 0/incomplete results, so I could not run a genuine full-repo grep from the connector alone. A C1 full-repo grep (including implicit toString/equals/hashCode uses, Set/Map storage, and MediaRss.toString callers) is required before any of the 6 is merged.

## Blockers / decisions needed (parent, not me)

1. C1 full-repo caller grep for the 6 UNREACHABLE proposals and for BaseItem.equals/hashCode (which decide #11/#24). Do not merge the 6 on this report alone.
2. Decision on the dispatch standard for the OPEN chain: is a WorkManager doWork edge + a SAX startElement edge acceptable as standard/non_standard with an INFERRED via, or is printed WorkManager/SAX dispatch source required before any of the 32 chain methods can become REACHABLE? This decides whether batch 14 can close as mostly REACHABLE or stays OPEN.
3. Branch-provenance caveat: I passed ref=work-2026-10-31 to get_file_contents, but the directory-listing URLs the connector returned carried ref=7a4a73016a43f3336be4a739542ef16157a7d089 (the result head named in the task). I could not independently confirm from the connector output that the printed feedparser lines came from work-2026-10-31 rather than result. The parent should confirm the two branches agree on these files, or re-fetch with an explicit work-branch check, before merging.
4. Rate-limit note: three handover files (AGENT_BRIEF_V2.md, CONVERSION_RECIPE.md, CHATGPT_PROMPT_LIBRETORRENT_3.md) first failed with HTTP 429 and were retried successfully after a delay; no content was invented for them.

## What I did not do

- No push, edit, or merge. No work on batch 13 or any other batch. Batch 14 is not merged and not done.
- This VM has no local clone; I did not run tools/build_graph.py, and I report no build, error, warning, or REACHABLE count.
