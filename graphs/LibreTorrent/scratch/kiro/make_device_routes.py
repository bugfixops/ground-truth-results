"""Write device/routes/LibreTorrent/ (ROUTES.csv, route_NN.py, setup_route_NN.py) from the final
verification.csv path rows, out/methods.csv and the per-edge actions below (Kiro, 2026-11-03).

Run from the repo root: python3 -I graphs/LibreTorrent/scratch/kiro/make_device_routes.py
Actions come from printed layout/menu/strings/handler lines in scratch/kiro/prints/ui_map.txt;
every edge without an action gets r.comment(<trigger>, edge=...)."""
import csv
import glob
import json
import os
import re

APP = 'LibreTorrent'
PKG = 'org.proninyaroslav.libretorrent.debug'
MAIN = PKG + '/org.proninyaroslav.libretorrent.ui.main.MainActivity'
ADD_TORRENT = PKG + '/org.proninyaroslav.libretorrent.ui.addtorrent.AddTorrentActivity'
OUT = 'device/routes/LibreTorrent'
STORAGE = 'android.permission.READ_EXTERNAL_STORAGE;android.permission.WRITE_EXTERNAL_STORAGE'
TORRENT_FIX = 'gen:kiro_sample.torrent -> /sdcard/Download/kiro_sample.torrent'

g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
lab = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % APP, encoding='utf-8'))}
paths = [r for r in csv.DictReader(open('graphs/%s/verification.csv' % APP, encoding='utf-8')) if r['type'] == 'path']
table = {}
for line in open('graphs/%s/scratch/route_table.md' % APP, encoding='utf-8'):
    m = re.match(r'^\| (\d+) \| (\S+) \| \w+ \| \d+ \| (\w+) \|', line)
    if m:
        table[m.group(2)] = (int(m.group(1)), m.group(3))

