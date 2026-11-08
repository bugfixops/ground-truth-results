# ---- Helper batch_032 label part (2025-01-18)

# GeneralDialogCreation methods - static dialog factory class

# showBasicDialog called from MainActivity.onOptionsItemSelected and PermissionsActivity
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'sethome menu item shows dialog to confirm setting path as home',
  evidence='SRC MainActivity.java:952, GeneralDialogCreation.java:123-138')

e('PermissionsActivity.requestStoragePermission', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'shows permission request dialog',
  evidence='SRC PermissionsActivity.java:54, GeneralDialogCreation.java:123-138')

e('PermissionsActivity.requestInstallApkPermission', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'shows install APK permission request dialog',
  evidence='SRC PermissionsActivity.java:65, GeneralDialogCreation.java:123-138')

e('GeneralDialogCreation.showOtgSafExplanationDialog', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'delegates to showBasicDialog for OTG SAF explanation',
  evidence='SRC GeneralDialogCreation.java:1214-1216')

# deleteFilesDialog called from ItemPopupMenu and MainFragment
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'delete menu item shows delete confirmation dialog',
  evidence='SRC ItemPopupMenu.java:123-126, GeneralDialogCreation.java:183-355')

e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'delete action in selection mode shows delete dialog',
  evidence='SRC MainFragment.java:660-661, GeneralDialogCreation.java:183-355')

# showNameDialog called from MainFragment and MainActivityHelper
e('MainFragment.rename', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows dialog to rename file',
  evidence='SRC MainFragment.java:1210-1220, GeneralDialogCreation.java:140-181')

e('MainActivityHelper.mk', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows dialog to create new file/folder with name',
  evidence='SRC MainActivityHelper.java:196-202, GeneralDialogCreation.java:140-181')

e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows save-as dialog for encrypted file',
  evidence='SRC GeneralDialogCreation.java:686-710')

# showPropertiesDialog variants
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showPropertiesDialogWithPermissions', 'CALL', 'properties menu item shows properties dialog with permissions',
  evidence='SRC ItemPopupMenu.java:68-69, GeneralDialogCreation.java:358-361')

e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.showPropertiesDialogWithPermissions', 'CALL', 'properties action shows dialog with permissions',
  evidence='SRC MainFragment.java:654-656, GeneralDialogCreation.java:358-361')

e('GeneralDialogCreation.showPropertiesDialogWithPermissions', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with showPermissions=true',
  evidence='SRC GeneralDialogCreation.java:360, GeneralDialogCreation.java:371-585')

e('TextEditorActivity.lambda$initStatusBarResources$2', 'GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CALL', 'info menu shows properties without permissions',
  evidence='SRC TextEditorActivity.java:369-370, GeneralDialogCreation.java:363-365')

e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with showPermissions=false',
  evidence='SRC GeneralDialogCreation.java:364, GeneralDialogCreation.java:371-585')

e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showPropertiesDialogForStorage', 'CALL', 'shows storage properties dialog for drive',
  evidence='SRC Drawer.java:612-613, GeneralDialogCreation.java:367-369')

e('GeneralDialogCreation.showPropertiesDialogForStorage', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with forStorage=true',
  evidence='SRC GeneralDialogCreation.java:368, GeneralDialogCreation.java:371-585')

# showPropertiesDialog internal call to setPermissionsDialog
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.setPermissionsDialog', 'CALL', 'sets up permissions UI when showPermissions is true and user is root',
  evidence='SRC GeneralDialogCreation.java:536-541, GeneralDialogCreation.java:1129-1181')

# Cloud dialog
e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showCloudDialog', 'CALL', 'long-press on cloud connection shows remove dialog',
  evidence='SRC Drawer.java:628-634, GeneralDialogCreation.java:605-637')

# Encryption dialogs
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptWarningDialog', 'CALL', 'encrypt menu shows warning dialog',
  evidence='SRC ItemPopupMenu.java:192-194, GeneralDialogCreation.java:639-679')

e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'CALL', 'encrypt with preset password shows save-as dialog',
  evidence='SRC ItemPopupMenu.java:160-166, GeneralDialogCreation.java:681-712')

e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptAuthenticateDialog', 'CALL', 'encrypt menu shows authentication dialog',
  evidence='SRC ItemPopupMenu.java:168-170, GeneralDialogCreation.java:714-807')

