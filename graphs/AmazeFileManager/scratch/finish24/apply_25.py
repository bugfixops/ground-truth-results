import difflib
import re
import sys

PATH = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
APPLY = '--apply' in sys.argv
GD = open(PATH, encoding='utf-8').read().split('\n')
ORIG = list(GD)


def dd(line):
    s = re.sub(r"'[^']*'", '', line)
    return s.count('(') - s.count(')')


def span(n):
    i = n - 1
    assert GD[i].startswith('e('), (n, GD[i][:80])
    d, j = 0, i
    while True:
        d += dd(GD[j])
        if d <= 0:
            return i, j
        j += 1
        assert j < len(GD), n


def sub(n, old, new):
    assert GD[n - 1].count(old) == 1, (n, old, GD[n - 1][:140])
    GD[n - 1] = GD[n - 1].replace(old, new)


def resub(n, pat, new):
    s, k = re.subn(pat, new, GD[n - 1])
    assert k == 1, (n, pat, GD[n - 1][:140])
    GD[n - 1] = s


def remove(n):
    i, j = span(n)
    del GD[i:j + 1]


def insert(n, text):
    i, j = span(n)
    GD[j + 1:j + 1] = text.split('\n') + ['']


SUBS = [
    (640, "'AppConfig.toast'", "'AppConfig.toast(Context,int)'"),
    (4296, "'AppConfig.toast'", "'AppConfig.toast(Context,int)'"),
    (918, "'FileUtils.openFile', 'DatabaseViewerActivity.<init>'",
     "'FileUtils.openFile(File,MainActivity,SharedPreferences)', 'DatabaseViewerActivity.<init>'"),
    (1489, "'ColorPickerDialog$SavedState.<init>', 'ColorPickerDialog$SavedState.<clinit>'",
     "'ColorPickerDialog.onSaveInstanceState', 'ColorPickerDialog$SavedState.<clinit>'"),
    (1491, "evidence='SRC ColorPickerDialog.java:253')", "evidence='SRC ColorPickerDialog.java:256')"),
    (3920, "'SevenZFile.<init>'", "'SevenZFile.readHeaders'"),
    (3921, "'SevenZFile.<init>'", "'SevenZFile.buildDecodingStream'"),
    (3922, "'SevenZFile.<init>'", "'SevenZFile.buildDecodingStream'"),
    (3923, "'SevenZFile.<init>'", "'SevenZFile.buildDecodingStream'"),
    (3930, "'SevenZFile.<init>'", "'SevenZFile.<init>(File,char[])'"),
    (6180, "'SevenZFile.<init>'", "'SevenZFile.readHeaders'"),
    (7381, "'RootHelper.getFilesList'", "'RootHelper.getFiles'"),
    (7395, "'RootHelper.getFilesList'", "'RootHelper.getFiles'"),
    (7843, "'GeneralDialogCreation.showSortDialog'", "'GeneralDialogCreation.showSortDialog(AppsListFragment,AppTheme)'"),
    (7843, "'item selection callback in sort dialog'", "'sort dialog button callback'"),
    (7845, "'GeneralDialogCreation.showSortDialog'", "'GeneralDialogCreation.showSortDialog(AppsListFragment,AppTheme)'"),
    (7845, "'item selection callback in sort dialog'", "'sort dialog button callback'"),
    (8985, "'HybridFile.getName'", "'HybridFile.getName()'"),
    (8993, "'HybridFile.isDirectory'", "'HybridFile.isDirectory()'"),
    (9015, "'HybridFile.length'", "'HybridFile.length()'"),
    (9033, "'FileUtils.scanFile', 'HybridFile.exists()'", "'FileUtils.scanFile(Context,HybridFile[])', 'HybridFile.exists()'"),
    (9624, "'Indicator.<init>'", "'Indicator.<init>(Context,AttributeSet,int)'"),
    (9655, "'Indicator.<init>'", "'Indicator.<init>(Context,AttributeSet,int)'"),
    (10062, "'LruBitmapCache.<init>'", "'LruBitmapCache.<init>()'"),
    (10066, "'LruBitmapCache.<init>'", "'LruBitmapCache.<init>()'"),
    (10070, "'LruBitmapCache.<init>'", "'LruBitmapCache.<init>()'"),
    (11334, "'SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.execute', 'CALL',",
     "'SftpConnectDialog.lambda$onCreateDialog$9', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC',"),
    (11336, "SRC SftpConnectDialog.java:230 }).execute();", "SRC SftpConnectDialog.java:229 }).execute();"),
    (11349, "'GetSshHostFingerprintTask.execute', 'CALL',", "'GetSshHostFingerprintTask.doInBackground', 'ASYNC',"),
    (11351, "SRC SftpConnectDialog.java:198 }).execute();", "SRC SftpConnectDialog.java:199 }).execute();"),
    (11464, "'PemToKeyPairTask.execute', 'CALL',", "'PemToKeyPairTask.doInBackground', 'ASYNC',"),
    (12581, "'ColorPref.lambda$onCreate$0(Object,Preference,int,Object)'", "'ColorPref$1.onNeutral'"),
    (12582, "'ColorPref color change callback sets restart activity flag'",
     "'ColorPref neutral button sets restart activity flag'"),
    (12585, "'ColorPref.lambda$onCreate$1(Preference)'", "'ColorPref.lambda$loadSection1$1'"),
    (12586, "'ColorPref icon color change callback sets restart activity flag'",
     "'ColorPref selected colours listener sets restart activity flag'"),
    (12929, "'S_PREFERENCES'", "'S_PREFS'"),
    (14320, "'S_PREFERENCE_click'", "'S_PREFS'"),
    (14853, "'AsyncTaskResult$Callback.onResult'", "'SftpConnectDialog.lambda$onActivityResult$14'"),
    (5778, "'AsyncTaskResult.<init>'", "'AsyncTaskResult.<init>(Object)'"),
    (5937, "'AsyncTaskResult.<init>'", "'AsyncTaskResult.<init>(Throwable)'"),
]
for n in (14334, 14343, 14354, 14365, 14375, 14385, 14395):
    SUBS.append((n, "'S_EDITTEXT_watch'", "'S_DIALOG'"))

