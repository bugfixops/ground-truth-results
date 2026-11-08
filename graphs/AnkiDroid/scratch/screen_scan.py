import os, re, sys
ROOT = 'final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java'
decl = re.compile(r'^\s*(?:(?:public|private|protected|static|final|abstract)\s+)*(class|interface|enum)\s+(\w+)([^{;]*)\{', re.M)
classes = {}
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if not f.endswith('.java'):
            continue
        p = os.path.join(dp, f)
        txt = open(p, encoding='utf-8', errors='replace').read()
        pkg = re.search(r'^package\s+([\w.]+);', txt, re.M)
        pkg = pkg.group(1) if pkg else ''
        for m in decl.finditer(txt):
            name = m.group(2)
            if name != f[:-5]:
                continue
            hdr = re.sub(r'<[^{]*?>', '', m.group(3) or '')
            em = re.search(r'extends\s+([\w.]+)', hdr)
            ext = em.group(1) if em else ''
            classes[pkg + '.' + name] = (ext, p, txt[:m.start()].count('\n') + 1)
ANDROID = {'Activity': 'android.app.Activity', 'Fragment': 'android.app.Fragment', 'Service': 'android.app.Service',
           'BroadcastReceiver': 'android.content.BroadcastReceiver', 'ContentProvider': 'android.content.ContentProvider',
           'Application': 'android.app.Application', 'AppWidgetProvider': 'android.appwidget.AppWidgetProvider',
           'IntentService': 'android.app.IntentService', 'DialogFragment': 'android.app.DialogFragment',
           'AppCompatActivity': 'androidx.appcompat.app.AppCompatActivity', 'ListActivity': 'android.app.ListActivity',
           'PreferenceActivity': 'android.preference.PreferenceActivity', 'FragmentActivity': 'android.support.v4.app.FragmentActivity'}
def resolve(full, ext, pkg, seen=()):
    simple = ext.split('.')[-1]
    cand = pkg + '.' + simple
    if cand in classes:
        return cand
    for k in classes:
        if k.endswith('.' + simple) and k not in seen:
            return k
    return None
def base_kind(full, depth=0):
    if depth > 12:
        return 'loop'
    ext, p, _ = classes[full]
    simple = ext.split('.')[-1] if ext else ''
    if simple in ANDROID or ext.startswith('android.') or ext.startswith('androidx.') or ext.startswith('com.google'):
        return simple or ext
    if not ext:
        return ''
    pkg = full.rsplit('.', 1)[0]
    r = resolve(full, ext, pkg)
    if r is None:
        return 'UNRESOLVED:' + ext
    return base_kind(r, depth + 1)
rows = []
for full in sorted(classes):
    ext, p, line = classes[full]
    if not ext:
        continue
    kind = base_kind(full)
    rows.append((full, kind, ext, p.replace(ROOT + '/', ''), line))
out = open('graphs/AnkiDroid/scratch/screen_scan.tsv', 'w')
out.write('class\tbase_kind\textends\tfile\tline\n')
for r in rows:
    out.write('\t'.join(str(x) for x in r) + '\n')
out.close()
import collections
print('classes with extends:', len(rows))
print(collections.Counter(r[1] for r in rows).most_common())
