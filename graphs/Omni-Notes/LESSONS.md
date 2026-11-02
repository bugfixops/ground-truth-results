# Omni-Notes — lessons

- Resolve file locations through `method_list.json` class paths, never guesses: the first IntroActivity fetch failed ("path does not exist") because the root package was guessed; the class path `it/feio/android/omninotes/intro/IntroActivity` gave the correct `intro/` path at once.
- Classify a checker's bad count before it means anything: `check_bytecode_lines.py` first reported 297 bad edges, but all 297 were "file not found" for 10 unheld files and zero were genuine line mismatches among held files. Fetching the 10 files turned it into a clean result instead of a false failure.
- A partial cache is never a pass: `check_citations.py` first failed on exactly one unheld framework file (AdapterView.java); the fix was fetching that file and re-running, not declaring the partial run good.
- One wrong best route does not mean a wrong label: `DbHelper.deleteNote` is REACHABLE (a real Merge path exists), but the drawn best route is inconsistent because a STATE cannot express how an editor was opened. Record the modelling limit and leave the label alone; do not force an edge fix that breaks the build.
- Clinit edges are a convention, not a temporal claim: `X.<init> -> X.<clinit> -> X$1.<init>` means "first use triggers class init". Note it in the judgment; do not "fix" the direction.
- Verify a file's identity before mirroring it: the branch root `AGENT_NOTES.md` turned out to be AmazeFileManager's notes, not Omni-Notes'. The local `AGENT_NOTES.md` was started fresh instead of copying another app's log.
- Tool coverage never flips a label: `sanity_check.csv` shows 0 UNREACHABLE-but-ran contradictions; 79 ENV-gated-but-ran methods are expected where the runs granted permissions or the gate is an exception branch.