RESUBS = [
    (3920, r"evidence=.*\)$", "evidence='SRC SevenZFile.java:435')"),
    (3921, r"evidence=.*\)$", "evidence='SRC SevenZFile.java:1033')"),
    (3922, r"evidence=.*\)$", "evidence='SRC SevenZFile.java:1033')"),
    (3923, r"evidence=.*\)$", "evidence='SRC SevenZFile.java:1033')"),
    (3930, r"evidence=.*\)$", "evidence='SRC SevenZipHelperTask.java:69')"),
    (6181, r"evidence='SRC sevenz/SevenZFile\.java:371,429,998'\)", "evidence='SRC sevenz/SevenZFile.java:371,429')"),
    (7396, r"evidence='SRC RootHelper\.java:232,300'\)", "evidence='SRC RootHelper.java:300')"),
    (7844, r"evidence='SRC GeneralDialogCreation\.java:1011 or 1066 \(overloaded method\)'\)",
     "evidence='SRC GeneralDialogCreation.java:1066 (onNegative)')"),
    (7846, r"evidence='SRC GeneralDialogCreation\.java:1011 or 1066 \(overloaded method\)'\)",
     "evidence='SRC GeneralDialogCreation.java:1073 (onPositive)')"),
    (919, r"evidence='SRC FileUtils\.java:613,658,757,835'\)", "evidence='SRC FileUtils.java:757')"),
    (12583, r"ColorPref\.java:117:", "ColorPref.java:183:"),
    (12587, r"ColorPref\.java:156:", "ColorPref.java:225:"),
    (1491, r"^$", ""),
]
RESUBS = [r for r in RESUBS if r[1] != r"^$"]

STRUCT = [
    ('remove', 1790),
    ('remove', 4796),
    ('remove', 5228),
    ('remove', 10813),
    ('remove', 11307),
    ('remove', 11405),
    ('remove', 11476),
    ('remove', 11534),
    ('remove', 12188),
    ('remove', 12599),
    ('remove', 12906),
    ('insert', 918, "e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', "
                    "'DatabaseViewerActivity.<init>', 'INTENT', 'Intent for .db files',\n"
                    "  evidence='SRC FileUtils.java:835')"),
    ('insert', 1489, "e('ColorPickerDialog.onSaveInstanceState', "
                     "'ColorPickerDialog$SavedState.<init>(Parcelable)', 'CALL',\n"
                     "  'onSaveInstanceState wraps super state in SavedState',\n"
                     "  evidence='SRC ColorPickerDialog.java:256')"),
    ('insert', 3920, "e('SevenZFile.buildDecodingStream', 'Coders.addDecoder', 'FRAMEWORK',\n"
                     "  'Unpacks bytes using coders in data stream', evidence='SRC SevenZFile.java:1030')"),
    ('insert', 3930, "e('SevenZipHelperTask.<init>', 'SevenZFile.<init>(File)', 'FRAMEWORK',\n"
                     "  'SevenZipHelperTask opens 7z archive', evidence='SRC SevenZipHelperTask.java:70')"),
    ('insert', 6180, "e('SevenZFile.buildDecodingStream', 'BoundedFileChannelInputStream.<init>', 'CALL',\n"
                     "  'SevenZ data stream creates bounded input stream', evidence='SRC sevenz/SevenZFile.java:998')"),
    ('insert', 7395, "e('RootHelper.isDirectory(String,boolean,int)', 'FileUtils.parseName', 'CALL',\n"
                     "  'parses ls output line', evidence='SRC RootHelper.java:232')"),
]

for n, old, new in SUBS:
    sub(n, old, new)
for n, pat, new in RESUBS:
    resub(n, pat, new)
for op in sorted(STRUCT, key=lambda o: -o[1]):
    if op[0] == 'remove':
        remove(op[1])
    else:
        insert(op[1], op[2])

diff = list(difflib.unified_diff(ORIG, GD, 'before', 'after', lineterm='', n=0))
print('changed lines:', sum(1 for d in diff if d[:1] in '+-' and d[:3] not in ('+++', '---')))
print('\n'.join(diff[:400]))

if APPLY:
    open(PATH, 'w', encoding='utf-8').write('\n'.join(GD))
    print('APPLIED')
else:
    print('DRY RUN (no write)')
