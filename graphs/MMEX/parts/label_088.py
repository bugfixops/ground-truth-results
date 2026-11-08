# ================================================================== batch 088 (label_088): PriceCsvExport (5 methods), PriceCsvParser (3), PriceEditActivity (15), PriceEditActivity_MembersInjector (4), PriceEditActivity_ViewBinding (11: its two constructors, unbind, and the listener classes $1 to $4 with constructor and doClick), PriceEditModel (2). 40 methods in all (graphs/MMEX/scratch/batches/batch_088.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_088.md (35 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_088.grep.txt (sections 1-6).
# This file writes:
#   - 1 SCREENS key: S_PRICE_EDIT (new; no S_PRICE* or S_WATCH* key exists in graph_def.py or the parts);
#   - 13 e() edges: 1 INTENT into PriceEditActivity.<init> (from WatchlistItemsFragment.onContextItemSelected, no auto record: the Intent is built from a class literal); 1 LIFECYCLE <init> -> onCreate; 1 ENTERS onCreate -> S_PRICE_EDIT; 1 CALL (cls non_standard) onCreate -> ViewBinding.<init>(PriceEditActivity) (ButterKnife.bind(this), PriceEditActivity.java:70; not in auto_calls.json); 1 FRAMEWORK onCreate -> onCreateOptionsMenu; 1 LIFECYCLE onCreate -> onSaveInstanceState; 6 GUI edges from S_PRICE_EDIT (the four ButterKnife listeners $1 to $4, cls non_standard; the save icon -> onOptionsItemSelected; the date dialog listener lambda, cls non_standard); 1 RESULT CalculatorActivity.returnResult -> PriceEditActivity.onActivityResult;
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor) and of the UNREACHABLE injectMembers (to injectDateTimeUtilsLazy);
#   - 5 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers and ViewBinding.unbind (generated, INFERRED, grep.txt sections 3-4); PriceCsvParser.getContext (app source, SOURCE).
# Not written: no CALL edge that is already in auto_calls.json (D7). The route into the watchlist (batches 092 and 094, not merged) stays interim (D8).

SCREENS.update({'S_PRICE_EDIT': 'The security price editor (PriceEditActivity), opened from the watchlist item context menu (Edit price): the amount field (amountTextView) opens the calculator, the date field (dateTextView) opens a date dialog, the previous and next day buttons change the date, and the save icon in the toolbar (MenuHelper.save) saves the price'})

# ---- PriceEditActivity: entry, lifecycle and the generated ButterKnife binding

e('WatchlistItemsFragment.onContextItemSelected', 'PriceEditActivity.<init>', 'INTENT',
  'the Edit price context-menu item builds an Intent for PriceEditActivity (IntentFactory.getPriceEditIntent) and starts it with startActivityForResult; the framework then creates the activity by reflection',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:240-253 (EditPrice case; getPriceEditIntent at 245; startActivityForResult at 253); SRC core/IntentFactory.java:80-83 (new Intent(context, PriceEditActivity.class)); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity: cl.loadClass(className).newInstance()); the watchlist route is interim (batches 092 and 094, not merged, D8)')

e('PriceEditActivity.<init>', 'PriceEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity (Instrumentation.callActivityOnCreate, then Activity.performCreate)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2669 (newActivity), 2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6997 and 6999)')

e('PriceEditActivity.onCreate', 'S_PRICE_EDIT', 'ENTERS',
  'setContentView(R.layout.activity_price_edit) shows the price editor (PriceEditActivity.java:66)',
  evidence='SRC investment/PriceEditActivity.java:66 (setContentView); res/layout/activity_price_edit.xml:27 (appbar), 77 (priceEditorScrollView); auto_calls.json record PriceEditActivity.onCreate -> MmxBaseFragmentActivity.setContentView (PriceEditActivity.java:66, exact)')

e('PriceEditActivity.onCreate', 'PriceEditActivity_ViewBinding.<init>(PriceEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated PriceEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC investment/PriceEditActivity.java:70 (ButterKnife.bind(this); the return value is not kept); label_088.grep.txt section 4 (no class file has a Methodref to the one-argument constructor; PriceEditActivity.class holds only the ButterKnife.bind call)')

