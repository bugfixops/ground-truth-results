# ================================================================== batch 133 (label_133): transactions.EditTransactionCommonFunctions_MembersInjector (5 methods), EditTransactionViewHolder (1), EditTransactionViewHolder_ViewBinding (2), IntentDataParameters (3), SplitCategoriesActivity (18), SplitCategoriesActivity$1 (2), SplitCategoriesActivity_ViewBinding (3), SplitCategoriesActivity_ViewBinding$1 (2); 36 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_133.md (31 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence, with the printed output of each grep for a generated or library claim: graphs/MMEX/parts/label_133.grep.txt.
# This file writes 18 e() edges (INTENT 1, LIFECYCLE 2, ENTERS 1, FRAMEWORK 1, GUI 3, RESULT 2, REGISTER 3, ASYNC 3, CALL 2), 0 gui() edges, 5 UNREACHABLE entries and 3 sup pairs.
# Edges are written only where the destination is owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# Callers outside this batch are interim (D8): the owner of EditTransactionCommonFunctions.showSplitCategoriesForm is not merged; CategoryListFragment.setResult and CalculatorActivity.returnResult are in common/; the three EventBus posters are in SplitCategoriesAdapter (batch 134); the route through HomeFragment.onEvent(AmountEnteredEvent) is batch 024 (AGENT_NOTES D14(b)); CheckingTransactionEditActivity and RecurringTransactionEditActivity are not merged.
# S_SPLIT_CATEGORIES is defined here, because no split screen key existed (grep G12 in label_133.grep.txt). Batch 134 may reuse it.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source or library was not read (EventBus, ButterKnife, AppCompat, Dagger generated code beyond the auto_calls records).

SCREENS.update({
    'S_SPLIT_CATEGORIES': 'Split categories form (SplitCategoriesActivity): one row per split with its amount, category, transaction type and notes; the add button; the save icon in the action bar; the invalid amount dialog',
})

# ---- entry, lifecycle and screen edges

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitCategoriesActivity.<init>', 'INTENT',
  'startActivityForResult(new Intent(getContext(), SplitCategoriesActivity.class), RequestCodes.SPLIT_TX) with the split rows, currency and transaction type as extras',
  gui=['Tap the split button on the transaction edit form while the transaction is not split yet', 'Tap the category field on the transaction edit form while the transaction is already split'],
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); the category field takes the split branch (EditTransactionCommonFunctions.java:462-469)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1519-1528 (intent 1519; startActivityForResult 1528); 598-605 (split button listener; showSplitCategoriesForm at 605); 455-469 (category field listener; showSplitCategoriesForm at 469, reached through access$700 per auto_calls.json); SRC transactions/SplitCategoriesActivity.java:57 (auto_calls.json record to MmxBaseFragmentActivity.<init>); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity creates the instance through newInstance at 1174); FW-SRC core/java/android/app/ActivityThread.java:2667-2671 (newActivity at 2669-2670). INTERIM: the owner of showSplitCategoriesForm is not merged (D8)')

e('SplitCategoriesActivity.<init>', 'SplitCategoriesActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6989-7000 (performCreate calls onCreate at 6997 and 6999)')

e('SplitCategoriesActivity.onCreate', 'S_SPLIT_CATEGORIES', 'ENTERS',
  'the split categories form is shown',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView R.layout.activity_split_categories); SRC res/layout/activity_split_categories.xml:68-69 (the fab view)')

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='SRC transactions/SplitCategoriesActivity.java:108-115 (onCreateOptionsMenu; addSaveToolbarIcon at 112); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:626-633 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3392 (onCreateOptionsMenu at 3388); INFERRED: the activity extends the AppCompat base, and the AppCompat delegate path to onCreatePanelMenu is not in fw_src and was not read')

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread.callCallActivityOnSaveInstanceState calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); SRC transactions/SplitCategoriesActivity.java:180-189 (body)')

# ---- GUI edges from the screen

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item; the save item calls onActionDoneClick',
  gui=['Tap the save (check) icon in the action bar of the split categories form'],
  evidence='SRC transactions/SplitCategoriesActivity.java:112 (addSaveToolbarIcon), 117-123 (onOptionsItemSelected; MenuHelper.save at 119-120 returns onActionDoneClick); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the AppCompat dispatch from the action bar to onOptionsItemSelected is not in fw_src')

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity_ViewBinding$1.doClick', 'GUI',
  'the user taps the add button (R.id.fab): the generated @OnClick listener calls onFabClick, which adds a split row',
  gui=['Tap the add (floating action) button on the split categories form'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated SplitCategoriesActivity_ViewBinding (INFERRED: the ButterKnife library and the generated code are not read beyond the auto_calls.json record at line 36)',
  evidence='SRC transactions/SplitCategoriesActivity.java:191-194 (@OnClick(R.id.fab) onFabClick); SRC res/layout/activity_split_categories.xml:68-69 (fab id); auto_calls.json record SplitCategoriesActivity_ViewBinding$1.doClick -> SplitCategoriesActivity.onFabClick (SplitCategoriesActivity_ViewBinding.java:36)')

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity$1.onClick', 'GUI',
  'the user taps OK in the invalid amount dialog: the dialog closes through dialog.dismiss',
  gui=['Tap OK in the invalid amount dialog after a negative amount was returned for a split row'],
  needs_state=state_text('a negative amount is returned from the calculator for a split row, so showInvalidAmountDialog runs (SplitCategoriesActivity.java:276-278)', ('data',)),
  evidence='SRC transactions/SplitCategoriesActivity.java:317-329 (showInvalidAmountDialog: setPositiveButton(android.R.string.ok) with the listener at 321; onClick 323-326; dismiss at 325; show at 328); SRC transactions/SplitCategoriesActivity.java:20 (import android.app.AlertDialog: the framework dialog); SRC transactions/SplitCategoriesActivity.java:276-279 (negative amount gate); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (mButtonPositive.setOnClickListener(mButtonHandler)), 125-146 (mButtonHandler click message at 140), 160-166 (handleMessage calls the OnClickListener at 166)')

