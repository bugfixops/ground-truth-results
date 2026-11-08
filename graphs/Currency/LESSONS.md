# Currency — lessons

- Read the framework source before modelling a broadcast: the implicit
  `ACTION_APPWIDGET_UPDATE` reaches the app's own manifest receiver
  because Android 8.1 limits that action to the caller's own package
  (ActivityManagerService.java:19199-19224) and the delivery skip needs
  both component and package to be null (BroadcastQueue.java:1267-1279).
  A recalled framework rule would have marked the widget routes
  unreachable; the printed lines say otherwise.
- Split a node when its guard splits: the derived route to
  `ChartActivity$DateAxisValueFormatter.getFormattedValue` went through
  `onActivityResult` via Back (RESULT_CANCELED) and then took an edge
  needing RESULT_OK. `onActivityResult` is now `@OK` and `@CANCEL`
  nodes, and `check_routes.py` flags exactly such guard contradictions.
- Re-audit every guard against the code, not the old labels: 23 of the
  140 reachable labels changed (widget methods gained ENV `other_app`,
  the picker restore gained ENV `hardware`, bundled-rates readers gained
  STATE `data`), and the 74 framework claims first recalled from memory
  were re-read against Android 8.1.0_r1 (plus MPAndroidChart 3.1.0) —
  none was wrong, but only the re-read citations count as evidence.
- Report the drawn sample count, not the requested one: seed 20261025
  draws 27 methods today, while the recorded final sample has 28 path
  rows (3 rows not redrawn, 2 newly drawn methods unchecked). A judged
  log is not rewritten to chase a redraw; only a row failing build
  validation changes, and the drift is recorded instead.
- Treat check-8 hits as triage, not contradictions: the one hit,
  `Singleton.getList` called from `ChartActivity.onCreate`, is exactly
  the dead else-branch its `branch_never_taken` reason already
  explains (instance is null whenever onCreate starts).
- Keep unclear unclear: the widget routes (launcher behaviour) and
  `Main.onEditorAction` (soft keyboard / IME behaviour) stay unclear
  because their blocking steps live in another app's code that was not
  read; app-side evidence alone must not upgrade them to correct.
- Make the log writer fail loudly: the Currency writer seeds once,
  validates every row against the built graph, and stops on any
  mismatch instead of writing a partial file — including stopping when
  the source trees it checks refs against are absent, as a synthetic
  DEVICE-rows test proved.
