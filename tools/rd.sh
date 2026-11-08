#!/bin/bash
# compact source view: strip imports/comments/blank/brace-only lines, trim long lines
for f in "$@"; do echo "=================== $f"; cat -n "$f" | grep -v -E '^\s+[0-9]+\s+(import |package |\s*$|\s*//|\s*\*|\s*/\*|\s*@Override\s*$|\s*[{}]+\s*$|\s*\}\);?\s*$|\s*\}\s*else\s*\{\s*$)' | cut -c1-165; done
