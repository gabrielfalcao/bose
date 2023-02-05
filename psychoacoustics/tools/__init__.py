"""
Tools for testing
-----------------

psychoacoustics.tools provides a few convenience functions to make writing tests
easier. You don't have to use them; nothing in the rest of psychoacoustics depends
on any of these methods.

"""
from psychoacoustics.tools.nontrivial import *
from psychoacoustics.tools.nontrivial import __all__ as nontrivial_all
from psychoacoustics.tools.trivial import *
from psychoacoustics.tools.trivial import __all__ as trivial_all

__all__ = trivial_all + nontrivial_all
