# MMEX B7 lessons — what found real errors (from this run's record)

- Rebuild privately from the tree sources plus dereferenced
  clone inputs, and never trust the tree's committed `out/`:
  it still held the post-B6 build (8256 edges) while the
  current sources build to 8441 — every B7 number taken from
  it would have been stale by 185 edges.
- Re-read every output and never trust an exit code alone: a
  failed writer run leaves the previous `verification.csv`
  byte-identical in place, so only the `wrote ...` stdout
  line plus a re-read proves a fresh successful run.
- Writer tripwires are the backstop for id re-issues: a bogus
  corrected edge, a wrong sample, or a stale path edge must
  refuse before anything is written — and the refusal was
  smoke-tested live in this run, not merely cited from the
  writer-fix audit.
- Landing order decides id overlaps; never silently union id
  sets across implementations: the §9 mirror id Eafb31232
  was a genuine new id at §9 time and a genuinely retired id
  after Sync, and only the landing order tells which.
- Generate judgments mechanically from the route table: the
  verdict errors that matter enter through transcription,
  and a script extract of method + verdict + first bullet
  leaves no transcription step for an audit to catch.
- Per-package diffs do not add: combined diffs aggregate
  (SyncManager.getContext 10 to 14 is §9 +1 and Sync +3 on
  the same row), so per-package figures explain a combined
  diff only when each is read against its own landing
  baseline.
- A zero-row decision needs an explicit artifact, not an
  absence: the empty `corrected_edges.tsv` records "B7
  carries no edge rows" in a way a missing file never could,
  because the fixed writer refuses on a missing file.

## Re-audit lessons (Kiro, November 2026)

- Clearing a baseline gate can move many best routes onto an outside entry that was cheaper before; after every baseline edit, count the methods whose best route carries an env gate, not only the cleared texts.
- A gate edit changes the edge id (the id hashes the gate texts), so device route files and verification paths that name edge ids go stale; map old to new ids by src, dst and kind before a dry run.
- Check anonymous-class numbers with javap: javac numbers them in source order, and one skipped number shifts every later class.

- Rows the Android app only reads and never writes (attachments, a base currency row) come from a desktop database: env other_app, not state.
- onActivityResult edges need the gate of their request-code case: a document-picker result case is env other_app even when the route arrives through another result.
