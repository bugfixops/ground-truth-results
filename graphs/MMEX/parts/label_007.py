# ================================================================== batch 007 (label_007): com.money.manager.ex.account.AccountEditActivity (methods 41-52 of 52)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_007.md.
# Every edge below has a batch 007 method as its destination. Its source is the page S_ACCOUNT_EDIT (defined in part 006).
# The listener constructors ($4.<init> to $9.<init>) and the bytecode calls out of them are in auto_calls.json, so no CALL edge is written here.
# No method of this batch is UNREACHABLE, so there are no UNREACHABLE entries and no sup pairs.

# ---- AccountEditActivity$4: the currency field

e('S_ACCOUNT_EDIT', 'AccountEditActivity$4.onClick', 'GUI',
  'the currency field is tapped: startActivityForResult(ACTION_PICK) opens CurrencyListActivity with RequestCodes.CURRENCY',
  gui=['Tap the currency field (textViewSelectCurrency) on the account form'],
  evidence='SRC account/AccountEditActivity.java:390-397 (listener 390; onClick 392-396; startActivityForResult 395); res/layout/activity_account_edit.xml:138')

# ---- AccountEditActivity$5: the initial date text and the date picker

e('S_ACCOUNT_EDIT', 'AccountEditActivity$5.onClick', 'GUI',
  'the initial date text is tapped: a DatePickerDialog opens on the account initial date, with the listener from the field initialiser',
  gui=['Tap the date text between the two arrows on the account form'],
  evidence='SRC account/AccountEditActivity.java:400-421 (listener 400; onClick 407-420; DatePickerDialog 411-419); SRC account/AccountEditViewHolder.java:60 (txtInitialDate is textViewDate); res/layout/activity_account_edit.xml:207-215')

e('AccountEditActivity$5.onClick', 'AccountEditActivity$5.lambda$$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog.onClick calls the OnDateSetListener, which is this lambda, and the lambda body runs',
  gui=['Tap the date text, then tap OK in the date picker'],
  evidence='SRC account/AccountEditActivity.java:401-405 (lambda listener); SRC account/AccountEditActivity.java:411-417 (DatePickerDialog built with the listener); FW-SRC core/java/android/app/DatePickerDialog.java:88-90 (public constructor passes the listener on), 122 (BUTTON_POSITIVE set to this), 136 (listener stored), 164-172 (BUTTON_POSITIVE calls mDateSetListener.onDateSet at 171); INFERRED the dialog button dispatch to DatePickerDialog.onClick is not printed (AlertController not read)')

# ---- AccountEditActivity$6: previous-day arrow

e('S_ACCOUNT_EDIT', 'AccountEditActivity$6.onClick', 'GUI',
  'the previous-day arrow is tapped: the initial date moves back one day (MmxDate.minusDays(1)) and showDate runs',
  gui=['Tap the left arrow beside the initial date'],
  evidence='SRC account/AccountEditActivity.java:423-430 (listener 423; onClick 425-429); res/layout/activity_account_edit.xml:197-204 (previousDayButton)')

# ---- AccountEditActivity$7: next-day arrow

e('S_ACCOUNT_EDIT', 'AccountEditActivity$7.onClick', 'GUI',
  'the next-day arrow is tapped: the initial date moves forward one day (MmxDate.plusDays(1)) and showDate runs',
  gui=['Tap the right arrow beside the initial date'],
  evidence='SRC account/AccountEditActivity.java:432-439 (listener 432; onClick 434-438); res/layout/activity_account_edit.xml:218-222 (nextDayButton)')

# ---- AccountEditActivity$8: default-account checkbox

e('S_ACCOUNT_EDIT', 'AccountEditActivity$8.onCheckedChanged', 'GUI',
  'the default-account checkbox is tapped: the CheckBox changes its checked state and calls the listener, which sets mIsDefault and calls displayDefaultAccount',
  gui=['Tap the default-account checkbox'],
  evidence='SRC account/AccountEditActivity.java:512-518 (listener 512; onCheckedChanged 513-518); res/layout/activity_account_edit.xml:75-78 (defaultAccountCheckbox); INFERRED the CheckBox toggle and the call to the listener are not in fw_src (CompoundButton.java not read)')

# ---- AccountEditActivity$9: default-account text

e('S_ACCOUNT_EDIT', 'AccountEditActivity$9.onClick', 'GUI',
  'the default-account label text is tapped: mIsDefault is inverted and displayDefaultAccount runs',
  gui=['Tap the default-account label text next to the checkbox'],
  evidence='SRC account/AccountEditActivity.java:521-528 (listener 521; onClick 523-527); res/layout/activity_account_edit.xml:81-84 (defaultAccountText)')
