# AnkiDroid route_25 — UNSCRIPTABLE

- Route: route_25, target CollectionLoader.deliverResult, table
  verdict FIXED.
- BFS route (11 edges, byte-identical to the route print): launcher
  -> DeckPicker -> onFinishedStartup -> showStartupScreensAndDialogs
  -> S_DLG_DECKPICKER_NO_SPACE (Ed48ce341) -> collection-not-locked
  guard (E4cf8a1d9) -> CollectionLoader chain -> target. Edge ids
  in device/routes/AnkiDroid/ROUTES.csv row route_25.
- Why unscriptable: the route is genuine only through the no-space
  dialog, whose guard is "BackupManager.enoughDiscSpace is false
  (not enough disc space for backup)" (DeckPicker.java:848-850).
  No UI action produces a not-enough-disc-space state, and the
  numeric free-space threshold that enoughDiscSpace uses is not in
  the graph or the drafts (BackupManager.java source is not in the
  workspace to read it from), so no storage-fill fixture can be
  certified here. Filling the run disk is conceivable in principle
  but unverified, its threshold unknown, and it risks breaking the
  collection load the route itself needs.
- Revival path (recorded, not attempted): verify the threshold from
  BackupManager source; only then revive the carried 11-edge BFS
  list as a script with a run_app.sh storage-fill fixture.
- Audit: device-draft/AUDIT.md ruling (c) RULED-ACCEPTED as
  drafted, with the limit stated (not a proof that a fill fixture
  is impossible).
