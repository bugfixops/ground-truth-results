import os, re, json

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager'
APP = ROOT + '/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/'
W = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager'
names = sorted(json.load(open(W + '/out/amazefilemanager_trigger_graph.json'))['verdict'].keys())


def lines_of(p):
    return open(p, encoding='utf-8', errors='replace').read().split('\n')


def grep_v(rx):
    return [n for n in names if re.search(rx, n)]


print('VERDICT SevenZFile:', grep_v(r'^SevenZFile\.(buildDecodingStream|readHeaders|<init>)'))
print('VERDICT RootHelper:', grep_v(r'^RootHelper\.(getFiles|isDirectory|getFilesList)\b'))
print('VERDICT ColorPickerDialog onSave:', grep_v(r'^ColorPickerDialog\.onSaveInstanceState'))
print('VERDICT ColorPref anon:', grep_v(r'^ColorPref\$'))
print('VERDICT SftpConnectDialog lambdas:', grep_v(r'^SftpConnectDialog\.lambda'))
print('VERDICT GeneralDialogCreation showSort:', grep_v(r'showSortDialog'))
print('VERDICT CompressedHelperTask.<init>:', grep_v(r'^SevenZipHelperTask\.'))

print('--- SevenZFile 259-300')
L = lines_of(APP.replace('com/amaze/filemanager/', '') + '../../../../../../../')  if False else None
p = ROOT + '/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java'
if not os.path.exists(p):
    import glob
    c = glob.glob(ROOT + '/**/sevenz/SevenZFile.java', recursive=True)
    p = c[0] if c else p
L = lines_of(p)
for i in range(259, 300):
    if L[i - 1].strip():
        print('  %d %s' % (i, L[i - 1].rstrip()[:130]))

print('--- RootHelper parseName / getFiles call sites')
p = APP + 'filesystem/RootHelper.java'
for i, l in enumerate(lines_of(p), 1):
    if re.search(r'parseName\(|canListFiles\(|getFilesList\(|getFiles\(|isDirectory\(String', l):
        print('  %d %s' % (i, l.strip()[:140]))

print('--- GeneralDialogCreation 1056-1085')
p = APP + 'ui/dialogs/GeneralDialogCreation.java'
for i in range(1056, 1085):
    print('  %d %s' % (i, lines_of(p)[i - 1].rstrip()[:140]))

print('--- SftpConnectDialog 120-232 structure (lambda/new/execute/{ lines)')
p = APP + 'ui/dialogs/SftpConnectDialog.java'
for i, l in enumerate(lines_of(p), 1):
    if 120 <= i <= 232 and re.search(r'->|execute|new [A-Z]\w+\(|onPositive|onNegative|onNeutral|setOnClick|public void|void \w+\(', l):
        print('  %d %s' % (i, l.strip()[:130]))

print('--- ColorPref 136-186 and 218-230')
p = APP + 'fragments/preference_fragments/ColorPref.java'
for i, l in enumerate(lines_of(p), 1):
    if (136 <= i <= 186 or 218 <= i <= 230) and re.search(r'->|new [A-Z]\w+|setRestart|onNeutral|onPositive|onNegative|public|private|void', l):
        print('  %d %s' % (i, l.strip()[:130]))