LAUNCH = ('launch', MAIN)
TAP_ROW = ('tap', dict(text='kiro_sample.bin'))
UNSCRIPTABLE = {
    'TorrentDownloadImpl.havePiece':
        'unscriptable: step 13 (NanoHTTPD$ClientHandler.run) needs an HTTP client connected to the app streaming '
        'server and the route needs a downloaded piece to stream (TorrentInputStream.waitForPiece); no harness '
        'primitive makes an HTTP request on the device, and piece data needs a live BitTorrent peer (network)',
    'AdvancedPeerInfo.isUtp':
        'unscriptable: the route builds a PeerInfo for a connected peer (PeerInfo.java:110); a connected BitTorrent '
        'peer needs a live swarm on the network, which adb cannot create on an AOSP emulator',
    'TorrentEngine$5.lambda$onTorrentMoving$4':
        'unscriptable: the route needs a torrent that finishes downloading (TorrentDownloadImpl.handleTorrentFinished, '
        'step 11) with move-after-download on; finishing needs the data from a live BitTorrent peer (network)',
}
# Per-route: setup kind, permissions, fixtures, edge actions, docstring notes.
R = {
    'TrackerInfo.infoHashStatus': dict(setup='torrent', perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH], 'Ef521ec44': [TAP_ROW], 'E00bf2e7e': [('tap', dict(text='Trackers'))]},
        note='Tab labels from DetailTorrentFragment.java:192-207 (R.string.torrent_trackers = "Trackers"). '
             'If the tab view exposes its label in caps, the text match fails loudly (live risk).'),
    'TorrentDownloadImpl.pieces': dict(setup='torrent', perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH], 'Ef521ec44': [TAP_ROW], 'E00bf2e7e': [('tap', dict(text='Pieces'))]},
        note='Tab labels from DetailTorrentFragment.java:192-207 (R.string.torrent_pieces = "Pieces"). '
             'The Pieces tab may need the tab strip scrolled first (live risk).'),
    'SelectTagDialog.onTagClicked': dict(setup='torrent+tag', perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH], 'Ef521ec44': [TAP_ROW], 'E490f604c': [('tap', dict(text='Add tag'))],
        'E71fb1ae3': [('wait_for', dict(text='kirotag')), ('tap', dict(text='kirotag'))]},
        note='Route judged UNCLEAR (needs a tag no earlier step creates); the per-route setup creates tag '
             '"kirotag" first. Add-tag chip text: AddTagButton.java:60 (R.string.add_tag = "Add tag").'),
    'tag.TagsAdapter$ViewHolder.lambda$bind$0': dict(setup='torrent+tag', perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH], 'Ef521ec44': [TAP_ROW], 'E490f604c': [('tap', dict(text='Add tag'))],
        'E71fb1ae3': [('wait_for', dict(text='kirotag')), ('tap', dict(text='kirotag'))]},
        note='Route judged UNCLEAR (needs a tag no earlier step creates); the per-route setup creates tag '
             '"kirotag" first.'),
    'FixedRingBuffer$FixedRingBufferIterator.<init>': dict(acts={'Ef4711e98': [LAUNCH]}),
    'FileItem.<init>(int,String,boolean,long)': dict(setup='gen', perms='android.permission.READ_EXTERNAL_STORAGE',
        fix=TORRENT_FIX, acts={'Ec711e542': [('intent', ADD_TORRENT)]},
        note='Another app opening a .torrent is simulated with an explicit VIEW intent to the exported '
             'AddTorrentActivity (AndroidManifest.xml:62-92). Storage read is granted so the file:// source opens.'),
    'BencodeFileItem$1.<init>': dict(setup='gen', perms='android.permission.READ_EXTERNAL_STORAGE', fix=TORRENT_FIX,
        acts={'Ec711e542': [('intent', ADD_TORRENT)]},
        note='Explicit VIEW intent to the exported AddTorrentActivity (AndroidManifest.xml:62-92).'),
    'AddLinkViewModel.normalizeUrl': dict(perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH],
        'Ed7e1785e': [('tap', dict(res_id='fab_button')), ('tap', dict(text='Add link'))],
        'Ea674eaf3': [('tap', dict(res_id='link')), ('type', 'https://example.com/kiro.torrent'), ('tap', dict(text='Add'))]},
        note='FAB id fab_button (fragment_main.xml:33-34), item label R.string.add_link (MainFragment.java:445-449), '
             'link field id link (dialog_add_link.xml:24), positive button "Add" (AddLinkDialog.java:238-240).'),
    'SaveLogWorker.lambda$showSuccessToast$1': dict(perms=STORAGE, acts={
        'Ef4711e98': [LAUNCH],
        'E6507c563': [('tap', dict(desc='More options')), ('tap', dict(text='Journal'))],
        'E4fb31cce': [('tap', dict(desc='Save'))],
        'Ede62e53d': [('wait_for', dict(desc='OK')), ('tap', dict(desc='OK'))]},
        note='Menu: log_menu "Journal" (menu/main.xml:26-27, overflow), save_log_menu "Save" '
             '(menu/log.xml:17-20, ifRoom), FileManagerDialog OK (menu/filemanager.xml:15-18) with the prefilled '
             'file name (LogActivity.java:311). Storage write is granted for the save file.'),
    'TorrentCriticalWork.lambda$emitChangedEvent$0': dict(setup='torrent', perms=STORAGE, acts={
        'E2f8f0c2f': [('drag', (540, 5, 540, 1400, 'open the notification shade with a 600 ms swipe from the status bar (harness drag minimum 500 ms); the status bar edge has no view id')),
                      ('wait_for', dict(text='Shutdown')), ('tap', dict(text='Shutdown'))]},
        note='The per-route setup adds a torrent, so TorrentService runs with its foreground notification; '
             'the "Shutdown" action (TorrentService.java:483-489) sends the shutdown PendingIntent. If the action '
             'row is collapsed, the tap fails loudly (live risk).'),
}
for m in ('DefaultFsModule.<init>', 'SafFsModule.<init>', 'FileSystemFacadeImpl.<init>',
          'MainApplication.increaseCursorWindowSize', 'TorrentNotifier.makeNotifyChans', 'MainApplication.<init>',
          'FsModuleResolverImpl.<init>'):
    R[m] = dict(acts={'Ec86728f9': [LAUNCH], 'Edbdfd5b2': [LAUNCH]},
                note='Application process start: launching the launcher activity starts the process.')

