# AnkiDroid batch 037 (Statistics, 39 methods), LABEL helper. Writes the page, lifecycle, framework, GUI and
# cross-batch edges for the Statistics screen and its fragments, plus the UNREACHABLE entries. Method-level labels and
# sources are in graphs/AnkiDroid/parts/label_037.md (one row per method, and one EDGE row per edge below).
# No imports: e() and UNREACHABLE are the ones defined by graph_def.py, which loads this part.
# Automatic CALL edges come from graphs/AnkiDroid/auto_calls.json (dispatch exact or cha) and are not written here.
# onDestroy is on LC_NO_TRIGGER (graph_def.py:37), so the two onDestroy FRAMEWORK edges are written by hand.
# Support-library steps (Fragment lifecycle, FragmentPagerAdapter, ViewPager, AppCompat options menu) are not in
# fw_src: they are INFERRED, source not read. Framework spinner steps are read from fw_src (Spinner.java, AdapterView.java).
# AbsSpinner is not in fw_src, so the default spinner selection and the spinner draw path are INFERRED.
# No gate applies (the menus, the spinner and the Back key work once the collection has loaded): env is None and
# needs_state is not set on any edge. Gates MG312-MG321 are not needed.

# --- Existing page and framework edges (6) ---

e('S_STATISTICS', 'Statistics.onBackPressed', 'GUI',
  'the user presses the Back key on the statistics screen',
  gui=['the user presses the Back key on the statistics screen'],
  env=None,
  note='Back key route. Activity.onKeyUp calls onBackPressed (Activity.java:2979). The key tracking starts in onKeyDown (targetSdk >= ECLAIR).',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711; FW-SRC core/java/android/app/Activity.java:2886-2893, 2976-2981')

e('Statistics.onCreate', 'Statistics.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  note='ASYNC edge from onCreate to the collection-loaded callback. Written by hand: it is driven by the loader, not by a direct call.',
  evidence='SRC com/ichi2/anki/Statistics.java:88, 92; SRC com/ichi2/anki/AnkiActivity.java:255-262, 282-290')

e('Statistics.onCollectionLoaded', 'Statistics.onCreateOptionsMenu', 'FRAMEWORK',
  'supportInvalidateOptionsMenu at the end of onCollectionLoaded makes the framework build the options panel',
  env=None,
  note='Framework edge. The AppCompat path (supportInvalidateOptionsMenu) is in the support library, not fw_src: INFERRED, source not read. Activity.onCreatePanelMenu is read (Activity.java:3386-3388).',
  evidence='SRC com/ichi2/anki/Statistics.java:132, 170-177; FW-SRC core/java/android/app/Activity.java:3386-3388')

e('S_STATISTICS', 'Statistics.onOptionsItemSelected', 'GUI',
  'the user taps a time range (month, year, all) or the chooser in the options menu',
  gui=['the user taps a time range (month, year, all) or the chooser in the options menu'],
  env=None,
  note='Options menu item route. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3439-3450). No gate.',
  evidence='SRC res/menu/anki_stats.xml (src/main, lines 7-20); SRC com/ichi2/anki/Statistics.java:203-239; FW-SRC core/java/android/app/Activity.java:3439-3450')

e('S_STATISTICS', 'Statistics.onPrepareOptionsMenu', 'GUI',
  'the user opens the options panel of the statistics screen',
  gui=['the user opens the options panel of the statistics screen'],
  env=None,
  note='Options panel open route. The framework calls onPrepareOptionsMenu through onPreparePanel (Activity.java:3404-3406).',
  evidence='SRC com/ichi2/anki/Statistics.java:180-201; FW-SRC core/java/android/app/Activity.java:3404-3406')

e('Statistics.onCollectionLoaded', 'Statistics.onPrepareOptionsMenu', 'FRAMEWORK',
  'supportInvalidateOptionsMenu at the end of onCollectionLoaded prepares the panel',
  env=None,
  note='Framework edge. The AppCompat path is INFERRED (support library not read); the Activity.onPreparePanel path is read.',
  evidence='SRC com/ichi2/anki/Statistics.java:132, 180-201; FW-SRC core/java/android/app/Activity.java:3404-3406')

# --- Edges added for batch 037 (16) ---

e('Statistics.onCollectionLoaded', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the spinner draws the deck selector rows from the adapter set in onCollectionLoaded',
  env=None,
  note='Cross-batch edge: DeckDropDownAdapter.getView belongs to another batch. Written here as the caller part (precedent graph_def_before_part013.py). The spinner draw path is framework (AbsSpinner not in fw_src): INFERRED.',
  evidence='SRC com/ichi2/anki/Statistics.java:100; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:61-92, 90')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getItem', 'FRAMEWORK',
  'the pager asks for the fragment of a tab',
  env=None,
  note='The pager is a support-library FragmentPagerAdapter, so the call is framework-invoked (INFERRED, source not read). Body calls newInstance (306) and checkAndUpdate (307).',
  evidence='SRC com/ichi2/anki/Statistics.java:304-309')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getCount', 'FRAMEWORK',
  'the pager asks for the number of tabs',
  env=None,
  note='Support-library call (INFERRED, source not read). Returns 9 (Statistics.java:313).',
  evidence='SRC com/ichi2/anki/Statistics.java:311-314')

