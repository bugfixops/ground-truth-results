# LibreTorrent batch 14 — Phase 2 spot-check (UNVERIFIED proposal, labels only)

- Work file checked: `~/workspace/overnight/stream-A/work/batch14-merge-ready.md` (40 rows; REACHABLE proposed / UNREACHABLE proposed mix, 0 OPEN in the table as filed).
- Spot-check date: 2026-11-01. No merge-ready file was edited, no label was changed by this check, no push was made, no build/sampler/C1 was run (not this task).
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (281-file Java tree). No GitHub connector fetch was needed; no 429 was hit.
- Verdict rule: PASS requires the label AND the cited definition/caller lines to identify the right method and caller. A range running past the closing brace onto a blank line or the class-close brace is a nit, not a FAIL. A range that starts on the wrong line, ends mid-method, or names the wrong caller line is a FAIL.
- Phase 1 note: this file carries no dated 2026-11-01 Phase 1c revision (it was not in a Phase 1c application group), so there are no additional Phase 1 changed rows beyond the sample.

## Rows checked (8 of 40)

Sample rows 1, 6, 11, 16, 21, 26, 31, 36.

## Per-row verdicts

- Row 1 — MediaRssParser.isMediaRssElement — REACHABLE INFERRED — **PASS**. Call sites verified in `MediaRssParser.java`: `parseContent` :45, `parseHash` :60, `parsePeerLinks` :81 (private def at :94). Reached via `parse()` :29-38 ← `Rss2Item.getMediaRss` :115 ← core `FeedParser.java:190`. INFERRED is correct under the file's whole-route rule (WorkManager + SAX dispatch unprinted).
- Row 6 — Rss1Feed.\<init\> — REACHABLE INFERRED — **PASS**. Def `Rss1Feed.java:36-38` verified. Construction at `FeedHandler.java:62` (`new Rss1Feed(uri, RDF, attributes)`) verified; SAX dispatch unprinted, hence INFERRED.
- Row 11 — Rss1Item.getDescription — UNREACHABLE (derivative) — **PASS (as proposed)**. Def `Rss1Item.java:56-59` verified. Corpus-wide grep finds no caller outside the `BaseItem.getUniqueId` path (`BaseItem.java:41` inside private `getUniqueId`, which runs only via `BaseItem.equals` :56-57 / `hashCode` :67 — both proposed UNREACHABLE in batch 13). The file's conditional framing is correct: this label stands only while batch 13's `BaseItem.equals`/`hashCode` stay UNREACHABLE, and a saved full-repo grep trigger for them requires re-judging this row (not an automatic flip, since `getUniqueId` reaches `getDescription` only as a last fallback).
- Row 16 — Rss1Item.getMediaRss — REACHABLE INFERRED — **PASS**. Def `Rss1Item.java:112-114` verified (`return null`). Interface call at core `FeedParser.java:190` (`item.getMediaRss()`) verified. Returning null is a run of the method.
- Row 21 — Rss2Feed.getTitle — REACHABLE INFERRED — **PASS**. Def `Rss2Feed.java:47-51` verified. Call at core `FeedParser.java:86` (`feed.getTitle()`) verified.
- Row 26 — Rss2Item.getEzRssTorrentItem — REACHABLE INFERRED — **PASS**. Def `Rss2Item.java:119-121` verified (`new EzRss01Parser(this).parse()` :120). Call at core `FeedParser.java:238` verified.
- Row 31 — Rss2Item.getTitle — REACHABLE INFERRED — **PASS**. Def `Rss2Item.java:40-43` verified. Call at core `FeedParser.java:110` verified.
- Row 36 — Content.hashCode — UNREACHABLE — **PASS (as proposed)**. Def `mediarss/Content.java:76-80` verified. Corpus-wide grep finds no `hashCode()` call on a `Content` and no hash-based collection holding a `Content` (the only `hashCode` lines for this class are inside its own definition). The file's still-owed saved full-repo grep remains owed before merge; this check covered the Java corpus only.

## Totals

- Checked: 8. **PASS: 8. FAIL: 0.**
- No label found wrong, no citation found wrong, no correction proposed.
