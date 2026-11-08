# repair batch 31 - extra round 1

# RecyclerPreloadModelProvider.getPreloadItems - Framework callback from Glide RecyclerViewPreloader
e('RecyclerAdapter.setItems', 'RecyclerPreloadModelProvider.<init>', 'CALL',
  'setItems creates RecyclerPreloadModelProvider and passes to RecyclerViewPreloader',
  evidence='SRC RecyclerAdapter.java:388 modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);')

e('RecyclerPreloadModelProvider.<init>', 'RecyclerPreloadModelProvider.getPreloadItems', 'FRAMEWORK',
  'Glide RecyclerViewPreloader calls getPreloadItems via ListPreloader.PreloadModelProvider interface',
  evidence='SRC RecyclerAdapter.java:389 preloader = new RecyclerViewPreloader<>(GlideApp.with(mainFrag), modelProvider, sizeProvider, GlideConstants.MAX_PRELOAD_FILES); RecyclerPreloadModelProvider.java:23 public class RecyclerPreloadModelProvider implements ListPreloader.PreloadModelProvider<IconDataParcelable> { SRC RecyclerPreloadModelProvider.java:35-38 @Override public List<IconDataParcelable> getPreloadItems(int position) { IconDataParcelable iconData = urisToLoad.get(position); ... }; INFERRED Glide RecyclerViewPreloader calls PreloadModelProvider.getPreloadItems')

# RootHelper.lambda$runShellCommandToList$0 - Lambda from runShellCommandToList
e('RootHelper.runShellCommandToList', 'RootHelper.lambda$runShellCommandToList$0', 'ASYNC',
  'runShellCommandToList passes lambda to runShellCommandWithCallback',
  evidence='SRC RootHelper.java:50 runShellCommandWithCallback(cmd, (commandCode, exitCode, output) -> result.addAll(output));')

e('RootHelper.lambda$runShellCommandToList$0', 'RootHelper.runShellCommandWithCallback', 'CALL',
  'lambda$runShellCommandToList$0 is the desugared lambda body passed to runShellCommandWithCallback',
  evidence='SRC RootHelper.java:50 runShellCommandWithCallback(cmd, (commandCode, exitCode, output) -> result.addAll(output)); INFERRED lambda desugaring creates synthetic method')

# RootUtils.lambda$changePermissions$0 - Lambda from changePermissions  
e('RootUtils.changePermissions', 'RootUtils.lambda$changePermissions$0', 'ASYNC',
  'changePermissions passes lambda callback to RootHelper.runShellCommandWithCallback',
  evidence='SRC RootUtils.java:117-121 RootHelper.runShellCommandWithCallback(command, (commandCode, exitCode, output) -> { if (exitCode < 0) { onOperationPerform.callback(false); } else { onOperationPerform.callback(true); } });')

e('RootUtils.lambda$changePermissions$0', 'RootHelper.runShellCommandWithCallback', 'CALL',
  'lambda$changePermissions$0 is the desugared lambda body',
  evidence='SRC RootUtils.java:117-121 (commandCode, exitCode, output) -> { if (exitCode < 0) { onOperationPerform.callback(false); } else { onOperationPerform.callback(true); } }; INFERRED lambda desugaring creates synthetic method')

# ProgressHandler.<init>(int,long) - Unreachable, never called
UNREACHABLE['ProgressHandler.<init>(int,long)'] = (
    'no_trigger_in_app',
    'two-argument constructor never called; all call sites use no-argument constructor',
    'SRC ProgressHandler.java:48-51 public ProgressHandler(int sourceFiles, long totalSize) { this.sourceFiles = sourceFiles; this.totalSize = totalSize; }; grep output: CopyService.java:83 private ProgressHandler progressHandler = new ProgressHandler(); ZipService.java:76 private ProgressHandler progressHandler = new ProgressHandler(); ExtractService.java:78 private ProgressHandler progressHandler = new ProgressHandler(); DecryptService.java:49 private ProgressHandler progressHandler = new ProgressHandler(); EncryptService.java:50 private ProgressHandler progressHandler = new ProgressHandler(); (all use no-argument constructor)',
    'SOURCE'
)

# RootHelper.<init> - Unreachable, utility class with only static methods
UNREACHABLE['RootHelper.<init>'] = (
    'no_trigger_in_app',
    'utility class with only static methods, constructor never called',
    'SRC RootHelper.java:36 public class RootHelper { (no explicit constructor, default constructor generated); grep -rn "new RootHelper" returns no matches',
    'SOURCE'
)