# ---- ButterKnife binding (generated classes; the library is not read: INFERRED, D22)

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity_ViewBinding.<init>(SplitCategoriesActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handler and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SplitCategoriesActivity_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC transactions/SplitCategoriesActivity.java:52 (import butterknife.ButterKnife), 101 (ButterKnife.bind(this); the returned Unbinder is discarded); label_133.grep.txt G5 and G6 (build class SplitCategoriesActivity_ViewBinding.class); label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

e('EditTransactionViewHolder.<init>', 'EditTransactionViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, view) builds the generated binding for this view holder',
  cls='non_standard', via='ButterKnife.bind(this, view) (library): reflection builds EditTransactionViewHolder_ViewBinding (INFERRED, library not read)',
  evidence='SRC transactions/EditTransactionViewHolder.java:37 (import butterknife.ButterKnife), 45 (ButterKnife.bind(this, view); the returned Unbinder is discarded); label_133.grep.txt G5 and G6; label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

# ---- EventBus: the activity subscribes in the base onStart, the three posters are in batch 134 (library dispatch: INFERRED)

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(AmountEntryRequestedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(AmountEntryRequestedEvent) at SplitCategoriesActivity.java:205-211 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (onStart at 134, register at 141, unregister at 146); SRC transactions/SplitCategoriesActivity.java:205-211 (@Subscribe and body); INFERRED: EventBus library source not read')

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(CategoryRequestedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(CategoryRequestedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(CategoryRequestedEvent) at SplitCategoriesActivity.java:213-216 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146; SRC transactions/SplitCategoriesActivity.java:213-216 (@Subscribe and body); INFERRED: EventBus library source not read')

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(SplitItemRemovedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(SplitItemRemovedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(SplitItemRemovedEvent) at SplitCategoriesActivity.java:200-203 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146; SRC transactions/SplitCategoriesActivity.java:200-203 (@Subscribe and body); INFERRED: EventBus library source not read')

e('SplitCategoriesAdapter$1.onClick', 'SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'ASYNC',
  'the user taps the amount of a split row: the listener posts AmountEntryRequestedEvent and EventBus calls onEvent, which opens the calculator for that row',
  cls='non_standard', via='EventBus (greenrobot): post(AmountEntryRequestedEvent) to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:161 (txtAmount.setOnClickListener), 174 (EventBus.getDefault().post(new AmountEntryRequestedEvent(...))); SRC transactions/SplitCategoriesActivity.java:205-211 (subscriber); the adapter belongs to batch 134 and its listener is not labelled here; INFERRED: EventBus library dispatch not read')

e('SplitCategoriesAdapter$2.onClick', 'SplitCategoriesActivity.onEvent(CategoryRequestedEvent)', 'ASYNC',
  'the user taps the category of a split row: the listener posts CategoryRequestedEvent and EventBus calls onEvent, which opens the category selector',
  cls='non_standard', via='EventBus (greenrobot): post(CategoryRequestedEvent) to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:180 (txtSelectCategory.setOnClickListener), 185 (post of CategoryRequestedEvent); SRC transactions/SplitCategoriesActivity.java:213-216 (subscriber); INFERRED: EventBus library dispatch not read')

e('SplitCategoriesAdapter.onItemDismiss', 'SplitCategoriesActivity.onEvent(SplitItemRemovedEvent)', 'ASYNC',
  'a row is swiped away: the item touch callback calls onItemDismiss, which posts SplitItemRemovedEvent, and EventBus calls onEvent, which removes the row',
  cls='non_standard', via='ItemTouchHelper callback (library) calls onItemDismiss; EventBus post to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:252-255 (onItemDismiss; post of SplitItemRemovedEvent at 255); SRC transactions/SplitCategoriesActivity.java:200-203 (subscriber); SRC transactions/SplitCategoriesActivity.java:271 (SplitItemTouchCallback created in initRecyclerView, auto_calls.json); INFERRED: the ItemTouchHelper dispatch to onItemDismiss is library code and was not read')

# ---- result edges (startActivityForResult from this activity; the result is set in another class)

e('CategoryListFragment.setResult', 'SplitCategoriesActivity.onActivityResult', 'RESULT',
  'the category list returns the checked category: setResult(RESULT_OK, result) and finish, and the framework calls onActivityResult with REQUEST_PICK_CATEGORY',
  guard='requestCode is REQUEST_PICK_CATEGORY (SplitCategoriesActivity.java:131) and resultCode is RESULT_OK with data non-null (SplitCategoriesActivity.java:129); the RESULT_OK branch needs ACTION_PICK and a checked category (CategoryListFragment.java:314, 324, 351-354)',
  evidence='SRC common/CategoryListFragment.java:313-359 (protected setResult; ACTION_PICK at 314; checked category at 321-324; RESULT_OK at 354; RESULT_CANCELED at 356); SRC common/BaseListFragment.java:177-180 (setResultAndFinish calls setResult at 178, then finish); SRC transactions/SplitCategoriesActivity.java:69 (REQUEST_PICK_CATEGORY = 1), 314 (startActivityForResult with REQUEST_PICK_CATEGORY); FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults calls dispatchActivityResult at 4264-4265); FW-SRC core/java/android/app/Activity.java:7259-7266 (onActivityResult at 7266)')

e('CalculatorActivity.returnResult', 'SplitCategoriesActivity.onActivityResult', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult with the row request code plus the amount offset',
  guard='requestCode >= amountRequestOffset (SplitCategoriesActivity.java:142) and resultCode is RESULT_OK with data non-null (SplitCategoriesActivity.java:129); the request code is the row request id plus 1000 (SplitCategoriesActivity.java:79, 207-210; Calculator.java:79 passes it to startActivityForResult)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC transactions/SplitCategoriesActivity.java:79 (amountRequestOffset = 1000), 207-210 (Calculator show with event.requestId + amountRequestOffset); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (build class transactions/EditTransactionCommonFunctions_MembersInjector.class, not in the source root). Its only caller record is EditTransactionCommonFunctions_MembersInjector.create (auto_calls.json, line 31), and create has no caller record (the auto_calls query in label_133.grep.txt shows 0 incoming records). The app source has no reference to the MembersInjector name (grep G2)',
  'auto_calls.json record EditTransactionCommonFunctions_MembersInjector.java:31; label_133.grep.txt G2, G3 and the auto_calls query',
  'INFERRED')

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json: the name occurs only as the source of records, never as a destination (0 incoming records). The app source has no MembersInjector reference (grep G2)',
  'label_133.grep.txt G2, G3 and the auto_calls query (0 incoming records)',
  'INFERRED')

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record for any receiver in auto_calls.json (0 incoming records). The component calls the static injectors directly (DaggerMmxComponent.java:569 and 571), not injectMembers',
  'auto_calls.json records DaggerMmxComponent.java:569, 571; label_133.grep.txt G2, G3 and the auto_calls query (0 incoming records)',
  'INFERRED')

UNREACHABLE['EditTransactionViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated Unbinder method (build class EditTransactionViewHolder_ViewBinding.class defines it; grep G4). The constructor is called from EditTransactionViewHolder.<init> at line 45, which discards the returned binding, so no unbind call exists. The transactions/ source has no unbind (grep G1), and no auto_calls.json record has unbind as a source or destination (0 records)',
  'SRC transactions/EditTransactionViewHolder.java:45; label_133.grep.txt G1, G4 and the unbind query (0 records)',
  'INFERRED')

UNREACHABLE['SplitCategoriesActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated Unbinder method (build class SplitCategoriesActivity_ViewBinding.class defines it; grep G4). The constructor is called from SplitCategoriesActivity.onCreate at line 101, which discards the returned binding, and SplitCategoriesActivity declares no onDestroy (grep G13). The transactions/ source has no unbind (grep G1), and no auto_calls.json record has unbind as a source or destination (0 records)',
  'SRC transactions/SplitCategoriesActivity.java:101; label_133.grep.txt G1, G4, G13 and the unbind query (0 records)',
  'INFERRED')

# ---- auto edges that cannot run: cut the exact edge only (D14); the MembersInjector injectors stay reachable through DaggerMmxComponent

sup(('EditTransactionCommonFunctions_MembersInjector.create', 'EditTransactionCommonFunctions_MembersInjector.<init>'))  # create has no caller, so the bytecode call at auto_calls.json line 31 cannot run
sup(('EditTransactionCommonFunctions_MembersInjector.injectMembers', 'EditTransactionCommonFunctions_MembersInjector.injectDateTimeUtilsLazy'))  # injectMembers has no caller; auto_calls.json line 38
sup(('EditTransactionCommonFunctions_MembersInjector.injectMembers', 'EditTransactionCommonFunctions_MembersInjector.injectMDatabases'))  # injectMembers has no caller; auto_calls.json line 37