e('Statistics.onCollectionLoaded', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after mSectionsPagerAdapter.notifyDataSetChanged() at line 133',
  env=None,
  note='Refresh path: notifyDataSetChanged, then FragmentPagerAdapter calls getItemPosition (INFERRED, support library). getItemPosition runs checkAndUpdate (automatic CHA, line 298).',
  evidence='SRC com/ichi2/anki/Statistics.java:133, 293-302')

e('Statistics.selectDropDownItem', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after notifyDataSetChanged at line 256',
  env=None,
  note='Same refresh path as the onCollectionLoaded edge (INFERRED, support library).',
  evidence='SRC com/ichi2/anki/Statistics.java:256, 293-302')

e('Statistics.onOptionsItemSelected', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after a time range is changed at lines 215, 223 or 231',
  env=None,
  note='Same refresh path (INFERRED, support library).',
  evidence='SRC com/ichi2/anki/Statistics.java:215, 223, 231, 293-302')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getPageTitle', 'FRAMEWORK',
  'the tab strip draws the tab titles',
  env=None,
  note='Tab titles are set by SlidingTabLayout.populateTabStrip (SlidingTabLayout.java:222), reached from onCollectionLoaded line 126 via SlidingTabLayout.setViewPager. The edge is drawn from the page node; the middle of the chain is in another batch. The framework-invoked call is INFERRED.',
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:222; SRC com/ichi2/anki/Statistics.java:126, 317')

e('Statistics$ChartFragment.<init>', 'Statistics$ChartFragment.onCreate', 'LIFECYCLE',
  'fragment lifecycle: onCreate follows the constructor',
  env=None,
  note='Fragment lifecycle (support library not read: INFERRED). The lifecycle edges at graph_def.py:209-210 cover only the Statistics activity, so this fragment edge is written here.',
  evidence='SRC com/ichi2/anki/Statistics.java:416-418, 556-559')

e('Statistics$ChartFragment.onCreate', 'Statistics$ChartFragment.onCreateView', 'LIFECYCLE',
  'fragment lifecycle: onCreateView follows onCreate',
  env=None,
  note='Fragment lifecycle (INFERRED, support library not read).',
  evidence='SRC com/ichi2/anki/Statistics.java:556-559, 420-421')

e('Statistics$ChartFragment.onCreateView', 'Statistics$StatisticFragment.onResume', 'LIFECYCLE',
  'fragment lifecycle: onResume follows onCreateView; the inherited onResume calls checkAndUpdate',
  env=None,
  note='Fragment lifecycle (INFERRED). Dispatches to ChartFragment.checkAndUpdate (automatic CHA, line 393).',
  evidence='SRC com/ichi2/anki/Statistics.java:420-481, 390-395')

e('Statistics$OverviewStatisticsFragment.<init>', 'Statistics$OverviewStatisticsFragment.onCreateView', 'LIFECYCLE',
  'fragment lifecycle: onCreateView follows the constructor',
  env=None,
  note='Fragment lifecycle (INFERRED). No onCreate override in this fragment.',
  evidence='SRC com/ichi2/anki/Statistics.java:587-589, 592-594')