# RootHelper.generateBaseFile(DocumentFile) - Unreachable, never called
UNREACHABLE['RootHelper.generateBaseFile(DocumentFile)'] = (
    'no_trigger_in_app',
    'DocumentFile overload never called; all call sites use File parameter overload',
    'SRC RootHelper.java:151-158 public static HybridFileParcelable generateBaseFile(DocumentFile file) { long size = 0; if (!file.isDirectory()) size = file.length(); HybridFileParcelable baseFile = new HybridFileParcelable(file.getName(), parseDocumentFilePermission(file), file.lastModified(), size, file.isDirectory()); baseFile.setName(file.getName()); baseFile.setMode(OpenMode.OTG); return baseFile; }; grep -rn "RootHelper.generateBaseFile" shows all call sites use "new File" parameter except AppsAdapter.java:248 which calls generateBaseFile(f, true) with File parameter',
    'SOURCE'
)

# RootHelper.runNonRootShellCommand - Unreachable, deprecated and never called
UNREACHABLE['RootHelper.runNonRootShellCommand'] = (
    'no_trigger_in_app',
    'deprecated method never called',
    'SRC RootHelper.java:83-94 @deprecated Use {@link #runShellCommand(String)} instead which runs command on an interactive shell public static List<String> runNonRootShellCommand(String cmd) { return Shell.SH.run(cmd); }; grep -rn "runNonRootShellCommand" returns only the method definition',
    'SOURCE'
)

# RootUtils.<init> - Unreachable, utility class with only static methods
UNREACHABLE['RootUtils.<init>'] = (
    'no_trigger_in_app',
    'utility class with only static methods and constants, constructor never called',
    'SRC RootUtils.java:15 public class RootUtils { (no explicit constructor); grep -rn "new RootUtils" returns no matches',
    'SOURCE'
)

# RootUtils.getFilePermissions - Unreachable, private method never called
UNREACHABLE['RootUtils.getFilePermissions'] = (
    'no_trigger_in_app',
    'private method never called within class',
    'SRC RootUtils.java:163-166 private static int getFilePermissions(String path) throws ShellNotRunningException { String line = RootHelper.runShellCommandToList("stat -c  %a \\"" + path + "\\"").get(0); return Integer.valueOf(line); }; grep -rn "getFilePermissions" within RootUtils.java shows only the method definition',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.draw - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.draw(Canvas)'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:75-100 @Override public void draw(Canvas canvas) { super.draw(canvas); ... }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.fitSystemWindows - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.fitSystemWindows(Rect)'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:66-74 @Override protected boolean fitSystemWindows(Rect insets) { mInsets = new Rect(insets); setWillNotDraw(mInsetForeground == null); ViewCompat.postInvalidateOnAnimation(this); if (mOnInsetsCallback != null) { mOnInsetsCallback.onInsetsChanged(insets); } return true; }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.init - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.init(Context,AttributeSet,int)'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:57-65 private void init(Context context, AttributeSet attrs, int defStyle) { final TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.ScrimInsetsFrameLayout, defStyle, 0); if (a == null) { return; } mInsetForeground = a.getDrawable(R.styleable.ScrimInsetsFrameLayout_insetForeground); a.recycle(); setWillNotDraw(true); }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.onAttachedToWindow - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.onAttachedToWindow()'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:102-108 @Override protected void onAttachedToWindow() { super.onAttachedToWindow(); if (mInsetForeground != null) { mInsetForeground.setCallback(this); } }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.onDetachedFromWindow - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.onDetachedFromWindow()'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:110-116 @Override protected void onDetachedFromWindow() { super.onDetachedFromWindow(); if (mInsetForeground != null) { mInsetForeground.setCallback(null); } }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)

# ScrimInsetsRelativeLayout.setOnInsetsCallback - Unreachable, custom view never instantiated
UNREACHABLE['ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback)'] = (
    'no_trigger_in_app',
    'custom view never instantiated in any XML layout or Java code',
    'SRC ScrimInsetsRelativeLayout.java:123-125 public void setOnInsetsCallback(OnInsetsCallback onInsetsCallback) { mOnInsetsCallback = onInsetsCallback; }; grep in XML layouts and Java code returns no usage of ScrimInsetsRelativeLayout',
    'SOURCE'
)
