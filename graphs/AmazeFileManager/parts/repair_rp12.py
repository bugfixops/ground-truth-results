# Repair batch 12: 36 methods  
# Schema-2 edge entries for AmazeFileManager

EDGES = {}

# NOTE: 18 methods from this batch already have routes in graph_def.py and are marked REACHABLE in the build.
# This file contains only the 18 UNRESOLVED methods from the batch.

# ============================================================================
# CircularColorsView.<init>(Context,AttributeSet)
# ============================================================================
# REACHABLE: Inflated from XML layout files
# Evidence: SRC selectedcolors_preference.xml:7, item_colorpicker.xml:28
#   <com.amaze.filemanager.ui.views.CircularColorsView
# The framework calls the 2-arg constructor when inflating custom views from XML

EDGES['E_rp12_001'] = {
    'src': 'android.view.LayoutInflater.inflate',
    'dst': 'CircularColorsView.<init>(Context,AttributeSet)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'Framework inflates CircularColorsView from XML layouts',
    'evidence': 'SRC selectedcolors_preference.xml:7, item_colorpicker.xml:28'
}

EDGES['E_rp12_002'] = {
    'src': 'CircularColorsView.<init>(Context,AttributeSet)',
    'dst': 'CircularColorsView.<init>(Context)',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': '2-arg constructor calls 1-arg constructor via super chain',
    'evidence': 'SRC CircularColorsView.java:36-38'
}

# ============================================================================
# CustomNavigationView.<init>
# ============================================================================
# REACHABLE: Inflated from XML layout
# Evidence: SRC main_toolbar.xml:58
#   <com.amaze.filemanager.ui.views.drawer.CustomNavigationView android:id="@+id/navigation"
# NOTE: graph_def.py has edges for this using full package path names. This uses canonical short name.

EDGES['E_rp12_003'] = {
    'src': 'android.view.LayoutInflater.inflate',
    'dst': 'CustomNavigationView.<init>',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'Framework inflates CustomNavigationView from main_toolbar.xml',
    'evidence': 'SRC main_toolbar.xml:58'
}

EDGES['E_rp12_004'] = {
    'src': 'CustomNavigationView.<init>',
    'dst': 'CustomNavigationView.setNavigationItemSelectedListener',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'Constructor calls super.setNavigationItemSelectedListener(this)',
    'evidence': 'SRC CustomNavigationView.java:24'
}

# ============================================================================
# CustomNavigationView.onItemChecked
# ============================================================================
# REACHABLE: Called from onNavigationItemSelected
# Evidence: SRC CustomNavigationView.java:34-45

EDGES['E_rp12_005'] = {
    'src': 'CustomNavigationView.onNavigationItemSelected',
    'dst': 'CustomNavigationView.onItemChecked',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'onNavigationItemSelected calls onItemChecked when item should be selected',
    'evidence': 'SRC CustomNavigationView.java:38, 43'
}

# ============================================================================
# CustomNavigationView.isNavigationViewSavedStateMissing
# ============================================================================
# UNREACHABLE: Called only from onSaveInstanceState and onRestoreInstanceState, which are themselves unreachable
# The method checks for Android M-P bug workaround. However, onSaveInstanceState and onRestoreInstanceState
# are lifecycle methods that would be called by the framework during configuration changes, but there's
# evidence they're not being called (see graph_def.py UNREACHABLE entries).
# Evidence: grep shows only calls from unreachable methods

UNREACHABLE['CustomNavigationView.isNavigationViewSavedStateMissing'] = (
    'framework_never_calls',
    'Method is called only from onSaveInstanceState and onRestoreInstanceState, which are unreachable per graph_def.py; grep shows only these two callers',
    'SRC CustomNavigationView.java:69, 88',
    'SOURCE'
)

# ============================================================================
# DataUtils.addHiddenFile
# ============================================================================
# REACHABLE: Called from MainFragment.hide
# Evidence: SRC MainFragment.java:1553

