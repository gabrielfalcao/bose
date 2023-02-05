This is a test of the bug reported in issue 100: test.address() fails
for a case defined in a doctest.

    >>> import unittest
    >>> import psychoacoustics.case
    >>> class SimpleTest(unittest.TestCase):
    ...
    ...     def runTest(self):
    ...         pass
    >>> test = psychoacoustics.case.Test(SimpleTest())
    >>> test.address()
    (None, '__builtin__', 'SimpleTest.runTest')
