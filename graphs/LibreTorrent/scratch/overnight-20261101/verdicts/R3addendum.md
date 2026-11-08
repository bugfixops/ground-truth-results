# Coordinator addendum — SelectionTracker hashCode rows (supersedes L1's OPEN hold for these five rows)

L1 held 95/35, 99/18, 112/30, 73/31, 3/26 OPEN pending a printed androidx
MutableSelection/SelectionTracker source. The coordinator has now obtained the
print below. This addendum decides all five rows as Muse's own decision (never
Yang's), for user/Yang review.

## Pinned version (from the branch, not guessed)

`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/build.gradle`
(branch work-2026-10-31, connector fetch, blob SHA 0c0170bc88e129a6bdf1bc01a96c9a5215a99a09):
`implementation 'androidx.recyclerview:recyclerview-selection:1.1.0'`.

## Print obtained (version caveat stated, not hidden)

`androidx/androidx`, ref `androidx-main`, via the GitHub connector (no token):
- `recyclerview/recyclerview-selection/src/main/java/androidx/recyclerview/selection/MutableSelection.java`,
  blob SHA 689e6bc1b0b3ff69be1364a5b79978d9675d93a4 (2,390 bytes):
  `public final class MutableSelection<K> extends Selection<K>`, with add /
  remove / copyFrom / clear all delegating to super.
- `recyclerview/recyclerview-selection/src/main/java/androidx/recyclerview/selection/Selection.java`,
  blob SHA 72dcf2c7ac3fd91560cef42b3cc45ac639190616 (8,114 bytes).
The 1.1.0 tag was not resolved through the connector in this session (the
preference 1.2.1 tag attempts failed ref resolution; no separate tag guess
was retried for selection). The print is therefore androidx-main, NOT pinned
1.1.0. Revert condition: if a pinned 1.1.0 print shows non-hash-backed
storage with no hashCode reliance, all four key rows revert to OPEN (D30
literal reading); they do NOT flip directly to UNREACHABLE on a non-hash
print without a further merger ruling.

## What the print shows (Selection.java, androidx-main)

- Storage (lines 63-68): `final Set<K> mSelection;` /
  `final Set<K> mProvisionalSelection;`, constructed as
  `mSelection = new LinkedHashSet<>();` (:67) and
  `mProvisionalSelection = new LinkedHashSet<>();` (:68).
  LinkedHashSet is hash-backed: add / contains / addAll dispatch to the
  element's hashCode()/equals().
- `contains(key)` (:82-83): `mSelection.contains(key) ||
  mProvisionalSelection.contains(key)` — hash lookup on the key.
- `add(key)` (:183-184): `return mSelection.add(key);` — hash insertion
  of the key, invoking key.hashCode().
- `copyFrom(source)` (:207-212): clears then
  `mProvisionalSelection.addAll(source.mProvisionalSelection)` (and the
  primary set likewise) — hash insertion of every copied key.
- `Selection.hashCode()` (:232-233) combines the SETS' hashCodes; that is
  the Selection object's own hashCode, NOT the basis here. The basis is the
  LinkedHashSet operations on keys above.

## Application to the rows (with L1's verified in-app sites)

L1 verified the app's copySelection sites (fragments copying the tracker
selection into a MutableSelection, which runs copyFrom → addAll → hash
insertion of every key) and the selection-add path (user selection adds keys
via add() → hash insertion). The keys are the row objects themselves:
- 112/30 TorrentListItem.hashCode — TorrentListItem keys (MainFragment
  copySelection sites :575-576/:599-600/:610-611 per L1).
- 99/18 FeedChannelItem.hashCode — FeedChannelItem keys (FeedFragment
  copySelection :446-447/:466-467/:483-484/:496-497/:511-512 per L1).
- 95/35 TrackerItem.hashCode — TrackerItem keys (DetailTorrentTrackersFragment
  copySelection :362-363/:376-377 per L1).
- 73/31 FileItem.hashCode — TorrentContentFileItem keys enter MutableSelection
  (DetailTorrentFilesFragment copySelection :438-439/:496-497/:511-512 per L1);
  TorrentContentFileItem defines no hashCode, so the LinkedHashSet dispatch
  lands on the inherited FileItem.hashCode. Inheritance step stated, not
  assumed: L1 verified TorrentContentFileItem has no own hashCode.

## Verdicts (coordinator decision D36)

- 112/30, 99/18, 95/35, 73/31 — OPEN → REACHABLE INFERRED. Reason: printed
  hash-backed (LinkedHashSet) storage + printed hash-insertion operations
  on keys on the app's printed copySelection/selection paths; dispatch is
  library-internal, hence INFERRED, not SOURCE.
- 3/26 TagInfo.hashCode — OPEN → UNREACHABLE no_trigger_in_app INFERRED.
  Reason (distinct from the four above): L1 verified NO SelectionTracker
  <TagItem> site exists anywhere in the 281 files, so the MutableSelection
  print cannot reach TagInfo at all; its only printed paths run through
  drawer TagItem.hashCode (10/39, now UNREACHABLE) and ui/tag TagItem.hashCode
  (11/7, standing UNREACHABLE); L1's saved full-scope grep found zero other
  triggers. No printed route exists: no-route rule (P1), not a guess about
  the library. If a printed trigger for TagInfo.hashCode outside those two
  delegators is later produced, 3/26 reverts to OPEN.

Note on D30: this addendum follows D30's outcome-1 branch (hash-backed print
→ REACHABLE) for the four key rows, and resolves 3/26 on the independent
no-route ground above rather than on the MutableSelection print.
