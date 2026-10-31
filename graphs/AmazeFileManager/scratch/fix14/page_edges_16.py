import ast
import os
import shutil

W = '/Users/darshan/Desktop/yang/work'
os.chdir(W)
S = 'graphs/AmazeFileManager/scratch/'
G = 'graphs/AmazeFileManager/graph_def.py'
R = 'final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/'

CHECKS = [
    ('activities/MainActivity.java', 277, 'public void onCreate(final Bundle savedInstanceState)'),
    ('fragments/MainFragment.java', 237, 'public View onCreateView('),
    ('activities/superclasses/PermissionsActivity.java', 53, 'public void requestStoragePermission('),
    ('activities/superclasses/PermissionsActivity.java', 54, 'GeneralDialogCreation.showBasicDialog('),
    ('activities/TextEditorActivity.java', 126, 'public void onCreate(Bundle'),
    ('activities/DatabaseViewerActivity.java', 79, 'public void onCreate(Bundle'),
    ('asynchronous/services/ExtractService.java', 97, 'public int onStartCommand('),
    ('ui/views/drawer/Drawer.java', 522, 'public void open()'),
    ('activities/MainActivity.java', 1204, 'protected void onDestroy()'),
]

for f, n, needle in CHECKS:
    line = open(R + f, encoding='utf-8', errors='replace').read().split('\n')[n - 1]
    assert needle in line, (f, n, line)

NEW = [
    """e('MainActivity.onCreate', 'S_MAIN', 'LIFECYCLE',
  'onCreate builds the main shell (views, tabs, drawer, FAB)',
  evidence='SRC activities/MainActivity.java:277 public void onCreate(Bundle) builds the main screen')""",
    """e('MainFragment.onCreateView', 'S_MAIN_TAB', 'LIFECYCLE',
  'onCreateView inflates the tab that shows the file list',
  evidence='SRC fragments/MainFragment.java:237 public View onCreateView(LayoutInflater, ViewGroup, Bundle)')""",
    """e('PermissionsActivity.requestStoragePermission', 'S_PERM', 'CALL',
  'requestStoragePermission asks for WRITE_EXTERNAL_STORAGE',
  evidence='SRC activities/superclasses/PermissionsActivity.java:53-60 requestStoragePermission calls requestPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE, ...)')""",
    """e('PermissionsActivity.requestStoragePermission', 'S_DIALOG', 'CALL',
  'requestStoragePermission shows the grant-storage-permission dialog',
  evidence='SRC activities/superclasses/PermissionsActivity.java:54 GeneralDialogCreation.showBasicDialog(this, grant_storage_permission, ...)')""",
    """e('TextEditorActivity.onCreate', 'S_TEXT_EDITOR', 'LIFECYCLE',
  'onCreate shows the text viewer/editor screen',
  evidence='SRC activities/TextEditorActivity.java:126 public void onCreate(Bundle)')""",
    """e('DatabaseViewerActivity.onCreate', 'S_DB_VIEWER', 'LIFECYCLE',
  'onCreate shows the SQLite database viewer screen',
  evidence='SRC activities/DatabaseViewerActivity.java:79 public void onCreate(Bundle)')""",
    """e('ExtractService.onStartCommand', 'S_SERVICE', 'LIFECYCLE',
  'onStartCommand starts the background extraction work, so a service is running',
  evidence='SRC asynchronous/services/ExtractService.java:97 public int onStartCommand(Intent, int, int)')""",
    """e('Drawer.open', 'S_DRAWER', 'CALL',
  'open() opens the navigation drawer',
  evidence='SRC ui/views/drawer/Drawer.java:522 public void open()')""",
    """e('MainActivity.onDestroy', 'S_EXIT', 'LIFECYCLE',
  'onDestroy ends the activity; the app is leaving the main screen',
  evidence='SRC activities/MainActivity.java:1204 protected void onDestroy()')""",
]

src = open(G, encoding='utf-8').read()
for stmt in NEW:
    head = stmt.split(',', 2)[0] + ', ' + stmt.split(',', 2)[1]
    assert src.count(head) == 0, head

tree = ast.parse(src)
last = None
for st in tree.body:
    if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and getattr(st.value.func, 'id', '') == 'e':
        last = st
assert last is not None

lines = src.split('\n')
lines[last.end_lineno:last.end_lineno] = [''] + '\n\n'.join(NEW).split('\n')
text = '\n'.join(lines)
ast.parse(text)

if not os.path.exists(S + 'graph_def_before_finish_16.py'):
    shutil.copy(G, S + 'graph_def_before_finish_16.py')
open(G, 'w', encoding='utf-8').write(text)
print('inserted after line', last.end_lineno, 'statements', len(NEW))
