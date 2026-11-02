# AnkiDroid lessons (finish run)

- A task-dispatch switch is not a route: most WRONG routes (8 of 18)
  launched one DeckTask type and then took another type's branch
  (LOAD_DECK_COUNTS vs RENDER_BROWSER_QA). The fix is a rebuilt prefix
  from the actually-launched task, never a variant split of the switch.
- Dialog pages are not interchangeable: three WRONG routes conflated
  dialogs that share a page node (SyncErrorDialog types 0/9,
  ConfirmationDialog DeckPicker-full-sync vs ModelFieldEditor-rename vs
  NoteEditor-change-type). Splitting the page node by dialog variant is
  the fix; guards alone cannot carry it because BFS ignores guard text.
- A checker regex can be the bug: check 2's 3 problems came from an
  unanchored ROOT_STYLE substring match inside an already-correct
  full-path citation, and check 4's Utils failures came from the
  resolver picking the short-path api Utils over libanki Utils. Both
  were fixed on the citation side without touching tools/.
- "Already present" beats "add it": the B4 paint-sync "8 NEW entries"
  already existed in sup() blocks, and the F2/F3 shared edge
  (E47fbe466 -> Ecdba007c) had to be applied exactly once. Verify
  before duplicating, especially for SUPPRESS entries.
- Apply a fix by edge+line, never by blind replace-all: the route-17
  step-6 evidence fragment also occurs in an unrelated RESULT edge;
  the merge changed only the intended edge block and left the RESULT
  edge byte-identical.
- Never trust an exit code alone in this environment: Python writes
  can fail silently (exit 0, 0-byte file). Every build, writer and
  staging output in this run was re-read from disk and confirmed
  non-empty with expected content before any push.
- A redraw sample is not stable across id-changing fixes: the sampler
  spreads over route_edge_ids, so guard/evidence fixes that change ids
  change the sample itself. Record which sample a table covers, and
  flag a redraw/sample mismatch for a coordinator ruling instead of
  silently re-judging a different sample.
- Guards do not change BFS cost: after a guard fix, the best route can
  still show the old, now guard-inconsistent prefix. A guard-checking
  redraw (not a plain BFS re-print) is what validates a fixed route.
