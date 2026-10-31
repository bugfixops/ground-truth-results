STATUS RUNNING 2026-10-29 10:07 EDT (batch 048, label_048)

# batch 048: CurrencyUIFeatures, its listeners, ExchangeRateUpdaterFactory and two event constructors (39 methods, 4 class groups)

Class groups: CurrencyUIFeatures (11 methods), CurrencyUIFeatures$1 to $11 (24 methods), ExchangeRateUpdaterFactory (2), CurrencyDeletionConfirmedEvent (1), ExchangeRateUpdateConfirmedEvent (1).
Result: 33 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE.
Edges: 11 e() edges in graphs/MMEX/parts/label_048.py (7 FRAMEWORK listener edges, 4 non_standard RxJava CALL edges) and 13 sup pairs (4 same-batch, 9 from batch 050 callers).
Evidence: graphs/MMEX/parts/label_048.grep.txt (sections A to F). Source root: final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/.

| method | label | kind | reason | printed file:lines |
|---|---|---|---|---|
| CurrencyUIFeatures.<init> | REACHABLE | CALL (auto) | constructed by CurrencyListFragment on the menu, context menu, FAB and PriceDownloadedEvent paths; the list screen is CurrencyListActivity, started from the main menu | CurrencyUIFeatures.java:52-54; CurrencyListFragment.java:185, 239, 325, 356; CurrencyListActivity.java:50; MainActivity.java:643; AndroidManifest.xml:210 |
| CurrencyUIFeatures.getContext | REACHABLE | CALL (auto) | called on the reachable paths of notifyCurrencyCanNotBeDeleted, showDialogDeleteCurrency, showDialogImportAllCurrencies, showDialogUpdateExchangeRates, startCurrencyEditActivity, importCurrencies and onPriceDownloaded | CurrencyUIFeatures.java:59-61; CurrencyUIFeatures.java:74, 108, 115, 138, 161, 224, 231 |
| CurrencyUIFeatures.getService | REACHABLE | CALL (auto) | lazily creates CurrencyService; called by onPriceDownloaded and by the Rx Callable $11.call | CurrencyUIFeatures.java:63-68; CurrencyUIFeatures.java:92, 99, 236 |
| CurrencyUIFeatures.importCurrencies | REACHABLE | CALL (auto) | private; called by the OK listener $5.onClick, which the import-all dialog runs | CurrencyUIFeatures.java:227-258; CurrencyUIFeatures.java:146; CurrencyListFragment.java:189 |
| CurrencyUIFeatures.notifyCurrencyCanNotBeDeleted | REACHABLE | CALL (auto) | called by CurrencyListFragment.onContextItemSelected case 3 | CurrencyUIFeatures.java:70-84; CurrencyListFragment.java:274 |
| CurrencyUIFeatures.onPriceDownloaded | REACHABLE | CALL (auto) | called by CurrencyListFragment.onEvent(PriceDownloadedEvent), an EventBus subscriber; FixerService posts the event after a Retrofit response, so this route needs the network | CurrencyUIFeatures.java:90-111; CurrencyListFragment.java:357; FixerService.java:120 |
| CurrencyUIFeatures.showActiveInactiveSelectorForUpdate | UNREACHABLE | none (no route) | its only caller is CurrencyRecyclerListFragment.onOptionsItemSelected, and that fragment has no start site: the activity is in the manifest without an intent-filter and its only Intent is commented out | CurrencyUIFeatures.java:185-211; CurrencyRecyclerListFragment.java:311; CurrencyRecyclerListActivity.java:41; AndroidManifest.xml:359; MainActivity.java:644 |
| CurrencyUIFeatures.showDialogDeleteCurrency | REACHABLE | CALL (auto), FRAMEWORK to $2 and $3 | called by CurrencyListFragment.onContextItemSelected case 3 | CurrencyUIFeatures.java:113-134; CurrencyListFragment.java:278 |
| CurrencyUIFeatures.showDialogImportAllCurrencies | REACHABLE | CALL (auto), FRAMEWORK to $4 and $5 | called by CurrencyListFragment.onOptionsItemSelected (menu_import_all_currencies) | CurrencyUIFeatures.java:136-157; CurrencyListFragment.java:189 |
| CurrencyUIFeatures.showDialogUpdateExchangeRates | REACHABLE | CALL (auto), FRAMEWORK to $6 and $7 | called by CurrencyListFragment.onOptionsItemSelected (menu_update_exchange_rate) | CurrencyUIFeatures.java:159-180; CurrencyListFragment.java:193 |
| CurrencyUIFeatures.startCurrencyEditActivity | REACHABLE | CALL (auto); INTENT edge in label_046.py | called by CurrencyListFragment.onContextItemSelected case 0 and onFloatingActionButtonClicked | CurrencyUIFeatures.java:213-225; CurrencyListFragment.java:245, 326 |
| CurrencyUIFeatures$1.<init> | REACHABLE | CALL (auto) | created by notifyCurrencyCanNotBeDeleted | CurrencyUIFeatures.java:75 (auto), 76-81 (class body) |
| CurrencyUIFeatures$1.onClick | REACHABLE | FRAMEWORK | OK listener of the cannot-delete dialog; the framework calls it on tap; the body dismisses the dialog | CurrencyUIFeatures.java:78-80; AlertDialog.java:611-613; AlertController.java:160-167 |
| CurrencyUIFeatures$2.<init> | REACHABLE | CALL (auto) | created by showDialogDeleteCurrency (negative button) | CurrencyUIFeatures.java:120 (auto), 126-131 (class body) |
| CurrencyUIFeatures$2.onClick | REACHABLE | FRAMEWORK | Cancel listener of the delete dialog; calls dialog.cancel() | CurrencyUIFeatures.java:128-130; AlertDialog.java:637-639; AlertController.java:160-167 |
| CurrencyUIFeatures$3.<init> | REACHABLE | CALL (auto) | created by showDialogDeleteCurrency (positive button) | CurrencyUIFeatures.java:119 (auto), 120-125 (class body) |
| CurrencyUIFeatures$3.onClick | REACHABLE | FRAMEWORK, then CALL (auto) | OK listener of the delete dialog; posts CurrencyDeletionConfirmedEvent at line 123 (the EventBus subscribers are in batches 049 and 050) | CurrencyUIFeatures.java:122-124; AlertDialog.java:611-613; AlertController.java:160-167 |
| CurrencyUIFeatures$4.<init> | REACHABLE | CALL (auto) | created by showDialogImportAllCurrencies (negative button) | CurrencyUIFeatures.java:143 (auto), 149-154 (class body) |
| CurrencyUIFeatures$4.onClick | REACHABLE | FRAMEWORK | Cancel listener of the import dialog; calls dialog.cancel() | CurrencyUIFeatures.java:151-153; AlertDialog.java:637-639; AlertController.java:160-167 |
| CurrencyUIFeatures$5.<init> | REACHABLE | CALL (auto) | created by showDialogImportAllCurrencies (positive button) | CurrencyUIFeatures.java:142 (auto), 143-148 (class body) |
| CurrencyUIFeatures$5.onClick | REACHABLE | FRAMEWORK, then CALL (auto) | OK listener of the import dialog; calls importCurrencies at line 146 | CurrencyUIFeatures.java:145-147; AlertDialog.java:611-613; AlertController.java:160-167 |
| CurrencyUIFeatures$6.<init> | REACHABLE | CALL (auto) | created by showDialogUpdateExchangeRates (negative button) | CurrencyUIFeatures.java:166 (auto), 172-177 (class body) |
| CurrencyUIFeatures$6.onClick | REACHABLE | FRAMEWORK | Cancel listener of the update dialog; calls dialog.cancel() | CurrencyUIFeatures.java:174-176; AlertDialog.java:637-639; AlertController.java:160-167 |
| CurrencyUIFeatures$7.<init> | REACHABLE | CALL (auto) | created by showDialogUpdateExchangeRates (positive button) | CurrencyUIFeatures.java:165 (auto), 166-171 (class body) |
| CurrencyUIFeatures$7.onClick | REACHABLE | FRAMEWORK, then CALL (auto) | OK listener of the update dialog; posts ExchangeRateUpdateConfirmedEvent(true) at line 169 | CurrencyUIFeatures.java:168-170; AlertDialog.java:611-613; AlertController.java:160-167 |
| CurrencyUIFeatures$8.<init> | UNREACHABLE | none (no route) | created only in showActiveInactiveSelectorForUpdate, which is UNREACHABLE; its auto CALL at line 195 is cut by sup | CurrencyUIFeatures.java:203-208; label_048.grep.txt section D |
| CurrencyUIFeatures$8.onClick | UNREACHABLE | none (no route) | empty OK listener of the single-choice dialog, which is never shown; the class file has no post or dismiss call | CurrencyUIFeatures.java:205-207; label_048.grep.txt section C |
| CurrencyUIFeatures$9.<init> | UNREACHABLE | none (no route) | created only in showActiveInactiveSelectorForUpdate, which is UNREACHABLE; its auto CALL at line 194 is cut by sup | CurrencyUIFeatures.java:195-202; label_048.grep.txt section D |
| CurrencyUIFeatures$9.onClick | UNREACHABLE | none (no route) | single-choice listener of the dialog that is never shown; its auto CALL to ExchangeRateUpdateConfirmedEvent.<init> (line 199) is cut by sup | CurrencyUIFeatures.java:197-201; label_048.grep.txt sections C, D |
| CurrencyUIFeatures$10.<init> | REACHABLE | CALL (auto) | created by importCurrencies and passed to the Observable subscribe call | CurrencyUIFeatures.java:240 (auto), 241-257 (class body) |
| CurrencyUIFeatures$10.onCompleted | REACHABLE | CALL (Rx, non_standard) | RxJava calls it on the main thread after a successful call(); it closes the progress dialog (auto CALL at line 244) | CurrencyUIFeatures.java:243-246; label_048.grep.txt section D |
| CurrencyUIFeatures$10.onError | REACHABLE | CALL (Rx, non_standard), guard | RxJava calls it only when call() throws; it logs the error | CurrencyUIFeatures.java:248-251 |
| CurrencyUIFeatures$10.onNext | REACHABLE | CALL (Rx, non_standard) | RxJava delivers the Boolean result on the main thread; the body is empty | CurrencyUIFeatures.java:253-256 |
| CurrencyUIFeatures$11.<init> | REACHABLE | CALL (auto) | created by importCurrencies and passed to Observable.fromCallable | CurrencyUIFeatures.java:233 (auto), 233-238 (class body) |
| CurrencyUIFeatures$11.call | REACHABLE | CALL (Rx, non_standard) | RxJava runs call() on Schedulers.io() when importCurrencies subscribes; call() runs getService().importCurrenciesFromSystemLocales() (auto CALLs at line 236) | CurrencyUIFeatures.java:234-237; label_048.grep.txt section D |
| ExchangeRateUpdaterFactory.<init> | UNREACHABLE | none (no route) | the class has only static members, and no source in the source root constructs it (section B is empty for a new ExchangeRateUpdaterFactory); no auto record has it as destination | ExchangeRateUpdaterFactory.java:33; label_048.grep.txt section B |
| ExchangeRateUpdaterFactory.getUpdaterInstance | REACHABLE | CALL (auto) | called by CurrencyService.updateExchangeRates (line 519), which is reached from CurrencyService.updateExchangeRate (line 499), CurrencyListFragment.onContextItemSelected case 2, and CurrencyListFragment.onEvent(ExchangeRateUpdateConfirmedEvent) | ExchangeRateUpdaterFactory.java:35-58; CurrencyService.java:499, 519; CurrencyListFragment.java:265-267, 368 |
| CurrencyDeletionConfirmedEvent.<init> | REACHABLE | CALL (auto) | created by the OK listener $3.onClick | events/CurrencyDeletionConfirmedEvent.java:24-27; CurrencyUIFeatures.java:123 |
| ExchangeRateUpdateConfirmedEvent.<init> | REACHABLE | CALL (auto) | created by the OK listener $7.onClick; the auto CALL from $9.onClick (line 199) is cut | events/ExchangeRateUpdateConfirmedEvent.java:24-26; CurrencyUIFeatures.java:169 |

