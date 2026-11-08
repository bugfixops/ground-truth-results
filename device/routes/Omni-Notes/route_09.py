"""Device route script route_09 for Omni-Notes.

Method: Tag$1.<init>
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 E7e3c321b Ed7cc3cfc Ec7f86b0f E1381b1f8 E0d56ea8a E9d4da329
    E35369cf7 Ebb3d1b0a E40638447 Ed4644675 E2da2a402 Ef30cdbc6
Printed route: graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt
    (Tag$1.<init>, 19 steps; DbHelper.java:685-706; Tag.java:65-70)
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none.
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it). The note with a
#tag the route needs (STATE "at least one #tag is written in some note") is
created as STATE steps folded into the Ed7cc3cfc block, before that edge's
own search-icon tap, following the precedent for STATE steps in other
device scripts; it is marked STATE there, not presented as the Ed7cc3cfc
trigger itself. DbHelper.getTags matches notes whose title or content
contains '#' (DbHelper.java:696-700), so the tag in the content suffices.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 E7e3c321b Ed7cc3cfc Ec7f86b0f E1381b1f8 E0d56ea8a '
            'E9d4da329 E35369cf7 Ebb3d1b0a E40638447 Ed4644675 E2da2a402 '
            'Ef30cdbc6').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_09', EDGE_IDS, a.log,
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
    # Ed7cc3cfc S_LIST@NOTES -> ListFragment$2.onMenuItemActionExpand: tap the
    # search icon. STATE first (this route needs a note containing a #tag):
    # create a note the way route_01 creates one — long-press the + button
    # (res/layout/fab.xml id fab), tap the title field
    # (res/layout/fragment_detail.xml id detail_title) and the content field
    # (res/layout/fragment_detail_content.xml id detail_content), type a
    # #tag in the content, then Back saves the note and returns to the list.
    r.long_tap('Ed7cc3cfc', res_id='it.feio.android.omninotes:id/fab')
    r.tap('Ed7cc3cfc', res_id='it.feio.android.omninotes:id/detail_title')
    r.type_text('Route09 note', 'Ed7cc3cfc')
    r.tap('Ed7cc3cfc', res_id='it.feio.android.omninotes:id/detail_content')
    r.type_text('Note with #route09tag inside', 'Ed7cc3cfc')
    r.back('Ed7cc3cfc')
    # The edge's own trigger: tap the search icon (menu_list.xml id
    # menu_search, title "Search"). UNCERTAINTY: a toolbar icon item has no
    # text node, so this taps by content description; the description is
    # taken to be the item title, which is not verified on device (see report).
    r.tap('Ed7cc3cfc', desc='Search')
    # Ec7f86b0f onMenuItemActionExpand -> S_LIST_SEARCH_EDIT: the search view
    # expands and takes focus, no action.
    r.comment('The search view expands and takes focus', 'Ec7f86b0f')
    # E1381b1f8 S_LIST_SEARCH_EDIT -> ListFragment.onOptionsItemSelected@TAGS:
    # tap the tags icon, which is visible while the search view has focus
    # (ListFragment.java:775; menu_list.xml id menu_tags, title "Tags").
    # Same content-description uncertainty as the search icon above.
    r.tap('E1381b1f8', desc='Tags')
    # E0d56ea8a onOptionsItemSelected@TAGS -> ListFragment.performAction@T_TAGS:
    # explicit call, no action.
    r.comment('performAction(item, null)', 'E0d56ea8a')
    # E9d4da329 performAction@T_TAGS -> ListFragment.filterByTags: the tags
    # branch of the toolbar switch, no action.
    r.comment('The tags branch of the toolbar switch', 'E9d4da329')
    # E35369cf7 filterByTags -> TagsHelper.getAllTags: explicit call, no action.
    r.comment('Direct call', 'E35369cf7')
    # Ebb3d1b0a TagsHelper.getAllTags -> DbHelper.getTags(): explicit call, no action.
    r.comment('Direct call', 'Ebb3d1b0a')
    # E40638447 DbHelper.getTags() -> DbHelper.getTags(Note): explicit call, no action.
    r.comment('Direct call', 'E40638447')
    # Ed4644675 DbHelper.getTags(Note) -> Tag.<init>(String,Integer): one Tag
    # per #tag found in a note; the STATE tag above satisfies it, no action.
    r.comment('One Tag per #tag found in a note', 'Ed4644675')
    # E2da2a402 Tag.<init>(String,Integer) -> Tag.<clinit>: class initialisation
    # on first use, no action.
    r.comment('Class initialisation on first use', 'E2da2a402')
    # Ef30cdbc6 Tag.<clinit> -> Tag$1.<init>: explicit call, no action; the
    # coverage lookup detects the target (the CREATOR built in Tag.java:65).
    r.comment('The class initialiser builds the CREATOR', 'Ef30cdbc6')
    r.done()


if __name__ == '__main__':
    main()
