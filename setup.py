from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'rank',
    version          = '0.0.1',
    description      = 'An app to Rank',
    long_description = readme,
    author           = 'Mario Han',
    author_email     = 'hanmario@bu.edu',
    url              = 'http://wiki',
    packages         = ['rank'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'rank = rank.__main__:main'
            ]
        }
)
