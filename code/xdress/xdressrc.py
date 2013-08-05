## Do basic setup
package = 'hsfpypy'  # top-level python package name
packagedir = 'hsfpypy'  # location of the generated python package
sourcedir = '../'  # location of the original C++ source

## List the plugins we need. This step is optional, but we use it because we
# need to filter out some types
plugins = ('xdress.stlwrap', 'xdress.autoall', 'xdress.autodescribe',
           # 'xdress.doxygen',
           'xdress.descfilter',
           'xdress.cythongen')

# Which types to ignore or exclude in the wrappers

## Which stl containers we need for this code
stlcontainers = [
    # NOTE: There is an xdress bug that makes it fail to compile if a 'set' or
    #       'map' container isn't included in this list.
    ('set', 'uint'),
    ('vector', 'float64'),  # DoubleVec
    ('vector', 'int32'),  # IntVec
    ('vector', ('vector', 'int32')),  # IntVecVec
    ('vector', ('vector', 'float64')),   # DoubleVecVec
    ]


## Which classes to create wrappers for.
classes = [
    # classname, source filename[, destination filename]
    ('HKnotVector', 'HKnotVector'),
    ]

## Which functions to create wrappers for
functions = [ ]

## which variables to wrap
variables = []
