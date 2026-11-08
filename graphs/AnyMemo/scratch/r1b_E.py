"""Round 1b Group E (database helpers, AsyncTask, state texts). Applied once; every anchor must match exactly once."""
import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply, add_gate_entries, GD

text = open(GD, encoding='utf-8').read()
LINES = text.split('\n')


def line_of(prefix):
    hits = [l for l in LINES if l.startswith(prefix)]
    if len(hits) != 1:
        print('LINE FAIL (%d hits): %r' % (len(hits), prefix[:100]))
        sys.exit(1)
    return hits[0]


# GATE keys added in this group must not exist yet (a duplicate key in the dict literal would silently win)
GATE_KEYS = [
    ('MiscTabFragment.onClick', 'DatabaseMerger.<init>'),
    ('DatabaseMerger.onClick', 'DatabaseMerger$1.doHeavyTask'),
    ('DatabaseUtil.mergeDatabases', 'CardDaoImpl.createCards'),
    ('StudyActivity.onOptionsItemSelected', 'StudyActivity.showCategoriesDialog'),
    ('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.onPreExecute'),
    ('AMFileUtil.deleteFileWithBackup', 'AMFileUtil.deleteDbSafe'),
    ('AMFileUtil.deleteDbSafe', 'AMPrefUtil.removePrefKeys'),
    ('RecentListFragment.loadRecentItemsWithDetails', 'AnyMemoDBOpenHelper.getCardDao'),
    ('ConverterFragment.startConversion', 'ConverterFragment.invokeConverterService'),
]
for a, b in GATE_KEYS:
    k = "('%s', '%s'):" % (a, b)
    if text.count(k):
        print('GATE KEY ALREADY PRESENT: %s' % k)
        sys.exit(1)

IMP = ['SupermemoXMLImporter', 'Supermemo2008XMLImporter', 'QATxtImporter', 'Mnemosyne2CardsImporter',
       'ZipImporter', 'MnemosyneXMLImporter', 'CSVImporter']
EXP = ['Mnemosyne2CardsExporter', 'CSVExporter', 'MnemosyneXMLExporter', 'ZipExporter', 'QATxtExporter']

pairs = []

# ---- E4 and E5: CardDaoImpl batch call and AbstractHelperDaoImpl.create variant split ----
E4_OLD = ("e('CardDaoImpl.createCards', 'CardDaoImpl$2.call', 'FRAMEWORK', "
          "'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:491', "
          "evidence=FW_RX + '; SRC dao/CardDaoImpl.java:491-496')")
E4_NEW = (
    "# Round 1b E4: ORMLite's callBatchTasks (AbstractHelperDaoImpl.java:149-151 calls super.callBatchTasks) runs the Callable.\n"
    "# The call() edge now starts at callBatchTasks; the automatic CALL createCards -> callBatchTasks is unchanged.\n"
    "e('AbstractHelperDaoImpl.callBatchTasks', 'CardDaoImpl$2.call', 'FRAMEWORK', "
    "'ORMLite batch runner (super.callBatchTasks) invokes call(), which runs createCardsNoBatch (CardDaoImpl.java:493)', "
    "evidence=FW_ORMLITE + '; SRC dao/AbstractHelperDaoImpl.java:149-151; dao/CardDaoImpl.java:491-496')\n"
    "# Round 1b E5: variant split of AbstractHelperDaoImpl.create (AbstractHelperDaoImpl.java:122 sets the creation date by domain type)\n"
    "sup(('AbstractHelperDaoImpl.create', 'Category.setCreationDate'),\n"
    "    ('AbstractHelperDaoImpl.create', 'Card.setCreationDate'))\n"
    "e('CategoryDaoImpl.createOrReturn', 'AbstractHelperDaoImpl.create@CATEGORY', 'CALL', "
    "'create(nc): the new category row is inserted (CategoryDaoImpl.java:37)', evidence='SRC dao/CategoryDaoImpl.java:37')\n"
    "e('CardDaoImpl.createCardsNoBatch', 'AbstractHelperDaoImpl.create@CATEGORY', 'CALL', "
    "'categoryDao.create(card.getCategory()): a new, non-empty category is inserted (CardDaoImpl.java:852)', "
    "guard='card category name is not in categoryMap and is not empty (CardDaoImpl.java:846-851)', "
    "evidence='SRC dao/CardDaoImpl.java:846-852')\n"
    "e('CardDaoImpl.create', 'AbstractHelperDaoImpl.create@CARD', 'CALL', "
    "'super.create(c): the card row is inserted (CardDaoImpl.java:228)', evidence='SRC dao/CardDaoImpl.java:228')\n"
    "e('AbstractHelperDaoImpl.create@CATEGORY', 'Category.setCreationDate', 'CALL', "
    "'the category is a VersionableDomainObject: setCreationDate(new Date()) (AbstractHelperDaoImpl.java:122)', "
    "evidence='SRC dao/AbstractHelperDaoImpl.java:122')\n"
    "e('AbstractHelperDaoImpl.create@CARD', 'Card.setCreationDate', 'CALL', "
    "'the card is a VersionableDomainObject: setCreationDate(new Date()) (AbstractHelperDaoImpl.java:122)', "
    "evidence='SRC dao/AbstractHelperDaoImpl.java:122')"
)
pairs.append((E4_OLD, E4_NEW))

