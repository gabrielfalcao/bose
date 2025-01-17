# There are more attribute plugin unit tests in unit_tests/test_plugins.py
from psychoacoustics.tools import eq_
from psychoacoustics.plugins.attrib import attr

def test_flags():
    # @attr('one','two')
    def test():
        pass
    test = attr('one','two')(test)
    
    eq_(test.one, 1)
    eq_(test.two, 1)

def test_values():
    # @attr(mood="hohum", colors=['red','blue'])
    def test():
        pass
    test = attr(mood="hohum", colors=['red','blue'])(test)
    
    eq_(test.mood, "hohum")
    eq_(test.colors, ['red','blue'])

def test_mixed():
    # @attr('slow', 'net', role='integration')
    def test():
        pass
    test = attr('slow', 'net', role='integration')(test)
    
    eq_(test.slow, 1)
    eq_(test.net, 1)
    eq_(test.role, 'integration')

def test_class_attrs():
    # @attr('slow', 'net', role='integration')
    class MyTest:
        def setUp():
            pass
        def test_one(self):
            pass
        def test_two(self):
            pass

    class SubClass(MyTest):
        pass

    MyTest = attr('slow', 'net', role='integration')(MyTest)
    eq_(MyTest.slow, 1)
    eq_(MyTest.net, 1)
    eq_(MyTest.role, 'integration')
    eq_(SubClass.slow, 1)

    assert not hasattr(MyTest.setUp, 'slow')
    assert not hasattr(MyTest.test_two, 'slow')
