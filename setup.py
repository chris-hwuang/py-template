# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='',
    version='0.1.0',
    description='',
    long_description=readme,
    author='chris_h',
    author_email='chris_hwuang@163.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

