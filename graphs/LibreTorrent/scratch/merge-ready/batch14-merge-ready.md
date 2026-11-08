**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 14 — merge-ready file (UNVERIFIED proposal)

Scope: Feed-parser implementation classes: MediaRssParser, Rss1Feed/Rss1Item, Rss2Feed/Rss2Item, mediarss Content/Hash, plus mediarss rows carried into batch 15.

## Conventions used in this file (recorded, not decided)

- Status: UNVERIFIED proposal only. NOT verified for merge. No row in this file has passed spot-check, py_compile, build, or C1.
- confirmed_by is only SOURCE or INFERRED, never DYN / FW-MEMORY / UNVERIFIED.
- Batch 14 rule: every REACHABLE row is INFERRED because the route crosses two unprinted framework dispatches (WorkManager
  enqueue -> doWork, and SAX parser.parse -> FeedHandler.startElement). Batch 15/16 rule: SOURCE means a printed line names the
  method as a direct callee on a printed chain from the TorrentStreamServer anchor (ctor/start/stop/setter chains); INFERRED means
  the only printed path crosses Thread.start, a virtual/framework dispatch, or JVM class-load. The merger must reconcile the
  batch-14 whole-route rule with the batch-15/16 printed-callee rule project-wide; the two rules are NOT silently mixed here.
- Strict-entry caveat (undecided, applies to every REACHABLE row in this file): routes are anchored at FeedSettingsFragment
  preference change (batch 14) and TorrentEngine streaming start (batches 15/16). No launcher -> settings-page and no
  launcher -> TorrentService/TorrentEngine step was printed in this pass. Under a strict printed-launcher-entry rule, all
  REACHABLE rows in this file revert to OPEN. Recorded, not decided.
- UNREACHABLE proposed rows are all INFERRED and grep-owed: a saved full-repo grep (rule-F/C5 form) for the method name must be
  run before merge. A saved grep hit for a live caller flips that row to REACHABLE; a grep hit for a trigger of
  BaseItem.equals/hashCode flips batch 14 rows 11/24 to REACHABLE. No connector search_code 0-result was used as absence evidence
  anywhere in this file, and no row was flipped from OPEN to UNREACHABLE on absence alone without a named grep target.
- Plan labels were NOT adopted: every batch 14-16 plan row is TODO_CANDIDATE_REACHABLE with the generator label
  "REACHABLE (generator candidate, no hand route yet)". Verdicts below were re-derived from printed source, not copied from the
  plan, from prior proposals, or from corrected files (those were leads only; where this file agrees with a corrected file, the
  agreement is a check result, not a copy).
