"""
Tools for testing
-----------------

bose.tools provides a few convenience functions to make writing tests
easier. You don't have to use them; nothing in the rest of bose depends
on any of these methods.

"""
from bose.tools.nontrivial import *
from bose.tools.nontrivial import __all__ as nontrivial_all
from bose.tools.trivial import *
from bose.tools.trivial import __all__ as trivial_all

__all__ = trivial_all + nontrivial_all
