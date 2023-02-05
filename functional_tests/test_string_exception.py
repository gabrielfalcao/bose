import os
import sys
import unittest

from bose.plugins import PluginTester
from bose.plugins.builtin import Deprecated, Skip
from bose.plugins.skip import SkipTest


support = os.path.join(os.path.dirname(__file__), 'support')


class TestStringException(PluginTester, unittest.TestCase):
    activate = '-v'
    plugins = [Deprecated(), Skip()]
    args = []
    suitepath = os.path.join(support, 'string-exception')

    def test_string_exception_works(self):
        if sys.version_info >= (2, 6):
            raise SkipTest("String exceptions are not supported in this "
                           "version of Python")

        print
        print '!' * 70
        print str(self.output)
        print '!' * 70
        print
        assert 'raise "string exception"' in str(self.output)
        assert 'raise "string exception in setup"' in str(self.output)
        assert 'raise "string exception in teardown"' in str(self.output)
        assert 'raise "string exception in test"' in str(self.output)
