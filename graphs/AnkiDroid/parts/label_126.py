# AnkiDroid batch 126 (LABEL helper). EasySSLSocketFactory (9 methods) and EasyX509TrustManager (4 methods).
# The full row list is in graphs/AnkiDroid/parts/label_126.md.
#
# Route ownership:
# - Direct CALL edges inside this batch (EasySSLSocketFactory.<init>, createEasySSLContext, createSocket(),
#   getSSLContext, EasyX509TrustManager.<init>, and connectSocket into createSocket()) come from auto_calls.json.
#   They are not written here.
# - The library dispatch edges from HttpSyncer.req (to connectSocket, createSocket(Socket,String,int,boolean) and
#   isSecure) belong to batch 106 and are not written here (see the Leads in the .md).
# - This batch owns the one edge whose source is in this batch: createSocket(Socket,...) -> checkServerTrusted.
# Gate: ENV_NETWORK (the sync server is reachable).

e('EasySSLSocketFactory.createSocket(Socket,String,int,boolean)', 'EasyX509TrustManager.checkServerTrusted', 'FRAMEWORK',
  'the HTTP library layers TLS on the socket, and the TLS handshake checks the server certificate chain',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x and the platform TLS stack (library and platform source not read)'],
  evidence='SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:94-98; SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:46-53, 91; SRC com/ichi2/libanki/sync/HttpSyncer.java:226-228, 236; INFERRED (library and platform source not read)',
  note='createSocket(Socket,...) returns the layered socket at line 97; the handshake that calls checkServerTrusted runs on that socket after it is returned. checkServerTrusted always delegates to the platform trust manager at line 91 of EasyX509TrustManager. The dispatch from HttpSyncer.req to createSocket(Socket,...) is owned by batch 106 and is not written here.')

UNREACHABLE['EasySSLSocketFactory.equals'] = ('no_trigger_in_app',
  'No app code calls equals on this factory. The factory is built only at HttpSyncer.req line 228 and registered there with SchemeRegistry. A grep of the source root for SchemeRegistry and new Scheme( lists only HttpSyncer. The HTTP library could compare a scheme that holds this factory, but its source is not read, so no such route is seen. Least certain entry of this batch.',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:107-110; SRC com/ichi2/libanki/sync/HttpSyncer.java:33, 43, 226-228; INFERRED (Apache HttpClient 4.x source not read)',
  'INFERRED')

UNREACHABLE['EasySSLSocketFactory.hashCode'] = ('no_trigger_in_app',
  'No app code calls hashCode on this factory. Its only construction is at HttpSyncer.req line 228, and the only SchemeRegistry use is there. The HTTP library could hash a scheme that holds this factory, but its source is not read, so no such route is seen.',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:113-116; SRC com/ichi2/libanki/sync/HttpSyncer.java:33, 43, 226-228; INFERRED (Apache HttpClient 4.x source not read)',
  'INFERRED')

UNREACHABLE['EasyX509TrustManager.checkClientTrusted'] = ('framework_never_calls',
  'No app call site: a grep of the source root for checkClientTrusted, checkServerTrusted and getAcceptedIssuers finds no call outside EasyX509TrustManager (its only call is its own delegate at line 39). The factory only creates client-side sockets (lines 77 and 97 use SSLContext.getSocketFactory() with no server socket), and a TLS client calls checkServerTrusted, not checkClientTrusted (INFERRED; platform TLS source not read).',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:37-40; SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:77, 97; INFERRED (platform TLS source not read)',
  'INFERRED')

UNREACHABLE['EasyX509TrustManager.getAcceptedIssuers'] = ('framework_never_calls',
  'No app call site: a grep of the source root for getAcceptedIssuers finds no call outside EasyX509TrustManager (its only call is its own delegate at line 100). The TLS client does not ask its trust manager for accepted issuers (INFERRED; platform TLS source not read), and the factory only creates client-side sockets (lines 77 and 97).',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:98-101; SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:77, 97; INFERRED (platform TLS source not read)',
  'INFERRED')
