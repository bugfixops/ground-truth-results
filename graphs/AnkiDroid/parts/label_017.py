# AnkiDroid batch 017 (LABEL helper). CardContentProvider (32 methods, with onCreate) and SdCardReceiver (<init> and onReceive).
# The 34 route rows (REACHABLE or UNREACHABLE, with route, kind, reason and source) are in graphs/AnkiDroid/parts/label_017.md.
#
# Route ownership: every CardContentProvider method in batch_017 is in this part, so the CALL edges between them come from
# auto_calls.json and are not written here. CardContentProvider.onCreate and SdCardReceiver.onReceive are not in
# batch_017.txt; the coordinator added their rows to this part (34 method rows). Their S_ENTRY edges are in graph_def.py:145
# and graph_def.py:149-150 and are not written here; the LIFECYCLE edge <init> -> onCreate is in graph_def.py:293.
# The broadcast edge SdCardReceiver.onReceive -> DeckPicker$18.onReceive was not in graph_def.py, so it is written below.
#
# Page edges from S_ENTRY are written here, because their destination method is in this part:
#   S_ENTRY -> CardContentProvider.<clinit>          process start (no env)
#   S_ENTRY -> query, insert, update, delete, bulkInsert, getType   another app calls ContentResolver (ENV_PROVIDER_CALL)
#   S_ENTRY -> SdCardReceiver.<init>                 MEDIA_MOUNTED or MEDIA_EJECT broadcast (ENV_SDCARD_EVENT)
#
# Gates: numbers only, in the note text (no constants added). Meanings used in the rows:
#   MG112 the caller holds com.ichi2.anki.permission.READ_WRITE_DATABASE (hasReadWritePermission true). Without it, on
#         API 27, the security check throws SecurityException (query 209-210, update 417-418, delete 674-675,
#         bulkInsert 711-712, insert 813-814). getType has no check (159-195).
#   MG113 the URI type case of the switch that the route names (query 222-, update 429-, delete 683-, insert 825-).
#   MG114 bulkInsert: match == NOTES (718) and the deckId query parameter parses as a long (719-727).
#   MG115 update SCHEDULE: cardOrd and noteID were set from the values (633-634) and getCard returns a card (635-636).
#   MG116 query SCHEDULE: the selection has deckID=... and selectDeckWithCheck returns true (326-334).
#   MG117 update DECK_SELECTED: the values have a DECK_ID key (651-657).
#   MG118 SDK_INT below 23 (CompatHelper.isMarshmallow false). Only path to knownRogueClient; not on API 27.
#   MG119 CollectionHelper.getCol returns a collection (else IllegalStateException at 214-215 for query; 420, 677, 816, 740 for the others).
#   MG120 SDK_INT >= 19 (KITKAT) in getCallingPackageSafe (1327-1329). The other branch (1330-1334) needs SDK_INT below 19.
#   MG121 query DECKS_ID: a due-tree node has the requested deck id (384-389).
#
# Judgement calls (also in label_017.md):
#   - No STATE gate on the entry edges. CollectionHelper.getCol (CollectionHelper.java:85-) opens or creates the collection,
#     so collection.anki2 need not exist before the call; a failed directory setup returns null (MG119).
#   - ENV_PROVIDER_CALL is used for getType too. Its permission text does not apply to getType, which has no check.
#   - knownRogueClient is closed_by_api_level (its only callers are behind an SDK check that holds on API 27), not
#     branch_never_taken. On API 22 and lower (minSdkVersion 10 in build.gradle:12) it is reachable.
#   - The binder hop from another process to ContentProvider.Transport is INFERRED: ContentProviderNative is not in fw_src.
#   - The ASYNC broadcast edge to DeckPicker$18.onReceive has no env and no gate number; its registration condition is in the note.

# --- Page entry edges (destination methods are in this batch).

e('S_ENTRY', 'CardContentProvider.<clinit>', 'ENTRY',
  'process start: the framework installs the manifest provider in the app process and loads its class',
  env=None,
  evidence='SRC com/ichi2/anki/provider/CardContentProvider.java:109-112, 139, 142; FW-SRC core/java/android/app/ActivityThread.java:5722, 6227-6228; SRC AndroidManifest.xml:324-330; INFERRED the process start that reaches installContentProviders (FW-SRC core/java/android/app/ActivityThread.java:5722) is not read in full',
  note='The static blocks (112, 142) and the FlashCardsContract.Note.<clinit> call (139) run here. Same process-start entry as CardContentProvider.onCreate in graph_def.py:145. No permission gate on the process start.')

e('CardContentProvider.<clinit>', 'CardContentProvider.<init>', 'FRAMEWORK',
  'the framework creates the provider instance after the class is initialized (Class.newInstance)',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:6227-6228; INFERRED Class.newInstance runs class initialization before the constructor (JVM behaviour, not in fw_src)',
  note='CardContentProvider has no explicit constructor (class at CardContentProvider.java:89), so <init> is the default constructor. The LIFECYCLE edge <init> -> onCreate is in graph_def.py:293.')

