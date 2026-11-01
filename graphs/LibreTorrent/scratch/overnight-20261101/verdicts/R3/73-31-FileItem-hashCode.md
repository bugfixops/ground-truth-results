# R3 verdict — 73/31 FileItem.hashCode (via inheritance)

## Identity (verified from the work file first)
- Batch file: `phase3/work/batch73-merge-ready.md`, row 31, currently OPEN.
- Method: `FileItem.hashCode()`, definition `FileItem.java:103-112`
  (work file row 31; corpus confirms `ui/FileItem.java:103`
  `public int hashCode()`).
- Prior state: stays OPEN under D6 (printed-trigger rule; app-tree
  zero alone never closes it). The work file's conditional table:
  (a) under a hash-backed-library-dispatch decision, flips to
  REACHABLE INFERRED; (b) under an explicit-app-caller-only rule,
  flips to UNREACHABLE `no_trigger_in_app` INFERRED. Not decided
  in the work file.

## Verdict: OPEN (unchanged)
- Label: OPEN, confirmed_by —.
- NOT flipped to REACHABLE, NOT flipped to UNREACHABLE.

## The inheritance step, stated explicitly (verified in the corpus)
1. The selection key type at the in-app sites is
   `TorrentContentFileItem`, not `FileItem`:
   `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:92`
   — `SelectionTracker<TorrentContentFileItem> selectionTracker`.
2. `ui/detailtorrent/pages/files/TorrentContentFileItem.java:32` —
   `public class TorrentContentFileItem extends FileItem`.
3. A corpus-wide grep for `hashCode` over `TorrentContentFileItem.java`
   and `FileItem.java` returns exactly one definition:
   `FileItem.java:103`. `TorrentContentFileItem` defines NO
   `hashCode` of its own.
4. Therefore, IF any library code on the copySelection path performs
   a hashCode-reliant operation on a `TorrentContentFileItem` key,
   Java virtual dispatch resolves it to the inherited
   `FileItem.hashCode` (73/31) — that is the only hashCode the key
   type has. The inheritance step is sound; what is unprinted is
   whether the library performs such an operation at all (see below).
   The work file's batch-73 note that `TorrentContentFilesAdapter:88`
   `selectionTracker.isSelected(item)` passes TorrentContentFileItem
   keys is the same-storage question, not independent evidence:
   `isSelected` → `Selection.contains` → the same unknown Set.

## In-app route verified in the corpus (not trusted blindly)
- `MutableSelection<TorrentContentFileItem>` declarations at
  DetailTorrentFilesFragment :438, :496, :511, each followed on the
  next line by `selectionTracker.copySelection(selections)` at
  :439, :497, :512. (Task-cited `:438-439` / `:496-497` / `:511-512`
  are the declaration + copy line pairs.)
- DiffUtil uses `equals`, not hashCode; `getCurrentList().indexOf`
  uses `equals`. No printed `.hashCode()` call on a FileItem
  receiver exists in the 252-file tree (work file round-2 note).

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
- Note on scope: D30's named SelectionTracker list omits 73/31, but
  L1 correctly holds it on the same print — the key type's hashCode
  IS 73/31 by inheritance, so the print question is identical in
  kind to 95/35, 99/18, and 112/30.

## Why OPEN, under the task's verdict rules
- REACHABLE INFERRED requires a printed hash-backed storage plus a
  hashCode-reliant key operation on the copySelection path. The
  inheritance dispatch (step 4 above) is established, but the
  storage half is unprinted, so the chain is incomplete. "Two sets"
  must not be read as "HashSet-backed".
- UNREACHABLE is barred here for the same reason as the three
  direct key rows: a live in-app route into unprinted library code
  exists (three copySelection sites feeding TorrentContentFileItem
  keys whose hashCode is 73/31), so this is a genuine open
  dispatcher question, not app-tree zero. Per D30's literal reading
  as extended by L1 to this row, even a printed non-hash storage
  would leave the row OPEN (merger may then close it to
  UNREACHABLE under outcome 2); no print at all leaves it OPEN.
- The work file's option (b) (explicit-app-caller-only rule →
  UNREACHABLE) is NOT adopted here: it is a project-rule decision
  for the merger, not a consequence of the print attempt, and the
  task's verdict rules for the no-print branch say OPEN.
- Nothing fabricated: no storage class, no hashCode call, no
  artifact version asserted.

## Exact missing print (resolver, unchanged)
Printed androidx `MutableSelection` source showing the concrete Set
instantiation in its constructor (hash-backed or non-hash), plus
the `DefaultSelectionTracker.copySelection` implementation showing
the copy path — version noted. Hash-backed → 73/31 flips to
REACHABLE INFERRED via the inheritance step above. Non-hash →
stays OPEN per D30 literal reading, merger note that outcome 2 may
then close it to UNREACHABLE. Unobtainable → stays OPEN.

## Hygiene
No work file edited; no push; no branch edit; no token used. This
verdict file only, under `phase3/verdicts/R3/`.
