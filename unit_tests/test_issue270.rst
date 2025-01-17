Multiprocess test collection from packages
------------------------------------------

Tests that the multiprocess plugin correctly collects tests from packages

    >>> import os
    >>> from psychoacoustics.plugins.plugintest import run_buffered as run
    >>> from psychoacoustics.plugins.multiprocess import MultiProcess
    >>> support = os.path.join(os.path.dirname(__file__), 'support')
    >>> issue270 = os.path.join(support, 'issue270')

The test package has a package-level fixture, which causes the entire package
to be dispatched to a multiprocess worker. Tests are still collected and run
properly.

    >>> argv = [__file__, '--processes=2', issue270]
    >>> run(argv=argv, plugins=[MultiProcess()])
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in ...s
    <BLANKLINE>
    OK
