# LESSONS: what found real errors in AnyMemo

- A lifecycle callback with "no automatic trigger" (onDestroy, onConfigurationChanged) is not evidence it is dead.
  All six round-1 placeholders turned out REACHABLE once the real exit was read: a dialog dismiss(), a finish() in
  restartActivity(), Back on an activity with no onBackPressed override, or a declared onConfigurationChanged.

- "Ran in a tool run" (the sanity check) only proves a method executed; it never gives the trigger. Every verdict
  here was decided from the source, not from coverage.

- Read the exit sites, not just the callback. CardListActivity.onDestroy had a finish() in restartActivity(), but
  restartActivity is itself unreachable, so the real exit is Back; the finish() site alone would have been the wrong
  trigger.

- Check for the absence of a call too. QuizLauncherDialogFragment has no dismiss() and no setCancelable(false)
  anywhere in the file, which is what makes the default cancel path the only destroy trigger.

- Per-host fragment cloning hides automatic CALL edges under @host names. The ten "dropped" edges were all present as
  @AM / @DBX variants; searching only the base pair would have reported them missing.

- A tool's known bug can silently truncate the evidence. show_route.py dies on any citation containing a comma
  (for example "File.java:594, 480"); the route must then be read from the edge list and the comma ranges printed by
  hand, or whole routes go unchecked.

- A heuristic route check can false-positive on explanatory text. check_routes.py flagged the import route only
  because the picker edge's ENV text contains the word "RESULT_CANCELED" (describing the device-less baseline), not
  because a guard actually contradicts the route.

- Overnight connector lesson: the GitHub connector cannot display files over
  ~1 MB and offers no chunked fetch, so a graph whose auto_calls.json exceeds
  that limit cannot be rebuilt from connector fetches alone; a partial NO-AUTO
  build still validates the hand-written graph (here it reproduced all 241
  UNREACHABLE verdicts exactly) but must never be reported as the gate build.
