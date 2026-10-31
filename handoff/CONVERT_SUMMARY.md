# Overnight convert run summary (2026-10-31)

Work order: AmazeFileManager, AnkiDroid, MMEX (handoff/PROGRESS_V2.md). LibreTorrent ("- [H]") was not touched. The 2026-10-29 summary, which marked AnkiDroid as blocked, is kept as handoff/CONVERT_SUMMARY.md.bak_20261029_0411 and is superseded.

## AmazeFileManager: labelled ("- [L]"), route checks not started

Build 28 (graphs/AmazeFileManager/scratch/build_finish_28.txt), exit 0: UNRESOLVED 0, errors 0, warnings 0; REACHABLE 2509, UNREACHABLE 472. The AboutActivity labels, the removed dead-constructor edge and the framework-target cleanups are recorded under "## Convert run decisions (AmazeFileManager overnight labelling, 2026-10-30)" in handoff/HANDOFF_V2.md. Open for route checks and not blocking the gate: E89e2cedd (SftpConnectDialog.lambda$null$2, an unverified nested-lambda name), Ee1aeff93 (CompressedExplorerFragment.<init> to Decompressor.decompress; trigger and source question), 21 Glide UNREACHABLE-but-ran contradictions (GlideOptions.*, GlideRequest.*; rule C5 still open), and conflicts.md entries for the 21 tool-run contradictions, which were not written.

## AnkiDroid: labelled ("- [L]"), route checks not started

Build 204 (graphs/AnkiDroid), exit 0: REACHABLE 3275, UNREACHABLE 911, UNRESOLVED 0, errors 0, warnings 0. The labels were written as parts 134 to 150, with builds 185 to 204, and replace the blocked state in the 2026-10-29 summary. Open, not in the gate: Card.toString is UNREACHABLE (no_trigger_in_app) but one tool-run hit exists, and its caller is unknown; this must be resolved before a route is assigned to it in route checks. The 2026-10-29 open items (EasySSLSocketFactory.equals and hashCode, the reference API level 27 against target 23, and the Hooks.runFilter pair) were not re-checked in this run. Decisions are under "## Convert run decisions (AnkiDroid overnight labelling, 2026-10-30)" in handoff/HANDOFF_V2.md.

## MMEX: labelled ("- [L]"), route checks not started

Build p147 (graphs/MMEX/scratch/build_p147.txt), exit 0: methods 4270, pages 43, edges 8027, REACHABLE 3430, UNREACHABLE 840, UNRESOLVED 0, errors 0, warnings 0. Parts 001 to 147 are merged; the brief said 084, but the files showed more (see the decisions). Batches 128 and 130 stalled and were relaunched. Parts 144, 146 and 147 were written by the orchestrator: the configure activity is REACHABLE through the manifest's APPWIDGET_CONFIGURE entry, four methods reached only through REGISTER edges got dispatch edges, and receiver-copy and dialog-listener edges cleared the last nine unresolved methods. Items for review in route checks: several INFERRED UNREACHABLE entries (getPageTitle, AccountBillsWidgetService.onGetViewFactory, MmxDatabaseUtils.<clinit>, generated Dagger and ButterKnife methods). Details are in handoff/HANDOFF_V2.md under "## Convert run decisions (MMEX overnight labelling, 2026-10-31)" and in graphs/MMEX/AGENT_NOTES.md.
