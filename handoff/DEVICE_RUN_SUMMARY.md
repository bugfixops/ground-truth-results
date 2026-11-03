# Device run summary (real emulator run, all 13 apps)

- Run: `41593209101-1` (GitHub Actions "Device replay" run 41593209101, started by a push of `handoff/DEVICE_REPLAY_REQUEST.txt`, user instruction 2026-11-03).
- Image: Google APIs, API 27, **x86** (Google publishes no API 27 `google_apis` x86_64 image; see "Runs before this one").
- Date: 2026-11-03.
- CI after the DEVICE-row fix: `<CI commit>` `[ci] rebuild and checks`: all 13 apps errors 0, warnings 0, check 2 0 problems, check 4 0, verdicts unchanged, DEVICE rows on their own `verification device:` line (the first CI after the DEVICE rows, `c2e5b6b7`, request `21c73e8e`, read them wrongly; see the correction below).
- Numbers below are copied from `device/results/41593209101-1/SUMMARY.md` and the per-app `results.csv` / step logs.

**"Not reached" never changes a label.** A route that was not reached, whose script failed, or that is unscriptable gives an `unclear` DEVICE row; no route becomes `wrong` and no label changes. These routes are candidates for the reviewer and Yang to look at; they are not errors in the graph.

## Correction after the reviewer's check (2026-11-03)

The first CI after the DEVICE rows (`c2e5b6b7`) let `tools/build_graph.py` treat the DEVICE rows like the reviewer's path rows: the path error rates counted routes twice, the 14 WRONG routes and 210 SOURCE_OK routes showed UNCHECKED, and `paths[]` listed methods twice. Fixed in `<fix commit>`: DEVICE rows are counted on their own line (`verification device:`), never lower a path status, and never override WRONG; a reached route whose script ran to the end is `DEVICE_OK` (100 routes). The 4 routes that reached the method although the script stopped early (Currency route_05; Vanilla-Music route_05, route_23, route_25) keep a `correct` DEVICE row but their path keeps its earlier status. Verdicts, labels and the path error rates are again exactly those of `f435fca8`.

| App | Routes | Reached | Not reached | Script failed | Unscriptable | Share reached |
|---|---|---|---|---|---|---|
| Currency | 28 | 18 | 10 | 3 | 0 | 64.3% |
| Diary | 30 | 16 | 14 | 11 | 0 | 53.3% |
| hash-checker | 37 | 23 | 13 | 4 | 1 | 62.2% |
| Omni-Notes | 33 | 8 | 23 | 20 | 2 | 24.2% |
| openlauncher | 27 | 5 | 21 | 11 | 1 | 18.5% |
| Vanilla-Music | 30 | 8 | 22 | 19 | 0 | 26.7% |
| Markor | 30 | 7 | 23 | 18 | 0 | 23.3% |
| AnyMemo | 30 | 5 | 22 | 18 | 3 | 16.7% |
| Aegis | 25 | 1 | 21 | 16 | 3 | 4.0% |
| AmazeFileManager | 30 | 0 | 24 | 23 | 4 | 0.0% |
| AnkiDroid | 30 | 0 | 26 | 20 | 4 | 0.0% |
| MMEX | 30 | 6 | 20 | 15 | 4 | 20.0% |
| LibreTorrent | 29 | 7 | 10 | 0 | 12 | 24.1% |
| Total | 389 | 104 | 249 | 178 | 34 | 26.7% |

"Not reached" counts every scripted route whose target method had no covered instruction; "script failed" is the subset whose script stopped before its last step (both can hold for one route, so the columns do not add up to the route count).

## Runs before this one (what was fixed)

- `41578755210` (manual dispatch): all 13 jobs failed in the emulator setup: `system-images;android-27;google_apis;x86_64` does not exist. Fixed: `arch` default `x86` (commit `e97b62cb`).
- `41579432533`: a real-run request was read as a dry run. Fixed: the plan job decides dry/real from the files of the pushed commit (`60862462`).
- `41580035601`: 1 route per app; ROUTES fields shifted (tab IFS collapses empty columns) and adb consumed the route list; Amaze sshd needed an absolute path. Fixed in `device/run_app.sh` (`a147c559`).
- `41580858995`: every UI dump failed to parse (status line after the XML); method names with commas broke results.csv; non-root sshd could not read the system config. Fixed (`453a3b6a`).
- `41581852815` (first complete run, 70 reached): taps raced cold starts. Fixed: tap polls, wait_for floor 30 s, visible-labels diagnostics (`71d7ca9d`).
- `41583852305` (62 reached; Markor lost to a JaCoCo download error): AnyMemo and AmazeFileManager launch components named the application id instead of the code package. Fixed in their route scripts, JaCoCo download retried (`3404c1c9`).
- `41586297765` (76 reached): all-caps button/tab text; Diary's start-up permission dialog. Fixed: case-insensitive fallback, Diary permissions (`5c2bc466`).
- `41589762145` (102 reached): baseline fixtures never pushed; Vanilla library empty without storage permission. Fixed (`d4b1e3af`). This run: 104 reached.

## Routes not reached or failed, per app

### Currency (10)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_02 | `AboutPreference.onBindDialogView` | failed_at_step_16 | Ed6e8977b comment Settings_list_shown ok / E2c2000b9 tap text=About failed |
| route_04 | `ChartActivity.onInvertClick` | failed_at_step_8 | E7cc15d45 comment SELECT_MODE_entered,_row_highlighted ok / E32b68288 tap desc=Chart failed |
| route_07 | `ChartActivity.showToast(String)` | ok | E8fefbfc4 comment automatic:_showToast(int)_delegates_to_showToast(String,Object[]) ok / Ea1dbc7bc comment automatic:_showToast(String,Object[])_delegates_to_showToast(String) ok |
| route_11 | `Singleton.<init>` | ok (method_absent_in_report) | E5330d1fb comment automatic:_ChartActivity.onCreate_calls_Singleton.getInstance ok / E3c7b2a35 comment automatic:_first_call_in_this_process_constructs_the_Singleton ok |
| route_13 | `ChartParser$Handler.<init>` | ok | Ed937b929 comment automatic:_worker_thread_starts_the_ChartParser ok / Ef3349d6d comment automatic:_Handler_constructed_after_ECB_HTTPS_stream_opens ok |
| route_16 | `Data.<init>` | ok (method_absent_in_report) | E2c242327 comment onCreate_calls_Data.getInstance(this) ok / E2f8ae154 comment first_call_in_process:_instance_is_null,_new_Data() ok |
| route_21 | `ChartActivity$DateAxisValueFormatter.getFormattedValue` | ok | Ee53a0deb comment RESULT_OK_result_follows_the_picker_tap;_no_action ok / Eddbb6185 comment MPAndroidChart_redraw_calls_the_formatter;_no_user_action ok |
| route_25 | `CurrencyWidgetProvider.onDeleted` | ok | E0f9de2df comment system_delivers_APPWIDGET_DELETED_to_onReceive;_no_action ok / Eaa043033 comment super.onReceive_dispatches_APPWIDGET_DELETED_to_onDeleted ok |
| route_26 | `CurrencyWidgetUpdate.onDateResult` | ok | E3ec638f8 comment download_failed:_worker_posts_onDateResult(null);_environment-determined,_no_user_action ok / E530d2b10 comment listener.onDateResult(null)_runs_on_the_main_thread ok |
| route_27 | `CurrencyWidgetUpdate.onDestroy` | ok | E3226d82d comment listener.onDataResult(map)_runs_on_the_main_thread ok / E279da83c comment onDataResult_calls_stopSelf()_->_onDestroy ok |