e('PriceEditActivity.onCreate', 'PriceEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (the save icon is added there)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); the AppCompat toolbar path is a library (not read, INFERRED)')

e('PriceEditActivity.onCreate', 'PriceEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused with saveState set (same shape as AccountEditActivity.onCreate -> onSaveInstanceState, graph_def.py:622): ActivityThread.performPauseActivity calls callCallActivityOnSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (performPauseActivity; callCallActivityOnSaveInstanceState at 3875 when saveState is set and the activity is not finished); FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState calls Instrumentation); FW-SRC core/java/android/app/Instrumentation.java:1385-1386')

# ---- GUI edges from the price editor page S_PRICE_EDIT (ButterKnife @OnClick listeners: INFERRED; the handlers are auto CALL records)

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the amount field: the @OnClick listener of the generated binding calls onPriceClick, which opens the calculator for the price',
  gui=['Tap the amount field (amountTextView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:135-141 (@OnClick(R.id.amountTextView) at 135; onPriceClick 136-141); SRC res/layout/activity_price_edit.xml:219 (amountTextView); auto_calls.json record PriceEditActivity_ViewBinding.java:40 ($1.doClick -> onPriceClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the date field: the @OnClick listener of the generated binding calls onDateClick, which opens the date dialog',
  gui=['Tap the date field (dateTextView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:143-162 (@OnClick(R.id.dateTextView) at 143; onDateClick 144-162); SRC res/layout/activity_price_edit.xml:176 (dateTextView); auto_calls.json record PriceEditActivity_ViewBinding.java:48 ($2.doClick -> onDateClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$3.doClick', 'GUI',
  'tap the previous day button: the @OnClick listener of the generated binding calls onPreviousDayClick, which moves the date back one day and redisplays the page',
  gui=['Tap the previous day button (previousDayButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:164-169 (@OnClick(R.id.previousDayButton) at 164; onPreviousDayClick 165-169); SRC res/layout/activity_price_edit.xml:152 (previousDayButton); auto_calls.json record PriceEditActivity_ViewBinding.java:56 ($3.doClick -> onPreviousDayClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$4.doClick', 'GUI',
  'tap the next day button: the @OnClick listener of the generated binding calls onNextDayClick, which moves the date forward one day and redisplays the page',
  gui=['Tap the next day button (nextDayButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:171-176 (@OnClick(R.id.nextDayButton) at 171; onNextDayClick 172-176); SRC res/layout/activity_price_edit.xml:187 (nextDayButton); auto_calls.json record PriceEditActivity_ViewBinding.java:64 ($4.doClick -> onNextDayClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity.onOptionsItemSelected', 'GUI',
  'tap the save icon in the toolbar (MenuHelper.save): save() writes the price and its history, then setResult(RESULT_OK) and finish()',
  gui=['Tap the save icon in the toolbar (MenuHelper.save)'],
  evidence='SRC investment/PriceEditActivity.java:101-109 (onCreateOptionsMenu; addSaveToolbarIcon at 106); SRC investment/PriceEditActivity.java:111-126 (onOptionsItemSelected; case MenuHelper.save at 118; save() at 120; setResult at 121; finish at 122); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

e('S_PRICE_EDIT', 'PriceEditActivity.lambda$onDateClick$0', 'GUI',
  'tap the date field, then pick a date and tap OK in the date dialog: the dialog calls the OnDateSetListener lambda, which stores the new date and redisplays the page',
  gui=['Tap the date field (dateTextView), then pick a date and tap OK in the date dialog'],
  cls='non_standard', via='DatePickerDialog (framework): its positive button calls the OnDateSetListener (FW-SRC core/java/android/app/DatePickerDialog.java:122 and 164-171); the dialog is shown inside this page (D9)',
  evidence='SRC investment/PriceEditActivity.java:143-150 (onDateClick; DatePickerDialog listener lambda at 147-150); SRC investment/PriceEditActivity.java:21 import android.app.DatePickerDialog; FW-SRC core/java/android/app/DatePickerDialog.java:122 (positive button set to this), 164-171 (onClick; positive case 166; mDateSetListener.onDateSet at 171); auto_calls.json lambdas record PriceEditActivity.java:147 (onDateClick -> lambda$onDateClick$0; a different source, kept)')

# ---- RESULT: the calculator returns the amount to this activity

e('CalculatorActivity.returnResult', 'PriceEditActivity.onActivityResult', 'RESULT',
  'CalculatorActivity.returnResult (called at CalculatorActivity.java:149 and 249) sets the result and finishes; the framework delivers the result to the caller, which calls onActivityResult (framework delivery not read, INFERRED)',
  guard='resultCode is not RESULT_CANCELED and data is not null (PriceEditActivity.java:90, otherwise return); requestCode must be RequestCodes.AMOUNT (line 94); the AMOUNT branch reads the amount (95) and redisplays the page (97)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult; setResult(AppCompatActivity.RESULT_OK, result) at 443; finish at 444); SRC common/Calculator.java:77-81 (show(requestCode) calls activity.startActivityForResult at 79); SRC investment/PriceEditActivity.java:87-99 (onActivityResult); framework delivery of the result not read (INFERRED)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('PriceEditActivity_MembersInjector.create', 'PriceEditActivity_MembersInjector.<init>'),
    ('PriceEditActivity_MembersInjector.injectMembers', 'PriceEditActivity_MembersInjector.injectDateTimeUtilsLazy'))

# ================================================================== UNREACHABLE (batch 088). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['PriceEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes the Provider). Its only caller record is create (auto_calls.json, PriceEditActivity_MembersInjector.java:23), and create has no caller: no class file has a Methodref to create, and the component (the only other class that names the injector) refers only to the static injectDateTimeUtilsLazy. The app source has no reference to the class.',
  'python-printed class-file parse of PriceEditActivity_MembersInjector.class (label_088.grep.txt section 4: METHODS list, Methodref hits); grep of the app source root (section 1); auto_calls.json record PriceEditActivity_MembersInjector.java:23 (section 5)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (flags 0x9). No caller: no class file has a Methodref to create (label_088.grep.txt section 4). The component calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.injectPriceEditActivity, DaggerMmxComponent.java:410), not create. No app source reference (section 1).',
  'class-file parse (label_088.grep.txt section 4); auto_calls.json record DaggerMmxComponent.java:410 (section 5); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (flags 0x1, takes the PriceEditActivity). No caller: no class file has a Methodref to it (section 4), and the component refers only to the static injectDateTimeUtilsLazy. Its only outgoing record, injectMembers -> injectDateTimeUtilsLazy (PriceEditActivity_MembersInjector.java:28), is cut by the sup pair above. The synthetic bridge injectMembers(Object) (flags 0x1041) is not in this batch (open point in label_088.md).',
  'class-file parse (label_088.grep.txt section 4: METHODS list and Methodref hits); auto_calls.json record PriceEditActivity_MembersInjector.java:28 (section 5)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (flags 0x1, generated class only). ButterKnife.bind(this) at PriceEditActivity.java:70 discards the returned Unbinder, PriceEditActivity has no onDestroy, and no class file has a Methodref to unbind (section 4). No Unbinder reference exists in the app source (section 1), and no auto_calls.json record has unbind as dst (section 5).',
  'SRC investment/PriceEditActivity.java:70; label_088.grep.txt sections 1, 4, 5',
  'INFERRED')

UNREACHABLE['PriceCsvParser.getContext'] = ('no_trigger_in_app',
  'Public getter (PriceCsvParser.java:48-50) with no caller. The only use of the parser in app source is YahooCsvQuoteDownloaderRetrofit.java:113-116 (new PriceCsvParser(getContext()), then parser.parse(content)), and nothing asks the parser for its context. No Methodref to PriceCsvParser.getContext exists in any build class file (section 4), and auto_calls.json has no record with it as dst (section 5).',
  'SRC investment/PriceCsvParser.java:48-50; SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:113-116; label_088.grep.txt sections 2, 4, 5',
  'SOURCE')
