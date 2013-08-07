import sys
sys.path.insert(0, '.')

## Do basic setup
package = 'hsfpy'  # top-level python package name
packagedir = 'hsfpy'  # location of the generated python package
sourcedir = 'src'  # location of the original C++ source

# Options for my utils.init_setup plugin
init_filename = '__init__.py'
setup_filename = 'setup.py'
run_setup = False


## List the plugins we need. This step is optional, but we use it because we
# need to filter out some types
plugins = ('xdress.autoall',
           'xdress.autodescribe',
           'xdress.doxygen',
           'xdress.descfilter',
           'xdress.cythongen',
           'xdress.stlwrap',
           'utils.init_setup')

# Which types to ignore or exclude in the wrappers
skiptypes = ['ExtractData', 'HExtractCache', 'HMeshCache', 'istream',
             'basic_istream', 'basic_ostream', 'HTrunkData', 'Activity', 'bool',
             'Cell', 'BFunc', 'HExtract', 'Knot', 'Tree', 'CellFace']

# Which methods to skip in various classes
skipmethods = {
    'HNurbsTree': ['saveFile', 'saveTSplineFile', 'loadStreamBody'],
    'HForest': ['loadFile', 'saveFile', 'loadPointsFile', 'loadStream']
}

## Which stl containers we need for this code
stlcontainers = [
    ('set', 'uint'),
    ('vector', 'float64'),  # DoubleVec
    ('vector', 'int32'),  # IntVec
    ('vector', ('vector', 'int32')),  # IntVecVec
    ('vector', ('vector', 'float64')),   # DoubleVecVec
    ('vector', 'HKnotVector'),  # vector< HKnotVector >
    ('vector', ('Point', 3, 'double', False)),  # vector< Point3d >
    ('vector', ('Point', 3, 'double', True)),  # vector< APoint3d >
]

variables = [
    ('Activity', 'common'),  # Activity enum
    ('MeshType', 'HMesh')  # MeshType enum
]

## Which classes to create wrappers for.
classes = [
    ('HKnotVector', 'HKnotVector'),
    (('Point', 3, 'double', False), 'Point', 'Point', 'APoint3d'),
    (('Point', 3, 'double', True), 'Point', 'Point', 'Point3d'),
    ('HNurbs', 'HNurbs'),
    ('Index', 'common'),
    ('HNurbsTree', 'HNurbsTree'),
    ('HForest', 'HForest'),
]

## Which functions to create wrappers for
functions = [
    ('linearParameterizeNURBS', 'HNurbs')
]
