import datetime

W = '/Users/darshan/Desktop/yang/work'
N = W + '/graphs/AnkiDroid/AGENT_NOTES.md'
H = W + '/handoff/HANDOFF_V2.md'
now = datetime.datetime.now().strftime('%H:%M')

rows = [
    '| 174 | 9129 | 2302 | 885 | 999 | 0 (addendum to part 106: three FRAMEWORK edges from HttpSyncer.req to EasySSLSocketFactory.connectSocket, createSocket(Socket,...) and isSecure; no sup) |',
    '| 175 | 9121 | 2302 | 895 | 989 | 0 after sup175 (part 125, 40 rows; premerge had 2 warnings, GraphicsWrap.drawRect and GraphicsWrap.drawImage; 8 pairs: five drawBar closed branches, LinesPoints.drawPoint, Lines.drawPoint, ReliefDrawer.drawColoredRelief) |',
    '| 176 | 9122 | 2303 | 899 | 984 | 0 (part 126, 14 rows: EasySSLSocketFactory and EasyX509TrustManager; equals and hashCode stay INFERRED, see conflicts.md) |',
    '| 177 | 9122 | 2303 | 901 | 982 | 0 after sup177 (part 127, 38 rows: 34 REACHABLE, 2 UNREACHABLE, 2 EDGE; premerge had 2 warnings; 2 pairs: AnkiDroidApp.onCreate to ProductionCrashReportingTree.<init> and <clinit>, closed by the BuildConfig.DEBUG branch) |',
    '| 178 | 9125 | 2307 | 901 | 978 | 0 (part 128, 42 rows, 3 ASYNC edges; no sup) |',
    '| 179 | 9116 | 2606 | 908 | 672 | 0 after sup179 (part 129, 39 rows; premerge had 7 warnings; 11 pairs: CompatV10, CompatV11 and Nook bodies shadowed on API 27 by CompatV21 inheritance, plus CompatHelper.<init> to the Nook constructor) |',
]

lines = open(N, encoding='utf-8').read().split('\n')
idx173 = next(i for i, l in enumerate(lines) if l.startswith('| 173 |'))
lines[idx173 + 1:idx173 + 1] = rows

cs = lines.index('## Current step')
s2 = lines.index('## Status at 02:53 (superseded)')
body = [
    'Status as of 2026-10-29 %s EDT. Parts 121-129 are merged as builds 170-179, each after C1 (problems 0) and a citation spot-check; premerge warnings were cleared by sup blocks justified in the build log. Build 179: edges 9116, REACHABLE 2606, UNREACHABLE 908, UNRESOLVED 672, errors 694, warnings 0.' % now,
    'Helpers for batches 130-133 are running; they merge as builds 180-183 in plan order. Then batches 134-139, four helpers at a time, the 30-minute stuck rule.',
    'Open: EasySSLSocketFactory.equals and hashCode (INFERRED, OPEN in scratch/conflicts.md); Card.toString contradiction (OPEN); Hooks.runFilter to AdvancedStatistics.runFilter is a suspect automatic pair, not suppressed, to revisit with batches 135-137.',
    '',
]
lines = lines[:cs + 1] + body + lines[s2:]
open(N, 'w', encoding='utf-8').write('\n'.join(lines))

decisions = '''
- 2026-10-29, AnkiDroid overnight run, after batch 124.
- Part 106 addendum (build 174): HttpSyncer.req (5-argument overload, HttpSyncer.java:226-236) gets three FRAMEWORK edges to EasySSLSocketFactory.connectSocket, createSocket(Socket,String,int,boolean) and isSecure. The edges sit in an addendum to part 106 because the source method is in part 106. Batch 126 had REACHABLE rows for those targets, and no route existed. Library dispatch is INFERRED (Apache HttpClient source not read).
- Batch 126 (build 176): EasySSLSocketFactory.equals and hashCode stay UNREACHABLE no_trigger_in_app, INFERRED. The app constructs the factory only at HttpSyncer.java:228. The unchecked assumption is that Apache HttpClient Scheme.equals and hashCode do not run during a request. Logged OPEN in scratch/conflicts.md for the reviewer.
- Batch 125 (build 175): eight sup pairs. Five drawBar methods (BarGraph, XAxisBarGraph, YAxisBarGraph, XAxisHistoGram, YAxisHistoGram) to GraphicsWrap.drawRect; LinesPoints.drawPoint and Lines.drawPoint to drawRect; ReliefDrawer.drawColoredRelief to GraphicsWrap.drawImage. Each pair was justified by a source grep, the closed-branch or never-constructed reasoning recorded in parts/label_125.md. Lines does not extend PointDrawer2D, and its drawPoint call is commented out.
- Batch 127 (build 177): two sup pairs, AnkiDroidApp.onCreate to ProductionCrashReportingTree.<init> and <clinit>. The only creation is in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155-166). The dataset APK is the debug build (final_java_only/AnkiDroid/app/DATASET.txt line 4). Build 177 showed a CALL edge to <clinit> as well as <init>; both are suppressed.
- Batch 129 (build 179): eleven sup pairs. On API 27, CompatHelper selects CompatV21 (CompatHelper.java:35-36). CompatV21 inherits disableDatabaseWriteAheadLogging and updateWidgetDimensions from CompatV16, and enableCookiesForFileSchemePages from CompatV12, so the CompatV10 and CompatV11 bodies and the Nook class are shadowed. The pairs cover the automatic CALL edges from Collection.close, DB.<init>, AnkiDroidApp.onCreate, AnkiDroidWidgetSmall and CompatHelper.<init>.
- Reference level: the graph uses API 27 for closed_by_api_level, as in earlier batches (AGENT_NOTES.md build log). DATASET.txt says min_sdk 10 and target_sdk 23 (lines 6-7). This tension is not resolved. For the reviewer: confirm that API 27 is the intended reference level.
- Batch 128 (build 178): no sup. The suspect automatic pair Hooks.runFilter to AdvancedStatistics.runFilter is not suppressed. Revisit it when batches 135-137 merge.
- LibreTorrent: not touched by this run. It stays "- [H]" in handoff/PROGRESS_V2.md (handed to ChatGPT 2026-10-28).
'''
open(H, 'a', encoding='utf-8').write(decisions)
print('updated', now)
