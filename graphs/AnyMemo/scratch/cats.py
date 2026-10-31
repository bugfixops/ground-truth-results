import json, re, collections, sys
G='/Users/darshan/Desktop/yang/work/graphs/AnyMemo/'
C=json.load(open(G+'scratch/classify.json'))
A=json.load(open(G+'auto_calls.json'))
PKG='org.liberty.android.fantastischmemo.'
unres=[c['method'] for c in C]
FWCB={'onPreExecute','doInBackground','onPostExecute','onCancelled','onLoaderReset','onCreateLoader','onLoadFinished',
      'getView','getItemCount','onBindViewHolder','onCreateViewHolder','getCount','getItem','getSections','getSectionForPosition',
      'getPositionForSection','getItemOffsets','onDraw','getList','getItemId','onClick','onItemClick','onItemLongClick','onLongClick',
      'onTouch','onCheckedChanged','onMenuItemClick','onItemSelected','onNothingSelected','onPageFinished','onNewIntent','onReceive',
      'run','call','accept','onFailure','onResponse','onError','onSuccess','onComplete','onCancel','onDismiss','onActionItemClicked',
      'onPrepareActionMode','onDestroyActionMode','onCreateActionMode','compare','getFormattedValue','onDestroy','onRebind','onUnbind',
      'onStartCommand','onCreate','onStart','onStop','onResume','onPause','onAttach','onDetach','onCreateView','onViewCreated',
      'onActivityResult','onOptionsItemSelected','onCreateOptionsMenu','onPrepareOptionsMenu','onBackPressed','onSaveInstanceState',
      'onConfigurationChanged','onCreateAnimation','onDowngrade','onUpgrade','onQueryTextChange','onQueryTextSubmit','onTextChanged',
      'beforeTextChanged','afterTextChanged','onInit','onUtteranceCompleted','onGesturePerformed','onCompletion','onProgressChanged',
      'onStopTrackingTouch','onStartTrackingTouch','onSharedPreferenceChanged','getSrcExtension','onPreferenceClick','onPreferenceChange',
      'getPersistedString','persistString','onFileBrowserFileClick','onNavigationItemSelected','onGetViewFactory','onAuthCodeError','onAuthCodeReceived',
      'onBeginRecording','onDataSetChanged','getViewAt','getCount','onDoubleClick','onDraw','getItemOffsets','onRestoreInstanceState','onAuthenticated','onNext'}
GEN=re.compile(r'(DataBinderMapperImpl|\.BR\b|BindingImpl|Binding$|Binding\.|^Dagger|DaggerAppComponents|_Provide|_Factory|InstanceHolder|DaoImpl|AppModules?$|ActivityModules|AppComponents|DataBindingTriggerClass|DataBinderMapper|InnerBrLookup|InnerLayoutIdLookup)')
rows=[]
for m in unres:
    short=m.replace(PKG,'')
    cls, _, name = short.rpartition('.')
    if GEN.search(m) or GEN.search(cls): cat='generated'
    elif name in ('<init>','<clinit>'): cat='init/clinit'
    elif name in FWCB: cat='framework-cb:'+name
    elif '$' in cls: cat='inner-no-cb'
    else: cat='plain'
    rows.append((cat,short))
cnt=collections.Counter(r[0].split(':')[0] for r in rows)
print(len(rows), dict(cnt))
fw=collections.Counter(r[0] for r in rows if r[0].startswith('framework-cb'))
print(sorted(fw.items(), key=lambda x:-x[1]))
for cat in ('generated','init/clinit','plain','inner-no-cb'):
    xs=[r[1] for r in rows if r[0]==cat]
    print('\n##',cat,len(xs)); print('; '.join(xs[:400]))
json.dump(rows, open(G+'scratch/cats.json','w'))
