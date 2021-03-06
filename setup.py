#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "structlog==21.5.0",
    "python-dotenv==0.19.2",
]

test_requirements = [ ]

setup(
    author="Aleksandr Saiapin",
    author_email='alstutor@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="A custom Python logger supporting JSON logging",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='custom_logger',
    name='custom_logger',
    packages=find_packages(include=['custom_logger', 'custom_logger.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/alstutor/custom_logger',
    version='0.1.0',
    zip_safe=False,
)