# ---- E7, E8, E9: AsyncTask edges go through onPreExecute ----
E7_OLD = line_of("e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$InitTask.doInBackground', 'ASYNC'")
E7_NEW = ("# Round 1b E7: the direct onCreateView -> doInBackground edge is replaced; AsyncTask runs onPreExecute first\n"
          "e('CategoryEditorFragment$InitTask.onPreExecute', 'CategoryEditorFragment$InitTask.doInBackground', 'ASYNC', "
          "'AsyncTask runs doInBackground after onPreExecute, which creates the category adapter (CategoryEditorFragment.java:137)', "
          "evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:135-150')")
pairs.append((E7_OLD, E7_NEW))

E8_OLD = line_of("e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.doInBackground', 'ASYNC'")
E8_NEW = ("# Round 1b E8: the direct onClick -> NewCategoryTask.doInBackground edge is replaced; onPreExecute runs first\n"
          "e('CategoryEditorFragment$NewCategoryTask.onPreExecute', 'CategoryEditorFragment$NewCategoryTask.doInBackground', 'ASYNC', "
          "'AsyncTask runs doInBackground after onPreExecute (CategoryEditorFragment.java:241-250)', "
          "evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:241-250')")
pairs.append((E8_OLD, E8_NEW))

E9_OLD = line_of("e('DetailScreen.onCreate', 'DetailScreen$InitTask.doInBackground', 'ASYNC'")
E9_NEW = ("# Round 1b E9: the direct onCreate -> doInBackground edge is replaced; onPreExecute (progress dialog) runs first\n"
          "e('DetailScreen$InitTask.onPreExecute', 'DetailScreen$InitTask.doInBackground', 'ASYNC', "
          "'AsyncTask runs doInBackground after onPreExecute (DetailScreen.java:242-269)', "
          "evidence=FW_ASYNC + '; SRC ui/DetailScreen.java:242-269')")
pairs.append((E9_OLD, E9_NEW))

# ---- E10: state text for the typed-name database file ----
pairs.append(("NEED_AUDIO_FILE = state_text(",
              "NEED_TYPED_DB_FILE = state_text('a database file with the typed name already exists in the current folder "
              "(made by an earlier Create DB or a fixture)', ('file',))\nNEED_AUDIO_FILE = state_text("))
pairs.append(("'the file name typed in the Create DB dialog already exists (DatabaseOperationDialogUtil.java:57-58)'},",
              "'the file name typed in the Create DB dialog already exists (DatabaseOperationDialogUtil.java:57-58)', "
              "'needs_state': NEED_TYPED_DB_FILE},"))

# ---- E14: schema version 0 state; the onDowngrade/onUpgrade state text is reworded ----
pairs.append(("DB_NEW_OR_CHANGED = state_text('the database file is new or its schema version changed "
              "(fresh install, upgrade or downgrade)', ('data',))",
              "DB_VERSION_ZERO = state_text('the database file has schema version 0 (a new or empty file never set up by AnyMemo)', ('data',))\n"
              "DB_NEW_OR_CHANGED = state_text(\"the stored schema version is newer or older than the app's\", ('data',))"))
