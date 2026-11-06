# W5 decisions (Kiro, self-checked only) for the edges list_library_edges.py prints.
# Usage, from the repo root, on the build BEFORE the W5 edits (ESR_CREATION on is fine):
#   python3 -I graphs/MMEX/scratch/reaudit/w5_decide.py <App>
# Writes graphs/<App>/scratch/reaudit/library_edges.csv and prints the (src, dst, kind) -> via map
# that the app's graph_def.py W5 block applies. The same script is copied into each app's
# scratch/reaudit/. Rules applied (each edge's source was printed; the cited lines are in the CSV):
#   NON_STANDARD when a library or reflection makes the link itself:
#     - the constructor of a class that LayoutInflater or the preference inflater builds from an XML tag;
#     - a data-binding Binding*Impl created by the generated DataBinderMapperImpl;
#     - an Rx subscribe consumer (method reference) that RxJava calls.
#   KEEP (standard or explicit) when the link is:
#     - the Android framework creating a manifest component (activity, receiver, service, provider,
#       backup agent) or a widget/receiver class, even though ActivityThread uses newInstance;
#     - a fragment or dialog lifecycle step after app code created it (new X(), a static newInstance factory);
#     - a framework or support-library callback on an object the app built (adapter getItem, preference
#       listeners the app registered, getSharedPreferences, saveInstanceState, options menus);
#     - a direct app call that only mentions a library in its text (a static newInstance factory, a call
#       that returns an Rx type, an EventBus register in onStart);
#     - an already-classified edge whose callee inherits library through ESR_CREATION (the creation edge
#       is non_standard).
import csv
import glob
import json
import re
import subprocess
import sys

app = sys.argv[1]
S = 'graphs/%s/scratch/reaudit/' % app
listing = '/tmp/w5_listing_%s.csv' % app
subprocess.run([sys.executable, '-I', 'graphs/MMEX/scratch/reaudit/list_library_edges.py', app, listing], check=True,
               stdout=subprocess.DEVNULL)
rows = list(csv.DictReader(open(listing, encoding='utf-8')))

NONSTD = {
    'Aegis': {},
    'AmazeFileManager': {i: 'XML inflation: LayoutInflater or the preference inflater builds this class from its XML tag through the (Context, AttributeSet) constructor (layout or preference XML cited in the evidence)'
                         for i in ('E4b4df74e', 'E2df0c4aa', 'E9ae2b3cb', 'E628d8e3d', 'Ed8aca398', 'E3023962a', 'E6a305bc8',
                                   'Ed7b3c924', 'E7b8e8ce7', 'E5c3e8784', 'Ebeb8fe03', 'E17cc5cb9')},
    'AnkiDroid': {i: 'XML inflation: the preference inflater builds this Preference class from its XML tag through the (Context, AttributeSet) constructor (preference XML cited in the evidence)'
                  for i in ('E319bec48', 'E21f346ef', 'E85911aac', 'Ea555d5e6', 'Ec60a84f3', 'Ee927e695')},
    'LibreTorrent': {},
    'MMEX': {i: 'XML inflation: LayoutInflater builds this view from its XML tag through the (Context, AttributeSet) constructor (layout XML cited in the evidence)'
             for i in ('Ed8d6cd00', 'E280c46e3')},
}
if app == 'LibreTorrent':
    for r in rows:
        if r['src'].endswith('DataBinderMapperImpl.<init>') or 'DataBinderMapperImpl.getDataBinder' in r['src']:
            NONSTD['LibreTorrent'][r['id']] = ('data binding: the generated DataBinderMapperImpl creates the Binding class for the '
                                               'inflated layout (DataBindingUtil.inflate; mapper line cited in the evidence)')
    NONSTD['LibreTorrent']['E4f5f9101'] = 'Rx: subscribe(onNext, this::backupFeedsErrorDialog) - RxJava calls the error consumer (ui/feeds/FeedActivity.java:359-370)'
    NONSTD['LibreTorrent']['E15eca4bb'] = 'Rx: subscribe(onComplete, this::restoreFeedsBackupErrorDialog) - RxJava calls the error consumer (ui/feeds/FeedActivity.java:346-356)'


def keep_reason(r):
    t, k, s, d = r['text'], r['kind'], r['src'], r['dst']
    if k == 'ENTRY' or (k in ('LIFECYCLE', 'FRAMEWORK') and re.search(r'ActivityThread|BackupAgent|ContentProvider|receiver|JobIntentService', t)):
        return 'the Android framework creates a manifest component (ActivityThread); standard component start, not app reflection'
    if k == 'INTENT':
        return 'an Intent start of an app activity; the framework creates the activity (standard)'
    if k == 'LIFECYCLE':
        return 'a lifecycle step on an object the app created (new or a static newInstance factory); standard lifecycle'
    if k == 'GUI':
        return 'a tap dispatched to a listener or callback the app registered; standard GUI dispatch (an object only XML creates gets library through ESR_CREATION)'
    if k == 'REGISTER':
        return 'the app registers its own listener (setOn...Listener); explicit'
    if k == 'CALL':
        return 'a direct app call (the text names a library type or a static newInstance factory only); explicit'
    if k == 'ENTERS':
        return 'page entry'
    return 'a framework or support-library callback on an object the app built (adapter, preference store, saved state, options menu); standard'


out = []
for r in rows:
    via = NONSTD[app].get(r['id'])
    ev = re.findall(r'SRC [^;]+', r['text'])
    out.append([r['id'], r['kind'], r['edge_class'], r['src'], r['dst'], r['mechanism'],
                'NON_STANDARD' if via else 'KEEP', via or keep_reason(r), (ev[0][:200] if ev else ''), 'self'])
missing = set(NONSTD[app]) - {r['id'] for r in rows}
assert not missing, missing
with open(S + 'library_edges.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['id', 'kind', 'class_before', 'src', 'dst', 'mechanism', 'decision', 'reason or via', 'evidence', 'checked_by'])
    w.writerows(out)
print('%s: %d listed, NON_STANDARD %d, KEEP %d' % (app, len(out), sum(1 for o in out if o[6] == 'NON_STANDARD'),
                                                  sum(1 for o in out if o[6] == 'KEEP')))
print('_W5_NONSTD = {')
for o in out:
    if o[6] == 'NON_STANDARD':
        print('    (%r, %r, %r):\n        %r,' % (o[3], o[4], o[1], o[7]))
print('}')