- Build: NOT RUN (runs on the user's Mac after a push). C1: NOT RUN. Never claimed passed.
- Push: 5e0983f (UNVERIFIED, before [L]). Pushes are held until LibreTorrent labels are verified and merged to [L].

## Sources printed fresh in this session (branch work-2026-10-31, GitHub connector, one file at a time)

Root for app sources: final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
- com/ernieyu/feedparser/impl/MediaRssParser.java (98 lines), Rss1Feed.java (123), Rss1Item.java (124), Rss2Feed.java (137),
  Rss2Item.java (122), BaseItem.java (70), FeedHandler.java (132), DefaultFeedParser.java (48)
- com/ernieyu/feedparser/mediarss/Content.java (90), Hash.java (81), MediaRss.java (50), PeerLink.java (69)
- org/proninyaroslav/libretorrent/core/FeedParser.java (267 lines, core parser)
- org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java (270), Scheduler.java (145)
- org/proninyaroslav/libretorrent/ui/settings/sections/FeedSettingsFragment.java (163)
- org/nanohttpd/NanoHTTPD.java (1850 lines)
- org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java (284)
- org/proninyaroslav/libretorrent/core/model/TorrentEngine.java (1658; streaming sections :1050-1085 read in full)
All 19 files fetched via the GitHub connector in this session; the feedparser, NanoHTTPD, TorrentStreamServer and TorrentEngine
files are byte-identical to prior local copies where one existed. No fresh HTTP 429 occurred in this pass.
Plan: handoff/LIBRETORRENT_BATCH_PLAN.tsv, local copy ~/workspace/agent27-plan.tsv, 4732 rows + header.
NOTE on plan hash: the local copy hashes to sha256 f4860569052b365233459da8d527a568fdb54d3f1fa5073e36ac03c4ebe9fd3e
(sha1 afedc8af26fd3564ea03b7197f2a99cf2b7ce8bb), which does NOT match the 0104806d... prefix recorded in handoff memory.
Membership below was verified row-for-row against the local copy (40 rows per batch, plan order, names + descriptors exact);
the main agent should confirm the local copy matches the branch plan before merge. This discrepancy is flagged, not hidden.

## Shared trunk (freshly printed this session)

FeedSettingsFragment.bindOnPreferenceChangeListener :119-122 registers `setOnPreferenceChangeListener(this)` (:121);
onPreferenceChange :124+ calls Scheduler.runPeriodicalRefreshFeeds at :134 (auto-refresh toggle) and :142 (interval change).
Scheduler.runPeriodicalRefreshFeeds :112-125 builds Data with FeedFetcherWorker.ACTION_FETCH_ALL_CHANNELS (:114) and enqueues a
PeriodicWorkRequest via WorkManager (:124) — the WorkManager dispatch to FeedFetcherWorker.doWork is unprinted, hence INFERRED.
FeedFetcherWorker.doWork :74-105 dispatches ACTION_FETCH_CHANNEL (:93-94) -> fetchChannel, ACTION_FETCH_CHANNEL_LIST (:96-97) ->
fetchChannelsByUrl (:107-115, fetchChannel :115), ACTION_FETCH_ALL_CHANNELS (:99-100) -> fetchChannels (:124-142, fetchChannel :134).
fetchChannel :144-187 constructs core FeedParser (:156), calls parser.getItems() (:165) and parser.getTitle() (:176).
Core FeedParser ctor :62-82 calls FeedParserFactory.newParser().parse(bsStream) (:71); DefaultFeedParser.parse :22-47 constructs
FeedHandler (:34), calls parser.parse(..., handler) (:37, SAX dispatch INFERRED) and handler.getFeed() (:38).
FeedHandler.startElement constructs Rss1Feed (:62), Rss2Feed (:69), Rss1Item (:85), Rss2Item (:88).
Core getTitle :84-87 (feed.getTitle :86); getItems :89-116+ (feed.getItemList :95, item.getLinks :96, item.getPubDate :104,
item.getTitle :110, item.getEnclosures :170, item.getMediaRss :190, item.getEzRssTorrentItem :238, item.getGuid :256);
watchMediaContent :188-207 (item.getMediaRss :190, media.getContent :194, content.getUrl :199, content.getType :202,
watchMediaHash :201/:207); watchMediaHash :215-229 (media.getHash :217, hash.getValue :221, hash.getAlgorithm :224).
Gates on this trunk: STATE settings (feed auto-refresh preference + interval) and ENV network (WorkManager constraint,
Scheduler.getRefreshFeedsConstraints: CONNECTED minimum, NOT_ROAMING/UNMETERED per settings).
Trap avoided: feed-level Rss1Feed.getDescription (:67) / Rss2Feed.getDescription (:68) are DIFFERENT methods from item rows 11/24
and are not cited for them. Rss1Item.getMediaRss returns null (:112-114) and Rss1Item.getEzRssTorrentItem returns null (:121-123);
both methods still run via core getItems, so they are REACHABLE, not UNREACHABLE.

## Table (plan order)

| # | Method | JVM descriptor | Proposed label | confirmed_by | Route / reason |
|---:|--------|---------------|----------------|--------------|----------------|
| 1 | MediaRssParser.isMediaRssElement | `(Lcom/ernieyu/feedparser/Element;)Z` | REACHABLE proposed | INFERRED | MediaRssParser.parseContent :45 / parseHash :60 / parsePeerLinks :81; reached via parse :29-38 <- Rss2Item.getMediaRss :115 <- core getItems :190. WorkManager+SAX dispatch unprinted, hence INFERRED. |
| 2 | MediaRssParser.parse | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | REACHABLE proposed | INFERRED | Def MediaRssParser :29-38 (parseContent :33, parseHash :34, parsePeerLinks :35, new MediaRss :37); caller Rss2Item.getMediaRss :115 <- core getItems :190. Dispatch unprinted, hence INFERRED. |
| 3 | MediaRssParser.parseContent | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :40-56 (isMediaRssElement :45, new Content :52); caller parse :33 <- Rss2Item.getMediaRss :115 <- core getItems :190. INFERRED as row 2. |
| 4 | MediaRssParser.parseHash | `()Lcom/ernieyu/feedparser/mediarss/Hash;` | REACHABLE proposed | INFERRED | Def :58-74 (isMediaRssElement :60, new Hash :68, setAlgorithm :71); caller parse :34. INFERRED as row 2. |
| 5 | MediaRssParser.parsePeerLinks | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :76-92 (isMediaRssElement :81, new PeerLink :88); caller parse :35. INFERRED as row 2. |
| 6 | Rss1Feed.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | REACHABLE proposed | INFERRED | Def Rss1Feed :36-38; constructed FeedHandler.startElement :62 (SAX dispatch INFERRED). |
| 7 | Rss1Feed.getItemList | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :103-116; caller core FeedParser.getItems :95 (feed.getItemList). INFERRED: feed object arrives via SAX dispatch. |
| 8 | Rss1Feed.getTitle | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :46-50; caller core FeedParser.getTitle :86 (feed.getTitle). INFERRED as row 7. |
| 9 | Rss1Feed.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :120-122. No printed caller in the fresh corpus (FeedParser-core, FeedHandler, DefaultFeedParser, all feedparser impl files). Proposed only; saved full-repo grep owed before merge. |
| 10 | Rss1Item.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | REACHABLE proposed | INFERRED | Def Rss1Item :29-31; constructed FeedHandler :85 (SAX dispatch INFERRED). |
| 11 | Rss1Item.getDescription | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :56-59. Only printed caller path is BaseItem.getUniqueId :41, which runs only via BaseItem.equals :56-57 / hashCode :67, both proposed UNREACHABLE in batch 13 with no printed trigger. Flips to REACHABLE iff a saved grep finds a trigger for BaseItem.equals/hashCode. Proposed only; grep owed. |
| 12 | Rss1Item.getEnclosures | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :88-105; caller core getItems :170 (item.getEnclosures). INFERRED as row 7. |
| 13 | Rss1Item.getEzRssTorrentItem | `()Lcom/ernieyu/feedparser/EzRssTorrentItem;` | REACHABLE proposed | INFERRED | Def :121-123 (returns null); caller core getItems :238 (item.getEzRssTorrentItem). Method runs even though it returns null. INFERRED as row 7. |
| 14 | Rss1Item.getGuid | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :69-73; caller core getItems :256 (item.getGuid). INFERRED as row 7. (BaseItem.getUniqueId :32 is a second, conditional path via equals/hashCode; not needed.) |
| 15 | Rss1Item.getLinks | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :45-53; caller core getItems :96 (item.getLinks). INFERRED as row 7. |
| 16 | Rss1Item.getMediaRss | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | REACHABLE proposed | INFERRED | Def :112-114 (returns null); caller core getItems :190 (item.getMediaRss). INFERRED as row 7. |
| 17 | Rss1Item.getPubDate | `()Ljava/util/Date;` | REACHABLE proposed | INFERRED | Def :76-80; caller core getItems :104 (item.getPubDate). INFERRED as row 7. |
| 18 | Rss1Item.getTitle | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :39-42; caller core getItems :110 (item.getTitle). INFERRED as row 7. |
| 19 | Rss2Feed.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | REACHABLE proposed | INFERRED | Def Rss2Feed :37-39; constructed FeedHandler :69 (SAX dispatch INFERRED). |
| 20 | Rss2Feed.getItemList | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :113-130; caller core getItems :95. INFERRED as row 7. |
| 21 | Rss2Feed.getTitle | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :47-51; caller core getTitle :86. INFERRED as row 7. |
| 22 | Rss2Feed.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :134-136. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 23 | Rss2Item.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | REACHABLE proposed | INFERRED | Def Rss2Item :30-32; constructed FeedHandler :88 (SAX dispatch INFERRED). |
| 24 | Rss2Item.getDescription | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :57-60. Same BaseItem.getUniqueId-only path as row 11 (BaseItem :41 <- equals :56-57 / hashCode :67, both batch-13-proposed-UNREACHABLE). Flips on a saved grep trigger for BaseItem.equals/hashCode. Proposed only; grep owed. |
| 25 | Rss2Item.getEnclosures | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :94-111; caller core getItems :170. INFERRED as row 7. |
| 26 | Rss2Item.getEzRssTorrentItem | `()Lcom/ernieyu/feedparser/EzRssTorrentItem;` | REACHABLE proposed | INFERRED | Def :119-121 (new EzRss01Parser(this).parse()); caller core getItems :238. INFERRED as row 7. |
| 27 | Rss2Item.getGuid | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :69-72; caller core getItems :256. INFERRED as row 7. |
| 28 | Rss2Item.getLinks | `()Ljava/util/List;` | REACHABLE proposed | INFERRED | Def :46-54; caller core getItems :96. INFERRED as row 7. |
| 29 | Rss2Item.getMediaRss | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | REACHABLE proposed | INFERRED | Def :114-116 (new MediaRssParser(this).parse() :115); caller core getItems :190. INFERRED as row 7. |
| 30 | Rss2Item.getPubDate | `()Ljava/util/Date;` | REACHABLE proposed | INFERRED | Def :75-78; caller core getItems :104. INFERRED as row 7. |
| 31 | Rss2Item.getTitle | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :40-43; caller core getItems :110. INFERRED as row 7. |
| 32 | Content.<init> | `(Ljava/lang/String;Ljava/lang/String;)V` | REACHABLE proposed | INFERRED | Def Content :36-39; constructed MediaRssParser.parseContent :52. INFERRED as row 3. |
| 33 | Content.equals | `(Ljava/lang/Object;)Z` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :64-73. No printed caller in the fresh corpus (no comparison/log site). Proposed only; saved full-repo grep owed before merge. |
| 34 | Content.getType | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :59-61; caller core watchMediaContent :202 (content.getType). INFERRED as row 7. |
| 35 | Content.getUrl | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :48-50; caller core watchMediaContent :199 (content.getUrl). INFERRED as row 7. |
| 36 | Content.hashCode | `()I` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :76-80. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 37 | Content.toString | `()Ljava/lang/String;` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :84-89. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 38 | Hash.<init> | `(Ljava/lang/String;)V` | REACHABLE proposed | INFERRED | Def Hash :21-23; constructed MediaRssParser.parseHash :68. INFERRED as row 4. |
| 39 | Hash.equals | `(Ljava/lang/Object;)Z` | UNREACHABLE proposed no_trigger_in_app | INFERRED | Def :55-64. No printed caller in the fresh corpus. Proposed only; saved full-repo grep owed before merge. |
| 40 | Hash.getAlgorithm | `()Ljava/lang/String;` | REACHABLE proposed | INFERRED | Def :44-46; caller core watchMediaHash :224 (hash.getAlgorithm). INFERRED as row 7. |

Counts: 32 REACHABLE proposed / 8 UNREACHABLE proposed / 0 OPEN, out of 40. Sequence 1-40 intact, plan order, names + descriptors from the plan TSV.

## Still owed before any merge (not claimed done)

- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1.
- Saved full-repo grep for every UNREACHABLE-proposed row and every OPEN row (none in this batch) before any merge.
- Strict-entry decision (see conventions) and batch-14 vs batch-15/16 confirmed_by reconciliation.
- For batch 14 rows 11/24: saved grep for a BaseItem.equals/hashCode trigger.
