# Converted from repair_rp32.py
# Original: 4 edges, Duplicates removed: 0, New: 4

e('SevenZFile.buildDecoderStack', 'SevenZFile$1.<init>', 'CALL',
  'buildDecoderStack creates anonymous FilterInputStream at line 997 to track compressed bytes read',
  evidence='SRC SevenZFile.java:997-1022: InputStream inputStreamStack = new FilterInputStream(new BufferedInputStream(new BoundedFileChannelInputStream(channel, archive.packSizes[firstPackStreamIndex]))) { ... }')

e('SevenZFile$1.read()', 'SevenZFile$1.count', 'CALL',
  'After reading from parent FilterInputStream, calls count() to track compressed bytes',
  evidence='SRC SevenZFile.java:1001-1007: public int read() throws IOException { final int r = in.read(); if (r >= 0) { count(1); } return r; } - in.read() is FilterInputStream.read()')

e('SevenZFile$1.read(byte[])', 'SevenZFile$1.read(byte[],int,int)', 'CALL',
  'read(byte[]) delegates to read(byte[],int,int) with full array bounds',
  evidence='SRC SevenZFile.java:1009-1011: public int read(final byte[] b) throws IOException { return read(b, 0, b.length); }')

e('SevenZFile$1.read(byte[],int,int)', 'SevenZFile$1.count', 'CALL',
  'After reading from parent FilterInputStream, calls count() with number of bytes read',
  evidence='SRC SevenZFile.java:1013-1019: public int read(final byte[] b, final int off, final int len) throws IOException { final int r = in.read(b, off, len); if (r >= 0) { count(r); } return r; } - in.read() is FilterInputStream.read(byte[],int,int)')

