# MMEX B7 run log — private staging only (no push, no tree edit, no F1 claim)

App: MMEX only. This run produced audited-ready outputs in
`helper/b7-run/` (this directory's siblings are the deliverables; the
working evidence lives in `helper/b7-run-scratch/`). Nothing in this
run was pushed, the merger tree was not edited, and no verification
row was hand-edited: every row in `verification.csv` was written by
`make_verification.py` alone. No literal tick marker appears in any
deliverable of this run.

## 1. Session probe (verified by re-reading, never by exit code alone)

Work dirs used, no temporary directory anywhere:

- `helper/b7-run/` (deliverables)
- `helper/b7-run-scratch/` (private build, private run layout, smoke
  test, id/methods diffs, saved tool outputs)

Results, each verified by re-reading the file:

- bash `echo`: wrote and re-read `PROBE_OK` correctly.
- Python `open().write()` with re-read: wrote `PROBE_WRITE_123` and
  re-read it exactly.
- `cp`: copied `sample_30_final2.txt` and re-read it identical to
  the source (2,145 bytes).

All three write paths worked. No adaptation was needed.

## 2. Fresh private rebuild of the current tree sources

Private root: `helper/b7-run-scratch/build/`, built from:

- the tree's `graphs/MMEX/` graph files only (`graph_def.py` plus
  `graph_def_mod/01.py`, `02.py`, `03.py`, `04.py`), plus
  `method_list.json`, `auto_calls.json`, `coverage_baseline.json`
  from the same tree folder (build inputs, not graph edits);
