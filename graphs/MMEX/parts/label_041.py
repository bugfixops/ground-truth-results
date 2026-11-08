# batch 041 (label_041): core/bundlers PriceDownloadedEventBundler (3 methods), core/database DatabaseManager (8), core/docstorage DocFileMetadata (1), FileStorageHelper (21) and its inner classes FileStorageHelper$1, $2, $3 (4): 37 methods, 33 REACHABLE, 4 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_041.md; grep output: graphs/MMEX/parts/label_041.grep.txt.
# CALL edges come from auto_calls.json (none written here, D7). The one edge written here is FRAMEWORK: Handler.postDelayed runs FileStorageHelper$3.run, and no auto record reaches run.
# The sup cut is for an auto CALL record whose caller is UNREACHABLE in this batch (D14a): deleteRemoteFile to getContext. The edge from EditPriceDialog$$Icepick.<clinit> (batch 085) to PriceDownloadedEventBundler.<init> is cut in batch 085 (D14a).
# get and put have no incoming edge at all. The Icepick helper that would call them is never loaded, because EditPriceDialog is never constructed (grep sections 5, 6, 9 of label_041.grep.txt), so no edge is written into them.

# ================================================================== FRAMEWORK edge (batch 041)

e('FileStorageHelper.pollNewRemoteTimestamp', 'FileStorageHelper$3.run', 'FRAMEWORK',
  'pollNewRemoteTimestamp queues the runnable on a main-looper Handler with a 2 s delay; the framework runs run() when the delay ends (run then polls again through the same handler while the remote timestamp is unchanged)',
  evidence='SRC core/docstorage/FileStorageHelper.java:402-431 (Handler 407, Runnable 408, run 410-428, self-repeat postDelayed 419, first postDelayed(runnable, milliseconds) at 431); FW-SRC core/java/android/os/Handler.java:427-429 (postDelayed calls sendMessageDelayed), 596 (sendMessageDelayed)')

# ================================================================== sup cuts (batch 041)

sup(('FileStorageHelper.deleteRemoteFile', 'FileStorageHelper.getContext'))

# ================================================================== UNREACHABLE (batch 041)

UNREACHABLE['PriceDownloadedEventBundler.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the Icepick bundler for the @State field mPrice of EditPriceDialog (EditPriceDialog.java:83). Its only caller is the generated static initialiser EditPriceDialog$$Icepick.<clinit> (auto CALL record, EditPriceDialog$$Icepick.java:16). That initialiser runs only when Icepick loads the helper for a saved or restored EditPriceDialog (EditPriceDialog.java:105, 174). EditPriceDialog has no creation site: its constructor (EditPriceDialog.java:89) has no caller record, the only other mention of new EditPriceDialog is commented out (WatchlistItemsFragment.java:255), and no app source or resource names it (grep sections 5, 6, 9). The dialog never exists, so the helper never loads.',
  'SRC investment/EditPriceDialog.java:83, 89, 103-105, 171-174; SRC investment/watchlist/WatchlistItemsFragment.java:255; SRC core/bundlers/PriceDownloadedEventBundler.java:33; label_041.grep.txt sections 3, 5, 6, 9',
  'INFERRED')

UNREACHABLE['PriceDownloadedEventBundler.get'] = ('no_trigger_in_app',
  'Read method of the Icepick bundler for mPrice (PriceDownloadedEventBundler.java:41-44). The caller is the Icepick library helper (Helper.getWithBundler, library not in the dataset) reached from the generated restore method EditPriceDialog$$Icepick.restore. Restore runs only from Icepick.restoreInstanceState in EditPriceDialog.onCreateDialog (EditPriceDialog.java:104-105), and that dialog is never constructed (see PriceDownloadedEventBundler.<init>). No auto CALL record reaches get (grep section 9).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:41-44; SRC investment/EditPriceDialog.java:103-105; label_041.grep.txt sections 3, 4, 5, 9',
  'INFERRED')

UNREACHABLE['PriceDownloadedEventBundler.put'] = ('no_trigger_in_app',
  'Write method of the Icepick bundler for mPrice (PriceDownloadedEventBundler.java:36-38). The caller is the Icepick library helper (Helper.putWithBundler, library not in the dataset) reached from the generated save method EditPriceDialog$$Icepick.save. Save runs only from Icepick.saveInstanceState in EditPriceDialog.onSaveInstanceState (EditPriceDialog.java:171-174), and that dialog is never constructed (see PriceDownloadedEventBundler.<init>). No auto CALL record reaches put (grep section 9).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:36-38; SRC investment/EditPriceDialog.java:171-174; label_041.grep.txt sections 3, 4, 5, 9',
  'INFERRED')

UNREACHABLE['FileStorageHelper.deleteRemoteFile'] = ('no_trigger_in_app',
  'Private method with no caller. Its only occurrence in the app source is the definition at FileStorageHelper.java:325 (grep section 1). The javadoc at 320-324 says it was meant for a temp file upload, and no call site exists. No auto CALL record has it as dst (grep section 9). The inner classes FileStorageHelper$1 to $3 do not contain the name (grep section 2), so no accessor calls it. Its one outgoing call, to getContext at line 326, is cut above with sup.',
  'SRC core/docstorage/FileStorageHelper.java:320-333; label_041.grep.txt sections 1, 2, 9',
  'SOURCE')
