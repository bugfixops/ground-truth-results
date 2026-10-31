# ================================================================== batch 138 (label_138): com.money.manager.ex.utils.MmxDate (methods 1-40 of 56 in this class; 40 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_138.md (34 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_138.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 6 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The six UNREACHABLE methods have no auto CALL records into them.
# getHour and getMinute keep their outgoing auto CALL records (to getHourOfDay and getMinuteOfHour, REACHABLE, owned by no other batch), so no sup pair is written (D14(a), D18, D20).
# Routes through batch 139 (MmxDate.setTimeToBeginningOfDay, MmxDate.java:317-318) are interim (D8): setHour (row 40) uses that hop.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

UNREACHABLE['MmxDate.<init>(Calendar)'] = (
  'no_trigger_in_app',
  'Constructor taking a Calendar. zero auto CALL records target it (auto_calls.json has no dst MmxDate.<init>(Calendar)). None of the 106 source "new MmxDate(" sites passes a Calendar: the single-argument sites pass Date, String or long values, and the Calendar-typed locals in the six files that also build an MmxDate (IncomeVsExpensesListFragment.java:489-493, InvestmentTransactionEditActivity.java:348-349, MmxDateTimeUtils.java:151-152) are not passed to a constructor.',
  'label_138.grep.txt S1 (106 hits of new MmxDate( in the source root), S2 continued ("MmxDate.<init>(Calendar) incoming 0"), S2b, S2c; MmxDate.java:94-96',
  'SOURCE')

UNREACHABLE['MmxDate.getCalendar'] = (
  'no_trigger_in_app',
  'Accessor returning the internal Calendar. zero auto CALL records target it, and the source root has no ".getCalendar()" call (python3 -I grep, 0 hits). Nothing in the app reads the Calendar back out of an MmxDate.',
  'label_138.grep.txt S2 ("\\.getCalendar\\(\\)  hits: 0"), S2 continued ("MmxDate.getCalendar incoming 0"); MmxDate.java:167-169',
  'SOURCE')

UNREACHABLE['MmxDate.getHour'] = (
  'no_trigger_in_app',
  'Alias of getHourOfDay. zero auto CALL records target it, and the source root has no ".getHour()" call (python3 -I grep, 0 hits). Its outgoing edge to MmxDate.getHourOfDay (REACHABLE, MmxDate.java:180) is an auto record and is kept; no sup is written for it.',
  'label_138.grep.txt S2 ("\\.getHour\\(\\)  hits: 0"), S2 continued ("MmxDate.getHour incoming 0"); MmxDate.java:179-181',
  'SOURCE')

UNREACHABLE['MmxDate.getMinute'] = (
  'no_trigger_in_app',
  'Alias of getMinuteOfHour. zero auto CALL records target it, and the source root has no ".getMinute()" call (python3 -I grep, 0 hits). Its outgoing edge to MmxDate.getMinuteOfHour (REACHABLE, MmxDate.java:192) is an auto record and is kept; no sup is written for it.',
  'label_138.grep.txt S2 ("\\.getMinute\\(\\)  hits: 0"), S2 continued ("MmxDate.getMinute incoming 0"); MmxDate.java:191-193',
  'SOURCE')

UNREACHABLE['MmxDate.setCalendar'] = (
  'no_trigger_in_app',
  'Setter replacing the internal Calendar. zero auto CALL records target it, and the source root has no ".setCalendar(" call (python3 -I grep, 0 hits).',
  'label_138.grep.txt S2 ("\\.setCalendar\\(  hits: 0"), S2 continued ("MmxDate.setCalendar incoming 0"); MmxDate.java:267-270',
  'SOURCE')

UNREACHABLE['MmxDate.setDate'] = (
  'no_trigger_in_app',
  'Setter for day of month taking an int. zero auto CALL records target MmxDate.setDate(int). The 8 source ".setDate(" hits all call entity setters with a Date argument (MainActivity.java:1267 accountTrx.setDate(scheduledTrx.getPaymentDate()); EditTransactionCommonFunctions.java:484 and 1549-1552 with Date values; CheckingTransactionEditActivity.java:262, 286, 436, 576; SmsReceiverTransactions.java:236), so none binds to the int overload.',
  'label_138.grep.txt S2 ("\\.setDate\\(  hits: 8"), S2 continued ("MmxDate.setDate incoming 0"); MainActivity.java:1267; EditTransactionCommonFunctions.java:484, 1549-1552; MmxDate.java:272-275',
  'SOURCE')
