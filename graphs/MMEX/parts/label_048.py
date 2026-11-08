# label_048.py: batch 048 (39 methods in 4 class groups): CurrencyUIFeatures (11), CurrencyUIFeatures$1 to $11 (24),
# ExchangeRateUpdaterFactory (2), CurrencyDeletionConfirmedEvent.<init> (1), ExchangeRateUpdateConfirmedEvent.<init> (1).
# Result: 33 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE. Rows and printed lines: graphs/MMEX/parts/label_048.md.
# Grep evidence: graphs/MMEX/parts/label_048.grep.txt (sections A to F).
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 7 FRAMEWORK edges from the dialog-building methods to their OK and Cancel listeners (AlertDialog, AlertController),
#   - 4 non_standard CALL edges from importCurrencies to the RxJava Callable and Subscriber methods (library, INFERRED),
#   - 13 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE and whose callee is in batch 048.
#     4 pairs start in showActiveInactiveSelectorForUpdate or its listener $9.onClick (same batch).
#     9 pairs start in CurrencyRecyclerListFragment methods of batch 050 (the fragment has no start site).
# EventBus POST edges from $3.onClick and $7.onClick go to the @Subscribe methods of batches 049 and 050, which write them (D1).

# ================================================================== dialog listeners (FRAMEWORK)

e('CurrencyUIFeatures.notifyCurrencyCanNotBeDeleted', 'CurrencyUIFeatures$1.onClick', 'FRAMEWORK',
  'the cannot-delete-currency dialog is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  evidence='SRC currency/CurrencyUIFeatures.java:76-80 (setPositiveButton at 76, onClick dismisses at 79); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166)')

e('CurrencyUIFeatures.showDialogDeleteCurrency', 'CurrencyUIFeatures$3.onClick', 'FRAMEWORK',
  'the delete-currency dialog is shown; the user taps OK and the framework calls the positive listener, which posts CurrencyDeletionConfirmedEvent',
  evidence='SRC currency/CurrencyUIFeatures.java:120-125 (setPositiveButton at 120, post at 123); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogDeleteCurrency', 'CurrencyUIFeatures$2.onClick', 'FRAMEWORK',
  'the delete-currency dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:126-131 (setNegativeButton at 126, cancel at 129); FW-SRC core/java/android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogImportAllCurrencies', 'CurrencyUIFeatures$5.onClick', 'FRAMEWORK',
  'the import-all-currencies dialog is shown; the user taps OK and the framework calls the positive listener, which calls importCurrencies',
  evidence='SRC currency/CurrencyUIFeatures.java:143-148 (setPositiveButton at 143, importCurrencies at 146); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogImportAllCurrencies', 'CurrencyUIFeatures$4.onClick', 'FRAMEWORK',
  'the import-all-currencies dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:149-154 (setNegativeButton at 149, cancel at 152); FW-SRC core/java/android/app/AlertDialog.java:637-639; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogUpdateExchangeRates', 'CurrencyUIFeatures$7.onClick', 'FRAMEWORK',
  'the update-exchange-rates dialog is shown; the user taps OK and the framework calls the positive listener, which posts ExchangeRateUpdateConfirmedEvent(true)',
  evidence='SRC currency/CurrencyUIFeatures.java:166-171 (setPositiveButton at 166, post at 169); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogUpdateExchangeRates', 'CurrencyUIFeatures$6.onClick', 'FRAMEWORK',
  'the update-exchange-rates dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:172-177 (setNegativeButton at 172, cancel at 175); FW-SRC core/java/android/app/AlertDialog.java:637-639; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

# ================================================================== importCurrencies (RxJava, library not read: INFERRED)

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$11.call', 'CALL',
  'importCurrencies subscribes to Observable.fromCallable; RxJava runs call() on the io scheduler, which imports the currencies from the system locales',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Observable.fromCallable(Callable) runs Callable.call when subscribed on Schedulers.io() (subscribeOn at CurrencyUIFeatures.java:239)',
  evidence='SRC currency/CurrencyUIFeatures.java:233-240 (fromCallable, subscribeOn); auto_calls records CurrencyUIFeatures$11.call -> CurrencyUIFeatures.getService and CurrencyService.importCurrenciesFromSystemLocales (236)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onNext', 'CALL',
  'the Subscriber receives the Boolean result of call() on the main thread; the onNext body is empty',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onNext delivered after observeOn(AndroidSchedulers.mainThread()) (CurrencyUIFeatures.java:240)',
  evidence='SRC currency/CurrencyUIFeatures.java:241-256 (subscribe with Subscriber, onNext at 254-256)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onCompleted', 'CALL',
  'after call() finishes without an error RxJava calls onCompleted on the main thread, which closes the progress dialog',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onCompleted after observeOn(AndroidSchedulers.mainThread())',
  evidence='SRC currency/CurrencyUIFeatures.java:243-246; auto_calls record CurrencyUIFeatures$10.onCompleted -> DialogUtils.closeProgressDialog (244)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onError', 'CALL',
  'RxJava calls onError with the exception and onError logs it',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onError delivers the exception thrown by Callable.call',
  guard='call() throws, so RxJava delivers the exception to onError instead of onNext and onCompleted',
  evidence='SRC currency/CurrencyUIFeatures.java:248-251 (onError, Timber.e at 250)')

