# ---- Helper batch_026 label part (2025-01-18)
# FileUtil, FileUtil$1, FileUtil$MediaFile - 37 methods

# Edges for REACHABLE methods

# FileUtil.checkFolder is public static, called from CopyService, DecryptService, EncryptService
e('CopyService.run', 'FileUtil.checkFolder', 'CALL', 'check target path writable',
  evidence='SRC CopyService.java:350')
e('DecryptService.doInBackground', 'FileUtil.checkFolder', 'CALL', 'check output folder writable',
  evidence='SRC DecryptService.java:142')
e('EncryptService.doInBackground', 'FileUtil.checkFolder', 'CALL', 'check output folder writable',
  evidence='SRC EncryptService.java:186')

# FileUtil.copyFile is private static, called from FileUtil.renameFolder
e('FileUtil.renameFolder', 'FileUtil.copyFile', 'CALL', 'fallback to copy when rename fails',
  evidence='SRC FileUtil.java:455')

# FileUtil.deleteFile is package-private static, called from HybridFile.delete
e('HybridFile.delete', 'FileUtil.deleteFile', 'CALL', 'delete file in FILE mode',
  evidence='SRC HybridFile.java:1236')

# FileUtil.getDocumentFile is public static, called from GenericCopyUtil, FileUtils
e('GenericCopyUtil.copyFiles', 'FileUtil.getDocumentFile', 'CALL', 'get SAF document for source',
  evidence='SRC GenericCopyUtil.java:168')
e('GenericCopyUtil.copyFiles', 'FileUtil.getDocumentFile', 'CALL', 'get SAF document for target',
  evidence='SRC GenericCopyUtil.java:266')
e('FileUtils.scanFile', 'FileUtil.getDocumentFile', 'CALL', 'get document file for SAF delete',
  evidence='SRC FileUtils.java:268')

# FileUtil.getExtSdCardFolder is private static, called from FileUtil.isOnExtSdCard and getDocumentFile
e('FileUtil.isOnExtSdCard', 'FileUtil.getExtSdCardFolder', 'CALL', 'check if file on ext sd',
  evidence='SRC FileUtil.java:814')
e('FileUtil.getDocumentFile', 'FileUtil.getExtSdCardFolder', 'CALL', 'get base folder for SAF',
  evidence='SRC FileUtil.java:830')

# FileUtil.getExtSdCardPaths is private static, called from FileUtil.getExtSdCardFolder
e('FileUtil.getExtSdCardFolder', 'FileUtil.getExtSdCardPaths', 'CALL', 'get all ext sd paths',
  evidence='SRC FileUtil.java:793')

# FileUtil.getExtSdCardPathsForActivity is public static, called from MainActivity
e('MainActivity.onActivityResult', 'FileUtil.getExtSdCardPathsForActivity', 'CALL', 'get ext sd paths for storage picker',
  evidence='SRC MainActivity.java:681')

# FileUtil.getOutputStream is public static, called from WriteFileAbstraction, ZipService, HybridFile, extractors
e('WriteFileAbstraction.doInBackground', 'FileUtil.getOutputStream', 'CALL', 'get output stream for SAF',
  evidence='SRC WriteFileAbstraction.java:79')
e('ZipService.compress', 'FileUtil.getOutputStream', 'CALL', 'get output stream for zip file',
  evidence='SRC ZipService.java:255')
e('HybridFile.getOutputStream', 'FileUtil.getOutputStream', 'CALL', 'get output stream in FILE mode',
  evidence='SRC HybridFile.java:1065')

# FileUtil.isOnExtSdCard is public static, called from MainActivityHelper, Operations, FileUtil itself
e('MainActivityHelper.mkDir', 'FileUtil.isOnExtSdCard', 'CALL', 'check if folder on ext sd',
  evidence='SRC MainActivityHelper.java:340')
e('Operations.mkDir', 'FileUtil.isOnExtSdCard', 'CALL', 'check if folder on ext sd',
  evidence='SRC Operations.java:495')
