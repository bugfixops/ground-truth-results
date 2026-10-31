# batch 005: WebChangelogFragment (5 methods), the Changelog tab of the About screen. Edges only; rows and printed lines: graphs/MMEX/parts/label_005.md.
# The bytecode CALL edges AboutTabAdapter.getItem -> newInstance, newInstance -> <init> and onCreateView -> loadChangelog are in auto_calls.json, so none is written here (D7).
# No UNREACHABLE entry: all five methods have a route. The Changelog tab has no page of its own (the About screen is S_ABOUT_ACTIVITY, part 004), so no new page and no ENTERS edge.

e('WebChangelogFragment.<init>', 'WebChangelogFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor, when the Changelog fragment is added to the tab pager',
  evidence='SRC about/WebChangelogFragment.java:39-41, 58-66; INFERRED androidx Fragment lifecycle calls onCreate after the constructor (androidx source not read)')

e('WebChangelogFragment.onCreate', 'WebChangelogFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC about/WebChangelogFragment.java:58-77; INFERRED androidx Fragment lifecycle calls onCreateView after onCreate (androidx source not read)')
