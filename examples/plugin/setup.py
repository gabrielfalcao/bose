"""
An example of how to create a simple bose plugin.

"""
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='Example plugin',
    version='0.1',
    author='Jason Pellerin',
    author_email = 'jpellerin+bose@gmail.com',
    description = 'Example bose plugin',
    license = 'GNU LGPL',
    py_modules = ['plug'],
    entry_points = {
        'bose.plugins.0.10': [
            'example = plug:ExamplePlugin'
            ]
        }

    )
