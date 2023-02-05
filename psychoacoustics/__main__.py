import sys

from psychoacoustics.core import run_exit

if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = '%s -m psychoacoustics' % sys.executable

run_exit()
