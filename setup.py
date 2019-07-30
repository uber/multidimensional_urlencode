from __future__ import print_function
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


def read_long_description(filename="README.rst"):
    with open(filename) as f:
        return f.read().strip()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='multidimensional_urlencode',
    version='0.0.4',
    url='https://github.com/uber/multidimensional_urlencode',
    license='MIT',
    author='Sam Marcellus, Charles-Axel Dein',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    author_email='charles@uber.com',
    description='Urlencode a multidimensional dict ',
    long_description=read_long_description(),
    packages=['multidimensional_urlencode'],
    include_package_data=True,
    platforms='any',
    test_suite='multidimensional_urlencode.tests.test_urlencode',
    zip_safe=False,
    keywords=["urlencode", "params", "multidimensional"],
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        ],
)