e('FileUtil.deleteFile', 'FileUtil.isOnExtSdCard', 'CALL', 'check if file on ext sd for SAF delete',
  evidence='SRC FileUtil.java:381')

# FileUtil.isReadable is public static, called from GenericCopyUtil
e('GenericCopyUtil.copyFiles', 'FileUtil.isReadable', 'CALL', 'check source file readable',
  evidence='SRC GenericCopyUtil.java:152')

# FileUtil.isValidFilename is public static, called from GeneralDialogCreation, MainFragment, MainActivityHelper
e('GeneralDialogCreation.mkDir', 'FileUtil.isValidFilename', 'CALL', 'validate new folder name',
  evidence='SRC GeneralDialogCreation.java:973')
e('MainFragment.onMenuItemClick', 'FileUtil.isValidFilename', 'CALL', 'validate new file name',
  evidence='SRC MainFragment.java:1228')
e('MainActivityHelper.mkDir', 'FileUtil.isValidFilename', 'CALL', 'validate folder name',
  evidence='SRC MainActivityHelper.java:142')

# FileUtil.isWritable is public static, called from MainActivityHelper, GenericCopyUtil, Operations, FileUtil
e('MainActivityHelper.mkDir', 'FileUtil.isWritable', 'CALL', 'check folder writable',
  evidence='SRC MainActivityHelper.java:352')
e('GenericCopyUtil.copyFiles', 'FileUtil.isWritable', 'CALL', 'check target file writable',
  evidence='SRC GenericCopyUtil.java:255')
e('Operations.mkDir', 'FileUtil.isWritable', 'CALL', 'check folder writable',
  evidence='SRC Operations.java:515')

# FileUtil.isWritableNormalOrSaf is public static, called from MainActivityHelper, Operations, FileUtil itself
e('MainActivityHelper.mkDir', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check folder writable with SAF',
  evidence='SRC MainActivityHelper.java:346')
e('Operations.mkDir', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check folder writable with SAF',
  evidence='SRC Operations.java:503')
e('FileUtil.writeUriToStorage', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check target folder writable',
  evidence='SRC FileUtil.java:235')

# FileUtil.mkdir is public static, called from Operations, HybridFile, extractors, FileUtil
e('Operations.mkDir', 'FileUtil.mkdir', 'CALL', 'create directory',
  evidence='SRC Operations.java:169')
e('HybridFile.mkdir', 'FileUtil.mkdir', 'CALL', 'create directory in FILE mode',
  evidence='SRC HybridFile.java:1209')
e('FileUtil.renameFolder', 'FileUtil.mkdir', 'CALL', 'create target folder for manual rename',
  evidence='SRC FileUtil.java:443')

# FileUtil.mkdirs is public static, called from CryptUtil
e('CryptUtil.encryptFile', 'FileUtil.mkdirs', 'CALL', 'create output directory',
  evidence='SRC CryptUtil.java:169')
e('CryptUtil.decryptFile', 'FileUtil.mkdirs', 'CALL', 'create output directory',
  evidence='SRC CryptUtil.java:221')

# FileUtil.mkfile is public static, called from Operations
e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',
  evidence='SRC Operations.java:307')

# FileUtil.rename is private static, called from FileUtil.renameFolder
e('FileUtil.renameFolder', 'FileUtil.rename', 'CALL', 'try normal rename first',
  evidence='SRC FileUtil.java:425')

# FileUtil.renameFolder is package-private static, called from Operations
e('Operations.rename', 'FileUtil.renameFolder', 'CALL', 'rename folder',
  evidence='SRC Operations.java:444')

# FileUtil.rmdir is private static, called from FileUtil.deleteFile
e('FileUtil.deleteFile', 'FileUtil.rmdir', 'CALL', 'recursively delete directory',
  evidence='SRC FileUtil.java:376')

# FileUtil.writeUriToStorage is public static final, called from MainActivity
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save ACTION_OPEN_DOCUMENT content',
  evidence='SRC MainActivity.java:567')
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save ACTION_GET_CONTENT content',
  evidence='SRC MainActivity.java:576')
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save saved instance uris',
  evidence='SRC MainActivity.java:1389')