pairs.append(("  'the first DAO request opens the database; when the file is new, SQLiteOpenHelper calls onCreate',\n"
              "  needs_state=DB_NEW_OR_CHANGED,",
              "  'the first DAO request opens the database; when the file is new, SQLiteOpenHelper calls onCreate',\n"
              "  needs_state=DB_VERSION_ZERO,"))

# ---- E15: hand clinit edge for Setting$CardStyle (replaces the automatic one on the same pair) ----
pairs.append(("# ---- D. fragments, views and menus (framework callbacks) ----",
              "# Round 1b E15: the field initialiser cardStyle = CardStyle.SINGLE_SIDED (Setting.java:46) runs the enum class initialiser.\n"
              "# This hand edge is on the same pair as the automatic CALL Setting.<init> -> Setting$CardStyle.<clinit>, which is therefore suppressed.\n"
              "e('Setting.<init>', 'Setting$CardStyle.<clinit>', 'LIFECYCLE', 'the JVM runs the static initialiser of Setting$CardStyle "
              "before the field initialiser cardStyle = CardStyle.SINGLE_SIDED (Setting.java:46) runs', "
              "cls='non_standard', via=C4_CLINIT_VIA, evidence='SRC entity/Setting.java:46')\n"
              "# ---- D. fragments, views and menus (framework callbacks) ----"))

# ---- E17: ConvertIntentService variants (import from the Misc tab, export from the converter dialog) ----
L_IMP = line_of("e('MiscTabFragment.invokeImportConversion', 'ConvertIntentService.onCreate', 'ENTRY'")
L_EXP = line_of("e('ConverterFragment.invokeConverterService', 'ConvertIntentService.onCreate', 'ENTRY'")
L_LC = line_of("e('ConvertIntentService.onCreate', 'ConvertIntentService.onHandleIntent', 'LIFECYCLE'")
C17_HDR = line_of('# ---- ConvertIntentService (IntentService')

N_IMP = ("# Round 1b E17: the Misc tab import entry goes to the onCreate@IMPORT variant\n"
         "e('MiscTabFragment.invokeImportConversion', 'ConvertIntentService.onCreate@IMPORT', 'ENTRY', "
         "'startService(ConvertIntentService) for an importer picked in the Misc tab import list', "
         "guard='EXTRA_CONVERTER_CLASS is the importer launched from the Misc tab import list (launchImportConvert sets "
         "pendingImportConverterClass; MiscTabFragment.java:267-288, 408-409, 469-477)', "
         "evidence='SRC ui/MiscTabFragment.java:469-477')")
N_EXP = ("# Round 1b E17: ConverterFragment is opened only from the Misc tab export items, so its entry goes to onCreate@EXPORT\n"
         "e('ConverterFragment.invokeConverterService', 'ConvertIntentService.onCreate@EXPORT', 'ENTRY', "
         "'getActivity().startService(intent) for an exporter (ConverterFragment is opened from the Misc tab export items, "
         "MiscTabFragment.java:291-333)', evidence='SRC ui/ConverterFragment.java:162; ui/MiscTabFragment.java:291-333')")

old_lc_head = "'ConvertIntentService.onCreate', 'ConvertIntentService.onHandleIntent'"
assert L_LC.count(old_lc_head) == 1
N_LC_IMP = L_LC.replace(old_lc_head, "'ConvertIntentService.onCreate@IMPORT', 'ConvertIntentService.onHandleIntent@IMPORT'")
N_LC_EXP = L_LC.replace(old_lc_head, "'ConvertIntentService.onCreate@EXPORT', 'ConvertIntentService.onHandleIntent@EXPORT'")

call_lines = ["# Round 1b E17: the import variant calls the importers; the export variant calls the exporters.",
              "# TabTxtImporter and TabTxtExporter extend CSVImporter and CSVExporter (TabTxtImporter.java:27, TabTxtExporter.java:23)",
              "# and inherit convert(), so the CSV convert edges cover them."]
