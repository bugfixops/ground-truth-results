STATUS: RUNNING 23:36

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| Indicator.<init>(Context) | REACHABLE | | Constructor delegates to 3-arg constructor | SRC Indicator.java:115-117 |
| Indicator.<init>(Context,AttributeSet) | REACHABLE | | Constructor delegates to 3-arg constructor | SRC Indicator.java:119-121 |
| Indicator.<init>(Context,AttributeSet,int) | REACHABLE | | Framework calls when inflating from XML in TabFragment | SRC TabFragment.java:84-85; SRC Indicator.java:123-163 |
| Indicator.calculateDotPositions | REACHABLE | | Called from onMeasure after dimensions set | SRC Indicator.java:257; SRC Indicator.java:220-237 |
| Indicator.cancelJoiningAnimations | REACHABLE | | Called from PendingRetreatAnimator$1.onAnimationStart but body only has TODO comment | SRC Indicator.java:648-650 method body "// TODO: 20/08/18 ?" |
| Indicator.clearJoiningFractions | REACHABLE | | Called from PendingRetreatAnimator$1.onAnimationStart (class in different batch) | SRC Indicator.java:637-642 method definition; INFERRED caller in Indicator$PendingRetreatAnimator$1 |
| Indicator.createMoveSelectedAnimator | REACHABLE | | Called from setSelectedPage to create move animation | SRC Indicator.java:571-575; SRC Indicator.java:579-630 |
| Indicator.drawSelected | REACHABLE | | Called from onDraw to render selected page dot | SRC Indicator.java:284; SRC Indicator.java:633-635 |
| Indicator.drawUnselected | REACHABLE | | Called from onDraw to render unselected page dots | SRC Indicator.java:283; SRC Indicator.java:287-302 |
| Indicator.getDesiredHeight | REACHABLE | | Called from onMeasure to calculate desired view height | SRC Indicator.java:234; SRC Indicator.java:270-272 |
| Indicator.getDesiredWidth | REACHABLE | | Called from onMeasure to calculate desired view width | SRC Indicator.java:243-251; SRC Indicator.java:278-280 |
| Indicator.getRequiredWidth | REACHABLE | | Called from getDesiredWidth | SRC Indicator.java:279; SRC Indicator.java:274-276 |
| Indicator.getRetreatingJoinPath | REACHABLE | | Called from drawUnselected when retreating join animation active | SRC Indicator.java:299-300; SRC Indicator.java:625-630 |
| Indicator.getUnselectedPath | REACHABLE | | Called from drawUnselected for each page dot | SRC Indicator.java:292-296; SRC Indicator.java:317-623 |
| Indicator.lambda$createMoveSelectedAnimator$0 | REACHABLE | | Lambda registered in createMoveSelectedAnimator update listener | SRC Indicator.java:598-602 |
| Indicator.onDraw | REACHABLE | | Framework View.onDraw callback for rendering | SRC Indicator.java:44 extends View; SRC Indicator.java:281-285; INFERRED framework calls onDraw |
| Indicator.onMeasure | REACHABLE | | Framework View.onMeasure callback for layout measurement | SRC Indicator.java:44 extends View; SRC Indicator.java:231-258; INFERRED framework calls onMeasure |
| Indicator.onPageScrollStateChanged | REACHABLE | | ViewPager.OnPageChangeListener callback on scroll state change | SRC Indicator.java:44 implements OnPageChangeListener; SRC Indicator.java:166; SRC Indicator.java:210-212 |
| Indicator.onPageScrolled | REACHABLE | | ViewPager.OnPageChangeListener callback during page scroll | SRC Indicator.java:44 implements OnPageChangeListener; SRC Indicator.java:166; SRC Indicator.java:177-197 |
| Indicator.onPageSelected | REACHABLE | | ViewPager.OnPageChangeListener callback when page selected | SRC Indicator.java:44 implements OnPageChangeListener; SRC Indicator.java:166; SRC Indicator.java:199-208 |
| Indicator.onViewAttachedToWindow | REACHABLE | | View.OnAttachStateChangeListener callback when attached | SRC Indicator.java:44-45 implements OnAttachStateChangeListener; SRC Indicator.java:162; SRC Indicator.java:260-262 |
| Indicator.onViewDetachedFromWindow | REACHABLE | | View.OnAttachStateChangeListener callback when detached | SRC Indicator.java:44-45 implements OnAttachStateChangeListener; SRC Indicator.java:162; SRC Indicator.java:264-266 |
| Indicator.resetState | REACHABLE | | Called from setPageCount and Indicator$2.onAnimationEnd | SRC Indicator.java:217; SRC Indicator.java:593; SRC Indicator.java:220-229 |
| Indicator.setCurrentPageImmediate | REACHABLE | | Called from setViewPager and calculateDotPositions | SRC Indicator.java:174; SRC Indicator.java:236; SRC Indicator.java:238-247 |
| Indicator.setDotRevealFraction | REACHABLE | | Called from PendingRetreatAnimator and PendingRevealAnimator (classes in different batches) | SRC Indicator.java:644-647 method definition; INFERRED callers in other Indicator inner classes |
| Indicator.setJoiningFraction | REACHABLE | | Called from onPageScrolled and setSelectedPage | SRC Indicator.java:196; SRC Indicator.java:561-569; SRC Indicator.java:637-646 |
| Indicator.setPageCount | REACHABLE | | Called from setViewPager and Indicator$1.onChanged | SRC Indicator.java:167; SRC Indicator.java:171; SRC Indicator.java:214-218 |
| Indicator.setSelectedPage | REACHABLE | | Called from onPageSelected to trigger page selection animation | SRC Indicator.java:203; SRC Indicator.java:548-577 |
| Indicator.setViewPager | REACHABLE | | Called from TabFragment.onCreateView to set up ViewPager | SRC TabFragment.java:178; SRC Indicator.java:164-175 |
| Indicator$1.<init> | REACHABLE | | DataSetObserver created in setViewPager | SRC Indicator.java:168-173 |
| Indicator$1.onChanged | REACHABLE | | DataSetObserver.onChanged callback when adapter data changes | SRC Indicator.java:169-172; INFERRED PagerAdapter notifies observers |
| Indicator$2.<init> | REACHABLE | | AnimatorListenerAdapter created in createMoveSelectedAnimator for retreat animation | SRC Indicator.java:590-597 |
| Indicator$2.onAnimationEnd | REACHABLE | | AnimatorListener.onAnimationEnd callback when retreat animation completes | SRC Indicator.java:592-596; INFERRED ValueAnimator invokes listener |
| Indicator$3.<init> | REACHABLE | | AnimatorListenerAdapter created in createMoveSelectedAnimator for move animation | SRC Indicator.java:604-618 |
| Indicator$3.onAnimationEnd | REACHABLE | | AnimatorListener.onAnimationEnd callback when move animation completes | SRC Indicator.java:611-617; INFERRED ValueAnimator invokes listener |
| Indicator$3.onAnimationStart | REACHABLE | | AnimatorListener.onAnimationStart callback when move animation starts | SRC Indicator.java:605-609; INFERRED ValueAnimator invokes listener |
| Indicator$LeftwardStartPredicate.<init> | REACHABLE | | LeftwardStartPredicate created for leftward page transitions | SRC Indicator.java:590; SRC Indicator.java:823-829 |
| Indicator$LeftwardStartPredicate.shouldStart | REACHABLE | | Predicate method called from PendingStartAnimator (class in different batch) | SRC Indicator.java:827-829; INFERRED caller in Indicator$PendingStartAnimator.startIfNecessary |

STATUS: DONE 23:42
