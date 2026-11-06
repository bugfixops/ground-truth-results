# Aegis 3.4.2 trigger graph, schema 2. Package com.beemdevelopment.aegis.debug (debug build, final_java_only/Aegis/app/DATASET.txt).
# Source: final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main (AndroidManifest.xml and java/com/beemdevelopment/aegis/).
# Standard configuration: fresh install on an API 27 emulator; runtime permissions only where a route needs them.
# The system creates the Application before any component (ActivityThread.java:5740), so every route starts at
# S_ENTRY -> AegisApplication.<init> -> Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate -> S_PROCESS, and component entries start at S_PROCESS.
# Direct app-to-app calls come from the bytecode (USE_AUTO); the hand edges below set the guards, the states and the gates.

TITLE = 'Aegis 3.4.2 trigger graph'
USE_AUTO = True
STRICT = True

# ------------------------------------------------------------------ ENV gates (outside the app or the device)
ENV_VIEW = 'another app opens an otpauth:// link (ACTION_VIEW, MainActivity intent filter, AndroidManifest.xml:52-59)'
ENV_SEND = 'another app shares text or images to Aegis (ACTION_SEND or ACTION_SEND_MULTIPLE, AndroidManifest.xml:60-66)'
ENV_PANIC = ('the Guardian Project panic app sends info.guardianproject.panic.action.TRIGGER from a trusted signer '
             '(TrustedIntents, PanicResponderActivity.java:29-37)')
ENV_QS = 'the user taps the Aegis tile in the Quick Settings panel (AndroidManifest.xml:108-132)'
ENV_SHORTCUT = 'the user long-presses the Aegis launcher icon and taps the "new entry" shortcut (the dynamic shortcut set by AegisApplicationBase.initAppShortcuts, AegisApplicationBase.java:60, 70-88)'
ENV_SCREEN_OFF = 'the screen is switched off (ACTION_SCREEN_OFF, AegisApplicationBase.java:49-51)'
ENV_BOOT = 'the device boots or the user unlocks it (BOOT_COMPLETED or USER_UNLOCKED, AndroidManifest.xml:140-147)'
ENV_BACKUP = 'the system runs a full backup of the app data (AegisBackupAgent.onFullBackup, AegisBackupAgent.java:43-71)'
ENV_RESTORE = 'the system restores the app data from an Android backup (AegisBackupAgent.onRestoreFile, AegisBackupAgent.java:95-112)'
ENV_PICKER = 'the system document picker of another app returns a file (ACTION_GET_CONTENT, WelcomeSlide.java:43-47)'
ENV_PICKER_SETTINGS = 'the system document picker of another app returns a file (ACTION_GET_CONTENT, ImportExportPreferencesFragment.java:110-112)'
ENV_PANIC_SENDER = ('the Guardian Project panic app sends info.guardianproject.panic.action.TRIGGER '
                    '(the manifest intent filter matches it, AndroidManifest.xml:91-101; PanicResponderActivity.java:19-22)')
ENV_INSTALLED_GA = ('Google Authenticator with versionCode 5000100 or lower is installed (another app; '
                    'GoogleAuthImporter.isInstalledAppVersionSupported, GoogleAuthImporter.java:40-49)')
ENV_ROOT = ('the device grants Aegis root access, so the root shell opens and reports root '
            '(ImportEntriesActivity.java:149-153; RootShellTask.java:17-20)')
ENV_PICKER_ICON = 'the system document picker of another app returns an icon pack file (ACTION_GET_CONTENT, IconPacksManagerFragment.java:173-174)'
ENV_BIOMETRIC = ('a fingerprint or face is enrolled and accepted by the sensor (BiometricPrompt, AuthActivity.java:270-293); '
                 'the unlock screen shows the button only when the vault has a biometric slot (AuthActivity.java:132-150)')
ENV_CAMERA = 'the user grants the camera permission in the system dialog (PermissionHelper.request, MainActivity.java:803-810)'
ENV_CAMERA_GRANTED = 'the camera permission was already granted: PermissionHelper.request returns true and the scanner opens (PermissionHelper.java:22-36; MainActivity.java:804-809)'
ENV_QR_CODE = 'a QR code with an otpauth:// link, or a Google export link whose code is the last of its batch, is held in front of the camera (ScannerActivity reads the camera frames)'
ENV_CLIPBOARD = 'the clipboard holds a valid otpauth:// link, copied by the user or another app (ClipboardUtils.readText, MainActivity.java:475-496)'
ENV_PICK_IMAGE = 'the user picks an image or a file in the chooser of another app (MainActivity.startScanImageActivity, MainActivity.java:812-824)'
ENV_PICK_ICON = 'the user picks an image or a file in the chooser of another app (EditEntryActivity.startImageSelectionActivity, EditEntryActivity.java:568-577)'
ENV_AUTO_TIME_OFF = 'the device automatic date and time is off (Settings.Global AUTO_TIME is 0, MainActivity.java:757-758)'
ENV_CLOCK_FORWARD = ('the device clock is moved forward by at least 14 days after the first run, so the password reminder is due '
                     '(Preferences.java:64-65 sets the timestamp on the first construction; 118-123 default frequency BIWEEKLY; '
                     'PassReminderFreq.java:20-21,34 is 14 days; Preferences.java:138-145 duration check)')
ENV_EXPORT_RESULT = ('the user saves the export file in the system document creator (ACTION_CREATE_DOCUMENT) or sends it through the '
                     'share chooser (ACTION_SEND), and the other app returns to Aegis (ImportExportPreferencesFragment.java:270-277,320-326)')
ENV_BACKUP_RESULT = ('the user picks a backup folder (ACTION_OPEN_DOCUMENT_TREE) or chooses where to save the single backup file '
                     '(ACTION_CREATE_DOCUMENT) in the system document picker of another app, and that app returns to Aegis '
                     '(BackupsPreferencesFragment.java:255-271)')
ENV_BIOMETRIC_FAIL = ('the sensor reads a fingerprint or face that does not match (onAuthenticationFailed), or the prompt ends with an error '
                      'such as a cancel or a lockout (onAuthenticationError; BiometricSlotInitializer.java:116-130)')
ENV_AUTOFILL = ('an autofill service is enabled in the system settings and the framework asks this window for its structure '
                '(View.java:7512-7535) or a field takes focus (View.java:6970,12196)')

# ------------------------------------------------------------------ STATE gates (an earlier in-app action or a stored setting)
ST_VAULT_FILE = 'A vault file exists in the app data (created by an earlier intro run; MainActivity.onStart reads it)'
ST_PLAIN_VAULT_FILE = ('A plain-text vault file exists in the app data, saved by an earlier intro run that chose no security '
                       '(cross-run state, no producer in this run; MainActivity.onStart reads it, MainActivity.java:951-973)')
ST_ENCRYPTED_VAULT_FILE = ('An encrypted vault file exists in the app data, saved by an earlier intro run that chose a password '
                           'or biometrics (cross-run state, no producer in this run; MainActivity.onStart reads it, MainActivity.java:950-977)')
ST_YANDEX_ENTRY = 'The vault file holds a Yandex entry (OtpInfo.fromJson type YandexInfo.ID, OtpInfo.java:131-133)'
ST_MOTP_ENTRY = ('The vault file holds a MOTP entry with a PIN, added in an earlier run (OtpInfo.fromJson type MotpInfo.ID, '
                 'OtpInfo.java:134-136; MotpInfo.toJson writes the PIN, MotpInfo.java:56)')
ST_HOTP_ENTRY = 'The vault file holds a HOTP entry (OtpInfo.fromJson type HotpInfo.ID, OtpInfo.java:128-129)'
ST_SHOW_NEXT_CODE = 'The next code is shown for this entry: the entry is TOTP or MOTP and the show-next-code setting is on (EntryHolder.java:144,307)'
ST_HOLDERS_BOUND = 'At least one entry row is bound, so EntryAdapter.onBindViewHolder has added an EntryHolder to _holders (EntryAdapter.java:569)'
ST_VAULT_ENTRIES = 'The vault holds at least one entry (the loop in Vault.toJson(EntryFilter) runs, Vault.java:9-12)'
# stage 5 batch 7: own label for the calculateShownEntries loop (ST_VAULT_ENTRIES is shared by three other edges, left as is)
ST_ENTRY_LIST_NONEMPTY = 'the entry list passed in is not empty: the for loop at EntryAdapter.java:301 runs once per entry'
ST_IMPORTED = 'The Welcome slide imported a vault file in this intro run (intro state "imported")'
ST_NOT_IMPORTED = 'The Welcome slide did not import a vault in this intro run (intro state "imported" is false, IntroActivity.java:86-100)'
ST_PASSWORD_SLOT = 'The vault has a password slot (the intro chose the password security)'
ST_BIO_SLOT = ('The vault has a biometric slot and a key store key, saved by an earlier intro run that chose biometrics '
               '(cross-run state, no producer in this run)')
ST_REMINDER_DUE = ('A password reminder is due: the reminder timestamp saved by an earlier run is old enough '
                   '(Preferences.java:138-146; cross-run state, no producer in this run)')
ST_UNLOCKED = 'The vault is loaded in this process and has not been locked since'
ST_LIST_LOADED = 'This MainActivity instance has loaded the entry list (loadEntries ran)'
ST_ACTIVITY_OPEN = 'An AegisActivity is open and registered as a lock listener (AegisActivity.java:77)'
ST_PANIC_ON = 'The panic trigger preference is on (pref_panic_trigger, default off; Preferences.java:107-108)'
ST_FAB_OPEN = 'The floating action menu is open (FabMenuHelper.open ran; FabMenuHelper.java:76-102)'
ST_SEARCH_OPEN = 'The search box is expanded, opened by the search icon or by focus (MainActivity.java:1021-1024,1060-1064)'
ST_ACTION_MODE = 'The selection action mode is open (startActionMode ran; MainActivity.java:1303-1308)'
ST_ASSIGN_DIALOG = 'The assign-groups dialog is open (startAssignGroupsDialog ran; MainActivity.java:533-601)'
ST_SAVE_CHIP = 'The save-filter chip is visible after a group filter change (setSaveChipVisibility(true), MainActivity.java:335,373-377)'
ST_ERROR_CARD = 'The main screen shows an error card (updateErrorCard set an ErrorCardInfo, MainActivity.java:1163-1197)'
ST_VAULT_UNREADABLE = ('The vault file exists but cannot be read (VaultRepository.readVaultFile throws, MainActivity.java:954-955); '
                       'an earlier run left it unreadable, and no step on any route writes it')
ST_ICON_PACK_INSTALLED = ('An icon pack is already installed in the icons folder from an earlier run '
                          '(IconPackManager.java:33 rescans the folder at startup)')
ST_SEARCH_IN_GROUPS = ('SEARCH_IN_GROUPS is set in preferences and the app relaunched '
                       '(the mask is read once at MainActivity.onCreate, MainActivity.java:234; '
                       'set by BehaviorPreferencesFragment.java:57)')
ST_SUBMITTED_QUERY_SAVED = ('A search query was submitted in this MainActivity instance and saved to the instance bundle '
                          '(MainActivity.java:1040 sets _submittedSearchQuery; :419-420 saves it; :204-205 restores it)')
ST_CLIPBOARD_DIALOG = ('The clipboard import dialog is open (startEditEntryActivity found a valid otpauth link on the clipboard; '
                       'MainActivity.java:476-491)')
ST_DELETE_DIALOG = 'The delete-entries dialog is open (showDeleteEntriesDialog ran; MainActivity.java:1508-1516)'
ST_SVG_PICK = 'The icon picker returned an SVG file and its import task was started (EditEntryActivity.java:148-158)'
ST_SETTINGS_IMPORT = 'The Settings import picker returned a file and its import task was started (ImportExportPreferencesFragment.java:146-158)'
ST_CAMERA_READY = 'The camera provider is ready and a lens exists: the camera switch icon is set (ScannerActivity.java:70, 79-88)'
ST_BIOMETRICS_AVAILABLE = 'Biometrics are available on the device (BiometricsHelper.isAvailable returns true, helpers/BiometricsHelper.java:27-29); the biometrics row is enabled only then (SecurityPreferencesFragment.java:277)'
ST_SECURITY_NONE = 'The intro security picker chose none, so the setup slide is skipped (IntroActivity.java:50-55)'
ST_PAGE_UNFINISHED = 'The current intro slide is not finished (its isFinished returned false; IntroBaseActivity.java:84-88)'
ST_ENCRYPTION_OFF = 'The vault is not encrypted: Vault.isEncryptionEnabled is false, so the Encryption switch opens the set-password dialog (SecurityPreferencesFragment.java:83)'
ST_VAULT_ENCRYPTED = 'The vault is encrypted: VaultRepository.isEncryptionEnabled is true (the vault has credentials, VaultRepository.java:352-354), so a save writes crypt parameters (VaultRepository.java:119-121)'
ST_ICONS_NOT_OPTIMIZED = 'The vault icons are not marked optimised yet: Vault.areIconsOptimized is false (MainActivity.java:767)'
ST_ENTRY_CHANGED = 'The edit page has unsaved changes: a field was edited, so the back callback is enabled (EditEntryActivity.java:955-957, 966-976)'
ST_GOOGLE_EXPORTABLE = ('The vault holds a TOTP or HOTP entry with SHA-1 and 6 digits, so the Google Authenticator export is not empty '
                        '(ImportExportPreferencesFragment.java:352-363)')

ENV_KINDS_OF = {
    ENV_VIEW: ['other_app'], ENV_SEND: ['other_app'], ENV_PANIC: ['other_app'], ENV_QS: ['other_app'], ENV_SHORTCUT: ['other_app'],
    ENV_SCREEN_OFF: ['system_event'], ENV_BOOT: ['system_event'], ENV_BACKUP: ['system_event'], ENV_RESTORE: ['system_event'],
    ENV_PICKER: ['other_app'], ENV_PICKER_ICON: ['other_app'], ENV_BIOMETRIC: ['hardware'],
    ENV_CAMERA: ['permission'], ENV_CAMERA_GRANTED: ['permission'], ENV_QR_CODE: ['hardware'], ENV_CLIPBOARD: ['other_app'], ENV_PICK_IMAGE: ['other_app'], ENV_PICK_ICON: ['other_app'],
    ENV_AUTO_TIME_OFF: ['time'], ENV_CLOCK_FORWARD: ['time'],ENV_EXPORT_RESULT: ['other_app'], ENV_BACKUP_RESULT: ['other_app'],
    ENV_BIOMETRIC_FAIL: ['hardware'], ENV_AUTOFILL: ['other_app'],
    ENV_PICKER_SETTINGS: ['other_app'], ENV_PANIC_SENDER: ['other_app'], ENV_INSTALLED_GA: ['other_app'], ENV_ROOT: ['other'],
}
STATE_KINDS_OF = {
    ST_VAULT_FILE: ['file'], ST_PLAIN_VAULT_FILE: ['file'], ST_ENCRYPTED_VAULT_FILE: ['file'], ST_REMINDER_DUE: ['settings'], ST_IMPORTED: ['data'], ST_NOT_IMPORTED: ['data'], ST_PASSWORD_SLOT: ['data'], ST_BIO_SLOT: ['data'], ST_SEARCH_IN_GROUPS: ['settings'],
    ST_UNLOCKED: ['session'], ST_LIST_LOADED: ['session'], ST_ACTIVITY_OPEN: ['session'], ST_PANIC_ON: ['settings'],
    ST_FAB_OPEN: ['session'], ST_SEARCH_OPEN: ['session'], ST_ACTION_MODE: ['session'], ST_ASSIGN_DIALOG: ['session'],
    ST_SAVE_CHIP: ['session'], ST_ERROR_CARD: ['settings'], ST_VAULT_UNREADABLE: ['file'], ST_ICON_PACK_INSTALLED: ['file'], ST_CLIPBOARD_DIALOG: ['session'], ST_DELETE_DIALOG: ['session'],
    ST_SECURITY_NONE: ['data'], ST_PAGE_UNFINISHED: ['session'], ST_ENCRYPTION_OFF: ['data'],
    ST_VAULT_ENCRYPTED: ['data'], ST_ICONS_NOT_OPTIMIZED: ['data'], ST_ENTRY_CHANGED: ['session'],
    ST_SHOW_NEXT_CODE: ['settings'], ST_HOLDERS_BOUND: ['session'], ST_SVG_PICK: ['session'], ST_SETTINGS_IMPORT: ['session'], ST_CAMERA_READY: ['session'], ST_BIOMETRICS_AVAILABLE: ['session'],
    ST_GOOGLE_EXPORTABLE: ['data'], ST_YANDEX_ENTRY: ['data'], ST_MOTP_ENTRY: ['data'], ST_HOTP_ENTRY: ['data'], ST_VAULT_ENTRIES: ['data'], ST_ENTRY_LIST_NONEMPTY: ['data'],
    ST_SUBMITTED_QUERY_SAVED: ['session'],
}

# ------------------------------------------------------------------ framework evidence (FW-SRC lines were printed and read; INFERRED where the source was not read)
FW_APP_CREATE = 'FW-SRC core/java/android/app/ActivityThread.java:5740 (the system calls Application.onCreate)'
FW_CREATE = ('FW-SRC core/java/android/app/ActivityThread.java:2729-2731,2741 '
             '(the system calls Activity.onCreate, then performStart)')
FW_RESUME = 'INFERRED Activity.onResume follows onStart (ActivityThread performResume was not printed)'
FW_RESULT = ('FW-SRC core/java/android/app/ActivityThread.java:4253-4265 '
             '(deliverResults passes each result to dispatchActivityResult of the starting activity)')
FW_FINISH = 'FW-SRC core/java/android/app/Activity.java:5526-5527 (finish)'
FW_BACK = ('FW-SRC core/java/android/app/Activity.java:3001-3010 '
           '(the platform onBackPressed; not reached when an OnBackPressedCallback is enabled)')
FW_CLICK = 'FW-SRC core/java/android/view/View.java:6289-6296 (performClick calls the OnClickListener.onClick)'
FW_ASYNC = ('FW-SRC core/java/android/os/AsyncTask.java:594-595 (execute), 632-650 (executeOnExecutor), '
            '326-339 (doInBackground at 333), 369-374 (postResult), 705-713 (handleMessage), 691-697 (finish calls onPostExecute at 695)')
FW_LAUNCHER = 'INFERRED androidx.activity.result: the launcher callback runs with the result (androidx source not cached)'
FW_DISPATCH = 'INFERRED androidx.activity: the OnBackPressedDispatcher calls handleOnBackPressed of the enabled callback (androidx source not cached)'
FW_BIOPROMPT = 'INFERRED androidx.biometric.BiometricPrompt calls the AuthenticationCallback methods (androidx source not cached)'
FW_LIFECYCLE = 'INFERRED androidx.lifecycle: ProcessLifecycleOwner calls the observer with ON_STOP when the app goes to the background (androidx source not cached)'
FW_TILE = 'INFERRED android.service.quicksettings.TileService: the system calls onClick when the tile is tapped (source not read)'
FW_BACKUP = 'INFERRED android.app.backup.BackupAgent: the system calls onFullBackup and onRestoreFile for the manifest backupAgent (source not read)'
FW_RECEIVER = 'INFERRED android.content.BroadcastReceiver: the system calls onReceive for a manifest or registered receiver (source not read)'
FW_APPINTRO = 'INFERRED AppIntro library: onBeforeSlideChanged is called when the slide changes (library source not cached)'
FW_STATE_FINISH = 'INFERRED Activity.finishAffinity and finishAndRemoveTask close the task (framework source not read)'
# batch 1 (MainActivity, FabMenuHelper): framework callbacks not read yet, so all are INFERRED
FW_SEARCH = 'INFERRED androidx.appcompat SearchView calls its query, focus, close and search-click listeners (AppCompat source not read)'
FW_ACTIONMODE = ('INFERRED androidx.appcompat: startSupportActionMode calls Callback.onCreateActionMode and onPrepareActionMode; '
                 'ActionMode.finish calls onDestroyActionMode (source not read)')
FW_FAB_ANIM = 'INFERRED android.view.ViewPropertyAnimator and ValueAnimator call the start, end and update listeners (framework source not read)'
FW_POST = 'INFERRED View.postDelayed runs the Runnable on the main thread after the delay (framework source not read)'
FW_OPTIONS = 'INFERRED androidx.appcompat: onCreateOptionsMenu runs after onCreate, onOptionsItemSelected on a menu tap (source not read)'
FW_MENU = 'INFERRED androidx.appcompat: a tap on a toolbar menu item calls onOptionsItemSelected (source not read)'
FW_KEYS = 'INFERRED Activity.dispatchKeyEvent calls onKeyDown for a key press (framework source not read)'
FW_PERMRESULT = 'INFERRED ActivityCompat.requestPermissions: the system calls onRequestPermissionsResult with the grant results (source not read)'
FW_SAVE = 'INFERRED Activity: on API 27 the framework saves the instance state after onPause and before onStop (framework source not read)'
FW_RESTORE = 'INFERRED Activity: the framework calls onRestoreInstanceState after onStart when a saved state exists (framework source not read)'
FW_RECREATE = 'INFERRED Activity.recreate destroys the activity (onDestroy) and creates it again (framework source not read)'
FW_DIALOG = 'INFERRED androidx.appcompat AlertDialog: show() runs the OnShowListener (AppCompat source not read)'
FW_ITEM = 'INFERRED AdapterView.OnItemClickListener: a tap on a dropdown row calls onItemClick (framework source not read)'
FW_CHECK = 'INFERRED CompoundButton.OnCheckedChangeListener: a chip tap calls onCheckedChanged (Material source not read)'

# ------------------------------------------------------------------ pages (screens of the model)
SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, a link or shared content from another app, a Quick Settings tile, the panic app, a system broadcast, a backup',
    'S_PROCESS': 'The application is created and the process runs: every component starts from here',
    'S_EXIT': 'Aegis leaves the screen: the activity or the task is finished, no vault is shown',
    'S_INTRO_WELCOME': 'Intro slide 1 (Welcome): Import button, Next and Previous',
    'S_INTRO_PICKER': 'Intro slide 2 (security picker): none, password, biometrics; Next and Previous',
    'S_INTRO_SETUP': 'Intro slide 3 (security setup): password fields or biometric setup; Next and Previous',
    'S_INTRO_DONE': 'Intro last slide (Done)',
    'S_SCANNER': 'QR scanner (ScannerActivity): the camera preview; the camera switch icon when two lenses exist',
    'S_AUTH': 'Unlock screen (AuthActivity): password field, unlock button, biometric button when a biometric slot exists, Back',
    'S_LIST': 'Main screen with the entry list (vault loaded): toolbar, lock icon, FAB, group chips',
    'S_SETTINGS_MAIN': 'Settings main list (MainPreferencesFragment rows): the categories that open a sub-page',
    'S_MAIN_STOPPED': 'Main screen stopped (Home key, another app or a system screen on top)',
}


def gui(src, dst, text, kind='GUI', **kw):
    # The build accepts GUI edges only from a page (S_*). A tap inside a dialog that a method opened (Dialogs.showX, or a listener
    # method such as lambda$...) starts at that method, so it is written as FRAMEWORK: the framework dispatches the click (FW_CLICK).
    if not src.startswith('S_'):
        kind = 'FRAMEWORK'
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)


# Auto edges between Dagger / Hilt generated classes (they are compiled into the APK) are direct calls, so they are explicit.
# The build's NONSTD_HINT regex flags any text that contains "Dagger", so the class is set here instead of by reword.
HILT_MARKERS = ('Dagger', 'HiltComponents', 'Hilt_')


def CLASSIFY(x):
    if x.get('auto') and x['kind'] == 'CALL' and any(m in x['src'] or m in x['dst'] for m in HILT_MARKERS):
        return 'explicit'
    if x['kind'] == 'FRAMEWORK' and 'dagger' in (x.get('evidence') or '').lower():
        return ('non_standard', 'Dagger / Hilt dependency injection: the library makes the link to the generated component')
    return None


# Calls whose bytecode line is one or more lines off, and calls the name check cannot match (checked by hand against the source)
FIX_LINES = {
    ('AegisGlideModule.registerComponents', 'SvgBytesDecoder.<init>', 'SRC AegisGlideModule.java:25 (bytecode)'): 'SRC AegisGlideModule.java:26 (bytecode line was 25)',
    ('AegisGlideModule.registerComponents', 'SvgDecoder.<init>', 'SRC AegisGlideModule.java:24 (bytecode)'): 'SRC AegisGlideModule.java:25 (bytecode line was 24)',
    ('AssignIconsActivity.onAssignIconEntryClick', 'IconPack.getName', 'SRC AssignIconsActivity.java:190 (bytecode)'): 'SRC AssignIconsActivity.java:191 (bytecode line was 190)',
    ('AssignIconsActivity.onCreate', 'IconPack.getName', 'SRC AssignIconsActivity.java:96 (bytecode)'): 'SRC AssignIconsActivity.java:97 (bytecode line was 96)',
    ('EditEntryActivity.startIconSelection', 'IconPack.getName', 'SRC EditEntryActivity.java:586 (bytecode)'): 'SRC EditEntryActivity.java:587 (bytecode line was 586)',
    ('EntryAdapter.doesAnyGroupMatchSearchFilter', 'VaultGroup.getName', 'SRC EntryAdapter.java:227 (bytecode)'): 'SRC EntryAdapter.java:228 (bytecode line was 227)',
    ('EntryAdapter.onItemMove', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'SRC EntryAdapter.java:389 (bytecode)'): 'SRC EntryAdapter.java:386-389 (bytecode line was 389)',
    ('EntryAdapter.refreshEntryList', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'SRC EntryAdapter.java:281 (bytecode)'): 'SRC EntryAdapter.java:278-281 (bytecode line was 281)',
    ('EntryAdapter.setEntries', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'SRC EntryAdapter.java:182 (bytecode)'): 'SRC EntryAdapter.java:179-182 (bytecode line was 182)',
    ('EntryAdapter.setErrorCardInfo', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'SRC EntryAdapter.java:159 (bytecode)'): 'SRC EntryAdapter.java:157 (bytecode line was 159)',
    ('GlideHelper.setCommonOptions', 'GlideHelper$ViewReadyListener.<init>', 'SRC GlideHelper.java:59 (bytecode)'): 'SRC GlideHelper.java:60 (bytecode line was 59)',
    ('GoogleAuthInfo$Export.getMissingIndices', 'GoogleAuthInfo$Export.getBatchIndex', 'SRC GoogleAuthInfo.java:370 (bytecode)'): 'SRC GoogleAuthInfo.java:371 (bytecode line was 370)',
    ('IconAdapter.loadIcons', 'IconPack$Icon.getCategory', 'SRC IconAdapter.java:55 (bytecode)'): 'SRC IconAdapter.java:56 (bytecode line was 55)',
    ('IconPickerDialog.lambda$create$2', 'IconPack.getName', 'SRC IconPickerDialog.java:131 (bytecode)'): 'SRC IconPickerDialog.java:132 (bytecode line was 131)',
    ('PreferencesActivity.onCreate', 'PreferencesActivity$FragmentResumeListener.<init>', 'SRC PreferencesActivity.java:32 (bytecode)'): 'SRC PreferencesActivity.java:33 (bytecode line was 32)',
    ('Slot.fromJson', 'SCryptParameters.<init>', 'SRC Slot.java:140 (bytecode)'): 'SRC Slot.java:136-140 (bytecode line was 140)',
    ('SlotList.findBackupPasswordSlots', 'PasswordSlot.isBackup', 'SRC SlotList.java:60 (bytecode)'): 'SRC SlotList.java:61 (bytecode line was 60)',
    ('VaultFile.exportable', 'VaultFile$Header.<init>', 'SRC VaultFile.java:131 (bytecode)'): 'SRC VaultFile.java:129 (bytecode line was 131)',
    ('VaultFile.exportable', 'VaultFile.<init>(Object,Header)', 'SRC VaultFile.java:131 (bytecode)'): 'SRC VaultFile.java:129 (bytecode line was 131)',
    ('MainActivity.checkIconOptimization', 'UUIDMap$Value.getUUID', 'SRC MainActivity.java:769 (bytecode)'): 'SRC MainActivity.java:772 (VaultEntry::getUUID method reference in the collect; the bytecode line table says 769)',
    ('ImportEntriesActivity.processDecryptedImporterState', 'UUIDMap$Value.getUUID', 'SRC ImportEntriesActivity.java:216 (bytecode)'): 'SRC ImportEntriesActivity.java:219 (VaultEntry::getUUID method reference in the collect; the bytecode line table says 216)',
    ('ImportEntriesActivity.showWipeEntriesDialog', 'ImportEntriesActivity.saveAndFinish', 'SRC ImportEntriesActivity.java:255 (bytecode)'): 'SRC ImportEntriesActivity.java:258 (this::saveAndFinish method reference; the bytecode line table says 255)',
    ('BackupsPreferencesFragment.lambda$onCreatePreferences$5', 'BackupsPreferencesFragment.saveAndDisableBackupReminder', 'SRC BackupsPreferencesFragment.java:99 (bytecode)'): 'SRC BackupsPreferencesFragment.java:102 (this::saveAndDisableBackupReminder method reference; the bytecode line table says 99)',
    ('ImportEntriesActivity.saveAndFinish', 'UUIDMap.iterator', 'SRC ImportEntriesActivity.java:278 (bytecode)'): 'SRC ImportEntriesActivity.java:278 (for-each loop: the iterator() call is implicit)',
    ('WinAuthImporter$State.convert', 'UUIDMap.iterator', 'SRC WinAuthImporter.java:39 (bytecode)'): 'SRC WinAuthImporter.java:39 (for-each loop: the iterator() call is implicit)',
    ('Vault.toJson(EntryFilter)', 'UUIDMap.iterator', 'SRC Vault.java:38 (bytecode)'): 'SRC Vault.java:38 (for-each loop: the iterator() call is implicit)',
    ('SlotList.toJson', 'UUIDMap.iterator', 'SRC SlotList.java:16 (bytecode)'): 'SRC SlotList.java:16 (for-each loop: the iterator() call is implicit)',
    # Row 23 variant: auto replication onto SlotList.toJson@RAW strips the for-each qualifier to bare (bytecode),
    # which check 4 then flags (line 16 is a for-each, the iterator() call is implicit). Same correction as the base edge.
    ('SlotList.toJson@RAW', 'UUIDMap.iterator', 'SRC SlotList.java:16 (bytecode)'): 'SRC SlotList.java:16 (for-each loop: the iterator() call is implicit)',
    ('SlotList.find', 'UUIDMap.iterator', 'SRC SlotList.java:40 (bytecode)'): 'SRC SlotList.java:40 (for-each loop: the iterator() call is implicit)',
    ('SlotList.findAll', 'UUIDMap.iterator', 'SRC SlotList.java:50 (bytecode)'): 'SRC SlotList.java:50 (for-each loop: the iterator() call is implicit)',
    ('SlotList.exportable', 'UUIDMap.iterator', 'SRC SlotList.java:90 (bytecode)'): 'SRC SlotList.java:90 (for-each loop: the iterator() call is implicit)',
    ('IntroActivity.onCreate', 'IntroBaseActivity.addSlide@IntroActivity', 'SRC IntroActivity.java:41 (bytecode)'): 'SRC IntroActivity.java:38-41 (bytecode line was 41; addSlide(WelcomeSlide) is line 38)',
    ('AegisActivity.<init>', 'Hilt_AegisActivity.<init>()', 'SRC AegisActivity.java:45 (bytecode)'): 'INFERRED Hilt superclass: AegisActivity extends Hilt_AegisActivity only in the Hilt-rewritten build class (the generated file is not in the source tree; source AegisActivity.java:45 declares extends AppCompatActivity); the bytecode of AegisActivity.<init> makes the implicit super() call (bytecode line table: AegisActivity.java:45)',
}
# Generated classes are compiled into the APK; their source is not in the tree, so the line is not a source citation
GENERATED_FILES = (
    'AppDatabase_Impl.java', 'AuditLogDao_Impl.java', 'DaggerAegisApplication_HiltComponents_SingletonC.java',
    'GeneratedAppGlideModuleImpl.java', 'GeneratedRequestManagerFactory.java', 'GlideOptions.java', 'GlideRequests.java',
    'GoogleAuthProtos.java', 'Hilt_AegisActivity.java', 'Hilt_AegisApplication.java', 'Hilt_AuditLogPreferencesFragment.java',
    'Hilt_IconPacksManagerFragment.java', 'Hilt_PreferencesFragment.java', 'Hilt_VaultLockReceiver.java',
)


def EDIT(x):
    import re
    ev = x.get('evidence') or ''
    for (src_, dst_, old_), new_ in FIX_LINES.items():
        if x['src'] == src_ and x['dst'] == dst_ and old_ in ev:
            ev = ev.replace(old_, new_)
    m = re.search(r'SRC (\S+\.java):(\d+) \(bytecode\)', ev)
    if m and m.group(1) in GENERATED_FILES:
        ev = ev.replace(m.group(0), 'INFERRED generated code (%s is not in the source tree; the call is in the build class, line %s)' % (m.group(1), m.group(2)))
    x['evidence'] = ev


# ================================================================== A. process start and the components that start from it
e('S_ENTRY', 'AegisApplication.<init>', 'ENTRY', 'Any outside trigger starts the app process; the application class is created first, except in a backup or restore start, which uses the base Application class',
  guard='not a full backup or restore start (FW ActivityThread.java:5713-5715)',
  evidence='SRC AndroidManifest.xml:21-27 (android:name=".AegisApplication", backupAgent=".AegisBackupAgent")')
e('AegisApplication.<init>', 'Hilt_AegisApplication.onCreate', 'LIFECYCLE',
  'Application.onCreate: the Hilt-generated superclass onCreate runs first (Hilt injection), then AegisApplicationBase.onCreate',
  evidence=FW_APP_CREATE + '; INFERRED Hilt rewrites the superclass: AegisApplication extends Hilt_AegisApplication (generated file, not in the source tree; source AegisApplication.java:6 has no onCreate)')
e('AegisApplicationBase.onCreate', 'S_PROCESS', 'ENTERS', 'the application is created: the process can start a component',
  evidence='SRC AegisApplicationBase.java:45-67; ' + FW_APP_CREATE)
# batch 4: the Hilt component is built the first time the application asks for it (library code; the build chain after it is in the bytecode)
e('Hilt_AegisApplication.generatedComponent', 'Hilt_AegisApplication$1.get', 'FRAMEWORK',
  'ApplicationComponentManager asks the anonymous ComponentSupplier for the singleton component the first time it is needed',
  evidence='INFERRED dagger.hilt.android.internal.managers.ApplicationComponentManager (Hilt library source not read); generated Hilt_AegisApplication.java:36 (auto_calls row generatedComponent -> componentManager)')
# batch 4: the framework attaches the activity context, then Hilt injects the activity and builds its component (library code, INFERRED)
e('AegisActivity.onCreate', 'Hilt_AegisActivity$1.onContextAvailable', 'FRAMEWORK',
  'the framework calls the OnContextAvailableListener registered in _initHiltInternal, inside the super.onCreate call of the activity\'s onCreate',
  guard='AegisActivity.onCreate has reached its super.onCreate call (AegisActivity.java:67; the framework runs the listener inside that call); MainActivity.onCreate calls AegisActivity.onCreate first (MainActivity.java:194)',
  evidence='INFERRED androidx.activity ComponentActivity: context-available listeners run inside onCreate (framework source not read); generated Hilt_AegisActivity.java:43 (auto_calls row _initHiltInternal -> $1.<init>); SRC ui/AegisActivity.java:61-67 (onCreate, super.onCreate at 67); SRC ui/MainActivity.java:193-195 (onCreate, super.onCreate at 194, setContentView at 195)')
for _dst, _note in [
    ('DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.retainedComponentBuilder', 'the activity component manager asks the application component for the retained-component builder (Hilt EntryPoint)'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCBuilder.build', 'the library builds the retained component from the builder it was given'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl.activityComponentBuilder', 'the library asks the retained component for the activity component builder'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.activity', 'the library sets the activity on the activity component builder'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.build', 'the library builds the activity component (ActivityCImpl), which injects this activity'),
]:
    e('Hilt_AegisActivity.generatedComponent', _dst, 'FRAMEWORK', _note,
      evidence='INFERRED dagger.hilt.android.internal.managers.ActivityComponentManager and ActivityRetainedComponentManager (Hilt library source not read); generated Hilt_AegisActivity.java:77 (auto_calls row generatedComponent -> componentManager)')
# the runtime receiver for screen-off and the lifecycle observer are registered in onCreate (not traversed: REGISTER)
e('AegisApplicationBase.onCreate', 'VaultLockReceiver.onReceive', 'REGISTER', 'registerReceiver(VaultLockReceiver) for ACTION_SCREEN_OFF',
  evidence='SRC AegisApplicationBase.java:49-51')
e('AegisApplicationBase.onCreate', 'AegisApplicationBase$AppLifecycleObserver.onStateChanged', 'REGISTER',
  'ProcessLifecycleOwner.addObserver(new AppLifecycleObserver())', evidence=FW_LIFECYCLE + '; SRC AegisApplicationBase.java:54')

# system broadcasts (the receivers are delivered by the system to the app process)
e('S_PROCESS', 'VaultLockReceiver.onReceive', 'SYSTEM', 'the screen turns off (the runtime receiver gets ACTION_SCREEN_OFF)',
  env=ENV_SCREEN_OFF,
  evidence=FW_RECEIVER + '; SRC AegisApplicationBase.java:49-51; SRC receivers/VaultLockReceiver.java:24-34')
e('S_PROCESS', 'QsTileRefreshReceiver.onReceive', 'ENTRY', 'BOOT_COMPLETED or USER_UNLOCKED reaches the manifest receiver',
  env=ENV_BOOT, evidence='SRC AndroidManifest.xml:140-147; SRC receivers/QsTileRefreshReceiver.java:17-30; ' + FW_RECEIVER)

# MainActivity entries
e('S_PROCESS', 'MainActivity.<init>', 'ENTRY', 'Tap the Aegis icon in the launcher (MAIN / LAUNCHER)',
  gui=['Tap the Aegis icon in the launcher'], evidence='SRC AndroidManifest.xml:44-51')
e('S_PROCESS', 'MainActivity.<init>', 'ENTRY', 'another app opens an otpauth:// link (VIEW)',
  env=ENV_VIEW, evidence='SRC AndroidManifest.xml:52-59')
e('S_PROCESS', 'MainActivity.<init>', 'ENTRY', 'another app shares text or images (SEND / SEND_MULTIPLE)',
  env=ENV_SEND, evidence='SRC AndroidManifest.xml:60-66')
e('MainActivity.<init>', 'MainActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate after the constructor',
  evidence=FW_CREATE + '; SRC ui/MainActivity.java:192-194')
e('MainActivity.<init>', 'MainActivity.lambda$new$0', 'REGISTER', 'authResultLauncher callback', evidence='SRC ui/MainActivity.java:134-140')
e('MainActivity.<init>', 'MainActivity.lambda$new$1', 'REGISTER', 'introResultLauncher callback', evidence='SRC ui/MainActivity.java:142-148')
e('MainActivity.onCreate', 'MainActivity.onStart', 'LIFECYCLE', 'Activity.onStart after onCreate',
  evidence=FW_CREATE + '; SRC ui/MainActivity.java:938-940')
e('MainActivity.onStart', 'AegisActivity.onResume', 'LIFECYCLE', 'Activity.onResume (MainActivity has no own onResume)',
  evidence=FW_RESUME + '; SRC ui/AegisActivity.java:89-92')

# tiles
e('S_PROCESS', 'LaunchAppTileService.onClick', 'ENTRY', 'the Aegis tile is tapped in Quick Settings',
  env=ENV_QS, evidence='SRC AndroidManifest.xml:108-119; SRC LaunchAppTileService.java:29-43; ' + FW_TILE)
e('LaunchAppTileService.onClick', 'MainActivity.<init>', 'INTENT', 'starts MainActivity (NEW_TASK | CLEAR_TASK, ACTION_MAIN)',
  evidence='SRC LaunchAppTileService.java:29-43')
e('S_PROCESS', 'LaunchScannerTileService.onClick', 'ENTRY', 'the scanner tile is tapped in Quick Settings',
  env=ENV_QS, evidence='SRC AndroidManifest.xml:121-132; SRC LaunchScannerTileService.java:29-44; ' + FW_TILE)
e('LaunchScannerTileService.onClick', 'MainActivity.<init>', 'INTENT', 'starts MainActivity with the extra action = scan',
  evidence='SRC LaunchScannerTileService.java:29-44')

# panic app: the trigger needs the preference on (ST_PANIC_ON), a trusted sender and the TRIGGER action
e('S_PROCESS', 'PanicResponderActivity.<init>', 'ENTRY', 'the panic app starts PanicResponderActivity',
  env=ENV_PANIC_SENDER, cls='non_standard', via='intent resolved by action name: the system matches the panic app action info.guardianproject.panic.action.TRIGGER to the manifest intent-filter (AndroidManifest.xml:91-101)',
  evidence='SRC AndroidManifest.xml:91-101; SRC ui/PanicResponderActivity.java:19-22')
e('PanicResponderActivity.<init>', 'PanicResponderActivity.onCreate', 'LIFECYCLE',
  'Activity.onCreate of the panic responder; its super.onCreate runs AegisActivity.onCreate first, which sets _prefs (AegisActivity.java:63)',
  evidence=FW_CREATE + '; SRC ui/PanicResponderActivity.java:19-20; SRC ui/AegisActivity.java:61-67')
e('PanicResponderActivity.onCreate', 'S_EXIT', 'ENTERS', 'finish(): the panic preference is off (toast) or the intent is not the TRIGGER action',
  guard='pref_panic_trigger is off (22-26), or no intent or not the TRIGGER action (39-46)',
  evidence='SRC ui/PanicResponderActivity.java:22-26,39-46; ' + FW_STATE_FINISH)
e('PanicResponderActivity.onCreate', 'VaultRepository.deleteFile', 'CALL', 'the TRIGGER action deletes the vault file',
  guard='pref_panic_trigger is on (ST_PANIC_ON) and the sender is trusted (BuildConfig.TEST is an AtomicBoolean(false) in build.gradle:37, so the check runs) and the action is the TRIGGER',
  needs_state=ST_PANIC_ON, evidence='SRC ui/PanicResponderActivity.java:29-40; SRC app/build.gradle:37')
e('PanicResponderActivity.onCreate', 'VaultManager.lock', 'CALL', 'the TRIGGER action locks the vault (lock(false))',
  guard='pref_panic_trigger is on and the sender is trusted and the action is the TRIGGER',
  needs_state=ST_PANIC_ON, evidence='SRC ui/PanicResponderActivity.java:41')
e('PanicResponderActivity.onCreate', 'PanicResponderActivity.finishApp', 'CALL', 'the TRIGGER action ends the app',
  guard='pref_panic_trigger is on and the sender is trusted and the action is the TRIGGER',
  needs_state=ST_PANIC_ON, evidence='SRC ui/PanicResponderActivity.java:42')
e('PanicResponderActivity.finishApp', 'ExitActivity.exitAppAndRemoveFromRecents', 'CALL', 'the app task is removed from recents',
  evidence='SRC ui/PanicResponderActivity.java:49-52')
e('ExitActivity.exitAppAndRemoveFromRecents', 'ExitActivity.<init>', 'INTENT', 'starts ExitActivity (NEW_TASK | CLEAR_TASK | NO_ANIMATION | EXCLUDE_FROM_RECENTS)',
  evidence='SRC ui/ExitActivity.java:17-25')
e('ExitActivity.<init>', 'ExitActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of ExitActivity', evidence=FW_CREATE + '; SRC ui/ExitActivity.java:10-15')
e('ExitActivity.onCreate', 'S_EXIT', 'ENTERS', 'finishAndRemoveTask: the task is removed', evidence='SRC ui/ExitActivity.java:14; ' + FW_STATE_FINISH)
e('PanicResponderActivity.finishApp', 'S_EXIT', 'ENTERS', 'finishAndRemoveTask after the exit intent', evidence='SRC ui/PanicResponderActivity.java:51; ' + FW_STATE_FINISH)

# group D M1 (ApkSignaturePin.getSignatures): the sender check runs only with the panic trigger on (PanicResponderActivity.java:22-26) and not in the test build (29)
sup(('PanicResponderActivity.onCreate', 'TrustedIntents.getIntentFromTrustedSender'))
e('PanicResponderActivity.onCreate', 'TrustedIntents.getIntentFromTrustedSender', 'CALL',
  'the panic trigger is on and this is not a test build: the sender is checked',
  guard='the panic trigger is enabled (PanicResponderActivity.java:22-26 finish and return otherwise) and the test build check is false (PanicResponderActivity.java:29; the else branch at 35-36 uses getIntent())',
  needs_state=ST_PANIC_ON, evidence='SRC ui/PanicResponderActivity.java:22-34')
sup(('TrustedIntents.getIntentFromTrustedSender', 'TrustedIntents.isPackageNameTrusted'))
e('TrustedIntents.getIntentFromTrustedSender', 'TrustedIntents.isPackageNameTrusted', 'CALL',
  'the calling package name is known',
  guard='the calling package name is not empty (TrustedIntents.java:106-109); getCallingPackageName returns a package only when this activity was started with startActivityForResult (getCallingActivity, TrustedIntents.java:131-142; the warning at 120-124 says a singleInstance or singleTask activity cannot get the calling activity; without a request code the calling activity is null, FW-SRC core/java/android/app/Activity.java:5384-5399)',
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:104-110,120-124,131-142; FW-SRC core/java/android/app/Activity.java:5384-5399')
sup(('TrustedIntents.checkTrustedSigner(String)', 'TrustedIntents.checkTrustedSigner(Signature[])'))
e('TrustedIntents.checkTrustedSigner(String)', 'TrustedIntents.checkTrustedSigner(Signature[])', 'CALL',
  'the package info is returned', guard='pm.getPackageInfo returns the package (TrustedIntents.java:216)',
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:214-217')
sup(('TrustedIntents.checkTrustedSigner(Signature[])', 'ApkSignaturePin.getSignatures'))
e('TrustedIntents.checkTrustedSigner(Signature[])', 'ApkSignaturePin.getSignatures', 'CALL',
  'the signatures are compared with each trusted pin',
  guard='the signatures pass the checks (TrustedIntents.java:227-231) and a pin is in the list (234); the pins are added earlier in the same onCreate (PanicResponderActivity.java:31-32)',
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:225-235; SRC ui/PanicResponderActivity.java:31-32')

# backup agent: the system calls the agent in the app process
e('S_PROCESS', 'AegisBackupAgent.onFullBackup', 'ENTRY', 'the system runs a full backup of the app data',
  env=ENV_BACKUP, guard='Android backups are enabled (pref_android_backups, default off) or the transfer is device-to-device (D2D, allowed at 51-52)',
  evidence='SRC AegisBackupAgent.java:43-56; SRC AndroidManifest.xml:21-27; ' + FW_BACKUP)
e('S_PROCESS', 'AegisBackupAgent.onRestoreFile', 'ENTRY', 'the system restores the app data from an Android backup',
  env=ENV_RESTORE, evidence='SRC AegisBackupAgent.java:95-112; SRC AndroidManifest.xml:21-27; ' + FW_BACKUP)

# ================================================================== B. MainActivity.onStart: its early returns become guards on the callees
# the bytecode edges from onStart ignore the early returns, so the pairs are suppressed and written by hand with their guards
sup(('MainActivity.onStart', 'MainActivity.startIntroActivity'), ('MainActivity.onStart', 'MainActivity.startAuthActivity'),
    ('MainActivity.onStart', 'MainActivity.loadEntries'), ('MainActivity.onStart', 'MainActivity.checkTimeSyncSetting'),
    ('MainActivity.onStart', 'MainActivity.checkIconOptimization'), ('MainActivity.onStart', 'MainActivity.handleIncomingIntent'),
    ('MainActivity.onStart', 'MainActivity.setGroups'))
e('MainActivity.onStart', 'Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)', 'CALL',
  'the vault file cannot be read: an error dialog is shown and onStart returns (the unlock screen is not started)',
  guard='reading the vault file throws VaultRepositoryException (MainActivity.java:954-955; the catch shows the dialog at 957 and returns at 960); reached only when isVaultInitNeeded() is false (MainActivity.java:942-947) and isVaultLoaded() is false (MainActivity.java:951)',
  needs_state=ST_VAULT_UNREADABLE,
  evidence='SRC ui/MainActivity.java:946-960 (intro return at 946-947; readVaultFile catch at 954-960: showErrorDialog at 957, return at 960)')
e('MainActivity.onStart', 'Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)', 'CALL',
  'the plain-text vault file cannot be loaded: an error dialog is shown and onStart returns',
  guard='the vault file is plain text (not encrypted) and VaultManager.loadFrom throws; the catch shows the dialog at MainActivity.java:968 and returns at 971',
  needs_state=ST_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:963-971 (plain-text branch; loadFrom at 965; catch at 966-971)')
e('MainActivity.onStart', 'MainActivity.startIntroActivity', 'CALL', 'no vault file exists (fresh install): the intro starts and onStart returns',
  guard='vault init needed: no vault file exists', evidence='SRC ui/MainActivity.java:942-948')
e('MainActivity.onStart', 'VaultManager.loadFrom(VaultFile)', 'CALL', 'the plain-text vault file is read and loaded in onStart',
  guard='the vault is not loaded yet and the vault file is not encrypted (MainActivity.java:951-973)', needs_state=ST_PLAIN_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:951-965')
e('OtpInfo.fromJson', 'YandexInfo.<init>(byte[],String)', 'CALL', 'the vault entry has type Yandex and is built from its JSON',
  needs_state=ST_YANDEX_ENTRY, evidence='SRC otp/OtpInfo.java:131-133')

# the vault load chain (group D M4): the loader's own throws and the entry type are written as guards, because the bytecode edges have none
sup(('VaultManager.loadFrom(VaultFile,VaultFileCredentials)', 'VaultRepository.fromFile'), ('Vault.fromJson', 'VaultEntry.fromJson'),
    ('OtpInfo.fromJson', 'HotpInfo.<init>(byte[],String,int,long)'))
e('VaultManager.loadFrom(VaultFile,VaultFileCredentials)', 'VaultRepository.fromFile', 'CALL', 'the vault is read from its file',
  guard='the manager holds no vault yet (VaultManager.java:81-83 throws otherwise)', evidence='SRC vault/VaultManager.java:80-85')
e('Vault.fromJson', 'VaultEntry.fromJson', 'CALL', 'the entry is parsed from the vault JSON',
  guard='the vault version is supported (Vault.java:61-62 throws otherwise) and the entries array holds at least one entry (Vault.java:75-77)',
  evidence='SRC vault/Vault.java:59-63,75-77')
e('OtpInfo.fromJson', 'HotpInfo.<init>(byte[],String,int,long)', 'CALL', 'the vault entry has type HOTP and is built from its JSON',
  guard='the entry type is the HOTP id (OtpInfo.java:121, 128)', needs_state=ST_HOTP_ENTRY, evidence='SRC otp/OtpInfo.java:121,128-129')
sup(('OtpInfo.fromJson', 'TotpInfo.<init>(byte[],String,int,int)'))
e('OtpInfo.fromJson', 'TotpInfo.<init>(byte[],String,int,int)', 'CALL', 'the vault entry has type TOTP and is built from its JSON',
  guard='the entry type is the TOTP id (OtpInfo.java:121, 122)', evidence='SRC otp/OtpInfo.java:121-123')
e('YandexInfo.validateSecret', 'YandexInfo.getNumberOfLeadingZeros', 'CALL',
  'the checksum loop runs; a secret from a QR code (16 bytes) returns before it',
  guard='the Yandex secret is the 26-byte checksummed form (SECRET_FULL_LENGTH; the 16-byte form returns at YandexInfo.java:116-118)',
  evidence='SRC otp/YandexInfo.java:110-118,156')
# batch k (group B): the first-load and the later-start refresh calls, each with its state (loadEntries runs before the call, MainActivity.java:992)
e('MainActivity.onStart', 'EntryListView.onRefreshStart', 'CALL', 'plain-text vault (intro chose no security): the list is loaded, then its codes are refreshed',
  guard='the plain-text vault file is loaded earlier in this onStart call (MainActivity.java:963-965) and this instance has not loaded the list: the else branch at 991-996 runs loadEntries (992) before onRefreshStart (996)',
  needs_state=ST_VAULT_FILE, evidence='SRC ui/MainActivity.java:950-974,991-996; SRC ui/MainActivity.java:1133-1144')
e('MainActivity.onStart', 'EntryListView.onRefreshStart', 'CALL', 'vault unlocked in this process: the list is loaded, then its codes are refreshed',
  guard='the vault is loaded and this instance has not loaded the list: the else branch at 991-996 runs loadEntries (992) before onRefreshStart (996)',
  needs_state=ST_UNLOCKED, evidence='SRC ui/MainActivity.java:976,991-996; SRC ui/MainActivity.java:1133-1144')
e('MainActivity.onStart', 'EntryListView.onRefreshStart', 'CALL', 'the list was loaded by an earlier start: its codes are refreshed',
  guard='the vault is loaded and this instance loaded the list before (the else-if branch at 978-990; the call is at 990)',
  needs_state=ST_LIST_LOADED, evidence='SRC ui/MainActivity.java:976-978,990')
e('MainActivity.onStart', 'MainActivity.checkTimeSyncSetting', 'CALL', 'first list load: time sync check',
  guard='the vault is loaded and this instance has not loaded the list yet', needs_state=ST_UNLOCKED, evidence='SRC ui/MainActivity.java:993')
e('MainActivity.onStart', 'MainActivity.checkIconOptimization', 'CALL', 'first list load: icon optimisation check',
  guard='the vault is loaded and this instance has not loaded the list yet', needs_state=ST_UNLOCKED, evidence='SRC ui/MainActivity.java:994')
e('MainActivity.checkIconOptimization', 'MainActivity.onIconsOptimized', 'CALL', 'no entry icon needs optimising, so the empty result is applied at once',
  guard='the icons are not marked optimised yet and no entry has an icon to optimise (MainActivity.java:767,774-778)',
  needs_state=ST_ICONS_NOT_OPTIMIZED, evidence='SRC ui/MainActivity.java:767-778 (bytecode line 778)')
# batch k (group B): guards on auto CALL edges of the encryption paths (a hand edge with the same pair replaces the auto edge)
e('SecurityPreferencesFragment.lambda$onCreatePreferences$4', 'Dialogs.showSecureDialog', 'CALL', 'the Encryption switch is turned off on an encrypted vault: the disable confirmation dialog opens',
  guard='the vault is encrypted (isEncryptionEnabled is true, SecurityPreferencesFragment.java:83), so the disable dialog is the else branch (85-86)',
  evidence='SRC ui/fragments/preferences/SecurityPreferencesFragment.java:83-86')
e('VaultManager.disableEncryption', 'VaultManager.save', 'CALL', 'the vault is saved as plain text: the credentials were cleared first',
  guard='credentials cleared (VaultManager.java:120), so isEncryptionEnabled() is false and the header has no crypt parameters (VaultRepository.java:119-122, 348-354; VaultFile.java:102-105)',
  evidence='SRC vault/VaultManager.java:120-121; SRC vault/VaultRepository.java:119-122,348-354; SRC vault/VaultFile.java:102-105')
e('VaultFile$Header.toJson', 'CryptParameters.toJson', 'CALL', 'the header writes its crypt parameters, which exist only for an encrypted vault',
  guard='the header has crypt parameters: _params is not null (VaultFile.java:162)', needs_state=ST_VAULT_ENCRYPTED,
  evidence='SRC vault/VaultFile.java:162; SRC vault/VaultRepository.java:119-121')
# --- Row 23 fix (audit PASS, fix-row23): @RAW variant chain, design sections 4.1-4.4.
# 4.1: the base junction edge VaultFile$Header.toJson -> SlotList.toJson (Efb793e9d) is DELETED here
# (it was the line above this block in the pre-fix file); it was the only base incoming edge to
# SlotList.toJson, so deleting it kills the disable prefix's tail. The sibling CryptParameters edge above is untouched.
# Expected delta vs post-F2 baseline 6366: +24 (6390) with both sups below, +25 without the defensive
# Slot.toJson sup (audit C1). Fix-log corrections C2-C5: the @RAW route carries STATE kinds file + data
# (not 1); Password/Biometric CHA routes are 17 steps (not 16); CryptParameters comparison is 2-vs-2
# kinds decided on steps 27 < 29; import-alternative lines are AegisImporter.java:66-67, decrypt at 81-85, 89-101.
e('AegisActivity.saveAndBackupVault@RAW', 'VaultManager.saveAndBackup@RAW', 'CALL', 'the repaired-slot save after unlock backs the vault up', guard='called from the unlock repaired-slot save (AuthActivity.java:301)', evidence='SRC ui/AegisActivity.java:141 (bytecode)')
e('VaultManager.saveAndBackup@RAW', 'VaultManager.save@RAW', 'CALL', 'the repaired-slot save after unlock saves the vault', guard='called from the unlock repaired-slot save (AuthActivity.java:301)', evidence='SRC vault/VaultManager.java:140 (bytecode)')
e('VaultManager.save@RAW', 'VaultRepository.save@RAW', 'CALL', 'the repaired-slot save after unlock saves the repository', guard='called from the unlock repaired-slot save (AuthActivity.java:301)', evidence='SRC vault/VaultManager.java:136 (bytecode)')
e('VaultRepository.save@RAW', 'VaultFile.toBytes@RAW', 'CALL', 'the repaired-slot save after unlock serializes the vault file: credentials are non-null, so the encrypted branch ran', guard='isEncryptionEnabled() is true (VaultRepository.java:352-354,119-121): the credentials are the file header slots from AuthActivity.java:296, so setContent(obj, _creds) built Header(creds.getSlots(), params) (VaultFile.java:114)', evidence='SRC vault/VaultRepository.java:126 (bytecode)')
e('VaultFile.toBytes@RAW', 'VaultFile.toJson@RAW', 'CALL', 'the repaired-slot save after unlock writes the vault JSON', guard='called from the unlock repaired-slot save (AuthActivity.java:301)', evidence='SRC vault/VaultFile.java:52 (bytecode)')
e('VaultFile.toJson@RAW', 'VaultFile$Header.toJson@RAW', 'CALL', 'the repaired-slot save after unlock writes the vault header', guard='called from the unlock repaired-slot save (AuthActivity.java:301)', evidence='SRC vault/VaultFile.java:43 (bytecode)')
e('VaultFile$Header.toJson@RAW', 'SlotList.toJson@RAW', 'CALL', 'the header writes the slots of the unlocked encrypted vault', guard='_slots is not null: the header was built by setContent(obj, _creds) with the file header slots (VaultFile.java:114), not by the plain setContent that sets Header(null, null) (VaultFile.java:104)', evidence='SRC vault/VaultFile.java:161,102-105,114')
e('SlotList.toJson@RAW', 'Slot.toJson@RawSlot', 'CALL', 'the slot list of the unlocked encrypted vault is serialized: the iterated slot is the plain raw slot from the file header', guard='the iterated slot is a plain RawSlot deserialized from the file header slots array with type TYPE_RAW (Slot.java:131-133; AuthActivity.java:131 keeps that list as _slots)', evidence='SRC vault/slots/SlotList.java:17 (bytecode)')
# 4.3: re-write the eight suppressed base edges by hand (same trigger/evidence as the auto edges, so ids are preserved).
e('AuthActivity.finish', 'AegisActivity.saveAndBackupVault', 'CALL', 'Direct call', evidence='SRC AuthActivity.java:301 (bytecode)')
e('AegisActivity.saveAndBackupVault', 'VaultManager.saveAndBackup', 'CALL', 'Direct call', evidence='SRC AegisActivity.java:141 (bytecode)')
e('VaultManager.saveAndBackup', 'VaultManager.save', 'CALL', 'Direct call', evidence='SRC VaultManager.java:140 (bytecode)')
e('VaultManager.save', 'VaultRepository.save', 'CALL', 'Direct call', evidence='SRC VaultManager.java:136 (bytecode)')
e('VaultRepository.save', 'VaultFile.toBytes', 'CALL', 'Direct call', evidence='SRC VaultRepository.java:126 (bytecode)')
e('VaultFile.toBytes', 'VaultFile.toJson', 'CALL', 'Direct call', evidence='SRC VaultFile.java:52 (bytecode)')
e('VaultFile.toJson', 'VaultFile$Header.toJson', 'CALL', 'Direct call', evidence='SRC VaultFile.java:43 (bytecode)')
e('SlotList.toJson', 'Slot.toJson', 'CALL', 'Direct call', evidence='SRC SlotList.java:17 (bytecode)')
# 4.4: suppress two false auto CHA edges, base pairs only. Do NOT sup the BiometricSlot pairs (that would flip BiometricSlot.getType to UNREACHABLE).
sup(('AuthActivity$PasswordDerivationListener.onTaskFinished', 'RawSlot.getType'))
sup(('Slot.toJson', 'RawSlot.getType'))
e('MainActivity.onStart', 'MainActivity.setGroups', 'CALL', 'the group chips are refreshed (list loaded earlier in this instance)',
  guard='the vault is loaded and this instance loaded the list before (the _loaded branch at 978-980)', needs_state=ST_LIST_LOADED,
  evidence='SRC ui/MainActivity.java:978-980')
# incoming intents: handleIncomingIntent returns when the vault is not loaded (854-856), so the state is needed; the outside intent
# is the ENV gate on this edge (a shared node would otherwise be reached cheaper through the launcher)
e('MainActivity.onStart', 'MainActivity.handleIncomingIntent', 'CALL', 'a VIEW link from another app is handled (vault loaded)',
  guard='the vault is loaded (handleIncomingIntent returns at 854-856) and the intent is ACTION_VIEW with a data URI',
  needs_state=ST_UNLOCKED, env=ENV_VIEW, evidence='SRC ui/MainActivity.java:1003; SRC ui/MainActivity.java:853-870')
e('MainActivity.onStart', 'MainActivity.handleIncomingIntent', 'CALL', 'shared text or images from another app are handled (vault loaded)',
  guard='the vault is loaded (handleIncomingIntent returns at 854-856) and the intent is ACTION_SEND',
  needs_state=ST_UNLOCKED, env=ENV_SEND, evidence='SRC ui/MainActivity.java:1003; SRC ui/MainActivity.java:853-905')
e('MainActivity.handleIncomingIntent', 'MainActivity.startEditEntryActivityForNew', 'CALL', 'VIEW link: the add-entry page opens with the parsed entry',
  evidence='SRC ui/MainActivity.java:853-870')
e('MainActivity.handleIncomingIntent', 'MainActivity.startDecodeQrCodeImages', 'CALL', 'SEND image: QR codes in the shared image are decoded',
  env=ENV_SEND, guard='the intent is ACTION_SEND with a non-null EXTRA_STREAM (MainActivity.java:884-892)', evidence='SRC ui/MainActivity.java:884-892')

# ================================================================== C. intro (fresh install, no vault file)
e('MainActivity.startIntroActivity', 'IntroActivity.<init>', 'INTENT', 'startActivityForResult(IntroActivity) through introResultLauncher',
  guard='intro not already running (_isDoingIntro false, MainActivity.java:604)',
  evidence='SRC ui/MainActivity.java:603-612; ' + FW_LAUNCHER)
e('IntroActivity.<init>', 'IntroActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the intro', evidence=FW_CREATE + '; SRC ui/IntroActivity.java:35-41')
e('IntroActivity.onCreate', 'IntroBaseActivity.onCreate', 'CALL', 'super.onCreate: layout, back handler and the slides',
  evidence='SRC ui/IntroActivity.java:35-41; SRC ui/intro/IntroBaseActivity.java:36-58')
e('IntroBaseActivity.addSlide@IntroActivity', 'S_INTRO_WELCOME', 'ENTERS', 'the first slide (Welcome) is shown',
  guard='the added slide is the first one, the Welcome slide (IntroBaseActivity.java:183-186; IntroActivity.java:38)',
  evidence='SRC ui/intro/IntroBaseActivity.java:174-188; SRC ui/IntroActivity.java:38')

# Next and Previous on each slide
for pg in ('S_INTRO_WELCOME', 'S_INTRO_PICKER', 'S_INTRO_SETUP', 'S_INTRO_DONE'):
    gui(pg, 'IntroBaseActivity.lambda$onCreate$1', 'Tap Next (Done on the last slide)', evidence=FW_CLICK + '; SRC ui/intro/IntroBaseActivity.java:47')
for pg in ('S_INTRO_PICKER', 'S_INTRO_SETUP'):
    gui(pg, 'IntroBaseActivity.lambda$onCreate$0', 'Tap Previous', evidence=FW_CLICK + '; SRC ui/intro/IntroBaseActivity.java:45')
e('IntroBaseActivity.lambda$onCreate$1', 'IntroBaseActivity.goToNextSlide', 'CALL', 'the Next button calls goToNextSlide',
  evidence='SRC ui/intro/IntroBaseActivity.java:47,80-93')
e('IntroBaseActivity.lambda$onCreate$0', 'IntroBaseActivity.goToPreviousSlide', 'CALL', 'the Previous button calls goToPreviousSlide',
  evidence='SRC ui/intro/IntroBaseActivity.java:45,96-101')
# Previous (and Back) moves one page back. These edges start from the page the user is on, not from the shared
# goToPreviousSlide method, so a route cannot jump from Welcome to a later page.
e('S_INTRO_PICKER', 'S_INTRO_WELCOME', 'ENTERS', 'Previous or Back on the security picker: the Welcome slide is shown',
  guard='the security picker is the current slide (goToPreviousSlide, IntroBaseActivity.java:96-101)', evidence='SRC ui/intro/IntroBaseActivity.java:96-101')
e('S_INTRO_SETUP', 'S_INTRO_PICKER', 'ENTERS', 'Previous or Back on the setup slide: the security picker is shown',
  guard='the security setup is the current slide (goToPreviousSlide, IntroBaseActivity.java:96-101)', evidence='SRC ui/intro/IntroBaseActivity.java:96-101')

# Back on an intro slide: the handler goes to the previous slide; on the first slide nothing changes (the intro does not close)
gui('S_INTRO_WELCOME', 'IntroBaseActivity$BackPressHandler.handleOnBackPressed', 'Press Back on the first slide (no previous slide: nothing changes)',
    evidence=FW_DISPATCH + '; SRC ui/intro/IntroBaseActivity.java:39,190-199')
gui('S_INTRO_PICKER', 'IntroBaseActivity$BackPressHandler.handleOnBackPressed', 'Press Back (previous slide)',
    evidence=FW_DISPATCH + '; SRC ui/intro/IntroBaseActivity.java:39,190-199')
gui('S_INTRO_SETUP', 'IntroBaseActivity$BackPressHandler.handleOnBackPressed', 'Press Back (previous slide)',
    evidence=FW_DISPATCH + '; SRC ui/intro/IntroBaseActivity.java:39,190-199')
e('IntroBaseActivity$BackPressHandler.handleOnBackPressed', 'IntroBaseActivity.goToPreviousSlide', 'CALL',
  'Back calls goToPreviousSlide (a no-op on the first slide)', evidence='SRC ui/intro/IntroBaseActivity.java:190-199')

# Welcome: Next moves on, or the AppIntro library reports the change to IntroActivity
e('IntroBaseActivity.goToNextSlide', 'IntroActivity.onBeforeSlideChanged', 'FRAMEWORK', 'the slide changes: IntroActivity can skip slides',
  guard='the current slide is finished and is not the last slide (IntroBaseActivity.java:82-86)',
  evidence=FW_APPINTRO + '; SRC ui/intro/IntroBaseActivity.java:80-93; SRC ui/IntroActivity.java:44-62')
# The two skips depend on a state that an earlier action sets. The router ignores states, so each skip starts only at a
# variant (@IMPORTED, @NONE) that its producer chain reaches; the plain onBeforeSlideChanged has no skip.
# Import: importVault sets _imported and calls goToNextSlide through SlideFragment (WelcomeSlide.java:98-109; SlideFragment.java:58-61).
# The plain SlideFragment.goToNextSlide edge is written again by hand: a hand pair with the same names removes the automatic one.
e('WelcomeSlide.importVault', 'SlideFragment.goToNextSlide@IMPORTED', 'CALL', 'the vault is imported: the Welcome slide moves on with the imported flag set',
  evidence='SRC ui/slides/WelcomeSlide.java:98-109')
e('SlideFragment.goToNextSlide@IMPORTED', 'IntroBaseActivity.goToNextSlide@IMPORTED', 'CALL', 'SlideFragment.goToNextSlide calls the parent goToNextSlide',
  evidence='SRC ui/intro/SlideFragment.java:58-61')
e('SlideFragment.goToNextSlide', 'IntroBaseActivity.goToNextSlide', 'CALL', 'SlideFragment.goToNextSlide calls the parent goToNextSlide',
  evidence='SRC ui/intro/SlideFragment.java:58-61')
e('IntroBaseActivity.goToNextSlide@IMPORTED', 'IntroActivity.onBeforeSlideChanged@IMPORTED', 'FRAMEWORK',
  'the slide changes after the import: IntroActivity can skip the picker and setup',
  guard='the Welcome slide imported a vault: goToNextSlide saves the intro state before the change (IntroBaseActivity.java:85)',
  evidence=FW_APPINTRO + '; SRC ui/intro/IntroBaseActivity.java:80-93; SRC ui/IntroActivity.java:57-62')
e('IntroActivity.onBeforeSlideChanged@IMPORTED', 'IntroBaseActivity.skipToSlide', 'CALL', 'the Welcome slide imported a vault: the picker and setup are skipped',
  guard='the Welcome slide imported a vault (IntroActivity.java:57-62)', needs_state=ST_IMPORTED,
  evidence='SRC ui/IntroActivity.java:57-62')
# Security none: the picker's None is checked (a page state), then Next saves cryptType (SecurityPickerSlide.java:72-88) and the pager moves on
e('S_INTRO_PICKER', 'S_INTRO_PICKER@NONE', 'ENTERS', 'the user taps the None radio button on the security picker',
  evidence='SRC res/layout/fragment_security_picker_slide.xml:41 (rb_none tapped); INFERRED the radio group checks the tapped button (android.widget.RadioGroup not read); SRC ui/intro/IntroBaseActivity.java:85 (Next saves cryptType, SecurityPickerSlide.java:72-88)')
gui('S_INTRO_PICKER@NONE', 'IntroBaseActivity.lambda$onCreate$1@NONE', 'Tap Next on the security picker with None checked',
    evidence=FW_CLICK + '; SRC ui/intro/IntroBaseActivity.java:47')
e('IntroBaseActivity.lambda$onCreate$1@NONE', 'IntroBaseActivity.goToNextSlide@NONE', 'CALL', 'the Next button calls goToNextSlide',
  evidence='SRC ui/intro/IntroBaseActivity.java:47,80-93')
e('IntroBaseActivity.goToNextSlide@NONE', 'IntroActivity.onBeforeSlideChanged@NONE', 'CALL',
  'the pager moves on: setPagerPosition calls onBeforeSlideChanged, which IntroActivity overrides',
  guard='the current slide is finished and it is not the last slide (IntroBaseActivity.java:82-86)',
  evidence='SRC ui/intro/IntroBaseActivity.java:86,138,149-151; SRC ui/IntroActivity.java:45')
e('IntroActivity.onBeforeSlideChanged@NONE', 'IntroBaseActivity.skipToSlide', 'CALL', 'security "none" skips the setup slide',
  guard='the security picker chose none and the setup slide is next (IntroActivity.java:50-55)', needs_state=ST_SECURITY_NONE,
  evidence='SRC ui/IntroActivity.java:50-55')
e('IntroBaseActivity.skipToSlide', 'S_INTRO_DONE', 'ENTERS', 'the Done slide is shown after the skip',
  guard='the skip is the imported-vault skip or the security-none skip', evidence='SRC ui/intro/IntroBaseActivity.java:104; SRC ui/IntroActivity.java:50-62')
# Next on each page moves to the next page. These edges start from the page (S_...), not from the shared goToNextSlide
# method, so a route cannot jump over a page. The tap itself is the GUI edge above (lambda -> goToNextSlide).
e('S_INTRO_WELCOME', 'S_INTRO_PICKER', 'ENTERS', 'Next on Welcome (Welcome did not import): the security picker is shown',
  guard='Welcome did not import a vault (the intro state "imported" is false; IntroActivity.java:57-62)',
  evidence='SRC ui/intro/IntroBaseActivity.java:80-93; SRC ui/IntroActivity.java:57-62')
e('S_INTRO_PICKER', 'S_INTRO_SETUP', 'ENTERS', 'Next on the security picker: the password or biometric setup slide is shown',
  guard='the security picker chose password or biometrics (IntroActivity.java:50-55); a choice was made (SecurityPickerSlide.java:63-65)',
  evidence='SRC ui/intro/IntroBaseActivity.java:80-93; SRC ui/IntroActivity.java:50-55; SRC ui/slides/SecurityPickerSlide.java:63-65')
# The setup slide is finished only after the key derivation callback has stored the password slot (isFinished,
# SecuritySetupSlide.java:117-135), so the Done slide follows that callback and the Next tap alone cannot reach it.
e('SecuritySetupSlide$PasswordDerivationListener.onTaskFinished', 'S_INTRO_DONE', 'ENTERS',
  'the callback stores the slot and calls goToNextSlide: the setup slide is now finished, so the pager moves to the Done slide',
  guard='the key derivation for the intro password has finished (SecuritySetupSlide.java:153-167; IntroBaseActivity.java:82-86)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:153-167,117-135; SRC ui/intro/IntroBaseActivity.java:80-93')

# Next on the last slide reaches onDonePressed through the Done page's tap (gui S_INTRO_DONE, below). The shared goToNextSlide node
# must not carry that edge, or a route from Welcome would jump to Done through it.
sup(('IntroBaseActivity.goToNextSlide', 'IntroActivity.onDonePressed'))
# goToNextSlide is shared by every page, so this edge is kept only from the setup page (Next on an unfinished setup slide
# starts the key derivation, IntroBaseActivity.java:84-88; SecuritySetupSlide.java:138-146)
sup(('IntroBaseActivity.goToNextSlide', 'SecuritySetupSlide.onNotFinishedError'))
e('S_INTRO_SETUP', 'SecuritySetupSlide.onNotFinishedError', 'CALL', 'Next on the setup slide when it is not finished: goToNextSlide calls onNotFinishedError, which starts the key derivation',
  guard='the setup slide is not finished (IntroBaseActivity.java:84-88; SecuritySetupSlide.isFinished, SecuritySetupSlide.java:117-135)', needs_state=ST_PAGE_UNFINISHED,
  evidence='SRC ui/intro/IntroBaseActivity.java:84-88; SRC ui/slides/SecuritySetupSlide.java:138-146')
e('SecuritySetupSlide.onNotFinishedError', 'SecuritySetupSlide.deriveKey', 'CALL',
  'Next on the password setup with matching passwords: the key derivation starts',
  guard='the passwords match and the security type is password, not biometric (SecuritySetupSlide.java:139, 141-142)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:138-142')
e('SecuritySetupSlide.onNotFinishedError', 'SecuritySetupSlide.showBiometricPrompt', 'CALL',
  'Next on the biometric setup with matching passwords and no biometric slot yet: the biometric prompt starts',
  guard='the passwords match, the security type is biometric, and the vault has no biometric slot yet (SecuritySetupSlide.java:139, 141, 143-144)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:138-146')
e('SecuritySetupSlide.showBiometricPrompt', 'BiometricSlotInitializer.authenticate', 'CALL',
  'the biometric prompt starts for the intro setup slide (the listener is created first, then the prompt)',
  guard='started from the intro biometric branch of onNotFinishedError (SecuritySetupSlide.java:143-144)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:100-107')
e('BiometricSlotInitializer.onAuthenticationSucceeded', 'SecuritySetupSlide$BiometricsListener.onInitializeSlot', 'CALL',
  'the intro biometric prompt succeeded: the listener adds the biometric slot to the new vault',
  guard='the biometric prompt was started by the intro setup slide (SecuritySetupSlide.java:100-107; the listener is created at line 101)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:100-107,170-183')
e('SecuritySetupSlide$BiometricsListener.onInitializeSlot', 'SecuritySetupSlide.deriveKey', 'CALL',
  'the biometric slot is stored, then the password key is derived',
  guard='the slot was stored without a SlotException (the catch returns at SecuritySetupSlide.java:179)',
  evidence='SRC ui/slides/SecuritySetupSlide.java:173-182')
e('SecuritySetupSlide$PasswordDerivationListener.onTaskFinished', 'PasswordSlot.setKey', 'CALL',
  'the intro listener stores the password slot with the key and the cipher',
  evidence='SRC ui/slides/SecuritySetupSlide.java:157-158')

# Welcome: Import opens the system picker of another app; the returned content URI is read
gui('S_INTRO_WELCOME', 'WelcomeSlide.lambda$onCreateView$1', 'Tap Import (the picker of another app opens)', env=ENV_PICKER,
    evidence=FW_CLICK + '; SRC ui/slides/WelcomeSlide.java:43-47; ' + FW_LAUNCHER)
e('WelcomeSlide.lambda$onCreateView$1', 'WelcomeSlide.lambda$new$0', 'RESULT', 'the picker returns a content URI to the Welcome slide',
  env=ENV_PICKER, evidence='SRC ui/slides/WelcomeSlide.java:32-38; ' + FW_LAUNCHER)
e('WelcomeSlide.lambda$new$0', 'WelcomeSlide.startImportVault', 'CALL', 'the returned URI is imported (ImportFileTask)',
  guard='the picker returned a URI: data != null and data.getData() != null (WelcomeSlide.java:35-36)',
  evidence='SRC ui/slides/WelcomeSlide.java:30-40')

# Done: the last slide's Next calls onDonePressed; the vault is created (initNew) or loaded from the imported file
gui('S_INTRO_DONE', 'IntroActivity.onDonePressed', 'Tap Next on the Done slide: goToNextSlide calls onDonePressed (the tap path is lambda -> goToNextSlide -> onDonePressed)',
    evidence=FW_CLICK + '; SRC ui/intro/IntroBaseActivity.java:47,80-93')
e('IntroActivity.onDonePressed', 'VaultManager.initNew', 'CALL', 'a new vault is created (no import)',
  guard='the Welcome slide did not import a vault (state "imported" is false)', needs_state=ST_NOT_IMPORTED,
  evidence='SRC ui/IntroActivity.java:86-100')
# The RESULT edge sits on a variant that only the successful initNew or import path reaches, so the route cannot skip the vault creation
e('VaultManager.initNew', 'IntroActivity.onDonePressed@SAVED', 'CALL', 'initNew returns: the new vault exists and onDonePressed goes on to set the intro-done flag and return',
  guard='initNew returns without VaultRepositoryException (IntroActivity.java:100-104); the none path needs creds null (IntroActivity.java:92-96)',
  evidence='SRC ui/IntroActivity.java:92-104')
e('IntroActivity.onDonePressed', 'IntroActivity.onDonePressed@SAVED', 'CALL', 'the imported vault is read and loaded, then onDonePressed goes on',
  env=ENV_PICKER, guard='the Welcome slide imported a vault (IntroActivity.java:57-62) and readVaultFile and loadFrom return without an error (IntroActivity.java:106-123)', needs_state=ST_IMPORTED,
  evidence='SRC ui/IntroActivity.java:106-123')
e('IntroActivity.onDonePressed@SAVED', 'MainActivity.lambda$new$1', 'RESULT', "setResult(RESULT_OK) and finish() return the result to the caller's launcher",
  guard='the vault was created by initNew or loaded from the import, with no error dialog (the error branches return at 104, 113 and 121)',
  evidence='SRC ui/IntroActivity.java:126-129; ' + FW_RESULT + '; ' + FW_FINISH + '; ' + FW_LAUNCHER)
e('IntroActivity.onDonePressed', 'Dialogs.showErrorDialog(Context,int,Exception)', 'CALL', 'the vault could not be created or read: an error dialog is shown and the intro stays',
  guard='VaultRepositoryException from initNew (101-104) or from readVaultFile / loadFrom (109-121)',
  evidence='SRC ui/IntroActivity.java:99-122')

# ================================================================== D. unlock (AuthActivity)
e('MainActivity.startAuthActivity', 'AuthActivity.<init>', 'INTENT', 'startActivityForResult(AuthActivity) through authResultLauncher',
  guard='no unlock screen is already running (!_isAuthenticating, MainActivity.java:1147)',
  evidence='SRC ui/MainActivity.java:1146-1153; ' + FW_LAUNCHER)
e('AuthActivity.<init>', 'AuthActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the unlock screen', evidence=FW_CREATE + '; SRC ui/AuthActivity.java:73-195')
e('AuthActivity.onCreate', 'AuthActivity.onResume', 'LIFECYCLE', 'Activity.onResume (focus, biometric prompt when allowed)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2741 (performStart runs onStart between onCreate and onResume; neither ui/AuthActivity.java nor ui/AegisActivity.java defines onStart, grep no match, so the skipped step runs no app code); FW-SRC core/java/android/app/ActivityThread.java:3556 (performResumeActivity calls performResume) and 3621 (handleResumeActivity calls performResumeActivity); SRC ui/AuthActivity.java:210-224')
e('AuthActivity.onResume', 'S_AUTH', 'ENTERS', 'the unlock screen is in front', evidence='SRC ui/AuthActivity.java:73-224')
e('AuthActivity.onResume', 'AuthActivity.showBiometricPrompt', 'CALL', 'the biometric prompt starts on resume',
  guard='the biometric prompt is not inhibited and no password reminder is needed (AuthActivity.java:210-224)', needs_state=ST_BIO_SLOT,
  evidence='SRC ui/AuthActivity.java:210-224,270-293')
e('AuthActivity.showBiometricPrompt', 'AuthActivity$BiometricPromptListener.onAuthenticationSucceeded', 'FRAMEWORK',
  'the fingerprint or face is accepted (the prompt calls the listener)', env=ENV_BIOMETRIC,
  evidence=FW_BIOPROMPT + '; SRC ui/AuthActivity.java:270-293,366-401')
e('AuthActivity$BiometricPromptListener.onAuthenticationSucceeded', 'AuthActivity.finish', 'CALL',
  'the biometric key unlocks the vault and the screen finishes', evidence='SRC ui/AuthActivity.java:366-401,295-311')

# password: the Enter key or the unlock button runs the decrypt (the lambda runs the task directly)
gui('S_AUTH', 'AuthActivity.lambda$onCreate$2', 'Tap the unlock button with the password typed', needs_state=ST_PASSWORD_SLOT,
    evidence=FW_CLICK + '; SRC ui/AuthActivity.java:167-178')
gui('S_AUTH', 'AuthActivity.lambda$onCreate$0', 'Press Enter (done) in the password field', needs_state=ST_PASSWORD_SLOT,
    evidence='INFERRED TextView calls the editor action listener (TextView source not cached); SRC ui/AuthActivity.java:98-103')
e('AuthActivity.lambda$onCreate$0', 'AuthActivity.lambda$onCreate$2', 'CALL', 'the Enter key calls the decrypt button (performClick)',
  evidence=FW_CLICK + '; SRC ui/AuthActivity.java:98-103')
e('AuthActivity.lambda$onCreate$2', 'ProgressDialogTask.execute', 'CALL', 'the password decrypt task is started with the lifecycle and the params',
  evidence='SRC ui/AuthActivity.java:167-178; SRC ui/tasks/ProgressDialogTask.java:69-74')
e('AuthActivity.lambda$onCreate$2', 'PasswordSlotDecryptTask.doInBackground@AUTH', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (decrypt the password slot)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/AuthActivity.java:175; SRC ui/tasks/PasswordSlotDecryptTask.java:27')
e('SecurityPreferencesFragment.lambda$onCreatePreferences$7', 'PasswordSlotDecryptTask.doInBackground@SECURITY', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (decrypt the password slot to confirm the PIN)',
  guard='the typed PIN contains only digits (SecurityPreferencesFragment.java:158)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:158-162; SRC ui/tasks/PasswordSlotDecryptTask.java:27')
# replaced by the $1@WELCOME / $1@IMPORT task edges in the Aegis chains above (single @AEGIS task deleted).
# PasswordSlotDecryptTask split by builder (PasswordSlotDecryptTask.java:87-90 calls _cb.onTaskFinished, and
# _cb is fixed by the constructor argument at the build site). The shared doInBackground->onPostExecute edge
# and the shared callback edges are replaced by one variant chain per builder, so a task built by one caller
# can never deliver to another caller's callback (that cross-delivery was route 06 step 28, and, through the
# Aegis callback, route 16 step 30). The plain doInBackground/onPostExecute nodes keep their labels via
# their variants; no other caller of doInBackground exists in the graph.
for _tag, _cb in [
    ('@AUTH', 'AuthActivity$PasswordDerivationListener.onTaskFinished'),
    ('@SECURITY', 'SecurityPreferencesFragment$PasswordConfirmationListener.onTaskFinished'),
    ('@AEGIS_WELCOME', 'AegisImporter$EncryptedState.lambda$decrypt$0@WELCOME'),
    ('@AEGIS_IMPORT', 'AegisImporter$EncryptedState.lambda$decrypt$0@IMPORT'),
]:
    e('PasswordSlotDecryptTask.doInBackground' + _tag, 'PasswordSlotDecryptTask.onPostExecute' + _tag, 'ASYNC', 'the result is posted to the main thread',
      guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
      evidence=FW_ASYNC + '; SRC ui/tasks/PasswordSlotDecryptTask.java:27,87-90')
e('PasswordSlotDecryptTask.onPostExecute@SECURITY', 'SecurityPreferencesFragment$PasswordConfirmationListener.onTaskFinished', 'CALL',
  'the settings PIN confirmation: the callback receives the decrypt result',
  guard='the task was built with PasswordConfirmationListener (SecurityPreferencesFragment.java:161)',
  evidence='SRC ui/tasks/PasswordSlotDecryptTask.java:87-90; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:156-161,450')
e('PasswordSlotDecryptTask.onPostExecute@AUTH', 'AuthActivity$PasswordDerivationListener.onTaskFinished', 'CALL', '_cb.onTaskFinished(result)',
  guard='the task was built with PasswordDerivationListener (AuthActivity.java:173-174)',
  evidence='SRC ui/tasks/PasswordSlotDecryptTask.java:87-90; SRC ui/AuthActivity.java:343-364')
e('AuthActivity$PasswordDerivationListener.onTaskFinished', 'AuthActivity.finish', 'CALL',
  'the password matched a slot: the vault loads and the screen finishes', guard='the decrypt result is not null (a slot matched the password, 346)',
  evidence='SRC ui/AuthActivity.java:345-356; SRC ui/AuthActivity.java:295-311')
e('AuthActivity$PasswordDerivationListener.onTaskFinished', 'AuthActivity.onInvalidPassword', 'CALL',
  'the password did not match: the failed-attempt dialog is shown', guard='the decrypt result is null (wrong password, 357-361)',
  evidence='SRC ui/AuthActivity.java:357-362; SRC ui/AuthActivity.java:313-327')
e('AuthActivity.onInvalidPassword', 'S_AUTH', 'ENTERS', 'the unlock screen stays with the error dialog',
  evidence='SRC ui/AuthActivity.java:313-327')

gui('S_AUTH', 'AuthActivity.lambda$onCreate$4', 'Tap the biometric button (fingerprint or face)', env=ENV_BIOMETRIC, needs_state=ST_BIO_SLOT,
    guard='readVaultFile does not throw (AuthActivity.java:121-128); the button is visible: BiometricSlot present, BiometricsHelper.isAvailable true, keystore key found and not null (AuthActivity.java:132-150)',
    evidence=FW_CLICK + '; SRC ui/AuthActivity.java:180-194; ' + FW_BIOPROMPT)
e('AuthActivity.lambda$onCreate$4', 'AuthActivity.showBiometricPrompt', 'CALL', 'the biometric prompt starts (no password reminder needed)',
  guard='no password reminder is needed (else the reminder dialog is shown, AuthActivity.java:180-194)',
  evidence='SRC ui/AuthActivity.java:180-194')

gui('S_AUTH', 'AuthActivity$BackPressHandler.handleOnBackPressed', 'Press Back on the unlock screen (cancels the unlock and finishes the app task)',
    evidence=FW_DISPATCH + '; SRC ui/AuthActivity.java:329-340')
e('AuthActivity$BackPressHandler.handleOnBackPressed', 'S_EXIT', 'ENTERS', 'setResult(RESULT_CANCELED) and finishAffinity: the task closes, no vault is loaded',
  evidence='SRC ui/AuthActivity.java:329-340; ' + FW_STATE_FINISH)

# result of the unlock: AuthActivity.finish sets RESULT_OK; the launcher callback decrypts the list
e('AuthActivity.finish', 'MainActivity.lambda$new$0', 'RESULT', 'RESULT_OK after the vault loads: the launcher callback runs',
  guard='loadFrom succeeded (no error dialog, 298-310)', evidence='SRC ui/AuthActivity.java:295-311; ' + FW_RESULT + '; ' + FW_FINISH + '; ' + FW_LAUNCHER)
e('AuthActivity.finish', 'Dialogs.showErrorDialog(Context,int,Exception)', 'CALL', 'the vault could not be loaded: an error dialog is shown and the unlock screen stays',
  guard='VaultRepositoryException from loadFrom (303-306)', evidence='SRC ui/AuthActivity.java:295-307')
e('MainActivity.lambda$new$0', 'MainActivity.onDecryptResult', 'CALL', 'RESULT_OK: the unlock result is handled',
  guard='activityResult.getResultCode() == RESULT_OK (MainActivity.java:137)',
  evidence='SRC ui/MainActivity.java:134-140')
e('MainActivity.onDecryptResult', 'MainActivity.loadEntries', 'CALL', 'the entries are loaded after the unlock',
  evidence='SRC ui/MainActivity.java:797-801')
e('MainActivity.onIntroResult', 'MainActivity.loadEntries', 'CALL', 'the entries are loaded after the intro',
  evidence='SRC ui/MainActivity.java:752-754')
e('MainActivity.lambda$new$1', 'MainActivity.onIntroResult', 'CALL', 'RESULT_OK from the intro: the list is loaded',
  guard='the intro returned RESULT_OK (MainActivity.java:145)',
  evidence='SRC ui/MainActivity.java:142-148')
e('MainActivity.loadEntries', 'S_LIST', 'ENTERS', 'the list is shown (vault loaded, list loaded in this instance)',
  guard='list not yet loaded in this instance (_loaded false, MainActivity.java:1134) and the vault is loaded (getVault() throws when none is loaded, VaultManager.java:231-233): a producer of the loaded vault must come earlier on the route (the intro result, or an unlock)',
  evidence='SRC ui/MainActivity.java:1133-1144; SRC vault/VaultManager.java:231-233')

# ================================================================== E. the main screen: stop, background auto-lock, lock events
e('S_LIST', 'MainActivity.onPause', 'SYSTEM', 'Press Home or open another app', gui=['Press Home'], evidence='SRC ui/MainActivity.java:402-416')
e('MainActivity.onPause', 'MainActivity.onStop', 'SYSTEM', 'MainActivity is no longer visible', evidence='SRC ui/MainActivity.java:932-936')
e('MainActivity.onStop', 'S_MAIN_STOPPED', 'ENTERS', 'MainActivity is stopped', evidence='SRC ui/MainActivity.java:932-936')
e('S_MAIN_STOPPED', 'MainActivity.onStart', 'SYSTEM', 'Return to Aegis from the recent apps list',
  gui=['Return to the app'], evidence=FW_CREATE + '; SRC ui/MainActivity.java:938-940')
e('S_MAIN_STOPPED', 'AegisApplicationBase$AppLifecycleObserver.onStateChanged', 'SYSTEM', 'the app goes to the background (ON_STOP)',
  needs_state=ST_UNLOCKED, evidence=FW_LIFECYCLE + '; SRC AegisApplicationBase.java:105-114')
e('AegisApplicationBase$AppLifecycleObserver.onStateChanged', 'VaultManager.lock', 'CALL',
  'the vault locks when the app is minimised (auto-lock on minimise; default off)',
  guard='AUTO_LOCK_ON_MINIMIZE is on and the auto-lock is not blocked (default flags: Preferences.java:189)',
  evidence='SRC AegisApplicationBase.java:105-114; SRC Preferences.java:189')

e('VaultLockReceiver.onReceive', 'VaultManager.lock', 'CALL', 'the vault locks on the screen-off broadcast (lock(false))',
  guard='AUTO_LOCK_ON_DEVICE_LOCK is on (isAutoLockEnabled, VaultLockReceiver.java:24-34)', evidence='SRC receivers/VaultLockReceiver.java:24-34')

# VaultManager.lock calls every registered LockListener (registered in AegisActivity.onCreate, line 77)
e('VaultManager.lock', 'MainActivity.onLocked', 'CALL', 'LockListener dispatch: the main screen clears the list',
  guard='the MainActivity instance is registered (AegisActivity.java:77) and the list is loaded', needs_state=ST_LIST_LOADED,
  evidence='SRC vault/VaultManager.java:103-107; SRC ui/AegisActivity.java:77; SRC ui/MainActivity.java:1347-1360')
e('VaultManager.lock', 'AegisActivity.onLocked', 'CALL', 'LockListener dispatch: another open AegisActivity (not MainActivity) is finished',
  guard='the listener is an AegisActivity that does not override onLocked (MainActivity overrides, 1348)', needs_state=ST_ACTIVITY_OPEN,
  evidence='SRC vault/VaultManager.java:103-107; SRC ui/AegisActivity.java:97-111')
e('MainActivity.onLocked', 'MainActivity.startAuthActivity', 'CALL', 'a user-initiated lock starts the unlock screen',
  guard='userInitiated is true (1362-1363)', evidence='SRC ui/MainActivity.java:1347-1364')
e('MainActivity.onLocked', 'AegisActivity.onLocked', 'CALL', 'an automatic lock finishes the main screen',
  guard='userInitiated is false (1364-1365)', evidence='SRC ui/MainActivity.java:1347-1365')
e('AegisActivity.onLocked', 'S_EXIT', 'ENTERS', 'the activity is finished through the hidden finish(int) overload (reflection), or finishAndRemoveTask',
  cls='non_standard', via='reflection: Activity.class.getDeclaredMethod("finish", int.class) (AegisActivity.java:103-105), fallback finishAndRemoveTask (109)',
  evidence='SRC ui/AegisActivity.java:97-111; INFERRED the hidden finish(int) overload was not read in the framework')

# ================================================================== F. batch 1: floating menu, toolbar, search, back presses, action mode, chips, error cards, async tasks,
# camera and picker, intents to child activities, lifecycle of MainActivity.
# javac numbers a nested lambda before the lambda that contains it (post-order). The names below follow the descriptors in method_list.json:
# FabMenuHelper $2 = inner click (59-64), $3 = outer forEach lambda (58); MainActivity $12 = clipboard Yes, $13 = clipboard No.

# --- floating action menu (FabMenuHelper): + button, scrim, menu items, animations
gui('S_LIST', 'FabMenuHelper.lambda$setupClickListeners$0', 'Tap the + floating button (opens the menu)', evidence=FW_CLICK + '; SRC helpers/FabMenuHelper.java:55')
gui('FabMenuHelper.open', 'FabMenuHelper.lambda$setupClickListeners$1', 'Tap the dimmed background while the menu is open (closes it)', needs_state=ST_FAB_OPEN,
    evidence=FW_CLICK + '; SRC helpers/FabMenuHelper.java:56')
e('FabMenuHelper.setupClickListeners', 'FabMenuHelper.lambda$setupClickListeners$3', 'CALL',
  'Map.forEach runs the outer lambda once per menu item (it sets each item click listener)', cls='non_standard',
  via='java.util.Map.forEach (JDK) calls the BiConsumer lambda$setupClickListeners$3 for each action (the map is built at MainActivity.java:253-256)',
  evidence='SRC helpers/FabMenuHelper.java:54-58; INFERRED Map.forEach (JDK source not read)')
gui('FabMenuHelper.open', 'FabMenuHelper.lambda$setupClickListeners$2', 'Tap a menu item (scan, scan image or enter) while the menu is open', needs_state=ST_FAB_OPEN,
    evidence=FW_CLICK + '; SRC helpers/FabMenuHelper.java:59-64')
e('FabMenuHelper.lambda$setupClickListeners$2', 'MainActivity.startScanActivity', 'CALL', 'the scan item runs its Runnable: startScanActivity',
  cls='non_standard', via='java.lang.Runnable.run (the method reference this::startScanActivity, MainActivity.java:254)',
  evidence='SRC helpers/FabMenuHelper.java:60-63; SRC ui/MainActivity.java:254')
e('FabMenuHelper.lambda$setupClickListeners$2', 'MainActivity.startScanImageActivity', 'CALL', 'the scan-image item runs its Runnable: startScanImageActivity',
  cls='non_standard', via='java.lang.Runnable.run (the method reference this::startScanImageActivity, MainActivity.java:255)',
  evidence='SRC helpers/FabMenuHelper.java:60-63; SRC ui/MainActivity.java:255')
e('FabMenuHelper.lambda$setupClickListeners$2', 'MainActivity.startEditEntryActivity()', 'CALL', 'the enter item runs its Runnable: startEditEntryActivity',
  cls='non_standard', via='java.lang.Runnable.run (the method reference this::startEditEntryActivity, MainActivity.java:256)',
  evidence='SRC helpers/FabMenuHelper.java:60-63; SRC ui/MainActivity.java:256')
e('FabMenuHelper.open', 'FabMenuHelper.lambda$open$4', 'FRAMEWORK', 'the scrim fade-in starts: its start action makes the scrim visible',
  evidence=FW_FAB_ANIM + '; SRC helpers/FabMenuHelper.java:83-87')
e('FabMenuHelper.close', 'FabMenuHelper.lambda$close$5', 'FRAMEWORK', 'the scrim fade-out ends: its end action hides the scrim',
  evidence=FW_FAB_ANIM + '; SRC helpers/FabMenuHelper.java:111-115')
e('FabMenuHelper.close', 'FabMenuHelper.lambda$close$6', 'FRAMEWORK', 'postDelayed: after the animation the menu container is hidden if the menu is still closed',
  evidence=FW_POST + '; SRC helpers/FabMenuHelper.java:125-129')
e('FabMenuHelper.animateFabIcon', 'FabMenuHelper.lambda$animateFabIcon$7', 'FRAMEWORK', 'ValueAnimator update: the + icon is rotated on each frame',
  evidence=FW_FAB_ANIM + '; SRC helpers/FabMenuHelper.java:150-160')
e('FabMenuHelper.animateActionOut', 'FabMenuHelper.lambda$animateActionOut$8', 'FRAMEWORK', 'the item fade-out ends: the item is hidden',
  evidence=FW_FAB_ANIM + '; SRC helpers/FabMenuHelper.java:180-187')

# --- scan, camera permission and picker (PermissionHelper, ScannerActivity, the system picker of another app)
sup(('MainActivity.doShortcutActions', 'MainActivity.startScanActivity'))
e('LaunchScannerTileService.onClick', 'MainActivity.doShortcutActions@SCAN', 'INTENT',
  'the scanner tile starts MainActivity with extra action = scan; onCreate and onStart run on the way',
  guard='onStart reaches the shortcut actions: a plain-text vault file is loaded in onStart (MainActivity.java:963-965), vault init not needed (MainActivity.java:942), error returns at 960 and 971 not taken',
  needs_state=ST_PLAIN_VAULT_FILE,
  evidence='SRC LaunchScannerTileService.java:29-44; SRC ui/MainActivity.java:938-948,957-971,837-841')
e('S_PROCESS', 'MainActivity.doShortcutActions@SCAN', 'ENTRY',
  'the launcher shortcut "new entry" starts MainActivity with extra action = scan; onCreate and onStart run on the way',
  env=ENV_SHORTCUT,
  guard='onStart reaches the shortcut actions: a plain-text vault file is loaded in onStart (MainActivity.java:963-965), vault init not needed (MainActivity.java:942), error returns at 960 and 971 not taken',
  needs_state=ST_PLAIN_VAULT_FILE,
  evidence='SRC AegisApplicationBase.java:60,70-88 (setDynamicShortcuts with extra action = scan); SRC ui/MainActivity.java:938-948,957-971,837-841')
e('MainActivity.doShortcutActions@SCAN', 'MainActivity.startScanActivity', 'CALL', 'the scan shortcut opens the camera scanner',
  guard='intent action is "scan" (put by the scanner tile or the dynamic shortcut) and the vault is loaded (MainActivity.java:840-846)', needs_state=ST_PLAIN_VAULT_FILE,
  note='a plain-text vault is loaded in onStart without the unlock screen (MainActivity.java:963-965); this state is still required here',
  evidence='SRC ui/MainActivity.java:837-846; SRC LaunchScannerTileService.java:33')
e('MainActivity.startScanActivity', 'ScannerActivity.<init>', 'INTENT', 'the camera permission is already granted: the scanner opens through scanResultLauncher',
  env=ENV_CAMERA_GRANTED, evidence='SRC ui/MainActivity.java:803-810; SRC helpers/PermissionHelper.java:22-36; ' + FW_LAUNCHER)
e('PermissionHelper.request', 'MainActivity.onRequestPermissionsResult', 'FRAMEWORK', 'the system permission dialog returns the grant result (CODE_PERM_CAMERA)',
  env=ENV_CAMERA, evidence=FW_PERMRESULT + '; SRC helpers/PermissionHelper.java:22-34; SRC ui/MainActivity.java:430-441')
# the Activity overload of the shared launcher node has two callers (MainActivity.java:823, EditEntryActivity.java:577); each caller gets a
# variant so a picker result cannot route into the other picker's callback (G1 R1 step 66). Same pattern as _FIL_SETTINGS.
_FIL_QR = 'VaultManager.fireIntentLauncher(Activity,Intent,ActivityResultLauncher)@QR_SCAN'
_FIL_EDIT_PICK = 'VaultManager.fireIntentLauncher(Activity,Intent,ActivityResultLauncher)@EDIT_PICK'
e('MainActivity.startScanImageActivity', _FIL_QR, 'CALL',
  'the scan-image chooser is started through the launcher of the QR scan result',
  evidence='SRC ui/MainActivity.java:812-824')
e(_FIL_QR, 'MainActivity.lambda$new$7', 'RESULT',
  'the picker of another app returns the chosen image or file to the launcher callback', env=ENV_PICK_IMAGE,
  evidence='SRC vault/VaultManager.java:243-252; SRC ui/MainActivity.java:185-190,812-824; ' + FW_RESULT)

# --- entries: clipboard dialog, add and edit pages (EditEntryActivity itself is written in its own batch)
gui('S_LIST', 'MainActivity.lambda$startEditEntryActivity$12', 'Tap Yes in the clipboard import dialog (the dialog appears only when the clipboard holds an otpauth link)',
    env=ENV_CLIPBOARD, needs_state=ST_CLIPBOARD_DIALOG, evidence=FW_DIALOG + '; SRC ui/MainActivity.java:474-493')
gui('S_LIST', 'MainActivity.lambda$startEditEntryActivity$13', 'Tap No in the clipboard import dialog (the entry is entered by hand)',
    env=ENV_CLIPBOARD, needs_state=ST_CLIPBOARD_DIALOG, evidence=FW_DIALOG + '; SRC ui/MainActivity.java:474-500')
e('MainActivity.startEditEntryActivityForNew', 'EditEntryActivity.<init>', 'INTENT', 'the add-entry page opens with the parsed entry (isManual false)',
  evidence='SRC ui/MainActivity.java:502-507; ' + FW_LAUNCHER)
e('MainActivity.startEditEntryActivityForManual', 'EditEntryActivity.<init>', 'INTENT', 'the add-entry page opens for a manual entry (isManual true)',
  evidence='SRC ui/MainActivity.java:509-514; ' + FW_LAUNCHER)
e('MainActivity.startEditEntryActivity(VaultEntry)', 'EditEntryActivity.<init>', 'INTENT', 'the edit page opens for the selected entry (entryUUID)',
  evidence='SRC ui/MainActivity.java:516-520; ' + FW_LAUNCHER)
e('MainActivity.startAssignIconsActivity', 'AssignIconsActivity.<init>', 'INTENT', 'the assign-icons page opens with the selected entries',
  evidence='SRC ui/MainActivity.java:522-531; ' + FW_LAUNCHER)
e('MainActivity.startPreferencesActivity(Class,String)', 'PreferencesActivity.<init>', 'INTENT', 'the settings page opens (fragment and preference extras)',
  evidence='SRC ui/MainActivity.java:826-835; ' + FW_LAUNCHER)

# --- toolbar: menu creation, lock icon, settings, about, sort options
e('MainActivity.onCreate', 'MainActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate (menu inflated, search view and lock icon set up)',
  evidence=FW_OPTIONS + '; SRC ui/MainActivity.java:1011-1016')
# One toolbar tap enters this method, and the method branches on the item. Each branch carries its own guard, so a route
# cannot take the lock branch after a Settings tap (a route step that says "tap the lock icon" then opens Settings was wrong).
gui('S_LIST', 'MainActivity.onOptionsItemSelected', 'Tap an item in the list toolbar or overflow menu: the lock icon, Settings, About or a sort option',
    evidence=FW_MENU + '; SRC ui/MainActivity.java:1086-1118')
e('MainActivity.onOptionsItemSelected', 'VaultManager.lock', 'CALL', 'the lock icon: the vault locks (lock(true))',
  guard='the lock icon was tapped (action_lock, MainActivity.java:1093-1094); the icon is shown only when the vault has encryption (updateLockIcon, MainActivity.java:1155-1161)',
  evidence='SRC ui/MainActivity.java:1093-1094; SRC ui/MainActivity.java:1155-1161')
e('MainActivity.onOptionsItemSelected', 'MainActivity.startPreferencesActivity()', 'CALL', 'the Settings item opens the settings page',
  guard='the Settings item was tapped (action_settings, MainActivity.java:1088-1089)',
  evidence='SRC ui/MainActivity.java:1088-1089')
e('MainActivity.onOptionsItemSelected', 'AboutActivity.<init>', 'INTENT', 'Tap About: the about page opens',
  guard='the About item was tapped (action_about, MainActivity.java:1090-1092)',
  evidence='SRC ui/MainActivity.java:1090-1092')
e('MainActivity.onOptionsItemSelected', 'SortCategory.<clinit>', 'CALL', 'a sort option was tapped: the sort category enum is first used',
  guard='a sort option was tapped (the sort group check, MainActivity.java:1096-1097)',
  evidence='SRC ui/MainActivity.java:1096-1117')
e('MainActivity.onOptionsItemSelected', 'EntryListView.setSortCategory', 'CALL', 'a sort option was tapped: the list is re-sorted',
  guard='a sort option was tapped (the sort group check, MainActivity.java:1096-1097)',
  evidence='SRC ui/MainActivity.java:1117')
# EntryAdapter.setSortCategory refreshes only when apply is true; the graph has no argument values, so the refresh is drawn per caller
sup(('EntryAdapter.setSortCategory', 'EntryAdapter.refreshEntryList'))
e('MainActivity.onOptionsItemSelected', 'EntryAdapter.refreshEntryList', 'CALL',
  'a sort option was tapped and the category changed: the list is re-sorted and refreshed (apply is true)',
  guard='the chosen sort differs from the current one (EntryAdapter.java:253-254) and the sort menu passes apply=true (MainActivity.java:1117)',
  needs_state=ST_LIST_LOADED, evidence='SRC ui/MainActivity.java:1117; SRC ui/views/EntryListView.java:258; SRC ui/views/EntryAdapter.java:253-259')
e('MainActivity.onOptionsItemSelected', 'Preferences.setCurrentSortCategory', 'CALL', 'a sort option was tapped: the choice is saved',
  guard='a sort option was tapped (the sort group check, MainActivity.java:1096-1097)',
  evidence='SRC ui/MainActivity.java:1118')

# --- search box (SearchView listeners; the anonymous class MainActivity$1 holds the query callbacks)
gui('S_LIST', 'MainActivity$1.onQueryTextChange', 'Type in the search box', needs_state=ST_SEARCH_OPEN,
    evidence=FW_SEARCH + '; SRC ui/MainActivity.java:1046-1058')
gui('S_LIST', 'MainActivity$1.onQueryTextSubmit', 'Submit the search text (Search or Enter key)', needs_state=ST_SEARCH_OPEN,
    evidence=FW_SEARCH + '; SRC ui/MainActivity.java:1034-1044')
gui('S_LIST', 'MainActivity.lambda$onCreateOptionsMenu$25', 'Tap the search icon (the search box opens)',
    evidence=FW_SEARCH + '; SRC ui/MainActivity.java:1060-1064')
gui('S_LIST', 'MainActivity.lambda$onCreateOptionsMenu$23', 'Focus the search box (its field gains focus)',
    evidence=FW_SEARCH + '; SRC ui/MainActivity.java:1021-1024')
gui('S_LIST', 'MainActivity.lambda$onCreateOptionsMenu$24', 'Close the search box (the close icon)', needs_state=ST_SEARCH_OPEN,
    evidence=FW_SEARCH + '; SRC ui/MainActivity.java:1025-1030')

# --- Back presses: the four OnBackPressedCallbacks (each is enabled only in its own state) and the key handler
gui('S_LIST', 'MainActivity$SearchViewBackPressHandler.handleOnBackPressed', 'Press Back with the search box open (clears the search)',
    needs_state=ST_SEARCH_OPEN, evidence=FW_DISPATCH + '; SRC ui/MainActivity.java:212-213,1398-1415')
gui('S_LIST', 'MainActivity$ActionModeBackPressHandler.handleOnBackPressed', 'Press Back with the selection action mode open (closes it)',
    needs_state=ST_ACTION_MODE, evidence=FW_DISPATCH + '; SRC ui/MainActivity.java:214-215,1430-1441')
gui('FabMenuHelper.open', 'MainActivity$FabMenuBackPressHandler.handleOnBackPressed', 'Press Back with the floating menu open (closes it)',
    needs_state=ST_FAB_OPEN, evidence=FW_DISPATCH + '; SRC ui/MainActivity.java:216-217,1443-1454')
gui('S_LIST', 'MainActivity$LockBackPressHandler.handleOnBackPressed', 'Press Back on the main screen (locks the vault)',
    guard='the back-button lock is on: default on (Preferences.java:189), set in onStart (MainActivity.java:999-1001)',
    evidence=FW_DISPATCH + '; SRC ui/MainActivity.java:210-211,999-1001,1417-1428')
gui('S_LIST', 'MainActivity.onKeyDown', 'Press a key or the D-pad on the main screen', evidence=FW_KEYS + '; SRC ui/MainActivity.java:443-447')

# --- selection action mode (the long press that starts it is in EntryListView, written in its own batch)
e('MainActivity.startActionMode', 'MainActivity$ActionModeCallbacks.onCreateActionMode', 'FRAMEWORK', 'startSupportActionMode creates the action bar menu',
  evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1303-1304')
e('MainActivity.startActionMode', 'MainActivity$ActionModeCallbacks.onPrepareActionMode', 'FRAMEWORK', 'startSupportActionMode prepares the action bar menu',
  evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1303-1304')
gui('MainActivity.startActionMode', 'MainActivity$ActionModeCallbacks.onActionItemClicked',
    'Tap an item of the selection action bar (copy, edit, favorite, share, delete, select all, assign icons or assign groups)',
    needs_state=ST_ACTION_MODE, evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1469-1531')
e('MainActivity$ActionModeCallbacks.onActionItemClicked', 'MainActivity.startEditEntryActivity(VaultEntry)', 'CALL',
  'Tap Edit with the selection: the edit page opens for the selected entry',
  guard='the Edit item is tapped (action_edit, MainActivity.java:1480) and the selection is not empty (MainActivity.java:1471-1474)',
  evidence='SRC ui/MainActivity.java:1471-1474,1480-1481')
e('MainActivity$ActionModeCallbacks.onActionItemClicked', 'TransferEntriesActivity.<init>', 'INTENT',
  'Tap Share QR: the transfer page opens with the selected entries', evidence='SRC ui/MainActivity.java:1493-1506')
e('VaultRepository.editEntry', 'MainActivity$ActionModeCallbacks.lambda$onActionItemClicked$0', 'CALL',
  'Tap Favorite: the editor lambda toggles the favourite flag of each copied entry', cls='non_standard',
  via='VaultRepository.EntryEditor.edit (interface call; the lambda is passed at MainActivity.java:1485-1487)',
  evidence='SRC vault/VaultRepository.java:253-256,364-366; SRC ui/MainActivity.java:1484-1487')
e('MainActivity$ActionModeCallbacks.onActionItemClicked', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  'mode.finish after an action: the framework calls onDestroyActionMode', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1470-1531')
e('MainActivity$ActionModeBackPressHandler.handleOnBackPressed', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  '_actionMode.finish (Back): the framework calls onDestroyActionMode', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1436-1439')
e('MainActivity.onLocked', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  'the lock closes the action mode: the framework calls onDestroyActionMode', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1349-1351')
e('MainActivity.onEntryClick', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  'the last selected entry is tapped again: the action mode is finished', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:1244-1246')
e('MainActivity.lambda$addChipTo$9', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  'a group chip is changed while the action mode is open: the action mode is finished', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:330-332')
e('MainActivity.lambda$startAssignGroupsDialog$15', 'MainActivity$ActionModeCallbacks.onDestroyActionMode', 'FRAMEWORK',
  'OK in the assign-groups dialog finishes the action mode', evidence=FW_ACTIONMODE + '; SRC ui/MainActivity.java:570-595')

# --- assign groups dialog: shown by a framework callback, its controls are gated by the dialog state
e('MainActivity.startAssignGroupsDialog', 'MainActivity.lambda$startAssignGroupsDialog$16', 'FRAMEWORK',
  'the assign-groups dialog is shown: its OnShowListener sets the OK button listener', evidence=FW_DIALOG + '; SRC ui/MainActivity.java:568-600')
gui('S_LIST', 'MainActivity.lambda$startAssignGroupsDialog$14', 'Pick a group in the dropdown of the assign-groups dialog', needs_state=ST_ASSIGN_DIALOG,
    evidence=FW_ITEM + '; SRC ui/MainActivity.java:547-559')
gui('S_LIST', 'MainActivity.lambda$startAssignGroupsDialog$15', 'Tap OK in the assign-groups dialog (assigns the groups to the selected entries)',
    needs_state=ST_ASSIGN_DIALOG, evidence=FW_CLICK + '; SRC ui/MainActivity.java:570-597')

# --- group chips and the group filter (stream callbacks run from the JDK)
gui('S_LIST', 'MainActivity.lambda$addChipTo$9', 'Tap a group chip in the group bar (check or uncheck it)', needs_state=ST_LIST_LOADED,
    evidence=FW_CHECK + '; SRC ui/MainActivity.java:330-349')
gui('S_LIST', 'MainActivity.lambda$addSaveChip$10', 'Tap the Save chip after the group filter changed', needs_state=ST_SAVE_CHIP,
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:365-368')
e('MainActivity.cleanGroupFilter', 'MainActivity.lambda$cleanGroupFilter$8', 'CALL',
  'the stream filter keeps the group UUIDs that still exist', cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$cleanGroupFilter$8 for each UUID',
  evidence='SRC ui/MainActivity.java:302-307; INFERRED Stream.filter (JDK source not read)')
e('MainActivity.getGroupFilter', 'MainActivity.lambda$getGroupFilter$11', 'CALL',
  'the stream map turns each checked chip into its group UUID', cls='non_standard',
  via='java.util.stream.Stream.map (JDK) calls the Function lambda$getGroupFilter$11 for each checked chip id',
  evidence='SRC ui/MainActivity.java:379-393; INFERRED Stream.map (JDK source not read)')
e('MainActivity.checkIconOptimization', 'MainActivity.lambda$checkIconOptimization$20', 'CALL',
  'the stream filter keeps the entries whose icons are not optimised yet', cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$checkIconOptimization$20 for each entry',
  evidence='SRC ui/MainActivity.java:766-772; INFERRED Stream.filter (JDK source not read)')

# --- error cards (EntryListView shows the card; its click listener is the lambda)
gui('S_LIST', 'MainActivity.lambda$updateErrorCard$27', 'Tap the backup error card (the last backup failed)', needs_state=ST_ERROR_CARD,
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1163-1172; INFERRED the card calls its listener (EntryListView not read yet)')
gui('S_LIST', 'MainActivity.lambda$updateErrorCard$29', 'Tap the backup reminder card', needs_state=ST_ERROR_CARD,
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1173-1191; INFERRED the card calls its listener (EntryListView not read yet)')
gui('S_LIST', 'MainActivity.lambda$updateErrorCard$30', 'Tap the plaintext export warning card', needs_state=ST_ERROR_CARD,
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1192-1193; INFERRED the card calls its listener (EntryListView not read yet)')
e('MainActivity.showPlaintextExportWarningOptions', 'MainActivity.lambda$showPlaintextExportWarningOptions$32', 'FRAMEWORK',
  'the warning dialog is shown: its OnShowListener sets the OK button listener', evidence=FW_DIALOG + '; SRC ui/MainActivity.java:1199-1226')
gui('S_LIST', 'MainActivity.lambda$showPlaintextExportWarningOptions$31', 'Tap OK in the plaintext export warning dialog (saves the choice)',
    needs_state=ST_ERROR_CARD, evidence=FW_CLICK + '; SRC ui/MainActivity.java:1213-1224')

# --- background work: QR decode of picked or shared images, and icon optimisation
# ProgressDialogTask.execute is shared by every task, so each caller links straight to the doInBackground of the task it creates
# onScanImageResult calls startDecodeQrCodeImages on two paths: one picked image (getData, line 641) and several images (ClipData, line 657).
# One auto row covered both, so the auto row is suppressed and each path gets its own guard.
sup(('MainActivity.onScanImageResult', 'MainActivity.startDecodeQrCodeImages'))
e('MainActivity.onScanImageResult', 'MainActivity.startDecodeQrCodeImages', 'CALL', 'the picker returns one image: it is decoded',
  guard='intent.getData() is non-null (MainActivity.java:640-641; the method returns at 642)',
  evidence='SRC ui/MainActivity.java:640-642')
e('MainActivity.onScanImageResult', 'MainActivity.startDecodeQrCodeImages', 'CALL', 'the picker returns several images as ClipData: the images with a URI are decoded',
  guard='intent.getData() is null and intent.getClipData() is non-null with at least one item holding a URI (MainActivity.java:645-656; the call at 657 needs uris.size() > 0)',
  evidence='SRC ui/MainActivity.java:645-657')
e('MainActivity.startDecodeQrCodeImages', 'QrDecodeTask.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (decode each image)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/MainActivity.java:669,726; SRC ui/tasks/QrDecodeTask.java:24')
e('QrDecodeTask.doInBackground', 'QrDecodeTask.onPostExecute', 'ASYNC', 'the decode results are posted to the main thread',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/QrDecodeTask.java:51-53')
e('QrDecodeTask.onPostExecute', 'MainActivity.lambda$startDecodeQrCodeImages$18', 'CALL',
  '_cb.onTaskFinished(results): the QR callback imports the entries or shows the errors', cls='non_standard',
  via='QrDecodeTask.Callback.onTaskFinished (interface call; the lambda is passed at MainActivity.java:669)',
  evidence='SRC ui/tasks/QrDecodeTask.java:53,56-58; SRC ui/MainActivity.java:669')
e('MainActivity.lambda$startDecodeQrCodeImages$18', 'GoogleAuthInfo.parseExportUri(Uri)', 'CALL',
  'the scanned export link is parsed into a batch of entries',
  guard='decode had no error (MainActivity.java:675-678) and the scanned URI scheme equals GoogleAuthInfo.SCHEME_EXPORT (682), inside try (680)',
  evidence='SRC ui/MainActivity.java:673-690')
sup(('MainActivity.lambda$startDecodeQrCodeImages$18', 'Dialogs.showPartialGoogleAuthImportWarningDialog'))
e('MainActivity.lambda$startDecodeQrCodeImages$18', 'Dialogs.showPartialGoogleAuthImportWarningDialog', 'CALL',
  'the scan had missing codes: the partial-import warning opens',
  guard='googleAuthExports is not empty, it is a single batch, and missingIndices is not empty (MainActivity.java:700-712)',
  evidence='SRC ui/MainActivity.java:700-712')
e('MainActivity.checkIconOptimization', 'IconOptimizationTask.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (optimise the icons)',
  guard='some vault entry icons are not optimised yet (MainActivity.java:774)', needs_state=ST_ICONS_NOT_OPTIMIZED,
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/MainActivity.java:774-776; SRC ui/tasks/IconOptimizationTask.java:25')
e('ImportEntriesActivity.processDecryptedImporterState', 'IconOptimizationTask.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (optimise the icons of the imported entries)',
  guard='some imported icons are not optimised yet (ImportEntriesActivity.java:220)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/ImportEntriesActivity.java:220-229; SRC ui/tasks/IconOptimizationTask.java:25')
e('IconOptimizationTask.doInBackground', 'IconOptimizationTask.onPostExecute', 'ASYNC', 'the optimised icons are posted to the main thread',
  evidence=FW_ASYNC + '; SRC ui/tasks/IconOptimizationTask.java:55-57')
e('IconOptimizationTask.onPostExecute', 'MainActivity.onIconsOptimized', 'CALL', '_cb.onTaskFinished(results): the optimised icons are saved to the entries',
  cls='non_standard', via='IconOptimizationTask.Callback.onTaskFinished (interface call; the method reference this::onIconsOptimized is passed at MainActivity.java:775)',
  evidence='SRC ui/tasks/IconOptimizationTask.java:57,60-61; SRC ui/MainActivity.java:775')

# --- lifecycle of MainActivity that the batch needs (onPause, onSaveInstanceState, onStart, onRestoreInstanceState, onDestroy)
# On API 27 the save runs between onPause and onStop (the order changed in later Android versions), so the edge starts at onPause.
e('MainActivity.onPause', 'MainActivity.onSaveInstanceState', 'SYSTEM',
  'API 27: the framework saves the instance state after onPause and before onStop', evidence=FW_SAVE + '; SRC ui/MainActivity.java:402-427')
# R4 producer chain for @RESTORED: the framework saves the submitted query, then a configuration
# change recreates the activity and the menu is created again from the saved bundle.
e('MainActivity.onSaveInstanceState', 'MainActivity.onCreateOptionsMenu@RESTORED', 'SYSTEM', 'a configuration change recreates the activity: onCreate runs with the saved bundle and the menu is created again, restoring the submitted search',
  guard='the saved bundle holds a submitted query (MainActivity.java:419-420 saves _submittedSearchQuery; :204-205 restores it) and no pending query (MainActivity.java:1066-1073 else-if branch)',
  needs_state=ST_SUBMITTED_QUERY_SAVED,
  evidence=FW_RECREATE + '; SRC ui/MainActivity.java:419-420,204-205,1066-1073')
e('MainActivity.onStart', 'MainActivity.onRestoreInstanceState', 'LIFECYCLE', 'the framework restores the saved state after onStart',
  guard='a saved state exists (savedInstanceState is not null: after recreate() from onPreferencesResult, or a configuration change)',
  evidence=FW_RESTORE + '; SRC ui/MainActivity.java:1230-1231')
# onDestroy: onPreferencesResult calls recreate() when the entry list was loaded (MainActivity.java:467-472); the framework then destroys the activity.
e('MainActivity.onPreferencesResult', 'MainActivity.onDestroy', 'FRAMEWORK',
  'recreate() after the settings page closed: the framework destroys the activity (onDestroy, which clears the entry list listener)',
  guard='the entry list was loaded (_loaded is true, MainActivity.java:469-470)',
  evidence=FW_RECREATE + '; SRC ui/MainActivity.java:396-399,467-472')

# --- batch 2: the generic dialogs in Dialogs.java and the listeners they call.
# A dialog tap starts at the dialog method (src = Dialogs.showX). When the dialog's OnShowListener replaces a button's click listener,
# the tap starts at that show listener instead: the show listener runs before any tap, so the replaced listener is never reached.
# A listener that a caller passes in gets a caller-specific edge in the caller's block (MainActivity, below), because the Dialogs OK taps
# do not reach it. The time sync listener is the exception: it has one caller, so its Dialogs lambda gets a non_standard CALL.

# --- set password (Dialogs.java:121-192)
e('Dialogs.showSetPasswordDialog', 'Dialogs.lambda$showSetPasswordDialog$4', 'FRAMEWORK',
  'the set-password dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:153-156')
gui('Dialogs.showSetPasswordDialog', 'Dialogs.lambda$showSetPasswordDialog$1', 'Tick or untick Show password in the set-password dialog',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:132-142')
gui('Dialogs.showSetPasswordDialog', 'Dialogs.lambda$showSetPasswordDialog$5',
    'Type a password in the set-password dialog (the strength bar updates; OK is enabled when the two passwords match)',
    evidence='SRC ui/dialogs/Dialogs.java:183-189; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showSetPasswordDialog$4', 'Dialogs.lambda$showSetPasswordDialog$3', 'Tap OK in the set-password dialog (starts the key derivation)',
    guard='the two password fields are equal (OK is disabled until then, Dialogs.java:185; the click also returns early at 160-162)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:159-162')
# Fix-design 01 (C3 routes 01): the KeyDerivationTask callback is fixed at task construction (Dialogs.java:166
# builds the task with the showSetPasswordDialog lambda; SecuritySetupSlide.java:112 builds it with
# PasswordDerivationListener). The plain onPostExecute node therefore cannot feed the Dialogs lambda: the
# dialog's task gets its own variant chain, reached only from the dialog's OK tap, following the
# ImportFileTask.doInBackground@SVG_PICK precedent. The plain chain (deriveKey -> doInBackground ->
# onPostExecute -> PasswordDerivationListener) is unchanged.
e('Dialogs.lambda$showSetPasswordDialog$3', 'KeyDerivationTask.doInBackground@SETPWD', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (derive the key from the password; this task was built by the set-password dialog)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/dialogs/Dialogs.java:166,178-179; SRC ui/tasks/KeyDerivationTask.java:21')
e('SecuritySetupSlide.deriveKey', 'KeyDerivationTask.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (derive the key from the password of the new vault)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/slides/SecuritySetupSlide.java:112-113; SRC ui/tasks/KeyDerivationTask.java:21')
e('KeyDerivationTask.doInBackground', 'KeyDerivationTask.onPostExecute', 'ASYNC', 'the derived key is posted to the main thread',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/KeyDerivationTask.java:39-41')
e('KeyDerivationTask.doInBackground@SETPWD', 'KeyDerivationTask.onPostExecute@SETPWD', 'ASYNC', 'the derived key is posted to the main thread (the set-password dialog task)',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/KeyDerivationTask.java:39-41')
e('KeyDerivationTask.onPostExecute@SETPWD', 'Dialogs.lambda$showSetPasswordDialog$2', 'CALL',
  '_cb.onTaskFinished(slot, key): the lambda makes the cipher and gives the slot to the listener', cls='non_standard',
  guard='the task was built by Dialogs.showSetPasswordDialog (Dialogs.java:166); only the @SETPWD variant reaches this lambda',
  via='KeyDerivationTask.Callback.onTaskFinished (interface call; the lambda is passed at Dialogs.java:166)',
  evidence='SRC ui/tasks/KeyDerivationTask.java:41,80-82; SRC ui/dialogs/Dialogs.java:166-177')
e('KeyDerivationTask.onPostExecute', 'SecuritySetupSlide$PasswordDerivationListener.onTaskFinished', 'CALL',
  '_cb.onTaskFinished(slot, key) for the intro setup slide: the listener stores the password slot', cls='non_standard',
  via='KeyDerivationTask.Callback.onTaskFinished (interface call; the listener is passed at SecuritySetupSlide.java:112)',
  needs_state=ST_PAGE_UNFINISHED,
  evidence='SRC ui/tasks/KeyDerivationTask.java:41; SRC ui/slides/SecuritySetupSlide.java:112,153-167')

# --- text input (Dialogs.java:194-240, the 8-argument overload that the other overloads forward to)
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)', 'Dialogs.lambda$showTextInputDialog$8', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8', 'Dialogs.lambda$showTextInputDialog$6',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6', 'Dialogs.lambda$showTextInputDialog$7', 'Tap OK in the input dialog (gives the text to the listener)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')

# --- checkbox (Dialogs.java:274-303)
gui('Dialogs.showCheckboxDialog', 'Dialogs.lambda$showCheckboxDialog$9', 'Tap No in the checkbox dialog (the listener gets false)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:282-283')
e('Dialogs.showCheckboxDialog', 'Dialogs.lambda$showCheckboxDialog$11', 'FRAMEWORK',
  'the checkbox dialog is shown: its OnShowListener disables Yes until the checkbox is ticked', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:294-298')
gui('Dialogs.showCheckboxDialog', 'Dialogs.lambda$showCheckboxDialog$12', 'Tick the checkbox in the checkbox dialog (this enables Yes)',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:300')
gui('Dialogs.lambda$showCheckboxDialog$12', 'Dialogs.lambda$showCheckboxDialog$10', 'Tap Yes in the checkbox dialog (gives the checkbox state to the listener)',
    guard='the checkbox is ticked (Yes is disabled until then, Dialogs.java:296-300)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:284-285')

# --- number pickers (Dialogs.java:305-353)
gui('Dialogs.showTapToRevealTimeoutPickerDialog', 'Dialogs.lambda$showTapToRevealTimeoutPickerDialog$13', 'Pick the seconds in the timeout picker and tap OK',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:316-317')
gui('Dialogs.showBackupVersionsPickerDialog', 'Dialogs.lambda$showBackupVersionsPickerDialog$14', 'Pick the number of kept backup versions and tap OK',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:345-349')

# --- error dialogs (Dialogs.java:379-418, the String/CharSequence overload that the other overloads forward to)
e('Dialogs.showErrorDialog(Context,String,CharSequence,OnClickListener)', 'Dialogs.lambda$showErrorDialog$18', 'FRAMEWORK',
  'the error dialog is shown: its OnShowListener replaces the Details button click listener (the first tap shows the details, the next copies them)',
  evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:401-404')
gui('Dialogs.showErrorDialog(Context,String,CharSequence,OnClickListener)', 'Dialogs.lambda$showErrorDialog$15', 'Tap OK in the error dialog',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:391-395')
gui('Dialogs.lambda$showErrorDialog$18', 'Dialogs.lambda$showErrorDialog$17', 'Tap Details, then Copy, in the error dialog (copies the error text to the clipboard)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:403-413')

# --- multi-error dialogs (Dialogs.java:427-487); the Details button has no show listener here
gui('Dialogs.showMultiErrorDialog', 'Dialogs.lambda$showMultiErrorDialog$19', 'Tap OK in the multi-error dialog',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:434-438')
gui('Dialogs.showMultiErrorDialog', 'Dialogs.lambda$showMultiErrorDialog$20', 'Tap Details in the multi-error dialog (opens the full list)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:439-441')
e('Dialogs.showDetailedMultiErrorDialog', 'Dialogs.lambda$showDetailedMultiErrorDialog$23', 'FRAMEWORK',
  'the detailed error dialog is shown: its OnShowListener sets the Copy button click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:476-479')
gui('Dialogs.showDetailedMultiErrorDialog', 'Dialogs.lambda$showDetailedMultiErrorDialog$21', 'Tap OK in the detailed error dialog',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:468-472')
gui('Dialogs.lambda$showDetailedMultiErrorDialog$23', 'Dialogs.lambda$showDetailedMultiErrorDialog$22',
    'Tap Copy in the detailed error dialog (copies all the error texts to the clipboard)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:478-483')

# --- time sync warning (Dialogs.java:489-513): shown only when the automatic date and time is off (MainActivity.java:757-759)
gui('Dialogs.showTimeSyncWarningDialog', 'Dialogs.lambda$showTimeSyncWarningDialog$24', 'Tap Yes in the time sync warning (opens the date settings)',
    env=ENV_AUTO_TIME_OFF, evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:499-505; SRC ui/MainActivity.java:757-762')
e('Dialogs.lambda$showTimeSyncWarningDialog$24', 'MainActivity.lambda$checkTimeSyncSetting$19', 'CALL',
  'listener.onClick(dialog, which): the MainActivity listener opens the date settings (the only caller)', cls='non_standard',
  via='DialogInterface.OnClickListener.onClick (interface call; the lambda is passed at MainActivity.java:759)',
  evidence='SRC ui/dialogs/Dialogs.java:503-504; SRC ui/MainActivity.java:759-762')
gui('Dialogs.showTimeSyncWarningDialog', 'Dialogs.lambda$showTimeSyncWarningDialog$25', 'Tap No in the time sync warning (the warning is turned off when the box is ticked)',
    env=ENV_AUTO_TIME_OFF, evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:507-511')

# --- importer list (Dialogs.java:515-540)
# The dialog is opened from two rows (isDirect false for the file import, isDirect true for the app import), and its OK button
# always calls the same listener code. The route is state-blind, so the dialog is split into two context variants:
#   @FILE: opened by pref_import (isDirect false); OK goes to the file listener lambda$onCreatePreferences$5
#   @APP:  opened by pref_import_app (isDirect true); OK goes to the app listener lambda$onCreatePreferences$7
_IMP_FILE = 'Dialogs.showImportersDialog@FILE'
_IMP_APP = 'Dialogs.showImportersDialog@APP'
_IMP_OK_FILE = 'Dialogs.lambda$showImportersDialog$27@FILE'
_IMP_OK_APP = 'Dialogs.lambda$showImportersDialog$27@APP'
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$6', _IMP_FILE, 'CALL',
  'the file import row opens the importer dialog (isDirect false)',
  guard='the call passes isDirect false (ImportExportPreferencesFragment.java:107)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-107')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$8', _IMP_APP, 'CALL',
  'the app import row opens the importer dialog (isDirect true)',
  guard='the call passes isDirect true (ImportExportPreferencesFragment.java:119)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:117-119')
gui(_IMP_FILE, 'Dialogs.lambda$showImportersDialog$26', 'Pick an app in the importer list (its help text is shown)',
    evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:529-531')
# The app dialog (isDirect) opens with index 0 checked (Dialogs.java:519-522,528); index 0 of the direct-filtered
# list is Authy (DatabaseImporter.java:99-102; Authy supportsDirect, :37), so OK on this path needs a row tap first
_IMP_PICK_APP = 'Dialogs.lambda$showImportersDialog$26@APP'
gui(_IMP_APP, _IMP_PICK_APP, 'Tap the Google Authenticator row in the importer list (its help text is shown)',
    guard='the Google Authenticator row is tapped (the default checked row is Authy: isDirect leaves i at 0, Dialogs.java:519-522,528; Authy is first among supportsDirect entries, DatabaseImporter.java:99-102,37)',
    evidence=FW_ITEM + '; FW-SRC core/java/android/widget/AbsListView.java:1136-1150 (single-choice tap sets the checked row); SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:37,44')
e(_IMP_FILE, 'DatabaseImporter$Definition.getName', 'REGISTER', 'Creates the lambda / method reference (its body runs when invoked)',
  evidence='SRC Dialogs.java:517 (bytecode)')
e(_IMP_APP, 'DatabaseImporter$Definition.getName', 'REGISTER', 'Creates the lambda / method reference (its body runs when invoked)',
  evidence='SRC Dialogs.java:517 (bytecode)')
gui(_IMP_FILE, _IMP_OK_FILE, 'Tap OK in the importer dialog (gives the chosen importer to the listener)',
    evidence=FW_CLICK + '; INFERRED Material MaterialAlertDialogBuilder (Dialogs.java:533; the Material library source is not on disk); SRC ui/dialogs/Dialogs.java:533-538')
gui(_IMP_PICK_APP, _IMP_OK_APP, 'Tap OK after the Google Authenticator row was tapped (gives the chosen importer to the listener)',
    guard='the GA row was tapped first: in the single-choice list a tap sets the checked row (AbsListView.java:1136-1150), so OK reads the GA importer (Dialogs.java:537), not the default Authy row',
    evidence=FW_CLICK + '; INFERRED Material MaterialAlertDialogBuilder (Dialogs.java:533; the Material library source is not on disk); SRC ui/dialogs/Dialogs.java:533-538')

# --- partial Google Auth import warning (Dialogs.java:542-581)
e('Dialogs.showPartialGoogleAuthImportWarningDialog', 'Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$28', 'CALL',
  'the stream map turns each missing index into its text', cls='non_standard',
  via='java.util.stream.Stream.map (JDK) calls the Function lambda$showPartialGoogleAuthImportWarningDialog$28 for each index',
  evidence='SRC ui/dialogs/Dialogs.java:543-545; INFERRED Stream.map (JDK source not read)')
gui('Dialogs.showPartialGoogleAuthImportWarningDialog', 'Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$29',
    'Tap OK in the partial import warning (the listener continues the import)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:560-562')
e('Dialogs.showPartialGoogleAuthImportWarningDialog', 'Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$31', 'FRAMEWORK',
  'the warning dialog is shown: its OnShowListener sets the Show error details click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:570-578')
gui('Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$31', 'Dialogs.lambda$showPartialGoogleAuthImportWarningDialog$30',
    'Tap Show error details in the partial import warning (the error list appears)',
    guard='the scan had errors (the button exists only then, Dialogs.java:565-567)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:571-576')

# --- backup versions strategy (Dialogs.java:583-629)
e('Dialogs.showBackupsVersioningStrategy', 'Dialogs.lambda$showBackupsVersioningStrategy$35', 'FRAMEWORK',
  'the dialog is shown: its OnShowListener selects the radio button of the current strategy', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:619-627')
gui('Dialogs.showBackupsVersioningStrategy', 'Dialogs.lambda$showBackupsVersioningStrategy$32', 'Pick a strategy radio button in the backup versions dialog',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:591-599')
gui('Dialogs.lambda$showBackupsVersioningStrategy$32', 'Dialogs.lambda$showBackupsVersioningStrategy$34',
    'Tap OK in the backup versions dialog after keeping X versions is picked', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:594,609-616')
gui('Dialogs.lambda$showBackupsVersioningStrategy$32', 'Dialogs.lambda$showBackupsVersioningStrategy$33',
    'Tick the risk checkbox (shown after the single-backup radio button is picked)',
    guard='the single-backup radio button is picked (the checkbox is visible only then, Dialogs.java:596-598)',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:600-605')
gui('Dialogs.lambda$showBackupsVersioningStrategy$33', 'Dialogs.lambda$showBackupsVersioningStrategy$34',
    'Tap OK in the backup versions dialog after single backup is picked and the risk is accepted',
    guard='the risk checkbox is ticked (OK is enabled only then, Dialogs.java:600-604)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:609-616')

# --- delete entries (Dialogs.java:71-97)
e('Dialogs.showDeleteEntriesDialog', 'Dialogs.lambda$showDeleteEntriesDialog$0', 'CALL',
  'the stream map turns each entry into its name for the message', cls='non_standard',
  via='java.util.stream.Stream.map (JDK) calls the Function lambda$showDeleteEntriesDialog$0 for each entry',
  evidence='SRC ui/dialogs/Dialogs.java:75-77; INFERRED Stream.map (JDK source not read)')

# --- caller-specific edges: the listeners that the Dialogs callers pass in (the taps of the dialogs above do not reach them)
gui('MainActivity.onStart', 'MainActivity.lambda$onStart$21', 'Tap OK in the vault-load error dialog (the app closes)',
    guard='reading the vault file threw VaultRepositoryException (MainActivity.java:955-959)',
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:955-959; SRC ui/dialogs/Dialogs.java:391-395')
gui('MainActivity.onStart', 'MainActivity.lambda$onStart$22', 'Tap OK in the plaintext vault error dialog (the app closes)',
    guard='the vault file is plain text and loading it threw VaultRepositoryException (MainActivity.java:963-972)',
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:963-972; SRC ui/dialogs/Dialogs.java:391-395')
gui('MainActivity.lambda$startDecodeQrCodeImages$18', 'MainActivity.lambda$startDecodeQrCodeImages$17',
    'Tap OK in an import error dialog of the QR scan (imports the readable entries)',
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:699,712,719,721')
gui('MainActivity.lambda$updateErrorCard$27', 'MainActivity.lambda$updateErrorCard$26', 'Tap OK in the backup error dialog (opens the backup settings)',
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1169-1171; SRC ui/dialogs/Dialogs.java:391-395')
gui('MainActivity.lambda$updateErrorCard$29', 'MainActivity.lambda$updateErrorCard$28', 'Tap Yes in the backup reminder dialog (opens the backup settings)',
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1181-1188')
gui('MainActivity$ActionModeCallbacks.onActionItemClicked', 'MainActivity$ActionModeCallbacks.lambda$onActionItemClicked$1',
    'Tap Yes in the delete dialog (removes the selected entries)', needs_state=ST_DELETE_DIALOG,
    evidence=FW_CLICK + '; SRC ui/MainActivity.java:1508-1516; SRC ui/dialogs/Dialogs.java:94')

# --- batch 3 (unlocking power): each activity constructor is reachable, but the framework calls onCreate after it (LIFECYCLE), so the
# six activity onCreate methods were missing their one edge. Then the child results that feed the MainActivity launchers (lambda$new$2 to
# $6, in declaration order: scan, assign icons, preferences, edit entry, add entry), the entry list fragment, its RecyclerView adapter, and the
# row tap listeners.
e('EditEntryActivity.<init>', 'EditEntryActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the add or edit page',
  evidence=FW_CREATE + '; SRC ui/EditEntryActivity.java:165')
e('AssignIconsActivity.<init>', 'AssignIconsActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the assign-icons page',
  evidence=FW_CREATE + '; SRC ui/AssignIconsActivity.java:57')
e('PreferencesActivity.<init>', 'PreferencesActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the settings page',
  evidence=FW_CREATE + '; SRC ui/PreferencesActivity.java:24')
sup(('PreferencesActivity.onCreate', 'MainPreferencesFragment.<init>'))
e('PreferencesActivity.onCreate', 'MainPreferencesFragment.<init>', 'CALL', 'the settings page creates its main fragment on a fresh start',
  guard='onCreate did not abort (PreferencesActivity.java:26-27, abortIfOrphan returns false) and savedInstanceState is null (PreferencesActivity.java:40)', evidence='SRC ui/PreferencesActivity.java:26-27,40-41')
e('ScannerActivity.<init>', 'ScannerActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the scanner',
  evidence=FW_CREATE + '; SRC ui/ScannerActivity.java:53')
e('TransferEntriesActivity.<init>', 'TransferEntriesActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the transfer page',
  evidence=FW_CREATE + '; SRC ui/TransferEntriesActivity.java:55')
e('AboutActivity.<init>', 'AboutActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the about page',
  evidence=FW_CREATE + '; SRC ui/AboutActivity.java:38')

# child results into the MainActivity launchers (MainActivity.java:135-190, the launcher order is auth, intro, scan, assign icons, preferences,
# edit entry, add entry, code scan). A launcher callback runs only when the child finishes with RESULT_OK and the intent is set.
e('ScannerActivity.finish', 'MainActivity.lambda$new$2', 'RESULT', 'setResult(RESULT_OK) with the scanned entries, then finish: the scan launcher runs',
  evidence=FW_RESULT + '; SRC ui/ScannerActivity.java:236-241; SRC ui/MainActivity.java:151-157')
e('AssignIconsActivity.saveAndFinish', 'MainActivity.lambda$new$3', 'RESULT',
  'setResult(RESULT_OK) with the entry UUIDs, then finish: the assign-icons launcher runs', guard='saveAndBackupVault() returned true (AssignIconsActivity.java:146)',
  evidence=FW_RESULT + '; SRC ui/AssignIconsActivity.java:125-149; SRC ui/MainActivity.java:159-165')
e('PreferencesActivity.onOptionsItemSelected', 'MainActivity.lambda$new$4', 'RESULT',
  'the settings page closes with Up or Back: the preferences launcher runs onPreferencesResult (no result check)',
  evidence=FW_RESULT + '; ' + FW_BACK + '; SRC ui/PreferencesActivity.java:69-73; SRC ui/MainActivity.java:167')
e('EditEntryActivity.saveAndFinish', 'MainActivity.lambda$new$5', 'RESULT',
  'setResult(RESULT_OK) and finish after an existing entry is saved: the edit launcher runs', guard='the page was opened for an existing entry (MainActivity.java:516-520)',
  evidence=FW_RESULT + '; SRC ui/EditEntryActivity.java:698-706; SRC ui/MainActivity.java:170-176')
# Fix-design 02 (C3 route 02): saveAndFinish conflates its two callers. deleteAndFinish calls it with
# delete=true (EditEntryActivity.java:695) and addAndFinish with delete=false (:680), but the shared node
# fed both result launchers, so a delete could reach the add launcher (lambda$new$6) and hence
# onAddEntryResult/onEntryAdded, which throw or return early for a removed entry (UUIDMap.java:124-130;
# EntryListView.java:444-446). The add caller gets its own variant, following the @SETPWD/@SVG_PICK
# pattern; the plain node keeps only the edit launcher, which is what a delete result reaches
# (onEditEntryResult only refreshes the list). The delete path can therefore no longer reach
# setTempHighlightEntry; the save path (onSave -> addAndFinish -> saveAndFinish@ADD -> lambda$new$6)
# is the route to the target. The two hand edges below replace the auto rows on the save branch
# with the branch guards (save item tapped; parse succeeds and no duplicate for a new entry).
e('EditEntryActivity.onOptionsItemSelected', 'EditEntryActivity.onSave', 'CALL',
  'the save toolbar item is tapped (not delete, which is hidden for a new entry, EditEntryActivity.java:658-659)',
  guard='itemId == R.id.action_save (EditEntryActivity.java:539-540)',
  evidence='SRC ui/EditEntryActivity.java:535-544,656-660')
e('EditEntryActivity.onSave', 'EditEntryActivity.addAndFinish', 'CALL',
  'the entry parses and, for a new entry, has no duplicate name and issuer, so the save finishes',
  guard='parseEntry() succeeds (EditEntryActivity.java:852-856) and no existing entry has the same name and issuer (:859-864); otherwise onSaveError or the duplicate sheet runs instead',
  evidence='SRC ui/EditEntryActivity.java:845-867')
e('EditEntryActivity.addAndFinish', 'EditEntryActivity.saveAndFinish@ADD', 'CALL',
  'addAndFinish saves the entry with delete=false (EditEntryActivity.java:680)',
  evidence='SRC ui/EditEntryActivity.java:668-682')
e('EditEntryActivity.saveAndFinish@ADD', 'MainActivity.lambda$new$5', 'RESULT',
  'setResult(RESULT_OK) and finish after an existing entry is saved: the edit launcher runs', guard='the page was opened for an existing entry (MainActivity.java:516-520); the save came from addAndFinish (EditEntryActivity.java:680)',
  evidence=FW_RESULT + '; SRC ui/EditEntryActivity.java:698-706; SRC ui/MainActivity.java:170-176')
e('EditEntryActivity.saveAndFinish@ADD', 'MainActivity.lambda$new$6', 'RESULT',
  'setResult(RESULT_OK) and finish after a new entry is saved: the add launcher runs', guard='the vault backup succeeds (saveAndBackupVault() returned true, EditEntryActivity.java:703) and delete is false (saveAndFinish from addAndFinish, EditEntryActivity.java:680)',
  evidence=FW_RESULT + '; SRC ui/EditEntryActivity.java:698-706; SRC ui/MainActivity.java:178-184')

# --- stage 2, group G1 corrections: guards on CALL edges whose auto rows had no guard (a hand edge on the same pair replaces the auto row)
# Aegis decrypt is split by DecryptListener: the Welcome import and the ImportEntries import use
# different listeners, so a task built from one prefix can never deliver to the other's listener
# (that mix was route 16 step 30 and the route 06 intro-prefix confusion). The Welcome slide reads
# ONLY with AegisImporter (WelcomeSlide.java:66-67, 'new AegisImporter'), so the virtual edges from
# WelcomeSlide$2 to every other importer's decrypt are false and are suppressed below.
e('WelcomeSlide.lambda$startImportVault$2', 'AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@WELCOME', 'CALL',
  'the picked vault file is encrypted: the importer asks for the password and decrypts it',
  cls='explicit', guard='file read without error (WelcomeSlide.java:60-63) and the file is encrypted (state.isEncrypted(), WelcomeSlide.java:68)',
  evidence='SRC ui/slides/WelcomeSlide.java:60-63,68-69; SRC importers/AegisImporter.java:66-90')
# --- C3 sample fix 3: Aegis decrypt@IMPORT moved onto the @FILE variant (getKey route).
# The dumped getKey route ran the @APP prefix (GA row tapped) into Aegis decrypt@IMPORT
# through this hand edge's base src. That prefix cannot produce an Aegis state: Aegis
# has supportsDirect false (DatabaseImporter.java:34) and its getAppPath throws
# UnsupportedOperationException (AegisImporter.java:39-42), so the direct dialog never
# offers it; and the GA state on that prefix is never encrypted, so decrypt is never
# called at all. The genuine Aegis path is file-only (an encrypted vault file read
# returns EncryptedState, AegisImporter.java:44-52). The edge therefore moves from the
# base node to the @FILE variant fed by startImportFile (fix 2); the base node keeps
# every other importer's dispatch but no longer reaches Aegis decrypt. The auto CHA
# edge to Aegis decrypt stays suppressed by this hand edge's base pair, as before.
e('ImportEntriesActivity.processImporterState@FILE', 'AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@IMPORT', 'CALL',
  'the picked file import is an encrypted Aegis vault: the importer asks for the password and decrypts it',
  guard='the file import picked Aegis (supportsDirect false, DatabaseImporter.java:34; getAppPath throws, AegisImporter.java:39-42) and the picked vault file is encrypted (read returns EncryptedState, AegisImporter.java:44-52)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/AegisImporter.java:44-52,85-90')

# --- C3 sample fix 2: processImporterState dispatch split by import path (AndOtp route).
# The dumped AndOtp route ran the @APP prefix (Google Authenticator row tapped in the
# direct dialog) into AndOtpImporter decrypt through the shared virtual edge
# processImporterState -> AndOtp decrypt (auto CHA, ImportEntriesActivity.java:179).
# That prefix cannot produce an AndOtp state: andOTP has supportsDirect false
# (DatabaseImporter.java:35) and its getAppPath throws UnsupportedOperationException
# (AndOtpImporter.java:59-62), so the app-import path never yields it; and the GA state
# built on that prefix is never encrypted (GoogleAuthImporter.State super(false),
# GoogleAuthImporter.java:74-76), so processImporterState takes the decrypted branch and
# never calls state.decrypt at all. The genuine AndOtp path is file-only: the @FILE
# dialog pick, the file picker, AndOtpImporter.read returning EncryptedState when the
# file is not JSON (AndOtpImporter.java:76-80). The dispatch is therefore split: the
# file reader feeds a @FILE variant of processImporterState (and the base node, for all
# other importers), the auto CHA edge to AndOtp decrypt is suppressed, and only the
# @FILE variant reaches AndOtp decrypt. The @APP prefix keeps the base node and its
# other importers' dispatch, but no longer reaches AndOtp decrypt.
# --- file-pick v2 V8 (PRIVATE BUILD, not pushed): base-feed deletion (LAST, design section 5 step 2).
# The file-to-base hand edge is DELETED (it was fix 2's pre-variant compromise: "the file
# reader feeds ... the base node, for all other importers"). Once every non-default importer
# has its own variant dispatch, the base feed is a pure leak. KEPT: startImportFile ->
# processImporterState@FILE (Aegis-default and decrypted-only @FILE routes). After V8 the
# base node is reachable only from lambda$startImportApp$5 (the @APP feed), and no decrypt
# incoming count changes (all eight variant targets already land only via their variant E19s).
e('ImportEntriesActivity.startImportFile', 'ImportEntriesActivity.processImporterState@FILE', 'CALL',
  'the file just read is processed on the file-import path',
  guard='the import page was opened with a file (startImport@FILE, ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode)')
sup(('ImportEntriesActivity.processImporterState', 'AndOtpImporter$EncryptedState.decrypt(Context,DecryptListener)'))

# --- C3 sample fix 4: Stratum dispatch split (Stratum decrypt route).
# The dumped Stratum route ran the @APP prefix (GA row tapped) into Stratum decrypt
# through the shared virtual edge processImporterState -> Stratum decrypt (auto CHA,
# :179). That prefix cannot produce a Stratum state: the GA state built on it is never
# encrypted (GoogleAuthImporter.State super(false)), so processImporterState takes the
# decrypted branch and never calls state.decrypt. Stratum is genuinely reachable BOTH
# ways, unlike AndOtp/Aegis: it has supportsDirect true (DatabaseImporter.java:49)
# and a real getAppPath (StratumImporter.java:65-66), so the direct dialog CAN offer
# it — but only when its own row is tapped, not GA's. The fix therefore threads a
# @STRATUM chain (Stratum row -> OK -> import-app listener -> import page -> app
# import -> root-shell callback -> @STRATUM dispatch) alongside the @FILE variant,
# and suppresses the shared auto CHA edge. The base node keeps every other importer's
# dispatch. Note: the variant hand edge from lambda$startImportApp$5 suppresses the
# auto lambda$5 -> processImporterState edge by its base pair, so the base edge is
# re-written by hand below (same pattern as startImportFile in fix 2). The
# app-version-warning lambdas are NOT threaded for @STRATUM (direct path only: the
# supported-version case suffices for REACHABLE; a Stratum import through the warning
# would need its own variants).
e('ImportEntriesActivity.lambda$startImportApp$5', 'ImportEntriesActivity.processImporterState', 'CALL',
  'Direct call', evidence='SRC ImportEntriesActivity.java:157 (bytecode)')
sup(('ImportEntriesActivity.processImporterState', 'StratumImporter$EncryptedState.decrypt(Context,DecryptListener)'))
# --- file-pick v2 V2 (PRIVATE BUILD, not pushed): Stratum @FILE_STRATUM variant chain (E1, E3-E16, 2x E19).
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# One pick chain, two dispatch guards (AUTHENTICATORPRO header -> Encrypted; AuthenticatorPro
# legacy header -> Legacy). V2 combined private state: the old @FILE Encrypted hand edge
# (E8360a30f) is DELETED, replaced by the variant Encrypted E19 below; the Legacy base-pair
# sup below lands with the chain (the variant Legacy E19 hand edge already suppresses the
# Legacy auto copies by the manual-edge base-pair rule — verified in the chain-first build,
# where Legacy incoming was already [variant] only — so the sup is explicit, not load-bearing).
# Encrypted incoming 1 (variant only); Legacy incoming 1 (variant only). Never pushed in an
# intermediate state (R1: single final commit when full section 9 passes).
sup(('ImportEntriesActivity.processImporterState', 'StratumImporter$LegacyEncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_STRATUM', 'Tap the `Stratum` row in the importer list (its help text is shown)',
  guard='the `Stratum` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_STRATUM', 'Dialogs.lambda$showImportersDialog$27@FILE_STRATUM', 'Tap OK after the `Stratum` row was tapped (gives the chosen importer to the listener)',
  guard='the `Stratum` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `Stratum` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_STRATUM', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_STRATUM', 'CALL',
  'the OK button gives the chosen `Stratum` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `Stratum` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_STRATUM', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_STRATUM', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `Stratum` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_STRATUM', 'ImportExportPreferencesFragment.lambda$new$0@FILE_STRATUM', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_STRATUM', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_STRATUM', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_STRATUM', 'ImportFileTask.doInBackground@FILE_STRATUM', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_STRATUM', 'ImportFileTask.onPostExecute@FILE_STRATUM', 'ASYNC',
  'the result is posted to the main thread (the `Stratum` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_STRATUM', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_STRATUM', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_STRATUM', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_STRATUM', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `Stratum` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_STRATUM', 'ImportEntriesActivity.<init>@FILE_STRATUM', 'INTENT',
  'the import page opens with the chosen `Stratum` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_STRATUM', 'ImportEntriesActivity.onCreate@FILE_STRATUM', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_STRATUM', 'ImportEntriesActivity.startImport@FILE_STRATUM', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_STRATUM', 'ImportEntriesActivity.startImportFile@FILE_STRATUM', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_STRATUM', 'ImportEntriesActivity.processImporterState@FILE_STRATUM', 'CALL',
  'the file just read is processed on the `Stratum` file-import path',
  guard='the import page was opened with a file for the `Stratum` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_STRATUM', 'StratumImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted Stratum backup: the importer asks for the password and decrypts it',
  guard='the file import picked Stratum and the file is not JSON, so readExternal falls to readEncrypted and the AUTHENTICATORPRO header yields EncryptedState (StratumImporter.java:80-105)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/StratumImporter.java:80-105')
e('ImportEntriesActivity.processImporterState@FILE_STRATUM', 'StratumImporter$LegacyEncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is a legacy-header Stratum backup: the importer asks for the password and decrypts it',
  guard='the file import picked Stratum and the file is not JSON, so readExternal falls to readEncrypted and the AuthenticatorPro (legacy) header yields LegacyEncryptedState (StratumImporter.java:80-105)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/StratumImporter.java:80-105')
# --- file-pick v2 V3 (PRIVATE BUILD, not pushed): TOTP Authenticator @FILE_TOTP variant chain (E1, E3-E16, E19).
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# V3 combined private state: the TOTP base-pair sup below lands with the chain (the variant E19
# hand edge already suppressed all three TOTP auto copies in the chain-first build — incoming
# was already [variant] only — so the sup is explicit, not load-bearing). TOTP incoming 1
# (variant only). Never pushed in an intermediate state (R1).
sup(('ImportEntriesActivity.processImporterState', 'TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_TOTP', 'Tap the `TOTP Authenticator` row in the importer list (its help text is shown)',
  guard='the `TOTP Authenticator` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_TOTP', 'Dialogs.lambda$showImportersDialog$27@FILE_TOTP', 'Tap OK after the `TOTP Authenticator` row was tapped (gives the chosen importer to the listener)',
  guard='the `TOTP Authenticator` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `TOTP Authenticator` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_TOTP', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TOTP', 'CALL',
  'the OK button gives the chosen `TOTP Authenticator` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `TOTP Authenticator` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TOTP', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TOTP', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `TOTP Authenticator` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TOTP', 'ImportExportPreferencesFragment.lambda$new$0@FILE_TOTP', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_TOTP', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_TOTP', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_TOTP', 'ImportFileTask.doInBackground@FILE_TOTP', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_TOTP', 'ImportFileTask.onPostExecute@FILE_TOTP', 'ASYNC',
  'the result is posted to the main thread (the `TOTP Authenticator` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_TOTP', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TOTP', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TOTP', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TOTP', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `TOTP Authenticator` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TOTP', 'ImportEntriesActivity.<init>@FILE_TOTP', 'INTENT',
  'the import page opens with the chosen `TOTP Authenticator` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_TOTP', 'ImportEntriesActivity.onCreate@FILE_TOTP', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_TOTP', 'ImportEntriesActivity.startImport@FILE_TOTP', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_TOTP', 'ImportEntriesActivity.startImportFile@FILE_TOTP', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_TOTP', 'ImportEntriesActivity.processImporterState@FILE_TOTP', 'CALL',
  'the file just read is processed on the `TOTP Authenticator` file-import path',
  guard='the import page was opened with a file for the `TOTP Authenticator` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_TOTP', 'TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted TOTP Authenticator backup: the importer asks for the password and decrypts it',
  guard='the file import picked TOTP Authenticator and the file read is the external (isInternal false) branch, so read returns EncryptedState (TotpAuthenticatorImporter.java:70-95); the internal branch always yields DecryptedState and never reaches decrypt',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/TotpAuthenticatorImporter.java:70-95')
# --- file-pick v2 V4 (PRIVATE BUILD, not pushed): FreeOTP @FILE_FREEOTP variant chain (E1, E3-E16, E19).
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# V4 combined private state: the FreeOTP base-pair sup below lands with the chain (the variant E19
# hand edge already suppressed all three FreeOTP auto copies in the chain-first build — incoming
# was already [variant] only — so the sup is explicit, not load-bearing). FreeOTP incoming 1
# (variant only). Never pushed in an intermediate state (R1). R3: v2 item 1 for FreeOTP
# evaluated here (file route through @FILE_FREEOTP); re-read after F2 as shortest-FILE-route.
sup(('ImportEntriesActivity.processImporterState', 'FreeOtpImporter$EncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_FREEOTP', 'Tap the `FreeOTP` row in the importer list (its help text is shown)',
  guard='the `FreeOTP` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_FREEOTP', 'Dialogs.lambda$showImportersDialog$27@FILE_FREEOTP', 'Tap OK after the `FreeOTP` row was tapped (gives the chosen importer to the listener)',
  guard='the `FreeOTP` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `FreeOTP` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_FREEOTP', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_FREEOTP', 'CALL',
  'the OK button gives the chosen `FreeOTP` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `FreeOTP` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_FREEOTP', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_FREEOTP', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `FreeOTP` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_FREEOTP', 'ImportExportPreferencesFragment.lambda$new$0@FILE_FREEOTP', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_FREEOTP', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_FREEOTP', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_FREEOTP', 'ImportFileTask.doInBackground@FILE_FREEOTP', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_FREEOTP', 'ImportFileTask.onPostExecute@FILE_FREEOTP', 'ASYNC',
  'the result is posted to the main thread (the `FreeOTP` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_FREEOTP', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_FREEOTP', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_FREEOTP', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_FREEOTP', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `FreeOTP` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_FREEOTP', 'ImportEntriesActivity.<init>@FILE_FREEOTP', 'INTENT',
  'the import page opens with the chosen `FreeOTP` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_FREEOTP', 'ImportEntriesActivity.onCreate@FILE_FREEOTP', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_FREEOTP', 'ImportEntriesActivity.startImport@FILE_FREEOTP', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_FREEOTP', 'ImportEntriesActivity.startImportFile@FILE_FREEOTP', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_FREEOTP', 'ImportEntriesActivity.processImporterState@FILE_FREEOTP', 'CALL',
  'the file just read is processed on the `FreeOTP` file-import path',
  guard='the import page was opened with a file for the `FreeOTP` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_FREEOTP', 'FreeOtpImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted FreeOTP backup: the importer asks for the password and decrypts it',
  guard='the file import picked FreeOTP and the file has V2 magic, so read returns EncryptedState via readV2 (FreeOtpImporter.java:69-86,106-115); a V1 file yields DecryptedStateV1 and takes the decrypted branch instead',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/FreeOtpImporter.java:69-115')
# --- file-pick v2 V5 (PRIVATE BUILD, not pushed): 2FAS @FILE_TWOFAS variant chain (E1, E3-E16, E19) + sup.
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# Combined single build per design section 5 step 1 (chain + sup together; the hand-E19
# suppression mechanism is already proven at V2/V3/V4, so no separate chain-first build is
# needed here — the combined gates below verify the outcome). Never pushed in an
# intermediate state (R1).
sup(('ImportEntriesActivity.processImporterState', 'TwoFASImporter$EncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_TWOFAS', 'Tap the `2FAS` row in the importer list (its help text is shown)',
  guard='the `2FAS` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_TWOFAS', 'Dialogs.lambda$showImportersDialog$27@FILE_TWOFAS', 'Tap OK after the `2FAS` row was tapped (gives the chosen importer to the listener)',
  guard='the `2FAS` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `2FAS` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_TWOFAS', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TWOFAS', 'CALL',
  'the OK button gives the chosen `2FAS` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `2FAS` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_TWOFAS', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TWOFAS', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `2FAS` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_TWOFAS', 'ImportExportPreferencesFragment.lambda$new$0@FILE_TWOFAS', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_TWOFAS', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_TWOFAS', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_TWOFAS', 'ImportFileTask.doInBackground@FILE_TWOFAS', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_TWOFAS', 'ImportFileTask.onPostExecute@FILE_TWOFAS', 'ASYNC',
  'the result is posted to the main thread (the `2FAS` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_TWOFAS', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TWOFAS', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_TWOFAS', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TWOFAS', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `2FAS` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_TWOFAS', 'ImportEntriesActivity.<init>@FILE_TWOFAS', 'INTENT',
  'the import page opens with the chosen `2FAS` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_TWOFAS', 'ImportEntriesActivity.onCreate@FILE_TWOFAS', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_TWOFAS', 'ImportEntriesActivity.startImport@FILE_TWOFAS', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_TWOFAS', 'ImportEntriesActivity.startImportFile@FILE_TWOFAS', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_TWOFAS', 'ImportEntriesActivity.processImporterState@FILE_TWOFAS', 'CALL',
  'the file just read is processed on the `2FAS` file-import path',
  guard='the import page was opened with a file for the `2FAS` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_TWOFAS', 'TwoFASImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted 2FAS backup: the importer asks for the password and decrypts it',
  guard='the file import picked 2FAS (supportsDirect false, DatabaseImporter.java:33; getAppPath throws, TwoFASImporter.java:55-57) and the file is valid JSON with schemaVersion ≤ 4 and `servicesEncrypted` split into ≥ 3 parts, so read returns EncryptedState (TwoFASImporter.java:60-84)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/TwoFASImporter.java:60-84')
# --- file-pick v2 V6 (PRIVATE BUILD, not pushed): Authenticator Plus @FILE_AUTHPLUS variant chain (E1, E3-E16, E19) + sup.
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# Combined single build per design section 5 step 1 (chain + sup together). Never pushed in an
# intermediate state (R1).
sup(('ImportEntriesActivity.processImporterState', 'AuthenticatorPlusImporter$EncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_AUTHPLUS', 'Tap the `Authenticator Plus` row in the importer list (its help text is shown)',
  guard='the `Authenticator Plus` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_AUTHPLUS', 'Dialogs.lambda$showImportersDialog$27@FILE_AUTHPLUS', 'Tap OK after the `Authenticator Plus` row was tapped (gives the chosen importer to the listener)',
  guard='the `Authenticator Plus` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `Authenticator Plus` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_AUTHPLUS', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_AUTHPLUS', 'CALL',
  'the OK button gives the chosen `Authenticator Plus` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `Authenticator Plus` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_AUTHPLUS', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_AUTHPLUS', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `Authenticator Plus` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_AUTHPLUS', 'ImportExportPreferencesFragment.lambda$new$0@FILE_AUTHPLUS', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_AUTHPLUS', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_AUTHPLUS', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_AUTHPLUS', 'ImportFileTask.doInBackground@FILE_AUTHPLUS', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_AUTHPLUS', 'ImportFileTask.onPostExecute@FILE_AUTHPLUS', 'ASYNC',
  'the result is posted to the main thread (the `Authenticator Plus` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_AUTHPLUS', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_AUTHPLUS', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_AUTHPLUS', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_AUTHPLUS', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `Authenticator Plus` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_AUTHPLUS', 'ImportEntriesActivity.<init>@FILE_AUTHPLUS', 'INTENT',
  'the import page opens with the chosen `Authenticator Plus` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_AUTHPLUS', 'ImportEntriesActivity.onCreate@FILE_AUTHPLUS', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_AUTHPLUS', 'ImportEntriesActivity.startImport@FILE_AUTHPLUS', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_AUTHPLUS', 'ImportEntriesActivity.startImportFile@FILE_AUTHPLUS', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_AUTHPLUS', 'ImportEntriesActivity.processImporterState@FILE_AUTHPLUS', 'CALL',
  'the file just read is processed on the `Authenticator Plus` file-import path',
  guard='the import page was opened with a file for the `Authenticator Plus` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_AUTHPLUS', 'AuthenticatorPlusImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted Authenticator Plus backup: the importer asks for the password and decrypts it',
  guard='the file import picked Authenticator Plus (supportsDirect false, DatabaseImporter.java:36; getAppPath throws, AuthenticatorPlusImporter.java:26-28) and read returns EncryptedState for any file (AuthenticatorPlusImporter.java:31-35)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/AuthenticatorPlusImporter.java:31-35')
# --- file-pick v2 V7 (PRIVATE BUILD, not pushed): Authy @FILE_AUTHY variant chain (E1, E3-E16, E19) + sup.
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# Combined single build per design section 5 step 1 (chain + sup together). After V7, all six
# v2 sups have landed, so the transient auto cross-edges from variant dispatch nodes should
# read ZERO (verified below). Never pushed in an intermediate state (R1).
sup(('ImportEntriesActivity.processImporterState', 'AuthyImporter$EncryptedState.decrypt(Context,DecryptListener)'))
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_AUTHY', 'Tap the `Authy` row in the importer list (its help text is shown)',
  guard='the `Authy` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_AUTHY', 'Dialogs.lambda$showImportersDialog$27@FILE_AUTHY', 'Tap OK after the `Authy` row was tapped (gives the chosen importer to the listener)',
  guard='the `Authy` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `Authy` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_AUTHY', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_AUTHY', 'CALL',
  'the OK button gives the chosen `Authy` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `Authy` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_AUTHY', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_AUTHY', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `Authy` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_AUTHY', 'ImportExportPreferencesFragment.lambda$new$0@FILE_AUTHY', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_AUTHY', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_AUTHY', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_AUTHY', 'ImportFileTask.doInBackground@FILE_AUTHY', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_AUTHY', 'ImportFileTask.onPostExecute@FILE_AUTHY', 'ASYNC',
  'the result is posted to the main thread (the `Authy` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_AUTHY', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_AUTHY', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_AUTHY', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_AUTHY', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `Authy` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_AUTHY', 'ImportEntriesActivity.<init>@FILE_AUTHY', 'INTENT',
  'the import page opens with the chosen `Authy` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_AUTHY', 'ImportEntriesActivity.onCreate@FILE_AUTHY', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_AUTHY', 'ImportEntriesActivity.startImport@FILE_AUTHY', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_AUTHY', 'ImportEntriesActivity.startImportFile@FILE_AUTHY', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_AUTHY', 'ImportEntriesActivity.processImporterState@FILE_AUTHY', 'CALL',
  'the file just read is processed on the `Authy` file-import path',
  guard='the import page was opened with a file for the `Authy` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_AUTHY', 'AuthyImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted Authy backup: the importer asks for the password and decrypts it',
  guard='the file import picked Authy, a `.key` entry is found in the preferences XML, and some entry in the file lacks both `decryptedSecret` and `secretSeed`, so read returns EncryptedState (AuthyImporter.java:101-135)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/AuthyImporter.java:101-135')
# --- FreeOtp stage 2 F2 (PRIVATE BUILD, not pushed): @FREEOTP app-import producer chain F1–F13 (LAST).
# Design helper/freeotp-design/DESIGN.md section 4 stage 2 (audit PASS). Mirrors the @STRATUM
# block node for node with @FREEOTP in place of @STRATUM. No app-version-warning lambdas
# (FreeOtp never reaches them: default supported = true) and no onCreate@FREEOTP side
# branches (not on the route; methods stay reachable via @APP/@FILE variants). Deliberately
# unchanged: GA pick/OK edges, lambda$startImportApp$5 -> GoogleAuthImporter.readFromApp,
# GA State label, processDecrypted branch. F2 gates (R4): FreeOtp decrypt 1 -> 2 (variant
# file E19 + F13); no other decrypt's incoming count changes; stage-2 auto total 27
# (pick 1, <init> 1, onCreate 6, startImport 8, startImportApp 1, onPostExecute 1,
# lambda$5 4, processImporterState 5 — the design's section 6 processImporterState 10 is
# corrected to 5 post-v2, since all six v2 decrypt pairs are suppressed and the @FREEOTP
# dispatch node gets only the 5 non-decrypt auto outs); any deviation explained edge by
# edge per design section 7 stop rule; any incoming edge to FreeOtp decrypt beyond
# E19/F13 sends the design back to audit. Independent pre-merge audit required (design
# section 7 item 5: auditor checks >= 1 in 3 new edges) before any push.
gui('Dialogs.showImportersDialog@APP', 'Dialogs.lambda$showImportersDialog$26@FREEOTP', 'Tap the FreeOTP row in the importer list (its help text is shown)',
  guard='the FreeOTP row is tapped (the default checked row on the direct dialog is Authy, `i` stays 0, Dialogs.java:519-522,528; FreeOTP is a `supportsDirect` entry, DatabaseImporter.java:42,99-102)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:42; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FREEOTP', 'Dialogs.lambda$showImportersDialog$27@FREEOTP', 'Tap OK after the FreeOTP row was tapped (gives the chosen importer to the listener)',
  guard='the FreeOTP row was tapped first, so OK reads the FreeOTP importer (Dialogs.java:537)',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538')
e('Dialogs.lambda$showImportersDialog$27@FREEOTP', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$7@FREEOTP', 'CALL',
  'the OK button gives the chosen importer to the import-app listener: the import page opens',
  guard='the dialog was opened by Import from another app (isDirect true, ImportExportPreferencesFragment.java:119)',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:119-121')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$7@FREEOTP', 'ImportExportPreferencesFragment.startImportEntriesActivity@FREEOTP', 'CALL',
  'Direct call', evidence='SRC ImportExportPreferencesFragment.java:120 (bytecode)')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FREEOTP', 'ImportEntriesActivity.<init>@FREEOTP', 'INTENT',
  'the import page opens with the chosen importer and no file (app import)',
  guard='the file argument is null on the app import path (ImportExportPreferencesFragment.java:120)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:120')
e('ImportEntriesActivity.<init>@FREEOTP', 'ImportEntriesActivity.onCreate@FREEOTP', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FREEOTP', 'ImportEntriesActivity.startImport@FREEOTP', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan(savedInstanceState) is false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157) and the file extra is null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104; SRC ui/AegisActivity.java:154-157')
e('ImportEntriesActivity.startImport@FREEOTP', 'ImportEntriesActivity.startImportApp@FREEOTP', 'CALL',
  'no file was passed and the installed app version is supported: the entries are read from the app',
  guard='no file was passed (ImportEntriesActivity.java:109) and isInstalledAppVersionSupported is true by default (DatabaseImporter.java:69-71; FreeOtpImporter does not override it, so no warning branch exists)',
  evidence='SRC ui/ImportEntriesActivity.java:109-111; SRC importers/DatabaseImporter.java:69-71')
e('ImportEntriesActivity.startImportApp@FREEOTP', 'RootShellTask.doInBackground@FREEOTP', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (open the root shell; started by AsyncTask.execute, not ProgressDialogTask.execute)',
  evidence=FW_ASYNC + '; SRC ui/ImportEntriesActivity.java:173; SRC ui/tasks/RootShellTask.java:17-20')
e('RootShellTask.doInBackground@FREEOTP', 'RootShellTask.onPostExecute@FREEOTP', 'ASYNC',
  'the shell is posted to the main thread',
  evidence=FW_ASYNC + '; SRC ui/tasks/RootShellTask.java:17,23-25')
e('RootShellTask.onPostExecute@FREEOTP', 'ImportEntriesActivity.lambda$startImportApp$5@FREEOTP', 'CALL',
  '_cb.onTaskFinished(shell): the callback reads the entries from the installed app, or closes the page when there is no root',
  evidence='SRC ui/tasks/RootShellTask.java:25,28-30; SRC ui/ImportEntriesActivity.java:143-174')
e('ImportEntriesActivity.lambda$startImportApp$5@FREEOTP', 'ImportEntriesActivity.processImporterState@FREEOTP', 'CALL',
  'Direct call', evidence='SRC ImportEntriesActivity.java:157 (bytecode)')
e('ImportEntriesActivity.processImporterState@FREEOTP', 'FreeOtpImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the FreeOTP app import is a V2 backup: the importer asks for the password and decrypts it',
  guard="the page's importer is FreeOTP (F1–F2 pick, DatabaseImporter.java:42); the root shell is present and root (ImportEntriesActivity.java:149-153, otherwise toast + finish before dispatch); the app state is a V2 EncryptedState (readFromApp → read(stream, true) → magic → readV2 → super(true): DatabaseImporter.java:79-87; FreeOtpImporter.java:69-78,106-110,130); and isEncrypted() is true so dispatch calls decrypt (ImportEntriesActivity.java:176-179)",
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/FreeOtpImporter.java:69-78,106-110,130; SRC importers/DatabaseImporter.java:42')
# CORRECTION 2026-11-01 (Stratum-correction step; refutes fix-4 edge, kept out of
# the judged table): the processImporterState@STRATUM -> Stratum decrypt edge is
# REMOVED. DatabaseImporter.readFromApp passes isInternal=true
# (DatabaseImporter.java:79-87), so StratumImporter.read takes readInternal
# (StratumImporter.java:70-72), which returns SqlState with super(false)
# (StratumImporter.java:324-328); processImporterState then takes the decrypted
# branch (ImportEntriesActivity.java:176-182) and EncryptedState.decrypt never
# fires on ANY app-import prefix. The @STRATUM chain up to processImporterState
# stays (genuine decrypted-branch path); the genuine Stratum decrypt path is
# @FILE only (readExternal -> readEncrypted -> EncryptedState, :80-105).
_IMP_PICK_STRATUM = 'Dialogs.lambda$showImportersDialog$26@STRATUM'
_IMP_OK_STRATUM = 'Dialogs.lambda$showImportersDialog$27@STRATUM'
gui('Dialogs.showImportersDialog@APP', _IMP_PICK_STRATUM, 'Tap the Stratum row in the importer list (its help text is shown)',
    guard='the Stratum row is tapped (Stratum supportsDirect, DatabaseImporter.java:49; the direct dialog lists only supportsDirect importers, Dialogs.java:516)',
    evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:49')
gui(_IMP_PICK_STRATUM, _IMP_OK_STRATUM, 'Tap OK after the Stratum row was tapped (gives the chosen importer to the listener)',
    guard='the Stratum row was tapped first: in the single-choice list a tap sets the checked row, so OK reads the Stratum importer (Dialogs.java:537)',
    evidence=FW_CLICK + '; INFERRED Material MaterialAlertDialogBuilder (Dialogs.java:533; the Material library source is not on disk); SRC ui/dialogs/Dialogs.java:533-538')
e(_IMP_OK_STRATUM, 'ImportExportPreferencesFragment.lambda$onCreatePreferences$7@STRATUM', 'CALL',
  'the OK button gives the chosen importer to the import-app listener: the import page opens',
  guard='the dialog was opened by Import from another app (isDirect true, ImportExportPreferencesFragment.java:119)',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:119-121')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$7@STRATUM', 'ImportExportPreferencesFragment.startImportEntriesActivity@STRATUM', 'CALL',
  'Direct call', evidence='SRC ImportExportPreferencesFragment.java:120 (bytecode)')
e('ImportExportPreferencesFragment.startImportEntriesActivity@STRATUM', 'ImportEntriesActivity.<init>@STRATUM', 'INTENT',
  'the import page opens with the chosen importer and no file (app import)',
  guard='the file argument is null on the app import path (ImportExportPreferencesFragment.java:120)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:120')
e('ImportEntriesActivity.<init>@STRATUM', 'ImportEntriesActivity.onCreate@STRATUM', 'LIFECYCLE', 'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@STRATUM', 'ImportEntriesActivity.startImport@STRATUM', 'CALL', 'the import page starts the import from its intent extras',
  guard='abortIfOrphan(savedInstanceState) is false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157) and the file extra is null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104; SRC ui/AegisActivity.java:154-157')
e('ImportEntriesActivity.startImport@STRATUM', 'ImportEntriesActivity.startImportApp@STRATUM', 'CALL',
  'no file was passed and the installed app version is supported: the entries are read from the app',
  guard='no file was passed (ImportEntriesActivity.java:109) and the installed app version is supported (isInstalledAppVersionSupported, ImportEntriesActivity.java:110)',
  evidence='SRC ui/ImportEntriesActivity.java:109-111')
# the root-shell async chain is variant-split too: feeding lambda$5@STRATUM from the
# SHARED onPostExecute node would let the @APP (GA) prefix reach the @STRATUM dispatch
# through the shared async nodes, so the @STRATUM chain uses its own async variants
# (same pattern as ImportFileTask@SVG_PICK / @SETTINGS_IMPORT elsewhere in this file)
e('ImportEntriesActivity.startImportApp@STRATUM', 'RootShellTask.doInBackground@STRATUM', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (open the root shell; started by AsyncTask.execute, not ProgressDialogTask.execute)',
  evidence=FW_ASYNC + '; SRC ui/ImportEntriesActivity.java:173; SRC ui/tasks/RootShellTask.java:17-20')
e('RootShellTask.doInBackground@STRATUM', 'RootShellTask.onPostExecute@STRATUM', 'ASYNC', 'the shell is posted to the main thread',
  evidence=FW_ASYNC + '; SRC ui/tasks/RootShellTask.java:17,23-25')
e('RootShellTask.onPostExecute@STRATUM', 'ImportEntriesActivity.lambda$startImportApp$5@STRATUM', 'CALL',
  '_cb.onTaskFinished(shell): the callback reads the entries from the installed app, or closes the page when there is no root',
  evidence='SRC ui/tasks/RootShellTask.java:25,28-30; SRC ui/ImportEntriesActivity.java:143-174')
e('ImportEntriesActivity.lambda$startImportApp$5@STRATUM', 'ImportEntriesActivity.processImporterState@STRATUM', 'CALL',
  'Direct call', evidence='SRC ImportEntriesActivity.java:157 (bytecode)')
# --- file-pick v2 V1 (PRIVATE BUILD, not pushed): andOTP @FILE_ANDOTP variant chain (E1, E3-E16, E19).
# Template DESIGN.md 4.2/4.4 (audit PASS); E2/E17/E18 deleted by audit D1/D2 (auto expansion).
# V1 combined private state: the old @FILE hand edge (Efee7d0a4) is DELETED and replaced by the
# variant E19 below, in the same private sequence (D3: chain and hand-move never separate).
# AndOtp decrypt incoming is 1 (variant E19 only). Never pushed in an intermediate state
# (R1: single final commit when full section 9 passes).
gui('Dialogs.showImportersDialog@FILE', 'Dialogs.lambda$showImportersDialog$26@FILE_ANDOTP', 'Tap the `andOTP` row in the importer list (its help text is shown)',
  guard='the `andOTP` row is tapped (the dialog lists all importers when isDirect is false, DatabaseImporter.java:99-106; a tap sets the checked row in the single-choice list, FW-SRC AbsListView.java:1136-1150 and/or dialog_importers.xml choiceMode="singleChoice", Dialogs.java:529-531)',
  evidence=FW_ITEM + '; SRC ui/dialogs/Dialogs.java:523-531; SRC importers/DatabaseImporter.java:99-106; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
gui('Dialogs.lambda$showImportersDialog$26@FILE_ANDOTP', 'Dialogs.lambda$showImportersDialog$27@FILE_ANDOTP', 'Tap OK after the `andOTP` row was tapped (gives the chosen importer to the listener)',
  guard='the `andOTP` row was tapped first: in the single-choice list a tap sets the checked row (FW-SRC AbsListView.java:1136-1150, dialog_importers.xml choiceMode="singleChoice"), so OK reads the `andOTP` importer (Dialogs.java:537), not the default Aegis row',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:533-538; FW-SRC core/java/android/widget/AbsListView.java:1136-1150')
e('Dialogs.lambda$showImportersDialog$27@FILE_ANDOTP', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_ANDOTP', 'CALL',
  'the OK button gives the chosen `andOTP` importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107) and the `andOTP` row was tapped',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5@FILE_ANDOTP', 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_ANDOTP', 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the `andOTP` importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-112')
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@FILE_ANDOTP', 'ImportExportPreferencesFragment.lambda$new$0@FILE_ANDOTP', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146-148) and the launcher callback data is not null (ImportExportPreferencesFragment.java:73-79)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146-148; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.lambda$new$0@FILE_ANDOTP', 'ImportExportPreferencesFragment.onImportSelectResult@FILE_ANDOTP', 'CALL',
  'the picker result carries data: onImportSelectResult runs',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportExportPreferencesFragment.onImportSelectResult@FILE_ANDOTP', 'ImportFileTask.doInBackground@FILE_ANDOTP', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  evidence=FW_ASYNC + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportFileTask.doInBackground@FILE_ANDOTP', 'ImportFileTask.onPostExecute@FILE_ANDOTP', 'ASYNC',
  'the result is posted to the main thread (the `andOTP` file-import task)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@FILE_ANDOTP', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_ANDOTP', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='result.getError() is null (ImportExportPreferencesFragment.java:152-155)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-155')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11@FILE_ANDOTP', 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE_ANDOTP', 'CALL',
  'Direct call',
  guard='`_importerDef` is the `andOTP` definition and the task result file (ImportExportPreferencesFragment.java:152-153) is passed to the import page',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:152-153; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportExportPreferencesFragment.startImportEntriesActivity@FILE_ANDOTP', 'ImportEntriesActivity.<init>@FILE_ANDOTP', 'INTENT',
  'the import page opens with the chosen `andOTP` importer and the file (file import)',
  guard='the file argument is non-null (ImportExportPreferencesFragment.java:161-165)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165')
e('ImportEntriesActivity.<init>@FILE_ANDOTP', 'ImportEntriesActivity.onCreate@FILE_ANDOTP', 'LIFECYCLE',
  'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
e('ImportEntriesActivity.onCreate@FILE_ANDOTP', 'ImportEntriesActivity.startImport@FILE_ANDOTP', 'CALL',
  'the import page starts the import from its intent extras',
  guard='abortIfOrphan is false (ImportEntriesActivity.java:64-66) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104')
e('ImportEntriesActivity.startImport@FILE_ANDOTP', 'ImportEntriesActivity.startImportFile@FILE_ANDOTP', 'CALL',
  'Direct call',
  guard='a file was passed (ImportEntriesActivity.java:109,127)',
  evidence='SRC ImportEntriesActivity.java:127 (bytecode); SRC ui/ImportEntriesActivity.java:109,127')
e('ImportEntriesActivity.startImportFile@FILE_ANDOTP', 'ImportEntriesActivity.processImporterState@FILE_ANDOTP', 'CALL',
  'the file just read is processed on the `andOTP` file-import path',
  guard='the import page was opened with a file for the `andOTP` importer',
  evidence='SRC ImportEntriesActivity.java:134 (bytecode); SRC ui/ImportEntriesActivity.java:131-134; SRC importers/DatabaseImporter.java:75-76')
e('ImportEntriesActivity.processImporterState@FILE_ANDOTP', 'AndOtpImporter$EncryptedState.decrypt(Context,DecryptListener)', 'CALL',
  'the picked file import is an encrypted andOTP backup: the importer asks for the format and password and decrypts it',
  guard='the file import picked andOTP (supportsDirect false, DatabaseImporter.java:35; getAppPath throws, AndOtpImporter.java:59-62) and the file is not JSON, so read returns EncryptedState (AndOtpImporter.java:76-80)',
  evidence='SRC ui/ImportEntriesActivity.java:176-182; SRC importers/AndOtpImporter.java:66-80')
sup(('WelcomeSlide.lambda$startImportVault$2', 'AndOtpImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'AuthyImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'AuthenticatorPlusImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'FreeOtpImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'StratumImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'StratumImporter$LegacyEncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener)'),
    ('WelcomeSlide.lambda$startImportVault$2', 'TwoFASImporter$EncryptedState.decrypt(Context,DecryptListener)'))
# Listener-split cleanup: after the Welcome->non-Aegis decrypt suppression, every
# non-Aegis importer decrypt is called only by ImportEntries processImporterState,
# whose listener is ImportEntries $2, never Welcome $1. The auto virtual edges from
# those importers' callbacks to Welcome $1.onStateDecrypted are therefore false and
# are suppressed (they would otherwise let an ImportEntries import reach the intro
# completion path). The corresponding onError/onCanceled virtual edges are left:
# they end in a dialog/cancel report and reach no target, and Aegis's own onError /
# onCanceled edges are genuinely shared between the two prefixes.
sup(('AndOtpImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('AndOtpImporter$EncryptedState.decrypt(Context,char[],boolean,DecryptListener)', 'WelcomeSlide$1.onStateDecrypted'),
    ('FreeOtpImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('StratumImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('StratumImporter$LegacyEncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('TotpAuthenticatorImporter$EncryptedState.decrypt(char[],DecryptListener)', 'WelcomeSlide$1.onStateDecrypted'),
    ('AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('TwoFASImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'),
    ('AuthyImporter$EncryptedState.lambda$decrypt$0', 'WelcomeSlide$1.onStateDecrypted'))
# Aegis dialog+task chains by listener. The hand $0-variant edges below suppress the auto
# virtual $0->listener edges (base-pair rule), so each $0 variant delivers only to its own listener.
# variant password-dialog chain @WELCOME: only the dialog opened by AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@WELCOME reaches AegisImporter$EncryptedState.lambda$decrypt$1@WELCOME.
e('AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@WELCOME', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@WELCOME', 'CALL', 'Direct call',
  evidence='SRC importers/AegisImporter.java:90 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@WELCOME', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@WELCOME', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@WELCOME', 'Dialogs.lambda$showTextInputDialog$8@WELCOME', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@WELCOME', 'Dialogs.lambda$showTextInputDialog$6@WELCOME',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@WELCOME', 'Dialogs.lambda$showTextInputDialog$7@WELCOME', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@WELCOME', 'AegisImporter$EncryptedState.lambda$decrypt$1@WELCOME', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/AegisImporter.java:90-108',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/AegisImporter.java:90-108')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@WELCOME', 'AegisImporter$EncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=('INFERRED androidx.appcompat AlertDialog: a cancel (Back or a tap outside) calls the OnCancelListener set with '
             'setOnCancelListener (AppCompat source not read)') + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/AegisImporter.java:109')
e('AegisImporter$EncryptedState.lambda$decrypt$1@WELCOME', 'PasswordSlotDecryptTask.doInBackground@AEGIS_WELCOME', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (decrypt the password slot of the Aegis backup)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/AegisImporter.java:93,108; SRC ui/tasks/PasswordSlotDecryptTask.java:27')
e('PasswordSlotDecryptTask.onPostExecute@AEGIS_WELCOME', 'AegisImporter$EncryptedState.lambda$decrypt$0@WELCOME', 'CALL',
  'the Aegis slot result goes back to the importer, which builds the vault credentials and decrypts',
  cls='non_standard', via='interface callback: onTaskFinished (PasswordSlotDecryptTask.java:89); the callback is the lambda at AegisImporter.java:93-105',
  evidence='SRC ui/tasks/PasswordSlotDecryptTask.java:87-90; SRC importers/AegisImporter.java:93-105')
e('AegisImporter$EncryptedState.lambda$decrypt$0@WELCOME', 'WelcomeSlide$1.onStateDecrypted', 'CALL',
  'the decrypted Aegis vault state goes to the page that started the import',
  cls='non_standard', via='interface callback: DatabaseImporter.DecryptListener.onStateDecrypted (the listener is passed to decrypt at AegisImporter.java:93-105)',
  evidence='SRC ui/slides/WelcomeSlide.java:69-94; SRC importers/AegisImporter.java:93-105')
# variant password-dialog chain @IMPORT: only the dialog opened by AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@IMPORT reaches AegisImporter$EncryptedState.lambda$decrypt$1@IMPORT.
e('AegisImporter$EncryptedState.decrypt(Context,DecryptListener)@IMPORT', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@IMPORT', 'CALL', 'Direct call',
  evidence='SRC importers/AegisImporter.java:90 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@IMPORT', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@IMPORT', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@IMPORT', 'Dialogs.lambda$showTextInputDialog$8@IMPORT', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@IMPORT', 'Dialogs.lambda$showTextInputDialog$6@IMPORT',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@IMPORT', 'Dialogs.lambda$showTextInputDialog$7@IMPORT', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@IMPORT', 'AegisImporter$EncryptedState.lambda$decrypt$1@IMPORT', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/AegisImporter.java:90-108',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/AegisImporter.java:90-108')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@IMPORT', 'AegisImporter$EncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=('INFERRED androidx.appcompat AlertDialog: a cancel (Back or a tap outside) calls the OnCancelListener set with '
             'setOnCancelListener (AppCompat source not read)') + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/AegisImporter.java:109')
e('AegisImporter$EncryptedState.lambda$decrypt$1@IMPORT', 'PasswordSlotDecryptTask.doInBackground@AEGIS_IMPORT', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (decrypt the password slot of the Aegis backup)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/AegisImporter.java:93,108; SRC ui/tasks/PasswordSlotDecryptTask.java:27')
e('PasswordSlotDecryptTask.onPostExecute@AEGIS_IMPORT', 'AegisImporter$EncryptedState.lambda$decrypt$0@IMPORT', 'CALL',
  'the Aegis slot result goes back to the importer, which builds the vault credentials and decrypts',
  cls='non_standard', via='interface callback: onTaskFinished (PasswordSlotDecryptTask.java:89); the callback is the lambda at AegisImporter.java:93-105',
  evidence='SRC ui/tasks/PasswordSlotDecryptTask.java:87-90; SRC importers/AegisImporter.java:93-105')
e('AegisImporter$EncryptedState.lambda$decrypt$0@IMPORT', 'ImportEntriesActivity$2.onStateDecrypted', 'CALL',
  'the decrypted Aegis vault state goes to the page that started the import',
  cls='non_standard', via='interface callback: DatabaseImporter.DecryptListener.onStateDecrypted (the listener is passed to decrypt at AegisImporter.java:93-105)',
  evidence='SRC ui/ImportEntriesActivity.java:179-182; SRC importers/AegisImporter.java:93-105')
e('EditEntryActivity.lambda$new$0', 'EditEntryActivity$CustomSvgIcon.<init>', 'CALL',
  'the picked SVG is read: the custom icon is built from the file',
  cls='explicit', guard='no read error (EditEntryActivity.java:151); the error branch at 154-156 shows a dialog instead',
  evidence='SRC ui/EditEntryActivity.java:151-152')
e('MainActivity.lambda$new$6', 'MainActivity.onAddEntryResult', 'CALL',
  'the add-entry result is handled: the new entry is added to the list',
  cls='explicit', guard='result RESULT_OK with data (MainActivity.java:179-180)',
  evidence='SRC ui/MainActivity.java:179-182')
e('EntryAdapter.updatePeriodUniformity', 'EntryHolder.setShowProgress', 'CALL',
  'a TOTP row shows its progress bar when its period differs from the most frequent period',
  cls='explicit', guard='period uniformity changed since the last update (the early return at EntryAdapter.java:578-580 is not taken); the holder is a TOTP entry (line 586) and its period differs from the most frequent period (line 587); at least one row is bound, so _holders is not empty (EntryAdapter.java:569,88-99)',
  needs_state=ST_HOLDERS_BOUND,
  evidence='SRC ui/views/EntryAdapter.java:578-587')
# Fix-design 03 (C3 route 03): updatePeriodUniformity loops over _holders (EntryAdapter.java:585-588),
# which is empty until RecyclerView binds rows (onBindViewHolder adds at :569; the constructor sets an
# empty list, :88-99). The old edge let a filter change on an unloaded adapter reach setShowProgress,
# which never happens over an empty list. The edge now carries the bound-holders state, and the bind
# producer (setData -> setShowProgress, nonUniform from onBindViewHolder :446) gets its guard in full,
# so the target's best route runs through loaded entries and bound rows.
e('EntryHolder.setData', 'EntryHolder.setShowProgress', 'CALL',
  'a bound row shows its progress bar when its period is not uniform',
  cls='explicit', guard='nonUniform is true: the bound entry is a TOTP-family entry whose period differs from the most frequent period (EntryAdapter.java:446); with a single TOTP-family entry that period is its own (:605-608), so at least two TOTP-family entries with different periods are needed',
  evidence='SRC ui/views/EntryAdapter.java:446,605-608; SRC ui/views/EntryHolder.java:128,150')

# stage 2 G2 (route checker): hand edges that replace the auto rows on the same pairs, each with its guard
e('MainActivity.lambda$new$2', 'MainActivity.onScanResult', 'CALL', 'the scan result reaches the main screen: the launcher passes the intent on',
  guard='the result is RESULT_OK with data (MainActivity.java:152-154)', evidence='SRC ui/MainActivity.java:150-156')
e('IconPacksManagerFragment.onViewCreated', 'IconPackAdapter.addIconPack', 'CALL', 'each icon pack already installed is added to the list',
  guard='at least one icon pack is installed (IconPacksManagerFragment.java:103-105)', needs_state=ST_ICON_PACK_INSTALLED,
  evidence='SRC ui/fragments/preferences/IconPacksManagerFragment.java:103-105')
e('IconPackManager.removeIconPack', 'IconPackException.<init>(Throwable)', 'CALL', 'the pack folder cannot be deleted: the removal fails with an IconPackException',
  guard='deleting the pack folder fails: the IOException from deleteDir (IconPackManager.java:56-58; deleteDir throws when File.delete returns false, IconPackManager.java:219-220)',
  evidence='SRC icons/IconPackManager.java:53-59; SRC icons/IconPackManager.java:209-221')

# batch 4: the framework calls onDestroy after onCreate (when the activity finishes or is destroyed)
e('AegisActivity.onCreate', 'AegisActivity.onDestroy', 'LIFECYCLE', 'Activity.onDestroy: the framework calls it later, when the activity finishes or is destroyed',
  evidence='INFERRED Activity lifecycle: onDestroy follows onCreate (framework source not read); SRC ui/AegisActivity.java:84')
# batch 4: reflection (cls non_standard). PanicResponderActivity adds the two GuardianProject signers only when the panic trigger is on
# (ST_PANIC_ON check at PanicResponderActivity.java:22-25) and the build is not the test build (BuildConfig.TEST, line 29)
e('TrustedIntents.addTrustedSigner', 'GuardianProjectRSA4096.<init>', 'CALL',
  'Constructor.newInstance builds the GuardianProject RSA4096 signer pin, which then calls ApkSignaturePin.<init>',
  cls='non_standard', via='reflection: cls.getConstructor() then constructor.newInstance((Object[]) null) (TrustedIntents.java:168-171)',
  env=ENV_PANIC, needs_state=ST_PANIC_ON,
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:168-171; SRC ui/PanicResponderActivity.java:22-32')
e('TrustedIntents.addTrustedSigner', 'GuardianProjectFDroidRSA2048.<init>', 'CALL',
  'Constructor.newInstance builds the GuardianProject F-Droid RSA2048 signer pin, which then calls ApkSignaturePin.<init>',
  cls='non_standard', via='reflection: cls.getConstructor() then constructor.newInstance((Object[]) null) (TrustedIntents.java:168-171)',
  env=ENV_PANIC, needs_state=ST_PANIC_ON,
  evidence='SRC info/guardianproject/trustedintents/TrustedIntents.java:168-171; SRC ui/PanicResponderActivity.java:22-32')

# entry list fragment: the layout holds it (MainActivity.java:219 finds it by id), so the FragmentManager creates it and calls its lifecycle
e('MainActivity.onCreate', 'EntryListView.<init>', 'FRAMEWORK', 'the layout holds the entry list fragment (key_profiles): the FragmentManager creates it',
  cls='non_standard', via='reflection: the androidx FragmentManager creates the fragment class named in the layout (android:name, res/layout/activity_main.xml:54-56)',
  evidence='INFERRED androidx.fragment: the fragment in the layout is created by the FragmentManager (source not read); SRC ui/MainActivity.java:195; SRC res/layout/activity_main.xml:54-56')
e('EntryListView.<init>', 'EntryListView.onCreate', 'LIFECYCLE', 'Fragment.onCreate after the constructor',
  evidence='INFERRED androidx.fragment: the FragmentManager calls onCreate (source not read); SRC ui/views/EntryListView.java:84')
e('EntryListView.onCreate', 'EntryListView.onCreateView', 'LIFECYCLE', 'Fragment.onCreateView inflates the list and sets the adapter',
  evidence='INFERRED androidx.fragment: the FragmentManager calls onCreateView (source not read); SRC ui/views/EntryListView.java:97-144')

# RecyclerView draws the rows when the entry list is set (framework calls the adapter; the framework source is not read)
e('EntryListView.setEntries', 'EntryAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView creates the row views for the list',
  evidence='INFERRED androidx.recyclerview: RecyclerView creates rows after the adapter data changes (source not read); SRC ui/views/EntryAdapter.java:407')
e('EntryListView.setEntries', 'EntryAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView binds each visible row to its entry',
  guard='the list holds at least one row', needs_state=ST_VAULT_ENTRIES,
  evidence='INFERRED androidx.recyclerview: RecyclerView binds visible rows after the data changes (source not read); SRC ui/views/EntryAdapter.java:437')
e('EntryListView.setEntries', 'EntryAdapter.getItemCount', 'FRAMEWORK', 'RecyclerView asks the adapter how many rows to lay out',
  evidence='INFERRED androidx.recyclerview: RecyclerView calls getItemCount (source not read); SRC ui/views/EntryAdapter.java:764-765')

# the row listeners are set in onBindViewHolder: a tap on a row starts them (needs the list loaded, so the rows are bound)
gui('S_LIST', 'EntryAdapter$1.onClick', 'Tap an entry in the list (the row click listener)', needs_state=ST_LIST_LOADED,
    evidence=FW_CLICK + '; SRC ui/views/EntryAdapter.java:464-519')
gui('S_LIST', 'EntryAdapter$2.onLongClick', 'Long press an entry in the list (the row long-click listener)', needs_state=ST_LIST_LOADED,
    evidence='INFERRED View.OnLongClickListener: performLongClick calls onLongClick (framework source not read); SRC ui/views/EntryAdapter.java:520-536')
gui('S_LIST', 'EntryAdapter$3.onTouch', 'Touch an entry in the list (the row touch listener)', needs_state=ST_LIST_LOADED,
    evidence='INFERRED View.OnTouchListener: dispatchTouchEvent calls onTouch (framework source not read); SRC ui/views/EntryAdapter.java:537-548')
gui('S_LIST', 'EntryAdapter$4.onClick', 'Tap the refresh button on an entry row (the code is refreshed)', needs_state=ST_LIST_LOADED,
    evidence=FW_CLICK + '; SRC ui/views/EntryAdapter.java:549-567')
e('EntryAdapter$1.onClick', 'EntryAdapter$1.lambda$onClick$0', 'FRAMEWORK', 'View.postDelayed clears the double-tap state after the delay',
  evidence=FW_POST + '; SRC ui/views/EntryAdapter.java:490')

# --- batch 5 (Room): AegisModule.provideAppDatabase builds the database with Room.databaseBuilder (AegisModule.java:50-52)
e('AegisModule.provideAppDatabase', 'AppDatabase_Impl.<init>', 'CALL',
  'Room.databaseBuilder(...).build() loads the generated AppDatabase_Impl class by name and calls its constructor',
  cls='non_standard', via='reflection: Room library loads the generated class (AppDatabase_Impl) by name and calls its constructor (Room library source not read)',
  evidence='INFERRED Room library (generated AppDatabase_Impl is in the dataset, not the source tree); SRC AegisModule.java:50-52; SRC database/AppDatabase.java:12-13')
for _dst, _note in [
    ('AppDatabase_Impl.createOpenDelegate', 'Room builds the open-helper delegate while the database is built'),
    ('AppDatabase_Impl.createInvalidationTracker', 'Room builds the invalidation tracker while the database is built'),
    ('AppDatabase_Impl.getRequiredTypeConverters', 'Room asks the generated database for its type converters while it is built'),
    ('AppDatabase_Impl.getAutoMigrations', 'Room asks the generated database for its auto-migrations while it is built'),
    ('AppDatabase_Impl.getRequiredAutoMigrationSpecs', 'Room asks the generated database for its auto-migration specs while it is built'),
]:
    e('AegisModule.provideAppDatabase', _dst, 'FRAMEWORK', _note,
      evidence='INFERRED Room library (library source not read); generated AppDatabase_Impl (dataset, not source tree); SRC AegisModule.java:50-52')
for _dst in ['createAllTables', 'dropAllTables', 'onCreate', 'onOpen', 'onPreMigrate', 'onPostMigrate', 'onValidateSchema']:
    e('AppDatabase_Impl.createOpenDelegate', 'AppDatabase_Impl$1.' + _dst, 'FRAMEWORK',
      'Room opens the database file on the first DAO call and calls this open-helper delegate callback (create, open, migrate or validate)',
      evidence='INFERRED Room library: RoomOpenHelper calls the delegate on open (library source not read); generated AppDatabase_Impl$1 (dataset, not source tree)')

# --- batch 5 (Glide). Glide.with(...) is library code. Each site below is an app method that calls Glide.with (SRC refs given).
# Generated Glide classes are in the dataset, not the source tree, so their edges are INFERRED.
_GLIDE_SITES = [
    ('GlideHelper.loadIconFile', 'ui/glide/GlideHelper.java:31-32'),
    ('GlideHelper.loadIcon', 'ui/glide/GlideHelper.java:35-36'),
    ('GlideHelper.loadEntryIcon', 'ui/glide/GlideHelper.java:39-41'),
    ('EntryHolder.loadIcon', 'ui/views/EntryHolder.java:225'),
    ('AssignIconHolder.setData', 'ui/views/AssignIconHolder.java:42'),
    ('AssignIconHolder.setNewIcon', 'ui/views/AssignIconHolder.java:48-50'),
    ('IconHolder.loadIcon', 'ui/views/IconHolder.java:42-47'),
    ('EditEntryActivity.onCreate', 'ui/EditEntryActivity.java:253'),
    ('EditEntryActivity.selectIcon', 'ui/EditEntryActivity.java:613'),
    ('EditEntryActivity.startEditingIcon', 'ui/EditEntryActivity.java:617-618'),
    ('AssignIconsActivity$EntryIconPreloadProvider.getPreloadRequestBuilder', 'ui/AssignIconsActivity.java:236'),
    ('AssignIconsActivity$IconPreloadProvider.getPreloadRequestBuilder', 'ui/AssignIconsActivity.java:256'),
    ('IconPickerDialog$1IconPreloadProvider.getPreloadRequestBuilder', 'ui/dialogs/IconPickerDialog.java:78'),
    ('EntryListView.onCreateView', 'ui/views/EntryListView.java:124'),
    ('EntryListView$IconPreloadProvider.getPreloadRequestBuilder', 'ui/views/EntryListView.java:712'),
]
for _site, _ref in _GLIDE_SITES:
    e(_site, 'GeneratedRequestManagerFactory.build', 'FRAMEWORK',
      'Glide.with: the library asks the generated request-manager factory for a request manager (GlideRequests)',
      cls='non_standard', via='library lookup: Glide finds the generated request-manager factory through the generated module (Glide library source not on disk)',
      evidence='INFERRED Glide library (source not read); generated GeneratedRequestManagerFactory is on disk in the build classes (dirs/com/bumptech/glide/GeneratedRequestManagerFactory.class, build method; not in the source tree); SRC ' + _ref)
    e(_site, 'GeneratedAppGlideModuleImpl.<init>', 'CALL',
      'the first Glide.with starts Glide, which loads the generated module by name and calls its constructor',
      cls='non_standard', via='reflection: Glide library loads GeneratedAppGlideModuleImpl by name and calls its constructor (Glide library source not read)',
      evidence='INFERRED Glide library (source not read); generated GeneratedAppGlideModuleImpl (dataset, not source tree); SRC ' + _ref)
for _m in ['applyOptions', 'getExcludedModuleClasses', 'getRequestManagerFactory', 'isManifestParsingEnabled', 'registerComponents']:
    e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.' + _m, 'FRAMEWORK',
      'Glide calls this module method while it starts (library calls on the module object)',
      evidence='INFERRED Glide library (source not read); generated GeneratedAppGlideModuleImpl (dataset, not source tree)')
e('GlideRequests.<init>', 'GlideRequests.setRequestOptions', 'FRAMEWORK',
  'the RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides (it wraps the options in GlideOptions)',
  cls='non_standard', via='library virtual dispatch: the Glide RequestManager constructor calls setRequestOptions, which the generated GlideRequests overrides (Glide library source not on disk)',
  evidence='INFERRED Glide library RequestManager constructor (source not read); generated GlideRequests (dataset, not source tree)')
# the app's rm.load(...) calls reach the generated load overloads (the RequestManager object is a GlideRequests)
e('GlideHelper.loadIconFile', 'GlideRequests.load(File)', 'FRAMEWORK',
  'rm.load(file): the request manager is a GlideRequests, so its generated load(File) override runs',
  evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/glide/GlideHelper.java:32')
e('GlideHelper.loadEntryIcon', 'GlideRequests.load(Object)', 'FRAMEWORK',
  'rm.load(entry.getIcon()): the VaultEntryIcon argument matches load(Object); the generated override runs',
  evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/glide/GlideHelper.java:41; SRC vault/VaultEntry.java:133')
e('GlideRequests.load(File)', 'GlideRequests.asDrawable', 'CALL', 'generated load(File) starts with asDrawable()',
  evidence='INFERRED generated GlideRequests (dataset, not source tree)')
e('GlideRequests.load(Object)', 'GlideRequests.asDrawable', 'CALL', 'generated load(Object) starts with asDrawable()',
  evidence='INFERRED generated GlideRequests (dataset, not source tree)')
e('GlideRequests.load(File)', 'GlideRequest.load(File)', 'CALL', 'generated load(File) returns asDrawable().load(file): the GlideRequest overload runs',
  evidence='INFERRED generated GlideRequests (dataset, not source tree)')
e('GlideRequests.load(Object)', 'GlideRequest.load(Object)', 'CALL', 'generated load(Object) returns asDrawable().load(model): the GlideRequest overload runs',
  evidence='INFERRED generated GlideRequests (dataset, not source tree)')
e('GlideRequests.asDrawable', 'GlideRequests.as', 'FRAMEWORK', 'RequestManager.asDrawable (library) calls as(Class), which the generated GlideRequests overrides',
  evidence='INFERRED Glide library RequestManager.asDrawable (source not read); generated GlideRequests (dataset, not source tree)')
e('GlideRequests.asBitmap', 'GlideRequests.as', 'FRAMEWORK', 'RequestManager.asBitmap (library) calls as(Class), which the generated GlideRequests overrides',
  evidence='INFERRED Glide library RequestManager.asBitmap (source not read); generated GlideRequests (dataset, not source tree)')
e('GlideRequests.as', 'GlideRequest.<init>(Glide,RequestManager,Class,Context)', 'CALL', 'generated as(Class) creates the GlideRequest for the requested type',
  evidence='INFERRED generated GlideRequests (dataset, not source tree)')
# the app's Glide.with(...).asBitmap().load(data) chain (EditEntryActivity.java:617-618) and the RequestBuilder calls on GlideHelper.java:55-62
e('EditEntryActivity.startEditingIcon', 'GlideRequests.asBitmap', 'FRAMEWORK', 'Glide.with(this).asBitmap(): the request manager is a GlideRequests, so its generated asBitmap override runs',
  evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/EditEntryActivity.java:617-618')
e('EditEntryActivity.startEditingIcon', 'GlideRequest.load(Uri)', 'FRAMEWORK', 'the RequestBuilder from asBitmap() is a GlideRequest, so .load(data) runs its generated override',
  evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/EditEntryActivity.java:619')
for _site in ['EditEntryActivity.startEditingIcon']:
    for _dst in ['GlideRequest.diskCacheStrategy', 'GlideRequest.skipMemoryCache']:
        e(_site, _dst, 'FRAMEWORK', 'the RequestBuilder chain sets the cache options; the object is a GlideRequest, so its generated override runs',
          evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/EditEntryActivity.java:620-621')
for _dst in ['GlideRequest.set', 'GlideRequest.listener', 'GlideRequest.diskCacheStrategy', 'GlideRequest.skipMemoryCache']:
    e('GlideHelper.setCommonOptions', _dst, 'FRAMEWORK', 'rb.set / listener / diskCacheStrategy / skipMemoryCache on a RequestBuilder that is a GlideRequest: its generated override runs',
      evidence='INFERRED virtual dispatch to the generated override (dataset, not source tree); SRC ui/glide/GlideHelper.java:59-67')

# --- Room chain (batch 6): the generated getter reaches the provider's get() through javax.inject.Provider.
# round 7 (run 9): SwitchingProvider.get is one method for four bindings and its case is chosen by the binding id. Each
# binding gets its own variant with one hand edge, and the plain method's automatic case edges are removed, so a route
# cannot reach one binding's case through another binding's caller (G5 R3 went getVaultManager -> IconPackManager).
_SP = 'DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl$SwitchingProvider.get'
sup((_SP, 'AegisModule.provideVaultManager'), (_SP, 'AegisModule.provideIconPackManager'),
    (_SP, 'AegisModule.provideAppDatabase'), (_SP, 'AegisModule.provideAuditLogRepository'))
_SP_EVID = ('INFERRED generated switch rows of SwitchingProvider.get (DaggerAegisApplication_HiltComponents_SingletonC.java: '
            ':627 provideVaultManager, :630 provideAuditLogRepository, :633 provideAppDatabase, :636 provideIconPackManager)')
e('DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.getVaultManager', _SP + '@VAULT', 'FRAMEWORK',
  'the generated getter asks the switching provider for the VaultManager binding',
  evidence='INFERRED Dagger generated code calls javax.inject.Provider.get (generated file, not in the source tree); auto_calls.json framework_calls row for getVaultManager')
e(_SP + '@VAULT', 'AegisModule.provideVaultManager', 'CALL', 'the VaultManager case builds it through the module provide method',
  cls='explicit', evidence=_SP_EVID + '; SRC AegisModule.java:39-40')
e(_SP + '@VAULT', _SP + '@AUDIT', 'CALL', 'the VaultManager case takes an AuditLogRepository argument, which its provider supplies',
  cls='explicit', evidence='SRC AegisModule.java:39-40 (provideVaultManager takes an AuditLogRepository); INFERRED argument fetch in the generated case (not in the source tree)')
e(_SP + '@AUDIT', 'AegisModule.provideAuditLogRepository', 'CALL', 'the AuditLogRepository case builds it through the module provide method',
  cls='explicit', evidence=_SP_EVID + '; SRC AegisModule.java:32-35')
e(_SP + '@AUDIT', _SP + '@DB', 'CALL', 'the AuditLogRepository case takes an AppDatabase argument, which its provider supplies',
  cls='explicit', evidence='SRC AegisModule.java:32 (provideAuditLogRepository takes an AppDatabase); INFERRED argument fetch in the generated case (not in the source tree)')
e(_SP + '@DB', 'AegisModule.provideAppDatabase', 'CALL', 'the AppDatabase case builds the Room database through the module provide method',
  cls='explicit', evidence=_SP_EVID + '; SRC AegisModule.java:50-54')
e('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.injectAegisActivity2', _SP + '@ICON', 'CALL',
  'the activity injection fills the @Inject IconPackManager field from its provider',
  guard='the activity is being injected (Hilt_AegisActivity.inject, generated): AegisActivity._iconPackManager is an @Inject field',
  cls='non_standard', via='interface call: Provider.get on the generic SwitchingProvider field (auto_calls.json row injectAegisActivity2 -> Provider.get, target unresolved)',
  evidence='INFERRED generated code (not in the source tree); SRC ui/AegisActivity.java:55-56')
e(_SP + '@ICON', 'AegisModule.provideIconPackManager', 'CALL', 'the IconPackManager case builds it through the module provide method',
  cls='explicit', evidence=_SP_EVID + '; SRC AegisModule.java:26-27')

# --- batch 6 (EditEntryActivity): the entry points into its lambdas and callbacks. REGISTER is documentation only (not traversed);
# the traversed edges are RESULT, GUI (FRAMEWORK) or CALL edges. Lambdas get hand edges; their callees come from the auto CALL rows.
e('EditEntryActivity.<init>', 'EditEntryActivity.lambda$new$1', 'REGISTER',
  'pickImageResultLauncher: the launcher callback is registered in the field initializer',
  evidence='SRC ui/EditEntryActivity.java:141-162')
e('EditEntryActivity.startImageSelectionActivity', _FIL_EDIT_PICK, 'CALL',
  'the image chooser of another app is started through the launcher of the icon picker',
  evidence='SRC ui/EditEntryActivity.java:568-577')
e(_FIL_EDIT_PICK, 'EditEntryActivity.lambda$new$1', 'RESULT',
  'the picker of another app returns the chosen image or file to the launcher callback (the icon picker custom option opened it)',
  env=ENV_PICK_ICON, guard='RESULT_OK with data (EditEntryActivity.java:144-146)',
  evidence='SRC vault/VaultManager.java:243-252; SRC ui/EditEntryActivity.java:568-577,141-162; ' + FW_RESULT)
# the SVG pick has its own variant chain (doInBackground and onPostExecute), so only the icon picker reaches the icon callback
e('EditEntryActivity.lambda$new$1', 'ImportFileTask.doInBackground@SVG_PICK', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked SVG file)',
  guard='the picked file is an SVG (EditEntryActivity.java:148)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/EditEntryActivity.java:148-158; SRC ui/tasks/ImportFileTask.java:18')
e('ImportExportPreferencesFragment.onImportSelectResult', 'ImportFileTask.doInBackground@SETTINGS_IMPORT', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked file)',
  guard='the picker returned RESULT_OK with a URI (ImportExportPreferencesFragment.java:146)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:146,151-158; SRC ui/tasks/ImportFileTask.java:18')
e('WelcomeSlide.startImportVault', 'ImportFileTask.doInBackground@WELCOME', 'ASYNC',
  'AsyncTask runs doInBackground on the worker thread (read the picked vault file)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/slides/WelcomeSlide.java:59,95; SRC ui/tasks/ImportFileTask.java:27')
e('ImportFileTask.doInBackground@SETTINGS_IMPORT', 'ImportFileTask.onPostExecute@SETTINGS_IMPORT', 'ASYNC', 'the result is posted to the main thread (the Settings import task)',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.doInBackground@WELCOME', 'ImportFileTask.onPostExecute@WELCOME', 'ASYNC', 'the result is posted to the main thread (the Welcome import task)',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.doInBackground@SVG_PICK', 'ImportFileTask.onPostExecute@SVG_PICK', 'ASYNC', 'the result is posted to the main thread (the icon picker task)',
  guard='the task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ImportFileTask.java:53-56')
e('ImportFileTask.onPostExecute@SVG_PICK', 'EditEntryActivity.lambda$new$0', 'CALL',
  '_cb.onTaskFinished(result): the SVG import result goes to the lambda (selectIcon, or an error dialog)',
  guard='none on this edge (ImportFileTask.java:55 calls the callback unconditionally); the SVG check is EditEntryActivity.java:148, the guard of the task edge above', needs_state=ST_SVG_PICK,
  evidence='SRC ui/tasks/ImportFileTask.java:53-59; SRC ui/EditEntryActivity.java:150-157')

# onCreate: the click, focus and item-click listeners (EditEntryActivity.java:249-380)
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$2', 'Tap the advanced settings header (the advanced fields open)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:249')
e('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$3', 'FRAMEWORK',
  'the group UUIDs are mapped while the page is set up (Stream.map calls the mapper)',
  evidence='INFERRED java.util.stream (library source not read) calls the mapper; SRC ui/EditEntryActivity.java:293-300')
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$4', 'Pick an OTP type in the dropdown (the advanced fields are updated)',
    evidence='INFERRED AdapterView calls OnItemClickListener on a pick (android.widget source not read); SRC ui/EditEntryActivity.java:323-326')
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$5', 'Tap the icon (the icon picker opens)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:364-368')
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$6', 'Tap the group field (the group dialog opens)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:369')
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$7', 'Focus the group field (the group dialog opens)',
    evidence='INFERRED View.OnFocusChangeListener is called on a focus change (android.view source not read); SRC ui/EditEntryActivity.java:370-375')
gui('EditEntryActivity.onCreate', 'EditEntryActivity.lambda$onCreate$8', 'Tap the group layout (the group dialog opens)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:376-380')

# onCreate attaches the two text watchers (EditEntryActivity.java:307-320); each forwards to its lambda (SimpleTextWatcher.java:24-26)
gui('EditEntryActivity.onCreate', 'SimpleTextWatcher.afterTextChanged', 'Type or change a text field of the entry (the watchers run)',
    evidence='INFERRED TextView calls the TextWatcher on each change (android.widget source not read); SRC ui/EditEntryActivity.java:307-320; SRC helpers/SimpleTextWatcher.java:24-26')
e('SimpleTextWatcher.afterTextChanged', 'EditEntryActivity.lambda$new$25', 'CALL',
  'the listener runs the validation watcher: the back-press handler state is updated',
  evidence='SRC helpers/SimpleTextWatcher.java:24-26; SRC ui/EditEntryActivity.java:311-320,955-957')
e('SimpleTextWatcher.afterTextChanged', 'EditEntryActivity.lambda$new$26', 'CALL',
  'the listener runs the name watcher: the icon placeholder is regenerated from the name and issuer',
  evidence='SRC helpers/SimpleTextWatcher.java:24-26; SRC ui/EditEntryActivity.java:307-308,959-962')

# onCreate adds two back-press callbacks (EditEntryActivity.java:182-185); the dispatcher calls the enabled one
gui('EditEntryActivity.onCreate', 'EditEntryActivity$BackPressHandler.handleOnBackPressed',
    'Press Back on the edit page (asks to discard unsaved changes, or closes the page)', needs_state=ST_ENTRY_CHANGED,
    guard='the handler is enabled only while the entry has unsaved changes (EditEntryActivity.java:966-975); otherwise Back closes the page',
    evidence='INFERRED OnBackPressedDispatcher calls the enabled callback (androidx source not read); SRC ui/EditEntryActivity.java:182-183,978-988')
gui('EditEntryActivity.onCreate', 'EditEntryActivity$IconBackPressHandler.handleOnBackPressed',
    'Press Back while the icon editor is open (stops editing the icon)',
    evidence='INFERRED OnBackPressedDispatcher calls the enabled callback (androidx source not read); SRC ui/EditEntryActivity.java:184-185,989-1000')

# the toolbar menu (EditEntryActivity.java:656-660 and 535-552)
e('EditEntryActivity.onCreate', 'EditEntryActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate',
  evidence=FW_OPTIONS + '; SRC ui/EditEntryActivity.java:656-660')
gui('EditEntryActivity.onCreateOptionsMenu', 'EditEntryActivity.onOptionsItemSelected',
    'Tap a toolbar item: save, delete, discard, or reset the usage count (a menu tap)',
    evidence=FW_MENU + '; SRC ui/EditEntryActivity.java:535-552')
# Fix-design 02b (C3 route 02, step 20): the delete tap was reachable from a new-entry page, on which
# the delete item is hidden (EditEntryActivity.java:658-659). The edit page gets an @EDIT variant chain
# reached only from the entryUUID-carrying launch (MainActivity.java:516-520, entryUUID extra; onCreate
# sets _isNew only when entryUUID is null, :190-196), following the MainActivity.doShortcutActions@SCAN
# precedent. The plain tap edge is removed, so the delete dialog is reachable only on an existing-entry
# page; the plain menu chain (save, discard, reset) is unchanged.
e('MainActivity.startEditEntryActivity(VaultEntry)', 'EditEntryActivity.<init>@EDIT', 'INTENT', 'the edit page opens for the selected entry (entryUUID)',
  evidence='SRC ui/MainActivity.java:516-520')
e('EditEntryActivity.<init>@EDIT', 'EditEntryActivity.onCreate@EDIT', 'LIFECYCLE', 'Activity.onCreate of the edit page for an existing entry',
  evidence=FW_CREATE + '; SRC ui/EditEntryActivity.java:165')
e('EditEntryActivity.onCreate@EDIT', 'EditEntryActivity.onCreateOptionsMenu@EDIT', 'FRAMEWORK', 'the toolbar menu is created after onCreate (existing entry: the delete item stays visible)',
  evidence=FW_OPTIONS + '; SRC ui/EditEntryActivity.java:656-660')
gui('EditEntryActivity.onCreateOptionsMenu@EDIT', 'EditEntryActivity.onOptionsItemSelected@EDIT',
    'Tap a toolbar item on an existing-entry page: save, delete, discard, or reset the usage count (a menu tap)',
    evidence=FW_MENU + '; SRC ui/EditEntryActivity.java:535-552')
gui('EditEntryActivity.onOptionsItemSelected@EDIT', 'EditEntryActivity.lambda$onOptionsItemSelected$18',
    'Tap Yes in the delete dialog (the entry is deleted)',
    guard='the page edits an existing entry: the delete item is hidden for a new entry (EditEntryActivity.java:658-659, onCreateOptionsMenu); only the @EDIT chain reaches this tap',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:542-545; SRC ui/dialogs/Dialogs.java (showDeleteEntriesDialog)')
gui('EditEntryActivity.onOptionsItemSelected', 'EditEntryActivity.lambda$onOptionsItemSelected$19',
    'Tap Yes in the reset usage count dialog (the usage count is reset)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:546-552')

# the discard dialog (EditEntryActivity.java:505-531): the dialog opens only with unsaved changes (EditEntryActivity.java:514-520)
gui('EditEntryActivity.discardAndFinish', 'EditEntryActivity.lambda$discardAndFinish$16',
    'Tap Save in the discard dialog (the entry is saved, or the parse error is shown)',
    guard='the entry has unsaved changes (EditEntryActivity.java:514-520); the dialog appears only then',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:514-531; SRC ui/dialogs/Dialogs.java (showDiscardDialog)')
gui('EditEntryActivity.discardAndFinish', 'EditEntryActivity.lambda$discardAndFinish$17',
    'Tap Discard in the discard dialog (the page closes without saving)',
    guard='the entry has unsaved changes (EditEntryActivity.java:514-520); the dialog appears only then',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:514-531; SRC ui/dialogs/Dialogs.java (showDiscardDialog)')

# the advanced settings fade-out (EditEntryActivity.java:485-500): the library calls the adapter, the adapter calls the lambda
gui('EditEntryActivity.openAdvancedSettings', 'SimpleAnimationEndListener.onAnimationEnd',
    'the fade-out animation of the advanced settings link ends (the listener is called)',
    evidence='INFERRED android.view.animation calls AnimationListener.onAnimationEnd (library source not read); SRC ui/EditEntryActivity.java:485-500')
e('SimpleAnimationEndListener.onAnimationEnd', 'EditEntryActivity.lambda$openAdvancedSettings$15', 'CALL',
  '_listener.onAnimationEnd(animation): the lambda shows the advanced fields',
  evidence='SRC helpers/SimpleAnimationEndListener.java:18-21; SRC ui/EditEntryActivity.java:491-496')

# the icon editor (EditEntryActivity.java:616-641): the image loads through Glide into a CustomTarget
e('EditEntryActivity.startEditingIcon', 'EditEntryActivity$2.onResourceReady', 'FRAMEWORK',
  'Glide loads the picked image and calls the CustomTarget with it (the icon editor shows it)',
  evidence='INFERRED Glide library calls CustomTarget.onResourceReady after the load (Glide source not read); SRC ui/EditEntryActivity.java:621-630')
e('EditEntryActivity.startEditingIcon', 'EditEntryActivity$2.onLoadCleared', 'FRAMEWORK',
  'Glide clears the target when the load is replaced or cancelled',
  evidence='INFERRED Glide library calls CustomTarget.onLoadCleared (Glide source not read); SRC ui/EditEntryActivity.java:621-640')
gui('EditEntryActivity.startEditingIcon', 'EditEntryActivity.lambda$startEditingIcon$20',
    'Tap the save button of the icon editor (the icon is kept and the editor stops)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:636-641')

# the group dialog (EditEntryActivity.java:384-438): taps on the group field and the dialog buttons
gui('EditEntryActivity.showGroupSelectionDialog', 'EditEntryActivity.lambda$showGroupSelectionDialog$10',
    'Tap Add in the group dialog (asks for a new group name)', evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:403-419')
gui('EditEntryActivity.lambda$showGroupSelectionDialog$10', 'EditEntryActivity.lambda$showGroupSelectionDialog$9',
    'Tap OK in the new-group text dialog (the group is added and checked)',
    evidence='SRC ui/EditEntryActivity.java:403-419; SRC ui/dialogs/Dialogs.java (showTextInputDialog)')
gui('EditEntryActivity.showGroupSelectionDialog', 'EditEntryActivity.lambda$showGroupSelectionDialog$11',
    'Tap Save in the group dialog (the checked groups are applied to the entry)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:421-432')
gui('EditEntryActivity.showGroupSelectionDialog', 'EditEntryActivity.lambda$showGroupSelectionDialog$12',
    'Tap Clear in the group dialog (all groups are unchecked)', evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:433-437')
e('EditEntryActivity.getCheckedUUID', 'EditEntryActivity.lambda$getCheckedUUID$13', 'FRAMEWORK',
  'Stream.map calls the mapper for each checked chip', evidence='INFERRED java.util.stream (library) calls the mapper; SRC ui/EditEntryActivity.java:451-458')
e('EditEntryActivity.getCheckedNames', 'EditEntryActivity.lambda$getCheckedNames$14', 'FRAMEWORK',
  'Stream.map calls the mapper for each checked chip', evidence='INFERRED java.util.stream (library) calls the mapper; SRC ui/EditEntryActivity.java:461-468')

# the duplicate sheet (EditEntryActivity.java:871-941): shown only when onSave finds a duplicate (EditEntryActivity.java:860-861)
gui('EditEntryActivity.showDuplicateBottomSheet', 'EditEntryActivity.lambda$showDuplicateBottomSheet$22',
    'Tap Overwrite in the duplicate sheet (asks to delete the duplicate first)',
    guard='a new entry has the same name and issuer as an existing entry (EditEntryActivity.java:858-861)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:886-903,900')
gui('EditEntryActivity.lambda$showDuplicateBottomSheet$22', 'EditEntryActivity.lambda$showDuplicateBottomSheet$21',
    'Tap Delete in the confirmation dialog (the duplicate is removed, then the entry is added)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:919-927')
gui('EditEntryActivity.showDuplicateBottomSheet', 'EditEntryActivity.lambda$showDuplicateBottomSheet$23',
    'Tap Add suffix in the duplicate sheet (the name gets a suffix, then the entry is added)',
    guard='a new entry has the same name and issuer as an existing entry (EditEntryActivity.java:858-861)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:933-937')
gui('EditEntryActivity.showDuplicateBottomSheet', 'EditEntryActivity.lambda$showDuplicateBottomSheet$24',
    'Tap Cancel in the duplicate sheet (the sheet closes)',
    guard='a new entry has the same name and issuer as an existing entry (EditEntryActivity.java:858-861)',
    evidence=FW_CLICK + '; SRC ui/EditEntryActivity.java:939')

# --- still open after batch 3: the EntryListView forwards to the MainActivity listener (onEntryClick, onSelect, onDeselect, onLongEntryClick,
# onEntryListTouch, onEntryMove, ...) are checked against the build output, the filter lambda (EntryAdapter.lambda$onBindViewHolder$3), and the
# caller listeners of the other Dialogs callers (ImportEntriesActivity, EditEntryActivity, AuthActivity, GroupManagerActivity, the preference fragments).
UNREACHABLE = {
    'Dialogs.lambda$showErrorDialog$16': ('branch_never_taken',
        'INFERRED: the OnShowListener (Dialogs.java:401-404) replaces this Details button click listener before the dialog can be tapped, so the '
        'default listener at Dialogs.java:396-398 is never called (AlertDialog source not read)', 'ui/dialogs/Dialogs.java:396-398', 'INFERRED'),
}



# --- batch 7 UNREACHABLE: the generated Glide API classes GlideApp and GlideOptions. Their names occur nowhere in the app
# source tree (grep of app/src: no GlideApp or GlideOptions), so no app code can call their static helpers or constructor.
# This block must come AFTER the UNREACHABLE = {...} literal above (a later literal would discard these entries).
# The group is read from the method universe (method_list.json) so that every method of the two classes is covered.
import json as _json
_UNIV_SHORT = [_r['short'] for _r in _json.load(open(GDIR + '/method_list.json'))]
# The builder lets an UNREACHABLE entry override a path, so the five GlideOptions methods that have a path are kept out of the group:
# <init> and apply come from the auto call row GlideRequests.setRequestOptions -> GlideOptions.apply/<init> (GlideRequests.java:176);
# autoClone, clone and lock get their edges below (the coverage run executed them, see out/sanity_check.csv).
_B7_REACHED = {'GlideOptions.<init>', 'GlideOptions.apply', 'GlideOptions.autoClone', 'GlideOptions.clone', 'GlideOptions.lock'}
_B7_REASON = ('no_trigger_in_app', 'generated Glide API class (GlideApp or GlideOptions, created by the Glide annotation processor from ui/glide/AegisGlideModule.java:19): no app source file names either class (grep of app/src), so no app code calls its helpers; the app calls Glide.with directly (e.g. ui/AssignIconsActivity.java:236)', 'ui/glide/AegisGlideModule.java:19', 'SOURCE')
for _m in _UNIV_SHORT:
    if (_m.startswith('GlideApp.') or _m.startswith('GlideOptions.')) and _m not in _B7_REACHED and _UNIV_SHORT.count(_m) == 1:
        UNREACHABLE[_m] = _B7_REASON
# The loop above uses the raw short names, so overloads (the builder renames them with their parameter types) are listed by hand.
_B7_OVERLOADS = """
GlideApp.getPhotoCacheDir(Context)
GlideApp.getPhotoCacheDir(Context,String)
GlideApp.init(Context,GlideBuilder)
GlideApp.init(Glide)
GlideApp.with(Activity)
GlideApp.with(Fragment)
GlideApp.with(Context)
GlideApp.with(View)
GlideApp.with(Fragment)#2
GlideApp.with(FragmentActivity)
GlideOptions.error(int)
GlideOptions.error(Drawable)
GlideOptions.errorOf(int)
GlideOptions.errorOf(Drawable)
GlideOptions.fallback(int)
GlideOptions.fallback(Drawable)
GlideOptions.optionalTransform(Transformation)
GlideOptions.optionalTransform(Class,Transformation)
GlideOptions.override(int)
GlideOptions.override(int,int)
GlideOptions.overrideOf(int)
GlideOptions.overrideOf(int,int)
GlideOptions.placeholder(int)
GlideOptions.placeholder(Drawable)
GlideOptions.placeholderOf(int)
GlideOptions.placeholderOf(Drawable)
GlideOptions.transform(Transformation)
GlideOptions.transform(Class,Transformation)
GlideOptions.transform(Transformation[])
""".split()
for _m in _B7_OVERLOADS:
    UNREACHABLE[_m] = _B7_REASON

# --- batch 7 reached GlideOptions methods (the Glide library calls its own RequestOptions methods on the generated options object;
# the library source is not read, so these edges are INFERRED; the coverage run executed all three, see out/sanity_check.csv)
e('GlideRequests.setRequestOptions', 'GlideOptions.apply', 'CALL',
  'the options are not a GlideOptions yet: the generated override wraps them with new GlideOptions().apply(toSet)',
  guard='the options passed in are not already a GlideOptions (GlideRequests.java:176 is the else branch of the instanceof check)',
  evidence='INFERRED generated code (GlideRequests.java is not in the source tree; the call is in the build class, line 176))')
e('GlideOptions.apply', 'GlideOptions.autoClone', 'FRAMEWORK',
  'the library RequestOptions.apply calls autoClone() on the options (virtual call, so the generated override runs); the library source is not on disk, so this step is not verified',
  cls='non_standard', via='library virtual dispatch: Glide RequestOptions.apply calls autoClone(), which the generated GlideOptions overrides (Glide library source not on disk)',
  evidence='INFERRED Glide library RequestOptions.apply -> autoClone (library source not on disk); generated GlideOptions.java not in the source tree')
e('GlideOptions.autoClone', 'GlideOptions.clone', 'FRAMEWORK',
  'the library RequestOptions.autoClone copies the options by calling clone() (virtual call, so the generated override runs)',
  cls='non_standard', via='library virtual dispatch: Glide RequestOptions.autoClone calls clone(), which the generated GlideOptions overrides (Glide library source not on disk)',
  evidence='INFERRED Glide library RequestOptions.autoClone -> clone (library source not on disk)')
e('GlideRequests.setRequestOptions', 'GlideOptions.lock', 'FRAMEWORK',
  'the library locks the default options after they are set on the request manager (lock() on the generated options object)',
  evidence='INFERRED Glide library RequestManager calls RequestOptions.lock on the default options (library source not read)')

# --- batch 8 (preferences): PreferencesActivity and the settings fragments. The main list is created by the activity's commit
# (PreferencesActivity.java:41-46). Each sub-page is created by the framework from its android:fragment class name (reflection through
# FragmentFactory.instantiate, PreferencesActivity.java:81; names in res/xml/preferences.xml:8-44). The fragment lifecycle is written from
# each <init> in the order the framework calls it (attach, onCreatePreferences, onResume), like the Activity <init> -> onCreate edges.
FW_PREF = ('INFERRED androidx.preference: a tap on a Preference row calls its OnPreferenceClickListener, or the activity callback '
           'OnPreferenceStartFragmentCallback for a row with android:fragment (androidx source not cached)')
FW_FRAG = ('INFERRED androidx.fragment: a committed transaction attaches the fragment, then PreferenceFragmentCompat.onCreate builds the '
           'list (onCreatePreferences), then onResume runs (androidx source not cached)')
FW_HILT = ('INFERRED Hilt fragment base: the generated Hilt_PreferencesFragment is not in the source tree; its onAttach(Context) injects the '
           'fragment (same pattern as Hilt_AegisActivity, graph_def.py:150-165)')
FW_INSETS = ('INFERRED androidx.core ViewCompat.setOnApplyWindowInsetsListener: the listener runs when the window insets are dispatched '
             '(androidx source not cached)')
FW_ANIM = ('INFERRED androidx.fragment: a transaction with custom animations asks the fragment for its animation through '
           'onCreateAnimation (androidx source not cached)')

# PreferencesActivity: the fragment-started listener, the state save, the Up arrow and the sub-page taps
e('PreferencesActivity.onCreate', 'PreferencesActivity$FragmentResumeListener.onFragmentStarted', 'FRAMEWORK',
  'the main list starts after its commit: the listener sets the settings title', evidence=FW_FRAG + '; SRC ui/PreferencesActivity.java:32-33,44-46,113-118')
e('PreferencesActivity.showFragment', 'PreferencesActivity$FragmentResumeListener.onFragmentStarted', 'FRAMEWORK',
  'a sub-page starts after its commit: the listener sets the title of the appearance page', evidence=FW_FRAG + '; SRC ui/PreferencesActivity.java:91-97,113-122')
e('PreferencesActivity.onCreate', 'PreferencesActivity.onSaveInstanceState', 'SYSTEM',
  'API 27: the framework saves the instance state after onPause (the page is left or the device is rotated)',
  evidence=FW_SAVE + '; SRC ui/PreferencesActivity.java:63-66')
gui('PreferencesActivity.onCreate', 'PreferencesActivity.onOptionsItemSelected', 'Tap the Up arrow in the settings toolbar (home item)',
    evidence=FW_MENU + '; SRC ui/PreferencesActivity.java:35-37,69-73')
e('MainPreferencesFragment.onCreatePreferences', 'S_SETTINGS_MAIN', 'ENTERS', 'the settings main list is shown (the preferences.xml rows)',
  evidence='SRC ui/PreferencesActivity.java:40-46; SRC ui/fragments/preferences/MainPreferencesFragment.java:7-12; SRC res/xml/preferences.xml:8-44')
gui('S_SETTINGS_MAIN', 'PreferencesActivity.onPreferenceStartFragment',
    'Tap a row of the main settings list that opens a sub-page (android:fragment in preferences.xml)',
    evidence=FW_PREF + '; SRC ui/PreferencesActivity.java:19,80-84; SRC res/xml/preferences.xml:8-44')

# sub-pages created by the framework from the android:fragment name of the tapped row (reflection, non_standard)
_B8_ROWS = [
    ('AppearancePreferencesFragment', 8), ('BehaviorPreferencesFragment', 14), ('IconPacksManagerFragment', 20),
    ('SecurityPreferencesFragment', 26), ('BackupsPreferencesFragment', 32), ('ImportExportPreferencesFragment', 38),
    ('AuditLogPreferencesFragment', 44),
]
for _cls, _line in _B8_ROWS:
    e('PreferencesActivity.onPreferenceStartFragment', _cls + '.<init>', 'CALL',
      'the framework creates the sub-page named by the tapped row (' + _cls + ')', cls='non_standard',
      via='reflection: FragmentFactory.instantiate(getClassLoader(), pref.getFragment()) loads the class named in android:fragment and calls its constructor (PreferencesActivity.java:81; res/xml/preferences.xml:%d)' % _line,
      guard='the tapped row has android:fragment=%s (res/xml/preferences.xml:%d)' % (_cls, _line),
      evidence=FW_FRAG + '; SRC ui/PreferencesActivity.java:80-84; SRC res/xml/preferences.xml:%d' % _line)

# the requested sub-page from the error card: the class in the intent extra is created with newInstance (reflection)
e('PreferencesActivity.getRequestedFragment', 'BackupsPreferencesFragment.<init>', 'CALL',
  'the error card opened the backups page: the class from the intent extra is created', cls='non_standard',
  via='reflection: fragmentType.newInstance() on the Class from the "fragment" intent extra (PreferencesActivity.java:100-107); MainActivity passes BackupsPreferencesFragment.class (MainActivity.java:1170,1187)',
  guard='the intent has the fragment extra (set by startPreferencesActivity(Class,String), MainActivity.java:830)', needs_state=ST_ERROR_CARD,
  evidence='SRC ui/PreferencesActivity.java:48-51,100-107; SRC ui/MainActivity.java:830,1170,1187')

# fragment lifecycle of the six settings fragments that the batch needs (attach, list, resume), each from its <init>
_B8_LIFECYCLE = [
    ('MainPreferencesFragment', 'PreferencesFragment.onResume'),
    ('AppearancePreferencesFragment', 'PreferencesFragment.onResume'),
    ('BehaviorPreferencesFragment', 'PreferencesFragment.onResume'),
    ('SecurityPreferencesFragment', 'SecurityPreferencesFragment.onResume'),
    ('BackupsPreferencesFragment', 'BackupsPreferencesFragment.onResume'),
    ('ImportExportPreferencesFragment', 'PreferencesFragment.onResume'),
]
for _cls, _resume in _B8_LIFECYCLE:
    e(_cls + '.<init>', 'Hilt_PreferencesFragment.onAttach(Context)', 'LIFECYCLE',
      'the fragment is attached after its transaction commits (' + _cls + ')', evidence=FW_FRAG + '; ' + FW_HILT)
    e(_cls + '.<init>', _cls + '.onCreatePreferences', 'LIFECYCLE',
      'the preference list is built after the attach (' + _cls + ')',
      evidence=FW_FRAG + ('; SRC ui/PreferencesActivity.java:41-46' if _cls == 'MainPreferencesFragment' else '; SRC ui/PreferencesActivity.java:84,91-97'))
    e(_cls + '.onCreatePreferences', 'PreferencesFragment.onCreateRecyclerView', 'LIFECYCLE',
      'the view is created around the list (onCreateView of PreferenceFragmentCompat)', evidence=FW_FRAG)
    e(_cls + '.<init>', _resume, 'LIFECYCLE', 'the fragment is resumed after its list is built (' + _cls + ')',
      evidence=FW_FRAG + '; SRC ui/fragments/preferences/PreferencesFragment.java:49-61')

# Hilt base of the settings fragments (generated, not in the source tree): attach, then inject through the component manager
e('Hilt_PreferencesFragment.onAttach(Context)', 'Hilt_PreferencesFragment.onAttach(Activity)', 'FRAMEWORK',
  'Fragment.onAttach(Context) calls the onAttach(Activity) overload when the host is an activity',
  evidence='INFERRED androidx.fragment Fragment.onAttach(Context) (framework source not read); generated Hilt_PreferencesFragment not in source tree')
e('Hilt_PreferencesFragment.onAttach(Context)', 'Hilt_PreferencesFragment.initializeComponentContext', 'FRAMEWORK',
  'the Hilt base sets up its component context on attach', evidence=FW_HILT)
e('Hilt_PreferencesFragment.onAttach(Context)', 'Hilt_PreferencesFragment.inject', 'FRAMEWORK',
  'the Hilt base injects the fragment fields on attach', evidence=FW_HILT)
e('Hilt_PreferencesFragment.inject', 'Hilt_PreferencesFragment.generatedComponent', 'FRAMEWORK',
  'inject reads the generated component (created on first use)', evidence=FW_HILT)
e('Hilt_PreferencesFragment.generatedComponent', 'Hilt_PreferencesFragment.componentManager', 'FRAMEWORK',
  'the component is read through the component manager', evidence=FW_HILT)
e('Hilt_PreferencesFragment.componentManager', 'Hilt_PreferencesFragment.createComponentManager', 'FRAMEWORK',
  'the first call creates the component manager', evidence=FW_HILT)

# animation of a sub-page and the window insets of the list
e('PreferencesActivity.showFragment', 'PreferencesFragment.onCreateAnimation', 'FRAMEWORK',
  'the sub-page transaction has slide animations: the fragment supplies them', evidence=FW_ANIM + '; SRC ui/PreferencesActivity.java:92-96')
e('PreferencesFragment.onCreateRecyclerView', 'PreferencesFragment.lambda$onCreateRecyclerView$0', 'FRAMEWORK',
  'the window insets reach the list: the listener pads its bottom by the system bars',
  evidence=FW_INSETS + '; SRC ui/fragments/preferences/PreferencesFragment.java:73-86')

# ImportExportPreferencesFragment: the four preference taps (onCreatePreferences registers them)
gui('ImportExportPreferencesFragment.onCreatePreferences', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$6',
    'Tap Import in the import and export settings (pref_import)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:105-115')
gui('ImportExportPreferencesFragment.onCreatePreferences', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$8',
    'Tap Import from another app (pref_import_app)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:117-123')
gui('ImportExportPreferencesFragment.onCreatePreferences', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$9',
    'Tap Export (pref_export)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:125-129')
gui('ImportExportPreferencesFragment.onCreatePreferences', 'ImportExportPreferencesFragment.lambda$onCreatePreferences$10',
    'Tap Google Authenticator style export (pref_google_auth_style_export)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:131-135')

# the importer dialog passes the chosen importer to the listener (an interface callback, written as a call into the lambda)
e(_IMP_OK_FILE, 'ImportExportPreferencesFragment.lambda$onCreatePreferences$5', 'CALL',
  'the OK button gives the chosen importer to the import listener: the file picker opens',
  guard='the dialog was opened by the Import preference (showImportersDialog with isDirect false, ImportExportPreferencesFragment.java:107)',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:107-113')
e(_IMP_OK_APP, 'ImportExportPreferencesFragment.lambda$onCreatePreferences$7', 'CALL',
  'the OK button gives the chosen importer to the import-app listener: the import page opens',
  guard='the dialog was opened by Import from another app (isDirect true, ImportExportPreferencesFragment.java:119)',
  evidence='SRC ui/dialogs/Dialogs.java:536-538; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:119-121')

# the file picker result (ACTION_GET_CONTENT) runs the import launcher, which runs onImportSelectResult (already a CALL)
# the Settings import has its own variant of the shared launcher node (the icon packs and the backups use the shared node).
# The launch is a hand CALL into the variant from the importer dialog's listener (ImportExportPreferencesFragment.java:110-112).
# A hand edge to the variant also suppresses the auto row to the shared node (build_graph.add_auto_edges, manual-edge rule).
_FIL_SETTINGS = 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@SETTINGS_IMPORT'
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$5', _FIL_SETTINGS, 'CALL',
  'the file picker opens (ACTION_GET_CONTENT) through the import launcher, after the importer is chosen',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:110-112')
e(_FIL_SETTINGS, 'ImportExportPreferencesFragment.lambda$new$0', 'RESULT',
  'the file picker returns a file: the import launcher runs onImportSelectResult', env=ENV_PICKER_SETTINGS,
  guard='the picker returned RESULT_OK with a URI (onImportSelectResult returns early otherwise, ImportExportPreferencesFragment.java:146-148)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79,112')
e('ImportExportPreferencesFragment.lambda$new$0', 'ImportExportPreferencesFragment.onImportSelectResult', 'CALL',
  'the picker result carries data: onImportSelectResult runs with the result code and the data',
  guard='activityResult.getData() is not null (ImportExportPreferencesFragment.java:76)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:73-79')
e('ImportFileTask.onPostExecute@SETTINGS_IMPORT', 'ImportExportPreferencesFragment.lambda$onImportSelectResult$11', 'CALL',
  'the file is read: the callback opens the import page, or shows the read error',
  guard='no condition on the call (ImportFileTask.java:55 is unconditional); inside the lambda, result.getError() == null opens the import page, otherwise the read error dialog is shown (ImportExportPreferencesFragment.java:152-155)', needs_state=ST_SETTINGS_IMPORT,
  evidence='SRC ui/tasks/ImportFileTask.java:53-56; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:150-157')
e('ImportExportPreferencesFragment.startImportEntriesActivity', 'ImportEntriesActivity.<init>', 'INTENT',
  'the import page opens with the chosen importer and the file (no file for an app import)',
  guard='the file argument is the ImportFileTask result on the file import path (ImportExportPreferencesFragment.java:153), or null on the app import path (line 120)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:120,153')
e('ImportEntriesActivity.<init>', 'ImportEntriesActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the import page',
  evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')

# import-page split by the file argument (ImportEntriesActivity.java:107-128). startImport calls
# startImportFile only when the intent file extra is non-null (Settings file import, :153) and
# startImportApp only when it is null (app import, :120). The shared startImport node let a route mix
# the app prefix (file null) with the file suffix (file non-null) — route 16 after the dialog/task
# splits. The page chain is therefore split @FILE/@APP from startImportEntriesActivity down to
# startImport. Both callers of startImportEntriesActivity use variants, so the plain chain has no
# incoming edge and cannot carry a mixed route. Variant onCreate nodes keep the page's other hand
# edges (menu, scroll listener, save button) so those methods stay reachable through both variants.
_SIE_APP = 'ImportExportPreferencesFragment.startImportEntriesActivity@APP'
_SIE_FILE = 'ImportExportPreferencesFragment.startImportEntriesActivity@FILE'
e('ImportExportPreferencesFragment.lambda$onCreatePreferences$7', _SIE_APP, 'CALL',
  'Direct call', evidence='SRC ImportExportPreferencesFragment.java:120 (bytecode)')
e('ImportExportPreferencesFragment.lambda$onImportSelectResult$11', _SIE_FILE, 'CALL',
  'Direct call', evidence='SRC ImportExportPreferencesFragment.java:153 (bytecode)')
e(_SIE_APP, 'ImportEntriesActivity.<init>@APP', 'INTENT',
  'the import page opens with the chosen importer and no file (app import)',
  guard='the file argument is null on the app import path (ImportExportPreferencesFragment.java:120)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:120')
e(_SIE_FILE, 'ImportEntriesActivity.<init>@FILE', 'INTENT',
  'the import page opens with the chosen importer and the file (file import)',
  guard='the file argument is the ImportFileTask result on the file import path (ImportExportPreferencesFragment.java:153)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:161-165; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:153')
for _tag in ('@APP', '@FILE'):
    e('ImportEntriesActivity.<init>' + _tag, 'ImportEntriesActivity.onCreate' + _tag, 'LIFECYCLE', 'Activity.onCreate of the import page',
      evidence=FW_CREATE + '; SRC ui/ImportEntriesActivity.java:62')
    e('ImportEntriesActivity.onCreate' + _tag, 'ImportEntriesActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate',
      evidence=FW_OPTIONS + '; SRC ui/ImportEntriesActivity.java:397-401')
    e('ImportEntriesActivity.onCreate' + _tag, 'ImportEntriesActivity$1.onScrolled', 'FRAMEWORK',
      'the list scrolls: the save button follows the scroll',
      evidence='INFERRED androidx.recyclerview: RecyclerView calls each OnScrollListener.onScrolled while the list moves (source not read); SRC ui/ImportEntriesActivity.java:79-85')
    gui('ImportEntriesActivity.onCreate' + _tag, 'ImportEntriesActivity.lambda$onCreate$0',
        'Tap the save button: the wipe dialog opens if the wipe option is on and the vault has entries, otherwise the selected entries are saved',
        evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:92-100')
e('ImportEntriesActivity.onCreate@APP', 'ImportEntriesActivity.startImport@APP', 'CALL', 'the import page starts the import from its intent extras',
  guard='abortIfOrphan(savedInstanceState) is false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157) and the file extra is null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104; SRC ui/AegisActivity.java:154-157')
e('ImportEntriesActivity.onCreate@FILE', 'ImportEntriesActivity.startImport@FILE', 'CALL', 'the import page starts the import from its intent extras',
  guard='abortIfOrphan(savedInstanceState) is false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157) and the file extra is non-null (ImportEntriesActivity.java:104,109)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104; SRC ui/AegisActivity.java:154-157')
e('ImportEntriesActivity.startImport@APP', 'ImportEntriesActivity.startImportApp', 'CALL',
  'no file was passed and the installed app version is supported: the entries are read from the app',
  guard='no file was passed (ImportEntriesActivity.java:109) and the installed app version is supported (isInstalledAppVersionSupported, ImportEntriesActivity.java:110)',
  evidence='SRC ui/ImportEntriesActivity.java:109-111')
e('ImportEntriesActivity.startImport@FILE', 'ImportEntriesActivity.startImportFile', 'CALL',
  'Direct call', evidence='SRC ImportEntriesActivity.java:127 (bytecode)')

# the app-version warning lives on the @APP branch only (file is null, ImportEntriesActivity.java:110-123):
# Yes reads from the installed app, No closes the page. The plain startImport node is dead after the
# split, so these two gui edges are re-written on the variant, or lambda$startImport$1/$2 lose their route.
gui('ImportEntriesActivity.startImport@APP', 'ImportEntriesActivity.lambda$startImport$1',
    'Tap Yes in the app version warning: the entries are read from the installed app',
    guard='the installed app version is not supported (ImportEntriesActivity.java:110-113); the warning opens only then',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:113-120')
gui('ImportEntriesActivity.startImport@APP', 'ImportEntriesActivity.lambda$startImport$2',
    'Tap No in the app version warning: the page closes',
    guard='the installed app version is not supported (ImportEntriesActivity.java:110-113); the warning opens only then',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:121-123')

# --- batch 9 (export): the Export row (lambda $9 calls startExport) and the Google Authenticator style export row ($10).
# startExport opens a dialog; the dialog's lambdas get their own hand edges because auto_calls 'lambdas' rows make no edges.
# Lambda map (javac numbers; line in ImportExportPreferencesFragment.java): $12 format dropdown item (:182), $20 OnShowListener (:209),
# $13 state validator (:213), $14 Encrypt checkbox (:230), $15 accept checkbox (:239), $16 export-all checkbox (:243),
# $17 OK (:252), $19 Share (:280), $18 Share callback (:308), $21 group filter (:341), $22-$25 finish callbacks (:446, :484, :495, :499),
# $1.lambda$onSlotResult$0 finish callback (:467), $26 result callback (:514), $1-$4 export launchers (:82-94).
# The groups dropdown dismiss method reference (stateValidator::enableIfValid, :250) also runs $13; not modelled, $13 is reached above.
_B9_IE = 'ImportExportPreferencesFragment.'
gui(_B9_IE + 'startExport', _B9_IE + 'lambda$startExport$12',
    'Pick a format in the export dropdown (the item click sets the Encrypt checkbox and the password text)',
    evidence=FW_ITEM + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:180-187')
e(_B9_IE + 'startExport', _B9_IE + 'lambda$startExport$20', 'FRAMEWORK',
  'the export dialog is shown: its OnShowListener sets up the checkboxes and the OK and Share buttons',
  evidence=FW_DIALOG + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:201-209,332')

# the three checkboxes call the state validator $13 to enable or disable OK and Share (interface callback)
for _lam, _text, _listen, _call in [
    ('lambda$startExport$14', 'Tick or untick Encrypt in the export dialog', 230, 231),
    ('lambda$startExport$15', 'Tick or untick the accept checkbox (plain export) in the export dialog', 239, 240),
    ('lambda$startExport$16', 'Tick or untick Export all groups in the export dialog', 243, 247),
]:
    gui(_B9_IE + 'lambda$startExport$20', _B9_IE + _lam, _text,
        evidence=FW_CHECK + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:%d-%d' % (_listen, _call))
    e(_B9_IE + _lam, _B9_IE + 'lambda$startExport$13', 'CALL',
      'the checkbox changed: the state validator enables or disables the OK and Share buttons', cls='non_standard',
      via='interface callback: DialogStateValidator.enableIfValid (lambda $13 implements it, ImportExportPreferencesFragment.java:213-228)',
      evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:%d' % _call)

# the OK and Share buttons (the guard is the same as the buttons' own early returns)
gui(_B9_IE + 'lambda$startExport$20', _B9_IE + 'lambda$startExport$17',
    'Tap OK in the export dialog (the export goes to the document creator, ACTION_CREATE_DOCUMENT)',
    guard='Encrypt or the accept checkbox is ticked, and all groups are exported or a group is chosen (ImportExportPreferencesFragment.java:215-217,255-265)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:252-278')
gui(_B9_IE + 'lambda$startExport$20', _B9_IE + 'lambda$startExport$19',
    'Tap Share in the export dialog (the export is written to the cache, then the share chooser opens)',
    guard='Encrypt or the accept checkbox is ticked, and all groups are exported or a group is chosen (ImportExportPreferencesFragment.java:284-293)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:280-329')
e(_B9_IE + 'lambda$startExport$19', _B9_IE + 'lambda$startExport$18', 'CALL',
  'Share: startExportVault gets the Share callback and runs it with the chosen format',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:308-327')

# the file picker result of the export: onExportResult calls startExportVault, which runs the StartExportCallback lambda $26.
# A variant of startExportVault: the plain node is also reached from the Share path, which must not reach $26
_SEV_RESULT = _B9_IE + 'startExportVault@RESULT'
e(_B9_IE + 'onExportResult', _SEV_RESULT, 'CALL',
  'the export file was picked: onExportResult starts the export with the result callback',
  guard='the result is RESULT_OK with a URI (onExportResult returns early otherwise, ImportExportPreferencesFragment.java:506-512)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:505-514')
e(_SEV_RESULT, _B9_IE + 'lambda$onExportResult$26', 'CALL',
  'startExportVault runs the result callback for the chosen format',
  guard='the export result callback runs for the chosen format (onExportResult passes $26 to startExportVault, ImportExportPreferencesFragment.java:514)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:442-499,514')
# --- route 06 format split: the export-result chain is split by format, so the
# encrypted-format branch can never win on a plain vault. $1 (CODE_EXPORT) and $2
# (CODE_EXPORT_PLAIN) are the launcher callbacks at :82/:86; the hand edges below
# suppress the auto $1/$2 -> plain onExportResult edges (src-specific rule), so
# the plain onExportResult stays only for the HTML/Google launchers ($3/$4). The
# @ENC chain carries needs_state ST_VAULT_ENCRYPTED (the $22 finish callback exists
# only in the CODE_EXPORT + isEncryptionEnabled branch, :444-446), so on a plain
# vault it costs one more setup edge than the @PLAIN chain and the cheapest dumped
# route is the fully consistent plain-format branch. No Share-path edge is added:
# the Share callback $18 does not run ExportTask in the baseline graph, and this
# split does not change that.
e('ImportExportPreferencesFragment.lambda$new$1', 'ImportExportPreferencesFragment.onExportResult@ENC', 'CALL', 'Direct call',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:83 (bytecode)')
e('ImportExportPreferencesFragment.lambda$new$2', 'ImportExportPreferencesFragment.onExportResult@PLAIN', 'CALL', 'Direct call',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:87 (bytecode)')
e('ImportExportPreferencesFragment.onExportResult@ENC', 'ImportExportPreferencesFragment.startExportVault@ENC_RESULT', 'CALL',
  'the export file was picked: onExportResult starts the export with the result callback',
  guard='the result is RESULT_OK with a URI (onExportResult returns early otherwise, ImportExportPreferencesFragment.java:506-512)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:505-514')
e('ImportExportPreferencesFragment.onExportResult@PLAIN', 'ImportExportPreferencesFragment.startExportVault@PLAIN_RESULT', 'CALL',
  'the export file was picked: onExportResult starts the export with the result callback',
  guard='the result is RESULT_OK with a URI (onExportResult returns early otherwise, ImportExportPreferencesFragment.java:506-512)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:505-514')
e('ImportExportPreferencesFragment.startExportVault@ENC_RESULT', 'ImportExportPreferencesFragment.lambda$onExportResult$26@ENC', 'CALL',
  'startExportVault runs the result callback for the encrypted format',
  guard='the encrypted Aegis format is chosen: requestCode == CODE_EXPORT (ImportExportPreferencesFragment.java:444) and vault.isEncryptionEnabled() (line 445)',
  needs_state=ST_VAULT_ENCRYPTED,
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:442-499,514')
e('ImportExportPreferencesFragment.startExportVault@PLAIN_RESULT', 'ImportExportPreferencesFragment.lambda$onExportResult$26@PLAIN', 'CALL',
  'startExportVault runs the result callback for the plain format',
  guard='the plain Aegis format is chosen: requestCode == CODE_EXPORT_PLAIN (ImportExportPreferencesFragment.java:483-484)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:442-499,514')
e('ImportExportPreferencesFragment.lambda$onExportResult$26@ENC', 'ExportTask.doInBackground', 'ASYNC', 'the export runs on a background thread (the export task is started by the export callback)',
  guard='temp file written with no VaultRepositoryException or IOException (the catch at ImportExportPreferencesFragment.java:521-524 returns, so the execute at line 535 is skipped)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:535; SRC ui/tasks/ExportTask.java:24')
e('ImportExportPreferencesFragment.lambda$onExportResult$26@PLAIN', 'ExportTask.doInBackground', 'ASYNC', 'the export runs on a background thread (the export task is started by the export callback)',
  guard='temp file written with no VaultRepositoryException or IOException (the catch at ImportExportPreferencesFragment.java:521-524 returns, so the execute at line 535 is skipped)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:535; SRC ui/tasks/ExportTask.java:24')

# the two callbacks ($18 Share, $26 result) run the finish callback that startExportVault built for the chosen format
_B9_FINISH = [
    ('lambda$startExportVault$22', 'the Aegis format with encryption and an encrypted vault is chosen (startExportVault CODE_EXPORT, :444-446)', 446),
    ('lambda$startExportVault$23', 'the plain Aegis format is chosen (startExportVault CODE_EXPORT_PLAIN, :483-484)', 484),
    ('lambda$startExportVault$24', 'the Google Authenticator URI format is chosen (startExportVault CODE_EXPORT_GOOGLE_URI, :494-495)', 495),
    ('lambda$startExportVault$25', 'the HTML format is chosen (startExportVault CODE_EXPORT_HTML, :498-499)', 499),
    ('ImportExportPreferencesFragment$1.lambda$onSlotResult$0', 'the Aegis format with encryption and no password slot yet: the set-password dialog ran (startExportVault :454-467)', 467),
]
for _cb, _line in [('lambda$startExport$18', 310), ('lambda$onExportResult$26', 520)]:
    for _fin, _guard, _fline in _B9_FINISH:
        if _fin.startswith('ImportExportPreferencesFragment$1.'):
            _dst = _fin
        else:
            _dst = _B9_IE + _fin
        e(_B9_IE + _cb, _dst, 'CALL', 'the callback writes the export through the finish callback of the chosen format',
          cls='non_standard', via='interface callback: FinishExportCallback.exportVault (the lambda is passed to the callback by startExportVault; the callback calls it at ImportExportPreferencesFragment.java:%d)' % _line,
          guard=_guard, evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:%d,%d' % (_line, _fline))

# the group filter is returned to the dialog and kept for the export; the vault applies it to each entry (Vault.java:31)
e(_B9_IE + 'getVaultEntryFilter', _B9_IE + 'lambda$getVaultEntryFilter$21', 'CALL',
  'the group filter is kept for the export: the vault asks it for each entry it writes', cls='non_standard',
  via='interface callback: Vault.EntryFilter.includeEntry (the lambda is returned at ImportExportPreferencesFragment.java:341; Vault.java:31 calls it)',
  guard='at least one group is ticked in the dropdown (ImportExportPreferencesFragment.java:341)',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:335-348; SRC vault/Vault.java:31')

# the export launches (OK at :277 in lambda $17, Share chooser at :326 in lambda $18) use a variant of fireIntentLauncher, so the
# export result callbacks are reached only from the export launches (the shared node also serves the import and icon launches)
_FIL_EXPORT = 'VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)@EXPORT'
e(_B9_IE + 'lambda$startExport$17', _FIL_EXPORT, 'CALL', 'Tap OK: the export goes to the system document creator through the launcher of the chosen format',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:277 (getExportRequestLauncher, :403-411)')
e(_B9_IE + 'lambda$startExport$18', _FIL_EXPORT, 'CALL', 'Share: the share chooser is started through the launcher of the chosen format',
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:326 (getExportRequestLauncher, :403-411)')
# the system document creator or the share chooser returns through the export launchers (ActivityResultLauncher)
for _lam, _guard, _line in [
    ('lambda$new$1', 'the Aegis format with encryption is chosen (getExportRequestLauncher returns exportResultLauncher, :404-405)', 82),
    ('lambda$new$2', 'the Aegis format without encryption is chosen (getExportRequestLauncher returns exportPlainResultLauncher, :405)', 86),
    ('lambda$new$3', 'the HTML format is chosen (getExportRequestLauncher returns exportHtmlResultLauncher, :407)', 90),
    ('lambda$new$4', 'the Google Authenticator URI format is chosen (getExportRequestLauncher returns exportGoogleUriResultLauncher, :410)', 94),
]:
    e(_FIL_EXPORT, _B9_IE + _lam, 'RESULT',
      'the export returns to Aegis: the launcher runs onExportResult with the result code and the file URI',
      env=ENV_EXPORT_RESULT, guard=_guard,
      evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:%d,403-411' % _line)

# the export task: started by the callback, runs on a background thread, then the listener shows the result
e('ImportExportPreferencesFragment.lambda$onExportResult$26', 'ExportTask.doInBackground', 'ASYNC', 'the export runs on a background thread (the export task is started by the export callback)',
  guard='temp file written with no VaultRepositoryException or IOException (the catch at ImportExportPreferencesFragment.java:521-524 returns, so the execute at line 535 is skipped)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:535; SRC ui/tasks/ExportTask.java:24')
e('ExportTask.doInBackground', 'ExportTask.onPostExecute', 'ASYNC', 'the result is posted to the main thread',
  guard='the export task was not cancelled (a cancelled task calls onCancelled instead, AsyncTask.java:691-697)',
  evidence=FW_ASYNC + '; FW-SRC core/java/android/os/AsyncTask.java:691-697 (finish); SRC ui/tasks/ExportTask.java:43-45')
e('ExportTask.onPostExecute', 'ImportExportPreferencesFragment$ExportResultListener.onTaskFinished', 'CALL',
  'the export task is done: the listener shows the error dialog or the success toast',
  guard='the export task finished (ExportTask.java:43-45)',
  evidence='SRC ui/tasks/ExportTask.java:43-45; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:535,550-563')

# the Google Authenticator style export (row $10): the transfer page opens when at least one entry can be exported
e(_B9_IE + 'startGoogleAuthenticatorStyleExport', 'TransferEntriesActivity.<init>', 'INTENT',
  'the Google Authenticator style export page opens with the QR batches',
  guard='at least one entry is TOTP or HOTP with the default 6 digits and SHA-1, so the export list is not empty (ImportExportPreferencesFragment.java:357-363,384-390)',
  needs_state=ST_GOOGLE_EXPORTABLE,
  evidence='SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:384-390')

# --- batch 10 (appearance and behavior pages): each preference row is a tap (gui from onCreatePreferences, FW_PREF); the dialog a
# row opens is created in the row's lambda, so its item and button lambdas are wired from that row lambda. javac numbers a nested
# lambda just before the lambda that contains it (Appearance $1 inside $2, $3 inside $4, ...). Every name below gets one incoming edge.
FW_CHOICE = ('INFERRED androidx.appcompat AlertDialog: a tap on a single-choice or multi-choice row calls the OnClickListener or '
             'OnMultiChoiceClickListener of the dialog (AppCompat source not read)')
FW_PREF_CHANGE = ('INFERRED androidx.preference: a change of a preference value calls its OnPreferenceChangeListener '
                  '(androidx source not cached)')
_B10_AP = 'AppearancePreferencesFragment.'
_B10_BH = 'BehaviorPreferencesFragment.'

# Appearance: the groups row opens the groups page (GroupManagerActivity)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$0', 'Tap Groups in the appearance settings (pref_groups)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:32-37')
e(_B10_AP + 'lambda$onCreatePreferences$0', 'GroupManagerActivity.<init>', 'INTENT', 'the groups page opens',
  evidence='SRC ui/fragments/preferences/AppearancePreferencesFragment.java:34-35')
e('GroupManagerActivity.<init>', 'GroupManagerActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the groups page',
  evidence=FW_CREATE + '; SRC ui/GroupManagerActivity.java:36-40')
sup(('GroupManagerActivity.onOptionsItemSelected', 'GroupManagerActivity.onRemoveUnusedGroups'))
e('GroupManagerActivity.onOptionsItemSelected', 'GroupManagerActivity.onRemoveUnusedGroups', 'CALL', 'the delete-unused-groups menu item is tapped',
  guard='the action_delete_unused_groups menu item was tapped (GroupManagerActivity.java:201-202)', evidence='SRC ui/GroupManagerActivity.java:201-202')

# Appearance: reset usage count (confirm dialog)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$2', 'Tap Reset usage count (pref_reset_usage_count)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:39-48')
gui(_B10_AP + 'lambda$onCreatePreferences$2', _B10_AP + 'lambda$onCreatePreferences$1', 'Tap Yes in the reset-usage-count dialog (clears the usage counts)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:41-46')

# Appearance: dark mode (theme choice; the activity is recreated)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$4', 'Tap Dark mode (pref_dark_mode) to open the theme choice',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:51-53')
gui(_B10_AP + 'lambda$onCreatePreferences$4', _B10_AP + 'lambda$onCreatePreferences$3', 'Pick a theme in the choose-theme dialog (the theme is saved and the activity is recreated)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:56-67')

# Appearance: dynamic colors (preference change; the activity is recreated)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$5', 'Turn Dynamic colors on or off (pref_dynamic_colors; the activity is recreated)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:72-77')

# Appearance: language (the row exists on SDK above 23 only)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$7', 'Tap Language (pref_lang)',
    guard='the language row is set up only on SDK above 23 (AppearancePreferencesFragment.java:80,102-105)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:79-86')
gui(_B10_AP + 'lambda$onCreatePreferences$7', _B10_AP + 'lambda$onCreatePreferences$6', 'Pick a language in the choose-language dialog (the language is saved and the activity is recreated)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:87-99')

# Appearance: view mode (the account name text is refreshed)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$9', 'Tap View mode (pref_view_mode)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:108-110')
gui(_B10_AP + 'lambda$onCreatePreferences$9', _B10_AP + 'lambda$onCreatePreferences$8', 'Pick a view mode in the choose-view-mode dialog',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:113-123')

# Appearance: code digit grouping
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$11', 'Tap Code digit grouping (pref_code_group_size_string)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:135-136')
gui(_B10_AP + 'lambda$onCreatePreferences$11', _B10_AP + 'lambda$onCreatePreferences$10', 'Pick a grouping in the code-grouping dialog (the grouping is saved)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:139-148')

# Appearance: account name position (the summary and the account name text are refreshed)
gui(_B10_AP + 'onCreatePreferences', _B10_AP + 'lambda$onCreatePreferences$13', 'Tap Account name position (pref_account_name_position)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:153-155')
gui(_B10_AP + 'lambda$onCreatePreferences$13', _B10_AP + 'lambda$onCreatePreferences$12', 'Pick a position in the choose-position dialog (the summary and the account name text update)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/AppearancePreferencesFragment.java:158-168')

# Behavior: search behavior (multi-choice dialog; OK is enabled only with at least one ticked)
gui(_B10_BH + 'onCreatePreferences', _B10_BH + 'lambda$onCreatePreferences$2', 'Tap Search behavior (pref_search_behavior)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:21-23')
gui(_B10_BH + 'lambda$onCreatePreferences$2', _B10_BH + 'lambda$onCreatePreferences$0', 'Tick or untick a search behavior in the dialog (the OK button follows the ticks)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:31-48')
gui(_B10_BH + 'lambda$onCreatePreferences$2', _B10_BH + 'lambda$onCreatePreferences$1', 'Tap OK in the search-behavior dialog (the search mask is saved)',
    guard='at least one search behavior is ticked (the OK button is enabled only then, BehaviorPreferencesFragment.java:36-47)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:49-59')

# Behavior: copy behavior (single choice)
gui(_B10_BH + 'onCreatePreferences', _B10_BH + 'lambda$onCreatePreferences$4', 'Tap Copy behavior (pref_copy_behavior)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:66-69')
gui(_B10_BH + 'lambda$onCreatePreferences$4', _B10_BH + 'lambda$onCreatePreferences$3', 'Pick a copy behavior in the choose-copy dialog (the summary updates)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:72-81')

# Behavior: tap to highlight (preference change; the pause row follows it)
gui(_B10_BH + 'onCreatePreferences', _B10_BH + 'lambda$onCreatePreferences$5', 'Turn Tap to highlight the entry on or off (pref_highlight_entry)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/BehaviorPreferencesFragment.java:89-93')

# --- batch 11 (backups page): each row is a tap or a switch change (gui from onCreatePreferences). The dialogs are created in the
# row lambdas; their buttons are wired from the Dialogs methods, so a dialog answer reaches the backup code through an interface
# call (cls='non_standard'). The backup file and folder pickers return through backupsResultLauncher (RESULT, ENV_BACKUP_RESULT).
_B11_BP = 'BackupsPreferencesFragment.'
_B11_DG = 'Dialogs.'

# status rows: a tap shows the error dialog for the last failed backup (the row is selectable only when the last backup failed)
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$1', 'Tap the built-in backup status row (pref_status_backup_builtin)',
    guard='the row is visible only when backups are on (BackupsPreferencesFragment.java:217); selectable only after a failed backup (:224)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:62-68')
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$2', 'Tap the Android backup status row (pref_status_backup_android)',
    guard='the row is visible only when the Android backup is on (BackupsPreferencesFragment.java:218); selectable only after a failed backup (:224)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:70-76')

# backups switch: turning it on opens the versioning-strategy dialog; turning it off saves the state
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$4', 'Turn Backups (pref_backups) on or off',
    guard='the switch is enabled only when the vault is encrypted (BackupsPreferencesFragment.java:205)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:79-94')
gui(_B11_DG + 'showBackupsVersioningStrategy', _B11_DG + 'lambda$showBackupsVersioningStrategy$34', 'Tap OK in the versioning-strategy dialog (the chosen strategy goes to the listener)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:609-616')
gui(_B11_DG + 'showBackupsVersioningStrategy', _B11_DG + 'lambda$showBackupsVersioningStrategy$35', 'The versioning-strategy dialog is shown: its show listener selects the current strategy',
    evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:619-627')
gui(_B11_DG + 'showBackupsVersioningStrategy', _B11_DG + 'lambda$showBackupsVersioningStrategy$32', 'Pick a strategy radio button (single backup shows the warning; OK follows the choice)',
    evidence=FW_CHOICE + '; SRC ui/dialogs/Dialogs.java:591-599')
gui(_B11_DG + 'showBackupsVersioningStrategy', _B11_DG + 'lambda$showBackupsVersioningStrategy$33', 'Tick the risk-accept box in the single-backup choice (OK follows the box)',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:600-605')
# the pref_backups listener's strategy callback ($3): multiple backups opens the folder picker, single backup creates the file
e(_B11_DG + 'lambda$showBackupsVersioningStrategy$34', _B11_BP + 'lambda$onCreatePreferences$3', 'CALL',
  'the strategy from the dialog is passed back: multiple backups opens the folder picker, single backup creates the file',
  cls='non_standard', via='interface callback: Dialogs.BackupsVersioningStrategyListener.onStrategySelectionResult (Dialogs.java:612-614); the listener is created at BackupsPreferencesFragment.java:81',
  guard='the user taps OK with a strategy chosen (Dialogs.java:611-615)',
  evidence='SRC ui/dialogs/Dialogs.java:609-616; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:81-87')

# reminder: turning it off asks for a confirmation (checkbox dialog); turning it on saves the state
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$5', 'Change the backup reminder (pref_backup_reminder); turning it off asks for a confirmation',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:97-110')
gui(_B11_DG + 'showCheckboxDialog', _B11_DG + 'lambda$showCheckboxDialog$9', 'Tap No in the reminder dialog (the callback gets false)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:282-283')
gui(_B11_DG + 'showCheckboxDialog', _B11_DG + 'lambda$showCheckboxDialog$10', 'Tap Yes in the reminder dialog (the callback gets the checkbox state)',
    guard='the Yes button is enabled only when the checkbox is ticked (Dialogs.java:294-300)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:284-285')
gui(_B11_DG + 'showCheckboxDialog', _B11_DG + 'lambda$showCheckboxDialog$11', 'The reminder dialog is shown: its show listener disables the Yes button',
    evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:294-298')
gui(_B11_DG + 'showCheckboxDialog', _B11_DG + 'lambda$showCheckboxDialog$12', 'Tick the checkbox in the reminder dialog (the Yes button follows the box)',
    evidence=FW_CHECK + '; SRC ui/dialogs/Dialogs.java:300')
e(_B11_DG + 'lambda$showCheckboxDialog$9', _B11_BP + 'saveAndDisableBackupReminder', 'CALL',
  'the No answer is passed to saveAndDisableBackupReminder(false), which changes nothing',
  cls='non_standard', via='interface callback: Dialogs.CheckboxInputListener.onCheckboxInputResult (Dialogs.java:283); the listener is the method reference this::saveAndDisableBackupReminder (BackupsPreferencesFragment.java:102)',
  evidence='SRC ui/dialogs/Dialogs.java:282-283; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:102,172-177')
e(_B11_DG + 'lambda$showCheckboxDialog$10', _B11_BP + 'saveAndDisableBackupReminder', 'CALL',
  'the Yes answer is passed to saveAndDisableBackupReminder(true): the reminder is turned off',
  cls='non_standard', via='interface callback: Dialogs.CheckboxInputListener.onCheckboxInputResult (Dialogs.java:285); the listener is the method reference this::saveAndDisableBackupReminder (BackupsPreferencesFragment.java:102)',
  guard='the Yes button is enabled only when the checkbox is ticked (Dialogs.java:294-300)',
  evidence='SRC ui/dialogs/Dialogs.java:284-285; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:102,172-177')

# location and backup trigger rows: each calls the folder or file picker, or runs the backup now
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$9', 'Tap Backups location (pref_backups_location)',
    guard='the row is visible only when backups are on (BackupsPreferencesFragment.java:208)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:142-150')
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$10', 'Tap Backup trigger (pref_backups_trigger) to back up now',
    guard='the row is visible only when backups are on (BackupsPreferencesFragment.java:209); the backup runs only when backups are on (:154)',
    needs_state=ST_VAULT_ENCRYPTED,
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:153-159,197-199,209')

# versioning row: opens the strategy dialog (its callback is $6)
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$7', 'Tap Versioning strategy (pref_versioning_strategy)',
    guard='the row is visible only when backups are on (BackupsPreferencesFragment.java:207)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:114-127')
e(_B11_DG + 'lambda$showBackupsVersioningStrategy$34', _B11_BP + 'lambda$onCreatePreferences$6', 'CALL',
  'the strategy from the dialog is passed back: multiple backups opens the folder picker, single backup creates the file',
  cls='non_standard', via='interface callback: Dialogs.BackupsVersioningStrategyListener.onStrategySelectionResult (Dialogs.java:612-614); the listener is created at BackupsPreferencesFragment.java:116',
  guard='the user taps OK with a strategy chosen that differs from the current one (Dialogs.java:611-615; BackupsPreferencesFragment.java:117-119)',
  evidence='SRC ui/dialogs/Dialogs.java:609-616; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:116-125')

# Android backups switch: the vault must be encrypted; turning it on schedules the Android backup
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$8', 'Turn Android backups (pref_android_backups) on or off',
    guard='the switch is enabled only when the vault is encrypted (BackupsPreferencesFragment.java:203)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:131-138')

# backup versions row: opens the picker; the picked number is passed back (callback $11)
gui(_B11_BP + 'onCreatePreferences', _B11_BP + 'lambda$onCreatePreferences$12', 'Tap Backup versions (pref_backups_versions)',
    guard='the row is visible only when backups are on and the strategy is not single backup (BackupsPreferencesFragment.java:210)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:163-169')
gui(_B11_DG + 'showBackupVersionsPickerDialog', _B11_DG + 'lambda$showBackupVersionsPickerDialog$14', 'Tap OK in the backup versions picker (the picked number goes to the listener)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:345-349')
e(_B11_DG + 'lambda$showBackupVersionsPickerDialog$14', _B11_BP + 'lambda$onCreatePreferences$11', 'CALL',
  'the picked number of versions is saved and the summary is refreshed',
  cls='non_standard', via='interface callback: Dialogs.NumberInputListener.onNumberInputResult (Dialogs.java:348); the listener is created at BackupsPreferencesFragment.java:164-167',
  evidence='SRC ui/dialogs/Dialogs.java:345-349; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:164-167')

# the folder or file picker returns to Aegis through backupsResultLauncher (RESULT); the launch comes from createBackupFile or selectBackupsLocation
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)', _B11_BP + 'lambda$new$0', 'RESULT',
  'the backup picker returns to Aegis: the launcher runs onSelectBackupsLocationResult with the result code and the URI',
  env=ENV_BACKUP_RESULT,
  guard='the launch came from createBackupFile or selectBackupsLocation (BackupsPreferencesFragment.java:260,270); the location is saved only when the result is OK and a URI is returned (:181-183)',
  evidence=FW_LAUNCHER + '; SRC ui/fragments/preferences/BackupsPreferencesFragment.java:41-48,260,270')

# --- batch 12 (security page): each row is a tap or a switch change (gui from onCreatePreferences). Dialogs created in a row lambda
# are wired from that lambda (the dialog buttons and items); a dialog answer that the Dialogs class passes back to a row listener is
# an interface callback (cls='non_standard'). Biometric success is a framework callback (FW_BIOPROMPT, ENV_BIOMETRIC).
FW_STREAM = ('INFERRED java.util.stream: a terminal toArray runs the map lambda and the array factory while the statement '
             'executes (JDK source not read)')
FW_CANCEL = ('INFERRED androidx.appcompat AlertDialog: a cancel (Back or a tap outside) calls the OnCancelListener set with '
             'setOnCancelListener (AppCompat source not read)')
_B12_SF = 'SecurityPreferencesFragment.'
_B12_DG = 'Dialogs.'
_B12_TIDLG = 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)'

gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$0', 'Turn Secure screen (pref_secure_screen) on or off (the window gets or loses FLAG_SECURE)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:60-69')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$2', 'Tap Tap to reveal time (pref_tap_to_reveal_time)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:71-79')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$4', 'Turn Encryption (pref_encryption) on or off: on opens the set-password dialog, off asks to confirm',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:81-108')
e(_B12_SF + 'lambda$onCreatePreferences$4', 'Dialogs.showSetPasswordDialog', 'CALL',
  'the Encryption switch is turned on: the set-password dialog opens', needs_state=ST_ENCRYPTION_OFF,
  guard='the vault is not encrypted yet (SecurityPreferencesFragment.java:83)',
  evidence='SRC ui/fragments/preferences/SecurityPreferencesFragment.java:83-84')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$5', 'Turn Biometrics (pref_biometrics) on or off: on starts the biometric prompt, off removes the slot',
    guard='the row is enabled only when biometrics are available and at most one biometric slot exists (SecurityPreferencesFragment.java:277)',
    needs_state=ST_BIOMETRICS_AVAILABLE,
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:110-143')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$6', 'Tap Password (pref_password) to change the master password',
    guard='the row is enabled only when encrypted and at most one password slot exists (SecurityPreferencesFragment.java:262,276)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:145-149')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$9', 'Turn Pin keyboard (pref_pin_keyboard) on: asks for the password to confirm the digits-only pin',
    guard='the pin keyboard switch is turned on (SecurityPreferencesFragment.java:153-155); the switch is visible only when the vault is encrypted (SecurityPreferencesFragment.java:259, 265; preferences_security.xml:86 android:dependency="pref_encryption")',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:151-177,259-265')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$12', 'Tap Auto-lock (pref_auto_lock)',
    guard='the row is visible only when encrypted (SecurityPreferencesFragment.java:264)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:179-207')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$16', 'Tap Password reminder frequency (pref_password_reminder_freq)',
    guard='the row is visible only when a biometric slot exists (SecurityPreferencesFragment.java:279)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:209-230')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$17', 'Turn Backup password (pref_backup_password) on or off: on sets the password, off removes the backup slots',
    guard='the row is shown only when encrypted (SecurityPreferencesFragment.java:266)',
    evidence=FW_PREF_CHANGE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:232-249')
gui(_B12_SF + 'onCreatePreferences', _B12_SF + 'lambda$onCreatePreferences$18', 'Tap Change backup password (pref_backup_password_change)',
    guard='the row is visible only when a backup password is set (SecurityPreferencesFragment.java:268) and enabled at most for one backup password slot (:280)',
    evidence=FW_PREF + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:251-255')

# encryption row: the disable dialog is created in $4; its Yes button is $3
gui(_B12_SF + 'lambda$onCreatePreferences$4', _B12_SF + 'lambda$onCreatePreferences$3', 'Tap Yes in the disable-encryption dialog: the vault is decrypted and the backups are turned off',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:86-104')

# auto-lock dialog (created in $12): multi-choice item $10, OK $11
gui(_B12_SF + 'lambda$onCreatePreferences$12', _B12_SF + 'lambda$onCreatePreferences$10', 'Tick or untick an auto-lock type in the multi-choice list (the list is kept in checkedItems)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:189-191')
gui(_B12_SF + 'lambda$onCreatePreferences$12', _B12_SF + 'lambda$onCreatePreferences$11', 'Tap OK in the auto-lock dialog: the ticked types are saved as the auto-lock mask',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:192-202')

# password-reminder dialog (created in $16): the stream lambdas $13 (map) and $14 (array factory) run inside $16; the single-choice item is $15
e(_B12_SF + 'lambda$onCreatePreferences$16', _B12_SF + 'lambda$onCreatePreferences$13', 'FRAMEWORK',
  'the reminder names are built: the map lambda runs for each frequency while the statement executes',
  evidence=FW_STREAM + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:214-215')
e(_B12_SF + 'lambda$onCreatePreferences$16', _B12_SF + 'lambda$onCreatePreferences$14', 'FRAMEWORK',
  'the reminder names are collected into an array: the array factory runs at the end of the stream',
  evidence=FW_STREAM + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:216')
gui(_B12_SF + 'lambda$onCreatePreferences$16', _B12_SF + 'lambda$onCreatePreferences$15', 'Pick a reminder frequency in the single-choice list (the summary updates and the dialog closes)',
    evidence=FW_CHOICE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:218-226')

# pin keyboard (row $9): the password input dialog is shown by $9 (auto CALL); its OK is Dialogs $7 and its cancel is the dismiss listener $8
gui(_B12_TIDLG, _B12_DG + 'lambda$showTextInputDialog$8', 'The password dialog is shown: its show listener disables OK until the input is not empty',
    evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-231')
gui(_B12_DG + 'lambda$showTextInputDialog$6', _B12_DG + 'lambda$showTextInputDialog$7', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='OK is enabled only when the input is not empty (Dialogs.java:8-12,33-36)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-241')
# pin-keyboard variant of the password dialog (SecurityPreferencesFragment.java:157-162). The shared
# showTextInputDialog $7 is split by caller: only the dialog opened by the PIN keyboard reaches the
# pin-keyboard listener. The AegisImporter dialog stays on the plain chain and reaches the Aegis lambda,
# never this listener. The plain PWD5->TIDLG delegation is an auto edge, and the hand variant delegation
# below suppresses it (base-pair rule), so the plain delegation is re-written by hand to keep the other
# password dialogs (Aegis, Stratum, TwoFAS, FreeOTP) on the plain chain.
_PWD5_SEC = 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@SECURITY'
_TIDLG_SEC = 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@SECURITY'
e(_B12_SF + 'lambda$onCreatePreferences$9', _PWD5_SEC, 'CALL',
  'the PIN keyboard password dialog opens (Security dialog instance)',
  guard='the dialog was opened by the PIN keyboard (SecurityPreferencesFragment.java:157-162)',
  evidence='SRC ui/fragments/preferences/SecurityPreferencesFragment.java:157')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:271 (bytecode)')
e(_PWD5_SEC, _TIDLG_SEC, 'CALL', 'Direct call', evidence='SRC Dialogs.java:271 (bytecode)')
gui(_TIDLG_SEC, 'Dialogs.lambda$showTextInputDialog$8@SECURITY', 'The password dialog is shown: its show listener disables OK until the input is not empty',
    evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-231')
gui('Dialogs.lambda$showTextInputDialog$8@SECURITY', 'Dialogs.lambda$showTextInputDialog$6@SECURITY',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@SECURITY', 'Dialogs.lambda$showTextInputDialog$7@SECURITY', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='OK is enabled only when the input is not empty (Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@SECURITY', _B12_SF + 'lambda$onCreatePreferences$7', 'CALL',
  'the typed password is passed to the pin-keyboard listener: the digits-only check runs, then the password is decrypted in a background task',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at SecurityPreferencesFragment.java:157',
  guard='the dialog was opened by the PIN keyboard (SecurityPreferencesFragment.java:157-162)',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:157-162')
gui(_TIDLG_SEC, _B12_SF + 'lambda$onCreatePreferences$8', 'Cancel the password dialog (Back or a tap outside): the dismiss listener unticks the pin keyboard',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:24-26; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:173-175')
gui(_B12_TIDLG, _B12_SF + 'lambda$onCreatePreferences$8', 'Cancel the password dialog (Back or a tap outside): the dismiss listener unticks the pin keyboard',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:24-26; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:173-175')

# tap to reveal (row $2): the timeout picker is shown by $2 (auto CALL); its OK is Dialogs $13, which passes the number back to $1
gui(_B12_DG + 'showTapToRevealTimeoutPickerDialog', _B12_DG + 'lambda$showTapToRevealTimeoutPickerDialog$13', 'Tap OK in the tap-to-reveal timeout picker (the number goes to the listener)',
    evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:315-317')
e(_B12_DG + 'lambda$showTapToRevealTimeoutPickerDialog$13', _B12_SF + 'lambda$onCreatePreferences$1', 'CALL',
  'the picked number of seconds is saved and the summary is refreshed',
  cls='non_standard', via='interface callback: Dialogs.NumberInputListener.onNumberInputResult (Dialogs.java:317); the listener is the lambda at SecurityPreferencesFragment.java:74-77',
  evidence='SRC ui/dialogs/Dialogs.java:315-317; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:74-77')

e(_B12_SF + 'lambda$onCreatePreferences$5', 'BiometricSlotInitializer.authenticate', 'CALL',
  'the biometric row starts the biometric prompt to add a new biometric slot',
  guard='biometrics are available and no biometric slot exists yet (SecurityPreferencesFragment.java:115-116); the prompt starts at line 122',
  evidence='SRC ui/fragments/preferences/SecurityPreferencesFragment.java:111-122')
# biometric (row $5): the prompt runs in BiometricSlotInitializer; success is the framework callback onAuthenticationSucceeded, which
# passes the cipher to the listener. The sensor step is a device condition (ENV_BIOMETRIC).
e('BiometricSlotInitializer.authenticate', 'BiometricSlotInitializer.onAuthenticationSucceeded', 'FRAMEWORK',
  'the biometric prompt is shown and the sensor accepts the fingerprint or face: the library calls onAuthenticationSucceeded',
  env=ENV_BIOMETRIC,
  evidence=FW_BIOPROMPT + '; SRC helpers/BiometricSlotInitializer.java:45-77,122-124')
e('BiometricSlotInitializer.onAuthenticationSucceeded', 'SecurityPreferencesFragment$RegisterBiometricsListener.onInitializeSlot', 'CALL',
  'the cipher from the biometric prompt is passed to the listener: the biometric slot is added and the vault saved',
  cls='non_standard', via='interface callback: BiometricSlotInitializer.Listener.onInitializeSlot (BiometricSlotInitializer.java:124); the listener is SecurityPreferencesFragment.RegisterBiometricsListener (created at SecurityPreferencesFragment.java:117)',
  evidence='SRC helpers/BiometricSlotInitializer.java:122-124; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:117,401-415')

# --- batch 13: IconPacksManagerFragment (the icon packs sub-page), its Hilt base, IconPackAdapter and IconPackHolder.
# The fragment is opened by PreferencesActivity.onPreferenceStartFragment through reflection (batch 8, _B8_ROWS). The app's own calls
# (onViewCreated, the import chain, the Hilt inject chain and the Dagger inject methods) already have auto_calls rows, so only the
# framework, lambda, callback and generated-base edges are written here.
FW_ATTACH = ('INFERRED androidx.fragment: a committed transaction attaches the fragment and calls its onAttach '
             '(androidx source not cached)')
FW_VIEW = ('INFERRED androidx.fragment: an attached fragment with a layout id (IconPacksManagerFragment.java:65) gets its view from '
           'that layout, then onViewCreated runs (androidx source not cached)')
FW_SCROLL = ('INFERRED androidx.recyclerview: RecyclerView calls each OnScrollListener.onScrolled while the list moves '
             '(androidx source not cached)')
FW_ROWS = ('INFERRED androidx.recyclerview: RecyclerView creates and binds the row views of an adapter after its data changes '
           '(androidx source not cached)')

# lifecycle of the fragment (plain Fragment, not a PreferenceFragmentCompat: no onCreatePreferences)
e('IconPacksManagerFragment.<init>', 'Hilt_IconPacksManagerFragment.onAttach(Context)', 'LIFECYCLE',
  'the icon packs page is attached after its transaction commits', evidence=FW_ATTACH + '; ' + FW_HILT)
e('IconPacksManagerFragment.<init>', 'Hilt_IconPacksManagerFragment.onGetLayoutInflater', 'LIFECYCLE',
  'the view is created: the framework asks the Hilt base for the layout inflater first',
  evidence='INFERRED androidx.fragment: Fragment.performGetLayoutInflater calls onGetLayoutInflater before the view is created (androidx source not cached); generated Hilt_IconPacksManagerFragment not in source tree')
e('IconPacksManagerFragment.<init>', 'IconPacksManagerFragment.onViewCreated', 'LIFECYCLE',
  'the view is created from the layout, then onViewCreated builds the page',
  evidence=FW_VIEW + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:65,69')
e('Hilt_IconPacksManagerFragment.onAttach(Context)', 'Hilt_IconPacksManagerFragment.onAttach(Activity)', 'FRAMEWORK',
  'Fragment.onAttach(Context) calls the onAttach(Activity) overload when the host is an activity',
  evidence='INFERRED androidx.fragment Fragment.onAttach(Context) (framework source not read); generated Hilt_IconPacksManagerFragment not in source tree')
e('IconPacksManagerFragment.onViewCreated', 'Hilt_IconPacksManagerFragment.getContext', 'FRAMEWORK',
  'requireContext() (line 91) returns getContext(), which the Hilt base overrides to set up its component context',
  evidence='INFERRED androidx.fragment Fragment.requireContext calls the overridable getContext() (androidx source not read); SRC ui/fragments/preferences/IconPacksManagerFragment.java:91')

# the view: the add button, its window insets, the list scroll, the list rows and the picker result
gui('IconPacksManagerFragment.onViewCreated', 'IconPacksManagerFragment.lambda$onViewCreated$1',
    'Tap the add floating button (the system file picker opens)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:70-71')
e('IconPacksManagerFragment.onViewCreated', 'IconPacksManagerFragment.lambda$onViewCreated$2', 'FRAMEWORK',
  'the window insets are dispatched to the add button: the listener moves it clear of the system bars',
  evidence=FW_INSETS + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:75-85')
e('IconPacksManagerFragment.onViewCreated', 'IconPacksManagerFragment$1.onScrolled', 'FRAMEWORK',
  'the user scrolls the icon pack list: RecyclerView calls the scroll listener added at line 95',
  evidence=FW_SCROLL + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:95-101')
e('IconPackAdapter.addIconPack', 'IconPackAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the notify call in addIconPack asks RecyclerView to create the row view of the new icon pack',
  evidence=FW_ROWS + '; SRC ui/views/IconPackAdapter.java:25-33,46-49')
e('IconPackAdapter.addIconPack', 'IconPackAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView binds the new row to its icon pack after the notify call',
  evidence=FW_ROWS + '; SRC ui/views/IconPackAdapter.java:25-33,52-57')
gui('IconPackAdapter.onBindViewHolder', 'IconPackAdapter.lambda$onBindViewHolder$0',
    'Tap the delete button of an icon pack row (the remove dialog opens)',
    evidence=FW_CLICK + '; SRC ui/views/IconPackAdapter.java:54-57; SRC ui/views/IconPackHolder.java:29-31')
gui('IconPacksManagerFragment.onRemoveIconPack', 'IconPacksManagerFragment.lambda$onRemoveIconPack$3',
    'Tap Yes in the remove icon pack dialog (the pack is removed)',
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:122-130' + '; SRC ui/dialogs/Dialogs.java:66-69; AndroidX/Material AlertDialog positive-button dispatch (library, not on disk)')

# the sub-page slide animation (the sub-page transaction sets custom animations, PreferencesActivity.java:92-96)
e('PreferencesActivity.showFragment', 'IconPacksManagerFragment.onCreateAnimation', 'FRAMEWORK',
  'the icon packs sub-page transaction has slide animations: the fragment supplies them (its own override)',
  guard='the transaction has custom animations, so nextAnim is not 0 (PreferencesActivity.java:92-96; IconPacksManagerFragment.java:113)',
  evidence=FW_ANIM + '; SRC ui/PreferencesActivity.java:92-96; SRC ui/fragments/preferences/IconPacksManagerFragment.java:112-117')

# the file picker result (ACTION_GET_CONTENT) runs the launcher callback, which imports the picked file
e('VaultManager.fireIntentLauncher(Fragment,Intent,ActivityResultLauncher)', 'IconPacksManagerFragment.lambda$new$0', 'RESULT',
  'the file picker returns a file: the launcher callback imports the icon pack', env=ENV_PICKER_ICON,
  evidence=FW_LAUNCHER + '; SRC vault/VaultManager.java:263-269; SRC ui/fragments/preferences/IconPacksManagerFragment.java:56-62,175')
e('IconPacksManagerFragment.lambda$new$0', 'IconPacksManagerFragment.importIconPack', 'CALL',
  'the picked file is imported: the launcher callback calls importIconPack',
  guard='RESULT_OK && data != null && data.getData() != null (IconPacksManagerFragment.java:59)',
  evidence='SRC ui/fragments/preferences/IconPacksManagerFragment.java:55-62')

# the import runs in a background AsyncTask; its result goes to the callback lambda (interface Callback, not a direct call)
e('IconPacksManagerFragment.importIconPack', 'ImportIconPackTask.doInBackground', 'ASYNC',
  'the icon pack is copied and imported on a background thread',
  note='ProgressDialogTask.execute at IconPacksManagerFragment.java:155 runs unconditionally, so doInBackground runs for every import.',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC ui/fragments/preferences/IconPacksManagerFragment.java:133-155; SRC ui/tasks/ImportIconPackTask.java:17,26')
e('ImportIconPackTask.doInBackground', 'IconPackManager.importPack', 'CALL', 'the ZIP is parsed and the pack is imported (refused when it is already installed)',
  evidence='SRC ui/tasks/ImportIconPackTask.java:41')
e('IconPackManager.importPack', 'IconPackExistsException.<init>', 'CALL', 'the pack is refused: its directory exists or its UUID is already installed',
  guard='packDir.exists() (IconPackManager.java:84) or getIconPackByUUID(UUID) != null (IconPackManager.java:87-89)',
  evidence='SRC icons/IconPackManager.java:84-90')

# G5 (stage 2): the pack load in rescanIconPacks carries its guard (this hand edge replaces the auto row for the pair)
e('IconPackManager.rescanIconPacks', 'IconPack.fromBytes', 'CALL', 'each pack folder with a UUID name and a readable definition file is parsed at startup',
  guard='the icons dir lists files, the entry is a directory with a UUID name, its latest version dir is non-null, and the pack definition file opens (IconPackManager.java:136-158)',
  needs_state=ST_ICON_PACK_INSTALLED,
  evidence='SRC icons/IconPackManager.java:136-158 (bytecode line 158)')
# stage 3 round 3, batch 1b (G5 route check): guards and states on auto CALL rows (a hand edge on the same pair replaces the auto row)
e('IconPack.fromJson', 'IconPack$Icon.fromJson', 'CALL', 'each icon of the pack is parsed from its JSON entry',
  guard='the icons array has at least one entry: the for loop runs (IconPack.java:120)',
  evidence='SRC icons/IconPack.java:117,120-121')
e('SlotList.fromJson', 'Slot.fromJson', 'CALL', 'each slot of the slot list is parsed from its JSON entry',
  guard='the slots array has at least one entry: the for loop at SlotList.java:27 runs',
  evidence='SRC vault/slots/SlotList.java:27-29')
e('Slot.fromJson', 'RawSlot.<init>(UUID,byte[],CryptParameters)', 'CALL', 'a raw slot is built from the slot JSON',
  guard='the slot type is TYPE_RAW (switch case at Slot.java:132)',
  evidence='SRC vault/slots/Slot.java:131-133')
e('MainActivity.onStart', 'VaultRepository.readVaultFile', 'CALL', 'the vault file is read in onStart (the vault is not loaded yet and the intro is not needed)',
  guard='the vault is not loaded yet in this process and the intro is not needed (MainActivity.java:942-951)', needs_state=ST_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:942-954')
e('VaultRepository.readVaultFile', 'VaultFile.fromBytes', 'CALL', 'the file bytes are parsed into a vault file',
  needs_state=ST_VAULT_FILE,
  evidence='SRC vault/VaultRepository.java:65-70')
e('EntryAdapter.calculateShownEntries', 'EntryAdapter.isEntryFiltered', 'CALL', 'each entry is tested by the search filter and kept when it is not filtered out',
  guard='the entries list has at least one entry: the for loop runs (EntryAdapter.java:301)', needs_state=ST_ENTRY_LIST_NONEMPTY,
  evidence='SRC ui/views/EntryAdapter.java:280; SRC ui/views/EntryAdapter.java:299-302')
# stage 3 round 3, batch 2 (route check): new hand edges that replace auto rows, each with its guard (source confirmed)
e('MainActivity.onStart', 'MainActivity.doShortcutActions', 'CALL', 'the shortcut actions run at the end of onStart',
  needs_state=ST_VAULT_FILE,
  guard='vault init not needed: isVaultInitNeeded() is false (MainActivity.java:942), so the return at 947 (inside the vault-init branch, 942-948) is not taken; the error returns at 960 and 971 are not taken (the call is at 1006)',
  evidence='SRC ui/MainActivity.java:942-948,957-960,966-971,1006')
e('MainActivity.startEditEntryActivity()', 'MainActivity.startEditEntryActivityForManual', 'CALL', 'no usable clipboard URI: the manual entry page opens',
  guard='the clipboard holds no text (readText returns null, MainActivity.java:476) or the text is not an otpauth URI (parseUri throws GoogleAuthInfoException, caught at 494-496)',
  evidence='SRC ui/MainActivity.java:475-476,494-499')
e('MainActivity.onAddEntryResult', 'EntryListView.onEntryAdded', 'CALL', 'the new entry is shown in the list at once',
  guard='the list is loaded: _loaded is true (MainActivity.java:619)',
  evidence='SRC ui/MainActivity.java:618-623')
e('FabMenuHelper.toggle', 'FabMenuHelper.open', 'CALL', 'the closed floating menu is opened by toggle',
  guard='_isOpen is false: the else branch of toggle (FabMenuHelper.java:69-73)',
  evidence='SRC helpers/FabMenuHelper.java:68-74')
e('EntryHolder.setShowProgress', 'EntryHolder.startRefreshLoop', 'CALL', 'a row with a progress bar starts its refresh loop',
  guard='showProgress is true and the entry is not HOTP (EntryHolder.java:245-252); showProgress is true only when this row period differs from the most frequent period (EntryAdapter.java:585-588), and with one TOTP-family entry that period is its own (EntryAdapter.java:605-608), so the state needs a second TOTP-family entry with another period',
  evidence='SRC ui/views/EntryHolder.java:245-256; SRC ui/views/EntryAdapter.java:585-588,605-608')
e('AuthyImporter$EncryptedState.lambda$decrypt$0', 'ImportEntriesActivity$2.onStateDecrypted', 'CALL', 'the password decrypts the Authy backup: the decrypted state is passed on',
  guard='decrypt(password) does not throw (AuthyImporter.java:209; the catch at 211-212 calls onError instead)',
  evidence='SRC importers/AuthyImporter.java:206-212')

# Authy-caller variant of the password dialog (AuthyImporter.java:207-214). Only the dialog opened by
# AuthyImporter.decrypt reaches the Authy lambda; the Security dialog reaches only the Security listener
# via @SECURITY. Authy is the sole caller of the 4-argument showPasswordInputDialog overload, so its plain
# delegation is re-written by hand here (same base-pair suppression as @SECURITY above).
_PWD4_AUTHY = 'Dialogs.showPasswordInputDialog(Context,int,TextInputListener,OnCancelListener)@AUTHY'
_TIDLG_AUTHY = 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@AUTHY'
e('AuthyImporter$EncryptedState.decrypt(Context,DecryptListener)', _PWD4_AUTHY, 'CALL',
  'the Authy password dialog opens (Authy dialog instance)',
  guard='the dialog was opened by AuthyImporter.decrypt (AuthyImporter.java:207-214)',
  evidence='SRC importers/AuthyImporter.java:207')
e('Dialogs.showPasswordInputDialog(Context,int,TextInputListener,OnCancelListener)', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:267 (bytecode)')
e(_PWD4_AUTHY, _TIDLG_AUTHY, 'CALL', 'Direct call', evidence='SRC Dialogs.java:267 (bytecode)')
gui(_TIDLG_AUTHY, 'Dialogs.lambda$showTextInputDialog$8@AUTHY', 'The password dialog is shown: its show listener disables OK until the input is not empty',
    evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-231')
gui('Dialogs.lambda$showTextInputDialog$8@AUTHY', 'Dialogs.lambda$showTextInputDialog$6@AUTHY',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@AUTHY', 'Dialogs.lambda$showTextInputDialog$7@AUTHY', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='OK is enabled only when the input is not empty (Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@AUTHY', 'AuthyImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/AuthyImporter.java:207-214',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/AuthyImporter.java:207-214')
gui(_TIDLG_AUTHY, 'AuthyImporter$EncryptedState.lambda$decrypt$1', 'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/AuthyImporter.java:214')
e('IconPackExistsException.<init>', 'ImportIconPackTask.doInBackground', 'CALL',
  'the exception is caught in doInBackground and returned as the task result (Result(null, e))',
  guard='the exception thrown by importPack is caught (ImportIconPackTask.java:43-45) and returned as the result',
  evidence='SRC ui/tasks/ImportIconPackTask.java:43-45')
e('ImportIconPackTask.doInBackground', 'ImportIconPackTask.onPostExecute', 'ASYNC',
  'the result is posted to the main thread', evidence=FW_ASYNC + '; SRC ui/tasks/ImportIconPackTask.java:26,54')
e('ImportIconPackTask.onPostExecute', 'IconPacksManagerFragment.lambda$importIconPack$5', 'CALL',
  'the import result reaches the callback: a new pack is added, an exists error asks to replace it, any other error shows the error dialog',
  evidence='SRC ui/tasks/ImportIconPackTask.java:54-61; SRC ui/fragments/preferences/IconPacksManagerFragment.java:134-154')
gui('IconPacksManagerFragment.lambda$importIconPack$5', 'IconPacksManagerFragment.lambda$importIconPack$4',
    'Tap Yes in the icon pack exists dialog (the old pack is removed, then the import runs again)',
    guard='the import failed with IconPackExistsException (IconPacksManagerFragment.java:136-137)', needs_state=ST_ICON_PACK_INSTALLED,
    evidence=FW_CLICK + '; SRC ui/fragments/preferences/IconPacksManagerFragment.java:137-147')

# generated Hilt base and Dagger parts that no app code calls (one group per kind)
UNREACHABLE['Hilt_IconPacksManagerFragment.<init>()'] = ('no_trigger_in_app',
    'generated no-argument constructor of the Hilt base: IconPacksManagerFragment.java:65 calls super(R.layout.fragment_icon_packs), which selects '
    'Hilt_IconPacksManagerFragment(int), so this constructor has no caller', 'ui/fragments/preferences/IconPacksManagerFragment.java:65', 'INFERRED')
UNREACHABLE['_com_beemdevelopment_aegis_ui_fragments_preferences_IconPacksManagerFragment_GeneratedInjector.<init>'] = ('no_trigger_in_app',
    'generated Hilt entry point class of IconPacksManagerFragment: no app source names it and no auto_calls row calls its constructor, so nothing runs it',
    'ui/fragments/preferences/IconPacksManagerFragment.java:43', 'INFERRED')
UNREACHABLE['Hilt_IconPacksManagerFragment.getDefaultViewModelProviderFactory'] = ('framework_never_calls',
    'the Hilt override supplies the ViewModel factory only when a ViewModel is requested (viewModels() or a ViewModelProvider); '
    'IconPacksManagerFragment.java requests none (whole file, 1-187)', 'ui/fragments/preferences/IconPacksManagerFragment.java:44-187', 'INFERRED')

# batch 13, icon pack model: the manager's stream filter, the list-removal equality and the two model methods with no caller.
# IconPack$Icon.getName stays a frontier for the icon picker cluster (IconHolder.java:37 calls it).
e('IconPackManager.getIconPackByUUID', 'IconPackManager.lambda$getIconPackByUUID$0', 'FRAMEWORK',
  'the stream runs the filter lambda for each icon pack while the list is collected (a terminal collect)',
  evidence='INFERRED java.util.stream: a terminal collect runs the filter for each element while the statement executes (JDK source not read); SRC icons/IconPackManager.java:37-38')
e('IconPackAdapter.removeIconPack', 'IconPack.equals', 'FRAMEWORK',
  'the adapter finds the row of the removed pack: ArrayList.indexOf compares each pack with equals',
  evidence='INFERRED java.util.ArrayList.indexOf calls equals on each element (JDK source not read); SRC ui/views/IconPackAdapter.java:36-37; SRC icons/IconPack.java:93-99')
UNREACHABLE['IconPack.getDirectory'] = ('no_trigger_in_app',
    'no app code calls IconPack.getDirectory: a grep of the whole app tree finds only its declaration', 'icons/IconPack.java:79', 'SOURCE')
UNREACHABLE['IconPack.hashCode'] = ('no_trigger_in_app',
    'no hash-based collection holds IconPack: the packs are kept in lists (IconPackManager.java:28-31, IconPackAdapter.java:18), and a grep of the app tree finds no HashSet, HashMap or Set/Map of IconPack',
    'icons/IconPack.java:103-104', 'SOURCE')

# --- batch 14: AuditLogPreferencesFragment (the audit log sub-page), its adapter and item decoration, the repository executor and the Room DAO path.
# The fragment is opened by reflection (batch 8, _B8_ROWS). The app's own calls (onViewCreated, the repository, the DAO, the holder and the
# adapter bind) already have auto_calls rows, so only the framework, lambda, executor, Room-generated and Hilt-base edges are written here.
FW_DECOR = ('INFERRED androidx.recyclerview: RecyclerView calls getItemOffsets of each ItemDecoration added with addItemDecoration, '
            'while it lays out the rows (androidx source not cached)')
FW_LIVE = ('INFERRED androidx.lifecycle: LiveData.observe calls the observer with the current value once the owner is started, '
           'and again on each change (androidx source not cached)')

# lifecycle of the fragment (plain Fragment with a layout id; the Hilt base is generated and absent from the source tree)
e('AuditLogPreferencesFragment.<init>', 'Hilt_AuditLogPreferencesFragment.onAttach(Context)', 'LIFECYCLE',
  'the audit log page is attached after its transaction commits',
  evidence=FW_ATTACH + '; generated Hilt_AuditLogPreferencesFragment not in source tree (same pattern as FW_HILT, graph_def.py:1164)')
e('AuditLogPreferencesFragment.<init>', 'Hilt_AuditLogPreferencesFragment.onGetLayoutInflater', 'LIFECYCLE',
  'the view is created: the framework asks the Hilt base for the layout inflater first',
  evidence='INFERRED androidx.fragment: Fragment.performGetLayoutInflater calls onGetLayoutInflater before the view is created (androidx source not cached); generated Hilt_AuditLogPreferencesFragment not in source tree')
e('AuditLogPreferencesFragment.<init>', 'AuditLogPreferencesFragment.onViewCreated', 'LIFECYCLE',
  'the view is created from the layout, then onViewCreated builds the page',
  evidence='INFERRED androidx.fragment: an attached fragment with a layout id gets its view from that layout, then onViewCreated runs (androidx source not cached); SRC ui/fragments/preferences/AuditLogPreferencesFragment.java:48,52')
e('Hilt_AuditLogPreferencesFragment.onAttach(Context)', 'Hilt_AuditLogPreferencesFragment.onAttach(Activity)', 'FRAMEWORK',
  'Fragment.onAttach(Context) calls the onAttach(Activity) overload when the host is an activity',
  evidence='INFERRED androidx.fragment Fragment.onAttach(Context) (framework source not read); generated Hilt_AuditLogPreferencesFragment not in source tree')
e('AuditLogPreferencesFragment.onViewCreated', 'Hilt_AuditLogPreferencesFragment.getContext', 'FRAMEWORK',
  'requireContext() (line 58) returns getContext(), which the Hilt base overrides to set up its component context',
  evidence='INFERRED androidx.fragment Fragment.requireContext calls the overridable getContext() (androidx source not read); SRC ui/fragments/preferences/AuditLogPreferencesFragment.java:58')

# the view: the window insets listener (line 64), the entries observer (line 75) and the row spacing decoration (line 59)
e('AuditLogPreferencesFragment.onViewCreated', 'AuditLogPreferencesFragment.lambda$onViewCreated$0', 'FRAMEWORK',
  'the window insets are dispatched to the list: the listener sets the bottom padding to clear the system bars',
  evidence=FW_INSETS + '; SRC ui/fragments/preferences/AuditLogPreferencesFragment.java:64-73')
e('AuditLogPreferencesFragment.onViewCreated', 'AuditLogPreferencesFragment.lambda$onViewCreated$1', 'FRAMEWORK',
  'the entries LiveData gives its value to the observer when the view is started, and again on each change',
  evidence=FW_LIVE + '; SRC ui/fragments/preferences/AuditLogPreferencesFragment.java:75-90')
e('AuditLogPreferencesFragment.onViewCreated', 'AuditLogPreferencesFragment$SpacesItemDecoration.getItemOffsets', 'FRAMEWORK',
  'the list lays out its rows: RecyclerView asks the decoration added at line 59 for the spacing of each row',
  evidence=FW_DECOR + '; SRC ui/fragments/preferences/AuditLogPreferencesFragment.java:59,101-109')

# the adapter: the notify call in addAuditLogEntryModel makes RecyclerView create and bind the row
e('AuditLogAdapter.addAuditLogEntryModel', 'AuditLogAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the notify call in addAuditLogEntryModel asks RecyclerView to create the row view of the new entry',
  evidence=FW_ROWS + '; SRC ui/views/AuditLogAdapter.java:28-37,43-48')
e('AuditLogAdapter.addAuditLogEntryModel', 'AuditLogAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView binds the new row to its entry after the notify call',
  evidence=FW_ROWS + '; SRC ui/views/AuditLogAdapter.java:28-37,50-56')

# the repository writes on its single background thread; the Room DAO code is generated (not in the source tree), so its edges are INFERRED
e('AuditLogRepository.insert', 'AuditLogRepository.lambda$insert$0', 'ASYNC',
  'the write runs on the repository single background thread, not on the caller thread',
  evidence='INFERRED java.util.concurrent: Executor.execute runs the Runnable on the executor thread (JDK source not read); SRC database/AuditLogRepository.java:17,60-63')
e('AuditLogDao_Impl.insert', 'AuditLogDao_Impl.lambda$insert$0', 'FRAMEWORK',
  'the generated insert runs its body (the insertion adapter) through the Room transaction helper',
  evidence='INFERRED androidx.room: generated AuditLogDao_Impl.java:53 creates the lambda inside insert, and Room runs the Runnable in a transaction (Room source not cached)')
e('AuditLogDao_Impl.lambda$insert$0', 'AuditLogDao_Impl$1.bind', 'FRAMEWORK',
  'the insertion adapter binds the entry columns to the insert statement',
  evidence='INFERRED androidx.room EntityInsertionAdapter.insert calls the bind override of the generated adapter (Room source not cached)')
e('AuditLogDao_Impl.lambda$insert$0', 'AuditLogDao_Impl$1.createQuery', 'FRAMEWORK',
  'the insertion adapter asks for its SQL text when it prepares the insert statement',
  evidence='INFERRED androidx.room EntityInsertionAdapter acquires its statement by calling the createQuery override (Room source not cached)')
e('AuditLogDao_Impl.getAll', 'AuditLogDao_Impl.lambda$getAll$1', 'FRAMEWORK',
  'the LiveData runs the query Callable when an observer becomes active: the Callable reads the rows and builds the entries',
  guard='the LiveData has an active observer (AuditLogPreferencesFragment.java:75 adds one)',
  evidence='INFERRED androidx.room createLiveData keeps the Callable and runs it on the query executor when the LiveData becomes active (Room source not cached); generated AuditLogDao_Impl.java:62 creates the lambda')

# generated Hilt base and Dagger entry points with no caller, and one app method with no caller (one group per kind)
UNREACHABLE['Hilt_AuditLogPreferencesFragment.<init>()'] = ('no_trigger_in_app',
    'generated no-argument constructor of the Hilt base: AuditLogPreferencesFragment.java:48 calls super(R.layout.fragment_audit_log), which selects '
    'Hilt_AuditLogPreferencesFragment(int), so this constructor has no caller', 'ui/fragments/preferences/AuditLogPreferencesFragment.java:48', 'INFERRED')
UNREACHABLE['_com_beemdevelopment_aegis_ui_fragments_preferences_AuditLogPreferencesFragment_GeneratedInjector.<init>'] = ('no_trigger_in_app',
    'generated Hilt entry point class of AuditLogPreferencesFragment: no app source names it and no auto_calls row calls its constructor, so nothing runs it',
    'ui/fragments/preferences/AuditLogPreferencesFragment.java:33', 'INFERRED')
UNREACHABLE['Hilt_AuditLogPreferencesFragment.getDefaultViewModelProviderFactory'] = ('framework_never_calls',
    'the Hilt override supplies the ViewModel factory only when a ViewModel is requested (viewModels() or a ViewModelProvider); '
    'AuditLogPreferencesFragment.java requests none (whole file, 1-111)', 'ui/fragments/preferences/AuditLogPreferencesFragment.java:34-111', 'INFERRED')
UNREACHABLE['AuditLogAdapter.addReferencedEntry'] = ('no_trigger_in_app',
    'no app code calls addReferencedEntry: a grep of the app tree finds only its declaration', 'ui/views/AuditLogAdapter.java:39', 'SOURCE')

# --- batch 15: the Hilt base of the settings fragments (onGetLayoutInflater, ViewModel factory), the groups page (GroupManagerActivity)
# and its adapter (GroupAdapter). Only framework, dialog-callback, lambda and generated-base edges are written here; the app's own calls have auto_calls rows.
FW_TOUCH_DRAG = ('INFERRED androidx.recyclerview ItemTouchHelper: attachToRecyclerView registers the touch listener; a touch asks the callback '
                 'for its movement flags, then calls onMove for each drag step (androidx source not cached)')

# the settings fragments share one Hilt base (PreferencesFragment, the class at PreferencesFragment.java:32): onGetLayoutInflater runs before the view
for _cls, _resume in _B8_LIFECYCLE:
    e(_cls + '.<init>', 'Hilt_PreferencesFragment.onGetLayoutInflater', 'LIFECYCLE',
      'the view is created: the framework asks the Hilt base for the layout inflater first (' + _cls + ')',
      evidence='INFERRED androidx.fragment: Fragment.performGetLayoutInflater calls onGetLayoutInflater before the view is created (androidx source not cached); generated Hilt_PreferencesFragment not in source tree')
# no app code requests a ViewModel: a grep of the app tree finds no viewModels() and no ViewModelProvider
UNREACHABLE['Hilt_PreferencesFragment.getDefaultViewModelProviderFactory'] = ('framework_never_calls',
    'the Hilt override supplies the ViewModel factory only when a ViewModel is requested; no app code requests one (grep of the app tree: no viewModels() and no ViewModelProvider)',
    'ui/fragments/preferences/PreferencesFragment.java:32-109', 'INFERRED')

# the groups page: the toolbar menu, the back press (its callback is enabled only after a change), the save and the touch reorder
e('GroupManagerActivity.onCreate', 'GroupManagerActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate',
  evidence=FW_OPTIONS + '; SRC ui/GroupManagerActivity.java:188-192')
gui('GroupManagerActivity.onCreateOptionsMenu', 'GroupManagerActivity.onOptionsItemSelected',
    'Tap a toolbar item: Up (discard), save, or delete the unused groups (a menu tap)',
    evidence=FW_MENU + '; SRC ui/GroupManagerActivity.java:194-208')
gui('GroupManagerActivity.onCreate', 'GroupManagerActivity$BackPressHandler.handleOnBackPressed',
    'Press Back after a change (the discard check runs)',
    guard='the back callback is enabled only after a rename or a removal (GroupManagerActivity.java:121,137,157); with no change the default back closes the page',
    evidence=FW_DISPATCH + '; SRC ui/GroupManagerActivity.java:48-49,220-229')
e('GroupManagerActivity.onCreate', 'GroupManagerActivity.onSaveInstanceState', 'SYSTEM',
  'API 27: the framework saves the instance state when the page is left or the device is rotated (after onPause)',
  evidence=FW_SAVE + '; SRC ui/GroupManagerActivity.java:103-111')
gui('GroupManagerActivity.onCreate', 'GroupManagerActivity$1.getMovementFlags',
    'Touch a group row to reorder it (the helper asks for the allowed directions)',
    evidence=FW_TOUCH_DRAG + '; SRC ui/GroupManagerActivity.java:61-68,90')
gui('GroupManagerActivity.onCreate', 'GroupManagerActivity$1.onMove',
    'Drag a group row up or down (the list is reordered)',
    evidence=FW_TOUCH_DRAG + '; SRC ui/GroupManagerActivity.java:70-78,90')
UNREACHABLE['GroupManagerActivity$1.onSwiped'] = ('framework_never_calls',
    'the helper calls onSwiped only for a swipe, and getMovementFlags allows only the UP and DOWN drag flags with no swipe flags, so no swipe starts',
    'ui/GroupManagerActivity.java:63-68,80-81', 'INFERRED')

# the rename dialog is split by caller (@GROUP): the plain Dialogs $7 never delivers to the rename
# listener, so a rename dialog can no longer reach an importer password lambda (that mix was route 16's
# cheapest false route after the Security/Authy splits). The hand variant delegation below suppresses
# the auto plain TIDLG5->TIDLG8 delegation (base-pair rule), so the plain delegation is re-written by
# hand to keep the other direct text-input dialogs on the plain chain.
e('GroupManagerActivity.onEditGroup', 'Dialogs.showTextInputDialog(Context,int,int,TextInputListener,String)@GROUP', 'CALL', 'Direct call',
  evidence='SRC ui/GroupManagerActivity.java:125 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,TextInputListener,String)', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:243 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,TextInputListener,String)@GROUP', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@GROUP', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:243 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@GROUP', 'Dialogs.lambda$showTextInputDialog$8@GROUP', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@GROUP', 'Dialogs.lambda$showTextInputDialog$6@GROUP',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@GROUP', 'Dialogs.lambda$showTextInputDialog$7@GROUP', 'Tap OK in the input dialog (gives the text to the listener)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@GROUP', 'GroupManagerActivity.lambda$onEditGroup$0', 'CALL',
  'the typed name is passed to the rename listener: the name is trimmed, the group is cloned and replaced in the list',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at GroupManagerActivity.java:115',
  evidence='SRC ui/GroupManagerActivity.java:114-126; SRC ui/dialogs/Dialogs.java:231-241')
gui('GroupManagerActivity.onRemoveGroup', 'GroupManagerActivity.lambda$onRemoveGroup$1',
    'Tap Yes in the remove group dialog (the group is removed from the list)',
    evidence=FW_CLICK + '; SRC ui/GroupManagerActivity.java:130-141')
gui('GroupManagerActivity.onRemoveUnusedGroups', 'GroupManagerActivity.lambda$onRemoveUnusedGroups$2',
    'Tap Yes in the remove unused groups dialog (every unused group is removed from the list)',
    evidence=FW_CLICK + '; SRC ui/GroupManagerActivity.java:145-162' + '; SRC ui/dialogs/Dialogs.java:66-69; AndroidX/Material AlertDialog positive-button dispatch (library, not on disk)')
# the discard dialog (Dialogs.showDiscardDialog passes both listeners to the buttons, Dialogs.java:111-118); it opens only when groups were removed
gui('GroupManagerActivity.discardAndFinish', 'GroupManagerActivity.lambda$discardAndFinish$3',
    'Tap Save in the discard dialog (the groups are saved, then the page closes)',
    guard='groups were removed: the dialog opens only then (GroupManagerActivity.java:178-181)',
    evidence=FW_CLICK + '; SRC ui/GroupManagerActivity.java:177-186; SRC ui/dialogs/Dialogs.java:111-118')
gui('GroupManagerActivity.discardAndFinish', 'GroupManagerActivity.lambda$discardAndFinish$4',
    'Tap Discard in the discard dialog (the page closes without saving)',
    guard='groups were removed: the dialog opens only then (GroupManagerActivity.java:178-181)',
    evidence=FW_CLICK + '; SRC ui/GroupManagerActivity.java:177-186; SRC ui/dialogs/Dialogs.java:111-118')

# the adapter: the add and replace calls make RecyclerView create and bind the rows; the two row buttons are click listeners
e('GroupAdapter.addGroup', 'GroupAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the notify call in addGroup asks RecyclerView to create the row view of the new group',
  evidence=FW_ROWS + '; SRC ui/views/GroupAdapter.java:26-35,54-58')
e('GroupAdapter.addGroup', 'GroupAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView binds the new row to its group after the notify call',
  evidence=FW_ROWS + '; SRC ui/views/GroupAdapter.java:26-35,61-70')
e('GroupAdapter.replaceGroup', 'GroupAdapter.onBindViewHolder', 'FRAMEWORK',
  'notifyItemChanged makes RecyclerView rebind the renamed row',
  evidence=FW_ROWS + '; SRC ui/views/GroupAdapter.java:41-46')
gui('GroupAdapter.onBindViewHolder', 'GroupAdapter.lambda$onBindViewHolder$0',
    'Tap the edit button of a group row (the rename dialog opens)',
    evidence=FW_CLICK + '; SRC ui/views/GroupAdapter.java:63-66; SRC ui/views/GroupHolder.java:28-30')
gui('GroupAdapter.onBindViewHolder', 'GroupAdapter.lambda$onBindViewHolder$1',
    'Tap the delete button of a group row (the remove dialog opens)',
    evidence=FW_CLICK + '; SRC ui/views/GroupAdapter.java:67-70; SRC ui/views/GroupHolder.java:32-34')
# the ItemTouchHelperAdapter callbacks onItemDismiss and onItemDrop have no caller for this adapter: the groups page uses its own callback
# (GroupManagerActivity.java:61-82, onMove only) and SimpleItemTouchHelperCallback is created only with the EntryAdapter (EntryListView.java:141,67)
UNREACHABLE['GroupAdapter.onItemDismiss'] = ('no_trigger_in_app',
    'no app code calls onItemDismiss on a GroupAdapter: the groups page helper calls only onMove (GroupManagerActivity.java:70-78), and the only SimpleItemTouchHelperCallback is built with the EntryAdapter (EntryListView.java:141)',
    'ui/views/GroupAdapter.java:79-80', 'SOURCE')
UNREACHABLE['GroupAdapter.onItemDrop'] = ('no_trigger_in_app',
    'no app code calls onItemDrop on a GroupAdapter: the groups page helper calls only onMove (GroupManagerActivity.java:70-78), and the only SimpleItemTouchHelperCallback is built with the EntryAdapter (EntryListView.java:141)',
    'ui/views/GroupAdapter.java:82-83', 'SOURCE')

# --- batch 16: AboutActivity (the about page). Its onCreate lambdas $0-$9 are tap listeners (FW_CLICK), $10 is the window-insets listener;
# the helpers openUrl, openMail and copyToClipboard are reached by CALL rows from inside those lambdas (auto_calls).
_B16_TAPS = [
    (0, 'Tap the license button (the license dialog opens)', 'SRC ui/AboutActivity.java:53-58'),
    (2, 'Tap the app version (the version is copied to the clipboard)', 'SRC ui/AboutActivity.java:69-72'),
    (3, 'Tap the GitHub row (the project page opens in a browser)', 'SRC ui/AboutActivity.java:74-75'),
    (4, 'Tap the Alexander row (his website opens in a browser)', 'SRC ui/AboutActivity.java:77-78'),
    (5, 'Tap the Michael row (his GitHub page opens in a browser)', 'SRC ui/AboutActivity.java:80-81'),
    (6, 'Tap the e-mail row (a mail app is offered)', 'SRC ui/AboutActivity.java:83-84'),
    (7, 'Tap the website row (the website opens in a browser)', 'SRC ui/AboutActivity.java:86-87'),
    (8, 'Tap the rate row (the Play Store page opens)', 'SRC ui/AboutActivity.java:89-90'),
    (9, 'Tap the changelog button (the changelog dialog opens)', 'SRC ui/AboutActivity.java:92-97'),
]
for _n, _text, _src in _B16_TAPS:
    gui('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$%d' % _n, _text,
        evidence=FW_CLICK + '; ' + _src)
gui('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$1',
    'Tap third-party licenses (the licenses page opens)',
    evidence=FW_CLICK + '; SRC ui/AboutActivity.java:60-64')
e('AboutActivity.lambda$onCreate$1', 'LicensesActivity.<init>', 'INTENT',
  'the button starts the licenses page with an explicit intent',
  evidence='SRC ui/AboutActivity.java:62-63 (explicit Intent to LicensesActivity.class)')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$10', 'FRAMEWORK',
  'the window insets are dispatched: the scroll view gets its bottom padding',
  evidence=FW_INSETS + '; SRC ui/AboutActivity.java:99-108')
gui('AboutActivity.onCreate', 'AboutActivity.onOptionsItemSelected',
    'Tap the Up arrow in the about toolbar (home item): the page closes',
    evidence=FW_MENU + '; SRC ui/AboutActivity.java:45-51,148-159')
# the static URL and address strings are set when the class is first created (JVM class initialization runs before the constructor body)
e('AboutActivity.<init>', 'AboutActivity.<clinit>', 'LIFECYCLE',
  'the first creation of the about page initializes its static URL and address strings',
  evidence='INFERRED JVM class initialization (JLS 12.4.1): the framework creates the page by its class name; static fields SRC ui/AboutActivity.java:29-35')
# no app code calls getThemeColorAsHex: its only occurrence in the app tree is its own declaration (grep of the app tree)
UNREACHABLE['AboutActivity.getThemeColorAsHex'] = ('no_trigger_in_app',
    'no app code calls getThemeColorAsHex: its only occurrence in the app tree is its own declaration',
    'ui/AboutActivity.java:143-146', 'SOURCE')

# --- batch 17: ImportEntriesActivity (the import review page). Its DecryptListener anonymous class ($2: onStateDecrypted, onError,
# onCanceled and lambda$onError$0) is called by the importers' decrypt code, so it stays UNRESOLVED until the importer cluster is wired (AGENT_NOTES).
FW_SNACK = ('INFERRED com.google.android.material: Snackbar.show runs Callback.onShown when the bar appears and Callback.onDismissed when it leaves '
            '(material source not cached)')

# the toolbar menu (created after onCreate) and its taps
e('ImportEntriesActivity.onCreate', 'ImportEntriesActivity.startImport', 'CALL', 'the import page starts the import from its intent extras',
  guard='abortIfOrphan(savedInstanceState) is false (ImportEntriesActivity.java:64-66; AegisActivity.java:154-157)',
  evidence='SRC ui/ImportEntriesActivity.java:62-66,103-104; SRC ui/AegisActivity.java:154-157')
e('ImportEntriesActivity.onCreate', 'ImportEntriesActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate',
  evidence=FW_OPTIONS + '; SRC ui/ImportEntriesActivity.java:397-401')
gui('ImportEntriesActivity.onCreateOptionsMenu', 'ImportEntriesActivity.onOptionsItemSelected',
    'Tap a toolbar item: Up (closes the page), show or hide the checkboxes, or toggle the wipe-vault option',
    evidence=FW_MENU + '; SRC ui/ImportEntriesActivity.java:404-417')

# the list scroll listener ($1 is the first anonymous class of this page; it moves the save button)
e('ImportEntriesActivity.onCreate', 'ImportEntriesActivity$1.onScrolled', 'FRAMEWORK',
  'the list scrolls: the save button follows the scroll',
  evidence=FW_SCROLL + '; SRC ui/ImportEntriesActivity.java:79-85')

# the save button: the wipe dialog opens only when the vault has entries and the wipe option is checked; otherwise the entries are saved
gui('ImportEntriesActivity.onCreate', 'ImportEntriesActivity.lambda$onCreate$0',
    'Tap the save button: the wipe dialog opens if the wipe option is on and the vault has entries, otherwise the selected entries are saved',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:92-100')

# the app-version warning (startImport): both buttons come straight from the builder
gui('ImportEntriesActivity.startImport', 'ImportEntriesActivity.lambda$startImport$1',
    'Tap Yes in the app version warning: the entries are read from the installed app',
    guard='the installed app version is not supported (ImportEntriesActivity.java:110-113); the warning opens only then',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:113-120')
gui('ImportEntriesActivity.startImport', 'ImportEntriesActivity.lambda$startImport$2',
    'Tap No in the app version warning: the page closes',
    guard='the installed app version is not supported (ImportEntriesActivity.java:110-113); the warning opens only then',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:121-123')

sup(('ImportEntriesActivity.startImport', 'ImportEntriesActivity.startImportApp'))
e('ImportEntriesActivity.startImport', 'ImportEntriesActivity.startImportApp', 'CALL',
  'no file was passed and the installed app version is supported: the entries are read from the app',
  env=ENV_INSTALLED_GA,
  guard='no file was passed (ImportEntriesActivity.java:109) and the installed app version is supported (isInstalledAppVersionSupported, ImportEntriesActivity.java:110; GoogleAuthImporter.java:40-49)',
  evidence='SRC ui/ImportEntriesActivity.java:109-111; SRC importers/GoogleAuthImporter.java:40-49')
# RootShellTask: the root shell opens on a worker thread; the callback runs on the main thread with the shell
e('ImportEntriesActivity.startImportApp', 'RootShellTask.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (open the root shell; started by AsyncTask.execute, not ProgressDialogTask.execute)',
  evidence=FW_ASYNC + '; SRC ui/ImportEntriesActivity.java:173; SRC ui/tasks/RootShellTask.java:17-20')
e('RootShellTask.doInBackground', 'RootShellTask.onPostExecute', 'ASYNC', 'the shell is posted to the main thread',
  evidence=FW_ASYNC + '; SRC ui/tasks/RootShellTask.java:17,23-25')
e('RootShellTask.onPostExecute', 'ImportEntriesActivity.lambda$startImportApp$5', 'CALL',
  '_cb.onTaskFinished(shell): the callback reads the entries from the installed app, or closes the page when there is no root',
  evidence='SRC ui/tasks/RootShellTask.java:25,28-30; SRC ui/ImportEntriesActivity.java:143-174')
sup(('ImportEntriesActivity.lambda$startImportApp$5', 'GoogleAuthImporter.readFromApp'))
e('ImportEntriesActivity.lambda$startImportApp$5', 'GoogleAuthImporter.readFromApp', 'CALL',
  'the Google Authenticator importer reads the app database (the page is open and the root shell is open)',
  env=ENV_ROOT,
  guard='the page is not finishing (ImportEntriesActivity.java:145-147), the shell is not null and is root (lines 149-153; otherwise a toast and finish), and the importer on this page is GoogleAuthImporter (importer.readFromApp, line 156, is a virtual call on the chosen importer)',
  evidence='SRC ui/ImportEntriesActivity.java:145-156; SRC importers/GoogleAuthImporter.java:60-68')

# the four error dialogs that pass a page listener: Dialogs.lambda$showErrorDialog$15 is the OK button, and it calls the listener it was given
# (Dialogs.java:391-395). The listener is the page lambda named in each row (the caller shows the dialog only on the stated error).
for _lam, _why, _at in [
    ('ImportEntriesActivity.lambda$startImportFile$3', 'the file cannot be read (ImportEntriesActivity.java:137-139)', 'ImportEntriesActivity.java:139'),
    ('ImportEntriesActivity.lambda$startImportApp$4', 'the app read fails with a DatabaseImporterException (ImportEntriesActivity.java:162-164)', 'ImportEntriesActivity.java:164'),
    ('ImportEntriesActivity.lambda$processImporterState$6', 'the file cannot be decrypted or parsed (ImportEntriesActivity.java:199-201)', 'ImportEntriesActivity.java:201'),
    ('ImportEntriesActivity.lambda$processDecryptedImporterState$7', 'the entries cannot be converted (ImportEntriesActivity.java:208-211)', 'ImportEntriesActivity.java:211'),
]:
    e('Dialogs.lambda$showErrorDialog$15', _lam, 'CALL',
      'Tap OK in the error dialog: the page closes. The dialog opens when ' + _why,
      cls='non_standard', via='DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at ' + _at + ')',
      evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ' + _at)

# processDecryptedImporterState: the icon-optimisation callback and the icon filter stream
e('ImportEntriesActivity.processDecryptedImporterState', 'ImportEntriesActivity.lambda$processDecryptedImporterState$8', 'FRAMEWORK',
  'the icon filter runs when the stream collects the entries that carry an icon to optimise',
  evidence=FW_STREAM + '; SRC ui/ImportEntriesActivity.java:215-219')
e('IconOptimizationTask.onPostExecute', 'ImportEntriesActivity.lambda$processDecryptedImporterState$9', 'CALL',
  '_cb.onTaskFinished(results): the optimised icons are set on the entries, then the entries are listed for review',
  cls='non_standard', via='IconOptimizationTask.Callback.onTaskFinished (interface call; the lambda is passed at ImportEntriesActivity.java:221)',
  evidence='SRC ui/tasks/IconOptimizationTask.java:57; SRC ui/ImportEntriesActivity.java:221-232')

# the save: after the vault is saved, the assign-icons dialog opens when an icon pack is installed (the dialog buttons come straight from the builder)
gui('ImportEntriesActivity.saveAndFinish', 'ImportEntriesActivity.lambda$saveAndFinish$10',
    'Tap Yes in the assign icons dialog: the assign icons page opens and this page closes',
    guard='the save succeeded and an icon pack is installed (ImportEntriesActivity.java:313-322)',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:329-335')
e('ImportEntriesActivity.lambda$saveAndFinish$10', 'AssignIconsActivity.<init>', 'INTENT',
  'the assign icons page starts with an explicit intent (the imported entry ids are passed as an extra)',
  evidence='SRC ui/ImportEntriesActivity.java:322-333')
gui('ImportEntriesActivity.saveAndFinish', 'ImportEntriesActivity.lambda$saveAndFinish$11',
    'Tap No in the assign icons dialog: this page closes',
    guard='the save succeeded and an icon pack is installed (ImportEntriesActivity.java:313-322)',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:336')
e('ImportEntriesActivity.findDuplicates', 'ImportEntriesActivity.lambda$findDuplicates$12', 'FRAMEWORK',
  'the duplicate check runs for each imported entry (the stream filter compares issuer and secret)',
  evidence=FW_STREAM + '; SRC ui/ImportEntriesActivity.java:344-349')

# the duplicate snackbar: its callbacks (shown, dismissed) and the Undo tap; they run only when a duplicate was found
e('ImportEntriesActivity.findDuplicates', 'ImportEntriesActivity$3.onShown', 'FRAMEWORK',
  'the duplicate snackbar appears: the list gets bottom padding for it',
  guard='at least one duplicate was found (ImportEntriesActivity.java:356-358)',
  evidence=FW_SNACK + '; SRC ui/ImportEntriesActivity.java:361-373')
e('ImportEntriesActivity.findDuplicates', 'ImportEntriesActivity$3.onDismissed', 'FRAMEWORK',
  'the duplicate snackbar leaves (Undo or a swipe): the bottom padding is removed',
  guard='at least one duplicate was found (ImportEntriesActivity.java:356-358)',
  evidence=FW_SNACK + '; SRC ui/ImportEntriesActivity.java:375-385')
gui('ImportEntriesActivity.findDuplicates', 'ImportEntriesActivity$4.onClick',
    'Tap Undo in the duplicate snackbar: the duplicates are checked again',
    guard='at least one duplicate was found (ImportEntriesActivity.java:356-358)',
    evidence=FW_CLICK + '; SRC ui/ImportEntriesActivity.java:387-392')

# --- batch 18: the entry list adapter (EntryAdapter) row callbacks, its DiffUtil callback and the list's drag helper
# (helpers/SimpleItemTouchHelperCallback.java). EntryListView creates the adapter (EntryListView.java:86) and attaches the helper (EntryListView.java:141-143).
# The EntryListView methods themselves (decorations, scroll, drop and move hand-off, onDestroy) are batch 19.
# The helper's callbacks are driven by a user touch on a row, so they are GUI edges from the list (S_LIST) with ST_LIST_LOADED.

# RecyclerView asks the adapter for each row's view type and recycles rows when the data changes (the row views leave the layout)
e('EntryListView.setEntries', 'EntryAdapter.getItemViewType', 'FRAMEWORK', 'RecyclerView asks each row for its view type when the list is laid out',
  evidence=FW_ROWS + '; SRC ui/views/EntryAdapter.java:394-404')
e('EntryListView.setEntries', 'EntryAdapter.onViewRecycled', 'FRAMEWORK', 'RecyclerView recycles the row views that leave the layout after a data change',
  evidence=FW_ROWS + '; SRC ui/views/EntryAdapter.java:429-434')

# DiffUtil compares the old and the new list (replaceEntryList builds the DiffCallback at EntryAdapter.java:286)
FW_DIFF = ('INFERRED androidx.recyclerview DiffUtil: calculateDiff reads the two list sizes, then compares the rows by identity and by contents '
           '(DiffUtil source not cached)')
e('EntryAdapter.replaceEntryList', 'EntryAdapter$DiffCallback.getOldListSize', 'FRAMEWORK', 'DiffUtil asks the old list for its size',
  evidence=FW_DIFF + '; SRC ui/views/EntryAdapter.java:286,905-907')
e('EntryAdapter.replaceEntryList', 'EntryAdapter$DiffCallback.getNewListSize', 'FRAMEWORK', 'DiffUtil asks the new list for its size',
  evidence=FW_DIFF + '; SRC ui/views/EntryAdapter.java:286,910-912')
e('EntryAdapter.replaceEntryList', 'EntryAdapter$DiffCallback.areItemsTheSame', 'FRAMEWORK', 'DiffUtil compares the rows at each position by identity',
  note='INFERRED: DiffUtil calls the compare methods only when both lists have rows',
  evidence=FW_DIFF + '; SRC ui/views/EntryAdapter.java:286,915-933')
e('EntryAdapter.replaceEntryList', 'EntryAdapter$DiffCallback.areContentsTheSame', 'FRAMEWORK', 'DiffUtil compares the contents of the rows whose identity matched',
  note='INFERRED: DiffUtil calls the compare methods only when both lists have rows',
  guard='both lists hold at least one row: the footer is always present (EntryAdapter.java:835-844)', needs_state=ST_LIST_LOADED,
  evidence=FW_DIFF + '; SRC ui/views/EntryAdapter.java:286,835-844,937-949')
e('Vault.toJson(EntryFilter)', 'VaultEntry.toJson', 'CALL', 'the export writes each entry the filter includes',
  guard='the entry is included by the filter (filter == null or includeEntry, Vault.java:10)', needs_state=ST_VAULT_ENTRIES,
  evidence='SRC vault/Vault.java:9-12')
e('VaultEntry.toJson', 'MotpInfo.getTypeId', 'CALL', 'the entry type id is written: MOTP info (dispatch on the runtime type of _info)',
  guard='the entry info is MotpInfo (VaultEntry.java:55 dispatches on the runtime type)', needs_state=ST_MOTP_ENTRY,
  evidence='SRC vault/VaultEntry.java:55')
sup(('VaultEntry.equivalates', 'OtpInfo.equals'))
e('VaultEntry.equivalates', 'MotpInfo.equals', 'CALL', 'the stored entry info is compared: the MOTP override runs first (getInfo().equals dispatches on the runtime type)',
  guard='both entries hold MOTP info (MotpInfo.java:74-76 returns false for other types)', needs_state=ST_MOTP_ENTRY,
  evidence='SRC vault/VaultEntry.java:235; SRC otp/MotpInfo.java:72-79')
e('MotpInfo.equals', 'TotpInfo.equals', 'CALL', 'MotpInfo.equals first compares the base TOTP fields (super.equals)',
  evidence='SRC otp/MotpInfo.java:79; SRC otp/TotpInfo.java:89-97')
e('TotpInfo.equals', 'OtpInfo.equals', 'CALL', 'TotpInfo.equals first compares the base OTP fields (super.equals)',
  guard='the other object is a TotpInfo (TotpInfo.java:91-93)', evidence='SRC otp/TotpInfo.java:91-96; SRC otp/OtpInfo.java:147-161')

# error card -> row comparison -> entry comparison (group D M3): the bytecode edges for these pairs have no guard, so they are cut and the guarded hand edges below replace them
sup(('MainActivity.onStart', 'MainActivity.updateErrorCard'), ('EntryAdapter.setErrorCardInfo', 'EntryAdapter.replaceEntryList'),
    ('EntryAdapter$DiffCallback.areContentsTheSame', 'VaultEntry.equals'), ('VaultEntry.equivalates', 'TotpInfo.equals'),
    ('OtpInfo.equals', 'MotpInfo.getTypeId'))
e('MainActivity.onStart', 'MainActivity.updateErrorCard', 'CALL', 'the error card is updated at the end of onStart',
  guard='onStart did not return early (MainActivity.java:942-948, 960, 971)', needs_state=ST_VAULT_FILE,
  evidence='SRC ui/MainActivity.java:942-1007')
e('EntryAdapter.setErrorCardInfo', 'EntryAdapter.replaceEntryList', 'CALL', 'the error card info is set and the list is replaced',
  guard='the error card info differs from the one shown (EntryAdapter.java:153-155) and the new info is not null (with null on both sides Objects.equals is true and the list is kept): an errored built-in backup (Preferences.java:495-499), a needed and enabled backup reminder (pref_backups_reminder_needed, Preferences.java:542-543), or the plaintext-backup warning (pref_plaintext_backup_warning_needed, Preferences.java:550-552); MainActivity.java:1163-1193 picks the card',
  evidence='SRC ui/views/EntryAdapter.java:152-157; SRC ui/MainActivity.java:1163-1193')
e('EntryAdapter$DiffCallback.areContentsTheSame', 'VaultEntry.equals', 'CALL', 'the two rows are entries: their contents are compared',
  guard='the rows are not both footers (EntryAdapter.java:938-940) and not both error cards (942-944)', evidence='SRC ui/views/EntryAdapter.java:937-949')
e('VaultEntry.equivalates', 'TotpInfo.equals', 'CALL', 'the stored entry info is compared with the TOTP equals (dispatch on the runtime type)',
  guard='the stored entry info has no equals override of its own: not MOTP (MotpInfo.java:73), Yandex (YandexInfo.java:86) or HOTP (HotpInfo.java:80)',
  evidence='SRC vault/VaultEntry.java:235; SRC otp/TotpInfo.java:89-97; SRC otp/MotpInfo.java:73; SRC otp/YandexInfo.java:86; SRC otp/HotpInfo.java:80')
e('OtpInfo.equals', 'MotpInfo.getTypeId', 'CALL', 'the entry type id of this object is compared: MOTP info (runtime dispatch on this)',
  guard='this object is a MotpInfo (MotpInfo.java:47-50 overrides getTypeId) and the other object is not this and is an OtpInfo (OtpInfo.java:149-154)',
  needs_state=ST_MOTP_ENTRY, evidence='SRC otp/OtpInfo.java:147-157; SRC otp/MotpInfo.java:47-50')
sup(('OtpInfo.getType', 'MotpInfo.getTypeId'))
e('OtpInfo.getType', 'MotpInfo.getTypeId', 'CALL', 'the type name is read from this object: MOTP info (runtime dispatch on this)',
  guard='this object is a MotpInfo (MotpInfo.java:47-50 overrides getTypeId)', needs_state=ST_MOTP_ENTRY,
  evidence='SRC otp/OtpInfo.java:41-43; SRC otp/MotpInfo.java:47-50')
sup(('EditEntryActivity.onCreate', 'MotpInfo.getTypeId'))
e('EditEntryActivity.onCreate', 'MotpInfo.getTypeId', 'CALL', 'the edited entry is a MOTP entry: its type id sets the PIN field visibility (runtime dispatch)',
  guard='the edited entry info is MotpInfo (MotpInfo.java:47-50 overrides getTypeId; EditEntryActivity.java:291 dispatches on the runtime type)',
  needs_state=ST_MOTP_ENTRY, evidence='SRC ui/EditEntryActivity.java:290-291; SRC otp/MotpInfo.java:47-50')

# stream lambdas inside the adapter (the stream runs when its method runs)
e('EntryAdapter.isEntryFiltered@FILTERED', 'EntryAdapter.lambda$isEntryFiltered$0', 'FRAMEWORK', 'the stream tests each search token against the entry fields',
  guard='a search text is set (_searchFilter is not null, EntryAdapter.java:200); reached only through the filter-set refresh chain (setSearchFilter -> refreshEntryList@FILTERED -> calculateShownEntries@FILTERED)',
  evidence='INFERRED java.util.stream: the terminal allMatch (EntryAdapter.java:205) runs the predicate lambda once per token (JDK source not read); SRC ui/views/EntryAdapter.java:204-210')
e('EntryAdapter.doesAnyGroupMatchSearchFilter', 'EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1', 'FRAMEWORK',
  'the stream keeps the groups that the entry belongs to',
  note='the group-name test is in lambda$doesAnyGroupMatchSearchFilter$2 (EntryAdapter.java:229), which this route does not reach',
  evidence='INFERRED java.util.stream: the terminal anyMatch (EntryAdapter.java:229) pulls elements through filter and map (JDK source not read); SRC ui/views/EntryAdapter.java:226-229')
e('EntryAdapter.doesAnyGroupMatchSearchFilter', 'EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$2', 'FRAMEWORK',
  'anyMatch tests each group name against the search token',
  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:228-229')

# G5 (stage 2): hand edges that carry the guards for the search-filter calls (each replaces the auto row for its pair)
# R4 variant (route 20 fix): the restore call lives ONLY on the recreated-menu variant, reached
# solely through the save/restore producer chain below. The base onCreateOptionsMenu no longer
# feeds setSearchFilter directly, so the router cannot take the producer-less restore shortcut.
e('MainActivity.onCreateOptionsMenu@RESTORED', 'EntryListView.setSearchFilter', 'CALL', 'a submitted search is restored when the menu is created: the list is filtered by it',
  guard='_pendingSearchQuery == null and _submittedSearchQuery != null (MainActivity.java:1066-1073); this menu instance is the recreated one',
  needs_state=ST_SUBMITTED_QUERY_SAVED,
  evidence='SRC ui/MainActivity.java:1066-1073 (bytecode line 1073)')
# R4b variant (route 20 fix, part 2): the filter-set refresh chain lives ONLY on @FILTERED
# variants. Base refresh (sort, group filter, hard refresh) and initial load (setEntries)
# still call base calculateShownEntries -> base isEntryFiltered, which has NO lambda$0 edge:
# with no filter set, isEntryFiltered returns before the token stream (EntryAdapter.java:200).
# Only the setSearchFilter refresh reaches lambda$0, so the router cannot shortcut through load.
e('EntryAdapter.setSearchFilter', 'EntryAdapter.refreshEntryList@FILTERED', 'CALL', 'a changed search text refreshes the list',
  guard='the new search text differs from the current _searchFilter (EntryAdapter.java:271); this refresh runs with a search filter set',
  evidence='SRC ui/views/EntryAdapter.java:271-273 (bytecode line 273)')
e('EntryAdapter.refreshEntryList@FILTERED', 'EntryAdapter.calculateShownEntries@FILTERED', 'CALL', 'the filtered list is recomputed from the current entries',
  evidence='SRC ui/views/EntryAdapter.java:277-281')
e('EntryAdapter.calculateShownEntries@FILTERED', 'EntryAdapter.isEntryFiltered@FILTERED', 'CALL', 'each entry is tested by the search filter and kept when it is not filtered out',
  guard='the entries list has at least one entry: the for loop runs (EntryAdapter.java:301)', needs_state=ST_ENTRY_LIST_NONEMPTY,
  evidence='SRC ui/views/EntryAdapter.java:280; SRC ui/views/EntryAdapter.java:299-302')
# R4b follow-up (route 20 fix): hand edges replacing the auto rows for the refreshEntryList
# -> EntryList.<init> pairs. The variant-duplicated auto row cited only :281 (the closing line
# of the new EntryList( call), which does not show the callee; both pairs cite the full call
# span :278-281 instead. Note the build's add_auto_edges suppresses an auto call when its
# base pair has a hand edge, so the base pair needs its own hand edge too, or the true base
# call would be unmodelled.
e('EntryAdapter.refreshEntryList@FILTERED', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'CALL', 'Direct call',
  evidence='SRC ui/views/EntryAdapter.java:278-281 (bytecode line 281)')
e('EntryAdapter.refreshEntryList', 'EntryAdapter$EntryList.<init>(List,List,ErrorCardInfo)', 'CALL', 'Direct call',
  evidence='SRC ui/views/EntryAdapter.java:278-281 (bytecode line 281)')
e('EntryAdapter.lambda$isEntryFiltered$0', 'EntryAdapter.doesAnyGroupMatchSearchFilter', 'CALL', 'the search token is tested against the group names',
  guard='_searchBehaviorMask includes SEARCH_IN_GROUPS and the token did not match the issuer, name or note (EntryAdapter.java:206-209)',
  needs_state=ST_SEARCH_IN_GROUPS,
  evidence='SRC ui/views/EntryAdapter.java:206-209 (bytecode line 209)')
e('EntryAdapter.onBindViewHolder', 'EntryAdapter.lambda$onBindViewHolder$3', 'FRAMEWORK',
  'the stream counts the entries with the same issuer, so the account name is shown only when it is needed',
  guard='the preference "only show necessary account names" is on (_onlyShowNecessaryAccountNames, EntryAdapter.java:448)',
  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:448-452')

# the drag helper: the user presses a row, then drags it. The helper asks each callback in turn (FW_TOUCH_DRAG)
gui('S_LIST', 'SimpleItemTouchHelperCallback.isLongPressDragEnabled',
    'Press and hold a row (the helper asks whether a long press may start a drag)', needs_state=ST_LIST_LOADED,
    evidence=FW_TOUCH_DRAG + '; SRC helpers/SimpleItemTouchHelperCallback.java:25-28; SRC ui/views/EntryListView.java:141-143')
gui('S_LIST', 'SimpleItemTouchHelperCallback.isItemViewSwipeEnabled',
    'Touch a row (the helper asks whether a swipe is allowed; the answer is no)', needs_state=ST_LIST_LOADED,
    evidence=FW_TOUCH_DRAG + '; SRC helpers/SimpleItemTouchHelperCallback.java:45-48')
gui('S_LIST', 'SimpleItemTouchHelperCallback.getMovementFlags',
    'Press and hold a row, then drag it (the helper asks which moves are allowed for the row)', needs_state=ST_LIST_LOADED,
    evidence=FW_TOUCH_DRAG + '; SRC helpers/SimpleItemTouchHelperCallback.java:54-78')
gui('S_LIST', 'SimpleItemTouchHelperCallback.onMove',
    'Drag a row over another row (the entry moves, unless it is a favorite or a filter is set)', needs_state=ST_LIST_LOADED,
    evidence=FW_TOUCH_DRAG + '; SRC helpers/SimpleItemTouchHelperCallback.java:80-94')
gui('S_LIST', 'SimpleItemTouchHelperCallback.clearView',
    'Let go of a touched row (the drop is saved only if the row moved)', needs_state=ST_LIST_LOADED,
    evidence=FW_TOUCH_DRAG + '; SRC helpers/SimpleItemTouchHelperCallback.java:101-110')

# no swipe can start: isItemViewSwipeEnabled is false and getMovementFlags never adds a swipe flag, so onSwiped never runs
UNREACHABLE['SimpleItemTouchHelperCallback.onSwiped'] = ('framework_never_calls',
    'the helper calls onSwiped only for a swipe; isItemViewSwipeEnabled returns false (SimpleItemTouchHelperCallback.java:46-48) and getMovementFlags never sets a swipe flag (lines 69, 77), so no swipe starts',
    'helpers/SimpleItemTouchHelperCallback.java:46-48,69,77', 'INFERRED')
# the only app caller of onItemDismiss is onSwiped (above), which never runs; the body is empty too.
# NOTE: this leaves one warning (an UNREACHABLE method with an incoming CALL edge from onSwiped), which is correct: the call site exists but never runs.
UNREACHABLE['EntryAdapter.onItemDismiss'] = ('framework_never_calls',
    'the only caller is SimpleItemTouchHelperCallback.onSwiped, which never runs (no swipe can start), and the body is empty (EntryAdapter.java:350-352)',
    'ui/views/EntryAdapter.java:349-352; helpers/SimpleItemTouchHelperCallback.java:97-99', 'INFERRED')

# --- batch 19: the rest of the entry list (EntryListView: scroll, span lookup, touch and insets listeners, refresher, decorations, icon
# preloading, lifecycle), EntryHolder (the row's refresh listener, focus and copy animations, expiration colour) and the shared
# UiRefresher helper (helpers/UiRefresher.java). UiRefresher.start posts two runnables; each one reposts itself, so only the first run
# is an edge here. The listener calls inside the runnables are auto CALL edges (dispatch cha), so the refresh and expiring callbacks
# of EntryListView$3 and EntryHolder$1 get their edges from them.

# the refresher's two runnables: the first run starts the loop (UiRefresher.java:22-42)
e('UiRefresher.start', 'UiRefresher$1.run', 'FRAMEWORK', 'the handler runs the refresh runnable after its first delay (it then reposts itself)',
  guard='the refresher is not running yet (UiRefresher.java:23-25)',
  evidence=FW_POST + '; SRC helpers/UiRefresher.java:22-34')
e('UiRefresher.start', 'UiRefresher$2.run', 'FRAMEWORK', 'the handler runs the expiring runnable after its delay (it then reposts itself)',
  guard='the refresher is not running yet (UiRefresher.java:23-25)',
  evidence=FW_POST + '; SRC helpers/UiRefresher.java:22,36-42')

# UiRefresher$1.run and $2.run are shared by every refresher (the list's and each row's), so their listener edges are split by caller
sup(('UiRefresher$1.run', 'EntryHolder$1.onRefresh'), ('UiRefresher$1.run', 'EntryListView$3.onRefresh'),
    ('UiRefresher$2.run', 'EntryHolder$1.onExpiring'), ('UiRefresher$2.run', 'EntryListView$3.onExpiring'))
e('EntryListView.onRefreshStart', 'EntryListView$3.onRefresh', 'CALL', 'the list refresher calls the list listener: the codes of the list are refreshed',
  cls='non_standard', via='UiRefresher.start posts the runnable; UiRefresher$1.run calls _listener.onRefresh() (UiRefresher.java:31) on the list listener',
  guard='the list has a TOTP entry: getMostFrequentPeriod() != -1 (EntryListView.java:213)',
  evidence='SRC ui/views/EntryListView.java:146-151,212-215; SRC helpers/UiRefresher.java:22-34')
e('EntryListView.onRefreshStart', 'EntryListView$3.onExpiring', 'CALL', 'the list refresher calls the list listener before a code expires (vibration)',
  cls='non_standard', via='UiRefresher.start posts the runnable; UiRefresher$2.run calls _listener.onExpiring() (UiRefresher.java:39) on the list listener',
  guard='the list has a TOTP entry: getMostFrequentPeriod() != -1 (EntryListView.java:213)',
  evidence='SRC ui/views/EntryListView.java:154-156,212-215; SRC helpers/UiRefresher.java:36-42')
e('EntryHolder.startRefreshLoop', 'EntryHolder$1.onRefresh', 'CALL', 'the row refresher calls the row listener: the code of this row is refreshed',
  cls='non_standard', via='UiRefresher.start posts the runnable; UiRefresher$1.run calls _listener.onRefresh() (UiRefresher.java:31) on the row listener',
  needs_state=ST_HOLDERS_BOUND,
  guard='the refresher is not already running (UiRefresher.java:23-25; the progress-bar guard is on the call to startRefreshLoop, EntryHolder.java:245-252)',
  evidence='SRC ui/views/EntryHolder.java:107-111,282-284; SRC helpers/UiRefresher.java:22-34')
e('EntryHolder.startRefreshLoop', 'EntryHolder$1.onExpiring', 'CALL', 'the row refresher calls the row listener before the code expires (no action in the row)',
  cls='non_standard', via='UiRefresher.start posts the runnable; UiRefresher$2.run calls _listener.onExpiring() (UiRefresher.java:39) on the row listener',
  needs_state=ST_HOLDERS_BOUND,
  guard='the row shows its progress bar: showProgress is true and the entry is not HOTP (EntryHolder.java:245-252)',
  evidence='SRC ui/views/EntryHolder.java:107-108,113-114,282-284; SRC helpers/UiRefresher.java:36-42')

# the list (EntryListView): a user scroll, the grid span lookup, a touch and the insets listener of the recycler view
gui('S_LIST', 'EntryListView$1.onScrolled', 'Scroll the list (the Listener gets the scroll distances)', needs_state=ST_LIST_LOADED,
    evidence=FW_SCROLL + '; SRC ui/views/EntryListView.java:104-111')
e('EntryListView.setEntries', 'EntryListView$2.getSpanSize', 'FRAMEWORK', 'the grid layout asks for the span of each row when it lays out the list',
  evidence='INFERRED androidx.recyclerview GridLayoutManager: the layout asks the span lookup for each row (framework source not read); SRC ui/views/EntryListView.java:127-139')
gui('S_LIST', 'EntryListView.lambda$onCreateView$0', 'Touch the list (the Listener is told about the touch)', needs_state=ST_LIST_LOADED,
    evidence='INFERRED View.OnTouchListener: dispatchTouchEvent calls onTouch (framework source not read); SRC ui/views/EntryListView.java:114-119')
e('EntryListView.onCreateView', 'EntryListView.lambda$onCreateView$1', 'FRAMEWORK', 'the window insets listener runs when the system bars change (the list padding is set)',
  evidence=FW_INSETS + '; SRC ui/views/EntryListView.java:174-184')

# a new entry that is off screen: the list scrolls to it, and a touch during that scroll stops it (EntryListView.java:448-489)
e('EntryListView.onEntryAdded', 'EntryListView$4.onScrollStateChanged', 'FRAMEWORK',
  'the list reports its scroll state while it scrolls to the new entry; with the smooth scroll it starts the highlight when idle',
  guard='the entry is off screen (EntryListView.java:448-451) and the smooth scroll is on (line 451)',
  evidence=FW_SCROLL + '; SRC ui/views/EntryListView.java:452-473')
e('EntryListView.onEntryAdded', 'EntryListView$4.onScrolled', 'FRAMEWORK',
  'the list scrolls to the new entry; without the smooth scroll it starts the highlight at once',
  guard='the entry is off screen (EntryListView.java:448-451) and the smooth scroll is off (line 451)',
  evidence=FW_SCROLL + '; SRC ui/views/EntryListView.java:452-473')
e('EntryListView.onEntryAdded', 'EntryListView.lambda$onEntryAdded$2', 'FRAMEWORK',
  'the user touches the list while it scrolls to the new entry (the scroll listener is removed and the scroll stops)',
  guard='the entry is off screen (EntryListView.java:448-451)',
  evidence='INFERRED View.OnTouchListener: dispatchTouchEvent calls onTouch (framework source not read); SRC ui/views/EntryListView.java:474-482')
# the entry is already on screen: the else branch of the scroll test starts the highlight at once
e('EntryListView.onEntryAdded', 'EntryListView.tempHighlightEntry', 'CALL', 'the entry is on screen: the highlight starts at once',
  guard='valid position (EntryListView.java:444-446) and no scroll needed (the scroll test at 449-450 is false, so the else at 490 runs)',
  evidence='SRC ui/views/EntryListView.java:444-446,449-450,490-491')

# the icon preloader is a scroll listener (EntryListView.java:124-125): a scroll asks it for the entries about to show
gui('S_LIST', 'EntryListView$IconPreloadProvider.getPreloadItems',
    'Scroll the list (the Glide preloader asks which entries are about to show, so their icons load early)', needs_state=ST_LIST_LOADED,
    evidence=FW_SCROLL + '; INFERRED Glide RecyclerViewPreloader: onScrolled asks the model provider for the items (library source not read); SRC ui/views/EntryListView.java:689-707')
gui('S_LIST', 'EntryListView$IconPreloadProvider.getPreloadRequestBuilder',
    'Scroll the list: the preloader builds the request for each entry that has an icon',
    guard='the entry has an icon (EntryListView.java:701-706)', needs_state=ST_LIST_LOADED,
    evidence='INFERRED Glide RecyclerViewPreloader: it builds a request for each item that getPreloadItems returned (library source not read); SRC ui/views/EntryListView.java:711-715')

# the item decorations are added by updateDividerDecoration (EntryListView.java:524-537); RecyclerView then calls them on each layout pass
e('EntryListView.updateDividerDecoration', 'EntryListView$TileSpaceItemDecoration.getItemOffsets', 'FRAMEWORK',
  'RecyclerView asks the tile decoration for the offsets of each row when it lays out the list',
  guard='the view mode is TILES (EntryListView.java:530-531)',
  evidence='INFERRED androidx.recyclerview ItemDecoration: the layout pass calls getItemOffsets for each row (framework source not read); SRC ui/views/EntryListView.java:530-536,665-667')
e('EntryListView.updateDividerDecoration', 'EntryListView$VerticalSpaceItemDecoration.getItemOffsets', 'FRAMEWORK',
  'RecyclerView asks the list decoration for the offsets of each row when it lays out the list',
  guard='the view mode is not TILES (EntryListView.java:530-533)',
  evidence='INFERRED androidx.recyclerview ItemDecoration: the layout pass calls getItemOffsets for each row (framework source not read); SRC ui/views/EntryListView.java:530-536,581-585')

# fragment lifecycle: the view is destroyed (the refresher stops), then the fragment (the adapter releases its rows)
e('EntryListView.onCreateView', 'EntryListView.onDestroyView', 'LIFECYCLE', 'the fragment destroys its view when it leaves the screen (the refresher stops)',
  evidence='INFERRED androidx.fragment: the FragmentManager calls onDestroyView after onCreateView (fragment source not read); SRC ui/views/EntryListView.java:203-206')
e('EntryListView.onDestroyView', 'EntryListView.onDestroy', 'LIFECYCLE', 'the fragment is destroyed after its view (the adapter releases its rows)',
  evidence='INFERRED androidx.fragment: the FragmentManager calls onDestroy after onDestroyView (fragment source not read); SRC ui/views/EntryListView.java:91-94')

# EntryHolder: the scale-out animation of an unfocused row ends and the listener hides the row (EntryHolder.java:265-276)
gui('EntryHolder.setFocusedAndAnimate', 'SimpleAnimationEndListener.onAnimationEnd',
    'Unfocus a row: its scale-out animation ends', guard='the row is unfocused (EntryHolder.java:268-272)',
    evidence='INFERRED android.view.animation: the animation calls onAnimationEnd on its listener (framework source not read); SRC ui/views/EntryHolder.java:270-272')
e('SimpleAnimationEndListener.onAnimationEnd', 'EntryHolder.lambda$setFocusedAndAnimate$0', 'CALL',
  'the listener passes the animation end to the lambda, which hides the row',
  evidence='SRC helpers/SimpleAnimationEndListener.java:18-21; SRC ui/views/EntryHolder.java:272-274')

# the expiration colour (EntryHolder.java:428-466): the early return for a period of 7 s or less, then the two branches
e('EntryHolder.startExpirationAnimation', 'EntryHolder.lambda$startExpirationAnimation$1', 'FRAMEWORK',
  'the code text turns the error colour after the delay (animations are off, or Android is older than O)',
  guard='the expiration state is shown and the period is over 7 s (EntryHolder.java:430-439), animations are off or Android is older than O (EntryHolder.java:442-443), and the colour change is still ahead (EntryHolder.java:445-450)',
  evidence=FW_POST + '; SRC ui/views/EntryHolder.java:442-451')
e('EntryHolder.startExpirationAnimation', 'EntryHolder.lambda$startExpirationAnimation$2', 'FRAMEWORK',
  'the colour animation sets the code text colour on each frame',
  guard='the expiration state is shown and the period is over 7 s (EntryHolder.java:430-439), and animations are on on Android O or newer (EntryHolder.java:442-443,456-465)',
  evidence='INFERRED android.animation: a ValueAnimator calls its update listener on each frame (framework source not read); SRC ui/views/EntryHolder.java:463-465')

# the copy animation: one timed fade-back for the list layouts, one for Tiles (EntryHolder.java:535-553)
e('EntryHolder.animateCopyText', 'EntryHolder.lambda$animateCopyText$3', 'FRAMEWORK',
  'after 3 s the copy text fades back (the row is not in Tiles mode)',
  guard='the view mode is not TILES (EntryHolder.java:535-543)',
  evidence=FW_POST + '; SRC ui/views/EntryHolder.java:540-543')
e('EntryHolder.animateCopyText', 'EntryHolder.lambda$animateCopyText$4', 'FRAMEWORK',
  'after 3 s the copy text fades back (the row is in Tiles mode)',
  guard='the view mode is TILES (EntryHolder.java:544-553)',
  evidence=FW_POST + '; SRC ui/views/EntryHolder.java:550-553')

UNREACHABLE['EntryHolder.isHidden'] = ('no_trigger_in_app',
    'no code in the app calls isHidden (grep of the app tree: only the definition at EntryHolder.java:503)',
    'ui/views/EntryHolder.java:503-505', 'SOURCE')

# --- batch 20: the importer decrypt paths (the picked importer is created by reflection; the password, cancel, warning and choice dialogs; the key-derivation tasks; the error-dialog OK)
# (a) DatabaseImporter.create builds the importer the user picked, by reflection (DatabaseImporter.java:92). One edge per class in the Definition list (DatabaseImporter.java:33-51), 19 classes.
for _imp in [
    'TwoFASImporter', 'AegisImporter', 'AndOtpImporter', 'AuthenticatorPlusImporter', 'AuthyImporter',
    'BattleNetImporter', 'BitwardenImporter', 'DuoImporter', 'EnteAuthImporter', 'FreeOtpImporter',
    'FreeOtpPlusImporter', 'GoogleAuthImporter', 'MicrosoftAuthImporter', 'GoogleAuthUriImporter',
    'ProtonAuthenticatorImporter', 'SteamImporter', 'StratumImporter', 'TotpAuthenticatorImporter', 'WinAuthImporter',
]:
    e('DatabaseImporter.create', _imp + '.<init>', 'CALL',
      'the picked importer is created by its Context constructor',
      cls='non_standard', via='reflection: type.getConstructor(Context.class).newInstance(context) (DatabaseImporter.java:92); the type is the Definition the user picked (ImportEntriesActivity.java:108)',
      evidence='SRC importers/DatabaseImporter.java:33-51,90-98; SRC ui/ImportEntriesActivity.java:108')

# (b) the password dialog (Dialogs.showTextInputDialog): its OK button (Dialogs $7) gives the typed text to the listener it was given (Dialogs.java:233). Each importer password lambda is one such listener.
# (b) the password dialog is split by caller: the plain Dialogs $7 delivers to NO importer
# any more. Each importer password lambda is reached only through its own dialog chain, so
# a dialog opened by one caller can never deliver to another caller's lambda (the shared-$7
# cross-delivery was route 16 steps 27 and 33, and route 06 step 25). Plain $7 keeps only
# its getEditTextChars leaf. Plain cancel edges are kept: a cancel reports to the page and
# never reaches any target, so it is not a source of false routes.
# variant password-dialog chain @ANDOTP: only the dialog opened by AndOtpImporter$EncryptedState.lambda$decrypt$3 reaches AndOtpImporter$EncryptedState.lambda$decrypt$1.
e('AndOtpImporter$EncryptedState.lambda$decrypt$3', 'Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@ANDOTP', 'CALL', 'Direct call',
  evidence='SRC importers/AndOtpImporter.java:191 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@ANDOTP', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@ANDOTP', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:259 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@ANDOTP', 'Dialogs.lambda$showTextInputDialog$8@ANDOTP', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@ANDOTP', 'Dialogs.lambda$showTextInputDialog$6@ANDOTP',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@ANDOTP', 'Dialogs.lambda$showTextInputDialog$7@ANDOTP', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@ANDOTP', 'AndOtpImporter$EncryptedState.lambda$decrypt$1', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/AndOtpImporter.java:191-196',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/AndOtpImporter.java:191-196')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@ANDOTP', 'AndOtpImporter$EncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/AndOtpImporter.java:197')
# variant password-dialog chain @FREEOTP: only the dialog opened by FreeOtpImporter$EncryptedState.lambda$decrypt$3 reaches FreeOtpImporter$EncryptedState.lambda$decrypt$1.
e('FreeOtpImporter$EncryptedState.lambda$decrypt$3', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@FREEOTP', 'CALL', 'Direct call',
  evidence='SRC importers/FreeOtpImporter.java:182 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@FREEOTP', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@FREEOTP', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@FREEOTP', 'Dialogs.lambda$showTextInputDialog$8@FREEOTP', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@FREEOTP', 'Dialogs.lambda$showTextInputDialog$6@FREEOTP',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@FREEOTP', 'Dialogs.lambda$showTextInputDialog$7@FREEOTP', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@FREEOTP', 'FreeOtpImporter$EncryptedState.lambda$decrypt$1', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/FreeOtpImporter.java:182-194',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/FreeOtpImporter.java:182-194')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@FREEOTP', 'FreeOtpImporter$EncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/FreeOtpImporter.java:194')
# variant password-dialog chain @STRATUM: only the dialog opened by StratumImporter$EncryptedState.decrypt(Context,DecryptListener) reaches StratumImporter$EncryptedState.lambda$decrypt$1.
e('StratumImporter$EncryptedState.decrypt(Context,DecryptListener)', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@STRATUM', 'CALL', 'Direct call',
  evidence='SRC importers/StratumImporter.java:168 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@STRATUM', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@STRATUM', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@STRATUM', 'Dialogs.lambda$showTextInputDialog$8@STRATUM', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@STRATUM', 'Dialogs.lambda$showTextInputDialog$6@STRATUM',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@STRATUM', 'Dialogs.lambda$showTextInputDialog$7@STRATUM', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@STRATUM', 'StratumImporter$EncryptedState.lambda$decrypt$1', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/StratumImporter.java:168-180',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/StratumImporter.java:168-180')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@STRATUM', 'StratumImporter$EncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/StratumImporter.java:180')
# variant password-dialog chain @LEGACY: only the dialog opened by StratumImporter$LegacyEncryptedState.decrypt(Context,DecryptListener) reaches StratumImporter$LegacyEncryptedState.lambda$decrypt$1.
e('StratumImporter$LegacyEncryptedState.decrypt(Context,DecryptListener)', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@LEGACY', 'CALL', 'Direct call',
  evidence='SRC importers/StratumImporter.java:243 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@LEGACY', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@LEGACY', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@LEGACY', 'Dialogs.lambda$showTextInputDialog$8@LEGACY', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@LEGACY', 'Dialogs.lambda$showTextInputDialog$6@LEGACY',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@LEGACY', 'Dialogs.lambda$showTextInputDialog$7@LEGACY', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@LEGACY', 'StratumImporter$LegacyEncryptedState.lambda$decrypt$1', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/StratumImporter.java:243-255',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/StratumImporter.java:243-255')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@LEGACY', 'StratumImporter$LegacyEncryptedState.lambda$decrypt$2',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/StratumImporter.java:255')
# variant password-dialog chain @TOTP: only the dialog opened by TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$2 reaches TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0.
e('TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$2', 'Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@TOTP', 'CALL', 'Direct call',
  evidence='SRC importers/TotpAuthenticatorImporter.java:159 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@TOTP', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TOTP', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:259 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TOTP', 'Dialogs.lambda$showTextInputDialog$8@TOTP', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@TOTP', 'Dialogs.lambda$showTextInputDialog$6@TOTP',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@TOTP', 'Dialogs.lambda$showTextInputDialog$7@TOTP', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@TOTP', 'TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/TotpAuthenticatorImporter.java:159-160',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/TotpAuthenticatorImporter.java:159-160')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TOTP', 'TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$1',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/TotpAuthenticatorImporter.java:161')
# variant password-dialog chain @AUTHPLUS: only the dialog opened by AuthenticatorPlusImporter$EncryptedState.decrypt(Context,DecryptListener) reaches AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$0.
e('AuthenticatorPlusImporter$EncryptedState.decrypt(Context,DecryptListener)', 'Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@AUTHPLUS', 'CALL', 'Direct call',
  evidence='SRC importers/AuthenticatorPlusImporter.java:67 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,TextInputListener,OnCancelListener)@AUTHPLUS', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@AUTHPLUS', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:259 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@AUTHPLUS', 'Dialogs.lambda$showTextInputDialog$8@AUTHPLUS', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@AUTHPLUS', 'Dialogs.lambda$showTextInputDialog$6@AUTHPLUS',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@AUTHPLUS', 'Dialogs.lambda$showTextInputDialog$7@AUTHPLUS', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@AUTHPLUS', 'AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/AuthenticatorPlusImporter.java:67-74',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/AuthenticatorPlusImporter.java:67-74')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@AUTHPLUS', 'AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$1',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/AuthenticatorPlusImporter.java:74')
# variant password-dialog chain @TWOFAS: only the dialog opened by TwoFASImporter$EncryptedState.decrypt(Context,DecryptListener) reaches TwoFASImporter$EncryptedState.lambda$decrypt$0.
e('TwoFASImporter$EncryptedState.decrypt(Context,DecryptListener)', 'Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@TWOFAS', 'CALL', 'Direct call',
  evidence='SRC importers/TwoFASImporter.java:140 (bytecode)')
e('Dialogs.showPasswordInputDialog(Context,int,int,TextInputListener,OnCancelListener)@TWOFAS', 'Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TWOFAS', 'CALL', 'Direct call',
  evidence='SRC ui/dialogs/Dialogs.java:271 (bytecode)')
e('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TWOFAS', 'Dialogs.lambda$showTextInputDialog$8@TWOFAS', 'FRAMEWORK',
  'the input dialog is shown: its OnShowListener disables OK and sets the OK click listener', evidence=FW_DIALOG + '; SRC ui/dialogs/Dialogs.java:226-229')
gui('Dialogs.lambda$showTextInputDialog$8@TWOFAS', 'Dialogs.lambda$showTextInputDialog$6@TWOFAS',
    'Type in the input dialog (OK is enabled when the text is not empty)',
    evidence='SRC ui/dialogs/Dialogs.java:201-205; INFERRED TextWatcher.afterTextChanged runs on each text change (androidx source not read)')
gui('Dialogs.lambda$showTextInputDialog$6@TWOFAS', 'Dialogs.lambda$showTextInputDialog$7@TWOFAS', 'Tap OK in the password dialog (the typed text goes to the listener, then the dialog closes)',
    guard='the text is not empty (OK is disabled until then, Dialogs.java:203)', evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:231-235')
e('Dialogs.lambda$showTextInputDialog$7@TWOFAS', 'TwoFASImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the typed password goes to the importer, which starts the key derivation or the decryption',
  cls='non_standard', via='interface callback: Dialogs.TextInputListener.onTextInputResult (Dialogs.java:233); the listener is the lambda at importers/TwoFASImporter.java:140-146',
  evidence='SRC ui/dialogs/Dialogs.java:231-241; SRC importers/TwoFASImporter.java:140-146')
gui('Dialogs.showTextInputDialog(Context,int,int,int,TextInputListener,OnCancelListener,boolean,String)@TWOFAS', 'TwoFASImporter$EncryptedState.lambda$decrypt$1',
    'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/TwoFASImporter.java:147')

# (c) the cancel listener is set on the password dialog builder (Dialogs.java:217-219): a cancel (Back or a tap outside) runs the importer cancel lambda, which reports the cancel to the page
_CANCEL_LISTENERS = [
    ('AegisImporter$EncryptedState.lambda$decrypt$2', 'importers/AegisImporter.java:109'),
    ('AndOtpImporter$EncryptedState.lambda$decrypt$2', 'importers/AndOtpImporter.java:197'),
    ('FreeOtpImporter$EncryptedState.lambda$decrypt$2', 'importers/FreeOtpImporter.java:194'),
    ('StratumImporter$EncryptedState.lambda$decrypt$2', 'importers/StratumImporter.java:180'),
    ('StratumImporter$LegacyEncryptedState.lambda$decrypt$2', 'importers/StratumImporter.java:255'),
    ('TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$1', 'importers/TotpAuthenticatorImporter.java:161'),
    ('AuthyImporter$EncryptedState.lambda$decrypt$1', 'importers/AuthyImporter.java:214'),
    ('AuthenticatorPlusImporter$EncryptedState.lambda$decrypt$1', 'importers/AuthenticatorPlusImporter.java:74'),
]
for _lam, _at in _CANCEL_LISTENERS:
    gui(_B12_TIDLG, _lam, 'Cancel the password dialog (Back or a tap outside): the importer reports the cancel to the page',
        evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC ' + _at)

# (d) the warning and choice dialogs the importers build with MaterialAlertDialogBuilder: the framework runs each button listener (FW_CLICK)
gui('AndOtpImporter$EncryptedState.decrypt(Context,DecryptListener)', 'AndOtpImporter$EncryptedState.lambda$decrypt$3',
    'Tap OK in the andOTP format choice: the chosen format is read, then the password dialog opens',
    evidence=FW_CLICK + '; SRC importers/AndOtpImporter.java:186-189')
gui('TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener)', 'TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$2',
    'Tap Yes in the TOTP Authenticator question: the password dialog opens',
    evidence=FW_CLICK + '; SRC importers/TotpAuthenticatorImporter.java:158-162')
gui('TotpAuthenticatorImporter$EncryptedState.decrypt(Context,DecryptListener)', 'TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$3',
    'Tap No in the TOTP Authenticator question: the built-in password is used (decrypt(char[],DecryptListener) with PASSWORD)',
    evidence=FW_CLICK + '; SRC importers/TotpAuthenticatorImporter.java:163-165')
gui('FreeOtpImporter$EncryptedState.decrypt(Context,DecryptListener)', 'FreeOtpImporter$EncryptedState.lambda$decrypt$3',
    'Tap OK in the FreeOTP warning: the password dialog opens',
    evidence=FW_CLICK + '; SRC importers/FreeOtpImporter.java:180-182')

# (e) the key-derivation and decrypt tasks hand their result to the callback the importer gave them (interface call in onPostExecute; PBKDFTask.java:60, Argon2Task.java:41, PasswordSlotDecryptTask.java:89; these onPostExecute methods have no early return)
# replaced by the onPostExecute@AEGIS_WELCOME / @AEGIS_IMPORT callback edges in the Aegis chains above.
e('PBKDFTask.onPostExecute@ANDOTP', 'AndOtpImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the derived key goes back to the andOTP importer, which decrypts the new format',
  cls='non_standard', via='interface callback: PBKDFTask.Callback.onTaskFinished (PBKDFTask.java:60); the callback is the lambda at AndOtpImporter.java:166-173',
  evidence='SRC ui/tasks/PBKDFTask.java:57-61; SRC importers/AndOtpImporter.java:166-173')
e('PBKDFTask.onPostExecute@FREEOTP', 'FreeOtpImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the derived key goes back to the FreeOTP importer, which decrypts',
  cls='non_standard', via='interface callback: PBKDFTask.Callback.onTaskFinished (PBKDFTask.java:60); the callback is the lambda at FreeOtpImporter.java:184-191',
  evidence='SRC ui/tasks/PBKDFTask.java:57-61; SRC importers/FreeOtpImporter.java:184-191')
e('PBKDFTask.onPostExecute@LEGACY', 'StratumImporter$LegacyEncryptedState.lambda$decrypt$0', 'CALL',
  'the derived key goes back to the legacy Stratum importer, which decrypts',
  cls='non_standard', via='interface callback: PBKDFTask.Callback.onTaskFinished (PBKDFTask.java:60); the callback is the lambda at StratumImporter.java:245-252',
  evidence='SRC ui/tasks/PBKDFTask.java:57-61; SRC importers/StratumImporter.java:245-252')
e('Argon2Task.onPostExecute', 'StratumImporter$EncryptedState.lambda$decrypt$0', 'CALL',
  'the Argon2 key goes back to the Stratum importer, which decrypts',
  cls='non_standard', via='interface callback: Argon2Task.Callback.onTaskFinished (Argon2Task.java:41); the callback is the lambda at StratumImporter.java:170-177',
  evidence='SRC ui/tasks/Argon2Task.java:38-42; SRC importers/StratumImporter.java:170-177')

# (f) PBKDF2 and Argon2 key derivation: each importer's decrypt starts its own task (ProgressDialogTask.execute is shared, so it is not a source of these edges)
# PBKDF split by builder (same pattern as PasswordSlotDecryptTask): PBKDFTask.java:60 calls
# _cb.onTaskFinished, and _cb is fixed by the constructor argument at the build site, so a key
# derived for one importer can never deliver to another importer's lambda (that cross-delivery
# would otherwise survive the dialog splits as a new false route to ImportEntries $2).
e('AndOtpImporter$EncryptedState.decrypt(Context,char[],boolean,DecryptListener)', 'PBKDFTask.doInBackground@ANDOTP', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (PBKDF2 key derivation)',
  guard='the backup uses the new format, so the key is derived (AndOtpImporter.java:161-164)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/AndOtpImporter.java:161-175; SRC ui/tasks/PBKDFTask.java:29-35')
e('FreeOtpImporter$EncryptedState.lambda$decrypt$1', 'PBKDFTask.doInBackground@FREEOTP', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (PBKDF2 key derivation)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/FreeOtpImporter.java:184-193; SRC ui/tasks/PBKDFTask.java:29-35')
e('StratumImporter$LegacyEncryptedState.lambda$decrypt$1', 'PBKDFTask.doInBackground@LEGACY', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (PBKDF2 key derivation)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/StratumImporter.java:245-254; SRC ui/tasks/PBKDFTask.java:29-35')
for _tag in ['@ANDOTP', '@FREEOTP', '@LEGACY']:
    e('PBKDFTask.doInBackground' + _tag, 'PBKDFTask.onPostExecute' + _tag, 'ASYNC', 'the derived key is posted to the main thread',
      evidence=FW_ASYNC + '; SRC ui/tasks/PBKDFTask.java:29-35,57-61')
e('StratumImporter$EncryptedState.lambda$decrypt$1', 'Argon2Task.doInBackground', 'ASYNC', 'AsyncTask runs doInBackground on the worker thread (Argon2 key derivation)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:69-74; SRC importers/StratumImporter.java:170-179; SRC ui/tasks/Argon2Task.java:21-27')
e('Argon2Task.doInBackground', 'Argon2Task.onPostExecute', 'ASYNC', 'the derived key is posted to the main thread',
  evidence=FW_ASYNC + '; SRC ui/tasks/Argon2Task.java:21-27,38-42')

# (g) the decryption-error dialog of ImportEntriesActivity (line 188) is the same Dialogs error dialog as the four rows above: its OK button (Dialogs $15, Dialogs.java:391-393) runs the listener the page passed (finish)
e('Dialogs.lambda$showErrorDialog$15', 'ImportEntriesActivity$2.lambda$onError$0', 'CALL',
  'Tap OK in the decryption-error dialog: the import page closes',
  cls='non_standard', via='DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at ImportEntriesActivity.java:188)',
  evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ui/ImportEntriesActivity.java:188')

# (h) the first creation of these two importers runs their static initializers before the constructor body (JVM class initialization, JLS 12.4.1)
e('TotpAuthenticatorImporter.<init>', 'TotpAuthenticatorImporter.<clinit>', 'LIFECYCLE',
  'the first creation of the TOTP Authenticator importer initializes its static constants (the password and the IV)',
  evidence='INFERRED JVM class initialization (JLS 12.4.1); static fields SRC importers/TotpAuthenticatorImporter.java:52-53')
e('AuthyImporter.<init>', 'AuthyImporter.<clinit>', 'LIFECYCLE',
  'the first creation of the Authy importer initializes its static constants (file names, iterations, key size and the IV)',
  evidence='INFERRED JVM class initialization (JLS 12.4.1); static fields SRC importers/AuthyImporter.java:49-56')

# (i) overloads with no caller in the app tree (grep of every decrypt and decryptNewFormat call in the importers and ui folders): the importers decrypt through decrypt(Context, DecryptListener) and decryptNewFormat(SecretKey)
UNREACHABLE['AegisImporter$EncryptedState.decrypt(char[])'] = ('no_trigger_in_app',
    'no code calls this overload: the only occurrences are its declaration and the decrypt(VaultFileCredentials) call in its body',
    'importers/AegisImporter.java:81-86', 'SOURCE')
UNREACHABLE['FreeOtpImporter$EncryptedState.decrypt(char[])'] = ('no_trigger_in_app',
    'no code calls this overload: the only occurrences are its declaration and the decrypt(SecretKey) call in its body',
    'importers/FreeOtpImporter.java:149-152', 'SOURCE')
UNREACHABLE['StratumImporter$EncryptedState.decrypt(char[])'] = ('no_trigger_in_app',
    'no code calls this overload: the only occurrences are its declaration and the decrypt(SecretKey) call in its body',
    'importers/StratumImporter.java:149-152', 'SOURCE')
UNREACHABLE['StratumImporter$LegacyEncryptedState.decrypt(char[])'] = ('no_trigger_in_app',
    'no code calls this overload: the only occurrences are its declaration and the decrypt(SecretKey) call in its body',
    'importers/StratumImporter.java:224-227', 'SOURCE')
UNREACHABLE['AndOtpImporter$EncryptedState.decryptNewFormat(char[])'] = ('no_trigger_in_app',
    'no code calls this overload: the only occurrences are its declaration and the decryptNewFormat(SecretKey) call in its body (the key callback at AndOtpImporter.java:168 passes a SecretKey)',
    'importers/AndOtpImporter.java:153-157', 'SOURCE')

# --- batch 21: the SQL importers (each row is built by reflection), the Steam and Bitwarden file lambdas, the stream filter of the importer list, the import-entry list (adapter and holder), the TwoFAS password listener, and two UNREACHABLE entries
# (a) SqlImporterHelper.read(Class,File,String) builds each SQL row by reflection (SqlImporterHelper.java:106). The importers pass their Entry class in: GoogleAuthImporter.java:55,66; MicrosoftAuthImporter.java:39,49; StratumImporter.java:75.
for _row in ['StratumImporter$SqlEntry', 'GoogleAuthImporter$Entry', 'MicrosoftAuthImporter$Entry']:
    e('SqlImporterHelper.read(Class,File,String)', _row + '.<init>', 'CALL',
      'the SQL row is turned into its entry class by the Cursor constructor',
      cls='non_standard', via='reflection: type.getDeclaredConstructor(Cursor.class).newInstance(cursor) (SqlImporterHelper.java:106); the type is the Entry class the importer passes to read',
      evidence='SRC importers/SqlImporterHelper.java:99-107; SRC importers/GoogleAuthImporter.java:55,66; SRC importers/MicrosoftAuthImporter.java:39,49; SRC importers/StratumImporter.java:75')

# (b) the two file-name filters: libsu calls accept once for each name in the folder (INFERRED: the libsu source is not cached)
e('SqlImporterHelper.findDatabaseFiles', 'SqlImporterHelper.lambda$findDatabaseFiles$0', 'FRAMEWORK',
  'the folder listing calls the name filter for each file name; the filter keeps the names that start with the database file name',
  cls='non_standard', via='library callback: libsu SuFile.listFiles(FilenameFilter) calls the filter for each name in the folder (libsu source not on disk)',
  guard='the file name starts with the database file name (name.startsWith(path.getName()), SqlImporterHelper.java:67-68)',
  evidence='INFERRED libsu SuFile.listFiles(FilenameFilter) calls accept for each name in the folder (libsu source not cached); SRC importers/SqlImporterHelper.java:67-68')
e('SteamImporter.getAppPath', 'SteamImporter.lambda$getAppPath$0', 'FRAMEWORK',
  'the folder listing calls the name filter for each file name; the filter keeps the Steam Guard file',
  guard='the root shell reads the Steam app folder (SteamImporter.java:36-38; the caller is DatabaseImporter.readFromApp)',
  evidence='INFERRED libsu SuFile.listFiles(FilenameFilter) calls accept for each name in the folder (libsu source not cached); SRC importers/SteamImporter.java:36-38')

# (c) the Bitwarden CSV branch: forEachRemaining calls the row consumer for each remaining row (INFERRED: the Iterator default method or the CSV iterator override; JDK and CSV source not cached)
e('BitwardenImporter.read', 'BitwardenImporter.lambda$read$0', 'FRAMEWORK',
  'forEachRemaining hands each CSV row to the consumer, which keeps the login_totp values',
  guard='the export is not JSON: the JSON parse threw JSONException (BitwardenImporter.java:63-67)',
  evidence='INFERRED java.util.Iterator.forEachRemaining calls the consumer for each remaining row (JDK and CSV iterator source not cached); SRC importers/BitwardenImporter.java:63-72')

# (d) the stream filter in DatabaseImporter.getImporters (the Definition::supportsDirect method reference): a direct import keeps only the importers that support it
e('DatabaseImporter.getImporters', 'DatabaseImporter$Definition.supportsDirect', 'FRAMEWORK',
  'the terminal collect calls supportsDirect for each importer while the direct list is built',
  guard='a direct import is requested (isDirect is true, DatabaseImporter.java:100-101)',
  evidence='INFERRED java.util.stream: a terminal collect runs the filter for each element while the statement executes (JDK source not read); SRC importers/DatabaseImporter.java:99-105')

# (e) the import-entry list: addEntry notifies the adapter (ImportEntriesAdapter.java:27-32); RecyclerView creates, binds and recycles the rows
e('ImportEntriesAdapter.addEntry', 'ImportEntriesAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the notify call in addEntry asks RecyclerView to create a row view for the new entry',
  evidence=FW_ROWS + '; SRC ui/views/ImportEntriesAdapter.java:24-33,37-40')
e('ImportEntriesAdapter.addEntry', 'ImportEntriesAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView binds the new row to its entry after the notify call',
  evidence=FW_ROWS + '; SRC ui/views/ImportEntriesAdapter.java:24-33,43-47')
e('ImportEntriesAdapter.addEntry', 'ImportEntriesAdapter.onViewRecycled', 'FRAMEWORK',
  'RecyclerView recycles the row views that leave the layout after a data change',
  guard='the first entry calls notifyDataSetChanged (ImportEntriesAdapter.java:27-29), which recycles the rows',
  evidence=FW_ROWS + '; SRC ui/views/ImportEntriesAdapter.java:24-33,50-52')

# (f) a tap on an import row toggles its checkbox: the holder sets the click listener in its constructor (ImportEntryHolder.java:26)
gui('ImportEntryHolder.<init>', 'ImportEntryHolder.lambda$new$0',
    'Tap the import row: its checkbox toggles',
    evidence=FW_CLICK + '; SRC ui/views/ImportEntryHolder.java:26')

# (g) the TwoFAS password dialog: the OK button (Dialogs $7, nested in the show listener $8 at Dialogs.java:226-235) gives the typed password to the TwoFAS listener (TwoFASImporter.java:140-146); the cancel listener set on the builder (Dialogs.java:217-219) runs the TwoFAS cancel lambda
# TwoFAS plain $7 delivery deleted: the @TWOFAS chain above replaces it (see section (b)).
gui(_B12_TIDLG, 'TwoFASImporter$EncryptedState.lambda$decrypt$1',
    'Cancel the password dialog (Back or a tap outside): TwoFAS reports the cancel to the page',
    evidence=FW_CANCEL + '; SRC ui/dialogs/Dialogs.java:217-219; SRC importers/TwoFASImporter.java:147')

# (h) UNREACHABLE: the private constructor of the FreeOTP parser is never called; the class is used only through its static parse method (called at FreeOtpImporter.java:108)
UNREACHABLE['FreeOtpImporter$SerializedHashMapParser.<init>'] = ('no_trigger_in_app',
    'no code creates a SerializedHashMapParser: the class is used only through its static parse method, called at FreeOtpImporter.java:108',
    'importers/FreeOtpImporter.java:108,366-370', 'SOURCE')
# UNREACHABLE: nothing calls getText on a DatabaseImporterEntryException; the error dialog takes a generic Throwable list and calls toString (Dialogs.java:445-453)
UNREACHABLE['DatabaseImporterEntryException.getText'] = ('no_trigger_in_app',
    'no code calls getText on a DatabaseImporterEntryException: the error dialog takes a generic Throwable list and calls toString (Dialogs.java:445-453)',
    'importers/DatabaseImporterEntryException.java:16-18', 'SOURCE')

# --- batch 22: the generated Glide request classes (GlideRequest, GlideRequests). The app calls only load (on a RequestManager with a File or a
# VaultEntryIcon; on a builder from asBitmap with a Uri), asBitmap, set, listener, diskCacheStrategy and skipMemoryCache: those are REACHABLE above.
# The Glide library source is not read, so two library paths are INFERRED: into(ImageView) copies the request options and applies one optional
# scale-type option. clone, autoClone, optionalCenterCrop, optionalCenterInside and optionalFitCenter get edges from the two into(ImageView) sites.
# Every other generated method gets an UNREACHABLE entry (one group per reason).
for _src, _ref in [('GlideHelper.loadEntryIcon', 'ui/glide/GlideHelper.java:41'), ('GlideHelper.load', 'ui/glide/GlideHelper.java:54')]:
    for _dst in ['GlideRequest.autoClone', 'GlideRequest.clone', 'GlideRequest.optionalCenterCrop', 'GlideRequest.optionalCenterInside', 'GlideRequest.optionalFitCenter']:
        e(_src, _dst, 'FRAMEWORK',
          'into(ImageView) (Glide library): the scale-type branch copies the request options and applies one optional option, which the generated GlideRequest override runs',
          guard='the ImageView has a scale type that the library maps to this option (INFERRED: library source not read)',
          evidence='INFERRED Glide library RequestBuilder.into(ImageView) (source not read); generated GlideRequest (dataset, not source tree); SRC ' + _ref)

_B22_OPTION = """
GlideRequest.addListener
GlideRequest.centerCrop
GlideRequest.centerInside
GlideRequest.circleCrop
GlideRequest.decode
GlideRequest.disallowHardwareConfig
GlideRequest.dontAnimate
GlideRequest.dontTransform
GlideRequest.downsample
GlideRequest.encodeFormat
GlideRequest.encodeQuality
GlideRequest.error(int)
GlideRequest.error(Drawable)
GlideRequest.error(RequestBuilder)
GlideRequest.error(Object)
GlideRequest.fallback(int)
GlideRequest.fallback(Drawable)
GlideRequest.fitCenter
GlideRequest.format
GlideRequest.frame
GlideRequest.load(Bitmap)
GlideRequest.load(Drawable)
GlideRequest.load(Integer)
GlideRequest.load(String)
GlideRequest.load(URL)
GlideRequest.load(byte[])
GlideRequest.onlyRetrieveFromCache
GlideRequest.optionalCircleCrop
GlideRequest.optionalTransform(Transformation)
GlideRequest.optionalTransform(Class,Transformation)
GlideRequest.override(int)
GlideRequest.override(int,int)
GlideRequest.placeholder(int)
GlideRequest.placeholder(Drawable)
GlideRequest.priority
GlideRequest.signature
GlideRequest.sizeMultiplier
GlideRequest.theme
GlideRequest.thumbnail(float)
GlideRequest.thumbnail(RequestBuilder)
GlideRequest.thumbnail(List)
GlideRequest.thumbnail(RequestBuilder[])
GlideRequest.timeout
GlideRequest.transform(Transformation)
GlideRequest.transform(Class,Transformation)
GlideRequest.transform(Transformation[])
GlideRequest.transforms
GlideRequest.transition
GlideRequest.useAnimationPool
GlideRequest.useUnlimitedSourceGeneratorsPool
""".split()
_B22_OPTION_WHY = ('no_trigger_in_app', 'generated Glide option that no app code calls (grep of the Glide-importing app files: the only Glide calls are load, asBitmap, set, listener, diskCacheStrategy, skipMemoryCache and into); the into(ImageView) path is covered by the edges above (INFERRED)', 'ui/glide/GlideHelper.java:59-67', 'SOURCE')
_B22_LATER = """
GlideRequest.getDownloadOnlyRequest
GlideRequest.apply
GlideRequest.<init>(Class,RequestBuilder)
""".split()
_B22_LATER_WHY = ('no_trigger_in_app', 'download-only helper of the generated GlideRequest: no app code calls download, downloadOnly, asFile or asGif (grep of the Glide-importing app files); auto_calls.json lists it as the caller of apply and <init>(Class,RequestBuilder), and its own generated callers are not in auto_calls.json (INFERRED)', 'ui/glide/GlideHelper.java:59-67', 'INFERRED')
_B22_LOCK_WHY = ('no_trigger_in_app', 'no app code calls lock (grep of the Glide-importing app files) and auto_calls.json has no in-universe caller of GlideRequest.lock; the Glide library may lock an options object internally, which is not read here (INFERRED)', 'ui/glide/GlideHelper.java:59-67', 'INFERRED')
_B22_GR_LOAD = """
GlideRequests.load(Bitmap)
GlideRequests.load(Drawable)
GlideRequests.load(Uri)
GlideRequests.load(Integer)
GlideRequests.load(String)
GlideRequests.load(URL)
GlideRequests.load(byte[])
""".split()
_B22_GR_LOAD_WHY = ('no_trigger_in_app', 'no app code passes a Bitmap, Drawable, Integer, String, URL, byte[] or Uri to a RequestManager load: the seven load calls in the Glide-importing app files pass a File or a VaultEntryIcon to the manager (ui/glide/GlideHelper.java:32,41; ui/AssignIconsActivity.java:237,257; ui/views/EntryListView.java:713; ui/dialogs/IconPickerDialog.java:79), and a Uri only to a builder from asBitmap (ui/EditEntryActivity.java:619)', 'ui/glide/GlideHelper.java:32', 'SOURCE')
_B22_GR_DEFAULT = """
GlideRequests.addDefaultRequestListener
GlideRequests.applyDefaultRequestOptions
GlideRequests.setDefaultRequestOptions
""".split()
_B22_GR_DEFAULT_WHY = ('no_trigger_in_app', 'the app sets no default request options or listeners: AegisGlideModule overrides only registerComponents (ui/glide/AegisGlideModule.java:21-27), and no app code calls setDefaultRequestOptions, applyDefaultRequestOptions or addDefaultRequestListener (grep)', 'ui/glide/AegisGlideModule.java:21-27', 'SOURCE')
_B22_GR_DL = """
GlideRequests.asFile
GlideRequests.asGif
GlideRequests.download
GlideRequests.downloadOnly
""".split()
_B22_GR_DL_WHY = ('no_trigger_in_app', 'no app code calls download, downloadOnly, asFile or asGif (grep of the Glide-importing app files)', 'ui/glide/GlideHelper.java:59-67', 'SOURCE')
_B22_GR_CLEAR = """
GlideRequests.clearOnStop
""".split()
_B22_GR_CLEAR_WHY = ('no_trigger_in_app', 'no app code calls clearOnStop (grep of the Glide-importing app files); the Glide library may call it from the activity lifecycle, which is not read here (INFERRED)', 'ui/glide/GlideHelper.java:59-67', 'INFERRED')
for _group, _why in [
        (_B22_OPTION, _B22_OPTION_WHY), (_B22_LATER, _B22_LATER_WHY), ([ 'GlideRequest.lock' ], _B22_LOCK_WHY),
        (_B22_GR_LOAD, _B22_GR_LOAD_WHY), (_B22_GR_DEFAULT, _B22_GR_DEFAULT_WHY),
        (_B22_GR_DL, _B22_GR_DL_WHY), (_B22_GR_CLEAR, _B22_GR_CLEAR_WHY)]:
    for _m in _group:
        assert _m.split('(')[0] in _UNIV_SHORT, _m
        UNREACHABLE[_m] = _why

# --- batch 23: TransferEntriesActivity (the share page for the QR export). onCreate registers four click listeners and one
# global-layout listener ($1). generateQR and setBrightness were UNRESOLVED only because no path reached those listeners.
# Lambda map (javac order, TransferEntriesActivity.java): $0 Next (:84-96), $1 Previous (:98-108), $2 Copy (:114-132), $3 QR tap (:154-162).
FW_B23_LAYOUT = ('INFERRED android.view ViewTreeObserver: the global-layout listener runs after the window lays out the view '
                 '(framework source not read)')
gui('TransferEntriesActivity.onCreate', 'TransferEntriesActivity.lambda$onCreate$0',
    'Tap Next (shown only when the list has more than one entry; the Done label on the last entry closes the page)',
    guard='the Next button is shown: the list has more than one entry (TransferEntriesActivity.java:81-82)',
    evidence=FW_CLICK + '; SRC ui/TransferEntriesActivity.java:84-96')
# batch 8 (G3 route 2 step 26): the auto row (bytecode, no guard) is suppressed and replaced by one with the guard at line 85
sup(('TransferEntriesActivity.lambda$onCreate$0', 'TransferEntriesActivity.generateQR'))
e('TransferEntriesActivity.lambda$onCreate$0', 'TransferEntriesActivity.generateQR', 'CALL',
  'Tap Next while entries remain: the next QR code is generated',
  guard='_currentEntryCount < _authInfos.size() (TransferEntriesActivity.java:85): the code is generated only while the count is below the list size; otherwise the else branch calls finish (line 94)',
  evidence='SRC ui/TransferEntriesActivity.java:85,88,94')
gui('TransferEntriesActivity.onCreate', 'TransferEntriesActivity.lambda$onCreate$1',
    'Tap Previous (moves back one entry; does nothing on the first entry)',
    guard='the page is past the first entry (the count is above 1, TransferEntriesActivity.java:99)',
    evidence=FW_CLICK + '; SRC ui/TransferEntriesActivity.java:98-108')
gui('TransferEntriesActivity.onCreate', 'TransferEntriesActivity.lambda$onCreate$2',
    'Tap Copy (copies the URI of the selected entry to the clipboard)',
    guard='the copy button is shown: the first entry is a GoogleAuthInfo (TransferEntriesActivity.java:110-112)',
    evidence=FW_CLICK + '; SRC ui/TransferEntriesActivity.java:114-132')
sup(('TransferEntriesActivity.lambda$onCreate$2', 'GoogleAuthInfo$Export.getUri'))
e('TransferEntriesActivity.lambda$onCreate$2', 'GoogleAuthInfo.getUri', 'CALL',
  'Tap Copy: the URI of the selected GoogleAuthInfo entry is copied to the clipboard',
  cls='non_standard', via='Transferable.getUri (interface call; the list holds GoogleAuthInfo items)',
  guard='the copy button is shown: the first entry is a GoogleAuthInfo (TransferEntriesActivity.java:110-112)',
  evidence='SRC ui/TransferEntriesActivity.java:110-118; SRC otp/GoogleAuthInfo.java:22,279')
gui('TransferEntriesActivity.onCreate', 'TransferEntriesActivity.lambda$onCreate$3',
    'Tap the QR code (switches the screen brightness to maximum, and back on the next tap)',
    evidence=FW_CLICK + '; SRC ui/TransferEntriesActivity.java:154-162')
e('TransferEntriesActivity.onCreate', 'TransferEntriesActivity$1.onGlobalLayout', 'FRAMEWORK',
  'the QR image is laid out for the first time: the QR size is set and the QR code is drawn once',
  evidence=FW_B23_LAYOUT + '; SRC ui/TransferEntriesActivity.java:135-151')
gui('TransferEntriesActivity.onCreate', 'TransferEntriesActivity.onOptionsItemSelected',
    'Tap the Up arrow in the transfer toolbar (home item): the page closes',
    evidence=FW_MENU + '; SRC ui/TransferEntriesActivity.java:73-76,183-193')

# --- batch 24: the protobuf (GoogleAuthProtos) internals. The app uses only the nested types (GoogleAuthInfo.java:7,195-204,400-446;
# grep of the app tree), so the outer class members are never called. The other generated methods are called by the protobuf runtime
# (INFERRED, runtime source not read) from the two REACHABLE entry points: parseFrom(byte[]) (import, GoogleAuthInfo.java:198) and
# GoogleAuthInfo$Export.getUri (export, GoogleAuthInfo.java:400-459).
_B24_OUTER = ('no_trigger_in_app', 'no app code uses a member of the outer GoogleAuthProtos class: its only uses are the nested types (grep of the app tree)',
              'otp/GoogleAuthInfo.java:7,195-446', 'SOURCE')
for _m in ['GoogleAuthProtos.<clinit>', 'GoogleAuthProtos.<init>', 'GoogleAuthProtos.registerAllExtensions']:
    assert _m.split('(')[0] in _UNIV_SHORT, _m
    UNREACHABLE[_m] = _B24_OUTER

_B24_RT = ('INFERRED protobuf-lite runtime (its source is not read; the generated GoogleAuthProtos classes are in the dataset, '
           'not the source tree)')
_B24_MP = 'GoogleAuthProtos$MigrationPayload.'
_B24_OP = 'GoogleAuthProtos$MigrationPayload$OtpParameters.'
_B24_PARSE = _B24_MP + 'parseFrom(byte[])'
_B24_EXPORT = 'GoogleAuthInfo$Export.getUri'
e(_B24_PARSE, _B24_MP + 'getDefaultInstance', 'FRAMEWORK', 'the runtime parses the payload from the default instance',
  evidence=_B24_RT + '; SRC otp/GoogleAuthInfo.java:198')
e(_B24_PARSE, _B24_MP + 'dynamicMethod', 'FRAMEWORK', 'the runtime parses the payload with the generated parse method',
  evidence=_B24_RT + '; SRC otp/GoogleAuthInfo.java:198')
e(_B24_PARSE, _B24_MP + 'parser', 'FRAMEWORK', 'the runtime gets the parser of the payload type',
  evidence=_B24_RT + '; SRC otp/GoogleAuthInfo.java:198')
e(_B24_EXPORT, _B24_MP + 'getDefaultInstance', 'FRAMEWORK', 'the export builder starts from the default payload instance',
  evidence=_B24_RT + '; SRC otp/GoogleAuthInfo.java:400')
e(_B24_EXPORT, _B24_MP + 'dynamicMethod', 'FRAMEWORK', 'the built payload is finished and serialized (toByteArray, GoogleAuthInfo.java:459)',
  evidence=_B24_RT + '; SRC otp/GoogleAuthInfo.java:459-460')
e(_B24_MP + 'newBuilder()', 'GoogleAuthProtos$MigrationPayload$Builder.<init>', 'CALL', 'newBuilder creates the payload Builder',
  evidence='INFERRED generated GoogleAuthProtos body (dataset, not in the source tree): newBuilder constructs its Builder; SRC otp/GoogleAuthInfo.java:400')
e(_B24_OP + 'newBuilder()', 'GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.<init>', 'CALL', 'newBuilder creates the OtpParameters Builder',
  evidence='INFERRED generated GoogleAuthProtos body (dataset, not in the source tree): newBuilder constructs its Builder; SRC otp/GoogleAuthInfo.java:407')
# the payload's repeated otp_parameters messages are read and written by the runtime through the payload's dynamicMethod
e(_B24_MP + 'dynamicMethod', _B24_OP + 'dynamicMethod', 'FRAMEWORK', 'the runtime reads or writes each OtpParameters message of the payload',
  evidence=_B24_RT)
e(_B24_MP + 'dynamicMethod', _B24_OP + 'getDefaultInstance', 'FRAMEWORK', 'the runtime starts each OtpParameters message from its default instance',
  evidence=_B24_RT)
e(_B24_MP + 'dynamicMethod', _B24_OP + 'parser', 'FRAMEWORK', 'the runtime gets the OtpParameters parser',
  evidence=_B24_RT)
# the three enum fields of OtpParameters: the runtime maps numbers to enum constants and checks the range with the verifier
for _E, _V in [('Algorithm', 'AlgorithmVerifier'), ('DigitCount', 'DigitCountVerifier'), ('OtpType', 'OtpTypeVerifier')]:
    _EP = 'GoogleAuthProtos$MigrationPayload$' + _E + '.'
    _VP = 'GoogleAuthProtos$MigrationPayload$' + _E + '$' + _V + '.'
    e(_B24_OP + 'dynamicMethod', _EP + 'internalGetValueMap', 'FRAMEWORK', 'the runtime reads the ' + _E + ' enum value map of an OtpParameters field',
      evidence=_B24_RT)
    e(_B24_OP + 'dynamicMethod', _EP + 'internalGetVerifier', 'FRAMEWORK', 'the runtime gets the ' + _E + ' verifier of an OtpParameters field',
      evidence=_B24_RT)
    e(_B24_OP + 'dynamicMethod', 'GoogleAuthProtos$MigrationPayload$' + _E + '$1.findValueByNumber', 'FRAMEWORK', 'the runtime maps the number to a ' + _E + ' constant',
      evidence=_B24_RT)
    e(_B24_OP + 'dynamicMethod', _VP + 'isInRange', 'FRAMEWORK', 'the runtime checks the ' + _E + ' number is in range',
      evidence=_B24_RT)
    e(_EP + 'internalGetVerifier', _VP + '<clinit>', 'LIFECYCLE', 'the ' + _V + ' singleton is created on first use',
      evidence='INFERRED JVM class initialization (JLS 12.4.1): the verifier class is initialized when its singleton is read; generated body (dataset)')
    e(_VP + '<clinit>', _VP + '<init>', 'CALL', 'the ' + _V + ' singleton constructor runs during class initialization',
      evidence='INFERRED generated GoogleAuthProtos body (dataset, not in the source tree): the verifier singleton is created in its static field')

# --- batch 25: the scanner (ScannerActivity, helpers/QrCodeAnalyzer) and its export and single-link helpers. The camera, Guava and
# Handler callbacks are framework or library callbacks (INFERRED: their sources are not read). The chain starts at
# ScannerActivity.onCreate (REACHABLE; the entry edge carries ENV_CAMERA) and ends in GoogleAuthInfo.parseUri / parseExportUri.
_FW_B25_FUTURE = ('INFERRED Guava ListenableFuture.addListener: the listener runs on the given executor (the main executor here) '
                  'when the ProcessCameraProvider future completes (framework and CameraX source not read)')
_FW_B25_POST = ('INFERRED android.os.Handler.post: the runnable runs on the handler looper (the main looper here; '
                'framework source not read)')
_FW_B25_ANALYZE = ('INFERRED androidx.camera ImageAnalysis: setAnalyzer keeps the analyzer, and CameraX calls analyze(ImageProxy) '
                   'on the analysis executor for each camera frame (CameraX source not read)')
_FW_B25_TOSTRING = ('INFERRED java.lang.Throwable.toString: it builds the text from getLocalizedMessage(), which returns getMessage() '
                    '(JDK source not read)')
_B25_SC = 'ScannerActivity.'
_B25_QA = 'QrCodeAnalyzer.'
_B25_OPEN = 'the scanner is open and the camera is bound (ScannerActivity.java:177-181)'
_B25_BAD = 'the QR code cannot be read as an import: GoogleAuthInfoException is caught (ScannerActivity.java:189-194)'
_B25_NEXT = 'the scanned batch index follows the previous one (ScannerActivity.java:219)'

# the scanner opens: the camera provider future completes on the main thread, the lenses are listed, the preview is bound
e(_B25_SC + 'onCreate', _B25_SC + 'lambda$onCreate$0', 'FRAMEWORK',
  'the camera provider is ready: the future listener runs on the main thread (on failure it throws at ScannerActivity.java:74 and sets no lens)',
  guard='onCreate did not abort (ScannerActivity.java:55-57; AegisActivity.java:154-157)',
  evidence=_FW_B25_FUTURE + '; SRC ui/ScannerActivity.java:67-68,74,88')
e(_B25_SC + 'lambda$onCreate$0', _B25_SC + 'addCamera', 'CALL',
  'the back lens and then the front lens are checked for a camera',
  evidence='SRC ui/ScannerActivity.java:77-78')
e(_B25_SC + 'lambda$onCreate$0', _B25_SC + 'updateCameraIcon', 'CALL',
  'the first lens is chosen and the camera switch icon is set',
  guard='at least one lens exists (ScannerActivity.java:79-83 finish the page otherwise)',
  evidence='SRC ui/ScannerActivity.java:84-85')
e(_B25_SC + 'lambda$onCreate$0', _B25_SC + 'bindPreview', 'CALL',
  'the preview and the QR analyzer are bound to the camera',
  guard='at least one lens exists (ScannerActivity.java:79-83 finish the page otherwise)',
  evidence='SRC ui/ScannerActivity.java:87')
e(_B25_SC + 'onCreate', _B25_SC + 'onCreateOptionsMenu', 'FRAMEWORK',
  'the toolbar menu is created after onCreate (it holds the camera switch item)',
  evidence=FW_OPTIONS + '; SRC ui/ScannerActivity.java:100-104')
# the camera switch works only after the camera provider listener has run: the listener enters the scanner page variant, and the tap starts there
e(_B25_SC + 'onCreate', 'S_SCANNER', 'ENTERS', 'the scanner page is shown after onCreate',
  guard='onCreate did not abort (ScannerActivity.java:55-57)', evidence='SRC ui/ScannerActivity.java:53-62')
e(_B25_SC + 'lambda$onCreate$0', 'S_SCANNER@CAMERA_READY', 'ENTERS', 'the camera provider is ready and a lens exists: the camera switch icon can be tapped',
  guard='onCreate did not abort (ScannerActivity.java:55-57) and a lens exists (ScannerActivity.java:79-83 finish the page otherwise)', evidence='SRC ui/ScannerActivity.java:70,77-87')
gui('S_SCANNER@CAMERA_READY', _B25_SC + 'onOptionsItemSelected', 'Tap the camera switch icon in the scanner toolbar: the other lens is used',
    guard='the camera provider is set (ScannerActivity.java:108-110 return early until then) and the icon is shown (two lenses, ScannerActivity.java:137-148)',
    needs_state=ST_CAMERA_READY, evidence=FW_MENU + '; SRC ui/ScannerActivity.java:107-118,134-150')
e(_B25_SC + 'onOptionsItemSelected', _B25_SC + 'unbindPreview', 'CALL', 'the camera switch: the current preview is unbound',
  guard='the camera provider is set (ScannerActivity.java:108-110 return early otherwise) and the tapped item is the camera switch (ScannerActivity.java:112)', evidence='SRC ui/ScannerActivity.java:108-113')
e(_B25_SC + 'onOptionsItemSelected', _B25_SC + 'bindPreview', 'CALL', 'the camera switch: the preview is bound again with the other lens',
  guard='the tapped item is the camera switch (ScannerActivity.java:112)', evidence='SRC ui/ScannerActivity.java:114-115')
e(_B25_SC + 'onOptionsItemSelected', _B25_SC + 'updateCameraIcon', 'CALL', 'the camera switch: the icon is set for the lens that the next tap selects',
  guard='the tapped item is the camera switch (ScannerActivity.java:112)', evidence='SRC ui/ScannerActivity.java:116')
e(_B25_SC + 'onCreate', _B25_SC + 'onDestroy', 'LIFECYCLE',
  'the scanner closes (finish or Back): the framework calls onDestroy, which shuts the camera executor down',
  guard='onCreate did not abort (ScannerActivity.java:55-57)',
  evidence='INFERRED Activity lifecycle: onDestroy follows onCreate (framework source not read); SRC ui/ScannerActivity.java:92-94')
e(_B25_SC + 'onDestroy', 'AegisActivity.onDestroy', 'CALL', 'the base activity closes after the executor is shut down',
  evidence='SRC ui/ScannerActivity.java:96')

# the camera analyzer: the class is initialized when bindPreview reads RESOLUTION; CameraX then calls analyze for each frame
e(_B25_SC + 'bindPreview', _B25_QA + '<clinit>', 'LIFECYCLE', 'the RESOLUTION constant is read: the analyzer class is initialized',
  evidence='INFERRED JVM class initialization (JLS 12.4.1): reading a static field starts the class initialization; SRC ui/ScannerActivity.java:161; SRC helpers/QrCodeAnalyzer.java:20')
e(_B25_SC + 'bindPreview', _B25_QA + '<init>', 'CALL', 'the analyzer is created with the scanner as its listener',
  evidence='SRC ui/ScannerActivity.java:164; SRC helpers/QrCodeAnalyzer.java:24-26')
e(_B25_SC + 'bindPreview', _B25_QA + 'analyze', 'FRAMEWORK', 'CameraX delivers each camera frame to the analyzer that bindPreview set (a QR code is in view)',
  env=ENV_QR_CODE, evidence=_FW_B25_ANALYZE + '; SRC ui/ScannerActivity.java:164; SRC helpers/QrCodeAnalyzer.java:29')
e(_B25_QA + 'analyze', 'QrCodeHelper.decodeFromSource', 'CALL', 'the camera frame is decoded to a QR code',
  guard='the frame has the YUV_420_888 format (QrCodeAnalyzer.java:31-35 return otherwise)',
  evidence='SRC helpers/QrCodeAnalyzer.java:55')
e(_B25_QA + 'analyze', _B25_SC + 'onQrCodeDetected', 'CALL', 'a QR code is decoded: the scanner receives the result (the listener is the scanner itself)',
  guard='the frame is YUV_420_888 (QrCodeAnalyzer.java:31-34) and the listener is set (QrCodeAnalyzer.java:56); the frame decodes (QrCodeAnalyzer.java:55-58; a NotFoundException at line 59 skips the call)',
  evidence='SRC helpers/QrCodeAnalyzer.java:55-58; SRC ui/ScannerActivity.java:36,175')

# a QR result is posted to the main thread: the export link goes to handleExportUri, a single link to handleUri, a failed read to the error dialog
e(_B25_SC + 'onQrCodeDetected', _B25_SC + 'lambda$onQrCodeDetected$2', 'FRAMEWORK',
  'the QR result is posted to the main thread',
  evidence=_FW_B25_POST + '; SRC ui/ScannerActivity.java:175-176')
e(_B25_SC + 'lambda$onQrCodeDetected$2', _B25_SC + 'handleExportUri', 'CALL', 'the QR code is an export link: the batch is handled',
  guard=_B25_OPEN + '; the text uses the export scheme (ScannerActivity.java:184)',
  evidence='SRC ui/ScannerActivity.java:183-185')
e(_B25_SC + 'lambda$onQrCodeDetected$2', _B25_SC + 'handleUri', 'CALL', 'the QR code is a single entry link: the entry is handled',
  guard=_B25_OPEN + '; the text uses another scheme (ScannerActivity.java:184,186-187)',
  evidence='SRC ui/ScannerActivity.java:183-187')
e(_B25_SC + 'lambda$onQrCodeDetected$2', _B25_SC + 'unbindPreview', 'CALL',
  'the QR code cannot be read: the camera is unbound while the error dialog is open',
  guard=_B25_OPEN + '; ' + _B25_BAD, evidence='SRC ui/ScannerActivity.java:189-192')
e(_B25_SC + 'lambda$onQrCodeDetected$2', 'GoogleAuthInfoException.isPhoneFactor', 'CALL',
  'the error text is picked: the phonefactor text when the link is a phonefactor link',
  guard=_B25_OPEN + '; ' + _B25_BAD, evidence='SRC ui/ScannerActivity.java:195; SRC otp/GoogleAuthInfoException.java:26-28')
e(_B25_SC + 'lambda$onQrCodeDetected$2', 'Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)@SCANNER_ERROR', 'CALL',
  'the error dialog opens with the exception text; its OK button restarts the camera',
  guard=_B25_OPEN + '; ' + _B25_BAD, evidence='SRC ui/ScannerActivity.java:194-196')
# scanner-error variant of the error-dialog overload chain (Dialogs.java:367-376). The plain delegations are
# auto edges, and a hand variant->variant delegation suppresses the plain auto edge (base-pair rule),
# so the plain delegations are re-written by hand here to keep the other error dialogs intact.
# Only the scanner error branch reaches the @SCANNER_ERROR chain; its OK relay goes only to the scanner lambda.
e('Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)', 'Dialogs.showErrorDialog(Context,int,CharSequence,OnClickListener)', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:368 (bytecode)')
e('Dialogs.showErrorDialog(Context,int,CharSequence,OnClickListener)', 'Dialogs.showErrorDialog(Context,String,CharSequence,OnClickListener)', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:376 (bytecode)')
e('Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)@SCANNER_ERROR', 'Dialogs.showErrorDialog(Context,int,CharSequence,OnClickListener)@SCANNER_ERROR', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:368 (bytecode)')
e('Dialogs.showErrorDialog(Context,int,CharSequence,OnClickListener)@SCANNER_ERROR', 'Dialogs.showErrorDialog(Context,String,CharSequence,OnClickListener)@SCANNER_ERROR', 'CALL',
  'Direct call', evidence='SRC Dialogs.java:376 (bytecode)')
gui('Dialogs.showErrorDialog(Context,String,CharSequence,OnClickListener)@SCANNER_ERROR', 'Dialogs.lambda$showErrorDialog$15@SCANNER_ERROR', 'Tap OK in the error dialog',
  evidence=FW_CLICK + '; SRC ui/dialogs/Dialogs.java:391-395')
e('Dialogs.lambda$showErrorDialog$15@SCANNER_ERROR', _B25_SC + 'lambda$onQrCodeDetected$1', 'CALL',
  'Tap OK in the scanner error dialog: the preview restarts',
  cls='non_standard', via='DialogInterface.OnClickListener.onClick (Dialogs.java:391-393; listener at ScannerActivity.java:196)',
  needs_state=ST_CAMERA_READY,
  evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ui/ScannerActivity.java:194-196')
e('Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)', 'GoogleAuthInfoException.getMessage', 'FRAMEWORK',
  'the error dialog builds its text with e.toString(), which calls the exception getMessage',
  guard=_B25_BAD, evidence=_FW_B25_TOSTRING + '; SRC ui/dialogs/Dialogs.java:368; SRC otp/GoogleAuthInfoException.java:31-40')
# the fifth error dialog that passes a page listener (the scanner's): its OK button runs the listener, which binds the camera again
# deleted: the plain $15 relay never delivers to the Scanner lambda (that was
# route 04 step 12). The @SCANNER_ERROR relay above replaces it.
e(_B25_SC + 'lambda$onQrCodeDetected$1', _B25_SC + 'bindPreview', 'CALL', 'the camera is bound again after the error dialog',
  evidence='SRC ui/ScannerActivity.java:196')
# the same OK relay serves the two error dialogs that MainActivity.onStart opens; each relay edge goes to the lambda that closes the app
e('Dialogs.lambda$showErrorDialog$15', 'MainActivity.lambda$onStart$21', 'CALL', 'Tap OK in the vault-load error dialog (the app closes)',
  guard='the dialog was opened by the vault-read error in onStart (MainActivity.java:954-960); the OK relay is shared by all error dialogs',
  cls='non_standard', via='DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at MainActivity.java:957-959)',
  evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ui/MainActivity.java:954-959')
e('Dialogs.lambda$showErrorDialog$15', 'MainActivity.lambda$onStart$22', 'CALL', 'Tap OK in the plaintext vault error dialog (the app closes)',
  guard='the dialog was opened by the plain-text load error in onStart (MainActivity.java:966-971); the OK relay is shared by all error dialogs',
  cls='non_standard', via='DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at MainActivity.java:968-970)',
  evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ui/MainActivity.java:963-972')

# the export batch and the single link: the parsers are GoogleAuthInfo methods (their own edges are in the GoogleAuthInfo batches), and the page closes
e(_B25_SC + 'handleExportUri', 'GoogleAuthInfo.parseExportUri(Uri)', 'CALL', 'the export link is parsed into a batch of entries',
  evidence='SRC ui/ScannerActivity.java:210')
e('GoogleAuthInfo.parseExportUri(Uri)', 'GoogleAuthProtos$MigrationPayload.parseFrom(byte[])', 'CALL',
  'the export payload is parsed from the link data (protobuf)',
  guard='scheme equals SCHEME_EXPORT (GoogleAuthInfo.java:181-183); host equals "offline" (185-188); data parameter not null (190-193)',
  evidence='SRC otp/GoogleAuthInfo.java:181-198')
e(_B25_SC + 'handleExportUri', 'GoogleAuthInfo$Export.getBatchId', 'CALL', 'the batch id is read (the first scanned code sets it)',
  evidence='SRC ui/ScannerActivity.java:213,217')
e(_B25_SC + 'handleExportUri', 'GoogleAuthInfo$Export.getBatchIndex', 'CALL', 'the index of the scanned code in the batch is read',
  evidence='SRC ui/ScannerActivity.java:216')
e(_B25_SC + 'handleExportUri', 'GoogleAuthInfo$Export.getEntries', 'CALL', 'the entries of the scanned code are added to the list',
  guard=_B25_NEXT, evidence='SRC ui/ScannerActivity.java:220')
e(_B25_SC + 'handleExportUri', 'VaultEntry.<init>(GoogleAuthInfo)', 'CALL', 'each entry of the scanned code becomes a vault entry',
  guard=_B25_NEXT, evidence='SRC ui/ScannerActivity.java:221')
e(_B25_SC + 'handleExportUri', 'GoogleAuthInfo$Export.getBatchSize', 'CALL', 'the batch size is read for the progress text and the last-code check',
  guard=_B25_NEXT, evidence='SRC ui/ScannerActivity.java:226,230')
e(_B25_SC + 'handleExportUri', _B25_SC + 'finish', 'CALL', 'the last code of the batch is scanned: all entries are returned and the page closes',
  guard='the batch id matches (ScannerActivity.java:217); the first code of this scanner session or the next index (219); and it is the last code of its batch (226-227): with no earlier code in this session the scanned code must be the last one of its batch (ENV_QR_CODE)',
  evidence='SRC ui/ScannerActivity.java:212-227')
e(_B25_SC + 'handleUri', 'GoogleAuthInfo.parseUri(Uri)', 'CALL', 'the single entry link is parsed',
  evidence='SRC ui/ScannerActivity.java:203')
e(_B25_SC + 'handleUri', 'VaultEntry.<init>(GoogleAuthInfo)', 'CALL', 'the parsed entry becomes a vault entry',
  evidence='SRC ui/ScannerActivity.java:205')
e(_B25_SC + 'handleUri', _B25_SC + 'finish', 'CALL', 'the entry is returned and the page closes',
  evidence='SRC ui/ScannerActivity.java:206')

# the String overload of parseExportUri: no app code calls it (its callers pass a Uri)
assert 'GoogleAuthInfo.parseExportUri' in _UNIV_SHORT, 'GoogleAuthInfo.parseExportUri'
UNREACHABLE['GoogleAuthInfo.parseExportUri(String)'] = ('no_trigger_in_app',
    'no app code calls the String overload (grep of the app tree: MainActivity.java:683 and ScannerActivity.java:210 pass a Uri)',
    'otp/GoogleAuthInfo.java:171-176', 'SOURCE')

# --- batch 26: the icon picker (ui/dialogs/IconPickerDialog.java, ui/views/IconAdapter.java, IconHolder, IconCategoryHolder, IconRecyclerView).
# The picker opens from EditEntryActivity.startIconSelection (EditEntryActivity.java:594) and AssignIconsActivity.java:194, and it is REACHABLE.
# The bytecode rows (auto_calls.json) already give the CALL edges between these methods (for example IconPickerDialog.create -> IconAdapter.loadIcons,
# and the adapter click lambdas -> the listener methods), so this block writes only the framework entries that start them.
_B26_CR = 'IconPickerDialog.create'
_B26_LI = 'IconAdapter.loadIcons'
_B26_OBV = 'IconAdapter.onBindViewHolder'
_B26_GIC = 'IconAdapter.getItemCount'
_B26_GCA = 'IconAdapter.getCategoryAt'
_FW_B26_INFLATE = ('INFERRED LayoutInflater creates each view named in an XML layout through its (Context,AttributeSet) constructor '
                   '(framework source not read)')
_FW_B26_WATCH = 'INFERRED android.widget.TextView calls the TextWatcher methods on each change of its text (framework source not read)'
_FW_B26_FOCUS = 'INFERRED View.OnFocusChangeListener is called when the focus of the view changes (android.view source not read)'
_FW_B26_POPUP = 'INFERRED androidx.appcompat PopupMenu: a tap on a popup row calls its OnMenuItemClickListener (AppCompat source not read)'
_FW_B26_SPAN = ('INFERRED androidx.recyclerview GridLayoutManager: it asks the SpanSizeLookup for the span of each row while it lays out '
                'the grid (source not read)')
_FW_B26_STREAM = ('INFERRED java.util.stream: a terminal operation (findFirst, sum) runs the filter and map lambdas for each element '
                  '(JDK source not read)')
_FW_B26_CMP = ('INFERRED java.util.Comparator.thenComparing: the composed comparator calls the first comparator, then the key extractor, '
               'for each pair (JDK source not read)')
_FW_B26_MEASURE = 'INFERRED android.view.View.measure calls onMeasure during the layout pass (framework source not read)'

# the adapter's row callbacks: loadIcons ends with notifyDataSetChanged (IconAdapter.java:90), so the grid asks the adapter for its rows
e(_B26_LI, 'IconAdapter.onCreateViewHolder', 'FRAMEWORK', 'the grid asks for a row view after the data changes',
  evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,159-164')
e(_B26_LI, 'IconAdapter.onBindViewHolder', 'FRAMEWORK', 'the grid fills a row view after the data changes',
  evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,166-168')
e(_B26_LI, 'IconAdapter.getItemCount', 'FRAMEWORK', 'the grid asks how many rows there are after the data changes',
  evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,201-203')
e(_B26_LI, 'IconAdapter.getItemViewType', 'FRAMEWORK', 'the grid asks the view type of each row after the data changes',
  evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,215-222')

# loadIcons sorts with a composed comparator (IconAdapter.java:48-53): the first comparator is a lambda, the key extractor is a method reference
e(_B26_LI, 'IconAdapter.lambda$loadIcons$0', 'FRAMEWORK', 'Collections.sort compares two icons by their category',
  evidence=_FW_B26_CMP + '; SRC ui/views/IconAdapter.java:48-53')
e(_B26_LI, 'IconPack$Icon.getName', 'FRAMEWORK', 'Collections.sort compares two icons by their name when their categories are equal',
  evidence=_FW_B26_CMP + '; SRC ui/views/IconAdapter.java:53')

# the stream terminal operations run their lambdas (IconAdapter.java:113-116 and 207-210)
e(_B26_GCA, 'IconAdapter.lambda$getCategoryAt$1', 'FRAMEWORK', 'findFirst runs the filter on each category header',
  evidence=_FW_B26_STREAM + '; SRC ui/views/IconAdapter.java:113-116')
e(_B26_GIC, 'IconAdapter.lambda$getItemCount$4', 'FRAMEWORK', 'sum runs the filter on each category header',
  evidence=_FW_B26_STREAM + '; SRC ui/views/IconAdapter.java:207-210')
e(_B26_GIC, 'IconAdapter.lambda$getItemCount$5', 'FRAMEWORK', 'sum maps each open category to its icon count',
  guard='the category is not collapsed (IconAdapter.java:208)',
  evidence=_FW_B26_STREAM + '; SRC ui/views/IconAdapter.java:207-210')

# the row click listeners are set in onBindViewHolder (IconAdapter.java:173-179 for an icon, 184-197 for a category header)
gui(_B26_OBV, 'IconAdapter.lambda$onBindViewHolder$2', 'Tap an icon in the grid',
    guard='the row is an icon row (IconAdapter.java:168-169)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:173-179')
gui(_B26_OBV, 'IconAdapter.lambda$onBindViewHolder$3', 'Tap a category header in the grid to collapse or expand it',
    guard='the row is a category header (IconAdapter.java:180-181)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:184-197')

# IconPickerDialog.create: the focus, icon pack and popup lambdas (IconPickerDialog.java:85-90 and 130-154); javac numbers the
# inner popup lambda first, so lambda$create$1 is the popup item and lambda$create$2 is the icon pack button (see the bytecode rows)
gui(_B26_CR, 'IconPickerDialog.lambda$create$0', 'Tap the icon search box (it takes focus and the sheet expands)',
    evidence=_FW_B26_FOCUS + '; SRC ui/dialogs/IconPickerDialog.java:85-90')
gui(_B26_CR, 'IconPickerDialog.lambda$create$2', 'Tap the icon pack name button above the grid',
    evidence=FW_CLICK + '; SRC ui/dialogs/IconPickerDialog.java:130-134')
gui('IconPickerDialog.lambda$create$2', 'IconPickerDialog.lambda$create$1', 'Tap an icon pack name in the popup menu',
    evidence=_FW_B26_POPUP + '; SRC ui/dialogs/IconPickerDialog.java:135-147')

# the search box watcher (IconPickerDialog.java:91-107): the text view calls each of its three methods on a change
gui(_B26_CR, 'IconPickerDialog$2.beforeTextChanged', 'Type in the icon search box (the watcher runs before the text changes)',
    evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91-96')
gui(_B26_CR, 'IconPickerDialog$2.onTextChanged', 'Type in the icon search box (the watcher runs as the text changes)',
    evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91,97-101')
gui(_B26_CR, 'IconPickerDialog$2.afterTextChanged', 'Type in the icon search box (the watcher runs after the text changes)',
    evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91,103-106')

# the preloader is a scroll listener (IconPickerDialog.java:109-111 and 126): a scroll asks it for the icons about to show
gui(_B26_CR, 'IconPickerDialog$1IconPreloadProvider.getPreloadItems',
    'Scroll the icon grid (the preloader asks which icons are about to show, so their images load early)',
    evidence=FW_SCROLL + '; INFERRED Glide RecyclerViewPreloader: onScrolled asks the model provider for the items '
             '(library source not read); SRC ui/dialogs/IconPickerDialog.java:67-74,109-111,126')
gui(_B26_CR, 'IconPickerDialog$1IconPreloadProvider.getPreloadRequestBuilder',
    'Scroll the icon grid: the preloader builds the request for each icon it was given',
    guard='the icon was returned by getPreloadItems (IconPickerDialog.java:70-73)',
    evidence='INFERRED Glide RecyclerViewPreloader: it builds a request for each item that getPreloadItems returned '
             '(library source not read); SRC ui/dialogs/IconPickerDialog.java:76-81')

# the grid's span lookup (IconPickerDialog.java:114-123): the grid layout asks it for the span of each row
e(_B26_CR, 'IconPickerDialog$3.getSpanSize', 'FRAMEWORK', 'the grid layout asks for the span of each row when it lays out the picker',
  evidence=_FW_B26_SPAN + '; SRC ui/dialogs/IconPickerDialog.java:114-123')

# the picker layout names the IconRecyclerView grid (dialog_icon_picker.xml:65); the inflater builds it through the two-argument constructor
e(_B26_CR, 'IconRecyclerView.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflating the picker layout creates the icon grid',
  evidence=_FW_B26_INFLATE + '; SRC ui/dialogs/IconPickerDialog.java:43,112; SRC res/layout/dialog_icon_picker.xml:65')
e(_B26_CR, 'IconRecyclerView.onMeasure', 'FRAMEWORK', 'the bottom sheet measures the icon grid when it lays out the picker',
  evidence=_FW_B26_MEASURE + '; SRC ui/views/IconRecyclerView.java:49-56')

# batch-26 UNREACHABLE: constructors that no app code and no inflater path calls
assert 'IconPickerDialog.<init>' in _UNIV_SHORT, 'IconPickerDialog.<init>'
assert 'IconRecyclerView.<init>' in _UNIV_SHORT, 'IconRecyclerView.<init>'
UNREACHABLE['IconPickerDialog.<init>'] = ('no_trigger_in_app',
    'private constructor of a static helper: no app code creates an IconPickerDialog (grep of the app tree: the only match is the constructor at IconPickerDialog.java:38); the class is used only through its static create method',
    'ui/dialogs/IconPickerDialog.java:38-40', 'SOURCE')
UNREACHABLE['IconRecyclerView.<init>(Context)'] = ('no_trigger_in_app',
    'no app code creates an IconRecyclerView with one argument (grep of the app tree: no new IconRecyclerView); the layout inflater uses the two-argument constructor',
    'ui/views/IconRecyclerView.java:19-22', 'SOURCE')
UNREACHABLE['IconRecyclerView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'LayoutInflater builds an XML view only through its (Context,AttributeSet) constructor (framework source not read), and no app code calls this three-argument constructor (grep of the app tree: no new IconRecyclerView)',
    'ui/views/IconRecyclerView.java:29-32', 'INFERRED')

# --- batch 27: the assign-icons page (ui/AssignIconsActivity.java, ui/views/AssignIconAdapter.java, ui/views/AssignIconHolder.java).
# The page opens from MainActivity.startAssignIconsActivity (MainActivity.java:522-524) and ImportEntriesActivity.java:322, and its onCreate is
# reached through LIFECYCLE (batch 3). The bytecode rows (auto_calls.json) already give the CALL edges between these methods, so this block
# writes only the framework entries that start them: the list's adapter callbacks, the row and reset taps, the preload providers, the item
# decoration, the toolbar menu, and the discard prompt buttons.
_B27_ON = 'AssignIconsActivity.onCreate'
_B27_DISCARD = 'AssignIconsActivity.discardAndFinish'
_B27_OBV = 'AssignIconAdapter.onBindViewHolder'
_FW_B27_LAYOUT = ('INFERRED androidx.recyclerview: the list asks its adapter for the row count, then creates and binds the visible rows, '
                  'during the first layout pass after setAdapter (framework source not read)')
_FW_B27_PRELOAD = ('INFERRED Glide RecyclerViewPreloader: onScrolled asks the model provider for the items to preload '
                   '(Glide source not read)')
_FW_B27_PRELOAD_RB = ('INFERRED Glide RecyclerViewPreloader: it builds a request for each item that getPreloadItems returned '
                      '(Glide source not read)')

# the list gets its adapter at AssignIconsActivity.java:90 and its entries at line 113, before the first layout pass
e(_B27_ON, 'AssignIconAdapter.getItemCount', 'FRAMEWORK', 'the list asks how many entries there are before it lays out the rows',
  evidence=_FW_B27_LAYOUT + '; SRC ui/AssignIconsActivity.java:90,113; SRC ui/views/AssignIconAdapter.java:46-49')
e(_B27_ON, 'AssignIconAdapter.onCreateViewHolder', 'FRAMEWORK', 'the list creates a row view for each visible entry',
  evidence=_FW_B27_LAYOUT + '; SRC ui/AssignIconsActivity.java:90; SRC ui/views/AssignIconAdapter.java:29-35')
e(_B27_ON, _B27_OBV, 'FRAMEWORK', 'the list fills each visible row with its entry',
  evidence=_FW_B27_LAYOUT + '; SRC ui/AssignIconsActivity.java:90,113; SRC ui/views/AssignIconAdapter.java:38-44')

# the row tap (AssignIconAdapter.java:40-42) is set when a row is bound; the reset tap (AssignIconHolder.java:34) is set when a row view is built
gui(_B27_OBV, 'AssignIconAdapter.lambda$onBindViewHolder$0', 'Tap an entry row (opens the icon picker for that entry)',
    evidence=FW_CLICK + '; SRC ui/views/AssignIconAdapter.java:40-42')
gui('AssignIconHolder.<init>', 'AssignIconHolder.lambda$new$0', 'Tap the reset icon on a row (clears the new icon)',
    guard='the reset button is shown, which needs a new icon (AssignIconHolder.java:54)',
    evidence=FW_CLICK + '; SRC ui/views/AssignIconHolder.java:34')

# the two preload providers and the item decoration are set up in onCreate (AssignIconsActivity.java:80-94)
gui(_B27_ON, 'AssignIconsActivity$EntryIconPreloadProvider.getPreloadItems',
    'Scroll the entry list (the preloader asks which entry icons are about to show, so they load early)',
    evidence=FW_SCROLL + '; ' + _FW_B27_PRELOAD + '; SRC ui/AssignIconsActivity.java:81,84,93,225-231')
gui(_B27_ON, 'AssignIconsActivity$EntryIconPreloadProvider.getPreloadRequestBuilder',
    'Scroll the entry list: the preloader builds the request for each entry icon it was given',
    guard='the item was returned by getPreloadItems (the entry has an icon, AssignIconsActivity.java:227)',
    evidence=_FW_B27_PRELOAD_RB + '; SRC ui/AssignIconsActivity.java:235-238')
gui(_B27_ON, 'AssignIconsActivity$IconPreloadProvider.getPreloadItems',
    'Scroll the entry list (the preloader asks which chosen icons are about to show)',
    evidence=FW_SCROLL + '; ' + _FW_B27_PRELOAD + '; SRC ui/AssignIconsActivity.java:80,83,93,245-251')
gui(_B27_ON, 'AssignIconsActivity$IconPreloadProvider.getPreloadRequestBuilder',
    'Scroll the entry list: the preloader builds the request for each chosen icon it was given',
    guard='the item was returned by getPreloadItems (the entry has a new icon, AssignIconsActivity.java:247)',
    evidence=_FW_B27_PRELOAD_RB + '; SRC ui/AssignIconsActivity.java:255-258')
e(_B27_ON, 'AssignIconsActivity$SpacesItemDecoration.getItemOffsets', 'FRAMEWORK',
  'the list asks each row for its spacing when it lays out the rows',
  evidence=FW_DECOR + '; SRC ui/AssignIconsActivity.java:92,270-279')

# the toolbar menu: the framework inflates it after onCreate (AssignIconsActivity.java:164-168), and a menu tap calls onOptionsItemSelected (170-186)
e(_B27_ON, 'AssignIconsActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is created after onCreate (the Save action and the Up arrow)',
  evidence=FW_OPTIONS + '; SRC ui/AssignIconsActivity.java:164-168')
gui('AssignIconsActivity.onCreateOptionsMenu', 'AssignIconsActivity.onOptionsItemSelected', 'Tap Save or the Up arrow in the toolbar',
    evidence=FW_MENU + '; SRC ui/AssignIconsActivity.java:170-186')

# the discard prompt (Dialogs.showDiscardDialog, Dialogs.java:111-118) gives the positive button onSave and the negative button onDiscard
gui(_B27_DISCARD, 'AssignIconsActivity.lambda$discardAndFinish$0', 'Tap Save in the discard prompt (saves the icons, then closes the page)',
    evidence=FW_CLICK + '; SRC ui/AssignIconsActivity.java:153-160; SRC ui/dialogs/Dialogs.java:116')
gui(_B27_DISCARD, 'AssignIconsActivity.lambda$discardAndFinish$1', 'Tap Discard in the discard prompt (closes the page without saving)',
    evidence=FW_CLICK + '; SRC ui/AssignIconsActivity.java:161; SRC ui/dialogs/Dialogs.java:117')

# batch-27 UNREACHABLE: the back-press callback is built disabled (super(false), AssignIconsActivity.java:212-213) and no code enables it
# (grep of the file: _backPressHandler appears only at lines 52, 77 and 78), so the back dispatcher does not run handleOnBackPressed
assert 'AssignIconsActivity$BackPressHandler.handleOnBackPressed' in _UNIV_SHORT, 'AssignIconsActivity$BackPressHandler.handleOnBackPressed'
UNREACHABLE['AssignIconsActivity$BackPressHandler.handleOnBackPressed'] = ('framework_never_calls',
    'the back-press callback is built disabled (super(false), AssignIconsActivity.java:212-213) and no code enables it (grep of the file: _backPressHandler is used only at lines 52, 77 and 78), so the back dispatcher does not run it (androidx source not read)',
    'ui/AssignIconsActivity.java:211-219', 'INFERRED')

# --- batch 28: the export groups dropdown (DropdownCheckBoxes) and the text icon (TextDrawable, TextDrawableHelper)
_FW_B28_POPUP = ('INFERRED AutoCompleteTextView popup: a tap on the field shows the popup, which asks its adapter for the row count, '
                 'the item and the item id, then draws each row through getView (AppCompat source not read)')
_FW_B28_BOX = ('INFERRED CompoundButton.OnCheckedChangeListener: a tap on a row checkbox calls onCheckedChanged '
               '(Android source not read)')
_FW_B28_DRAW = ('INFERRED android.widget.ImageView: it draws the drawable it holds (setImageDrawable) and asks the drawable '
                'for its intrinsic size when it measures the view (framework source not read)')
_FW_B28_OPAQUE = ('INFERRED android.widget.ImageView: it asks the drawable for its opacity while it prepares to draw it '
                  '(framework source not read; this route is not checked against the source)')

# the groups dropdown is created by LayoutInflater when startExport inflates the dialog (ImportExportPreferencesFragment.java:170, dialog_export.xml:94)
e('ImportExportPreferencesFragment.startExport', 'DropdownCheckBoxes.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the export dialog is inflated, which creates the groups dropdown from its XML element',
  evidence=_FW_B26_INFLATE + '; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:170; SRC res/layout/dialog_export.xml:94')
# a tap on the field opens the popup, which asks the adapter (set in initialise, line 54) for its rows
gui('DropdownCheckBoxes.initialise', 'DropdownCheckBoxes$CheckboxAdapter.getView', 'Tap the groups field (the popup opens and draws the group rows)',
    evidence=_FW_B28_POPUP + '; SRC ui/components/DropdownCheckBoxes.java:54,130-153')
e('DropdownCheckBoxes.initialise', 'DropdownCheckBoxes$CheckboxAdapter.getCount', 'FRAMEWORK', 'the popup asks how many group rows there are',
  evidence=_FW_B28_POPUP + '; SRC ui/components/DropdownCheckBoxes.java:54,115-117')
e('DropdownCheckBoxes.initialise', 'DropdownCheckBoxes$CheckboxAdapter.getItem', 'FRAMEWORK', 'the popup asks for the group behind each row',
  evidence=_FW_B28_POPUP + '; SRC ui/components/DropdownCheckBoxes.java:54,120-122')
e('DropdownCheckBoxes.initialise', 'DropdownCheckBoxes$CheckboxAdapter.getItemId', 'FRAMEWORK', 'the popup asks for the id of each row',
  evidence=_FW_B28_POPUP + '; SRC ui/components/DropdownCheckBoxes.java:54,125-127')
# ticking a row runs the checkbox listener (line 142), which adds or removes that group from the checked set
gui('DropdownCheckBoxes$CheckboxAdapter.getView', 'DropdownCheckBoxes$CheckboxAdapter.lambda$getView$0',
    'Tick or untick a group row (adds or removes that group from the checked set)',
    evidence=_FW_B28_BOX + '; SRC ui/components/DropdownCheckBoxes.java:142-150')

# the text icon is drawn and measured by the image view it is set on (three callers set it: GlideHelper.java:49, EditEntryActivity.java:556 and :962)
for _src, _ref in [('GlideHelper.loadEntryIcon', 'ui/glide/GlideHelper.java:49'),
                   ('EditEntryActivity.onOptionsItemSelected', 'ui/EditEntryActivity.java:556'),
                   ('EditEntryActivity.lambda$new$26', 'ui/EditEntryActivity.java:962')]:
    e(_src, 'TextDrawable.draw', 'FRAMEWORK', 'the image view draws the text icon it now holds',
      evidence=_FW_B28_DRAW + '; SRC ' + _ref + '; SRC com/amulyakhare/textdrawable/TextDrawable.java:71,78 (vendored)')
    e(_src, 'TextDrawable.getIntrinsicWidth', 'FRAMEWORK', 'the image view asks the text icon for its width when it measures the view',
      evidence=_FW_B28_DRAW + '; SRC ' + _ref + '; SRC com/amulyakhare/textdrawable/TextDrawable.java:126 (vendored)')
    e(_src, 'TextDrawable.getIntrinsicHeight', 'FRAMEWORK', 'the image view asks the text icon for its height when it measures the view',
      evidence=_FW_B28_DRAW + '; SRC ' + _ref + '; SRC com/amulyakhare/textdrawable/TextDrawable.java:131 (vendored)')
    e(_src, 'TextDrawable.getOpacity', 'FRAMEWORK', 'the image view asks the text icon for its opacity before it draws it',
      evidence=_FW_B28_OPAQUE + '; SRC ' + _ref + '; SRC com/amulyakhare/textdrawable/TextDrawable.java:121 (vendored)')

# batch-28 filter path: typing is closed (allow_filtering=false, input type 0, dialog_export.xml:98), but the framework still runs the filter.
# The tool run recorded getFilter, its anonymous Filter and performFiltering, so the route is kept as REACHABLE (not UNREACHABLE).
# The trigger of the framework's filter run is not identified from the app source (AutoCompleteTextView source not held): see readme_notes.md Limits.
_FW_B28_SETADAPTER = ('INFERRED AutoCompleteTextView.setAdapter stores the Filter of a Filterable adapter (it calls getFilter when the adapter is set; '
                      'AppCompat source not held)')
_FW_B28_FILTER = ('INFERRED android.widget.Filter: a filter run calls performFiltering with the query, then publishResults with the results '
                  '(framework source not held); the app source gives no typing trigger, and the trigger of the framework run is not identified')
_FW_B28_STREAM = 'INFERRED java.util.stream: the terminal collect runs the filter predicate for each element of the group list (JDK source not read)'
e('DropdownCheckBoxes.initialise', 'DropdownCheckBoxes$CheckboxAdapter.getFilter', 'FRAMEWORK',
  'setAdapter asks the adapter for its filter when the adapter is set (line 54)',
  evidence=_FW_B28_SETADAPTER + '; SRC ui/components/DropdownCheckBoxes.java:54,156-157')
e('DropdownCheckBoxes$CheckboxAdapter.getFilter', 'DropdownCheckBoxes$CheckboxAdapter$1.performFiltering', 'FRAMEWORK',
  'the framework starts a filter run and calls performFiltering with the query (the trigger is not identified from the app source)',
  guard='the framework starts a filter run (typing is closed by allow_filtering=false, dialog_export.xml:98)',
  evidence=_FW_B28_FILTER + '; SRC ui/components/DropdownCheckBoxes.java:159-160')
e('DropdownCheckBoxes$CheckboxAdapter$1.performFiltering', 'DropdownCheckBoxes$CheckboxAdapter$1.publishResults', 'FRAMEWORK',
  'the filter hands its results to publishResults, which replaces the visible rows',
  evidence=_FW_B28_FILTER + '; SRC ui/components/DropdownCheckBoxes.java:175-178')
e('DropdownCheckBoxes$CheckboxAdapter$1.performFiltering', 'DropdownCheckBoxes$CheckboxAdapter$1.lambda$performFiltering$0', 'FRAMEWORK',
  'the stream runs the filter predicate for each group when the query is not empty',
  guard='the query is not empty and the group list has items (DropdownCheckBoxes.java:161-162)',
  evidence=_FW_B28_STREAM + '; SRC ui/components/DropdownCheckBoxes.java:163-168')

# batch-28 UNREACHABLE (dropdown constructors)
assert 'DropdownCheckBoxes.<init>' in _UNIV_SHORT, 'DropdownCheckBoxes.<init>'
UNREACHABLE['DropdownCheckBoxes.<init>(Context)'] = ('no_trigger_in_app',
    'no app code creates a DropdownCheckBoxes with one argument (grep of the app tree: no "new DropdownCheckBoxes"); the layout inflater uses the two-argument constructor (dialog_export.xml:94)',
    'ui/components/DropdownCheckBoxes.java:37-40', 'SOURCE')
UNREACHABLE['DropdownCheckBoxes.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'LayoutInflater creates XML views through the (Context,AttributeSet) constructor only (framework source not read), and no app code calls the three-argument form (grep: no "new DropdownCheckBoxes")',
    'ui/components/DropdownCheckBoxes.java:47-50', 'INFERRED')

# batch-28 UNREACHABLE (TextDrawable$Builder): the text icon uses beginConfig, width, height, endConfig and buildRound only (TextDrawableHelper.java:48-52)
for _m, _line in [('bold', 209), ('fontSize', 204), ('textColor', 189), ('toUpperCase', 214), ('useFont', 199), ('withBorder', 194)]:
    assert 'TextDrawable$Builder.' + _m in _UNIV_SHORT, 'TextDrawable$Builder.' + _m
    UNREACHABLE['TextDrawable$Builder.' + _m] = ('no_trigger_in_app',
        'no app code calls the builder method %s (grep of the app tree: no builder call); the text icon is built with beginConfig, width, height, endConfig and buildRound only (helpers/TextDrawableHelper.java:48-52)' % _m,
        'com/amulyakhare/textdrawable/TextDrawable.java:%d' % _line, 'SOURCE')
assert 'TextDrawable$Builder.buildRect' in _UNIV_SHORT, 'TextDrawable$Builder.buildRect'
UNREACHABLE['TextDrawable$Builder.buildRect'] = ('no_trigger_in_app',
    'no app code calls buildRect (grep of the app tree: no call); the text icon ends with buildRound (helpers/TextDrawableHelper.java:52)',
    'com/amulyakhare/textdrawable/TextDrawable.java:250', 'SOURCE')
assert 'TextDrawable$Builder.buildRoundRect' in _UNIV_SHORT, 'TextDrawable$Builder.buildRoundRect'
UNREACHABLE['TextDrawable$Builder.buildRoundRect'] = ('no_trigger_in_app',
    'no app code calls buildRoundRect (grep of the app tree: no call); the text icon ends with buildRound (helpers/TextDrawableHelper.java:52)',
    'com/amulyakhare/textdrawable/TextDrawable.java:256', 'SOURCE')
# rect and roundRect have one caller each, buildRect and buildRoundRect (both UNREACHABLE): this gives two consistency flags (see readme_notes.md Limits)
assert 'TextDrawable$Builder.rect' in _UNIV_SHORT, 'TextDrawable$Builder.rect'
UNREACHABLE['TextDrawable$Builder.rect'] = ('no_trigger_in_app',
    'no app code calls rect (grep of the app tree: no call); its only caller is buildRect, which is UNREACHABLE (TextDrawable.java:250-252)',
    'com/amulyakhare/textdrawable/TextDrawable.java:230', 'SOURCE')
assert 'TextDrawable$Builder.roundRect' in _UNIV_SHORT, 'TextDrawable$Builder.roundRect'
UNREACHABLE['TextDrawable$Builder.roundRect'] = ('no_trigger_in_app',
    'no app code calls roundRect (grep of the app tree: no call); its only caller is buildRoundRect, which is UNREACHABLE (TextDrawable.java:256-258)',
    'com/amulyakhare/textdrawable/TextDrawable.java:242', 'SOURCE')

# batch-28 UNREACHABLE (TextDrawableHelper): the constructor is private and nothing creates the helper
assert 'TextDrawableHelper.<init>' in _UNIV_SHORT, 'TextDrawableHelper.<init>'
UNREACHABLE['TextDrawableHelper.<init>'] = ('no_trigger_in_app',
    'private constructor of a static helper: no app code creates a TextDrawableHelper (grep of the app tree: no "new TextDrawableHelper"); the app calls its static generate method',
    'helpers/TextDrawableHelper.java:35-37', 'SOURCE')

# batch-28 UNREACHABLE (TextDrawable drawing hooks that the framework does not call for these views)
assert 'TextDrawable.setAlpha' in _UNIV_SHORT, 'TextDrawable.setAlpha'
UNREACHABLE['TextDrawable.setAlpha'] = ('framework_never_calls',
    'the framework sets a drawable alpha only through an ImageView alpha setter (framework source not read), and no app code sets an image alpha (grep: no setImageAlpha; the setAlpha calls at AegisActivity.java:228,233, EntryHolder.java:172,492 and FabMenuHelper.java:42,165 act on views, not on text icons)',
    'com/amulyakhare/textdrawable/TextDrawable.java:111', 'INFERRED')
assert 'TextDrawable.setColorFilter' in _UNIV_SHORT, 'TextDrawable.setColorFilter'
UNREACHABLE['TextDrawable.setColorFilter'] = ('framework_never_calls',
    'the only app setColorFilter is IconHolder.java:44, and that view holds a resource drawable (setImageResource, IconHolder.java:45) or a Glide drawable, never a text icon; the text-icon views (loadEntryIcon targets at EditEntryActivity.java:253, AssignIconHolder.java:42, EntryHolder.java:225) get no colour filter (framework source not read)',
    'com/amulyakhare/textdrawable/TextDrawable.java:116', 'INFERRED')

# --- batch 29: the unlock screen (AuthActivity: lifecycle, the password reminder, the wrong-password and vault-load dialogs, the biometric
# callbacks) and the unused Dialogs overloads. The framework runs onResume (ActivityThread.performResumeActivity, line 3621), then makeVisible
# (ActivityThread.java:3721-3722, Activity.java:5421-5428: the decor view is added to the window manager). The first traversal dispatches the
# attach (ViewRootImpl.java:1668); DecorView calls its Window.Callback, the Activity, whose onAttachedToWindow is Activity.java:3169.
_FW_B29_ATTACH = ('FW-SRC core/java/android/app/ActivityThread.java:3621,3721-3722; FW-SRC core/java/android/app/Activity.java:5421-5428,3169; '
    'FW-SRC core/java/android/view/ViewRootImpl.java:1668; FW-SRC core/java/com/android/internal/policy/DecorView.java:1585-1590')
_FW_B29_POST = 'FW-SRC core/java/android/view/View.java:15777-15785 (post hands the Runnable to the attach handler, or queues it until the view attaches)'
# lifecycle: the screen loses focus (Home or another app), then the framework saves the instance state (API 27: after onPause)
e('S_AUTH', 'AuthActivity.onPause', 'SYSTEM', 'Press Home or switch apps (the unlock screen loses focus)', gui=['Press Home'],
  evidence='SRC ui/AuthActivity.java:226-234')
e('AuthActivity.onPause', 'AuthActivity.onSaveInstanceState', 'SYSTEM',
  'API 27: the framework saves the instance state after onPause', evidence=FW_SAVE + '; SRC ui/AuthActivity.java:198-201')
# the decor view is added after the first resume; the attach then calls onAttachedToWindow
e('AuthActivity.onResume', 'AuthActivity.onAttachedToWindow', 'LIFECYCLE',
  'the decor view is added to the window after the first resume, and the framework then attaches it (onAttachedToWindow)',
  evidence=_FW_B29_ATTACH + '; SRC ui/AuthActivity.java:236-241')
e('AuthActivity.onAttachedToWindow', 'AuthActivity.showPasswordReminder', 'CALL',
  'a biometric key exists and the password reminder is due: the reminder popup is set up',
  guard='a biometric key exists and the password reminder is due (AuthActivity.java:237-240)',
  evidence='SRC ui/AuthActivity.java:236-240')
e('AuthActivity.showPasswordReminder', 'AuthActivity.lambda$showPasswordReminder$5', 'FRAMEWORK',
  'View.post runs the popup code on the main thread (it returns early when the activity is finishing)',
  evidence=_FW_B29_POST + '; SRC ui/AuthActivity.java:255-258')

# isPasswordReminderNeeded(long) returns early for NEVER, so the interval check is reached only when the reminder is on
e('Preferences.isPasswordReminderNeeded(long)', 'PassReminderFreq.getDurationMillis', 'CALL',
  'the time since the last reminder is compared with the chosen interval',
  guard='the password reminder frequency is not NEVER (on a fresh install the default is BIWEEKLY: Preferences.java:120-124,140-142)',
  evidence='SRC Preferences.java:140-145')

# the wrong-password dialog (AuthActivity.java:313-320): OK selects the password text again
e('AuthActivity.onInvalidPassword', 'AuthActivity.lambda$onInvalidPassword$6', 'FRAMEWORK',
  'the wrong-password dialog is shown: tap OK (the password text is selected again)',
  evidence=FW_CLICK + '; SRC ui/AuthActivity.java:313-320')
e('AuthActivity.lambda$onInvalidPassword$6', 'AuthActivity.selectPassword', 'CALL', 'the password text is selected and the keyboard is shown',
  evidence='SRC ui/AuthActivity.java:319,203-208')
# the password reminder dialog (AuthActivity.java:181-190): its OK starts the biometric prompt
e('AuthActivity.lambda$onCreate$4', 'AuthActivity.lambda$onCreate$3', 'FRAMEWORK',
  'the password reminder dialog is shown from the biometric button: tap OK',
  guard='readVaultFile does not throw (AuthActivity.java:121-128) and a password reminder is due (the dialog replaces the prompt, AuthActivity.java:181-190)', env=ENV_CLOCK_FORWARD,
  evidence=FW_CLICK + '; SRC ui/AuthActivity.java:181-190')
# the vault-load error dialog (AuthActivity.java:121-128): its OK runs the back dispatcher
e('AuthActivity.onCreate', 'Dialogs.showErrorDialog(Context,int,Exception,OnClickListener)', 'CALL',
  'the vault file cannot be read: the error dialog opens with the OK listener, and onCreate returns',
  guard='VaultRepositoryException from VaultRepository.readVaultFile (AuthActivity.java:121-128)',
  evidence='SRC ui/AuthActivity.java:121-128')
e('Dialogs.lambda$showErrorDialog$15', 'AuthActivity.lambda$onCreate$1', 'CALL',
  'Tap OK in the error dialog: the listener calls the back dispatcher (the back handler closes the task)',
  cls='non_standard', via='DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at AuthActivity.java:124-126)',
  evidence='SRC ui/dialogs/Dialogs.java:391-395; SRC ui/AuthActivity.java:124-126')

# the biometric prompt reports an error or a finger or face that does not match (the same prompt as onAuthenticationSucceeded)
e('AuthActivity.showBiometricPrompt', 'AuthActivity$BiometricPromptListener.onAuthenticationError', 'FRAMEWORK',
  'the prompt reports an error (cancel, too many tries, or a sensor error): the listener shows the error text', env=ENV_BIOMETRIC,
  evidence=FW_BIOPROMPT + '; SRC ui/AuthActivity.java:270-293,366-376')
e('AuthActivity.showBiometricPrompt', 'AuthActivity$BiometricPromptListener.onAuthenticationFailed', 'FRAMEWORK',
  'the sensor reads a finger or face that does not match (the prompt calls the listener)', env=ENV_BIOMETRIC,
  evidence=FW_BIOPROMPT + '; SRC ui/AuthActivity.java:270-293,397-400')

# Dialogs: the overloads below have no app caller (bytecode call rows and grep of the app tree); the int-message overloads are the ones used
assert 'Dialogs.<init>' in _UNIV_SHORT, 'Dialogs.<init>'
UNREACHABLE['Dialogs.<init>'] = ('no_trigger_in_app',
    'private constructor of a static helper: no app code creates a Dialogs (grep of the app tree: no "new Dialogs")',
    'ui/dialogs/Dialogs.java:56-58', 'SOURCE')
assert 'Dialogs.showErrorDialog' in _UNIV_SHORT, 'Dialogs.showErrorDialog'
UNREACHABLE['Dialogs.showErrorDialog(Context,String,Exception)'] = ('no_trigger_in_app',
    'no app caller: the bytecode call rows have no call to this String-message overload (the int-message overloads are used)',
    'ui/dialogs/Dialogs.java:359-361', 'SOURCE')
UNREACHABLE['Dialogs.showErrorDialog(Context,String,Exception,OnClickListener)'] = ('no_trigger_in_app',
    'the only caller is the String-message 3-argument overload above (Dialogs.java:360), which no app code calls',
    'ui/dialogs/Dialogs.java:360,371-373', 'SOURCE')
assert 'Dialogs.showPasswordInputDialog' in _UNIV_SHORT, 'Dialogs.showPasswordInputDialog'
UNREACHABLE['Dialogs.showPasswordInputDialog(Context,TextInputListener)'] = ('no_trigger_in_app',
    'no app caller: the bytecode call rows have no call to this 2-argument overload (the overloads with an OnCancelListener are used)',
    'ui/dialogs/Dialogs.java:254-256', 'SOURCE')
UNREACHABLE['Dialogs.showPasswordInputDialog(Context,int,TextInputListener)'] = ('no_trigger_in_app',
    'no app caller: the bytecode call rows have no call to this overload',
    'ui/dialogs/Dialogs.java:262-264', 'SOURCE')
assert 'Dialogs.showTextInputDialog' in _UNIV_SHORT, 'Dialogs.showTextInputDialog'
UNREACHABLE['Dialogs.showTextInputDialog(Context,int,int,TextInputListener,boolean)'] = ('no_trigger_in_app',
    'private: its only caller is the 2-argument showPasswordInputDialog (Dialogs.java:255), which no app code calls',
    'ui/dialogs/Dialogs.java:246-248,255', 'SOURCE')

# --- batch 30: the backup agent (AegisBackupAgent), the notification service (NotificationService, never started), the security page's
#     switch (SwitchPreference), and the two About dialogs (SimpleWebViewDialog; LicenseDialog and ChangelogDialog are its subclasses)
_FW_B30_AGENT = ('FW-SRC core/java/android/app/ActivityThread.java:3248-3268 (the system creates the agent with newInstance, '
    'attaches it, then calls onCreate and onBind)')
_FW_B30_KV = ('INFERRED android.app.backup.BackupAgent: an app with android:fullBackupOnly="true" gets no key-value backup or restore calls '
    '(BackupAgent source not in fw_src; SRC AndroidManifest.xml:24)')
_FW_B30_INFLATE = ('INFERRED androidx.preference: the page inflates each XML tag through its (Context, AttributeSet) constructor '
    '(androidx source not read)')
_FW_B30_TWOSTATE = ('INFERRED androidx.preference TwoStatePreference: a persistent switch gets its stored value through onSetInitialValue, '
    'which calls the one-argument setChecked (androidx source not read)')
_FW_B30_SHOW = ('INFERRED androidx.fragment DialogFragment: show() commits a fragment transaction, then the fragment calls onCreateDialog '
    '(androidx source not read)')
_NS_REASON = ('the service is never started: the startService call of VaultManager.startNotificationService is inside a comment '
    '(VaultManager.java:280-283, issue #1047), and the service is not exported (no intent filter, no exported attribute)')

# backup agent: the system creates the agent for a full backup or for a restore, by its class name (ActivityThread.java:3256)
e('S_PROCESS', 'AegisBackupAgent.<init>', 'ENTRY', 'the system creates the backup agent for a full backup',
  env=ENV_BACKUP, cls='non_standard', via='reflection: ActivityThread.handleCreateBackupAgent loads the class by name and calls newInstance (ActivityThread.java:3256)',
  evidence=_FW_B30_AGENT + '; SRC AegisBackupAgent.java:25 (no constructor is declared); SRC AndroidManifest.xml:27')
e('S_PROCESS', 'AegisBackupAgent.<init>', 'ENTRY', 'the system creates the backup agent to restore the app data',
  env=ENV_RESTORE, cls='non_standard', via='reflection: ActivityThread.handleCreateBackupAgent loads the class by name and calls newInstance (ActivityThread.java:3256)',
  evidence=_FW_B30_AGENT + '; SRC AegisBackupAgent.java:25 (no constructor is declared); SRC AndroidManifest.xml:27')
# the static TAG is set when the class is first created (JVM class initialization runs before the constructor body), as in the AboutActivity block
e('AegisBackupAgent.<init>', 'AegisBackupAgent.<clinit>', 'LIFECYCLE',
  'the first creation of the agent initializes its static TAG',
  evidence='INFERRED JVM class initialization (JLS 12.4.1): the system creates the agent by its class name; static field SRC AegisBackupAgent.java:26')
e('AegisBackupAgent.<init>', 'AegisBackupAgent.onCreate', 'LIFECYCLE',
  'the system calls onCreate right after it creates the agent (the agent sets up its preferences, audit log and database)',
  evidence=_FW_B30_AGENT + '; SRC AegisBackupAgent.java:32-40')
# the key-value callbacks: the manifest sets android:fullBackupOnly="true", so the system runs only the full backup for this app
UNREACHABLE['AegisBackupAgent.onBackup'] = ('framework_never_calls',
    'key-value backup callback: the manifest sets android:fullBackupOnly="true", so the system runs only the full backup for this app',
    'AegisBackupAgent.java:121-123; AndroidManifest.xml:24', 'INFERRED')
UNREACHABLE['AegisBackupAgent.onRestore'] = ('framework_never_calls',
    'key-value restore callback: the same manifest setting (android:fullBackupOnly="true") means the system does not run a key-value restore',
    'AegisBackupAgent.java:126-128; AndroidManifest.xml:24', 'INFERRED')
UNREACHABLE['AegisBackupAgent.onQuotaExceeded'] = ('framework_never_calls',
    'key-value quota callback: only the key-value backup reports a quota, and android:fullBackupOnly="true" switches that backup off (AndroidManifest.xml:24)',
    'AegisBackupAgent.java:115-118; AndroidManifest.xml:24', 'INFERRED')

# notification service: nothing starts it (see _NS_REASON), so none of its methods has a path
UNREACHABLE['NotificationService.<init>'] = ('no_trigger_in_app', _NS_REASON,
    'services/NotificationService.java:17; vault/VaultManager.java:279-284; AndroidManifest.xml:105', 'SOURCE')
UNREACHABLE['NotificationService.onBind'] = ('no_trigger_in_app',
    'no app code calls bindService (grep of the app tree: no call), and the service is not exported (no intent filter, no exported attribute)',
    'services/NotificationService.java:62-66; AndroidManifest.xml:105', 'SOURCE')
UNREACHABLE['NotificationService.onStartCommand'] = ('no_trigger_in_app', _NS_REASON,
    'services/NotificationService.java:22-27; vault/VaultManager.java:279-284', 'SOURCE')
UNREACHABLE['NotificationService.serviceMethod'] = ('no_trigger_in_app',
    'its only caller is onStartCommand (bytecode call row), and onStartCommand has no path (' + _NS_REASON + ')',
    'services/NotificationService.java:25,29-47', 'SOURCE')
UNREACHABLE['NotificationService.onDestroy'] = ('no_trigger_in_app',
    'the system calls onDestroy only after the service has been started and stopped; the service is never started (' + _NS_REASON + ')',
    'services/NotificationService.java:49-54', 'SOURCE')
UNREACHABLE['NotificationService.onTaskRemoved'] = ('no_trigger_in_app',
    'the system calls onTaskRemoved only for a started service; the service is never started (' + _NS_REASON + ')',
    'services/NotificationService.java:56-60', 'SOURCE')
# the start intent is built only inside the comment at VaultManager.java:282, so no app code calls this getter
UNREACHABLE['VaultManager.getNotificationServiceIntent'] = ('no_trigger_in_app',
    'its only call is inside the comment of startNotificationService (VaultManager.java:282, issue #1047), so no app code runs it',
    'vault/VaultManager.java:282,291-292', 'SOURCE')

# security page: the switch rows (preferences_security.xml:8,22,39) are this class; the page inflates them when it is built
assert 'SwitchPreference.<init>' in _UNIV_SHORT, 'SwitchPreference.<init>'
e('SecurityPreferencesFragment.onCreatePreferences', 'SwitchPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the security page is built and its preference rows are inflated from preferences_security.xml',
  cls='non_standard', via='reflection: the preference inflater builds each XML tag through its (Context, AttributeSet) constructor (androidx source not read)',
  evidence=_FW_B30_INFLATE + '; SRC ui/fragments/preferences/SecurityPreferencesFragment.java:58; SRC res/xml/preferences_security.xml:8,22,39')
# the one-argument setChecked is what the library calls for the stored value; this override ignores its argument (it always sets the switch on)
e('SecurityPreferencesFragment.onCreatePreferences', 'SwitchPreference.setChecked(boolean)', 'FRAMEWORK',
  'the security page loads: each persistent switch is set to its stored value (the one-argument setChecked, which ignores its argument)',
  evidence=_FW_B30_TWOSTATE + '; SRC ui/preferences/SwitchPreference.java:34-37; SRC res/xml/preferences_security.xml:8,22,39')
# the constructors that the inflater does not use and the app never calls
assert 'SwitchPreference.<init>' in _UNIV_SHORT, 'SwitchPreference.<init>'
UNREACHABLE['SwitchPreference.<init>(Context)'] = ('no_trigger_in_app',
    'no app code creates a SwitchPreference with one argument (grep of the app tree: no "new SwitchPreference"), and the XML inflater uses only the (Context, AttributeSet) constructor',
    'ui/preferences/SwitchPreference.java:24-26', 'INFERRED')
UNREACHABLE['SwitchPreference.<init>(Context,AttributeSet,int)'] = ('no_trigger_in_app',
    'no app code calls this constructor (grep of the app tree: no "new SwitchPreference"), and the XML inflater uses only the (Context, AttributeSet) constructor',
    'ui/preferences/SwitchPreference.java:16-18', 'INFERRED')
UNREACHABLE['SwitchPreference.<init>(Context,AttributeSet,int,int)'] = ('no_trigger_in_app',
    'no app code calls this constructor (grep of the app tree: no "new SwitchPreference"), and the XML inflater uses only the (Context, AttributeSet) constructor',
    'ui/preferences/SwitchPreference.java:12-14', 'INFERRED')

# the About page's license and changelog taps show a SimpleWebViewDialog subclass; the fragment then builds it through onCreateDialog,
# and getContent, getBackgroundColor, getTextColor, colorToCSS and readAssetAsString follow from it by the bytecode call rows
e('AboutActivity.lambda$onCreate$0', 'SimpleWebViewDialog.onCreateDialog', 'FRAMEWORK',
  'tap the license button: the license dialog is shown, and the fragment builds its dialog',
  evidence=_FW_B30_SHOW + '; SRC ui/AboutActivity.java:54-58; SRC ui/dialogs/SimpleWebViewDialog.java:41-65')
e('AboutActivity.lambda$onCreate$9', 'SimpleWebViewDialog.onCreateDialog', 'FRAMEWORK',
  'tap the changelog button: the changelog dialog is shown, and the fragment builds its dialog',
  evidence=_FW_B30_SHOW + '; SRC ui/AboutActivity.java:93-97; SRC ui/dialogs/SimpleWebViewDialog.java:41-65')

# --- batch 31: the backup writer and the backup-folder cleanup (VaultBackupManager), and two SlideFragment methods that nothing calls
_FW_B31_SORT = ('INFERRED JDK Collections.sort: the sort calls Comparator.compare on pairs of list items (java.util source not held)')
_FW_B31_PARSE = ('INFERRED JDK DateFormat.parse(String): the method calls the overridden parse(String, ParsePosition) (java.text source not held)')
assert 'VaultBackupManager.scheduleBackup' in _UNIV_SHORT and 'VaultBackupManager.lambda$scheduleBackup$0' in _UNIV_SHORT
assert 'VaultBackupManager$FileInfo.getFilename' in _UNIV_SHORT and 'SlideFragment.skipToSlide' in _UNIV_SHORT

# the executor runs the lambda on its worker thread (the lambda body is not reached by a plain call)
e('VaultBackupManager.scheduleBackup', 'VaultBackupManager.lambda$scheduleBackup$0', 'ASYNC',
  'the backup is written on the worker thread of the single-thread executor',
  evidence='SRC vault/VaultBackupManager.java:57-67; INFERRED java.util.concurrent single-thread executor runs each submitted task on its worker thread')
# the cleanup sorts the backup files by date; the sort compares only pairs, so it needs at least two files (and versions to keep above 0, the early return)
e('VaultBackupManager.enforceVersioning', 'VaultBackupManager$FileComparator.compare', 'FRAMEWORK',
  'the cleanup sorts the backup files by date, then deletes the oldest ones',
  guard='versions to keep is above 0 and the folder holds at least two backup files (the sort compares only pairs)',
  evidence=_FW_B31_SORT + '; SRC vault/VaultBackupManager.java:163-190,289')
# the strict date format is used by the parser: the JDK calls the overridden two-argument parse for the one-argument parse
e('VaultBackupManager$FileInfo.parseFilename', 'VaultBackupManager$StrictDateFormat.parse', 'FRAMEWORK',
  'the date part of the backup file name is parsed with the strict format',
  guard='the file name ends in .json, has a prefix and two date parts, and the prefix is aegis-backup',
  evidence=_FW_B31_PARSE + '; SRC vault/VaultBackupManager.java:215-243,294-312')
e('VaultBackupManager.enforceVersioning', 'VaultBackupManager$BackupFile.<init>', 'CALL',
  'the cleanup builds a backup file object for each regular, non-virtual file in the backup folder',
  guard='versions to keep is above 0 (the early return at VaultBackupManager.java:164-166 is not taken) and the entry is a regular file that is not virtual (line 172); the constructor parses its name (lines 174-175)',
  evidence='SRC vault/VaultBackupManager.java:164-166,171-175')
e('VaultBackupManager$FileInfo.parseFilename', 'VaultBackupManager$FileInfo.throwBadFormat', 'CALL',
  'the file name does not match the backup format: the parser throws the bad-format error',
  guard='the file name fails one of the format checks (the throwBadFormat calls at VaultBackupManager.java:222, 229, 234, 239)',
  note='needs a file in the backup folder whose name fails the format check; no step on this route creates one. The ParseException is caught and ignored at VaultBackupManager.java:175, so the route ends with no visible effect',
  evidence='SRC vault/VaultBackupManager.java:216-240')
e('VaultBackupManager.createBackup(File,Uri,int)', 'VaultBackupManager.enforceVersioning', 'CALL',
  'the backup is written, then the old backups are cleaned up',
  guard='the backup file is written, so no exception is thrown before the call (the persisted SAF permission exists, hasPermissionsAt at VaultBackupManager.java:118-120; no file with the same name, 125-127; createFile returns a file, 130-131; the stream copy does not fail, 136-141); the callee returns at once when versions to keep is 0 (VaultBackupManager.java:164-166)',
  evidence='SRC vault/VaultBackupManager.java:110-150; SRC vault/VaultBackupManager.java:164-166')
e('ImportEntriesActivity.processDecryptedImporterState', 'ImportEntriesActivity.processImporterResult', 'CALL',
  'no imported icon needs optimising: the result is shown at once',
  guard='the import data converts (state.convert() does not throw, ImportEntriesActivity.java:207-212) and the icon list is empty (ImportEntriesActivity.java:220, 230-231)',
  evidence='SRC ui/ImportEntriesActivity.java:220-231')
e('ImportEntriesActivity.processImporterResult', 'Dialogs.showMultiExceptionDialog', 'CALL',
  'the importer result has entry errors: the error dialog lists them',
  guard='the importer result has errors (ImportEntriesActivity.java:245-248)',
  evidence='SRC ui/ImportEntriesActivity.java:245-248')
e('ImportEntriesActivity.lambda$onCreate$0', 'ImportEntriesActivity.saveAndFinish', 'CALL',
  'the save button saves at once, without the wipe dialog',
  guard='the vault has no entries or the wipe option is off, so the wipe dialog is not shown (ImportEntriesActivity.java:94-98)',
  evidence='SRC ui/ImportEntriesActivity.java:92-99')
e('IconAdapter.lambda$onBindViewHolder$2', 'EditEntryActivity$1.onCustomSelected', 'CALL',
  'the custom icon row is tapped on the edit page: the custom icon page opens',
  guard='the tapped row is the custom entry (icon instanceof DummyIcon; ui/views/IconAdapter.java:174-175)',
  evidence='SRC ui/views/IconAdapter.java:168-175')
sup(('IconAdapter.lambda$onBindViewHolder$2', 'AssignIconsActivity$1.onCustomSelected'))

# --- C3 sample fix 1: icon picker split by installing activity (CustomSvgIcon route).
# The dumped first-draw route reached EditEntryActivity$1.onCustomSelected from an
# AssignIconsActivity prefix: the graph's single listener edge ignored which activity
# installed the picker. In code the picker opens with showAddCustom=true only from
# EditEntryActivity.startIconSelection (EditEntryActivity.java:594) and with
# showAddCustom=false from AssignIconsActivity.onAssignIconEntryClick
# (AssignIconsActivity.java:194); the DummyIcon custom row exists only when
# showAddCustom is true (IconAdapter.java:63-64), and the adapter's listener is the
# IconPickerDialog$1 forwarder created in create() (IconPickerDialog.java:53-66),
# whose onCustomSelected dismisses and calls the installing activity's listener
# (:62-64). The chain is therefore split @EDIT/@ASSIGN from create down to the
# dispatch; the base chain is unfed after the split (both callers use variants),
# so its edges stay as documentation only. The search-clear path calls
# loadIcons(pack, false) unconditionally (IconAdapter.setQuery, IconAdapter.java:92-96),
# so it goes to a @NOCUSTOM variant whose grid has no DummyIcon row and therefore no
# onCustomSelected dispatch. onIconSelected dispatch is split in the block below
# (after the onCustomSelected forwarder block): the @EDIT/@ASSIGN forwarder variants
# carry the non-Dummy tap to the installing activity's listener, so selectIcon and
# setNewIcon routes no longer share a dispatch.
_PICK_EDIT = 'IconPickerDialog.create@EDIT'
_PICK_ASSIGN = 'IconPickerDialog.create@ASSIGN'
e('EditEntryActivity.startIconSelection', _PICK_EDIT, 'CALL',
  'the edit page opens the icon picker (the custom row is offered)',
  guard='the call passes showAddCustom true (EditEntryActivity.java:594)',
  evidence='SRC ui/EditEntryActivity.java:594')
e('AssignIconsActivity.onAssignIconEntryClick', _PICK_ASSIGN, 'CALL',
  'the assign-icons page opens the icon picker (no custom row is offered)',
  guard='the call passes showAddCustom false (AssignIconsActivity.java:194)',
  evidence='SRC ui/AssignIconsActivity.java:194')
e(_PICK_EDIT, 'IconAdapter.loadIcons@EDIT', 'CALL',
  'the picker fills the grid from the first icon pack (the custom row is included)',
  guard='showAddCustom is true on this picker (IconPickerDialog.java:127)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:127')
e(_PICK_ASSIGN, 'IconAdapter.loadIcons@ASSIGN', 'CALL',
  'the picker fills the grid from the first icon pack (no custom row)',
  guard='showAddCustom is false on this picker (IconPickerDialog.java:127)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:127')
gui(_PICK_EDIT, 'IconPickerDialog.lambda$create$2@EDIT', 'Tap the icon pack name button above the grid',
    evidence=FW_CLICK + '; SRC ui/dialogs/IconPickerDialog.java:130-134')
gui(_PICK_ASSIGN, 'IconPickerDialog.lambda$create$2@ASSIGN', 'Tap the icon pack name button above the grid',
    evidence=FW_CLICK + '; SRC ui/dialogs/IconPickerDialog.java:130-134')
gui('IconPickerDialog.lambda$create$2@EDIT', 'IconPickerDialog.lambda$create$1@EDIT', 'Tap an icon pack name in the popup menu',
    evidence=_FW_B26_POPUP + '; SRC ui/dialogs/IconPickerDialog.java:135-147')
gui('IconPickerDialog.lambda$create$2@ASSIGN', 'IconPickerDialog.lambda$create$1@ASSIGN', 'Tap an icon pack name in the popup menu',
    evidence=_FW_B26_POPUP + '; SRC ui/dialogs/IconPickerDialog.java:135-147')
e('IconPickerDialog.lambda$create$1@EDIT', 'IconAdapter.loadIcons@EDIT', 'CALL',
  'the pack switch refills the grid (the custom row is kept)',
  guard='the pack switch passes the same showAddCustom flag (IconPickerDialog.java:138)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:138')
e('IconPickerDialog.lambda$create$1@ASSIGN', 'IconAdapter.loadIcons@ASSIGN', 'CALL',
  'the pack switch refills the grid (still no custom row)',
  guard='the pack switch passes the same showAddCustom flag (IconPickerDialog.java:138)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:138')
# the shared create machinery (focus, watcher, preloader, span lookup, grid inflation)
# is replicated onto both variants so those methods stay reachable; the auto constructor
# edges (create -> $1.<init>, $2.<init>, $1IconPreloadProvider.<init>) replicate on their own
for _pk in (_PICK_EDIT, _PICK_ASSIGN):
    gui(_pk, 'IconPickerDialog.lambda$create$0', 'Tap the icon search box (it takes focus and the sheet expands)',
        evidence=_FW_B26_FOCUS + '; SRC ui/dialogs/IconPickerDialog.java:85-90')
    gui(_pk, 'IconPickerDialog$2.beforeTextChanged', 'Type in the icon search box (the watcher runs before the text changes)',
        evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91-96')
    gui(_pk, 'IconPickerDialog$2.onTextChanged', 'Type in the icon search box (the watcher runs as the text changes)',
        evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91,97-101')
    gui(_pk, 'IconPickerDialog$2.afterTextChanged', 'Type in the icon search box (the watcher runs after the text changes)',
        evidence=_FW_B26_WATCH + '; SRC ui/dialogs/IconPickerDialog.java:91,103-106')
    gui(_pk, 'IconPickerDialog$1IconPreloadProvider.getPreloadItems',
        'Scroll the icon grid (the preloader asks which icons are about to show, so their images load early)',
        evidence=FW_SCROLL + '; INFERRED Glide RecyclerViewPreloader: onScrolled asks the model provider for the items '
                 '(library source not read); SRC ui/dialogs/IconPickerDialog.java:67-74,109-111,126')
    gui(_pk, 'IconPickerDialog$1IconPreloadProvider.getPreloadRequestBuilder',
        'Scroll the icon grid: the preloader builds the request for each icon it was given',
        guard='the icon was returned by getPreloadItems (IconPickerDialog.java:70-73)',
        evidence='INFERRED Glide RecyclerViewPreloader: it builds a request for each item that getPreloadItems returned '
                 '(library source not read); SRC ui/dialogs/IconPickerDialog.java:76-81')
    e(_pk, 'IconPickerDialog$3.getSpanSize', 'FRAMEWORK', 'the grid layout asks for the span of each row when it lays out the picker',
      evidence=_FW_B26_SPAN + '; SRC ui/dialogs/IconPickerDialog.java:114-123')
    e(_pk, 'IconRecyclerView.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflating the picker layout creates the icon grid',
      evidence=_FW_B26_INFLATE + '; SRC ui/dialogs/IconPickerDialog.java:43,112; SRC res/layout/dialog_icon_picker.xml:65')
    e(_pk, 'IconRecyclerView.onMeasure', 'FRAMEWORK', 'the bottom sheet measures the icon grid when it lays out the picker',
      evidence=_FW_B26_MEASURE + '; SRC ui/views/IconRecyclerView.java:49-56')
# the grid rows: onBindViewHolder is split (it is the dispatch point); the other
# loadIcons framework edges are replicated onto both variants to shared nodes
for _pt in ('@EDIT', '@ASSIGN'):
    e('IconAdapter.loadIcons' + _pt, 'IconAdapter.onCreateViewHolder', 'FRAMEWORK', 'the grid asks for a row view after the data changes',
      evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,159-164')
    e('IconAdapter.loadIcons' + _pt, 'IconAdapter.onBindViewHolder' + _pt, 'FRAMEWORK', 'the grid fills a row view after the data changes',
      evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,166-168')
    e('IconAdapter.loadIcons' + _pt, 'IconAdapter.getItemCount', 'FRAMEWORK', 'the grid asks how many rows there are after the data changes',
      evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,201-203')
    e('IconAdapter.loadIcons' + _pt, 'IconAdapter.getItemViewType', 'FRAMEWORK', 'the grid asks the view type of each row after the data changes',
      evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,215-222')
    e('IconAdapter.loadIcons' + _pt, 'IconAdapter.lambda$loadIcons$0', 'FRAMEWORK', 'Collections.sort compares two icons by their category',
      evidence=_FW_B26_CMP + '; SRC ui/views/IconAdapter.java:48-53')
    e('IconAdapter.loadIcons' + _pt, 'IconPack$Icon.getName', 'FRAMEWORK', 'Collections.sort compares two icons by their name when their categories are equal',
      evidence=_FW_B26_CMP + '; SRC ui/views/IconAdapter.java:53')
gui('IconAdapter.onBindViewHolder@EDIT', 'IconAdapter.lambda$onBindViewHolder$2@EDIT', 'Tap an icon in the grid',
    guard='the row is an icon row (IconAdapter.java:168-169)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:173-179')
gui('IconAdapter.onBindViewHolder@ASSIGN', 'IconAdapter.lambda$onBindViewHolder$2@ASSIGN', 'Tap an icon in the grid',
    guard='the row is an icon row (IconAdapter.java:168-169)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:173-179')
# the category-header tap is installer-independent (collapse/expand only), so the shared
# lambda$3 is reached from both variants; without this replication it (and its
# setIsCollapsed downstream) lose all paths and the build errors
gui('IconAdapter.onBindViewHolder@EDIT', 'IconAdapter.lambda$onBindViewHolder$3', 'Tap a category header in the grid to collapse or expand it',
    guard='the row is a category header (IconAdapter.java:180-181)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:184-197')
gui('IconAdapter.onBindViewHolder@ASSIGN', 'IconAdapter.lambda$onBindViewHolder$3', 'Tap a category header in the grid to collapse or expand it',
    guard='the row is a category header (IconAdapter.java:180-181)',
    evidence=FW_CLICK + '; SRC ui/views/IconAdapter.java:184-197')
e('IconAdapter.lambda$onBindViewHolder$2@EDIT', 'EditEntryActivity$1.onCustomSelected', 'CALL',
  'the custom icon row is tapped on the edit page: the custom icon page opens',
  guard='the tapped row is the custom entry (icon instanceof DummyIcon, which exists only when showAddCustom is true; ui/views/IconAdapter.java:63-64,174-175)',
  evidence='SRC ui/views/IconAdapter.java:168-175')
e('IconAdapter.lambda$onBindViewHolder$2@ASSIGN', 'AssignIconsActivity$1.onCustomSelected', 'CALL',
  'the custom icon row is tapped on the assign-icons page: nothing happens',
  guard='the listener is AssignIconsActivity$1, whose onCustomSelected is empty (AssignIconsActivity.java:201); the chain dead-ends here',
  evidence='SRC ui/views/IconAdapter.java:168-175; SRC ui/AssignIconsActivity.java:201')
# the forwarder path is split the same way: the adapter's listener is always the
# IconPickerDialog$1 instance created in create(), which forwards to the installing
# activity's listener (IconPickerDialog.java:62-64); without this split the @ASSIGN
# prefix would still reach EditEntryActivity$1 through the shared forwarder
e('IconAdapter.lambda$onBindViewHolder$2@EDIT', 'IconPickerDialog$1.onCustomSelected@EDIT', 'CALL',
  'the tapped row is the custom entry: the adapter calls its listener (the picker forwarder)',
  guard='the tapped row is the custom entry (icon instanceof DummyIcon, which exists only when showAddCustom is true; ui/views/IconAdapter.java:63-64,174-175)',
  evidence='SRC ui/views/IconAdapter.java:168-175')
e('IconAdapter.lambda$onBindViewHolder$2@ASSIGN', 'IconPickerDialog$1.onCustomSelected@ASSIGN', 'CALL',
  'the tapped row is the custom entry: the adapter calls its listener (the picker forwarder)',
  guard='the tapped row is the custom entry (IconAdapter.java:174-175); on this picker no DummyIcon row exists (showAddCustom false, :63-64), so the tap cannot occur — the edge documents the listener binding',
  evidence='SRC ui/views/IconAdapter.java:168-175')
e('IconPickerDialog$1.onCustomSelected@EDIT', 'EditEntryActivity$1.onCustomSelected', 'CALL',
  'the picker forwarder dismisses and calls the edit page listener: the custom icon page opens',
  guard='the picker was opened by the edit page (IconPickerDialog.java:53-66)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:62-64; SRC ui/EditEntryActivity.java:601-602')
e('IconPickerDialog$1.onCustomSelected@ASSIGN', 'AssignIconsActivity$1.onCustomSelected', 'CALL',
  'the picker forwarder dismisses and calls the assign-icons listener: nothing happens',
  guard='the picker was opened by the assign-icons page (IconPickerDialog.java:53-66); the listener body is empty (AssignIconsActivity.java:201)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:62-64; SRC ui/AssignIconsActivity.java:201')
# onIconSelected dispatch is split the same way as onCustomSelected above (fix-1
# pattern, applied to the non-Dummy tap): the adapter's listener is always the
# IconPickerDialog$1 forwarder created in create(), which forwards to the installing
# activity's listener (IconPickerDialog.java:55-57); without this split the @ASSIGN
# prefix would still reach EditEntryActivity$1 through the shared forwarder, and the
# direct @ASSIGN lambda edge would still reach it (judged selectIcon step 41).
# The guards use the non-Dummy branch (IconAdapter.java:176-177), not the Dummy
# branch (:174-175) the onCustomSelected edges use.
e('IconAdapter.lambda$onBindViewHolder$2@EDIT', 'EditEntryActivity$1.onIconSelected', 'CALL',
  'the tapped icon is passed to the edit page listener: the edit page keeps the icon',
  guard='the row is a non-Dummy icon row (IconAdapter.java:176-177) and the picker was opened by the edit page (EditEntryActivity.java:594)',
  evidence='SRC ui/views/IconAdapter.java:173-179; SRC ui/EditEntryActivity.java:594-597')
e('IconAdapter.lambda$onBindViewHolder$2@ASSIGN', 'AssignIconsActivity$1.onIconSelected', 'CALL',
  'the tapped icon is passed to the assign-icons listener: the imported entry keeps the icon',
  guard='the row is a non-Dummy icon row (IconAdapter.java:176-177) and the picker was opened by the assign-icons page (AssignIconsActivity.java:194)',
  evidence='SRC ui/views/IconAdapter.java:173-179; SRC ui/AssignIconsActivity.java:194-197')
e('IconAdapter.lambda$onBindViewHolder$2@EDIT', 'IconPickerDialog$1.onIconSelected@EDIT', 'CALL',
  'the tapped icon is passed to the adapter listener (the picker forwarder)',
  guard='the row is a non-Dummy icon row (IconAdapter.java:176-177); the adapter listener is the IconPickerDialog$1 instance created in create() (IconPickerDialog.java:53-57)',
  evidence='SRC ui/views/IconAdapter.java:173-179; SRC ui/dialogs/IconPickerDialog.java:53-57')
e('IconAdapter.lambda$onBindViewHolder$2@ASSIGN', 'IconPickerDialog$1.onIconSelected@ASSIGN', 'CALL',
  'the tapped icon is passed to the adapter listener (the picker forwarder)',
  guard='the row is a non-Dummy icon row (IconAdapter.java:176-177); the adapter listener is the IconPickerDialog$1 instance created in create() (IconPickerDialog.java:53-57)',
  evidence='SRC ui/views/IconAdapter.java:173-179; SRC ui/dialogs/IconPickerDialog.java:53-57')
e('IconPickerDialog$1.onIconSelected@EDIT', 'EditEntryActivity$1.onIconSelected', 'CALL',
  'the picker forwarder dismisses and calls the edit page listener: the edit page keeps the icon',
  guard='the picker was opened by the edit page (IconPickerDialog.java:53-66); the forwarder calls the listener passed to create() (:57)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:53-57; SRC ui/EditEntryActivity.java:596-597')
e('IconPickerDialog$1.onIconSelected@ASSIGN', 'AssignIconsActivity$1.onIconSelected', 'CALL',
  'the picker forwarder dismisses and calls the assign-icons listener: the imported entry keeps the icon',
  guard='the picker was opened by the assign-icons page (IconPickerDialog.java:53-66); the forwarder calls the listener passed to create() (:57)',
  evidence='SRC ui/dialogs/IconPickerDialog.java:53-57; SRC ui/AssignIconsActivity.java:196-197')
# the search-clear path: setQuery(null) reloads with showAddCustom false, so its grid
# has no DummyIcon row and no onCustomSelected dispatch; the chain ends at the row fill
sup(('IconAdapter.setQuery', 'IconAdapter.loadIcons'))
e('IconAdapter.setQuery', 'IconAdapter.loadIcons@NOCUSTOM', 'CALL',
  'clearing the search refills the grid without the custom row',
  guard='a null query reloads with showAddCustom false (IconAdapter.java:92-96)',
  evidence='SRC ui/views/IconAdapter.java:92-96')
e('IconAdapter.loadIcons@NOCUSTOM', 'IconAdapter.onBindViewHolder@NOCUSTOM', 'FRAMEWORK', 'the grid fills a row view after the data changes',
  evidence=FW_ROWS + '; SRC ui/views/IconAdapter.java:90,166-168')
e('EditEntryActivity.lambda$new$1', 'EditEntryActivity.startEditingIcon', 'CALL',
  'the picked file is an image other than SVG: the icon editor opens with it',
  guard='the picked file is not an SVG (ui/EditEntryActivity.java:148-160; startEditingIcon at 160)',
  evidence='SRC ui/EditEntryActivity.java:144-160')

# the getters have no caller anywhere in the app (grep of the whole app tree: only the declarations)
UNREACHABLE['VaultBackupManager$FileInfo.getFilename'] = ('no_trigger_in_app',
    'no app code calls the getter (grep of the whole app tree: only the declaration)',
    'vault/VaultBackupManager.java:249-251', 'SOURCE')
UNREACHABLE['VaultBackupManager$FileInfo.getExtension'] = ('no_trigger_in_app',
    'no app code calls the getter (grep of the whole app tree: only the declaration)',
    'vault/VaultBackupManager.java:253-255', 'SOURCE')
# the slide's own goToPreviousSlide and skipToSlide: the Previous button, the Back press and IntroActivity call the activity's methods
UNREACHABLE['SlideFragment.goToPreviousSlide'] = ('no_trigger_in_app',
    'no app code calls the slide method: the Previous button and the Back press call the activity method (IntroBaseActivity.java:45,197), and no slide calls it (grep of the whole app tree)',
    'ui/intro/SlideFragment.java:63-66; ui/intro/IntroBaseActivity.java:45,197', 'SOURCE')
UNREACHABLE['SlideFragment.skipToSlide'] = ('no_trigger_in_app',
    'no app code calls the slide method: IntroActivity skips slides on the activity (IntroActivity.java:53,60), and no slide calls it (grep of the whole app tree)',
    'ui/intro/SlideFragment.java:68-71; ui/IntroActivity.java:53,60', 'SOURCE')

# --- batch 32: the intro slides (ui/slides/*), the slide base class and indicator (ui/intro/*), and the span on the hidden code dots (helpers/CenterVerticalSpan)
assert 'SlideIndicator.<init>' in _UNIV_SHORT and 'SlideIndicator.onDraw' in _UNIV_SHORT
assert 'CenterVerticalSpan.updateDrawState' in _UNIV_SHORT and 'CenterVerticalSpan.updateMeasureState' in _UNIV_SHORT
assert 'IntroBaseActivity$ScreenSlidePagerAdapter.createFragment' in _UNIV_SHORT and 'IntroBaseActivity$SlideSkipBlocker.onPageScrollStateChanged' in _UNIV_SHORT
assert 'WelcomeSlide.lambda$startImportVault$2' in _UNIV_SHORT and 'SecuritySetupSlide.lambda$onCreateView$0' in _UNIV_SHORT
_FW_B32_VP = ('INFERRED androidx.viewpager2: the pager lays out its pages after onCreate returns (the slides are added first, IntroActivity.java:33-41) '
              'and asks the adapter for the page count and each page fragment (androidx source not read)')
_FW_B32_ATTACH = ('INFERRED androidx.viewpager2 FragmentStateAdapter: the new page fragment is added to the FragmentManager, which calls onAttach '
                  '(androidx source not read)')
_FW_B32_FRAG = ('INFERRED androidx.fragment: the FragmentManager calls onCreateView and onResume of a page fragment while its page is shown '
                '(androidx source not read)')
_FW_B32_SCROLL = ('INFERRED androidx.viewpager2: setCurrentItem with a smooth scroll reports the scroll state to the registered OnPageChangeCallback '
                  '(androidx source not read)')
_FW_B32_CHECK = ('INFERRED android.widget.CompoundButton.OnCheckedChangeListener: a tap on the checkbox calls onCheckedChanged '
                 '(framework source not read)')
_FW_B32_SPAN = ('INFERRED android.text: the text view measures the spanned text (updateMeasureState) and draws it (updateDrawState) '
                '(framework source not read)')
_FW_B32_DRAW = 'FW-SRC core/java/android/view/View.java:19161,19192 (View.draw calls onDraw)'
_B32_NEWINST = 'reflection: Class.newInstance on the page type (IntroBaseActivity.java:212)'

# the pager builds the page fragments from the page list (createFragment); the reflection edges go to each page's constructor
e('IntroBaseActivity.onCreate', 'IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'FRAMEWORK',
  'the pager asks the adapter for the first page fragment after the slides are added',
  evidence=_FW_B32_VP + '; SRC ui/intro/IntroBaseActivity.java:50-52,208-216')
e('IntroBaseActivity.onCreate', 'IntroBaseActivity$ScreenSlidePagerAdapter.getItemCount', 'FRAMEWORK',
  'the pager asks how many pages there are before it lays them out',
  evidence=_FW_B32_VP + '; SRC ui/intro/IntroBaseActivity.java:219-221')
e('IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'WelcomeSlide.<init>', 'FRAMEWORK',
  'the pager creates the Welcome page (the first slide)', cls='non_standard', via=_B32_NEWINST,
  guard='the page position is 0: the Welcome slide is added first (IntroActivity.java:33-41)',
  evidence='SRC ui/intro/IntroBaseActivity.java:208-216; SRC ui/IntroActivity.java:33-41')
e('IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'SecurityPickerSlide.<init>', 'FRAMEWORK',
  'the pager creates the security picker page', cls='non_standard', via=_B32_NEWINST,
  guard='the page position is 1: the security picker is the second slide (IntroActivity.java:33-41)',
  evidence='SRC ui/intro/IntroBaseActivity.java:208-216; SRC ui/IntroActivity.java:33-41')
e('IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'SecuritySetupSlide.<init>', 'FRAMEWORK',
  'the pager creates the security setup page', cls='non_standard', via=_B32_NEWINST,
  guard='the page position is 2: the security setup is the third slide (IntroActivity.java:33-41)',
  evidence='SRC ui/intro/IntroBaseActivity.java:208-216; SRC ui/IntroActivity.java:33-41')
e('IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'DoneSlide.<init>', 'FRAMEWORK',
  'the pager creates the Done page', cls='non_standard', via=_B32_NEWINST,
  guard='the page position is 3: the Done slide is the last slide (IntroActivity.java:33-41)',
  evidence='SRC ui/intro/IntroBaseActivity.java:208-216; SRC ui/IntroActivity.java:33-41')
e('IntroBaseActivity$ScreenSlidePagerAdapter.createFragment', 'SlideFragment.onAttach', 'FRAMEWORK',
  'the new page fragment is attached to the intro activity (its context must be IntroBaseActivity)',
  evidence=_FW_B32_ATTACH + '; SRC ui/intro/SlideFragment.java:17-25')

# the page on screen: the framework inflates and resumes the page fragment (SYSTEM from the screen state, as for S_LIST and MainActivity.onPause)
e('S_INTRO_WELCOME', 'WelcomeSlide.onCreateView', 'SYSTEM', 'the Welcome page is shown: its layout (the Import button) is inflated',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/WelcomeSlide.java:40-49')
e('S_INTRO_WELCOME', 'SlideFragment.onResume', 'SYSTEM',
  'the Welcome page resumes (it has no onResume of its own): it tells the activity it is the current slide',
  evidence=_FW_B32_FRAG + '; SRC ui/intro/SlideFragment.java:28-32')
e('S_INTRO_PICKER', 'SecurityPickerSlide.onCreateView', 'SYSTEM', 'the security picker page is shown: its layout (the three options) is inflated',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/SecurityPickerSlide.java:28-36')
e('S_INTRO_PICKER', 'SecurityPickerSlide.onResume', 'SYSTEM', 'the security picker page resumes: the biometrics option is refreshed',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/SecurityPickerSlide.java:38-42')
e('S_INTRO_SETUP', 'SecuritySetupSlide.onCreateView', 'SYSTEM', 'the security setup page is shown: its layout (the password fields) is inflated',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/SecuritySetupSlide.java:53-86')
e('S_INTRO_SETUP', 'SecuritySetupSlide.onResume', 'SYSTEM', 'the security setup page resumes: it reads the security type that the picker saved',
  guard='the picker saved password or biometrics (the page throws for none or an invalid type, SecuritySetupSlide.java:92-95)',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/SecuritySetupSlide.java:88-98')
e('S_INTRO_DONE', 'DoneSlide.onCreateView', 'SYSTEM', 'the Done page is shown: its layout is inflated',
  evidence=_FW_B32_FRAG + '; SRC ui/slides/DoneSlide.java:12-15')
gui('S_INTRO_SETUP', 'SecuritySetupSlide.lambda$onCreateView$0', 'Tick or untick Show password (the password fields show or hide the text)',
    evidence=_FW_B32_CHECK + '; SRC ui/slides/SecuritySetupSlide.java:63-73')

# the intro activity: restore and save of the intro state, the pager scroll callback, the indicator view and its draw
e('IntroBaseActivity.onCreate', 'IntroBaseActivity.onRestoreInstanceState', 'LIFECYCLE',
  'the framework restores the saved intro state after onStart (the intro was recreated, for example after a rotation)',
  guard='a saved instance state exists', evidence=FW_RESTORE + '; SRC ui/intro/IntroBaseActivity.java:63-67')
e('IntroBaseActivity.onCreate', 'IntroBaseActivity.onSaveInstanceState', 'SYSTEM',
  'API 27: the framework saves the instance state after onPause (the intro is left or the device is rotated)',
  evidence=FW_SAVE + '; SRC ui/intro/IntroBaseActivity.java:70-73')
e('IntroBaseActivity.setPagerPosition(int)', 'IntroBaseActivity$SlideSkipBlocker.onPageScrollStateChanged', 'FRAMEWORK',
  'the pager reports its scroll state while it moves to the next or previous slide: the buttons are disabled until it settles',
  guard='the transition animation is on, so the move is a smooth scroll (IntroBaseActivity.java:141-142)',
  evidence=_FW_B32_SCROLL + '; SRC ui/intro/IntroBaseActivity.java:141-142,224-231')
e('IntroBaseActivity.onCreate', 'SlideIndicator.<init>', 'FRAMEWORK',
  'setContentView inflates the intro layout, which creates the slide indicator view',
  evidence=_FW_B26_INFLATE + '; SRC res/layout/activity_intro.xml; SRC ui/intro/IntroBaseActivity.java:38,48')
e('IntroBaseActivity.onCreate', 'SlideIndicator.onDraw', 'FRAMEWORK',
  'the intro is drawn: View.draw calls onDraw, which paints the dots',
  guard='the slide count is above 0 (onDraw returns early otherwise, SlideIndicator.java:69-71)',
  evidence=_FW_B32_DRAW + '; SRC ui/intro/SlideIndicator.java:67-71')

# the Welcome import: the ImportFileTask result goes to the callback lambda (same mechanism as EditEntryActivity.lambda$new$0 above)
e('ImportFileTask.onPostExecute@WELCOME', 'WelcomeSlide.lambda$startImportVault$2', 'CALL',
  '_cb.onTaskFinished(result): the import result goes to the Welcome slide (an error dialog, or the vault is imported and the slide moves on)',
  evidence='SRC ui/tasks/ImportFileTask.java:53-59; SRC ui/slides/WelcomeSlide.java:59-94')

# the span on the hidden code dots: EntryHolder.updateTextViewWithDots sets the spanned text, and the text view calls the span when it measures and draws it
e('EntryHolder.updateTextViewWithDots', 'CenterVerticalSpan.updateMeasureState', 'FRAMEWORK',
  'the hidden code dots are set on the text view: the text view measures the spanned text, which calls updateMeasureState',
  guard='the entry shows hidden codes (hideCode runs from EntryHolder.setData, EntryHolder.java:166, or from the focus changes, EntryAdapter.java:643,670)',
  evidence=_FW_B32_SPAN + '; SRC ui/views/EntryHolder.java:387-425; SRC helpers/CenterVerticalSpan.java:16-19')
e('EntryHolder.updateTextViewWithDots', 'CenterVerticalSpan.updateDrawState', 'FRAMEWORK',
  'the text view draws the dots: View.draw calls onDraw of the text view, which draws the spanned text and calls updateDrawState',
  guard='the entry shows hidden codes (see the measure edge above)',
  evidence=_FW_B32_DRAW + '; ' + _FW_B32_SPAN + '; SRC helpers/CenterVerticalSpan.java:21-24')

# --- batch 33 (Glide icon loading): after GlideHelper.loadEntryIcon starts a load, the Glide library calls the VaultEntryIcon model loader,
# its key, its fetcher, the SVG decoders and the transcoder. The Glide source is not read, so these library calls are INFERRED and carry guards.
# The app-side constructor calls (buildLoadData -> Fetcher.<init> and Key.<init>, Factory.build -> loader.<init>, SvgBytesDecoder -> SvgDecoder)
# already come from the bytecode auto rows.
assert 'VaultEntryIconLoader$Factory.build' in _UNIV_SHORT and 'VaultEntryIconLoader.handles' in _UNIV_SHORT
assert 'VaultEntryIconLoader.buildLoadData' in _UNIV_SHORT and 'VaultEntryIconKey.updateDiskCacheKey' in _UNIV_SHORT
assert 'VaultEntryIconKey.hashCode' in _UNIV_SHORT and 'VaultEntryIconKey.equals' in _UNIV_SHORT
assert 'VaultEntryIconLoader$Fetcher.getDataClass' in _UNIV_SHORT and 'VaultEntryIconLoader$Fetcher.getDataSource' in _UNIV_SHORT
assert 'VaultEntryIconLoader$Fetcher.loadData' in _UNIV_SHORT and 'VaultEntryIconLoader$Fetcher.cleanup' in _UNIV_SHORT
assert 'VaultEntryIconLoader$Fetcher.cancel' in _UNIV_SHORT and 'VaultEntryIconLoader$Factory.teardown' in _UNIV_SHORT
assert 'SvgBytesDecoder.handles' in _UNIV_SHORT and 'SvgBytesDecoder.decode' in _UNIV_SHORT
assert 'SvgDrawableTranscoder.transcode' in _UNIV_SHORT and 'GlideHelper.lambda$setCommonOptions$0' in _UNIV_SHORT
assert 'GlideHelper$ViewReadyListener.onResourceReady' in _UNIV_SHORT and 'GlideHelper$ViewReadyListener.onLoadFailed' in _UNIV_SHORT
assert 'GlideHelper.<init>' in _UNIV_SHORT
_B33_ICON_GUARD = 'the entry has an icon (GlideHelper.java:40-41)'
_B33_ICON_EV = 'INFERRED Glide (source not read); SRC ui/glide/GlideHelper.java:41; SRC ui/glide/AegisGlideModule.java:23'
_B33_FETCH_EV = 'INFERRED Glide (source not read); SRC ui/glide/VaultEntryIconLoader.java:39-42,57-65'
_B33_DEC_EV = 'INFERRED Glide (source not read); SRC ui/glide/SvgBytesDecoder.java:17-28; SRC ui/glide/SvgDecoder.java:23-26'
_B33_LISTENER_EV = 'INFERRED Glide (source not read); SRC ui/glide/GlideHelper.java:57-63,84-105'
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Factory.build', 'FRAMEWORK',
  'the Glide library builds the loader for the VaultEntryIcon model (registered at AegisGlideModule.java:23) the first time that model is loaded',
  guard=_B33_ICON_GUARD + ', and no loader for this model exists yet (INFERRED: Glide builds each loader once)', evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader.handles', 'FRAMEWORK',
  'the Glide library asks the model loader whether it handles the VaultEntryIcon model before it starts the load',
  guard=_B33_ICON_GUARD, evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader.buildLoadData', 'FRAMEWORK',
  'the Glide library builds the load data (a key and a fetcher) for the entry icon',
  guard=_B33_ICON_GUARD + ', and the load is not answered from the memory cache (INFERRED)', evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconKey.updateDiskCacheKey', 'FRAMEWORK',
  'the Glide library adds the icon hash to the disk-cache key when it builds one',
  guard=_B33_ICON_GUARD + ', and the library builds a disk-cache key (INFERRED: DiskCacheStrategy.NONE at GlideHelper.java:66 may skip it)', evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconKey.hashCode', 'FRAMEWORK',
  'the Glide library hashes the key to place the load in its internal maps',
  guard=_B33_ICON_GUARD + ' (INFERRED: the library keeps the key in a map)', evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconKey.equals', 'FRAMEWORK',
  'the Glide library compares the key with the keys already in its internal maps',
  guard=_B33_ICON_GUARD + ' (INFERRED: the library keeps the key in a map)', evidence=_B33_ICON_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Fetcher.getDataClass', 'FRAMEWORK',
  'the Glide library asks the fetcher for its data class (ByteBuffer) before it decodes the data',
  guard=_B33_ICON_GUARD + ', and the fetch is started (INFERRED)', evidence=_B33_FETCH_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Fetcher.getDataSource', 'FRAMEWORK',
  'the Glide library asks where the fetched data came from (the fetcher reports MEMORY_CACHE, because the bytes are already in memory)',
  guard=_B33_ICON_GUARD + ', and the fetch is started (INFERRED)', evidence=_B33_FETCH_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Fetcher.loadData', 'FRAMEWORK',
  'the Glide library starts the fetch: loadData passes the icon bytes to the library callback',
  guard=_B33_ICON_GUARD + ', and the load is not answered from the memory cache (INFERRED)', evidence=_B33_FETCH_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Fetcher.cleanup', 'FRAMEWORK',
  'the Glide library calls cleanup on the fetcher once the fetch has finished',
  guard=_B33_ICON_GUARD + ', and the fetch has finished (INFERRED)', evidence=_B33_FETCH_EV)
e('GlideHelper.loadEntryIcon', 'VaultEntryIconLoader$Fetcher.cancel', 'FRAMEWORK',
  'rm.clear(targetView) cancels the pending load for this view, and the library cancels its running fetch',
  guard='the entry has no icon (the else branch, GlideHelper.java:43-45), and an earlier load for this view is still running (INFERRED)', evidence=_B33_FETCH_EV)
# the library hands the bytes to its decoders inside the callback of loadData (the same thread; INFERRED)
e('VaultEntryIconLoader$Fetcher.loadData', 'SvgBytesDecoder.handles', 'FRAMEWORK',
  'the Glide library hands the icon bytes to its decoders and asks the SVG decoder whether it handles them, inside the callback that loadData makes',
  guard='the icon type is SVG (GlideHelper.java:59 sets ICON_TYPE; SvgDecoder.handles answers true only for SVG)', evidence=_B33_DEC_EV)
e('VaultEntryIconLoader$Fetcher.loadData', 'SvgBytesDecoder.decode', 'FRAMEWORK',
  'the Glide library decodes the bytes with the SVG decoder once handles has returned true',
  guard='the icon type is SVG, and the bitmap decoders before it did not take the bytes (INFERRED: Glide decoder order)', evidence=_B33_DEC_EV)
e('VaultEntryIconLoader$Fetcher.loadData', 'SvgDrawableTranscoder.transcode', 'FRAMEWORK',
  'the Glide library turns the decoded SVG into a PictureDrawable with the registered transcoder',
  guard='the SVG decode succeeded (INFERRED: the transcoder gets an SVG resource)', evidence='INFERRED Glide (source not read); SRC ui/glide/AegisGlideModule.java:24; SRC ui/glide/SvgDrawableTranscoder.java:23-29')
e('GlideHelper.setCommonOptions', 'GlideHelper$ViewReadyListener.onResourceReady', 'FRAMEWORK',
  'the Glide library calls the request listener that setCommonOptions registered, once the resource is ready',
  guard='the request has an icon type, so the listener is set (GlideHelper.java:58-63), and the load succeeds (INFERRED)', evidence=_B33_LISTENER_EV)
e('GlideHelper.setCommonOptions', 'GlideHelper$ViewReadyListener.onLoadFailed', 'FRAMEWORK',
  'the Glide library calls the request listener that setCommonOptions registered, when the load fails',
  guard='the request has an icon type (GlideHelper.java:58-63), and the load fails (INFERRED; for example an SVG that SvgDecoder.java:40-41 rejects)', evidence=_B33_LISTENER_EV)
e('GlideHelper$ViewReadyListener.onResourceReady', 'GlideHelper.lambda$setCommonOptions$0', 'CALL',
  'onResourceReady passes the target image view to the listener, which is the lambda from setCommonOptions (the interface call is not in auto_calls.json)',
  guard='the target is a drawable image-view target and a listener is set (GlideHelper.java:98-100)', evidence='SRC ui/glide/GlideHelper.java:60-63,98-102')
# Glide calls teardown on a model-loader factory only when its registry is torn down; no app code calls Glide.tearDown (grep: no hit)
UNREACHABLE['VaultEntryIconLoader$Factory.teardown'] = ('no_trigger_in_app',
    'Glide calls a model-loader factory teardown only when its registry is torn down (Glide.tearDown); no app code calls Glide.tearDown (grep of app/src/main: no hit), and the Glide source is not read',
    'ui/glide/VaultEntryIconLoader.java:76-77', 'INFERRED')
# private constructor of a static helper class (batch-28 TextDrawableHelper precedent); grep: no "new GlideHelper"
UNREACHABLE['GlideHelper.<init>'] = ('no_trigger_in_app',
    'private constructor of a static helper: no app code creates a GlideHelper (grep of app/src/main: no "new GlideHelper"); the app calls its static methods',
    'ui/glide/GlideHelper.java:27-29', 'SOURCE')

# --- batch 34 UNREACHABLE: private constructors of static helpers, implicit constructors of static-only classes, unused constructor and
# method overloads, and two OTP getters. Each reason was checked by grep of app/src/main (no "new X(" for the classes, no caller for the
# overloads, no call of the getters) and by reading the class or its callers.
_B34_CTORS = [
    ('AnimationsHelper', 'helpers/AnimationsHelper.java:10'),
    ('BiometricsHelper', 'helpers/BiometricsHelper.java:9'),
    ('BitmapHelper', 'helpers/BitmapHelper.java:13'),
    ('ContextHelper', 'helpers/ContextHelper.java:16'),
    ('DropdownHelper', 'helpers/DropdownHelper.java:14'),
    ('EditTextHelper', 'helpers/EditTextHelper.java:9'),
    ('MetricsHelper', 'helpers/MetricsHelper.java:7'),
    ('PermissionHelper', 'helpers/PermissionHelper.java:14'),
    ('QrCodeHelper', 'helpers/QrCodeHelper.java:28'),
    ('SafHelper', 'helpers/SafHelper.java:12'),
    ('ViewHelper', 'helpers/ViewHelper.java:10'),
    ('Cloner', 'util/Cloner.java:11'),
    ('IOUtils', 'util/IOUtils.java:12'),
    ('JsonUtils', 'util/JsonUtils.java:8'),
    ('PreferenceParser', 'util/PreferenceParser.java:11'),
    ('TimeUtils', 'util/TimeUtils.java:12'),
]
for _c, _ref in _B34_CTORS:
    _k = _c + '.<init>'
    assert _k in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app',
        'private constructor: no app code creates an instance (grep of app/src/main: no "new ' + _c + '(")', _ref, 'SOURCE')
_B34_IMPLICIT = [
    ('VibrationPatterns', 'VibrationPatterns.java:5'),
    ('CryptoUtils', 'crypto/CryptoUtils.java:26'),
    ('ClipboardUtils', 'util/ClipboardUtils.java:7'),
    ('CollectionUtils', 'util/CollectionUtils.java:5'),
]
for _c, _ref in _B34_IMPLICIT:
    _k = _c + '.<init>'
    assert _k in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app',
        'the class declares no constructor and has no instance members (grep of its file: every member is static), and no app code creates an instance (grep of app/src/main: no "new ' + _c + '(")', _ref, 'SOURCE')
_B34_EXC = [
    ('KeyStoreHandleException.<init>(String)', 'crypto/KeyStoreHandleException.java:8',
        'the String overload is never used: every throw site passes a caught Throwable (crypto/KeyStoreHandle.java:32,40,62,66,80,109,119)'),
    ('EncodingException.<init>(String)', 'encoding/EncodingException.java:10',
        'the String overload is never used: every throw site passes a caught exception (encoding/Base32.java:17, Base64.java:16, Hex.java:16)'),
    ('SlotIntegrityException.<init>()', 'vault/slots/SlotIntegrityException.java:4',
        'the no-argument overload is never used: the only throw site passes a caught exception (vault/slots/Slot.java:57)'),
    ('SlotListException.<init>(String)', 'vault/slots/SlotListException.java:8',
        'the String overload is never used: the only throw site passes a caught exception (vault/slots/SlotList.java:33)'),
    ('VaultEntryException.<init>(String)', 'vault/VaultEntryException.java:8',
        'the String overload is never used: every throw site passes a caught exception (vault/VaultEntry.java:117, vault/VaultGroup.java:43)'),
]
for _k, _ref, _why in _B34_EXC:
    assert _k.split('(')[0] in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app', _why, _ref, 'SOURCE')
assert 'MOTP.generateOTP' in _UNIV_SHORT
UNREACHABLE['MOTP.generateOTP(byte[],String,int,int,String)'] = ('no_trigger_in_app',
    'the five-argument overload only forwards to the six-argument one (MOTP.java:25), and no app code calls it: MotpInfo.java:40 calls the six-argument overload',
    'crypto/otp/MOTP.java:22-25', 'SOURCE')
assert 'TOTP.generateOTP' in _UNIV_SHORT
UNREACHABLE['TOTP.generateOTP(byte[],String,int,long)'] = ('no_trigger_in_app',
    'the four-argument overload only forwards to the five-argument one (TOTP.java:19), and no app code calls it: TotpInfo.java:37 and SteamInfo.java:27 call the five-argument overload',
    'crypto/otp/TOTP.java:17-19', 'SOURCE')
assert 'YAOTP.generateOTP' in _UNIV_SHORT
UNREACHABLE['YAOTP.generateOTP(byte[],String,int,String,long)'] = ('no_trigger_in_app',
    'the five-argument overload only forwards to the six-argument one (YAOTP.java:28), and no app code calls it: YandexInfo.java:47 calls the six-argument overload',
    'crypto/otp/YAOTP.java:25-28', 'SOURCE')
assert 'OTP.getCode' in _UNIV_SHORT and 'OTP.getDigits' in _UNIV_SHORT
UNREACHABLE['OTP.getCode'] = ('no_trigger_in_app',
    'no app code calls OTP.getCode (grep of app/src/main: no ".getCode(" call at all); OTP.toString reads the field directly (crypto/otp/OTP.java:27)',
    'crypto/otp/OTP.java:16-18', 'SOURCE')
UNREACHABLE['OTP.getDigits'] = ('no_trigger_in_app',
    'no app code calls OTP.getDigits (every ".getDigits(" call is on an OtpInfo or GoogleAuthInfo object); OTP.toString reads the field directly (crypto/otp/OTP.java:27-31)',
    'crypto/otp/OTP.java:20-22', 'SOURCE')

# --- batch 35: crypto constructors, unused Preferences and enum methods, the sort comparators, YandexInfo
_B35_CTORS = [
    ('Base32', 'encoding/Base32.java:9'),
    ('Base64', 'encoding/Base64.java:8'),
    ('Hex', 'encoding/Hex.java:8'),
    ('SCrypt', 'crypto/bc/SCrypt.java:39'),
    ('Salsa20Engine', 'crypto/bc/Salsa20Engine.java:27'),
    ('HOTP', 'crypto/otp/HOTP.java:12'),
    ('TOTP', 'crypto/otp/TOTP.java:8'),
]
for _c, _ref in _B35_CTORS:
    _k = _c + '.<init>'
    assert _k in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app',
        'private constructor: no app code creates an instance (grep of app/src/main: no "new ' + _c + '(")', _ref, 'SOURCE')
_B35_UNUSED = [
    ('Preferences.getTimeout', 'Preferences.java:360',
        'no app code calls Preferences.getTimeout (grep of app/src/main: only the definition)'),
    ('Preferences.isAutoLockEnabled', 'Preferences.java:211',
        'no app code calls the no-argument Preferences.isAutoLockEnabled (the app calls VaultManager.isAutoLockEnabled(int), a different method: AegisApplicationBase.java:109, MainActivity.java:1000, VaultLockReceiver.java:31)'),
    ('Preferences.setFocusSearch', 'Preferences.java:430',
        'no app code calls Preferences.setFocusSearch (grep of app/src/main: only the definition)'),
    ('Preferences.setIsPanicTriggerEnabled', 'Preferences.java:111',
        'no app code calls Preferences.setIsPanicTriggerEnabled (grep of app/src/main: only the definition)'),
    ('EventType.fromInteger', 'EventType.java:18',
        'no app code calls EventType.fromInteger (grep of app/src/main: only the definition)'),
    ('ColorGenerator.getRandomColor', 'com/amulyakhare/textdrawable/util/ColorGenerator.java:62',
        'no app or vendored code calls ColorGenerator.getRandomColor (grep of app/src/main: only the definition)'),
    ('YandexInfo.setPin', 'otp/YandexInfo.java:59-61',
        'no app code calls YandexInfo.setPin (the pin is passed to the two-argument constructor at EditEntryActivity.java:779, OtpInfo.java:132 and GoogleAuthInfo.java:106; the other setPin calls are in MotpInfo, which has its own method)'),
]
for _k, _ref, _why in _B35_UNUSED:
    assert _k.split('(')[0] in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app', _why, _ref, 'SOURCE')
assert 'YandexInfo.<init>' in _UNIV_SHORT
UNREACHABLE['YandexInfo.<init>(byte[])'] = ('no_trigger_in_app',
    'the one-argument constructor only delegates to the two-argument one (YandexInfo.java:31), and no app code calls it: the three creation sites all pass a pin (EditEntryActivity.java:779, OtpInfo.java:132, GoogleAuthInfo.java:106)',
    'otp/YandexInfo.java:30-32', 'SOURCE')
# the comparators run only through EntryAdapter.sortEntries (the category sort, then the favorites sort); Collections.sort compares pairs, so a list needs two or more entries
_FW_B35_TIE = ('INFERRED java.util.Comparator.thenComparing: the composed comparator calls the second comparator only when the first returns 0 (JDK source not read)')
e('EntryAdapter.sortEntries', 'FavoriteComparator.compare', 'FRAMEWORK',
  'the shown entries are sorted with the favorites first',
  guard='the list holds two or more entries (the sort compares only pairs)',
  evidence=_FW_B31_SORT + '; SRC ui/views/EntryAdapter.java:319-320; SRC helpers/comparators/FavoriteComparator.java:9-11')
e('EntryAdapter.sortEntries', 'AccountNameComparator.compare', 'FRAMEWORK',
  'the category sort compares the shown entries by account name',
  guard='the list holds two or more entries, and the category is ACCOUNT or ACCOUNT_REVERSED, or ISSUER or ISSUER_REVERSED with equal issuers (SortCategory.java:35-45)',
  evidence=_FW_B31_SORT + '; ' + _FW_B35_TIE + '; SRC ui/views/EntryAdapter.java:311-315; SRC SortCategory.java:35-45; SRC helpers/comparators/AccountNameComparator.java:9-11')
e('EntryAdapter.sortEntries', 'IssuerNameComparator.compare', 'FRAMEWORK',
  'the category sort compares the shown entries by issuer',
  guard='the list holds two or more entries, and the category is ISSUER or ISSUER_REVERSED, or ACCOUNT or ACCOUNT_REVERSED with equal account names (SortCategory.java:35-45)',
  evidence=_FW_B31_SORT + '; ' + _FW_B35_TIE + '; SRC ui/views/EntryAdapter.java:311-315; SRC SortCategory.java:35-45; SRC helpers/comparators/IssuerNameComparator.java:9-11')
e('EntryAdapter.sortEntries', 'UsageCountComparator.compare', 'FRAMEWORK',
  'the category sort orders the shown entries by usage count, most used first',
  guard='the list holds two or more entries and the category is USAGE_COUNT (SortCategory.java:47-48)',
  evidence=_FW_B31_SORT + '; SRC ui/views/EntryAdapter.java:311-315; SRC SortCategory.java:47-48; SRC helpers/comparators/UsageCountComparator.java:9-11')
e('EntryAdapter.sortEntries', 'LastUsedComparator.compare', 'FRAMEWORK',
  'the category sort orders the shown entries by last use, most recent first',
  guard='the list holds two or more entries and the category is LAST_USED (SortCategory.java:50-51)',
  evidence=_FW_B31_SORT + '; SRC ui/views/EntryAdapter.java:311-315; SRC SortCategory.java:50-51; SRC helpers/comparators/LastUsedComparator.java:9-11')

# --- batch 36: unused VaultEntry, Slot, VaultGroupModel, VaultHtmlExporter and ErrorCardInfo methods, the animation listeners, the insets lambda, the error card equality, the stream filters
_B36_UNUSED = [
    ('VaultEntry.isDefault', 'vault/VaultEntry.java:249-251',
        'no app code calls VaultEntry.isDefault (grep of app/src/main: no call, and no layout or data-binding reference)'),
    ('Slot.getEncryptedMasterKey', 'vault/slots/Slot.java:100-102',
        'no app code calls the protected Slot.getEncryptedMasterKey (grep of app/src/main: no call)'),
    ('VaultGroupModel.getGroup', 'ui/models/VaultGroupModel.java:31-33',
        'no app code calls VaultGroupModel.getGroup (grep of app/src/main: no call)'),
    ('VaultHtmlExporter.<init>', 'vault/VaultHtmlExporter.java:26-28',
        'private constructor: no app code creates an instance (grep of app/src/main: the only use is the static call VaultHtmlExporter.export at VaultRepository.java:217)'),
    ('ErrorCardInfo.hashCode', 'ui/models/ErrorCardInfo.java:27-29',
        'no code puts ErrorCardInfo in a hash-based collection or calls hashCode (grep of app/src/main: MainActivity.java:1164-1196 creates the card, EntryAdapter.java:152-153 and 943 compare it with Objects.equals)'),
]
for _k, _ref, _why in _B36_UNUSED:
    assert _k.split('(')[0] in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app', _why, _ref, 'SOURCE')
# the listener is attached only to animations that never repeat (the default repeat count is 0)
assert 'SimpleAnimationEndListener.onAnimationRepeat' in _UNIV_SHORT
UNREACHABLE['SimpleAnimationEndListener.onAnimationRepeat'] = ('framework_never_calls',
    'the listener is attached only to animations that never repeat: the fade-out AlphaAnimation (EditEntryActivity.java:486, no repeat set) and item_scale_out (no android:repeatCount in res/anim; the default repeat count is 0)',
    'helpers/SimpleAnimationEndListener.java:25-27', 'INFERRED')
_FW_B36_ANIM_START = ('INFERRED android.view.animation calls AnimationListener.onAnimationStart when the animation first runs (Animation source not in fw_src)')
_FW_B36_VPA_END = ('INFERRED android.animation: ViewPropertyAnimator calls AnimatorListener.onAnimationEnd when the slide ends (android.animation source not in fw_src)')
# the fade-out and the scale-out start first, then the listener is set; the animation starts on the next draw, so the listener is in place (INFERRED)
e('EditEntryActivity.openAdvancedSettings', 'SimpleAnimationEndListener.onAnimationStart', 'FRAMEWORK',
  'the fade-out of the advanced settings link starts',
  note='the listener is set after startAnimation (EditEntryActivity.java:489, then 491); the animation starts on the next draw, so the listener is in place (INFERRED)',
  evidence=_FW_B36_ANIM_START + '; SRC ui/EditEntryActivity.java:489-491')
e('EntryHolder.setFocusedAndAnimate', 'SimpleAnimationEndListener.onAnimationStart', 'FRAMEWORK',
  'the scale-out of an unfocused row starts',
  guard='the row is unfocused (EntryHolder.java:270-272)',
  note='the same order as openAdvancedSettings: startAnimation (EntryHolder.java:271), then the listener (line 272) (INFERRED)',
  evidence=_FW_B36_ANIM_START + '; SRC ui/views/EntryHolder.java:271-272')
# the two anonymous AnimatorListenerAdapter classes in FabScrollHelper: $1 is the show branch, $2 the hide branch (source order)
e('FabScrollHelper.setVisible', 'FabScrollHelper$1.onAnimationEnd', 'FRAMEWORK',
  'the menu finishes sliding in: the listener clears the animating flag',
  guard='visible is true (FabScrollHelper.java:27-38)',
  evidence=_FW_B36_VPA_END + '; SRC helpers/FabScrollHelper.java:29-38')
e('FabScrollHelper.setVisible', 'FabScrollHelper$2.onAnimationEnd', 'FRAMEWORK',
  'the menu finishes sliding out: the listener hides the menu',
  guard='visible is false (FabScrollHelper.java:39-53)',
  evidence=_FW_B36_VPA_END + '; SRC helpers/FabScrollHelper.java:43-53')
e('ViewHelper.setupAppBarInsets', 'ViewHelper.lambda$setupAppBarInsets$0', 'FRAMEWORK',
  'window insets are dispatched to the app bar, which calls the insets listener',
  evidence='FW-SRC core/java/android/view/View.java:9196-9197 (setOnApplyWindowInsetsListener stores the listener) and View.java:9225 (the listener is called); INFERRED androidx ViewCompat passes the lambda to it (androidx source not read); SRC helpers/ViewHelper.java:14-24')
e('EntryAdapter.setErrorCardInfo', 'ErrorCardInfo.equals', 'FRAMEWORK',
  'the new error card is compared with the current one (Objects.equals)',
  guard='the new card is not null and is not the same object as the current card (JDK Objects.equals calls a.equals(b) only then)',
  evidence='INFERRED java.util.Objects.equals: a.equals(b) runs only when a is not null and a is not b (JDK source not read); SRC ui/views/EntryAdapter.java:152-154; SRC ui/models/ErrorCardInfo.java:32-43')
# stream filters: Stream.filter (JDK) calls the Predicate lambda for each element, so the lambda is reached through the JDK
e('VaultRepository.findGroupByName', 'VaultRepository.lambda$findGroupByName$0', 'CALL',
  'the stream filter keeps the group with the given name',
  guard='the vault holds at least one group (the predicate runs once per group until a match)',
  cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$findGroupByName$0 for each group until one matches',
  evidence='SRC vault/VaultRepository.java:289-294; INFERRED Stream.filter (JDK source not read)')
e('VaultRepository.getUsedGroups', 'VaultRepository.lambda$getUsedGroups$1', 'CALL',
  'the stream filter keeps the groups that at least one entry uses',
  guard='the vault holds at least one group (the predicate runs once per group)',
  cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$getUsedGroups$1 for each group',
  evidence='SRC vault/VaultRepository.java:321-329; INFERRED Stream.filter (JDK source not read)')
e('Vault.migrateOldGroup', 'Vault.lambda$migrateOldGroup$0', 'CALL',
  'the stream filter keeps the group whose name matches the entry old group name',
  guard='the entry has an old group name (Vault.java:119)',
  cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$migrateOldGroup$0 for each group until one matches',
  evidence='SRC vault/Vault.java:118-123; INFERRED Stream.filter (JDK source not read)')
e('SlotList.findRegularPasswordSlots', 'SlotList.lambda$findRegularPasswordSlots$0', 'CALL',
  'the stream filter keeps the password slots that are not backups',
  guard='the vault holds at least one password slot',
  cls='non_standard',
  via='java.util.stream.Stream.filter (JDK) calls the Predicate lambda$findRegularPasswordSlots$0 for each password slot',
  evidence='SRC vault/slots/SlotList.java:65-69; INFERRED Stream.filter (JDK source not read)')

# --- batch 37: the biometric failure callbacks and the executor, the text watcher callbacks, the inflated progress bars and
# no-autofill text fields (and their autofill type), the unused-groups equality, the group dropdown text, and the unused constructors and getters
_FW_B37_EXEC = ('INFERRED androidx.biometric.BiometricPrompt runs its callbacks through the Executor it was given '
                '(androidx source not cached)')
_FW_B37_TEXT = ('FW-SRC core/java/android/widget/TextView.java:9309-9316 and 9359-9366 (sendBeforeTextChanged and sendOnTextChanged '
                'call each TextWatcher); INFERRED the typing path calls them (the TextView input path is not read)')
_FW_B37_REMOVE = ('INFERRED java.util.AbstractSet.removeAll (JDK source not read): when the set is not larger than the collection, '
                  'it calls collection.contains for each element, and ArrayList.indexOf calls the argument equals against each stored element')
_FW_B37_AUTOFILL = ('FW-SRC core/java/android/view/View.java:7512-7535 (onProvideStructureForAssistOrAutofill asks getAutofillType for an '
                    'autofill structure) and View.java:6970,8013-8015,12196 (isAutofillable asks getAutofillType when a field takes focus); '
                    'INFERRED the framework takes these routes only with an autofill service (autofill source not read beyond these lines)')

# biometric (the prompt runs in BiometricSlotInitializer): the two failure callbacks, and the executor the prompt posts its callbacks through
e('BiometricSlotInitializer.authenticate', 'BiometricSlotInitializer.onAuthenticationError', 'FRAMEWORK',
  'the prompt ends with an error (the user cancels, or the sensor locks out): the library calls onAuthenticationError',
  env=ENV_BIOMETRIC_FAIL,
  evidence=FW_BIOPROMPT + '; SRC helpers/BiometricSlotInitializer.java:45-72,116-119')
e('BiometricSlotInitializer.authenticate', 'BiometricSlotInitializer.onAuthenticationFailed', 'FRAMEWORK',
  'the sensor reads a fingerprint or face that does not match: the library calls onAuthenticationFailed',
  env=ENV_BIOMETRIC_FAIL,
  evidence=FW_BIOPROMPT + '; SRC helpers/BiometricSlotInitializer.java:45-72,128-130')
e('BiometricSlotInitializer.authenticate', 'UiThreadExecutor.execute', 'FRAMEWORK',
  'the prompt starts and the library hands its callbacks to the executor that the initializer created',
  evidence=_FW_B37_EXEC + '; SRC helpers/BiometricSlotInitializer.java:29-37,45-72')
e('AuthActivity.showBiometricPrompt', 'UiThreadExecutor.execute', 'FRAMEWORK',
  'the unlock prompt starts and the library hands its callbacks to the executor that the screen created',
  evidence=_FW_B37_EXEC + '; SRC ui/AuthActivity.java:284,291')

# the text watchers: beforeTextChanged and onTextChanged are empty; TextView calls them on each change, on the same registration as afterTextChanged
gui('EditEntryActivity.onCreate', 'SimpleTextWatcher.beforeTextChanged', 'Type or change a text field of the entry (the watchers run)',
    evidence=_FW_B37_TEXT + '; SRC ui/EditEntryActivity.java:307-320; SRC helpers/SimpleTextWatcher.java:14-16')
gui('EditEntryActivity.onCreate', 'SimpleTextWatcher.onTextChanged', 'Type or change a text field of the entry (the watchers run)',
    evidence=_FW_B37_TEXT + '; SRC ui/EditEntryActivity.java:307-320; SRC helpers/SimpleTextWatcher.java:19-21')

# the inflated views: LayoutInflater creates each XML view through its (Context,AttributeSet) constructor, so each view is created
# when its layout is inflated (the list fragment, the entry cards, and the two activity layouts through setContentView)
e('EntryListView.onCreateView', 'TotpProgressBar.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the list fragment is inflated, which creates the progress bar from its XML element',
  evidence=_FW_B26_INFLATE + '; SRC ui/views/EntryListView.java:98; SRC res/layout/fragment_entry_list_view.xml:8')
e('EntryAdapter.onCreateViewHolder', 'TotpProgressBar.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'each entry row is inflated from its card layout, which creates the progress bar from its XML element',
  guard='the row is an entry card, not the error card or the footer (EntryAdapter.java:395-403: the error-card and footer checks come first, then the card layout is returned)',
  evidence=_FW_B26_INFLATE + '; SRC ui/views/EntryAdapter.java:407-411; SRC ViewMode.java:22-34; SRC res/layout/card_entry.xml:197; '
           'SRC res/layout/card_entry_compact.xml:202; SRC res/layout/card_entry_tile.xml:189; SRC res/layout/card_entry_small.xml:198')
e('EditEntryActivity.onCreate', 'NoAutofillEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the edit page is inflated by setContentView, which creates the no-autofill text field from its XML element',
  evidence=_FW_B26_INFLATE + '; SRC ui/EditEntryActivity.java:170; SRC res/layout/activity_edit_entry.xml:200')
e('AuthActivity.onCreate', 'NoAutofillEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the unlock screen is inflated by setContentView, which creates the no-autofill text field from its XML element',
  evidence=_FW_B26_INFLATE + '; SRC ui/AuthActivity.java:75; SRC res/layout/activity_auth.xml:72')

# the no-autofill text field returns AUTOFILL_TYPE_NONE; the framework asks for it only when an autofill service is enabled
e('EditEntryActivity.onCreate', 'NoAutofillEditText.getAutofillType', 'FRAMEWORK',
  'an autofill service asks the edit page for its structure, or a field takes focus: the framework asks the field for its autofill type',
  env=ENV_AUTOFILL,
  evidence=_FW_B37_AUTOFILL + '; SRC ui/components/NoAutofillEditText.java:27-34; SRC ui/EditEntryActivity.java:170')
e('AuthActivity.onCreate', 'NoAutofillEditText.getAutofillType', 'FRAMEWORK',
  'an autofill service asks the unlock screen for its structure, or a field takes focus: the framework asks the field for its autofill type',
  env=ENV_AUTOFILL,
  evidence=_FW_B37_AUTOFILL + '; SRC ui/components/NoAutofillEditText.java:27-34; SRC ui/AuthActivity.java:75')

# the unused-groups removal: HashSet.removeAll reaches equals through its contains branch, which runs only when every group is used
e('GroupManagerActivity.lambda$onRemoveUnusedGroups$2', 'VaultGroup.equals', 'FRAMEWORK',
  'the removal compares the groups with the used groups (HashSet.removeAll), which calls equals when every group is used',
  guard='at least one group exists and every group is used by an entry (the used-group list is a filter of the group list, VaultRepository.java:327-329, so the set is not larger than the used-group list and removeAll takes its contains branch)',
  cls='non_standard', via='JDK library: HashSet.removeAll (AbstractSet.removeAll) reaches equals through its contains branch (JDK source not on disk)',
  evidence=_FW_B37_REMOVE + '; SRC ui/GroupManagerActivity.java:150-151; SRC vault/VaultRepository.java:321-330; SRC vault/VaultGroup.java:47-55')

# the export groups popup draws each row with item.toString(); the items are VaultGroupModel, whose toString gives the name
e('DropdownCheckBoxes$CheckboxAdapter.getView', 'VaultGroupModel.toString', 'CALL',
  'the groups popup draws each row: item.toString() gives the group name (the items are VaultGroupModel)',
  evidence='SRC ui/components/DropdownCheckBoxes.java:130-138; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:176; '
           'SRC ui/models/VaultGroupModel.java:54-56')

# UNREACHABLE: no app code creates, calls or converts these (grep of the app tree, one reason per method)
_B37_UNUSED = [
    ('BiometricSlotInitializer.<init>(FragmentActivity,Listener)', 'helpers/BiometricSlotInitializer.java:34-37',
     'no app code passes a FragmentActivity: both callers pass a Fragment (SecurityPreferencesFragment.java:117 passes '
     'SecurityPreferencesFragment.this; SecuritySetupSlide.java:101 passes this, and SecuritySetupSlide extends SlideFragment at SecuritySetupSlide.java:42)'),
    ('BiometricSlotInitializer.cancelAuthentication', 'helpers/BiometricSlotInitializer.java:78-85',
     'no app code calls BiometricSlotInitializer.cancelAuthentication: the only cancelAuthentication call in the app is AuthActivity.java:229, '
     'on the prompt of the unlock screen'),
    ('TotpProgressBar.<init>(Context)', 'ui/views/TotpProgressBar.java:18-20',
     'no app code calls the one-argument constructor (grep of the app tree: no "new TotpProgressBar"); the XML inflater uses the '
     '(Context,AttributeSet) constructor (FW-SRC LayoutInflater.java:90-91)'),
    ('NoAutofillEditText.<init>(Context)', 'ui/components/NoAutofillEditText.java:15-17',
     'no app code calls the one-argument constructor (grep of the app tree: no "new NoAutofillEditText"); the XML inflater uses the '
     '(Context,AttributeSet) constructor (FW-SRC LayoutInflater.java:90-91)'),
    ('PasswordSlotDecryptTask$Result.<init>(MasterKey,PasswordSlot)', 'ui/tasks/PasswordSlotDecryptTask.java:121-123',
     'no app code calls the two-argument constructor: the only creation of a Result is the three-argument call at '
     'PasswordSlotDecryptTask.java:77 (grep of the app tree: no other "new Result" in that file)'),
    ('ImportFileTask$Result.getUri', 'ui/tasks/ImportFileTask.java:101-103',
     'no app code calls Result.getUri: the three import callbacks read only getError and getFile (EditEntryActivity.java:151-155, '
     'ImportExportPreferencesFragment.java:152-155, WelcomeSlide.java:60-88; grep of the app tree: no getUri on a result)'),
    ('QrDecodeTask$Result.getUri', 'ui/tasks/QrDecodeTask.java:73-75',
     'no app code calls Result.getUri: the QR results are read through getException, getFileName and getResult only '
     '(MainActivity.java:674-688; grep of the app tree: no getUri on a QR result)'),
    ('VaultGroup.toString', 'vault/VaultGroup.java:65-68',
     'no app code converts a VaultGroup to a string: the dropdowns and rows hold VaultGroupModel (ImportExportPreferencesFragment.java:176; '
     'MainActivity.java:541-544), whose toString returns getName() (VaultGroupModel.java:54-56); grep of the app tree: no group string conversion'),
]
for _k, _ref, _why in _B37_UNUSED:
    assert _k.split('(')[0] in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app', _why, _ref, 'SOURCE')

# the constructors that the XML inflater never uses (it calls only the (Context,AttributeSet) constructor, FW-SRC LayoutInflater.java:90-91)
_B37_INFLATE_ONLY = ('the XML inflater creates views through the (Context,AttributeSet) constructor only (FW-SRC LayoutInflater.java:90-91), '
                     'and no app code calls this constructor (grep of the app tree)')
UNREACHABLE['TotpProgressBar.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', _B37_INFLATE_ONLY + ': no "new TotpProgressBar"',
    'ui/views/TotpProgressBar.java:26-28', 'INFERRED')
UNREACHABLE['TotpProgressBar.<init>(Context,AttributeSet,int,int)'] = ('framework_never_calls', _B37_INFLATE_ONLY + ': no "new TotpProgressBar"',
    'ui/views/TotpProgressBar.java:30-32', 'INFERRED')
UNREACHABLE['NoAutofillEditText.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', _B37_INFLATE_ONLY + ': no "new NoAutofillEditText"',
    'ui/components/NoAutofillEditText.java:23-25', 'INFERRED')

# --- batch 38: the action mode callbacks of the activity and their status guard, the application's static block, the licenses
# page, the export page's save, the progress dialog (pre-execute, progress lines, pause), the boot receiver and the two tile services;
# the unused constructors and the module that nothing creates
_FW_B38_ACTIONACT = ('INFERRED androidx.appcompat (AppCompat source not in fw_src): when an action mode starts or finishes, '
                     'AppCompat calls the activity callbacks onSupportActionModeStarted and onSupportActionModeFinished')
_FW_B38_PROGRESS = ('INFERRED AsyncTask.publishProgress (AsyncTask.java is in fw_src; the publishProgress lines were not read): '
                    'the values go to the UI thread, which calls onProgressUpdate')
_FW_B38_OBSERVER = ('INFERRED androidx.lifecycle: the library finds the method marked @OnLifecycleEvent(ON_PAUSE) on the observer '
                    'and calls it when the owner pauses (library source not read)')
_FW_B38_FRAGSAVE = ('INFERRED androidx.fragment: the FragmentManager saves each added fragment in its activity state by calling '
                    'Fragment.onSaveInstanceState (androidx source not read)')
_FW_B38_INIT = ('INFERRED JLS 12.4.2 (the Java language specification, not framework source): initializing a class first initializes its superclass')
_FW_B38_LISTEN = ('INFERRED android.service.quicksettings.TileService: the system calls onStartListening when the tile is listening, '
                  'and TileService.requestListeningState asks for that state (source not read)')

# the status guard: AegisActivity.java:69 creates it in onCreate; apply returns early when the constructor did not find the fields
_B38_GUARD = 'the constructor found both delegate fields (AegisActivity.java:193-196); without them apply returns at lines 202-204'

# the action mode: MainActivity starts it (MainActivity.java:1303-1304) and ends it in onDestroyActionMode (MainActivity.java:1534)
e('MainActivity.startActionMode', 'AegisActivity.onSupportActionModeStarted', 'FRAMEWORK',
  'the selection action mode starts (startSupportActionMode), and the framework tells the activity that it started',
  evidence=_FW_B38_ACTIONACT + '; SRC ui/MainActivity.java:1303-1304; SRC ui/AegisActivity.java:167-170')
e('MainActivity$ActionModeCallbacks.onDestroyActionMode', 'AegisActivity.onSupportActionModeFinished', 'FRAMEWORK',
  'the action mode ends (onDestroyActionMode), and the framework then tells the activity that it finished',
  evidence=_FW_B38_ACTIONACT + '; SRC ui/MainActivity.java:1534; SRC ui/AegisActivity.java:172-176')
e('AegisActivity.onSupportActionModeStarted', 'AegisActivity$ActionModeStatusGuardHack.apply', 'CALL',
  'the status guard sets the action bar background to visible (apply with View.VISIBLE)',
  guard=_B38_GUARD, evidence='SRC ui/AegisActivity.java:167-170,186-204')
e('AegisActivity.onSupportActionModeFinished', 'AegisActivity$ActionModeStatusGuardHack.apply', 'CALL',
  'the status guard sets the action bar background to gone (apply with View.GONE)',
  guard=_B38_GUARD, evidence='SRC ui/AegisActivity.java:172-176,186-204')

# the application's static block runs when AegisApplication is created, because its superclass is initialized first
e('AegisApplication.<init>', 'AegisApplicationBase.<clinit>', 'LIFECYCLE',
  'creating AegisApplication initializes its superclasses first, so the static block of AegisApplicationBase runs (it sets the libsu verbose logging flag)',
  evidence=_FW_B38_INIT + '; SRC AegisApplicationBase.java:39-42; SRC AegisApplication.java:6')

# the progress dialog task: AsyncTask calls onPreExecute before the work, onProgressUpdate for each publishProgress line, and the observer's onPause
e('ProgressDialogTask.execute', 'ProgressDialogTask.onPreExecute', 'ASYNC',
  'AsyncTask calls onPreExecute on the UI thread before the work starts (the dialog is shown)',
  evidence=FW_ASYNC + '; SRC ui/tasks/ProgressDialogTask.java:41-43,69-74')
e('IconOptimizationTask.doInBackground', 'ProgressDialogTask.onProgressUpdate', 'ASYNC',
  'the task posts a progress line for each icon (publishProgress), and AsyncTask runs onProgressUpdate on the UI thread',
  guard='more than one icon is optimised (IconOptimizationTask.java:32)',
  evidence=_FW_B38_PROGRESS + '; SRC ui/tasks/IconOptimizationTask.java:25-34; SRC ui/tasks/ProgressDialogTask.java:54-58')
e('QrDecodeTask.doInBackground', 'ProgressDialogTask.onProgressUpdate', 'ASYNC',
  'the task posts a progress line for each QR image (publishProgress), and AsyncTask runs onProgressUpdate on the UI thread',
  guard='more than one image is analysed (QrDecodeTask.java:31)',
  evidence=_FW_B38_PROGRESS + '; SRC ui/tasks/QrDecodeTask.java:24-33; SRC ui/tasks/ProgressDialogTask.java:54-58')
e('ProgressDialogTask.execute', 'ProgressDialogTask$Observer.onPause', 'LIFECYCLE',
  'the lifecycle owner pauses while the task runs (ON_PAUSE): the observer dismisses the progress dialog',
  cls='non_standard', via='reflection: the androidx lifecycle library finds the method marked @OnLifecycleEvent(ON_PAUSE) on the observer and calls it (library source not read)',
  guard='the caller passed a non-null lifecycle (ProgressDialogTask.java:70-73)',
  evidence=_FW_B38_OBSERVER + '; SRC ui/tasks/ProgressDialogTask.java:69-90')

# the licenses page: AboutActivity opens it (lambda$onCreate$1 at AboutActivity.java:61-64), and the activity's onCreate follows
e('LicensesActivity.<init>', 'LicensesActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate of the licenses page (the About page opened it)',
  evidence=FW_CREATE + '; SRC ui/LicensesActivity.java:19-33')

# the export page's state: PreferencesActivity saves its state, and the fragment manager saves the open import and export page
e('PreferencesActivity.onSaveInstanceState', 'ImportExportPreferencesFragment.onSaveInstanceState', 'FRAMEWORK',
  'the activity saves its state, and the fragment manager saves the state of the open import and export page',
  guard='the import and export page is open in PreferencesActivity (it is shown from the preference at res/xml/preferences.xml:38)',
  evidence=FW_SAVE + '; ' + _FW_B38_FRAGSAVE + '; SRC ui/PreferencesActivity.java:63-65; SRC ui/fragments/preferences/ImportExportPreferencesFragment.java:139-141')

# the boot receiver is created by the system before it runs onReceive (the same manifest entry as the existing onReceive edge)
e('S_PROCESS', 'QsTileRefreshReceiver.<init>', 'ENTRY', 'the system creates the receiver when BOOT_COMPLETED or USER_UNLOCKED is delivered to it',
  env=ENV_BOOT, evidence=FW_RECEIVER + '; SRC AndroidManifest.xml:140-147; SRC receivers/QsTileRefreshReceiver.java:15-17')

# the two tile services: the system creates each one and calls onStartListening when the panel shows the tile; the boot receiver also asks for it
for _tile, _manifest in [('LaunchAppTileService', 'AndroidManifest.xml:108-119'),
                         ('LaunchScannerTileService', 'AndroidManifest.xml:121-132')]:
    _tile_file = 'services/%s.java' % _tile
    e('S_PROCESS', _tile + '.<init>', 'ENTRY', 'the system creates the tile service when the tile is tapped or its listening state is requested',
      env=ENV_QS, evidence=FW_TILE + '; SRC %s; SRC %s' % (_manifest, _tile_file))
    e('S_PROCESS', _tile + '.onStartListening', 'ENTRY', 'the Quick Settings panel opens with the tile added, and the system tells the tile that it is listening',
      env=ENV_QS, evidence=_FW_B38_LISTEN + '; SRC %s; SRC %s' % (_manifest, _tile_file))
    e('QsTileRefreshReceiver.onReceive', _tile + '.onStartListening', 'FRAMEWORK',
      'the receiver asks the system for the tile listening state (requestListeningState), and the system calls onStartListening',
      env=ENV_BOOT, guard='the device runs Android 7.0 or later (QsTileRefreshReceiver.java:24)',
      evidence=_FW_B38_LISTEN + '; SRC receivers/QsTileRefreshReceiver.java:17-28; SRC %s' % _tile_file)

# UNREACHABLE: the app never calls these (one reason each; the Hilt base constructor and the module are shown in their own source)
_B38_UNUSED = [
    ('AegisApplicationBase.initNotificationChannels', 'AegisApplicationBase.java:63-66', 'SOURCE',
     'the only call is inside a comment (issue #1047), so no code runs this method'),
    ('Hilt_AegisActivity.<init>(int)', 'AegisActivity.java:45', 'SOURCE',
     'no app source names Hilt_AegisActivity (grep of the app tree: no hits). AegisActivity, its only subclass, has no explicit '
     'constructor, so its implicit super() call runs Hilt_AegisActivity.<init>() (auto_calls row AegisActivity.<init> to '
     'Hilt_AegisActivity.<init>(), AegisActivity.java:45); no auto_calls row calls the (int) overload'),
    ('AegisModule.<init>', 'AegisModule.java:21-23', 'SOURCE',
     'the module has only static @Provides methods (AegisModule.java:24-54); no auto_calls row has AegisModule.<init> as its destination '
     '(the four rows that name it are caller-side keys or a lookup table entry)'),
]
for _k, _ref, _conf, _why in _B38_UNUSED:
    assert _k.split('(')[0] in _UNIV_SHORT, _k
    UNREACHABLE[_k] = ('no_trigger_in_app', _why, _ref, _conf)
assert 'Hilt_AegisActivity.getDefaultViewModelProviderFactory' in _UNIV_SHORT
UNREACHABLE['Hilt_AegisActivity.getDefaultViewModelProviderFactory'] = ('framework_never_calls',
    'the Hilt override supplies the ViewModel factory only when a ViewModel is requested (viewModels() or a ViewModelProvider); '
    'no app code requests one (grep of the app tree: no ViewModelProvider, viewModels() or ViewModel class)',
    'AegisActivity.java:45', 'INFERRED')

# --- batch 39: the generated Hilt components. Ten of these methods ran in the tool run (monkey or APE), so they get paths:
# the activity's retained component (saved-state holder, lifecycle, the SwitchingProvider it uses), the preferences fragment's
# component (the fragment builder, then build and fragment), and the fragment's getContext fix flag. The rest have no path in
# the app (the only @AndroidEntryPoint classes are AegisActivity, PreferencesFragment, AuditLogPreferencesFragment,
# IconPacksManagerFragment and VaultLockReceiver, so no Service, View or ViewModel component is ever built), and they are UNREACHABLE by group.
_FW_B39_HILT = ('INFERRED dagger.hilt library (the Hilt library and the generated DaggerAegisApplication_HiltComponents_SingletonC '
                'source are not in fw_src): the component manager calls the generated builder and component methods listed here')
_FW_B39_SWITCH = ('INFERRED (the retained lifecycle is read through the generic Provider interface, so the bytecode has no direct '
                  'call row (auto_calls.json has no row from getActivityRetainedLifecycle); SwitchingProvider.<init> is reached from initialize (generated line 493)')

e('Hilt_AegisActivity.generatedComponent', 'DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCBuilder.savedStateHandleHolder', 'FRAMEWORK',
  'the activity component manager gives the retained-component builder its saved-state holder before it builds the component',
  evidence=_FW_B39_HILT + '; generated Hilt_AegisActivity.java:77 (auto_calls row generatedComponent -> componentManager)')
e('Hilt_AegisActivity.generatedComponent', 'DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl.getActivityRetainedLifecycle', 'FRAMEWORK',
  'the activity component manager reads the retained component lifecycle, so the retained component can be cleared when the activity is destroyed',
  evidence=_FW_B39_HILT + '; generated Hilt_AegisActivity.java:77')
e('DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl.getActivityRetainedLifecycle',
  'DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl$SwitchingProvider.get', 'CALL',
  'the lifecycle provider creates the lifecycle object on first use',
  cls='non_standard', via='interface call: Provider.get on the generic SwitchingProvider field (a generic call has no auto_calls row)',
  evidence=_FW_B39_SWITCH)

e('Hilt_PreferencesFragment.generatedComponent', 'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.fragmentComponentBuilder', 'FRAMEWORK',
  'the fragment component manager asks the host activity component for the fragment component builder',
  evidence=_FW_B39_HILT + '; generated Hilt_PreferencesFragment.java:82 and :94 (auto_calls rows generatedComponent -> componentManager -> createComponentManager); SRC ui/fragments/preferences/PreferencesFragment.java:31')
e('Hilt_PreferencesFragment.generatedComponent', 'DaggerAegisApplication_HiltComponents_SingletonC$FragmentCBuilder.fragment', 'FRAMEWORK',
  'the library sets the fragment on the fragment component builder',
  evidence=_FW_B39_HILT + '; generated Hilt_PreferencesFragment.java:82')
e('Hilt_PreferencesFragment.generatedComponent', 'DaggerAegisApplication_HiltComponents_SingletonC$FragmentCBuilder.build', 'FRAMEWORK',
  'the library builds the fragment component (FragmentCImpl), which then injects the fragment (injectPreferencesFragment)',
  evidence=_FW_B39_HILT + '; generated Hilt_PreferencesFragment.java:104 (inject -> generatedComponent)')

e('Hilt_PreferencesFragment.getContext', 'DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.getDisableFragmentGetContextFix', 'FRAMEWORK',
  'the fragment reads the application flag that turns off its getContext fix before it looks for its context',
  evidence=_FW_B39_HILT + '; generated Hilt_PreferencesFragment.java:70 (getContext -> initializeComponentContext)')

_B39_VIEWMODEL_WHY = ('Hilt builds a ViewModel component only when a ViewModel is requested through the activity default factory '
                      '(Hilt_AegisActivity.getDefaultViewModelProviderFactory is UNREACHABLE, batch 38) or a @HiltViewModel exists; '
                      'the app has no @HiltViewModel and no ViewModel use (grep of the app tree)')
_B39_SERVICE_WHY = ('Hilt builds a service component only for a @AndroidEntryPoint service; the app has none '
                    '(grep of the app tree: the only @AndroidEntryPoint classes are AegisActivity, PreferencesFragment, '
                    'AuditLogPreferencesFragment, IconPacksManagerFragment and VaultLockReceiver)')
_B39_VIEW_WHY = ('Hilt builds a view component only for a @AndroidEntryPoint view; no app view has the annotation '
                 '(same grep; the View subclasses have no @AndroidEntryPoint)')
_B39_VIEWWF_WHY = ('Hilt builds a view-in-fragment component only for a @AndroidEntryPoint view inside a Hilt fragment; '
                   'no app view has the annotation (same grep)')
_B39_MARKER_WHY = ('generated Hilt marker or type: the aggregated root, sentinel, codegen and hilt_aggregated_deps classes, '
                   'the GeneratedInjector and EntryPoint types, the outer component class and the component tree holder; '
                   'no auto_calls.json row calls the constructor and the app never creates these objects')
_B39_GROUPS = [
    ('framework_never_calls', _B39_VIEWMODEL_WHY, 'AegisActivity.java:44-45', [
        'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getHiltInternalFactoryFactory',
        'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getViewModelComponentBuilder',
        'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getViewModelKeys',
        'DaggerAegisApplication_HiltComponents_SingletonC$FragmentCImpl.getHiltInternalFactoryFactory',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.build',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.savedStateHandle',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.viewModelLifecycle',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCImpl.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCImpl.getHiltViewModelAssistedMap',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCImpl.getHiltViewModelMap',
        'AegisApplication_HiltComponents$ViewModelC.<init>',
    ]),
    ('no_trigger_in_app', _B39_SERVICE_WHY, 'AegisActivity.java:44', [
        'AegisApplication_HiltComponents$ServiceC.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCBuilder.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCBuilder.build',
        'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCBuilder.service',
        'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCImpl.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.serviceComponentBuilder',
    ]),
    ('no_trigger_in_app', _B39_VIEW_WHY, 'AegisActivity.java:44', [
        'AegisApplication_HiltComponents$ViewC.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.viewComponentBuilder',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewCBuilder.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewCBuilder.build',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewCBuilder.view',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewCImpl.<init>',
    ]),
    ('no_trigger_in_app', _B39_VIEWWF_WHY, 'AegisActivity.java:44', [
        'AegisApplication_HiltComponents$ViewWithFragmentC.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$FragmentCImpl.viewWithFragmentComponentBuilder',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCBuilder.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCBuilder.build',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCBuilder.view',
        'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCImpl.<init>',
    ]),
    ('no_trigger_in_app', _B39_MARKER_WHY, 'AegisApplication.java:5-6', [
        'AegisApplication_ComponentTreeDeps.<init>',
        'AegisApplication_HiltComponents.<init>',
        'DaggerAegisApplication_HiltComponents_SingletonC.<init>',
        '_com_beemdevelopment_aegis_AegisApplicationBase_EntryPoint.<init>',
        '_com_beemdevelopment_aegis_AegisApplication_GeneratedInjector.<init>',
        '_com_beemdevelopment_aegis_AegisModule.<init>',
        '_com_beemdevelopment_aegis_receivers_VaultLockReceiver_GeneratedInjector.<init>',
        '_com_beemdevelopment_aegis_ui_AegisActivity_GeneratedInjector.<init>',
        '_com_beemdevelopment_aegis_ui_fragments_preferences_PreferencesFragment_GeneratedInjector.<init>',
        'aggregatedroot.codegen._com_beemdevelopment_aegis_AegisApplication.<init>',
        'codegen._com_beemdevelopment_aegis_HiltWrapper_AegisApplicationBase_EntryPoint.<init>',
        'codegen._com_beemdevelopment_aegis_ui_AegisActivity_PrefEntryPoint.<init>',
        'codegen._com_beemdevelopment_aegis_ui_LicensesActivity_PrefEntryPoint.<init>',
        'hilt_aggregated_deps._com_beemdevelopment_aegis_HiltWrapper_AegisApplicationBase_EntryPoint.<init>',
        'hilt_aggregated_deps._com_beemdevelopment_aegis_ui_AegisActivity_PrefEntryPoint.<init>',
        'hilt_aggregated_deps._com_beemdevelopment_aegis_ui_LicensesActivity_PrefEntryPoint.<init>',
        'processedrootsentinel.codegen._com_beemdevelopment_aegis_AegisApplication.<init>',
    ]),
]
for _kind, _why, _ref, _keys in _B39_GROUPS:
    for _k in _keys:
        _base = _k.split('(')[0]
        # the build adds the package prefix (for example 'aggregatedroot.codegen.') when two classes share a simple name
        assert _base in _UNIV_SHORT or any(_base == _p + _s for _p in ('aggregatedroot.codegen.', 'processedrootsentinel.codegen.',
                                                                        'codegen.', 'hilt_aggregated_deps.')
                                           for _s in _UNIV_SHORT), _k
        UNREACHABLE[_k] = (_kind, _why, _ref, 'INFERRED')

# --- batch 5 UNREACHABLE (Room): the app never calls clearAllTables (grep of the app tree: no call; AppDatabase.java:12-14 declares only auditLogDao)
UNREACHABLE['AppDatabase_Impl.clearAllTables'] = ('no_trigger_in_app',
    'generated Room method for clearing all tables: no app code calls it (grep of the app tree: no clearAllTables call), and Room does not call it while the database opens',
    'database/AppDatabase.java:12-14', 'SOURCE')

# --- batch 3 UNREACHABLE groups: one kind and one reason per group. Each group lists only methods with no caller in the
# call graph and no runtime or reflection path (those stay frontier). See readme_notes.md Limits for the frontier list.
_B3_GLIDE = """

""".split()
for _m in _B3_GLIDE:
    UNREACHABLE[_m] = ('no_trigger_in_app', 'generated Glide API classes (GlideApp, GlideOptions, GlideRequest, GlideRequests) that no app code calls: no app source file names them (grep of the app tree), and the app calls Glide.with directly (e.g. ui/AssignIconsActivity.java:236). The runtime path into this cluster, GlideRequests.<init> (built by GeneratedRequestManagerFactory), is kept out of this group as frontier.', 'ui/glide/AegisGlideModule.java:19', 'SOURCE')
_B3_PROTO = """
GoogleAuthProtos$MigrationPayload$Algorithm.valueOf
GoogleAuthProtos$MigrationPayload$Builder.addAllOtpParameters
GoogleAuthProtos$MigrationPayload$Builder.addOtpParameters(Builder)
GoogleAuthProtos$MigrationPayload$Builder.addOtpParameters(int,Builder)
GoogleAuthProtos$MigrationPayload$Builder.addOtpParameters(int,OtpParameters)
GoogleAuthProtos$MigrationPayload$Builder.clearBatchId
GoogleAuthProtos$MigrationPayload$Builder.clearBatchIndex
GoogleAuthProtos$MigrationPayload$Builder.clearBatchSize
GoogleAuthProtos$MigrationPayload$Builder.clearOtpParameters
GoogleAuthProtos$MigrationPayload$Builder.clearVersion
GoogleAuthProtos$MigrationPayload$Builder.getBatchId
GoogleAuthProtos$MigrationPayload$Builder.getBatchIndex
GoogleAuthProtos$MigrationPayload$Builder.getBatchSize
GoogleAuthProtos$MigrationPayload$Builder.getOtpParameters
GoogleAuthProtos$MigrationPayload$Builder.getOtpParametersCount
GoogleAuthProtos$MigrationPayload$Builder.getOtpParametersList
GoogleAuthProtos$MigrationPayload$Builder.getVersion
GoogleAuthProtos$MigrationPayload$Builder.hasBatchIndex
GoogleAuthProtos$MigrationPayload$Builder.removeOtpParameters
GoogleAuthProtos$MigrationPayload$Builder.setOtpParameters(int,Builder)
GoogleAuthProtos$MigrationPayload$Builder.setOtpParameters(int,OtpParameters)
GoogleAuthProtos$MigrationPayload$DigitCount.valueOf
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearAlgorithm
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearCounter
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearDigits
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearIssuer
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearName
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearSecret
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearType
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getAlgorithm
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getAlgorithmValue
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getCounter
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getDigits
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getDigitsValue
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getIssuer
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getIssuerBytes
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getName
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getNameBytes
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getSecret
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getType
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getTypeValue
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setAlgorithmValue
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setDigitsValue
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setIssuerBytes
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setNameBytes
GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setTypeValue
GoogleAuthProtos$MigrationPayload$OtpParameters.clearAlgorithm
GoogleAuthProtos$MigrationPayload$OtpParameters.clearCounter
GoogleAuthProtos$MigrationPayload$OtpParameters.clearDigits
GoogleAuthProtos$MigrationPayload$OtpParameters.clearIssuer
GoogleAuthProtos$MigrationPayload$OtpParameters.clearName
GoogleAuthProtos$MigrationPayload$OtpParameters.clearSecret
GoogleAuthProtos$MigrationPayload$OtpParameters.clearType
GoogleAuthProtos$MigrationPayload$OtpParameters.getAlgorithmValue
GoogleAuthProtos$MigrationPayload$OtpParameters.getDigitsValue
GoogleAuthProtos$MigrationPayload$OtpParameters.getIssuerBytes
GoogleAuthProtos$MigrationPayload$OtpParameters.getNameBytes
GoogleAuthProtos$MigrationPayload$OtpParameters.getTypeValue
GoogleAuthProtos$MigrationPayload$OtpParameters.newBuilder(OtpParameters)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseDelimitedFrom(InputStream)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseDelimitedFrom(InputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(ByteBuffer)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(ByteBuffer,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(ByteString)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(ByteString,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(CodedInputStream)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(CodedInputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(InputStream)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(InputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(byte[])
GoogleAuthProtos$MigrationPayload$OtpParameters.parseFrom(byte[],ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload$OtpParameters.setAlgorithmValue
GoogleAuthProtos$MigrationPayload$OtpParameters.setDigitsValue
GoogleAuthProtos$MigrationPayload$OtpParameters.setIssuerBytes
GoogleAuthProtos$MigrationPayload$OtpParameters.setNameBytes
GoogleAuthProtos$MigrationPayload$OtpParameters.setTypeValue
GoogleAuthProtos$MigrationPayload$OtpType.valueOf
GoogleAuthProtos$MigrationPayload.addAllOtpParameters
GoogleAuthProtos$MigrationPayload.addOtpParameters(int,OtpParameters)
GoogleAuthProtos$MigrationPayload.clearBatchId GoogleAuthProtos$MigrationPayload.clearBatchIndex
GoogleAuthProtos$MigrationPayload.clearBatchSize
GoogleAuthProtos$MigrationPayload.clearOtpParameters GoogleAuthProtos$MigrationPayload.clearVersion
GoogleAuthProtos$MigrationPayload.getOtpParameters
GoogleAuthProtos$MigrationPayload.getOtpParametersCount
GoogleAuthProtos$MigrationPayload.getOtpParametersOrBuilder
GoogleAuthProtos$MigrationPayload.getOtpParametersOrBuilderList
GoogleAuthProtos$MigrationPayload.getVersion GoogleAuthProtos$MigrationPayload.hasBatchIndex
GoogleAuthProtos$MigrationPayload.newBuilder(MigrationPayload)
GoogleAuthProtos$MigrationPayload.parseDelimitedFrom(InputStream)
GoogleAuthProtos$MigrationPayload.parseDelimitedFrom(InputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.parseFrom(ByteBuffer)
GoogleAuthProtos$MigrationPayload.parseFrom(ByteBuffer,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.parseFrom(ByteString)
GoogleAuthProtos$MigrationPayload.parseFrom(ByteString,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.parseFrom(CodedInputStream)
GoogleAuthProtos$MigrationPayload.parseFrom(CodedInputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.parseFrom(InputStream)
GoogleAuthProtos$MigrationPayload.parseFrom(InputStream,ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.parseFrom(byte[],ExtensionRegistryLite)
GoogleAuthProtos$MigrationPayload.removeOtpParameters
GoogleAuthProtos$MigrationPayload.setOtpParameters
""".split()
for _m in _B3_PROTO:
    UNREACHABLE[_m] = ('no_trigger_in_app', 'generated protobuf API that the app never calls: otp/GoogleAuthInfo.java is the only app file that uses GoogleAuthProtos, and it calls parseFrom(byte[]) (line 198), getOtpParametersList (204), newBuilder, the setters, addOtpParameters(OtpParameters) and build().toByteArray() (459). Protobuf runtime entry points (dynamicMethod, parser, getDefaultInstance, <clinit>, <init>, internalGet*, findValueByNumber, isInRange, registerAllExtensions) and the members they reach are kept out of this group as frontier. INFERRED: the generated writeTo reads fields directly, so the get*Value and get*Bytes accessors are not on the toByteArray path.', 'otp/GoogleAuthInfo.java:198', 'INFERRED')
_B3_HELPER = """
ThemeMap.<init>
""".split()
for _m in _B3_HELPER:
    UNREACHABLE[_m] = ('no_trigger_in_app', 'private constructor of a static-only helper class (ThemeMap): no code calls it (no incoming edge), and the class is used only through static members (ui/AegisActivity.java:117 uses ThemeMap.DEFAULT).', 'ThemeMap.java:8', 'SOURCE')
_B3_APP = """
ApkSignaturePin.doFingerprintsMatchCertificates ApkSignaturePin.getFingerprint
ApkSignaturePin.getMD5Fingerprint ApkSignaturePin.getSHA1Fingerprint
ApkSignaturePin.getSHA256Fingerprint TrustedIntents.checkTrustedSigner(PackageInfo)
TrustedIntents.isIntentSane TrustedIntents.isReceiverTrusted(ActivityInfo)
TrustedIntents.isReceiverTrusted(Intent) TrustedIntents.isReceiverTrusted(ResolveInfo)
TrustedIntents.isTrustedSigner TrustedIntents.removeAllTrustedSigners
TrustedIntents.removeTrustedSigner TrustedIntents.startActivity
""".split()
for _m in _B3_APP:
    UNREACHABLE[_m] = ('no_trigger_in_app', 'method of the bundled TrustedIntents / ApkSignaturePin library with no call site: grep of the app tree finds no caller outside its own class. The app uses only TrustedIntents.get, addTrustedSigner and getIntentFromTrustedSender (ui/PanicResponderActivity.java:30-34). The reflective path (addTrustedSigner creating the GuardianProject pins) is kept out of this group as frontier.', 'ui/PanicResponderActivity.java:30', 'SOURCE')

# batch 43: the refresh path of a MOTP code (Hex.encode route). Each hand edge has the same src and dst as the automatic row
# it replaces, so the guard and state apply to that row.
e('MainActivity.onStart', 'EntryListView.refresh', 'CALL', 'the vault is loaded and the list was loaded earlier in this instance: the codes are refreshed (refresh(false))',
  guard='the vault is loaded and _loaded is true (MainActivity.java:976-978): an earlier loadEntries ran and no lock happened since (MainActivity.java:1348-1360)',
  needs_state=ST_LIST_LOADED, evidence='SRC ui/MainActivity.java:976-988')
e('EntryAdapter.refresh', 'EntryHolder.refresh', 'CALL', 'refresh(false): every bound row refreshes its codes',
  guard='hard is false (EntryAdapter.java:233-235)', needs_state=ST_HOLDERS_BOUND,
  evidence='SRC ui/views/EntryAdapter.java:233-239; SRC ui/views/EntryAdapter.java:569')
e('EntryHolder.refreshCode', 'EntryHolder.updateCodes', 'CALL', 'the codes are updated when the row is visible and not paused',
  guard='!_hidden && !_paused (EntryHolder.java:298-299; _paused is set by setPaused, 507-511)',
  evidence='SRC ui/views/EntryHolder.java:298-299')
e('EntryHolder.updateCodes', 'EntryHolder.getOtp(int)', 'CALL', 'the next code is shown: getOtp(1) gives the code after the current one',
  guard='_showNextCode is set (EntryHolder.java:307; set at 144 for TOTP and MOTP entries when the setting is on)', needs_state=ST_SHOW_NEXT_CODE,
  evidence='SRC ui/views/EntryHolder.java:144,307-308')
e('EntryHolder.getOtp(int)', 'MotpInfo.getOtp', 'CALL', 'the entry info is a MOTP entry: the MOTP override of getOtp(long) runs',
  guard='the entry info is a TotpInfo, and so a MotpInfo (EntryHolder.java:325; MotpInfo extends TotpInfo, MotpInfo.java:14)', needs_state=ST_MOTP_ENTRY,
  via='TotpInfo.getOtp(long) override (virtual call on the TotpInfo reference, EntryHolder.java:326)',
  evidence='SRC ui/views/EntryHolder.java:325-326; SRC otp/MotpInfo.java:34')
e('MotpInfo.getOtp', 'MOTP.generateOTP(byte[],String,int,int,String,long)', 'CALL', 'the OTP is generated from the secret and the PIN',
  guard='the PIN is set: _pin is not null (MotpInfo.java:35-37; the method throws IllegalStateException otherwise)',
  evidence='SRC otp/MotpInfo.java:35-40')

# batch 42: a bytecode call from one UNREACHABLE method to another is not drawn (the caller is never reached, so the call
# carries no route). The callers are named in the callee reason; a warning check would otherwise flag each callee.
_B42_CALLS = [
    ('ApkSignaturePin.doFingerprintsMatchCertificates', 'ApkSignaturePin.getSHA256Fingerprint'),
    ('ApkSignaturePin.getMD5Fingerprint', 'ApkSignaturePin.getFingerprint'),
    ('ApkSignaturePin.getSHA1Fingerprint', 'ApkSignaturePin.getFingerprint'),
    ('ApkSignaturePin.getSHA256Fingerprint', 'ApkSignaturePin.getFingerprint'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getHiltInternalFactoryFactory', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getViewModelComponentBuilder', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.viewComponentBuilder', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewCBuilder.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$FragmentCImpl.getHiltInternalFactoryFactory', 'DaggerAegisApplication_HiltComponents_SingletonC$ActivityCImpl.getHiltInternalFactoryFactory'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$FragmentCImpl.viewWithFragmentComponentBuilder', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCBuilder.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ServiceCBuilder.build', 'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCImpl.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ServiceCImpl.<init>', 'AegisApplication_HiltComponents$ServiceC.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.serviceComponentBuilder', 'DaggerAegisApplication_HiltComponents_SingletonC$ServiceCBuilder.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewCBuilder.build', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewCImpl.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewCImpl.<init>', 'AegisApplication_HiltComponents$ViewC.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCBuilder.build', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCImpl.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewModelCImpl.<init>', 'AegisApplication_HiltComponents$ViewModelC.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCBuilder.build', 'DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCImpl.<init>'),
    ('DaggerAegisApplication_HiltComponents_SingletonC$ViewWithFragmentCImpl.<init>', 'AegisApplication_HiltComponents$ViewWithFragmentC.<init>'),
    ('Dialogs.showErrorDialog(Context,String,Exception)', 'Dialogs.showErrorDialog(Context,String,Exception,OnClickListener)'),
    ('Dialogs.showPasswordInputDialog(Context,TextInputListener)', 'Dialogs.showTextInputDialog(Context,int,int,TextInputListener,boolean)'),
    ('GlideOptions.bitmapTransform', 'GlideOptions.transform(Transformation)'),
    ('GlideOptions.centerCropTransform', 'GlideOptions.centerCrop'),
    ('GlideOptions.centerInsideTransform', 'GlideOptions.centerInside'),
    ('GlideOptions.circleCropTransform', 'GlideOptions.circleCrop'),
    ('GlideOptions.decodeTypeOf', 'GlideOptions.decode'),
    ('GlideOptions.diskCacheStrategyOf', 'GlideOptions.diskCacheStrategy'),
    ('GlideOptions.downsampleOf', 'GlideOptions.downsample'),
    ('GlideOptions.encodeFormatOf', 'GlideOptions.encodeFormat'),
    ('GlideOptions.encodeQualityOf', 'GlideOptions.encodeQuality'),
    ('GlideOptions.errorOf(Drawable)', 'GlideOptions.error(Drawable)'),
    ('GlideOptions.errorOf(int)', 'GlideOptions.error(int)'),
    ('GlideOptions.fitCenterTransform', 'GlideOptions.fitCenter'),
    ('GlideOptions.formatOf', 'GlideOptions.format'),
    ('GlideOptions.frameOf', 'GlideOptions.frame'),
    ('GlideOptions.noAnimation', 'GlideOptions.dontAnimate'),
    ('GlideOptions.noTransformation', 'GlideOptions.dontTransform'),
    ('GlideOptions.option', 'GlideOptions.set'),
    ('GlideOptions.overrideOf(int)', 'GlideOptions.override(int)'),
    ('GlideOptions.overrideOf(int,int)', 'GlideOptions.override(int,int)'),
    ('GlideOptions.placeholderOf(Drawable)', 'GlideOptions.placeholder(Drawable)'),
    ('GlideOptions.placeholderOf(int)', 'GlideOptions.placeholder(int)'),
    ('GlideOptions.priorityOf', 'GlideOptions.priority'),
    ('GlideOptions.signatureOf', 'GlideOptions.signature'),
    ('GlideOptions.sizeMultiplierOf', 'GlideOptions.sizeMultiplier'),
    ('GlideOptions.skipMemoryCacheOf', 'GlideOptions.skipMemoryCache'),
    ('GlideOptions.timeoutOf', 'GlideOptions.timeout'),
    ('GlideRequest.getDownloadOnlyRequest', 'GlideRequest.<init>(Class,RequestBuilder)'),
    ('GlideRequest.getDownloadOnlyRequest', 'GlideRequest.apply'),
    ('GoogleAuthProtos$MigrationPayload$Builder.addAllOtpParameters', 'GoogleAuthProtos$MigrationPayload.addAllOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$Builder.addOtpParameters(int,Builder)', 'GoogleAuthProtos$MigrationPayload.addOtpParameters(int,OtpParameters)'),
    ('GoogleAuthProtos$MigrationPayload$Builder.addOtpParameters(int,OtpParameters)', 'GoogleAuthProtos$MigrationPayload.addOtpParameters(int,OtpParameters)'),
    ('GoogleAuthProtos$MigrationPayload$Builder.clearBatchId', 'GoogleAuthProtos$MigrationPayload.clearBatchId'),
    ('GoogleAuthProtos$MigrationPayload$Builder.clearBatchIndex', 'GoogleAuthProtos$MigrationPayload.clearBatchIndex'),
    ('GoogleAuthProtos$MigrationPayload$Builder.clearBatchSize', 'GoogleAuthProtos$MigrationPayload.clearBatchSize'),
    ('GoogleAuthProtos$MigrationPayload$Builder.clearOtpParameters', 'GoogleAuthProtos$MigrationPayload.clearOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$Builder.clearVersion', 'GoogleAuthProtos$MigrationPayload.clearVersion'),
    ('GoogleAuthProtos$MigrationPayload$Builder.getOtpParameters', 'GoogleAuthProtos$MigrationPayload.getOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$Builder.getOtpParametersCount', 'GoogleAuthProtos$MigrationPayload.getOtpParametersCount'),
    ('GoogleAuthProtos$MigrationPayload$Builder.getVersion', 'GoogleAuthProtos$MigrationPayload.getVersion'),
    ('GoogleAuthProtos$MigrationPayload$Builder.hasBatchIndex', 'GoogleAuthProtos$MigrationPayload.hasBatchIndex'),
    ('GoogleAuthProtos$MigrationPayload$Builder.removeOtpParameters', 'GoogleAuthProtos$MigrationPayload.removeOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$Builder.setOtpParameters(int,Builder)', 'GoogleAuthProtos$MigrationPayload.setOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$Builder.setOtpParameters(int,OtpParameters)', 'GoogleAuthProtos$MigrationPayload.setOtpParameters'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearAlgorithm', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearAlgorithm'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearCounter', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearCounter'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearDigits', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearDigits'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearIssuer', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearIssuer'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearName', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearName'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearSecret', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearSecret'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.clearType', 'GoogleAuthProtos$MigrationPayload$OtpParameters.clearType'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getAlgorithmValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.getAlgorithmValue'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getDigitsValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.getDigitsValue'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getIssuerBytes', 'GoogleAuthProtos$MigrationPayload$OtpParameters.getIssuerBytes'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getNameBytes', 'GoogleAuthProtos$MigrationPayload$OtpParameters.getNameBytes'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.getTypeValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.getTypeValue'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setAlgorithmValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.setAlgorithmValue'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setDigitsValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.setDigitsValue'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setIssuerBytes', 'GoogleAuthProtos$MigrationPayload$OtpParameters.setIssuerBytes'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setNameBytes', 'GoogleAuthProtos$MigrationPayload$OtpParameters.setNameBytes'),
    ('GoogleAuthProtos$MigrationPayload$OtpParameters$Builder.setTypeValue', 'GoogleAuthProtos$MigrationPayload$OtpParameters.setTypeValue'),
    ('NotificationService.onStartCommand', 'NotificationService.serviceMethod'),
    ('SimpleItemTouchHelperCallback.onSwiped', 'EntryAdapter.onItemDismiss'),
    ('TextDrawable$Builder.buildRect', 'TextDrawable$Builder.rect'),
    ('TextDrawable$Builder.buildRoundRect', 'TextDrawable$Builder.roundRect'),
    ('TrustedIntents.isReceiverTrusted(Intent)', 'TrustedIntents.isIntentSane'),
    ('TrustedIntents.startActivity', 'TrustedIntents.isIntentSane'),
]
# Round-4 guards on calls that the bytecode scan writes automatically (auto_calls.json). A hand-written edge with the same
# source and target replaces the automatic one (build_graph.add_auto_edges skips a pair that is already written by hand).
e('Dialogs.lambda$showSetPasswordDialog$2', 'SecurityPreferencesFragment$SetBackupPasswordListener.onSlotResult', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='Slot.createEncryptCipher did not throw SlotException (Dialogs.java:168-174)',
  evidence='SRC ui/dialogs/Dialogs.java:168-175')
e('SecurityPreferencesFragment$SetBackupPasswordListener.onSlotResult', 'PreferencesFragment.saveAndBackupVault', 'CALL',
  'Direct call',
  guard='setKey and the slot add did not throw SlotException (SecurityPreferencesFragment.java:370-384)',
  evidence='SRC ui/fragments/preferences/SecurityPreferencesFragment.java:370-387')
e('VaultManager.saveAndBackup', 'VaultManager.scheduleBackup', 'CALL',
  'Direct call',
  guard='the vault is encrypted (VaultManager.java:143) and pref_backups is on (VaultManager.java:144)',
  evidence='SRC vault/VaultManager.java:143-147')
e('VaultBackupManager.createBackup(File,BackupsVersioningStrategy,Uri,int)', 'VaultBackupManager.createBackup(File,Uri,int)', 'CALL',
  'Direct call',
  guard='uri is non-null (VaultBackupManager.java:72-74) and strategy is MULTIPLE_BACKUPS (VaultBackupManager.java:77-78)',
  evidence='SRC vault/VaultBackupManager.java:72-78')
e('VaultFile.fromJson', 'VaultFile$Header.fromJson', 'CALL',
  'Direct call',
  guard='obj.getInt("version") <= VERSION (VaultFile.java:64-66)',
  evidence='SRC vault/VaultFile.java:62-68')
e('VaultFile$Header.fromJson', 'SlotList.fromJson', 'CALL',
  'Direct call',
  guard='not (obj.isNull("slots") and obj.isNull("params")) (VaultFile.java:145-147)',
  evidence='SRC vault/VaultFile.java:144-150')
e('AuthenticatorPlusImporter$EncryptedState.decrypt(char[])', 'DatabaseImporter.read', 'CALL',
  'Direct call',
  guard='a zip entry named FILENAME is found (AuthenticatorPlusImporter.java:53-55)',
  evidence='SRC importers/AuthenticatorPlusImporter.java:53-55')
# virtual read call: the receiver is the importer that ImportEntriesActivity created (lines 107-108); this hand edge gives the Aegis override its guard
e('DatabaseImporter.read', 'AegisImporter.read', 'CALL', 'the virtual read call (DatabaseImporter.java:76) runs the Aegis override',
  guard='the receiver is an AegisImporter: DatabaseImporter.create picked it from the chosen importer type (ImportEntriesActivity.java:107-108)',
  evidence='SRC importers/DatabaseImporter.java:75-77; SRC ui/ImportEntriesActivity.java:107-108')
e('VaultRepository.fromFile', 'Vault.fromJson', 'CALL',
  'Direct call',
  guard='the file is not encrypted or creds is not null (VaultRepository.java:93-95 throws otherwise)',
  evidence='SRC vault/VaultRepository.java:92-106')
e('MainActivity.onScanResult', 'MainActivity.importScannedEntries', 'CALL',
  'Direct call',
  guard='entries != null (MainActivity.java:611-614)',
  evidence='SRC ui/MainActivity.java:611-614')
# round 6 (run 9): the generated Hilt inject runs the component injection only while its injected flag is false
e('Hilt_VaultLockReceiver.inject', 'DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.injectVaultLockReceiver', 'CALL',
  'Interface call: the generated component injects the receiver (the implementation is SingletonCImpl)',
  guard='the receiver is not injected yet: the generated injected flag is false (the build class Hilt_VaultLockReceiver.class has that field)',
  evidence='INFERRED generated code: Hilt_VaultLockReceiver.java is not in the source tree; javap is not available here, so the flag test was not decompiled (the class constant pool names injected and injectVaultLockReceiver)')
_B42_CALLERS = {}
for _s, _d in _B42_CALLS:
    SUPPRESS.add((_s, _d))
    _B42_CALLERS.setdefault(_d, []).append(_s)
for _d, _srcs in _B42_CALLERS.items():
    _k, _r, _ref, _st = UNREACHABLE[_d]
    _plural = len(_srcs) > 1
    UNREACHABLE[_d] = (_k, _r + ' Bytecode caller%s %s %s UNREACHABLE too (each has its own reason), so %s not drawn.' % ('s' if _plural else '', ', '.join(sorted(_srcs)), 'are' if _plural else 'is', 'these calls are' if _plural else 'this call is'), _ref, _st)

# --- DESIGN_V2 section 1.2: @IMP chain (append-last, binding) + L3 feeder.
# The @RAW tail itself is unchanged: 9 edges total from saveAndBackupVault@RAW
# to RawSlot.getType, including Ea9adb818 as the SlotList-to-Slot dispatch edge.
# I2 cites IntroActivity.java:57-62 for the imported skip branch (audit note 2).
# No password-prefixed chain, node, or edge anywhere in this block. No bytecode token on
# any new hand edge. Deletion of the line-470 feeder edge (above) + feeder L3 are one atomic change.
e('IntroActivity.onBeforeSlideChanged@IMPORTED', 'IntroBaseActivity.skipToSlide@IMP', 'CALL', 'the Welcome slide imported a vault: the picker and setup are skipped',
  guard='the Welcome slide imported a vault (IntroActivity.java:57-62)', needs_state=ST_IMPORTED,
  evidence='SRC ui/IntroActivity.java:57-62')
e('IntroBaseActivity.skipToSlide@IMP', 'S_INTRO_DONE@IMP', 'ENTERS', 'the Done slide is shown after the skip',
  guard='the skip is the imported-vault skip (IntroActivity.java:57-62)',
  evidence='SRC ui/intro/IntroBaseActivity.java:104; SRC ui/IntroActivity.java:57-62')
gui('S_INTRO_DONE@IMP', 'IntroActivity.onDonePressed@IMP', 'Tap Next on the Done slide',
    evidence=FW_CLICK + '; SRC ui/intro/IntroBaseActivity.java:47,80-93')
e('IntroActivity.onDonePressed@IMP', 'IntroActivity.onDonePressed@SAVED@IMP', 'CALL', 'the imported vault is read and loaded, then onDonePressed goes on',
  guard='the Welcome slide imported a vault (IntroActivity.java:57-62) and readVaultFile and loadFrom return without an error (IntroActivity.java:106-123)', needs_state=ST_IMPORTED,
  evidence='SRC ui/IntroActivity.java:106-123')
e('IntroActivity.onDonePressed@SAVED@IMP', 'MainActivity.lambda$new$1@IMP', 'RESULT', "setResult(RESULT_OK) and finish() return the result to the caller's launcher",
  guard='the vault was loaded from the import, with no error dialog (the error branches return at 113 and 121)',
  evidence='SRC ui/IntroActivity.java:125-129; ' + FW_RESULT + '; ' + FW_FINISH + '; ' + FW_LAUNCHER)
e('MainActivity.lambda$new$1@IMP', 'MainActivity.onIntroResult@IMP', 'CALL', 'RESULT_OK from the intro: the list is loaded',
  guard='the intro returned RESULT_OK (MainActivity.java:145)',
  evidence='SRC ui/MainActivity.java:142-148')
e('MainActivity.onIntroResult@IMP', 'MainActivity.loadEntries@IMP', 'CALL', 'the entries are loaded after the intro',
  evidence='SRC ui/MainActivity.java:752-754')
e('MainActivity.loadEntries@IMP', 'S_LIST@IMP', 'ENTERS', 'the list is shown (vault loaded, list loaded in this instance)',
  guard='list not yet loaded in this instance (_loaded false, MainActivity.java:1134) and the vault is loaded (getVault() throws when none is loaded, VaultManager.java:231-233): a producer of the loaded vault must come earlier on the route (the intro result)',
  evidence='SRC ui/MainActivity.java:1133-1144; SRC vault/VaultManager.java:231-233')
gui('S_LIST@IMP', 'MainActivity.lambda$startAssignGroupsDialog$15@IMP', 'Tap OK in the assign-groups dialog (assigns the groups to the selected entries)',
    needs_state=ST_ASSIGN_DIALOG, evidence=FW_CLICK + '; SRC ui/MainActivity.java:570-597')
e('MainActivity.lambda$startAssignGroupsDialog$15@IMP', 'MainActivity.saveAndBackupVault@IMP', 'CALL', 'Direct call',
  evidence='SRC ui/MainActivity.java:594')
e('MainActivity.saveAndBackupVault@IMP', 'AegisActivity.saveAndBackupVault@RAW', 'CALL', 'the imported live vault is saved and backed up: the plain save calls the superclass save',
  guard='this is a plain (unconditional) save from the imported live vault, not a repaired-slot save: the override calls super (MainActivity.java:1370-1371) and the superclass save backs the vault up (AegisActivity.java:139-141)',
  evidence='SRC ui/MainActivity.java:1370-1371; SRC ui/AegisActivity.java:139-141')
# --- DESIGN_V3_CORRECTED section 1.2: plain counterparts P1/P2 (append-last, binding).
# P1/P2 DO use the (bytecode) token deliberately, to preserve the ids of the suppressed
# plain auto edges Ed3fd969c and E30bbb737: short file form, no ui/ prefix, verbatim.
# P1/P2 are plain-to-plain restorations only: neither feeds a @RAW node, and neither
# adds a new base pair beyond L2/L3. P1 first, then P2.
e('MainActivity.lambda$startAssignGroupsDialog$15', 'MainActivity.saveAndBackupVault', 'CALL', 'Direct call',
  evidence='SRC MainActivity.java:594 (bytecode)')
e('MainActivity.saveAndBackupVault', 'AegisActivity.saveAndBackupVault', 'CALL', 'Direct call',
  evidence='SRC MainActivity.java:1371 (bytecode)')


# ---- W2 REAUDIT (Kiro): baseline and setup-only screens (appended at the end,
# so EDIT below wraps the EDIT defined above) ----
# Baseline for Aegis (review/TASK_NOTE.md): the onboarding is passed and the
# vault holds two entries; the setup vault is password-protected (unlocking is
# typing the password, a GUI action: MUSE_REAUDIT_QUESTIONS.md Q3) and the two
# entries are default TOTP entries (Q6). Baseline state never counts as state,
# so the gates the baseline satisfies are cleared in EDIT below, with the
# reason in the edge note. The four intro pages are only shown during the
# first-run setup, so they go into SETUP_ONLY (their gate texts are kept).
# Per-text decisions and source evidence: graphs/Aegis/scratch/reaudit/state_gates.csv.
SETUP_ONLY = {'S_INTRO_WELCOME', 'S_INTRO_PICKER', 'S_INTRO_SETUP', 'S_INTRO_DONE'}

_W2_CLEARED = {
    'The intro security picker chose none, so the setup slide is skipped (IntroActivity.java:50-55)':
        'baseline: the onboarding (first-run setup) is passed; the intro picker branch belongs to that setup, and the intro pages are in SETUP_ONLY (IntroActivity.java:50-55)',
    'The Welcome slide did not import a vault in this intro run (intro state "imported" is false, IntroActivity.java:86-100)':
        'baseline: the onboarding is passed with a new vault, not an imported one; the intro Done branch belongs to the setup, and the intro pages are in SETUP_ONLY (IntroActivity.java:86-100)',
    'The vault is loaded in this process and has not been locked since':
        'baseline: the setup vault exists; a normal start reads it and, when it is encrypted, opens AuthActivity, where unlocking is typing the password (a GUI action, Q3) (MainActivity.java:950-976)',
    'This MainActivity instance has loaded the entry list (loadEntries ran)':
        'baseline: once the vault is loaded, MainActivity.onStart calls loadEntries on the normal start, which sets the entries of the list (MainActivity.java:991-992; MainActivity.java:1133-1138)',
    'A vault file exists in the app data (created by an earlier intro run; MainActivity.onStart reads it)':
        'baseline: the onboarding created the vault file, which MainActivity.onStart reads (MainActivity.java:950-953)',
    'The vault holds a TOTP or HOTP entry with SHA-1 and 6 digits, so the Google Authenticator export is not empty (ImportExportPreferencesFragment.java:352-363)':
        'baseline: the vault holds two entries; a new entry defaults to TOTP with SHA1 and 6 digits (Q6), so the export list is not empty (ImportExportPreferencesFragment.java:352-360; VaultEntry.java:253-255; OtpInfo.java:14-15)',
    'At least one entry row is bound, so EntryAdapter.onBindViewHolder has added an EntryHolder to _holders (EntryAdapter.java:569)':
        'baseline: the vault holds two entries, so the list binds their rows when the main screen shows them (EntryAdapter.java:569; MainActivity.java:1137)',
    'The vault holds at least one entry (the loop in Vault.toJson(EntryFilter) runs, Vault.java:9-12)':
        'baseline: the setup vault holds two entries, so the loop in Vault.toJson runs (Vault.java:9-12)',
    'The vault has a password slot (the intro chose the password security)':
        'baseline: the setup vault is password-protected (Q3), so it has a password slot (AuthActivity.java:172-174 (unlock with the password slots); MUSE_REAUDIT_QUESTIONS.md Q3)',
    'the entry list passed in is not empty: the for loop at EntryAdapter.java:301 runs once per entry':
        'baseline: the setup vault holds two entries, so loadEntries passes a non-empty list (EntryAdapter.java:301; MainActivity.java:1137)',
    'The vault is encrypted: VaultRepository.isEncryptionEnabled is true (the vault has credentials, VaultRepository.java:352-354), so a save writes crypt parameters (VaultRepository.java:119-121)':
        'baseline: the setup vault is password-protected (Q3), so it has credentials and isEncryptionEnabled is true (VaultRepository.java:352-354)',
    'An AegisActivity is open and registered as a lock listener (AegisActivity.java:77)':
        'baseline: every AegisActivity registers itself as a lock listener in onCreate, so any open app screen satisfies it (AegisActivity.java:76-77)',
}
_W2_ORIG_EDIT = EDIT


def EDIT(x):
    _W2_ORIG_EDIT(x)
    _t = x.get('needs_state')
    if _t in _W2_CLEARED:
        x['needs_state'] = None
        x['state_kinds'] = []
        x['note'] = ((x.get('note') + ' | ') if x.get('note') else '') + _W2_CLEARED[_t]


# ---- W3 REAUDIT (Kiro): the unlock screen from the normal launcher start ----
# Under the re-audit baseline the setup vault exists and is password-protected
# (MUSE_REAUDIT_QUESTIONS.md Q3, Q6), so a normal start from the launcher
# reads the encrypted vault file, leaves it unloaded and starts the unlock
# screen (MainActivity.java:950-977). The pair is in the onStart sup() block
# (line 396) and its hand edge was removed in the earlier vault round, when
# the encrypted vault counted as cross-run state; it is baseline now, so the
# edge comes back without a state gate. Without it the unlock routes started
# from the screen-off broadcast (S_PROCESS -> VaultLockReceiver.onReceive,
# system_event), an outside entry where an in-app start exists (W3).
e('MainActivity.onStart', 'MainActivity.startAuthActivity', 'CALL',
  'the encrypted setup vault is not loaded yet: the unlock screen is started',
  guard='the vault exists (isVaultInitNeeded() false, MainActivity.java:942-947), the file reads without error (954-960), it is encrypted, so loadFrom is skipped (963-973), and isVaultLoaded() is false (976)',
  note='baseline: the setup vault is password-protected (Q3), so a launcher start opens the unlock screen (W3)',
  evidence='SRC ui/MainActivity.java:942-977')
