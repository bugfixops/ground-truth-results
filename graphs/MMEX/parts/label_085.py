# ================================================================== batch 085 (label_085): EditPriceDialog (11 methods), EditPriceDialog$$Icepick (4), EditPriceDialog$1 to $7 (15 methods: constructors and callbacks), EditPriceDialog_MembersInjector (4), EditPriceViewHolder (3) and EditPriceViewHolder_ViewBinding (2). 39 methods in all (graphs/MMEX/scratch/batches/batch_085.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_085.md (3 REACHABLE, 36 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_085.grep.txt (sections 1-10).
# This file writes:
#   - 1 CALL edge (cls non_standard): EditPriceViewHolder.bind(AppCompatActivity) to EditPriceViewHolder_ViewBinding.<init> (ButterKnife.bind(this, activity) at EditPriceViewHolder.java:53; no auto_calls.json record, so no D7 duplicate);
#   - 66 sup pairs (D14a): 65 auto CALL records whose caller is UNREACHABLE in this batch, and the cross-batch cut DaggerMmxComponent.injectEditPriceDialog -> EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy (AGENT_NOTES.md line 307: batch 085 owns it; the batch 044 caller is UNREACHABLE);
#   - 36 UNREACHABLE entries.
# Not written here: the records of PriceEditActivity.onCreate (lines 80-81) stay, because they make the holder REACHABLE (route through batch 088, interim per D8); the cuts of injectEditPriceDialog -> MmxDateTimeUtils_Factory.<clinit> and .create belong to batch 140; the cut of DaggerMmxComponent.inject(EditPriceDialog) -> injectEditPriceDialog is in label_043.py.

# ---- REACHABLE: the holder's constructor and bind(AppCompatActivity), by auto CALL records from PriceEditActivity.onCreate (batch 088, not merged)
# ---- and the ButterKnife binding constructor, which has no auto record (generated class, built by reflection)

