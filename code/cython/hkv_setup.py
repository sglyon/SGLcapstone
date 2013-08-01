from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

incdirs = ['..', '.', np.get_include()]

HKnotVector = Extension("hbspy.HKnotVector",
                        ["hbspy/HKnotVector.pyx"],
                        include_dirs=incdirs, language="c++")

ext_modules = [HKnotVector]

setup(name='hbspy',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules,
      packages=['hbspy']
      )
