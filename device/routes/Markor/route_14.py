#!/usr/bin/env python3
"""Markor route_14: AppSettings.getAttachmentFolder.

Method: AppSettings.getAttachmentFolder
Edge ids (in route order):
    E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
    E0ecb8e4d E54b4aedd E80c409ce E5bdf9e1e Ef154d966 E0ef1d7c9
    E617037b7 Ec0b77f96 Ee7e8240b Eb1705f8e
Printed route file: graphs/Markor/scratch/route_print/route_14.txt
ROUTES.csv permissions: none.
ROUTES.csv fixtures: Documents/todo.txt (pushed by run_app.sh; the
    todo tab opens the todo document, so the long-press below acts
    on that fixture file -- no fixture push in this script).
Setup (verbatim): push fixtures/Documents; first-run tutorial can trap
    a tool.
No pm clear here (run_app.sh does it) and no fixture push here
    (run_app.sh does it per ROUTES.csv).
Camera-result caveat: the camera-return edge (Ec0b77f96) is driven by
    the emulator camera app, whose shutter/accept UI is not pinned by
    any Markor source, so no shutter tap is invented here. See
    REPORT.md.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "harness"))
from harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_14",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914",
                         "Ed25af8f4", "Eba46a594", "E659e191c",
                         "E0ecb8e4d", "E54b4aedd", "E80c409ce",
                         "E5bdf9e1e", "Ef154d966", "E0ef1d7c9",
                         "E617037b7", "Ec0b77f96", "Ee7e8240b",
                         "Eb1705f8e"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E211966cc: Tap the Markor launcher icon (MAIN / LAUNCHER
        # intent filter, AndroidManifest.xml:61-71).
        r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
                 edge="E211966cc")
        # Ed6414d9f: The system calls Application.onCreate.
        r.comment("system calls Application.onCreate", edge="Ed6414d9f")
        # E0254b914: MAIN / LAUNCHER intent starts MainActivity after
        # Application.onCreate on a cold start. No separate action:
        # the launch above starts it.
        r.comment("system starts MainActivity after Application.onCreate",
                  edge="E0254b914")
        # Ed25af8f4: The system calls Activity.onCreate.
        r.comment("system calls Activity.onCreate", edge="Ed25af8f4")
        # Eba46a594: The system calls Activity.onStart then onResume.
        r.comment("system calls onStart then onResume", edge="Eba46a594")
        # E659e191c: Activity.performResume calls onPostResume.
        r.comment("performResume calls onPostResume", edge="E659e191c")
        # E0ecb8e4d: The notebook tab is the first page the pager
        # shows (position 0, MainActivity.java:105-106). No action.
        r.comment("notebook tab is the default startup tab",
                  edge="E0ecb8e4d")
        # E54b4aedd: Tap a bottom navigation tab. The To-Do item is
        # res/menu/main__bottom_nav.xml:20 (title @string/todo =
        # "To-Do", res/values/string-not_translatable.xml:42); the
        # listener is MainActivity.java:109-114. This tab opens the
        # todo document, i.e. the pushed fixture Documents/todo.txt.
        r.tap(edge="E54b4aedd", text="To-Do")
        # E80c409ce: Tab Todo is shown (the listener selects its
        # position). No action.
        r.comment("todo tab is shown", edge="E80c409ce")
        # E5bdf9e1e: Long-press an action button in the toolbar of
        # the todo page (the todo.txt format). Action buttons get
        # their content description from rstr(action.stringId)
        # (ActionButtonBase.java:343-354), and the insert-image
        # string resource value is literally
        # "abid_common_insert_image" (res/values/string-not_
        # translatable.xml:239). Its long-press case calls
        # insertCameraPhoto (ActionButtonBase.java:839, bytecode;
        # via runCommonLongPressAction, TodoTxtActionButtons
        # .java:208, bytecode).
        r.long_tap(edge="E5bdf9e1e", desc="abid_common_insert_image")
        # Ef154d966: Direct call to runCommonLongPressAction
        # (TodoTxtActionButtons.java:208, bytecode).
        r.comment("onActionLongClick calls runCommonLongPressAction",
                  edge="Ef154d966")
        # E0ef1d7c9: Direct call to insertCameraPhoto
        # (ActionButtonBase.java:839, bytecode).
        r.comment("runCommonLongPressAction calls insertCameraPhoto",
                  edge="E0ef1d7c9")
        # E617037b7: Direct call to fetchAndInsertItem
        # (AttachLinkOrFileDialog.java:510, bytecode).
        r.comment("insertCameraPhoto calls fetchAndInsertItem",
                  edge="E617037b7")
        # Ec0b77f96: FRAMEWORK, outside package: the camera app
        # returns the picture, and the callback inserts it.
        # fetchAndInsertItem passes the callback to
        # requestCameraPicture (AttachLinkOrFileDialog.java:414-420),
        # which starts MediaStore.ACTION_IMAGE_CAPTURE with
        # startActivityForResult (GsContextUtils.java:1777-1805).
        # The shutter/accept tap belongs to the emulator camera app,
        # whose UI is not pinned by any Markor source, so no tap
        # target is invented here; on a live run the operator (or a
        # camera-app step) captures and accepts, and the callback
        # at AttachLinkOrFileDialog.java:355-375 then fires.
        r.comment("camera app returns picture; callback inserts it "
                  "(operator/camera-app capture step, see REPORT.md)",
                  edge="Ec0b77f96")
        # Ee7e8240b: Direct call to setupFileAttachment
        # (AttachLinkOrFileDialog.java:373, bytecode).
        r.comment("callback calls setupFileAttachment",
                  edge="Ee7e8240b")
        # Eb1705f8e: Direct call to getAttachmentFolder
        # (AttachLinkOrFileDialog.java:287, bytecode). Target method
        # reached. (For a non-wikitext document this is the branch
        # at AttachLinkOrFileDialog.java:287-293.)
        r.comment("setupFileAttachment calls getAttachmentFolder",
                  edge="Eb1705f8e")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