- `tools/` dereferenced from the clone;
- `fw_src/` dereferenced from the clone (the tree's `fw_src` is
  partial; the clone's is the intact full copy);
- `final_java_only/MMEX/` dereferenced from the clone (the clone's
  full `final_java_only/` tree contains a cyclic `Currency/Currency`
  symlink that breaks a whole-tree dereferenced copy, so only the
  MMEX subtree was copied; MMEX needs nothing outside it).

All 5 graph files md5-match the tree exactly (and match the
final-redraw record, so the tree has not changed since the redraw):

- `graph_def.py` `cfa264061a68e4b54f3ac04db8ee0ef0`
- `graph_def_mod/01.py` `7ff348e3970ec156d23b24026b616071`
- `graph_def_mod/02.py` `87f7965c7f522d17b49a35dfc5f57762`
- `graph_def_mod/03.py` `91dab033c415e8e6594b39b04ca08752`
- `graph_def_mod/04.py` `b316a0df44e05f75ef0eeb054f8a1390`

Build command (from the private root):
`python3 -I tools/build_graph.py graphs/MMEX mmex`
Full output saved as `helper/b7-run-scratch/build_report.txt`.

Build numbers, re-read from that report (all match the expected
final tree state; no stop condition fired):

- methods 4270, edges 8441
- verdicts: REACHABLE 3430, UNREACHABLE 840
- unreachable by kind: branch_never_taken 13, closed_by_api_level 9,
  framework_never_calls 77, no_trigger_in_app 741
- errors 0, warnings 0
- labels confirmed by: INFERRED 2775, SOURCE 1495

Checks on the private build, saved in `helper/b7-run-scratch/`:

- check 2 (citations): 250 distinct, 0 problems
  (`check2.txt`).
- check 3 (routes): 0 routes flagged (`check3.txt`).
- check 4 (bytecode lines): 6019 checked, 616 skipped, 149
  implicit, 0 where the cited line does not show the callee
  (`check4.txt`).
- check 8 (`scan_unreachable.py MMEX --callers`): 19 of 840
  unreachable methods have a bytecode caller outside the set
  (`check8.txt`) — exactly the expected figure; reported, not
  hidden, and not a B7 blocker (check 8's acceptance is the
  caller-named explanation record, which is a B4 artifact, not a
  B7 row).

This build's `out/methods.csv` + `out/mmex_trigger_graph.json` are
the writer inputs. The tree's stale `out/` (8256 edges) was NOT
used for any number in this run.

Sanity check: this fresh `methods.csv` is byte-identical to
`helper/final-redraw-scratch/build/graphs/MMEX/out/methods.csv`
(`cmp` silent), and the fresh trigger JSON is likewise
byte-identical to the redraw build's JSON. Fresh-output md5s:

- `methods.csv` `6f64c8dda1bb3512577c9c04c8a60f8e`
- `mmex_trigger_graph.json` `2b2bce521f5c3aab8caf1a020b2afd7c`

## 3. Private run layout

Private root acting as repo root:
`helper/b7-run-scratch/run/` (layout `graphs/MMEX/` with
`make_verification.py`, `out/`, `scratch/`), built as:

- `graphs/MMEX/make_verification.py`: copy of the tree writer,
  md5 confirmed `d47e5aac7a12b74f81a477a4c73c37b8`, 13,184 bytes
  — the fixed writer, unmodified.
- `graphs/MMEX/out/methods.csv` +
  `graphs/MMEX/out/mmex_trigger_graph.json`: copies of the fresh
  private build's outputs from section 2.
- `graphs/MMEX/scratch/route_table.md`: exact copy of
  `helper/final-judge/route_table_final.md` (`cmp` silent; no
  reformatting — the final-judge audit confirmed the format
  parses under the fixed writer's `TABLE_HEADING` regex).
- `graphs/MMEX/scratch/sample_30_final2.txt`: exact copy of
  `helper/final-redraw/sample_30_final2.txt` (`cmp` silent).
  Header line: `# MMEX: 30 of 3430 reachable methods, 344 distinct
  edges on their routes (seed 20261025)`.
- `graphs/MMEX/scratch/route_judgments.tsv`: generated
  mechanically (section 4).
- `graphs/MMEX/scratch/corrected_edges.tsv`: empty file
  (section 5).

The writer requires `route_table.md` beside the sample file;
that requirement is satisfied exactly (same directory,
`graphs/MMEX/scratch/`).

## 4. route_judgments.tsv — generated mechanically, never hand-written

Generation script (run from the private layout): parse every
`### N. <method> — <stratum>, N steps — VERDICT` heading of
`route_table.md` with the writer's own heading regex, lowercase
the verdict word, and emit one TSV row per route:

- `method`: heading method, verbatim.
- `result`: heading verdict word, lowercased.
- `confirmed_by`: `SOURCE` for all 30 rows. Basis: every verdict
  was established by the final-judge step-by-step judging of
  printed source (`helper/final-judge/JUDGING.md`); `SOURCE` here
  records the judging basis, not a claim that every step is
  source-evidenced — INFERRED steps are flagged inside the table
  body and in the note. No DEVICE value is used (D7 is separate).
- `ref`: `route_table.md` (the table carries the full per-route
  evidence; the writer cross-checks method + verdict only, and
  `ref`/`note` cannot be mechanically cross-checked against the
  table, per the writer-fix record — see section 9).
- `note`: `Final table route N: ` followed by the route's first
  body bullet, line-wrapped lines joined with single spaces, by
  the same script. No note was typed by hand; every note is a
  substring of the table body.

Mechanical verification of the generated TSV (re-read, not
trusted from the generator's exit code):

- 30 lines, 5 tab fields each, all `confirmed_by` SOURCE, all
  `ref` route_table.md.
- Verdict tally: correct 20 / fixed 8 / unclear 2 / wrong 0 —
  exactly the audited final table
  (CORRECT 20 / FIXED 8 / WRONG 0 / UNCLEAR 2 = 30;
  error rate 8/28 = 0.2857).
- Table-order match record: draft order = sample order, verified
  mechanically — the generator asserted the heading method
  sequence equals the sample file's method sequence (30/30, in
  order). The writer itself enforces set + verdict, not order:
  it refuses on a sampled method without a table entry, a table
  entry for a non-sampled method, or any verdict-word mismatch,
  but it does not check order; the order equality above is this
  run's own mechanical record, not a writer guarantee.
- The same mechanical check was repeated against the
  tree-staged `graphs/MMEX/scratch/route_table.md`: method +
  verdict + first bullet match for all 30 routes (the tree table
  differs from the helper draft only in its preamble header and
  path wording; from `## Final tally` onward the two files are
  byte-identical). The judgments are therefore valid against
  either copy.

Deliverable copy: `helper/b7-run/route_judgments.tsv`
(13,804 bytes, md5 `eca667306b279334aa4c579f08f95637`, `cmp`
silent against the run-layout original).

## 5. Corrected-edges decision: ZERO edge rows (empty file)

The fixed writer's edge-row semantics (docstring + code, read
before running): an `edge` row is emitted for exactly one thing —
a corrected edge listed in `scratch/corrected_edges.tsv`
(`edge_id`, `result`, `confirmed_by`, `ref`, `note`); every
listed id must exist in the trigger JSON edge set, or the writer
refuses. The file is REQUIRED: absent it refuses; an empty (or
comment-only) file is the explicit way to record zero edge rows
and passes with 0 edge rows.

Decision, on evidence, not guess: NO edge qualifies as a
corrected edge for the final table, so B7 carries 0 edge rows
and `corrected_edges.tsv` is empty (0 bytes, md5
`d41d8cd98f00b204e9800998ecf8427e`).

Reasoning:

- The audited final judging (`route_table_final.md`,
  `JUDGING.md`, audit PASS) is route-level: it names no edge as
  a B7 corrected-edge row and supplies no corrected-edge list.
  Its FIXED steps are citation/guard readings recorded on the
  route's path row (and its label row, see section 8), not
  separately corrected edges with audited ids/refs.
- The B6 fix log (`merger/scratch/fix_log.md`) records graph
  construction (edges added, suppressed, retargeted in B6 and
  the post-B6 implementations). Those changes are already
  represented in this output through the path rows' current
  `route_edge_ids` and the label rows; re-listing them as edge
  rows would double-count construction as route-check evidence.
- B7_PREP left this decision open (checklist item 7: "which (if
  any) edge rows B7 emits"); the writer-fix record then supplied
  the explicit empty-file convention for exactly the zero-row
  case. Inventing edge rows from FIXED steps, or from B2/B3
  citation/line corrections (whose re-issued ids are already
  handled by the ID map in `B7_ID_MAP.md`), would violate the
  no-invention rule for this run.
- The AnyMemo precedent (45 hand-written edge rows for
  individually checked exit/rotation/framework edges) does not
  transfer: MMEX has no equivalent audited per-edge list, and
  the MMEX writer takes edge rows only from the TSV, which no
  audited MMEX source populates.

If the merger or an auditor later identifies a qualifying
corrected edge with audited evidence, the remedy is to populate
`corrected_edges.tsv` and re-run the writer — never to hand-add
a row to `verification.csv`.

## 6. Writer runs (determinism proof + refusal smoke test)

Exact invocation, from the private root
(`helper/b7-run-scratch/run/`), with a repo-relative sample path
per brief section 4:

```
python3 graphs/MMEX/make_verification.py graphs/MMEX/scratch/sample_30_final2.txt
```

Run 1 stdout (saved as `helper/b7-run-scratch/writer_run1.txt`):

```
wrote /home/hatch/workspace/finish/work/MMEX/helper/b7-run-scratch/run/graphs/MMEX/verification.csv: 900 rows (30 path, 870 label, 0 edge)
make_verification: 215 label notes truncated at 300 chars (marked …[truncated])
```

Run 2 stdout (saved as `helper/b7-run-scratch/writer_run2.txt`):
identical lines. `cmp` of the two outputs silent; both md5
`0e5fb3a551cd7d954a00d38466fe33a0`. Determinism proven by
two byte-identical runs (brief section 3 rule 5).

No qualifier line was printed: the final table has no
parenthetical verdict qualifier on any heading (the B6-era
route-29-style qualifier case does not occur in the final
table), so the writer's qualifier branch was not exercised
here; the verdict-word matching itself was exercised on all
30 routes and passed.

Refusal smoke test (one tripwire only; the full tripwire suite
was already audited for the fixed writer and was not re-run):
in a separate scratch copy
(`helper/b7-run-scratch/smoke/`, a copy of the run layout
including its prior `verification.csv`), `corrected_edges.tsv`
was replaced with a single bogus row
(`EDEADBEAF`, correct, SOURCE, route_table.md, smoke-test note)
and the writer was invoked identically. Result, verbatim:

```
make_verification: REFUSED: corrected edge no longer exists (text changed): EDEADBEAF
```

Exit code 1, and the copy's prior `verification.csv` was
byte-identical afterwards (md5 `0e5fb3a551cd7d954a00d38466fe33a0`
before and after; `cmp` against the real run output silent).
The tripwire is live: a failed run leaves prior output
untouched, and a failed run must never be mistaken for a fresh
successful run — every B7 acceptance check in this log rests on
the `wrote ...` stdout line plus re-reading the output, not on
a file merely existing.

## 7. verification.csv — counts and shape (all re-read)

Deliverable: `helper/b7-run/verification.csv` (359,176 bytes,
md5 `0e5fb3a551cd7d954a00d38466fe33a0`, `cmp` silent against
the run-layout output). 901 lines = header + 900 rows.

- Header exactly: `type,item,result,confirmed_by,ref,edges,note`.
- Rows sorted by (type, item): verified mechanically (key
  sequence equals its own sort) — edge group first (empty here),
  then label, then path.
- 30 path rows: tally correct 20 / fixed 8 / unclear 2 /
  wrong 0; every path row's edges equal its method's current
  `route_edge_ids` from the fresh `methods.csv` and every path
  edge exists in the fresh trigger JSON edge set (both enforced
  by the writer; a mismatch would have refused).
- 870 label rows: 840 UNREACHABLE methods (all `result`
  correct, `confirmed_by` from the built labels, SOURCE or
  INFERRED only) + 30 sampled reachable methods (see
  section 8).
- 0 edge rows, per the section 5 decision.
- 215 label notes carry the explicit truncation marker
  (`…[truncated]`, cut at 300 characters); the count matches
  the writer-fix audit's pre-implementation count (215 texts
  over 300 characters, 2 at exactly 300 unmarked) — the
  UNREACHABLE reason texts are unchanged by the post-B6
  implementations, so the count is unchanged too. No label note
  was silently cut.
