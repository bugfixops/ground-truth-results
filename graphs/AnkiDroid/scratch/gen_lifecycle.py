import csv, collections
G = 'graphs/AnkiDroid/'
nodes = {}
for r in csv.DictReader(open(G + 'scratch/node_names.tsv'), delimiter='\t'):
    nodes[r['node']] = r
scan = list(csv.DictReader(open(G + 'scratch/screen_scan.tsv'), delimiter='\t'))
COMP = {'Activity', 'AppCompatActivity', 'FragmentActivity', 'PreferenceActivity', 'Fragment', 'DialogFragment',
        'Service', 'BroadcastReceiver', 'ContentProvider', 'Application', 'AppWidgetProvider'}
LCB = ['onAttach', 'onCreate', 'onCreateView', 'onCreateDialog', 'onStart', 'onResume', 'onPause', 'onStop',
       'onDestroyView', 'onDestroy', 'onDetach']
FWA = ('FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), '
       '1673 (onPause), 1858 (onStop), 1909 (onDestroy)')
FWS = 'FW-SRC core/java/android/app/Service.java:343 (onCreate), 515 (onDestroy)'
out = []
for r in scan:
    if r['base_kind'] not in COMP:
        continue
    simple = r['class'].split('.')[-1]
    cbs = []
    cites = []
    for cb in LCB:
        n = '%s.%s' % (simple, cb)
        if n in nodes:
            cbs.append(cb)
            cites.append(nodes[n]['source_file'] + ':' + (nodes[n]['decl_line'] or '?'))
    if not cbs:
        continue
    rel = r['file']
    kind = r['base_kind']
    if kind in ('Activity', 'AppCompatActivity', 'FragmentActivity', 'PreferenceActivity'):
        fw = FWA
    elif kind == 'Service':
        fw = FWS
    elif kind in ('Fragment', 'DialogFragment'):
        fw = 'INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read)'
    else:
        fw = 'INFERRED system calls this callback in order (framework source not read for this component)'
    ev = fw + '; SRC ' + ', '.join(cites)
    out.append((simple, cbs, ev, kind))
for simple, cbs, ev, kind in out:
    print('for cb, lsrc in lc_chain(%r, %r):' % (simple, tuple(cbs)))
    print("    e(lsrc, %r + '.' + cb, 'LIFECYCLE', 'lifecycle callback of %s (%s)', evidence=%r)" % (simple, simple, kind, ev))
    print()