e('EditPriceViewHolder.bind(AppCompatActivity)', 'EditPriceViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, activity) builds the generated binding for the holder, which binds the @BindView fields of the activity',
  cls='non_standard', via='ButterKnife.bind(this, activity) (library): the generated EditPriceViewHolder_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC investment/EditPriceViewHolder.java:52-54 (ButterKnife.bind at 53); SRC investment/EditPriceViewHolder.java:28-29 (butterknife imports); label_085.grep.txt section 6 (ButterKnife.bind call sites), section 10 (the generated class is in build/intermediates; no class file names it except itself)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(
    # EditPriceDialog$$Icepick.<clinit>: cut here (AGENT_NOTES.md line 315; label_041 PriceDownloadedEventBundler.<init> stays UNREACHABLE)
    ('EditPriceDialog$$Icepick.<clinit>', 'PriceDownloadedEventBundler.<init>'),
    # EditPriceDialog$5.onClick, $6.onClick, $4.onClick, $4.lambda$onClick$0 (date and day buttons, date picker)
    ('EditPriceDialog$5.onClick', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$5.onClick', 'MmxDate.toDate'),
    ('EditPriceDialog$5.onClick', 'MmxDate.minusDays'),
    ('EditPriceDialog$5.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$6.onClick', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$6.onClick', 'MmxDate.toDate'),
    ('EditPriceDialog$6.onClick', 'MmxDate.plusDays'),
    ('EditPriceDialog$6.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getDayOfMonth'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getMonthOfYear'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getYear'),
    ('EditPriceDialog$4.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$4.lambda$onClick$0', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$4.lambda$onClick$0', 'MmxDate.toDate'),
    ('EditPriceDialog$4.lambda$onClick$0', 'MmxDate.<init>(int,int,int)'),
    # EditPriceDialog$7.onClick (amount listener; the 4-argument AmountInputDialog.getInstance stays reached through other overloads, see label_023)
    ('EditPriceDialog$7.onClick', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'),
    # EditPriceDialog$1.get (formatUtilitiesLazy)
    ('EditPriceDialog$1.get', 'FormatUtilities.<init>(Context)'),
    # EditPriceDialog.<init>: cut the cha-dispatch record to the Dagger member injector (AGENT_NOTES.md line 307)
    ('EditPriceDialog.<init>', 'MmexApplication.<clinit>'),
    ('EditPriceDialog.<init>', 'EditPriceDialog$1.<init>'),
    ('EditPriceDialog.<init>', 'DaggerMmxComponent.inject(EditPriceDialog)'),
    ('EditPriceDialog.<init>', 'MmexApplication.getApp'),
    # EditPriceDialog.onCreateDialog
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.create'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.showCurrentPrice'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.showDate'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setNegativeButton'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog$3.<init>'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setPositiveButton'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog$2.<init>'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.initializeControls'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceViewHolder.bind(View)'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceViewHolder.<init>'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setView'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setIcon'),
    ('EditPriceDialog.onCreateDialog', 'UIHelper.getIcon'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setTitle(CharSequence)'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.<init>'),
    ('EditPriceDialog.onCreateDialog', 'UIHelper.<init>'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.createNewEntity'),
    # EditPriceDialog.onEvent, createNewEntity, getUserDateFormat, initializeControls, showCurrentPrice, showDate
    ('EditPriceDialog.onEvent', 'EditPriceDialog.showCurrentPrice'),
    ('EditPriceDialog.createNewEntity', 'PriceDownloadedEvent.<init>'),
    ('EditPriceDialog.createNewEntity', 'MmxDate.toDate'),
    ('EditPriceDialog.createNewEntity', 'MmxDate.<init>(String)'),
    ('EditPriceDialog.getUserDateFormat', 'MmxDateTimeUtils.getUserDatePattern'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$7.<init>'),
    ('EditPriceDialog.initializeControls', 'Account.getCurrencyId'),
    ('EditPriceDialog.initializeControls', 'AccountRepository.load'),
    ('EditPriceDialog.initializeControls', 'AccountRepository.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$6.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$5.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog.showDate'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$4.<init>'),
    ('EditPriceDialog.showCurrentPrice', 'FormatUtilities.format(Money,String)'),
    ('EditPriceDialog.showDate', 'MmxDateTimeUtils.format'),
    ('EditPriceDialog.showDate', 'EditPriceDialog.getUserDateFormat'),
    ('EditPriceDialog.showDate', 'MmxDateTimeUtils.<init>()'),
    # EditPriceDialog_MembersInjector.create and injectMembers (their callee records are internal to the UNREACHABLE injector)
    ('EditPriceDialog_MembersInjector.create', 'EditPriceDialog_MembersInjector.<init>'),
    ('EditPriceDialog_MembersInjector.injectMembers', 'EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'),
    # EditPriceDialog$2.onClick (positive button): addStockHistoryRecord(PriceDownloadedEvent) cut per D14c (AGENT_NOTES.md line 328)
    ('EditPriceDialog$2.onClick', 'SyncManager.<clinit>'),
    ('EditPriceDialog$2.onClick', 'SyncManager.dataChanged'),
    ('EditPriceDialog$2.onClick', 'SyncManager.<init>'),
    ('EditPriceDialog$2.onClick', 'StockHistoryRepository.addStockHistoryRecord(PriceDownloadedEvent)'),
    ('EditPriceDialog$2.onClick', 'StockHistoryRepository.<init>'),
    ('EditPriceDialog$2.onClick', 'StockRepository.updateCurrentPrice'),
    ('EditPriceDialog$2.onClick', 'StockRepository.<init>'),
    # cross-batch cut owned by batch 085 (AGENT_NOTES.md line 307); the caller row is label_044
    ('DaggerMmxComponent.injectEditPriceDialog', 'EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'),
)

# ================================================================== UNREACHABLE (batch 085). Tuple: (kind, reason, evidence, confirmed_by)
# Shared basis for the dialog family: the app source never constructs EditPriceDialog (see the entry for its constructor).

UNREACHABLE['EditPriceDialog.<init>'] = ('no_trigger_in_app',
  'Constructor of the DialogFragment. The app source never constructs EditPriceDialog: the only construction (WatchlistItemsFragment.java:255) is commented out, its show call (WatchlistItemsFragment.java:263) is commented out too, and MmxComponent.java:90 declares only the members injection inject(EditPriceDialog), which needs an instance. PriceEditActivity uses only the ARG_ constants (PriceEditActivity.java:198-204).',
  'SRC investment/EditPriceDialog.java:89-99; SRC investment/watchlist/WatchlistItemsFragment.java:255-263; SRC core/ioc/MmxComponent.java:90; label_085.grep.txt sections 1, 2',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onCreateDialog'] = ('no_trigger_in_app',
  'DialogFragment callback. The framework calls it only on a live instance, and none is created (see the constructor). Its callees, including EditPriceViewHolder.bind(View), are unreached from here. EditPriceViewHolder.<init> stays REACHABLE through PriceEditActivity.',
  'SRC investment/EditPriceDialog.java:103-154; auto_calls record EditPriceDialog.java:122 (bind(View)); label_085.grep.txt sections 1, 9',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onStart'] = ('no_trigger_in_app',
  'Fragment lifecycle callback. It needs a live instance, so the EventBus registration at EditPriceDialog.java:160 never runs.',
  'SRC investment/EditPriceDialog.java:157-161; label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onStop'] = ('no_trigger_in_app',
  'Fragment lifecycle callback. It needs a live instance, so the EventBus unregistration at EditPriceDialog.java:167 never runs.',
  'SRC investment/EditPriceDialog.java:164-168; label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onSaveInstanceState'] = ('no_trigger_in_app',
  'Fragment callback. It needs a live instance, so Icepick.saveInstanceState(this, ...) at EditPriceDialog.java:174 never runs.',
  'SRC investment/EditPriceDialog.java:170-175; label_085.grep.txt sections 1, 5',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onEvent'] = ('no_trigger_in_app',
  '@Subscribe handler for AmountEnteredEvent. EventBus delivers only to registered subscribers, and this instance registers only in onStart (EditPriceDialog.java:160), which needs an instance. The handler is therefore never called, even though the event type is reachable elsewhere.',
  'SRC investment/EditPriceDialog.java:157-161, 177-181; auto_calls record EditPriceDialog.java:180 (showCurrentPrice); label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.createNewEntity'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:107), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:107, 187-194; auto_calls record EditPriceDialog.java:107',
  'SOURCE')

UNREACHABLE['EditPriceDialog.getUserDateFormat'] = ('no_trigger_in_app',
  'Private helper, called only from showDate (EditPriceDialog.java:274), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:196-201, 274; auto_calls record EditPriceDialog.java:274',
  'SOURCE')

UNREACHABLE['EditPriceDialog.initializeControls'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:123), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:123, 203-266; auto_calls record EditPriceDialog.java:123',
  'SOURCE')

UNREACHABLE['EditPriceDialog.showCurrentPrice'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:151) and onEvent (EditPriceDialog.java:180), both unreached.',
  'SRC investment/EditPriceDialog.java:151, 180, 268-271; auto_calls records EditPriceDialog.java:151, 180',
  'SOURCE')

UNREACHABLE['EditPriceDialog.showDate'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:150), initializeControls (EditPriceDialog.java:230) and the listeners at EditPriceDialog.java:213, 237 and 244, all unreached.',
  'SRC investment/EditPriceDialog.java:150, 213, 230, 237, 244, 273-275; auto_calls records EditPriceDialog.java:150, 230, 237, 244',
  'SOURCE')

# ---- Icepick helper (generated; not in the source root; reached only through Icepick reflection on the dialog instance)

UNREACHABLE['EditPriceDialog$$Icepick.<clinit>'] = ('no_trigger_in_app',
  'Generated Icepick helper static initializer. Icepick uses the helper only from Icepick.restoreInstanceState and saveInstanceState (EditPriceDialog.java:105, 174), which run on an instance that is never created. Its only record is <clinit> -> PriceDownloadedEventBundler.<init> (EditPriceDialog$$Icepick.java:16), which is cut here.',
  'auto_calls record EditPriceDialog$$Icepick.java:16; SRC investment/EditPriceDialog.java:105, 174; label_085.grep.txt sections 3, 5, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.<init>'] = ('no_trigger_in_app',
  'Generated helper constructor. No caller: no source file names the helper, no auto_calls record targets it, and no other class file names it (section 10).',
  'label_085.grep.txt sections 4, 9, 10; class file build/intermediates EditPriceDialog$$Icepick.class (section 3)',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.restore'] = ('no_trigger_in_app',
  'Generated helper method. Icepick calls it from Icepick.restoreInstanceState(this, bundle) (EditPriceDialog.java:105) in onCreateDialog, which runs only on an instance that is never created. No record names restore.',
  'SRC investment/EditPriceDialog.java:103-106; label_085.grep.txt sections 5, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.save'] = ('no_trigger_in_app',
  'Generated helper method. Icepick calls it from Icepick.saveInstanceState(this, bundle) (EditPriceDialog.java:174) in onSaveInstanceState, which runs only on an instance that is never created. No record names save.',
  'SRC investment/EditPriceDialog.java:170-175; label_085.grep.txt sections 5, 9, 10',
  'INFERRED')

# ---- anonymous classes and lambda of the dialog (SOURCE: created only inside the unreached dialog methods)

UNREACHABLE['EditPriceDialog$1.<init>'] = ('no_trigger_in_app',
  'Anonymous Lazy for formatUtilitiesLazy, created in the dialog constructor (EditPriceDialog.java:93), which is unreached.',
  'SRC investment/EditPriceDialog.java:87, 89-99; auto_calls record EditPriceDialog.java:93',
  'SOURCE')

UNREACHABLE['EditPriceDialog$1.get'] = ('no_trigger_in_app',
  'Lazy.get of formatUtilitiesLazy, called only from showCurrentPrice (EditPriceDialog.java:269), which is unreached.',
  'SRC investment/EditPriceDialog.java:93-98, 268-271; auto_calls record EditPriceDialog.java:96',
  'SOURCE')

UNREACHABLE['EditPriceDialog$2.<init>'] = ('no_trigger_in_app',
  'Anonymous listener for the positive button, created in onCreateDialog (EditPriceDialog.java:126), which is unreached.',
  'SRC investment/EditPriceDialog.java:126-142; auto_calls record EditPriceDialog.java:126',
  'SOURCE')

UNREACHABLE['EditPriceDialog$2.onClick'] = ('no_trigger_in_app',
  'Positive-button listener (EditPriceDialog.java:127-141). Its only entry is onCreateDialog, which is unreached, so the price update and history record (addStockHistoryRecord at line 134) are dead here. Its records are cut in this file (D14a); the cut of the addStockHistoryRecord(PriceDownloadedEvent) record is D14c (AGENT_NOTES.md line 328).',
  'SRC investment/EditPriceDialog.java:126-142; auto_calls records EditPriceDialog.java:130-140; label_057.py (addStockHistoryRecord(PriceDownloadedEvent) is UNREACHABLE there)',
  'SOURCE')

UNREACHABLE['EditPriceDialog$3.<init>'] = ('no_trigger_in_app',
  'Anonymous listener for the negative button, created in onCreateDialog (EditPriceDialog.java:143), which is unreached.',
  'SRC investment/EditPriceDialog.java:143-148; auto_calls record EditPriceDialog.java:143',
  'SOURCE')

UNREACHABLE['EditPriceDialog$3.onClick'] = ('no_trigger_in_app',
  'Negative-button listener (EditPriceDialog.java:145-147). The dialog is never built, so it never runs.',
  'SRC investment/EditPriceDialog.java:143-148',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.<init>'] = ('no_trigger_in_app',
  'Anonymous date-field listener, created in initializeControls (EditPriceDialog.java:206), which is unreached.',
  'SRC investment/EditPriceDialog.java:203-206; auto_calls record EditPriceDialog.java:206',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.onClick'] = ('no_trigger_in_app',
  'Date-field click listener (EditPriceDialog.java:207-226). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:206-227; auto_calls records EditPriceDialog.java:209, 219-221',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.lambda$onClick$0'] = ('no_trigger_in_app',
  'Synthetic lambda for the DatePickerDialog listener (EditPriceDialog.java:211-214). It is created only inside EditPriceDialog$4.onClick, which is unreached.',
  'SRC investment/EditPriceDialog.java:211-214; auto_calls records EditPriceDialog.java:212-213',
  'SOURCE')

UNREACHABLE['EditPriceDialog$5.<init>'] = ('no_trigger_in_app',
  'Anonymous previous-day listener, created in initializeControls (EditPriceDialog.java:233), which is unreached.',
  'SRC investment/EditPriceDialog.java:233-239; auto_calls record EditPriceDialog.java:233',
  'SOURCE')

UNREACHABLE['EditPriceDialog$5.onClick'] = ('no_trigger_in_app',
  'Previous-day listener (EditPriceDialog.java:235-238). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:233-239; auto_calls records EditPriceDialog.java:236-237',
  'SOURCE')

UNREACHABLE['EditPriceDialog$6.<init>'] = ('no_trigger_in_app',
  'Anonymous next-day listener, created in initializeControls (EditPriceDialog.java:240), which is unreached.',
  'SRC investment/EditPriceDialog.java:240-246; auto_calls record EditPriceDialog.java:240',
  'SOURCE')

UNREACHABLE['EditPriceDialog$6.onClick'] = ('no_trigger_in_app',
  'Next-day listener (EditPriceDialog.java:242-245). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:240-246; auto_calls records EditPriceDialog.java:243-244',
  'SOURCE')

UNREACHABLE['EditPriceDialog$7.<init>'] = ('no_trigger_in_app',
  'Anonymous amount-field listener, created in initializeControls (EditPriceDialog.java:256), which is unreached.',
  'SRC investment/EditPriceDialog.java:256-265; auto_calls record EditPriceDialog.java:256',
  'SOURCE')

UNREACHABLE['EditPriceDialog$7.onClick'] = ('no_trigger_in_app',
  'Amount-field listener (EditPriceDialog.java:258-263). Its only entry is initializeControls, which is unreached, so this route to AmountInputDialog.getInstance (line 259) is dead. The 4-argument getInstance stays reached through other overloads (AmountInputDialog.java:64-83; see label_085.grep.txt section 9 and the report to the orchestrator).',
  'SRC investment/EditPriceDialog.java:256-265; auto_calls record EditPriceDialog.java:259; label_085.grep.txt section 9',
  'SOURCE')

# ---- Dagger member injector of EditPriceDialog (generated; INFERRED: class file in build/intermediates, no source)

UNREACHABLE['EditPriceDialog_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (EditPriceDialog_MembersInjector.java:23), and create has no caller (see create below).',
  'auto_calls record EditPriceDialog_MembersInjector.java:23; label_085.grep.txt sections 3, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No auto_calls record targets create, and the component calls injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:488), not create. Its callee record (EditPriceDialog_MembersInjector.java:23) is cut here.',
  'auto_calls records EditPriceDialog_MembersInjector.java:23, DaggerMmxComponent.java:488; label_085.grep.txt sections 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance member injector. No auto_calls record targets injectMembers, and the component calls only injectDateTimeUtilsLazy (DaggerMmxComponent.java:488). Its callee record (EditPriceDialog_MembersInjector.java:28) is cut here.',
  'auto_calls records EditPriceDialog_MembersInjector.java:28, DaggerMmxComponent.java:488; label_085.grep.txt sections 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'] = ('no_trigger_in_app',
  'Dagger-generated static member injector for dateTimeUtilsLazy. Its callers are DaggerMmxComponent.injectEditPriceDialog (DaggerMmxComponent.java:488; UNREACHABLE in label_044) and injectMembers (no caller). The record from injectEditPriceDialog is cut here (sup). injectEditPriceDialog is unreached because inject(EditPriceDialog) has no reached caller (label_043 and label_044).',
  'auto_calls records DaggerMmxComponent.java:488, EditPriceDialog_MembersInjector.java:28; label_043.py; label_044.py',
  'INFERRED')

# ---- EditPriceViewHolder: bind(View) is unreached; the constructor and bind(AppCompatActivity) are REACHABLE (above)

UNREACHABLE['EditPriceViewHolder.bind(View)'] = ('no_trigger_in_app',
  'Called only from EditPriceDialog.onCreateDialog (auto_calls record EditPriceDialog.java:122), which is unreached. No other record names bind(View) with another caller, and the ButterKnife call for this overload is only at EditPriceViewHolder.java:49.',
  'SRC investment/EditPriceViewHolder.java:48-50; auto_calls record EditPriceDialog.java:122; label_085.grep.txt sections 6, 7, 9',
  'SOURCE')

# ---- EditPriceViewHolder_ViewBinding.unbind (generated; nothing calls it)

UNREACHABLE['EditPriceViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'Generated unbind. Nothing calls it: ButterKnife.bind(this, activity) at EditPriceViewHolder.java:53 does not keep the Unbinder, and no auto_calls record targets unbind for this class.',
  'SRC investment/EditPriceViewHolder.java:52-54; label_085.grep.txt sections 6, 9, 10',
  'INFERRED')
