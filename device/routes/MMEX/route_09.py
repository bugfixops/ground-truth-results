"""MMEX route_09: CategoryListFragment$2.onClick -- SCRIPTED.

Method: CategoryListFragment$2.onClick
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ec1f72a40 Eb0beae6e
    E4e5784ab Edf5d5223 E8342ecee Ef41768f3 E3811dbae E6ca1fa24
    E315abb2d Edd98083e E72bda0fb E74dc669d
Printed route source:
    graphs/MMEX/scratch/route_print_final2/CategoryListFragment_2.onClick.txt
    (16 steps; print header env=- state=data) and the matching path
    row of graphs/MMEX/verification.csv (edge lists identical,
    checked). Cross-checked against out/methods.csv: state = "the
    row is a category (subCategId <= 0, line 455) and no account
    transaction uses it (CategoryService.isCategoryUsed false, line
    457)".
Permissions: none (no ENV permission gate on this route).
Fixtures: none (no STATE file gate; no MMEX file exists in
    $WEMU/fixtures).
Setup: MMEX first-run/database setup (tutorial + database creation;
    MainActivity.showPrerequisite, MainActivity.java:1478-1489).
    Setup runs before this script; the script itself starts at launch.
    In addition, the script creates its own unused category on the
    category list (setup taps inside the E315abb2d block, labelled
    SETUP): a fresh database has no category the delete dialog can
    offer Cancel for, and the created category is by construction
    unused, satisfying the state gate (CategoryListFragment.java:
    455-457).
Target: the Cancel button of the confirm-delete dialog.
    showDialogDeleteCategorySub builds the dialog with a positive
    android.R.string.ok button (listener $1) and a negative
    android.R.string.cancel button (listener $2, dialog.cancel())
    (CategoryListFragment.java:480-501); $2.onClick is therefore the
    Cancel tap. The script waits for the dialog title "Delete
    Category" (R.string.delete_category, strings.xml:135) before
    tapping Cancel, so it cannot mistake the cannot-delete dialog
    (which shows only OK, CategoryListFragment.java:460-476) for it.
Run (from the repo root, once placed under device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_09.py --package
    com.money.manager.ex --log steps/route_09.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ec1f72a40",
    "Eb0beae6e", "E4e5784ab", "Edf5d5223", "E8342ecee", "Ef41768f3",
    "E3811dbae", "E6ca1fa24", "E315abb2d", "Edd98083e", "E72bda0fb",
    "E74dc669d",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_09", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        # AndroidManifest.xml:136-143 (.home.MainActivity, MAIN +
        # LAUNCHER intent filter; package com.money.manager.ex).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Framework lifecycle, no user action.
        r.comment("framework calls MainActivity.onCreate after "
                  "creating the instance", edge="E2e074fc1")
        # E5d5a9c2f: Direct call, no user action.
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: Home screen shown, no user action. (First-run
        # tutorial + database creation are setup, done before this
        # script; see docstring.)
        r.comment("initHomeFragment commits HomeFragment (S_HOME)",
                  edge="Eff22f7d2")
        # Ec1f72a40: Tap the search action in the home options menu.
        # home_menu.xml:23-25 (menu_search, title @string/search =
        # "Search", showAsAction ifRoom); the action-bar icon exposes
        # its title as content description. HomeFragment.
        # onOptionsItemSelected handles menu_search
        # (HomeFragment.java:364-365).
        r.tap(desc="Search", edge="Ec1f72a40")
        # Eb0beae6e: Intent, no separate adb action.
        r.comment("home options menu starts SearchActivity",
                  edge="Eb0beae6e")
        # E4e5784ab: Framework lifecycle, no user action.
        r.comment("framework creates SearchActivity and calls "
                  "onCreate", edge="E4e5784ab")
        # Edf5d5223: Search page shown, no user action.
        r.comment("SearchActivity.onCreate shows the search page "
                  "(S_SEARCH)", edge="Edf5d5223")
        # E8342ecee: Tap Select category in the search form.
        # search_parameters_fragment.xml:187 (@+id/
        # textViewSelectCategory); the click listener starts
        # CategoryListActivity with ACTION_PICK
        # (SearchParametersFragment.java:199-207). Tap by res_id:
        # the field's displayed text is set programmatically and
        # starts empty.
        r.tap(res_id="textViewSelectCategory", edge="E8342ecee")
        # Ef41768f3: Intent, no separate adb action.
        r.comment("category field tap starts CategoryListActivity "
                  "(ACTION_PICK)", edge="Ef41768f3")
        # E3811dbae: Framework lifecycle, no user action.
        r.comment("framework calls CategoryListActivity.onCreate",
                  edge="E3811dbae")
        # E6ca1fa24: Framework lifecycle, no user action.
        r.comment("activity adds the fragment; framework calls "
                  "CategoryListFragment.onActivityCreated",
                  edge="E6ca1fa24")
        # E315abb2d: Category list page shown, no route action.
        # SETUP (not route edges, logged under this page edge):
        # create one fresh, unused category so the delete dialog
        # below offers Cancel. FAB tap: @+id/fab
        # (expandable_list_fragment.xml:67; wired at
        # BaseExpandableListFragment.java:225-230) calls
        # CategoryListFragment.onFloatingActionButtonClickListener
        # (CategoryListFragment.java:367-368), which shows the type
        # selector (CategoryListFragment.java:707-720). "Category"
        # is arrays.xml:358-360 item 0 (@string/category =
        # "Category", strings.xml:128); the edit dialog's field is
        # @+id/editTextCategName (dialog_new_edit_category.xml:25;
        # CategoryListFragment.java:517) and its positive button is
        # android.R.string.ok ("OK", CategoryListFragment.java:
        # 530-531).
        r.comment("category list page shown (S_CATEGORY_LIST)",
                  edge="E315abb2d")
        r.tap(res_id="fab", edge="E315abb2d")
        r.tap(text="Category", edge="E315abb2d")
        r.type_text("DeviceTestCategory", edge="E315abb2d")
        r.tap(text="OK", edge="E315abb2d")
        r.wait_for(text="DeviceTestCategory", edge="E315abb2d",
                   timeout=30)
        # Edd98083e: Long-press the new category row to open its
        # context menu (registerForContextMenu at
        # CategoryListFragment.java:130), then tap Delete.
        # Context menu items are added at
        # CategoryListFragment.java:173-176: Edit, Delete
        # (R.string.delete = "Delete", strings.xml:181), View
        # transactions.
        r.long_tap(text="DeviceTestCategory", edge="Edd98083e")
        r.tap(text="Delete", edge="Edd98083e")
        # E72bda0fb: Direct call, no user action. The DELETE case
        # calls showDialogDeleteCategorySub
        # (CategoryListFragment.java:216-217).
        r.comment("DELETE case calls showDialogDeleteCategorySub",
                  edge="E72bda0fb")
        # E74dc669d: Tap Cancel in the confirm-delete dialog.
        # Dialog title R.string.delete_category = "Delete Category"
        # (strings.xml:135); the negative button is
        # android.R.string.cancel ("Cancel") whose listener is $2
        # (CategoryListFragment.java:495-501). Waiting for the
        # title first rules out the cannot-delete dialog (OK only).
        r.wait_for(text="Delete Category", edge="E74dc669d",
                   timeout=30)
        r.tap(text="Cancel", edge="E74dc669d")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
