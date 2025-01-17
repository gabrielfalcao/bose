import os
import sys
import unittest
import psychoacoustics.config
import psychoacoustics.importer

class TestImporter(unittest.TestCase):

    def setUp(self):
        self.p = sys.path[:]

    def tearDown(self):
        sys.path = self.p[:]
    
    def test_add_paths(self):
        where = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'support'))
        foo = os.path.join(where, 'foo')
        foobar = os.path.join(foo, 'bar')
        psychoacoustics.importer.add_path(foobar)
        
        assert not foobar in sys.path
        assert not foo in sys.path
        assert where in sys.path
        assert sys.path[0] == where, "%s first should be %s" % (sys.path, where)

    def test_import(self):
        where = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'support'))
        foo = os.path.join(where, 'foo')
        foobar = os.path.join(foo, 'bar')

        imp = psychoacoustics.importer.Importer()
        mod = imp.importFromDir(foobar, 'buz')
        assert where in sys.path
        # buz has an intra-package import that sets boodle
        assert mod.boodle

    def test_module_no_file(self):
        where = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'support'))
        foo = os.path.join(where, 'foo')
        foobar = os.path.join(foo, 'bar')

        # something that's not a real module and has no __file__
        sys.modules['buz'] = 'Whatever'

        imp = psychoacoustics.importer.Importer()
        mod = imp.importFromDir(foobar, 'buz')
        assert where in sys.path
        # buz has an intra-package import that sets boodle
        assert mod.boodle

    def test_module_init_prefix(self):
        where = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'support', 'init_prefix_bug'))
        psychoacoustics.importer.add_path(where)
        mod = os.path.join(where, '__init__not.py')
        fqname = 'init_prefix_bug.__init__not'

        imp = psychoacoustics.importer.Importer()
        mod = imp.importFromPath(mod, fqname)
        
if __name__ == '__main__':
    unittest.main()
