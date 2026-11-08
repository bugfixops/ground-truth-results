# Spot-check — LibreTorrent batch 76 (Stream A Phase 2)

- Source file checked: `~/workspace/overnight/stream-A/work/batch76-merge-ready.md` (UNVERIFIED proposal, not a result; not edited).
- Method: each row below was re-derived from already-fetched printed source in `~/workspace/overnight/stream-A/corpus/java/` and `~/workspace/overnight/stream-A/corpus/res/layout/dialog_add_feed_channel.xml` (no connector fetch needed, no 429, no missing file). No build/sampler/C1 run (not this task).
- Check set: sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra changed rows apply.
- Filed labels: all 8 checked rows filed REACHABLE.

## Per-row verdicts

- Row 1 — AddFeedMutableParams.getName — PASS. Filed REACHABLE SOURCE. Definition AddFeedMutableParams.java:60–63; called AddFeedViewModel.java:174 (applyParams, FeedChannel construction). Direct printed call = SOURCE as filed.
- Row 6 — AddFeedMutableParams.setAutoDownload — PASS. Filed REACHABLE INFERRED. Definition AddFeedMutableParams.java:77–81; only printed app-code call site AddFeedViewModel.java:158, inside the Rx subscribe body :155–161 (fetchParams). Rx dispatch unprinted = INFERRED as filed. Two-way binding `dialog_add_feed_channel.xml:80` (`@={viewModel.mutableParams.autoDownload}`) is a generated route, likewise unprinted, and does not change the verdict.
- Row 11 — AddFeedMutableParams.setRegexFilter — PASS. Filed REACHABLE INFERRED. Definition AddFeedMutableParams.java:113–117; called AddFeedViewModel.java:160 (same Rx subscribe body :155–161). Rx dispatch unprinted = INFERRED as filed. Two-way binding `dialog_add_feed_channel.xml:155` (`@={viewModel.mutableParams.regexFilter}`) likewise unprinted.
- Row 16 — AddFeedViewModel.deleteChannel — PASS (label; boundary flag noted, not decided). Filed REACHABLE INFERRED. Body AddFeedViewModel.java:122–143; called AddFeedDialog.java:413 from deleteChannel, reached via the Rx event lambda AddFeedDialog.java:303–326 (deleteChannel() :313). Rx dispatch unprinted = INFERRED as filed. The file's boundary flag stands: if the merger counts a directly-printed call inside an Rx body as SOURCE, this row's confirmed_by flips to SOURCE with no label change. That convention is NOT decided here.
- Row 21 — AddFeedViewModel.initEditMode — PASS. Filed REACHABLE SOURCE. Body AddFeedViewModel.java:99–104 (mode=EDIT + setFeedId + fetchParams); called AddFeedDialog.java:135 (initParams feedId branch). Direct printed call = SOURCE as filed.
- Row 26 — AddFeedViewModel.refreshChannel — PASS. Filed REACHABLE SOURCE. Body AddFeedViewModel.java:203–219 (WorkManager enqueue of FeedFetcherWorker, ACTION_FETCH_CHANNEL :209–211, enqueue :218); called AddFeedViewModel.java:109 (addChannel) and :117 (updateChannel). The method itself is directly called, so downstream WorkManager dispatch does not affect the verdict. Direct printed calls = SOURCE as filed.
- Row 31 — AddLinkActivity.onCreate — PASS (label; same standard-edge convention note as batch 75). Filed REACHABLE SOURCE. Body AddLinkActivity.java:23–34 (findFragmentByTag :29, newInstance :31, show :32). Standard activity lifecycle edge; label verified on the printed body and manifest entry route.
- Row 36 — AddLinkDialog.checkUrlField — PASS. Filed REACHABLE SOURCE. Body AddLinkDialog.java:290–303; called AddLinkDialog.java:269 (inside addLink). Direct printed call = SOURCE as filed.

## Totals

- Rows checked: 8. PASS: 8. FAIL: 0.

## Proposed corrections

- None. No label or confirmed_by change proposed; the merge-ready file was not edited. The Rx-body SOURCE/INFERRED boundary flag on row 16 is left for the merger.
