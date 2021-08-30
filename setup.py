"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    setup_requires=['scrapy', 'selenium', 'undetected-chromedriver']
)
