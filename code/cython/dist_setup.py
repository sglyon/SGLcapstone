import os
from distutils.core import setup
from distutils.extension import Extension
import numpy as np

inc_dirs = [np.get_include(),
            '..']

hkv = Extension("hsfpypy.HKnotVector", ['HKnotVector.pyx'],
                include_dirs=['..', '.', np.get_include()], language="c++")

setup(name="Pairwise distance", ext_modules=[hkv])
