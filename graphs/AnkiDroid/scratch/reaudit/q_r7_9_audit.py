"""1-in-3 audit of the Q-R7-9 entries (AnkiDroid). Run from the repo root.
Samples every third item (sorted) of: the 25 removed S_ENTRY edges, the 53 UNREACHABLE entries, the 65 sup() pairs.
Checks, re-printed from source and the built graph:
  removed edge : not in the new graph; the old edge (git HEAD~ graph json) was S_ENTRY -> api method; the target is now
                 UNREACHABLE no_trigger_in_app.
  UNREACHABLE  : the method's simple name has no occurrence in app code outside api/ (grep), and the class name neither;
                 the label kind is no_trigger_in_app; no edge into it remains in the graph.
  sup pair     : the pair is in auto_calls.json as a CALL, the source is UNREACHABLE in the new graph, and the edge is
                 not in the new graph.
"""
import json, os, re, subprocess, sys

ROOT = 'final_java_only/AnkiDroid/app/AnkiDroid-#4200'
new = json.load(open('graphs/AnkiDroid/out/ankidroid_trigger_graph.json'))
old = json.loads(subprocess.check_output(['git', 'show', 'd0ef178c:graphs/AnkiDroid/out/ankidroid_trigger_graph.json']))
labels = new['labels']
new_pairs = {(e['src'], e['dst']) for e in new['edges']}
new_dst = {e['dst'] for e in new['edges']}
ns = {}
src = open('graphs/AnkiDroid/graph_def_mod/04.py', encoding='utf-8').read()
methods = eval(re.search(r'_Q_R7_9_METHODS = (\[.*?\n\])', src, re.S).group(1))
sups = eval('[' + re.search(r'sup\((\(.*?\))\)\s*$', src, re.S).group(1) + ']')
removed = sorted((e['id'], e['dst']) for e in old['edges'] if e['src'] == 'S_ENTRY' and e['dst'].startswith('AddContentApi'))
auto = json.load(open('graphs/AnkiDroid/auto_calls.json'))
auto_s = json.dumps(auto)

app_files = []
for d, _, fs in os.walk(ROOT):
    if os.sep + 'api' + os.sep in d + os.sep and d.startswith(os.path.join(ROOT, 'api')):
        continue
    for f in fs:
        if f.endswith(('.java', '.kt', '.xml', '.gradle')):
            app_files.append(os.path.join(d, f))
texts = {p: open(p, encoding='utf-8', errors='replace').read() for p in app_files}


def grep(word):
    return sorted(p[len(ROOT) + 1:] for p, t in texts.items() if re.search(r'\b%s\b' % re.escape(word), t))


def simple(m):
    name = m.split('(')[0].rsplit('.', 1)[1]
    cls = m.split('(')[0].rsplit('.', 1)[0].split('.')[-1].split('$')[-1]
    return name, cls


print('# Q-R7-9 1-in-3 audit (AnkiDroid), by Kiro, 2026-11-09. App files searched outside api/: %d' % len(app_files))
print('# grep for the client classes outside api/: AddContentApi %s; NoteInfo %s; com.ichi2.anki.api %s'
      % (grep('AddContentApi') or 'none', grep('NoteInfo') or 'none',
         sorted(p[len(ROOT) + 1:] for p, t in texts.items() if 'com.ichi2.anki.api' in t) or 'none'))
bad = 0
print('\n## removed S_ENTRY edges: %d, sampled %d' % (len(removed), len(removed[::3])))
for i, d in removed[::3]:
    ok = ('S_ENTRY', d) not in new_pairs and (labels.get(d, {}).get('unreachable') or {}).get('kind') == 'no_trigger_in_app'
    bad += not ok
    print('%s S_ENTRY -> %s : gone from graph %s; target %s -> %s' % (
        i, d, ('S_ENTRY', d) not in new_pairs, (labels.get(d, {}).get('unreachable') or {}).get('kind'), 'OK' if ok else 'MISMATCH'))
ms = sorted(methods)
print('\n## UNREACHABLE entries: %d, sampled %d' % (len(ms), len(ms[::3])))
for m in ms[::3]:
    name, cls = simple(m)
    kind = (labels.get(m, {}).get('unreachable') or {}).get('kind')
    hits = grep(name) if not name.startswith('<') else []
    chits = grep(cls)
    if m.startswith('api.Utils'):
        # api.Utils is package-private (Utils.java:32 "class Utils"): only code in package com.ichi2.anki.api can name it.
        # The app has its own com.ichi2.libanki.Utils, so keep only hits that are in, or import from, that package.
        chits = [p for p in chits if 'com.ichi2.anki.api' in texts[os.path.join(ROOT, p)]]
    ok = kind == 'no_trigger_in_app' and m not in new_dst and not chits
    bad += not ok
    print('%s : kind %s; incoming edges %s; class name %s outside api/: %s; method name %s outside api/: %s -> %s' % (
        m, kind, m in new_dst, cls, chits or 'none', name, (hits[:4] + (['...'] if len(hits) > 4 else [])) or 'none',
        'OK' if ok else 'MISMATCH'))
ss = sorted(sups)
print('\n## sup pairs: %d, sampled %d' % (len(ss), len(ss[::3])))
for s, d in ss[::3]:
    sk = (labels.get(s, {}).get('unreachable') or {}).get('kind')
    in_auto = ('"%s"' % s in auto_s) and ('"%s"' % d in auto_s)
    ok = bool(sk) and (s, d) not in new_pairs and in_auto
    bad += not ok
    print('(%s -> %s) : source UNREACHABLE %s; in auto_calls %s; edge gone %s -> %s' % (
        s, d, sk, in_auto, (s, d) not in new_pairs, 'OK' if ok else 'MISMATCH'))
print('\nmismatches: %d' % bad)