### Diary (14)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `DiaryWidgetUpdate.getYear` | failed_at_step_5 | Ee6b8aa80 tap text=Widgets ok / Ee6b8aa80 wait_for text=Diary failed |
| route_02 | `DiaryWidgetProvider.getHome` | failed_at_step_5 | Ee6b8aa80 tap text=Widgets ok / Ee6b8aa80 wait_for text=Diary failed |
| route_04 | `DiaryWidgetUpdate.nextMonth` | failed_at_step_5 | Ee6b8aa80 tap text=Widgets ok / Ee6b8aa80 wait_for text=Diary failed |
| route_05 | `FileUtils.isLocal` | failed_at_step_13 | E70b5909f comment fragment_resumes_with_the_activity ok / E7ada6d09 wait_for text=Copy_images failed |
| route_06 | `Diary.lambda$addLink$21` | failed_at_step_9 | E86b7a9c5 comment chooser_opened_by_addMedia() ok / Efd4a5146 tap text=Files failed |
| route_08 | `Diary.lambda$sortFiles$0` | failed_at_step_11 | Ee6b8aa80 tap text=Go_to_date… ok / Ee6b8aa80 tap desc=2_November_2026 failed |
| route_09 | `Diary$FindTask.lambda$onPostExecute$0` | failed_at_step_12 | Ea885d6f1 wait_for res_id=markdown ok / E002e1746 tap desc=Search… failed |
| route_10 | `Diary.dateCheck(CharSequence,String)` | failed_at_step_14 | Ee6b8aa80 tap text=Go_to_date… ok / Ee6b8aa80 tap desc=4_November_2026 failed |
| route_12 | `QueryHandler.onInsertComplete` | ok | E8515bd78 comment insertEvent_queries_Calendars_for_an_id ok / E06a409c9 comment first_calendar_id:_startInsert_->_onInsertComplete ok |
| route_19 | `Diary.onRestoreInstanceState` | failed_at_step_14 | E7ada6d09 comment Settings_list_shown ok / E5e8f27e8 tap text=Theme failed |
| route_22 | `Editor.lambda$onBackPressed$3` | failed_at_step_16 | Ea16479ba comment onBackPressed_calls_alertDialog,_changed_branch ok / E2c02c361 wait_for text=Save_changes? failed |
| route_25 | `FileProvider.buildPath` | ok | Ecd7e7fc1 comment sCache_miss,_so_parsePathStrategy_runs ok / Ee37ab436 comment parsePathStrategy_calls_buildPath_for_each_root ok |
| route_26 | `Diary.onDateSet(CustomCalendarView,int,int,int)` | failed_at_step_7 | E002e1746 tap desc=Go_to_date… failed / E002e1746 tap text=Go_to_date… failed |
| route_28 | `Diary.getNextCalendarMonth` | ok | E7a3bcc72 comment vertical_fling_up_calls_onSwipeUp ok / E38e0b13b comment onSwipeUp_calls_getNextCalendarMonth ok |

