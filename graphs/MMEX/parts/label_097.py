# ================================================================== batch 097 (label_097): SmsReceiverTransactions (18 methods), SmsReceiverTransactions_MembersInjector (4), SyncNotificationModel (1), Encryptor (10), FingerprintHandler (6): 39 methods, 25 REACHABLE, 14 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_097.md; grep output: graphs/MMEX/parts/label_097.grep.txt.
# Edges here: S_ENTRY to SmsReceiverTransactions.<clinit> and <init> (manifest SMS_RECEIVED receiver, exported=true), LIFECYCLE from <init> to onReceive (state gate: the bank SMS setting), and FRAMEWORK edges from FingerprintHandler.startAuth to its four callbacks (INFERRED, FingerprintManager source not in fw_src).
# Every other REACHABLE row rests on an auto_calls.json CALL record (D7: no edge written for those). The SyncNotificationModel.<init> and FingerprintHandler.<init>/startAuth rows rest on auto records as well.

ENV_SMS_BROADCAST = env_text(
    'outside package: the system delivers an SMS (SMS_RECEIVED) to the receiver, or another app sends an explicit broadcast to this exported receiver',
    ('system_event', 'other_app'))

STATE_BANK_SMS = state_text(
    'the bank SMS setting is on (Behaviour settings, default off): the body of onReceive runs only then',
    ('settings',))

ENV_FINGERPRINT_RESULT = env_text(
    'outside package: the user places a finger on the fingerprint sensor, and the framework reports the result (success, failure, help or error)',
    ('hardware',))

# ================================================================== batch 097: ENTRY and LIFECYCLE edges (SMS receiver)

e('S_ENTRY', 'SmsReceiverTransactions.<clinit>', 'ENTRY',
  'The framework loads the SMS receiver class by name before it creates the receiver; the class static fields are initialized then',
  env=ENV_SMS_BROADCAST,
  evidence='SRC AndroidManifest.xml:126-131; SRC notifications/SmsReceiverTransactions.java:87-94 (static fields); FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver loads and creates the receiver); JVM class initialization is not in fw_src: INFERRED, source not read')

e('S_ENTRY', 'SmsReceiverTransactions.<init>', 'ENTRY',
  'The framework creates the receiver by class name when a broadcast is delivered to it (the manifest receiver for SMS_RECEIVED, exported=true, no android:permission attribute)',
  env=ENV_SMS_BROADCAST,
  evidence='SRC AndroidManifest.xml:126-131; FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver creates the receiver with loadClass(component).newInstance())')

e('SmsReceiverTransactions.<init>', 'SmsReceiverTransactions.onReceive', 'LIFECYCLE',
  'The framework calls onReceive on the receiver it has just created; the body runs only when the bank SMS setting is on (line 117)',
  needs_state=STATE_BANK_SMS,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive); SRC notifications/SmsReceiverTransactions.java:97, 117; SRC settings/BehaviourSettings.java:67-68 (getBankSmsTrans, default false)')

# ================================================================== batch 097: FRAMEWORK edges (fingerprint callbacks)

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationSucceeded', 'FRAMEWORK',
  'FingerprintManager.authenticate (called at startAuth line 32) delivers the result to the callback object it was given (this handler); the framework calls onAuthenticationSucceeded when the sensor matches a finger',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 51-61; SRC PasscodeActivity.java:193-195; FingerprintManager is not in fw_src: the callback dispatch is INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationFailed', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers a failed match to the callback (this handler), which calls onAuthenticationFailed',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 41-43; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationHelp', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers a help message to the callback (this handler), which calls onAuthenticationHelp',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 46-48; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationError', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers an error to the callback (this handler), which calls onAuthenticationError',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 36-38; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

# ================================================================== UNREACHABLE (batch 097): Encryptor (SOURCE: no call site in app source)

UNREACHABLE['Encryptor.<init>'] = ('no_trigger_in_app',
    'implicit default constructor (Encryptor.java declares no constructor); no new Encryptor in the app source, and the build classes name Encryptor only in its own class file',
    'passcode/Encryptor.java:41; label_097.grep.txt sections 1, 5',
    'SOURCE')

