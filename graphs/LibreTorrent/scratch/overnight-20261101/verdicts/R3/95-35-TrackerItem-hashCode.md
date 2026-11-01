# R3 verdict — 95/35 TrackerItem.hashCode

## Identity (verified from the work file first)
- Batch file: `phase3/work/batch95-merge-ready.md`, row 35, currently OPEN.
- Method: `TrackerItem.hashCode()`, definition `TrackerItem.java:34-37`
  (`return url.hashCode()` — a String call inside the body, not a
  TrackerItem call).
- Prior state: OPEN-closing round 2 conditional table — (a) REACHABLE
  INFERRED if the project accepts the unprinted-internals lead that
  androidx MutableSelection storage is hash-backed; (b) otherwise OPEN.
  No app-Java hashCode caller was printed.

## Verdict: OPEN (unchanged)
- Label: OPEN, confirmed_by —.
- NOT flipped to REACHABLE, NOT flipped to UNREACHABLE.

## In-app route verified in the corpus (not trusted blindly)
Corpus files under `overnight/stream-A/corpus/java/`:
- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:84`
  — `SelectionTracker<TrackerItem> selectionTracker`.
- `:362` — `MutableSelection<TrackerItem> selections = new MutableSelection<>();`
  followed by `:363` — `selectionTracker.copySelection(selections);`
- `:376` — same declaration line; `:377` — `copySelection(selections);`
- (Task-cited `:362-363` / `:376-377` are the declaration + copy lines
  paired; the copy calls themselves sit at :363 and :377.)
- Tracker built with `StorageStrategy.createParcelableStorage(TrackerItem.class)`
  (work file :183) — Parcelable storage, not itself a hashCode call.
- Adapter diffing is equals-only (`areContentsTheSame`, `areItemsTheSame`,
  `indexOf`); the inner KeyProvider calls `getItemKey`/`getItemPosition`,
  never hashCode (work file, round-2 re-check). No app-Java hashCode
  caller on a TrackerItem exists in the saved greps.

## The print: NOT OBTAINED
This run ran 11 public web searches (MutableSelection / Selection /
DefaultSelectionTracker source, AOSP googlesource, HashSet-storage
phrasings) in addition to L1's 4 searches. Returned, verbatim:
- developer.android.com API reference for `MutableSelection` and
  `Selection`: `Selection` "tracks selected items by managing two
  sets" (primary + provisional). That is a Set-interface statement:
  it names no concrete class (HashSet, TreeSet, ArraySet, list-backed
  all satisfy "two sets") and no key.hashCode() invocation.
- AOSP `SelectionTracker.java` (androidx-main, blob
  41ddefa9b1c46c5ceb9c4f0874cf5d187177706f), read in full:
  `copySelection` is declared ABSTRACT (`public abstract void
  copySelection(@NonNull MutableSelection<K> dest)`); the Builder
  builds a `DefaultSelectionTracker`. The file imports only
  `java.util.Set` (for `setProvisionalSelection(Set<K>)`) and shows
  no storage instantiation and no hashCode reliance.
- No `MutableSelection.java`, no `Selection.java`, and no
  `DefaultSelectionTracker.java` source text was returned by any
  search, so no such file could be opened (browser.open requires a
  verbatim URL from a tool result; no sibling-file URL was ever
  returned, and none was guessed). The one outlink on the
  SelectionTracker page re-opens the same page.

## Why OPEN, under the task's verdict rules
- The flip to REACHABLE INFERRED requires a PRINTED hash-backed
  storage plus a hashCode-reliant operation on keys on the
  copySelection path. Neither half is printed: the destination
  `MutableSelection`'s concrete Set class is unprinted, and the
  `DefaultSelectionTracker.copySelection` implementation (which the
  API doc describes only as updating `dest` to reflect the current
  selection, via `MutableSelection.copyFrom`, "clones primary and
  provisional selection") is unprinted. The API doc's "two sets"
  sentence must not be upgraded into "HashSet-backed".
- The flip to UNREACHABLE is barred by D30's literal reading for
  exactly this row: a live in-app route into unprinted library code
  exists (copySelection at :363/:377), so the storage question is a
  genuine open dispatcher question, not app-tree zero. Per D30 and
  the task instruction, a non-hash print would ALSO leave the row
  OPEN (merger may then close it to UNREACHABLE under outcome 2);
  a fortiori, no print at all leaves it OPEN.
- Nothing was fabricated: no storage class, no hashCode call, and no
  version pin for the app's recyclerview-selection artifact is
  asserted here.

## Exact missing print (resolver, unchanged)
Printed androidx `MutableSelection` source showing the concrete Set
instantiation in its constructor (hash-backed, e.g. HashSet, or
non-hash), together with the `DefaultSelectionTracker.copySelection`
implementation showing the copy path into that storage — version
noted. If hash-backed → this row flips to REACHABLE INFERRED. If
non-hash → stays OPEN per D30 literal reading, with a merger note
that outcome 2 may then close it to UNREACHABLE. If still
unobtainable → stays OPEN.

## Hygiene
No work file edited; no push; no branch edit; no token used. This
verdict file only, under `phase3/verdicts/R3/`.
