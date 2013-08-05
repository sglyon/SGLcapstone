cimport numpy as np
from libc.stdlib cimport free
from libcpp.vector cimport vector as cpp_vector
import numpy as np

np.import_array()


cdef class HKnotVector:
    def __cinit__(self, *args, **kwargs):
        self._inst = NULL
        self._free_inst = True

    def __dealloc__(self):
        if self._free_inst:
            free(self._inst)

    # constuctors
    def _constructor1(self):
        self._inst = new cpp_HKnotVector.HKnotVector()

    def _constructor2(self, degree, knots):
        cdef cpp_vector[double] cpp_knots
        cdef int i
        cdef int knots_size = len(knots)
        cpp_knots = cpp_vector[double](<size_t> knots_size)
        for i in range(knots_size):
            cpp_knots[i] = <double> knots[i]
        self._inst = new cpp_HKnotVector.HKnotVector(<unsigned int> long(degree), cpp_knots)

    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self._constructor2(*args, **kwargs)
        else:
            self._constructor1(*args, **kwargs)

    # methods
    def degree(self):
        cdef unsigned int rtnval
        rtnval = (<cpp_HKnotVector.HKnotVector *> self._inst).degree()
        return int(rtnval)


    def isEven(self):
        cdef bint rtnval
        rtnval = (<cpp_HKnotVector.HKnotVector *> self._inst).isEven()
        return bool(rtnval)


    def isOdd(self):
        cdef bint rtnval
        rtnval = (<cpp_HKnotVector.HKnotVector *> self._inst).isOdd()
        return bool(rtnval)