UNREACHABLE['Encryptor.encrypt'] = ('no_trigger_in_app',
    'public method that returns "not implemented"; no call site in app source (the only reference is a todo comment at core/Passcode.java:126)',
    'passcode/Encryptor.java:45-47; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.deriveKeyInsecurely'] = ('no_trigger_in_app',
    'public static method; no live call site in app source (its only call sites in Encryptor.java, lines 130 and 137, are commented out in getKeyFor); no live auto caller',
    'passcode/Encryptor.java:56-66, 130; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.deriveKeySecurely'] = ('no_trigger_in_app',
    'private method; its only call sites (Encryptor.java:132, 137) are commented out in getKeyFor, and getKeyFor has no call site',
    'passcode/Encryptor.java:71-83, 132, 137; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.getKeyFor'] = ('no_trigger_in_app',
    'private method; no call site anywhere in app source (the definition at line 90 is the only occurrence of the name outside its commented-out callers)',
    'passcode/Encryptor.java:90-121; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.encryptOrDecrypt'] = ('no_trigger_in_app',
    'private static helper; its only callers are encryptData (line 157) and decryptData (line 160), and neither has a call site',
    'passcode/Encryptor.java:145-155, 157, 160; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.encryptData'] = ('no_trigger_in_app',
    'private static method; no call site (the name occurs only at its definition, line 156)',
    'passcode/Encryptor.java:156-158; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.decryptData'] = ('no_trigger_in_app',
    'private static method; no call site (the name occurs only at its definition, line 159)',
    'passcode/Encryptor.java:159-161; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.retrieveSalt'] = ('no_trigger_in_app',
    'private method; its only caller is deriveKeySecurely (line 73), which has no call site',
    'passcode/Encryptor.java:73, 163-169; label_097.grep.txt sections 1, 2, 3',
    'SOURCE')

UNREACHABLE['Encryptor.readFromFileOrCreateRandom'] = ('no_trigger_in_app',
    'private method; its only caller is retrieveSalt (line 167), which is itself unreachable',
    'passcode/Encryptor.java:167, 176-185; label_097.grep.txt sections 1, 2, 3',
    'SOURCE')

# ================================================================== UNREACHABLE (batch 097): SmsReceiverTransactions_MembersInjector (INFERRED: Dagger-generated, source not in the repo)

UNREACHABLE['SmsReceiverTransactions_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor (not in the source root; class file in build/intermediates). Its only caller record is create (auto record SmsReceiverTransactions_MembersInjector.java:22), and create has no caller. The app source does not name the class (label_097.grep.txt section 4)',
    'SmsReceiverTransactions_MembersInjector.java:22 (auto record); label_097.grep.txt sections 4, 5',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory; no caller record in auto_calls.json; no app-source reference to the class (section 4); no build class except its own names the class (section 5)',
    'label_097.grep.txt sections 4, 5 (auto query: 0 callers)',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.injectDatabase'] = ('no_trigger_in_app',
    'Dagger-generated member injector for the receiver field; its only caller record is injectMembers (SmsReceiverTransactions_MembersInjector.java:27), and injectMembers has no caller',
    'SmsReceiverTransactions_MembersInjector.java:27 (auto record); label_097.grep.txt sections 4, 5',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated instance method; no caller record in auto_calls.json (section 5); no app-source reference (section 4)',
    'label_097.grep.txt sections 4, 5 (auto query: 0 callers)',
    'INFERRED')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.<clinit>'),
    ('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'),
    ('Encryptor.deriveKeySecurely', 'Encryptor.retrieveSalt'),
    ('Encryptor.encryptData', 'Encryptor.encryptOrDecrypt'),
    ('Encryptor.decryptData', 'Encryptor.encryptOrDecrypt'),
    ('Encryptor.retrieveSalt', 'Encryptor.readFromFileOrCreateRandom'),
    ('SmsReceiverTransactions_MembersInjector.create', 'SmsReceiverTransactions_MembersInjector.<init>'),
    ('SmsReceiverTransactions_MembersInjector.injectMembers', 'SmsReceiverTransactions_MembersInjector.injectDatabase'))
