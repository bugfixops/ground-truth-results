"""MMEX route_16: SingleAccountWidgetConfigureActivity.saveTitlePref.

Method: SingleAccountWidgetConfigureActivity.saveTitlePref
Edge ids (in route order):
    E882eaf1e E13aab3f4 E1e63003e Ea6a92c49
Printed route source:
    graphs/MMEX/scratch/route_print_final2/SingleAccountWidgetConfigureActivity.saveTitlePref.txt
    (edges verified identical to the verification.csv path row for
    SingleAccountWidgetConfigureActivity.saveTitlePref).
Permissions: none (the route's ENV gate is other_app, not a permission
    gate; no runtime grant is needed).
Fixtures: none.
Setup: none (apps.csv MMEX setup is effectively none; this route is
    launched directly by intent and never goes through MainActivity,
    so the first-run tutorial / database prerequisite does not apply).
Run (from the repo root, after merge to device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_16.py --package
    com.money.manager.ex --log steps/route_16.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E882eaf1e", "E13aab3f4", "E1e63003e", "Ea6a92c49",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_16", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E882eaf1e: Another app sends an APPWIDGET_CONFIGURE intent to
        # the exported SingleAccountWidgetConfigureActivity
        # (AndroidManifest.xml:327-329, exported=true with the
        # APPWIDGET_CONFIGURE intent filter). The --ei extra is
        # required: onCreate finishes at once when the intent carries
        # no valid widget id (widget/
        # SingleAccountWidgetConfigureActivity.java:71-79: the id is
        # read from AppWidgetManager.EXTRA_APPWIDGET_ID and
        # INVALID_APPWIDGET_ID makes onCreate finish). Any id other
        # than INVALID (0) keeps the screen up; 1 is used here.
        r.start_intent(action="android.appwidget.action.APPWIDGET_CONFIGURE",
                       component="com.money.manager.ex/.widget.SingleAccountWidgetConfigureActivity",
                       extras_args=["--ei", "appWidgetId", "1"],
                       edge="E882eaf1e")
        # E13aab3f4: The framework calls onCreate right after the
        # constructor. No user action.
        r.comment("framework calls SingleAccountWidgetConfigureActivity "
                  "onCreate after the constructor", edge="E13aab3f4")
        # E1e63003e: Tap the Add button. onCreate sets the field
        # listener on add_button (widget/
        # SingleAccountWidgetConfigureActivity.java:65); the button is
        # res/layout/single_account_widget_configure.xml add_button
        # with text @string/add_widget = "Add widget"
        # (res/values/strings.xml:591). No text needs typing first:
        # onClick reads the (possibly empty) widget text and still
        # calls saveTitlePref.
        r.tap(res_id="add_button", edge="E1e63003e")
        # Ea6a92c49: onClick calls saveTitlePref directly (widget/
        # SingleAccountWidgetConfigureActivity.java:92). Consequence
        # of the tap, not a separate action.
        r.comment("SingleAccountWidgetConfigureActivity$1.onClick calls "
                  "saveTitlePref", edge="Ea6a92c49")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
