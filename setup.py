from setuptools import setup
from setuptools.command.install import install
import os

setup(
      name='termboxplot',
      version='0.0.1',
      license='GPL',
      description='Tufte inspired, one-liner, pipe-able, tidy data compatible, utf8, unicode boxplots',
      author='git314',
      author_email='git314@tutanota.com',
      url='https://github.com/git314/termboxplot',
      keywords=['terminal','boxplot','unicode', 'ascii', 'utf8'],
      py_modules=['termboxplot'],
      install_requires=['Click', 'pandas', 'numpy'],
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research/Business',
        'License :: OSI Approved :: GPL',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5'
        ],
      entry_points='''
      [console_scripts]
      termbox=termboxplot:main
      '''
)
