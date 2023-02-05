from namespace_pkg import example
from namespace_pkg import example2

def test_namespace_pkg():
    assert example.test == 'the bose knows'
    assert example2.test == 'put that snoot to use'
