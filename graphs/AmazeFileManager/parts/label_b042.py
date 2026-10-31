# ---- Helper batch_042 label part (2024)

# ItemPopupMenu - file row overflow menu constructed from RecyclerAdapter
e('RecyclerAdapter.showPopup', 'ItemPopupMenu.<init>', 'CALL',
  'RecyclerAdapter constructs ItemPopupMenu for file row actions',
  evidence='SRC RecyclerAdapter.java:950 new ItemPopupMenu(context, mainFrag.getMainActivity(), utilsProvider, mainFrag, rowItem, view, sharedPrefs)')

e('ItemPopupMenu.<init>', 'ItemPopupMenu.onMenuItemClick', 'CALL',
  'Constructor sets this as menu item click listener',
  evidence='SRC ItemPopupMenu.java:58 setOnMenuItemClickListener(this)')

# ItemPopupMenu anonymous inner classes - callback interfaces in encrypt case
e('ItemPopupMenu.onMenuItemClick', 'ItemPopupMenu$1.<init>', 'CALL',
  'First anonymous EncryptButtonCallbackInterface created for authentication',
  evidence='SRC ItemPopupMenu.java:138-146 new EncryptDecryptUtils.EncryptButtonCallbackInterface() with onButtonPressed methods')

e('ItemPopupMenu.onMenuItemClick', 'ItemPopupMenu$2.<init>', 'CALL',
  'Second anonymous EncryptButtonCallbackInterface created for main encrypt flow',
  evidence='SRC ItemPopupMenu.java:149-175 new EncryptDecryptUtils.EncryptButtonCallbackInterface() checking master password and fingerprint')

e('ItemPopupMenu$1.<init>', 'ItemPopupMenu$1.onButtonPressed', 'CALL',
  'Callback interface onButtonPressed called by dialog flow',
  evidence='SRC ItemPopupMenu.java:143-146 onButtonPressed(Intent, String) calls EncryptDecryptUtils.startEncryption')

e('ItemPopupMenu$2.<init>', 'ItemPopupMenu$2.onButtonPressed', 'CALL',
  'Callback interface onButtonPressed called by dialog or direct flow',
  evidence='SRC ItemPopupMenu.java:151-173 onButtonPressed(Intent) checks preferences and shows dialogs')

# InterestingConfigChange - utility for detecting configuration changes
e('AppListLoader.onStartLoading', 'InterestingConfigChange.isConfigChanged', 'CALL',
  'AppListLoader checks if configuration changed',
  evidence='SRC AppListLoader.java:123 boolean didConfigChange = InterestingConfigChange.isConfigChanged(getContext().getResources())')

e('AppListLoader.onStopLoading', 'InterestingConfigChange.recycle', 'CALL',
  'AppListLoader recycles static state when stopping',
  evidence='SRC AppListLoader.java:160 InterestingConfigChange.recycle()')

# InvalidablePreferenceCategory - preference UI component inflated by framework
e('ColorPref.onViewCreated', 'InvalidablePreferenceCategory.invalidate', 'CALL',
  'ColorPref invalidates preference category with accent color',
  evidence='SRC ColorPref.java:235 ((InvalidablePreferenceCategory) findPreference("category")).invalidate(activity.getAccent())')

e('InvalidablePreferenceCategory.invalidate', 'InvalidablePreferenceCategory.onBindView', 'FRAMEWORK',
  'Framework calls onBindView after notifyChanged',
  evidence='SRC InvalidablePreferenceCategory.java:31 notifyChanged() triggers framework to call onBindView; INFERRED: framework source not read')

# Indicator - ViewPager indicator widget inflated from layout main_toolbar.xml
e('Indicator.<init>', 'Indicator.setViewPager', 'CALL',
  'After inflation, MainActivity calls setViewPager',
  evidence='SRC Indicator.java:162-171 setViewPager stores viewPager, adds listener, calls setPageCount')

