"""MMEX route_24: NumericHelper.getNumberOfDecimals.

Method: NumericHelper.getNumberOfDecimals
Edge ids (in route order):
    Eabecce51 Ec0bef66f Ef46663fc E526e2cf0 E8707ce77 E1c7f52cc
    E8c18509f E75f796ec
Printed route source:
    graphs/MMEX/scratch/route_print_final2/NumericHelper.getNumberOfDecimals.txt
    (8 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for NumericHelper.getNumberOfDecimals
    exactly (checked by the helper; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate, so no
    permission from the manifest is granted by this route).
Fixtures: none (no STATE file gate).
Setup: none (apps.csv MMEX setup is effectively none).
Caveat for the merger/device lead (not a script action): the format
    branch runs only when the base currency resolves to a real
    Currency (CurrencyService.java:297-309: a null currency returns
    value.toString() at :301-303 and never calls format). The graph
    records no state gate for this route, so this script implements
    the printed route as written; a replay database with no base
    currency would take the null branch and never reach the target.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_24.py --package
    com.money.manager.ex --log steps/route_24.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "Eabecce51", "Ec0bef66f", "Ef46663fc", "E526e2cf0", "E8707ce77",
    "E1c7f52cc", "E8c18509f", "E75f796ec",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_24", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eabecce51: The framework creates the widget receiver by
        # class name because the manifest declares it exported with
        # the APPWIDGET_UPDATE intent filter
        # (AndroidManifest.xml:89-99, .widget.AccountBillsWidgetProvider).
        # A broadcast to that component with a non-empty widget-id
        # array drives the same entry; there is no launcher tap for a
        # widget receiver.
        r.broadcast(edge="Eabecce51",
                    action="android.appwidget.action.APPWIDGET_UPDATE",
                    extras_args=["--eia", "appWidgetIds", "1"],
                    component="com.money.manager.ex/.widget.AccountBillsWidgetProvider")
        # Ec0bef66f: AppWidgetProvider.onReceive calls onUpdate for
        # ACTION_APPWIDGET_UPDATE (FW-SRC AppWidgetProvider.java:57-68),
        # guarded on non-null extras and a non-empty id array; the
        # --eia extra above supplies both. No separate action.
        r.comment("onReceive calls onUpdate (APPWIDGET_UPDATE)",
                  edge="Ec0bef66f")
        # Ef46663fc: onUpdate calls getBaseCurrencyFormatted
        # (AccountBillsWidgetProvider.java:52). No user action.
        r.comment("onUpdate calls getBaseCurrencyFormatted",
                  edge="Ef46663fc")
        # E526e2cf0: getBaseCurrencyFormatted calls
        # getCurrencyFormatted (CurrencyService.java:280).
        # No user action.
        r.comment("getBaseCurrencyFormatted calls getCurrencyFormatted",
                  edge="E526e2cf0")
        # E8707ce77: getCurrencyFormatted formats the value with the
        # currency for the given id (CurrencyService.java:297-309;
        # format is called only at :309, when getCurrency is non-null).
        # No user action. See the docstring caveat.
        r.comment("getCurrencyFormatted calls FormatUtilities.format",
                  edge="E8707ce77")
        # E1c7f52cc: format(Money, Currency) forwards to the
        # show-symbols overload (FormatUtilities.java:180).
        # No user action.
        r.comment("format forwards to format(Money, boolean, Currency)",
                  edge="E1c7f52cc")
        # E8c18509f: format forwards to the scale/pattern overload
        # with the currency (FormatUtilities.java:157-160; null
        # returns "n/a" at :157). No user action.
        r.comment("format forwards to scale/pattern overload",
                  edge="E8c18509f")
        # E75f796ec: format(Money, int, String, String) calls
        # getNumberOfDecimals (FormatUtilities.java:191).
        # No user action.
        r.comment("format calls getNumberOfDecimals",
                  edge="E75f796ec")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
