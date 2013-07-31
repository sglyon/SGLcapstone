#!/usr/bin/env python
"""
setup.py file for building SWIG hbs extensions
"""

from distutils.core import setup, Extension

h_knot_vector = Extension('_hbspy',
                          sources=['./HKnotVector_wrap.cxx']
                          )

setup(name='hbspy',
      version='0.1',
      author="Spencer Lyon",
      description="""Wrapping HBS for python using SWIG""",
      ext_modules=[h_knot_vector],
      py_modules=["hbspy"],
      )
