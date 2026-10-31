# Repair part 21: labels for batch rp_21

# PasteHelper$1.createFromParcel and PasteHelper$1.newArray
# These are Parcelable.Creator methods - framework calls them when unparceling
e('E_rp21_001', 'S_PARCEL_read', 'PasteHelper$1.createFromParcel', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:2993 calls Creator.createFromParcel; PasteHelper.java:45-47', '', 'standard')
e('E_rp21_002', 'S_PARCEL_read', 'PasteHelper$1.newArray', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:3032 calls Creator.newArray; PasteHelper.java:49-51', '', 'standard')

# CoderBase, DeltaDecoder, LZMA2Decoder - Apache Commons Compress sevenz library classes
# No app references found
UNREACHABLE['CoderBase.encode'] = ('framework_never_calls', 'Apache Commons Compress library class CoderBase (sevenz codec); grep found no app references to CoderBase', 'INFERRED', 'INFERRED')
UNREACHABLE['CoderBase.getOptionsAsProperties'] = ('framework_never_calls', 'Apache Commons Compress library class CoderBase (sevenz codec); grep found no app references to CoderBase', 'INFERRED', 'INFERRED')
UNREACHABLE['DeltaDecoder.encode'] = ('framework_never_calls', 'Apache Commons Compress library class DeltaDecoder (sevenz codec); grep found no app references to DeltaDecoder', 'INFERRED', 'INFERRED')
UNREACHABLE['DeltaDecoder.getOptionsAsProperties'] = ('framework_never_calls', 'Apache Commons Compress library class DeltaDecoder (sevenz codec); grep found no app references to DeltaDecoder', 'INFERRED', 'INFERRED')
UNREACHABLE['LZMA2Decoder.encode'] = ('framework_never_calls', 'Apache Commons Compress library class LZMA2Decoder (sevenz codec); grep found no app references to LZMA2Decoder', 'INFERRED', 'INFERRED')
UNREACHABLE['LZMA2Decoder.getOptions'] = ('framework_never_calls', 'Apache Commons Compress library class LZMA2Decoder (sevenz codec); grep found no app references to LZMA2Decoder', 'INFERRED', 'INFERRED')

# MainFragment$7 - anonymous Thread created in launchSMB
# MainFragment$7.run is called by Thread.start, MainFragment$7.lambda$run$0 is called from runOnUiThread lambda
e('E_rp21_003', 'MainFragment.launchSMB', 'MainFragment$7.<init>', 'CALL', False, False, '', 'SRC MainFragment.java:1658 new Thread() { public void run() ...', '', 'explicit')
e('E_rp21_004', 'MainFragment$7.<init>', 'Thread.<init>', 'CALL', False, False, '', 'SRC MainFragment.java:1658 extends Thread implicitly', '', 'explicit')
e('E_rp21_005', 'S_THREAD_run', 'MainFragment$7.run', 'ASYNC', False, False, '', 'SRC MainFragment.java:1658-1677 Thread.run override; FW-SRC Thread.java:764 calls run()', '', 'standard')
e('E_rp21_006', 'MainFragment$7.run', 'MainFragment$7.lambda$run$0', 'ASYNC', False, False, '', 'SRC MainFragment.java:1670 activity.runOnUiThread(() -> { ... }); lambda body', '', 'explicit')

# ProcessViewerFragment$CustomServiceConnection$1 - anonymous ProgressListener
# Created in CustomServiceConnection.onServiceConnected
e('E_rp21_007', 'ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ProcessViewerFragment$CustomServiceConnection$1.<init>', 'CALL', False, False, '', 'SRC ProcessViewerFragment.java:413-424 new AbstractProgressiveService.ProgressListener() { ... }', '', 'explicit')
e('E_rp21_008', 'ProcessViewerFragment$CustomServiceConnection$1.<init>', 'AbstractProgressiveService$ProgressListener.<init>', 'CALL', False, False, '', 'SRC ProcessViewerFragment.java:413 extends ProgressListener implicitly', '', 'explicit')
e('E_rp21_009', 'ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'ProcessViewerFragment.processResults', 'CALL', False, False, '', 'SRC ProcessViewerFragment.java:421 fragment.processResults(dataPackage, serviceType) inside lambda', '', 'explicit')
# The onUpdate callback is called by AbstractProgressiveService when progress updates
e('E_rp21_010', 'AbstractProgressiveService.progressUpdate', 'ProcessViewerFragment$CustomServiceConnection$1.onUpdate', 'CALL', False, False, '', 'INFERRED AbstractProgressiveService calls ProgressListener.onUpdate when progress changes', '', 'explicit')
e('E_rp21_011', 'ProcessViewerFragment$CustomServiceConnection$1.onUpdate', 'ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'ASYNC', False, False, '', 'SRC ProcessViewerFragment.java:421 fragment.getActivity().runOnUiThread(() -> ...); lambda body', '', 'explicit')

# PropertiesSheet$1 - anonymous OnScrollChangeListener
e('E_rp21_012', 'PropertiesSheet.setupDialog', 'PropertiesSheet$1.<init>', 'CALL', False, False, '', 'SRC PropertiesSheet.java:88-96 mNestedScrollView.setOnScrollChangeListener(new NestedScrollView.OnScrollChangeListener() { ... })', '', 'explicit')
e('E_rp21_013', 'PropertiesSheet$1.<init>', 'NestedScrollView$OnScrollChangeListener.<init>', 'CALL', False, False, '', 'SRC PropertiesSheet.java:88 implements OnScrollChangeListener implicitly', '', 'explicit')
e('E_rp21_014', 'S_NESTED_SCROLL', 'PropertiesSheet$1.onScrollChange', 'GUI', False, False, '', 'SRC PropertiesSheet.java:90-95 onScrollChange override; FW-SRC NestedScrollView.java dispatches onScrollChange', '', 'standard')

# ColorPref$1 - anonymous MaterialDialog.ButtonCallback
e('E_rp21_015', 'ColorPref.colorChangeDialog', 'ColorPref$1.<init>', 'CALL', False, False, '', 'SRC ColorPref.java:177-184 .callback(new MaterialDialog.ButtonCallback() { ... })', '', 'explicit')
e('E_rp21_016', 'ColorPref$1.<init>', 'MaterialDialog$ButtonCallback.<init>', 'CALL', False, False, '', 'SRC ColorPref.java:177 extends ButtonCallback implicitly', '', 'explicit')
e('E_rp21_017', 'MaterialDialog.onNeutralClick', 'ColorPref$1.onNeutral', 'GUI', False, False, '', 'SRC ColorPref.java:179-184 onNeutral override; MaterialDialog library calls onNeutral when neutral button clicked', '', 'explicit')

# QuickAccessPref.onCreate and QuickAccessPref.onPreferenceClick
e('E_rp21_018', 'S_PREF_FRAGMENT_create', 'QuickAccessPref.onCreate', 'LIFECYCLE', False, False, '', 'SRC QuickAccessPref.java:40-53 onCreate override; FW-SRC PreferenceFragment lifecycle', '', 'standard')
e('E_rp21_019', 'S_PREFERENCE_click', 'QuickAccessPref.onPreferenceClick', 'GUI', False, False, '', 'SRC QuickAccessPref.java:56-60 onPreferenceClick override; registered at line 51; FW-SRC Preference.java calls listener', '', 'standard')

# UserColorPreferences$1 - Parcelable.Creator
e('E_rp21_020', 'S_PARCEL_read', 'UserColorPreferences$1.createFromParcel', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:2993 calls Creator.createFromParcel; UserColorPreferences.java:36-40', '', 'standard')
e('E_rp21_021', 'S_PARCEL_read', 'UserColorPreferences$1.newArray', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:3032 calls Creator.newArray; UserColorPreferences.java:42-46', '', 'standard')

# RenameBookmark$1 and RenameBookmark$2 - anonymous SimpleTextWatcher instances
e('E_rp21_022', 'RenameBookmark.onCreateDialog', 'RenameBookmark$1.<init>', 'CALL', False, False, '', 'SRC RenameBookmark.java:63-69 conName.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_023', 'RenameBookmark$1.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC RenameBookmark.java:63 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_024', 'S_EDITTEXT_watch', 'RenameBookmark$1.afterTextChanged', 'GUI', False, False, '', 'SRC RenameBookmark.java:65-69 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')
e('E_rp21_025', 'RenameBookmark.onCreateDialog', 'RenameBookmark$2.<init>', 'CALL', False, False, '', 'SRC RenameBookmark.java:85-90 ip.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_026', 'RenameBookmark$2.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC RenameBookmark.java:85 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_027', 'S_EDITTEXT_watch', 'RenameBookmark$2.afterTextChanged', 'GUI', False, False, '', 'SRC RenameBookmark.java:87-90 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

# SftpConnectDialog$1 - anonymous SimpleTextWatcher (validator)
e('E_rp21_028', 'SftpConnectDialog.onCreateDialog', 'SftpConnectDialog$1.<init>', 'CALL', False, False, '', 'SRC SftpConnectDialog.java:246-265 TextWatcher validator = new SimpleTextWatcher() { ... }', '', 'explicit')
e('E_rp21_029', 'SftpConnectDialog$1.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC SftpConnectDialog.java:246 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_030', 'S_EDITTEXT_watch', 'SftpConnectDialog$1.afterTextChanged', 'GUI', False, False, '', 'SRC SftpConnectDialog.java:248-265 afterTextChanged override; registered at lines 267-270; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

# SmbConnectDialog$1, $2, $3, $4 - anonymous SimpleTextWatcher instances
e('E_rp21_031', 'SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$1.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:70-77 conName.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_032', 'SmbConnectDialog$1.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:70 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_033', 'S_EDITTEXT_watch', 'SmbConnectDialog$1.afterTextChanged', 'GUI', False, False, '', 'SRC SmbConnectDialog.java:72-77 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

e('E_rp21_034', 'SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$2.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:79-86 ip.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_035', 'SmbConnectDialog$2.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:79 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_036', 'S_EDITTEXT_watch', 'SmbConnectDialog$2.afterTextChanged', 'GUI', False, False, '', 'SRC SmbConnectDialog.java:81-86 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

e('E_rp21_037', 'SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$3.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:88-95 domain.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_038', 'SmbConnectDialog$3.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:88 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_039', 'S_EDITTEXT_watch', 'SmbConnectDialog$3.afterTextChanged', 'GUI', False, False, '', 'SRC SmbConnectDialog.java:90-95 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

e('E_rp21_040', 'SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$4.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:97-104 user.addTextChangedListener(new SimpleTextWatcher() { ... })', '', 'explicit')
e('E_rp21_041', 'SmbConnectDialog$4.<init>', 'SimpleTextWatcher.<init>', 'CALL', False, False, '', 'SRC SmbConnectDialog.java:97 extends SimpleTextWatcher implicitly', '', 'explicit')
e('E_rp21_042', 'S_EDITTEXT_watch', 'SmbConnectDialog$4.afterTextChanged', 'GUI', False, False, '', 'SRC SmbConnectDialog.java:99-104 afterTextChanged override; FW-SRC TextView.java dispatches TextWatcher callbacks', '', 'standard')

# MimeTypes.<init> and MimeTypes.mimeTypeMatch
e('E_rp21_043', 'MimeTypes.getMimeType', 'MimeTypes.<init>', 'CALL', False, False, '', 'SRC MimeTypes.java:117-133 constructor called when class methods accessed; static MIME_TYPES map initialized', '', 'explicit')
e('E_rp21_044', 'MimeTypes.getMimeType', 'MimeTypes.mimeTypeMatch', 'CALL', False, False, '', 'SRC MimeTypes.java:136-138 public static method called from app code', '', 'explicit')

# Indicator$PendingRetreatAnimator.lambda$new$0 and lambda$new$1
# These are lambdas inside PendingRetreatAnimator constructor
e('E_rp21_045', 'Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator.lambda$new$0', 'GUI', False, False, '', 'SRC Indicator.java:728-734 addUpdateListener lambda for rightward retreat; ValueAnimator dispatches update listener', '', 'explicit')
e('E_rp21_046', 'Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator.lambda$new$1', 'GUI', False, False, '', 'SRC Indicator.java:746-752 addUpdateListener lambda for leftward retreat; ValueAnimator dispatches update listener', '', 'explicit')

# DatapointParcelable$1 - Parcelable.Creator
e('E_rp21_047', 'S_PARCEL_read', 'DatapointParcelable$1.createFromParcel', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:2993 calls Creator.createFromParcel; DatapointParcelable.java:136-141', '', 'standard')
e('E_rp21_048', 'S_PARCEL_read', 'DatapointParcelable$1.newArray', 'FRAMEWORK', False, False, '', 'FW-SRC Parcel.java:3032 calls Creator.newArray; DatapointParcelable.java:143-147', '', 'standard')
