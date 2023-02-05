"""
An example of how to create a simple psychoacoustics plugin.

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
    author_email = 'jpellerin+psychoacoustics@gmail.com',
    description = 'Example psychoacoustics plugin',
    license = 'GNU LGPL',
    py_modules = ['plug'],
    entry_points = {
        'psychoacoustics.plugins.0.10': [
            'example = plug:ExamplePlugin'
            ]
        }

    )
