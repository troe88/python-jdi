__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='jdi-test',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            []
    },
    install_requires=[
        'selenium',
        'pytest-runner',
        'PyHamcrest',
        'utils',
        'pytest-html',
        'tests',
        'pytest-allure-adaptor',
        'pytest',
        'pytest-xdist'
    ]
)
