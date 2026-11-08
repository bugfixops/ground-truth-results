# Omni-Notes — decisions (Muse's own, for user/Yang review)

None of these are made in Yang's name. Each states what was decided, why, and what
would change it. Nothing here was pushed anywhere; all work is local.

## D1. DEAD|FRAMEWORK_ONLY grep: report the literal 11, do not fake a 0

`grep` on the local `graph_def.py` copy finds 11 lines matching `DEAD|FRAMEWORK_ONLY`:
population (1635, 1641), SUPPRESS uses (1693-1694, 1793-1794, 1801, 1808), a comment
(2078), the conversion loop into UNREACHABLE (2136), and the reset `DEAD, FRAMEWORK_ONLY
= {}, {}` (2145). The effective legacy entries are 0: the dicts are emptied at line 2145
before the build, and the build's verdict kinds contain only the four real UNREACHABLE
kinds (no 'unclassified'). The task's check (5)-(7) asks for 0; the honest report is
"literal 11, effective 0, mechanism-only". Faking a 0 by editing the graph locally would
break the byte-identical rebuild and hide the mechanism. What would change it: a
branch-side cleanup removing the legacy-dict machinery from `graph_def.py` entirely.

## D2. verification.csv regeneration is BLOCKED; branch file kept verbatim

`make_verification.py` is not locatable on branch work-2026-10-31: absent from the
`tools/` root listing and from `tools_dev/` (only `.design_scratch/`, DESIGN.md,
design_review.json, design_review.md); a scoped `search_code` query for
`make_verification` in the repo returned total_count 0 with incomplete_results=true
(which, per the task rules, is not proof of absence elsewhere — only that no locatable
copy was found). The task says `verification.csv` is produced ONLY via
`make_verification.py`, so the branch file (196,534 B, header exactly
`type,item,result,confirmed_by,ref,edges,note`, 370 rows) is kept verbatim as the audit
log and is NOT hand-edited. Fresh judgments live only in
`scratch/sample_30_judgment.md`, never merged into `verification.csv`. What would
change it: the parent locating `make_verification.py`, after which the judgment file is
the input to regenerate from.

## D3. DbHelper.deleteNote route: judge wrong, attempt no local graph fix

The drawn best route to `DbHelper.deleteNote(long,boolean)` is internally inconsistent
(FAB-created new note + merged-note STATE; see `scratch/sample_30_judgment.md`). The
label REACHABLE is right (a real Merge path exists), but fixing the route properly needs
a new editor context (e.g. @MERGE) with its own Back/save chain — a graph-model change,
not a one-edge edit. A local edit without full verification could break the 0-error
build, and the branch `readme_notes.md` "Limits" section already documents this as the
one route that stays wrong. So: verdict wrong, no fix, parent decides whether one
documented wrong route blocks the "route checks pass" gate.

## D4. Clinit-ordering steps are a convention, not errors

Steps `X.<init> -> X.<clinit> -> X$1.<init>` (Tag, Attachment routes) mean "first use
triggers class init": the $1 CREATOR anonymous class is instantiated in static init
(Tag.java:65, Attachment.java:85). Temporally `<clinit>` runs before first use, but the
edge direction is not a temporal claim. Reachability holds either way. Judged correct
with a written note in the judgment file, not as errors.

## D5. check_citations: a targeted fw_src cache is valid; a partial cache is not a pass

The checker only consults files cited by the graph's FW-SRC evidence, so a cache holding
exactly the cited framework files is a valid run. The first run found 18 distinct cited
specs with 1 problem (AdapterView.java not held) — that run is NOT reported as a pass.
The missing file was fetched and the check re-run for a clean result, rather than
calling a partial-cache run good.

## D6. check_bytecode_lines: minimal-tree runs are reported with their caveat

The checker runs over the full graph, so a minimal tree (only route-cited files) cannot
yield a clean 0: every bytecode-cited edge in an unheld file reports "file not found".
The first run's 297 bad entries were ALL "file not found" for 10 unheld app files, with
ZERO genuine line mismatches among held files. The 10 files were fetched and the check
re-run, rather than presenting the minimal-tree output as a pass or a failure of the
graph. Residual caveat, recorded with the final result: with one copy per basename,
flavor disambiguation is limited (checker prefers `/src/main/` or a built flavor; built
flavor here is `play` per `class_files.json`); a duplicate-basename file in another
flavor folder could in principle resolve differently in a full tree.

## D7. scan_unreachable --all: not run, and not faked

`--all` searches the FULL app source tree for every unreachable method name. Only the
route-cited files plus the 10 bytecode-cited files are reconstructed here, so running
`--all` against this tree would fabricate "no other mention" results. It is reported as
not-run with this exact reason. `--callers` (needs only auto_calls + JSON) is the valid,
completed part: 5 of 254 unreachable methods have a bytecode caller outside the set, each
explained in its reason text (see `scratch/scan_unreachable_callers.txt`).

## D8. Coverage artifacts are not label evidence

`coverage_baseline.json` was fetched only to reproduce the branch build's sanity-check
artifact exactly. The sanity-check counts (848 ran, 0 UNREACHABLE-but-ran contradictions,
79 ENV-gated-but-ran) never set or change any label, per the task's label rules and the
tool's own docstring.

## D9. File locations resolve through method_list.json class paths, not guesses

The first IntroActivity fetch failed ("path does not exist") because the path was guessed
as the root package. `method_list.json` gives the authoritative class path
(`it/feio/android/omninotes/intro/IntroActivity` -> `intro/IntroActivity.java`), and the
corrected fetch succeeded. The same resolution was used for all 10 bytecode-missing
files. Guessed paths that fail are recorded as wrong guesses, never as missing files.

## D10. Branch root AGENT_NOTES.md is AmazeFileManager's, not Omni-Notes'

The file fetched as `scratch/branch_AGENT_NOTES.md` is headed "# Agent Notes -
AmazeFileManager" and contains Amaze build logs. No Omni-Notes branch notes existed to
mirror, so the local `AGENT_NOTES.md` (Omni-Notes-specific, started fresh) remains the
mirror. Nothing was copied from the Amaze notes into Omni-Notes logs.

## D11. Sketch-route Back link accepted via fragment recreation

The step MainActivity.onBackPressed@SKETCH_DRAWN -> Attachment.<init>(Uri,String) rests
on: onBackPressed saves the sketch (SketchFragment.save, guarded by
SketchView.getBitmap() != null) and pops the back stack, so DetailFragment is recreated
and its onActivityCreated attaches `mainActivity.sketchUri` (DetailFragment 385-388).
This is standard fragment-lifecycle behavior, confirmed on both ends of the link, and is
judged correct — not an error — with the recreation step stated explicitly.
