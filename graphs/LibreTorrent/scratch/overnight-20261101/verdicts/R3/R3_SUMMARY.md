# R3 SUMMARY — LibreTorrent SelectionTracker hashCode rows (Stream A Phase 3 completion)

Task: obtain the PRINT — printed androidx `MutableSelection` /
`SelectionTracker` / `SelectionStorage` source showing the concrete
storage backing selection and whether any path invokes
key.hashCode() — and judge five OPEN hashCode rows. Branch
work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no
branch edits, no token anywhere, no work file under
`phase3/work/` edited (read-only), no tick marker written.

## Outcome of the print attempt: NOT OBTAINED
- 11 public web searches this run (MutableSelection / Selection /
  DefaultSelectionTracker source, AOSP googlesource, HashSet-storage
  phrasings, code-snippet phrasings), plus L1's 4 searches.
- Actually returned and read:
  - developer.android.com API reference for `MutableSelection` and
    `Selection`: `Selection` "tracks selected items by managing two
    sets" (primary + provisional). Set-interface statement only:
    no concrete class, no key.hashCode() invocation. This is the
    same sentence L1 already had; it is NOT a print of storage.
  - AOSP `SelectionTracker.java`, androidx-main (blob
    41ddefa9b1c46c5ceb9c4f0874cf5d187177706f), read in full
    (1856 lines): `copySelection` is declared ABSTRACT; the
    Builder constructs a `DefaultSelectionTracker`; the file
    imports only `java.util.Set` (for
    `setProvisionalSelection(Set<K>)`). No storage instantiation,
    no hashCode reliance, no copy implementation.
  - AOSP `GestureSelectionHelper.java` surfaced by one search —
    irrelevant to storage.
- Never returned by any search, therefore never opened (browser.open
  requires a verbatim URL from a tool result; none was guessed):
  `MutableSelection.java`, `Selection.java`,
  `DefaultSelectionTracker.java` source text. The SelectionTracker
  page's only outlink re-opens the same page. This is a search /
  indexing limitation, not a claim that the files do not exist:
  they exist in AOSP under
  `recyclerview/recyclerview-selection/src/main/java/androidx/recyclerview/selection/`,
  but no verbatim source URL for them was obtainable through the
  permitted route in this session. A future attempt with live
  browser navigation to the googlesource directory, or a local
  AndroidX checkout, could still obtain them; the exact files
  needed are named per row below.
- What was NOT done: no storage class inferred from "two sets",
  no HashSet assumed from general Java knowledge, no URL guessed
  by swapping a filename into the SelectionTracker URL.

