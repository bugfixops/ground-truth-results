#!/usr/bin/env python3
"""Diary route_14: Editor.alertDialog(int,String,int) — CONVERTED.

Method: Editor.alertDialog(int,String,int)
Edge ids (in route order):
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E05ca1e11
    Ea338626d Eded1f47a Ea3b59f09 Ebd97851f E652d1540 Ed1933649
    E4861418e Ea9aa4b4b
Printed route source: graphs/Diary/verification.csv path row for
    Editor.alertDialog(int,String,int) (result correct, SOURCE, ref
    Editor.java:411-425) plus
    graphs/Diary/out/diary_trigger_graph.json (path edges above).
    Diary has no scratch/route_print files, so none is cited.
Permissions (ROUTES.csv permissions cell, granted by run_app.sh
    before the script; the route method is not
    onRequestPermissionsResult, so the dialog-skip rule does not
    apply): android.permission.WRITE_EXTERNAL_STORAGE and
    android.permission.READ_EXTERNAL_STORAGE, both declared in the
    manifest (AndroidManifest.xml:26-27). Both grants are load
    bearing, not decorative: Editor.write() returns without writing
    when WRITE is not granted (Editor.java:396-409), and
    Editor.read() returns empty and raises the permission dialog
    when READ is not granted (Editor.java:364-377). With both
    granted, Accept reaches the FileWriter call.
Fixtures (ROUTES.csv fixtures cell, pushed by run_app.sh before
    the script; the script itself pushes nothing):
    device/routes/Diary/fixtures/css-blocker.txt
        -> /sdcard/Diary/css
    The pushed file is a regular text file standing exactly where
    Diary expects the css/ DIRECTORY of its resolved home folder
    (/sdcard/Diary/css, since the fresh-install folder preference
    "Diary" is relative, so Diary.getHome() falls back to
    Environment.getExternalStorageDirectory()/Diary,
    Diary.java:1981-1988, CSS_STYLES = "css/styles.css",
    Diary.java:199). The blocker sits DOWNSTREAM of getHome's
    fallback, so the fallback cannot rescue the write: getHome has
    already returned /sdcard/Diary before editStyles builds the
    css/styles.css path (Diary.java:1889-1895).
Setup: none (the Diary row of work-emulator/ci/apps.csv has an
    empty setup cell; no per-route setup script is used).
Route shape: Diary -> More options -> Edit styles opens the styles
    file in Editor (Diary.java:1889-1895) -> typing in Editor sets
    changed (Editor.java:146-168) -> tap Accept: write if changed
    (Editor.java:183-199) -> the write throws -> alertDialog
    (Editor.java:411-425).
Why the write throws (printed source, no privilege needed):
    Editor.write() (Editor.java:396-432) calls
    file.getParentFile().mkdirs() and ignores its return value
    (Editor.java:413), then constructs new FileWriter(file)
    (Editor.java:414). The parent /sdcard/Diary/css is a regular
    file, not a directory, so mkdirs() fails silently and the
    FileWriter constructor fails opening
    /sdcard/Diary/css/styles.css with ENOTDIR, throwing
    FileNotFoundException (an IOException). The catch block
    (Editor.java:420-425) calls alertDialog(R.string.appName,
    e.getMessage(), android.R.string.ok) — the (int,String,int)
    overload at Editor.java:346-360 — which is the target.
    No chmod, no remount, no disk fill, no run-as, no app-private
    manipulation is involved: the blocker is an ordinary text
    fixture pushed by the audited runner fixture phase to
    world-writable external storage, exactly as other routes push
    picker/text fixtures. No new harness primitive is used.
What the dry run does NOT prove: dry mode never executes the
    FileWriter, so it cannot prove the live throw. The throw
    follows from the printed source above plus standard Java
    file-open semantics (opening a path through a non-directory
    component fails). The CI live run settles it via JaCoCo: a
    miss is unclear, never wrong.
Live-run caveats (all unclear-on-miss, none claimed away):
    - Fresh emulator per CI run: if a previous run had already
      created a real /sdcard/Diary/css DIRECTORY, adb push of the
      blocker file onto that path would land inside it instead of
      replacing it, and the write would succeed. A fresh emulator
      (the workflow's normal case) has no such directory.
    - adb push creates the parent /sdcard/Diary directory when
      pushing to /sdcard/Diary/css; if a given adb build did not,
      the fixture phase fails loudly (fixture_push_failed) rather
      than silently passing.
    - The blocker persists in /sdcard after route_14 within the
      run. No other Diary route needs /sdcard/Diary/css as a
      directory: the only css uses are an exists() check
      (Diary.java:1674-1677, false through a file, as on a fresh
      install) and editStyles itself (route_14). Day files live
      under Diary/<year>/<month>/, unaffected.
Run (from the repo root):
    python3 -I device/routes/Diary/route_14.py --package
    org.billthefarmer.diary --log steps/route_14.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E05ca1e11", "Ea338626d", "Eded1f47a", "Ea3b59f09", "Ebd97851f",
    "E652d1540", "Ed1933649", "E4861418e", "Ea9aa4b4b",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Ee6b8aa80: Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter).
        r.launch(args.package + "/.Diary", edge="Ee6b8aa80")
        # Edd0b9192: The system instantiates Diary, then onCreate.
        r.comment("system instantiates Diary, then onCreate",
                  edge="Edd0b9192")
        # Ee63879c9: onStart -> onResume.
        r.comment("Diary onStart -> onResume", edge="Ee63879c9")
        # Ea885d6f1: Diary visible with the MarkdownView (markdown
        # on and shown, the default).
        r.comment("Diary visible with the MarkdownView (markdown on, "
                  "the default)", edge="Ea885d6f1")
        # E002e1746: Tap an action bar icon or an item under More
        # options (overflow). The overflow button exposes
        # "More options" in uiautomator dumps.
        r.tap(desc="More options", edge="E002e1746")
        # E05ca1e11: switch case R.id.editStyles. res/menu/main.xml
        # editStyles title @string/editStyles = "Edit styles...".
        r.tap(text="Edit styles\u2026", edge="E05ca1e11")
        # Ea338626d: startActivityForResult(ACTION_EDIT
        # file://<folder>/css/styles.css, Editor.class), EDIT_STYLES.
        r.comment("editStyles starts Editor on styles.css",
                  edge="Ea338626d")
        # Eded1f47a: The system instantiates Editor, then onCreate
        # (theme from pref_theme, Up arrow on).
        r.comment("system instantiates Editor, then onCreate",
                  edge="Eded1f47a")
        # Ea3b59f09: Editor shows the file with the Accept button
        # and the Up arrow (res/layout/editor.xml).
        r.comment("Editor shows styles.css with Accept button",
                  edge="Ea3b59f09")
        # Ebd97851f: Typing notifies the TextWatcher
        # (afterTextChanged). Tap the editor text field
        # (res/layout/editor.xml EditText id "text") and type.
        # Editor.read() on the blocked path throws inside
        # openInputStream and is caught silently (Editor.java:386-393),
        # so the editor starts empty; typing still sets changed.
        r.tap(res_id="text", edge="Ebd97851f")
        r.type_text("/* style edit */", edge="Ebd97851f")
        # E652d1540: changed = true (Back now asks Save / Discard).
        r.comment("TextWatcher sets changed = true",
                  edge="E652d1540")
        # Ed1933649: Tap the Accept (check) button: write if
        # changed, return RESULT_OK. The Editor accept button
        # (res/layout/editor.xml id "accept") has no text or
        # content description, so it is tapped by resource id.
        r.tap(res_id="accept", edge="Ed1933649")
        # E4861418e: changed: write(textView.getText(), file).
        # Internal call, no user action.
        r.comment("Accept handler calls write() for styles.css",
                  edge="E4861418e")
        # Ea9aa4b4b: FileWriter failed: alertDialog(appName,
        # e.getMessage(), OK). No user action; the throw is forced
        # by the runner-pushed blocker file at /sdcard/Diary/css
        # (see the docstring): mkdirs() on that parent fails
        # silently and new FileWriter(file) throws ENOTDIR, caught
        # at Editor.java:420-425. No dialog-text assert is added:
        # the dialog message is the OS error string, not a fixed
        # string, so asserting it would add a false-failure mode;
        # JaCoCo on the live run decides whether the target fired.
        r.comment("write throws ENOTDIR on blocker file; Editor calls "
                  "alertDialog", edge="Ea9aa4b4b")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