EDGES['E_rp12_006'] = {
    'src': 'MainFragment.hide',
    'dst': 'DataUtils.addHiddenFile',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'MainFragment.hide calls DataUtils.addHiddenFile to mark file as hidden',
    'evidence': 'SRC MainFragment.java:1553, DataUtils.java:276-283'
}

# ============================================================================
# DataUtils.contains(String,ArrayList)
# ============================================================================
# REACHABLE: Called from DataUtils.containsServer(String)
# Evidence: SRC DataUtils.java:90-103

EDGES['E_rp12_007'] = {
    'src': 'DataUtils.containsServer(String)',
    'dst': 'DataUtils.contains(String,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'containsServer(String) calls contains(String,ArrayList) to search servers list',
    'evidence': 'SRC DataUtils.java:95-102 (loops through servers checking x[1].equals(path))'
}

# ============================================================================
# DataUtils.sortBook
# ============================================================================
# REACHABLE: Called from bookmark rename dialog
# Evidence: SRC RenameBookmark.java:144
# NOTE: graph_def.py has edge from 'RenameBookmark.onClick' which doesn't exist in method_list.
# The actual caller is one of the lambda$onCreateDialog lambdas (positive button callback).

EDGES['E_rp12_008'] = {
    'src': 'RenameBookmark.lambda$onCreateDialog$0',
    'dst': 'DataUtils.sortBook',
    'kind': 'GUI',
    'origin': 'repair_rp12',
    'text': 'After renaming bookmark, sort the bookmarks list',
    'evidence': 'SRC RenameBookmark.java:144 (within setOnClickListener lambda), DataUtils.java:314-316'
}

# ============================================================================
# RootUtils.<init>
# ============================================================================
# UNREACHABLE: RootUtils is a utility class with only static methods; constructor never called
# Evidence: grep shows no "new RootUtils" in app source

UNREACHABLE['RootUtils.<init>'] = (
    'no_trigger_in_app',
    'RootUtils is a utility class with all static methods; constructor never instantiated; grep -rn "new RootUtils" over app source shows no matches',
    'SRC RootUtils.java:16-17 (class declaration with only static methods)',
    'SOURCE'
)

# ============================================================================
# RootUtils.getFilePermissions
# ============================================================================
# UNREACHABLE: Private method never called within RootUtils
# Evidence: grep shows only the definition at line 169

UNREACHABLE['RootUtils.getFilePermissions'] = (
    'no_trigger_in_app',
    'Private method defined at line 169 but never called; grep shows only definition line',
    'SRC RootUtils.java:169-172',
    'SOURCE'
)

# ============================================================================
# RootUtils.lambda$changePermissions$0
# ============================================================================
# REACHABLE: Lambda callback within changePermissions method
# Evidence: SRC RootUtils.java:117-122

EDGES['E_rp12_009'] = {
    'src': 'RootUtils.changePermissions',
    'dst': 'RootUtils.lambda$changePermissions$0',
    'kind': 'ASYNC',
    'origin': 'repair_rp12',
    'text': 'changePermissions passes lambda callback to RootHelper.runShellCommandWithCallback',
    'evidence': 'SRC RootUtils.java:117-122'
}

# ============================================================================
# RootUtils.mkDir
# ============================================================================
# REACHABLE: Called from Operations.copy/move
# Evidence: SRC Operations.java:175

EDGES['E_rp12_010'] = {
    'src': 'Operations.mkdirWithMode',
    'dst': 'RootUtils.mkDir',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'Operations.mkdirWithMode calls RootUtils.mkDir when file requires root access',
    'evidence': 'SRC Operations.java:175 (within if (file.isRoot()) branch), RootUtils.java:139-147'
}

# ============================================================================
# RootUtils.mkFile
# ============================================================================
# REACHABLE: Called from Operations.mkfile
# Evidence: SRC Operations.java:313

EDGES['E_rp12_011'] = {
    'src': 'Operations.mkfile',
    'dst': 'RootUtils.mkFile',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'Operations.mkfile calls RootUtils.mkFile when file requires root access',
    'evidence': 'SRC Operations.java:313 (within if (file.isRoot()) branch), RootUtils.java:155-163'
}

