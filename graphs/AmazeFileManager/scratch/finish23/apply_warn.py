import ast, shutil, sys

W = '/Users/darshan/Desktop/yang/work'
G = W + '/graphs/AmazeFileManager'
S = G + '/scratch/finish22'
GD = G + '/graph_def.py'
BACKUP = G + '/scratch/graph_def_before_finish_23.py'
APPLY = '--apply' in sys.argv

text = open(GD, encoding='utf-8').read()
lines = text.split('\n')
tree = ast.parse(text)
parents = {}
for p in ast.walk(tree):
    for c in ast.iter_child_nodes(p):
        parents[c] = p

E = {}
with open(S + '/edge_lines.tsv', encoding='utf-8') as f:
    next(f)
    for ln in f:
        ln = ln.rstrip('\n')
        if not ln:
            continue
        p = ln.split('\t', 8)
        E[p[0]] = dict(id=p[0], line=int(p[1]) if p[1] else None, auto=p[2] == '1',
                       src=p[3], dst=p[4], kind=p[5], sv=p[6], dv=p[7])
ROWS = []
with open(S + '/warn_table.tsv', encoding='utf-8') as f:
    h = next(f).rstrip('\n').split('\t')
    for ln in f:
        ln = ln.rstrip('\n')
        if ln:
            ROWS.append(dict(zip(h, ln.split('\t', 10))))

DEAD_MANUAL = [
    'E5de0752d', 'Ebc4d990c', 'Ef5d35a30', 'E75d78285',
    'Ea8a67983', 'Ef9f46f8e',
    'E0af3c565', 'E0af3c565-2', 'Eae8b1fc2',
    'E883af3e5', 'E883af3e5-2', 'Eb96a0791',
    'E648eb6d4', 'E648eb6d4-2', 'E27068abf',
    'E9a128e89', 'E9a128e89-2',
    'E0bbd70e0', 'Ef88bbe26', 'Eec39dbe5', 'Eba934020',
    'E46d3891b', 'E46d3891b-2', 'Ed6e4e1af', 'Ed6e4e1af-2',
    'Eab7f7c82', 'Eab7f7c82-2', 'Ebc1ce656', 'Ebc1ce656-2', 'Ee18437c9', 'Ee18437c9-2',
    'Effeac82b', 'E552ec35a', 'Ef28cfe83', 'Ef3192b4c', 'E963504e1', 'E73e754e6', 'Ec8923206',
    'Ea7b2e71c', 'Ef2580ce7', 'E9e955ede', 'Efa992ac0',
    'E12c1ae70', 'E335d3a15', 'Eaa0524fc', 'Ebb276b0a', 'E10c23b0f',
    'E0840c206', 'E3a4185c8', 'E613d2525', 'E3a320209',
]
WRONG = [
    'Ef3948c79', 'E403e7ab6', 'Ed21a35d9', 'E60dce3ed', 'E3c25eb66',
    'E7917e349', 'Efdd8c2fd', 'E91905db9', 'E0fe77960', 'E0fe77960-2',
]
extra = [e['id'] for e in E.values() if e['src'] == 'AppListLoader.onStopLoading'
         and e['dst'] == 'InterestingConfigChange.recycle' and e['line'] == 16387]
assert len(extra) == 1, extra
WRONG += extra

ROUTE = [
    'AES256SHA256Decoder.<init>', 'AES256SHA256Decoder.decode',
    'AppConfig.lambda$toast$0', 'AppConfig.lambda$toast$1',
    'AppDataParcelable.<clinit>',
    'AppListLoader.onCanceled', 'AppListLoader.onReleaseResources', 'AppListLoader.onStopLoading',
    'Archive.<init>', 'BindPair.<init>', 'BoundedFileChannelInputStream.read(int)',
    'CloudHandler.onCreate', 'CloudHandler.onUpgrade', 'CloudIconDataFetcher.cancel',
    'CompressedObjectParcelable$1.<init>', 'Coders$DeflateDecoder.<clinit>',
    'ColorPref.checkCustomization', 'ColorPref.invalidateColorPreference',
    'FileUtils.fileToContentUri(Context,String,boolean,String)', 'FileUtils.scanFile(Uri,Context)',
    'LZMADecoder.getDictionarySize', 'MediaStoreHack.<clinit>',
    'PasteHelper.<init>(Parcel)', 'PasteHelper.writeToParcel',
    'PermissionsActivity.isGranted', 'RarDecompressor.realRelativeDirectory',
    'Streamer.getNameFromPath', 'Streamer.setStreamSrc',
]
AUTO_DEAD_EXACT = {'Statvfs$Response.getFileSystemId', 'HybridFile$2.<init>',
                   'CustomNavigationView$SavedState.<clinit>',
                   'CustomNavigationView$SavedState.<init>(Parcelable)'}


