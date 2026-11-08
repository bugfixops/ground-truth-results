#!/usr/bin/env python3
"""Diary route_29: FileProvider$SimplePathStrategy.getUriForFile.

Method: FileProvider$SimplePathStrategy.getUriForFile
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E9bfb25aa
    E94b2b3d6 Ec300822c
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "FileProvider$SimplePathStrategy.getUriForFile").
Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.
Standard configuration: run_app.sh does pm clear before this script.
"Share..." is showAsAction="never" (res/menu/main.xml:77-79, title
    res/values/strings.xml:31), so it lives in the overflow menu.
The target fires while Diary.share() builds the share intent (the
    URI is built before the chooser appears), so the script ends
    after the Share tap: no tap on the chooser is needed or made.
    The shared file is Diary.png from the MarkdownView drawing cache
    (or the entry file); both are app files, so no permission grant
    is needed.
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
    "E9bfb25aa", "E94b2b3d6", "Ec300822c",
]
COMPONENT = "org.billthefarmer.diary/.Diary"


def main():
    parser = argparse.ArgumentParser(description="Diary route_29 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_29", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
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
    # options. Here: open the overflow menu.
    r.tap("E002e1746", desc="More options")

    # E9bfb25aa -- switch case R.id.share. The Share item is
    # showAsAction="never", so its text is in the overflow menu.
    r.tap("E9bfb25aa", text="Share\u2026")

    # E94b2b3d6 -- share -> FileProvider.getUriForFile: the Share
    # tap runs share(), which builds the content:// URI from the
    # drawing cache / entry file before any chooser appears.
    # No separate action.
    r.comment("share builds the content:// URI via FileProvider",
              "E94b2b3d6")

    # Ec300822c -- strategy.getUriForFile(file): most specific
    # root -> content://authority/<root>/<path>. Consequence of
    # the URI build above; no separate action. The chooser that
    # follows is deliberately not touched: the target has fired.
    r.comment("SimplePathStrategy.getUriForFile resolves the URI",
              "Ec300822c")

    r.done()


if __name__ == "__main__":
    main()
