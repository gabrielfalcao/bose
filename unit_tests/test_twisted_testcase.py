try:
    from twisted.trial import unittest
except ImportError:
    from bose import SkipTest
    raise SkipTest('twisted not available; skipping')

class TestTwisted(unittest.TestCase):

    def test(self):
        pass