# Decryption dialogs
e('EncryptDecryptUtils.decryptFile', 'GeneralDialogCreation.showDecryptFingerprintDialog', 'CALL', 'shows fingerprint authentication dialog for decryption on M+',
  evidence='SRC EncryptDecryptUtils.java:109-111, GeneralDialogCreation.java:809-837')

e('EncryptDecryptUtils.decryptFile', 'GeneralDialogCreation.showDecryptDialog', 'CALL', 'shows password dialog for decryption',
  evidence='SRC EncryptDecryptUtils.java:120-122, GeneralDialogCreation.java:839-856')

e('GeneralDialogCreation.showDecryptDialog', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'delegates to password dialog with decrypt callback',
  evidence='SRC GeneralDialogCreation.java:847-855, GeneralDialogCreation.java:858-896')

# Password dialog for archives
e('SevenZipHelperTask.onPostExecute', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'shows password dialog when 7z archive requires password',
  evidence='SRC SevenZipHelperTask.java:104-106, GeneralDialogCreation.java:858-896')

e('ExtractService.lambda$extract$0', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'shows password dialog when extraction requires password',
  evidence='SRC ExtractService.java:331-333, GeneralDialogCreation.java:858-896')

# SMB help dialog
e('SmbConnectDialog.lambda$new$2', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'shows SMB connection help dialog',
  evidence='SRC SmbConnectDialog.java:164, GeneralDialogCreation.java:898-904')

# Package and archive dialogs
e('FileUtils.openFile', 'GeneralDialogCreation.showPackageDialog', 'CALL', 'shows package installer dialog for APK files',
  evidence='SRC FileUtils.java:753, GeneralDialogCreation.java:906-922')

e('FileUtils.openFile', 'GeneralDialogCreation.showArchiveDialog', 'CALL', 'shows archive options dialog for compressed files',
  evidence='SRC FileUtils.java:755, GeneralDialogCreation.java:924-945')

# Compress dialog
e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.showCompressDialog', 'CALL', 'compress action shows compress dialog',
  evidence='SRC MainFragment.java:738, GeneralDialogCreation.java:947-997')

# Sort dialogs (overloaded)
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showSortDialog', 'CALL', 'sort menu for apps list shows sort dialog',
  evidence='SRC MainActivity.java:967, GeneralDialogCreation.java:1056-1083')

e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showSortDialog', 'CALL', 'sort menu for main fragment shows sort dialog',
  evidence='SRC MainActivity.java:972, GeneralDialogCreation.java:999-1034')

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.onSortTypeSelected', 'CALL', 'user selects sort direction, processes the selection',
  evidence='SRC GeneralDialogCreation.java:1027-1030, GeneralDialogCreation.java:1036-1054')

# History and hidden dialogs
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showHistoryDialog', 'CALL', 'history menu shows history dialog',
  evidence='SRC MainActivity.java:943, GeneralDialogCreation.java:1085-1104')

e('MainActivity.onNavigationItemSelected', 'GeneralDialogCreation.showHiddenDialog', 'CALL', 'hidden files menu shows hidden files dialog',
  evidence='SRC MainActivity.java:994, GeneralDialogCreation.java:1106-1127')

# Change paths dialog
e('BottomBar.lambda$initProperties$0', 'GeneralDialogCreation.showChangePathsDialog', 'CALL', 'path button click shows path change dialog',
  evidence='SRC BottomBar.java:153, GeneralDialogCreation.java:1183-1212')

# OTG SAF explanation dialog
e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showOtgSafExplanationDialog', 'CALL', 'OTG item click shows SAF explanation dialog',
  evidence='SRC Drawer.java:583, GeneralDialogCreation.java:1214-1216')

# Lambda methods - these are synthetic methods generated by the compiler from lambda expressions
# Each lambda is called from its parent method via invokedynamic

# deleteFilesDialog lambda
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation.lambda$deleteFilesDialog$0', 'ASYNC', 'positive button callback deletes files',
  evidence='SRC GeneralDialogCreation.java:193-197')

