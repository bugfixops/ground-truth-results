# ---- Helper batch_041 label part (2026-10-28)
# Batch 41: Indicator, Indicator$1, Indicator$2, Indicator$3, Indicator$LeftwardStartPredicate
# 5 classes, 38 methods

# Indicator is a ViewPager page indicator (dots animation view) used in TabFragment
# Entry: MainActivity.onCreate -> goToMain -> TabFragment.<init> -> TabFragment.onCreateView
#        -> findViewById(R.id.indicator) [framework inflates, calls 3-arg constructor]
#        -> Indicator.setViewPager

# Indicator constructors - framework-inflated from XML
e('TabFragment.onCreateView', 'Indicator.<init>', 'FRAMEWORK',
  'findViewById inflates Indicator from XML; framework calls 3-arg constructor',
  evidence='SRC TabFragment.java:84-85 findViewById(R.id.indicator); '
           'SRC Indicator.java:123-163 constructor chain (115-117, 119-121, 123-163)')

# setViewPager - explicitly called from TabFragment
e('TabFragment.onCreateView', 'Indicator.setViewPager', 'CALL',
  'TabFragment sets up ViewPager reference',
  evidence='SRC TabFragment.java:178 indicator.setViewPager(mViewPager); '
           'SRC Indicator.java:164-175')

# setViewPager internal calls
e('Indicator.setViewPager', 'Indicator.setPageCount', 'CALL',
  'setViewPager initializes page count from adapter',
  evidence='SRC Indicator.java:167 setPageCount(viewPager.getAdapter().getCount()); '
           'SRC Indicator.java:214-218')

e('Indicator.setViewPager', 'Indicator.setCurrentPageImmediate', 'CALL',
  'setViewPager sets initial selected dot position',
  evidence='SRC Indicator.java:174 setCurrentPageImmediate(); '
           'SRC Indicator.java:238-247')

e('Indicator.setViewPager', 'Indicator$1.<init>', 'CALL',
  'setViewPager registers DataSetObserver for adapter changes',
  evidence='SRC Indicator.java:168-173 registerDataSetObserver(new DataSetObserver() { ... })')

# setPageCount calls resetState
e('Indicator.setPageCount', 'Indicator.resetState', 'CALL',
  'setPageCount resets animation state arrays',
  evidence='SRC Indicator.java:217 resetState(); '
           'SRC Indicator.java:220-229')

# Indicator$1 DataSetObserver callbacks
e('Indicator$1.<init>', 'Indicator$1.onChanged', 'FRAMEWORK',
  'DataSetObserver.onChanged callback when ViewPager adapter data changes',
  evidence='SRC Indicator.java:169-172 onChanged() override; '
           'INFERRED PagerAdapter.notifyDataSetChanged calls observer.onChanged, source not read')

e('Indicator$1.onChanged', 'Indicator.setPageCount', 'CALL',
  'DataSetObserver updates page count when adapter changes',
  evidence='SRC Indicator.java:171 setPageCount(Indicator.this.viewPager.getAdapter().getCount())')

# View lifecycle - onMeasure called by framework
e('Indicator.<init>', 'Indicator.onMeasure', 'FRAMEWORK',
  'View.onMeasure callback for layout measurement',
  evidence='SRC Indicator.java:44 extends View; '
           'INFERRED View framework calls onMeasure during layout, source not read')

# onMeasure internal calls
e('Indicator.onMeasure', 'Indicator.getDesiredHeight', 'CALL',
  'onMeasure calculates desired view height',
  evidence='SRC Indicator.java:234 getDesiredHeight(); '
           'SRC Indicator.java:270-272')

e('Indicator.onMeasure', 'Indicator.getDesiredWidth', 'CALL',
  'onMeasure calculates desired view width',
  evidence='SRC Indicator.java:243-251 getDesiredWidth(); '
           'SRC Indicator.java:278-280')

e('Indicator.onMeasure', 'Indicator.getRequiredWidth', 'CALL',
  'getDesiredWidth calls getRequiredWidth',
  evidence='SRC Indicator.java:279 getRequiredWidth(); '
           'SRC Indicator.java:274-276')

