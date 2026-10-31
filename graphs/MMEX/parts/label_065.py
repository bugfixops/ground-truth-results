# batch 065: Currency (24 methods). All routes are auto CALL records or edges of other batches (D1, D7), so no e() here.
# Only Currency.getCentName is UNREACHABLE (no caller in the source). Its auto CALL to EntityBase.getString is cut (D14a).

UNREACHABLE['Currency.getCentName'] = ('no_trigger_in_app',
    'no caller: the only references are the definition and the setter call CurrencyEditActivity.java:222; no getCentName call in src/main (label_065.grep.txt)',
    'Currency.java:59-61; CurrencyEditActivity.java:222', 'SOURCE')

sup(('Currency.getCentName', 'EntityBase.getString'))
# Cut deferred to this batch by label_046.py (its caller CurrencyRepository.query is UNREACHABLE there).
sup(('CurrencyRepository.query', 'Currency.fromCursor'))
