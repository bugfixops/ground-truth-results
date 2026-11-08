# ================================================================== batch 006 (label_006): com.money.manager.ex.account.AccountEditActivity (40 of its 52 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_006.md.
# Every edge below has a batch 006 method as its destination (or is the ENTERS edge to the screen this batch defines).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

SCREENS.update({
    'S_ACCOUNT_EDIT': 'Account edit form (AccountEditActivity): account fields, the type and status spinners, the favourite and default toggles, save and cancel',
})

# ---- entry and intent edges into the activity

e('S_ENTRY', 'AccountEditActivity.<init>', 'ENTRY',
  'another app sends an ACTION_EDIT or ACTION_INSERT intent to the exported AccountEditActivity',
  env=env_text('outside package: another app sends an ACTION_EDIT or ACTION_INSERT intent to AccountEditActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:227-234; FW-SRC core/java/android/app/ActivityThread.java:2665-2670; FW-SRC core/java/android/app/Instrumentation.java:1143-1148; how the framework matches an implicit intent to this filter is not printed: INFERRED, source not read')

e('HomeFragment.onContextItemSelected', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Open the context menu of an account on the home screen and choose Edit'],
  guard='the menu title equals R.string.edit (HomeFragment.java:462)',
  evidence='SRC home/HomeFragment.java:450-469 (account check 455; EDIT check 462; intent 463-466; startActivity 466)')

e('HomeFragment$3.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with ACTION_INSERT',
  gui=['Tap the add account button (R.id.buttonAddAccount) on the welcome view'],
  needs_state=state_text('the account list is empty, so the welcome view with the add account button is shown (HomeFragment.java:793-794)', ('account',)),
  evidence='SRC home/HomeFragment.java:611-623 (btnAddAccount listener 614-622; intent 618-620); SRC home/HomeFragment.java:790-796 (welcome view visible when the list is empty, 793-794)')

e('WatchlistFragment$7.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the goto-account icon (R.id.imageViewGotoAccount) in the watchlist header'],
  evidence='SRC investment/watchlist/WatchlistFragment.java:572-581 (listener 573-581; intent 576-579)')

e('FilterDialogFragment$3.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the edit button (R.id.editButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:164-176 (editButton listener 168-175; intent 171-174)')

e('AccountTransactionListFragment$2.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the goto-account icon (R.id.imageViewGotoAccount) in the account transaction list header'],
  evidence='SRC account/AccountTransactionListFragment.java:534-544 (listener 536-544; intent 539-542)')

e('AccountListFragment.startAccountListEditActivity(Integer)', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(intent) with KEY_ACCOUNT_ID and ACTION_EDIT, when accountId is not null',
  gui=['Open the context menu of an account in the account list and choose Edit'],
  guard='accountId is not null (AccountListFragment.java:306); the EDIT case is at AccountListFragment.java:127-128',
  evidence='SRC account/AccountListFragment.java:115-130 (EDIT case 127-128); SRC account/AccountListFragment.java:302-314 (intent 304; EDIT 306-308; startActivity 313)')

e('AccountListFragment.startAccountListEditActivity(Integer)', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(intent) with ACTION_INSERT, when accountId is null',
  gui=['Tap the add (floating action) button on the account list'],
  guard='accountId is null (AccountListFragment.java:309-310); reached from onFloatingActionButtonClicked (250-251) through the no-argument overload (293-294)',
  evidence='SRC account/AccountListFragment.java:248-253 (onFloatingActionButtonClicked 250-251); SRC account/AccountListFragment.java:291-314 (no-argument overload 293-294; INSERT 309-310; startActivity 313)')

# ---- lifecycle, framework, screen and result edges

e('AccountEditActivity.<init>', 'AccountEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('AccountEditActivity.onCreate', 'S_ACCOUNT_EDIT', 'ENTERS',
  'the account edit form is shown',
  evidence='SRC account/AccountEditActivity.java:138 (setContentView R.layout.activity_account_edit)')

