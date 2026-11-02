"""Device route script route_01 for Omni-Notes (template for routes 02-33).

Method: DetailFragment.onCoordinatesResolved
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Ecd2baeb2 E98c7a8e7
    Ebe6a7b0b E09745b8d Ea87362d4 E7406d945 E4d5a7b78 E98516fc5 Ee785a0de
    Ef4bcf5f8 Eeff2288d E78011c56 Ebf2dbffb E7f80b736 E1468b13a
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (DetailFragment.onCoordinatesResolved, 26 steps; path row result fixed,
    confirmed_by SOURCE, ref GeocodeHelper.java:164-170; DetailFragment.java:2195-2228)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Ecd2baeb2 '
            'E98c7a8e7 Ebe6a7b0b E09745b8d Ea87362d4 E7406d945 E4d5a7b78 '
            'E98516fc5 Ee785a0de Ef4bcf5f8 Eeff2288d E78011c56 Ebf2dbffb '
            'E7f80b736 E1468b13a').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_01', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ea7466154 S_ENTRY -> MainActivity.<init>: launcher starts MainActivity.
    r.launch('it.feio.android.omninotes/.MainActivity', 'Ea7466154')
    # E89791c67 MainActivity.<init> -> MainActivity.onResume: lifecycle, no action.
    r.comment('Activity lifecycle callback', 'E89791c67')
    # Edf932a3c MainActivity.onResume -> MainActivity.checkPassword: cold start,
    # no password gate, no action.
    r.comment('Cold start: isPasswordAccepted false, checkPassword runs', 'Edf932a3c')
    # E075b4776 MainActivity.checkPassword -> MainActivity.init: explicit call, no action.
    r.comment('No password gate: init()', 'E075b4776')
    # E2436b969 MainActivity.init -> ListFragment.<init>: explicit call, no action.
    r.comment('init() adds the list fragment', 'E2436b969')
    # E54b170af ListFragment.<init> -> ListFragment.onActivityCreated: lifecycle, no action.
    r.comment('Fragment lifecycle callback', 'E54b170af')
    # Ef86ebfe1 ListFragment.onActivityCreated -> ListFragment.init: explicit call, no action.
    r.comment('init()', 'Ef86ebfe1')
    # E7e3c321b ListFragment.init -> S_LIST@NOTES: list set up, no action.
    r.comment('List set up on the default Notes navigation', 'E7e3c321b')
    # E01d0dfd6 S_LIST@NOTES -> Fab.lambda$init$1@LONG_NOTES: long-press the + button
    # (FloatingActionsMenu add button, res/layout/fab.xml id fab).
    r.long_tap('E01d0dfd6', res_id='it.feio.android.omninotes:id/fab')
    # Ee5d1ab81 Fab long-press -> ListFragment.lambda$initFab$0@MAIN: menu dispatch, no action.
    r.comment('onFabItemClick(fab_expand_menu_button)', 'Ee5d1ab81')
    # E8a16cf02 lambda$initFab$0@MAIN -> S_DETAIL@NEW: a new note opens, no action.
    r.comment('A new note is opened', 'E8a16cf02')
    # Ecd2baeb2 S_DETAIL@NEW -> DetailFragment.onOptionsItemSelected@ATTACHMENT:
    # tap "Attachment" in the toolbar menu (menu_detail.xml, title "Attachment").
    r.tap('Ecd2baeb2', text='Attachment')
    # E98c7a8e7 onOptionsItemSelected@ATTACHMENT -> showAttachmentsPopup: menu branch, no action.
    r.comment('The attachment branch of the menu switch', 'E98c7a8e7')
    # Ebe6a7b0b showAttachmentsPopup -> S_DLG_ATTACH: popup opens, no action.
    r.comment('The attachment popup opens', 'Ebe6a7b0b')
    # E09745b8d S_DLG_ATTACH -> AttachmentOnClickListener.onClick@LOCATION:
    # tap "Location" in the attachment popup (string location).
    r.tap('E09745b8d', text='Location')
    # Ea87362d4 onClick@LOCATION -> displayLocationDialog: location branch, no action.
    r.comment('The location branch', 'Ea87362d4')
    # E7406d945 displayLocationDialog -> getLocation@DIALOG: explicit call, no action.
    r.comment('getLocation(new OnGeoUtilResultListenerImpl(...))', 'E7406d945')
    # E4d5a7b78 getLocation@DIALOG -> lambda$getLocation$7@DIALOG: permission granted,
    # callback runs, no action.
    r.comment('ACCESS_FINE_LOCATION granted: the callback runs', 'E4d5a7b78')
    # E98516fc5 lambda$getLocation$7@DIALOG -> GeocodeHelper.getLocation@DIALOG:
    # explicit call, no action.
    r.comment('GeocodeHelper.getLocation(listener)', 'E98516fc5')
    # Ee785a0de GeocodeHelper.getLocation@DIALOG -> GeocodeHelper$1.onNext@DIALOG:
    # SmartLocation delivers a one-shot fix, no user action.
    r.comment('SmartLocation delivers a one-shot fix', 'Ee785a0de')
    # Ef4bcf5f8 GeocodeHelper$1.onNext@DIALOG -> OnGeoUtilResultListenerImpl.onLocationRetrieved:
    # explicit call, no action.
    r.comment('listener.onLocationRetrieved(location)', 'Ef4bcf5f8')
    # Eeff2288d onLocationRetrieved -> S_DLG_LOCATION: internet available, search
    # dialog opens, no action.
    r.comment('Internet available: the location search dialog opens', 'Eeff2288d')
    # E78011c56 S_DLG_LOCATION -> lambda$onLocationRetrieved$0: tap "Use current
    # location" (string use_current_location). The typed-address alternative in
    # the trigger is the same lambda reading the dialog input.
    r.tap('E78011c56', text='Use current location')
    # Ebf2dbffb lambda$onLocationRetrieved$0 -> getCoordinatesFromAddress: explicit
    # call, no action.
    r.comment('Use the dialog address', 'Ebf2dbffb')
    # E7f80b736 getCoordinatesFromAddress -> lambda$getCoordinatesFromAddress$1:
    # SmartLocation geocoding calls back, no user action.
    r.comment('SmartLocation geocoding calls back with the coordinates', 'E7f80b736')
    # E1468b13a lambda$getCoordinatesFromAddress$1 -> DetailFragment.onCoordinatesResolved:
    # interface dispatch, no user action; the coverage lookup detects the target.
    r.comment('Virtual/interface call dispatching to this implementation', 'E1468b13a')
    r.done()


if __name__ == '__main__':
    main()
