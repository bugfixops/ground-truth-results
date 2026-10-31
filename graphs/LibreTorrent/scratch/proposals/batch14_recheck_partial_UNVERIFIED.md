# UNVERIFIED RE-CHECK — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a re-check part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged. Batches 13-18 were unverified when the Claude run stopped.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# LibreTorrent batch 14 — PARTIAL re-check (connector rate-limited, no verdicts derived)

Status: 0 methods judged, 40 OPEN. No REACHABLE/UNREACHABLE label is proposed as verified in this run.
Reason: batch plan was fetched successfully, then the next GitHub connector call returned `Error: MCP request failed with HTTP 429: too many requests`. Per rate-limit rules no further GitHub calls were made, retried, or delegated.
Prior unverified proposal counts (0 REACHABLE / 6 UNREACHABLE / 34 OPEN, per task description only) were NOT re-read and are NOT carried over as evidence.

| # | method | descriptor | proposed label | confirmed_by | reason / remains |
|---:|---|---|---|---|---|
| 1 | MediaRssParser.isMediaRssElement | `(Lcom/ernieyu/feedparser/Element;)Z` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 2 | MediaRssParser.parse | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 3 | MediaRssParser.parseContent | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 4 | MediaRssParser.parseHash | `()Lcom/ernieyu/feedparser/mediarss/Hash;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 5 | MediaRssParser.parsePeerLinks | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 6 | Rss1Feed.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 7 | Rss1Feed.getItemList | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 8 | Rss1Feed.getTitle | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 9 | Rss1Feed.toString | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 10 | Rss1Item.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 11 | Rss1Item.getDescription | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 12 | Rss1Item.getEnclosures | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 13 | Rss1Item.getEzRssTorrentItem | `()Lcom/ernieyu/feedparser/EzRssTorrentItem;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 14 | Rss1Item.getGuid | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 15 | Rss1Item.getLinks | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 16 | Rss1Item.getMediaRss | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 17 | Rss1Item.getPubDate | `()Ljava/util/Date;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 18 | Rss1Item.getTitle | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 19 | Rss2Feed.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 20 | Rss2Feed.getItemList | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 21 | Rss2Feed.getTitle | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 22 | Rss2Feed.toString | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 23 | Rss2Item.<init> | `(Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 24 | Rss2Item.getDescription | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 25 | Rss2Item.getEnclosures | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 26 | Rss2Item.getEzRssTorrentItem | `()Lcom/ernieyu/feedparser/EzRssTorrentItem;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 27 | Rss2Item.getGuid | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 28 | Rss2Item.getLinks | `()Ljava/util/List;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 29 | Rss2Item.getMediaRss | `()Lcom/ernieyu/feedparser/mediarss/MediaRss;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 30 | Rss2Item.getPubDate | `()Ljava/util/Date;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 31 | Rss2Item.getTitle | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 32 | Content.<init> | `(Ljava/lang/String;Ljava/lang/String;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 33 | Content.equals | `(Ljava/lang/Object;)Z` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 34 | Content.getType | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 35 | Content.getUrl | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 36 | Content.hashCode | `()I` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 37 | Content.toString | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 38 | Hash.<init> | `(Ljava/lang/String;)V` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 39 | Hash.equals | `(Ljava/lang/Object;)Z` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |
| 40 | Hash.getAlgorithm | `()Ljava/lang/String;` | OPEN | — | Source not printed in this run (429 after plan fetch); handoff/rules/AGENT_NOTES/proposal/source files not read; full re-derivation still required |

Counts actually judged in this run: REACHABLE 0, UNREACHABLE 0, OPEN 40, total in batch 40.
