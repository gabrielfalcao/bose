psychoacoustics.plugins.plugintest, os.environ and sys.argv
------------------------------------------------

:class:`psychoacoustics.plugins.plugintest.PluginTester` and
:func:`psychoacoustics.plugins.plugintest.run` are utilities for testing psychoacoustics
plugins.  When testing plugins, it should be possible to control the
environment seen plugins under test, and that environment should never
be affected by ``os.environ`` or ``sys.argv``.

    >>> import os
    >>> import sys
    >>> import unittest
    >>> import psychoacoustics.config
    >>> from psychoacoustics.plugins import Plugin
    >>> from psychoacoustics.plugins.builtin import FailureDetail, Capture
    >>> from psychoacoustics.plugins.plugintest import PluginTester

Our test plugin takes no command-line arguments and simply prints the
environment it's given by psychoacoustics.

    >>> class PrintEnvPlugin(Plugin):
    ...     name = "print-env"
    ...
    ...     # no command line arg needed to activate plugin
    ...     enabled = True
    ...     def configure(self, options, conf):
    ...         if not self.can_configure:
    ...             return
    ...         self.conf = conf
    ...
    ...     def options(self, parser, env={}):
    ...         print "env:", env

To test the argv, we use a config class that prints the argv it's
given by psychoacoustics.  We need to monkeypatch psychoacoustics.config.Config, so that we
can test the cases where that is used as the default.

    >>> old_config = psychoacoustics.config.Config
    >>> class PrintArgvConfig(old_config):
    ...
    ...     def configure(self, argv=None, doc=None):
    ...         print "argv:", argv
    ...         old_config.configure(self, argv, doc)
    >>> psychoacoustics.config.Config = PrintArgvConfig

The class under test, PluginTester, is designed to be used by
subclassing.

    >>> class Tester(PluginTester):
    ...    activate = "-v"
    ...    plugins = [PrintEnvPlugin(),
    ...               FailureDetail(),
    ...               Capture(),
    ...               ]
    ...
    ...    def makeSuite(self):
    ...        return unittest.TestSuite(tests=[])

For the purposes of this test, we need a known ``os.environ`` and
``sys.argv``.

    >>> old_environ = os.environ
    >>> old_argv = sys.argv
    >>> os.environ = {"spam": "eggs"}
    >>> sys.argv = ["spamtests"]

PluginTester always uses the [psytests, self.activate] as its argv.
If ``env`` is not overridden, the default is an empty ``env``.

    >>> tester = Tester()
    >>> tester.setUp()
    argv: ['psytests', '-v']
    env: {}

An empty ``env`` is respected...

    >>> class EmptyEnvTester(Tester):
    ...    env = {}
    >>> tester = EmptyEnvTester()
    >>> tester.setUp()
    argv: ['psytests', '-v']
    env: {}

... as is a non-empty ``env``.

    >>> class NonEmptyEnvTester(Tester):
    ...    env = {"foo": "bar"}
    >>> tester = NonEmptyEnvTester()
    >>> tester.setUp()
    argv: ['psytests', '-v']
    env: {'foo': 'bar'}


``psychoacoustics.plugins.plugintest.run()`` should work analogously.

    >>> from psychoacoustics.plugins.plugintest import run_buffered as run
    >>> run(suite=unittest.TestSuite(tests=[]),
    ...     plugins=[PrintEnvPlugin()]) # doctest: +REPORT_NDIFF
    argv: ['psytests', '-v']
    env: {}
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 0 tests in ...s
    <BLANKLINE>
    OK
    >>> run(env={},
    ...     suite=unittest.TestSuite(tests=[]),
    ...     plugins=[PrintEnvPlugin()]) # doctest: +REPORT_NDIFF
    argv: ['psytests', '-v']
    env: {}
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 0 tests in ...s
    <BLANKLINE>
    OK
    >>> run(env={"foo": "bar"},
    ...     suite=unittest.TestSuite(tests=[]),
    ...     plugins=[PrintEnvPlugin()]) # doctest: +REPORT_NDIFF
    argv: ['psytests', '-v']
    env: {'foo': 'bar'}
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 0 tests in ...s
    <BLANKLINE>
    OK

An explicit argv parameter is honoured:

    >>> run(argv=["spam"],
    ...     suite=unittest.TestSuite(tests=[]),
    ...     plugins=[PrintEnvPlugin()]) # doctest: +REPORT_NDIFF
    argv: ['spam']
    env: {}
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 0 tests in ...s
    <BLANKLINE>
    OK

An explicit config parameter with an env is honoured:

    >>> from psychoacoustics.plugins.manager import PluginManager
    >>> manager = PluginManager(plugins=[PrintEnvPlugin()])
    >>> config = PrintArgvConfig(env={"foo": "bar"}, plugins=manager)
    >>> run(config=config,
    ...     suite=unittest.TestSuite(tests=[])) # doctest: +REPORT_NDIFF
    argv: ['psytests', '-v']
    env: {'foo': 'bar'}
    <BLANKLINE>
    ----------------------------------------------------------------------
    Ran 0 tests in ...s
    <BLANKLINE>
    OK


Clean up.

    >>> os.environ = old_environ
    >>> sys.argv = old_argv
    >>> psychoacoustics.config.Config = old_config
