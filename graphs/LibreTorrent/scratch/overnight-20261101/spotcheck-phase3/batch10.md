# Spot-check — batch 10 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (4)

All four labels/kinds/confirmed_by are correct per L1 (full-scope greps: greps/L1/grep_all_calls.txt, grep_hash_collections.txt, grep_selectiontracker.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt); every one FAILs on stale prose only.

- 10/30 PeerItem.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "REVISION 2026-11-01 (still OPEN)", "Stays OPEN: hashCode can be called implicitly by library/framework code with no app-Java site, and the project-wide hashCode-dispatch question is undecided", "REVISION 2026-11-01 round 2 (still OPEN, 0 flips in this pass)", "conditional table H … (H-printed: stays OPEN … H-lib: stays OPEN absent a printed library trigger)".
- 10/32 FeedItemsListItem.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "REVISION 2026-11-01 (still OPEN)", "Stays OPEN on the same ground as row 30 (implicit library/framework hash dispatch + undecided project hashCode rule)", "REVISION 2026-11-01 round 2 (still OPEN, 0 flips in this pass)", "conditional table H … (H-printed: stays OPEN … H-lib: stays OPEN absent a printed library trigger)".
- 10/39 drawer TagItem.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "This is the strongest OPEN row in batch 10, but still OPEN under the strict full-grep rule", "REVISION 2026-11-01 (still OPEN)", "Stays OPEN on the same ground as rows 30/32 (implicit dispatch + undecided project hashCode rule)", "REVISION 2026-11-01 round 2 (still OPEN, 0 flips in this pass)", "conditional table H … (H-printed: stays OPEN … H-lib: stays OPEN absent a printed library trigger)".
- 10/40 drawer TagItem.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "REVISION 2026-11-01 (still OPEN)", "Stays OPEN: toString can be called implicitly (string concat, logging) by library/framework code with no app-Java site, and no project toString rule is recorded", "REVISION 2026-11-01 round 2 (still OPEN, 0 flips in this pass)", "conditional table T … (T-printed: stays OPEN … T-lib: stays OPEN absent a printed trigger)". (The row's own near-miss rejection stands: TagsAdapter:114 `"Unknown item: " + item` is AbstractTagItem-typed and instanceof-guarded, so a TagItem never reaches that concat.)

## Sample rows (8 sample-only)

- 10/1 ItemTorrentDownloadableFileBinding.inflate(LayoutInflater) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Complete-tree grep zero direct calls (batch 5–9 grep).
- 10/6 ItemTorrentListBinding.bind(View,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Complete-tree grep zero direct calls.
- 10/11 ItemTrackersListBinding.bind(View) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Complete-tree grep zero direct calls.
- 10/16 ItemTrackersListBinding.inflate(LayoutInflater,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Complete-tree grep zero direct calls.
- 10/21 TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Complete-tree grep zero direct calls.
- 10/26 FixHintTextInputEditText.\<init\>(Context) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Fresh definition (59 lines, SHA ab825b19…); 1-arg ctor delegates to super + init; saved triaged greps cited.
- 10/31 FeedItemsListItem.compareTo — REACHABLE INFERRED — PASS. FeedItemsListItem :26 implements Comparable, :44-47 compareTo; FeedItemsAdapter :82-87 submitList calls Collections.sort(list) before super.submitList; FeedItemsFragment :152/:218/:233 subscribe adapter::submitList — sort→compareTo is library dispatch, hence INFERRED (row notes its own strict-entry caveat: fragment-attach step not freshly printed).
- 10/36 FileManagerSpinnerAdapter$StorageSpinnerItem.setSize — UNREACHABLE no_trigger_in_app INFERRED — PASS. Fresh definition (StorageSpinnerItem :51-93, setSize :89); saved triaged greps over all 252 app Java files show no caller.

Totals: checked 12 (4 changed + 8 sample-only) — PASS 8, FAIL-prose 4, FAIL-label 0.