# ================================================================== sup cuts (D14a)

# Caller showActiveInactiveSelectorForUpdate is UNREACHABLE in this batch (its only caller is in an unreachable fragment).
# Its auto CALLs to its two listeners and to getContext are cut here; the one auto CALL out of the dead listener $9.onClick is cut too.
sup(('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures$9.<init>'),
    ('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures$8.<init>'),
    ('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures.getContext'),
    ('CurrencyUIFeatures$9.onClick', 'ExchangeRateUpdateConfirmedEvent.<init>'))

# Callers in batch 050 (CurrencyRecyclerListFragment): the fragment is UNREACHABLE because CurrencyRecyclerListActivity has no start site
# (AndroidManifest.xml:359 has no intent-filter; the only Intent, MainActivity.java:644, is commented out). Their auto CALLs into batch 048
# are cut here, because the owner of the target writes the cut (D14a). Batch 050 must label these three callers UNREACHABLE; if it does not,
# remove these nine pairs and restore the edges.
sup(('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.showDialogImportAllCurrencies'),
    ('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.showActiveInactiveSelectorForUpdate'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.startCurrencyEditActivity'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.notifyCurrencyCanNotBeDeleted'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.showDialogDeleteCurrency'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'CurrencyUIFeatures.onPriceDownloaded'))

# ================================================================== UNREACHABLE (batch 048)

UNREACHABLE['CurrencyUIFeatures.showActiveInactiveSelectorForUpdate'] = ('no_trigger_in_app',
  'Its only caller is CurrencyRecyclerListFragment.onOptionsItemSelected (CurrencyRecyclerListFragment.java:311). That fragment is created only by CurrencyRecyclerListActivity.onCreate (line 41), and nothing starts that activity: the manifest entry (AndroidManifest.xml:359) has no intent-filter and the only Intent for it (MainActivity.java:644) is commented out. The currency menu starts CurrencyListActivity instead (MainActivity.java:643). Its auto CALLs are cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:185-211; recycler/CurrencyRecyclerListFragment.java:311; recycler/CurrencyRecyclerListActivity.java:41; AndroidManifest.xml:359; MainActivity.java:641-646; label_048.grep.txt sections B, E',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$8.<init>'] = ('no_trigger_in_app',
  'Constructed only inside showActiveInactiveSelectorForUpdate, which is UNREACHABLE. Its auto CALL (CurrencyUIFeatures.java:195) is cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:203-208; auto_calls record showActiveInactiveSelectorForUpdate -> CurrencyUIFeatures$8.<init>; label_048.grep.txt section D',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$8.onClick'] = ('no_trigger_in_app',
  'Empty positive listener of the single-choice dialog built by showActiveInactiveSelectorForUpdate, which is UNREACHABLE, so the dialog is never shown and the framework never calls this listener. The class file has no post or dismiss call (section C).',
  'SRC currency/CurrencyUIFeatures.java:203-208; label_048.grep.txt section C',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$9.<init>'] = ('no_trigger_in_app',
  'Constructed only inside showActiveInactiveSelectorForUpdate, which is UNREACHABLE. Its auto CALL (CurrencyUIFeatures.java:194) is cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:195-202; auto_calls record showActiveInactiveSelectorForUpdate -> CurrencyUIFeatures$9.<init>; label_048.grep.txt section D',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$9.onClick'] = ('no_trigger_in_app',
  'Single-choice listener of the dialog built by showActiveInactiveSelectorForUpdate, which is UNREACHABLE, so no click is delivered. Its auto CALL to ExchangeRateUpdateConfirmedEvent.<init> (CurrencyUIFeatures.java:199) is cut by sup above, so that event constructor is not reached from here.',
  'SRC currency/CurrencyUIFeatures.java:197-201; auto_calls record CurrencyUIFeatures$9.onClick -> ExchangeRateUpdateConfirmedEvent.<init> (199); label_048.grep.txt sections C, D',
  'SOURCE')

UNREACHABLE['ExchangeRateUpdaterFactory.<init>'] = ('no_trigger_in_app',
  'The class has only static members and no source in the source root constructs it (section B is empty for new ExchangeRateUpdaterFactory). No auto record has it as destination, so the implicit default constructor is never called.',
  'SRC currency/ExchangeRateUpdaterFactory.java:33 (no constructor declared); label_048.grep.txt section B',
  'SOURCE')