# ============================================================================
# ShareAdapter.<init>
# ============================================================================
# REACHABLE: Instantiated in ShareTask.onPostExecute
# Evidence: SRC ShareTask.java:121

EDGES['E_rp12_012'] = {
    'src': 'ShareTask.onPostExecute',
    'dst': 'ShareAdapter.<init>',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'ShareTask.onPostExecute creates ShareAdapter for share dialog',
    'evidence': 'SRC ShareTask.java:121, ShareAdapter.java:32-38'
}

# ============================================================================
# ShareAdapter.onCreateViewHolder
# ============================================================================
# REACHABLE: RecyclerView.Adapter lifecycle method called by RecyclerView framework
# Evidence: ShareAdapter extends RecyclerView.Adapter

EDGES['E_rp12_013'] = {
    'src': 'androidx.recyclerview.widget.RecyclerView',
    'dst': 'ShareAdapter.onCreateViewHolder',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'RecyclerView framework calls onCreateViewHolder to create view holders',
    'evidence': 'SRC ShareAdapter.java:20 (extends RecyclerView.Adapter), 42-46 (overrides onCreateViewHolder)'
}

# ============================================================================
# ShareAdapter.onBindViewHolder
# ============================================================================
# REACHABLE: RecyclerView.Adapter lifecycle method called by RecyclerView framework
# Evidence: ShareAdapter extends RecyclerView.Adapter

EDGES['E_rp12_014'] = {
    'src': 'androidx.recyclerview.widget.RecyclerView',
    'dst': 'ShareAdapter.onBindViewHolder',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'RecyclerView framework calls onBindViewHolder to bind data to view holders',
    'evidence': 'SRC ShareAdapter.java:20 (extends RecyclerView.Adapter), 49-51 (overrides onBindViewHolder)'
}

EDGES['E_rp12_015'] = {
    'src': 'ShareAdapter.onBindViewHolder',
    'dst': 'ShareAdapter$ViewHolder.render',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'onBindViewHolder calls ViewHolder.render to display item',
    'evidence': 'SRC ShareAdapter.java:50'
}

# ============================================================================
# ShareAdapter.getItemCount
# ============================================================================
# REACHABLE: RecyclerView.Adapter method called by RecyclerView framework
# Evidence: ShareAdapter extends RecyclerView.Adapter

EDGES['E_rp12_016'] = {
    'src': 'androidx.recyclerview.widget.RecyclerView',
    'dst': 'ShareAdapter.getItemCount',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'RecyclerView framework calls getItemCount to determine number of items',
    'evidence': 'SRC ShareAdapter.java:20 (extends RecyclerView.Adapter), 84-87 (overrides getItemCount)'
}

# ============================================================================
# ShareAdapter.getItemId
# ============================================================================
# REACHABLE: RecyclerView.Adapter method called by RecyclerView framework
# Evidence: ShareAdapter extends RecyclerView.Adapter

EDGES['E_rp12_017'] = {
    'src': 'androidx.recyclerview.widget.RecyclerView',
    'dst': 'ShareAdapter.getItemId',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp12',
    'text': 'RecyclerView framework calls getItemId to get stable ID for each item',
    'evidence': 'SRC ShareAdapter.java:20 (extends RecyclerView.Adapter), 80-82 (overrides getItemId)'
}

# ============================================================================
# ShareAdapter.updateMatDialog
# ============================================================================
# REACHABLE: Called from ShareTask.onPostExecute
# Evidence: SRC ShareTask.java:122

EDGES['E_rp12_018'] = {
    'src': 'ShareTask.onPostExecute',
    'dst': 'ShareAdapter.updateMatDialog',
    'kind': 'CALL',
    'origin': 'repair_rp12',
    'text': 'ShareTask.onPostExecute calls updateMatDialog to set dialog reference',
    'evidence': 'SRC ShareTask.java:122 (shareAdapter.updateMatDialog(b)), ShareAdapter.java:29-31'
}
