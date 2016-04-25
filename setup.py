import os
from setuptools import setup

__name__ = 'randomuser'
__version__ = '0.1.0'

setup(
    name=__name__,
    version=__version__,
    url='https://github.com/jonblum/randomuser',
    author='Jonathan Elliott Blum',
    author_email='jon@jonblumet.net',
    description='Randomuser.me wrapper for Python',

    py_modules=['randomuser'],

    install_requires=[
        'requests'
    ],

    classifiers=[],
)
