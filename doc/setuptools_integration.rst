Setuptools integration
======================

.. warning :: Please note that when run under the setuptools test command,
              many plugins will not be available, including the builtin
              coverage and profiler plugins. If you want to access to all
              available plugins, use the :doc:`psytests <api/commands>`
              command instead.

bose may be used with the setuptools_ test command. Simply specify
bose.collector as the test suite in your setup file::

  setup (
      # ...
      test_suite = 'bose.collector'
  )

Then to find and run tests, you can run::

  python setup.py test

When running under setuptools, you can configure bose settings via the
environment variables detailed in the psytests script usage message,
or the setup.cfg, ~/.boserc or ~/.bose.cfg config files.

`psytests` command
-------------------

bose also includes its own setuptools command, ``psytests``, that provides
support for all plugins and command line options. It works just like the
``test`` command::

  python setup.py psytests

See :doc:`api/commands` for more information about the ``psytests`` command.

.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools

