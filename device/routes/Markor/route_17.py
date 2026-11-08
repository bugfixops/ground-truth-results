"""Markor route_17: WrWidgetConfigure$1.<init>.

Edge ids in order: E211966cc, Ed6414d9f, Eac90525a, Ef6a25cc2, E252d515f,
E7e3cded2.
Printed route file: graphs/Markor/scratch/route_print/route_17.txt.
ROUTES.csv permissions: none. Fixtures: none.
Setup: push fixtures/Documents; first-run tutorial can trap a tool.
Package: net.gsantner.markor_test.

Flow: start the notebook-widget configure activity from outside the
package with the APPWIDGET_CONFIGURE action and a valid widget id, as
the launcher does when the widget is added (AndroidManifest.xml:91-97
declares WrWidgetConfigure exported with the APPWIDGET_CONFIGURE
filter). With a valid id, onCreate calls showWidgetSelectFolderDialog
(WrWidgetConfigure.java:44), which creates the anonymous
SelectionListenerAdapter (WrWidgetConfigure.java:58) -- the target
WrWidgetConfigure$1.<init>.
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
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_17",
               edge_ids=["E211966cc", "Ed6414d9f", "Eac90525a", "Ef6a25cc2",
                         "E252d515f", "E7e3cded2"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc: process starts when the widget is added -- the process
    # start is a system consequence of the configure launch below; no
    # separate user action (no launcher-icon tap: this route does not go
    # through MainActivity).
    r.comment("Process starts via the configure launch below", "E211966cc")
    # Ed6414d9f: system calls Application.onCreate -- no user action.
    r.comment("Application.onCreate runs by the system", "Ed6414d9f")
    # Eac90525a: Add the notebook widget: the setup screen opens and
    # asks for a folder. Started from outside the package, exactly as
    # the launcher starts it, with a valid widget id (otherwise
    # onCreate skips the folder dialog, WrWidgetConfigure.java:43-46).
    r.start_intent("Eac90525a",
                   action="android.appwidget.action.APPWIDGET_CONFIGURE",
                   component="net.gsantner.markor_test/other.writeily.widget.WrWidgetConfigure",
                   extras_args=["--ei", "appWidgetId", "1"])
    # Ef6a25cc2: system calls Activity.onCreate -- no user action.
    r.comment("Activity.onCreate runs by the system", "Ef6a25cc2")
    # E252d515f: direct call showWidgetSelectFolderDialog -- no user
    # action (WrWidgetConfigure.java:44).
    r.comment("showWidgetSelectFolderDialog runs from onCreate", "E252d515f")
    # E7e3cded2: direct call creating WrWidgetConfigure$1 -- no user
    # action (WrWidgetConfigure.java:58, the SelectionListenerAdapter
    # passed to showFolderDialog).
    r.comment("WrWidgetConfigure$1 created by showWidgetSelectFolderDialog",
              "E7e3cded2")
    r.done()


if __name__ == "__main__":
    main()
