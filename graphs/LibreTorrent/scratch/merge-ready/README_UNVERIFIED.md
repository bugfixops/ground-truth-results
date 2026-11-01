# LibreTorrent merge-ready parts — UNVERIFIED (updated 2026-11-01, before [L])

These 120 files (batches 1-120, all 4,732 plan rows) are merge-ready PROPOSALS only.
Nothing here is verified for merge, nothing has been merged into graph_def.py,
out/, or handoff/PROGRESS_V2.md, and the LibreTorrent status line is unchanged.

Update 2026-11-01 (OPEN-closing rounds 1-2 + grep-family flips + spot-checks):
mechanical label-column totals over the 120 files (see MERGE_PREP_TOTALS_UNVERIFIED.txt):
3858 REACHABLE proposed / 310 UNREACHABLE proposed / 564 OPEN proposed.
564 OPEN rows remain, so labels are NOT complete and this push is NOT [L].
Baseline at first push (2026-11-01 01:01 EDT) was 3,685 / 238 / 809.

Each file is marked UNVERIFIED in its header. Build and C1 are marked "not run"
(they run on the user's Mac after a push). No APKs, zips, secrets, or tokens are
included. This push went to branch work-2026-10-31 only, never main or result.

Remaining OPEN rows are convention-dependent (see the conditional tables in the
files and the convention dossiers): batches 5-9 base Binding statics (200 rows,
awaiting the user's decision), generated mapper rows, Parcelable trios, binding
callbacks, Room $N/finalize/converters, hashCode/toString, and setters/getters.
Spot-checks: all batches checked so far PASS on sampled rows (round-1 wave 42
batches, round-2 wave 4 batches, round-2-revision wave 14 batches, 126/126 PASS
in the last wave); no flipped row was re-opened.
