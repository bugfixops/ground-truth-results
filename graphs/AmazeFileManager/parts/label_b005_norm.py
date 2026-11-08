# ---- Batch 005: BottomBar and inner classes (2026-10-27 21:23)

# BottomBar entry point from AppBar
e('com.amaze.filemanager.ui.views.appbar.AppBar.<init>', 
  'com.amaze.filemanager.ui.views.appbar.BottomBar.<init>', 'EXPLICIT', 'AppBar constructor instantiates BottomBar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/AppBar.java:37')

# BottomBar public API calls from MainActivity
e('com.amaze.filemanager.activities.MainActivity.onCreate', 
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setClickListener', 'EXPLICIT', 'MainActivity onCreate calls setClickListener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:854')

e('com.amaze.filemanager.activities.MainActivity.onActivityResult',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.resetClickListener', 'EXPLICIT', 'MainActivity onActivityResult resets listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:892')

e('com.amaze.filemanager.activities.MainActivity.onPause',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath', 'EXPLICIT', 'MainActivity onPause updates bottom bar path',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:850')

e('com.amaze.filemanager.activities.MainActivity.updateBottomBarColor',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setBackgroundColor', 'EXPLICIT', 'MainActivity theme color applied to bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:1475')

# BottomBar calls from MainFragment
e('com.amaze.filemanager.fragments.MainFragment.onViewCreated',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setClickListener', 'EXPLICIT', 'MainFragment sets up touch listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:281')

e('com.amaze.filemanager.fragments.MainFragment.updateBottomBar',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath', 'EXPLICIT', 'MainFragment updates bottom bar on path change',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:451')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setPathText', 'EXPLICIT', 'MainFragment updates path text on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1604')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setFullPathText', 'EXPLICIT', 'MainFragment updates full path on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1605')

# BottomBar calls from TabFragment
e('com.amaze.filemanager.fragments.TabFragment.onFragmentResult',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath', 'EXPLICIT', 'TabFragment updates bottom bar on selection',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:222-305')

# BottomBar visibility from fragment lifecycle
e('com.amaze.filemanager.fragments.FtpServerFragment.onViewCreated',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setVisibility', 'EXPLICIT', 'FTP fragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/FtpServerFragment.java:157')

e('com.amaze.filemanager.fragments.AppsListFragment.onViewCreated',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setVisibility', 'EXPLICIT', 'AppsListFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:84')

e('com.amaze.filemanager.fragments.ProcessViewerFragment.onViewCreated',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.setVisibility', 'EXPLICIT', 'ProcessViewerFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:143')

e('com.amaze.filemanager.fragments.CompressedExplorerFragment.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath', 'EXPLICIT', 'CompressedExplorer updates bottom bar on navigation',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/CompressedExplorerFragment.java:445')

# BottomBar internal methods
e('com.amaze.filemanager.ui.views.appbar.BottomBar.setClickListener',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.onTouch', 'EXPLICIT', 'setClickListener registers onTouch listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:154-160')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onDown', 'EXPLICIT', 'onTouch delegates to GestureDetector',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:486, FW-SRC android/view/GestureDetector.java (onTouchEvent dispatches to listeners)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed', 'EXPLICIT', 'GestureDetector calls onSingleTapConfirmed',
  evidence='FW-SRC android/view/GestureDetector.java (onSingleTapConfirmed called on confirmed single tap)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onLongPress', 'EXPLICIT', 'GestureDetector calls onLongPress',
  evidence='FW-SRC android/view/GestureDetector.java (onLongPress called on long press)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons', 'EXPLICIT', 'Gesture handler calls showButtons',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:138, 144')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.areButtonsShowing', 'EXPLICIT', 'showButtons queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:167')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.createArrow', 'EXPLICIT', 'showButtons creates arrow button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:205')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.createFolderButton', 'EXPLICIT', 'showButtons creates folder button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:195')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$0', 'EXPLICIT', 'showButtons root button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:181')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$1', 'EXPLICIT', 'showButtons storage button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:187')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$2', 'EXPLICIT', 'showButtons folder button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:193')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.sendScroll', 'EXPLICIT', 'showButtons scrolls to position',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:233')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$3', 'EXPLICIT', 'showButtons post scrolling callback',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:229')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.areButtonsShowing', 'EXPLICIT', 'updatePath queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:239')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons', 'EXPLICIT', 'updatePath shows buttons on visible state',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:238')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.sendScroll', 'EXPLICIT', 'updatePath scrolls path view',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:461')

e('com.amaze.filemanager.ui.views.appbar.BottomBar.sendScroll',
  'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$sendScroll$4', 'EXPLICIT', 'sendScroll posts delayed scroll',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:483')

# Animation callbacks - BottomBar$3 (forward navigation)
e('com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.<init>', 'EXPLICIT', 'updatePath sets animation listener for forward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:345')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationStart',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.lambda$onAnimationStart$1', 'EXPLICIT', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:359')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationEnd',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.lambda$onAnimationEnd$0', 'EXPLICIT', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:349')

# Animation callbacks - BottomBar$4 (backward navigation)
e('com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$4.<init>', 'EXPLICIT', 'updatePath sets animation listener for backward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:374')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationStart',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$4.lambda$onAnimationStart$1', 'EXPLICIT', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:389')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationEnd',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$4.lambda$onAnimationEnd$0', 'EXPLICIT', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:379')

# CountDownTimer - BottomBar$1
e('com.amaze.filemanager.ui.views.appbar.BottomBar.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$1.<init>', 'EXPLICIT', 'BottomBar constructor creates countdown timer',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:113')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$1.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$1.onTick', 'LIFECYCLE', 'CountDownTimer invokes onTick periodically',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:115, FW-SRC android/os/CountDownTimer.java (onTick invoked every interval)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$1.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$1.onFinish', 'LIFECYCLE', 'CountDownTimer invokes onFinish on completion',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:118, FW-SRC android/os/CountDownTimer.java (onFinish invoked when countdown completes)')

# GestureDetector - BottomBar$2
e('com.amaze.filemanager.ui.views.appbar.BottomBar.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.<init>', 'EXPLICIT', 'BottomBar constructor creates gesture listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:123')

# Framework animation listeners
e('com.amaze.filemanager.ui.views.appbar.BottomBar$3.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$3.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$3.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationCancel', 'LIFECYCLE', 'Animator invokes onAnimationCancel',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationCancel called on animation cancel)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$4.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$4.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')

# No UNREACHABLE methods - all are reachable
