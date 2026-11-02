# AnkiDroid route_15 — UNSCRIPTABLE

- Route: route_15, target api.Utils.entsToTxt, table verdict FIXED.
- BFS route (6 edges, byte-identical to the route print): S_ENTRY ->
  AddContentApi.findDuplicateNotes (E100d6608,
  AddContentApi.java:161-167) -> api.Utils chain -> target. Edge
  ids in device/routes/AnkiDroid/ROUTES.csv row route_15.
- Why unscriptable: the entry is an external-caller entry — another
  app calls ContentResolver on the exported CardContentProvider
  (manifest exported=true, permission
  com.ichi2.anki.permission.READ_WRITE_DATABASE). No AnkiDroid-UI
  path reaches the entry, no driver/host app exists on the AOSP
  emulator, and the branch harness has no ContentProvider query/call
  action (its actions are UI/adb actions plus start_intent and
  broadcast, neither of which performs a provider API call).
  Precedent verified from the branch: device/routes/Omni-Notes/
  ROUTES.csv route_13 is unscriptable for the same external-host-app
  reason (DashClock/Pushbullet host app not available on the
  emulator).
- Revival path (not attempted here): commission a driver app that
  calls the provider, or add a provider-call action to the harness;
  either is new work outside this draft, not a script fix.
- Audit: device-draft/AUDIT.md ruling (b) RULED-ACCEPTED on the
  Anki facts alone (precedent also verified).
