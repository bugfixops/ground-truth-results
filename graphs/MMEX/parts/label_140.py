# ================================================================== batch 140 (label_140): utils and view classes, 38 methods in 7 classes
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_140.md (31 REACHABLE, 7 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_140.grep.txt.
# This file writes 1 e() edge (CALL, non_standard: the Provider hop from a Lazy<MmxDateTimeUtils> read to MmxDateTimeUtils_Factory.get), 0 gui() edges, 7 UNREACHABLE entries and 2 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# Dagger: MmxDateTimeUtils_Factory.get is the Provider behind the Lazy<MmxDateTimeUtils> fields (D16). It is REACHABLE because app code reads those Lazy fields from REACHABLE methods (precedent: batch 036 FormatUtilities_Factory.get, batch 047 CurrencyService_Factory.get). The generated classes are INFERRED (D5).
# D14a: the two DateDisplay constructors are UNREACHABLE, so their auto CALL records into DateDisplay.initialize are cut with sup.
# Not written: the TipsDialogFragment.onCreateDialog -> MmxFileUtils.getRawAsString record (TipsDialogFragment.java:100). Its source is a batch 074 method, not a batch 140 method, and getRawAsString stays REACHABLE through 13 other callers. See label_140.grep.txt Q5 and the report.
# Not written: the cuts of DaggerMmxComponent.injectEditPriceDialog into MmxDateTimeUtils_Factory.<clinit> and .create (AGENT_NOTES lines 345, 357). Their source is not a batch 140 method, and both destinations are REACHABLE.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- Dagger Provider get (Lazy<MmxDateTimeUtils> read in EditTransactionCommonFunctions.getUserDateFormat)

e('EditTransactionCommonFunctions.getUserDateFormat', 'MmxDateTimeUtils_Factory.get', 'CALL',
  'getUserDateFormat calls dateTimeUtilsLazy.get() (the Lazy<MmxDateTimeUtils> field); the Lazy is a DoubleCheck around the factory, which calls its provider get()',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:113 (@Inject Lazy<MmxDateTimeUtils> field), 1405 (dateTimeUtilsLazy.get().getUserDatePattern inside getUserDateFormat, auto record); auto_calls.json record DaggerMmxComponent.java:572 (injectEditTransactionCommonFunctions calls MmxDateTimeUtils_Factory.create; the generated source is not under final_java_only, grep Q4); INFERRED: generated DoubleCheck and Factory code not read (D5); label_140.grep.txt Q4',
  cls='non_standard',
  via='DoubleCheck around the generated Lazy<MmxDateTimeUtils> built by DaggerMmxComponent; its provider is the MmxDateTimeUtils_Factory instance')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_140.grep.txt, sections Q1-Q3)

UNREACHABLE['MmxFileUtils.copy'] = ('no_trigger_in_app',
  'No caller. The public static method is never called in the app source: the name occurs only at its declaration (BudgetService.copy(int) is a different method). No auto record has it as dst',
  'SRC utils/MmxFileUtils.java:59; grep Q2 (copy( search over the source root); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['MmxFileUtils.getContext'] = ('no_trigger_in_app',
  'No caller. The only MmxFileUtils instance is built at SelectDatabaseActivity.java:63 and only requestExternalStoragePermissions is called on it (line 64). No line calls getContext() on an MmxFileUtils receiver; requestPermission reads the field directly (MmxFileUtils.java:158). No auto record has it as dst',
  'SRC utils/MmxFileUtils.java:131; SRC home/SelectDatabaseActivity.java:63-64; grep Q2 (fileUtils and MmxFileUtils search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['NotificationUtils.<init>'] = ('no_trigger_in_app',
  'No caller. There is no new NotificationUtils in the source root (the only textual hit is a comment at SmsReceiverTransactions.java:1063), and the class has only static members, so the implicit constructor is never called. No auto record has it as dst',
  'SRC utils/NotificationUtils.java:35-90 (static members only); grep Q2 (new NotificationUtils search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['SpinnerHelper.<init>'] = ('no_trigger_in_app',
  'No caller. There is no new SpinnerHelper in the source root, and the class has only the static getPosition method, so the implicit constructor is never called. No auto record has it as dst',
  'SRC utils/SpinnerHelper.java:25-40 (static method only); grep Q2 (new SpinnerHelper search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['DateDisplay.<init>(Context)'] = ('no_trigger_in_app',
  'No caller. There is no new DateDisplay in the source root (the constructor lines are declarations). The only layout reference to the class is commented out (activity_price_edit.xml:144-149), and so is the @BindView field (EditPriceViewHolder.java:39). No layout names the class, so LayoutInflater.createView (FW-SRC LayoutInflater.java:592-615) never builds it',
  'SRC view/DateDisplay.java:32; SRC res/layout/activity_price_edit.xml:144-149 (commented); SRC investment/EditPriceViewHolder.java:39 (commented); FW-SRC core/java/android/view/LayoutInflater.java:592-615; grep Q2, Q3',
  'SOURCE')

UNREACHABLE['DateDisplay.<init>(Context,AttributeSet)'] = ('no_trigger_in_app',
  'No caller. Same as DateDisplay.<init>(Context): no new DateDisplay in the source root and no layout tag names the class (the commented XML at activity_price_edit.xml:144-149). The three-argument constructor at DateDisplay.java:38-42 is commented out',
  'SRC view/DateDisplay.java:44, 38-42 (commented); SRC res/layout/activity_price_edit.xml:144-149 (commented); FW-SRC core/java/android/view/LayoutInflater.java:592-615; grep Q2, Q3',
  'SOURCE')

UNREACHABLE['DateDisplay.initialize'] = ('no_trigger_in_app',
  'Its only callers are the two constructors (DateDisplay.java:35 and 52), and both are UNREACHABLE. R.layout.control_datedisplay (DateDisplay.java:61) is used nowhere else in the source root',
  'SRC view/DateDisplay.java:35, 52, 55-61; grep Q2, Q3; Q1 (2 incoming, both from the UNREACHABLE constructors)',
  'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is an UNREACHABLE batch 140 method and whose destination is batch 140 (DateDisplay.initialize)

sup(('DateDisplay.<init>(Context)', 'DateDisplay.initialize'))  # the constructor has no caller, so its call to initialize cannot run
sup(('DateDisplay.<init>(Context,AttributeSet)', 'DateDisplay.initialize'))  # same
