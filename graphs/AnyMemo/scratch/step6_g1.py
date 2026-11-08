"""Step 6 group 1: constructor lifecycle shortcut. Scratch script (deleted at the end)."""
import re
P = 'graphs/AnyMemo/graph_def.py'
src = open(P, encoding='utf-8').read()
L = src.split('\n')
HELPER_ANCHOR = '# ================================================================== A. helpers, FW citations, gates'
assert src.count(HELPER_ANCHOR) == 1
HELPER = '''# Lifecycle order for the edges that start at a constructor (X.<init>). The system creates the object and then
# calls its first callback: onAttach for a fragment (when the class has one), otherwise onCreate. Every later
# callback is reached from onCreate, which the framework calls before any other callback of the class, so no
# route goes from the constructor straight to a later callback. onOptionsItemSelected is reached from
# onCreateOptionsMenu when the class also overrides it (the menu is built before a menu item can be chosen).
def lc_chain(cls, cbs):
    has = tuple(cbs)
    first = 'onAttach' if 'onAttach' in has else ('onCreate' if 'onCreate' in has else None)
    out = []
    for cb in has:
        if cb == first or first is None:
            s = cls + '.<init>'
        elif cb == 'onCreate':
            s = cls + '.onAttach'
        elif cb == 'onOptionsItemSelected' and 'onCreateOptionsMenu' in has:
            s = cls + '.onCreateOptionsMenu'
        else:
            s = cls + '.onCreate'
        out.append((cb, s))
    return out


'''
L_hdrs = [251, 361, 509, 568, 597, 617, 636, 694, 715, 744, 772, 835, 913, 1081, 1179]  # 1-based 'for cb in' lines
pat = re.compile(r"^    e\('(\w+)\.<init>', '\1\.' \+ cb, 'LIFECYCLE'")
done = []
for h in sorted(L_hdrs, reverse=True):
    hi = h - 1
    hdr = L[hi]
    assert hdr.startswith('for cb in (') and hdr.endswith('):'), (h, hdr)
    body = L[hi + 1]
    m = pat.match(body)
    assert m, (h, body[:120])
    cls = m.group(1)
    tup = hdr[len('for cb in '):-1]
    L[hi] = "for cb, lsrc in lc_chain('%s', %s):" % (cls, tup)
    L[hi + 1] = body.replace("e('%s.<init>', " % cls, 'e(lsrc, ', 1)
    done.append((h, cls))

# Flipable / TwoFields card fragments: loop at 1520-1522 (two classes in one loop body)
i = 1520 - 1
assert L[i] == "for cb in ('onCreate', 'onCreateView'):", L[i]
assert L[i + 1].startswith("    e('FlipableCardFragment.<init>', 'FlipableCardFragment.' + cb, 'LIFECYCLE'"), L[i + 1][:80]
assert L[i + 2].startswith("    e('TwoFieldsCardFragment.<init>', 'TwoFieldsCardFragment.' + cb, 'LIFECYCLE'"), L[i + 2][:80]
f_body = L[i + 1].replace("e('FlipableCardFragment.<init>', ", 'e(lsrc, ', 1)
t_body = L[i + 2].replace("e('TwoFieldsCardFragment.<init>', ", 'e(lsrc, ', 1)
L[i:i + 3] = [
    "for cb, lsrc in lc_chain('FlipableCardFragment', ('onCreate', 'onCreateView')):",
    f_body,
    "for cb, lsrc in lc_chain('TwoFieldsCardFragment', ('onCreate', 'onCreateView')):",
    t_body,
]
src = '\n'.join(L)

# direct lines (exact text, expected count 1 each)
DIRECT = [
    ("e('AMApplication.<init>', 'AMApplication.onCreate', 'LIFECYCLE'",
     "e('AMApplication.attachBaseContext', 'AMApplication.onCreate', 'LIFECYCLE'"),
    ("e('QACardActivity.<init>', 'QACardActivity.onDestroy', 'LIFECYCLE'",
     "e('QACardActivity.onCreate', 'QACardActivity.onDestroy', 'LIFECYCLE'"),
    ("e('GradeButtonsFragment.<init>', 'GradeButtonsFragment.onDetach', 'LIFECYCLE'",
     "e('GradeButtonsFragment.onCreate', 'GradeButtonsFragment.onDetach', 'LIFECYCLE'"),
    ("e('CardPlayerActivity.<init>', 'CardPlayerActivity.onSaveInstanceState', 'LIFECYCLE'",
     "e('CardPlayerActivity.onCreate', 'CardPlayerActivity.onSaveInstanceState', 'LIFECYCLE'"),
]
for old, new in DIRECT:
    assert src.count(old) == 1, old
    src = src.replace(old, new)

assert src.count(HELPER_ANCHOR) == 1
src = src.replace(HELPER_ANCHOR, HELPER + HELPER_ANCHOR)
open(P, 'w', encoding='utf-8').write(src)
print('loops changed:', len(done), sorted(done))
print('direct changed:', len(DIRECT), '+ card fragments block')