e('Indicator.setViewPager', 'Indicator.setPageCount', 'CALL',
  'setViewPager calls setPageCount with adapter count',
  evidence='SRC Indicator.java:164 setPageCount(viewPager.getAdapter().getCount())')

e('Indicator.setPageCount', 'Indicator.resetState', 'CALL',
  'setPageCount resets animation state arrays',
  evidence='SRC Indicator.java:213 resetState()')

e('Indicator.setPageCount', 'Indicator.onMeasure', 'FRAMEWORK',
  'setPageCount calls requestLayout which triggers framework onMeasure',
  evidence='SRC Indicator.java:214 requestLayout(); INFERRED: framework source not read')

e('Indicator.onMeasure', 'Indicator.getDesiredHeight', 'CALL',
  'onMeasure calls getDesiredHeight for height spec',
  evidence='SRC Indicator.java:235 int desiredHeight = getDesiredHeight()')

e('Indicator.onMeasure', 'Indicator.getRequiredWidth', 'CALL',
  'onMeasure calls getRequiredWidth for width calculation',
  evidence='SRC Indicator.java:246 int desiredWidth = getDesiredWidth() which calls getRequiredWidth at line 271')

e('Indicator.onMeasure', 'Indicator.getDesiredWidth', 'CALL',
  'onMeasure calls getDesiredWidth for width spec',
  evidence='SRC Indicator.java:246 int desiredWidth = getDesiredWidth()')

e('Indicator.onMeasure', 'Indicator.calculateDotPositions', 'CALL',
  'onMeasure calls calculateDotPositions after setMeasuredDimension',
  evidence='SRC Indicator.java:256 calculateDotPositions(width, height)')

e('Indicator.calculateDotPositions', 'Indicator.setCurrentPageImmediate', 'CALL',
  'calculateDotPositions calls setCurrentPageImmediate to position selected dot',
  evidence='SRC Indicator.java:273 setCurrentPageImmediate()')

e('Indicator.onPageSelected', 'Indicator.setSelectedPage', 'CALL',
  'ViewPager.OnPageChangeListener callback calls setSelectedPage',
  evidence='SRC Indicator.java:201 setSelectedPage(position)')

e('Indicator.setSelectedPage', 'Indicator.setJoiningFraction', 'CALL',
  'setSelectedPage sets joining fractions to 1 for multi-step moves',
  evidence='SRC Indicator.java:566-574 for loop calls setJoiningFraction(previousPage + i, 1f)')

e('Indicator.setSelectedPage', 'Indicator.createMoveSelectedAnimator', 'CALL',
  'setSelectedPage creates move animator for selected dot',
  evidence='SRC Indicator.java:579 moveAnimation = createMoveSelectedAnimator(dotCenterX[now], previousPage, now, steps)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$PendingRetreatAnimator.<init>', 'CALL',
  'createMoveSelectedAnimator constructs PendingRetreatAnimator',
  evidence='SRC Indicator.java:587 retreatAnimation = new PendingRetreatAnimator(was, now, steps, predicate)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'createMoveSelectedAnimator constructs RightwardStartPredicate when moving right',
  evidence='SRC Indicator.java:589 new RightwardStartPredicate(moveTo - ((moveTo - selectedDotX) * 0.25f))')

e('Indicator$RightwardStartPredicate.<init>', 'Indicator$StartPredicate.<init>', 'CALL',
  'RightwardStartPredicate constructor calls super',
  evidence='SRC Indicator.java:826-828 RightwardStartPredicate(float thresholdValue) calls super(thresholdValue)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.resetState', 'CALL',
  'Animator listener calls resetState on animation end',
  evidence='SRC Indicator.java:590-595 AnimatorListenerAdapter.onAnimationEnd calls resetState()')

e('Indicator.createMoveSelectedAnimator', 'Indicator$PendingRetreatAnimator.startIfNecessary', 'CALL',
  'Move animator update listener calls startIfNecessary',
  evidence='SRC Indicator.java:599 retreatAnimation.startIfNecessary(selectedDotX)')