SETUP_TMPL = '''#!/usr/bin/env python3
"""LibreTorrent per-route setup for {route} ({method}). Generated by
graphs/LibreTorrent/scratch/kiro/make_device_routes.py (Kiro, 2026-11-03).

{what}

Invoked by run_app.sh after `pm clear`, before the fixture phase and the route script:
    setup_{route}.py --package <pkg> --log <log> --outdir <dir> --gen-dir <dir> [--adb adb]
Any failure exits 1 (failed_at_step_0, setup_failed). UI-driving setups are recorded as
MMEX-B3-UIDRIVE in device/run_app.sh; this one ends on the launcher (HOME), and the route
script starts with its own launch.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))

import lt_common  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--package", default="{pkg}")
    p.add_argument("--log", default=None)
    p.add_argument("--outdir", default=None)
    p.add_argument("--gen-dir", default=None)
    p.add_argument("--adb", default="adb")
    a = p.parse_args(argv)
    gen_dir = a.gen_dir or os.environ.get("GEN_DIR", "") or os.getcwd()
    os.makedirs(gen_dir, exist_ok=True)

    def log(msg):
        if a.log:
            with open(a.log, "a", encoding="utf-8") as f:
                f.write(msg + "\\n")
        print(msg)
{body}
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''
BODY_GEN = '''
    path = lt_common.make_torrent(os.path.join(gen_dir, lt_common.TORRENT_FILE))
    log("generated " + path)'''
BODY_TORRENT = '''
    from device.harness import Runner
    r = Runner(package=a.package, route="{route}-setup", edge_ids=None,
               log_path=a.log or os.path.join(gen_dir, "setup.log"), adb=a.adb,
               outdir=a.outdir or gen_dir)
    lt_common.add_torrent(a.adb, a.package, gen_dir, r, log)'''
BODY_TAG = BODY_TORRENT + '''
    # Create tag "kirotag": torrent detail -> "Add tag" chip (AddTagButton.java:60) -> SelectTagActivity
    # "New tag" (SelectTagDialog.java:147,156-158) -> AddTagDialog name field (dialog_add_tag.xml:24)
    # -> "Add" (AddTagDialog.java:177-178) -> back out of the select-tag dialog -> HOME.
    r.launch("{main}", edge="setup")
    r.wait_for(edge="setup", text=lt_common.TORRENT_NAME, timeout=30)
    r.tap(edge="setup", text=lt_common.TORRENT_NAME)
    r.wait_for(edge="setup", text="Add tag", timeout=30)
    r.tap(edge="setup", text="Add tag")
    r.wait_for(edge="setup", text="New tag", timeout=30)
    r.tap(edge="setup", text="New tag")
    r.wait_for(edge="setup", res_id="name", timeout=30)
    r.tap(edge="setup", res_id="name")
    r.type_text("kirotag", edge="setup")
    r.tap(edge="setup", text="Add")
    r.wait_for(edge="setup", text="kirotag", timeout=30)
    r.back(edge="setup")
    r.key("KEYCODE_HOME", edge="setup")
    r.done()
    log("created tag kirotag")'''
WHAT = {'gen': 'Generates kiro_sample.torrent (lt_common.make_torrent) into --gen-dir; the fixture phase pushes it '
               'to /sdcard/Download/kiro_sample.torrent (ROUTES.csv fixtures: gen:kiro_sample.torrent).',
        'torrent': 'Adds one torrent (kiro_sample.bin, lt_common.add_torrent) so the route has a listed torrent / a '
                   'live session torrent. Grants storage itself (needed before its own VIEW intent).',
        'torrent+tag': 'Adds one torrent and creates the tag "kirotag" through the app UI, so the select-tag list has '
                       'one row (the STATE the route needs).'}

SCRIPT_HEAD = '''"""LibreTorrent {route}: {method}.

Method: {method}
Edge ids (in route order):
{edges}
Printed route source:
    graphs/LibreTorrent/scratch/route_print/{pfile}.txt
    ({n} steps; env={env} state={state}). Judged {verdict} (route_table.md row {row:02d}).
Permissions: {perms}
Fixtures: {fixtures}
Setup: {setup}
Notes: {note}
Run (from the repo root):
    python3 -I device/routes/LibreTorrent/{route}.py --package {pkg}
    --log steps/{route}.log --outdir <outdir> [--dry-run] [--adb adb]
Generated by graphs/LibreTorrent/scratch/kiro/make_device_routes.py (Kiro, 2026-11-03).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
{edgelist}
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="{route}", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    gen_dir = os.environ.get("GEN_DIR", "")
    try:
'''
SCRIPT_TAIL = '''    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def pyrepr(s):
    return json.dumps(s)


def act_lines(eid, act):
    k = act[0]
    if k == 'launch':
        return ['r.launch(%s, edge=%s)' % (pyrepr(act[1]), pyrepr(eid))]
    if k == 'intent':
        return ['r.start_intent(edge=%s, action="android.intent.action.VIEW",' % pyrepr(eid),
                '               data="file:///sdcard/Download/kiro_sample.torrent",',
                '               mime="application/x-bittorrent", component=%s)' % pyrepr(act[1])]
    if k == 'type':
        return ['r.type_text(%s, edge=%s)' % (pyrepr(act[1]), pyrepr(eid))]
    if k == 'drag':
        x1, y1, x2, y2, why = act[1]
        return ['r.drag(edge=%s, x1=%d, y1=%d, x2=%d, y2=%d, duration_ms=600,' % (pyrepr(eid), x1, y1, x2, y2),
                '       why=%s)' % pyrepr(why)]
    kw = ', '.join('%s=%s' % (a, pyrepr(b)) for a, b in act[1].items())
    if k == 'wait_for':
        return ['r.wait_for(edge=%s, %s, timeout=30)' % (pyrepr(eid), kw)]
    return ['r.%s(edge=%s, %s)' % (k, pyrepr(eid), kw)]


def wrap(text, width=96, indent='        # '):
    words, lines, cur = text.split(), [], ''
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    return [indent + l for l in lines]


os.makedirs(OUT, exist_ok=True)
rows = []
for n, p in enumerate(paths, 1):
    route = 'route_%02d' % n
    m = p['item']
    ids = p['edges'].split()
    lr = lab[m]
    assert ids == lr['route_edge_ids'].split(), m
    row, verdict = table[m]
    assert row == n, (m, row, n)
    status, perms, fix, setup = 'scripted', '', '', ''
    if verdict == 'WRONG':
        status = 'unscriptable: route WRONG as drawn (see route_table.md)'
    elif m in UNSCRIPTABLE:
        status = UNSCRIPTABLE[m]
    else:
        spec = R[m]
        perms, fix = spec.get('perms', ''), spec.get('fix', '')
        kind = spec.get('setup')
        if kind:
            setup = 'setup_%s.py: %s' % (route, WHAT[kind])
            body = {'gen': BODY_GEN, 'torrent': BODY_TORRENT, 'torrent+tag': BODY_TAG}[kind]
            src = SETUP_TMPL.format(route=route, method=m, what=WHAT[kind], pkg=PKG,
                                    body=body.format(route=route, main=MAIN))
            open(os.path.join(OUT, 'setup_%s.py' % route), 'w', encoding='utf-8').write(src)
        pfile = re.sub(r'[$]', '_', m)
        if not os.path.exists('graphs/%s/scratch/route_print/%s.txt' % (APP, pfile)):
            pfile = m
        edges_doc = '\n'.join('    ' + ' '.join(ids[i:i + 6]) for i in range(0, len(ids), 6))
        head = SCRIPT_HEAD.format(route=route, method=m, edges=edges_doc, pfile=pfile, n=len(ids),
                                  env=lr['env_kinds'] or '-', state=lr['state_kinds'] or '-', verdict=verdict,
                                  row=row, perms=perms or 'none', fixtures=fix or 'none', setup=setup or 'none',
                                  note=spec.get('note', '-'), pkg=PKG,
                                  edgelist='\n'.join('    %s,' % pyrepr(i) for i in ids))
        body = []
        acts = spec['acts']
        for i in ids:
            x = E[i]
            body += wrap('%s: %s -> %s [%s]. %s%s' % (i, x['src'], x['dst'], x['kind'], x['trigger'],
                                                    (' Guard: %s.' % x['guard']) if x.get('guard') else ''))
            if i in acts:
                for a in acts[i]:
                    body += ['        ' + l for l in act_lines(i, a)]
            else:
                body.append('        r.comment(%s, edge=%s)' % (pyrepr(x['trigger']), pyrepr(i)))
        open(os.path.join(OUT, '%s.py' % route), 'w', encoding='utf-8').write(head + '\n'.join(body) + '\n' + SCRIPT_TAIL)
        unused = set(acts) - set(ids)
        assert not unused or unused == {'Ec86728f9'} or unused == {'Edbdfd5b2'}, (m, unused)
    rows.append([route, m, ' '.join(ids), 'route_table.md row %02d' % row, lr['env_kinds'], lr['state_kinds'],
                 perms, fix, setup, status])
with open(os.path.join(OUT, 'ROUTES.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['route', 'method', 'edges', 'source', 'env_kinds', 'state_kinds', 'permissions', 'fixtures', 'setup', 'status'])
    w.writerows(rows)
print('rows', len(rows), 'scripted', sum(r[-1] == 'scripted' for r in rows))
