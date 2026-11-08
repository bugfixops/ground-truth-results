# ================================================================== batch 131 (label_131): com.money.manager.ex.transactions.EditTransactionCommonFunctions (methods 41-80 of 115 in this class; 40 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_131.md (40 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_131.grep.txt.
# This file writes 6 e() edges (FRAMEWORK, listener callbacks), 0 gui() edges, 0 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# The callers of this batch's methods are in batches 128, 099, 130 and 132, which are not merged; those routes are interim (D8).
# A listener registered inside one of this batch's methods gets an edge from the registering method to the listener's callback (label_099.py convention). cls is standard.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source was not read.

# ---- account spinners (listener built in initAccountSelectors, set at 381 and 388)

e('EditTransactionCommonFunctions.initAccountSelectors', 'EditTransactionCommonFunctions$1.onItemSelected', 'FRAMEWORK',
  'the account spinner and the transfer-to spinner call onItemSelected when the user picks a row: AdapterView.fireOnSelected calls the listener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:310-312 (listener creation), 381 (spinAccount.setOnItemSelectedListener), 388 (spinAccountTo.setOnItemSelectedListener); FW-SRC core/java/android/widget/AdapterView.java:412-413 (setOnItemSelectedListener stores the listener), 937-944 (fireOnSelected calls onItemSelected at 944); INFERRED: AbsSpinner.java is not in fw_src, so the path from the user pick to fireOnSelected is not read')

e('EditTransactionCommonFunctions.initAccountSelectors', 'EditTransactionCommonFunctions$1.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when a spinner has no selected position: AdapterView.fireOnSelected calls the listener for a negative position',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:370-372 (empty onNothingSelected body), 381, 388 (listener set on both spinners); FW-SRC core/java/android/widget/AdapterView.java:945-947 (onNothingSelected called for a negative position); INFERRED: the code path that gives these spinners a negative position is not read')

# ---- remove-payee button (listener at 582)

e('EditTransactionCommonFunctions.initPayeeControls', 'EditTransactionCommonFunctions$10.onClick', 'FRAMEWORK',
  'the remove-payee button calls onClick on a tap: View.performClick calls the OnClickListener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:582-592 (removePayeeButton.setOnClickListener at 582; onClick body 583-591); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls li.mOnClickListener.onClick(this) at 6294); INFERRED: the touch path to performClick is not read')

# ---- split button (listener at 599)

e('EditTransactionCommonFunctions.initSplitCategories', 'EditTransactionCommonFunctions$11.onClick', 'FRAMEWORK',
  'the split button calls onClick on a tap: View.performClick calls the OnClickListener, which calls isSplitSelected and then either the split form or the reset notice',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:599-623 (splitButton.setOnClickListener at 599; onClick body within 599-623); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read')

# ---- status spinner (listener at 646)

e('EditTransactionCommonFunctions.initStatusSelector', 'EditTransactionCommonFunctions$12.onItemSelected', 'FRAMEWORK',
  'the status spinner calls onItemSelected when the user picks a status: AdapterView.fireOnSelected calls the listener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:646 (spinStatus.setOnItemSelectedListener), 646-657 (onItemSelected body); FW-SRC core/java/android/widget/AdapterView.java:412-413 (setOnItemSelectedListener stores the listener), 937-944 (fireOnSelected calls onItemSelected at 944); INFERRED: AbsSpinner.java is not in fw_src, as for $1')

e('EditTransactionCommonFunctions.initStatusSelector', 'EditTransactionCommonFunctions$12.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when the status spinner has no selected position: AdapterView.fireOnSelected calls the listener for a negative position',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:659-661 (empty onNothingSelected body), 646 (listener set); FW-SRC core/java/android/widget/AdapterView.java:945-947 (onNothingSelected called for a negative position); INFERRED: AbsSpinner.java is not in fw_src, so the path to a negative position is not read')
