# ================================================================== batch 136 (label_136): 32 methods in 8 classes
# tutorial/TutorialSyncFragment (4 methods), tutorial/TutorialTransactionsFragment (4), utils/ActivityUtils (3), utils/AlertDialogWrapper (11),
# utils/DialogUtils (3), utils/DrawableUtils (3), utils/ListUtils (2), utils/MathUtils (2)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_136.md (18 REACHABLE, 14 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_136.grep.txt.
# This file writes 4 e() edges (LIFECYCLE, fragment callbacks), 14 UNREACHABLE entries and 1 sup pair.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (D7) and is not written here.
# The tutorial route (MainActivity -> TutorialActivity -> TutorialPagerAdapter.getItem -> newInstance) is in batch 135 (not merged): interim (D8).
# The AlertDialogWrapper callers are in batch 074 (TipsDialogFragment.onCreateDialog) and batch 085 (EditPriceDialog.onCreateDialog).
# The DialogUtils callers are in batch 126 (SyncServiceMessageHandler.closeDialog) and batch 048 (CurrencyUIFeatures, onCompleted).
# The commented-out DialogUtils call in PriceUpdaterBase (batch 091, line 65) is not live. Batch 130 owns no caller (checked in grep G7).
# The fragment LIFECYCLE edges start at each fragment's own <init> (D21). androidx Fragment lifecycle is INFERRED (library source not read).
# UNREACHABLE: the entries with no_trigger_in_app have no call site in the app source (grep G1, G2). ActivityUtils.restoreOrientation is branch_never_taken (its guard is always false).
# The sup pair cuts the auto edge from CurrencyListActivity.onCreate into the UNREACHABLE restoreOrientation (D14). It does not cut forceCurrentOrientation, which is REACHABLE.
# Evidence labels: SRC = printed line of the source tree; INFERRED = a step whose source was not read.

# ---- tutorial fragments: LIFECYCLE from each fragment's own <init> (D21)

e('TutorialSyncFragment.<init>', 'TutorialSyncFragment.onCreate', 'LIFECYCLE',
  'the FragmentManager adds the fragment to the tutorial pager and calls onCreate after the constructor',
  evidence='SRC tutorial/TutorialSyncFragment.java:49-51 (constructor), 53-60 (onCreate); SRC tutorial/TutorialPagerAdapter.java:52-54 (newInstance for page 4; batch 135, interim D8); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialSyncFragment.<init>', 'TutorialSyncFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after the constructor; it inflates fragment_tutorial_sync',
  evidence='SRC tutorial/TutorialSyncFragment.java:49-51 (constructor), 62-68 (onCreateView, inflate at 66); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialTransactionsFragment.<init>', 'TutorialTransactionsFragment.onCreate', 'LIFECYCLE',
  'the FragmentManager adds the fragment to the tutorial pager and calls onCreate after the constructor',
  evidence='SRC tutorial/TutorialTransactionsFragment.java:50-52 (constructor), 54-61 (onCreate); SRC tutorial/TutorialPagerAdapter.java:43-45 (newInstance for page 1; batch 135, interim D8); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialTransactionsFragment.<init>', 'TutorialTransactionsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after the constructor; it inflates fragment_tutorial_transactions',
  evidence='SRC tutorial/TutorialTransactionsFragment.java:50-52 (constructor), 63-68 (onCreateView, inflate at 67); INFERRED androidx Fragment lifecycle (library source not read)')

# ---- UNREACHABLE (rows in graphs/MMEX/parts/label_136.md)

UNREACHABLE['ActivityUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs ActivityUtils: the class is used only through its static methods',
  'SRC utils/ActivityUtils.java:27; SRC currency/list/CurrencyListActivity.java:56, 58 (static calls only); grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['ActivityUtils.restoreOrientation'] = ('branch_never_taken',
  'the only caller (CurrencyListActivity.onCreate) calls it only under mPreviousOrientation != Constants.NOT_SET; the fragment is created fresh at line 50 and the field starts at NOT_SET, so the guard is never true',
  'SRC currency/list/CurrencyListActivity.java:50, 55, 58; SRC currency/list/CurrencyListFragment.java:76, 250; SRC Constants.java:22; SRC utils/ActivityUtils.java:60-65', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setIcon'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085): the app never constructs EditPriceDialog',
  'SRC investment/EditPriceDialog.java:114-116; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setMessage'] = ('no_trigger_in_app',
  'no call site: neither AlertDialogWrapper caller (EditPriceDialog, TipsDialogFragment) calls setMessage',
  'SRC utils/AlertDialogWrapper.java:57-60; SRC investment/EditPriceDialog.java:114-116; SRC fragment/TipsDialogFragment.java:115-129; grep G2 and auto_calls (no record)', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setNegativeButton'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085)',
  'SRC utils/AlertDialogWrapper.java:62-65; SRC investment/EditPriceDialog.java:143; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setPositiveButton'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085)',
  'SRC utils/AlertDialogWrapper.java:72-75; SRC investment/EditPriceDialog.java:126; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setTitle(int)'] = ('no_trigger_in_app',
  'no call site: both callers pass a CharSequence (EditPriceDialog.java:115, TipsDialogFragment.java:116), so the int overload is never selected',
  'SRC utils/AlertDialogWrapper.java:42-45; SRC investment/EditPriceDialog.java:115; SRC fragment/TipsDialogFragment.java:116; auto_calls setTitle(CharSequence) records', 'SOURCE')

UNREACHABLE['DialogUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs DialogUtils: the class is used only through its static method closeProgressDialog',
  'SRC utils/DialogUtils.java:29; SRC sync/SyncServiceMessageHandler.java:127; SRC currency/CurrencyUIFeatures.java:244; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DialogUtils.closeProgressBar'] = ('no_trigger_in_app',
  'no call site: the only mention in the app source is the definition (grep G2)',
  'SRC utils/DialogUtils.java:39-45; grep G2 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs DrawableUtils; both methods are static',
  'SRC utils/DrawableUtils.java:26; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.scaleImage(Context,Drawable,float)'] = ('no_trigger_in_app',
  'no call site in the app source (grep G2 finds only the definitions; auto_calls has no record)',
  'SRC utils/DrawableUtils.java:44-61; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.scaleImage(Context,Drawable,int,int)'] = ('no_trigger_in_app',
  'no call site in the app source (grep G2 finds only the definitions; auto_calls has no record)',
  'SRC utils/DrawableUtils.java:28-42; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['MathUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs MathUtils; its only method is static',
  'SRC utils/MathUtils.java:26; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['MathUtils.Round'] = ('no_trigger_in_app',
  'no call site in the app source: the text "Round(" appears only in the definition (grep G2)',
  'SRC utils/MathUtils.java:28-30; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

# ---- sup: cut the auto edge from a REACHABLE caller into an UNREACHABLE method (D14)
# forceCurrentOrientation is not cut: it is REACHABLE through CurrencyListFragment.java:250.

sup(('CurrencyListActivity.onCreate', 'ActivityUtils.restoreOrientation'))  # auto_calls.json, CurrencyListActivity.java:58; the guard at line 55 is never true (see UNREACHABLE)
