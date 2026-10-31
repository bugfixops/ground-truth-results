# batch 023 (label_023): com.money.manager.ex.common.AmountInputDialog, methods 1-40 of 43: the constructor, the instance and static methods, the generated helper AmountInputDialog$$Icepick (4 methods), the listeners $1-$5 (<init> and onClick each) and AmountInputDialog$6.<init>.
# The other three (AmountInputDialog$6.onClick, $7.<init>, $7.onClick) are in batch 024: graphs/MMEX/parts/label_024.py.
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_023.md. grep evidence: graphs/MMEX/parts/label_023.grep.txt.
# No page is defined. SCREENS has no home, settings or price-edit key, so the entry taps belong to the batches that own those screens. The keypad, delete and clear keys reach their listeners through FRAMEWORK edges from onCreateDialog, as in label_021.py.
# CALL edges come from auto_calls.json and are not written here. androidx DialogFragment and the icepick library are not in the dataset: INFERRED. The generated helper has no source in the app source root (grep section B).

# ---- the three callers outside this batch: each one calls show(), so the framework runs onCreate (LIFECYCLE)

e('HomeFragment.startBalanceAccount', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the balance account amount dialog is shown: dialog.show (HomeFragment.java:548) makes the fragment manager run onCreate',
  evidence='SRC home/HomeFragment.java:545-548 (getInstance 545-546, setTargetFragment 547, show 548); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

e('InvestmentSettingsFragment$1.onPreferenceClick', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the asset allocation threshold dialog is shown: show (InvestmentSettingsFragment.java:117) makes the fragment manager run onCreate',
  evidence='SRC settings/InvestmentSettingsFragment.java:111-119 (getInstance 116, show 117); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

e('EditPriceDialog$7.onClick', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the amount field of the price edit dialog shows the amount dialog: show (EditPriceDialog.java:260) makes the fragment manager run onCreate',
  evidence='SRC investment/EditPriceDialog.java:256-263 (getInstance 259, show 260); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

# ---- the dialog lifecycle (androidx DialogFragment: library not in the dataset, INFERRED)

e('AmountInputDialog.onCreate', 'AmountInputDialog.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, to build the dialog it shows',
  evidence='SRC common/AmountInputDialog.java:138-153 (onCreate), 155-156 (onCreateDialog); precedent label_012.py line 17; INFERRED androidx DialogFragment (library not in the dataset; source not read)')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog.onResume', 'LIFECYCLE',
  'the framework resumes the dialog fragment once the dialog has been created and shown',
  evidence='SRC common/AmountInputDialog.java:155-276 (onCreateDialog), 278-282 (onResume); INFERRED androidx Fragment lifecycle (library not in the dataset; source not read)')

e('AmountInputDialog.onResume', 'AmountInputDialog.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state through onSaveInstanceState (on rotation, or when the host activity stops)',
  evidence='SRC common/AmountInputDialog.java:278-295; precedent label_010.py line 47; INFERRED androidx FragmentManager (library not in the dataset; source not read)')

# ---- the keypad, the clear and equals keys, and the delete key: onCreateDialog stores the listeners; the framework calls onClick on a tap

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$1.onClick', 'FRAMEWORK',
  'a digit or decimal key is tapped: setOnClickListener stores the listener on each key, and performClick calls onClick',
  guard='the user taps a digit key (buttonKeyNum0-9) or the decimal key (buttonKeyNumDecimal) of the keypad (lines 178-181)',
  evidence='SRC common/AmountInputDialog.java:164-181 (listener 164-177; set on each key 178-181); FW-SRC core/java/android/view/View.java:6143-6147 (setOnClickListener stores the listener at 6147), 6289-6296 (performClick calls onClick at 6294)')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$2.onClick', 'FRAMEWORK',
  'an operator key is tapped: setOnClickListener stores the listener on each key, and performClick calls onClick',
  guard='the user taps an operator key (add, divide, less, multiplication, left or right parenthesis) (lines 193-196)',
  evidence='SRC common/AmountInputDialog.java:183-196 (listener 183-192; set on each key 193-196); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$3.onClick', 'FRAMEWORK',
  'the clear key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the clear key (buttonKeyClear) (line 200)',
  evidence='SRC common/AmountInputDialog.java:198-207 (clear listener set at 200-207); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$4.onClick', 'FRAMEWORK',
  'the equals key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the equals key (buttonKeyEqual) (line 211)',
  evidence='SRC common/AmountInputDialog.java:209-218 (equals listener set at 211-218); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$5.onClick', 'FRAMEWORK',
  'the delete key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the delete key (deleteButton); the listener is set only when the view exists (line 222), and both layouts define it',
  evidence='SRC common/AmountInputDialog.java:220-235 (guard 222, listener set at 223-234); RES layout/input_amount_dialog.xml:91 and RES layout-land/input_amount_dialog.xml:186 (deleteButton); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

# ---- icepick (@State on mAmount, line 122): the library loads the generated helper AmountInputDialog$$Icepick by reflection.
# The helper is not in the source root (label_023.grep.txt section B); the icepick library is not in the dataset: INFERRED for every edge below.

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State field mAmount: the library loads the generated helper by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:47 (import icepick.Icepick), 122 (@State mAmount), 417 (Icepick.restoreInstanceState); the icepick library and the helper are not in the dataset: INFERRED, source not read')

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.<init>', 'FRAMEWORK',
  'the library creates an instance of the generated helper by reflection when it restores the state',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:417; the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.restore', 'FRAMEWORK',
  'Icepick restores the @State field mAmount: the library calls the generated restore by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:122 (@State mAmount), 417 (Icepick.restoreInstanceState); the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick saves the @State field mAmount: the library loads the generated helper by reflection, which runs its static initialiser first (on a first save, before any restore)',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:47 (import icepick.Icepick), 122 (@State mAmount), 294 (Icepick.saveInstanceState); the icepick library and the helper are not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.<init>', 'FRAMEWORK',
  'the library creates an instance of the generated helper by reflection when it saves the state',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:294; the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.save', 'FRAMEWORK',
  'Icepick saves the @State field mAmount: the library calls the generated save by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:122 (@State mAmount), 294 (Icepick.saveInstanceState); the icepick library is not in the dataset: INFERRED, source not read')

