# ---- batch 100: RecurringTransactionEditActivity$4.onClick (1 method; rows in label_100.md, evidence in label_100.grep.txt)
# Edges are written only for destinations owned by this batch (D1). The auto CALL records out of $4.onClick (plusDays, toDate, getPaymentDate, setPaymentDate, the MmxDate constructor) and the record that creates $4 (initializePaymentDateSelector -> $4.<init>, line 390) are in auto_calls.json, so none is written here (D7).
# UNREACHABLE entries: none (the method is REACHABLE). sup pairs: none (no UNREACHABLE caller in this batch).
# SCREENS key S_RECURRING_TRANSACTION_EDIT is defined once, in label_099.py (merged first); this batch reuses it.

# ---- the next-day chevron on the payment date row (listener set at RecurringTransactionEditActivity.java:390)

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$4.onClick',
    'Tap the next-day chevron on the payment date row of the recurring transaction form',
    via='View.OnClickListener registered by setOnClickListener (line 390); the framework calls onClick from performClick on a tap (FW-SRC View.java:6294)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:390-396 (listener at 390; onClick 392-395; plusDays 393; setPaymentDate 394); SRC recurring/transactions/RecurringTransactionEditActivity.java:346-347 (early return only when paymentDateTextView is null), 419 (view set), 282 (initializePaymentDateSelector call), 280 (initializeControls), 136 (initializeControls call from onCreate); SRC res/layout/activity_edit_recurring_transaction.xml:127 (paymentNextDayButton), 100-145 (no visibility attribute); FW-SRC core/java/android/view/View.java:6143-6147 (setOnClickListener), 6289-6295 (performClick calls onClick at 6294), 12999 and 13029-13045 (a tap calls performClick); INFERRED com.shamanland.fonticon.FontIconView source not read')