# showPropertiesDialog lambdas (long-press listeners)
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$1', 'GUI', 'name field long-press copies name to clipboard',
  evidence='SRC GeneralDialogCreation.java:433-437')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$2', 'GUI', 'location field long-press copies location to clipboard',
  evidence='SRC GeneralDialogCreation.java:438-442')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$3', 'GUI', 'size field long-press copies size to clipboard',
  evidence='SRC GeneralDialogCreation.java:443-447')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$4', 'GUI', 'date field long-press copies date to clipboard',
  evidence='SRC GeneralDialogCreation.java:448-452')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$5', 'GUI', 'permissions button click toggles permissions table visibility',
  evidence='SRC GeneralDialogCreation.java:529-542')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$6', 'LIFECYCLE', 'dialog dismiss listener shuts down executor',
  evidence='SRC GeneralDialogCreation.java:567')

e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$7', 'GUI', 'positive button creates/deletes .nomedia file',
  evidence='SRC GeneralDialogCreation.java:568-582')

# showCloudDialog lambdas
e('GeneralDialogCreation.showCloudDialog', 'GeneralDialogCreation.lambda$showCloudDialog$8', 'GUI', 'positive button deletes cloud connection',
  evidence='SRC GeneralDialogCreation.java:629')

e('GeneralDialogCreation.showCloudDialog', 'GeneralDialogCreation.lambda$showCloudDialog$9', 'GUI', 'negative button cancels dialog',
  evidence='SRC GeneralDialogCreation.java:631')

# showEncryptWarningDialog lambdas
e('GeneralDialogCreation.showEncryptWarningDialog', 'GeneralDialogCreation.lambda$showEncryptWarningDialog$10', 'GUI', 'positive button confirms encryption',
  evidence='SRC GeneralDialogCreation.java:653-666')

e('GeneralDialogCreation.showEncryptWarningDialog', 'GeneralDialogCreation.lambda$showEncryptWarningDialog$11', 'GUI', 'negative button saves preference and encrypts',
  evidence='SRC GeneralDialogCreation.java:668-677')

# showEncryptWithPresetPasswordSaveAsDialog lambdas
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$12', 'GUI', 'positive button starts encryption with preset password',
  evidence='SRC GeneralDialogCreation.java:695-706')

e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$13', 'GUI', 'input validator checks filename format',
  evidence='SRC GeneralDialogCreation.java:707-710')

# showEncryptAuthenticateDialog lambdas
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$14', 'GUI', 'shows soft keyboard for password input',
  evidence='SRC GeneralDialogCreation.java:749-752')

e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$15', 'GUI', 'negative button cancels dialog',
  evidence='SRC GeneralDialogCreation.java:759')

e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$16', 'GUI', 'positive button starts encryption with entered password',
  evidence='SRC GeneralDialogCreation.java:760-772')

e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$17', 'GUI', 'text watcher enables OK button when all fields filled',
  evidence='SRC GeneralDialogCreation.java:784-788')

e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$18', 'GUI', 'password validator checks field is not empty',
  evidence='SRC GeneralDialogCreation.java:793-797')

e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$19', 'GUI', 'confirm password validator checks passwords match',
  evidence='SRC GeneralDialogCreation.java:800-804')

# showDecryptFingerprintDialog lambda
e('GeneralDialogCreation.showDecryptFingerprintDialog', 'GeneralDialogCreation.lambda$showDecryptFingerprintDialog$20', 'GUI', 'cancel button dismisses fingerprint dialog',
  evidence='SRC GeneralDialogCreation.java:832')

# showDecryptDialog lambda
e('GeneralDialogCreation.showDecryptDialog', 'GeneralDialogCreation.lambda$showDecryptDialog$21', 'GUI', 'password entry validates and decrypts file',
  evidence='SRC GeneralDialogCreation.java:849-855')

# showPasswordDialog lambdas
e('GeneralDialogCreation.showPasswordDialog', 'GeneralDialogCreation.lambda$showPasswordDialog$22', 'GUI', 'negative button cancels password dialog if no custom callback',
  evidence='SRC GeneralDialogCreation.java:886')

e('GeneralDialogCreation.showPasswordDialog', 'GeneralDialogCreation.lambda$showPasswordDialog$23', 'GUI', 'input validator checks password field is not empty',
  evidence='SRC GeneralDialogCreation.java:891-895')

