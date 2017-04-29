#!/usr/bin/env python

# Project skeleton maintained at https://github.com/the-allanc/skeleton
# All the hard work done by jaraco at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

name = 'skeleton'
description = ''

params = dict(
    name=name,
    version='0.1', # Remove if not using bumpversion.
    use_scm_version=True, # Remove if not using setuptools_scm.
    author="Allan Crooks",
    author_email="allan@increment.one",
    description=description or name,
    long_description=long_description,
    license='MIT',
    url="https://github.com/the-allanc/" + name,
    keywords=[],
    packages=setuptools.find_packages(),
    include_package_data=True,
    namespace_packages=name.split('.')[:-1],
    python_requires='>=2.7',
    install_requires=[
        'requests',
        'six',
    ],
    extras_require={
        'testing': [
            'pytest>=2.8',
            'pytest-sugar',
        ],
        'docs': [
            'sphinx',
            'jaraco.packaging>=3.2',
            'rst.linker>=1.9',
            'sphinx_py3doc_enhanced_theme',
        ],
    },
    setup_requires=[
        'setuptools_scm>=1.15.0', # Remove if not using setuptools_scm.
    ],
    classifiers=[
        #"Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
    },
)

if __name__ == '__main__':
    setuptools.setup(**params)
