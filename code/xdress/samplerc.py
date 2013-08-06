package = 'package'
packagedir = 'output'
sourcedir = 'src'

plugins = ('xdress.stlwrap', 'xdress.autoall', 'xdress.autodescribe',
           'xdress.cythongen', 'foopack.barplug')

## Which stl containers we need for this code
stlcontainers = [('vector', 'float64'),
                 ('set', 'int'),
                 ('map', 'int', ('map', ('vector', 'uint'), ('set', 'char'))),
                 ('vector', ('vector', 'float64')),
                 ('set', 'FooClassBar')
                 ]

## Which classes to create wrappers for.
classes = [('FooClass', 'Foo'),
           ('FooClass', 'Bar', 'Foo', 'FooClassBar'),
           ]

functions = [('FooFunc', 'Foo')]

variables = [('barVar', 'Bar')]
