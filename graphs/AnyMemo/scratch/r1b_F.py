import sys
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from r1b_tool import apply, add_gate_entries

# F3: new state text, right after NEED_PREF_SAVED
apply([
    ("NEED_PREF_SAVED = state_text('A value was saved for this preference before (its key exists in SharedPreferences; not on a fresh install)', ('settings',))\n",
     "NEED_PREF_SAVED = state_text('A value was saved for this preference before (its key exists in SharedPreferences; not on a fresh install)', ('settings',))\n"
     "NEED_FULLSCREEN = state_text('The Fullscreen mode box in Settings was ticked and saved before (SharedPreferences fullscreen_mode = true; option_screen.xml:66-69), so the flag is on when this activity is created', ('settings',))\n"),
    # F3: GATE entry gets the state
    ("    ('BaseActivity.onCreate', 'BaseActivity.enableImmersiveMode'): {'guard': 'the fullscreen mode preference is on (common/BaseActivity.java:36-37)'},",
     "    ('BaseActivity.onCreate', 'BaseActivity.enableImmersiveMode'): {'guard': 'the fullscreen mode preference is on (common/BaseActivity.java:36-37)', 'needs_state': NEED_FULLSCREEN},"),
    # F2: SettingsScreen loader edges start at onCreate (SettingsScreen.java:137-139)
    ("e('SettingsScreen.<init>', 'SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader in onCreate'",
     "e('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader in onCreate'"),
    ("e('SettingsScreen.<init>', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset', 'FRAMEWORK',",
     "e('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset', 'FRAMEWORK',"),
    ("    ('SettingsScreen.<init>', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset'): {",
     "    ('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset'): {"),
], 'F2 F3')

# F1, F4, F5: new GATE keys (none existed; checked by grep before this script)
add_gate_entries([
    "    # Round 1b F1: the three auto CALLs leave createNotificationChannels inside the API 26 block (NotificationChannelUtil.java:36-49)",
    "    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createConversationNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},",
    "    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createCardPlayerNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},",
    "    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createReviewReminderNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},",
    "    # Round 1b F4: the cached field is read first (BaseActivity.java:78)",
    "    ('BaseActivity.activityComponents', 'AMApplication.activityComponents'): {'guard': 'the cached field activityComponents is still null, i.e. the first call in this activity (BaseActivity.java:78)'},",
    "    # Round 1b F5: the null check before destroy (AnyMemo.java:408)",
    "    ('AnyMemo.onDestroy', 'MultipleLoaderManager.destroy'): {'guard': 'multipleLoaderManager != null (AnyMemo.java:408)'},",
], 'F1 F4 F5')
