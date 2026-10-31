# repair_rp28.py - Batch 28 repairs

def edge(src, dst, kind, summary='', evidence=''):
    """Schema-2 edge format"""
    return {'src': src, 'dst': dst, 'kind': kind, 'summary': summary, 'evidence': evidence}

EDGES = []

# Indicator.<init>(Context) - constructor delegation
# SRC Indicator.java:113-115
# public Indicator(Context context) {
#     this(context, null, 0);
# }
EDGES.append(edge(
    'Indicator.<init>(Context)',
    'Indicator.<init>(Context,AttributeSet,int)',
    'CALL',
    'Constructor delegation: single-arg constructor delegates to three-arg constructor with null AttributeSet and 0 defStyle',
    'SRC Indicator.java:113-115: public Indicator(Context context) { this(context, null, 0); }'
))

# Indicator.<init>(Context,AttributeSet) - constructor delegation
# SRC Indicator.java:117-119
# public Indicator(Context context, AttributeSet attrs) {
#     this(context, attrs, 0);
# }
EDGES.append(edge(
    'Indicator.<init>(Context,AttributeSet)',
    'Indicator.<init>(Context,AttributeSet,int)',
    'CALL',
    'Constructor delegation: two-arg constructor delegates to three-arg constructor with 0 defStyle',
    'SRC Indicator.java:117-119: public Indicator(Context context, AttributeSet attrs) { this(context, attrs, 0); }'
))

# Indicator.<init>(Context,AttributeSet,int) - already has routes in graph_def.py
# No new edges needed - already routed

# MainActivityHelper$4 lambdas - mkdir ErrorCallBack implementation

# MainActivityHelper$4.lambda$exists$0
# SRC MainActivityHelper.java:456-465
# Lambda inside exists() callback: ma.getActivity().runOnUiThread(() -> { ... })
EDGES.append(edge(
    'MainActivityHelper$4.exists',
    'MainActivityHelper$4.lambda$exists$0',
    'CALL',
    'exists callback runs lambda on UI thread via runOnUiThread',
    'SRC MainActivityHelper.java:456-465: ma.getActivity().runOnUiThread(() -> { if (toast != null) toast.cancel(); Toast.makeText(...); ... }); lambda at 456-465'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$exists$0',
    'Toast.cancel',
    'CALL',
    'Lambda cancels toast notification',
    'SRC MainActivityHelper.java:457: if (toast != null) toast.cancel();'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$exists$0',
    'Toast.makeText',
    'CALL',
    'Lambda shows "file exists" toast message',
    'SRC MainActivityHelper.java:458-459: Toast.makeText(mainActivity, mainActivity.getString(R.string.fileexist), Toast.LENGTH_SHORT).show();'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$exists$0',
    'MainActivityHelper.mkdir',
    'CALL',
    'Lambda retries mkdir with dialog prompted again',
    'SRC MainActivityHelper.java:462: mkdir(file.getMode(), file.getParent(), ma);'
))

# MainActivityHelper$4.lambda$launchSAF$1
# SRC MainActivityHelper.java:470-474
# Lambda inside launchSAF() callback
EDGES.append(edge(
    'MainActivityHelper$4.launchSAF(HybridFile)',
    'MainActivityHelper$4.lambda$launchSAF$1',
    'CALL',
    'launchSAF callback runs lambda on UI thread via runOnUiThread',
    'SRC MainActivityHelper.java:470-474: ma.getActivity().runOnUiThread(() -> { mainActivity.oppathe = path.getPath(); mainActivity.operation = DataUtils.NEW_FOLDER; guideDialogForLEXA(...); }); lambda at 470-474'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$launchSAF$1',
    'MainActivityHelper.guideDialogForLEXA',
    'CALL',
    'Lambda shows SAF guide dialog for creating new folder',
    'SRC MainActivityHelper.java:472: guideDialogForLEXA(mainActivity.oppathe);'
))

