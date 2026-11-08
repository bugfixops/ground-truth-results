# Repair batch 16: routes and unreachable labels
# Generated for AmazeFileManager schema-2 graph

# ========== ThemedImageView ==========

# ThemedImageView is used in XML layouts (fragment_sheet_cloud.xml, dialog_decrypt_fingerprint_authentication.xml)
# and extended by ThemedImageButton. When inflated from XML, Android framework calls constructors.

# ThemedImageView.<init>(Context) constructor
# SRC ui/views/ThemedImageView.java:21-23
# Called by framework when inflating from XML with no attributes
e('AndroidLayoutInflater.inflate', 'ThemedImageView.<init>(Context)', 'CALL',
  'Framework inflates ThemedImageView from XML',
  evidence='SRC ui/views/ThemedImageView.java:21-23 defines constructor; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 declares ThemedImageView elements')

# ThemedImageView.<init>(Context,AttributeSet) constructor  
# SRC ui/views/ThemedImageView.java:25-27
# Called by framework when inflating from XML with attributes (most common case)
e('AndroidLayoutInflater.inflate', 'ThemedImageView.<init>(Context,AttributeSet)', 'CALL',
  'Framework inflates ThemedImageView from XML with attributes',
  evidence='SRC ui/views/ThemedImageView.java:25-27 defines constructor; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 declares ThemedImageView elements')

e('ThemedImageView.<init>(Context,AttributeSet)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor chain: this(context, attrs, 0)',
  evidence='SRC ui/views/ThemedImageView.java:26')

# ThemedImageView.<init>(Context,AttributeSet,int) constructor
# SRC ui/views/ThemedImageView.java:29-40
# Main constructor implementation, called by other constructors
e('ThemedImageView.<init>(Context)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor chain: this(context, null, 0)',
  evidence='SRC ui/views/ThemedImageView.java:22')

e('ThemedImageView.<init>(Context,AttributeSet,int)', 'AndroidView.setColorFilter', 'CALL',
  'setColorFilter(Color.argb(255, 255, 255, 255)) when dark theme',
  guard='a != null && (a.getAppTheme().equals(AppTheme.DARK) || a.getAppTheme().equals(AppTheme.BLACK))',
  evidence='SRC ui/views/ThemedImageView.java:35')

e('ThemedImageView.<init>(Context,AttributeSet,int)', 'ThemedImageView.getActivity', 'CALL',
  'BasicActivity a = (BasicActivity) getActivity()',
  evidence='SRC ui/views/ThemedImageView.java:33')

# ThemedImageView.getActivity() private method
# SRC ui/views/ThemedImageView.java:42-51
# Called only from constructor to find Activity context
e('ThemedImageView.getActivity', 'AndroidContextWrapper.getBaseContext', 'CALL',
  'context = ((ContextWrapper)context).getBaseContext()',
  evidence='SRC ui/views/ThemedImageView.java:47')


# ========== SearchView$1 and SearchView$2 ==========

# SearchView$1 is the anonymous AnimatorListener in revealSearchView() lines 99-109
# SearchView$2 is the anonymous AnimatorListener in hideSearchView() lines 135-145

# SearchView is instantiated in MainActivity via AppBar.initSearchView
e('AppBar.initSearchView', 'SearchView.<init>', 'CALL',
  'new SearchView(appbar, mainActivity, searchListener)',
  evidence='SRC ui/views/appbar/SearchView.java:38; AppBar instantiates SearchView')

e('SearchView.<init>', 'SearchView$1.<init>', 'CALL',
  'anonymous AnimatorListener created in revealSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:99-109 defines anonymous class')

e('SearchView.<init>', 'SearchView$2.<init>', 'CALL',
  'anonymous AnimatorListener created in hideSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:135-145 defines anonymous class')

# SearchView$1 methods (revealSearchView animator listener)
e('AndroidAnimator.addListener', 'SearchView$1.onAnimationStart', 'CALL',
  'Framework calls onAnimationStart when reveal animation starts',
  evidence='SRC ui/views/appbar/SearchView.java:100 callback')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationEnd', 'CALL',
  'Framework calls onAnimationEnd when reveal animation completes',
  evidence='SRC ui/views/appbar/SearchView.java:103 callback sets enabled=true, shows keyboard')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationCancel', 'CALL',
  'Framework calls onAnimationCancel if reveal animation cancelled',
  evidence='SRC ui/views/appbar/SearchView.java:108 callback empty')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationRepeat', 'CALL',
  'Framework calls onAnimationRepeat if reveal animation repeats',
  evidence='SRC ui/views/appbar/SearchView.java:110 callback empty')

