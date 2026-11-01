# Diary route_14: UNSCRIPTABLE-CANDIDATE

Method: `Editor.alertDialog(int,String,int)`
Route: route_14 in `device/routes/Diary/ROUTES.csv`
Edges (14, in route order):
`Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E05ca1e11
Ea338626d Eded1f47a Ea3b59f09 Ebd97851f E652d1540 Ed1933649
E4861418e Ea9aa4b4b`
Printed route: `overnight/stream-D/Diary/scratch/route_steps.txt`,
section "Editor.alertDialog"; edge details in
`graphs/Diary/out/diary_trigger_graph.json` (same edge ids).

No script is written for this route, deliberately: the first 13
edges are ordinary GUI (launch Diary, open More options, tap
"Edit styles…", type in Editor, tap Accept), but the 14th edge
cannot be driven by any action the D2 harness offers on an AOSP
emulator, and writing a script that stops at edge 13 would falsely
suggest the target is reachable.

## The gate

Edge `Ea9aa4b4b` (`Editor.write@STYLES` ->
`Editor.alertDialog(int,String,int)`) has trigger "FileWriter
failed: alertDialog(appName, e.getMessage(), OK)" and env "writing
the target file fails with an I/O error (e.g. storage full or
read-only location)".

Printed handler source (all in the Diary app slice,
`final_java_only/Diary/app/Diary-#v1.105/src/main/`):

- `Editor.java:183-199` — the Accept button click: if `changed`,
  it calls `write(textView.getText(), file)`, then returns
  `RESULT_OK` and finishes.
- `Editor.java:396-425` — `write(CharSequence, File)`:
  - `Editor.java:397-410`: if `WRITE_EXTERNAL_STORAGE` is not
    granted (SDK >= M), it requests the permission and returns
    without writing — so the failure path also needs the
    permission granted first.
  - `Editor.java:412`: `file.getParentFile().mkdirs()`.
  - `Editor.java:413-419`: `new FileWriter(file)`, append, close.
  - `Editor.java:421-425`: `catch (IOException e)` calls
    `alertDialog(R.string.appName, e.getMessage(),
    android.R.string.ok)` — the target method, defined at
    `Editor.java:346-359` (title int, message String, neutral
    button int).
- `Diary.java:1889-1895` — `editStyles()` fixes the target file:
  `new File(getHome(), "css/styles.css")`, opened with
  `ACTION_EDIT` into `Editor.class`. The script cannot redirect
  this file to a failing location; the route edges require going
  through Diary's menu.
- `Diary.java:1982-1988` — `getHome()`: if the configured folder
  is not an existing writable directory, it falls back to
  `Environment.getExternalStorageDirectory()` plus the folder
  name. A read-only folder preference therefore does NOT make
  the write fail; it is silently replaced by writable storage.

## Why no harness action can create the failure

The D2 harness (`device/harness/harness.py`, `Runner`) offers
only: launch, tap/long_tap by text/res_id/desc (fixed x/y only
with a why string), type_text, key, back, scroll_to, wait_for,
start_intent, broadcast, grant/deny, push_fixture, screenshot,
dump_ui, assert_text, comment. It has no raw shell action and no
way to:

1. Make the styles file's parent read-only, chmod the file, or
   remount storage read-only (needs `adb shell` commands the
   harness does not expose).
2. Fill device storage (needs a huge pushed file plus a
   destructive, run-wide side effect; no such fixture is listed
   in ROUTES.csv, and filling the emulator disk would break
   every other route in the same run).
3. Replace `css/styles.css` with a directory via `push_fixture`:
   this is the only speculative avenue, and it is NOT claimed
   here, because it needs out-of-contract plumbing that does not
   exist today: a fixture directory shipped with the repo (or
   under `$WEMU/fixtures`), a ROUTES.csv fixtures entry for
   route_14, and unverified `adb push` directory semantics
   (whether pushing a directory creates the destination as a
   directory, and whether Diary's startup then leaves it alone).
   If the device lead verifies that avenue on a real emulator,
   this route can be re-scripted; until then it must not be
   presented as scripted.

On a normal AOSP emulator the write succeeds: storage is
writable, `mkdirs()` succeeds, and `FileWriter` opens the file.
The script would end at edge `Ed1933649` (Accept -> write)
with the target never reached.

## Conflict note for the merger

D1's `device/routes/Diary/ROUTES_NOTES.md` judged this row
"scripted, not unscriptable" ("heavy but adb-creatable"). That
judgment is about raw adb, not about the pushed D2 harness API
that route scripts are actually allowed to use. Under the
harness, the failure condition is not drivable, so this helper
reports route_14 as unscriptable-candidate. ROUTES.csv currently
lists route_14 status `scripted`; the merger / device lead
should flip it to `unscriptable: <reason>` (reason: I/O error
on save not creatable by harness actions on an AOSP emulator)
unless the directory avenue above is first verified on a real
emulator. One unscriptable row out of 30 is within the D3
at-most-10%-per-app allowance.

## What a future script would still need

If the failure is ever made creatable, the remaining steps are
already determined by the printed route: launch Diary, tap More
options, tap "Edit styles…" (`res/menu/main.xml` id
`editStyles`, string `res/values/strings.xml:35`), type in
Editor (`res/layout/editor.xml`, id `text`), tap Accept
(`res/layout/editor.xml`, id `accept`), with storage permission
granted first (else `write()` returns early, `Editor.java:
397-410`), then dismiss the alert dialog's OK button.
