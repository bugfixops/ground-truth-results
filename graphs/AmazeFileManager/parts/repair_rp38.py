# Repair batch 38: PrepareCopyTask, PemToKeyPairTask, ColorPref, MainFragment$3, PrepareCopyTask$CopyNode methods
# All methods except PrepareCopyTask$CopyNode.getFilesToCopy and getConflictingFiles already have routes.
# Only adding missing edges for CopyNode methods.

# PrepareCopyTask$CopyNode.hasStarted - called from PrepareCopyTask.onEndDialog
e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.hasStarted', 'CALL',
  'onEndDialog checks if BFS traversal has started',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:231: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();')

# PrepareCopyTask$CopyNode.getPath - called from PrepareCopyTask.onEndDialog
e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.getPath', 'CALL',
  'onEndDialog retrieves path from CopyNode to add to paths list',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:236: paths.add(c.getPath());')

# PrepareCopyTask$CopyNode.getUnvisitedChildNode - called from goToNextNode
e('PrepareCopyTask$CopyNode.goToNextNode', 'PrepareCopyTask$CopyNode.getUnvisitedChildNode', 'CALL',
  'goToNextNode searches for unvisited child in BFS traversal',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:365: if ((child = getUnvisitedChildNode(visited, node)) != null) {')

# PrepareCopyTask$CopyNode.getFilesToCopy - never called, fields accessed directly
UNREACHABLE['PrepareCopyTask$CopyNode.getFilesToCopy'] = ('no_trigger_in_app', 'Getter method never called; PrepareCopyTask.onEndDialog accesses filesToCopy field directly via c.filesToCopy (line 237,240); no app code calls this getter', 'SRC asynchronous/asynctasks/PrepareCopyTask.java:381-383 defines getter; grep shows no calls', 'SOURCE')

# PrepareCopyTask$CopyNode.getConflictingFiles - never called, fields accessed directly  
UNREACHABLE['PrepareCopyTask$CopyNode.getConflictingFiles'] = ('no_trigger_in_app', 'Getter method never called; PrepareCopyTask.onEndDialog accesses conflictingFiles field directly via c.conflictingFiles (line 240); no app code calls this getter', 'SRC asynchronous/asynctasks/PrepareCopyTask.java:385-387 defines getter; grep shows no calls', 'SOURCE')
