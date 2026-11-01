"""Diary route_06: Diary.lambda$addLink$21.

Method: Diary.lambda$addLink$21
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E78556c11
    E86b7a9c5 Efd4a5146 E880677b8 Edad80a88 E584dfb93 E1af5e817
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.lambda$addLink$21", ref Diary.java:2819-2844).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none from ROUTES.csv (setup column empty). The route's ENV
    other_app step (edge Efd4a5146) needs a non-image/audio/video file
    present in the device picker; this script picks "sample.pdf" from
    the picker, a candidate file named in device/routes/Diary/
    ROUTES_NOTES.md (Download/sample.pdf exists in work-emulator
    fixtures). The picker is another app, so its exact UI may vary;
    see the mapping note on edge Efd4a5146.
Standard configuration: run_app.sh clears the package before this
    script; no permissions are granted and no fixtures pushed.

Mapping notes:
- Launcher tap (Ee6b8aa80) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:52-59).
- Overflow items are tapped by their menu titles (res/menu/main.xml
  and res/values/strings.xml:34 "Add media...").
- The Add link dialog's EditText is res/layout/save_path.xml
  (@+id/pathText); its positive button text is R.string.addLink
  ("Add link", Diary.java:2855, res/values/strings.xml:27).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

PACKAGE_FALLBACK = "org.billthefarmer.diary"
COMPONENT = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E78556c11", "E86b7a9c5", "Efd4a5146", "E880677b8", "Edad80a88",
    "E584dfb93", "E1af5e817",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_06", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Driven as am start.
        r.launch(COMPONENT, "Ee6b8aa80")

        # Edd0b9192 -- The system instantiates Diary, then onCreate.
        # Lifecycle edge: no user action.
        r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

        # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
        r.comment("onStart -> onResume", "Ee63879c9")

        # Ea885d6f1 -- Diary visible with the MarkdownView.
        # Page arrival: wait for the MarkdownView (res/layout/main.xml
        # @+id/markdown).
        r.wait_for("Ea885d6f1", res_id="markdown")

        # E002e1746 -- Tap an action bar icon or an item under More
        # options. Add media lives in the overflow menu
        # (showAsAction="never", res/menu/main.xml), so open it.
        r.tap("E002e1746", desc="More options")

        # E78556c11 -- switch case R.id.addMedia (Diary.java:702-703).
        r.tap("E78556c11", text="Add media\u2026")

        # E86b7a9c5 -- startActivityForResult(createChooser(
        # GET_CONTENT */* OPENABLE), ADD_MEDIA) (Diary.java:1880-1885).
        # The chooser is opened by the previous tap; no extra action.
        r.comment("chooser opened by addMedia()", "E86b7a9c5")

        # Efd4a5146 -- Another kind of file is picked: RESULT_OK with
        # its URI (Diary.java:763-798). The picker is another app
        # (ENV other_app); its UI is not Diary's, so this step taps
        # the DocumentsUI app ("Files") and then a generic file,
        # "sample.pdf", whose type is not image/audio/video, so
        # onActivityResult falls through to addLink (Diary.java:788-
        # 797). If the emulator's picker lists files differently,
        # this is the step to adjust; the file must exist on device.
        r.tap("Efd4a5146", text="Files")
        r.scroll_to("Efd4a5146", text="sample.pdf")
        r.tap("Efd4a5146", text="sample.pdf")

        # E880677b8 -- Other or unknown type: addLink(uri, title,
        # false) opens the Add link dialog (Diary.java:788-797).
        # Called from onActivityResult; no user action.
        r.comment("addLink(uri, title, false) from onActivityResult",
                  "E880677b8")

        # Edad80a88 -- addLinkDialog(url, title or last segment,
        # listener) (Diary.java:2811-2817). Internal call; no action.
        r.comment("addLinkDialog(url, title, listener)", "Edad80a88")

        # E584dfb93 -- builder.show(): URL as message, title in the
        # EditText (Diary.java:2849-2870). Wait for the dialog's
        # EditText (res/layout/save_path.xml @+id/pathText).
        r.wait_for("E584dfb93", res_id="pathText")

        # E1af5e817 -- Keep or edit the title, tap Add link (or
        # Cancel) (Diary.java:2819-2844). Keep the prefilled title.
        r.tap("E1af5e817", text="Add link")
    finally:
        r.done()


if __name__ == "__main__":
    main()
