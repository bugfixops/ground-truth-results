# AnkiDroid batch 075 (LABEL helper). SeekBarPreference (10 methods) and SlidingTabLayout with its inner classes
# InternalViewPagerListener (4) and TabClickListener (2): 29 methods in total. The full row list is in
# graphs/AnkiDroid/parts/label_075.md.
#
# Route ownership:
# - Automatic CALL edges (the SlidingTabLayout constructor chain, setViewPager to populateTabStrip, the listener
#   constructors, scrollToTab, createDefaultTabView) come from the builder and are not written here.
# - Page edges from S_PREFERENCES, S_CARDTEMPLATEEDITOR and S_STATISTICS into methods of this batch are written here,
#   because the destination is in the batch.
# - One edge with a source in this batch: SeekBarPreference.onStopTrackingTouch -> Preferences$SettingsFragment.onSharedPreferenceChanged.
# - Gates: STATE_COLLECTION (the dayOffset row is enabled only with an open collection; the tabs exist only after
#   onCollectionLoaded); STATE_SETTINGS (a later open, after dayOffset has been stored). No MG ids are needed here.
# - The support ViewPager is not in the dataset, so the pager dispatch edges are INFERRED (source not read).

# --- SeekBarPreference: page edges and the persist edge.
e('S_PREFERENCES', 'SeekBarPreference.<init>', 'FRAMEWORK',
  'Opening the reviewing settings screen inflates the day-offset SeekBarPreference.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:34-43; SRC res/xml/preferences_reviewing.xml:36-39; FW-SRC core/java/android/preference/GenericInflater.java:376-385',
  note='Inflated when the reviewing subscreen is built (Preferences.java:242-243, 788). No gate: the screen opens without a collection.')

e('S_PREFERENCES', 'SeekBarPreference.onBindDialogView', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the dialog binder after the view is built.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:80-84; FW-SRC core/java/android/preference/DialogPreference.java:287-300; FW-SRC core/java/android/preference/Preference.java:1129-1135',
  note='Gate: the row is disabled when the collection is closed (Preferences.java:434-436), and Preference.performClick returns early when disabled (Preference.java:1131-1132).')

e('S_PREFERENCES', 'SeekBarPreference.onCreateDialogView', 'GUI',
  'Tap on the day-offset row opens the dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap on the day-offset row opens the dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:47-76; FW-SRC core/java/android/preference/PreferenceScreen.java:240-249',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onPrepareDialogBuilder', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the builder hook on the same tap.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:135-140; FW-SRC core/java/android/preference/DialogPreference.java:287-306',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onProgressChanged', 'GUI',
  'Drag the thumb or tap the bar in the open dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Drag the thumb or tap the bar in the open dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:99-105; FW-SRC core/java/android/widget/SeekBar.java:91-96',
  note='Gate: open collection (the dialog exists only on an enabled row). The fromTouch branch (lines 100-104) is taken.')

e('S_PREFERENCES', 'SeekBarPreference.onSetInitialValue', 'FRAMEWORK',
  'A later open of the screen, after dayOffset has been stored; the restore branch runs.',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:88-96, 116-119; FW-SRC core/java/android/preference/Preference.java:1547-1561',
  note='Gate: STATE_SETTINGS (dayOffset must have been stored by a prior setValue, which needs the collection: Preferences.java:400-402, 424-428).')

e('S_PREFERENCES', 'SeekBarPreference.onStartTrackingTouch', 'GUI',
  'Press the thumb of the open dialog SeekBar.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Press the thumb of the open dialog SeekBar.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:121-122; FW-SRC core/java/android/widget/SeekBar.java:112-117',
  note='Gate: open collection (see onBindDialogView). The body is empty.')

e('S_PREFERENCES', 'SeekBarPreference.onStopTrackingTouch', 'GUI',
  'Lift the finger after a drag; the dialog closes.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Lift the finger after a drag; the dialog closes.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; FW-SRC core/java/android/widget/SeekBar.java:119-125',
  note='Gate: open collection (see onBindDialogView). The body persists the value and dismisses the dialog (lines 127-130).')

e('SeekBarPreference.onStopTrackingTouch', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'FRAMEWORK',
  'persistInt commits the new value to SharedPreferences, which notifies the listener registered in SettingsFragment.onResume.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; SRC com/ichi2/anki/Preferences.java:796, 811-812; FW-SRC core/java/android/preference/Preference.java:1716-1735, 1587-1595; FW-SRC core/java/android/app/SharedPreferencesImpl.java:547, 551-563',
  note='The notify is skipped when the stored value is unchanged (Preference.java:1721-1724). No gate beyond the open dialog.')

# --- SlidingTabLayout: page edges (card template editor and statistics) into the batch methods.
e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the card template editor inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/card_template_editor_activity.xml:21-24; SRC com/ichi2/anki/CardTemplateEditor.java:127-130; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 130) runs before the collection loads.')

e('S_STATISTICS', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the statistics screen inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/activity_anki_stats.xml:18-21; SRC com/ichi2/anki/Statistics.java:84-88; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 86) runs before the collection loads.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the card template editor layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_STATISTICS', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the statistics layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title in the card template editor.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title in the card template editor.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 232).')

e('S_STATISTICS', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title on the statistics screen.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title on the statistics screen.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/Statistics.java:92, 125-126',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 126).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another template page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another template page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another statistics page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another statistics page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

# --- UNREACHABLE: no trigger in the app (every call site was grepped over src/main/java).
UNREACHABLE['SlidingTabLayout.<init>(Context)'] = ('no_trigger_in_app',
    'No new SlidingTabLayout(...) with one argument exists in the source root (grep finds no call site). LayoutInflater builds XML views with the (Context, AttributeSet) constructor only, so the one-argument form has no trigger.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:83-85; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabColorizer'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setCustomTabColorizer, a different method on a different class.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:112-114; SRC com/ichi2/ui/SlidingTabStrip.java:90-93',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabView'] = ('no_trigger_in_app',
    'No call site in the source root. Without it mTabViewLayoutId stays 0, so the custom-view branch is never taken and createDefaultTabView is always used.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:149-152, 207-212',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setDividerColors'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setDividerColors, a different method; the SlidingTabStrip calls at lines 75 and 105 are made inside SlidingTabStrip itself.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:128-130; SRC com/ichi2/ui/SlidingTabStrip.java:73-76, 102-106',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setOnPageChangeListener'] = ('no_trigger_in_app',
    'No call site in the source root, so mViewPagerPageChangeListener stays null and the forwarding branches in InternalViewPagerListener are never taken.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:139-141, 275-278, 285-287, 297-299',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setSelectedIndicatorColors'] = ('no_trigger_in_app',
    'No call site in the source root. The only other match is SlidingTabStrip.setSelectedIndicatorColors, a different method.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:120-122; SRC com/ichi2/ui/SlidingTabStrip.java:95-100',
    'SOURCE')
