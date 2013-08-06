import sys
import os
import io
from subprocess import call
from xdress.plugins import Plugin

if sys.version < 3:
    basestring = str

import collections


class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

_extension = """\
{tarfile} = Extension("{pack}.{tarfile}",
\t["{packdir}/{tarfile}.pyx", "{srcdir}/{srcfile}.cpp"],
\tinclude_dirs=incdirs, language="c++")
"""

_stl_extention = """\
stl_cont = Extension("{pack}.stlcontainers", ["{pack}/stlcontainers.pyx"],
                     include_dirs=incdirs, language="c++")
"""
_xd_extras_ext = """\
xdress_extras = Extension("{pack}.xdress_extra_types",
                          ["{pack}/xdress_extra_types.pyx"],
                          include_dirs=incdirs, language="c++")
"""

_setup_main = """\
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), '{packdir}'),
           os.path.join(os.getcwd(), '{srcdir}'),
           np.get_include()]

# Define extensions
{extensions}

ext_modules = {ext_mod_list}

setup(name='{pack}',
      cmdclass=dict([('build_ext', build_ext)]),
      ext_modules=ext_modules,
      packages=['{pack}']
      )
"""

_import_obj = "from {pack}.{tarfile} import {obj}\n"


_init_main = """\
# import classes
{classes}
# import functions
{functions}

"""


class XDressPlugin(Plugin):
    """Plugin for generating __init__.py and setup.py."""
    defaultrc = {'init_filename': '__init__.py',
                 'setup_filename': 'setup.py',
                 'run_setup': False}

    def execute(self, rc):
        package = rc.package
        packagedir = rc.packagedir
        srcdir = rc.sourcedir

        classes = rc.classes
        functions = rc.functions

        classes_set = OrderedSet()
        ext_set = OrderedSet()
        str_funcs = ''
        e_mod_list = OrderedSet()

        if os.path.isfile(packagedir + os.path.sep + 'xdress_extra_types.pyx'):
            ext_set.add(_xd_extras_ext.format(pack=package))
            e_mod_list.add('stl_cont')

        if os.path.isfile(packagedir + os.path.sep + 'stlcontainers.pyx'):
            ext_set.add(_stl_extention.format(pack=package))
            e_mod_list.add('xdress_extras')

        for cc in classes:
            srcfile = cc.srcfile
            tarfile = cc.tarfile
            c_tarname = cc.tarname
            if isinstance(c_tarname, basestring):
                tarname = c_tarname
            else:
                tarname = c_tarname[0]

            classes_set.add(_import_obj.format(pack=package,
                                               tarfile=tarfile,
                                               obj=tarname))

            ext_set.add(_extension.format(pack=package,
                                          tarfile=tarfile,
                                          packdir=packagedir,
                                          srcdir=srcdir,
                                          srcfile=srcfile
                                          ))
            e_mod_list.add(tarfile)

        for ff in functions:
            srcfile = ff.srcfile
            tarfile = ff.tarfile
            c_tarname = ff.tarname
            if isinstance(c_tarname, basestring):
                tarname = c_tarname
            else:
                tarname = c_tarname[0]

            str_funcs += _import_obj.format(pack=package,
                                            tarfile=tarfile,
                                            obj=tarname)

            ext_set.add(_extension.format(pack=package,
                                          tarfile=tarfile,
                                          packdir=packagedir,
                                          srcdir=srcdir,
                                          srcfile=srcfile
                                          ))
            e_mod_list.add(tarfile)

        # Create the string for the extension modules
        str_e_mod_list = '['
        str_e_mod_list += ',\n\t'.join(e_mod_list)
        str_e_mod_list += ']'

        # Create the string for the classes
        str_classes = ''.join(classes_set)

        # Create string for the extensions
        str_extensions = '\n\n'.join(ext_set)

        # Write the __init__.py
        init_name = packagedir + os.path.sep + rc.init_filename
        print('init_setup: Writing %s' % init_name)
        init_txt = _init_main.format(classes=str_classes, functions=str_funcs)
        with io.open(init_name, 'wb') as f:
            f.write(init_txt)

        setup_txt = _setup_main.format(extensions=str_extensions,
                                       ext_mod_list=str_e_mod_list,
                                       pack=package,
                                       packdir=packagedir,
                                       srcdir=srcdir)

        # Write the setup.py
        print('init_setup: Writing %s' % rc.setup_filename)
        with io.open(rc.setup_filename, 'wb') as f:
            f.write(setup_txt)

        if rc.run_setup:
            print('#' * 72 + '\nRunning setup.py')
            call(['python', 'setup.py', 'build_ext', '--inplace'])
