#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    reload(sys).setdefaultencoding("UTF-8")
except:
    pass

try:
    from setuptools import setup
except ImportError:
    print('Please install or upgrade setuptools or pip to continue')
    sys.exit(1)

import codecs


def read(filename):
    return codecs.open(filename, encoding='utf-8').read()


long_description = '\n\n'.join([read('README'),
                                read('AUTHORS'),
                                read('CHANGES')])

__doc__ = long_description

setup(
    name='pint-mtools',
    version='0.12.2',
    description='Physical quantities module (modified for unitdoc)',
    long_description=long_description,
    keywords='physical quantities unit conversion science',
    author='Hernan E. Grecco',
    author_email='hernan.grecco@gmail.com',
    url='https://github.com/hgrecco/pint',
    test_suite='pint.testsuite.testsuite',
    zip_safe=True,
    packages=['pint_mtools'],
    package_data={
        'pint_mtools': ['default_en.txt',
                        'constants_en.txt']
      },
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    extras_require={
        ':python_version == "2.7"': [
            'funcsigs',
        ],
    },
    )