e('Indicator$PendingRetreatAnimator.startIfNecessary', 'Indicator$RightwardStartPredicate.shouldStart', 'CALL',
  'startIfNecessary checks predicate shouldStart',
  evidence='SRC Indicator.java:668 if (!hasStarted && predicate.shouldStart(currentValue))')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRetreatAnimator constructor calls super',
  evidence='SRC Indicator.java:682 PendingRetreatAnimator calls super(predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRevealAnimator.<init>', 'CALL',
  'PendingRetreatAnimator creates reveal animators array',
  evidence='SRC Indicator.java:708,725 revealAnimations[i] = new PendingRevealAnimator(was + i, predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'PendingRetreatAnimator creates RightwardStartPredicate for reveal animators',
  evidence='SRC Indicator.java:709 new RightwardStartPredicate(dotCenterX[was + i])')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRevealAnimator.startIfNecessary', 'CALL',
  'Update listener calls startIfNecessary on each reveal animator',
  evidence='SRC Indicator.java:717,733 for (PendingRevealAnimator pendingReveal : revealAnimations) pendingReveal.startIfNecessary')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.cancelJoiningAnimations', 'CALL',
  'Animator listener calls cancelJoiningAnimations on start',
  evidence='SRC Indicator.java:742 cancelJoiningAnimations()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.clearJoiningFractions', 'CALL',
  'Animator listener calls clearJoiningFractions on start',
  evidence='SRC Indicator.java:743 clearJoiningFractions()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Animator listener calls setDotRevealFraction for dots to hide',
  evidence='SRC Indicator.java:746 setDotRevealFraction(dot, MINIMAL_REVEAL)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator$1.<init>', 'CALL',
  'PendingRetreatAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:740-758 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationStart', 'ASYNC',
  'Framework calls onAnimationStart when retreat animation begins',
  evidence='SRC Indicator.java:742-749 onAnimationStart(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when retreat animation completes',
  evidence='SRC Indicator.java:751-755 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRevealAnimator constructor calls super',
  evidence='SRC Indicator.java:768 PendingRevealAnimator calls super(predicate)')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Update listener calls setDotRevealFraction',
  evidence='SRC Indicator.java:775 setDotRevealFraction(PendingRevealAnimator.this.dot, (Float) valueAnimator.getAnimatedValue())')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingRevealAnimator$1.<init>', 'CALL',
  'PendingRevealAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:778-784 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRevealAnimator$1.<init>', 'Indicator$PendingRevealAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when reveal animation completes',
  evidence='SRC Indicator.java:780-783 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator.onPageScrolled', 'Indicator.setJoiningFraction', 'CALL',
  'ViewPager scroll callback calls setJoiningFraction',
  evidence='SRC Indicator.java:193 setJoiningFraction(leftDotPosition, fraction)')

e('Indicator.onDraw', 'Indicator.drawUnselected', 'FRAMEWORK',
  'Framework onDraw calls drawUnselected',
  evidence='SRC Indicator.java:291 drawUnselected(canvas); INFERRED: framework source not read')

e('Indicator.onDraw', 'Indicator.drawSelected', 'FRAMEWORK',
  'Framework onDraw calls drawSelected',
  evidence='SRC Indicator.java:292 drawSelected(canvas); INFERRED: framework source not read')

e('Indicator.drawUnselected', 'Indicator.getUnselectedPath', 'CALL',
  'drawUnselected calls getUnselectedPath for each dot',
  evidence='SRC Indicator.java:301-304 combinedUnselectedPath.op(getUnselectedPath(...))')

e('Indicator.drawUnselected', 'Indicator.getRetreatingJoinPath', 'CALL',
  'drawUnselected calls getRetreatingJoinPath when retreat active',
  evidence='SRC Indicator.java:308 combinedUnselectedPath.op(getRetreatingJoinPath(), Path.Op.UNION)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.lambda$createMoveSelectedAnimator$0', 'CALL',
  'Lambda desugared for animator update listener',
  evidence='SRC Indicator.java:597-600 moveSelected.addUpdateListener(valueAnimator -> {...})')

