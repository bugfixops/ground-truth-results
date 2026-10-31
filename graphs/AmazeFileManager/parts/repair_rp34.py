# repair_rp34.py - Batch 34 repairs

def edge(src, dst, kind, summary='', evidence=''):
    """Schema-2 edge format"""
    return {'src': src, 'dst': dst, 'kind': kind, 'summary': summary, 'evidence': evidence}

EDGES = []

# ==== Methods with existing routes (23 methods) ====
# These already have complete routes in graph_def.py:
# - SmbConnectDialog$3.afterTextChanged
# - SmbConnectDialog$4.afterTextChanged  
# - SmbSearchDialog$1.computerFound, lambda$computerFound$0, lambda$searchFinished$1, searchFinished
# - SshAuthenticationTask.doInBackground
# - SshClientUtils.deriveSftpPathFrom
# - SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)
# - SshConnectionPool.removeConnection
# - SshConnectionPool$AsyncRemoveConnection.<init>, doInBackground, onPostExecute
# - Statvfs$Response.getRawFileSystemId
# - StreamServer.lambda$new$0
# - SubnetScanner.run, tryWithBroadcast
# - TabFragment.onPageSelected
# - TabFragment$ScreenSlidePagerAdapter.getCount, getItem, getItemPosition
# - ThemedImageButton.getAccessibilityClassName, onSetAlpha

# ==== SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair) - 7-param constructor ====
# SRC SshAuthenticationTask.java:95-105
# This is the 7-parameter constructor that includes existingHostKey parameter
# Constructor delegates to field assignments
EDGES.append(edge(
    'SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair)',
    'Object.<init>',
    'CALL',
    'Constructor delegation to Object superclass',
    'SRC SshAuthenticationTask.java:95-105: public SshAuthenticationTask(...) { this.hostname = hostname; this.port = port; ... }'
))

# ==== SshAuthenticationTask.lambda$onPostExecute$0 ====
# SRC SshAuthenticationTask.java:180
# Lambda for dialog dismiss callback
EDGES.append(edge(
    'SshAuthenticationTask.onPostExecute',
    'SshAuthenticationTask.lambda$onPostExecute$0',
    'CALL',
    'onPostExecute creates lambda for AlertDialog positive button callback',
    'SRC SshAuthenticationTask.java:180: .setPositiveButton(R.string.ok, (dialog, which) -> dialog.dismiss()).show();'
))

EDGES.append(edge(
    'SshAuthenticationTask.lambda$onPostExecute$0',
    'DialogInterface.dismiss',
    'CALL',
    'Lambda dismisses the alert dialog',
    'SRC SshAuthenticationTask.java:180: (dialog, which) -> dialog.dismiss()'
))

# ==== SshAuthenticationTask.onPostExecute ====
# SRC SshAuthenticationTask.java:161-184
# Called by AsyncTask framework after doInBackground completes
EDGES.append(edge(
    'S_ASYNCTASK_result',
    'SshAuthenticationTask.onPostExecute',
    'FRAMEWORK',
    'AsyncTask framework calls onPostExecute after doInBackground completes',
    'SRC SshAuthenticationTask.java:161: protected void onPostExecute(AsyncTaskResult<SSHClient> result); AsyncTask lifecycle calls this on UI thread'
))

EDGES.append(edge(
    'SshAuthenticationTask.onPostExecute',
    'Toast.makeText',
    'CALL',
    'onPostExecute shows toast messages for various error conditions',
    'SRC SshAuthenticationTask.java:165,171,173: Toast.makeText(...) calls for socket errors, auth failures'
))

EDGES.append(edge(
    'SshAuthenticationTask.onPostExecute',
    'AlertDialog.Builder.<init>',
    'CALL',
    'onPostExecute creates AlertDialog for host key change warning',
    'SRC SshAuthenticationTask.java:176: new AlertDialog.Builder(AppConfig.getInstance().getMainActivityContext())'
))

# ==== SshAuthenticationTask$1 - anonymous KeyProvider implementation ====
# SRC SshAuthenticationTask.java:130-144
# Anonymous inner class implementing KeyProvider interface for key-based auth

# SshAuthenticationTask$1.<init>
EDGES.append(edge(
    'SshAuthenticationTask.doInBackground',
    'SshAuthenticationTask$1.<init>',
    'CALL',
    'doInBackground creates anonymous KeyProvider for key-based authentication',
    'SRC SshAuthenticationTask.java:130: sshClient.authPublickey(username, new KeyProvider() {...});'
))

# SshAuthenticationTask$1.getPrivate
EDGES.append(edge(
    'SSHClient.authPublickey',
    'SshAuthenticationTask$1.getPrivate',
    'FRAMEWORK',
    'SSHJ library calls getPrivate to obtain private key for authentication',
    'SRC SshAuthenticationTask.java:132-134: @Override public PrivateKey getPrivate() { return privateKey.getPrivate(); }'
))

