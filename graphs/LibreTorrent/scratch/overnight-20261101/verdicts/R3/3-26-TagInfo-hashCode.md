# R3 verdict — 3/26 TagInfo.hashCode

## Identity (verified from the work file first)
- Batch file: `phase3/work/batch3-merge-ready.md`, row 26, currently OPEN.
- Method: `TagInfo.hashCode()`, definition `TagInfo.java:94-99`.
- Prior state: OPEN under D6/D1. Its conditional table (round 2):
  flips to UNREACHABLE only if batch 10/39 flips to UNREACHABLE AND
  the project hashCode rule says implicit dispatch does not count
  without a printed trigger AND TorrentInfo.hashCode stays
  untriggered; flips to REACHABLE if 10/39 flips to REACHABLE, or a
  printed trigger appears for TorrentInfo.hashCode, or a printed
  hash-collection/log/concat caller of a TagInfo/TagItem instance
  appears; otherwise stays OPEN. The round-2 note adds: "a hashCode
  can be invoked implicitly by library/framework code with no
  app-Java call site, which is exactly the undecided project-wide
  question" — that sentence is the reason this row was held, and
  this verdict re-examines whether it still holds for THIS row.

## Verdict: UNREACHABLE, kind no_trigger_in_app, confirmed_by INFERRED
- Label change proposed: OPEN → UNREACHABLE (INFERRED).
- This is the one R3 row that moves. The reasoning, and the single
  condition on which it depends, are stated below so the merger can
  overturn it mechanically if the condition fails.

## All three in-app legs, and their current state
L1's full-scope grep (281 app Java files + 73 layout XML + 31
res/menu/xml XML fetched one at a time; saved under
`phase3/greps/L1/`) found NO trigger for TagInfo.hashCode outside
the bodies below. Each leg's host is now UNREACHABLE:
1. Drawer delegator: `ui/main/drawer/TagItem.hashCode :50-51`
   (`return info.hashCode()`) — batch 10/39, flipped OPEN →
   UNREACHABLE by L1 (`phase3/verdicts/L1/batch10.md`: zero
   external .hashCode() on drawer TagItem in grep_all_calls.txt;
   zero hash collection in grep_hash_collections.txt; consumers
   are MainActivity `TagItem::new` + drawer TagsAdapter DiffUtil
   equals/isSame + `.info` field reads only; no
   SelectionTracker for TagItem).
