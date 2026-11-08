"""Device route script route_33 for Omni-Notes.

Method: ListFragment.initNotesList
Edge ids: Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af
    Ef86ebfe1 Ec8760433
Printed route: route_print_ListFragment_initNotesList.txt (in this
    directory), constructed from the trigger graph
    (graphs/Omni-Notes/out/omni-notes_trigger_graph.json, edge ids in
    ROUTES.csv order, plus the shortest_path from out/methods.csv), NOT
    read step by step from a sample print: no dedicated section for this
    method exists in the overnight sample print
    (graphs/Omni-Notes/scratch/overnight-20261101/scratch-outputs/sample_30_routes.txt);
    the method appears there only as an intermediate step of longer routes.
Permissions (granted by run_app.sh from ROUTES.csv before this script runs):
    none (ROUTES.csv route_33 permission column is empty)
Fixtures: none. Setup (ROUTES.csv): push fixtures/Pictures (app-level first-run setup).
Standard configuration: run_app.sh already ran pm clear, the setup, the fixture
pushes, and the permission grants; this script starts from a fresh process.

One block per route edge, in route order. Lifecycle, page, explicit-call, and
framework edges with no user action get a comment, not an action. Every action
names an edge id of this route (the harness enforces it).

Why this script has no taps: the target is reached by the cold-start chain
itself. ListFragment.onActivityCreated calls init() (ListFragment.java:246),
and init() calls initNotesList(mainActivity.getIntent()) (ListFragment.java:255)
before any list-setup UI step. The list-setup work inside initNotesList
(progress wheel, NoteLoaderTask) follows the target edge and is not itself
scripted. No selector is used, so no selector needs grounding in
layout/menu/strings XML.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ea7466154 E89791c67 Edf932a3c E075b4776 E2436b969 E54b170af '
            'Ef86ebfe1 Ec8760433').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_33', EDGE_IDS, a.log,
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
    # Ec8760433 ListFragment.init -> ListFragment.initNotesList: direct call, no action;
    # the coverage lookup detects the target at entry. The list-setup work
    # inside initNotesList follows this edge and needs no UI step to reach it.
    r.comment('init() calls initNotesList(intent): target reached', 'Ec8760433')
    r.done()


if __name__ == '__main__':
    main()