EDGES.append(edge(
    'SshAuthenticationTask$1.getPrivate',
    'KeyPair.getPrivate',
    'CALL',
    'Returns private key from the KeyPair field',
    'SRC SshAuthenticationTask.java:133: return privateKey.getPrivate();'
))

# SshAuthenticationTask$1.getPublic
EDGES.append(edge(
    'SSHClient.authPublickey',
    'SshAuthenticationTask$1.getPublic',
    'FRAMEWORK',
    'SSHJ library calls getPublic to obtain public key for authentication',
    'SRC SshAuthenticationTask.java:136-138: @Override public PublicKey getPublic() { return privateKey.getPublic(); }'
))

EDGES.append(edge(
    'SshAuthenticationTask$1.getPublic',
    'KeyPair.getPublic',
    'CALL',
    'Returns public key from the KeyPair field',
    'SRC SshAuthenticationTask.java:137: return privateKey.getPublic();'
))

# SshAuthenticationTask$1.getType
EDGES.append(edge(
    'SSHClient.authPublickey',
    'SshAuthenticationTask$1.getType',
    'FRAMEWORK',
    'SSHJ library calls getType to determine key type (RSA/DSA/ECDSA)',
    'SRC SshAuthenticationTask.java:140-142: @Override public KeyType getType() { return KeyType.fromKey(getPublic()); }'
))

EDGES.append(edge(
    'SshAuthenticationTask$1.getType',
    'KeyType.fromKey',
    'CALL',
    'Determines KeyType from public key',
    'SRC SshAuthenticationTask.java:141: return KeyType.fromKey(getPublic());'
))

EDGES.append(edge(
    'SshAuthenticationTask$1.getType',
    'SshAuthenticationTask$1.getPublic',
    'CALL',
    'Calls getPublic to obtain public key for type determination',
    'SRC SshAuthenticationTask.java:141: return KeyType.fromKey(getPublic());'
))

# ==== SshConnectionPool.lambda$create$1 ====
# SRC SshConnectionPool.java:214-217
# Lambda callback for PemToKeyPairTask completion
EDGES.append(edge(
    'SshConnectionPool.create(String)',
    'SshConnectionPool.lambda$create$1',
    'CALL',
    'create method passes lambda callback to PemToKeyPairTask for key conversion result',
    'SRC SshConnectionPool.java:214: new PemToKeyPairTask(pem, result -> { keyPair.set(result); latch.countDown(); }).execute();'
))

EDGES.append(edge(
    'SshConnectionPool.lambda$create$1',
    'AtomicReference.set',
    'CALL',
    'Lambda stores converted KeyPair in AtomicReference',
    'SRC SshConnectionPool.java:215: keyPair.set(result);'
))

EDGES.append(edge(
    'SshConnectionPool.lambda$create$1',
    'CountDownLatch.countDown',
    'CALL',
    'Lambda signals completion via CountDownLatch',
    'SRC SshConnectionPool.java:216: latch.countDown();'
))

# ==== SshConnectionPool.lambda$expungeAllConnections$0 ====
# SRC SshConnectionPool.java:181-187
# Lambda for background thread to close all connections
EDGES.append(edge(
    'SshConnectionPool.expungeAllConnections',
    'SshConnectionPool.lambda$expungeAllConnections$0',
    'CALL',
    'expungeAllConnections runs lambda in background thread to close connections',
    'SRC SshConnectionPool.java:181: AppConfig.runInBackground(() -> { ... });'
))

EDGES.append(edge(
    'SshConnectionPool.lambda$expungeAllConnections$0',
    'SshClientUtils.tryDisconnect',
    'CALL',
    'Lambda disconnects each SSHClient in the connection pool',
    'SRC SshConnectionPool.java:183-184: for (SSHClient connection : connections.values()) { SshClientUtils.tryDisconnect(connection); }'
))

EDGES.append(edge(
    'SshConnectionPool.lambda$expungeAllConnections$0',
    'Map.clear',
    'CALL',
    'Lambda clears the connections map',
    'SRC SshConnectionPool.java:185: connections.clear();'
))

# ==== StreamSource methods ====
# StreamSource is used for streaming SMB files via HTTP server

# StreamSource.getFile
# SRC StreamSource.java:115-117
UNREACHABLE['StreamSource.getFile'] = (
    'no_trigger_in_app',
    'StreamSource.getFile is a getter method that returns the SmbFile field. However, StreamSource is only used internally by StreamServer (see StreamServer.java:52-89 where StreamSource is created and used). The getFile method is never called from app code. Grep shows no callers.',
    'SRC StreamSource.java:115-117: public SmbFile getFile(){ return file; }',
    'INFERRED'
)

