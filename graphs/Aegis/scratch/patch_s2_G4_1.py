"""Stage 2, G4 batch 1 (route checker stage2_G4.md, ERROR and UNCLEAR items only).
Every anchor is copied from the file text as it stood at md5 0ca0e411f4ed683e641a5cd3b59e3194 and must match EXACTLY ONCE,
or nothing is written. The backup scratch/graph_def_before_s2_G4_1.py is never overwritten by this script."""
import hashlib
import os
import sys

G = '/Users/darshan/Desktop/yang/work/graphs/Aegis'
TARGET = os.path.join(G, 'graph_def.py')
BACKUP = os.path.join(G, 'scratch', 'graph_def_before_s2_G4_1.py')
EXPECT_MD5 = '0ca0e411f4ed683e641a5cd3b59e3194'


def md5_of(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


assert md5_of(TARGET) == EXPECT_MD5, 'graph_def.py md5 is %s' % md5_of(TARGET)
assert md5_of(BACKUP) == EXPECT_MD5, 'backup md5 is %s' % md5_of(BACKUP)

PAIRS = []
A = PAIRS.append

# 1. ENV constants for the new gates (after ENV_PICKER)
A((r"""ENV_PICKER = 'the system document picker of another app returns a file (ACTION_GET_CONTENT, WelcomeSlide.java:43-47)'
ENV_PICKER_ICON = """,
   r"""ENV_PICKER = 'the system document picker of another app returns a file (ACTION_GET_CONTENT, WelcomeSlide.java:43-47)'
ENV_PICKER_SETTINGS = 'the system document picker of another app returns a file (ACTION_GET_CONTENT, ImportExportPreferencesFragment.java:110-112)'
ENV_PANIC_SENDER = ('the Guardian Project panic app sends info.guardianproject.panic.action.TRIGGER '
                    '(the manifest intent filter matches it, AndroidManifest.xml:91-101; PanicResponderActivity.java:19-22)')
ENV_INSTALLED_GA = ('Google Authenticator with versionCode 5000100 or lower is installed (another app; '
                    'GoogleAuthImporter.isInstalledAppVersionSupported, GoogleAuthImporter.java:40-49)')
ENV_ROOT = ('the device grants Aegis root access, so the root shell opens and reports root '
            '(ImportEntriesActivity.java:149-153; RootShellTask.java:17-20)')
ENV_PICKER_ICON = """))

# 2. ENV kinds for the new constants
A((r"""    ENV_BIOMETRIC_FAIL: ['hardware'], ENV_AUTOFILL: ['other_app'],
}""",
   r"""    ENV_BIOMETRIC_FAIL: ['hardware'], ENV_AUTOFILL: ['other_app'],
    ENV_PICKER_SETTINGS: ['other_app'], ENV_PANIC_SENDER: ['other_app'], ENV_INSTALLED_GA: ['other_app'], ENV_ROOT: ['other'],
}"""))

# 3. R1 step 5 (UNCLEAR): the panic ENTRY names the sender, not the trust checks. Class stays standard.
A((r"""  env=ENV_PANIC, evidence='SRC AndroidManifest.xml:91-101; SRC ui/PanicResponderActivity.java:19-22')""",
   r"""  env=ENV_PANIC_SENDER, evidence='SRC AndroidManifest.xml:91-101; SRC ui/PanicResponderActivity.java:19-22')"""))

# 4. R1 step 8 (UNCLEAR): the calling package needs startActivityForResult
A((r"""  'the calling package name is known', guard='the calling package name is not empty (TrustedIntents.java:106-109)',
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:104-110')""",
   r"""  'the calling package name is known',
  guard='the calling package name is not empty (TrustedIntents.java:106-109); getCallingPackageName returns a package only when this activity was started with startActivityForResult (getCallingActivity, TrustedIntents.java:131-142; the warning at 120-124 says a singleInstance or singleTask activity cannot get the calling activity; without a request code the calling activity is null, FW-SRC core/java/android/app/Activity.java:5384-5399)',
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:104-110,120-124,131-142; FW-SRC core/java/android/app/Activity.java:5384-5399')"""))

# 5. R2 step 8 and R5 step 8 (ERROR): the plain-text vault is a cross-run state (its constant names the earlier intro run)
A((r"""  needs_state=ST_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:950-974,991-992')""",
   r"""  needs_state=ST_PLAIN_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:950-974,991-992')"""))

# 6. R3 step 9 (ERROR): the Hilt context listener runs inside AegisActivity.onCreate (its super.onCreate, AegisActivity.java:67)
A((r"""e('Hilt_AegisActivity._initHiltInternal', 'Hilt_AegisActivity$1.onContextAvailable', 'FRAMEWORK',""",
   r"""e('AegisActivity.onCreate', 'Hilt_AegisActivity$1.onContextAvailable', 'FRAMEWORK',"""))
A((r"""  guard='the activity\'s onCreate has reached its super.onCreate call (the case read: MainActivity.onCreate, which calls super.onCreate first); the route shown from the constructor has no onCreate step before this listener',""",
   r"""  guard='AegisActivity.onCreate has reached its super.onCreate call (AegisActivity.java:67; the framework runs the listener inside that call); MainActivity.onCreate calls AegisActivity.onCreate first (MainActivity.java:194)',"""))
A((r"""SRC ui/MainActivity.java:193-195 (onCreate, super.onCreate at 194, setContentView at 195)')""",
   r"""SRC ui/AegisActivity.java:61-67 (onCreate, super.onCreate at 67); SRC ui/MainActivity.java:193-195 (onCreate, super.onCreate at 194, setContentView at 195)')"""))

# 7. R3 step 7 (UNCLEAR): the auto row AegisActivity.<init> -> Hilt_AegisActivity.<init>() gets an INFERRED evidence text (FIX_LINES key = the auto row's exact evidence)
A((r"""    ('IntroActivity.onCreate', 'IntroBaseActivity.addSlide@IntroActivity', 'SRC IntroActivity.java:41 (bytecode)'): 'SRC IntroActivity.java:38-41 (bytecode line was 41; addSlide(WelcomeSlide) is line 38)',
}""",
   r"""    ('IntroActivity.onCreate', 'IntroBaseActivity.addSlide@IntroActivity', 'SRC IntroActivity.java:41 (bytecode)'): 'SRC IntroActivity.java:38-41 (bytecode line was 41; addSlide(WelcomeSlide) is line 38)',
    ('AegisActivity.<init>', 'Hilt_AegisActivity.<init>()', 'SRC AegisActivity.java:45 (bytecode)'): 'INFERRED Hilt superclass: AegisActivity extends Hilt_AegisActivity only in the Hilt-rewritten build class (the generated file is not in the source tree; source AegisActivity.java:45 declares extends AppCompatActivity); the bytecode of AegisActivity.<init> makes the implicit super() call (bytecode line table: AegisActivity.java:45)',
}"""))

# 8. R4 step 7 (ERROR): the layout fragment is created by the FragmentManager by reflection
A((r"""'the layout holds the entry list fragment (key_profiles): the FragmentManager creates it',
""",
   r"""'the layout holds the entry list fragment (key_profiles): the FragmentManager creates it',
  cls='non_standard', via='reflection: the androidx FragmentManager creates the fragment class named in the layout (android:name, res/layout/activity_main.xml:54-56)',
"""))

# 9. R4 step 10 (ERROR): Glide.with reaches the generated factory through library lookup (the loop over _GLIDE_SITES)
A((r"""      'Glide.with: the library asks the generated request-manager factory for a request manager (GlideRequests)',
""",
   r"""      'Glide.with: the library asks the generated request-manager factory for a request manager (GlideRequests)',
      cls='non_standard', via='library lookup: Glide finds the generated request-manager factory through the generated module (Glide library source not on disk)',
"""))

# 10. R4 step 12 (ERROR): setRequestOptions is virtual dispatch from library code
A((r"""  'the RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides (it wraps the options in GlideOptions)',
""",
   r"""  'the RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides (it wraps the options in GlideOptions)',
  cls='non_standard', via='library virtual dispatch: the Glide RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides (Glide library source not on disk)',
"""))

# 11. R4 step 14 (ERROR): RequestOptions.apply -> autoClone is virtual dispatch; sanity_check citation removed
A((r"""  evidence='INFERRED Glide library RequestOptions.apply -> autoClone (library source not read, not on disk); generated GlideOptions.java not in the source tree; out/sanity_check.csv (coverage ran it)')""",
   r"""  cls='non_standard', via='library virtual dispatch: Glide RequestOptions.apply calls autoClone(), which the generated GlideOptions overrides (Glide library source not on disk)',
  evidence='INFERRED Glide library RequestOptions.apply -> autoClone (library source not on disk); generated GlideOptions.java not in the source tree')"""))

# 12. R4 step 15 (ERROR): autoClone -> clone is virtual dispatch; sanity_check citation removed
A((r"""  evidence='INFERRED Glide library RequestOptions.autoClone -> clone (library source not read); out/sanity_check.csv (coverage ran it)')""",
   r"""  cls='non_standard', via='library virtual dispatch: Glide RequestOptions.autoClone calls clone(), which the generated GlideOptions overrides (Glide library source not on disk)',
  evidence='INFERRED Glide library RequestOptions.autoClone -> clone (library source not on disk)')"""))

# 13. sibling of steps 14-15 (same wrong citation; not on a checked route): sanity_check citation removed
A((r"""  evidence='INFERRED Glide library RequestManager calls RequestOptions.lock on the default options (library source not read); out/sanity_check.csv (coverage ran it)')""",
   r"""  evidence='INFERRED Glide library RequestManager calls RequestOptions.lock on the default options (library source not read)')"""))

# 14. R5 step 23 (ERROR): the OK button is a Material dialog button (Dialogs.java:533); the AlertController citation is replaced; FW_CLICK kept
A((r"""    evidence=FW_CLICK + '; FW-SRC core/java/com/android/internal/app/AlertController.java:710 (setOnClickListener(mButtonHandler)), 127-140 (mButtonHandler.onClick sends the button message), 166 (ButtonHandler calls the OnClickListener); SRC ui/dialogs/Dialogs.java:536-538')""",
   r"""    evidence=FW_CLICK + '; INFERRED Material MaterialAlertDialogBuilder (Dialogs.java:533; the Material library source is not on disk); SRC ui/dialogs/Dialogs.java:533-538')"""))

# 15. R2 step 24 (ERROR): the Settings import result comes from its own variant of the shared launcher node
A((r"""e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)', 'ImportExportPreferencesFragment.lambda$new$0', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult', env=ENV_PICKER,
""",
   r"""# the Settings import has its own variant of the shared launcher node (the icon packs and the backups use the shared node).
# The launch is a hand CALL into the variant from the importer dialog's listener (ImportExportPreferencesFragment.java:110-112).
# A hand edge to the variant also suppresses the auto row to the shared node (build_graph.add_auto_edges, manual-edge rule).
_FIL_SETTINGS = 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@SETTINGS_IMPORT'
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5', _FIL_SETTINGS, 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:110-112')
e(_FIL_SETTINGS, 'ImportExportPreferencesFragment.lambda$new$0', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult', env=ENV_PICKER_SETTINGS,
"""))

# 16. R5 step 24 (ERROR): the Dialogs OK relays call the app's ImporterListener, so the class is explicit (both relays)
A((r"""  'the OK button gives the chosen importer to the import listener: the file picker opens', cls='non_standard',
  via='interface callback: ImporterListener.onImporterSelectionResult (Dialogs.java:536-538); the listener lambda is passed at ImportExportPreferencesFragment.java:107-113',
""",
   r"""  'the OK button gives the chosen importer to the import listener: the file picker opens',
"""))
A((r"""  'the OK button gives the chosen importer to the import-app listener: the import page opens', cls='non_standard',
  via='interface callback: ImporterListener.onImporterSelectionResult (Dialogs.java:536-538); the listener lambda is passed at ImportExportPreferencesFragment.java:119-121',
""",
   r"""  'the OK button gives the chosen importer to the import-app listener: the import page opens',
"""))

# 17. R5 step 29 (ERROR): the installed Google Authenticator version is an other-app gate
A((r"""  'no file was passed and the installed app version is supported: the entries are read from the app',
""",
   r"""  'no file was passed and the installed app version is supported: the entries are read from the app',
  env=ENV_INSTALLED_GA,
"""))

# 18. R5 step 32 (ERROR): RootShellTask.Callback.onTaskFinished is an app interface called from app code: explicit
A((r"""  '_cb.onTaskFinished(shell): the callback reads the entries from the installed app, or closes the page when there is no root',
  cls='non_standard', via='RootShellTask.Callback.onTaskFinished (interface call; the lambda is passed at ImportEntriesActivity.java:144)',
""",
   r"""  '_cb.onTaskFinished(shell): the callback reads the entries from the installed app, or closes the page when there is no root',
"""))

# 19. R5 step 33 (ERROR): root gate ENV, and the guard reworded to the source (line 108 is DatabaseImporter.create)
A((r"""  guard='the page is not finishing (ImportEntriesActivity.java:145-147), the shell is not null and is root (lines 149-153), and the chosen importer is GoogleAuthImporter (line 108)',
""",
   r"""  env=ENV_ROOT,
  guard='the page is not finishing (ImportEntriesActivity.java:145-147), the shell is not null and is root (lines 149-153; otherwise a toast and finish), and the importer on this page is GoogleAuthImporter (importer.readFromApp, line 156, is a virtual call on the chosen importer)',
"""))

# 20. R5 step 36 (UNCLEAR): the filter is a libsu callback (non_standard); the guard is the filter itself
A((r"""  guard='the SQL import reads a database from a folder (SqlImporterHelper.java:68)',
""",
   r"""  cls='non_standard', via='library callback: libsu SuFile.listFiles(FilenameFilter) calls the filter for each name in the folder (libsu source not on disk)',
  guard='the file name starts with the database file name (name.startsWith(path.getName()), SqlImporterHelper.java:67-68)',
"""))

# every anchor must match exactly once, checked in order against the progressively edited text
text = open(TARGET, 'rb').read().decode('utf-8')
new = text
for i, (old, rep) in enumerate(PAIRS, 1):
    n = new.count(old)
    if n != 1:
        print('ANCHOR %d matches %d times; nothing written' % (i, n))
        sys.exit(1)
    new = new.replace(old, rep, 1)

assert new != text
with open(TARGET, 'wb') as f:
    f.write(new.encode('utf-8'))
print('applied %d anchor replacements' % len(PAIRS))
print('new md5', hashlib.md5(new.encode('utf-8')).hexdigest())
