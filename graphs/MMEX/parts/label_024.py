# batch 024 (label_024): com.money.manager.ex.common.AmountInputDialog, methods 41-43 of 43: $6.onClick, $7.<init>, $7.onClick.
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_024.md.
# This batch defines and reuses no page (batch 023 defines none either).
# The three methods are reached from AmountInputDialog.onCreateDialog (batch 023). $7.<init> has its CALL edge in auto_calls.json (lines 35414-35416), so none is written here.
# The two button listeners are framework callbacks: AlertDialog.Builder stores them, and AlertController calls onClick on a tap. Framework lines were read from fw_src (FW-SRC).
# Which listener is which: the body of AmountInputDialog$7.onClick holds evalExpression (line 258) and the EventBus post (line 260), the OK body of source lines 255-264; the body of AmountInputDialog$6.onClick holds only DialogInterface.dismiss, the Cancel body of source lines 265-270 (auto_calls.json 70666-70668 and 71119-71126). grep evidence: graphs/MMEX/parts/label_024.grep.txt.

# ---- the buttons: onCreateDialog stores the listeners, the framework calls onClick on a tap

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$6.onClick', 'FRAMEWORK',
  'the Cancel button: setNegativeButton stores the listener (AlertDialog.java:637-641); AlertParams.apply sets the button with it (AlertController.java:1025-1027); setButton keeps the message with the listener (AlertController.java:344-360); a tap runs mButtonHandler, which sends the message (AlertController.java:125-147); ButtonHandler.handleMessage calls onClick (AlertController.java:160-167)',
  guard='the user taps Cancel (android.R.string.cancel) in the amount input dialog (the listener at lines 265-270)',
  evidence='SRC common/AmountInputDialog.java:265-270; auto_calls.json:70666-70668 (AmountInputDialog$6.onClick calls only DialogInterface.dismiss); FW-SRC core/java/android/app/AlertDialog.java:637-641; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 344-360, 125-147, 160-167')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$7.onClick', 'FRAMEWORK',
  'the OK button: setPositiveButton stores the listener (AlertDialog.java:611-613); AlertParams.apply sets the button with it (AlertController.java:1021-1024); setButton keeps the message with the listener (AlertController.java:344-355); a tap runs mButtonHandler, which sends the message (AlertController.java:125-147); ButtonHandler.handleMessage calls onClick (AlertController.java:160-167)',
  guard='the user taps OK (android.R.string.ok) in the amount input dialog (the listener at lines 255-264); the body returns before the post when evalExpression() is false (line 258)',
  evidence='SRC common/AmountInputDialog.java:255-264; auto_calls.json:39342-39363 (AmountInputDialog$7.onClick calls evalExpression at line 258 and EventBus.post with AmountEnteredEvent at line 260); auto_calls.json:71119-71126; FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1024, 344-355, 125-147, 160-167')
