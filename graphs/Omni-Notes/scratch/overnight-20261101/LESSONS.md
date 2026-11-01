# Omni-Notes — lessons (local mirror notes)

- Resolve file locations through `method_list.json` class paths, never guesses: the
  first IntroActivity fetch failed ("path does not exist") because the root package was
  guessed; the class path `it/feio/android/omninotes/intro/IntroActivity` gave the
  correct `intro/` path at once.
- Classify a checker's "bad" count before it means anything: `check_bytecode_lines.py`
  first reported 297 bad edges, but all 297 were "file not found" for 10 unheld files
  and zero were genuine line mismatches among held files. Fetching the 10 files turned
  it into a clean result instead of a false failure.
- A targeted cache is valid when the tool only consults cited files — but a partial
  cache must never be reported as a pass: `check_citations.py` first failed on exactly
  one unheld framework file (AdapterView.java); the fix was fetching that file and
  re-running, not declaring the partial run good.
- One wrong best route does not mean a wrong label: `DbHelper.deleteNote` is REACHABLE
  (a real Merge path exists), but the drawn best route is inconsistent because a STATE
  cannot express how an editor was opened. Record the modelling limit and leave the
  label alone; do not force an edge fix that breaks the build.
- Clinit edges are a convention, not a temporal claim: `X.<init> -> X.<clinit> ->
  X$1.<init>` means "first use triggers class init". Note it in the judgment; do not
  "fix" the direction.
- Fetch discipline that survived a restart: one file at a time with ~30 s pauses, raw
  MCP JSON to persistent `scratch/raw/` (not `/tmp`, which the restart wiped), decoded
  immediately per file — and treat only `ok:false` as the stop signal, since a naive
  "429" substring grep false-alarmed on `graph_def.py` (which legitimately contains
  "429" as a number).
- Verify a file's identity before mirroring it: the branch root `AGENT_NOTES.md` turned
  out to be AmazeFileManager's notes, not Omni-Notes'. The local mirror was started
  fresh instead of copying another app's log.
