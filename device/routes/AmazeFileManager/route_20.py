#!/usr/bin/env python3
"""AmazeFileManager route_20: ItemPopupMenu$2.onButtonPressed(Intent,String).

Method: ItemPopupMenu$2.onButtonPressed(Intent,String)
Edge ids in order:
    E61915364 E987df97b E3b805bab E89466062 E199e866f Ee1989850
    E76306566 Ebc940def E8c3004b6 E2e277bd5 E4bc6e8e1 E15498a19
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ItemPopupMenu_2.onButtonPressed(Intent,String).txt, verdict
    REACHABLE, 12 edges. The print's edge list matches
    methods.csv route_edge_ids and the d1_routes_draft.csv
    route_20 row exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
    (MainActivity's storage gate, MainActivity.java:436-484, and
    the encryption itself writes a new .aze file next to the
    fixture).
Fixtures: amaze_encrypt_fixture.txt (this directory), pushed to
    /sdcard/Download/amaze_encrypt_fixture.txt. It is a plain
    .txt file, so it is not already encrypted (no .aze suffix)
    and the encrypt menu item is shown for it.
Setup: none beyond the standard config. The script relies on
    fresh-install defaults: the current tab is the list view
    (MainFragment IS_LIST starts true, MainFragment.java:142),
    so the overflow View item is titled "Grid View"; and no
    master password or fingerprint is set and the encrypt
    warning has never been dismissed, so the warning dialog
    appears before the password dialog (see below).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (the storage pair above).

Mapping notes (printed source):
  - The View toggle is the trigger for switchView:
    MainActivity.onOptionsItemSelected case R.id.view
    (MainActivity.java:996-1024) calls ma.switchView(). The
    menu item itself has an empty title in XML
    (res/menu/activity_extra.xml: view item), but
    onPrepareOptionsMenu sets it dynamically: when the current
    fragment is in list view it becomes "Grid View"
    (MainActivity.java:847-849, res/values/strings.xml:139).
    The item has no showAsAction, so it lives in the overflow
    menu, opened with the "More options" content description.
  - The per-file overflow is the ItemViewHolder about button:
    RecyclerAdapter.onBindViewHolder calls showPopup
    (holder.about, rowItem) in both list and grid branches
    (RecyclerAdapter.java:557,813), and ItemViewHolder.about
    is R.id.properties (ItemViewHolder.java:50). showPopup
    sets an OnClickListener that builds an ItemPopupMenu,
    inflates res/menu/item_extras.xml, and shows it
    (RecyclerAdapter.java:948-984). The encrypt item is
    R.id.encrypt, title "Encrypt" (res/values/strings.xml:500);
    showPopup makes it visible for non-.aze files on API >= 18
    (RecyclerAdapter.java:974-978), which holds on the API 27
    emulator for this .txt fixture.
  - The printed edge onMenuItemClick -> showEncryptAuthenticate
    Dialog is a summary: the real UI passes through the warning
    dialog first, because the crypt-warning-remember preference
    defaults to false (PreferencesConstants.java:49).
    ItemPopupMenu case R.id.encrypt builds the encrypt intent
    and, since the preference is false, shows
    showEncryptWarningDialog (ItemPopupMenu.java:179-193,
    GeneralDialogCreation.java:639-680); tapping its positive
    button "Got it!" (res/values/strings.xml:514) calls the
    1-arg onButtonPressed, which -- with no master password
    (default "", PreferencesConstants.java:47) and no
    fingerprint (default false, :48) -- calls
    showEncryptAuthenticateDialog (ItemPopupMenu.java:156-170).
    The script therefore taps Encrypt, then "Got it!", and only
    then fills the password dialog. If the warning preference
    were already true, the "Got it!" tap would fail; the
    standard `pm clear` start guarantees it is false.
  - The password dialog is GeneralDialogCreation
    .showEncryptAuthenticateDialog (GeneralDialogCreation
    .java:714-807): title "Encrypt", two password fields
    R.id.edit_text_dialog_encrypt_password and
    R.id.edit_text_dialog_encrypt_password_confirm with hints
    "Password" and "Repeat password"
    (res/layout/dialog_encrypt_authenticate.xml,
    res/values/strings.xml:248,612), a save-as field prefilled
    with "<name>.aze" (:734), and positive button "OK"
    (res/values/strings.xml:148). The OK button starts
    disabled and is enabled by the text watcher once all three
    fields are non-empty (:768-780), and the confirm validator
    requires the two passwords to match (:790-794), so the
    script types the same disposable test password twice and
    leaves the prefilled .aze name untouched. The positive
    lambda (:752-764) then calls onButtonPressed(intent,
    password) at :757 -- the target.
  - The harness import below searches upward for the directory
    containing device/harness/harness.py instead of the template's
    fixed four-level climb, because this helper copy lives one
    level shallower than device/routes/<App>/; the same file
    therefore imports unchanged after the merger moves it there.
"""

import argparse
import os
import sys

_here = os.path.abspath(__file__)
for _depth in (3, 4):
    _root = _here
    for _ in range(_depth):
        _root = os.path.dirname(_root)
    if os.path.isfile(os.path.join(_root, "device", "harness", "harness.py")):
        sys.path.insert(0, _root)
        break
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E61915364", "E987df97b", "E3b805bab", "E89466062", "E199e866f",
    "Ee1989850", "E76306566", "Ebc940def", "E8c3004b6", "E2e277bd5",
    "E4bc6e8e1", "E15498a19",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/com.amaze.filemanager.activities.MainActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "amaze_encrypt_fixture.txt")