# StreamSource.getName
# SRC StreamSource.java:111-113
UNREACHABLE['StreamSource.getName'] = (
    'no_trigger_in_app',
    'StreamSource.getName is a getter that returns the file name. StreamSource is only instantiated in StreamServer.lambda$new$0 (line 53), and getName is never called from app code. The HTTP streaming uses read() methods, not getName.',
    'SRC StreamSource.java:111-113: public String getName(){ return name; }',
    'INFERRED'
)

# StreamSource.read()
# SRC StreamSource.java:76-80
EDGES.append(edge(
    'RandomAccessStream.readOneByte',
    'StreamSource.read',
    'FRAMEWORK',
    'Parent class RandomAccessStream calls read() for single-byte reads',
    'SRC StreamSource.java:76-80: @Override public int read() throws IOException { int read = input.read(); if(read != -1) fp++; return read; }'
))

EDGES.append(edge(
    'StreamSource.read',
    'InputStream.read',
    'CALL',
    'read() delegates to underlying InputStream',
    'SRC StreamSource.java:77: int read = input.read();'
))

# StreamSource.read(byte[],int,int)
# SRC StreamSource.java:82-86
EDGES.append(edge(
    'RandomAccessStream.readBytes',
    'StreamSource.read(byte[],int,int)',
    'FRAMEWORK',
    'Parent class RandomAccessStream calls read(byte[],int,int) for multi-byte reads',
    'SRC StreamSource.java:82-86: public int read(byte[] bytes, int start, int offs) throws IOException { int read = input.read(bytes, start, offs); fp += read; return read; }'
))

EDGES.append(edge(
    'StreamSource.read(byte[],int,int)',
    'InputStream.read',
    'CALL',
    'read(byte[],int,int) delegates to InputStream.read with buffer',
    'SRC StreamSource.java:83: int read = input.read(bytes, start, offs);'
))

# ==== SubnetScanner methods ====

# SubnetScanner.getResults
# SRC SubnetScanner.java:187-189
UNREACHABLE['SubnetScanner.getResults'] = (
    'no_trigger_in_app',
    'SubnetScanner.getResults returns the list of discovered computers. However, this method is never called from app code. The SmbSearchDialog creates a SubnetScanner and uses its ScanObserver callbacks (computerFound, searchFinished) to receive results, not getResults. Grep shows no callers of getResults.',
    'SRC SubnetScanner.java:187-189: public List<ComputerParcelable> getResults() { return new ArrayList<>(this.mResults); }',
    'INFERRED'
)

# SubnetScanner.onFound
# SRC SubnetScanner.java:175-181
# This is a private method called internally by SubnetScanner.run
EDGES.append(edge(
    'SubnetScanner.run',
    'SubnetScanner.onFound',
    'CALL',
    'run calls onFound when a computer is discovered to notify observer',
    'SRC SubnetScanner.java:125,168: onFound(computer) called from run method when computer is found'
))

EDGES.append(edge(
    'SubnetScanner.onFound',
    'ScanObserver.computerFound',
    'CALL',
    'onFound notifies the registered observer callback',
    'SRC SubnetScanner.java:178-179: if (this.observer != null) { this.observer.computerFound(computer); }'
))

# ==== ThemedImageButton constructors ====
# ThemedImageButton extends ThemedImageView

# ThemedImageButton.<init>(Context)
# SRC ThemedImageButton.java:16-18
EDGES.append(edge(
    'S_VIEW_inflate',
    'ThemedImageButton.<init>(Context)',
    'FRAMEWORK',
    'Android framework can inflate ThemedImageButton from XML layouts',
    'SRC ThemedImageButton.java:16-18: public ThemedImageButton(Context context) { super(context); }'
))

EDGES.append(edge(
    'ThemedImageButton.<init>(Context)',
    'ThemedImageView.<init>(Context)',
    'CALL',
    'Constructor delegates to parent ThemedImageView',
    'SRC ThemedImageButton.java:17: super(context);'
))

# ThemedImageButton.<init>(Context,AttributeSet)
# SRC ThemedImageButton.java:20-22
EDGES.append(edge(
    'S_VIEW_inflate',
    'ThemedImageButton.<init>(Context,AttributeSet)',
    'FRAMEWORK',
    'Android framework inflates ThemedImageButton from XML with attributes',
    'SRC ThemedImageButton.java:20-22: public ThemedImageButton(Context context, AttributeSet attrs) { super(context, attrs); }'
))

EDGES.append(edge(
    'ThemedImageButton.<init>(Context,AttributeSet)',
    'ThemedImageView.<init>(Context,AttributeSet)',
    'CALL',
    'Constructor delegates to parent ThemedImageView with attributes',
    'SRC ThemedImageButton.java:21: super(context, attrs);'
))

