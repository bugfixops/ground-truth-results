# D29 — user decision, 2026-11-01

Batch 5 rows 19, 20, 25, and 26 STAY UNREACHABLE.

Reason given by the user: the bytecode shows no caller outside their own
classes for all 200 statics (batches 5-9 generated base Binding statics).

Status in the pushed merge-ready files: all four rows are UNREACHABLE
no_trigger_in_app INFERRED in graphs/LibreTorrent/scratch/merge-ready/
batch5-merge-ready.md, consistent with this decision; totals unchanged
(3964 REACHABLE / 691 UNREACHABLE / 77 OPEN of 4732).

This decision is the user's, recorded by Muse. It closes the D29 tension
(the D4d parent-include argument) for these four rows.