e('Indicator.onMeasure', 'Indicator.calculateDotPositions', 'CALL',
  'onMeasure finalizes dot positions after dimensions set',
  evidence='SRC Indicator.java:257 calculateDotPositions(width, height); '
           'SRC Indicator.java:220-237')

e('Indicator.calculateDotPositions', 'Indicator.setCurrentPageImmediate', 'CALL',
  'calculateDotPositions updates selected dot X position',
  evidence='SRC Indicator.java:236 setCurrentPageImmediate()')

# onDraw called by framework
e('Indicator.<init>', 'Indicator.onDraw', 'FRAMEWORK',
  'View.onDraw callback for rendering',
  evidence='SRC Indicator.java:44 extends View; '
           'INFERRED View framework calls onDraw to render, source not read')

# onDraw calls drawUnselected and drawSelected
e('Indicator.onDraw', 'Indicator.drawUnselected', 'CALL',
  'onDraw renders unselected page dots',
  evidence='SRC Indicator.java:283 drawUnselected(canvas); '
           'SRC Indicator.java:287-302')

e('Indicator.onDraw', 'Indicator.drawSelected', 'CALL',
  'onDraw renders selected page dot',
  evidence='SRC Indicator.java:284 drawSelected(canvas); '
           'SRC Indicator.java:633-635')

# drawUnselected internal calls
e('Indicator.drawUnselected', 'Indicator.getUnselectedPath', 'CALL',
  'drawUnselected builds path for each dot',
  evidence='SRC Indicator.java:292-296 getUnselectedPath(page, ...) for each page; '
           'SRC Indicator.java:317-623')

e('Indicator.drawUnselected', 'Indicator.getRetreatingJoinPath', 'CALL',
  'drawUnselected draws retreating join animation if active',
  evidence='SRC Indicator.java:299-300 if retreatingJoinX1 != INVALID_FRACTION, getRetreatingJoinPath(); '
           'SRC Indicator.java:625-630')

# OnPageChangeListener callbacks - called by ViewPager
e('Indicator.setViewPager', 'Indicator.onPageScrolled', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageScrolled callback during scroll',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:177-197; '
           'INFERRED ViewPager calls listener.onPageScrolled during page transitions, source not read')

e('Indicator.setViewPager', 'Indicator.onPageSelected', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageSelected callback on page change',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:199-208; '
           'INFERRED ViewPager calls listener.onPageSelected when page selected, source not read')

e('Indicator.setViewPager', 'Indicator.onPageScrollStateChanged', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageScrollStateChanged callback',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:210-212; '
           'INFERRED ViewPager calls listener.onPageScrollStateChanged, source not read')

# onPageScrolled calls setJoiningFraction
e('Indicator.onPageScrolled', 'Indicator.setJoiningFraction', 'CALL',
  'onPageScrolled updates dot joining animation fraction',
  evidence='SRC Indicator.java:196 setJoiningFraction(leftDotPosition, fraction); '
           'SRC Indicator.java:637-646')

# onPageSelected calls setSelectedPage
e('Indicator.onPageSelected', 'Indicator.setSelectedPage', 'CALL',
  'onPageSelected triggers page selection animation',
  evidence='SRC Indicator.java:203 setSelectedPage(position); '
           'SRC Indicator.java:548-577')

# setSelectedPage calls setJoiningFraction
e('Indicator.setSelectedPage', 'Indicator.setJoiningFraction', 'CALL',
  'setSelectedPage sets joining fraction to 1 for multi-step transitions',
  evidence='SRC Indicator.java:561-569 setJoiningFraction(previousPage + i, 1f) in loop')

# setSelectedPage calls createMoveSelectedAnimator
e('Indicator.setSelectedPage', 'Indicator.createMoveSelectedAnimator', 'CALL',
  'setSelectedPage creates animator for selected dot movement',
  evidence='SRC Indicator.java:571-575 moveAnimation = createMoveSelectedAnimator(...); '
           'SRC Indicator.java:579-630')

