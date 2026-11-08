# R3 verdict — 112/30 TorrentListItem.hashCode

## Identity (verified from the work file first)
- Batch file: `phase3/work/batch112-merge-ready.md`, row 30, currently OPEN.
- Method: `TorrentListItem.hashCode()`, definition
  `TorrentListItem.java:56-58` (`torrentId.hashCode()` — a String
  call inside the body, not a TorrentListItem call).
- Prior state: stays OPEN — no printed trigger; SelectionTracker /
  createParcelableStorage is Parcelable storage, not a hash trigger;
  not flipped to UNREACHABLE on app-tree zero.

## Verdict: OPEN (unchanged)
- Label: OPEN, confirmed_by —.
- NOT flipped to REACHABLE, NOT flipped to UNREACHABLE.

## In-app route verified in the corpus (not trusted blindly)
Corpus files under `overnight/stream-A/corpus/java/`:
- `ui/main/MainFragment.java:100` —
  `SelectionTracker<TorrentListItem> selectionTracker` (work file
  cites tracker build :100/:157-162, storage :163).
- `MutableSelection<TorrentListItem>` declarations at :575, :599,
  :610, each followed on the next line by
  `selectionTracker.copySelection(selections)` at :576, :600, :611.
  (Task-cited `:575-576` / `:599-600` / `:610-611` are the
  declaration + copy line pairs.)
- `getItemPosition` uses `List.indexOf` (equals only, not hashCode);
  no app-Java hashCode caller on a TorrentListItem exists in the
  saved greps (work file: grep over the fresh files finds only the
  definition itself).

## The print: NOT OBTAINED
Same search set as the sibling R3 verdicts (11 searches this run
plus L1's 4). What was actually returned:
- developer.android.com API reference: `Selection` "tracks selected
  items by managing two sets" — a Set-interface statement, not a
  concrete storage class and not evidence of a key.hashCode()
  invocation.
- AOSP `SelectionTracker.java` (androidx-main) in full: `copySelection`
  is abstract; the concrete tracker is `DefaultSelectionTracker`;
  no storage instantiation and no hashCode reliance is shown.
- No `MutableSelection.java`, `Selection.java`, or
  `DefaultSelectionTracker.java` source text was returned by any
  search, so none could be opened (verbatim-URL rule; no URL was
  guessed). The SelectionTracker page's only outlink re-opens itself.

## Why OPEN, under the task's verdict rules
- REACHABLE INFERRED requires a printed hash-backed storage plus a
  hashCode-reliant key operation on the copySelection path. Neither
  is printed: the destination MutableSelection's concrete Set class
  and the DefaultSelectionTracker copy implementation are both
  unprinted. "Two sets" must not be read as "HashSet-backed".
- UNREACHABLE is barred for this row by D30's literal reading: a
  live in-app route into unprinted library code exists (three
  copySelection sites), so this is a genuine open dispatcher
  question. Per D30/task instruction, even a printed non-hash
  storage would leave the row OPEN (merger may then close it to
  UNREACHABLE under outcome 2); no print at all leaves it OPEN.
- Nothing fabricated: no storage class, no hashCode call, no
  artifact version asserted.

## Exact missing print (resolver, unchanged)
Printed androidx `MutableSelection` source showing the concrete Set
instantiation in its constructor (hash-backed or non-hash), plus
the `DefaultSelectionTracker.copySelection` implementation showing
the copy path — version noted. Hash-backed → REACHABLE INFERRED.
Non-hash → stays OPEN per D30 literal reading, merger note that
outcome 2 may then close it to UNREACHABLE. Unobtainable → stays OPEN.

## Hygiene
No work file edited; no push; no branch edit; no token used. This
verdict file only, under `phase3/verdicts/R3/`.
