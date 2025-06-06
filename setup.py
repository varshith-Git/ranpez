# setup.py

from setuptools import setup, find_packages
import time

setup(
    name='ranpez',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyarrow',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'ranpez=main:main',
        ],
    },
)
