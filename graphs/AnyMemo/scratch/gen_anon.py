"""Generate framework edges creator -> callback for unresolved methods of anonymous classes (section M)."""
import csv,json,re,os,collections
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
SRCROOT='/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
amap=json.load(open(G+'/scratch/anon_map2.json'))
types=json.load(open(G+'/scratch/anon_types.json'))
verdict={r['method']:r['verdict'] for r in csv.DictReader(open(G+'/out/methods.csv',encoding='utf-8'))}
# creator per anon class from listeners.txt
creator={}
for l in open(G+'/scratch/listeners.txt',encoding='utf-8'):
    p=l.rstrip('\n').split(' | ')
    if len(p)<4: continue
    cls=p[0].rsplit('.',1)[0]
    m=re.match(r'(\S+) \[',p[1])
    if m and cls not in creator: creator[cls]=m.group(1)
CB={ # callback method names by interface simple name
 'DialogInterface.OnClickListener':['onClick'],'DialogInterface.OnCancelListener':['onCancel'],
 'View.OnClickListener':['onClick'],'View.OnLongClickListener':['onLongClick'],'View.OnTouchListener':['onTouch'],
 'View.OnFocusChangeListener':['onFocusChange'],'View.OnSystemUiVisibilityChangeListener':['onSystemUiVisibilityChange'],
 'CompoundButton.OnCheckedChangeListener':['onCheckedChanged'],'RadioGroup.OnCheckedChangeListener':['onCheckedChanged'],
 'OnSeekBarChangeListener':['onProgressChanged','onStartTrackingTouch','onStopTrackingTouch'],
 'TextWatcher':['beforeTextChanged','onTextChanged','afterTextChanged'],
 'Runnable':['run'],'Thread':['run'],'Callable<Void>':['call'],
 'Consumer<File>':['accept'],'Consumer<Throwable>':['accept'],'io.reactivex.functions.Consumer<File>':['accept'],
 'MaybeOnSubscribe<File>':['subscribe'],'Comparator<CardWrapper>':['compare'],'Comparator<String>':['compare'],
 'Comparator<DownloadItem>':['compare'],'Comparator<Category>':['compare'],
 'View.OnTouchListener':['onTouch'],'AdapterView.OnItemLongClickListener':['onItemLongClick'],
 'OnItemClickListener':['onItemClick'],'AdapterView.OnItemClickListener':['onItemClick'],
 'PopupMenu.OnMenuItemClickListener':['onMenuItemClick'],'SearchView.OnQueryTextListener':['onQueryTextSubmit','onQueryTextChange'],
 'NavigationView.OnNavigationItemSelectedListener':['onNavigationItemSelected'],
 'BottomNavigationView.OnNavigationItemSelectedListener':['onNavigationItemSelected'],
 'Preference.OnPreferenceClickListener':['onPreferenceClick'],'OnCompletionListener':['onCompletion'],
 'OnCompletedListener':['onCompleted'],'AnyMemoTTS.OnTextToSpeechCompletedListener':['onTextToSpeechCompleted'],
 'BroadcastReceiver':['onReceive'],'ServiceConnection':['onServiceConnected','onServiceDisconnected'],
 'FilenameFilter':['accept'],'Filter':['performFiltering','publishResults'],
 'android.text.style.ClickableSpan':['onClick'],'Callback':['onCreateActionMode','onPrepareActionMode','onActionItemClicked','onDestroyActionMode'],
 'FileBrowserFragment.OnFileClickListener':['onFileBrowserFileClick'],'CardFragment.OnClickListener':['onClick'],
 'GradeButtonsFragment.OnCardChangedListener':['onCardChanged'],'CategoryEditorResultListener':['onReceiveCategory'],
 'CategoryEditorFragment.CategoryEditorResultListener':['onReceiveCategory'],'AudioRecorderResultListener':['onReceiveAudio'],
 'AMGUIUtility.ProgressTask':['doInBackground','onPostExecute','onCancelled'],
 'FragmentStatePagerAdapter':['getItem','getCount'],
}
FW={ # citation constant per interface
 'DialogInterface':'FW_DIALOGFRAG','View.':'FW_VIEW','CompoundButton':'FW_VIEW','RadioGroup':'FW_VIEW','OnSeekBar':'FW_VIEW',
 'TextWatcher':'FW_VIEW','AdapterView':'FW_VIEW','OnItemClick':'FW_VIEW','PopupMenu':'FW_MENU','SearchView':'FW_MENU',
 'NavigationView':'FW_MATERIAL','BottomNavigationView':'FW_MATERIAL','Preference':'FW_PREFERENCE',
 'OnCompletionListener':'FW_MEDIAPLAYER','OnCompletedListener':'FW_TTS','AnyMemoTTS':'FW_TTS','BroadcastReceiver':'FW_RECEIVER',
 'ServiceConnection':'FW_SERVICECONN','Callback':'FW_ACTIONMODE','FileBrowserFragment':'FW_FRAG','CardFragment':'FW_VIEW',
 'GradeButtonsFragment':'FW_FRAG','CategoryEditorResultListener':'FW_FRAG','CategoryEditorFragment':'FW_FRAG',
 'AudioRecorderResultListener':'FW_FRAG','Consumer':'FW_RX','MaybeOnSubscribe':'FW_RX','Callable':'FW_RX',
 'FragmentStatePagerAdapter':'FW_FRAG','ClickableSpan':'FW_VIEW','Filter':'FW_FRAG','FilenameFilter':'FW_FRAG','Runnable':'FW_HANDLER',
 'Thread':'FW_HANDLER','AMGUIUtility':'FW_ASYNC','Comparator':'FW_SORT',
 'SingleOnSubscribe':'FW_RX','CompletableOnSubscribe':'FW_RX','ObservableOnSubscribe':'FW_RX','DisposableSingleObserver':'FW_RX',
 'DisposableCompletableObserver':'FW_RX','WebViewClient':'FW_WEBVIEW','TagHandler':'FW_TAG','OnItemClick':'FW_VIEW',
}
def fw_for(t):
    if t.startswith('Comparator'): return 'FW_SORT'
    if t.startswith('TagHandler'): return 'FW_TAG'
    if t.startswith('WebViewClient'): return 'FW_WEBVIEW'
    for k in ['DialogInterface','View.','CompoundButton','RadioGroup','OnSeekBar','TextWatcher','AdapterView','OnItemClick','PopupMenu','SearchView',
              'NavigationView','BottomNavigationView','Preference','OnCompletionListener','OnCompletedListener','AnyMemoTTS','BroadcastReceiver',
              'ServiceConnection','Callback','FileBrowserFragment','CardFragment','GradeButtonsFragment','CategoryEditorResultListener',
              'CategoryEditorFragment','AudioRecorderResultListener','Consumer','MaybeOnSubscribe','Callable','FragmentStatePagerAdapter',
              'ClickableSpan','Filter','FilenameFilter','Runnable','Thread','AMGUIUtility','OnItemClick','SingleOnSubscribe','CompletableOnSubscribe','ObservableOnSubscribe','DisposableSingleObserver','DisposableCompletableObserver','WebViewClient','TagHandler']:
        if k in t: return FW[k]
    return None
