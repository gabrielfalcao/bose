import sys

from bose.core import run_exit

if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = '%s -m bose' % sys.executable

run_exit()
