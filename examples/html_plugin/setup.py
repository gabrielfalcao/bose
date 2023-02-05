import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='Example html output plugin',
    version='0.1',
    author='Jason Pellerin',
    author_email = 'jpellerin+psychoacoustics@gmail.com',
    description = 'Example psychoacoustics html output plugin',
    license = 'GNU LGPL',
    py_modules = ['htmlplug'],
    entry_points = {
        'psychoacoustics.plugins.0.10': [
            'htmlout = htmlplug:HtmlOutput'
            ]
        }

    )