GUIKIND={'DialogInterface.OnClickListener','View.OnClickListener','View.OnLongClickListener','View.OnTouchListener','View.OnFocusChangeListener',
 'CompoundButton.OnCheckedChangeListener','RadioGroup.OnCheckedChangeListener','OnSeekBarChangeListener','TextWatcher','AdapterView.OnItemClickListener',
 'OnItemClickListener','AdapterView.OnItemLongClickListener','PopupMenu.OnMenuItemClickListener','SearchView.OnQueryTextListener',
 'NavigationView.OnNavigationItemSelectedListener','BottomNavigationView.OnNavigationItemSelectedListener','Preference.OnPreferenceClickListener',
 'CardFragment.OnClickListener','FileBrowserFragment.OnFileClickListener','GradeButtonsFragment.OnCardChangedListener','android.text.style.ClickableSpan',
 'Callback','DialogInterface.OnCancelListener','View.OnSystemUiVisibilityChangeListener'}
out=[]; skipped=collections.Counter(); n=0
lines_src={}
for cls in sorted(amap):
    a=amap[cls]
    t=types.get(cls,'?')
    methods=[m for m,v in verdict.items() if v=='UNRESOLVED' and m.rsplit('.',1)[0]==cls and not m.endswith(('.<init>','.<clinit>'))]
    if not methods: continue
    cr=creator.get(cls)
    if cr is None: skipped['no creator row']+=1; print('NOCREATOR',cls,t,methods[:3]); continue
    if cr in ('NO-NEW-SITE',): continue
    fw=fw_for(t)
    if fw is None: skipped['no fw for '+t]+=1; continue
    cbs=CB.get(t)
    if cbs is None:
        SAM={'call','run','accept','subscribe','compare','onClick','onCompleted','onSuccess','onComplete','onError','onNext','onReceive',
             'doInBackground','onPostExecute','onPreExecute','onCancelled','getView','getCount','getItem','onFocusChange','onTouch',
             'onBindViewHolder','onCreateViewHolder','getItemCount','onLoadFinished','onCreateLoader','onLoaderReset','loadInBackground',
             'onFailure','onResponse','performFiltering','publishResults','onGesturePerformed','onCardChanged','onItemClick','handleTag',
             'onDismiss','onCancel','onPageFinished','onPreExecute','onCompletion','onServiceConnected','onServiceDisconnected','onSuccess',
             'onAuthCodeReceived','onAuthCodeError','onPageFinished','onNavigationItemSelected','onMenuItemClick','onCheckedChanged','onProgressChanged'}
        cbs=[m.rsplit('.',1)[1] for m in methods if m.rsplit('.',1)[1] in SAM] or [m.rsplit('.',1)[1] for m in methods]
    ev="%s + '; SRC %s:%d-%d'"%(fw,a['file'],a['start'],a['end'])
    # label of the trigger
    for m in methods:
        name=m.rsplit('.',1)[1]
        if name not in cbs and t in CB: continue
        if t in GUIKIND:
            if t.startswith('DialogInterface'):
                trig="Tap a dialog button (listener at %s:%d)"%(a['file'],a['new'])
                e_kind='GUI'
            elif t=='DialogInterface.OnCancelListener':
                trig="Cancel the dialog (back key or tap outside)"; e_kind='GUI'
            else:
                trig="Tap or use the control whose %s listener is set at %s:%d"%(t,a['file'],a['new']); e_kind='GUI'
            out.append("gui(%r, %r, %r, kind='FRAMEWORK', evidence=%s)"%(cr,m,trig,ev))
        else:
            out.append("e(%r, %r, 'FRAMEWORK', %r, evidence=%s)"%(cr,m,"the framework calls %s (%s) at %s:%d"%(name,t,a['file'],a['new']),ev))
        n+=1
print('edges',n,'skipped',dict(skipped))
open(G+'/scratch/section_m_anon.py','w',encoding='utf-8').write('\n'.join(out)+'\n')