### hash-checker (13)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_06 | `FNV1a.update256(byte[],int,int)` | failed_at_step_28 | Eb99504ff scroll_to text=todo.txt ok / Eb99504ff scroll_to text=todo.txt failed |
| route_08 | `JdkHashCalculator.inputStreamsFormFolder` | failed_at_step_0 (fixture_push_failed) | (no step log) |
| route_11 | `HashCalculatorFragment.writeHashToFile` | ok | Ed190d0ac tap text=Save ok / Eb39f4a0e comment call:_writeHashToFile_(target) ok |
| route_13 | `Clipboard.clear` | ok | E3d93fc17 wait_for text=From ok / E3d93fc17 comment async:_Clipboard.clear_fired_by_60s_handler ok |
| route_15 | `SettingsFragment.copyFile` | ok | E8654d3ef comment call:_copyUserDataToUserFolder ok / E8dd93771 comment call:_copyFile_(target) ok |
| route_17 | `HashCalculatorFragment.folderNameFromUri` | failed_at_step_0 (fixture_push_failed) | (no step log) |
| route_18 | `FeedbackFragment.sendEmail` | failed_at_step_19 | Eb87d737f wait_for text=Theme ok / Ea2d6404c tap text=Feedback failed |
| route_25 | `App.getShortcut` | ok | E2f51b4e7 comment call:_App.getShortcutForFolderType_(SDK>=26_guard) ok / E97f48490 wait_for res_id=com.smlnskgmail.jaman.hashchecker.thirdparty:id/tv_selected_hash_type ok |
| route_28 | `SharedPreferencesSettings.containsPreference` | ok | Ea8fdd297 comment App.setLocale_->_SharedPreferencesSettings.languageIsInitialized:_if_(!settings.languageIsInitialized())_(App.java:154)._Internal_call;_no_user_action. ok / E433eabe1 comment SharedPreferencesSettings.l |
| route_29 | `SharedPreferencesSettings$SharedPreferencesSettingsKeyExtractor.<init>` | ok | Ec9cfde17 comment App.onCreate_->_App$1.<init>:_new_SharedPreferencesSettings(...)_construction_begins_at_PreferenceManager.getDefaultSharedPreferences(this)_(App.java:58)._Internal_call;_no_user_action. ok / E75342ab8 c |
| route_35 | `DatabaseHelperModule.<init>` | ok | E7aab529b comment App.onCreate_lifecycle ok / E4a4779ed comment Dagger_builder_calls_new_DatabaseHelperModule() ok |
| route_36 | `SettingsHelperModule.<init>` | ok | E7aab529b comment App.onCreate_runs_right_after_App_construction_(framework_lifecycle,_no_user_action) ok / E13bfb3f1 comment App.onCreate_constructs_SettingsHelperModule_directly_(App.java:72,_plain_new_call,_no_user_ac |
| route_37 | `ThemeHelperModule.<init>` | ok | E7aab529b comment App.onCreate_runs_right_after_App_construction_(framework_lifecycle,_no_user_action) ok / Efe9214b4 comment App.onCreate_constructs_ThemeHelperModule_directly_(App.java:74,_plain_new_call,_no_user_actio |

### Omni-Notes (23)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `DetailFragment.onCoordinatesResolved` | failed_at_step_13 | E8a16cf02 comment A_new_note_is_opened ok / Ecd2baeb2 tap text=Attachment failed |
| route_02 | `SpringImportHelper.lambda$importDataFromSpringpad$0` | failed_at_step_10 | E7e3c321b comment List_set_up_on_the_default_Notes_navigation ok / E89ba0d21 tap desc=Open_navigation_drawer failed |
| route_03 | `FileHelper.isMediaDocument` | failed_at_step_10 | E7e3c321b comment List_set_up_on_the_default_Notes_navigation ok / E89ba0d21 tap desc=Open_navigation_drawer failed |
| route_04 | `DetailFragment.onLocationUnavailable` | failed_at_step_3 | Ea7466154 launch component=it.feio.android.omninotes/.MainActivity ok / E8050f4c2 tap desc=Open_navigation_drawer failed |
| route_05 | `DbHelper.deleteNote(long,boolean)` | failed_at_step_11 | E7e3c321b long_tap res_id=it.feio.android.omninotes:id/fab ok / E7e3c321b tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_06 | `Attachment.<init>(BaseAttachment)` | failed_at_step_11 | E7e3c321b long_tap res_id=it.feio.android.omninotes:id/fab ok / E7e3c321b tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_07 | `RecurrenceHelper.nextReminderFromRecurrenceRule(long,long,String)` | failed_at_step_11 | Ef79712d5 long_tap res_id=it.feio.android.omninotes:id/fab ok / Ef79712d5 tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_08 | `LogDelegate.w(String)` | failed_at_step_11 | E89ba0d21 long_tap res_id=it.feio.android.omninotes:id/fab ok / E89ba0d21 tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_09 | `Tag$1.<init>` | failed_at_step_11 | Ed7cc3cfc long_tap res_id=it.feio.android.omninotes:id/fab ok / Ed7cc3cfc tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_10 | `ListFragment.lambda$null$11` | failed_at_step_11 | E89ba0d21 long_tap res_id=it.feio.android.omninotes:id/fab ok / E89ba0d21 tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_11 | `CategoryBaseAdapter.isSelected` | failed_at_step_18 | E4c082c59 long_tap res_id=it.feio.android.omninotes:id/fab ok / E4c082c59 tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_12 | `IdeogramsWordCounter.<init>` | failed_at_step_16 | Edbf61bdc tap desc=More_options ok / Edbf61bdc tap text=Info failed |
| route_14 | `DataBackupIntentService.deleteData` | failed_at_step_30 | E7e0a24a4 comment The_delete_confirmation_opens ok / Ee925a6f2 tap text=Confirm failed |
| route_15 | `DetailFragment.removeAttachment(Attachment)` | ok | - comment DetailFragment.removeAttachment(Attachment)_UNREACHABLE_no_edges ok |
| route_16 | `BitmapHelper.getImageBitmap` | failed_at_step_13 | E8a16cf02 comment A_new_note_is_opened ok / E8a16cf02 tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_18 | `DateUtils.prettyTime(Long,Locale)` | ok | E44b7f1a8 comment Prettified-dates_preference_on_(default):_prettyTime(Long) ok / E0b50a073 comment Direct_call_dispatching_to_prettyTime(Long,Locale) ok |
| route_19 | `Category.<init>(Parcel)` | failed_at_step_13 | E8a16cf02 comment A_new_note_is_opened ok / Ea13ecca1 tap text=Category failed |
| route_20 | `DbHelper.deleteCategory` | failed_at_step_1 | (no step log) |
| route_21 | `Attachment$1.<init>` | failed_at_step_13 | E8a16cf02 comment A_new_note_is_opened ok / Ecd2baeb2 tap text=Attachment failed |
| route_22 | `Stats.getCharsMax` | failed_at_step_15 | E4306cbbb comment The_settings_root_is_shown ok / E4bc4bf24 tap text=Statistics failed |
| route_23 | `NoteProcessor.afterProcess` | failed_at_step_11 | E7e3c321b long_tap res_id=it.feio.android.omninotes:id/fab ok / E7e3c321b tap res_id=it.feio.android.omninotes:id/detail_title failed |
| route_24 | `NotificationChannels.getChannels` | ok | E9d299ee9 comment initNotificationChannels()_in_the_app_process ok / Edc764532 comment getChannels()_on_API_27 ok |
| route_31 | `MediaStoreFactory.<init>` | failed_at_step_21 | Edb933e2f comment The_system_document_picker_opens_(ACTION_GET_CONTENT,_application/zip) ok / E821c0225 tap text=archive.zip failed |

### openlauncher (21)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `HideAppsFragment$2$1.onClick` | failed_at_step_20 | Ee3b2c4ce comment Settings_root_fragment_with_7_category_buttons_added ok / Ea89dcc77 tap text=Icons failed |
| route_02 | `AppItemView.setTargetedWidth` | ok | Eca084228 comment factory.create_makes_a_new_ViewHolder ok / E56601e87 comment ViewHolder_calls_setTargetedWidth(itemWidth) ok |
| route_03 | `AppDrawerController.scrollToStart` | ok | E34537d4a comment animator_end_dispatches_to_Home$6.onEnd ok / E9c94ad31 comment onEnd_calls_scrollToStart ok |
| route_04 | `WidgetView.<init>(Context)` | ok | Eba47afc5 comment createView_calls_WidgetHost.onCreateView ok / Ebae97443 comment onCreateView_makes_a_new_WidgetView ok |
| route_06 | `MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.<init>` | ok | Eb65c5e5a comment ViewBinder.bind_creates_the_unbinder ok / E494d6177 comment TARGET:_createUnbinder_builds_InnerUnbinder ok |
| route_07 | `Tool.checkForUnusedIconAndDelete` | failed_at_step_16 | Ecb7f915c comment drawer_settles_open:_minibar_page_shown ok / Ee8ace45b tap text=Shortcut_for_the_OpenLauncher_settings. failed |
| route_08 | `LauncherSettings.setPinchGesture` | failed_at_step_16 | Ecb7f915c comment drawer_settles_open:_minibar_page_shown ok / Ee8ace45b tap text=Shortcut_for_the_OpenLauncher_settings. failed |
| route_09 | `Tool.clampInt` | ok | Ed7e82317 comment preamble_folder_icon_draws_itself_(GroupIconDrawable.draw) ok / E4e73e729 comment TARGET:_folder-icon_animation_calls_Tool.clampInt ok |
| route_10 | `GroupPopupView$6$1.hereIsTheText` | failed_at_step_14 | E506c5f2f wait_for res_id=desktop ok / E43dc7c02 tap text=Unnamed failed |
| route_11 | `GroupIconDrawable.init` | ok | E853298a5 comment direct_call:_getItemView_->_getGroupIconDrawable ok / Ed2cb52b1 comment direct_call:_GroupIconDrawable.<init>_->_init_(target) ok |
| route_12 | `DialogUtils.copy` | failed_at_step_20 | Ee3b2c4ce comment framework:_Settings_root_fragment_with_7_categories ok / E124be037 tap text=Other failed |
| route_13 | `Desktop$Item.newWidgetItem` | ok | E79df4ba0 comment framework:_onActivityResult_->_createWidget ok / E567cf400 comment direct_call:_createWidget_->_Desktop.Item.newWidgetItem_(target) ok |
| route_15 | `Tool.saveIconAndReturnID` | failed_at_step_13 | E9629945d comment framework:_groupPopup.dismissPopup() ok / E506c5f2f comment framework:_popup_hidden,_home_desktop_reached,_shortcut_receiver_registered ok |
| route_16 | `Home.configureWidget` | ok | E306c7943 comment NOT_DRIVEN:_choose_a_widget_in_the_system_picker_--_picker_is_system_UI,_widget_list_is_image-dependent,_no_verifiable_selector;_any_widget_with_RESULT_OK_satisfies_this_edge ok / Ed455aea5 comment fram |
| route_17 | `DeviceAdminReceiver.onReceive` | failed_at_step_4 | E15938fe2 tap text=Activate_this_device_admin_app failed / E15938fe2 tap text=Activate failed |
| route_19 | `Desktop$DesktopAdapter.getItemFromCoordinate` | failed_at_step_15 | E506c5f2f comment S_HOME_DESKTOP:_popup_hidden,_desktop_shown ok / E0f6246f9 long_tap text=All_Apps failed |
| route_20 | `MinibarEditActivity$Item$ViewHolder.<init>` | failed_at_step_18 | Ecb7f915c comment S_HOME_MINIBAR:_minibar_open_at_STATE_IDLE_with_the_left_drawer_open ok / E738b5300 tap res_id=iv failed |
| route_21 | `DialogUtils$2.onSelection` | failed_at_step_23 | Ee3b2c4ce comment S_SETTINGS_ROOT:_7_category_buttons_added_by_MaterialPrefFragment ok / E7ef50d09 tap text=App_Drawer failed |
| route_23 | `IconLabelItem$ViewHolder.<init>` | failed_at_step_24 | E2b9b86b1 scroll_to res_id=minBar ok / E2b9b86b1 scroll_to res_id=minBar failed |
| route_24 | `FiveSecsDelayContentProvider.onCreate` | ok | Edb156ef1 launch component=com.benny.openlauncher/com.benny.openlauncher.activity.Init ok / Ea9707b85 comment attachInfo_calls_provider_onCreate_at_process_start;_no_user_action ok |
| route_25 | `FiveSecsDelayContentProvider.<init>` | ok | Edb156ef1 launch component=com.benny.openlauncher/com.benny.openlauncher.activity.Init ok |

### Vanilla-Music (22)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_03 | `SongTimeline.removeSongPosition` | failed_at_step_9 | Ebe7c67e2 wait_for text=Play_all ok / Ebe7c67e2 tap text=Play_all ok |
| route_04 | `CoverCache$BitmapDiskCache.getUsedSpace` | failed_at_step_6 | E860e3aca tap text=Albums ok / E860e3aca wait_for text=Daybreak failed |
| route_06 | `SongTimeline.removeSong` | failed_at_step_7 | E80427a98 wait_for res_id=text ok / E80427a98 tap res_id=text ok |
| route_07 | `SongTimeline$FlagComparator.compare` | ok | E0591813a comment FlagComparator.compare_via_Collections.sort_(target) ok / E0591813a screenshot out/Vanilla-Music/screens/route_07/route_07_end.png ok |
| route_08 | `Limiter.<init>` | failed_at_step_5 | E80427a98 wait_for res_id=pager ok / E89b88b79 tap text=Files failed |
| route_10 | `CoverBitmap.drawText` | failed_at_step_7 | E80427a98 wait_for res_id=text ok / E80427a98 tap res_id=text ok |
| route_11 | `PlaylistActivity.onFancyItemSelected` | failed_at_step_6 | E80427a98 tap text=Tracks ok / E80427a98 wait_for text=Morning_Light failed |
| route_12 | `ScheduledLibraryUpdate.finalizeScan` | failed_at_step_15 | Ea27ba51e tap text=Tracks ok / Ea27ba51e wait_for text=Morning_Light failed |
| route_14 | `MiniPlaybackActivity.onClick` | failed_at_step_16 | E752a94e4 tap text=Tracks ok / E752a94e4 wait_for text=Morning_Light failed |
| route_15 | `AudioSearchActivity.onSearchCompleted` | ok | E1aa732d6 comment onPostExecute_dispatch,_no_user_action ok / E35daf840 comment onSearchCompleted_dispatch_from_onPostExecute,_target ok |
| route_16 | `TrackDetailsDialog$1$1.<init>` | failed_at_step_8 | E80427a98 tap text=Tracks ok / E4815c188 wait_for text=Morning_Light failed |
| route_18 | `MediaLibrary.updateSongPlayCounts` | failed_at_step_6 | E80427a98 tap text=Tracks ok / E80427a98 wait_for text=Morning_Light failed |
| route_19 | `BottomBarControls.setCover` | failed_at_step_15 | E5169a1ac tap text=Tracks ok / E5169a1ac wait_for text=Morning_Light failed |
| route_20 | `TrackDetailsDialog.<init>` | failed_at_step_6 | E80427a98 tap text=Tracks ok / E80427a98 wait_for text=Morning_Light failed |
| route_21 | `FullPlaybackActivity.updateQueuePosition` | ok | E0d982b9c comment handler-MSG_UPDATE_POSITION-no-user-action ok / E588dc475 comment message-branch-call-target-reached ok |
| route_22 | `MediaScanner$MediaScanPlan.clear` | failed_at_step_7 | E95b25aef comment openMenu-follows-overflow-tap ok / E38459d6f wait_for text=Settings failed |
| route_24 | `SlidingTabStrip.blendColors` | ok | Eeff96387 comment framework-onDraw-no-user-action ok / E05a156b0 comment direct-call-target-reached ok |
| route_26 | `PermissionRequestActivity.onRequestPermissionsResult` | failed_at_step_11 | E8799b914 comment activity_start:_system_creates_PermissionRequestActivity ok / E9c3875c1 comment lifecycle:_onCreate_runs_on_activity_start ok |
| route_27 | `MediaUtils.getCursorForFileQuery` | ok | E22acec54 comment direct_call:_runQuery_adds_the_songs_to_the_timeline ok / E99e07df4 comment direct_call:_timeline_query_reads_the_file_cursor ok |
| route_28 | `Song.hashCode` | ok | E32c7773c comment direct_call:_finish_action_compares_songs ok / E61cc58d1 comment direct_call:_equals_invokes_hashCode_(target) ok |
| route_29 | `LibraryPagerAdapter.setFilter` | failed_at_step_5 | E80427a98 wait_for text=Play_all ok / E4af31f11 tap desc=More_options failed |
| route_30 | `PlaybackService.getDuration` | failed_at_step_7 | E80427a98 tap text=Tracks ok / E80427a98 wait_for text=Morning_Light failed |

### Markor (23)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `ActionButtonSettingsActivity.lambda$saveNewOrder$0` | failed_at_step_9 | E0ecb8e4d comment notebook_tab_shown_by_default_after_cold_start ok / E54b4aedd tap text=More failed |
| route_02 | `SyntaxHighlighterBase.isFixupOverlap` | failed_at_step_9 | E0ecb8e4d comment notebook_tab_shown_by_default_after_cold_start ok / Eba14bdbd tap text=notes.md failed |
| route_03 | `SyntaxHighlighterBase$1.draw` | failed_at_step_9 | E0ecb8e4d comment notebook_tab_shown_by_default_after_cold_start ok / E54b4aedd tap text=To-Do failed |
| route_04 | `DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getLinkTitle` | failed_at_step_10 | E5426bbe1 comment share-into_screen_shown ok / E9a1bd2ed tap text=To-Do failed |
| route_05 | `StoragePermissionActivity.processPermissionState` | failed_at_step_14 | E38d9bf48 comment onActivityFirstTimeVisible_calls_askForPermissions ok / E2ff3aaf6 tap text=Yes failed |
| route_06 | `FlexmarkKatexExtension$KatexInlineMath.getText` | failed_at_step_3 | E211966cc launch component=net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity ok / E3b54bcd8 long_tap text=notes.md failed |
| route_07 | `DocumentEditAndViewFragment$2.lambda$search$0` | failed_at_step_3 | E211966cc launch component=net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity ok / E54b4aedd tap text=To-Do failed |
| route_08 | `FileSearchEngine.isEncryptedFile` | failed_at_step_3 | E211966cc launch component=net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity ok / E14b03637 tap res_id=toolbar failed |
| route_09 | `CsvConfig.findChar` | failed_at_step_3 | E211966cc launch component=net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity ok / E54b4aedd tap text=To-Do failed |
| route_10 | `WikitextLinkResolver.findNotebookRootDir(File,File,boolean)` | failed_at_step_3 | E211966cc launch component=net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity ok / E54b4aedd tap text=To-Do failed |
| route_11 | `WikitextLinkResolver.wikitextPagePathToRelativeFilePath` | failed_at_step_9 | E0ecb8e4d comment notebook_tab_is_the_default_startup_tab ok / E54b4aedd tap text=QuickNote failed |
| route_12 | `WrFilesWidgetFactory.getLoadingView` | ok | Ef25c6b36 comment adapter_calls_factory.onDataSetChanged ok / E5c43a497 comment adapter_calls_factory.getLoadingView ok |
| route_13 | `TodoWidgetRemoteViewsFactory.getCount` | ok | E54993a4b comment adapter_calls_factory.onDataSetChanged ok / E164691c4 comment adapter_calls_factory.getCount ok |
| route_14 | `AppSettings.getAttachmentFolder` | failed_at_step_9 | E0ecb8e4d comment notebook_tab_is_the_default_startup_tab ok / E54b4aedd tap text=To-Do failed |
| route_15 | `DocumentShareIntoFragment$ShareIntoImportOptionsFragment.lambda$hasLinks$1` | ok | E7756ddc7 comment afterOnCreate_calls_hasLinks ok / Eac7de4e9 comment hasLinks_forEachline_callback_runs_on_the_link_line ok |
| route_16 | `MarkorContextUtils.getIntentFile(Intent)` | failed_at_step_12 | E03c42d58 comment Todo_widget_shown_by_the_launcher ok / E7a697b93 tap res_id=todo_widget_container failed |
| route_18 | `GsPreferenceFragmentBase.tintPrefIconsRecursive` | failed_at_step_9 | E0ecb8e4d comment Notebook_tab_shown_by_default_after_cold_start ok / E70fd6983 tap text=More failed |
| route_19 | `GsFileBrowserListAdapter.createDirectoryHere` | failed_at_step_9 | E0ecb8e4d comment Notebook_tab_shown_by_default_after_cold_start ok / E3b54bcd8 long_tap text=notes.md failed |
| route_20 | `AppSettings.lambda$getPopularDocumentsSorted$1` | failed_at_step_9 | E0ecb8e4d comment Notebook_tab_shown_by_default_after_cold_start ok / E54b4aedd tap text=To-Do failed |
| route_21 | `SyntaxHighlighterBase$SpanGroup.compareTo` | failed_at_step_8 | E659e191c comment system_lifecycle:_onPostResume,_no_user_action ok / E0ecb8e4d wait_for text=To-Do failed |
| route_22 | `GsFileBrowserListAdapter.lambda$scrollToAndFlash$3` | failed_at_step_8 | E659e191c comment system_lifecycle:_onPostResume,_no_user_action ok / E0ecb8e4d wait_for text=.. failed |
| route_23 | `GsSharedPreferencesPropertyBackend.getStringListOne` | ok | E7b101054 comment direct_call:_getStringList,_no_user_action ok / Eb085a8fa comment direct_call:_getStringListOne,_no_user_action ok |
| route_29 | `GsSharedPreferencesPropertyBackend.rcolor` | ok | Eab4b9c7d comment fresh-install_guard_calls_setEditorBasicColor ok / Edd5ddb37 comment setEditorBasicColor_calls_rcolor_(target) ok |

### AnyMemo (22)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `DefaultScheduler.randomNumber` | failed_at_step_28 | E7318059a comment options_menu_inflated_by_the_framework ok / Ed6809c1a tap res_id=action_search failed |
| route_03 | `CardDaoImpl.getCardsByCategory` | ok | E29ea0011 comment queue_refilled_for_the_category ok / E3caa50fb comment target:_cards_loaded_by_category ok |
| route_04 | `Mnemosyne2CardsImporter$ValueType.<clinit>` | failed_at_step_33 | E3edbc981 tap text=.. ok / E3edbc981 tap text=Download failed |
| route_05 | `DownloaderUtils.downloadFile` | failed_at_step_31 | E30961aed comment download_confirmation_dialog_shown ok / Edbdccc47 comment download_confirmation_dialog_entered ok |
| route_06 | `AudioRecorderFragment$2.<init>` | failed_at_step_28 | Ea4753c40 tap res_id=editmenu_list_id failed / Ea4753c40 tap desc=More_options failed |
| route_07 | `SettingsScreen$11.onFileBrowserFileClick` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_(S_MAIN_RECENT) ok / E6da90567 tap desc=Misc failed |
| route_09 | `ExportAnyMemoDbFragment$3.accept` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_(S_MAIN_RECENT) ok / E6da90567 tap desc=Misc failed |
| route_10 | `DatabaseOperationDialogUtil$4$1.onCancel` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_(S_MAIN_RECENT) ok / E6da90567 tap desc=Open failed |
| route_11 | `Option.getCopyClipboard` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_(S_MAIN_RECENT) ok / E6da90567 tap desc=Misc failed |
| route_12 | `Category.setName` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_(S_MAIN_RECENT) ok / E6da90567 tap desc=Misc failed |
| route_13 | `AMDateUtil.<init>` | failed_at_step_12 | E690f7694 comment Recent_tab_shown;_first-run_sample_deck_present ok / E6da90567 tap text=Open failed |
| route_14 | `Card.setId` | failed_at_step_12 | E690f7694 comment Recent_tab_shown;_first-run_sample_deck_present ok / E6da90567 tap text=Open failed |
| route_15 | `FileBrowserActivity.fileClickAction` | failed_at_step_12 | E690f7694 comment Recent_tab_shown ok / E6da90567 tap text=Misc failed |
| route_16 | `AlgorithmCustomizationScreen$1$1.<init>` | failed_at_step_12 | E690f7694 comment Recent_tab_shown ok / E61565a0d tap text=Options failed |
| route_18 | `SettingsScreen$12.onFileBrowserFileClick` | failed_at_step_25 | Eb0ac90c3 comment posted_runnable_runs ok / Efa212a15 comment post-init_runnable_sets_content_view_and_updates_views ok |
| route_19 | `Option$DictApp.parse` | failed_at_step_25 | E42afebab tap text=.. ok / E42afebab tap text=empty.db failed |
| route_21 | `Card.setCreationDate` | failed_at_step_25 | E42afebab tap text=.. ok / E42afebab tap text=empty.db failed |
| route_22 | `CardDaoImpl$1.call` | failed_at_step_25 | E42afebab tap text=.. ok / E42afebab tap text=empty.db failed |
| route_23 | `SpeakWord.stripNonCardContent` | failed_at_step_12 | E690f7694 comment Recent_tab_shown_with_the_sample_database ok / E6da90567 tap text=Misc failed |
| route_24 | `NotificationChannelUtil.createConversationNotificationChannel` | ok | E59c50255 comment AMApplication.onCreate_calls_createNotificationChannels ok / E53a88770 comment createNotificationChannels_calls_createConversationNotificationChannel_(target_edge) ok |
| route_29 | `NotificationChannelUtil.createCardPlayerNotificationChannel` | ok | E59c50255 comment AMApplication.onCreate_calls_createNotificationChannels ok / E79c07339 comment createNotificationChannels_calls_createCardPlayerNotificationChannel_(target_edge) ok |
| route_30 | `NotificationChannelUtil.createReviewReminderNotificationChannel` | ok | E59c50255 comment AMApplication.onCreate_calls_createNotificationChannels ok / E8e2a72c5 comment createNotificationChannels_calls_createReviewReminderNotificationChannel_(target_edge) ok |

### Aegis (21)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `AndOtpImporter$EncryptedState.decryptNewFormat(SecretKey)` | failed_at_step_44 | Ec9f89766 comment the_OK_button_gives_the_chosen_`andOTP`_importer_to_the_import_listener:_the_file_picker_opens ok / E36789acd comment the_file_picker_opens_(ACTION_GET_CONTENT)_through_the_import_launcher,_after_the_`a |
| route_03 | `StratumImporter$EncryptedState.decrypt(SecretKey)` | failed_at_step_41 | Eb87e30cd comment the_file_import_row_opens_the_importer_dialog_(isDirect_false) ok / E9edc8c99 tap text=Stratum_(Authenticator_Pro) failed |
| route_04 | `TwoFASImporter$EncryptedState.deriveKey` | failed_at_step_45 | E0fa92879 comment the_file_picker_opens_(ACTION_GET_CONTENT)_through_the_import_launcher,_after_the_`2FAS`_importer_is_chosen ok / E4e57b914 tap text=twofas_backup.json failed |
| route_05 | `RawSlot.getType` | failed_at_step_15 | Ee1d29ff8 tap res_id=btnImport ok / E3870f4a6 wait_for text=aegis-vault-type0.json failed |
| route_06 | `TotpAuthenticatorImporter$EncryptedState.lambda$decrypt$0` | failed_at_step_41 | Eb87e30cd comment the_file_import_row_opens_the_importer_dialog_(isDirect_false) ok / Eb51c0932 tap text=TOTP_Authenticator failed |
| route_07 | `AuthenticatorPlusImporter$EncryptedState.decrypt(char[])` | failed_at_step_45 | E52e9d592 comment the_file_picker_opens_(ACTION_GET_CONTENT)_through_the_import_launcher,_after_the_`Authenticator_Plus`_importer_is_chosen ok / Eb153224d tap text=authplus_backup.zip failed |
| route_08 | `AuthyImporter$EncryptedState.decrypt(char[])` | failed_at_step_45 | E47e55c77 comment the_file_picker_opens_(ACTION_GET_CONTENT)_through_the_import_launcher,_after_the_`Authy`_importer_is_chosen ok / Ed873cb82 tap text=authy_backup.xml failed |
| route_10 | `EntryAdapter.setTempHighlightEntry` | failed_at_step_39 | E69bb265a type_text len=11 ok / E69bb265a tap res_id=text_issuer failed |
| route_11 | `GroupAdapter.getGroupByUUID` | failed_at_step_32 | Eb43a1733 type_text len=11 ok / Eb43a1733 tap res_id=text_issuer failed |
| route_12 | `ScannerActivity.lambda$onQrCodeDetected$1` | failed_at_step_43 | Eb421b292 comment direct_call_into_the_String_error_dialog ok / Ed9b44100 wait_for text=An_error_occurred_while_trying_to_read_the_QR_code failed |
| route_13 | `ImportExportPreferencesFragment$ExportResultListener.onTaskFinished` | ok | Ec9295cb2 comment export_result_posted_to_the_main_thread ok / E546cc6f9 comment export_task_done:_listener_shows_toast_or_error_dialog:_TARGET_REACHED ok |
| route_14 | `AegisImporter$DecryptedState.getCredentials` | ok | E616ffa9b comment decrypted_state_goes_to_the_Welcome_listener ok / Efd47250b comment onStateDecrypted_calls_getCredentials:_TARGET_REACHED ok |
| route_15 | `IconPackExistsException.getIconPack` | failed_at_step_43 | Eb2fa28dd tap text=device-icon-pack.zip ok / Eb2fa28dd wait_for text=Device_Icon_Pack failed |
| route_16 | `GoogleAuthProtos$MigrationPayload.parser` | failed_at_step_34 | Ef0ebbe1d comment scan-image_chooser_started_through_the_QR_scan_launcher ok / E6d7a279a wait_for text=device-qr-export.png failed |
| route_18 | `AuditLogDao_Impl.__EventType_enumToString` | ok | Ea076a7d4 comment insertion_adapter_binds_the_entry_columns ok / Eb7b2b852 comment Direct_call:_TARGET_REACHED ok |
| route_19 | `SlotIntegrityException.<init>(Throwable)` | failed_at_step_41 | E5c8f972e tap text=Encryption ok / E5c8f972e tap res_id=text_password failed |
| route_20 | `IconPack$Icon.<init>` | failed_at_step_15 | Eb9515d18 tap res_id=fab ok / Eb9515d18 wait_for text=aegis_icon_pack.zip failed |
| route_22 | `EditEntryActivity.deleteAndFinish` | failed_at_step_32 | Ea76ae1a0 type_text len=13 ok / Ea76ae1a0 tap res_id=text_issuer failed |
| route_23 | `GoogleAuthProtos$MigrationPayload$DigitCount$DigitCountVerifier.<init>` | failed_at_step_32 (method_absent_in_report) | Ea76ae1a0 type_text len=9 ok / Ea76ae1a0 tap res_id=text_issuer failed |
| route_24 | `Hilt_AegisApplication.<init>` | ok | Eb9515d18 launch component=com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity ok / Ecaf88dff comment superclass_constructor_runs_at_process_start:_target_reached ok |
| route_25 | `AegisApplication.<init>` | ok | Eb9515d18 launch component=com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity ok |

### AmazeFileManager (26)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `CloudIconDataFetcher.cancel` | failed_at_step_3 | Ef3576ae6 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / Ef3576ae6 tap desc=Open_navigation_drawer failed |
| route_02 | `FtpTileService.updateTileState` | failed_at_step_3 | Ef3576ae6 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / Ef3576ae6 tap desc=Open_navigation_drawer failed |
| route_03 | `ApkImageDataFetcher.cancel` | failed_at_step_3 | Ef3576ae6 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / Ef3576ae6 tap desc=Open_navigation_drawer failed |
| route_04 | `GlideRequests.load(Integer)` | failed_at_step_3 | E3f6c0e47 start_intent action=android.intent.action.VIEW ok / E3f6c0e47 wait_for text=sub failed |
| route_07 | `SshAuthenticationTask$1.getPublic` | failed_at_step_3 | E6b899d64 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E6b899d64 tap res_id=com.amaze.filemanager:id/fabs_menu failed |
| route_08 | `SshConnectionPool$AsyncRemoveConnection.onPostExecute` | failed_at_step_3 | E393625fa launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E393625fa tap res_id=com.amaze.filemanager:id/fabs_menu failed |
| route_09 | `PasteHelper.<init>(Parcel)` | failed_at_step_7 | E6a0c67c7 start_intent action=-_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E6a0c67c7 wait_for text=amaze_search.txt failed |
| route_10 | `PasteHelper.writeToParcel` | failed_at_step_3 | E795acdbd launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E795acdbd wait_for text=pastefixture.txt failed |
| route_11 | `PasteHelper$1.createFromParcel` | failed_at_step_7 | E6a0c67c7 start_intent action=-_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E6a0c67c7 wait_for text=amaze_search.txt failed |
| route_13 | `ProcessViewerFragment$CustomServiceConnection$1.<init>` | ok | E91123cce comment onServiceConnected_constructs_anonymous_ProgressListener_at_ProcessViewerFragment.java:416 ok / E91123cce screenshot out/AmazeFileManager/screens/route_13/route_13_process_viewer.png ok |
| route_14 | `ImmutableEntry.getValue` | failed_at_step_4 | Edd3316a5 start_intent action=android.intent.action.VIEW_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.TextEditorActivity ok / Ef5b5e2c8 wait_for res_id=fname failed |
| route_15 | `TextEditorActivity$3.onAnimationEnd` | failed_at_step_4 | Edd3316a5 start_intent action=android.intent.action.VIEW_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.TextEditorActivity ok / E02683734 wait_for res_id=fname failed |
| route_16 | `TextEditorActivity$2.onAnimationEnd` | failed_at_step_4 | Edd3316a5 start_intent action=android.intent.action.VIEW_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.TextEditorActivity ok / E02683734 wait_for res_id=fname failed |
| route_17 | `ReadFileTask$ReturnedValues.<init>(int)` | ok | Ee495bc45 comment load_executes_ReadFileTask;_AsyncTask_dispatches_doInBackground ok / E5c4cc446 comment openInputStream_throws_for_the_missing_row;_catch_(IOException)_returns_ReturnedValues(EXCEPTION_IO) ok |
| route_18 | `ShareAdapter$ViewHolder.lambda$render$0` | failed_at_step_3 | Ef3576ae6 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / Ec93a3d5b tap desc=Open_navigation_drawer failed |
| route_19 | `Indicator$PendingRevealAnimator$1.onAnimationEnd` | failed_at_step_3 (coverage_missing) | E380fe171 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E45d73a86 wait_for res_id=pager failed |
| route_20 | `ItemPopupMenu$2.onButtonPressed(Intent,String)` | failed_at_step_4 | E61915364 push_fixture /home/runner/work/ground-truth-results/ground-truth-results/device/routes/AmazeFileManager/amaze_encrypt_fixture.txt_->_/sdcard/Download/amaze_encrypt_fixture.txt ok / E987df97b tap desc=More_optio |
| route_21 | `MainFragment.onDetach` | failed_at_step_11 | E411e6c12 comment framework_runs_MainFragment.onResume ok / E6b1dbdd0 tap desc=Open_navigation_drawer failed |
| route_23 | `PemToKeyPairTask.toastOnParseError` | failed_at_step_3 | E393625fa launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E393625fa tap res_id=com.amaze.filemanager:id/fabs_menu failed |
| route_24 | `ThemedImageView.getActivity` | failed_at_step_3 | Ebe9ec603 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / Ebe9ec603 tap desc=Open_navigation_drawer failed |
| route_25 | `CompressedExplorerFragment.onDestroyView` | ok | E04be16b9 key KEYCODE_BACK ok / Efafabe30 comment BACK_navigation_drives_CompressedExplorerFragment.onDestroyView ok |
| route_26 | `GenericCopyUtil.doCopy` | failed_at_step_5 | E6b899d64 start_intent action=-_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E6b899d64 wait_for text=route26_source.txt failed |
| route_27 | `FileUtils.lambda$scanFile$1` | failed_at_step_6 | E69f5f041 start_intent action=-_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E69f5f041 wait_for text=route27_source.txt failed |
| route_28 | `ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0` | failed_at_step_5 (coverage_missing) | E7836345a start_intent action=-_component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E7836345a wait_for text=route28_archive.zip failed |
| route_29 | `HybridFile$11.<init>` | failed_at_step_3 | E13267468 launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E13267468 tap res_id=com.amaze.filemanager:id/fabs_menu failed |
| route_30 | `UtilsHandler.getSshAuthPrivateKeyColumn` | failed_at_step_3 | E393625fa launch component=com.amaze.filemanager.debug/com.amaze.filemanager.activities.MainActivity ok / E393625fa tap res_id=com.amaze.filemanager:id/fabs_menu failed |

### AnkiDroid (26)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `Phrase.<init>` | failed_at_step_9 | Ea73b74da comment study_options_fragment_shown ok / E518f89ef tap text=Study failed |
| route_03 | `Stats$1.compare` | failed_at_step_9 | Ea73b74da comment study_options_fragment_shown ok / E518f89ef tap text=Study failed |
| route_04 | `Sched._cntFnNew` | ok | E91386df9 comment _resetNewCount_->__walkingCount_(_cntFnNew_passed) ok / Ee3f8c63a comment _walkingCount_reflectively_invokes__cntFnNew_(target) ok |
| route_05 | `libanki.Utils$1.<init>` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_06 | `Sched.revDue` | ok | Efe9bd917 comment finishedMsg_appends__nextDueMsg ok / Eb7092458 comment revDue()_evaluated_as_the_if_test_(target) ok |
| route_07 | `MediaCheckDialog$3.<init>` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_08 | `ModelEditorContextMenu.onCreateDialog` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_09 | `Finder.findNotes` | failed_at_step_9 | Ea73b74da comment study_options_fragment_shown ok / E518f89ef tap text=Study failed |
| route_10 | `Template$1.compare` | ok | E82c9f13e comment render_unescaped ok / Ef98eff28 comment tag_sort_calls_Template$1.compare_(target;_JDK_dispatch_INFERRED) ok |
| route_11 | `StudyOptionsActivity.closeStudyOptions(int)` | failed_at_step_9 | Ea73b74da comment study-options_fragment_page_shown ok / E57aebbea tap desc=More_options failed |
| route_12 | `HttpFetcher.downloadFileToSdCardMethod` | failed_at_step_9 | Ea73b74da comment study-options_fragment_page_shown ok / E518f89ef tap text=Study failed |
| route_13 | `Sound.notifyConfigurationChanged` | failed_at_step_9 | Ea73b74da comment study-options_fragment_page_shown ok / E518f89ef tap text=Study failed |
| route_14 | `Models$TransformFieldDelete.<init>` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_15 | `Anki2Importer._mediaPick` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_18 | `Sched.sortCards(long[],int,int,boolean,boolean)` | failed_at_step_9 | Ea73b74da comment study-options_fragment_page_shown ok / Ec39ae90b tap desc=More_options failed |
| route_19 | `AdvancedStatistics$Card.setIvl` | failed_at_step_9 | Ea73b74da comment study-options_fragment_page_shown ok / E518f89ef tap text=Study failed |
| route_21 | `DiffEngine.diff_cleanupSemanticScore` | failed_at_step_9 | Ea73b74da comment study_options_fragment_shown ok / E518f89ef tap text=Study failed |
| route_23 | `Sched.getToday` | failed_at_step_9 | Ea73b74da comment study_options_fragment_shown_(dyn_deck_selected) ok / E57aebbea tap desc=More_options failed |
| route_24 | `DB.insert` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown,_collection_open ok / Ec0803f80 tap desc=More_options failed |
| route_29 | `Decks.id(String,boolean)` | ok | E390606b0 comment parent_deck_id_resolved ok / E5762310b comment deck_id_with_boolean_flag_reached ok |
| route_30 | `SimpleMessageDialog.<init>` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown,_collection_open ok / Ec0803f80 tap desc=More_options failed |
| route_31 | `Models.rem` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_32 | `Models$TransformFieldMove.<init>` | failed_at_step_6 | Eb3058057 comment deck-picker_page_shown ok / Ec0803f80 tap desc=More_options failed |
| route_33 | `FullSyncer.syncURL` | ok | E4ca0f18c comment request_overload_chain ok / Ec68f6b60 comment syncURL_reached_(target) ok |
| route_34 | `UIUtils$1.onPostExecute` | ok | Ea2b5de1a comment onPostExecute_forwards_to_TaskListener ok / Ebff1608e comment UIUtils_listener_reached_(target) ok |
| route_35 | `AnkiActivity.openUrl` | failed_at_step_9 | Eae5ab93a comment not-logged-in_sync-error_dialog_shown ok / E2e661eb4 tap text=Log_in failed |

### MMEX (20)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_01 | `DbModule_ProvideSqlBriteFactory.get` | failed_at_step_7 | Ed2488d54 key KEYCODE_MENU ok / Ed2488d54 tap text=Budgets failed |
| route_02 | `SplitCategoriesActivity$1.<init>` | failed_at_step_8 | E3759dc47 comment initializeInputControls_calls_initSplitCategories ok / Ee44c0eab tap res_id=splitButton failed |
| route_03 | `InvestmentTransactionEditActivity.onActivityResult` | failed_at_step_0 (setup_failed) | (no step log) |
| route_04 | `AllDataListFragment.displayRunningBalances` | failed_at_step_0 (setup_failed) | (no step log) |
| route_06 | `SplitRecurringCategoriesRepository.insert` | failed_at_step_0 (setup_failed) | (no step log) |
| route_09 | `CategoryListFragment$2.onClick` | failed_at_step_19 | E315abb2d tap text=OK ok / E315abb2d wait_for text=DeviceTestCategory failed |
| route_10 | `Core.resolveColorAttribute` | failed_at_step_0 (setup_failed) | (no step log) |
| route_12 | `IncomeVsExpensesListFragment$1.run` | failed_at_step_0 (setup_failed) | (no step log) |
| route_14 | `RecurringTransactionListActivity.onActivityResult` | failed_at_step_0 (setup_failed) | (no step log) |
| route_15 | `TutorialActivity.onOptionsItemSelected` | failed_at_step_10 | Eacaec855 key KEYCODE_MENU ok / Eacaec855 tap text=Settings failed |
| route_17 | `Authenticator.addAccount` | failed_at_step_3 | E5fc12eb9 start_intent action=android.settings.ADD_ACCOUNT_SETTINGS ok / E608059ee comment AccountManager_binds_AuthenticatorService;_framework_creates_the_service_and_calls_onCreate ok |
| route_18 | `CurrencyRepositorySql_Factory.get` | failed_at_step_0 (setup_failed) | (no step log) |
| route_20 | `AboutFragment.getLogcat` | failed_at_step_16 | Ecef22362 comment framework_calls_AboutFragment.onCreateView ok / E324d7c06 comment About_tab_page_shown ok |
| route_22 | `QueryAccountBills.setReconciled` | failed_at_step_0 (setup_failed) | (no step log) |
| route_23 | `DateRange.<init>()` | failed_at_step_0 (setup_failed) | (no step log) |
| route_25 | `AccountRepository.first` | ok | E64510675 comment loadAccount_calls_AccountRepository.load ok / Ef7590543 comment load_calls_AccountRepository.first ok |
| route_26 | `MmxContentProvider.prepareQuery` | ok | Eb152b23a comment MmxContentProvider.query_calls_query_internal_(MmxContentProvider.java:143) ok / Ec32826bf comment MmxContentProvider.query_internal_calls_prepareQuery_(MmxContentProvider.java:395) ok |
| route_27 | `MmxContentProvider.logUpdate` | ok | Ef2826f2c comment ContentResolver.update_delivered_to_MmxContentProvider.update_(RepositoryBase.java:183-190) ok / E84eb47fd comment MmxContentProvider.update_calls_logUpdate_(MmxContentProvider.java:205) ok |
| route_28 | `SyncPreferences.getUploadImmediately` | ok | Ef8378602 comment SqlRepositoryBase.notifySync_calls_SyncManager.dataChanged_(SqlRepositoryBase.java:132) ok / Ee260f9b8 comment SyncManager.dataChanged_calls_SyncPreferences.getUploadImmediately_(SyncManager.java:149) o |
| route_30 | `RecentDatabasesProvider.toJson` | ok | E2d19d91e comment RecentDatabasesProvider.add_calls_save_(RecentDatabasesProvider.java:75) ok / Ec87e03f4 comment RecentDatabasesProvider.save_calls_toJson_(RecentDatabasesProvider.java:171) ok |

### LibreTorrent (10)

| Route | Method | Script status | Last step log lines |
|---|---|---|---|
| route_15 | `FileItem.<init>(int,String,boolean,long)` | ok | E02a038f2 comment Wrap_each_file-tree_entry_for_display ok / E850d53c3 comment Direct_call ok |
| route_16 | `BencodeFileItem$1.<init>` | ok | E4ab5599c comment First_BencodeFileItem_construction_initialises_the_class_and_its_CREATOR_field ok / E86f9aa2b comment Class_initialisation_creates_the_CREATOR_anonymous_instance ok |
| route_21 | `TorrentCriticalWork.lambda$emitChangedEvent$0` | ok | E312fb53f comment Save-resume_flag_change_emits_a_state-change_event ok / E91ff5ea6 comment State-change_event_is_posted_on_the_tracker_thread_pool ok |
| route_23 | `DefaultFsModule.<init>` | ok | E4ebf1045 comment Facade_helper_constructs_the_module_resolver ok / Edf46c3a2 comment Resolver_construction_builds_the_default_module ok |
| route_24 | `SafFsModule.<init>` | ok | E4ebf1045 comment Facade_helper_constructs_the_module_resolver ok / E32956670 comment Resolver_construction_builds_the_SAF_module ok |
| route_25 | `FileSystemFacadeImpl.<init>` | ok | E554d7916 comment Direct_call ok / E67690991 comment Construct_the_concrete_filesystem_facade_on_first_access ok |
| route_26 | `MainApplication.increaseCursorWindowSize` | ok | Ec86728f9 launch component=org.proninyaroslav.libretorrent.debug/org.proninyaroslav.libretorrent.ui.main.MainActivity ok / E288f9e11 comment Increase_CursorWindow_capacity_after_ACRA_initialization ok |
| route_27 | `TorrentNotifier.makeNotifyChans` | ok | Ec86728f9 launch component=org.proninyaroslav.libretorrent.debug/org.proninyaroslav.libretorrent.ui.main.MainActivity ok / Efb33ff56 comment Create_notification_channels_during_application_startup ok |
| route_28 | `MainApplication.<init>` | ok | Edbdfd5b2 launch component=org.proninyaroslav.libretorrent.debug/org.proninyaroslav.libretorrent.ui.main.MainActivity ok |
| route_29 | `FsModuleResolverImpl.<init>` | ok | E554d7916 comment Direct_call ok / E4ebf1045 comment Facade_helper_constructs_the_module_resolver ok |

