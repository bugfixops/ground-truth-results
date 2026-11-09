"""Build run_result/ (a frozen copy of the final results) and the READMEs (README.md, run_result/README.md,
run_result/emulator/README.md) from the files on the branch. Every number in the generated text is computed here from
the committed files; the prose comes from tools/results_templates/*.md ({{NAME}} placeholders).

Run from the repo root on a clean tree, after the official CI commit you want to publish:
  python3 -I tools/pack_results.py .
It stops (exit 1) if any app's CI summary is not at 0 errors and 0 warnings, if the CI summaries name different
request commits, or if tools_dev/check_terms.py flags a generated README (publishing rule of the 2026-11-03 review).
The emulator run of record is RUN below; set the environment variable RUN_OF_RECORD to publish a newer run."""
import collections
import csv
import glob
import os
import re
import shutil
import subprocess
import sys

root = sys.argv[1]
TPL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results_templates')
os.chdir(root)
APPS = 'Currency Diary hash-checker Omni-Notes openlauncher Vanilla-Music Markor AnyMemo Aegis AmazeFileManager AnkiDroid MMEX LibreTorrent'.split()
RUN = os.environ.get('RUN_OF_RECORD') or '41593209101-1'
BASE = subprocess.run(['git', 'rev-parse', '--short=8', 'HEAD'], capture_output=True, text=True).stdout.strip()
OUT = 'run_result'
if os.path.exists(OUT):
    shutil.rmtree(OUT)


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def cptree(src, dst):
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))


def fmt(n):
    return '{:,}'.format(n)


def rate(e, c):
    return '%.3f' % (e / c) if c else 'n/a'


# ---------------------------------------------------------------- per-app numbers
rows = []
for a in APPS:
    s = open('graphs/%s/scratch/ci_latest/SUMMARY.txt' % a, encoding='utf-8').read()
    g = lambda rx: re.search(rx, s, re.M)
    m = [int(x) for x in g(r'^methods (\d+), pages (\d+), edges (\d+)').groups()]
    v = [int(x) for x in g(r'^verdicts: REACHABLE (\d+), UNREACHABLE (\d+)').groups()]
    d = [int(x) for x in g(r'^verification device: routes (\d+), reached (\d+) \(script finished (\d+)\), unclear (\d+)').groups()]
    assert g(r'^errors: 0$') and g(r'^warnings: 0$'), a
    ci = g(r'commit ([0-9a-f]+)').group(1)
    readme = open('graphs/%s/out/README.md' % a, encoding='utf-8').read()
    ps = dict((k, int(n)) for k, n in re.findall(r'(\w+) (\d+)', re.search(r'Path status over all reachable methods: (.*)\.', readme).group(1)))
    ver = collections.Counter()
    for r in csv.DictReader(open('graphs/%s/verification.csv' % a, encoding='utf-8')):
        if r['confirmed_by'] != 'DEVICE':
            ver[(r['type'], r['result'])] += 1
    row = {'app': a, 'methods': m[0], 'pages': m[1], 'edges': m[2], 'reachable': v[0], 'unreachable': v[1]}
    for t in ('label', 'edge', 'path'):
        c, f, w, u = (ver[(t, k)] for k in ('correct', 'fixed', 'wrong', 'unclear'))
        row.update({t + '_rows': c + f + w + u, t + '_checked': c + f + w, t + '_fixed': f, t + '_wrong': w,
                    t + '_unclear': u, t + '_error_rate': rate(f + w, c + f + w)})
    # The app's run of record is the one run its graphs/<App>/device/results.csv was written from (device/compare.py):
    # 41593209101-1 for the eight apps outside the re-audit, 42560435293-1 for the five re-audited apps.
    gres = list(csv.DictReader(open('graphs/%s/device/results.csv' % a, encoding='utf-8')))
    aruns = sorted({r['run'] for r in gres})
    assert len(aruns) == 1, (a, aruns)
    row['device_run'] = aruns[0]
    res = list(csv.DictReader(open('device/results/%s/%s/results.csv' % (aruns[0], a), encoding='utf-8')))
    # Device totals rule (reviewer, 2026-11-09). Two numbers, never mixed:
    #   device_routes / device_reached / device_ok / device_unclear: the run total, read from the app's run of record
    #     (device_run) results.csv, unchanged by later graph changes;
    #   device_rows / device_rows_reached / device_rows_ok: the DEVICE rows of verification.csv (the build line
    #     "verification device"), i.e. confirmations of the current best route under the device row rule
    #     (tools_dev/device_rows.py). A reached row that replays an older route is dropped there, so these can be lower.
    reached = [r for r in res if r['reached'] == 'yes']
    row.update({'device_routes': len(res), 'device_reached': len(reached),
                'device_ok': sum(1 for r in reached if r['script_status'] == 'ok'),
                'device_unclear': len(res) - len(reached),
                'device_rows': d[0], 'device_rows_reached': d[1], 'device_rows_ok': d[2],
                'device_scripted': sum(1 for r in res if r['script_status'] != 'unscriptable'),
                'device_unscriptable': sum(1 for r in res if r['script_status'] == 'unscriptable'),
                'path_status_DEVICE_OK': ps.get('DEVICE_OK', 0), 'path_status_SOURCE_OK': ps.get('SOURCE_OK', 0),
                'path_status_WRONG': ps.get('WRONG', 0), 'path_status_UNCHECKED': ps.get('UNCHECKED', 0), 'ci_request': ci})
    # Only reached rows may be dropped by the row rule: every missing verification row is a reached row of the app's
    # device/results.csv.
    assert len(gres) - d[0] == sum(1 for r in gres if r['reached'] == 'yes') - d[1] >= 0, a
    rows.append(row)
