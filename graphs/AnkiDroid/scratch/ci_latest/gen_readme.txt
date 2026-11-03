Traceback (most recent call last):
  File "/home/runner/work/ground-truth-results/ground-truth-results/tools/gen_readme_v2.py", line 145, in <module>
    main(sys.argv)
  File "/home/runner/work/ground-truth-results/ground-truth-results/tools/gen_readme_v2.py", line 91, in main
    ' (' + '; '.join(sorted({x['via'] for x in nonstd if x['via']}))[:300] + ')' if nonstd else ''))
                             ~^^^^^^^
TypeError: unhashable type: 'list'
