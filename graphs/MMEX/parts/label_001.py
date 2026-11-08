# batch 001: HelpActivity (3 methods) and the generated data-binding classes (16 methods).
# Edges and UNREACHABLE entries only. Rows and printed lines: graphs/MMEX/parts/label_001.md.
# Every edge below has a batch 001 method as its destination.

SCREENS.update({
    'S_HELP': 'Help page (HelpActivity): a WebView showing a help page from a raw file or a URL, opened by another app',
})

# ---- HelpActivity
e('S_ENTRY', 'HelpActivity.<init>', 'ENTRY',
  'another app starts the exported HelpActivity with the custom action WEB_VIEW_URL or WEB_VIEW_RAW_FILE and a file: URI',
  env=env_text('outside package: another app sends an intent with the custom action WEB_VIEW_URL or WEB_VIEW_RAW_FILE and a file: URI to the exported HelpActivity (AndroidManifest.xml:301-313)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:301-313; FW-SRC core/java/android/app/Instrumentation.java:1170-1175; FW-SRC core/java/android/app/ActivityThread.java:2669-2670; intent matching (IntentFilter) is not in fw_src: INFERRED, source not read')

e('HelpActivity.<init>', 'HelpActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='SRC HelpActivity.java:36-38; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/ActivityThread.java:2729-2731; FW-SRC core/java/android/app/Activity.java:6989-6999')

e('HelpActivity.onCreate', 'S_HELP', 'ENTERS',
  'the help page is shown: onCreate loads the raw file or the URL from the intent into the WebView',
  evidence='SRC HelpActivity.java:36-64')

e('HelpActivity.onCreate', 'HelpActivity.onKeyDown', 'FRAMEWORK',
  'the help page is in front and the user presses Back: the framework dispatches the key-down event to onKeyDown',
  gui=['Press Back while the help page is shown'],
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3274; FW-SRC core/java/android/view/KeyEvent.java:2684-2692; SRC HelpActivity.java:66-75')

# ---- data-binding library and generated classes: no trigger in the app
UNREACHABLE['databinding.DataBinderMapperImpl.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the data-binding library generated subclass of MergedDataBinderMapper. It is created only by the library DataBindingUtil, which no app class references, and no res layout has a <layout> root. Library source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 35-44, 75; auto_calls.json:4-13',
  'INFERRED')

UNREACHABLE['baseAdapters.BR.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the library constants class androidx.databinding.library.baseAdapters.BR. Its fields are constants; only its own class file mentions it and no source file mentions baseAdapters. Library class: source not read, so this is INFERRED.',
  'label_001.grep.txt:21-22, 52-53, 73',
  'INFERRED')

UNREACHABLE['ex.BR.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated com.money.manager.ex.BR constants class. BudgetViewModel reads BR.year, name and month as constants and never constructs BR; no auto_calls.json edge reaches ex.BR.<init>. Generated class: source not read, so this is INFERRED.',
  'BudgetViewModel.java:23, 81-94; label_001.grep.txt:9-20, 54-56, 72',
  'INFERRED')

UNREACHABLE['Constants.<init>'] = (
  'no_trigger_in_app',
  'Constants has only literal static final fields and no explicit constructor. No new Constants and no Constants() call exists in the source, and no auto_calls.json edge reaches Constants.<init>.',
  'Constants.java:17-56; label_001.grep.txt:24-26',
  'SOURCE')

sup(('databinding.DataBinderMapperImpl.<init>', 'ex.DataBinderMapperImpl.<clinit>'),
    ('databinding.DataBinderMapperImpl.<init>', 'ex.DataBinderMapperImpl.<init>'),
    ('ex.DataBinderMapperImpl.getLayoutId', 'ex.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'),
    ('ex.DataBinderMapperImpl.convertBrIdToString', 'ex.DataBinderMapperImpl$InnerBrLookup.<clinit>'))  # these callers are UNREACHABLE, so the bytecode calls cannot run

UNREACHABLE['ex.DataBinderMapperImpl.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the generated mapper. It runs only on first use of the mapper class; the only bytecode route is the androidx mapper constructor (auto_calls.json:4-5), which needs DataBindingUtil, and no app code uses it. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:4-5; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated mapper, called only from the androidx mapper constructor (auto_calls.json:12-13), which is reached only through the library DataBindingUtil (no app code uses it). Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:12-13; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.collectDependencies'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No auto_calls.json caller edge, and no app source or class file calls it; it is reached only through the library mapper machinery, which needs DataBindingUtil. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json (no caller edge); label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.convertBrIdToString'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No caller edge in auto_calls.json; its only outgoing edge is InnerBrLookup.<clinit> (lines 1150-1151). It is reached only through the library mapper machinery, which needs DataBindingUtil. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)'] = (
  'no_trigger_in_app',
  'Method of the generated mapper, called only by the library DataBindingUtil binding calls (inflate or bind). No app code calls those, and no auto_calls.json caller edge exists. Generated class: source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 39-44; auto_calls.json (no caller edge)',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)'] = (
  'no_trigger_in_app',
  'Second overload of the generated mapper getDataBinder, called only by the library DataBindingUtil binding calls (inflate or bind). No app code calls those, and no auto_calls.json caller edge exists. Generated class: source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 39-44; auto_calls.json (no caller edge)',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getLayoutId'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No caller edge in auto_calls.json; its only outgoing edge is InnerLayoutIdLookup.<clinit> (lines 1142-1143). It is reached only through the library DataBindingUtil, which no app code uses. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerBrLookup.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the nested BR lookup. The only edge into it is the call from convertBrIdToString (auto_calls.json:1150-1151), which has no app caller. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerBrLookup.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the nested BR lookup. No edge in the auto_calls.json calls section reaches it; the only edge into the lookup is the <clinit> call at line 1151. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the nested layout-id lookup. The only edge into it is the call from getLayoutId (auto_calls.json:1142-1143), which has no app caller. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerLayoutIdLookup.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the nested layout-id lookup. No edge in the auto_calls.json calls section reaches it; the only edge into the lookup is the <clinit> call at line 1143. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['DataBindingTriggerClass.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated marker class that carries the BindingBuildInfo annotation. No source file and no other app class file mentions it, and no auto_calls.json edge reaches it. Library and generated class: source not read, so the claim that no code instantiates it is INFERRED.',
  'label_001.grep.txt:32-33, 45-46, 74',
  'INFERRED')
