import sys
import unittest
import warnings
from psychoacoustics.plugins.errorclass import ErrorClass, ErrorClassPlugin
from psychoacoustics.exc import SkipTest

class TestErrorClassWithStringException(unittest.TestCase):

    def test_string_exception_not_masked(self):
        if sys.version_info >= (3,):
            raise SkipTest("Python 3.x does not support string exceptions")

        class X(Exception):
            pass

        class EP(ErrorClassPlugin):
            xes = ErrorClass(X, label='XXX', isfailure=True)

        warnings.filterwarnings(action='ignore', category=DeprecationWarning)
        try:

            raise "oh no!"
        except:
            exc = sys.exc_info()
        
        ep = EP()
        self.assertEqual(ep.addError(None, exc), None)