# FileUtil$1 is the anonymous inner class created in writeUriToStorage
e('FileUtil.writeUriToStorage', 'FileUtil$1.<init>', 'CALL', 'create async callback for uri write',
  evidence='SRC FileUtil.java:196')

# FileUtil$1.doInBackground and onPostExecute are invoked by AppConfig.runInParallel
e('AppConfig.runInParallel', 'FileUtil$1.doInBackground', 'ASYNC', 'async task execution',
  evidence='SRC FileUtil.java:198-363')
e('AppConfig.runInParallel', 'FileUtil$1.onPostExecute', 'ASYNC', 'async task completion',
  evidence='SRC FileUtil.java:364-372')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B026 = {
    'FileUtil.<clinit>': ('framework_never_calls', 'static initializer for Pattern field, runs on class load when FileUtil first referenced', 'SRC FileUtil.java:80-82', 'SOURCE'),
    'FileUtil.<init>': ('no_trigger_in_app', 'constructor of abstract class FileUtil, cannot be instantiated', 'SRC FileUtil.java:78 shows abstract class', 'SOURCE'),
    'FileUtil.copyDummyFile': ('no_trigger_in_app', 'private static method only called from copyDummyFiles which itself is never called; grep shows only internal calls at line 973-974', 'SRC FileUtil.java:888-926', 'SOURCE'),
    'FileUtil.copyDummyFiles': ('no_trigger_in_app', 'private static method, grep in app source shows only definition at FileUtil.java:971, no callers', 'SRC FileUtil.java:971-979', 'SOURCE'),
    'FileUtil.getTempFile': ('no_trigger_in_app', 'public static method, grep in app source shows only definition at FileUtil.java:476, no callers', 'SRC FileUtil.java:476-479', 'SOURCE'),
    'FileUtil$MediaFile.<clinit>': ('framework_never_calls', 'static initializer for MediaFile constants, runs on MediaFile class load', 'SRC FileUtil.java:983-985', 'SOURCE'),
    'FileUtil$MediaFile.<init>': ('no_trigger_in_app', 'constructor only called from MediaFile.mkdir() at line 1198, but mkdir() itself is never called; grep shows no MediaFile instantiation outside FileUtil', 'SRC FileUtil.java:1016-1022, call at 1198', 'SOURCE'),
    'FileUtil$MediaFile.delete': ('no_trigger_in_app', 'only called from MediaFile.mkdir() at line 1199, but mkdir() is never called', 'SRC FileUtil.java:1028-1059, call at 1199', 'SOURCE'),
    'FileUtil$MediaFile.getExternalFilesDir': ('no_trigger_in_app', 'private static, only called from installTemporaryTrack at line 1134, but that chain starts from mkdir() which is never called', 'SRC FileUtil.java:987-1010, call at 1134', 'SOURCE'),
    'FileUtil$MediaFile.getFile': ('no_trigger_in_app', 'public method, never called; MediaFile only instantiated at line 1198 within unreachable mkdir()', 'SRC FileUtil.java:1205-1207', 'SOURCE'),
    'FileUtil$MediaFile.getTemporaryAlbumId': ('no_trigger_in_app', 'private, only called from MediaFile.mkdir at line 1190, but mkdir is never called', 'SRC FileUtil.java:1062-1126, call at 1190', 'SOURCE'),
    'FileUtil$MediaFile.installTemporaryTrack': ('no_trigger_in_app', 'private, only called from getTemporaryAlbumId at line 1091, but that chain starts from mkdir() which is never called', 'SRC FileUtil.java:1129-1170, call at 1091', 'SOURCE'),
    'FileUtil$MediaFile.mkdir': ('no_trigger_in_app', 'public method but grep shows no callers in app; Kitkat workaround code that is unused', 'SRC FileUtil.java:1172-1202', 'SOURCE'),
    'FileUtil$MediaFile.write': ('no_trigger_in_app', 'public method but grep shows no callers in app; MediaFile is never instantiated outside its own mkdir()', 'SRC FileUtil.java:1207-1231', 'SOURCE'),
}
