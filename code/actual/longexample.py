from __future__ import print_function
from hsfpy import *
msg = "{0} is\n{1}\n"
f = open('longoutput.txt', 'w')


## Create HKnotVector objects
knots1 = [0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0]
knots2 = [0.0, 0.0, 0.0, 1./3, 2./3, 1.0, 1.0, 1.0]
hkv1 = HKnotVector(1, knots1)
hkv2 = HKnotVector(2, knots2)
print(msg.format('hkv1', repr(hkv1)), file=f)
print(msg.format('hkv2', repr(hkv2)), file=f)

## Create HNurbs
nurbs1 = HNurbs([hkv1, hkv2])

## Now create NURBS for the next level in the hierarchy
## The knot vectors are obtained by subdividing the nonzero segments in the previous set
knots1 = [0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0]
knots2 = [0.0, 0.0, 0.0, 1./6, 1./3, 1./2, 2./3, 5./6, 1.0, 1.0, 1.0]
hkv1 = HKnotVector(1, knots1)
hkv2 = HKnotVector(2, knots2)
print(msg.format('hkv1', repr(hkv1)), file=f)
print(msg.format('hkv2', repr(hkv2)), file=f)
nurbs2 = HNurbs([hkv1,hkv2])

# Note linearParameterizeNURBS makes nurbs2 = HNurbs([hkv2, hkv1])
linearParameterizeNURBS(2, 3, 2, 2, 2, 4, 4, 10., 2., 2., nurbs2)
print('HKnotVectors of nurbs2. First should be hkv2 and second hkv1\n', file=f)
print(msg.format('nurbs2.getKnots(0)', nurbs2.getKnots(0)), file=f)
print(msg.format('nurbs2.getKnots(1)', nurbs2.getKnots(1)), file=f)

## Create Trees
tree = HNurbsTree(0, nurbs1)
tree.addLevel(nurbs2)

## Create forest
forest = HForest(tree)

# get some data and verify integrity
direct = hkv2.getKnot(4)
nonstop1 = nurbs1.getKnot(1, 4)
nonstop2 = nurbs2.getKnot(0, 4)
layover = tree.getLevel(1).getKnots(0).getKnot(4)
longest = forest.getTree(0).getLevel(0).getKnots(1).getKnot(4)

print('Are the values of HKnotVector 2 preserved?', file=f)
print(str(direct == nonstop1 == nonstop2 == layover == longest), file=f)
f.close()
