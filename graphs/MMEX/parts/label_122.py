# ================================================================== batch 122 (label_122): SyncPreferencesActivity (3), CloudItemViewHolder (2), CloudItemViewHolder$1 (2), CloudStorageProviderEnum (2), SyncBroadcastReceiver (2), SyncCommon (2), SyncConstants (1)
# Result: 5 REACHABLE, 9 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_122.md). Grep evidence: graphs/MMEX/parts/label_122.grep.txt.
# Routes: the Settings list (SettingsFragment$8) starts SyncPreferencesActivity; its BROWSABLE manifest filter is an outside entry.
# SyncBroadcastReceiver is created by the alarm that SyncSchedulerBroadcastReceiver.startHeartbeat sets.
# CloudItemViewHolder, CloudStorageProviderEnum and SyncCommon have no caller in the source root (grep A1-A3).
# This file writes: SCREENS S_SYNC_SETTINGS (none existed; D9); INTENT and ENTRY into SyncPreferencesActivity.<init>; ENTRY into onNewIntent.
# It also writes LIFECYCLE and ENTERS edges, a FRAMEWORK edge into SyncBroadcastReceiver.<init> (dst owned here), and LIFECYCLE into onReceive.
# 3 sup cuts remove auto CALL records whose caller is UNREACHABLE in this batch (D14). 9 UNREACHABLE entries.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_SYNC_SETTINGS': 'Synchronization settings screen (SyncPreferencesActivity), which hosts SyncPreferenceFragment',
})

# ---- Start sites into this batch's activity (dst owned here, D1)

e('SettingsFragment$8.onPreferenceClick', 'SyncPreferencesActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), SyncPreferencesActivity.class)) from the Synchronisation preference',
  gui=['Open Settings and tap the Synchronisation preference'],
  evidence='SRC settings/SettingsFragment.java:153-158 (anonymous class $8 is created at line 153: auto_calls SettingsFragment.onCreate -> SettingsFragment$8.<init>, line 153)')

e('S_ENTRY', 'SyncPreferencesActivity.<init>', 'ENTRY',
  'The manifest declares the activity with a BROWSABLE VIEW filter for scheme com.money.manager.ex, so an outside link starts it when no instance is running; the framework creates it by class name (INFERRED)',
  evidence='SRC AndroidManifest.xml:268-279 (activity android:name=".settings.SyncPreferencesActivity", singleTask, exported, intent-filter VIEW/DEFAULT/BROWSABLE, data scheme com.money.manager.ex)')

# ---- SyncPreferencesActivity lifecycle and page

e('SyncPreferencesActivity.<init>', 'SyncPreferencesActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/SyncPreferencesActivity.java:28-38; INFERRED framework lifecycle (not read)')

e('SyncPreferencesActivity.onCreate', 'S_SYNC_SETTINGS', 'ENTERS',
  'the Synchronization settings screen is shown: setSettingFragment(new SyncPreferenceFragment())',
  evidence='SRC settings/SyncPreferencesActivity.java:33-38 (setSettingFragment at line 37)')

e('S_ENTRY', 'SyncPreferencesActivity.onNewIntent', 'ENTRY',
  'When the activity is already running (singleTask), an outside BROWSABLE VIEW intent with scheme com.money.manager.ex (for example an authentication redirect) is delivered to it, and the framework calls onNewIntent directly (INFERRED delivery)',
  evidence='SRC settings/SyncPreferencesActivity.java:41-57 (Javadoc, onNewIntent, Timber at 52, super call at 56); SRC AndroidManifest.xml:268-279; grep A5 (BaseSettingsFragmentActivity does not declare onNewIntent, so super is the framework method)')

# ---- SyncBroadcastReceiver: created by the alarm, then onReceive

