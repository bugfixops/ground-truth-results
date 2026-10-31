# Repair batch 01: SevenZOutputFile methods (all UNREACHABLE)
# All methods belong to SevenZOutputFile, a library class for writing 7z archives.
# The app only reads 7z archives using SevenZFile, never writes them.
# Grep proof: grep -rn "SevenZOutputFile" app/src/main/java shows no matches.

UNREACHABLE['SevenZOutputFile.<init>(File)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile (see SevenZipHelperTask.java:68-70, SevenZipExtractor.java:31). Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:68-72',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.<init>(SeekableByteChannel)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile. Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:86-89',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.close'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app. Grep shows no references to SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:126-133',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.closeArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:173-199',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.createArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:143-152',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.finish'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:237-277',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getContentMethods'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:329-332',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getCurrentOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:283-288',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.putArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:163-167',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.reverse'] = (
    'no_trigger_in_app',
    'Private static method of SevenZOutputFile. The class is never instantiated in the app, and this static method is only called from instance methods of SevenZOutputFile.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:628-634',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentCompression'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:100-107',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentMethods'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:119-122',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setupFileOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:290-327',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:205-208',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[])'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:214-217',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[],int,int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:225-229',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeBits'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileATimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:522-553',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileAntiItems'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:465-485',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileCTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:491-529',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyFiles'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:446-463',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyStreams'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:424-444',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileMTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:555-586',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileNames'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:487-502',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileWindowsAttributes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:588-612',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFilesInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:410-422',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFolder'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:387-399',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeHeader'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:334-342',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writePackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:355-375',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSingleCodec'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:401-418',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:344-353',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSubStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:420-431',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUint64'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUnpackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:377-408',
    'INFERRED'
)
