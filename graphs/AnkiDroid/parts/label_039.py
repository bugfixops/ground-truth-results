e('S_VIDEOPLAYER', 'VideoPlayer.onConfigurationChanged', 'SYSTEM',
  'the device configuration changes while the video player is open (rotation, locale, screen size); the activity is not restarted because the manifest lists these in configChanges',
  env=ENV_CONFIG_CHANGE,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:73-76; SRC final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/AndroidManifest.xml:184; FW-SRC core/java/android/app/ActivityThread.java:4893-4896, 4942',
  note='Delivery path: ActivityThread.handleConfigurationChanged (4971), loop at 5031-5037, performConfigurationChangedForActivity (4803-4809), activity.onConfigurationChanged (4942). The body call to Sound.notifyConfigurationChanged (line 75) is not written here. Constant ENV_CONFIG_CHANGE is graph_def.py:126.')

e('S_VIDEOPLAYER', 'VideoPlayer$1.onCompletion', 'FRAMEWORK',
  'the video reaches its end; the MediaPlayer completion listener is set directly on the player by Sound.playSound',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:50-59; SRC com/ichi2/libanki/Sound.java:322, 325-326, 328; FW-SRC media/java/android/media/MediaPlayer.java:3235-3240',
  note='MediaPlayer handles MEDIA_PLAYBACK_COMPLETE and calls onCompletionListener.onCompletion (FW-SRC MediaPlayer.java:3235-3240). The MediaPlayer step is FW-SRC grounded; the listener registration is Sound.java:325-326.')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceCreated', 'FRAMEWORK',
  'the video surface is created while the player screen is shown (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 49-50; SRC com/ichi2/libanki/Sound.java:268, 292-293',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). Body calls Sound.playSound with the path, the completion listener and mVideoView (lines 50-59).')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceChanged', 'FRAMEWORK',
  'the video surface changes size or format while the player screen is shown (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 61-66',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). The body is an empty TODO, so the call has no effect.')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceDestroyed', 'FRAMEWORK',
  'the video surface is destroyed when the player leaves the foreground or finishes (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 68-71',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). Body stops the sounds (line 69) and finishes the activity (line 70).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$1.onSelection', 'GUI',
  'the user taps a saved-search name in the LIST dialog',
  gui=['tap a saved-search name in the saved searches list dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:65-76; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:73',
  note='MISSING GATE MG332: at least one saved search must exist before the LIST dialog has a row to tap. No predefined STATE constant covers saved searches, so env and needs_state are unset. The MaterialDialog list callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnSelection is written in graph_def.py:1659.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$2.onInput', 'GUI',
  'the user types a name in the save-search dialog and confirms',
  gui=['type a name in the save searches dialog and confirm'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:77-87; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:85',
  note='The MaterialDialog input callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnSaveSearch is written in graph_def.py:1675. No gate: the save dialog is opened by the action_save_search menu item.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$3.onPositive', 'GUI',
  'the user taps OK on the remove-search confirmation dialog',
  gui=['tap OK on the remove saved search confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:102-121; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:112',
  note='MISSING GATE MG332: a saved search must exist so that removeSearch shows the confirmation dialog (line 103). No predefined STATE constant covers saved searches, so env and needs_state are unset. The MaterialDialog button callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnRemoveSearch is written in graph_def.py:1667.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter$1.onClick', 'GUI',
  'the user taps the remove button of a saved-search row in the LIST dialog',
  gui=['tap the remove button on a saved-search row in the saved searches list dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:161-166; SRC res/layout/card_browser_item_my_searches_dialog.xml:25; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG332: a saved-search row must exist to render the remove button (getView, line 143). No predefined STATE constant covers saved searches, so env and needs_state are unset. Body calls removeSearch through access$700 (line 164, auto CALL).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter.getView', 'FRAMEWORK',
  'the LIST dialog lays out a saved-search row',
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335, 2365; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:143-168',
  note='MISSING GATE MG332: at least one saved search must exist so that the list has a row. No predefined STATE constant covers saved searches, so env and needs_state are unset. The AbsListView.obtainView path is FW-SRC grounded; the library setAdapter call is INFERRED (library not read).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter.areAllItemsEnabled', 'FRAMEWORK',
  'the list view queries whether all items are enabled when the LIST dialog adapter is set',
  env=None,
  evidence='FW-SRC core/java/android/widget/ListView.java:552, 573; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:67-70, 182-184',
  note='The ListView.setAdapter call is INFERRED (the MaterialDialog builder path is not read). No gate: the LIST dialog itself is enough. Body returns true.')

e('CardBrowserMySearchesDialog$MySearchesArrayAdapter.notifyDataSetChanged', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter$2.compare', 'CALL',
  'Collections.sort inside notifyDataSetChanged calls the comparator to order the saved-search names',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:171-177',
  note='INFERRED: the JDK sort path is not in fw_src, so the comparator call is not read. No auto CALL edge exists for this pair in auto_calls.json, so the edge is written here.')