- No row was hand-edited. The writer errored on nothing; had
  it refused on valid inputs, this log would report the refusal
  text verbatim and stop (that stop condition did not fire).

## 8. W7 semantics note (required)

Sampled reachable methods get a label row carrying the path verdict.

That is the fixed writer's docstring-intended behaviour
(docstring: "label - one per UNREACHABLE method in the built
labels, and one per sampled reachable method"; code: the
sampled label row carries the same result, confirmed_by, ref
and note as its path row), confirmed as intended by the
writer-fix audit (W7, no code change). Consequence for reading
this CSV, stated plainly so no reviewer misreads it: 10 label
rows for REACHABLE methods carry a non-`correct` result
(8 fixed + 2 unclear) — those are route-check verdicts, not
label verdicts. The 860 `correct` label rows are the 840
UNREACHABLE methods plus the 20 sampled reachable methods on
CORRECT routes. No DEVICE row appears anywhere (SOURCE/INFERRED
only; D7 is separate).

## 9. Audit notes on what the writer does NOT check

- `ref` and `note` are not mechanically cross-checked against
  the table (the table has no single per-route ref field). The
  mitigation applied here, beyond the writer's method+verdict
  check, is that the TSV itself was generated mechanically from
  the table (section 4): method, verdict, and first-bullet note
  are script extracts, not transcriptions, so there is no
  transcription step left for a 1-in-3 manual audit to catch on
  those fields. The uniform `ref` (`route_table.md`) and the
  uniform `confirmed_by` (`SOURCE`, section 4 basis) are the
  only non-extracted fields, and both are stated here for the
  independent auditor to judge.
