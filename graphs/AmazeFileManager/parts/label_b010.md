STATUS: RUNNING 21:28

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| Coders.<clinit> | REACHABLE | LIFECYCLE | Class initialization; creates CODER_MAP with all decoders | SRC Coders.java:45-66 |
| Coders.<init> | UNREACHABLE | no_trigger_in_app | Coders is never instantiated; all methods are static | SRC Coders.java:45 |
| Coders.addDecoder | REACHABLE | CALL | Called from SevenZFile.readStreamsInfo and getBytesForCoder to create decoders | SRC SevenZFile.java:435,1030 |
| Coders.addEncoder | REACHABLE | CALL | Called from SevenZOutputFile.createEncoders to wrap output stream | SRC SevenZOutputFile.java:321 |
| Coders.findByMethod | REACHABLE | CALL | Called by addDecoder, addEncoder, SevenZFile.getBytesForCoder, and SevenZMethodConfiguration to retrieve coders | SRC Coders.java:76,87; SevenZFile.java:1033; SevenZMethodConfiguration.java:59 |
| Coders$1.<init> | REACHABLE | LIFECYCLE | Initializes CODER_MAP HashMap with all compression method decoders | SRC Coders.java:48-66 |
| Coders$BCJDecoder.<init> | REACHABLE | LIFECYCLE | Constructed in CODER_MAP for all BCJ filter variants | SRC Coders.java:57-62 |
| Coders$BCJDecoder.decode | REACHABLE | CALL | Virtual method called via CoderBase.decode from Coders.addDecoder | SRC Coders.java:78-80,107-117 |
| Coders$BCJDecoder.encode | REACHABLE | CALL | Virtual method called via CoderBase.encode from Coders.addEncoder | SRC Coders.java:87-89,119-121 |
| Coders$BZIP2Decoder.<init> | REACHABLE | LIFECYCLE | Constructed in CODER_MAP for BZIP2 compression | SRC Coders.java:54 |
| Coders$BZIP2Decoder.decode | REACHABLE | CALL | Virtual method called via CoderBase.decode from Coders.addDecoder | SRC Coders.java:78-80,230-236 |
| Coders$BZIP2Decoder.encode | REACHABLE | CALL | Virtual method called via CoderBase.encode from Coders.addEncoder | SRC Coders.java:87-89,237-241 |
| Coders$CopyDecoder.<init> | REACHABLE | LIFECYCLE | Constructed in CODER_MAP for COPY (passthrough) compression | SRC Coders.java:49 |
| Coders$CopyDecoder.decode | REACHABLE | CALL | Virtual method called via CoderBase.decode from Coders.addDecoder | SRC Coders.java:78-80,95-98 |
| Coders$CopyDecoder.encode | REACHABLE | CALL | Virtual method called via CoderBase.encode from Coders.addEncoder | SRC Coders.java:87-89,99-101 |
| Coders$Deflate64Decoder.<init> | REACHABLE | LIFECYCLE | Constructed in CODER_MAP for DEFLATE64 compression | SRC Coders.java:53 |
| Coders$Deflate64Decoder.decode | REACHABLE | CALL | Virtual method called via CoderBase.decode from Coders.addDecoder | SRC Coders.java:78-80,219-225 |
| Coders$DeflateDecoder.<clinit> | UNREACHABLE | no_trigger_in_app | Class initialization for ONE_ZERO_BYTE constant; not directly triggered from app code | SRC Coders.java:126 |
| Coders$DeflateDecoder.<init> | REACHABLE | LIFECYCLE | Constructed in CODER_MAP for DEFLATE compression | SRC Coders.java:52 |
| Coders$DeflateDecoder.decode | REACHABLE | CALL | Virtual method called via CoderBase.decode from Coders.addDecoder | SRC Coders.java:78-80,129-141 |
| Coders$DeflateDecoder.encode | REACHABLE | CALL | Virtual method called via CoderBase.encode from Coders.addEncoder | SRC Coders.java:87-89,142-147 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.<init> | REACHABLE | LIFECYCLE | Constructed in DeflateDecoder.decode to wrap InflaterInputStream | SRC Coders.java:160-163 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read | REACHABLE | CALL | Overloaded read() method delegates to wrapped InflaterInputStream | SRC Coders.java:170-172 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read | REACHABLE | CALL | Overloaded read(byte[], int, int) method delegates to wrapped InflaterInputStream | SRC Coders.java:175-177 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read | REACHABLE | CALL | Overloaded read(byte[]) method delegates to wrapped InflaterInputStream | SRC Coders.java:180-182 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.close | REACHABLE | CALL | Closes InflaterInputStream and releases Inflater resources | SRC Coders.java:184-190 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.<init> | REACHABLE | LIFECYCLE | Constructed in DeflateDecoder.encode to wrap DeflaterOutputStream | SRC Coders.java:199-202 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write | REACHABLE | CALL | Overloaded write(int) method delegates to wrapped DeflaterOutputStream | SRC Coders.java:206-208 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write | REACHABLE | CALL | Overloaded write(byte[]) method delegates to wrapped DeflaterOutputStream | SRC Coders.java:211-213 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write | REACHABLE | CALL | Overloaded write(byte[], int, int) method delegates to wrapped DeflaterOutputStream | SRC Coders.java:216-218 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.close | REACHABLE | CALL | Closes DeflaterOutputStream and releases Deflater resources | SRC Coders.java:220-226 |
| ColorAdapter.<init> | REACHABLE | LIFECYCLE | Constructed in ColorPref.showColorChooser for color selection dialog | SRC ColorPref.java:135-137 |
| ColorAdapter.getColorResAt | REACHABLE | CALL | Called from getView to retrieve color resource ID at position | SRC ColorAdapter.java:47 |
| ColorAdapter.getView | REACHABLE | CALL | Virtual method called by GridView.onLayout to render list items | SRC ColorAdapter.java:41-55 |
| ColorAdapter.onItemClick | REACHABLE | CALL | Set as GridView.OnItemClickListener; called on item selection | SRC ColorPref.java:170; ColorAdapter.java:57-64 |

STATUS: DONE 21:28
