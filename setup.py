# !/usr/bin/env python
"""Setup for django-cookiecutter."""

from setuptools import find_packages, setup

__version__ = "0.26.5"

setup(
    name="django-cookiecutter",
    packages=find_packages(exclude=("tests*", "testing*")),
    version=__version__,
    description="A Django project cookiecutter complete with built-in\
         continuous delivery using GitHub actions. ",
    author="Mark Sevelj",
    license="BSD",
    author_email="mark.sevelj@dunwright.com.au",
    url="https://github.com/imAsparky/djang-cookiecutter",
    keywords=[
        "Django",
        "cookiecutter",
        "Python 3",
        "template",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
