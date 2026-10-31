# ================================================================== batch 124 (label_124): SyncNotificationFactory (8 methods); 8 methods
# Result: 3 REACHABLE, 5 UNREACHABLE (rows: graphs/MMEX/parts/label_124.md). Grep evidence: graphs/MMEX/parts/label_124.grep.txt.
# This file writes:
#   - 5 UNREACHABLE entries (kind no_trigger_in_app): the getters with no live caller,
#   - 8 sup cuts (D14) for the auto CALL records from those five UNREACHABLE getters to getContext and NotificationUtils.createNotificationChannel,
#   - 2 sup cuts (D20 pattern) for the auto CALL records from SyncService.showNotificationUploading and showNotificationUploadComplete into the two UNREACHABLE upload getters (the callers are in batch 126; the target owner cuts here).
# No edge is written. Every REACHABLE route is made of auto CALL records already in auto_calls.json (D7), so the build finds it (D4).
# Batch 126 (SyncService) must still: label SyncService.showNotificationUploading and SyncService.showNotificationUploadComplete UNREACHABLE (no caller in the source root),
#   and cut its own auto records into <init> from them (SyncService.java:252 and 168) (D14). Those two cuts are not written here (ownership, D1).

# ---- UNREACHABLE: the five getters with no live caller

UNREACHABLE['SyncNotificationFactory.getNotificationBuilderProgress'] = ('no_trigger_in_app',
    'no caller anywhere in the source root: the name occurs only at its declaration (grep A2); no auto_calls.json record has it as src or dst (grep B1); no class file other than SyncNotificationFactory.class names it (grep C1); it has no outgoing auto record',
    'sync/SyncNotificationFactory.java:145-150; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationDownloadComplete'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (grep A2); SyncService has no download-complete notification method and no auto record has it as dst (grep B1); its two outgoing records (getContext line 87, NotificationUtils.createNotificationChannel line 69) are cut below (D14)',
    'sync/SyncNotificationFactory.java:67-89; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationForDownload'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (grep A2); SyncService has no download notification method and no auto record has it as dst (grep B1); its two outgoing records (getContext line 59, NotificationUtils.createNotificationChannel line 50) are cut below (D14)',
    'sync/SyncNotificationFactory.java:48-62; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationUploading'] = ('no_trigger_in_app',
    'its only caller is SyncService.showNotificationUploading (SyncService.java:251, call at 253, private). That method has no caller in the source root (grep A2: the name occurs only at line 251), so the getter has no live route; its incoming record (SyncService.java:253) is cut below (D20 pattern); its outgoing records (getContext line 105, NotificationUtils.createNotificationChannel line 96) are cut below (D14)',
    'sync/SyncNotificationFactory.java:94-108; sync/SyncService.java:251-253; label_124.grep.txt A2, B2, B3, C2',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationUploadComplete'] = ('no_trigger_in_app',
    'its only caller is SyncService.showNotificationUploadComplete (SyncService.java:155, call at 168-169, private). That method has no caller in the source root (grep A2: the name occurs only at line 155), so the getter has no live route; its incoming record (SyncService.java:169) is cut below (D20 pattern); its outgoing records (getContext line 132, NotificationUtils.createNotificationChannel line 120) are cut below (D14)',
    'sync/SyncNotificationFactory.java:113-135; sync/SyncService.java:155-172; label_124.grep.txt A2, B2, B3, C2',
    'SOURCE')

# ---- D14: the outgoing auto CALL records of the five UNREACHABLE getters (caller unreachable in this batch)

sup(('SyncNotificationFactory.getNotificationForDownload', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 59
sup(('SyncNotificationFactory.getNotificationForDownload', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 50
sup(('SyncNotificationFactory.getNotificationDownloadComplete', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 87
sup(('SyncNotificationFactory.getNotificationDownloadComplete', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 69
sup(('SyncNotificationFactory.getNotificationUploading', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 105
sup(('SyncNotificationFactory.getNotificationUploading', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 96
sup(('SyncNotificationFactory.getNotificationUploadComplete', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 132
sup(('SyncNotificationFactory.getNotificationUploadComplete', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 120

# ---- D20 pattern: the incoming auto records of the two UNREACHABLE upload getters (their callers are batch 126's and have no caller themselves)

sup(('SyncService.showNotificationUploading', 'SyncNotificationFactory.getNotificationUploading'))  # SyncService.java:253; target UNREACHABLE, no caller of showNotificationUploading (grep A2)
sup(('SyncService.showNotificationUploadComplete', 'SyncNotificationFactory.getNotificationUploadComplete'))  # SyncService.java:169; target UNREACHABLE, no caller of showNotificationUploadComplete (grep A2)
