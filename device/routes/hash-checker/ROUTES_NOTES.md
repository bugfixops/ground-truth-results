# hash-checker — ROUTES.csv judgment notes

Source inputs (all read-only, local only; nothing pushed, no connector used):

- `graphs/hash-checker/verification.csv` — 37 `path` rows, in file order, became
  route_01 … route_37. Edges, method (`item`) and source (`ref`) copied verbatim.
- `graphs/hash-checker/out/methods.csv` — `env_kinds` / `state_kinds` copied
  verbatim per method (single value or empty in every case here).
- `graphs/hash-checker/out/hash-checker_trigger_graph.json` — edge trigger /
  guard / env prose checked for every route edge (220 distinct edge ids, all
  present in the graph). No route edge trigger, guard, env or needs_state text
  names a permission.
- `final_java_only/hash-checker/app/hash-checker-#v3.7.3/app/src/main/AndroidManifest.xml`
  and the `src/debug` manifest (see "Permissions" below).
- `work-emulator/ci/apps.csv`, hash-checker row — setup cell is
  `any file as input (fixtures)`; placed on every row as instructed.
- `work-emulator/fixtures/` — every fixture named below was confirmed to exist
  on disk; no name was invented.

## Permissions: empty on all 37 rows — why

This is a deliberate empty, not an omission:

1. A grep of the whole main source tree for `Permission`,
   `checkSelfPermission`, `requestPermissions`, `READ_EXTERNAL_STORAGE` and
   `WRITE_EXTERNAL_STORAGE` returned zero hits: the app code never checks or
   requests a runtime permission.
2. No route edge in the trigger graph names a permission gate, so there was no
   gate text to resolve to a permission via handler source.
3. All file access on these routes goes through the Storage Access Framework —
   `ACTION_OPEN_DOCUMENT` (file pick), `ACTION_OPEN_DOCUMENT_TREE` (folder
   pick) and `ACTION_CREATE_DOCUMENT` (export/create output) — which grant URI
   access via the picker intent, not via a runtime permission.
4. The main manifest declares only `android.permission.VIBRATE` (normal,
   install-time, so excluded by the column rule even if it were relevant).
5. Manifest ambiguity, recorded not resolved silently: the `src/debug`
   manifest additionally declares `READ_EXTERNAL_STORAGE` and
   `WRITE_EXTERNAL_STORAGE` (both dangerous) plus `INTERNET`, `WAKE_LOCK` and
   `DISABLE_KEYGUARD`. Since app code never checks them, neither is listed for
   any route. If the replay APK is a debug build, the device lead may need to
   pre-grant storage permissions for the picker to see pushed fixtures, but
   that is a harness precondition, not a route permission gate, and it is
   flagged here rather than baked into the permissions column.

## Fixtures: what "STATE file gate" means for this app

hash-checker has no `state_kinds` value meaning "file": its state kinds are
only `data` (history rows), `settings` (hash-type preference) and `session`
(in-app generated text / non-empty field). None of those needs a fixture file;
each is produced inside the app during the script (generate a hash first, pick
a hash type in the sheet, type text). So, strictly, no route has a STATE file
gate.

The fixtures listed below are instead the *input* the route consumes through
its ENV `other_app` gate (system picker / VIEW intent). Without a pushed file
those scripts would have nothing to pick or send, and the apps.csv setup text
("any file as input (fixtures)") confirms any fixture file serves. This
reading is stated explicitly so the device lead / auditor can strip the column
if they want the strict STATE-only reading — no other route needs a file.

Per-route fixture notes (every non-empty fixtures value):

- route_06 `FNV1a.update256(byte[],int,int)` — fixtures `Download/todo.txt`.
  Gate: `S_EXT_PICK_FILE -> onActivityResult@PICK_FILE`, env prose "the
  system file picker (com.android.documentsui) must return a document".
  Script picks this file, then chooses the FNV-1a 256-bit type in the
  hash-type sheet (state `settings`). Any fixture file would do; todo.txt is
  small plain text.
- route_08 `JdkHashCalculator.inputStreamsFormFolder` — fixtures `Pictures`.
  Gate: `S_EXT_PICK_FOLDER -> onActivityResult@PICK_FOLDER` (folder pick).
  NOTE: this fixture is a *directory*, not a file — the script picks the
  Pictures folder itself (it contains photo_1.jpg … photo_6.jpg, all real),
  and the app hashes the files inside it.
- route_12 `MainActivity.getConfiguredBundleWithDataUri` — fixtures
  `Download/todo.txt`. Gate: another app sends a VIEW intent with a
  content:// URI (edge E3706e5f1). Script pushes todo.txt and sends the VIEW
  intent against its content URI (or a SEND with ClipData); no in-app picker
  step is involved.
- route_14 `Blake2B.update(byte[],int,int)` — fixtures `Download/todo.txt`.
  Same file-picker gate as route_06; script additionally chooses BLAKE2b in
  the hash-type sheet first (state `settings`).
- route_16 `HashCalculatorTask.<init>(Context,HashType,Uri,Uri,HashCalculatorTaskTarget)`
  — fixtures `Download/todo.txt`. Same file-picker gate as route_06; the task
  constructor is reached from the picked file (fileUri != null guard).
- route_17 `HashCalculatorFragment.folderNameFromUri` — fixtures `Pictures`.
  Same folder-pick gate as route_08 (directory pick, not a file pick); the
  method derives the folder name from the picked folder URI.
- route_34 `HashCalculatorFragment.selectFileFromSystemFileManager` —
  fixtures `Download/todo.txt`. The route ends at the picker invocation /
  result handling; the file picked is todo.txt. (The method itself only
  validates the returned URI, so any fixture file serves.)

