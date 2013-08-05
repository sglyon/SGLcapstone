from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

incdirs = ['..', '.', np.get_include()]

HKnotVector = Extension("hsfpypy.HKnotVector",
                        ["hsfpypy/HKnotVector.pyx"],
                        include_dirs=incdirs, language="c++")

ext_modules = [HKnotVector]

setup(name='hsfpypy',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules,
      packages=['hsfpypy']
      )
