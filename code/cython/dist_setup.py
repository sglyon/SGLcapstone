from distutils.core import setup
from Cython.Build import cythonize

setup(name="Pairwise distance", ext_modules=cythonize('cy_pairs.pyx'))