# SearchView$2 methods (hideSearchView animator listener)
e('AndroidAnimator.addListener', 'SearchView$2.onAnimationStart', 'CALL',
  'Framework calls onAnimationStart when hide animation starts',
  evidence='SRC ui/views/appbar/SearchView.java:136 callback')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationEnd', 'CALL',
  'Framework calls onAnimationEnd when hide animation completes',
  evidence='SRC ui/views/appbar/SearchView.java:139 callback sets visibility GONE, hides keyboard')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationCancel', 'CALL',
  'Framework calls onAnimationCancel if hide animation cancelled',
  evidence='SRC ui/views/appbar/SearchView.java:144 callback empty')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationRepeat', 'CALL',
  'Framework calls onAnimationRepeat if hide animation repeats',
  evidence='SRC ui/views/appbar/SearchView.java:146 callback empty')


# ========== CustomNavigationView$SavedState ==========

# CustomNavigationView$SavedState is a Parcelable for saving state, but blocked by isNavigationViewSavedStateMissing
# which returns true on API 23-28 (including API 27). Already marked UNREACHABLE in graph_def.py lines 2773-2815.
# These methods already have UNREACHABLE labels, so no new routes needed.


# ========== PathSwitchPreference ==========

# PathSwitchPreference is a Preference subclass, instantiated when preference screen is created
# SRC ui/views/preference/PathSwitchPreference.java:21-59

