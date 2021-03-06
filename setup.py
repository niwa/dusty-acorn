# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'click==7.0.*',
    'pyserial==3.4.*',
    'tornado==6.0.*'
]

setup_requires = [
    'pytest-runner>=4.4'
]

tests_require = [
    'pytest==4.4.*',
    'coverage>=4.5',
    'pytest-cov>=2.6'
]

sound_testing_require = [
    'pygame==1.9.*'
]

extras_require = {
    'tests': tests_require,
    'all': install_requires + tests_require + sound_testing_require
}

setup(
    name="dusty-acorn",
    version="2.0",
    description="Air Quality monitoring web application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niwa/dusty-acorn",
    packages=find_packages(),
    # find . -name "*.*" -exec sh -c 'echo "${0##*.}"' {} \; | sort | uniq
    package_data={
        '': [
            '*.css',
            '*.eot',
            '*.html',
            '*.jpg',
            '*.js',
            '*.json',
            '*.mp3',
            '*.mp4',
            '*.ods',
            '*.otf',
            '*.png',
            '*.svg',
            '*.ttf',
            '*.woff',
            '*.woff2'
        ],
    },
    python_requires='>=3.7',
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'dusty-acorn=dusty_acorn.main:main'
        ]
    }
)
