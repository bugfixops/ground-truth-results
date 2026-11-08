# AnkiDroid batch 067 (LABEL helper). 39 methods: HttpFetcher, DeckAdapter (and its ViewHolder), DeckDropDownAdapter
# (and its ViewHolder), FabBehavior, PopupMenuWithIcons.<init>, ActivityTransitionAnimation.<init>, ViewAnimation.
# The full row list is in graphs/AnkiDroid/parts/label_067.md.
#
# Route ownership:
# - Automatic CALL edges (auto_calls.json) are not written here, for example HttpFetcher -> LoadPronounciationActivity,
#   DeckPicker.onCreate -> DeckAdapter setters, DeckAdapter.buildDeckList -> processNodes, FabBehavior.onDependentViewChanged
#   -> getFabTranslationYForSnackbar, and AbstractFlashcardViewer -> ViewAnimation.fade.
# - Edges written here: page-sourced framework dispatch (S_DECKPICKER, S_STATISTICS, S_CARDBROWSER) into methods of this batch.
#   Support library dispatch (RecyclerView, CoordinatorLayout) is INFERRED, source not read.
#
# Gates: STATE_CARDS on the congrats or no-cards Snackbar path (FabBehavior.onDependentViewChanged). No MISSING GATE edge
# is written; the subdeck guard of DeckAdapter.setDeckExpander is MG612, described in the .md row only.

# --- Home screen deck list (S_DECKPICKER): RecyclerView adapter callbacks.
e('S_DECKPICKER', 'DeckAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the home screen deck list asks the adapter for a new row view',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:154-158; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.onBindViewHolder', 'FRAMEWORK',
  'the home screen deck list binds the data of each visible row',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:161-217; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.getItemCount', 'FRAMEWORK',
  'the RecyclerView asks the number of decks for its layout',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:220-222; RecyclerView dispatch is support library, INFERRED, source not read')

# --- Home screen FAB behavior (S_DECKPICKER): CoordinatorLayout behavior callbacks.
e('S_DECKPICKER', 'FabBehavior.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the support library creates the FAB behavior from layout_behavior when the home screen is inflated',
  env=None,
  needs_state=None,
  cls='non_standard',
  via='CoordinatorLayout behavior from layout_behavior (support library, not in the dataset)',
  evidence='SRC res/layout-v14/floating_add_button.xml:16; res/layout/deck_picker.xml:2-3, 36; res/layout/homescreen.xml:7; com/ichi2/anki/widgets/FabBehavior.java:42-44; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.layoutDependsOn', 'FRAMEWORK',
  'the CoordinatorLayout asks the FAB behavior whether it depends on each sibling view during layout',
  env=None,
  needs_state=None,
  evidence='SRC res/layout/deck_picker.xml:2-3, 36; com/ichi2/anki/widgets/FabBehavior.java:62-64; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.onDependentViewChanged', 'FRAMEWORK',
  'a Snackbar on the home screen root changes the dependency and the FAB behavior is told',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/widgets/FabBehavior.java:67-77; com/ichi2/anki/UIUtils.java:33-35; com/ichi2/anki/DeckPicker.java:656-664; CoordinatorLayout dispatch is support library, INFERRED, source not read',
  note='Gate STATE_CARDS: the congrats or no-cards-due Snackbar follows a study session with RESULT_NO_MORE_CARDS (DeckPicker.java:656-664).')

# --- Toolbar deck spinner of the Statistics screen (S_STATISTICS): framework Spinner calls into DeckDropDownAdapter.
e('S_STATISTICS', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/Statistics.java:100-101')

e('S_STATISTICS', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/Statistics.java:100-101')

# --- Toolbar deck spinner of the card browser (S_CARDBROWSER): same framework paths, CardBrowser.java:372-385.
e('S_CARDBROWSER', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner of the card browser measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner of the card browser draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the card browser toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the card browser toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open card browser toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open card browser toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/CardBrowser.java:372-373')

# --- UNREACHABLE entries (one per method with no route).
UNREACHABLE['HttpFetcher.<init>'] = ('no_trigger_in_app',
  'HttpFetcher declares no constructor and no code creates an instance; every caller uses the static methods',
  'com/ichi2/anki/web/HttpFetcher.java:47; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:212, 252; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:182',
  'SOURCE')

UNREACHABLE['ActivityTransitionAnimation.<init>'] = ('no_trigger_in_app',
  'ActivityTransitionAnimation declares no constructor and no code creates an instance; only the static slide method is used',
  'com/ichi2/anim/ActivityTransitionAnimation.java:9-20; com/ichi2/anki/AnkiActivity.java:232, 249',
  'SOURCE')

UNREACHABLE['ViewAnimation.<init>'] = ('no_trigger_in_app',
  'ViewAnimation declares no constructor and no code creates an instance; callers use the static fade method',
  'com/ichi2/anim/ViewAnimation.java:10-21; com/ichi2/anki/AbstractFlashcardViewer.java:1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['ViewAnimation.slide'] = ('no_trigger_in_app',
  'no caller: the only class that uses ViewAnimation calls fade, and no code calls ViewAnimation.slide',
  'com/ichi2/anim/ViewAnimation.java:23-62; com/ichi2/anki/AbstractFlashcardViewer.java:76, 1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['DeckDropDownAdapter.getItem'] = ('framework_never_calls',
  'the framework reaches the spinner getItem only through getSelectedItem or getItemAtPosition, and neither is called for this spinner; AbsSpinner.java not read',
  'FW-SRC core/java/android/widget/AdapterView.java:590-594, 796-798; FW-SRC core/java/android/widget/Spinner.java:981-983; FW-SRC core/java/android/preference/PreferenceFragment.java:452; com/ichi2/anki/Statistics.java:99-101, 112; com/ichi2/anki/CardBrowser.java:372-374, 385',
  'INFERRED')

UNREACHABLE['FabBehavior.<init>()'] = ('no_trigger_in_app',
  'no code calls new FabBehavior(); the support library uses the (Context, AttributeSet) constructor from layout_behavior (INFERRED, source not read)',
  'com/ichi2/anki/widgets/FabBehavior.java:38-40; res/layout-v14/floating_add_button.xml:16',
  'SOURCE')
