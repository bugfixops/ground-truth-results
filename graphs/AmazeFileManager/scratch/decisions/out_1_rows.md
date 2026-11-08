| method | verdict | edges or kind | source file:lines | confirmed_by |
|---|---|---|---|---|
| ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected | REACHABLE | ProcessViewerFragment.onResume -FRAMEWORK-> ...onServiceDisconnected | fragments/ProcessViewerFragment.java:158-159,390-433 | SOURCE |
| PropertiesSheet.<init> | UNREACHABLE | no_trigger_in_app | ui/ItemPopupMenu.java:70-77 | SOURCE |
| PropertiesSheet.generate | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:112-115 | SOURCE |
| PropertiesSheet.setupDialog | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:50-106 | SOURCE |
| PropertiesSheet$1.<init> | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:86-95 | SOURCE |
| PropertiesSheet$1.onScrollChange | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:87-94 | SOURCE |
| PropertiesSheet$2.<init> | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:117-129 | SOURCE |
| PropertiesSheet$2.onSlide | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:82,125-128 | SOURCE |
| PropertiesSheet$2.onStateChanged | UNREACHABLE | no_trigger_in_app | fragments/PropertiesSheet.java:82,118-123 | SOURCE |
| TabFragment$ScreenSlidePagerAdapter.getCount | REACHABLE | TabFragment.onCreateView -FRAMEWORK-> ...getCount | fragments/TabFragment.java:145,319-332 | SOURCE |
| TabFragment$ScreenSlidePagerAdapter.getItem | REACHABLE | TabFragment.onCreateView -FRAMEWORK-> ...getItem | fragments/TabFragment.java:145,338-343 | SOURCE |
| TabFragment$ScreenSlidePagerAdapter.getItemPosition | REACHABLE | TabFragment.onCreateView -FRAMEWORK-> ...getItemPosition | fragments/TabFragment.java:175,320-327 | SOURCE |
| ColorPref.onPause | REACHABLE | ColorPref.<init> -LIFECYCLE-> ColorPref.onPause | fragments/preference_fragments/ColorPref.java:68-71 | SOURCE |
| ColorPref.onSaveInstanceState | REACHABLE | ColorPref.<init> -LIFECYCLE-> ColorPref.onSaveInstanceState | fragments/preference_fragments/ColorPref.java:295-299 | SOURCE |
| ColorPref$1.onNeutral | REACHABLE | ColorPref.colorChangeDialog -FRAMEWORK-> ColorPref$1.onNeutral | fragments/preference_fragments/ColorPref.java:171-187 | SOURCE |
| QuickAccessPref.onCreate | REACHABLE | PreferencesActivity.selectItem -LIFECYCLE-> QuickAccessPref.onCreate | activities/PreferencesActivity.java:264,272-278 | SOURCE |
| QuickAccessPref.onPreferenceClick | REACHABLE | QuickAccessPref.onCreate -FRAMEWORK-> QuickAccessPref.onPreferenceClick | fragments/preference_fragments/QuickAccessPref.java:52-54 | SOURCE |
| UserColorPreferences.<init>(Parcel) | UNREACHABLE | no_trigger_in_app | ui/colors/UserColorPreferences.java:19-24; ui/colors/ColorPreferenceHelper.java:70-79 | SOURCE |
| UserColorPreferences.describeContents | UNREACHABLE | no_trigger_in_app | ui/colors/UserColorPreferences.java:34-37; ui/colors/ColorPreferenceHelper.java:70-79 | SOURCE |
| UserColorPreferences.writeToParcel | UNREACHABLE | no_trigger_in_app | ui/colors/UserColorPreferences.java:26-32; ui/colors/ColorPreferenceHelper.java:70-79 | SOURCE |
| ColorPickerDialog.<init> | REACHABLE | ColorPref.loadSection1 -FRAMEWORK-> ColorPickerDialog.<init> | fragments/preference_fragments/ColorPref.java:219; res/xml/conficolor_prefs.xml:3-5 | SOURCE |
| RenameBookmark$1.afterTextChanged | REACHABLE | RenameBookmark.onCreateDialog -FRAMEWORK-> RenameBookmark$1.afterTextChanged | ui/dialogs/RenameBookmark.java:86-93 | SOURCE |
| RenameBookmark$2.afterTextChanged | REACHABLE | RenameBookmark.onCreateDialog -FRAMEWORK-> RenameBookmark$2.afterTextChanged | ui/dialogs/RenameBookmark.java:112-119 | SOURCE |
| SftpConnectDialog$1.afterTextChanged | REACHABLE | SftpConnectDialog.onCreateDialog -FRAMEWORK-> SftpConnectDialog$1.afterTextChanged | ui/dialogs/SftpConnectDialog.java:266-294 | SOURCE |
| SmbConnectDialog$1.afterTextChanged | REACHABLE | SmbConnectDialog.onCreateDialog -FRAMEWORK-> SmbConnectDialog$1.afterTextChanged | ui/dialogs/SmbConnectDialog.java:116-122 | SOURCE |
| SmbConnectDialog$2.afterTextChanged | REACHABLE | SmbConnectDialog.onCreateDialog -FRAMEWORK-> SmbConnectDialog$2.afterTextChanged | ui/dialogs/SmbConnectDialog.java:124-131 | SOURCE |
| SmbConnectDialog$3.afterTextChanged | REACHABLE | SmbConnectDialog.onCreateDialog -FRAMEWORK-> SmbConnectDialog$3.afterTextChanged | ui/dialogs/SmbConnectDialog.java:132-139 | SOURCE |
| SmbConnectDialog$4.afterTextChanged | REACHABLE | SmbConnectDialog.onCreateDialog -FRAMEWORK-> SmbConnectDialog$4.afterTextChanged | ui/dialogs/SmbConnectDialog.java:140-147 | SOURCE |
| CircularColorsView.<init>(Context) | UNREACHABLE | no_trigger_in_app | ui/views/CircularColorsView.java:28-31 | SOURCE |
| CircularColorsView.<init>(Context,AttributeSet) | REACHABLE | ColorPickerDialog.inflateItem -FRAMEWORK-> CircularColorsView.<init>(Context,AttributeSet) | ui/dialogs/ColorPickerDialog.java:178-179; res/layout/item_colorpicker.xml:28-34 | SOURCE |
| CircularColorsView.init | REACHABLE | CircularColorsView.<init>(Context,AttributeSet) -CALL-> CircularColorsView.init | ui/views/CircularColorsView.java:34-37 | SOURCE |
| DisablableViewPager.<init> | REACHABLE | TabFragment.onCreateView -FRAMEWORK-> DisablableViewPager.<init> | fragments/TabFragment.java:80; res/layout/tabfragment.xml:20-24 | SOURCE |
| DisablableViewPager.onInterceptTouchEvent | REACHABLE | DisablableViewPager.<init> -FRAMEWORK-> onInterceptTouchEvent | ui/views/DisablableViewPager.java:25-29 | SOURCE |
| DisablableViewPager.onTouchEvent | REACHABLE | DisablableViewPager.<init> -FRAMEWORK-> onTouchEvent | ui/views/DisablableViewPager.java:20-23 | SOURCE |
| FastScroller.<init>(Context,AttributeSet) | REACHABLE | MainFragment.onCreateView -FRAMEWORK-> FastScroller.<init>(Context,AttributeSet) | fragments/MainFragment.java:238; res/layout/main_frag.xml:46-50 | SOURCE |
| FastScroller.<init>(Context,AttributeSet,int) | UNREACHABLE | no_trigger_in_app | ui/views/FastScroller.java:45-49; res/layout/main_frag.xml:46-50 | SOURCE |
| FastScroller.getRelativeTouchPosition | REACHABLE | FastScroller.onTouchEvent -CALL-> getRelativeTouchPosition | ui/views/FastScroller.java:105 | SOURCE |
| FastScroller.onTouchEvent | REACHABLE | FastScroller.<init>(Context,AttributeSet) -FRAMEWORK-> onTouchEvent | ui/views/FastScroller.java:101-121 | SOURCE |
| FastScroller.setRecyclerViewPosition | REACHABLE | FastScroller.onTouchEvent -CALL-> setRecyclerViewPosition | ui/views/FastScroller.java:108 | SOURCE |
| Indicator.<init>(Context) | UNREACHABLE | no_trigger_in_app | ui/views/Indicator.java:115-117; res/layout-v21/main_toolbar.xml:50-55 | SOURCE |
