"""Device replay script for Vanilla-Music route_29.

Method: LibraryPagerAdapter.setFilter
Edge ids: E47380ade E29472d10 E80427a98 E4af31f11 Ec9fbd220 E8fcdc3fd
    E30eace9c Efbc2494b
Printed route source: graphs/Vanilla-Music/verification.csv path row
    (result fixed; ref BottomBarControls.java:165-174,106-112;
    LibraryActivity.java:856,877-879,922-935,184,924) and
    device/routes/Vanilla-Music/ROUTES.csv route_29.
Permissions (ROUTES.csv): none. Fixtures: none (no STATE file gate).
Setup: push fixtures/Music + media scan (run_app setup step).
Standard config: run_app does pm clear before this script; the script
    starts by launching the app.
Selector notes (for the device lead to confirm on the replay image):
    the bottom-bar overflow is the standard action-bar overflow whose
    content description is "More options"; the search menu item is the
    MENU_SEARCH item. The search field is BottomBarControls' SearchView
    (res id search_view). If the overflow description differs on the
    replay image, that tap is the step to re-target; the rest of the
    chain (search field -> query text change -> setFilter) is fixed.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ["E47380ade", "E29472d10", "E80427a98", "E4af31f11", "Ec9fbd220",
            "E8fcdc3fd", "E30eace9c", "Efbc2494b"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_29", edge_ids=EDGE_IDS,
               log_path=a.log, dry_run=a.dry_run, outdir=a.outdir)
    # E47380ade: S_ENTRY -> LibraryActivity.<init>
    # MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("ch.blinkenlights.android.vanilla/.LibraryActivity",
             "E47380ade")
    # E29472d10: LibraryActivity.<init> -> onResume@LibraryActivity.
    # Activity lifecycle callback; no user action.
    r.comment("lifecycle: onResume runs on launch", "E29472d10")
    # E80427a98: onResume@LibraryActivity -> S_LIBRARY.
    # LibraryActivity is resumed and shown (default tab Artists).
    r.wait_for("E80427a98", text="Play all", timeout=30)
    # E4af31f11: S_LIBRARY -> BottomBarControls.onClick@MENUITEM.
    # Tap the search (magnifier) icon of the bottom bar: open the
    # action-bar overflow, then tap the search menu item (MENU_SEARCH).
    r.tap("E4af31f11", desc="More options")
    r.tap("E4af31f11", text="Search")
    # Ec9fbd220: onClick@MENUITEM -> onOptionsItemSelected@SEARCH.
    # The search icon was tapped (menu item MENU_SEARCH); no new action.
    r.comment("menu dispatch: search item selected", "Ec9fbd220")
    # E8fcdc3fd: onOptionsItemSelected@SEARCH -> S_LIBRARY_SEARCH.
    # The search field is open; tap it to focus it.
    r.tap("E8fcdc3fd", res_id="search_view")
    # E30eace9c: S_LIBRARY_SEARCH -> onQueryTextChange.
    # Type in the search field; the text change fires the callback.
    r.type_text("test", "E30eace9c")
    # Efbc2494b: onQueryTextChange -> setFilter. Direct call; target.
    r.comment("direct call: query text change sets the filter",
              "Efbc2494b")
    r.done()


if __name__ == "__main__":
    main()
