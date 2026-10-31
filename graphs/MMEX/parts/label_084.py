# ================================================================== batch 084 (label_084): SelectDatabaseActivity_MembersInjector (4 methods), SelectDatabaseActivity_ViewBinding (7 methods: its two constructors, unbind, and the listener classes $1 and $2 with their constructors and doClick), and the 7 home event classes (one constructor each). 18 methods in all (graphs/MMEX/scratch/batches/batch_084.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_084.md (12 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_084.grep.txt (sections 1-6).
# This file writes:
#   - 1 SCREENS key: S_SELECT_DATABASE (new; see Open points in label_084.md);
#   - 1 CALL edge (cls non_standard): SelectDatabaseActivity.onCreate to the ButterKnife binding constructor (ButterKnife.bind(this), SelectDatabaseActivity.java:60; not in auto_calls.json);
#   - 2 GUI edges (cls non_standard): S_SELECT_DATABASE to $1.doClick (Create database button) and $2.doClick (Open database button);
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor) and of the UNREACHABLE injectMembers (to injectMDatabasesLazy);
#   - 6 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers (generated, INFERRED); ViewBinding.unbind (generated, INFERRED); MessageEvent.<init> and RequestOpenDatabaseEvent.<init> (app source, SOURCE).
# Not written: the ENTERS edge into S_SELECT_DATABASE (batch 083 owns SelectDatabaseActivity.onCreate). No CALL edges from auto_calls.json (D7). Routes through batches 080, 081 and 083 stay REACHABLE with the owner named (D8).

SCREENS.update({'S_SELECT_DATABASE': 'The database chooser (SelectDatabaseActivity), shown when no valid database is open: the Create database button (createDatabaseButton) and the Open database button (openDatabaseButton)'})

# ---- ButterKnife binding of SelectDatabaseActivity: the generated binding is built by reflection in ButterKnife.bind(this) (generated class not in the source root: INFERRED)

e('SelectDatabaseActivity.onCreate', 'SelectDatabaseActivity_ViewBinding.<init>(SelectDatabaseActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SelectDatabaseActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC home/SelectDatabaseActivity.java:53-60 (ButterKnife.bind(this) at 60; the return value is not kept); INFERRED ButterKnife generated binding (label_084.grep.txt sections 2, 5: the generated class is in build/intermediates, not in the source root)')

# ---- GUI edges from the database chooser page S_SELECT_DATABASE (the two buttons; ButterKnife @OnClick listeners: INFERRED)

e('S_SELECT_DATABASE', 'SelectDatabaseActivity_ViewBinding$1.doClick', 'GUI',
  'tap the Create database button: the @OnClick listener of the generated binding calls onCreateDatabaseClick, which starts PasswordActivity and then the create-file picker',
  gui=['Tap the Create database button (createDatabaseButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC home/SelectDatabaseActivity.java:99-103 (@OnClick(R.id.createDatabaseButton) at 99; onCreateDatabaseClick 100-103, startActivity at 101, showCreateFilePicker at 103); SRC res/layout/activity_select_database.xml:62-65 (createDatabaseButton at 62); auto_calls.json record (file SelectDatabaseActivity_ViewBinding.java:38) SelectDatabaseActivity_ViewBinding$1.doClick -> SelectDatabaseActivity.onCreateDatabaseClick; INFERRED ButterKnife listener')

e('S_SELECT_DATABASE', 'SelectDatabaseActivity_ViewBinding$2.doClick', 'GUI',
  'tap the Open database button: the @OnClick listener of the generated binding calls onOpenDatabaseClick, which starts PasswordActivity (the open path)',
  gui=['Tap the Open database button (openDatabaseButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC home/SelectDatabaseActivity.java:106-108 (@OnClick(R.id.openDatabaseButton) at 106; onOpenDatabaseClick 107-108, startActivity at 108); SRC res/layout/activity_select_database.xml:80-83 (openDatabaseButton at 80); auto_calls.json record (file SelectDatabaseActivity_ViewBinding.java:46) SelectDatabaseActivity_ViewBinding$2.doClick -> SelectDatabaseActivity.onOpenDatabaseClick; INFERRED ButterKnife listener')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('SelectDatabaseActivity_MembersInjector.create', 'SelectDatabaseActivity_MembersInjector.<init>'),
    ('SelectDatabaseActivity_MembersInjector.injectMembers', 'SelectDatabaseActivity_MembersInjector.injectMDatabasesLazy'))

# ================================================================== UNREACHABLE (batch 084). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['SelectDatabaseActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (the generated class is in build/intermediates, label_084.grep.txt section 4). Its only caller record is create, and create has no caller: no class file names create, and the component refers only to injectMDatabasesLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record SelectDatabaseActivity_MembersInjector.java:24 (label_084.grep.txt section 5); class-file parse of SelectDatabaseActivity_MembersInjector.class and DaggerMmxComponent.class (sections 3, 4); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No caller: no class file references create (sections 3, 4). The component calls the static injectMDatabasesLazy directly (DaggerMmxComponent.injectSelectDatabaseActivity, DaggerMmxComponent.java:426), not create. No app source reference (section 1).',
  'class-file parse (label_084.grep.txt sections 3, 4); python-printed auto_calls record DaggerMmxComponent.java:426 (section 5); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (SelectDatabaseActivity-typed). No caller: the component refers only to injectMDatabasesLazy (section 4), and no other class file names the injector (section 3). Its only outgoing record, injectMembers -> injectMDatabasesLazy, is cut by the sup pair above. The synthetic bridge injectMembers(Object) is not in this batch (open point in label_084.md).',
  'python-printed auto_calls record SelectDatabaseActivity_MembersInjector.java:29 (section 5); class-file parse (sections 3, 4); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root). ButterKnife.bind(this) at SelectDatabaseActivity.java:60 discards the returned Unbinder, SelectDatabaseActivity has no onDestroy (section 2), and no class file references unbind (0 references, section 4). No Unbinder reference exists in the app source (section 1).',
  'SRC home/SelectDatabaseActivity.java:60; label_084.grep.txt sections 1, 2, 4; python-printed auto_calls check (no record with unbind as dst, section 5)',
  'INFERRED')

UNREACHABLE['MessageEvent.<init>'] = ('no_trigger_in_app',
  'Event class with only the implicit default constructor and no body (MessageEvent.java:22-23). No app source constructs it (section 1: the class name appears only in its own file), and no class file calls MessageEvent.<init> (section 4). With no construction site, no EventBus post can deliver it.',
  'SRC home/events/MessageEvent.java:22-23; label_084.grep.txt sections 1, 4, 5',
  'SOURCE')

UNREACHABLE['RequestOpenDatabaseEvent.<init>'] = ('no_trigger_in_app',
  'Event class with only the implicit default constructor and no body (RequestOpenDatabaseEvent.java:22-23). No app source constructs it (section 1: the class name appears in its own file, the import at MainActivity.java:86, and the subscriber at MainActivity.java:470), and no class file calls RequestOpenDatabaseEvent.<init> (sections 3, 4). The subscriber MainActivity.onEvent(RequestOpenDatabaseEvent) therefore has no post site in the app (open point in label_084.md).',
  'SRC home/events/RequestOpenDatabaseEvent.java:22-23; SRC home/MainActivity.java:86, 469-472; label_084.grep.txt sections 1, 3, 4',
  'SOURCE')
