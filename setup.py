"""
Name: setup.py
Description: Bolt message bus setup file
Date: 08/12/2017
Author: Saurabh Badhwar <sbadhwar@redhat.com>
"""
from codecs import open
from os import path
from setuptools import setup, find_packages

base_path = path.abspath(path.dirname(__file__))

with open(path.join(base_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bolt-message-bus',
    version='0.0.1',
    description='Bolt message bus subsystem',
    long_description=long_description,
    url='https://github.com/project-bolt/bolt-message-bus',
    author='Saurabh Badhwar',
    author_email='sbadhwar@redhat.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Langauge :: Python :: 2.7',
    ],
    keywords='bolt ci message bus',
    packages=find_packages(exclude=['docs', 'tests', 'temp']),
)
