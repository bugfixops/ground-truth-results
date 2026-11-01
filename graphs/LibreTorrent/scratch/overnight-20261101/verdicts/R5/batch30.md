# R5 verdicts — batch 30 (3 rows)

Scope: rows verified OPEN in the main table of `phase3/work/batch30-merge-ready.md`
(L178, L179, and 30/5 at L167). Note on the brief: 30/16 and 30/17 each occur
ONCE in the batch-30 file, in the main table — there is no competing
conditional-table row for them in this file (their stand/fall condition is
stated in DECISIONS.md D5b, not as a second row here), so "last occurrence
wins" is unambiguous. These rows are D5b dependency companions of trio rows,
not trio members themselves, so they are judged by the D5b dependency rule
exactly as L2 applied it — caller OPEN → stays OPEN; caller REACHABLE →
REACHABLE — with per-row confirmed_by (D1).

## 30/5 — TorrentInfo.compareTo — stays OPEN — confirmed_by —

- Work-file identity: main-table row L167, OPEN, `—`.
- Definition: TorrentInfo.java:186–187 (`name.compareTo(...)`).
- New grep (greps/R5/greps/compareTo_sort.txt): TorrentInfo lists are sorted
  via the TorrentSortingComparator / `SortingColumns.compare` on String
  names (TorrentSorting.java:42–44; MainFragment.java:293/:341;
  TorrentService.java:287/:304), never via this method; no
  `Collections.sort` site sorts TorrentInfo objects and no direct
  `.compareTo(` call names a TorrentInfo receiver. The work file's
  `containsAll` note concerns equals (row 7), not compareTo.
- No decided rule covers compareTo.
- Verdict: stays OPEN.
- What would change it: a printed sort/comparison site for TorrentInfo
  objects (not the String-name comparator), or a saved full-repo grep.
  Never UNREACHABLE on corpus-zero alone (P2).

## 30/16 — TorrentStateCode.fromValue — FLIPS to REACHABLE — confirmed_by SOURCE

- Work-file identity: main-table row L178, OPEN, `—`. Work file: "Only
  printed caller in this pass is TorrentInfo.java:125, inside the OPEN
  Parcel ctor (row 2). Dependency rule: stays OPEN. It flips to REACHABLE
  if and only if the Parcel-ctor route is ever resolved."
- Dependency resolved by L2 (verdicts/L2/batch30.md): 30/2
  (TorrentInfo.\<init\>(Parcel)) flipped to REACHABLE SOURCE via its caller
  30/12 (createFromParcel), which flipped REACHABLE INFERRED on the D20
  TorrentListItem storage site (MainFragment.java:162 + Parcel.java:2894
  `getField("CREATOR")`). L2 also flipped 30/10 (writeToParcel) and 30/12
  to REACHABLE on the same site.
- Printed caller, verified in corpus (greps/R5/greps/row30_16_17_callers.txt):
  TorrentInfo.java:125 `stateCode = TorrentStateCode.fromValue(source.readInt());`
  inside the now-REACHABLE Parcel ctor. Per-row SOURCE: the printed line
  names the method itself, inside a REACHABLE method (D1, D5b positive
  direction — the same direction L2 used for 30/2 itself).
- Verdict: REACHABLE, SOURCE.
- What would change it: if 30/2 reverts to OPEN (i.e. if 30/12 reverts),
  30/16 reverts with it (D5b dependency, symmetric).

## 30/17 — TorrentStateCode.value — FLIPS to REACHABLE — confirmed_by SOURCE

- Work-file identity: main-table row L179, OPEN, `—`. Work file: "Only
  printed callers in this pass are TorrentInfo.java:155 (inside the OPEN
  writeToParcel, row 10) and TorrentStateCode.java:71 (inside the OPEN
  fromValue, row 16). Dependency rule: stays OPEN, standing/falling with
  rows 10 and 16."
- Both dependencies now resolved REACHABLE: 30/10 flipped REACHABLE INFERRED
  by L2 (D20, MainFragment.java:162 site), and 30/16 flips REACHABLE SOURCE
  in this file (above).
- Printed callers, verified in corpus (greps/R5/greps/row30_16_17_callers.txt):
  TorrentInfo.java:155 `dest.writeInt(stateCode.value());` inside the
  now-REACHABLE writeToParcel, and TorrentStateCode.java:71
  `if (ev.value() == value)` inside the now-REACHABLE fromValue. Either
  alone suffices; per-row SOURCE on the printed line naming the method
  itself inside a REACHABLE method.
- Verdict: REACHABLE, SOURCE.
- What would change it: if BOTH 30/10 and 30/16 reverted to OPEN, 30/17
  would revert with them; reversion of only one leaves the other route
  standing.
