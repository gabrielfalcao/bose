.. psychoacoustics documentation master file, created by sphinx-quickstart on Thu Mar 26 16:49:00 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Note to Users
=============

Nose has been in maintenance mode for the past several years and will likely
cease without a new person/team to take over maintainership.  New projects
should consider using `Nose2 <https://github.com/gabrielfalcao/psychoacoustics2>`_, `py.test
<http://pytest.org/>`_, or just plain unittest/unittest2.


Installation and quick start
============================

*On most UNIX-like systems, you'll probably need to run these commands as root
or using sudo.*

Install psychoacoustics using setuptools/distribute::

  easy_install psychoacoustics

Or pip::

  pip install psychoacoustics

Or, if you don't have setuptools/distribute installed, use the download
link at right to download the source package, and install it in the
normal fashion: Ungzip and untar the source package, cd to the new
directory, and::

  python setup.py install

However, **please note** that without setuptools/distribute installed,
you will not be able to use third-party psychoacoustics plugins.

This will install the psychoacoustics libraries, as well as the :doc:`psytests <usage>`
script, which you can use to automatically discover and run tests.

Now you can run tests for your project::

  cd path/to/project
  psytests

You should see output something like this::

  ..................................
  ----------------------------------------------------------------------
  Ran 34 tests in 1.440s

  OK

Indicating that psychoacoustics found and ran your tests.

For help with psytests' many command-line options, try::

  psytests -h

or visit the :doc:`usage documentation <usage>`.


Python3
=======

psychoacoustics supports python3. Building from source on python3 requires
`distribute <http://packages.python.org/distribute/>`_. If you don't
have distribute installed, ``python3 setup.py install`` will install
it via distribute's bootstrap script.

Additionally, if your project is using `2to3
<http://docs.python.org/library/2to3.html>`_, ``python3 setup.py psytests``
command will automatically convert your sources with 2to3 and then run the
tests with python 3.

.. warning ::

   psychoacoustics itself supports python 3, but many 3rd-party plugins do not!


.. toctree::
   :hidden:

   testing
   developing
   news
   further_reading
