"""Print the model that a headless `claude -p --output-format json` run used for its main work, read from the JSON that the run prints last.
Usage: python3 -I tools/run_models.py <run output file>
The run also makes small calls of its own (for example on Haiku 4.5); they are listed as 'other calls'."""
import json, sys


def summary(path):
    lines = [l for l in open(path, encoding='utf-8', errors='replace').read().split('\n') if l.startswith('{') and '"modelUsage"' in l]
    if not lines:
        return 'no model usage in the output'
    d = json.loads(lines[-1])
    mu = d.get('modelUsage') or {}
    if not mu:
        return 'no model usage in the output'

    def tot(v):
        return sum(v.get(k, 0) for k in ('inputTokens', 'outputTokens', 'cacheReadInputTokens', 'cacheCreationInputTokens'))
    main = max(mu, key=lambda m: tot(mu[m]))
    side = sorted(m for m in mu if m != main)
    return 'main model %s; other calls: %s' % (main, ', '.join(side) or 'none')


if __name__ == '__main__':
    print(summary(sys.argv[1]))