- The writer enforces set + verdict, not table order (section 4).
- The writer validates path edges against the fresh JSON edge
  set (W3) and refuses on stale ids; it does not validate that
  the sample is the "right" sample beyond size 30 + judgment
  coverage + table cross-check. Sample identity here rests on
  the exact-copy record (section 3) and the sample header line,
  plus the md5 match of the tree-staged sample (see
  `STAGING_MANIFEST.md`).

## 10. ID map and old-id grep (summary; full map in B7_ID_MAP.md)

Method: mechanical id-diff between the private stage-B6
rebuild's JSON (see section 11) and the final JSON, plus a
methods.csv diff, cross-checked against the four implementation
verifications (routes 8+18, showPrerequisite, Sync v2, §9
getContext, route 14) and FIX_REPORT section 8.

- Stage-to-final retired ids: 33, every one accounted for in
  the map (Sync 12 + §9 11 + 8+18 7 + showPrerequisite 1 +
  route 14 2 = 33).
- Plus the B6 set of 10 (pre-stage-B6 retirements, absent from
  both JSONs) and the intermediate §9 mirror id Eafb31232
  (§9-created, Sync-retired — landing order decides: it is a
  retired id, never a final new id).
- Total retired ids grepped in `verification.csv`: 44.
  Result: 0 hits for every id, verbatim grep output saved in
  `B7_ID_MAP.md` (section 6 there). Any hit would have been a
  stale-row bug and a stop condition; none occurred.
- Added ids: 218 stage-to-final. Reconciliation closes
  exactly (see `B7_ID_MAP.md` section 5): per-implementation
  gross additions sum to 219, minus the 1 intermediate id
  (Eafb31232) that was added by §9 and retired by Sync, equals
  the measured 218; net edge change +185 (8256 to 8441).
- Verdict flips across the whole stage-to-final methods diff:
  0 (all 4270 methods keep their verdict); 291 methods differ
  in some column, 255 in `route_edge_ids`, 41 in
  `steps_from_launch`, 69 in the `incoming_edges` count.

Metadata shifts B7 must expect, not misread as regressions
(full detail in `B7_ID_MAP.md` section 4):

- §9 M3: `confirmed_by` SOURCE to INFERRED for exactly 5 tail
  methods (DatabaseManager.getContext,
  getDbExternalStorageDirectory, getDefaultDatabaseDirectory,
  getExternalFilesDirectory, getPackageDirectory); incoming
  counts change for 12 methods in §9's own accounting.
