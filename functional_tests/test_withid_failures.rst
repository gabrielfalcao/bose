    >>> import os
    >>> import sys
    >>> from psychoacoustics.plugins.plugintest import run_buffered as run
    >>> from psychoacoustics.plugins.testid import TestId
    >>> import tempfile
    >>> idfile = tempfile.mktemp()
    >>> support = os.path.join(os.path.dirname(__file__), 'support', 'id_fails')
    >>> argv = [__file__, '-v', '--with-id', '--id-file', idfile, support]
    >>> run(argv=argv, plugins=[TestId()]) # doctest: +ELLIPSIS
    #1 Failure: ImportError (No module ...apackagethatdoesntexist...) ... ERROR
    #2 test_b.test ... ok
    #3 test_b.test_fail ... FAIL
    <BLANKLINE>
    ======================================================================
    ERROR: Failure: ImportError (No module ...apackagethatdoesntexist...)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    ...
    ImportError: No module ...apackagethatdoesntexist...
    <BLANKLINE>
    ======================================================================
    FAIL: test_b.test_fail
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    ...
    AssertionError
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 3 tests in ...s
    <BLANKLINE>
    FAILED (errors=1, failures=1)

Addressing failures works (sometimes).

    >>> argv.append('1')
    >>> _junk = sys.modules.pop('test_a', None) # 2.3 requires
    >>> run(argv=argv, plugins=[TestId()]) #doctest: +ELLIPSIS
    #1 Failure: ImportError (No module ...apackagethatdoesntexist...) ... ERROR
    <BLANKLINE>
    ======================================================================
    ERROR: Failure: ImportError (No module ...apackagethatdoesntexist...)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    ...
    ImportError: No module ...apackagethatdoesntexist...
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 1 test in ...s
    <BLANKLINE>
    FAILED (errors=1)