# PathSwitchPreference used in preferences_quickaccesspaths.xml
e('AndroidPreferenceInflater.inflate', 'PathSwitchPreference.<init>(Context)', 'CALL',
  'Framework inflates PathSwitchPreference from XML',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:23-25 constructor')

# PathSwitchPreference.onCreateView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:27-31
e('AndroidPreference.onCreateView', 'PathSwitchPreference.onCreateView', 'CALL',
  'Framework calls onCreateView to create preference view',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:27-31 override')

# PathSwitchPreference.onBindView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:33-41
e('AndroidPreference.onBindView', 'PathSwitchPreference.onBindView', 'CALL',
  'Framework calls onBindView to bind preference view',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:33-41 override calls setListener twice')

e('PathSwitchPreference.onBindView', 'PathSwitchPreference.setListener', 'CALL',
  'setListener(view, R.id.edit, EDIT) and setListener(view, R.id.delete, DELETE)',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:35-36')

# PathSwitchPreference.setListener() private method
# SRC ui/views/preference/PathSwitchPreference.java:47-56
# Creates lambda (synthetic method PathSwitchPreference.lambda$setListener$0)
e('PathSwitchPreference.setListener', 'PathSwitchPreference.lambda$setListener$0', 'CALL',
  'Lambda view -> {...} compiled to synthetic lambda$setListener$0',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:50-53 lambda body')


# ========== OneCharacterCharSequence ==========

# OneCharacterCharSequence is a CharSequence implementation
# SRC utils/OneCharacterCharSequence.java:5-35

# Grep for usage:
# No calls found to "new OneCharacterCharSequence" in app source

UNREACHABLE['OneCharacterCharSequence.<init>'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence utility class not instantiated in app codebase',
    'SRC utils/OneCharacterCharSequence.java:8-11 constructor; grep shows no "new OneCharacterCharSequence" in app source',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.charAt'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.charAt not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:14-17 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.length'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.length not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:20-22 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.subSequence'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.subSequence not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:25-27 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.toString'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.toString not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:30-34 method; class not instantiated in app',
    'SOURCE')


# ========== ScreenUtils ==========

# ScreenUtils is instantiated in AppConfig.getInstance line 234
# SRC utils/application/AppConfig.java:234: screenUtils = new ScreenUtils(activity);
# Graph already has routes from AppConfig.getInstance to ScreenUtils methods (lines 1237-1249)

# ScreenUtils.convertPxToDb already has route in graph_def.py line 1237
# ScreenUtils.getScreenWidthInPx already has route in graph_def.py line 1240
# ScreenUtils.convertDbToPx already has route in graph_def.py line 1245

# ScreenUtils.getScreeHeightInDb - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreeHeightInDb', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:43-45 method')

# ScreenUtils.getScreenHeightInPx - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenHeightInPx', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:28-32 method')

# ScreenUtils.getScreenWidthInDp - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInDp', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:38-40 method')


# ========== Streamer ==========

# Streamer is for SMB streaming, instantiated via getInstance
# SRC utils/SmbStreamer/Streamer.java:29-43

# Check for usage of Streamer
# Grep shows no usage of Streamer.getInstance or Streamer.setStreamSrc in app source
# Cloud streaming uses CloudStreamer, not Streamer

UNREACHABLE['Streamer.getNameFromPath'] = (
    'no_trigger_in_app',
    'Streamer.getNameFromPath is private helper for serve method; Streamer not used in app (CloudStreamer used instead)',
    'SRC utils/SmbStreamer/Streamer.java:141-150 private static method; no calls to Streamer.getInstance found',
    'SOURCE')

UNREACHABLE['Streamer.isStreamMedia'] = (
    'no_trigger_in_app',
    'Streamer.isStreamMedia not called in app; Streamer class not used (CloudStreamer used instead for cloud files)',
    'SRC utils/SmbStreamer/Streamer.java:46-48 public static method; grep shows no usage in app source',
    'SOURCE')

UNREACHABLE['Streamer.serve'] = (
    'no_trigger_in_app',
    'Streamer.serve override not called because Streamer not instantiated or started in app',
    'SRC utils/SmbStreamer/Streamer.java:64-138 override method; no calls to Streamer.getInstance found',
    'SOURCE')

UNREACHABLE['Streamer.setStreamSrc'] = (
    'no_trigger_in_app',
    'Streamer.setStreamSrc not called because Streamer not used in app (CloudStreamer used for cloud streaming)',
    'SRC utils/SmbStreamer/Streamer.java:50-54 method; no calls to Streamer.setStreamSrc found',
    'SOURCE')


# ========== CloudUtil ==========

# CloudUtil has existing routes in graph_def.py lines 1792-1819
# CloudUtil.launchCloud already has route line 1806
# CloudUtil.getThumbnailInputStreamForCloud route missing - used by Glide to load thumbnails

e('LoadFilesListTask.doInBackground', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL',
  'CloudUtil.getThumbnailInputStreamForCloud loads thumbnails for cloud files',
  evidence='SRC utils/cloud/CloudUtil.java:262-318 method; called when loading cloud file thumbnails')

# CloudUtil.lambda$launchCloud$1 is synthetic lambda method
# SRC utils/cloud/CloudUtil.java:137-156
e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'CALL',
  'Lambda Thread run() compiled to synthetic lambda$launchCloud$1',
  evidence='SRC utils/cloud/CloudUtil.java:137-156 lambda defines thread body')

e('CloudUtil.lambda$launchCloud$1', 'CloudUtil.lambda$null$0', 'CALL',
  'Nested lambda activity.runOnUiThread() compiled to synthetic lambda$null$0',
  evidence='SRC utils/cloud/CloudUtil.java:139-155 nested lambda for UI thread execution')


# ========== RecyclerAdapter$1 ==========

# RecyclerAdapter$1 is anonymous RequestListener<Drawable> in showThumbnailWithBackground method
# SRC adapters/RecyclerAdapter.java:872-899
# This listener is used by Glide to handle thumbnail loading callbacks

e('RecyclerAdapter.showThumbnailWithBackground', 'RecyclerAdapter$1.<init>', 'CALL',
  'new RequestListener<Drawable>() {...} anonymous class',
  evidence='SRC adapters/RecyclerAdapter.java:872 anonymous RequestListener creation')

e('GlideRequest.listener', 'RecyclerAdapter$1.onLoadFailed', 'CALL',
  'Glide framework calls onLoadFailed when thumbnail load fails',
  evidence='SRC adapters/RecyclerAdapter.java:874-883 callback method')

e('RecyclerAdapter$1.onLoadFailed', 'RecyclerAdapter$1.lambda$onLoadFailed$0', 'CALL',
  'Lambda msg -> {...} compiled to synthetic lambda$onLoadFailed$0',
  evidence='SRC adapters/RecyclerAdapter.java:876-879 lambda body')

e('GlideRequest.listener', 'RecyclerAdapter$1.onResourceReady', 'CALL',
  'Glide framework calls onResourceReady when thumbnail loads successfully',
  evidence='SRC adapters/RecyclerAdapter.java:885-895 callback method')
