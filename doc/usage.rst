Basic usage
-----------

Use the psytests script (after installation by setuptools)::

  psytests [options] [(optional) test files or directories]

In addition to passing command-line options, you may also put configuration
options in a .psychoacousticsrc or psychoacoustics.cfg file in your home directory. These are
standard .ini-style config files. Put your psytests configuration in a
[psytests] section, with the -- prefix removed::

   [psytests]
   verbosity=3
   with-doctest=1

There is also possiblity to disable configuration files loading (might be
useful when runnig i.e. tox and you don't want your global psychoacoustics config file to
be used by tox). In order to ignore those configuration files simply set an
environment variable ``PSY_ECHOS_TICKS_IGNORE_CONFIG_FILES``.
  
There are several other ways to use the psychoacoustics test runner besides the
`psytests` script. You may use psychoacoustics in a test script::

  import psychoacoustics
  psychoacoustics.main()

If you don't want the test script to exit with 0 on success and 1 on failure
(like unittest.main), use psychoacoustics.run() instead::

  import psychoacoustics
  result = psychoacoustics.run()
  
`result` will be true if the test run succeeded, or false if any test failed
or raised an uncaught exception. Lastly, you can run psychoacoustics.core directly, which
will run psychoacoustics.main()::

  python /path/to/psychoacoustics/core.py
  
Please see the usage message for the psytests script for information
about how to control which tests psychoacoustics runs, which plugins are loaded,
and the test output.

Extended usage
^^^^^^^^^^^^^^

.. autohelp ::
