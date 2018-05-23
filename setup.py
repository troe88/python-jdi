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
            ['test_jdi = pytest -m jdi -v --capture=no', 'helloworld = helloworld.core:print_message']
    },
    install_requires=[
        'selenium', 'pytest-runner'
    ],
    tests_require=['pytest']
)