# showPackageDialog lambdas
e('GeneralDialogCreation.showPackageDialog', 'GeneralDialogCreation.lambda$showPackageDialog$24', 'GUI', 'positive button installs APK',
  evidence='SRC GeneralDialogCreation.java:916')

e('GeneralDialogCreation.showPackageDialog', 'GeneralDialogCreation.lambda$showPackageDialog$25', 'GUI', 'negative button opens APK as archive',
  evidence='SRC GeneralDialogCreation.java:917')

# showArchiveDialog lambdas
e('GeneralDialogCreation.showArchiveDialog', 'GeneralDialogCreation.lambda$showArchiveDialog$26', 'GUI', 'positive button extracts archive',
  evidence='SRC GeneralDialogCreation.java:938')

e('GeneralDialogCreation.showArchiveDialog', 'GeneralDialogCreation.lambda$showArchiveDialog$27', 'GUI', 'negative button views archive contents',
  evidence='SRC GeneralDialogCreation.java:939')

# showCompressDialog lambdas
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'GUI', 'positive button creates zip archive',
  evidence='SRC GeneralDialogCreation.java:965-967')

e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'GUI', 'input validator checks filename validity and suggests .zip extension',
  evidence='SRC GeneralDialogCreation.java:972-987')

e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'GUI', 'sets cursor to start of filename field',
  evidence='SRC GeneralDialogCreation.java:993')

# showSortDialog (MainFragment) lambdas
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$31', 'GUI', 'folder-specific sort checkbox state changed',
  evidence='SRC GeneralDialogCreation.java:1019-1026')

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$32', 'GUI', 'negative button selects ascending sort',
  evidence='SRC GeneralDialogCreation.java:1028-1030')

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$33', 'GUI', 'positive button selects descending sort',
  evidence='SRC GeneralDialogCreation.java:1031-1033')

# showSortDialog (AppsListFragment) lambdas
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$34', 'GUI', 'negative button selects ascending app sort',
  evidence='SRC GeneralDialogCreation.java:1070-1075')

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$35', 'GUI', 'positive button selects descending app sort',
  evidence='SRC GeneralDialogCreation.java:1077-1082')

# Note: lambda$showSortDialog$36 and $37 appear to be additional variants from overloaded showSortDialog
# These are synthetic and called through the same mechanism

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$36', 'GUI', 'item selection callback in sort dialog',
  evidence='SRC GeneralDialogCreation.java:1011 or 1066 (overloaded method)')

e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$37', 'GUI', 'item selection callback in sort dialog',
  evidence='SRC GeneralDialogCreation.java:1011 or 1066 (overloaded method)')

# showHistoryDialog lambda
e('GeneralDialogCreation.showHistoryDialog', 'GeneralDialogCreation.lambda$showHistoryDialog$38', 'GUI', 'negative button clears history',
  evidence='SRC GeneralDialogCreation.java:1095')

# lambda$null$39 is a nested lambda within setPermissionsDialog
e('GeneralDialogCreation.setPermissionsDialog', 'GeneralDialogCreation.lambda$null$39', 'ASYNC', 'permission change result callback',
  evidence='SRC GeneralDialogCreation.java:1167-1175')

# setPermissionsDialog lambda
e('GeneralDialogCreation.setPermissionsDialog', 'GeneralDialogCreation.lambda$setPermissionsDialog$40', 'GUI', 'set button applies permission changes',
  evidence='SRC GeneralDialogCreation.java:1163-1177')

# showChangePathsDialog lambdas
e('GeneralDialogCreation.showChangePathsDialog', 'GeneralDialogCreation.lambda$showChangePathsDialog$41', 'GUI', 'input callback validates path accessibility',
  evidence='SRC GeneralDialogCreation.java:1188-1191')

e('GeneralDialogCreation.showChangePathsDialog', 'GeneralDialogCreation.lambda$showChangePathsDialog$42', 'GUI', 'positive button navigates to entered path',
  evidence='SRC GeneralDialogCreation.java:1203-1205')

# UNREACHABLE methods
UNREACHABLE['GeneralDialogCreation.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods, no instances created; grep shows no "new GeneralDialogCreation()" calls',
    'SRC GeneralDialogCreation.java:120 class definition shows all static methods; grep -rn "new GeneralDialogCreation" shows only inner class SizeFormatter',
    'SOURCE'
)

