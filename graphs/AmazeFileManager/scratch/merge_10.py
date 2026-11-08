import ast
import os
import sys

G = 'graphs/AmazeFileManager/scratch/graph_def_before_finish_10.py'
D = 'graphs/AmazeFileManager/scratch/decisions/'
CAND = 'graphs/AmazeFileManager/scratch/graph_def_candidate.py'
BATCHES = [b for b in ['out_1.py', 'out_2.py', 'out_3.py', 'out_0.py'] if os.path.exists(D + b)]

STALE_SRC = {'MainFragment.showProperties', 'AndroidIntent.getParcelableExtra',
             'AndroidIntent.putParcelableExtra', 'AppBar.initSearchView', 'AndroidAnimator.addListener',
             'AndroidPreferenceInflater.inflate', 'AndroidPreference.onBindView'}
STALE_PAIRS = {('StreamSource.availableExact', 'RandomAccessStream.availableExact'),
               ('S_PARCEL_read', 'DatapointParcelable$1.createFromParcel'),
               ('S_PARCEL_read', 'DatapointParcelable$1.newArray')}
REMOVE_U = {'CustomNavigationView.onSaveInstanceState', 'CustomNavigationView.onRestoreInstanceState',
            'CustomNavigationView.isNavigationViewSavedStateMissing', 'PasteHelper$1.createFromParcel'}
SAVED = 'CustomNavigationView$SavedState'

NEW_SECTION = '''
# --- labelling run 2026-10-29: PasteHelper CREATOR is reached through the saved activity state ---
ENV_PASTE_RECREATE = env_text('the system recreates MainActivity with its saved state after a configuration change or process restore', ('system_event',))
NEED_PASTE_OP = state_text('A copy or cut operation is pending (MainActivity holds a PasteHelper)', ('session',))

e('ItemPopupMenu.onMenuItemClick', 'PasteHelper.<clinit>', 'CALL',
  'the first new PasteHelper(...) in the copy or cut menu item initializes the class, which runs the static initializer',
  evidence='SRC ui/ItemPopupMenu.java:103-104 PasteHelper pasteHelper = new PasteHelper(op, ...)')

e('PasteHelper.<clinit>', 'PasteHelper$1.<init>', 'CALL',
  'the static initializer constructs the anonymous Parcelable.Creator assigned to CREATOR',
  evidence='SRC filesystem/PasteHelper.java:42 public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {')

e('MainActivity.onSaveInstanceState', 'PasteHelper.writeToParcel', 'FRAMEWORK',
  'onSaveInstanceState puts the pending PasteHelper into outState; the Bundle parcels it through writeToParcel when the state is saved',
  needs_state=NEED_PASTE_OP,
  evidence='SRC activities/MainActivity.java:1077-1078 if(pasteHelper != null) outState.putParcelable(PASTEHELPER_BUNDLE, pasteHelper); INFERRED Bundle parcels the value on save')

e('MainActivity$1.onPostExecute', 'PasteHelper$1.createFromParcel', 'FRAMEWORK',
  'after a recreate with a saved state, the callback reads PASTEHELPER_BUNDLE; Bundle.getParcelable unparcels the PasteHelper through CREATOR.createFromParcel',
  needs_state=NEED_PASTE_OP, env=ENV_PASTE_RECREATE,
  evidence='SRC activities/MainActivity.java:425 pasteHelper = savedInstanceState.getParcelable(PASTEHELPER_BUNDLE); INFERRED Bundle.getParcelable calls CREATOR.createFromParcel')
'''


def e_pair(st):
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        a = st.value.args
        if len(a) >= 2 and isinstance(a[0], ast.Constant) and isinstance(a[1], ast.Constant):
            return (a[0].value, a[1].value)
    return None


def u_key(st):
    if (isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Subscript)
            and isinstance(st.targets[0].value, ast.Name) and st.targets[0].value.id == 'UNREACHABLE'
            and isinstance(st.targets[0].slice, ast.Constant)):
        return st.targets[0].slice.value
    return None


batch_e, batch_u, seen_pairs, seen_keys, rejected, other = [], [], set(), set(), [], []
for b in BATCHES:
    bsrc = open(D + b, encoding='utf-8').read()
    for st in ast.parse(bsrc).body:
        p = e_pair(st)
        if p:
            if p[0].startswith(SAVED) or p[1].startswith(SAVED):
                rejected.append((b, p))
                continue
            if p in seen_pairs:
                continue
            seen_pairs.add(p)
            batch_e.append(ast.get_source_segment(bsrc, st))
            continue
        k = u_key(st)
        if k is not None:
            if k in seen_keys:
                other.append((b, 'duplicate UNREACHABLE key ' + k))
                continue
            seen_keys.add(k)
            batch_u.append(ast.get_source_segment(bsrc, st))
            continue
        other.append((b, ast.get_source_segment(bsrc, st)[:80]))

gsrc = open(G, encoding='utf-8').read()
glines = gsrc.split('\n')
gtree = ast.parse(gsrc)

delete = set()
deleted_e = deleted_u = 0


def mark(st):
    for i in range(st.lineno, st.end_lineno + 1):
        delete.add(i)


for st in gtree.body:
    p = e_pair(st)
    if p:
        s, d = p
        if (s in STALE_SRC or s == 'MainFragment.showProperties' or d == 'MainFragment.showProperties'
                or p in STALE_PAIRS or s.startswith(SAVED) or d.startswith(SAVED) or p in seen_pairs):
            mark(st)
            deleted_e += 1
        continue
    k = u_key(st)
    if k in REMOVE_U:
        mark(st)
        deleted_u += 1

saved_init = [st for st in gtree.body if u_key(st) == SAVED + '.<init>']
if len(saved_init) == 2:
    first, second = saved_init
    glines[first.lineno - 1] = glines[first.lineno - 1].replace(
        "UNREACHABLE['%s.<init>']" % SAVED, "UNREACHABLE['%s.<init>(Parcelable)']" % SAVED)
    glines[second.lineno - 1] = glines[second.lineno - 1].replace(
        "UNREACHABLE['%s.<init>']" % SAVED, "UNREACHABLE['%s.<init>(Parcel)']" % SAVED)
else:
    sys.exit('expected 2 SavedState.<init> UNREACHABLE keys, found %d' % len(saved_init))

kind_changed = 0
for st in gtree.body:
    k = u_key(st)
    if k and k.startswith(SAVED) and st.lineno not in delete:
        for i in range(st.lineno - 1, st.end_lineno):
            if "'framework_never_calls'" in glines[i]:
                glines[i] = glines[i].replace("'framework_never_calls'", "'closed_by_api_level'")
                kind_changed += 1
                break

out = [line for i, line in enumerate(glines, start=1) if i not in delete]
text = '\n'.join(out).rstrip('\n') + '\n' + NEW_SECTION
text += '\n' + '\n'.join(batch_e) + '\n\n' + '\n'.join(batch_u) + '\n'
open(CAND, 'w', encoding='utf-8').write(text)

print('deleted e():', deleted_e, 'deleted UNREACHABLE:', deleted_u, 'kind changed:', kind_changed)
print('batch edges appended:', len(batch_e), 'batch UNREACHABLE appended:', len(batch_u))
print('rejected:', rejected)
print('other statements:', other)
