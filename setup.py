from setuptools import setup
from setuptools.command.install import install
import os

setup(
    name="termboxplot",
    version="0.0.5",
    license="GPL LGPL",
    description="Tufte inspired, one-liner, pipe-able, tidy data compatible, utf8, unicode boxplots",
    author="git314",
    author_email="git314@tutanota.com",
    url="https://github.com/git314/termboxplot",
    download_url="https://github.com/git314/termboxplot/releases/tag/0.0.1",
    keywords=["terminal", "boxplot", "unicode", "ascii", "utf8"],
    py_modules=["termboxplot"],
    install_requires=["Click", "pandas", "numpy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points="""
      [console_scripts]
      termbox=termboxplot:main
      """,
)
