STATUS: START 21:36

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| PasteHelper$1.createFromParcel | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework when unparceling | FW-SRC Parcel.java:2993; SRC PasteHelper.java:45-47 |
| PasteHelper$1.newArray | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework | FW-SRC Parcel.java:3032; SRC PasteHelper.java:49-51 |
| CoderBase.encode | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to CoderBase in app source |
| CoderBase.getOptionsAsProperties | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to CoderBase in app source |
| DeltaDecoder.encode | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to DeltaDecoder in app source |
| DeltaDecoder.getOptionsAsProperties | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to DeltaDecoder in app source |
| LZMA2Decoder.encode | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to LZMA2Decoder in app source |
| LZMA2Decoder.getOptions | UNREACHABLE | framework_never_calls | Apache Commons Compress library class (sevenz codec); no app references | INFERRED; grep found no references to LZMA2Decoder in app source |
| MainFragment$7.lambda$run$0 | REACHABLE | ASYNC | Lambda called from runOnUiThread inside Thread.run | SRC MainFragment.java:1670 activity.runOnUiThread(() -> ...) |
| MainFragment$7.run | REACHABLE | ASYNC | Thread.run override; called by framework when thread starts | SRC MainFragment.java:1658-1677; FW-SRC Thread.java:764 |
| ProcessViewerFragment$CustomServiceConnection$1.<init> | REACHABLE | CALL | Constructor of anonymous ProgressListener | SRC ProcessViewerFragment.java:413-424 new ProgressListener() |
| ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0 | REACHABLE | ASYNC | Lambda called from runOnUiThread inside onUpdate | SRC ProcessViewerFragment.java:421 runOnUiThread(() -> ...) |
| PropertiesSheet$1.<init> | REACHABLE | CALL | Constructor of anonymous OnScrollChangeListener | SRC PropertiesSheet.java:88-96 new OnScrollChangeListener() |
| PropertiesSheet$1.onScrollChange | REACHABLE | GUI | OnScrollChangeListener callback; dispatched by NestedScrollView | SRC PropertiesSheet.java:90-95; FW-SRC NestedScrollView.java |
| ColorPref$1.<init> | REACHABLE | CALL | Constructor of anonymous MaterialDialog.ButtonCallback | SRC ColorPref.java:177-184 .callback(new ButtonCallback()) |
| ColorPref$1.onNeutral | REACHABLE | GUI | MaterialDialog button callback; called when neutral button clicked | SRC ColorPref.java:179-184; MaterialDialog library |
| QuickAccessPref.onCreate | REACHABLE | LIFECYCLE | PreferenceFragment lifecycle method | SRC QuickAccessPref.java:40-53; FW-SRC PreferenceFragment |
| QuickAccessPref.onPreferenceClick | REACHABLE | GUI | Preference click listener; registered at line 51 | SRC QuickAccessPref.java:56-60, 51; FW-SRC Preference.java |
| UserColorPreferences$1.createFromParcel | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework | FW-SRC Parcel.java:2993; SRC UserColorPreferences.java:36-40 |
| UserColorPreferences$1.newArray | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework | FW-SRC Parcel.java:3032; SRC UserColorPreferences.java:42-46 |
| RenameBookmark$1.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC RenameBookmark.java:63-69 new SimpleTextWatcher() |
| RenameBookmark$1.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC RenameBookmark.java:65-69; FW-SRC TextView.java |
| RenameBookmark$2.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC RenameBookmark.java:85-90 new SimpleTextWatcher() |
| RenameBookmark$2.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC RenameBookmark.java:87-90; FW-SRC TextView.java |
| SftpConnectDialog$1.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher validator | SRC SftpConnectDialog.java:246-265 new SimpleTextWatcher() |
| SftpConnectDialog$1.afterTextChanged | REACHABLE | GUI | TextWatcher callback; registered at lines 267-270 | SRC SftpConnectDialog.java:248-265; FW-SRC TextView.java |
| SmbConnectDialog$1.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC SmbConnectDialog.java:70-77 new SimpleTextWatcher() |
| SmbConnectDialog$1.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC SmbConnectDialog.java:72-77; FW-SRC TextView.java |
| SmbConnectDialog$2.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC SmbConnectDialog.java:79-86 new SimpleTextWatcher() |
| SmbConnectDialog$2.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC SmbConnectDialog.java:81-86; FW-SRC TextView.java |
| SmbConnectDialog$3.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC SmbConnectDialog.java:88-95 new SimpleTextWatcher() |
| SmbConnectDialog$3.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC SmbConnectDialog.java:90-95; FW-SRC TextView.java |
| SmbConnectDialog$4.<init> | REACHABLE | CALL | Constructor of anonymous SimpleTextWatcher | SRC SmbConnectDialog.java:97-104 new SimpleTextWatcher() |
| SmbConnectDialog$4.afterTextChanged | REACHABLE | GUI | TextWatcher callback; dispatched by EditText | SRC SmbConnectDialog.java:99-104; FW-SRC TextView.java |
| MimeTypes.<init> | REACHABLE | CALL | Constructor called when static methods accessed | SRC MimeTypes.java:117-133 static initialization |
| MimeTypes.mimeTypeMatch | REACHABLE | CALL | Public static method called from app code | SRC MimeTypes.java:136-138 |
| Indicator$PendingRetreatAnimator.lambda$new$0 | REACHABLE | GUI | Lambda for ValueAnimator update listener (rightward retreat) | SRC Indicator.java:728-734 addUpdateListener |
| Indicator$PendingRetreatAnimator.lambda$new$1 | REACHABLE | GUI | Lambda for ValueAnimator update listener (leftward retreat) | SRC Indicator.java:746-752 addUpdateListener |
| DatapointParcelable$1.createFromParcel | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework | FW-SRC Parcel.java:2993; SRC DatapointParcelable.java:136-141 |
| DatapointParcelable$1.newArray | REACHABLE | FRAMEWORK | Parcelable.Creator method called by framework | FW-SRC Parcel.java:3032; SRC DatapointParcelable.java:143-147 |

STATUS: DONE 21:40