# ---- UNREACHABLE: overloads of getInstance with no live caller (grep output: graphs/MMEX/parts/label_023.grep.txt, sections A and C)

UNREACHABLE['AmountInputDialog.getInstance(int,Money)'] = (
  'no_trigger_in_app',
  'public static overload with no caller in the app. Every reference to AmountInputDialog under the source root is listed in the grep (20 hits): the three external callers use other overloads (HomeFragment.java:545-546 the 4-argument int form, InvestmentSettingsFragment.java:116 the String 2-argument form, EditPriceDialog.java:259 the String 4-argument form), and the only 3-argument call is commented out (EditTransactionCommonFunctions.java:410). No CALL edge into this overload exists in auto_calls.json. Its outgoing auto edge (line 64) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:62-65; SRC home/HomeFragment.java:545-546; SRC settings/InvestmentSettingsFragment.java:116; SRC investment/EditPriceDialog.java:259; SRC transactions/EditTransactionCommonFunctions.java:410 (commented); grep label_023.grep.txt sections A and C',
  'SOURCE')

UNREACHABLE['AmountInputDialog.getInstance(int,Money,int)'] = (
  'no_trigger_in_app',
  'public static overload whose only call site is commented out: transactions/EditTransactionCommonFunctions.java:410 begins with // (the dialog line and its show call at 411 are both comments). No live call in the app and no CALL edge into it in auto_calls.json. Its outgoing auto edge (line 73) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:71-74; SRC transactions/EditTransactionCommonFunctions.java:404-412 (410-411 commented); grep label_023.grep.txt sections A and C',
  'SOURCE')

UNREACHABLE['AmountInputDialog.getInstance(String,Money,int)'] = (
  'no_trigger_in_app',
  'public static overload with no caller: the String callers use the 2-argument form (InvestmentSettingsFragment.java:116) and the 4-argument form (EditPriceDialog.java:259); no call with three arguments exists (grep sections A and C), and no CALL edge into it exists in auto_calls.json. Its outgoing auto edge (line 77) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:76-78; SRC settings/InvestmentSettingsFragment.java:116; SRC investment/EditPriceDialog.java:259; grep label_023.grep.txt sections A and C',
  'SOURCE')

# ---- auto edges that cannot run: their source is one of the UNREACHABLE overloads above (their bodies never run)

sup(('AmountInputDialog.getInstance(int,Money)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 64
sup(('AmountInputDialog.getInstance(int,Money,int)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 73
sup(('AmountInputDialog.getInstance(String,Money,int)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 77
