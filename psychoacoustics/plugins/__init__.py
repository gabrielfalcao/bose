"""
Writing Plugins
---------------

psychoacoustics supports plugins for test collection, selection, observation and
reporting. There are two basic rules for plugins:

* Plugin classes should subclass :class:`psychoacoustics.plugins.Plugin`.

* Plugins may implement any of the methods described in the class
  :doc:`IPluginInterface <interface>` in psychoacoustics.plugins.base. Please note that
  this class is for documentary purposes only; plugins may not subclass
  IPluginInterface.

Hello World
===========

Here's a basic plugin.  It doesn't do much so read on for more ideas or dive
into the :doc:`IPluginInterface <interface>` to see all available hooks.

.. code-block:: python

    import logging
    import os

    from psychoacoustics.plugins import Plugin

    log = logging.getLogger('psychoacoustics.plugins.helloworld')

    class HelloWorld(Plugin):
        name = 'helloworld'

        def options(self, parser, env=os.environ):
            super(HelloWorld, self).options(parser, env=env)

        def configure(self, options, conf):
            super(HelloWorld, self).configure(options, conf)
            if not self.enabled:
                return

        def finalize(self, result):
            log.info('Hello pluginized world!')

Registering
===========

.. Note::
  Important note: the following applies only to the default
  plugin manager. Other plugin managers may use different means to
  locate and load plugins.

For psychoacoustics to find a plugin, it must be part of a package that uses
setuptools_, and the plugin must be included in the entry points defined
in the setup.py for the package:

.. code-block:: python

    setup(name='Some plugin',
        # ...
        entry_points = {
            'psychoacoustics.plugins.0.10': [
                'someplugin = someplugin:SomePlugin'
                ]
            },
        # ...
        )

Once the package is installed with install or develop, psychoacoustics will be able
to load the plugin.

.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools

Registering a plugin without setuptools
=======================================

It is currently possible to register a plugin programmatically by
creating a custom psychoacoustics runner like this :

.. code-block:: python

    import psychoacoustics
    from yourplugin import YourPlugin

    if __name__ == '__main__':
        psychoacoustics.main(addplugins=[YourPlugin()])

Defining options
================

All plugins must implement the methods ``options(self, parser, env)``
and ``configure(self, options, conf)``. Subclasses of psychoacoustics.plugins.Plugin
that want the standard options should call the superclass methods.

psychoacoustics uses optparse.OptionParser from the standard library to parse
arguments. A plugin's ``options()`` method receives a parser
instance. It's good form for a plugin to use that instance only to add
additional arguments that take only long arguments (--like-this). Most
of psychoacoustics's built-in arguments get their default value from an environment
variable.

A plugin's ``configure()`` method receives the parsed ``OptionParser`` options
object, as well as the current config object. Plugins should configure their
behavior based on the user-selected settings, and may raise exceptions
if the configured behavior is nonsensical.

Logging
=======

psychoacoustics uses the logging classes from the standard library. To enable users
to view debug messages easily, plugins should use ``logging.getLogger()`` to
acquire a logger in the ``psychoacoustics.plugins`` namespace.

Recipes
=======

* Writing a plugin that monitors or controls test result output

  Implement any or all of ``addError``, ``addFailure``, etc., to monitor test
  results. If you also want to monitor output, implement
  ``setOutputStream`` and keep a reference to the output stream. If you
  want to prevent the builtin ``TextTestResult`` output, implement
  ``setOutputSteam`` and *return a dummy stream*. The default output will go
  to the dummy stream, while you send your desired output to the real stream.

  Example: `examples/html_plugin/htmlplug.py`_

* Writing a plugin that handles exceptions

  Subclass :doc:`ErrorClassPlugin <errorclasses>`.

  Examples: :doc:`psychoacoustics.plugins.deprecated <deprecated>`,
  :doc:`psychoacoustics.plugins.skip <skip>`

* Writing a plugin that adds detail to error reports

  Implement ``formatError`` and/or ``formatFailure``. The error tuple
  you return (error class, error message, traceback) will replace the
  original error tuple.

  Examples: :doc:`psychoacoustics.plugins.capture <capture>`,
  :doc:`psychoacoustics.plugins.failuredetail <failuredetail>`

* Writing a plugin that loads tests from files other than python modules

  Implement ``wantFile`` and ``loadTestsFromFile``. In ``wantFile``,
  return True for files that you want to examine for tests. In
  ``loadTestsFromFile``, for those files, return an iterable
  containing TestCases (or yield them as you find them;
  ``loadTestsFromFile`` may also be a generator).

  Example: :doc:`psychoacoustics.plugins.doctests <doctests>`

* Writing a plugin that prints a report

  Implement ``begin`` if you need to perform setup before testing
  begins. Implement ``report`` and output your report to the provided stream.

  Examples: :doc:`psychoacoustics.plugins.cover <cover>`, :doc:`psychoacoustics.plugins.prof <prof>`

* Writing a plugin that selects or rejects tests

  Implement any or all ``want*``  methods. Return False to reject the test
  candidate, True to accept it -- which  means that the test candidate
  will pass through the rest of the system, so you must be prepared to
  load tests from it if tests can't be loaded by the core loader or
  another plugin -- and None if you don't care.

  Examples: :doc:`psychoacoustics.plugins.attrib <attrib>`,
  :doc:`psychoacoustics.plugins.doctests <doctests>`, :doc:`psychoacoustics.plugins.testid <testid>`


More Examples
=============

See any builtin plugin or example plugin in the examples_ directory in
the psychoacoustics source distribution. There is a list of third-party plugins
`on jottit`_.

.. _examples/html_plugin/htmlplug.py: http://python-psychoacoustics.googlecode.com/svn/trunk/examples/html_plugin/htmlplug.py
.. _examples: http://python-psychoacoustics.googlecode.com/svn/trunk/examples
.. _on jottit: http://psychoacoustics-plugins.jottit.com/

"""
from psychoacoustics.plugins.base import Plugin
from psychoacoustics.plugins.manager import *
from psychoacoustics.plugins.plugintest import PluginTester

if __name__ == '__main__':
    import doctest
    doctest.testmod()
