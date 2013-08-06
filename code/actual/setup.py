import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'hsfpy'),
           os.path.join(os.getcwd(), 'src'),
           np.get_include()]

# Define extensions
xdress_extras = Extension("hsfpy.xdress_extra_types",
                          ["hsfpy/xdress_extra_types.pyx"],
                          include_dirs=incdirs, language="c++")


stl_cont = Extension("hsfpy.stlcontainers", ["hsfpy/stlcontainers.pyx"],
                     include_dirs=incdirs, language="c++")


HKnotVector = Extension("hsfpy.HKnotVector",
	["hsfpy/HKnotVector.pyx", "src/HKnotVector.cpp"],
	include_dirs=incdirs, language="c++")


Point = Extension("hsfpy.Point",
	["hsfpy/Point.pyx", "src/Point.cpp"],
	include_dirs=incdirs, language="c++")


HNurbs = Extension("hsfpy.HNurbs",
	["hsfpy/HNurbs.pyx", "src/HNurbs.cpp"],
	include_dirs=incdirs, language="c++")


common = Extension("hsfpy.common",
	["hsfpy/common.pyx", "src/common.cpp"],
	include_dirs=incdirs, language="c++")


HNurbsTree = Extension("hsfpy.HNurbsTree",
	["hsfpy/HNurbsTree.pyx", "src/HNurbsTree.cpp"],
	include_dirs=incdirs, language="c++")


HForest = Extension("hsfpy.HForest",
	["hsfpy/HForest.pyx", "src/HForest.cpp"],
	include_dirs=incdirs, language="c++")


ext_modules = [stl_cont,
	xdress_extras,
	HKnotVector,
	Point,
	HNurbs,
	common,
	HNurbsTree,
	HForest]

setup(name='hsfpy',
      cmdclass=dict([('build_ext', build_ext)]),
      ext_modules=ext_modules,
      packages=['hsfpy']
      )
