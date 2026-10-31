# ================================================================== batch 068 (label_068): RecurringTransaction, methods 1-40 of 57
# Result: 38 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_068.md).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived) whose caller is reached in another batch.
# This file writes:
#   - UNREACHABLE entries for RecurringTransaction.getPaymentDateString and RecurringTransaction.setPaymentDate(String) (SOURCE),
#   - 2 sup pairs (D14a): their auto CALL records to EntityBase.getString and EntityBase.setString.
# Grep evidence: graphs/MMEX/parts/label_068.grep.txt (sections 1-3).

# ================================================================== RecurringTransaction: UNREACHABLE (source evidence)

UNREACHABLE['RecurringTransaction.getPaymentDateString'] = ('no_trigger_in_app',
    'no caller in app source: the name appears only at its definition (no XML or data-binding reference either); no bytecode CALL record targets it',
    'domainmodel/RecurringTransaction.java:212-214; label_068.grep.txt section 1', 'SOURCE')

UNREACHABLE['RecurringTransaction.setPaymentDate(String)'] = ('no_trigger_in_app',
    'no call site passes a String: the call sites in app source pass a Date (RecurringTransactionEditActivity.java:362, 386, 394, 404, 626, 635 and RecurringTransactionService.java:426), and no bytecode CALL record targets this overload',
    'domainmodel/RecurringTransaction.java:216-218; RecurringTransactionEditActivity.java:362, 386, 394, 404, 626, 635; RecurringTransactionService.java:426; label_068.grep.txt section 2', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransaction.getPaymentDateString', 'EntityBase.getString'))
sup(('RecurringTransaction.setPaymentDate(String)', 'EntityBase.setString'))
