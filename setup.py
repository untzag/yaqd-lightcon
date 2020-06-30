#! /usr/bin/env python3

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    return open(os.path.join(here, fname)).read()


with open(os.path.join(here, "yaqd_lightcon", "VERSION")) as version_file:
    version = version_file.read().strip()

extra_files = {"yaqd_lightcon": ["VERSION"]}

setup(
    name="yaqd-lightcon",
    packages=find_packages(exclude=("tests", "tests.*")),
    package_data=extra_files,
    python_requires=">=3.7",
    install_requires=["yaqd-core>=2020.05.1", "aiohttp"],
    extras_require={
        "docs": ["sphinx", "sphinx-gallery>=0.3.0", "sphinx-rtd-theme"],
        "dev": ["black", "pre-commit", "pydocstyle"],
    },
    version=version,
    description="Core structures for yaq component daemons",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="yaq Developers",
    license="LGPL v3",
    url="http://gitlab.com/yaq/yaqd-lightcon",
    entry_points={"console_scripts": [
        "yaqd-lightcon-topas4-motor=yaqd_lightcon._lightcon_topas4_motor:LightconTopas4Motor.main",
        "yaqd-lightcon-topas4-shutter=yaqd_lightcon._lightcon_topas4_shutter:LightconTopas4Shutter.main",
        ]},
    keywords="spectroscopy science multidimensional hardware",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
)
