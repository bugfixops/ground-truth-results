# ---- addendum to part 106 (2026-10-29): dispatch edges from HttpSyncer.req to EasySSLSocketFactory.
# The source method is in part 106 (HttpSyncer.java:226-236), so these edges belong to part 106.
# Batch 126 has REACHABLE rows for the three targets and needs these routes.

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.connectSocket', 'FRAMEWORK',
  'the HTTP client opens the https connection through the socket factory that req registered for the https scheme',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute, DefaultClientConnectionOperator (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The factory is registered at HttpSyncer.java:228 and the request is executed at :236. The library dispatch to connectSocket is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.createSocket(Socket,String,int,boolean)', 'FRAMEWORK',
  'the HTTP client layers TLS on the opened socket through the https socket factory',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute, LayeredSocketFactory (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The https scheme is registered at HttpSyncer.java:228. The library dispatch to the layered-socket method is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.isSecure', 'FRAMEWORK',
  'the HTTP client asks the https socket factory whether the opened connection is secure',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The https scheme is registered at HttpSyncer.java:228. The library dispatch to isSecure is INFERRED (library source not read).')
