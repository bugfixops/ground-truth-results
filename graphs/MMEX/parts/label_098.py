# ---- batch 098: InsecureSHA1PRNGKeyDerivator (8 methods), SimpleCrypto (11), Recurrence (4). Rows: graphs/MMEX/parts/label_098.md; evidence: graphs/MMEX/parts/label_098.grep.txt.
# No e() edges are written. The four Recurrence methods are REACHABLE only through auto CALL records (auto_calls.json: RecurringTransaction.java:70, 259, 260, 272, 276; RecurringTransactionService.java:79, 191, 198, 418, 433; RecurringTransactionEditActivity.java:246, 257; Recurrence.java:42, 61). The UNREACHABLE methods have no REACHABLE caller, so they need no edge.
# sup pairs cut the auto records whose caller is UNREACHABLE (D14). Groups: (1) inside InsecureSHA1PRNGKeyDerivator, 7 pairs; (2) Encryptor.deriveKeyInsecurely (batch 097) into this batch, 2 pairs, cross-batch; (3) inside SimpleCrypto, 9 pairs; (4) Passcode.decrypt and Passcode.encrypt (batch 038, REACHABLE, but their calls sit under if (Build.VERSION.SDK_INT <= 23), which is false on API 27) into SimpleCrypto.decrypt and SimpleCrypto.encrypt, 2 pairs, cross-batch.
# Total: 20 sup pairs. The same callers are not checked for receiver variants: auto_calls.json has no receiver_variants entry naming these classes.

# ---- sup pairs (1): InsecureSHA1PRNGKeyDerivator internal records; every caller is UNREACHABLE
sup(('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.<init>'),  # line 35
    ('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.setSeed'),  # line 36
    ('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.nextBytes'),  # line 38
    ('InsecureSHA1PRNGKeyDerivator.setSeed', 'InsecureSHA1PRNGKeyDerivator.updateSeed'),  # line 206
    ('InsecureSHA1PRNGKeyDerivator.updateSeed', 'InsecureSHA1PRNGKeyDerivator.updateHash'),  # line 181
    ('InsecureSHA1PRNGKeyDerivator.nextBytes', 'InsecureSHA1PRNGKeyDerivator.computeHash'),  # line 309
    ('InsecureSHA1PRNGKeyDerivator.updateHash', 'InsecureSHA1PRNGKeyDerivator.computeHash'))  # line 478

# ---- sup pairs (2): cross-batch, the caller Encryptor.deriveKeyInsecurely is batch 097's and is UNREACHABLE (no caller; Encryptor.java:130 is commented out)
sup(('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.<clinit>'),  # Encryptor.java:65
    ('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'))  # Encryptor.java:65

# ---- sup pairs (3): SimpleCrypto internal records; the callers are the closed String methods or the no-caller methods
sup(('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.getRawKey'),  # line 36
    ('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.encrypt(byte[],byte[])'),  # line 38
    ('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.toHex(byte[])'),  # line 39
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.getRawKey'),  # line 43
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.toByte'),  # line 44
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.decrypt(byte[],byte[])'),  # line 45
    ('SimpleCrypto.toHex(String)', 'SimpleCrypto.toHex(byte[])'),  # line 82
    ('SimpleCrypto.fromHex', 'SimpleCrypto.toByte'),  # line 85
    ('SimpleCrypto.toHex(byte[])', 'SimpleCrypto.appendHex'))  # line 101

# ---- sup pairs (4): cross-batch, the callers are batch 038's (Passcode.java). Their calls sit under if (Build.VERSION.SDK_INT <= 23), false on API 27 (see the UNREACHABLE reasons below).
sup(('Passcode.decrypt', 'SimpleCrypto.decrypt(String,String)'),  # Passcode.java:105
    ('Passcode.encrypt', 'SimpleCrypto.encrypt(String,String)'))  # Passcode.java:124

# ---- UNREACHABLE: InsecureSHA1PRNGKeyDerivator (8). Detail and grep evidence: label_098.md rows, label_098.grep.txt sections A, B, E2, E3.

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.<clinit>'] = (
  'no_trigger_in_app',
  'static initializer of the constant tables. The only active use of the class is Encryptor.deriveKeyInsecurely (Encryptor.java:65), which has no caller (its only other mention, line 130, is commented out). No class file other than Encryptor.class refers to this class.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:25, 48-138; SRC passcode/Encryptor.java:56-67, 130; grep label_098.grep.txt sections A, E2, E3',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.<init>'] = (
  'no_trigger_in_app',
  'private default constructor. Its only caller is deriveInsecureKey (line 35), which has no reachable caller.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:35, 156; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.computeHash'] = (
  'no_trigger_in_app',
  'private static SHA-1 helper. Its callers are nextBytes (line 309) and updateHash (line 478), both reached only from deriveInsecureKey.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:309, 353, 478; grep label_098.grep.txt sections A, E2',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'] = (
  'no_trigger_in_app',
  'public static entry point. Its only caller is Encryptor.deriveKeyInsecurely (Encryptor.java:65, batch 097), which has no caller. No class file calls it.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:34-40; SRC passcode/Encryptor.java:56-67, 130; grep label_098.grep.txt sections A, E2, E3',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.nextBytes'] = (
  'no_trigger_in_app',
  'protected synchronized method. Its only caller is deriveInsecureKey (line 38).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:38, 225, 309; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.setSeed'] = (
  'no_trigger_in_app',
  'private method. Its only caller is deriveInsecureKey (line 36).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:36, 196, 206; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.updateHash'] = (
  'no_trigger_in_app',
  'private static method. Its only caller is updateSeed (line 181), which is reached only from setSeed (line 206).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:181, 436, 478; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.updateSeed'] = (
  'no_trigger_in_app',
  'private method. Its only caller is setSeed (line 206).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:177-183, 206; grep label_098.grep.txt section A',
  'SOURCE')

