STATUS: RUNNING 21:55

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| GeneralDialogCreation.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods, never instantiated | SRC GeneralDialogCreation.java:120 |
| GeneralDialogCreation.deleteFilesDialog | REACHABLE | | Called from ItemPopupMenu delete action and MainFragment selection mode | SRC ItemPopupMenu.java:123-126, MainFragment.java:660-661, GeneralDialogCreation.java:183-355 |
| GeneralDialogCreation.lambda$deleteFilesDialog$0 | REACHABLE | | Positive button callback in deleteFilesDialog | SRC GeneralDialogCreation.java:193-197 |
| GeneralDialogCreation.lambda$null$39 | REACHABLE | | Nested lambda in setPermissionsDialog for permission change result | SRC GeneralDialogCreation.java:1167-1175 |
| GeneralDialogCreation.lambda$setPermissionsDialog$40 | REACHABLE | | Set button click in setPermissionsDialog | SRC GeneralDialogCreation.java:1163-1177 |
| GeneralDialogCreation.lambda$showArchiveDialog$26 | REACHABLE | | Positive button extracts archive | SRC GeneralDialogCreation.java:938 |
| GeneralDialogCreation.lambda$showArchiveDialog$27 | REACHABLE | | Negative button views archive contents | SRC GeneralDialogCreation.java:939 |
| GeneralDialogCreation.lambda$showChangePathsDialog$41 | REACHABLE | | Input validation callback in showChangePathsDialog | SRC GeneralDialogCreation.java:1188-1191 |
| GeneralDialogCreation.lambda$showChangePathsDialog$42 | REACHABLE | | Positive button navigates to entered path | SRC GeneralDialogCreation.java:1203-1205 |
| GeneralDialogCreation.lambda$showCloudDialog$8 | REACHABLE | | Positive button deletes cloud connection | SRC GeneralDialogCreation.java:629 |
| GeneralDialogCreation.lambda$showCloudDialog$9 | REACHABLE | | Negative button cancels dialog | SRC GeneralDialogCreation.java:631 |
| GeneralDialogCreation.lambda$showCompressDialog$28 | REACHABLE | | Positive button creates zip archive | SRC GeneralDialogCreation.java:965-967 |
| GeneralDialogCreation.lambda$showCompressDialog$29 | REACHABLE | | Input validator for compress filename | SRC GeneralDialogCreation.java:972-987 |
| GeneralDialogCreation.lambda$showCompressDialog$30 | REACHABLE | | Cursor positioning in filename field | SRC GeneralDialogCreation.java:993 |
| GeneralDialogCreation.lambda$showDecryptDialog$21 | REACHABLE | | Password validation and decryption callback | SRC GeneralDialogCreation.java:849-855 |
| GeneralDialogCreation.lambda$showDecryptFingerprintDialog$20 | REACHABLE | | Cancel button in fingerprint dialog | SRC GeneralDialogCreation.java:832 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$14 | REACHABLE | | Shows soft keyboard for password input | SRC GeneralDialogCreation.java:749-752 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$15 | REACHABLE | | Negative button cancels authentication | SRC GeneralDialogCreation.java:759 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$16 | REACHABLE | | Positive button starts encryption | SRC GeneralDialogCreation.java:760-772 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$17 | REACHABLE | | Text watcher enables OK button | SRC GeneralDialogCreation.java:784-788 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$18 | REACHABLE | | Password validator checks not empty | SRC GeneralDialogCreation.java:793-797 |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$19 | REACHABLE | | Confirm password validator checks match | SRC GeneralDialogCreation.java:800-804 |
| GeneralDialogCreation.lambda$showEncryptWarningDialog$10 | REACHABLE | | Positive button confirms encryption | SRC GeneralDialogCreation.java:653-666 |
| GeneralDialogCreation.lambda$showEncryptWarningDialog$11 | REACHABLE | | Negative button saves preference and encrypts | SRC GeneralDialogCreation.java:668-677 |
| GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$12 | REACHABLE | | Positive button starts encryption with preset password | SRC GeneralDialogCreation.java:695-706 |
| GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$13 | REACHABLE | | Input validator checks filename format | SRC GeneralDialogCreation.java:707-710 |
| GeneralDialogCreation.lambda$showHistoryDialog$38 | REACHABLE | | Negative button clears history | SRC GeneralDialogCreation.java:1095 |
| GeneralDialogCreation.lambda$showPackageDialog$24 | REACHABLE | | Positive button installs APK | SRC GeneralDialogCreation.java:916 |
| GeneralDialogCreation.lambda$showPackageDialog$25 | REACHABLE | | Negative button opens APK as archive | SRC GeneralDialogCreation.java:917 |
| GeneralDialogCreation.lambda$showPasswordDialog$22 | REACHABLE | | Negative button default cancel callback | SRC GeneralDialogCreation.java:886 |
| GeneralDialogCreation.lambda$showPasswordDialog$23 | REACHABLE | | Input validator checks password not empty | SRC GeneralDialogCreation.java:891-895 |
| GeneralDialogCreation.lambda$showPropertiesDialog$1 | REACHABLE | | Name field long-press copies to clipboard | SRC GeneralDialogCreation.java:433-437 |
| GeneralDialogCreation.lambda$showPropertiesDialog$2 | REACHABLE | | Location field long-press copies to clipboard | SRC GeneralDialogCreation.java:438-442 |
| GeneralDialogCreation.lambda$showPropertiesDialog$3 | REACHABLE | | Size field long-press copies to clipboard | SRC GeneralDialogCreation.java:443-447 |
| GeneralDialogCreation.lambda$showPropertiesDialog$4 | REACHABLE | | Date field long-press copies to clipboard | SRC GeneralDialogCreation.java:448-452 |
| GeneralDialogCreation.lambda$showPropertiesDialog$5 | REACHABLE | | Permissions button toggles table visibility | SRC GeneralDialogCreation.java:529-542 |
| GeneralDialogCreation.lambda$showPropertiesDialog$6 | REACHABLE | | Dialog dismiss shuts down executor | SRC GeneralDialogCreation.java:567 |
| GeneralDialogCreation.lambda$showPropertiesDialog$7 | REACHABLE | | Positive button manages .nomedia file | SRC GeneralDialogCreation.java:568-582 |
| GeneralDialogCreation.lambda$showSortDialog$31 | REACHABLE | | Folder-specific sort checkbox callback | SRC GeneralDialogCreation.java:1019-1026 |
| GeneralDialogCreation.lambda$showSortDialog$32 | REACHABLE | | Negative button selects ascending sort | SRC GeneralDialogCreation.java:1028-1030 |
| GeneralDialogCreation.lambda$showSortDialog$33 | REACHABLE | | Positive button selects descending sort | SRC GeneralDialogCreation.java:1031-1033 |
| GeneralDialogCreation.lambda$showSortDialog$34 | REACHABLE | | Negative button ascending app sort | SRC GeneralDialogCreation.java:1070-1075 |
| GeneralDialogCreation.lambda$showSortDialog$35 | REACHABLE | | Positive button descending app sort | SRC GeneralDialogCreation.java:1077-1082 |
| GeneralDialogCreation.lambda$showSortDialog$36 | REACHABLE | | Item selection callback in sort dialog | SRC GeneralDialogCreation.java:1011 |
| GeneralDialogCreation.lambda$showSortDialog$37 | REACHABLE | | Item selection callback in sort dialog | SRC GeneralDialogCreation.java:1066 |
| GeneralDialogCreation.onSortTypeSelected | REACHABLE | | Called from showSortDialog when user selects sort direction | SRC GeneralDialogCreation.java:1027-1030, GeneralDialogCreation.java:1036-1054 |
| GeneralDialogCreation.setPermissionsDialog | REACHABLE | | Called from showPropertiesDialog when permissions button clicked | SRC GeneralDialogCreation.java:536-541, GeneralDialogCreation.java:1129-1181 |
| GeneralDialogCreation.showArchiveDialog | REACHABLE | | Called from FileUtils.openFile for archive files | SRC FileUtils.java:755, GeneralDialogCreation.java:924-945 |
| GeneralDialogCreation.showBasicDialog | REACHABLE | | Called from MainActivity menu, PermissionsActivity, and showOtgSafExplanationDialog | SRC MainActivity.java:952, PermissionsActivity.java:54,65, GeneralDialogCreation.java:123-138 |
| GeneralDialogCreation.showChangePathsDialog | REACHABLE | | Called from BottomBar path button click | SRC BottomBar.java:153, GeneralDialogCreation.java:1183-1212 |
| GeneralDialogCreation.showCloudDialog | REACHABLE | | Called from Drawer for cloud connection removal | SRC Drawer.java:628-634, GeneralDialogCreation.java:605-637 |
| GeneralDialogCreation.showCompressDialog | REACHABLE | | Called from MainFragment compress action | SRC MainFragment.java:738, GeneralDialogCreation.java:947-997 |
| GeneralDialogCreation.showDecryptDialog | REACHABLE | | Called from EncryptDecryptUtils for password decryption | SRC EncryptDecryptUtils.java:120-122, GeneralDialogCreation.java:839-856 |
| GeneralDialogCreation.showDecryptFingerprintDialog | REACHABLE | | Called from EncryptDecryptUtils for fingerprint decryption on M+ | SRC EncryptDecryptUtils.java:109-111, GeneralDialogCreation.java:809-837 |
| GeneralDialogCreation.showEncryptAuthenticateDialog | REACHABLE | | Called from ItemPopupMenu encrypt action | SRC ItemPopupMenu.java:168-170, GeneralDialogCreation.java:714-807 |
| GeneralDialogCreation.showEncryptWarningDialog | REACHABLE | | Called from ItemPopupMenu encrypt menu | SRC ItemPopupMenu.java:192-194, GeneralDialogCreation.java:639-679 |
| GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog | REACHABLE | | Called from ItemPopupMenu for preset password encryption | SRC ItemPopupMenu.java:160-166, GeneralDialogCreation.java:681-712 |
| GeneralDialogCreation.showHiddenDialog | REACHABLE | | Called from MainActivity hidden files menu | SRC MainActivity.java:994, GeneralDialogCreation.java:1106-1127 |
| GeneralDialogCreation.showHistoryDialog | REACHABLE | | Called from MainActivity history menu | SRC MainActivity.java:943, GeneralDialogCreation.java:1085-1104 |
| GeneralDialogCreation.showNameDialog | REACHABLE | | Called from MainFragment.rename, MainActivityHelper.mk, and showEncryptWithPresetPasswordSaveAsDialog | SRC MainFragment.java:1210, MainActivityHelper.java:196, GeneralDialogCreation.java:686-710, GeneralDialogCreation.java:140-181 |
| GeneralDialogCreation.showOtgSafExplanationDialog | REACHABLE | | Called from Drawer OTG item click | SRC Drawer.java:583, GeneralDialogCreation.java:1214-1216 |
| GeneralDialogCreation.showPackageDialog | REACHABLE | | Called from FileUtils.openFile for APK files | SRC FileUtils.java:753, GeneralDialogCreation.java:906-922 |
| GeneralDialogCreation.showPasswordDialog | REACHABLE | | Called from showDecryptDialog, SevenZipHelperTask, and ExtractService | SRC GeneralDialogCreation.java:847-855, SevenZipHelperTask.java:104-106, ExtractService.java:331-333, GeneralDialogCreation.java:858-896 |
| GeneralDialogCreation.showPropertiesDialog | REACHABLE | | Called from three wrapper methods (WithPermissions, WithoutPermissions, ForStorage) | SRC GeneralDialogCreation.java:360,364,368, GeneralDialogCreation.java:371-585 |
| GeneralDialogCreation.showPropertiesDialogForStorage | REACHABLE | | Called from Drawer for storage properties | SRC Drawer.java:612-613, GeneralDialogCreation.java:367-369 |
| GeneralDialogCreation.showPropertiesDialogWithPermissions | REACHABLE | | Called from ItemPopupMenu and MainFragment properties actions | SRC ItemPopupMenu.java:68-69, MainFragment.java:654-656, GeneralDialogCreation.java:358-361 |
| GeneralDialogCreation.showPropertiesDialogWithoutPermissions | REACHABLE | | Called from TextEditorActivity info menu | SRC TextEditorActivity.java:369-370, GeneralDialogCreation.java:363-365 |
| GeneralDialogCreation.showSMBHelpDialog | REACHABLE | | Called from SmbConnectDialog help button | SRC SmbConnectDialog.java:164, GeneralDialogCreation.java:898-904 |
| GeneralDialogCreation.showSortDialog | REACHABLE | | Called from MainActivity for both MainFragment and AppsListFragment (overloaded) | SRC MainActivity.java:967,972, GeneralDialogCreation.java:999-1034,1056-1083 |
| GeneralDialogCreation.showSortDialog | REACHABLE | | Overloaded variant for AppsListFragment | SRC MainActivity.java:967, GeneralDialogCreation.java:1056-1083 |

STATUS: DONE 21:59