e('Statistics$OverviewStatisticsFragment.onCreateView', 'Statistics$StatisticFragment.onResume', 'LIFECYCLE',
  'fragment lifecycle: onResume follows onCreateView; the inherited onResume calls checkAndUpdate',
  env=None,
  note='Fragment lifecycle (INFERRED). Dispatches to OverviewStatisticsFragment.checkAndUpdate (automatic CHA, line 393).',
  evidence='SRC com/ichi2/anki/Statistics.java:592-646, 390-395')

e('Statistics.onBackPressed', 'Statistics$ChartFragment.onDestroy', 'FRAMEWORK',
  'the activity finishes from the Back key and its fragments are torn down',
  env=None,
  note='onDestroy is on LC_NO_TRIGGER (graph_def.py:37), so this hand-written edge is its route in. Fragment teardown is INFERRED (FragmentManager not in fw_src).',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711, 570-576; SRC graphs/AnkiDroid/graph_def.py:37')

e('Statistics.onBackPressed', 'Statistics$OverviewStatisticsFragment.onDestroy', 'FRAMEWORK',
  'the activity finishes from the Back key and its fragments are torn down',
  env=None,
  note='Same as the ChartFragment edge: onDestroy is on LC_NO_TRIGGER (graph_def.py:37); teardown INFERRED.',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711, 688-694; SRC graphs/AnkiDroid/graph_def.py:37')

e('Statistics.onCollectionLoaded', 'Statistics$1.onItemSelected', 'FRAMEWORK',
  'the spinner fires onItemSelected for the initial selection when its layout ends',
  env=None,
  note='Spinner layout ends with checkSelectionChanged (Spinner.java:681), which reaches AdapterView.fireOnSelected (AdapterView.java:937-947).',
  evidence='SRC com/ichi2/anki/Statistics.java:100-104; FW-SRC core/java/android/widget/Spinner.java:676-684; FW-SRC core/java/android/widget/AdapterView.java:937-947')

e('S_STATISTICS', 'Statistics$1.onItemSelected', 'GUI',
  'the user picks a deck in the toolbar spinner',
  gui=['the user picks a deck in the toolbar spinner'],
  env=None,
  note='Spinner selection route. onItemSelected calls selectDropDownItem (Statistics.java:104).',
  evidence='SRC com/ichi2/anki/Statistics.java:101-105; FW-SRC core/java/android/widget/AdapterView.java:937-947')

# --- UNREACHABLE entries (3) ---

UNREACHABLE['Statistics$1.onNothingSelected'] = ('framework_never_calls', "AdapterView fires onNothingSelected only when the selected position is negative (AdapterView.java:937-947, read). The deck spinner adapter DeckDropDownAdapter.getCount returns decks.size() + 1 (DeckDropDownAdapter.java:40-41), so it always has at least one row (the all-decks row) and the selection is never negative. The default selection when the adapter is set is in AbsSpinner, which is not in fw_src: INFERRED for that step.", 'SRC com/ichi2/anki/Statistics.java:107-110; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:40-41; FW-SRC core/java/android/widget/AdapterView.java:937-947', 'INFERRED')

UNREACHABLE['Statistics$ChartFragment.invalidateView'] = ('no_trigger_in_app', "No call site in the source root: the only occurrences are the abstract declaration in StatisticFragment (397), this override (563) and the OverviewStatisticsFragment override (661). No auto_calls.json row calls it, and no framework route to it is known (the Fragment base class is in the support library, not in fw_src: INFERRED).", 'SRC com/ichi2/anki/Statistics.java:397, 563-567, 661', 'SOURCE')

UNREACHABLE['Statistics$OverviewStatisticsFragment.invalidateView'] = ('no_trigger_in_app', "Same finding as ChartFragment.invalidateView: no call site in the source root (grep matches only 397, 563, 661), no auto_calls.json row, and no known framework route (Fragment base class not in fw_src: INFERRED).", 'SRC com/ichi2/anki/Statistics.java:397, 660-665', 'SOURCE')
