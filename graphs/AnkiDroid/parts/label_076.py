e('S_STATISTICS', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the statistics screen draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:86, 125-126; res/layout/activity_anki_stats.xml:18-21 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the statistics screen is shown.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the card template editor draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:130, 231-232; res/layout/card_template_editor_activity.xml:21-24 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the card template editor is shown.')

UNREACHABLE['SlidingTabStrip.blendColors'] = ('branch_never_taken',
  'The only call is at SlidingTabStrip.java:134, inside the branch where color != nextColor (line 133). Both colours come from the same colorizer, and its indicator array has one element: it is set once at line 74 to DEFAULT_SELECTED_INDICATOR_COLOR (line 33). getIndicatorColor returns mIndicatorColors[position % length] (lines 190-192), so nextColor always equals color. mCustomTabColorizer becomes non-null only at line 91, in setCustomTabColorizer, which has no caller. The other writer of the indicator array, setSelectedIndicatorColors, has no caller either.',
  'com/ichi2/ui/SlidingTabStrip.java:33, 74, 90-98, 129-134, 190-192; com/ichi2/ui/SlidingTabLayout.java:112-114, 120-122 (no callers)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setCustomTabColorizer'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setCustomTabColorizer (SlidingTabLayout.java:113). That public method has no caller in the source root: its definition is at line 112, and its own javadoc (lines 105-111) is text, not a call. The layout files name the view only (activity_anki_stats.xml:18-21; card_template_editor_activity.xml:21-24).',
  'com/ichi2/ui/SlidingTabStrip.java:90-93; com/ichi2/ui/SlidingTabLayout.java:105-114; res/layout/activity_anki_stats.xml:18-21 (src/main); res/layout/card_template_editor_activity.xml:21-24 (src/main)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setDividerColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setDividerColors (SlidingTabLayout.java:129), which has no caller in the source root: its definition is at line 128, and a link to it at line 109 is javadoc text, not a call.',
  'com/ichi2/ui/SlidingTabStrip.java:102-107; com/ichi2/ui/SlidingTabLayout.java:109, 128-130',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setSelectedIndicatorColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setSelectedIndicatorColors (SlidingTabLayout.java:121), which has no caller in the source root: its definition is at line 120, and its own javadoc (lines 116-119) and a link at line 109 are text, not calls.',
  'com/ichi2/ui/SlidingTabStrip.java:95-100; com/ichi2/ui/SlidingTabLayout.java:109, 116-122',
  'SOURCE')

UNREACHABLE['Upgrade.<init>'] = ('no_trigger_in_app',
  'Upgrade declares no constructor, so only the implicit default one exists, and no code creates an instance. The class holds only the static method upgradeJSONIfNecessary (Upgrade.java:11). In the source root the class is referenced only by its declaration (Upgrade.java:9), the import (CardBrowser.java:70) and the static call (CardBrowser.java:399).',
  'com/ichi2/upgrade/Upgrade.java:9-11; com/ichi2/anki/CardBrowser.java:70, 399',
  'SOURCE')