T = collections.Counter()
for r in rows:
    for k, val in r.items():
        if isinstance(val, int):
            T[k] += val
cis = sorted({r['ci_request'] for r in rows})
assert len(cis) == 1
CI = cis[0]

# ---------------------------------------------------------------- copy the results
for a in APPS:
    dst = '%s/apps/%s' % (OUT, a)
    for f in sorted(glob.glob('graphs/%s/out/*' % a)):
        cp(f, '%s/graph/%s' % (dst, os.path.basename(f)))
    for f in sorted(glob.glob('graphs/%s/scratch/ci_latest/*' % a)):
        cp(f, '%s/ci/%s' % (dst, os.path.basename(f)))
    cp('graphs/%s/verification.csv' % a, dst + '/verification.csv')
    cp('graphs/%s/readme_notes.md' % a, dst + '/readme_notes.md')
    cp('graphs/%s/device/results.csv' % a, dst + '/device/results.csv')
    cp('device/routes/%s/ROUTES.csv' % a, dst + '/routes.csv')
E = OUT + '/emulator'
cptree('device/results/%s' % RUN, '%s/run_%s' % (E, RUN))
runs = []
for p in sorted(glob.glob('device/results/*/')):
    rid = os.path.basename(p.rstrip('/'))
    per = [list(csv.DictReader(open(f, encoding='utf-8'))) for f in sorted(glob.glob(p + '*/results.csv'))]
    runs.append((rid, len(per), sum(len(x) for x in per), sum(1 for x in per for r in x if r['reached'] == 'yes')))
    if rid != RUN:
        cptree(p, '%s/earlier_runs/%s' % (E, rid))
dry = []
for p in sorted(glob.glob('device/dryrun/*/')):
    rid = os.path.basename(p.rstrip('/'))
    t = open(p + 'SUMMARY.md', encoding='utf-8').read() if os.path.exists(p + 'SUMMARY.md') else ''
    pf = re.findall(r'\|\s*(\d+)\s*\|\s*(\d+)\s*\|', t)
    dry.append((rid, len(pf), sum(int(x) for x, _ in pf), sum(int(y) for _, y in pf)))
    cptree(p, '%s/dry_runs/%s' % (E, rid))
for f in ('handoff/DEVICE_RUN_SUMMARY.md', 'handoff/KIRO_REPORT_EMULATOR.md', '.github/workflows/device-replay.yml'):
    cp(f, '%s/%s' % (E, os.path.basename(f)))

with open(OUT + '/SUMMARY.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\n')
    w.writeheader()
    w.writerows(rows)

# ---------------------------------------------------------------- tables
def table_main():
    L = ['| App | Methods | Edges | REACHABLE | UNREACHABLE | Label errors found | Edge errors found | Route errors found | Emulator: reached | DEVICE_OK |',
         '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows + [dict(T, app='**Total**')]:
        def er(t):
            e, c = r[t + '_fixed'] + r[t + '_wrong'], r[t + '_checked']
            return '%s of %s (%s)' % (fmt(e), fmt(c), rate(e, c)) if c else 'none checked'
        L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %d of %d | %d |' % (
            r['app'], fmt(r['methods']), fmt(r['edges']), fmt(r['reachable']), fmt(r['unreachable']),
            er('label'), er('edge'), er('path'), r['device_reached'], r['device_routes'], r['device_ok']))
    return '\n'.join(L)


def table_device():
    L = ['| App | Routes | Scripted | Unscriptable | Reached | Reached and script finished (DEVICE_OK) | Unclear |',
         '|---|---:|---:|---:|---:|---:|---:|']
    for r in rows + [dict(T, app='**Total**')]:
        L.append('| %s | %d | %d | %d | %d | %d | %d |' % (r['app'], r['device_routes'], r['device_scripted'], r['device_unscriptable'],
                                                     r['device_reached'], r['device_ok'], r['device_unclear']))
    return '\n'.join(L)