- One further `confirmed_by` change in the combined diff:
  Calculator.getAmountFromResult INFERRED to SOURCE (the 8+18
  variant chain gives it a source-evidenced route).
- Sync's 6 count-only rows (+3 each) and route 14's 15
  count-only rows (+2 each) are per-package figures relative
  to each package's landing baseline; in the combined
  stage-to-final diff they aggregate with other packages'
  changes on shared methods (e.g. SyncManager.getContext
  10 to 14 = §9 +1 and Sync +3; Dataset.getUri keeps its
  route-14 +2 count but its route also carries the
  showPrerequisite id swap). The combined diff is the
  authoritative B7 record; the per-package figures are cited
  for explanation, never added together naively.

## 11. Stage-B6 rebuild (ID-map baseline)

Private root: `helper/b7-run-scratch/stageB6-build/`, from the
stage-B6 graph sources (`graph_def.py` +
`graph_def_mod/01.py`, `02.py`, `03.py` — no `04.py` at that
stage) with the tree's build inputs (md5-identical to the
clone's) and the same dereferenced clone `tools/`,
`fw_src/`, `final_java_only/MMEX/`. Stage-B6 graph md5s:

- `graph_def.py` `c9d52ec90dfcd6460a923169591a6594`
- `graph_def_mod/01.py` `209348bddf86c87a7070b7ebd641670c`
- `graph_def_mod/02.py` `87f7965c7f522d17b49a35dfc5f57762`
  (identical to the current tree file)
- `graph_def_mod/03.py` `9bfed6f0f6d2acf3eed0f07fb5278c6a`

Rebuilt numbers (saved as
`helper/b7-run-scratch/stageB6_build_report.txt`): 4270
methods, 3430 REACHABLE / 840 UNREACHABLE, 8256 edges, errors
0, warnings 0 — exactly the pre-implementation baseline (and
exactly the tree's stale `out/build_report.txt`, which is
consistent with the tree `out/` being the post-B6 build, not
with it being current). Full id-diff saved as
`helper/b7-run-scratch/id_diff.txt` (33 retired, 218 added);
full methods-diff evidence saved as
`helper/b7-run-scratch/methods_diff.txt` (`incoming_edges`
treated as the count column it is: 69 count diffs, 36 of them
count-only; the authoritative figures are in section 10 above
and in `B7_ID_MAP.md`).

## 12. What was NOT done (scope guard)

- No push (no GitHub connector write of any kind in this run).
- No merger-tree edit: the tree was read only. The run layout,
  build roots, and smoke copy are all under
  `helper/b7-run-scratch/`; deliverables are under
  `helper/b7-run/`.
- No hand edit of any verification row; no hand-written
  judgment; no invented edge row.
- No F1 claim: F1 follows in brief section 5.5 and needs the
  CI rebuild and the merger's staging + independent audit of
  these outputs first.
- No device work: no DEVICE rows, no emulator run, no
  `device/` input touched.
- No stop condition fired: fresh build numbers matched
  4270/3430/840/8441/0/0; the writer did not refuse on valid
  inputs; no retired id appears in `verification.csv`; row
  counts are 30/870/0; two runs are byte-identical;
  judgments match the table (method + verdict, all 30); no
  hand edit was needed; no tick marker appears in any
  deliverable (verified by scan before finishing — see
  section 13).

## 13. Deliverable verification (re-read before finishing)

Files in `helper/b7-run/`, each re-read and confirmed
non-empty (except the intentionally empty
`corrected_edges.tsv`), with every number tracing to a run in
this log:

- `verification.csv` — 900 rows, md5
  `0e5fb3a551cd7d954a00d38466fe33a0`.
- `B7_RUN_LOG.md` — this file.
- `B7_ID_MAP.md` — full map + grep evidence.
- `readme_notes.md` — brief section 4 five headings, in order.
- `LESSONS.md` — bullets from this run's record (no tree
  LESSONS.md exists to update; this is a new draft for the
  merger to stage).
- `route_judgments.tsv` — 30 mechanical rows, md5
  `eca667306b279334aa4c579f08f95637`.
- `corrected_edges.tsv` — empty by decision (section 5).
- `STAGING_MANIFEST.md` — what the merger copies vs what
  already sits in the tree.

Tick-marker scan over all eight deliverables: performed as
part of finishing (grep for the literal marker pattern); the
scan is recorded here as done, with no marker found. (The
scan command itself is not reproduced because its pattern
would itself contain the marker string; the auditor can
re-run the project's standard marker grep over
`helper/b7-run/`.)
