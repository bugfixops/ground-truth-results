#!/usr/bin/env python3
"""Diary route_05: FileUtils.isLocal.

Method: FileUtils.isLocal
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72
    E003e3f4e Eb04234de E614e3b2e E18bac421 E70b5909f E7ada6d09
    E86da5854 E4cc3319e E02835c77 E4115ec95 Eef610ba3 Ee174274c
    E8c83c21e E8858b368 Eadc47a1d E703c40c2 E6f8e7966
Printed route: the FileUtils.isLocal section of the Diary route print
    (overnight stream-D Diary scratch route_steps.txt), verdict
    REACHABLE but path_status UNCHECKED / unclear-INFERRED, ref
    FileUtils.java:633; path row of graphs/Diary/verification.csv.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv. Prerequisite recorded as a
    judgment call below: the picked image must already be on the
    device for the picker step to succeed (see the E8858b368 block).
Setup: none (Diary row of work-emulator ci/apps.csv has an empty
    setup cell).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (none here).

Mapping notes and judgment calls (printed source):
  - Settings is an overflow item (menu main.xml:105-107,
    showAsAction="never"; title "Settings", strings.xml:45), reached
    via the AOSP overflow content-desc "More options".
  - "Copy images" is the CheckBoxPreference at preferences.xml:144-148
    (key pref_copy_media, title pref_copy_media = "Copy images",
    strings.xml:62, defaultValue="false"). From a fresh `pm clear`
    install it starts unticked, so one tap ticks it and the listener
    fires (SettingsFragment.onSharedPreferenceChanged).
  - Add media is an overflow item (menu main.xml:89-91,
    showAsAction="never"; title "Add media...", strings.xml:34).
    Diary.addMedia() (Diary.java:1880-1885) launches
    createChooser(GET_CONTENT */* OPENABLE) with ADD_MEDIA, so the
    next screen is another app's picker.
  - Picker step (E8858b368): the route print says "Pick an image
    (e.g. Pictures/...)" and notes the picker (another app) returns a
    content:// URI with a read grant; its source was not read. The
    script taps the file name in the picker UI. JUDGMENT CALL: the
    tapped name is "photo_1.jpg", the D1 candidate on-device file
    (work-emulator fixtures Pictures/photo_1.jpg). This step is the
    least deterministic in the script: it assumes the picker shows
    the device file list with that name as text, and that the file
    has been placed on the device before the run (ROUTES.csv now lists
    Pictures/photo_1.jpg for route_05, and the file exists in
    work-emulator fixtures/Pictures/; run_app.sh pushes listed fixtures
    before the run, so the picker step has its file). If the
    chooser first shows an app list, a tap on the picker app is
    needed before the file tap; that intermediate tap is not in the
    printed route and is not scripted here.
  - After the pick, Diary.onActivityResult ADD_MEDIA resolves an
    image type to addMedia(uri, false) (Diary.java:791-794); with
    Copy images on, addMedia(uri, boolean) calls
    FileUtils.getFile(this, media) (Diary.java:2767-2769), and
    FileUtils.getFile calls isLocal(path) (FileUtils.java:633) when
    the path is not http(s). Those three call edges follow
    automatically from the pick, so they are logged with r.comment.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
    "E70b5909f", "E7ada6d09", "E86da5854", "E4cc3319e", "E02835c77",
    "E4115ec95", "Eef610ba3", "Ee174274c", "E8c83c21e", "E8858b368",
    "Eadc47a1d", "E703c40c2", "E6f8e7966",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_05", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ee6b8aa80 S_ENTRY -> Diary.<init>: Tap the Diary icon in the
    # launcher (MAIN/LAUNCHER intent filter).
    r.launch(args.package + "/.Diary", "Ee6b8aa80")
    # Edd0b9192 Diary.<init> -> Diary.onCreate: system instantiates
    # Diary, then onCreate. No user action.
    r.comment("system instantiates Diary, then onCreate", "Edd0b9192")
    # Ee63879c9 Diary.onCreate -> Diary.onResume: onStart -> onResume.
    # No user action.
    r.comment("onStart -> onResume", "Ee63879c9")
    # Ea885d6f1 Diary.onResume -> S_DIARY_VIEW: Diary visible with the
    # MarkdownView. No user action.
    r.comment("Diary visible with the MarkdownView", "Ea885d6f1")
    # E002e1746 S_DIARY_VIEW -> Diary.onOptionsItemSelected@VIEW: open
    # the action bar menu (More options overflow).
    r.tap("E002e1746", desc="More options")
    # E65bffa72 Diary.onOptionsItemSelected@VIEW -> Diary.settings:
    # switch case R.id.settings (Diary.java:714-715).
    r.tap("E65bffa72", text="Settings")
    # E003e3f4e Diary.settings -> Settings.<init>: startActivity(new
    # Intent(this, Settings.class)) (Diary.java:1976-1979). Automatic
    # after the tap; no further action.
    r.comment("startActivity Settings intent", "E003e3f4e")
    # Eb04234de Settings.<init> -> Settings.onCreate: system
    # instantiates Settings, then onCreate. No user action.
    r.comment("system instantiates Settings, then onCreate", "Eb04234de")
    # E614e3b2e Settings.onCreate -> SettingsFragment.<init>:
    # replace(android.R.id.content, new SettingsFragment()).commit()
    # (Settings.java:91-94). No user action.
    r.comment("fragment transaction commits SettingsFragment", "E614e3b2e")
    # E18bac421 SettingsFragment.<init> -> SettingsFragment.onCreate:
    # the committed transaction runs fragment onCreate. No user action.
    r.comment("fragment onCreate runs", "E18bac421")
    # E70b5909f SettingsFragment.onCreate -> SettingsFragment.onResume:
    # the fragment resumes with the activity. No user action.
    r.comment("fragment resumes with the activity", "E70b5909f")
    # E7ada6d09 SettingsFragment.onResume -> S_SETTINGS: Settings list
    # shown. Wait for the Copy images row to confirm the screen.
    r.wait_for("E7ada6d09", text="Copy images")
    # E86da5854 S_SETTINGS -> SettingsFragment
    # .onSharedPreferenceChanged@COPY_MEDIA: tap the Copy images
    # checkbox row; the value flips and the listener fires.
    r.tap("E86da5854", text="Copy images")
    # E4cc3319e SettingsFragment.onSharedPreferenceChanged@COPY_MEDIA
    # -> S_SETTINGS@COPY_MEDIA: Settings stays shown with the new
    # value. No user action.
    r.comment("Settings stays shown with the new value", "E4cc3319e")
    # E02835c77 S_SETTINGS@COPY_MEDIA -> Diary.onResume@COPY_MEDIA:
    # Back finishes Settings; Diary resumes.
    r.back("E02835c77")
    # E4115ec95 Diary.onResume@COPY_MEDIA -> S_DIARY_VIEW@COPY: back
    # in Diary with the changed preference. No user action.
    r.comment("back in Diary with the changed preference", "E4115ec95")
    # Eef610ba3 S_DIARY_VIEW@COPY -> Diary.onOptionsItemSelected@COPY:
    # open the action bar menu (More options overflow).
    r.tap("Eef610ba3", desc="More options")
    # Ee174274c Diary.onOptionsItemSelected@COPY -> Diary.addMedia()
    # @COPY: switch case R.id.addMedia (Diary.java:702-703).
    r.tap("Ee174274c", text="Add media\u2026")
    # E8c83c21e Diary.addMedia()@COPY -> S_MEDIA_PICKER@COPY:
    # startActivityForResult(createChooser(GET_CONTENT */* OPENABLE),
    # ADD_MEDIA) (Diary.java:1880-1885). The chooser/picker is another
    # app; no Diary action follows the tap.
    r.comment("chooser GET_CONTENT picker launched by Diary",
              "E8c83c21e")
    # E8858b368 S_MEDIA_PICKER@COPY -> Diary.onActivityResult
    # @ADD_MEDIA_COPY: an image file is picked, RESULT_OK with its URI.
    # Other-app picker UI: tap the file name. See the docstring
    # judgment call: assumes photo_1.jpg is on the device and shown
    # as text by the picker.
    r.tap("E8858b368", text="photo_1.jpg")
    # Eadc47a1d Diary.onActivityResult@ADD_MEDIA_COPY -> Diary
    # .addMedia(Uri,boolean)@COPY: image (Copy images on):
    # addMedia(uri, false) (Diary.java:791-794). Automatic after the
    # pick; no user action.
    r.comment("image pick resolves to addMedia(uri, false)", "Eadc47a1d")
    # E703c40c2 Diary.addMedia(Uri,boolean)@COPY -> FileUtils.getFile:
    # oldMedia = FileUtils.getFile(this, media) (Diary.java:2767-2769).
    # Automatic; no user action.
    r.comment("addMedia calls FileUtils.getFile", "E703c40c2")
    # E6f8e7966 FileUtils.getFile -> FileUtils.isLocal: isLocal(path):
    # not http(s) (FileUtils.java:633). Automatic; no user action.
    # This is the target edge.
    r.comment("getFile calls isLocal(path)", "E6f8e7966")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
