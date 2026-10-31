STATUS: RUNNING 22:58

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FileUtil.<clinit> | UNREACHABLE | framework_never_calls | static initializer for Pattern field, runs on class load when FileUtil first referenced | SRC FileUtil.java:80-82 |
| FileUtil.<init> | UNREACHABLE | no_trigger_in_app | constructor of abstract class FileUtil, cannot be instantiated | SRC FileUtil.java:78 shows abstract class |
| FileUtil.checkFolder | REACHABLE | | Called from CopyService, DecryptService, EncryptService | SRC CopyService.java:350, DecryptService.java:142, EncryptService.java:186 |
| FileUtil.copyDummyFile | UNREACHABLE | no_trigger_in_app | private static method only called from copyDummyFiles which itself is never called | SRC FileUtil.java:888-926, grep shows calls only from 973-974 |
| FileUtil.copyDummyFiles | UNREACHABLE | no_trigger_in_app | private static method, no callers in app | SRC FileUtil.java:971-979, grep shows no callers |
| FileUtil.copyFile | REACHABLE | | private static, called from FileUtil.renameFolder | SRC FileUtil.java:455 |
| FileUtil.deleteFile | REACHABLE | | package-private static, called from HybridFile.delete | SRC HybridFile.java:1236 |
| FileUtil.getDocumentFile | REACHABLE | | public static, called from GenericCopyUtil, FileUtils | SRC GenericCopyUtil.java:168,266, FileUtils.java:268 |
| FileUtil.getExtSdCardFolder | REACHABLE | | private static, called from FileUtil.isOnExtSdCard, getDocumentFile | SRC FileUtil.java:814,830 |
| FileUtil.getExtSdCardPaths | REACHABLE | | private static, called from FileUtil.getExtSdCardFolder | SRC FileUtil.java:793 |
| FileUtil.getExtSdCardPathsForActivity | REACHABLE | | public static, called from MainActivity | SRC MainActivity.java:681 |
| FileUtil.getOutputStream | REACHABLE | | public static, called from WriteFileAbstraction, ZipService, HybridFile, extractors | SRC WriteFileAbstraction.java:79, ZipService.java:255, HybridFile.java:1065 |
| FileUtil.getTempFile | UNREACHABLE | no_trigger_in_app | public static method, no callers in app | SRC FileUtil.java:476-479, grep shows no callers |
| FileUtil.isOnExtSdCard | REACHABLE | | public static, called from MainActivityHelper, Operations, FileUtil methods | SRC MainActivityHelper.java:340, Operations.java:495, FileUtil.java:381 |
| FileUtil.isReadable | REACHABLE | | public static, called from GenericCopyUtil | SRC GenericCopyUtil.java:152 |
| FileUtil.isValidFilename | REACHABLE | | public static, called from GeneralDialogCreation, MainFragment, MainActivityHelper | SRC GeneralDialogCreation.java:973, MainFragment.java:1228, MainActivityHelper.java:142 |
| FileUtil.isWritable | REACHABLE | | public static, called from MainActivityHelper, GenericCopyUtil, Operations, FileUtil | SRC MainActivityHelper.java:352, GenericCopyUtil.java:255, Operations.java:515 |
| FileUtil.isWritableNormalOrSaf | REACHABLE | | public static, called from MainActivityHelper, Operations, FileUtil | SRC MainActivityHelper.java:346, Operations.java:503, FileUtil.java:235 |
| FileUtil.mkdir | REACHABLE | | public static, called from Operations, HybridFile, extractors, FileUtil | SRC Operations.java:169, HybridFile.java:1209, FileUtil.java:443 |
| FileUtil.mkdirs | REACHABLE | | public static, called from CryptUtil | SRC CryptUtil.java:169,221 |
| FileUtil.mkfile | REACHABLE | | public static, called from Operations | SRC Operations.java:307 |
| FileUtil.rename | REACHABLE | | private static, called from FileUtil.renameFolder | SRC FileUtil.java:425 |
| FileUtil.renameFolder | REACHABLE | | package-private static, called from Operations | SRC Operations.java:444 |
| FileUtil.rmdir | REACHABLE | | private static, called from FileUtil.deleteFile | SRC FileUtil.java:376 |
| FileUtil.writeUriToStorage | REACHABLE | | public static final, called from MainActivity | SRC MainActivity.java:567,576,1389 |
| FileUtil$1.<init> | REACHABLE | | anonymous inner class constructor, created in writeUriToStorage | SRC FileUtil.java:196 |
| FileUtil$1.doInBackground | REACHABLE | | async task execution invoked by AppConfig.runInParallel | SRC FileUtil.java:198-363 |
| FileUtil$1.onPostExecute | REACHABLE | | async task completion invoked by AppConfig.runInParallel | SRC FileUtil.java:364-372 |
| FileUtil$MediaFile.<clinit> | UNREACHABLE | framework_never_calls | static initializer for MediaFile constants, runs on MediaFile class load | SRC FileUtil.java:983-985 |
| FileUtil$MediaFile.<init> | UNREACHABLE | no_trigger_in_app | constructor only called from MediaFile.mkdir() which itself is never called | SRC FileUtil.java:1016-1022, call at 1198 |
| FileUtil$MediaFile.delete | UNREACHABLE | no_trigger_in_app | only called from MediaFile.mkdir() at line 1199, but mkdir() is never called | SRC FileUtil.java:1028-1059, call at 1199 |
| FileUtil$MediaFile.getExternalFilesDir | UNREACHABLE | no_trigger_in_app | private static, only called from installTemporaryTrack, but chain starts from mkdir() which is never called | SRC FileUtil.java:987-1010, call at 1134 |
| FileUtil$MediaFile.getFile | UNREACHABLE | no_trigger_in_app | public method, never called; MediaFile only instantiated within unreachable mkdir() | SRC FileUtil.java:1205-1207 |
| FileUtil$MediaFile.getTemporaryAlbumId | UNREACHABLE | no_trigger_in_app | private, only called from MediaFile.mkdir which is never called | SRC FileUtil.java:1062-1126, call at 1190 |
| FileUtil$MediaFile.installTemporaryTrack | UNREACHABLE | no_trigger_in_app | private, only called from getTemporaryAlbumId, but chain starts from mkdir() which is never called | SRC FileUtil.java:1129-1170, call at 1091 |
| FileUtil$MediaFile.mkdir | UNREACHABLE | no_trigger_in_app | public method but grep shows no callers in app; Kitkat workaround code that is unused | SRC FileUtil.java:1172-1202 |
| FileUtil$MediaFile.write | UNREACHABLE | no_trigger_in_app | public method but grep shows no callers in app; MediaFile never instantiated outside its own mkdir() | SRC FileUtil.java:1207-1231 |

STATUS: DONE 23:01
