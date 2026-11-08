# Currency — ROUTES notes

Scope: one row per `path` row in
`graphs/Currency/verification.csv`, in that file's order (28 rows).
`env_kinds` / `state_kinds` are copied semicolon-joined from
`graphs/Currency/out/methods.csv` for each method. No row was invented:
every method, edge list, and source citation below comes from those two
files, checked against `graphs/Currency/out/currency_trigger_graph.json`
for the gate prose.

## Permissions: empty on all 28 rows (nothing omitted)

Manifest
`final_java_only/Currency/app/Currency-#v1.58/src/main/AndroidManifest.xml`
declares exactly two permissions, at lines 8–9:

- `android.permission.INTERNET`
- `android.permission.ACCESS_NETWORK_STATE`

Both are normal install-time permissions, so neither is listed under this
task's dangerous-runtime-only rule. No route edge in the trigger graph
names a permission gate for any of the 28 routes (a full-graph grep for
permission names returns nothing on any edge), and a grep of the app
source finds no runtime permission check (`checkSelfPermission` /
`requestPermissions` absent; the only hits are LICENSE prose and a
comment in `SMSInstrumentedReceiver.java` saying the coverage file goes
to internal storage, which needs no permission). There was therefore no
permission gate whose handler source needed reading, and no permission
value to record on any row.

## Fixtures: empty on all 28 rows (nothing omitted)

No route has a STATE file gate. The only `state_kinds` value in this app
is `data` (routes 03, 06, 08): "no exchange rates saved yet — first
launch after install or after clearing the data" (methods.csv `state`
column; trigger-graph edge E1f5a81d0 / E576d70ee guard: `Data.map ==
null and pref_map not saved yet`). That state is created by a fresh
install or `pm clear`, not by pushing a file, so no fixture is listed.
Real fixture files were listed (Documents, Download, Music, Pictures,
contacts.json under `work-emulator/fixtures/`) and none of them applies
to any Currency gate; none is named in ROUTES.csv.

## Setup: identical on every row

`network (ECB); cert issue on API<=27 images` — the Currency row's
`setup` cell in `work-emulator/ci/apps.csv`, copied verbatim onto all
28 rows as instructed. It is a setup condition, not a per-route verdict.

## Status summary

28 rows, 28 scripted, 0 unscriptable (0%, below the 10% flag
threshold). No route meets the unscriptable test: no time condition, no
network/hardware condition adb cannot create on an AOSP emulator, and
no missing fixture blocks any route. The caveats below affect how
scripts must be written, not whether the routes can be scripted.

## Per-route judgments

- route_01 AboutPreference.\<init\> — no env/state gates. Plain
  Settings navigation (nav menu -> Settings -> About row). Scripted.
- route_02 AboutPreference.onBindDialogView — no env/state gates.
  Same navigation plus tapping the About row to bind the dialog.
  Scripted.
- route_03 Parser.startParser(Context,int) — STATE `data` only.
  Must run on a fresh install or after clearing app data, before any
  route that saves rates; the guard is edge E1f5a81d0
  (`Data.map == null and pref_map not saved yet`). No network gate:
  it parses the bundled raw resource. Scripted.
- route_04 ChartActivity.onInvertClick — ENV `network;tls_chain`.
  Requires the ECB history download to succeed (edges E850a7523,
  Eb5402ee6) so `histMap != null` and Invert is enabled. See the
  TLS/API image constraint below. Scripted.
- route_05 ChoiceDialog.onRestoreInstanceState — ENV `hardware`
  (rotation, edge Eb43116bb: picker recreated, not Home). Rotation is
  adb-creatable (rotation setting), so scripted, not unscriptable.
  The script must rotate while the picker is open and restore with
  the saved selection.
- route_06 Parser$Handler.startElement — STATE `data` only, same
  fresh-install condition as route_03 (edge E1f5a81d0, then
  E19c2a4c6 into SAX startElement). Scripted.
