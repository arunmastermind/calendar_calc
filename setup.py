#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='calendar_calc',
    version='0.1',
    license='MIT',
    description='Various calculations on a calendar like days, months etc...',
    # long_description='%s\n%s' % (
    #     re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
    #     re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    # ),
    author='Arun Kumar',
    author_email='arunmastermind.sci@gmail.com',
    url='https://github.com/arunmastermind/calendar_calc',
    packages=find_packages('calendar_calc'),
    package_dir={'': 'calendar_calc'},
    py_modules=[splitext(basename(path))[0] for path in glob('calendar_calc/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://calendar_calc.readthedocs.io/',
        'Changelog': 'https://calendar_calc.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/arunmastermind/calendar_calc/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
        'calendar',
        'days',
        'months',
        'time',
        'datetime',
        'week',
    ],
    python_requires='>=3',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        'datetime'
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        # 'console_scripts': [
        #     'mydemo = mydemo.cli:main',
        # ]
    },
)