def is_glide(m):
    return m.startswith('GlideOptions.') or m.startswith('GlideRequest.')


def call_stmt(eid):
    ed = E[eid]
    L = ed['line']
    cands = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name) and node.value.func.id in ('e', 'gui')
                and node.lineno <= L <= node.end_lineno):
            a = node.value.args
            if (len(a) >= 2 and isinstance(a[0], ast.Constant) and isinstance(a[1], ast.Constant)
                    and a[0].value == ed['src'] and a[1].value == ed['dst']):
                cands.append(node)
    if len(cands) != 1:
        raise SystemExit('edge %s line %s: %d candidates' % (eid, L, len(cands)))
    node = cands[0]
    if node.col_offset != 0:
        raise SystemExit('edge %s line %s is not a top-level statement' % (eid, L))
    return node


def is_unreach_dict(d):
    p = parents.get(d)
    if isinstance(p, (ast.Assign, ast.AnnAssign)):
        t = p.targets[0] if isinstance(p, ast.Assign) else p.target
        return isinstance(t, ast.Name) and t.id.startswith('UNREACHABLE')
    if isinstance(p, ast.Call) and isinstance(p.func, ast.Attribute) and p.func.attr == 'update':
        v = p.func.value
        return isinstance(v, ast.Name) and v.id.startswith('UNREACHABLE')
    return False


def entry_sites(name):
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            t = node.targets[0]
            if (isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name)
                    and t.value.id == 'UNREACHABLE' and isinstance(t.slice, ast.Constant)
                    and t.slice.value == name):
                if node.col_offset != 0:
                    raise SystemExit('entry %s not top-level' % name)
                out.append(('stmt', node.lineno, node.end_lineno))
        if isinstance(node, ast.Dict) and is_unreach_dict(node):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value == name:
                    kl = lines[k.lineno - 1]
                    el = lines[v.end_lineno - 1]
                    if kl.encode('utf-8')[:k.col_offset].strip() != b'':
                        raise SystemExit('entry %s key shares a line' % name)
                    if el.encode('utf-8')[v.end_col_offset:].strip() not in (b'', b','):
                        raise SystemExit('entry %s value shares a line' % name)
                    for k2, v2 in zip(node.keys, node.values):
                        if k2 is k:
                            continue
                        if k.lineno <= k2.lineno <= v.end_lineno or k.lineno <= v2.end_lineno <= v.end_lineno:
                            raise SystemExit('entry %s shares lines with another item' % name)
                    out.append(('item', k.lineno, v.end_lineno))
    return out


dele = set()
log = {'manual': 0, 'wrong': 0, 'route_stmt': 0, 'route_item': 0}
for eid in DEAD_MANUAL + WRONG:
    node = call_stmt(eid)
    dele.update(range(node.lineno, node.end_lineno + 1))
    log['manual' if eid in DEAD_MANUAL else 'wrong'] += 1

route_report = {}
for name in ROUTE:
    sites = entry_sites(name)
    route_report[name] = len(sites)
    for kind, a, b in sites:
        dele.update(range(a, b + 1))
        log['route_stmt' if kind == 'stmt' else 'route_item'] += 1

pairs = set()
for r in ROWS:
    if r['auto'] != '1':
        continue
    m = r['method']
    if is_glide(m) or m in AUTO_DEAD_EXACT:
        ed = E[r['edge_id']]
        pairs.add((ed['src'], ed['dst']))
pairs_sorted = sorted(pairs)

new_lines = [l for i, l in enumerate(lines, 1) if i not in dele]
new_text = '\n'.join(new_lines)
if not new_text.endswith('\n'):
    new_text += '\n'
sup_block = ['# Auto calls from UNREACHABLE callers, or inside SDK 23-28 guards (not API 27): not routes.',
             'sup(']
for a, b in pairs_sorted:
    sup_block.append('    (%r, %r),' % (a, b))
sup_block.append(')')
new_text = new_text + '\n'.join(sup_block) + '\n'

ast.parse(new_text)

print('manual/wrong edges removed:', log['manual'], log['wrong'])
print('route entries removed (stmt/item):', log['route_stmt'], log['route_item'])
missing = [n for n, c in route_report.items() if c == 0]
print('route names with zero entry sites:', missing)
print('sup pairs added:', len(pairs_sorted))
print('lines deleted:', len(dele), 'old', len(lines), 'new', len(new_lines))

if APPLY:
    shutil.copy2(GD, BACKUP)
    open(GD, 'w', encoding='utf-8').write(new_text)
    print('written', GD, 'backup', BACKUP)
else:
    print('dry run; pass --apply to write')