e('SyncSchedulerBroadcastReceiver.startHeartbeat', 'SyncBroadcastReceiver.<init>', 'FRAMEWORK',
  'startHeartbeat schedules an inexact repeating AlarmManager alarm whose PendingIntent is a broadcast to SyncBroadcastReceiver; when the alarm fires, the system creates the receiver to deliver the broadcast',
  needs_state=state_text('sync is enabled and the sync interval is above 0 (SyncSchedulerBroadcastReceiver.java:76, 82)', ('settings',)),
  via='AlarmManager repeat with a broadcast PendingIntent (AlarmManager delivery not read: INFERRED)',
  evidence='SRC sync/SyncSchedulerBroadcastReceiver.java:52-53 (PendingIntent to SyncBroadcastReceiver), 67 (startHeartbeat call), 76 (isSyncEnabled gate), 82 (interval gate), 90-94 (setInexactRepeating with pendingIntent); SRC AndroidManifest.xml:107 (receiver, no intent-filter); SRC home/MainActivity.java:242 (onCreate calls initializeSync), 1210-1218 (initializeSync calls sync.startSyncServiceHeartbeat when interval != 0), sync/SyncManager.java:268-273 (startSyncServiceHeartbeat sends the START broadcast); pattern label_096 (RecurringTransactionBootReceiver.setAlarm to RecurringTransactionReceiver.<init>); grep A6 and label_122.grep.txt section D')

e('SyncBroadcastReceiver.<init>', 'SyncBroadcastReceiver.onReceive', 'LIFECYCLE',
  'the framework calls onReceive on the receiver instance it has just created (INFERRED framework dispatch)',
  evidence='SRC sync/SyncBroadcastReceiver.java:31-45')

# ---- Auto CALL records whose caller is UNREACHABLE in this batch (D14): cut so no live edge leaves an UNREACHABLE method

sup(('CloudItemViewHolder.<init>', 'CloudItemViewHolder.initialize'))
sup(('CloudItemViewHolder.initialize', 'CloudItemViewHolder$1.<init>'))
sup(('CloudItemViewHolder$1.onClick', 'ListItemClickedEvent.<init>'))

# ---- UNREACHABLE (no caller in the source root; grep A1-A4 and auto_calls.json, see label_122.grep.txt)

UNREACHABLE['CloudItemViewHolder.<init>'] = ('no_trigger_in_app',
    'no caller: the class name occurs only in its own file (grep A1), and no auto_calls.json record has the constructor as dst; its outgoing record to initialize is cut above',
    'sync/CloudItemViewHolder.java:36-40; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder.initialize'] = ('no_trigger_in_app',
    'called only from the unreachable constructor (auto CALL, line 39); the click listener it registers is never set up; its outgoing record to $1.<init> is cut above',
    'sync/CloudItemViewHolder.java:47-57; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder$1.<init>'] = ('no_trigger_in_app',
    'created only by CloudItemViewHolder.initialize (auto CALL, line 49), which is unreachable',
    'sync/CloudItemViewHolder.java:49-54; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder$1.onClick'] = ('no_trigger_in_app',
    'view click listener set only by the unreachable initialize; no auto_calls.json record has it as dst; its CALL to ListItemClickedEvent.<init> is cut above (ListItemClickedEvent.<init> stays UNREACHABLE, label_033; its other caller is batch 050)',
    'sync/CloudItemViewHolder.java:50-53; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudStorageProviderEnum.<clinit>'] = ('no_trigger_in_app',
    'the enum name occurs only in its declaring file (grep A2), so no code path initialises the class; no auto_calls.json record has it as dst',
    'sync/CloudStorageProviderEnum.java:23-28; label_122.grep.txt A2, B',
    'SOURCE')

UNREACHABLE['CloudStorageProviderEnum.contains'] = ('no_trigger_in_app',
    'static helper with no caller: the enum name occurs only in its declaring file (grep A2), and no auto_calls.json calls record has contains as dst',
    'sync/CloudStorageProviderEnum.java:30-35; label_122.grep.txt A2, B',
    'SOURCE')

UNREACHABLE['SyncCommon.<init>'] = ('no_trigger_in_app',
    'no caller: the class name and getIntentForOpenDatabase occur only in SyncCommon.java (grep A3), so there is no subclass or instance; no auto_calls.json record has it as dst',
    'sync/SyncCommon.java:31; label_122.grep.txt A3, B',
    'SOURCE')

UNREACHABLE['SyncCommon.getIntentForOpenDatabase'] = ('no_trigger_in_app',
    'no caller in the source root (grep A3) and no auto_calls.json record has it as dst; its only app target MainActivity is reached only through this method, so no INTENT edge is written',
    'sync/SyncCommon.java:32-38; label_122.grep.txt A3, B',
    'SOURCE')

UNREACHABLE['SyncConstants.<init>'] = ('no_trigger_in_app',
    'no instance is created (grep A4 finds no new SyncConstants and no SyncConstants()); the class holds compile-time constants only; no auto_calls.json record has it as dst',
    'sync/SyncConstants.java:22; label_122.grep.txt A4, B',
    'SOURCE')
