# ================================================================== batch 112 (label_112): RecurringTransactionService (17 methods), ServiceBase (2), QifExport (5), QifGenerator (2), QifHeader (6), QifRecord (8)
# Result: 36 REACHABLE, 4 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_112.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_112.grep.txt (sections 1-9).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7). The routes start at callers in other batches (MainActivity, CheckingTransactionEditActivity, RecurringTransactionEditActivity, RecurringTransactionListFragment, AllDataListFragment).
# This file writes:
#   - UNREACHABLE entries for RecurringTransactionService.<init>(Context), RecurringTransactionService.load, RecurringTransactionService.getRecurrenceLocalizedName, QifHeader.createCreditCardHeader (SOURCE),
#   - 4 sup pairs (D14): the auto CALL records out of the UNREACHABLE methods.
# QifHeader.createCreditCardHeader has no CALL record out, so it has no sup pair. Its framework call (StringBuilder.<init>) and the framework calls of getRecurrenceLocalizedName (Context.getResources, Resources.getStringArray) are framework_calls, not CALL records to app methods, so they are not cut.

# ================================================================== RecurringTransactionService: UNREACHABLE (source evidence)

UNREACHABLE['RecurringTransactionService.<init>(Context)'] = ('no_trigger_in_app',
    'no caller: every constructor call in app source is the two-argument form (MainActivity.java:1281; CheckingTransactionEditActivity.java:238, 700; RecurringTransactionEditActivity.java:451; RecurringTransactionListFragment.java:312, 341); no subclass exists; no bytecode CALL record targets this constructor',
    'servicelayer/RecurringTransactionService.java:47-50; label_112.grep.txt sections 1, 2, 6, 7',
    'SOURCE')

UNREACHABLE['RecurringTransactionService.load'] = ('no_trigger_in_app',
    'no caller: no bytecode CALL record targets load, and in the five app files that name the service no call is made on a RecurringTransactionService variable (the .load calls there are on repository or database objects)',
    'servicelayer/RecurringTransactionService.java:167-169; label_112.grep.txt sections 3a-3d, 6, 7',
    'SOURCE')

UNREACHABLE['RecurringTransactionService.getRecurrenceLocalizedName'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration in the whole source root (every file type), and no bytecode CALL record targets it',
    'servicelayer/RecurringTransactionService.java:335-350; label_112.grep.txt sections 4, 6, 7, 9',
    'SOURCE')

# ================================================================== QifHeader: UNREACHABLE (source evidence)

UNREACHABLE['QifHeader.createCreditCardHeader'] = ('no_trigger_in_app',
    'private, no caller: the name occurs only at its declaration (QifHeader.java:131) in the whole source root, and no bytecode CALL record targets it; the body only returns the placeholder "not implemented" (line 142)',
    'servicelayer/qif/QifHeader.java:131-143; label_112.grep.txt sections 5, 7, 9',
    'SOURCE')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionService.<init>(Context)', 'ServiceBase.<init>'))  # the unreachable constructor's call into the base constructor cannot run (RecurringTransactionService.java:48)
sup(('RecurringTransactionService.load', 'RecurringTransactionRepository.load'))  # load has no caller (RecurringTransactionService.java:168)
sup(('RecurringTransactionService.load', 'RecurringTransactionService.getRepository'))  # load has no caller (RecurringTransactionService.java:168)
sup(('RecurringTransactionService.getRecurrenceLocalizedName', 'ServiceBase.getContext'))  # getRecurrenceLocalizedName has no caller (RecurringTransactionService.java:345)
