from bose.core import collector, main, run, run_exit, runmodule
# backwards compatibility
from bose.exc import SkipTest, DeprecatedTest
from bose.tools import with_setup

__author__ = 'Jason Pellerin'
__versioninfo__ = (1, 3, 7)
__version__ = '.'.join(map(str, __versioninfo__))

__all__ = [
    'main', 'run', 'run_exit', 'runmodule', 'with_setup',
    'SkipTest', 'DeprecatedTest', 'collector'
    ]