e('AccountEditActivity.onCreate', 'AccountEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388)')

e('AccountEditActivity.onCreate', 'AccountEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused: ActivityThread.performPauseActivity calls callCallActivityOnSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/ActivityThread.java:4713-4722; FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1501 (onSaveInstanceState at 1496)')

e('CurrencyListFragment.setResult', 'AccountEditActivity.onActivityResult', 'RESULT',
  'the currency list returns the checked currency and finishes: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='requestCode is RequestCodes.CURRENCY and resultCode is RESULT_OK (AccountEditActivity.java:150, 153); pick mode with a checked row (CurrencyListFragment.java:300-305)',
  evidence='SRC currency/list/CurrencyListFragment.java:298-320 (checked row loop 304-306; RESULT_OK at 314); SRC currency/list/CurrencyListFragment.java:330-341 (onListItemClick calls setResultAndFinish at 339); SRC common/BaseListFragment.java:177-180 (setResultAndFinish calls setResult and finish); SRC account/AccountEditActivity.java:393-395 (startActivityForResult with RequestCodes.CURRENCY); FW-SRC core/java/android/app/ActivityThread.java:4253-4264 (deliverResults calls dispatchActivityResult at 4264); FW-SRC core/java/android/app/Activity.java:7259-7266 (onActivityResult at 7266)')

e('CalculatorActivity.returnResult', 'AccountEditActivity.onActivityResult', 'RESULT',
  'the calculator returns the amount (save menu or equals key) and finishes: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='requestCode is RequestCodes.AMOUNT and resultCode is RESULT_OK (AccountEditActivity.java:150, 168-169)',
  evidence='SRC common/CalculatorActivity.java:435-445 (setResult RESULT_OK and finish at 443-444); SRC common/CalculatorActivity.java:145-150 (save menu calls returnResult at 149) and 247-250 (equals key calls returnResult at 249); SRC common/Calculator.java:77-83 (startActivityForResult at 79); SRC account/AccountEditActivity.java:304-307 (Calculator show with RequestCodes.AMOUNT); FW-SRC core/java/android/app/ActivityThread.java:4253-4264; FW-SRC core/java/android/app/Activity.java:7259-7266')

# ---- GUI edges from the screen

e('S_ACCOUNT_EDIT', 'AccountEditActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item (MenuHelper.save)',
  gui=['Tap the save (check) icon in the action bar'],
  evidence='SRC core/MenuHelper.java:37, 87-92 (save item added at 88); SRC account/AccountEditActivity.java:177-182 (menu built at 179); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$1.onClick', 'GUI',
  'the calculator opens for the initial balance: Calculator.show(RequestCodes.AMOUNT)',
  gui=['Tap the initial balance amount (txtInitialBalance)'],
  evidence='SRC account/AccountEditActivity.java:301-309 (listener 301; onClick 303-308; Calculator show 304-307)')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$2.onItemSelected', 'GUI',
  'an account type is picked in the account type spinner: mAccount.setType(...)',
  gui=['Choose an account type in the account type spinner'],
  guard='position is in range of mAccountTypeValues (AccountEditActivity.java:359)',
  evidence='SRC account/AccountEditActivity.java:356-364 (listener 356; onItemSelected 358-364); FW-SRC core/java/android/widget/Spinner.java:1184-1186 (drop-down click calls setSelection); FW-SRC core/java/android/widget/AdapterView.java:903-922 (selectionChanged dispatches the selection); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected at 944); the setSelection path in AdapterView and AbsSpinner is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$3.onItemSelected', 'GUI',
  'an account status is picked in the status spinner: mAccount.setStatus(...)',
  gui=['Choose an account status (Open or Closed) in the status spinner'],
  guard='position is in range of mAccountStatusValues (AccountEditActivity.java:375)',
  evidence='SRC account/AccountEditActivity.java:372-380 (listener 372; onItemSelected 374-380); FW-SRC core/java/android/widget/Spinner.java:1184-1186; FW-SRC core/java/android/widget/AdapterView.java:903-922, 937-949; the setSelection path in AdapterView and AbsSpinner is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$10.onClick', 'GUI',
  'the favourite flag is toggled: setFavorite(!getFavorite()) and displayFavouriteStatus',
  gui=['Tap the favourite star icon (imageViewAccountFav)', 'Tap the favourite label (favouriteAccountTextView)'],
  evidence='SRC account/AccountEditActivity.java:531-542 (listener 532-539; onClick 535-538; setOnClickListener 540-541)')

