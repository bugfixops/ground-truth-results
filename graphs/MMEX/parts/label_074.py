# ================================================================== batch 074 (label_074): TipsDialogFragment (22 methods),
# TipsDialogFragment$1 (2 methods), TipsDialogFragment$2 (2 methods): 26 in total (graphs/MMEX/scratch/batches/batch_074.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_074.md. Result: 26 REACHABLE, 0 UNREACHABLE.
# Every method is reached through the wildcard tip route: BaseListFragment.onStart (lines 100-107) or
# BaseExpandableListFragment.onStart (lines 101-108), gated by the settings state pref_text_search_type false (default true).
# This file writes:
#   - 2 LIFECYCLE edges from the two onStart callers into TipsDialogFragment.onCreate (the framework runs onCreate after show),
#   - the dialog lifecycle edges: onCreate to onCreateDialog, onCreateDialog to onSaveInstanceState,
#   - the two listener edges from onCreateDialog (checkbox and OK), and OK onClick to onDismiss.
# The auto CALL records (getters, setters, show, the listener <init> methods) are not written as edges (D7).
# No gui() edges (the dialog belongs to no single page, D6, D9). No sup pairs (no UNREACHABLE caller). No UNREACHABLE entries.
# No grep file: no library or generated class is UNREACHABLE.

# ---- show: the two onStart callers run the framework's onCreate (show is in the auto CALL records, D7)

e('BaseListFragment.onStart', 'TipsDialogFragment.onCreate', 'LIFECYCLE',
  'the wildcard tip is shown: show (BaseListFragment.java:106) makes the fragment manager run onCreate; show runs super.show only when mCanShow is true (TipsDialogFragment.java:134)',
  guard='mCanShow is true: the lookupswildcard key in PREF_DIALOG is not stored false (TipsDialogFragment.java:68); it is stored false only after the user ticks the do-not-show-again checkbox and taps OK (line 124)',
  needs_state=state_text('pref_text_search_type is false (the text search type switch is off; BaseListFragment.java:97-100; the default is on, preferences_behaviour.xml:52-57) and the wildcard tip is not yet shown (isShowTipsWildcard false, line 100)', ('settings',)),
  evidence='SRC fragment/TipsDialogFragment.java:66-72, 132-135; common/BaseListFragment.java:97-107; res/xml/preferences_behaviour.xml:52-57; INFERRED androidx DialogFragment.show commits a transaction and the fragment manager calls onCreate (library not read)')

e('BaseExpandableListFragment.onStart', 'TipsDialogFragment.onCreate', 'LIFECYCLE',
  'the wildcard tip is shown from the expandable list (category screen): show (BaseExpandableListFragment.java:107) makes the fragment manager run onCreate; show runs super.show only when mCanShow is true (TipsDialogFragment.java:134)',
  guard='mCanShow is true: the lookupswildcard key in PREF_DIALOG is not stored false (TipsDialogFragment.java:68); it is stored false only after the user ticks the do-not-show-again checkbox and taps OK (line 124)',
  needs_state=state_text('pref_text_search_type is false (the text search type switch is off; BaseExpandableListFragment.java:97-101; the default is on, preferences_behaviour.xml:52-57) and the wildcard tip is not yet shown (isShowTipsWildcard false, line 101)', ('settings',)),
  evidence='SRC fragment/TipsDialogFragment.java:66-72, 132-135; common/BaseExpandableListFragment.java:97-108; common/CategoryListFragment.java:111; res/xml/preferences_behaviour.xml:52-57; INFERRED androidx DialogFragment.show commits a transaction and the fragment manager calls onCreate (library not read)')

# ---- the dialog lifecycle (androidx DialogFragment: library not in the dataset, INFERRED)

e('TipsDialogFragment.onCreate', 'TipsDialogFragment.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, to build the dialog it shows',
  evidence='SRC fragment/TipsDialogFragment.java:74-87 (onCreate), 89-90 (onCreateDialog); precedent label_023.py line 23; INFERRED androidx DialogFragment (library not read)')

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (on rotation, or when the host activity stops) while the dialog is shown; onCreateDialog is the last app callback before that (no onResume override here, unlike AmountInputDialog, graph_def.py:1938)',
  evidence='SRC fragment/TipsDialogFragment.java:89-153 (onCreateDialog 89-130; onSaveInstanceState 145-153); INFERRED androidx FragmentManager saves state through onSaveInstanceState (library not read)')

# ---- the listeners: onCreateDialog stores them, the framework calls them on a change or a tap

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment$1.onCheckedChanged', 'FRAMEWORK',
  'the checkbox listener is stored by setOnCheckedChangeListener (line 106); the framework calls onCheckedChanged when the checkbox changes; body setCheckDontShowAgain (line 110)',
  guard='the user ticks or unticks the do-not-show-again checkbox (checkBoxDontShow, visible by default: setVisibleDontShowAgain runs only in the restore branch)',
  evidence='SRC fragment/TipsDialogFragment.java:103-112; res/layout/dialog_tips.xml:51-53; INFERRED Android CompoundButton listener dispatch (framework source not read in this batch)')

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment$2.onClick', 'FRAMEWORK',
  'the OK button: setNeutralButton stores the listener (line 119); a tap runs the button handler, which calls onClick (the same dispatch as label_024.py, AlertController.java:125-167)',
  guard='the user taps OK (android.R.string.ok) in the tips dialog (the listener at lines 121-127)',
  evidence='SRC fragment/TipsDialogFragment.java:119-128; auto_calls.json (TipsDialogFragment$2.onClick calls getKey and isCheckDontShowAgain at line 124, no other app callee); precedent label_024.py lines 10-30')

e('TipsDialogFragment$2.onClick', 'TipsDialogFragment.onDismiss', 'FRAMEWORK',
  'dialog.dismiss() (line 126) ends the dialog; the framework calls onDismiss (line 137), which writes the PREF_DIALOG value again (line 140)',
  guard='the OK button was tapped; the dialog is not cancelable (line 118), so OK is the only dismiss route from the user',
  evidence='SRC fragment/TipsDialogFragment.java:118, 126, 137-143; INFERRED androidx DialogFragment dismiss calls onDismiss (library not read)')