Deliberately empty fixtures, to avoid implying an input file is needed:

- route_10 `OrmLiteLocalDataStorage.getDatabaseFileName` and route_15
  `SettingsFragment.copyFile` — their picker edge is `ACTION_CREATE_DOCUMENT`
  (application/zip): an *output* destination the user confirms, not an input
  file. Their state gate (`data`: at least one history row) is produced
  in-app by generating a hash first.
- route_11 `HashCalculatorFragment.writeHashToFile` — same, output-only:
  `ACTION_CREATE_DOCUMENT` for the exported .txt; the content is the
  session-generated hash, not a fixture.
- route_01 / route_09 (`data` state) — history rows are produced in-app by
  generating a hash with "Save result to History" on (default on); no file.
- route_05 / route_06 / route_14 (`settings` state) — hash-type choice made
  in the in-app sheet; no file.
- route_11 / route_13 (`session` state) — a generated hash / non-empty field
  produced in-app; no file.

## Unscriptable rows: 1 of 37 (route_31, 2.7%, under the 10% threshold)

One route is marked unscriptable (route_31, below). No route needs
network, camera, GPS, NFC, telephony or any other hardware condition,
and no needed fixture is missing.
The closest calls, all judged scripted with the stated script approach
except route_31 (reclassified, see below):

- route_13 `Clipboard.clear` — env `time`: `handler.postDelayed(runnable,
  60 s)`. Time passing is adb-creatable: the script waits 60+ seconds after
  the copy tap. Not unscriptable merely because it is slow.
- route_31 `LogUtils.e` — env `other`: RECLASSIFIED UNSCRIPTABLE
  2026-11-01 (coordinator decision HC-D3-31, Muse's own, for user/Yang
  review; see ROUTE_UNSCRIPTABLE_31.md). The terminal edge is the
  catch block in `openSystemFileManager` (HashCalculatorFragment.java
  :191-200; catch :197-199 calls LogUtils.e at :198): LogUtils.e fires
  ONLY when no app handles ACTION_OPEN_DOCUMENT. On the replay image
  DocumentsUI handles that intent, so the catch never fires on a normal
  run. PRIOR approach (superseded, script removed from the bundle):
  remove the file-picker handler so `startActivityForResult
  (ACTION_OPEN_DOCUMENT)` throws ActivityNotFoundException — e.g. `pm
  disable-user com.android.documentsui` before the step, re-enabled
  after, via the non-public `runner._shell` call, explicitly marked
  PROVISIONAL pending device-lead confirmation. The D3 auditor's PASS
  for route_31 was explicitly conditional on that confirmation. The
  device lead, as harness owner, has now responded: the harness has
  no component-disable action, adding one is invasive and risks
  breaking the other picker routes if not re-enabled per route, and
  it recommends reclassification instead. The condition on the PASS
  has therefore failed. Manufacturing the precondition via a private
  shell call is not a supported replay step and not a UI route the
  app offers. The method's label is UNTOUCHED; under D7 a not-reached
  route maps to unclear, never wrong.
- route_18 `FeedbackFragment.sendEmail` — the method itself runs whether or
  not an email app exists: it calls `startActivity(createChooser(...))` inside
  a try block and falls back on ActivityNotFoundException. So no email app is
  required for coverage of `sendEmail` itself; the script taps send with a
  non-empty feedback message and accepts either the chooser or the fallback.
- route_12 — VIEW intent is sent by the script itself (adb), not by another
  app's UI; that is the documented `other_app` mechanism for this route.
- route_24 `SharedPreferencesSettings.saveStringPreference` and route_25
  `App.getShortcut` — both carry first-launch guards (language not yet
  initialised; shortcuts not yet created). Scriptable only on a fresh install
  / cleared app data; the device lead's per-route scripts must run these
  before any other route dirties that state, or clear data first. This is a
  script-ordering note, not an unscriptable reason.
- route_20 `AppSnackbar.lambda$show$0` — reached by tapping Generate with no
  source selected (guard `fileUri == null && folderUri == null &&
  !isTextSelected`); trivially scriptable on a fresh calculator screen.

## Other ambiguities not resolved silently

- env_kinds / state_kinds are copied exactly as printed in methods.csv,
  including route_31's env `other` (not `other_app`) and route_13's env
  `time`. No normalisation was applied.
- Verification `ref` values containing commas (e.g. route_05
  `Blake2B.java:91-107,152,171`, route_11, route_27) are preserved via proper
  CSV quoting; the file parses to exactly 37 data rows.
- Scratch "extra leads" files under
  `scratch/overnight-20261101/scratch-outputs/` (routes_30_steps etc.) were
  consulted only as leads and were not needed: every judgment above rests on
  verification.csv, methods.csv, the trigger graph, the manifests and the
  printed handler sources cited.
- No emulator was started and no adb command was run, per the task.

## Verification printed at build time

- Rows: 37 (equals verification.csv path-row count).
- Methods: 37/37 match a methods.csv row.
- Permissions: 0 listed; vacuous manifest check (nothing to check) plus the
  manual manifest/code grep above.
- Fixtures: 7 rows non-empty (route_06, route_08, route_12, route_14,
  route_16, route_17, route_34); 7/7 exist under
  `work-emulator/fixtures/` (Pictures verified as a directory).
- Status: 36 scripted, 1 unscriptable (route_31, 2.7%).
- Edges, method and source re-checked field-by-field against
  verification.csv: identical, in order. Route ids route_01 … route_37
  sequential.