# ---- Icepick (generated helper; the library is not in the dataset)

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper AccountEditActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC account/AccountEditActivity.java:59, 87, 92 (import and @State fields); the icepick library and its reflection are not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State fields (mCurrencyName, mIsDefault)',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC account/AccountEditActivity.java:87, 92 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'AccountEditActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State fields (mCurrencyName, mIsDefault)',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:152-156 (Icepick.saveInstanceState at 155); SRC account/AccountEditActivity.java:87, 92 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

sup(('MmxBaseFragmentActivity$1.onClick', 'AccountEditActivity.onActionCancelClick'))  # the cancel listener is registered only by CurrencyEditActivity (BudgetsActivity's toolbar.xml has no action_cancel), never on an AccountEditActivity

UNREACHABLE['AccountEditActivity.onActionCancelClick'] = (
  'no_trigger_in_app',
  'Overrides MmxBaseFragmentActivity.onActionCancelClick. The only app caller is the cancel listener that showStandardToolbarActions(View,int,int) registers (MmxBaseFragmentActivity.java:213-219). This activity does not register that listener: the call at AccountEditActivity.java:140 is commented out. The other callers of showStandardToolbarActions (CurrencyEditActivity.java:83, BudgetsActivity.java:48) belong to other activities. The cancel code in MmxBaseFragmentActivity.onOptionsItemSelected (118-122) is commented out, and the home branch (109-116) finishes the activity without calling it. No in-app route remains.',
  'account/AccountEditActivity.java:138-141, 212-216; common/MmxBaseFragmentActivity.java:107-131, 209-219; currency/CurrencyEditActivity.java:83; budget/BudgetsActivity.java:48',
  'SOURCE')

UNREACHABLE['AccountEditActivity$2.onNothingSelected'] = (
  'branch_never_taken',
  'AdapterView.fireOnSelected calls onNothingSelected only when the selected position is negative (AdapterView.java:941-947). The account type spinner gets its adapter from the fixed, non-empty accounttype_items array (7 items, arrays.xml:76-84) at AccountEditActivity.java:317, and the only setSelection call uses a position found in the value list (AccountEditActivity.java:319-321). The AbsSpinner and AdapterView.setSelection code is not printed (source not read), so the claim that a non-empty spinner always gets a valid selection is INFERRED.',
  'account/AccountEditActivity.java:317, 319-321, 356-370 (onNothingSelected 368-369); res/values/arrays.xml:76-84; FW-SRC core/java/android/widget/AdapterView.java:937-949',
  'INFERRED')

UNREACHABLE['AccountEditActivity$3.onNothingSelected'] = (
  'branch_never_taken',
  'Same reason for the account status spinner: fireOnSelected calls onNothingSelected only for a negative selected position (AdapterView.java:941-947). The adapter is set from fixed, non-empty arrays (accountstatus_items, 2 items, arrays.xml:91-94; accountstatus_values, arrays.xml:87-90) at AccountEditActivity.java:331-333, and the only setSelection call uses an index found in the value list (AccountEditActivity.java:336-337). The AbsSpinner and AdapterView.setSelection code is not printed (source not read): INFERRED.',
  'account/AccountEditActivity.java:331-337, 372-385 (onNothingSelected 383-384); res/values/arrays.xml:87-94; FW-SRC core/java/android/widget/AdapterView.java:937-949',
  'INFERRED')