DEVICE_PATH = "/sdcard/Download/amaze_encrypt_fixture.txt"
FIXTURE_NAME = "amaze_encrypt_fixture.txt"
# Disposable test password for the ephemeral emulator fixture
# only; it is never a real credential and is typed twice so the
# confirm validator passes.
TEST_PASSWORD = "AmazeTest123"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_20")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_20", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E61915364 S_ENTRY -> MainActivity.onOptionsItemSelected:
    # launch MainActivity (MAIN/LAUNCHER, AndroidManifest.xml
    # :61-65) and push the file to encrypt. The options-item
    # callback itself fires on the View tap in the next block.
    r.launch(MAIN, "E61915364")
    r.push_fixture(FIXTURE, "E61915364", dest=DEVICE_PATH)
    # E987df97b MainActivity.onOptionsItemSelected ->
    # MainFragment.switchView: open the overflow menu and tap
    # the View item, which onPrepareOptionsMenu titled
    # "Grid View" because the current fragment starts in list
    # view (MainActivity.java:847-849); the case calls
    # ma.switchView() (MainActivity.java:996-1024).
    r.tap("E987df97b", desc="More options")
    r.tap("E987df97b", text="Grid View")
    # E3b805bab MainFragment.switchView -> MainFragment
    # .reloadListElements: switchView reloads the list in grid
    # mode (MainFragment.java:391-393). No user action.
    r.comment("switchView reloads the list in grid mode",
              "E3b805bab")
    # E89466062 MainFragment.reloadListElements ->
    # RecyclerAdapter.<init>: the reload constructs a new
    # RecyclerAdapter (MainFragment.java:1107). Wait for the
    # file list view (R.id.listView) so the reload has run.
    r.wait_for("E89466062", res_id="listView", timeout=30)
    # E199e866f RecyclerAdapter.<init> -> RecyclerAdapter
    # .onCreateViewHolder: RecyclerView creates view holders.
    # No user action.
    r.comment("RecyclerView creates view holders", "E199e866f")
    # Ee1989850 RecyclerAdapter.onCreateViewHolder ->
    # RecyclerAdapter.onBindViewHolder: RecyclerView binds rows.
    # No user action.
    r.comment("RecyclerView binds rows", "Ee1989850")
    # E76306566 RecyclerAdapter.onBindViewHolder -> RecyclerAdapter
    # .showPopup: binding attaches the popup listener to each
    # row's about button (RecyclerAdapter.java:813). Navigate
    # to the fixture first: the current tab shows internal
    # storage root, so tap the Download folder, then scroll to
    # the fixture row.
    r.tap("E76306566", text="Download")
    r.scroll_to("E76306566", text=FIXTURE_NAME)
    # Ebc940def RecyclerAdapter.showPopup -> ItemPopupMenu
    # .<init>: tap the fixture row's overflow button
    # (R.id.properties); the showPopup listener constructs the
    # ItemPopupMenu and shows it (RecyclerAdapter.java:950).
    # The back row's about button is GONE (RecyclerAdapter
    # .java:503-505), so the first visible overflow button in
    # the Download listing belongs to a file row; the scroll
    # above puts the fixture row on screen.
    r.tap("Ebc940def", res_id="properties")
    # E8c3004b6 ItemPopupMenu.<init> -> ItemPopupMenu
    # .onMenuItemClick: the constructor registered this as the
    # menu click listener (ItemPopupMenu.java:60). Tap Encrypt
    # in the popup menu; the click listener takes the encrypt
    # case (ItemPopupMenu.java:132).
    r.tap("E8c3004b6", text="Encrypt")
    # E2e277bd5 ItemPopupMenu.onMenuItemClick ->
    # GeneralDialogCreation.showEncryptAuthenticateDialog: the
    # encrypt case first shows the warning dialog (the printed
    # edge summarizes this hop), because the
    # crypt-warning-remember preference defaults to false.
    # Tap its positive button "Got it!" to reach the password
    # dialog via the 1-arg onButtonPressed path (no master
    # password, no fingerprint set).
    r.tap("E2e277bd5", text="Got it!")
    # E4bc6e8e1 GeneralDialogCreation
    # .showEncryptAuthenticateDialog -> GeneralDialogCreation
    # .lambda$showEncryptAuthenticateDialog$16: fill both
    # password fields with the same test password (the confirm
    # validator requires a match), leave the prefilled
    # "<name>.aze" save-as value untouched, then tap OK; the
    # positive lambda runs (GeneralDialogCreation.java:752-764).
    r.tap("E4bc6e8e1", res_id="edit_text_dialog_encrypt_password")
    r.type_text(TEST_PASSWORD, "E4bc6e8e1")
    r.tap("E4bc6e8e1",
          res_id="edit_text_dialog_encrypt_password_confirm")
    r.type_text(TEST_PASSWORD, "E4bc6e8e1")
    r.tap("E4bc6e8e1", text="OK")
    # E15498a19 GeneralDialogCreation
    # .lambda$showEncryptAuthenticateDialog$16 ->
    # ItemPopupMenu$2.onButtonPressed(Intent,String): the
    # positive lambda calls onButtonPressed(intent, password)
    # (GeneralDialogCreation.java:757), which starts the
    # encryption. No further UI step; the target is reached.
    r.comment("positive lambda calls onButtonPressed(intent, "
              "password); encryption starts", "E15498a19")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
