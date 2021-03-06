import os

from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name="mate",
    url="https://github.com/Julian/Mate",

    description="Matchers for unittest",
    long_description=long_description,

    author="Julian Berman",
    author_email="Julian@GrayVines.com",

    license="MIT",

    packages=find_packages(),

    setup_requires=["vcversioner>=2.16.0.0"],
    vcversioner={"version_module_paths": ["mate/_version.py"]},

    classifiers=classifiers,
)
