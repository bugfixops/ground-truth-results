"""Device route script route_21 for Omni-Notes.

Method: Attachment$1.<init>
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b E01d0dfd6 Ee5d1ab81 E8a16cf02 Ecd2baeb2
    E98c7a8e7 Ebe6a7b0b E6c861a8c Ec92956d5 Eefdb669e Ed61c3c8e
    Eb51a57a5 E8b0fb848 Ea135f7e7 E637c6da8 E5ced9fba
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/
    sample_30_routes.txt (Attachment$1.<init>, 23 steps; path row result
    fixed, confirmed_by SOURCE, ref SketchFragment.java:208-226;
    DetailFragment.java:385-388)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

Sketch drawing: the guard on the Back edge is that at least one stroke
was drawn (SketchView.getBitmap() != null, SketchView.java:204-207).
A single touch on the canvas satisfies it: SketchView.onTouch
ACTION_DOWN calls touch_start, which adds a path (moveTo + lineTo,
"for draw a one touch path"), so a long-press on the drawing view
creates a stroke without needing a drag gesture the harness cannot
express. Drawing view: res/layout/fragment_sketch.xml id drawing.

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
            'E98c7a8e7 Ebe6a7b0b E6c861a8c Ec92956d5 Eefdb669e Ed61c3c8e '
            'Eb51a57a5 E8b0fb848 Ea135f7e7 E637c6da8 E5ced9fba').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_21', EDGE_IDS, a.log,
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
    # E6c861a8c S_DLG_ATTACH -> AttachmentOnClickListener.onClick@SKETCH:
    # tap "Sketch" in the attachment popup (res/layout/attachment_dialog.xml
    # id sketch, text "Sketch"; DetailFragment.java:2267-2320).
    r.tap('E6c861a8c', text='Sketch')
    # Ec92956d5 onClick@SKETCH -> DetailFragment.takeSketch: sketch branch, no action.
    r.comment('The sketch branch: takeSketch(null)', 'Ec92956d5')
    # Eefdb669e DetailFragment.takeSketch -> S_SKETCH@EMPTY: the sketch editor
    # replaces the editor, no action.
    r.comment('The sketch editor replaces the editor', 'Eefdb669e')
    # Ed61c3c8e S_SKETCH@EMPTY -> SketchView.onTouch: draw on the canvas.
    # Long-press the drawing view (res/layout/fragment_sketch.xml id
    # drawing); ACTION_DOWN creates a one-touch path, satisfying the
    # at-least-one-stroke guard on the Back edge.
    r.long_tap('Ed61c3c8e', res_id='it.feio.android.omninotes:id/drawing')
    # Eb51a57a5 SketchView.onTouch -> S_SKETCH@DRAWN: a stroke is added, no action.
    r.comment('A stroke is added to the canvas', 'Eb51a57a5')
    # E8b0fb848 S_SKETCH@DRAWN -> MainActivity.onBackPressed@SKETCH_DRAWN:
    # press Back; Back saves the sketch (MainActivity.java:255-269).
    r.back('E8b0fb848')
    # Ea135f7e7 MainActivity.onBackPressed@SKETCH_DRAWN -> Attachment.<init>(Uri,String):
    # Back saves the sketch and the editor attaches it (DetailFragment.java:385-388),
    # no user action.
    r.comment('Back saves the sketch; editor attaches it', 'Ea135f7e7')
    # E637c6da8 Attachment.<init>(Uri,String) -> Attachment.<clinit>:
    # class initialisation on first use, no action.
    r.comment('Class initialisation on first use', 'E637c6da8')
    # E5ced9fba Attachment.<clinit> -> Attachment$1.<init>:
    # direct call, no user action; the coverage lookup detects the target.
    r.comment('Direct call building the CREATOR', 'E5ced9fba')
    r.done()


if __name__ == '__main__':
    main()
