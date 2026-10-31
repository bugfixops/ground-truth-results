# ---- Helper batch_010 label part (2026-10-27)
# Batch 10: Coders (7z library), ColorAdapter (UI adapter)

# Coders static method entry points
e('SevenZFile.readStreamsInfo', 'Coders.addDecoder', 'CALL',
  'SevenZFile adds decoders for each coder in folder',
  evidence='SRC SevenZFile.java:435')

e('SevenZFile.getBytesForCoder', 'Coders.addDecoder', 'CALL',
  'Unpacks bytes using coders',
  evidence='SRC SevenZFile.java:1030')

e('Coders.addDecoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves decoder from CODER_MAP',
  evidence='SRC Coders.java:76')

e('SevenZOutputFile.createEncoders', 'Coders.addEncoder', 'CALL',
  'Encodes output stream with compression method',
  evidence='SRC SevenZOutputFile.java:321')

e('Coders.addEncoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves encoder from CODER_MAP',
  evidence='SRC Coders.java:87')

e('SevenZFile.getBytesForCoder', 'Coders.findByMethod', 'CALL',
  'Gets decoder options after adding decoder',
  evidence='SRC SevenZFile.java:1033')

e('SevenMethodConfiguration.setContentMethods', 'Coders.findByMethod', 'CALL',
  'SevenZMethodConfiguration validates encoder options',
  evidence='SRC SevenZMethodConfiguration.java:59')

# Coders static initializer - CODER_MAP creation
e('Coders.<clinit>', 'Coders$1.<init>', 'CALL',
  'Initializes CODER_MAP HashMap with decoders',
  evidence='SRC Coders.java:48-66')

e('Coders$1.<init>', 'Coders$CopyDecoder.<init>', 'CALL',
  'CODER_MAP puts CopyDecoder instance',
  evidence='SRC Coders.java:49')

e('Coders$1.<init>', 'Coders$BCJDecoder.<init>', 'CALL',
  'CODER_MAP puts BCJDecoder instances for various BCJ filters',
  evidence='SRC Coders.java:57-62')

e('Coders$1.<init>', 'Coders$DeflateDecoder.<init>', 'CALL',
  'CODER_MAP puts DeflateDecoder instance',
  evidence='SRC Coders.java:52')

e('Coders$1.<init>', 'Coders$Deflate64Decoder.<init>', 'CALL',
  'CODER_MAP puts Deflate64Decoder instance',
  evidence='SRC Coders.java:53')

e('Coders$1.<init>', 'Coders$BZIP2Decoder.<init>', 'CALL',
  'CODER_MAP puts BZIP2Decoder instance',
  evidence='SRC Coders.java:54')

# Decoder dispatch through virtual method calls
e('Coders.addDecoder', 'Coders$CopyDecoder.decode', 'CALL',
  'CopyDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BCJDecoder.decode', 'CALL',
  'BCJDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$DeflateDecoder.decode', 'CALL',
  'DeflateDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$Deflate64Decoder.decode', 'CALL',
  'Deflate64Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BZIP2Decoder.decode', 'CALL',
  'BZIP2Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addEncoder', 'Coders$CopyDecoder.encode', 'CALL',
  'CopyDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BCJDecoder.encode', 'CALL',
  'BCJDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$DeflateDecoder.encode', 'CALL',
  'DeflateDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BZIP2Decoder.encode', 'CALL',
  'BZIP2Decoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

# DeflateDecoder inner classes construction
e('Coders$DeflateDecoder.decode', 'Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 'CALL',
  'DeflateDecoder.decode constructs DeflateDecoderInputStream wrapper',
  evidence='SRC Coders.java:138-140')

e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL',
  'DeflateDecoder.encode constructs DeflateDecoderOutputStream wrapper',
  evidence='SRC Coders.java:145-147')

# DeflateDecoderInputStream methods
e('Coders$DeflateDecoder$DeflateDecoderInputStream.read', 'InflaterInputStream.read', 'CALL',
  'Delegates read to wrapped InflaterInputStream',
  evidence='SRC Coders.java:152-157')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.close', 'InflaterInputStream.close', 'CALL',
  'Closes underlying InflaterInputStream and ends Inflater',
  evidence='SRC Coders.java:159-165')

# DeflateDecoderOutputStream methods
e('Coders$DeflateDecoder$DeflateDecoderOutputStream.write', 'DeflaterOutputStream.write', 'CALL',
  'Delegates write to wrapped DeflaterOutputStream',
  evidence='SRC Coders.java:172-181')

e('Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'DeflaterOutputStream.close', 'CALL',
  'Closes underlying DeflaterOutputStream and ends Deflater',
  evidence='SRC Coders.java:183-189')

# ColorAdapter UI flow
e('ColorPref.showColorChooser', 'ColorAdapter.<init>', 'CALL',
  'Constructs ColorAdapter for color selection dialog',
  evidence='SRC ColorPref.java:135-137')

e('ColorAdapter.getView', 'ColorAdapter.getColorResAt', 'CALL',
  'getView retrieves color resource at position',
  evidence='SRC ColorAdapter.java:47')

e('GridView.onLayout', 'ColorAdapter.getView', 'CALL',
  'GridView renders items using adapter getView',
  evidence='SRC ColorAdapter.java:41-55')

e('GridView.onItemClick', 'ColorAdapter.onItemClick', 'CALL',
  'GridView item click dispatches to adapter listener',
  evidence='SRC ColorPref.java:170, ColorAdapter.java:57-64')

# UNREACHABLE entries for library decoder classes and internal classes
UNREACHABLE['Coders.<init>'] = ('no_trigger_in_app', 'Coders class has no public constructor; uses only static methods', 'SRC Coders.java:45', 'INFERRED')

UNREACHABLE['Coders$DeflateDecoder.<clinit>'] = ('no_trigger_in_app', 'Class initialization static block for ONE_ZERO_BYTE constant; not called directly from app', 'SRC Coders.java:126', 'INFERRED')
