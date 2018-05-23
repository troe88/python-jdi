from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='jdi-test',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    test_suite='tests.test_Classes',
    entry_points={
        'console_scripts':
            []
    },
    install_requires=[
        'selenium', 'pytest-runner', 'PyHamcrest'
    ],
    tests_require=['pytest']
)
