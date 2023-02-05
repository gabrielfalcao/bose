import os
import unittest
from psychoacoustics.plugins import Plugin
from psychoacoustics.plugins.plugintest import PluginTester
from psychoacoustics.plugins.manager import ZeroNinePlugin

here = os.path.abspath(os.path.dirname(__file__))

support = os.path.join(os.path.dirname(os.path.dirname(here)), 'support')


class EmptyPlugin(Plugin):
    pass

class TestEmptyPlugin(PluginTester, unittest.TestCase):
    activate = '--with-empty'
    plugins = [ZeroNinePlugin(EmptyPlugin())]
    suitepath = os.path.join(here, 'empty_plugin.rst')

    def test_empty_zero_nine_does_not_crash(self):
        print self.output
        assert "'EmptyPlugin' object has no attribute 'loadTestsFromPath'" \
            not in self.output

    

