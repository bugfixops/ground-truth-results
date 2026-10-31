import os, re

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
ROOT = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager'
JAVA_MAIN = ROOT + '/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/'
names = set(__import__('json').load(open(W + '/out/amazefilemanager_trigger_graph.json'))['verdict'].keys())


def find(fn):
    out = []
    for r, _, fs in os.walk(ROOT):
        if fn in fs:
            out.append(os.path.join(r, fn))
    return out


def header_above(lines, n):
    i = n - 1
    pat = re.compile(r'^\s*(public|private|protected|static|final|void|boolean|int|long|String|Intent|\w+\s+\w+\s*\()')
    while i > 0:
        l = lines[i]
        if re.match(r'^\s{0,8}(public|private|protected|static)\b.*\(', l) or re.match(r'^\s{0,8}\w[\w<>\[\], ]*\s+\w+\s*\(.*\)\s*\{?\s*$', l):
            return i + 1, l.strip()[:150]
        i -= 1
    return None, None


def show(path, n, before=0, after=0):
    L = open(path, encoding='utf-8', errors='replace').read().split('\n')
    print('  FILE', path.split('/java/')[-1] if '/java/' in path else path)
    h = header_above(L, n)
    print('  HEADER', h)


print('SEVENZ files', find('SevenZFile.java'))
print('SEVENZ helper call:')
p = JAVA_MAIN + 'asynchronous/asynctasks/SevenZipHelperTask.java'
if os.path.exists(p):
    for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        if 'SevenZFile' in l and 'new' in l: print('  ', i, l.strip()[:150])
else:
    print('  no helper at', p, find('SevenZipHelperTask.java'))
for f, ln in [('FileUtils.java', 613), ('FileUtils.java', 658), ('RootHelper.java', 232), ('RootHelper.java', 327),
              ('RootHelper.java', 228), ('GeneralDialogCreation.java', 1011), ('GeneralDialogCreation.java', 1066),
              ('HybridFile.java', 231), ('FileUtils.java', 244), ('AppConfig.java', 183)]:
    for path in find(f):
        if '/main/' in path and 'AmazeFileManager' in path:
            L = open(path, encoding='utf-8', errors='replace').read().split('\n')
            print('HDR', f, ln, '->', header_above(L, ln))
            break
for path in find('Indicator.java') + find('LruBitmapCache.java') + find('CircularColorsView.java') + find('ColorPickerDialog.java'):
    if '/main/' not in path: continue
    L = open(path, encoding='utf-8', errors='replace').read().split('\n')
    cons = [(i, l.strip()[:120]) for i, l in enumerate(L, 1) if re.search(r'public\s+(Indicator|LruBitmapCache|CircularColorsView|SavedState)\s*\(', l)]
    print('CTOR', path.split('/')[-1], cons)
for pat in [r'new LruBitmapCache\(', r'new Indicator\(', r'IconDataParcelable', r'new SevenZFile\(', r'showSortDialog\(', r'AppConfig\.toast\(']:
    hits = []
    for r, _, fs in os.walk(JAVA_MAIN):
        for fn in fs:
            if fn.endswith('.java'):
                for i, l in enumerate(open(os.path.join(r, fn), encoding='utf-8', errors='replace').read().split('\n'), 1):
                    if re.search(pat, l): hits.append('%s:%d %s' % (fn, i, l.strip()[:110]))
    print('USE', pat, len(hits)); print('\n'.join('   ' + h for h in hits[:6]))
print('VERDICT lambdas scanFile:', sorted(n for n in names if 'lambda$scanFile' in n))
print('VERDICT lambdas getFilesList:', sorted(n for n in names if 'RootHelper' in n and 'getFilesList' in n))
print('VERDICT AppConfig.toast:', sorted(n for n in names if n.startswith('AppConfig.toast')))
print('VERDICT Indicator:', sorted(n for n in names if n.startswith('Indicator.')))
print('VERDICT CircularColorsView:', sorted(n for n in names if n.startswith('CircularColorsView.')))
print('VERDICT HybridFile.length/exists:', sorted(n for n in names if n.startswith('HybridFile.length') or n.startswith('HybridFile.exists')))
