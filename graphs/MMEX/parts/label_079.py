# ================================================================== batch 079 (label_079): com.money.manager.ex.home HomeFragment_MembersInjector
# (Dagger-generated, 4 methods: graphs/MMEX/scratch/batches/batch_079.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_079.md (1 REACHABLE, 3 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_079.grep.txt (sections 1-8).
# This file writes:
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor, HomeFragment_MembersInjector.java:23)
#     and of the UNREACHABLE injectMembers (to injectInfoRepositorySqlLazy, HomeFragment_MembersInjector.java:28);
#   - 3 UNREACHABLE entries: <init>, create, injectMembers (no_trigger_in_app, INFERRED from the generated class file).
# Not written: no e() or gui() edges (no destination owned by this batch needs one). The REACHABLE row for
#   injectInfoRepositorySqlLazy rests on the auto CALL record DaggerMmxComponent.injectHomeFragment -> injectInfoRepositorySqlLazy
#   (DaggerMmxComponent.java:458, D7). No CALL edges.

sup(('HomeFragment_MembersInjector.create', 'HomeFragment_MembersInjector.<init>'),
    ('HomeFragment_MembersInjector.injectMembers', 'HomeFragment_MembersInjector.injectInfoRepositorySqlLazy'))

# ================================================================== UNREACHABLE (batch 079). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['HomeFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (the generated class is in build/intermediates, label_079.grep.txt section 5). Its only caller record is create, and create has no caller: no class file names create, and the component refers only to injectInfoRepositorySqlLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record HomeFragment_MembersInjector.java:23 (label_079.grep.txt section 6); class-file parse of HomeFragment_MembersInjector.class and DaggerMmxComponent.class (sections 3, 5); label_079.grep.txt section 1',
  'INFERRED')

UNREACHABLE['HomeFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No caller: no class file references create (sections 3, 5). The component calls the static injectX method directly (DaggerMmxComponent.injectHomeFragment, DaggerMmxComponent.java:458), not create. No app source reference (section 1).',
  'class-file parse (label_079.grep.txt sections 3, 5); python-printed auto_calls query, no record with create as dst (section 6); label_079.grep.txt section 1',
  'INFERRED')

UNREACHABLE['HomeFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (HomeFragment-typed). No caller: the component refers only to injectInfoRepositorySqlLazy (section 5), and no other class file names the injector (section 3). Its only outgoing record is injectMembers -> injectInfoRepositorySqlLazy, cut by the sup pair above.',
  'python-printed auto_calls record HomeFragment_MembersInjector.java:28 (section 6); class-file parse (sections 3, 5); label_044.grep.txt line 670 (the component calls the static injectInfoRepositorySqlLazy, not injectMembers)',
  'INFERRED')