for c in IMP:
    call_lines.append("e('ConvertIntentService.onHandleIntent@IMPORT', '%s.convert', 'CALL', "
                      "'converter.convert(input, output) runs the importer %s (ConvertIntentService.java:125)', "
                      "evidence='SRC service/ConvertIntentService.java:125; ui/MiscTabFragment.java:267-288')" % (c, c))
for c in EXP:
    call_lines.append("e('ConvertIntentService.onHandleIntent@EXPORT', '%s.convert', 'CALL', "
                      "'converter.convert(input, output) runs the exporter %s (ConvertIntentService.java:125)', "
                      "evidence='SRC service/ConvertIntentService.java:125; ui/MiscTabFragment.java:291-333')" % (c, c))

sup_lines = ("# Round 1b E17: the automatic converter CALLs from the base onHandleIntent are replaced by the variant CALLs below\n"
             "sup(" + ',\n    '.join("('ConvertIntentService.onHandleIntent', '%s.convert')" % c for c in IMP + EXP) + ")")

pairs.append((L_IMP, N_IMP))
pairs.append((L_EXP, N_EXP))
pairs.append((L_LC, N_LC_IMP + '\n' + N_LC_EXP + '\n' + '\n'.join(call_lines)))
pairs.append((C17_HDR, C17_HDR + '\n' + sup_lines))

# ---- E1, E2, E3, E6, E8, E11, E12, E13, E16: GATE entries (added before the closing brace of GATE) ----
apply(pairs, 'E-edits')

gate = [
    "    # Round 1b E1: the Misc tab merge button opens DatabaseMerger (MiscTabFragment.java:346-349); both duplicate edges get it",
    "    ('MiscTabFragment.onClick', 'DatabaseMerger.<init>'): {'guard': 'v == mergeButton (MiscTabFragment.java:346-349)'},",
    "    # Round 1b E2: the merge button starts the merge task (DatabaseMerger.java:115; AMGUIUtility.java:80-83)",
    "    ('DatabaseMerger.onClick', 'DatabaseMerger$1.doHeavyTask'): {'guard': 'v == mergeButton (DatabaseMerger.java:115)'},",
    "    # Round 1b E3: createCards runs only when the two paths differ (DatabaseUtil.java:47-48)",
    "    ('DatabaseUtil.mergeDatabases', 'CardDaoImpl.createCards'): {'guard': 'destPath is not equal to srcPath (DatabaseUtil.java:47-48)'},",
    "    # Round 1b E6: the menu item opens the category dialog (StudyActivity.java:163-164)",
    "    ('StudyActivity.onOptionsItemSelected', 'StudyActivity.showCategoriesDialog'): {'guard': 'itemId == R.id.menu_memo_category (StudyActivity.java:163-164)'},",
    "    # Round 1b E8: the new-category button starts NewCategoryTask (CategoryEditorFragment.java:111)",
    "    ('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.onPreExecute'): {'guard': 'v == newButton (CategoryEditorFragment.java:111)'},",
    "    # Round 1b E11: deleteDbSafe runs only when the file exists (AMFileUtil.java:72-73)",
    "    ('AMFileUtil.deleteFileWithBackup', 'AMFileUtil.deleteDbSafe'): {'guard': 'the file exists (AMFileUtil.java:72-73)'},",
    "    # Round 1b E12: the preference keys are removed only when the file exists (AMFileUtil.java:59-60)",
    "    ('AMFileUtil.deleteDbSafe', 'AMPrefUtil.removePrefKeys'): {'guard': 'the file exists (AMFileUtil.java:59-60)'},",
    "    # Round 1b E13: the recent-deck DAO is opened only with a context and an entry (RecentListFragment.java:337, 339-341)",
    "    ('RecentListFragment.loadRecentItemsWithDetails', 'AnyMemoDBOpenHelper.getCardDao'): {'guard': 'context is not null and the recent list has an entry (RecentListFragment.java:337, 339-341)', 'needs_state': NEED_RECENT},",
    "    # Round 1b E16: the converter runs only for a db destination whose output file does not exist (ConverterFragment.java:93-94, 123-125)",
    "    ('ConverterFragment.startConversion', 'ConverterFragment.invokeConverterService'): {'guard': 'destination extension is db and the output file does not exist (ConverterFragment.java:93-94, 123-125)'},",
]
add_gate_entries(gate, 'E-gates')
