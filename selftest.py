#!/usr/bin/env python

"""Test the copy of psychoacoustics in this directory, by running that psychoacoustics against itself.

You can test psychoacoustics using psychoacoustics in other ways, but if you don't use this script,
you might have one installation of psychoacoustics testing another installation, which is
not supported.
"""

# More detail:

# In the absence of some sort of deep renaming magic, psychoacoustics can't reasonably
# test a different installation of itself, given the existence of the global
# module registry sys.modules .

# If installed system-wide with setuptools, setuptools (via the site-packages
# easy-install.pth) takes you at your word and ensures that the installed psychoacoustics
# comes first on sys.path .  So the only way to test a copy of psychoacoustics other than
# the installed one is to install that version (e.g. by running python setup.py
# develop).

# This script provides a way of running psychoacoustics on psychoacoustics's own tests without
# installing the version to be tested, nor uninstalling the currently-installed
# version.

import glob
import os
import sys


if __name__ == "__main__":
    this_dir = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
    lib_dirs = [this_dir]
    test_dir = this_dir
    if sys.version_info >= (3,):
        # Under Python 3.x, we need to 'build' the source (using 2to3, etc)
        # first.  'python3 setup.py build_tests' will put everything under
        # build/tests (including psychoacoustics itself, since some tests are inside the
        # psychoacoustics source)
        # The 'py3where' argument in setup.cfg will take care of making sure we
        # pull our tests only from the build/tests directory.  We just need to
        # make sure the right things are on sys.path.
        lib_dirs = glob.glob(os.path.join(this_dir, 'build', 'lib*'))
        test_dir = os.path.join(this_dir, 'build', 'tests')
        if not os.path.isdir(test_dir):
            raise AssertionError("Error: %s does not exist.  Use the setup.py 'build_tests' command to create it." % (test_dir,))
    try:
        import pkg_resources
        env = pkg_resources.Environment(search_path=lib_dirs)
        distributions = env["psychoacoustics"]
        assert len(distributions) == 1, (
                "Incorrect usage of selftest.py; please see DEVELOPERS.txt")
        dist = distributions[0]
        dist.activate()
    except ImportError:
        pass
    # Always make sure our chosen test dir is first on the path
    sys.path.insert(0, test_dir)
    import psychoacoustics
    psychoacoustics.run_exit()