# createMoveSelectedAnimator creates inner class instances
e('Indicator.createMoveSelectedAnimator', 'Indicator$2.<init>', 'CALL',
  'createMoveSelectedAnimator creates AnimatorListenerAdapter for retreat animation end',
  evidence='SRC Indicator.java:590-597 retreatAnimation.addListener(new AnimatorListenerAdapter() { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator$3.<init>', 'CALL',
  'createMoveSelectedAnimator creates AnimatorListenerAdapter for move animation lifecycle',
  evidence='SRC Indicator.java:604-618 moveSelected.addListener(new AnimatorListenerAdapter() { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator.lambda$createMoveSelectedAnimator$0', 'CALL',
  'ValueAnimator.addUpdateListener registers lambda callback',
  evidence='SRC Indicator.java:598-602 moveSelected.addUpdateListener(valueAnimator -> { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator$LeftwardStartPredicate.<init>', 'CALL',
  'createMoveSelectedAnimator creates LeftwardStartPredicate for leftward page transitions',
  evidence='SRC Indicator.java:590 new LeftwardStartPredicate(moveTo + ...) when now < was')

# Indicator$2 AnimatorListenerAdapter callbacks
e('Indicator$2.<init>', 'Indicator$2.onAnimationEnd', 'FRAMEWORK',
  'Animator calls listener.onAnimationEnd when retreat animation completes',
  evidence='SRC Indicator.java:592-596 onAnimationEnd() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationEnd, source not read')

e('Indicator$2.onAnimationEnd', 'Indicator.resetState', 'CALL',
  'Listener resets state when retreat animation ends',
  evidence='SRC Indicator.java:593 resetState()')

# Indicator$3 AnimatorListenerAdapter callbacks
e('Indicator$3.<init>', 'Indicator$3.onAnimationStart', 'FRAMEWORK',
  'Animator calls listener.onAnimationStart when move animation starts',
  evidence='SRC Indicator.java:605-609 onAnimationStart() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationStart, source not read')

e('Indicator$3.<init>', 'Indicator$3.onAnimationEnd', 'FRAMEWORK',
  'Animator calls listener.onAnimationEnd when move animation completes',
  evidence='SRC Indicator.java:611-617 onAnimationEnd() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationEnd, source not read')

# OnAttachStateChangeListener - framework callbacks
e('Indicator.<init>', 'Indicator.onViewAttachedToWindow', 'FRAMEWORK',
  'View.OnAttachStateChangeListener.onViewAttachedToWindow callback',
  evidence='SRC Indicator.java:44-45 implements View.OnAttachStateChangeListener; '
           'SRC Indicator.java:162 addOnAttachStateChangeListener(this); '
           'SRC Indicator.java:260-262; '
           'INFERRED View framework calls onViewAttachedToWindow, source not read')

e('Indicator.<init>', 'Indicator.onViewDetachedFromWindow', 'FRAMEWORK',
  'View.OnAttachStateChangeListener.onViewDetachedFromWindow callback',
  evidence='SRC Indicator.java:44-45 implements View.OnAttachStateChangeListener; '
           'SRC Indicator.java:162 addOnAttachStateChangeListener(this); '
           'SRC Indicator.java:264-266; '
           'INFERRED View framework calls onViewDetachedFromWindow, source not read')

# Indicator$LeftwardStartPredicate methods
e('Indicator$LeftwardStartPredicate.<init>', 'Indicator$LeftwardStartPredicate.shouldStart', 'CALL',
  'PendingStartAnimator.startIfNecessary calls predicate.shouldStart',
  evidence='SRC Indicator.java:827-829 shouldStart() method; '
           'INFERRED called from Indicator$PendingStartAnimator.startIfNecessary at line 668, class not in this batch')

# Methods called by classes in other batches (edges recorded there)
# - Indicator.cancelJoiningAnimations called from Indicator$PendingRetreatAnimator$1.onAnimationStart
# - Indicator.clearJoiningFractions called from Indicator$PendingRetreatAnimator$1.onAnimationStart
# - Indicator.setDotRevealFraction called from Indicator$PendingRetreatAnimator$1.onAnimationStart and Indicator$PendingRevealAnimator lambdas
# These edges will be recorded in those batches

