# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from setuptools import setup, find_packages

setup(
    name="local_transfer_file",
    version="0.0.1",
    keywords=("local transfer file", "qr code"),
    description="local transfer file",
    long_description="eds sdk for python",
    license="MIT Licence",

    url="https://github.com/woshimanong1990/local_file_share",
    author="ant",
    author_email="qinghelanzhu@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "PyQt5",
        "qrcode"
    ],

    scripts=[],
    entry_points={
        'console_scripts': [
            'local_transfer_file = local_transfer_file.main:main'
        ]
    }
)