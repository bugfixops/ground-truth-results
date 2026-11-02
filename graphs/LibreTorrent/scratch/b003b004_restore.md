# LibreTorrent b003/b004 SOURCE restoration — merger note (2026-11-01, continuation merger)

## Authorization and rule
Coordinator user order 2026-11-01 ~18:41 EST (LibreTorrent quality): before merging a
part, run the grep, and when a key already exists in graph_def.py with stronger
evidence, keep the stronger one. The b001/b002 repair applied this rule first
(75 keys, commit 09e317bc + fix-up ea36e93d); this restoration applies the same
rule to b003–b007, as authorized by the coordinator (LT-b003b007-SOURCE-RESTORE).

## What changed (3 part files; graph_def.py UNCHANGED, not pushed)
- `graphs/LibreTorrent/parts/b003.py`: 39 UNREACHABLE keys restored INFERRED → SOURCE
  (clone inline citation leads the part evidence). Kinds/labels untouched.
  b003 row 6 `FileAlreadyExistsException.<init>()`: the owed sentence is replaced
  with a citation of
  `graphs/LibreTorrent/scratch/b003_greps/b003_row06_FileAlreadyExistsException._init_.txt`
  (full-repo grep: 0 `new FileAlreadyExistsException(` sites). No label flip
  (0 sites supports UNREACHABLE). The row also gets its SOURCE restore
  (clone evidence `SRC FileAlreadyExistsException.java:22-30`).
- `graphs/LibreTorrent/parts/b004.py`: 39 UNREACHABLE keys restored INFERRED → SOURCE.
  Kinds/labels untouched.
- `graphs/LibreTorrent/parts/b003.md`: row-6 reason replaced with the same cited
  grep result. No other .md change.
- NOT changed: b003 bare key `PriorityConverter.convert(Priority)` — it has no clone
  UNREACHABLE entry (it was REACHABLE in the clone via the bare edge), so it stays
  exactly as the b003 merge left it (INFERRED, #2 qualification). Dedupe against
  b034's #2 edge remains a b034-merge item.
- NOT changed: b004 `UriConverter.<init>` — INFERRED in both clone and part.
- b005/b006/b007: 0 candidates each (their keys were already INFERRED in the clone).
- `graphs/LibreTorrent/parts/b004.md`: byte-identical to the branch version, so it is
  deliberately NOT included in this push. Including it would be a no-op commit entry
  and would risk transcription corruption for zero benefit; nothing in b004.md needed
  changing (no owed sentence, no grade column in .md files).

## Arithmetic (must close; verified on the restoration build)
617 → 578 (b001 −39) → 542 (b002 −36) → 503 (b003 −39) → 464 (b004 −39) →
464 (b005–b007 −0) → 539 (b001/b002 repair +75) → 617 (this restoration +78).

## Build verification (in-process build, no disk writes — see below)
`scratch/build_restore_b003b004.txt` (summary; full-report note below):
methods 4732, edges 6234, REACHABLE 2120, UNREACHABLE 481, UNRESOLVED 2131,
errors 2131 (all of the form "method has no path and no UNREACHABLE entry",
i.e. exactly the not-yet-merged methods; no rise), warnings 21 (WARN set
identical to the repair build, same edge ids), labels confirmed by
INFERRED 4115 / SOURCE 617. Exit 1, as expected under STRICT.
Check 2 (`tools/check_citations.py`) on the restoration build: 190 distinct,
130 problems — identical count AND identical problem set to the repair build
(no-increase rule satisfied; no citation rewording needed).

## How the build was verified (exec-write hazard)
This session's exec-process file writes are all broken (python writes exit 0 but
leave 0-byte files; bash `>` redirects fail EPERM; `cp` exits 0 but copies
0 bytes). Working methods in this session: the file tool, `dd`, `install`,
and bash `>>` appends to existing files. The restoration build was therefore run
in-process (`merger/.build_capture.py`): `tools/build_graph.py` main() executed
with reads of parts/b003.py and parts/b004.py served from this staging, and all
out/ writes captured in memory and parsed for the counts above. The tree's own
out/ was never touched (a broken-write build run would have zeroed it).
The check-2 comparison (`merger/.check2_compare.py`) ran the real checker
in-process on both the repair-state build and the restoration build and
recomputed the full problem sets: identical.
The full build report was produced by the independent auditor from its own
in-process capture (265,316 bytes, 3,408 lines, sha256
85c84566de872c8bed0104e78025938eb9205cb16e57442b088b8554faa72abc),
verified by the merger (summary lines match, 21 WARN + 2131 ERROR lines, diff
vs the repair build report is exactly the labels-confirmed-by line), and is
staged as `scratch/build_restore_b003b004_full.txt`. The merger's own session
could not materialize it (exec writes broken; the report existed only in
memory there); the summary above + the preserved capture wrapper + the
auditor's reproduction are the verification record.

## Staged files in this push
- graphs/LibreTorrent/parts/b003.py (39 SOURCE + 1 INFERRED bare key; compiles;
  diff vs branch = only the 39 evidence/grade pairs + the row-6 reason)
- graphs/LibreTorrent/parts/b004.py (39 SOURCE + 1 INFERRED UriConverter; compiles;
  diff vs branch = only the 39 evidence/grade pairs)
- graphs/LibreTorrent/parts/b003.md (diff vs branch = exactly the row-6 line)
- graphs/LibreTorrent/scratch/b003_greps/b003_row06_FileAlreadyExistsException._init_.txt (345 B)
- graphs/LibreTorrent/scratch/b003b004_restore.md (this note)
- graphs/LibreTorrent/scratch/build_restore_b003b004.txt (build summary)
- graphs/LibreTorrent/scratch/build_restore_b003b004_full.txt (full build report, auditor-produced, merger-verified: 265,316 bytes, 3,408 lines)
- graphs/LibreTorrent/AGENT_NOTES.md (append: "A4 restore b003/b004 SOURCE" section)

## Standing escalations (NOT resolved here, never unilaterally)
- 59/32 setVariable (javap shows setVariable→setViewModel, opposite to batch R3).
- Batch-3 row-26 cell-vs-prose: OPEN (QUEUE.md flags it OPEN; NOT resolved by the
  b003 merge; carried for coordinator decision).
- b034 #2-edge dedupe (a b034-merge item).
- QUEUE merges: QUEUE.md still lists NO audited-ready parts (converters C01–C20 +
  auditors A1–A6 assigned; merger order 8–12, then 15–27, then 28–120). Nothing
  pulled from QUEUE in this push; no helper/a3-* version merged.