- route_07 ChartActivity.showToast(String) — ENV `network`, but note
  the polarity: this is the FAILURE branch. Edge E4c809227 fires
  when the network check fails ("network off, or not allowed by the
  Wi-Fi only / Roaming settings"), producing the No connection /
  No Wi-Fi / Roaming toast. The script must turn networking off (or
  set those preferences), not on. Scripted.
- route_08 Parser.getMap — STATE `data` only, same fresh-install
  condition as route_03 (edge E576d70ee). Scripted.
- route_09 HelpActivity.onOptionsItemSelected — no env/state gates.
  Scripted.
- route_10 Singleton.setMap — no env/state gates in methods.csv
  (the chart route reaches it via ChartActivity.onPause). Scripted.
- route_11 Singleton.\<init\> — no env/state gates. Scripted.
- route_12 ChartActivity.updateRange — no env/state gates in
  methods.csv. Scripted.
- route_13 ChartParser$Handler.\<init\> — ENV `network;tls_chain`.
  Same ECB-success requirement as route_04 (edge Ef3349d6d: new
  Handler after the HTTPS stream opened). See the TLS/API image
  constraint below. Scripted.
- route_14 Main.lambda$onUpdateClick$1 — no env/state gates.
  Scripted.
- route_15 Main$Currency.\<init\> — no env/state gates. The shortest
  route in the file: class initialisation only (E4c32b395,
  Ea2843361, building the 34-entry CURRENCIES table). Scripted.
- route_16 Data.\<init\> — no env/state gates (first `getInstance`
  call in the process). Scripted.
- route_17 Main.onItemClick — no env/state gates. Scripted.
- route_18 Main.onRefreshClick — no env/state gates. Scripted.
- route_19 Main.onCopyClick — no env/state gates. Scripted.
- route_20 Main.onActivityResult — no env/state gates. This is the
  cancelled-result path through the picker (edge Eb4cf7f67,
  RESULT_CANCELED); the method still runs to its early return.
  Scripted.
- route_21 ChartActivity$DateAxisValueFormatter.getFormattedValue —
  ENV `network;tls_chain`. Requires RESULT_OK plus loaded history
  (edge Eddbb6185) and a chart redraw for the newly picked pair.
  See the TLS/API image constraint below. Scripted.
- route_22 CurrencyWidgetProvider.\<init\> — no env/state gates in
  methods.csv. The route does NOT need a placed widget: it runs via
  Main.onPause -> updateWidgets -> broadcast (edges E3b5308ec,
  E2ea0fd55, E3b81bf90), which the system delivers to the manifest
  receiver. Scripted.
- route_23 CurrencyWidgetProvider.onReceive — no env/state gates.
  Same broadcast chain as route_22, ending at onReceive.
  Scripted.
- route_24 CurrencyWidgetProvider.onUpdate — ENV `other_app`. This
  one DOES need a widget placed on the home screen through the
  launcher (edge E2d9123e2: APPWIDGET_UPDATE with a non-empty id
  list). Launcher placement is UI automation, not a time/network/
  hardware blocker, so it is marked scripted per the task rule
  (difficulty alone is not unscriptable) — but the script must drive
  the launcher's widget picker, which is launcher-dependent. See
  the launcher caveat below. Scripted.
- route_25 CurrencyWidgetProvider.onDeleted — ENV `other_app`.
  Requires placing the widget, then the launcher deleting the id
  after a cancelled configure activity (edges E1cfacc94,
  Ee3672287, Eaa043033). Ambiguity flagged: the verification row is
  `unclear, INFERRED` — the launcher-delete step is launcher
  behaviour whose source was not read. The route is still marked
  scripted (a launcher UI script can place the widget and cancel
  configure; `other_app` is not one of the unscriptable causes),
  but replay success depends on the actual launcher's behaviour,
  which the device lead should confirm on the emulator image in
  use. Scripted, with that caveat.
- route_26 CurrencyWidgetUpdate.onDateResult — ENV
  `network;other_app`. Widget placement (as route_24) plus the
  download-FAILURE branch: edge E3ec638f8 posts
  `onDateResult(null)` when `startParser` returned false. The
  script should force the failure (network off) rather than wait
  for ECB. Verification row is `unclear, INFERRED` for the same
  launcher reason as route_25, plus a shared static Data listener
  (Main vs widget service). Scripted, with that caveat.
- route_27 CurrencyWidgetUpdate.onDestroy — ENV
  `network;other_app;tls_chain`. Widget placement plus the
  download-SUCCESS branch (edge E8c73e084: parsed download posted
  back, then onDataResult -> stopSelf -> onDestroy). Requires ECB
  success, so the TLS/API image constraint below applies, and the
  same launcher caveat as routes 25–26 applies (verification row
  `unclear, INFERRED`). Scripted, with those caveats.
- route_28 Main.onEditorAction — no env/state gates in methods.csv.
  The verification note records an IME ambiguity (soft keyboard
  must appear; a hardware Enter key reaches the method too). The
  script can use either: focus the value field and send keyevent
  66, or drive the soft keyboard's Done action. Scripted.

## Ambiguities the device lead must resolve at script time

1. TLS / emulator image choice (routes 04, 13, 21, 27): the ECB
   HTTPS download must succeed over a trusted certificate chain,
   and the dataset notes a certificate issue on API<=27 images.
   These routes are marked scripted on the basis that the device
   lead selects an image where the chain validates (API>27, or an
   image with the chain fixed). If the replay image is API<=27 and
   the ECB chain does not validate there, those four routes will
   fail at the download step through no fault of the script — that
   would be an image problem to report, not a reason to have marked
   them unscriptable here, since a suitable image is available.
2. Launcher behaviour (routes 24–27): widget placement, and for
   route_25 deletion after cancelled configure, depend on the
   emulator's launcher. The graph marks the launcher steps
   INFERRED (launcher source not read). Scripts must be written
   against the actual launcher on the replay image and confirmed
   there.
3. First-launch ordering (routes 03, 06, 08): these need
   no-saved-rates state. If the device lead's idempotent setup
   clears app data before every route, ordering is irrelevant;
   if setup runs once per app install, these three must run before
   any route that persists rates.
4. Network polarity (route_07 vs routes 04/13/21/27): route_07
   needs networking OFF (or Wi-Fi-only/roaming prefs blocking it),
   while the TLS routes need networking ON with ECB reachable.
   Scripts must set the network state per route, not once per app.

## Blocked items

None. All inputs were present and readable: verification.csv (28
path rows), methods.csv (all 28 methods found), trigger graph
(all 106 distinct route edge ids found), AndroidManifest.xml, the
Currency row of apps.csv, and the fixtures directory listing.
No input file was missing and no content was invented.
