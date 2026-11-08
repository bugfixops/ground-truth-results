#!/bin/bash
# L5 local full-scope greps: corpus java (281) + res-layout (73) + other-sourcesets (test/androidTest, excluded as triggers per D23 but listed separately)
J=~/workspace/overnight/stream-A/corpus/java
R=~/workspace/overnight/stream-A/corpus/res-layout
O=~/workspace/overnight/stream-A/phase3/greps/L5
echo "== corpus counts =="; find $J -name '*.java' | wc -l; find $R -name '*.xml' | wc -l
