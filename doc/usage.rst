Basic usage
-----------

Use the bosetests script (after installation by setuptools)::

  bosetests [options] [(optional) test files or directories]

In addition to passing command-line options, you may also put configuration
options in a .boserc or bose.cfg file in your home directory. These are
standard .ini-style config files. Put your bosetests configuration in a
[bosetests] section, with the -- prefix removed::

   [bosetests]
   verbosity=3
   with-doctest=1

There is also possiblity to disable configuration files loading (might be
useful when runnig i.e. tox and you don't want your global bose config file to
be used by tox). In order to ignore those configuration files simply set an
environment variable ``NOSE_IGNORE_CONFIG_FILES``.
  
There are several other ways to use the bose test runner besides the
`bosetests` script. You may use bose in a test script::

  import bose
  bose.main()

If you don't want the test script to exit with 0 on success and 1 on failure
(like unittest.main), use bose.run() instead::

  import bose
  result = bose.run()
  
`result` will be true if the test run succeeded, or false if any test failed
or raised an uncaught exception. Lastly, you can run bose.core directly, which
will run bose.main()::

  python /path/to/bose/core.py
  
Please see the usage message for the bosetests script for information
about how to control which tests bose runs, which plugins are loaded,
and the test output.

Extended usage
^^^^^^^^^^^^^^

.. autohelp ::