# MainActivityHelper$4.lambda$done$2
# SRC MainActivityHelper.java:483-489
# Lambda inside done() callback
EDGES.append(edge(
    'MainActivityHelper$4.done',
    'MainActivityHelper$4.lambda$done$2',
    'CALL',
    'done callback runs lambda on UI thread via runOnUiThread',
    'SRC MainActivityHelper.java:483-489: ma.getActivity().runOnUiThread(() -> { if (b) { ma.updateList(); } else { Toast.makeText(...); } }); lambda at 483-489'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$done$2',
    'MainFragment.updateList',
    'CALL',
    'Lambda updates file list on success',
    'SRC MainActivityHelper.java:484: if (b) { ma.updateList(); }'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$done$2',
    'Toast.makeText',
    'CALL',
    'Lambda shows operation unsuccessful toast on failure',
    'SRC MainActivityHelper.java:486-487: Toast.makeText(ma.getActivity(), ma.getString(R.string.operation_unsuccesful), Toast.LENGTH_SHORT).show();'
))

# MainActivityHelper$4.lambda$invalidName$3
# SRC MainActivityHelper.java:493-499
# Lambda inside invalidName() callback
EDGES.append(edge(
    'MainActivityHelper$4.invalidName',
    'MainActivityHelper$4.lambda$invalidName$3',
    'CALL',
    'invalidName callback runs lambda on UI thread via runOnUiThread',
    'SRC MainActivityHelper.java:493-499: ma.getActivity().runOnUiThread(() -> { if (toast != null) toast.cancel(); Toast.makeText(...); }); lambda at 493-499'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$invalidName$3',
    'Toast.cancel',
    'CALL',
    'Lambda cancels toast notification',
    'SRC MainActivityHelper.java:495: if (toast != null) toast.cancel();'
))

EDGES.append(edge(
    'MainActivityHelper$4.lambda$invalidName$3',
    'Toast.makeText',
    'CALL',
    'Lambda shows invalid name toast message',
    'SRC MainActivityHelper.java:496-497: Toast.makeText(ma.getActivity(), ma.getString(R.string.invalid_name) + ": " + file.getName(), Toast.LENGTH_LONG).show();'
))

# CALLBACK edges from Operations.mkdir to MainActivityHelper$4
EDGES.append(edge(
    'Operations.mkdir',
    'MainActivityHelper$4.exists',
    'CALLBACK',
    'Operations.mkdir calls exists callback when directory already exists',
    'SRC MainActivityHelper.java:453-455: Operations.mkdir(path, ma.getActivity(), mainActivity.isRootExplorer(), new Operations.ErrorCallBack() { @Override public void exists(final HybridFile file) { ... } }); mkdir invokes ErrorCallBack.exists'
))

EDGES.append(edge(
    'Operations.mkdir',
    'MainActivityHelper$4.launchSAF(HybridFile)',
    'CALLBACK',
    'Operations.mkdir calls launchSAF callback when SAF permission needed',
    'SRC MainActivityHelper.java:453,468-476: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void launchSAF(HybridFile file) { ... } }); mkdir invokes ErrorCallBack.launchSAF'
))

EDGES.append(edge(
    'Operations.mkdir',
    'MainActivityHelper$4.done',
    'CALLBACK',
    'Operations.mkdir calls done callback when mkdir operation completes',
    'SRC MainActivityHelper.java:453,482-490: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void done(HybridFile hFile, final boolean b) { ... } }); mkdir invokes ErrorCallBack.done'
))

EDGES.append(edge(
    'Operations.mkdir',
    'MainActivityHelper$4.invalidName',
    'CALLBACK',
    'Operations.mkdir calls invalidName callback when directory name is invalid',
    'SRC MainActivityHelper.java:453,493-500: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void invalidName(final HybridFile file) { ... } }); mkdir invokes ErrorCallBack.invalidName'
))

# Check for any UNREACHABLE methods
# All methods in this batch have routes, so no UNREACHABLE entries needed
