# LibreTorrent batch 107 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 107 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. This batch includes log settings, source factory, ViewModel, and session-filter dialog methods. The source shows local lifecycle, preference, and logging operations, but complete activity/user route, paging dispatch, and dialog callback routes were not verified row by row. All remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `LogSettingsActivity.<clinit>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 2 | `LogSettingsActivity.<init>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 3 | `LogSettingsActivity.lambda$onCreate$0` | `(Landroid/view/View;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 4 | `LogSettingsActivity.onCreate` | `(Landroid/os/Bundle;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 5 | `LogSettingsFragment.<clinit>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 6 | `LogSettingsFragment.<init>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 7 | `LogSettingsFragment.bindOnPreferenceChangeListener` | `(Landroidx/preference/Preference;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 8 | `LogSettingsFragment.lambda$onCreate$0` | `([Landroid/text/InputFilter;Landroid/widget/EditText;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 9 | `LogSettingsFragment.onCreate` | `(Landroid/os/Bundle;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 10 | `LogSettingsFragment.onCreatePreferences` | `(Landroid/os/Bundle;Ljava/lang/String;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 11 | `LogSettingsFragment.onPreferenceChange` | `(Landroidx/preference/Preference;Ljava/lang/Object;)Z` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 12 | `LogSourceFactory.<init>` | `(Lorg/proninyaroslav/libretorrent/core/logger/Logger;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 13 | `LogSourceFactory.create` | `()Landroidx/paging/DataSource;` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 14 | `LogViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 15 | `LogViewModel.copyLogEntryToClipboard` | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 16 | `LogViewModel.getLogEntriesCount` | `()I` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 17 | `LogViewModel.getSaveLogFileName` | `()Ljava/lang/String;` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 18 | `LogViewModel.initMutableParams` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 19 | `LogViewModel.logPausedManually` | `()Z` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 20 | `LogViewModel.logRecording` | `()Z` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 21 | `LogViewModel.observeLog` | `()Landroidx/lifecycle/LiveData;` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 22 | `LogViewModel.onCleared` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 23 | `LogViewModel.pauseLog` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 24 | `LogViewModel.pauseLogManually` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 25 | `LogViewModel.resumeLog` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 26 | `LogViewModel.resumeLogManually` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 27 | `LogViewModel.saveLog` | `(Landroid/net/Uri;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 28 | `LogViewModel.startLogRecording` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 29 | `LogViewModel.stopLogRecording` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 30 | `LogViewModel$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/log/LogViewModel;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 31 | `LogViewModel$1.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 32 | `SessionLogFilterDialog.<clinit>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 33 | `SessionLogFilterDialog.<init>` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 34 | `SessionLogFilterDialog.initLayoutView` | `(Landroid/view/View;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 35 | `SessionLogFilterDialog.lambda$initLayoutView$1` | `(Landroid/content/DialogInterface;I)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 36 | `SessionLogFilterDialog.lambda$onResume$0` | `(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 37 | `SessionLogFilterDialog.newInstance` | `()Lorg/proninyaroslav/libretorrent/ui/log/SessionLogFilterDialog;` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 38 | `SessionLogFilterDialog.onAttach` | `(Landroid/content/Context;)V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 39 | `SessionLogFilterDialog.onBackPressed` | `()V` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |
| 40 | `SessionLogFilterDialog.onCreateDialog` | `(Landroid/os/Bundle;)Landroid/app/Dialog;` | OPEN | Settings/ViewModel/dialog source is present; complete user entry and framework/library callback routes were not audited for every target. |

## Evidence
- `LogSettingsActivity.java:30-40`; `LogSettingsFragment.java:36-89`: settings activity/fragment and preference listeners.
- `LogSourceFactory.java:28-39`: factory class/create method.
- `LogViewModel.java:50-215`: observer, lifecycle, pause/resume, logging, save and clipboard helpers.
- `SessionLogFilterDialog.java:40-116`: fragment factory/lifecycle, dialog setup, and back action.

