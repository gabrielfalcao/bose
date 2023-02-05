import unittest
import bose.selector
from bose.config import Config
from bose.plugins.base import Plugin
from bose.plugins.manager import PluginManager

class TestSelectorPlugins(unittest.TestCase):

    def test_rejection(self):
        class EvilSelector(Plugin):
            def wantFile(self, filename, package=None):
                if 'good' in filename:
                    return False
                return None

        c = Config(plugins=PluginManager(plugins=[EvilSelector()]))
        s = bose.selector.Selector(c)
        s2 = bose.selector.Selector(Config())
        
        assert s.wantFile('test_neutral.py')
        assert s2.wantFile('test_neutral.py')
        
        assert s.wantFile('test_evil.py')
        assert s2.wantFile('test_evil.py')
        
        assert not s.wantFile('test_good.py')
        assert s2.wantFile('test_good.py')
        
if __name__ == '__main__':
    unittest.main()
