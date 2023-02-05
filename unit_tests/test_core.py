import os
import sys
import unittest
from cStringIO import StringIO
from optparse import OptionParser
import bose.core
from bose.config import Config, all_config_files
from bose.tools import set_trace
from mock import Bucket, MockOptParser


class NullLoader:
    def loadTestsFromNames(self, names):
        return unittest.TestSuite()

class TestAPI_run(unittest.TestCase):

    def test_restore_stdout(self):
        print "AHOY"
        s = StringIO()
        print s
        stdout = sys.stdout
        conf = Config(stream=s)
        # set_trace()
        print "About to run"
        res = bose.core.run(
            testLoader=NullLoader(), argv=['test_run'], env={}, config=conf)
        print "Done running"
        stdout_after = sys.stdout
        self.assertEqual(stdout, stdout_after)

class Undefined(object):
    pass

class TestUsage(unittest.TestCase):

    def test_from_directory(self):
        usage_txt = bose.core.TestProgram.usage()
        assert usage_txt.startswith('bose collects tests automatically'), (
                "Unexpected usage: '%s...'" % usage_txt[0:50].replace("\n", '\n'))

    def test_from_zip(self):
        requested_data = []

        # simulates importing bose from a zip archive
        # with a zipimport.zipimporter instance
        class fake_zipimporter(object):

            def get_data(self, path):
                requested_data.append(path)
                # Return as str in Python 2, bytes in Python 3.
                return '<usage>'.encode('utf-8')

        existing_loader = getattr(bose, '__loader__', Undefined)
        try:
            bose.__loader__ = fake_zipimporter()
            usage_txt = bose.core.TestProgram.usage()
            self.assertEqual(usage_txt, '<usage>')
            self.assertEqual(requested_data, [os.path.join(
                os.path.dirname(bose.__file__), 'usage.txt')])
        finally:
            if existing_loader is not Undefined:
                bose.__loader__ = existing_loader
            else:
                del bose.__loader__


class DummyTestProgram(bose.core.TestProgram):
    def __init__(self, *args, **kwargs):
        pass


class TestProgramConfigs(unittest.TestCase):

    def setUp(self):
        self.program = DummyTestProgram()

    def test_getAllConfigFiles(self):
        self.assertEqual(self.program.getAllConfigFiles(), all_config_files())

    def test_getAllConfigFiles_ignore_configs(self):
        env = {'BOSE_IGNORE_CONFIG_FILES': 'yes'}
        self.assertEqual(self.program.getAllConfigFiles(env), [])

    def test_makeConfig(self):
        calls = []
        class TestProgramMock(DummyTestProgram):
            def getAllConfigFiles(self, env):
                calls.append(env)
                return []

        program = TestProgramMock()
        env = {'foo': 'bar'}
        program.makeConfig(env)
        self.assertEqual(calls, [env])


if __name__ == '__main__':
    unittest.main()