Notes:
1. Edges written in label_048.py: 7 FRAMEWORK edges from each dialog builder to its OK and Cancel listeners, and 4 non_standard CALL edges from importCurrencies to $11.call and to the $10 Subscriber methods (RxJava, library not read, INFERRED).
2. Cuts (sup, 13 pairs): 4 in this batch (showActiveInactiveSelectorForUpdate and $9.onClick); 9 from CurrencyRecyclerListFragment (batch 050) into this batch. The 9 hold only if batch 050 labels onContextItemSelected, onEvent(PriceDownloadedEvent) and onOptionsItemSelected UNREACHABLE. The grep evidence for that is section E: no start site for CurrencyRecyclerListActivity.
3. EventBus POST edges from $3.onClick and $7.onClick go to the @Subscribe onEvent methods of CurrencyListFragment (batch 049) and CurrencyRecyclerListFragment (batch 050). Those batches write them (D1); this batch does not.
4. onPriceDownloaded depends on the network path through FixerService.onContentDownloaded (batch 090 writes the Retrofit and EventBus POST edges). getUpdaterInstance is reached through CurrencyService.updateExchangeRates, which batch 047 owns.
5. Anonymous class numbers were matched to listeners by class-file symbols (label_048.grep.txt section C), not by source order.

STATUS DONE 2026-10-29 10:10 EDT
