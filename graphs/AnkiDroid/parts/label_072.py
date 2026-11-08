# AnkiDroid batch 072 (LABEL helper). CompatHelper static methods, CompatV10 base bodies and its anonymous classes,
# CompatV11, CompatV15 ($1 listener), CompatV16 and CompatV17: 36 methods. The full row list is in
# graphs/AnkiDroid/parts/label_072.md.
#
# Route ownership: the three e() calls are the TTS listener edges from CompatV15.setTtsOnUtteranceProgressListener
# (CompatV15.java:13-30). The other CALL edges come from auto_calls.json and are not written here.
# Gates: ENV_TTS and STATE_SETTINGS (the TTS preference, as in label_053). No MISSING GATE is needed.
# UNREACHABLE: isNook (no caller) and 18 closed members on the standard API 27 path (12 CompatV10 base bodies that a
# CompatV11..CompatV21 class overrides, and 6 members of their anonymous classes).

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onDone', 'FRAMEWORK',
  'the TTS engine reports that an utterance finished and the listener speaks the next queued text',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-22; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body runs only when ReadText.sTextQueue is not empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onError', 'FRAMEWORK',
  'the TTS engine reports an error for an utterance',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-25; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onStart', 'FRAMEWORK',
  'the TTS engine reports that an utterance started',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-28; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

UNREACHABLE['CompatHelper.isNook'] = ('no_trigger_in_app',
  'No caller in the app source. The constructor uses the private isNookHdOrHdPlus (CompatHelper.java:33), not this method. A grep over src/main/java finds no other reference.',
  'com/ichi2/compat/CompatHelper.java:33, 101-103', 'SOURCE')

UNREACHABLE['CompatV10.detagged'] = ('closed_by_api_level',
  'CompatV16 overrides it (Html.escapeHtml). The base body runs only on API 10 to 15, not on the standard API 27 path.',
  'com/ichi2/compat/CompatV10.java:49-55; com/ichi2/compat/CompatV16.java:34-37; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.flushWebViewCookies'] = ('closed_by_api_level',
  'CompatV21 overrides it (CookieManager.flush). The base body (CookieSyncManager.sync) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:88-90; com/ichi2/compat/CompatV21.java:31-34; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.getPreferenceSubscreenIntent'] = ('closed_by_api_level',
  'CompatV11 overrides it. The base body (legacy headers, action only) does not run on API 11 and up, including API 27.',
  'com/ichi2/compat/CompatV10.java:183-188; com/ichi2/compat/CompatV11.java:40-49; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.isImmersiveSystemUiVisible'] = ('closed_by_api_level',
  'CompatV19 overrides it (SYSTEM_UI_FLAG_HIDE_NAVIGATION check). The base body (always false) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:196-198; com/ichi2/compat/CompatV19.java:90-93', 'SOURCE')

UNREACHABLE['CompatV10.openUrl'] = ('closed_by_api_level',
  'CompatV16 overrides it (Custom Tabs). The base body (CustomTabsFallback.openUri) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:132-134; com/ichi2/compat/CompatV16.java:76-87; com/ichi2/anki/AnkiActivity.java:322-323', 'SOURCE')

UNREACHABLE['CompatV10.restartActivityInvalidateBackstack'] = ('closed_by_api_level',
  'CompatV11 overrides it (TaskStackBuilder restart). The base body runs only on API 10, below the CompatV11 threshold.',
  'com/ichi2/compat/CompatV10.java:105-111; com/ichi2/compat/CompatV11.java:24-32; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.setFullScreen'] = ('closed_by_api_level',
  'CompatV19 overrides it (sticky immersive flags, no super call). The base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:113-120; com/ichi2/compat/CompatV19.java:25-26', 'SOURCE')

UNREACHABLE['CompatV10.setHTML5MediaAutoPlay'] = ('closed_by_api_level',
  'CompatV17 overrides it (setMediaPlaybackRequiresUserGesture). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:93-95; com/ichi2/compat/CompatV17.java:13-16', 'SOURCE')

UNREACHABLE['CompatV10.setSelectableBackground'] = ('closed_by_api_level',
  'CompatV21 overrides it (ripple effect). The base body (colorBackground) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:123-130; com/ichi2/compat/CompatV21.java:14-21', 'SOURCE')

UNREACHABLE['CompatV10.setStatusBarColor'] = ('closed_by_api_level',
  'CompatV21 overrides it (window.setStatusBarColor). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:191-193; com/ichi2/compat/CompatV21.java:36-39', 'SOURCE')

UNREACHABLE['CompatV10.setTtsOnUtteranceProgressListener'] = ('closed_by_api_level',
  'CompatV15 overrides it (UtteranceProgressListener). The API 27 route into the TTS init callback reaches CompatV15 (ReadText.java:195). The base body (deprecated OnUtteranceCompletedListener) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67; com/ichi2/compat/CompatV15.java:13-30; com/ichi2/anki/ReadText.java:195', 'SOURCE')

UNREACHABLE['CompatV10.supportAddContentMenu'] = ('closed_by_api_level',
  'Called only from the DeckPicker fallback, which runs only when the add_content_menu view is absent. That id is in the layout-v14 resource only, so API 27 does not take the fallback.',
  'com/ichi2/compat/CompatV10.java:141-180; com/ichi2/anki/DeckPicker.java:391-404; res/layout-v14/floating_add_button.xml:7; res/layout/floating_add_button.xml:1-14', 'SOURCE')

UNREACHABLE['CompatV10$1.<init>'] = ('closed_by_api_level',
  'Created only inside CompatV10.setTtsOnUtteranceProgressListener, which CompatV15 overrides on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67', 'SOURCE')

UNREACHABLE['CompatV10$1.onUtteranceCompleted'] = ('closed_by_api_level',
  'Body of the deprecated listener above. Never registered on API 27.',
  'com/ichi2/compat/CompatV10.java:58-66', 'SOURCE')

UNREACHABLE['CompatV10$2.<init>'] = ('closed_by_api_level',
  'Created only inside supportAddContentMenu, which is closed on API 27.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2.onSelection'] = ('closed_by_api_level',
  'Runs only from the dialog opened by supportAddContentMenu. Closed with it.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2$1.<init>'] = ('closed_by_api_level',
  'Created by the case 2 branch of onSelection. Closed with supportAddContentMenu.',
  'com/ichi2/compat/CompatV10.java:161-175', 'SOURCE')

UNREACHABLE['CompatV10$2$1.onClick'] = ('closed_by_api_level',
  'onPositive callback of the new-deck dialog. Reachable only through supportAddContentMenu, closed on API 27.',
  'com/ichi2/compat/CompatV10.java:165-173', 'SOURCE')
