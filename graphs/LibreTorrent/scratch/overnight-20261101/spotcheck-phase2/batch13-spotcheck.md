# LibreTorrent batch 13 — Phase 2 spot-check (UNVERIFIED proposal, labels only)

- Work file checked: `~/workspace/overnight/stream-A/work/batch13-merge-ready.md` (40 rows, 36 REACHABLE proposed / 4 UNREACHABLE proposed / 0 OPEN).
- Spot-check date: 2026-11-01. No merge-ready file was edited, no label was changed by this check, no push was made, no build/sampler/C1 was run (not this task).
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (281-file Java tree, including the feedparser library files). No GitHub connector fetch was needed; no 429 was hit.
- Verdict rule: PASS requires the label AND the cited definition/caller lines to identify the right method and caller. A range running past the closing brace onto a blank line or the class-close brace is a nit, not a FAIL. A range that starts on the wrong line, ends mid-method, or names the wrong caller line is a FAIL.
- Phase 1 note: this file carries no dated 2026-11-01 Phase 1c revision (it was not in a Phase 1c application group), so there are no additional Phase 1 changed rows beyond the sample.

## Rows checked (8 of 40)

Sample rows 1, 6, 11, 16, 21, 26, 31, 36.

## Per-row verdicts

- Row 1 — AtomItem.getEzRssTorrentItem — REACHABLE SOURCE — **PASS**. Def `AtomItem.java:136-138` verified (def :136, `return null` :137, close :138). Interface call at core `FeedParser.java:238` (`item.getEzRssTorrentItem()` inside `watchTorrentInfoHash`) verified. Returning null is a run of the method, not unreachability.
- Row 6 — AtomItem.getTitle — REACHABLE SOURCE — **PASS**. Def `AtomItem.java:40-43` verified (`getElement(TITLE)` :41, `getContent` :42). Unconditional call at core `FeedParser.java:110` (`item.getTitle()` in the `getItems` loop) verified.
- Row 11 — BaseElement.getElement — REACHABLE SOURCE — **PASS**. Def `BaseElement.java:73-76` verified. Callers verified: `AtomItem.java:41, 75, 81` and `EzRss01Parser.java:40, 48, 56, 64, 80, 88, 96` (all `item.getElement(…)` sites).
- Row 16 — BaseItem.equals — UNREACHABLE — **PASS (as proposed)**. Def `BaseItem.java:53-62` verified (calls `getUniqueId` :56-57, `FeedUtils.equalsOrNull` :58). Corpus-wide grep finds no explicit call to `equals` on a library Item and no hash-based collection holding a library Item; core code reads `item.getTitle()`/`getLinks()`/`getPubDate()`/`getGuid()`/`getMediaRss()`/`getEzRssTorrentItem()` explicitly. The label stands as proposed; the file's own caveat remains: a saved full-repo grep (res/generated/library scope) is still owed before merge, and a trigger there flips this row (and batch 12 row 21 with it).
- Row 21 — DefaultFeedParser.parse — REACHABLE SOURCE — **PASS**. Def `DefaultFeedParser.java:22-47` verified (class :19, parse :22). Call at core `FeedParser.java:71` (`FeedParserFactory.newParser().parse(bsStream)`) verified.
- Row 26 — EzRss01Parser.parseFileName — REACHABLE SOURCE — **PASS**. Def `EzRss01Parser.java:39-45` verified (`getElement` :40, `isEzRssElement` :41, `getContent` :44). Call from `parse()` at :27 verified.
- Row 31 — EzRss01Parser.parseSeeds — REACHABLE SOURCE — **PASS**. Def `EzRss01Parser.java:79-85` verified (`getElement` :80, `isEzRssElement` :81, `parseInt` :84). Call from `parse()` at :31 verified.
- Row 36 — FeedHandler.endElement — REACHABLE INFERRED — **PASS**. Def `FeedHandler.java:110-131` verified (calls `setContent` :121 and `addElement` :126). Registration at `DefaultFeedParser.java:37` (`parser.parse(new XMLInputStream(inStream), handler)`) verified; the SAX dispatch itself is unprinted, hence INFERRED is correct.

## Totals

- Checked: 8. **PASS: 8. FAIL: 0.**
- No label found wrong, no citation found wrong, no correction proposed.
- The file's still-owed saved full-repo grep for the UNREACHABLE-proposed rows (16–19) remains owed before merge; this check covered the Java corpus only.