## Corpus verification (done first, not trusted blindly)
All sites checked in `overnight/stream-A/corpus/java/` (the
corpus, not the task's line numbers alone). Task numbers are the
`new MutableSelection<>()` declaration lines; each copy call sits
on the following line:
- MainFragment (TorrentListItem): tracker :100; declarations
  :575/:599/:610 → copySelection :576/:600/:611.
- FeedFragment (FeedChannelItem): declarations :446/:466/:483/
  :496/:511 → copySelection :447/:467/:484/:497/:512.
- DetailTorrentTrackersFragment (TrackerItem): declarations
  :362/:376 → copySelection :363/:377.
- DetailTorrentFilesFragment (TorrentContentFileItem): declarations
  :438/:496/:511 → copySelection :439/:497/:512.
- Inheritance check for 73/31: `TorrentContentFileItem extends
  FileItem` (:32); corpus grep finds exactly one hashCode
  definition for the pair, `FileItem.java:103`; the subclass
  defines none. So a hashCode-reliant library operation on a
  TorrentContentFileItem key would dispatch to FileItem.hashCode —
  IF such an operation exists, which is exactly what the missing
  print would show.
- TagItem tracker check: corpus-wide grep for a
  SelectionTracker keyed on TagItem returns ZERO hits (L1's
  grep_selectiontracker.txt lists only TorrentListItem,
  FeedChannelItem, TrackerItem, TorrentContentFileItem).

## Verdicts (one line each in the final report; detail per file)
| Row | Method | Verdict |
| --- | ------ | ------- |
| 95/35 | TrackerItem.hashCode | OPEN — print not obtained; live copySelection route into unknown storage (D30 literal) |
| 99/18 | FeedChannelItem.hashCode | OPEN — print not obtained; live copySelection route into unknown storage (D30 literal) |
| 112/30 | TorrentListItem.hashCode | OPEN — print not obtained; live copySelection route into unknown storage (D30 literal) |
| 73/31 | FileItem.hashCode (inherited by TorrentContentFileItem keys) | OPEN — print not obtained; inheritance dispatch established, storage half unprinted (D30 literal, via L1 extension) |
| 3/26 | TagInfo.hashCode | UNREACHABLE no_trigger_in_app INFERRED — all three legs closed (10/39, 11/7, 30/8 UNREACHABLE), full-scope zero, and the candidate MutableSelection dispatcher affirmatively disconnected (no TagItem tracker); see its file for the D30-literal tension and the mechanical overturn rule |

## Why the four key rows stay OPEN and 3/26 does not (the distinction)
- The four key rows each have a LIVE in-app route into unprinted
  library code (copySelection into MutableSelection). Until the
  print shows the storage class, D30 outcome 3 applies: stays
  OPEN. A printed non-hash storage would also leave them OPEN
  per D30 literal reading, with a merger note that outcome 2 may
  then close them to UNREACHABLE — that distinction is recorded
  in each file, not collapsed.
- 3/26 has NO live route into library code: no TagItem tracker
  exists, so no MutableSelection print (hash-backed or not) can
  reach it. Its only legs are two delegators and one List leg,
  all of whose hosts are UNREACHABLE, and L1's full-scope grep
  found no other trigger. That meets D30 outcome 2 (full-scope
  zero + no plausible unprinted dispatcher) and matches L1's
  dependency closures (31/25, 73/32). D30's literal listing of
  3/26 among stay-OPEN rows rested on D6's premise that it
  "flips with them via the drawer-TagItem delegation" — a premise
  L1 disproved at the tracker link. This verdict treats that
  listing as vacated for 3/26 by the failed premise; the file
  states the fallback (OPEN on a strict literal reading) and the
  mechanical overturn rule (revive any of 10/39, 11/7, 30/8 →
  3/26 flips to REACHABLE with it).

## Exact missing print (resolver for the four OPEN rows)
Printed androidx `MutableSelection` source showing the concrete
Set instantiation in its constructor (hash-backed, e.g. HashSet,
or non-hash), together with the `DefaultSelectionTracker`
copySelection implementation showing the copy path into that
storage — version noted (the app's recyclerview-selection
artifact version is not pinned in the evidence used here; the
file read this run was androidx-main). Hash-backed → the four
key rows flip to REACHABLE INFERRED (73/31 via inheritance).
Non-hash → they stay OPEN per D30 literal reading, merger note
that outcome 2 may then close them to UNREACHABLE. Still
unobtainable → they stay OPEN. The print is IRRELEVANT to 3/26
either way (no TagItem tracker), which is why 3/26 is decided
now rather than held for it.

## Files written (verdicts only, under phase3/verdicts/R3/)
- `95-35-TrackerItem-hashCode.md`
- `99-18-FeedChannelItem-hashCode.md`
- `112-30-TorrentListItem-hashCode.md`
- `73-31-FileItem-hashCode.md`
- `3-26-TagInfo-hashCode.md`
- `R3_SUMMARY.md` (this file)

## Hygiene / limits
- No file under `phase3/work/` touched; no push; no branch edit;
  no token used or embedded; no tick marker written.
- No build, sampler, grep (beyond re-reading saved L1 greps and
  the corpus greps above), or C1 check was run or claimed; this
  task's evidence is the web print attempt + corpus/work-file
  verification stated above.
- 10/39's UNREACHABLE status is an L1 verdict proposal (work file
  still shows OPEN); 11/7 and 30/8 are likewise verdict-level
  except where L1 verified standing proposals. The 3/26 verdict
  is conditional on those verdicts standing at merge, as its
  file states.