e('S_ENTRY', 'CardContentProvider.query', 'ENTRY',
  'another app calls ContentResolver.query on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:209-240, 581, 605; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:208; INFERRED the cross-process hop into Transport.query (ContentProviderNative.onTransact) is not in fw_src',
  note='No readPermission is declared in the manifest, so the framework allows the call (ContentProvider.java:581, 605). Both branches of Transport.query call ContentProvider.this.query (lines 228 and 240). The body needs MG112 (query 209-210).')

e('S_ENTRY', 'CardContentProvider.insert', 'ENTRY',
  'another app calls ContentResolver.insert on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:256-265, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:812; INFERRED the cross-process hop into Transport.insert is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (insert 813-814). bulkInsert reaches insert too, through super.bulkInsert (CardContentProvider.java:730).')

e('S_ENTRY', 'CardContentProvider.update', 'ENTRY',
  'another app calls ContentResolver.update on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:348-357, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:416; INFERRED the cross-process hop into Transport.update is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (update 417-418).')

e('S_ENTRY', 'CardContentProvider.delete', 'ENTRY',
  'another app calls ContentResolver.delete on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:333-341, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:673; INFERRED the cross-process hop into Transport.delete is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (delete 674-675).')

e('S_ENTRY', 'CardContentProvider.bulkInsert', 'ENTRY',
  'another app calls ContentResolver.bulkInsert on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:272-280, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:710; INFERRED the cross-process hop into Transport.bulkInsert is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (bulkInsert 711-712).')

e('S_ENTRY', 'CardContentProvider.getType', 'ENTRY',
  'another app calls ContentResolver.getType on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:249-252; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:159; INFERRED the cross-process hop into Transport.getType is not in fw_src',
  note='Transport.getType calls ContentProvider.this.getType directly (line 252), with no permission check. getType (159-195) has no permission check either, so MG112 does not apply here.')

e('S_ENTRY', 'SdCardReceiver.<init>', 'ENTRY',
  'system broadcast MEDIA_MOUNTED or MEDIA_EJECT for a file volume: the framework instantiates the manifest receiver',
  env=ENV_SDCARD_EVENT,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3141-3166; SRC AndroidManifest.xml:268-282; SRC com/ichi2/anki/receiver/SdCardReceiver.java:35; INFERRED the system delivers the broadcast to the manifest receiver (not in fw_src)',
  note='SdCardReceiver has no explicit constructor (class at SdCardReceiver.java:35), so <init> is the default constructor. The framework creates a new receiver for each broadcast (handleReceiver, newInstance at ActivityThread.java:3166). onReceive is entered by its own edge (graph_def.py:149), not through <init>.')

# --- Broadcast edge out of SdCardReceiver.onReceive (source method is in this batch, so this part writes it).

e('SdCardReceiver.onReceive', 'DeckPicker$18.onReceive', 'ASYNC',
  'the receiver re-broadcasts MEDIA_EJECT (line 47) or MEDIA_MOUNT (line 56); the runtime receiver DeckPicker$18.onReceive handles it (MEDIA_EJECT: onSdCardNotMounted; MEDIA_MOUNT: restartActivity)',
  env=None,
  evidence='SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47, 52-56; SRC com/ichi2/anki/DeckPicker.java:369, 751, 1674-1680; FW-SRC core/java/android/app/ContextImpl.java:965; FW-SRC core/java/android/content/BroadcastReceiver.java:327; INFERRED the ActivityManager delivers the broadcast to the runtime-registered receiver (not in fw_src)',
  note='DeckPicker$18 is batch_004, and no edge in graph_def.py names it yet. The receiver exists only while DeckPicker is alive: DeckPicker.onCreate registers it (369) and onDestroy unregisters it (751). That registration condition is not written as a gate: a gate needs a new MG number, and this batch adds none. Also absent from graph_def.py and owned by batch_004: the registration edge DeckPicker.registerExternalStorageListener -> DeckPicker$18.<init>.')

# --- UNREACHABLE entry (the one method in this batch with no route).

UNREACHABLE['CardContentProvider.knownRogueClient'] = (
    'closed_by_api_level',
    "knownRogueClient is called from shouldEnforceQueryOrInsertSecurity (CardContentProvider.java:199) and shouldEnforceUpdateSecurity (204), and only when CompatHelper.isMarshmallow() returns false (it is the first operand of ||). isMarshmallow is getSdkVersion() >= M, and getSdkVersion returns Build.VERSION.SDK_INT. On API 27 the first operand is true, so knownRogueClient is never evaluated. It runs only on devices below API 23 (MG118), which is not the API 27 target in handoff/SCHEMA_V2.md. On those older devices (minSdkVersion 10 in build.gradle:12) the method is reachable, so the label is for the API 27 target and the method is not dead code.",
    'SRC com/ichi2/anki/provider/CardContentProvider.java:199, 204; SRC com/ichi2/compat/CompatHelper.java:55-57, 69-71',
    'SOURCE')
