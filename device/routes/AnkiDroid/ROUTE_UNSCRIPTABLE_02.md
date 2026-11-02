# AnkiDroid route_02 — UNSCRIPTABLE

- Route: route_02, target EasyX509TrustManager.<init>, table verdict WRONG.
- Corrected route (C02, SYNC task): launcher -> DeckPicker ->
  Synchronization -> sync(String) -> Connection.sync
  (DeckPicker.java:1284) -> Connection.doInBackgroundSync
  (Connection.java:188, SYNC task, not LOGIN) -> Syncer.sync ->
  RemoteServer.meta -> HttpSyncer.req overloads ->
  EasySSLSocketFactory.createSocket -> target. Edge ids in
  device/routes/AnkiDroid/ROUTES.csv row route_02 (21 tokens; the
  table's 19 steps spell the three req overloads as one step).
- Why unscriptable: reaching the target requires a real HTTPS sync
  against AnkiWeb with a stored hkey (non-empty). With an empty hkey
  the flow diverts to the not-logged-in dialog before any
  Connection.sync (guard on the route-21 variant edges,
  DeckPicker.java:1281-1282), so no test-account or offline path to
  the target exists in the chain. No test account exists, and a real
  sync must not be attempted on the CI emulator. This is the user's
  real-online-account/credential exception: only such routes stay
  unscriptable.
- Partial drive recorded in the ROUTES.csv setup column: launch, tap
  Synchronization, stops at the not-logged-in dialog when hkey is
  empty. No script file is claimed for this route.
- Audit: device-draft/AUDIT.md ruling (a) RULED-ACCEPTED.
