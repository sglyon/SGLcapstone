#!/usr/bin/env python
"""
setup.py file for building SWIG hsfpy extensions
"""

from distutils.core import setup, Extension

h_knot_vector = Extension('_hsfpy',
                          sources=['./HKnotVector_wrap.cxx']
                          )

setup(name='hsfpy',
      version='0.1',
      author="Spencer Lyon",
      description="""Wrapping hsfpy for python using SWIG""",
      ext_modules=[h_knot_vector],
      py_modules=["hsfpy"],
      )
