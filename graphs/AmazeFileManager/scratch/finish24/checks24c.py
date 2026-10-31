import json, re

W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
d = json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))
names = sorted(d['verdict'].keys())
GD = open(W + '/graph_def.py', encoding='utf-8').read().split('\n')
ml = json.load(open(W + '/method_list.json'))
ml = ml if isinstance(ml, list) else ml.get('methods', ml)

print('--- verdict names with execute/dismiss/startActivityForResult/onResult/serve/getDialog/setRestartActivity')
for n in names:
    if re.search(r'\.(execute|dismiss|startActivityForResult|onResult|serve|getDialog|setRestartActivity|onPostExecute|onPreferenceClick|afterTextChanged|doInBackground)\b', n):
        print('  ', n)

print('--- graph_def lines with dst startActivityForResult/dismiss/execute/getDialog/setRestartActivity')
for i, l in enumerate(GD, 1):
    if re.search(r"'[^']*\.(startActivityForResult|dismiss|getDialog|setRestartActivity|execute|serve|onResult)'", l):
        print('  ', i, l.strip()[:150])

print('--- method_list ColorPref / SftpConnectDialog / RenameBookmark lambdas / CompressedHelperTask / AsyncTaskResult / SavedState / SevenZFile')
for m in ml:
    c = m.get('class', '')
    s = m.get('short', '')
    if (c.endswith('ColorPref') or c.endswith('SftpConnectDialog') or c.endswith('RenameBookmark') or 'AsyncTaskResult' in c
            or 'SavedState' in c or c.endswith('SevenZFile') or c.endswith('LayoutElementParcelable')):
        if 'lambda' in s or '<init>' in s or c.endswith('SftpConnectDialog') or c.endswith('ColorPref'):
            print('  ', c, s, m.get('desc', '')[:80])

print('--- how S_ sources are defined near line 150-160 and 1410-1425')
for i in list(range(146, 160)) + list(range(1412, 1426)):
    print('  ', i, GD[i - 1].rstrip()[:150])
