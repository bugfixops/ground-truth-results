"""Device route script for Markor route_04.

Method: DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getLinkTitle
Printed route: graphs/Markor/scratch/route_print/route_04.txt
Edge ids in order:
  E211966cc Ed6414d9f Ef7fef146 Ed80ab76d E082a98b1 E73fb7cb9 E2bb3f607
  E5426bbe1 E9a1bd2ed Eb9b06845 E42076cb6 Ebd928226 Ee5d19e6f E780defd9
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: (none)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
from harness import Runner

EDGE_IDS = [
    "E211966cc", "Ed6414d9f", "Ef7fef146", "Ed80ab76d", "E082a98b1",
    "E73fb7cb9", "E2bb3f607", "E5426bbe1", "E9a1bd2ed", "Eb9b06845",
    "E42076cb6", "Ebd928226", "Ee5d19e6f", "E780defd9",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E211966cc: The process starts when another app shares into Markor --
    # no user action yet; the share intent below starts the process.
    r.comment("process starts on share intent below", "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    r.comment("system calls Application.onCreate", "Ed6414d9f")
    # Ef7fef146: Another app sends a text to Markor (other_app entry).
    # DocumentActivity declares the SEND intent filter
    # (AndroidManifest.xml:187-225) and DocumentActivity.java:168-178
    # routes ACTION_SEND to showShareInto. The component is pinned to
    # Markor's DocumentActivity, the adb equivalent of choosing Markor
    # in the share sheet. Shared text is a bare URL line with no title
    # prefix, so getLineLink calls getLinkTitle on the whole line
    # (DocumentShareIntoFragment.java:346-361: si == -1 branch).
    r.start_intent("Ef7fef146", action="android.intent.action.SEND",
                   mime="text/plain",
                   extras={"android.intent.extra.TEXT": "https://example.com"},
                   component="net.gsantner.markor_test/net.gsantner.markor.activity.DocumentActivity")
    # Ed80ab76d: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "Ed80ab76d")
    # E082a98b1: onCreate hands the other-app intent to
    # handleLaunchingIntent -- no user action.
    r.comment("onCreate calls handleLaunchingIntent", "E082a98b1")
    # E73fb7cb9: The ACTION_SEND branch calls showShareInto -- no action.
    r.comment("SEND branch calls showShareInto", "E73fb7cb9")
    # E2bb3f607: The share-into fragment is committed, activity resumes
    # -- no user action.
    r.comment("share-into fragment committed then activity resumes",
              "E2bb3f607")
    # E5426bbe1: The share-into screen is shown -- no user action.
    r.comment("share-into screen shown", "E5426bbe1")
    # E9a1bd2ed: Tap a row of the import options (To-Do target).
    # DocumentShareIntoFragment.java:541-543: the todo row calls
    # attachOrCopyAndClose(getTodoFile(), false); the row title is
    # @string/todo = "To-Do" (res/values/string-not_translatable.xml:42,
    # res/xml/prefactions_share_into.xml todo row). The shared text is a
    # bare web link, so the link checkbox is visible and checked by
    # default (AppSettings.getFormatShareAsLink default true,
    # AppSettings.java:1127-1129), so getFormatted takes the asLink path.
    r.tap("E9a1bd2ed", text="To-Do")
    # Eb9b06845: onPreferenceClicked calls attachOrCopyAndClose -- no action.
    r.comment("preference click calls attachOrCopyAndClose", "Eb9b06845")
    # E42076cb6: attachOrCopyAndClose calls getFormatted -- no user action.
    r.comment("attachOrCopyAndClose calls getFormatted", "E42076cb6")
    # Ebd928226: getFormatted's per-line lambda runs -- framework-driven.
    r.comment("getFormatted per-line lambda runs", "Ebd928226")
    # Ee5d19e6f: The lambda calls getLineLink -- no user action.
    r.comment("lambda calls getLineLink", "Ee5d19e6f")
    # E780defd9: getLineLink calls getLinkTitle on the bare URL line
    # (DocumentShareIntoFragment.java:352) -- no user action.
    r.comment("getLineLink calls getLinkTitle", "E780defd9")

    r.done()


if __name__ == "__main__":
    main()
