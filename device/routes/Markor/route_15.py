#!/usr/bin/env python3
"""Markor route_15: DocumentShareIntoFragment$ShareIntoImportOptionsFragment
    .lambda$hasLinks$1.

Method: DocumentShareIntoFragment$ShareIntoImportOptionsFragment
    .lambda$hasLinks$1
Edge ids (in route order):
    E211966cc Ed6414d9f Ef7fef146 Ed80ab76d E082a98b1 E73fb7cb9
    Ed4b1b345 Ec1d50c8b Ef4c784b7 E8a4e3755 E7756ddc7 Eac7de4e9
Printed route file: graphs/Markor/scratch/route_print/route_15.txt
ROUTES.csv permissions: none.
ROUTES.csv fixtures: none.
Setup (verbatim): push fixtures/Documents; first-run tutorial can trap
    a tool.
No pm clear here (run_app.sh does it) and no fixture push here
    (run_app.sh does it per ROUTES.csv).
The shared text is a single web-link line so that hasLinks finds a
    link line (DocumentShareIntoFragment.java:347-356, 358-370).
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

    r = Runner(package=args.package, route="route_15",
               edge_ids=["E211966cc", "Ed6414d9f", "Ef7fef146",
                         "Ed80ab76d", "E082a98b1", "E73fb7cb9",
                         "Ed4b1b345", "Ec1d50c8b", "Ef4c784b7",
                         "E8a4e3755", "E7756ddc7", "Eac7de4e9"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E211966cc: The process starts when the other-app SEND
        # intent is delivered (see Ef7fef146 below). No separate
        # launcher action: this route does not start from the
        # Markor launcher icon.
        r.comment("process starts on delivery of the SEND intent",
                  edge="E211966cc")
        # Ed6414d9f: The system calls Application.onCreate on the
        # cold start, before the first activity.
        r.comment("system calls Application.onCreate", edge="Ed6414d9f")
        # Ef7fef146: Another app sends a text to Markor. Document
        # Activity declares the SEND intent filter (AndroidManifest
        # .xml:187-225, text/plain and text/*). The explicit
        # component avoids a share-sheet chooser on the emulator.
        # The shared text is a web link, so the share-into editor
        # holds a link line for hasLinks below (Patterns.WEB_URL
        # guard, DocumentShareIntoFragment.java:347-356).
        r.start_intent(edge="Ef7fef146",
                       action="android.intent.action.SEND",
                       mime="text/plain",
                       extras={"android.intent.extra.TEXT":
                               "https://example.com"},
                       component=args.package +
                       "/net.gsantner.markor.activity.DocumentActivity")
        # Ed80ab76d: The system calls Activity.onCreate
        # (DocumentActivity.java:135).
        r.comment("system calls DocumentActivity.onCreate",
                  edge="Ed80ab76d")
        # E082a98b1: onCreate hands the intent to
        # handleLaunchingIntent (DocumentActivity.java:149, bytecode).
        r.comment("onCreate calls handleLaunchingIntent",
                  edge="E082a98b1")
        # E73fb7cb9: The intent action is ACTION_SEND, so
        # handleLaunchingIntent calls showShareInto
        # (DocumentActivity.java:168-178, 177 bytecode).
        r.comment("SEND action branch calls showShareInto",
                  edge="E73fb7cb9")
        # Ed4b1b345: The FragmentManager creates the share-into view
        # (DocumentActivity.java:304-307; DocumentShareIntoFragment
        # .java:90).
        r.comment("fragment manager creates share-into view",
                  edge="Ed4b1b345")
        # Ec1d50c8b: Direct call creating the import-options fragment
        # (DocumentShareIntoFragment.java:97, bytecode).
        r.comment("onViewCreated creates ShareIntoImportOptionsFragment",
                  edge="Ec1d50c8b")
        # Ef4c784b7: PreferenceFragmentCompat calls onCreate
        # Preferences on this receiver (GsPreferenceFragmentBase
        # .java:153-160).
        r.comment("framework calls onCreatePreferences",
                  edge="Ef4c784b7")
        # E8a4e3755: Direct call to afterOnCreate
        # (GsPreferenceFragmentBase.java:169, bytecode).
        r.comment("onCreatePreferences calls afterOnCreate",
                  edge="E8a4e3755")
        # E7756ddc7: Direct call to hasLinks (DocumentShareInto
        # Fragment.java:224, bytecode). With no attachment, after
        # OnCreate evaluates hasLinks on the shared editor text.
        r.comment("afterOnCreate calls hasLinks", edge="E7756ddc7")
        # Eac7de4e9: The forEachline callback inside hasLinks
        # (DocumentShareIntoFragment.java:358-370; the lambda runs
        # synchronously while hasLinks iterates the editor text,
        # not on a later UI event). The shared line
        # "https://example.com" matches getLineLink's WEB_URL test
        # (DocumentShareIntoFragment.java:347-356), so this callback
        # fires on that line. Target lambda reached.
        r.comment("hasLinks forEachline callback runs on the link line",
                  edge="Eac7de4e9")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
