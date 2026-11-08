TITLE = 'exp'
USE_AUTO = True
SCREENS = {'S_ENTRY': 'outside the app'}
e('S_ENTRY', 'IntentHandler.onCreate', 'ENTRY', 'launcher', evidence='SRC AndroidManifest.xml:81-89')
e('S_ENTRY', 'AnkiDroidApp.onCreate', 'ENTRY', 'process start', evidence='SRC AndroidManifest.xml:74')
e('S_ENTRY', 'CardContentProvider.onCreate', 'ENTRY', 'provider', evidence='SRC AndroidManifest.xml:324-330')