def table_runs():
    notes = {
        '41578755210-1': 'started by hand; every job failed at emulator setup: no Google APIs x86_64 image exists for API 27, so the image was switched to x86',
        '41580035601-1': 'only 1 route per app ran (route list read wrongly in run_app.sh); fixed',
        '41580858995-1': 'screen dumps could not be parsed (a status line after the XML); fixed',
        '41581852815-1': 'first complete run; taps came before cold-started screens were drawn; harness now waits',
        '41583852305-1': 'Markor job lost to a download error; AnyMemo and Amaze launch names fixed',
        '41586297765-1': 'all-caps button text and the Diary start-up permission dialog; fixed',
        '41589762145-1': 'shared sample files were not pushed to the device; Vanilla needed storage permission; fixed',
        RUN: '**run of record** (all results below)',
    }
    L = ['| Run | Apps with results | Routes | Reached | What happened |', '|---|---:|---:|---:|---|']
    for rid, napps, n, y in runs:
        where = 'run_%s/' % rid if rid == RUN else 'earlier_runs/%s/' % rid
        L.append('| [`%s`](%s) | %d | %d | %d | %s |' % (rid, where, napps, n, y, notes.get(rid, '')))
    return '\n'.join(L)


def table_dry():
    notes = {
        '41576644702-1': 'final dry run of all apps before the real run',
        '41578222764-1': 'after the workflow edit (Google APIs image, SSH server for Amaze)',
        '41579127015-1': 'after the switch to the x86 image and the real-run request file',
        '41579432533-1': 'a real-run request that ran as a dry run (fixed in the plan job)',
    }
    L = ['| Dry run | Apps | Scripts PASS | Scripts FAIL | Note |', '|---|---:|---:|---:|---|']
    for rid, napps, ok, bad in dry:
        if napps == 0:
            L.append('| [`%s`](dry_runs/%s/) | 0 | – | – | no results collected (early test of the collect step) |' % (rid, rid))
        else:
            L.append('| [`%s`](dry_runs/%s/) | %d | %d | %d | %s |' % (rid, rid, napps, ok, bad, notes.get(rid, 'dry run during the preparation of the route scripts')))
    return '\n'.join(L)


ps_tot = 'DEVICE_OK %s, SOURCE_OK %s, WRONG %s, UNCHECKED %s' % (fmt(T['path_status_DEVICE_OK']), fmt(T['path_status_SOURCE_OK']),
                                                                  fmt(T['path_status_WRONG']), fmt(T['path_status_UNCHECKED']))
low = sorted(rows, key=lambda r: r['device_reached'] / r['device_routes'])[:3]
low_s = ', '.join('%s %d/%d' % (r['app'], r['device_reached'], r['device_routes']) for r in low)
high = sorted(rows, key=lambda r: -r['device_reached'] / r['device_routes'])[:3]
high_s = ', '.join('%s %d/%d' % (r['app'], r['device_reached'], r['device_routes']) for r in high)
pct = 100.0 * T['device_reached'] / T['device_routes']

V = dict(BASE=BASE, CI=CI, RUN=RUN, TABLE_MAIN=table_main(), TABLE_DEVICE=table_device(), TABLE_RUNS=table_runs(), TABLE_DRY=table_dry(),
         M=fmt(T['methods']), E=fmt(T['edges']), R=fmt(T['reachable']), U=fmt(T['unreachable']),
         LROWS=fmt(T['label_rows']), EROWS=fmt(T['edge_rows']), PROWS=fmt(T['path_rows']),
         LFIX=T['label_fixed'], LWRONG=T['label_wrong'], EFIX=T['edge_fixed'], PFIX=T['path_fixed'], PWRONG=T['path_wrong'],
         ROUTES=T['device_routes'], SCRIPTED=T['device_scripted'], UNSCR=T['device_unscriptable'], REACHED=T['device_reached'],
         DOK=T['device_ok'], DUNCL=T['device_unclear'], PCT='%.1f' % pct, PARTIAL=T['device_reached'] - T['device_ok'],
         PS=ps_tot, LOW=low_s, HIGH=high_s, NRUNS=len(runs), NDRY=len(dry))

for tpl, dst in (('root_readme.md', 'README.md'), ('run_result.md', OUT + '/README.md'), ('emulator.md', E + '/README.md')):
    text = open(os.path.join(TPL, tpl), encoding='utf-8').read()
    for k, val in V.items():
        text = text.replace('{{%s}}' % k, str(val))
    left = re.findall(r'\{\{\w+\}\}', text)
    assert not left, (dst, left)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools_dev'))
    import check_terms
    lines = check_terms.flagged(text)
    if lines:
        sys.exit('%s: lines %s are flagged by tools_dev/check_terms.py (publishing rule: describe the sample only as an independent hand-labelled sample)' % (dst, lines))
    open(dst, 'w', encoding='utf-8').write(text)
    print('wrote', dst)
print('totals', dict((k, T[k]) for k in ('methods', 'edges', 'reachable', 'unreachable', 'device_routes', 'device_reached', 'device_ok')))
print('runs', runs)
print('dry', dry)