2. Tag delegator: `ui/tag/TagItem.hashCode :49-51`
   (`return info.hashCode()`) — batch 11/7, standing UNREACHABLE,
   verified by L1 against the full-repo standard (D6's revert flag
   did NOT revert it: the fresh L1 grep closes the "pending saved
   full-repo grep" gap its proposal recorded).
3. List leg: `TorrentInfo.hashCode :191-213`, `:210`
   `tags.hashCode()` — a List call, whose element dispatch would
   reach TagInfo.hashCode only if TorrentInfo.hashCode itself runs.
   TorrentInfo.hashCode is batch 30/8, flipped OPEN → UNREACHABLE
   by L1 (`phase3/verdicts/L1/batch30.md`: zero external .hashCode()
   on TorrentInfo; zero hash collection).
- No hash collection keyed/element-typed on TagInfo, either TagItem,
  or TorrentInfo exists (L1 grep_hash_collections.txt: every site
  is String/Integer/Long keyed; the one Set hit,
  SelectTagViewModel.java:51, holds Long ids). No databinding,
  log, or concat caller of a TagInfo/TagItem instance exists
  (L1 grep_log_concat.txt, grep_barevar_concat.txt,
  grep_databinding_text.txt). The TagsAdapter "Unknown item: " +
  item line is AbstractTagItem-typed AND instanceof-guarded — a
  TagItem never reaches it (L1 near-miss list).

## Why the "implicit library dispatch" objection does NOT save OPEN here
The objection that held this row (and the four key rows) is: some
unprinted library/framework code might invoke the method with no
app-Java call site. For the four key rows that objection is live,
because a real in-app route into library code exists (copySelection
into MutableSelection, storage unknown). For 3/26 it is not live,
because the one candidate library route has been affirmatively
disconnected, not merely left unprinted:
- A corpus-wide grep for `SelectionTracker<TagItem` (and any
  Tag-typed tracker) over `overnight/stream-A/corpus/java/` returns
  ZERO hits. L1's grep_selectiontracker.txt lists only four key
  types: TorrentListItem, FeedChannelItem, TrackerItem,
  TorrentContentFileItem. There is no SelectionTracker whose keys
  are TagItems, so no MutableSelection — hash-backed or not — can
  dispatch to either TagItem.hashCode, and therefore cannot reach
  TagInfo.hashCode through that route. The MutableSelection print,
  whatever it shows, cannot affect this row. L1's batch3 verdict
  file says exactly this: "the print alone cannot flip this row".
- No other plausible unprinted dispatcher was found for TagInfo:
  it is not a Room entity whose generated code might hash it (L1's
  Room argument covers entities; TagInfo is not reached that way
  on any printed DAO/entity), not a databinding text expression,
  not a Map key or Set element anywhere in the full-scope grep.
- This is precisely D30 outcome 2's test: "full-scope zero AND no
  plausible unprinted dispatcher → UNREACHABLE no_trigger_in_app
  INFERRED." Both halves are now met for 3/26, whereas for the
  four key rows the second half fails (their dispatcher is
  plausible and live). The rows are therefore correctly decided
  differently, and the difference is the presence/absence of a live
  route into library code, not a preference for one label.
- Dependency parity: L1 already applies this same logic elsewhere
  — 31/25 (TagInfo.toString) closed when all its concat hosts were
  UNREACHABLE, 73/32 closed when both super.toString() hosts were
  UNREACHABLE. A dependent whose every host is UNREACHABLE, with
  no other trigger and no live dispatcher, is UNREACHABLE. 3/26
  is the hashCode instance of that pattern.

## The D30-literal tension, stated plainly (merger: read this)
D30 literally lists 3/26 among the rows that "stay OPEN" if the
MutableSelection print is non-hash or unobtainable. That listing
rests on D6's premise that "3/26 flips with them via the
drawer-TagItem delegation (10/39)" on a hash-backed print. L1
disproved that premise: the delegation exists, but the tracker
link does not, so the print cannot carry 3/26 either way. This
verdict therefore treats D30's listing for 3/26 as vacated by the
failed premise, and decides the row on D30's own outcome-2 test
instead. If the merger insists on the literal D30 listing
regardless of the failed premise, the fallback is OPEN with this
file as the record — but that fallback would be holding the row
for a print already shown to be irrelevant to it, which is why it
is not the verdict here.

## Condition on this verdict (mechanical overturn rule)
This UNREACHABLE verdict stands ONLY while 10/39 and 11/7 stand
UNREACHABLE (and 30/8 stands UNREACHABLE for the List leg). If the
merger revives ANY of those three hosts to REACHABLE, 3/26 flips
with it to REACHABLE via the dependency rule (positive direction:
a REACHABLE delegator/host that calls it). If the merger overturns
this verdict to OPEN on the D30-literal ground above, that does not
disturb the four key rows, which stay OPEN on their own ground.

## What would change this verdict
- Any printed trigger outside an UNREACHABLE body: a REACHABLE
  delegator, a hash collection keyed/element-typed on TagInfo or
  either TagItem, a SelectionTracker for TagItem, or a printed
  library dispatch reaching TagInfo → REACHABLE (SOURCE if the
  trigger site itself is printed, else INFERRED via the wrapper).
- Nothing else: app-tree zero alone was never the basis (the basis
  is full-scope zero + closed hosts + affirmatively disconnected
  dispatcher).

## Hygiene
No work file edited; no push; no branch edit; no token used. This
verdict file only, under `phase3/verdicts/R3/`. The MutableSelection
print attempt is recorded in the sibling R3 verdicts and in
R3_SUMMARY.md; its non-obtainment does not block this row, for the
reasons above.