# ---- UNREACHABLE: SimpleCrypto (11). The API-level claims rest on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so they are INFERRED.

UNREACHABLE['SimpleCrypto.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor (the class declares none). No source or class file creates an instance; every use is a static call.',
  'SRC passcode/SimpleCrypto.java:33; SRC core/Passcode.java:105, 124; grep label_098.grep.txt sections A, E1',
  'SOURCE')

UNREACHABLE['SimpleCrypto.appendHex'] = (
  'closed_by_api_level',
  'private static helper. Its only caller is toHex(byte[]) (line 101), which is reached from encrypt(String,String) (line 39, closed) and from toHex(String) (line 82, no caller).',
  'SRC passcode/SimpleCrypto.java:96-108; SRC core/Passcode.java:120-133; grep label_098.grep.txt sections B, C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.decrypt(String,String)'] = (
  'closed_by_api_level',
  'public static method. Its only caller is Passcode.decrypt (Passcode.java:105), under if (Build.VERSION.SDK_INT <= 23) (line 104). That is false on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so the call never runs.',
  'SRC passcode/SimpleCrypto.java:42-47; SRC core/Passcode.java:101-113 (guard 104, call 105); handoff/SCHEMA_V2.md:38, 41; grep label_098.grep.txt section C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.decrypt(byte[],byte[])'] = (
  'closed_by_api_level',
  'private static method. Its only caller is decrypt(String,String) (line 45), which is closed.',
  'SRC passcode/SimpleCrypto.java:45, 73-79',
  'INFERRED')

UNREACHABLE['SimpleCrypto.encrypt(String,String)'] = (
  'closed_by_api_level',
  'public static method. Its only caller is Passcode.encrypt (Passcode.java:124), under if (Build.VERSION.SDK_INT <= 23) (line 123). That is false on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so the call never runs.',
  'SRC passcode/SimpleCrypto.java:35-40; SRC core/Passcode.java:120-133 (guard 123, call 124); handoff/SCHEMA_V2.md:38, 41; grep label_098.grep.txt section C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.encrypt(byte[],byte[])'] = (
  'closed_by_api_level',
  'private static method. Its only caller is encrypt(String,String) (line 38), which is closed.',
  'SRC passcode/SimpleCrypto.java:38, 65-71',
  'INFERRED')

UNREACHABLE['SimpleCrypto.fromHex'] = (
  'no_trigger_in_app',
  'public static method. No caller in the source root; the text fromHex occurs only at its declaration. The class file mentions fromHex only inside SimpleCrypto.class.',
  'SRC passcode/SimpleCrypto.java:84-86; grep label_098.grep.txt sections B, E4, E5',
  'SOURCE')

UNREACHABLE['SimpleCrypto.getRawKey'] = (
  'closed_by_api_level',
  'private static method. Its callers are encrypt(String,String) (line 36) and decrypt(String,String) (line 43), both closed.',
  'SRC passcode/SimpleCrypto.java:36, 43, 49-63',
  'INFERRED')

UNREACHABLE['SimpleCrypto.toByte'] = (
  'closed_by_api_level',
  'public static method. Its callers are decrypt(String,String) (line 44, closed) and fromHex (line 85, no caller).',
  'SRC passcode/SimpleCrypto.java:44, 85, 88-94',
  'INFERRED')

UNREACHABLE['SimpleCrypto.toHex(String)'] = (
  'no_trigger_in_app',
  'public static method. Nothing calls it: the calls at line 39 pass a byte array to toHex(byte[]), and the text match at line 82 is inside toHex(String) itself, which has no caller.',
  'SRC passcode/SimpleCrypto.java:39, 81-83; grep label_098.grep.txt sections B, E4, E6',
  'SOURCE')

UNREACHABLE['SimpleCrypto.toHex(byte[])'] = (
  'closed_by_api_level',
  'public static method. Its callers are encrypt(String,String) (line 39, closed) and toHex(String) (line 82, no caller).',
  'SRC passcode/SimpleCrypto.java:39, 82, 96-103',
  'INFERRED')

# ---- REACHABLE: Recurrence (4) have no edge written here; their routes are auto CALL records (see the header). No UNREACHABLE entries.
