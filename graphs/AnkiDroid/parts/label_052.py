# AnkiDroid batch 052 (LABEL helper). FieldEditText (10 methods), FlashCardsContract nested classes in the api
# module (14), Lookup (10) and Manifest (2). The full row list is in graphs/AnkiDroid/parts/label_052.md.
# Written here: two page-to-batch e() edges and 16 UNREACHABLE entries. CALL edges that auto_calls.json already
# holds (the <clinit> chains and the Lookup and NoteEditor callers) are not repeated.

# LayoutInflater creates the FieldEditText named in card_multimedia_editline.xml through the (Context, AttributeSet)
# constructor, by reflection. The editor opens from DeckPicker add note (DeckPicker.java:841).
e('S_NOTEEDITOR', 'FieldEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the note editor inflates card_multimedia_editline.xml, which instantiates the FieldEditText view',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1099; SRC com/ichi2/anki/FieldEditText.java:23-25; FW-SRC core/java/android/view/LayoutInflater.java:615, 647',
  note='Opened from DeckPicker add note (DeckPicker.java:841) and CardBrowser (493, 631). populateEditFields is called from setNote (NoteEditor.java:1380), updateFieldsFromMap (1497) and the note-type spinner (1637). The layout is src/main/res/layout/card_multimedia_editline.xml lines 8-16. Edit mode also needs a note (STATE_NOTE). The class initializer FieldEditText.<clinit> runs on the same reflective construction.')

# The dictionary dialog callback. The user taps a language in the LEO dialog built by Lookup.lookUp (Lookup.java:110-123).
# The lookup button is shown only when Lookup.isAvailable() (AbstractFlashcardViewer.java:1219).
e('S_REVIEWER', 'Lookup$1.onSelection', 'GUI',
  'tap the lookup button, then pick a language in the LEO dictionary dialog',
  env=ENV_BROWSER,
  needs_state=STATE_SETTINGS,
  gui=['tap the lookup button, then pick a language in the LEO dictionary dialog'],
  evidence='SRC com/ichi2/anki/Lookup.java:110-121; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1210, 1219, 1424',
  note='The dialog opens only for the LEO dictionaries (preference 3 or 4, Lookup.java:94-95). The LEO web variant needs a browser (ENV_BROWSER). The LEO app variant (preference 4) needs org.leo.android.dict installed (ENV_OTHER_APP_INTENT). The callback calls storeLanguage (Lookup.java:118, empty body) and lookupLeo (Lookup.java:119).')

UNREACHABLE['FieldEditText.<init>(Context)'] = ('no_trigger_in_app', 'No new FieldEditText( anywhere in src/main or api. LayoutInflater never uses the one-argument signature; it calls the (Context,AttributeSet) constructor (FW-SRC LayoutInflater.java:90-91). No class extends FieldEditText.', 'SRC com/ichi2/anki/FieldEditText.java:18-20', 'SOURCE')
UNREACHABLE['FieldEditText.<init>(Context,int,String,String)'] = ('no_trigger_in_app', 'No new FieldEditText( with four arguments exists in src/main or api. NoteEditor builds fields from XML (NoteEditor.java:1099) and calls init directly (NoteEditor.java:1247), so this constructor is never reached.', 'SRC com/ichi2/anki/FieldEditText.java:33-36', 'SOURCE')
UNREACHABLE['FieldEditText.<init>(Context,AttributeSet,int)'] = ('no_trigger_in_app', 'No new FieldEditText( with three arguments exists. LayoutInflater uses only the two-argument signature. The two-argument constructor calls super(context, attr) (FieldEditText.java:24), not this(...), so nothing chains into this one. No subclass exists.', 'SRC com/ichi2/anki/FieldEditText.java:28-30', 'SOURCE')
UNREACHABLE['FieldEditText.cleanText'] = ('no_trigger_in_app', 'The only occurrence of cleanText( in src/main is its definition (FieldEditText.java:70). No caller in src/main or api.', 'SRC com/ichi2/anki/FieldEditText.java:70-75', 'SOURCE')
UNREACHABLE['FieldEditText.getName'] = ('no_trigger_in_app', 'No .getName() call in src/main has a FieldEditText receiver. The receivers are File, Backup, list items of other types, and reflection Field and Class objects. No caller.', 'SRC com/ichi2/anki/FieldEditText.java:51-53', 'SOURCE')
UNREACHABLE['FlashCardsContract.<init>'] = ('no_trigger_in_app', 'Private constructor (api FlashCardsContract.java:119-120, "Don\'t create instances of this class"). No new FlashCardsContract( in src/main or api. The api file is outside the checker roots, so the source cell cites the provider import.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:41-42', 'SOURCE')
UNREACHABLE['FlashCardsContract$Card.<init>'] = ('no_trigger_in_app', 'Implicit constructor of the nested static class (api FlashCardsContract.java:708). No new Card( or new FlashCardsContract.Card( in the files that reference FlashCardsContract (CardContentProvider.java, NoteInfo.java, AddContentApi.java).', 'SRC com/ichi2/anki/provider/CardContentProvider.java:41-42', 'SOURCE')
UNREACHABLE['FlashCardsContract$CardTemplate.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:500). No new CardTemplate( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:42', 'SOURCE')
UNREACHABLE['FlashCardsContract$Deck.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:1078). No new Deck( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:368', 'SOURCE')
UNREACHABLE['FlashCardsContract$Model.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:438). No new Model( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:265', 'SOURCE')
UNREACHABLE['FlashCardsContract$Note.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:252). No new Note( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:139', 'SOURCE')
UNREACHABLE['FlashCardsContract$ReviewInfo.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:899). No new ReviewInfo( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:313', 'SOURCE')
UNREACHABLE['Lookup.<init>'] = ('no_trigger_in_app', 'Lookup has no explicit constructor (Lookup.java:17) and there is no new Lookup( in src/main or api. Every member is static, so the implicit constructor never runs.', 'SRC com/ichi2/anki/Lookup.java:17', 'SOURCE')
UNREACHABLE['Lookup.getSearchStringTitle'] = ('closed_by_api_level', 'Only caller: Reviewer.onCreateOptionsMenu (Reviewer.java:298-300), inside if (!CompatHelper.isHoneycomb() && !mDisableClipboard). isHoneycomb is SDK 11 or higher (CompatHelper.java:61-62). On the standard API 27 config the guard is false, so the branch never runs. minSdkVersion is 10 (build.gradle), so the branch is reachable only on API 10.', 'SRC com/ichi2/anki/Reviewer.java:298-300; SRC com/ichi2/compat/CompatHelper.java:61-62', 'SOURCE')
UNREACHABLE['Manifest.<init>'] = ('no_trigger_in_app', 'Generated class from aapt; its input is the permission declaration at AndroidManifest.xml:58. The generated file is not in the source tree. No new Manifest( in src/main or api. The app source refers only to android.Manifest (DeckPicker.java:24, CollectionHelper.java:19), a different class. confirmed_by INFERRED, not by a source line.', 'SRC AndroidManifest.xml:58', 'INFERRED')
UNREACHABLE['Manifest$permission.<init>'] = ('no_trigger_in_app', 'Nested class generated from the same permission declaration (AndroidManifest.xml:58). No new anywhere in src/main or api. confirmed_by INFERRED, not by a source line. A conflicts.md entry is needed; this helper may not write it, so the orchestrator must add it.', 'SRC AndroidManifest.xml:58', 'INFERRED')