# LZMA2Decoder - 7z compression library class accessed via Coders map
e('SevenZipHelperTask.doInBackground', 'SevenZFile.<init>', 'CALL',
  'SevenZipHelperTask opens 7z archive',
  evidence='SRC SevenZipHelperTask.java:68-70 new SevenZFile(new File(filePath))')

e('SevenZFile.buildDecodingStream', 'Coders.addDecoder', 'CALL',
  'SevenZFile calls Coders.addDecoder to decode each coder',
  evidence='SRC SevenZFile.java:435 inputStreamStack = Coders.addDecoder(fileName, inputStreamStack, ...)')

e('Coders.addDecoder', 'LZMA2Decoder.decode', 'CALL',
  'Coders.addDecoder looks up LZMA2Decoder from map and calls decode',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:69-75 cb = findByMethod(...); return cb.decode(...)')

e('LZMA2Decoder.decode', 'LZMA2Decoder.getDictionarySize', 'CALL',
  'decode calls getDictionarySize to extract dictionary size from coder properties',
  evidence='SRC LZMA2Decoder.java:36 final int dictionarySize = getDictionarySize(coder)')

e('SevenZFile.getOptionsFromCoder', 'LZMA2Decoder.getOptionsFromCoder', 'CALL',
  'SevenZFile calls getOptionsFromCoder to extract coder options',
  evidence='SRC SevenZFile.java:1033 Coders.findByMethod(method).getOptionsFromCoder(coder, inputStreamStack); Coders.java:53 map contains LZMA2Decoder')

e('SevenZOutputFile.writeFilesInfo', 'Coders.findByMethod', 'CALL',
  'SevenZOutputFile calls findByMethod to get coder for properties',
  evidence='SRC SevenZOutputFile.java:452 Coders.findByMethod(m.getMethod()).getOptionsAsProperties(m.getOptions())')

e('Coders.findByMethod', 'LZMA2Decoder.getOptionsAsProperties', 'CALL',
  'findByMethod returns LZMA2Decoder, caller invokes getOptionsAsProperties',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:67 return CODER_MAP.get(method)')

e('LZMA2Decoder.getOptionsAsProperties', 'LZMA2Decoder.getDictSize', 'CALL',
  'getOptionsAsProperties calls getDictSize to encode dictionary size',
  evidence='SRC LZMA2Decoder.java:56 final int dictSize = getDictSize(opts)')

e('LZMA2Decoder.getDictSize', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getDictSize calls numberOptionOrDefault when opts is not LZMA2Options',
  evidence='SRC LZMA2Decoder.java:71 return numberOptionOrDefault(opts)')

e('SevenZOutputFile.writeFileCoder', 'Coders.addEncoder', 'CALL',
  'SevenZOutputFile calls Coders.addEncoder to wrap output stream',
  evidence='SRC SevenZOutputFile.java:321 out = Coders.addEncoder(out, m.getMethod(), m.getOptions())')

e('Coders.addEncoder', 'LZMA2Decoder.encode', 'CALL',
  'Coders.addEncoder looks up LZMA2Decoder from map and calls encode',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:82-87 cb = findByMethod(method); return cb.encode(out, options)')

e('LZMA2Decoder.encode', 'LZMA2Decoder.getOptions', 'CALL',
  'encode calls getOptions to create LZMA2Options',
  evidence='SRC LZMA2Decoder.java:46 final LZMA2Options options = getOptions(opts)')

e('LZMA2Decoder.getOptions', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getOptions calls numberOptionOrDefault to get dict size',
  evidence='SRC LZMA2Decoder.java:93 options.setDictSize(numberOptionOrDefault(opts))')

# InterestingConfigChange static initializer
# Static fields initialized at class load, which happens on first access (isConfigChanged call)

# No UNREACHABLE methods in this batch - all methods are REACHABLE through the routes above
