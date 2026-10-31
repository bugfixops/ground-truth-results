# census of UNRESOLVED methods: creators, creation-line family, callback names (read-only over the built graph)
import json, re, collections, sys, os
BASE = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
SRCROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
g = json.load(open(BASE + '/out/anymemo_trigger_graph.json'))
verdict = g['verdict']
edges = g['edges']
def base(k): return k.split('(')[0]
def cls_meth(k):
    b = base(k); c, m = b.rsplit('.', 1); return c, m
U = [m for m, v in g['verdict'].items() if v == 'UNRESOLVED']
calls_in = collections.defaultdict(list)
for x in edges:
    calls_in[base(x['dst'])].append(x)
CALLBACK = set('''onClick onLongClick onItemClick onItemSelected onCheckedChanged onCancel onDismiss onShow onCreateLoader onLoadFinished onLoaderReset
loadInBackground onPreExecute doInBackground onPostExecute onCancelled onProgressUpdate getView getCount getItem getItemId getItemCount onBindViewHolder
onCreateViewHolder onCreateActionMode onPrepareActionMode onActionItemClicked onDestroyActionMode onQueryTextChange onQueryTextSubmit afterTextChanged
beforeTextChanged onTextChanged call run subscribe accept apply compare handleTag onInit onUtteranceCompleted onServiceConnected onServiceDisconnected
onReceive onGetViewFactory onDataSetChanged onStartCommand onBind onUnbind onRebind onDestroy onCreate onResume onPause onStop onStart onActivityResult
onCreateOptionsMenu onPrepareOptionsMenu onOptionsItemSelected onBackPressed onKeyDown onKeyUp onTouch onTouchEvent onGesturePerformed onPageFinished
onPreferenceClick onPreferenceChange onGesturePerformed onInitialized onEditorAction onFocusChange onGlobalLayout onScrolled onSingleTapUp onFling
onDrawerOpened onNavigationItemSelected onMenuItemClick onRequestPermissionsResult onAttach onDetach onViewCreated onCreateView onSaveInstanceState
onRestoreInstanceState onConfigurationChanged onHandleIntent onItemLongClick onLongClickListener onEntry onSuccess onNext onError onComplete'''.split())
def fam_of_line(text):
    t = text
    rules = [
        ('ActionMode', 'FW_ACTIONMODE'), ('LoaderCallbacks', 'FW_LOADER'), ('LoaderManager', 'FW_LOADER'),
        ('Dialog', 'FW_DIALOGFRAG'), ('AlertDialog', 'FW_DIALOGFRAG'), ('setPositiveButton', 'FW_DIALOGFRAG'),
        ('setNegativeButton', 'FW_DIALOGFRAG'), ('setNeutralButton', 'FW_DIALOGFRAG'), ('setOnCancelListener', 'FW_DIALOGFRAG'),
        ('setOnDismissListener', 'FW_DIALOGFRAG'), ('setOnItemClickListener', 'FW_VIEW'), ('OnClickListener', 'FW_VIEW'),
        ('OnLongClickListener', 'FW_VIEW'), ('TextWatcher', 'FW_VIEW'), ('Callable', 'FW_RX'), ('Observable', 'FW_RX'), ('Single', 'FW_RX'),
        ('subscribe', 'FW_RX'), ('Comparator', 'FW_SORT'), ('Runnable', 'FW_HANDLER'), ('post(', 'FW_HANDLER'), ('postDelayed', 'FW_HANDLER'),
        ('AsyncTask', 'FW_ASYNC'), ('execute(', 'FW_ASYNC'), ('ServiceConnection', 'FW_SERVICECONN'), ('OnInitListener', 'FW_TTS'),
        ('UtteranceProgressListener', 'FW_TTS'), ('OnUtteranceCompletedListener', 'FW_TTS'), ('TagHandler', 'FW_TAG'),
        ('ItemDecoration', 'FW_VIEW'), ('Adapter', 'FW_VIEW'), ('ViewHolder', 'FW_VIEW'), ('Html', 'FW_TAG'),
        ('OnCompletionListener', 'FW_MEDIAPLAYER'), ('setOnPreferenceClickListener', 'FW_PREFERENCE'),
        ('setOnPreferenceChangeListener', 'FW_PREFERENCE'), ('WebViewClient', 'FW_WEBVIEW'), ('Gesture', 'FW_GESTURE'),
        ('onGesturePerformed', 'FW_GESTURE'), ('Listener', 'FW_VIEW'), ('Callback', 'FW_VIEW'), ('Receiver', 'FW_RECEIVER'),
        ('Handler', 'FW_HANDLER'), ('new Thread', 'FW_HANDLER'), ('Thread', 'FW_HANDLER'),
    ]
    for pat, fam in rules:
        if pat in t: return fam
    return 'UNKNOWN'
def creation_text(cdst):
    # return (file, line) and text of the bytecode creation edge for class cdst, if any
    out = []
    for x in calls_in.get(cdst + '.<init>', []) if False else []:
        pass
    return out
if __name__ == '__main__':
    rows = []
    for m in U:
        c, name = cls_meth(m)
        ins = [x for x in calls_in.get(m, []) if x['kind'] != 'REGISTER']
        creators = [x['src'] for x in calls_in.get(c + '.<init>', []) if x['kind'] in ('CALL', 'ENTRY', 'LIFECYCLE', 'FRAMEWORK')]
        rows.append(dict(m=m, cls=c, name=name, incoming=len(ins), creators=sorted(set(creators))[:6],
                         cb=name in CALLBACK, outer=c.split('$')[0]))
    json.dump(rows, open(BASE + '/scratch/census.json', 'w'), indent=0)
    print('rows', len(rows))
    print('no incoming', sum(1 for r in rows if r['incoming'] == 0), 'with incoming', sum(1 for r in rows if r['incoming'] > 0))
    print('callback names', sum(1 for r in rows if r['cb']), 'init', sum(1 for r in rows if r['name'] == '<init>'))
    print('with creators', sum(1 for r in rows if r['creators']))
    print('sample', [ (r['m'], r['creators'][:2]) for r in rows if r['cb']][:8])
