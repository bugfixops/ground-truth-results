# AnkiDroid batch 074 (LABEL helper). StepsPreference (9 methods), HtmlColors (4), StyledProgressDialog (9),
# Themes (7), DividerItemDecoration (2). The full row list is in graphs/AnkiDroid/parts/label_074.md.
#
# Route ownership:
# - Auto CALL edges (bytecode builder, auto_calls.json) are not written here: StepsPreference internal calls,
#   the convertFromJSON and convertToJSON callers, HtmlColors.invertColors and nameToHex, the StyledProgressDialog
#   four-argument to five-argument delegation, the Themes overload calls, and DividerItemDecoration.<init> from DeckPicker.onCreate.
# - No MG ids are used. Gates are the predefined constants STATE_SETTINGS (invertedColors preference) and STATE_DECK.

# --- StepsPreference: inflated from XML by the framework preference inflater (GenericInflater reflection on the
# --- (Context, AttributeSet) constructor). Both screens that show the steps tags.
e('S_DECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'DeckOptions shows deck_options.xml, whose StepsPreference tags (newSteps, lapSteps) are inflated by the framework preference inflater through the (Context, AttributeSet) constructor, found by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/deck_options.xml:66-69, 138-141; SRC com/ichi2/anki/DeckOptions.java:499-500, 523; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The destination is a method of this batch, so the edge belongs here. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'FilteredDeckOptions shows cram_deck_options.xml for a filtered deck (else branch), whose StepsPreference tag (steps) is inflated through the (Context, AttributeSet) constructor by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/cram_deck_options.xml:50-54; SRC com/ichi2/anki/FilteredDeckOptions.java:369-378; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The else branch runs only when the deck is a filtered deck, FilteredDeckOptions.java:370-374. No gate constant covers this; env and needs_state unset.')

# --- StepsPreference.onDialogClosed: framework dispatch from DialogPreference.onDismiss (no app call site).
e('S_DECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the user taps a steps preference and the dialog closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/DeckOptions.java:499-523; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='The dialog is shown by DialogPreference.onClick (showDialog at line 277). The dismiss listener is set at line 318. The dispatch to onDialogClosed is at line 395, a framework call with no app call site. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the same steps dialog on the filtered-deck options screen closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/FilteredDeckOptions.java:370-378; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='Same framework dispatch as the DeckOptions edge. No gate.')

# --- HtmlColors static initialiser: runs at the invokestatic of HtmlColors.invertColors in AbstractFlashcardViewer.updateCard.
e('S_REVIEWER', 'HtmlColors.<clinit>', 'FRAMEWORK',
  'the first night-mode card display initialises the HtmlColors class, which runs its static initialiser before invertColors',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1722, 2112-2118; SRC com/ichi2/themes/HtmlColors.java:10-16, 84-85; JVM class-initialisation rule is not in fw_src: INFERRED, source not read',
  note='Gate STATE_SETTINGS: the invertedColors preference (AbstractFlashcardViewer.java:1722) is needed for mNightMode (line 2112). The initialisation happens at the invokestatic in updateCard (line 2118), so the source is the reviewer page. INFERRED.')

# --- DividerItemDecoration.onDrawOver: support-library RecyclerView dispatch (not in fw_src).
e('S_DECKPICKER', 'DividerItemDecoration.onDrawOver', 'FRAMEWORK',
  'the deck list RecyclerView draws the item decoration over its rows',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-376; SRC com/ichi2/ui/DividerItemDecoration.java:28-44; support-library RecyclerView dispatch is not in fw_src: INFERRED, source not read',
  note='Gate STATE_DECK: decks (rows) are on screen, so onDrawOver has children to draw dividers under. INFERRED.')

# --- UNREACHABLE entries.
UNREACHABLE['StepsPreference.<init>(Context)'] = ('framework_never_calls',
  'No app caller; the framework inflater looks up only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:51-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['StepsPreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
  'No app caller; the framework inflater uses only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:37-41; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['HtmlColors.<init>'] = ('no_trigger_in_app',
  'HtmlColors has only static members; no code creates an instance',
  'com/ichi2/themes/HtmlColors.java:9-30; com/ichi2/anki/AbstractFlashcardViewer.java:88, 2118',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.<init>'] = ('no_trigger_in_app',
  'The constructor runs only from new StyledProgressDialog(...), which does not occur in the source root; the static show overloads return MaterialDialog',
  'com/ichi2/themes/StyledProgressDialog.java:31-39, 53-73; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.animationEnabled'] = ('no_trigger_in_app',
  'Private static helper with no caller in the source root',
  'com/ichi2/themes/StyledProgressDialog.java:43-73, 76-82; com/ichi2/anki/AnkiActivity.java:119',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setMax'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setMax callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:84-86; com/ichi2/ui/SeekBarPreference.java:70, 82',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgress'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setProgress callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:89-91; com/ichi2/ui/SeekBarPreference.java:71, 83',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgressStyle'] = ('no_trigger_in_app',
  'No-op setter with no caller in the source root and no instance',
  'com/ichi2/themes/StyledProgressDialog.java:94-96',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show()'] = ('no_trigger_in_app',
  'Instance override of Dialog.show; no StyledProgressDialog instance is created, and the app uses the static show overloads',
  'com/ichi2/themes/StyledProgressDialog.java:42-50; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show(Context,CharSequence,CharSequence)'] = ('no_trigger_in_app',
  'Three-argument overload; every app call site passes four arguments, so nothing calls it',
  'com/ichi2/themes/StyledProgressDialog.java:53-55; com/ichi2/anki/DeckPicker.java:253-254, 294-296, 316-317; com/ichi2/anki/StudyOptionsFragment.java:316-317',
  'SOURCE')

UNREACHABLE['Themes.<init>'] = ('no_trigger_in_app',
  'Themes has only static members; no code creates an instance',
  'com/ichi2/themes/Themes.java:30-41; com/ichi2/anki/NoteEditor.java:1110',
  'SOURCE')

UNREACHABLE['Themes.getResFromAttr(Context,int)'] = ('no_trigger_in_app',
  'Single-attribute overload; both app call sites pass an int array and resolve to the array overload',
  'com/ichi2/themes/Themes.java:94-97; com/ichi2/anki/NoteEditor.java:1110; com/ichi2/anki/AbstractFlashcardViewer.java:1580',
  'SOURCE')
