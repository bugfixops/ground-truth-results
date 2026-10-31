# ================================================================== batch 078 (label_078): HomeFragment$3 to HomeFragment$8,
# 13 methods (graphs/MMEX/scratch/batches/batch_078.txt): $3 (onClick), $4 (onSuccess, onError), $5 (call), $6 (onChildClick),
# $7 (onGroupCollapse), $8 (onGroupExpand), and the six <init> methods.
# Rows, printed lines and counts: graphs/MMEX/parts/label_078.md. Result: 13 REACHABLE, 0 UNREACHABLE.
# This file writes:
#   - 4 gui() edges from the home page S_HOME (defined by batch 077, label_077.py line 9; not redefined here):
#     the add account button, an account row tap, and the group header taps (collapse and expand),
#   - 3 e() edges from HomeFragment.loadUsername (batch 077) into the RxJava 1 callbacks: Callable.call, onSuccess, onError
#     (cls='non_standard', the library dispatches them).
# The six <init> methods are auto CALL records (auto_calls.json), so no edge is written for them (D7).
# The INTENT edge from HomeFragment$3.onClick to AccountEditActivity.<init> is written by batch 006 (label_006.py), not here.
# No sup pairs (no UNREACHABLE caller). No UNREACHABLE entries. No grep file (no library or generated class is UNREACHABLE).
# No new named constants: the gate texts are inline state_text(...) calls (D2).

# ---- GUI edges from the home page S_HOME (MainActivity shows HomeFragment; its ENTERS edge is written by batch 080)

gui('S_HOME', 'HomeFragment$3.onClick',
    'Tap Add account (buttonAddAccount) on the welcome view; the welcome view is shown only when the account list is empty',
    needs_state=state_text('the account list is empty, so the welcome view with the Add account button is shown (HomeFragment.java:793-794)', ('account',)),
    evidence='SRC home/HomeFragment.java:612-622 (button 612, listener 614, onClick 617-621); SRC res/layout/welcome_layout.xml:65-66; SRC res/layout/home_fragment.xml:181-184; SRC home/HomeFragment.java:792-794 (visibility)')

gui('S_HOME', 'HomeFragment$6.onChildClick',
    'Tap an account row (a child row) in the account list, which is shown only when at least one account exists',
    needs_state=state_text('at least one account exists, so the account list shows rows (HomeFragment.java:793), and the row group is expanded (group expansion is saved in settings, HomeFragment.java:719 and 731)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:686-706 (onChildClick, event post 704), 792-794, 877-878 (listViewAccountBills); INFERRED the expandable list calls the child-click listener on a row tap (Android library not read)')

gui('S_HOME', 'HomeFragment$7.onGroupCollapse',
    'Tap an expanded account-type group header (the group title row) to collapse it',
    needs_state=state_text('at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is expanded (its saved setting is true, HomeFragment.java:754)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:710-719 (listener 710, body 716-719), 747-760 (saved flag read at 754), 792-794; INFERRED the expandable list calls the collapse listener on a header tap (Android library not read)')

gui('S_HOME', 'HomeFragment$8.onGroupExpand',
    'Tap a collapsed account-type group header (the group title row) to expand it',
    needs_state=state_text('at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is collapsed (its saved setting is false, HomeFragment.java:719)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:722-731 (listener 722, body 726-731), 747-760, 792-794; INFERRED the expandable list calls the expand listener on a header tap (Android library not read)')

# ---- RxJava 1 callbacks of the username load: loadUsername subscribes the Single (line 649); the library runs the callables

e('HomeFragment.loadUsername', 'HomeFragment$5.call', 'CALL',
  'RxJava 1 runs the Callable on the io thread once loadUsername subscribes the Single (subscribeOn at line 647); the body opens InfoService and reads the user name (lines 643-644)',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): Single.fromCallable(Callable) runs Callable.call when subscribed on Schedulers.io() (subscribeOn at HomeFragment.java:647)',
  evidence='SRC home/HomeFragment.java:638-662 (fromCallable 640, call 642-645, subscribeOn 647, subscribe 649); auto_calls records HomeFragment$5.call -> InfoService.<init> (line 643), InfoService.getInfoValue (line 644); the RxJava library is not in the dataset (INFERRED)')

e('HomeFragment.loadUsername', 'HomeFragment$4.onSuccess', 'CALL',
  'RxJava 1 delivers the value returned by call to SingleSubscriber.onSuccess on the main thread (observeOn at line 648); the body sets the user name and posts UsernameLoadedEvent (lines 652-653)',
  guard='call() returns normally: it does unless the InfoService constructor throws (InfoService.java:45-48, outside the try at line 112); getInfoValue returns null or a value when a database read fails, because its catch (line 123) does not rethrow',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): SingleSubscriber.onSuccess is delivered after observeOn(AndroidSchedulers.mainThread()) (HomeFragment.java:648-649)',
  evidence='SRC home/HomeFragment.java:638-662 (observeOn 648, subscribe 649, onSuccess 651-653); SRC servicelayer/InfoService.java:112-123 (getInfoValue catches Exception and returns ret); auto_calls record HomeFragment$4.onSuccess -> UsernameLoadedEvent.<init> (line 653)')

e('HomeFragment.loadUsername', 'HomeFragment$4.onError', 'CALL',
  'RxJava 1 delivers an exception thrown by Callable.call to SingleSubscriber.onError on the main thread; the body logs it with Timber (line 658)',
  guard='call() throws: only when the InfoService constructor throws (new InfoService at line 643; the constructor at InfoService.java:45-48 has no try). getInfoValue catches its own exceptions (InfoService.java:123), so a database failure reaches onSuccess instead',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): SingleSubscriber.onError delivers the exception thrown by Callable.call (HomeFragment.java:640-645, 657-658)',
  evidence='SRC home/HomeFragment.java:638-662 (onError 657-659, Timber.e 658); SRC servicelayer/InfoService.java:45-48, 112-123; auto_calls record HomeFragment$4.onError -> Timber.e')
