"""Device route script for Currency route_21.

Method: ChartActivity$DateAxisValueFormatter.getFormattedValue
Edge ids (in route order):
    E012ed474 Ee88066da Ef071a802 E4dd486ed E1d534c40 E7cc15d45 E32b68288
    Ed734335b Efb5de184 E38d20523 E14071438 Ed074f2c0 E1a13bbcc E00463ed3
    E90a0f80f E33c06b56 E91ef9af8 E1c05ac36 Ee53a0deb Eddbb6185
Printed route file:
    graphs/Currency/scratch/route_print/ChartActivity$DateAxisValueFormatter.getFormattedValue.txt
Permissions: (none)
Fixtures: (none)
Setup: network (ECB); cert issue on API<=27 images (handled by run_app.sh
    per-app setup, not by this script).
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E012ed474", "Ee88066da", "Ef071a802", "E4dd486ed", "E1d534c40",
    "E7cc15d45", "E32b68288", "Ed734335b", "Efb5de184", "E38d20523",
    "E14071438", "Ed074f2c0", "E1a13bbcc", "E00463ed3", "E90a0f80f",
    "E33c06b56", "E91ef9af8", "E1c05ac36", "Ee53a0deb", "Eddbb6185",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir,
               adb=args.adb)

    # E012ed474: S_ENTRY -> Main.<init>
    # Tap the Currency icon in the launcher (MAIN/LAUNCHER intent filter,
    # AndroidManifest.xml:19-24). Launcher component is Main, declared
    # without a package prefix, so ".Main" under the app package.
    r.launch("org.billthefarmer.currency/.Main", edge="E012ed474")

    # Ee88066da: Main.<init> -> Main.onCreate
    # Lifecycle edge: the system instantiates Main, then calls onCreate
    # (Main.java:242). No user action exists for this edge.
    r.comment("system instantiates Main then calls onCreate; no user action",
              edge="Ee88066da")

    # Ef071a802: Main.onCreate -> Main.onResume
    # Lifecycle edge: onStart -> onResume (Main.java:369). No user action.
    r.comment("onStart -> onResume; no user action", edge="Ef071a802")

    # E4dd486ed: Main.onResume -> S_MAIN_DISPLAY
    # Enters-page edge: Main becomes visible in DISPLAY_MODE (no selection
    # kept, Main.java:351-352). No user action.
    r.comment("Main visible in DISPLAY_MODE; no user action", edge="E4dd486ed")

    # E1d534c40: S_MAIN_DISPLAY -> Main.onItemLongClick
    # Long-press a currency row. Fresh install defaults (Main.java:94-97)
    # are USD, GBP, CAD, AUD, so "USD" is the first list row; its name
    # TextView (res/layout/item.xml, id/name) carries exactly that text.
    # Long-press switches Main to SELECT_MODE (Main.java:1428-1442).
    r.long_tap(text="USD", edge="E1d534c40")

    # E7cc15d45: Main.onItemLongClick -> S_MAIN_SELECT
    # Enters-page edge: mode = SELECT_MODE, the row is highlighted
    # (Main.java:1432-1437). No user action beyond the long-press above.
    r.comment("SELECT_MODE entered by the long-press above; no further action",
              edge="E7cc15d45")

    # E32b68288: S_MAIN_SELECT -> Main.onOptionsItemSelected@SELECT
    # Tap a menu item in the action bar (menu select.xml). "Chart" is an
    # icon-only item (showAsAction="ifRoom", res/menu/select.xml), so its
    # title appears as the action button's content description.
    r.tap(desc="Chart", edge="E32b68288")

    # Ed734335b: Main.onOptionsItemSelected@SELECT -> Main.onChartClick
    # Call edge: switch case R.id.action_chart (Main.java:805-806).
    # No user action beyond the Chart menu tap above.
    r.comment("menu case action_chart dispatches to onChartClick; no action",
              edge="Ed734335b")

    # Efb5de184: Main.onChartClick -> ChartActivity.<init>
    # Intent edge: startActivity(ChartActivity, CHART_LIST) (Main.java:955).
    # Follows directly from the Chart menu tap; no separate action.
    r.comment("startActivity(ChartActivity) follows the Chart tap; no action",
              edge="Efb5de184")

    # E38d20523: ChartActivity.<init> -> ChartActivity.onCreate
    # Lifecycle edge: the system instantiates ChartActivity, then onCreate
    # (ChartActivity.java:116). No user action.
    r.comment("system instantiates ChartActivity then onCreate; no action",
              edge="E38d20523")

    # E14071438: ChartActivity.onCreate -> ChartActivity.onResume
    # Lifecycle edge: onStart -> onResume (ChartActivity.java:285).
    # No user action.
    r.comment("onStart -> onResume; no user action", edge="E14071438")

    # Ed074f2c0: ChartActivity.onResume -> S_CHART_LOADING
    # Enters-page edge: no history yet ("Updating", Invert disabled),
    # guard histMap == null (ChartActivity.java:305,479). No user action.
    r.comment("chart loading, histMap == null; no user action",
              edge="Ed074f2c0")

    # E1a13bbcc: S_CHART_LOADING -> ChartActivity.onOptionsItemSelected@LOADING
    # Tap a menu item in the chart action bar (menu chart.xml). "New chart"
    # is an icon-only item (showAsAction="ifRoom", res/menu/chart.xml), so
    # its title appears as the action button's content description.
    # Timing note: this tap is made immediately after the chart opens,
    # while the ECB history download is still in flight, which is the
    # LOADING state the printed route requires.
    r.tap(desc="New chart", edge="E1a13bbcc")

    # E00463ed3: ChartActivity.onOptionsItemSelected@LOADING
    #     -> ChartActivity.onNewClick
    # Call edge: switch case R.id.action_new_chart
    # (ChartActivity.java:530-531). No user action beyond the tap above.
    r.comment("menu case action_new_chart dispatches to onNewClick; no action",
              edge="E00463ed3")

    # E90a0f80f: ChartActivity.onNewClick -> ChoiceDialog.<init>@CHART
    # Intent edge: startActivityForResult(ChoiceDialog, 0)
    # (ChartActivity.java:673-674). Follows from the New chart tap.
    r.comment("startActivityForResult(ChoiceDialog) follows the tap; no action",
              edge="E90a0f80f")

    # E33c06b56: ChoiceDialog.<init>@CHART -> ChoiceDialog.onCreate@CHART
    # Lifecycle edge: the system instantiates the dialog-themed
    # ChoiceDialog, then onCreate (ChoiceDialog.java:59). No user action.
    r.comment("system instantiates ChoiceDialog then onCreate; no action",
              edge="E33c06b56")

    # E91ef9af8: ChoiceDialog.onCreate@CHART -> S_CHOICE_DISPLAY@CHART
    # Enters-page edge: picker shown, nothing selected (ChoiceDialog.java:
    # 96-129; res/layout/choose.xml). No user action.
    r.comment("currency picker shown, nothing selected; no user action",
              edge="E91ef9af8")

    # E1c05ac36: S_CHOICE_DISPLAY@CHART -> ChoiceDialog.onItemClick@CHART
    # Tap a currency in the picker: it is picked and the picker closes
    # (ChoiceDialog.java:229-237). The picker lists Main.CURRENCIES in
    # order (ChoiceDialog.java:121-124), so "AUD" is the first row; its
    # name TextView (res/layout/choice.xml, id/name) carries that text.
    r.tap(text="AUD", edge="E1c05ac36")

    # Ee53a0deb: ChoiceDialog.onItemClick@CHART
    #     -> ChartActivity.onActivityResult@OK
    # Result edge: DISPLAY_MODE setResult(RESULT_OK, CHOICE=[position]);
    # finish() (ChoiceDialog.java:230-236). Follows from the picker tap.
    r.comment("RESULT_OK result follows the picker tap; no action",
              edge="Ee53a0deb")

    # Eddbb6185: ChartActivity.onActivityResult@OK
    #     -> ChartActivity$DateAxisValueFormatter.getFormattedValue
    # Framework edge: the MPAndroidChart library calls the formatter
    # (registered at ChartActivity.java:235) when the chart redraws for
    # the newly picked pair, once history has loaded (guard: RESULT_OK
    # and history loaded). No user action exists; the redraw is driven
    # by the library after the result, given the ECB download succeeds
    # (per-app setup handled by run_app.sh).
    r.comment("MPAndroidChart redraw calls the formatter; no user action",
              edge="Eddbb6185")

    r.done()


if __name__ == "__main__":
    main()
