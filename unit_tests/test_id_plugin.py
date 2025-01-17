import unittest
from psychoacoustics.config import Config
from psychoacoustics.plugins.builtin import TestId
import mock

class TestTestIdPlugin(unittest.TestCase):

    def test_default_id_file_is_in_working_dir(self):
        tid = TestId()
        c = Config()
        opt = mock.Bucket()
        opt.testIdFile = '.psychoacousticsids'
        tid.configure(opt, c)
        print tid.idfile
        assert tid.idfile.startswith(c.workingDir), \
               "%s is not under %s" % (tid.idfile, c.workingDir)


if __name__ == '__main__':
    unittest.main()
